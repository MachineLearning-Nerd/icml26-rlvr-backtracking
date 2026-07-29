# Primary-source audit

Paper: **Provable Benefits of RLVR over SFT for Reasoning Models: Learning to
Backtrack Efficiently**, OpenReview `P3Mnh7mF5a`, arXiv
[`2606.22938`](https://arxiv.org/abs/2606.22938).

Pinned public TeX source SHA-256:
`2cb8102f2468aabd83a54b187cc7c87ba8f120946053e8c260d0c2d6a198f7b4`.
The source fully specifies the finite multigraph, bigram/trigram transition
categories, gradient-flow statements, hitting-time recurrences, and Figure-3
synthetic setup. No external data, model weights, API, or GPU is required.

| Claim | Source anchor | Reproduction route |
|---|---|---|
| C1 | Theorem 2 | Finite SFT transition update: forward probabilities converge while unobserved backward transitions stay pretrained. |
| C2 | Theorem 3 | Source policy-gradient/sign-flow transition categories with failed-rollout backtracking signal. |
| C3 | Theorem 4 | Exact absorbing-Markov hitting-time systems across W/K/L grids. |
| C4 | Corollary 1 | Duplicate-state-avoiding search recurrence versus learned backtracking. |
| C5 | Theorem 5 and Figure 3 | Distilled trace policy and the stated W=15/K=15/L=5 synthetic hitting-time target `4WK=900`. |

Finite runs exercise the source construction; the public proof carries the
universal asymptotic statements.
