"""Read-only-source Blender node asset scout and opt-in private export.

Run:
  blender -b "<SOURCE.blend>" --python tools/blender_asset_scout.py -- --list
  blender -b "<SOURCE.blend>" --python tools/blender_asset_scout.py -- --group "<EXACT GROUP>" --id DF-LIFETIME-001
  blender -b "<SOURCE.blend>" --python tools/blender_asset_scout.py -- --group "<EXACT GROUP>" --id DF-LIFETIME-001 --out "<PRIVATE_OUTPUT.blend>" --export --rights-reviewed --accept-indirect-dependencies

No source-file save calls, no implicit overwrite, no automatic public upload.
CAUTION: bpy.data.libraries.write includes indirectly referenced ID blocks; this
is only a starting point. Human inspection of the exported .blend is required.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

try:
    import bpy
except ImportError as exc:
    raise SystemExit("Run inside Blender via --python; bpy is required") from exc


def cli_args():
    arg_list = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true", help="Read-only node group inventory")
    parser.add_argument("--group", help="Exact Blender node group name")
    parser.add_argument("--id", default="UNREGISTERED", help="Public-safe component ID")
    parser.add_argument("--out", help="Local private destination .blend")
    parser.add_argument("--export", action="store_true", help="Explicitly opt in to export")
    parser.add_argument("--rights-reviewed", action="store_true", help="User reviewed permissions")
    parser.add_argument(
        "--accept-indirect-dependencies",
        action="store_true",
        help="User understands all indirect ID dependencies may be bundled",
    )
    return parser.parse_args(arg_list)


def group_summary(tree):
    nested = []
    direct_ids = []
    for node in tree.nodes:
        child = getattr(node, "node_tree", None)
        if child is not None:
            nested.append(child.name)
        for field in ("object", "collection", "material", "image", "texture", "scene"):
            item = getattr(node, field, None)
            if item is not None and isinstance(item, bpy.types.ID):
                direct_ids.append({"kind": item.bl_rna.identifier, "name": item.name})
    sockets = []
    interface = getattr(tree, "interface", None)
    if interface:
        for item in interface.items_tree:
            if getattr(item, "item_type", None) == "SOCKET":
                sockets.append({
                    "name": item.name,
                    "direction": getattr(item, "in_out", "?"),
                    "socket_type": getattr(item, "socket_type", "?"),
                })
    has_sim = any("Simulation" in getattr(n, "bl_idname", "") for n in tree.nodes)
    return {
        "name": tree.name,
        "type": tree.bl_idname,
        "nodes": len(tree.nodes),
        "links": len(tree.links),
        "contains_simulation_node": has_sim,
        "nested_groups": nested,
        "direct_referenced_ids": direct_ids,
        "interface": sockets,
        "linked_external_library": bool(tree.library),
    }


def output(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main():
    args = cli_args()
    original = pathlib.Path(bpy.data.filepath) if bpy.data.filepath else None
    if args.list:
        output({
            "source_loaded": bool(original),
            "groups": [group_summary(g) for g in bpy.data.node_groups],
        })
        return
    if not args.group:
        raise SystemExit("Specify --group or --list")
    group = bpy.data.node_groups.get(args.group)
    if group is None or group.name != args.group:
        raise SystemExit("Exact node group name not found; use --list")
    if group.library:
        raise SystemExit("Linked group: resolve locally and review before exporting")
    info = {
        "component_id": args.id,
        "source_loaded": bool(original),
        "source_blender_version": bpy.app.version_string,
        "group": group_summary(group),
        "export_requested": bool(args.export),
        "warning": "Indirectly referenced datablocks may be included; never publish unreviewed exports.",
    }
    if not args.export:
        info["status"] = "INSPECT_ONLY_NO_FILE_WRITTEN"
        output(info)
        return
    if not (args.rights_reviewed and args.accept_indirect_dependencies):
        raise SystemExit("Export needs --rights-reviewed AND --accept-indirect-dependencies")
    if not original or not original.is_file():
        raise SystemExit("Must start Blender with a saved source .blend")
    if not args.out:
        raise SystemExit("Provide --out under a local private folder")
    dest = pathlib.Path(args.out).expanduser().resolve()
    if dest.suffix.lower() != ".blend" or dest.exists():
        raise SystemExit("Destination must be a new .blend (no overwriting)")
    if dest == original.resolve():
        raise SystemExit("Source overwrite forbidden")
    if not dest.parent.is_dir():
        raise SystemExit("Destination directory must exist; create it privately first")
    # Asset metadata changes only the in-memory copy loaded in this process.
    # Never call bpy.ops.wm.save_as_mainfile() or bpy.ops.wm.save_mainfile().
    group.asset_mark()
    group.asset_data.description = "Artworks component: " + args.id
    bpy.data.libraries.write(
        str(dest),
        {group},
        path_remap="NONE",
        fake_user=True,
        compress=True,
    )
    info.update({
        "status": "LOCAL_PACKAGE_WRITTEN_UNVERIFIED",
        "destination": str(dest),
        "bytes": dest.stat().st_size,
        "next_required": [
            "Inspect contents and indirect assets for rights/privacy",
            "Open package in a clean Blender file and use the group",
            "Run source-tick or matching render parity test",
            "Document author choice before raising catalog status",
        ],
    })
    output(info)


if __name__ == "__main__":
    main()
