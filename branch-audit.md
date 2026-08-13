# Branch audit

This repository currently has one branch, `main`, which is both the canonical
publication surface and the complete evidence surface.

| Branch | Purpose | Claim/evidence routes |
|---|---|---|
| `main` | Source-faithful CPU reproduction, results, source audit, and publication gate | C1–C5 are implemented in [`repro/src/verify.py`](repro/src/verify.py), summarized in [`outputs/verdict.json`](outputs/verdict.json), and checked by [`repro/src/publication_gate.py`](repro/src/publication_gate.py). |

There are no `orx/*`, hidden experiment, release-candidate, or stale
branch-specific code paths in the current repository. If future experiments
are added, they should retain `main` as the reader-facing contract and state
whether they extend the finite evidence or merely explore a new setting.

## Claim routing on `main`

| Claim | Primary implementation | Independent control |
|---|---|---|
| C1 | `sft_values` and `QuotientChain` in `repro/src/verify.py` | Golden-only paths leave backward rows frozen. |
| C2 | `train_rlvr`, Bellman solve, and occupancy gradient in `repro/src/verify.py` | Central finite differences agree with the analytic policy-gradient derivative. |
| C3 | `sft_exit_recurrence` and `source_optimal_hitting` | SFT recurrence grows while RLVR remains at `4WK`. |
| C4 | `search_grid` work accounting | Removing duplicate-state avoidance leaves the exponential SFT recurrence. |
| C5 | Teacher/student transition-support check | Golden-only traces omit the backward transition support. |

The branch history does not constitute a second verdict system. The final
status is the five-claim machine-readable verdict plus the fail-closed
publication gate on `main`.
