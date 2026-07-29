# Results

Run the complete CPU reproduction from this directory:

```bash
OPENBLAS_NUM_THREADS=1 .venv/bin/python repro/src/verify.py
.venv/bin/python repro/src/publication_gate.py
```

All five anchored claims pass. Structured raw evidence is in [`outputs/verdict.json`](outputs/verdict.json).

| Claim | Executable evidence | Negative control |
|---|---|---|
| C1 — golden-path SFT | Exact row-wise dynamics makes `a,c→1`, while `b,d` retain pretraining values | Backward rows never occur in golden paths |
| C2 — RLVR learns backtracking | Exact `W=15,K=15,L=5`, 0.01 sign-GD quotient solver: `50142→900.44`; every family exceeds `0.99996` | Central finite-difference gradients agree with occupancy/advantage derivatives (`2.8e-8`) |
| C3 — inference separation | Published SFT exit recurrence over `K∈{3,5,7}`, `L∈{2,3,5}`; RLVR source optimum is `4WK=900` | SFT recurrence grows geometrically while RLVR remains linear |
| C4 — duplicate-state search | Corollary work accounting grows as `Θ(WKL)` for SFT versus `Θ(WK)` for RLVR | Without duplicate prevention SFT retains the exponential exit recurrence |
| C5 — RLVR-trace distillation | Teacher traces support each desired forward/backward transition, so row-wise SFT inherits `Θ(WK)` | Golden-only traces omit backward transitions |

## Scope

This is a source-faithful theory/synthetic reproduction. The executable code solves the finite Markov construction and reproduces the Figure-3 setting, but finite grids are not presented as a new proof of universal `Θ` statements; those remain anchored to the primary-source proofs in the source audit.
