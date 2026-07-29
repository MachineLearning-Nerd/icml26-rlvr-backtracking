# Repro - Provable Benefits of RLVR over SFT for Reasoning Models

## Pages

| Page |
| --- |
| [Claim 1 — Golden-path SFT](#/claim-1-golden-path-sft) |
| [Claim 2 — RLVR backtracking](#/claim-2-rlvr-backtracking) |
| [Claim 3 — Inference separation](#/claim-3-inference-separation) |
| [Claim 4 — Search agent](#/claim-4-search-agent) |
| [Claim 5 — Trace distillation](#/claim-5-trace-distillation) |
| [Methods](#/methods) |
| [Negative controls](#/negative-controls) |
| [Conclusion](#/conclusion) |


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_e718ac42bf14", "created_at": "2026-07-29T12:37:50+00:00", "title": "Executive summary"}
-->
Five anchored claims passed on the exact finite multigraph from arXiv:2606.22938.

The full W=15, K=15, L=5 source protocol at sign-GD lr=0.01 moves exact expected hitting time from 50,142 to 900.44, matching the paper's 4WK=900 target up to finite convergence error.

CPU-only; no Hugging Face GPU used.
