#!/usr/bin/env python3
"""Verify that ToSpec's inline Light shortcut is no weaker than router §0."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


BOUNDARIES = {
    "confirmed_product_contract": {
        "skill": (r"confirmed product behavior", r"\bContract\b"),
        "router": (r"confirmed product/Contract",),
    },
    "schema_shared_persisted_data": {
        "skill": (r"\bschema\b", r"persisted/shared-data"),
        "router": (r"shared or persisted schema/data",),
    },
    "authorization_security_boundary": {
        "skill": (r"\bauthorization\b", r"security[- ]boundary"),
        "router": (r"authorization/security boundary",),
    },
    "global_cross_runtime_rule": {
        "skill": (r"\bglobal\b", r"cross-runtime rule"),
        "router": (r"global/cross-runtime rule",),
    },
    "production_ci_release_deployment_runtime": {
        "skill": (r"production/CI/release/deployment/runtime-configuration",),
        "router": (r"production/CI/release/deployment/runtime configuration",),
    },
    "irreversible": {
        "skill": (r"local reversibility",),
        "router": (r"\birreversible\b",),
    },
    "external_system": {
        "skill": (r"external-system change",),
        "router": (r"material external-system change",),
    },
}


def line_containing(text: str, marker: str, label: str) -> str:
    for line in text.splitlines():
        if marker in line:
            return line
    raise ValueError(f"{label}: missing marker {marker!r}")


def matched_boundaries(line: str, side: str) -> set[str]:
    return {
        name
        for name, patterns in BOUNDARIES.items()
        if all(re.search(pattern, line) for pattern in patterns[side])
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skill",
        default=str(Path(__file__).resolve().parents[1] / "SKILL.md"),
    )
    parser.add_argument("--router", required=True)
    parser.add_argument("--global-entry")
    args = parser.parse_args()

    skill_text = Path(args.skill).read_text(encoding="utf-8")
    router_text = Path(args.router).read_text(encoding="utf-8")
    skill_line = line_containing(skill_text, "A clearly Light task", "skill")
    router_line = line_containing(router_text, "| **Light** |", "router")

    skill_set = matched_boundaries(skill_line, "skill")
    router_set = matched_boundaries(router_line, "router")
    missing = sorted(router_set - skill_set)
    errors: list[str] = []

    if router_set != set(BOUNDARIES):
        errors.append("router normalization is incomplete; update validator aliases")
    if missing:
        errors.append("inline Light shortcut is weaker than router §0: " + ", ".join(missing))

    if args.global_entry:
        global_text = Path(args.global_entry).read_text(encoding="utf-8")
        global_line = line_containing(global_text, "若当前任务已加载", "global entry")
        required = ("不弱于 §0", "内联判 Light 必须蕴含 §0 判 Light", "非 Light")
        if "等价" in global_line:
            errors.append("global entry still claims exact equivalence")
        for marker in required:
            if marker not in global_line:
                errors.append(f"global entry missing invariant marker: {marker}")

    result = {
        "status": "pass" if not errors else "fail",
        "skill_boundaries": sorted(skill_set),
        "router_boundaries": sorted(router_set),
        "missing_from_skill": missing,
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
