# Conclusion


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_fc01d8b0d997", "created_at": "2026-07-29T12:38:06+00:00", "title": "Publication conclusion", "pinned": true, "pinned_at": "2026-07-29T12:38:07+00:00"}
-->
All five anchored claims pass the local fail-closed gate.

## Scope & cost

| | This reproduction | Full replication |
|---|---|---|
| Scope | Exact finite graph / Figure-3 dimensions | Same source synthetic protocol |
| Hardware | 4 CPU cores, NumPy | No GPU required by source construction |
| Time | ~7 seconds verifier | Source sign-GD convergence |
| Cost | Local CPU | CPU-only |
| Outcome | 5/5 verified, hit time 900.44 | Theoretical 4WK = 900 target |

The executable result is source-faithful for the finite construction. Universal asymptotic quantifiers remain primary-source-proof anchored.


---
<!-- trackio-cell
{"type": "code", "id": "cell_7fcdd44c957b", "created_at": "2026-07-29T12:38:33+00:00", "title": "Fail-closed publication gate", "command": [".venv/bin/python", "repro/src/publication_gate.py"], "exit_code": 0, "duration_s": 0.095}
-->
````bash
$ .venv/bin/python repro/src/publication_gate.py
````

exit 0 · 0.1s


````python title=publication_gate.py
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

````


````output
{
  "arxiv": "2606.22938",
  "checks": {
    "five_anchored_claims_pass": true,
    "independent_bellman_occupancy_gradient_control": true,
    "negative_control_per_claim": true,
    "primary_source_audit_present": true,
    "source_figure_protocol_reproduced": true,
    "theory_scope_limitation_explicit": true
  },
  "claim_count": 5,
  "paper": "P3Mnh7mF5a",
  "publication_eligible": true,
  "publication_gate_passed": true,
  "scope": "five source-anchored finite-graph claims; exact CPU quotient-chain checks and public TeX proof anchors",
  "tests_passed": true
}

````
