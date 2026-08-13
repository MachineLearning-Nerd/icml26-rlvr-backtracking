# Results

The source-faithful CPU reproduction passes all five anchored claims. This is
finite evidence for the paper’s construction, not a replacement for its
universal theorem proofs.

| Claim | Executable evidence | Negative control | Result |
|---|---|---|---|
| C1 — golden-path SFT | Forward rows `a,c` converge to one; backward rows `b,d` retain pretrained values. | Golden paths never contain the backward rows. | PASS |
| C2 — RLVR learns backtracking | At `W=15,K=15,L=5`, sign-GD reduces hitting time `50142→900.4437`; minimum transition probability is `0.999969`. | Independent central finite differences agree with the occupancy/advantage derivative to `2.73e-8`. | PASS |
| C3 — inference separation | Published SFT exit recurrence grows geometrically over the tested `K/L` grid; RLVR source optimum is `4WK=900`. | SFT recurrence grows while RLVR remains linear in `WK`. | PASS |
| C4 — duplicate-state search | Work accounting compares `W*K*(L+1)` for SFT with `4*W*K` for RLVR. | Without duplicate prevention, the SFT exit recurrence remains exponential. | PASS |
| C5 — trace distillation | Teacher traces contain all desired forward/backward transitions; student inherits them. | Golden-only traces omit backward-transition support. | PASS |

Structured raw evidence is in [`outputs/verdict.json`](outputs/verdict.json),
and the fail-closed result is in
[`outputs/publication_gate.json`](outputs/publication_gate.json).

No live evaluator score is recorded in this repository yet; the publication
status remains public and queued.
