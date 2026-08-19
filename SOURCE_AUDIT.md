# Source audit

The detailed source record is [`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md).

## Pinned source

| Source | Identifier/hash | Role |
| --- | --- | --- |
| Paper | [arXiv:2606.22938](https://arxiv.org/abs/2606.22938) | Claim wording, finite graph, and theorem anchors |
| Paper HTML | [arxiv.org/html/2606.22938](https://arxiv.org/html/2606.22938) | Navigable source |
| OpenReview | [P3Mnh7mF5a](https://openreview.net/forum?id=P3Mnh7mF5a) | Submission record |
| Pinned TeX | `2cb8102f2468aabd83a54b187cc7c87ba8f120946053e8c260d0c2d6a198f7b4` | Source hash recorded by the audit |

The executable evidence uses the paper's finite multigraph, edge-state policy,
transition dynamics, hitting-time recurrences, and Figure-3 values. No
external data, model weights, API, GPU, or quantum hardware is needed.

## Scope boundary

Finite CPU checks validate the registered mechanisms and controls. They do not
replace the universal asymptotic proofs in Theorems 2–5 or Corollary 1.
