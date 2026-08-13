# Primary-source audit

Paper: **Provable Benefits of RLVR over SFT for Reasoning Models: Learning to
Backtrack Efficiently**, by Stanley Wei and Juno Kim. See the
[arXiv record](https://arxiv.org/abs/2606.22938) and
[HTML source](https://arxiv.org/html/2606.22938).

OpenReview identifier: `P3Mnh7mF5a`.

Pinned public TeX source SHA-256:
`2cb8102f2468aabd83a54b187cc7c87ba8f120946053e8c260d0c2d6a198f7b4`.

The source specifies the finite multigraph, edge-state policy, gradient-flow
claims, hitting-time recurrences, and Figure-3 protocol. No external data,
model weights, API, GPU, or quantum hardware is required.

| Claim | Source anchor | Reproduction route | Scope of the executable evidence |
|---|---|---|---|
| C1 | Theorem 2 | Finite SFT row dynamics in `sft_values` | Forward probabilities converge while unobserved backward rows retain pretrained values; universal convergence remains source-proof anchored. |
| C2 | Theorem 3 and RLVR appendix | Quotient-chain Bellman/occupancy solve, sign policy-gradient updates, and finite-difference check | Full `W=15,K=15,L=5` construction at source learning rate `0.01`; the theorem proof remains primary-source evidence. |
| C3 | Theorem 4 | Published SFT exit recurrence over `W/K/L` grids versus RLVR source optimum `4WK` | Finite recurrence witnesses the separation; it does not replace the asymptotic proof. |
| C4 | Corollary 1 | Explicit duplicate-state search-work accounting | Checks the stated `WKL` versus `WK` scaling on a finite grid. |
| C5 | Theorem 5 and Figure 3 | Teacher/student transition-support check at the source Figure-3 target | Finite trace support and `4WK=900` target; universal distillation proof remains source anchored. |

The repository’s fail-closed publication gate requires each claim to carry a
source anchor, mechanism, scope, and negative control before it is reported as
passed.
