# Claim-to-evidence ledger

The five claim contracts are implemented on `main` by `repro/src/verify.py`
and checked by the fail-closed publication gate. Each result includes a
source anchor, executable mechanism, explicit scope, and negative control.

| Claim | Verdict | How the claim is produced | Primary evidence |
| --- | --- | --- | --- |
| C1. Golden-path SFT does not learn backtracking | `VERIFIED_SCOPED` | Apply row-wise binary-softmax dynamics to the finite edge-state quotient; forward rows `a,c` move toward one while backward rows `b,d` remain at pretrained values. Golden-only paths are the negative control. | [`repro/src/verify.py`](repro/src/verify.py) → `sft_values`; [`outputs/verdict.json`](outputs/verdict.json) |
| C2. RLVR learns backtracking | `VERIFIED_SCOPED` | Solve Bellman hitting times and occupancies on `QuotientChain`, train all four transition families with sign policy-gradient updates, and compare an independent finite-difference gradient. At `W=15,K=15,L=5`, hitting time falls from `50142` to `900.4437`, every family exceeds `0.999969`, and gradient disagreement is `2.73e-8`. | [`repro/src/verify.py`](repro/src/verify.py) → `QuotientChain`; [`outputs/verdict.json`](outputs/verdict.json) |
| C3. Inference-time separation | `VERIFIED_SCOPED` | Evaluate the published SFT exit recurrence over `K={3,5,7}` and `L={2,3,5}`, then compare with the source RLVR optimum `4WK=900`. The two-depth ratios exceed four for every tested `L`. | [`repro/src/verify.py`](repro/src/verify.py) → `sft_exit_recurrence`, `source_optimal_hitting` |
| C4. Duplicate-state search scaling | `VERIFIED_SCOPED` | Compare SFT work `W*K*(L+1)` with RLVR work `4*W*K` across a finite increasing `W,K,L` grid. The no-duplicate control retains the exponential SFT exit recurrence. | [`repro/src/verify.py`](repro/src/verify.py) → `search_grid` |
| C5. RLVR-trace distillation transfers backtracking | `VERIFIED_SCOPED` | Check that teacher traces contain every desired forward/backward transition and that row-wise SFT inherits the support. The student transition minimum is `1-1e-12`, matching the `900` source target; golden-only traces are the negative control. | [`repro/src/verify.py`](repro/src/verify.py) → teacher/student transition-support check |

## Branch-to-evidence map

`main` is the only branch and is simultaneously the source, evidence, and
publication surface. [`branch-audit.md`](branch-audit.md) records the routing
for C1–C5 and confirms that no hidden `orx/*` or experiment-only branch exists.

## Score boundary

The publication gate is passed and the repository is queued for the shared
ICML 2026 reproduction process, but no live evaluator score is claimed.
