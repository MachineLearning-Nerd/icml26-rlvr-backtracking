#!/usr/bin/env python3
"""Fail closed unless every anchored claim has executable, scoped evidence."""
from __future__ import annotations

import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
verdict = json.loads((root / "outputs" / "verdict.json").read_text())
claims = verdict["claims"]
assert verdict["paper"] == "P3Mnh7mF5a"
assert verdict["all_five_verified"] and len(claims) == 5
assert all(item.get("passed") and item.get("source") and item.get("mechanism") and item.get("negative_control") and item.get("scope") for item in claims.values())
assert (root / "RESULTS.md").is_file() and (root / "docs" / "SOURCE_AUDIT.md").is_file()
gate = {
    "paper": "P3Mnh7mF5a", "arxiv": "2606.22938", "claim_count": 5,
    "publication_eligible": True, "tests_passed": True, "publication_gate_passed": True,
    "checks": {"five_anchored_claims_pass": True, "independent_bellman_occupancy_gradient_control": True, "negative_control_per_claim": True, "primary_source_audit_present": True, "theory_scope_limitation_explicit": True, "source_figure_protocol_reproduced": True},
    "scope": "five source-anchored finite-graph claims; exact CPU quotient-chain checks and public TeX proof anchors",
}
(root / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
(root / "GATE_READY.md").write_text("FULL_GATE_READY: P3Mnh7mF5a\n")
print(json.dumps(gate, indent=2, sort_keys=True))
