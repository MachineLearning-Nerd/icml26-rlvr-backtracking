# Provable Benefits of RLVR over SFT for Reasoning Models

Independent CPU reproduction for [arXiv:2606.22938](https://arxiv.org/abs/2606.22938),
“Provable Benefits of RLVR over SFT for Reasoning Models: Learning to
Backtrack Efficiently,” by Stanley Wei and Juno Kim.

## Result at a glance

The repository’s publication gate passes all **five anchored claims** in a
finite, source-faithful construction. The evidence is eligible for the shared
ICML 2026 reproduction queue; the current status is **public and queued**, and
no live evaluator score is claimed here yet.

The reproduction is deliberately scoped. It exactly solves the paper’s
finite edge-state Markov quotient, checks the published recurrences and
transition dynamics, and reproduces the Figure-3 setting. It does not replace
the paper’s universal theorem proofs with finite numerical checks, and it does
not train a language model or use external data, model weights, a GPU, or
quantum hardware.

Start with [`RESULTS.md`](RESULTS.md), the [source audit](docs/SOURCE_AUDIT.md),
the [machine-readable verdict](outputs/verdict.json), and the
[publication gate](outputs/publication_gate.json).

## Paper and problem

The paper models chain-of-thought reasoning as pathfinding on a multigraph
with a source, a fork, `W` branches, `K` diamonds per branch, and `L`
parallel edges per diamond. It compares supervised fine-tuning (SFT) on
golden shortest paths with reinforcement learning with verifiable rewards
(RLVR), focusing on whether training exposes efficient backtracking.

The reproduced protocol uses the paper’s Figure-3 values
`W=15`, `K=15`, `L=5`, sign-policy-gradient learning rate `0.01`, and `1200`
updates.

## Claim-to-evidence ledger

| Claim | Paper anchor | How the result is produced | Result |
|---|---|---|---|
| C1 — golden-path SFT does not learn backtracking | Theorem 2 | [`sft_values`](repro/src/verify.py) applies the row-wise binary-softmax dynamics: forward rows `a,c` converge toward one while backward rows `b,d` remain at their pretrained values. The negative control checks that golden paths never update those backward rows. | PASS — finite transition families |
| C2 — RLVR learns backtracking | Theorem 3 and Appendix RLVR dynamics | [`QuotientChain`](repro/src/verify.py) independently solves Bellman hitting times and occupancies; sign policy-gradient updates train all four transition families. At the source setting, hitting time falls from `50142` to `900.4437`, every family exceeds `0.999969`, and an independent finite-difference gradient agrees to `2.73e-8`. | PASS — finite Figure-3 construction |
| C3 — inference-time separation | Theorem 4 | [`sft_exit_recurrence`](repro/src/verify.py) evaluates the published SFT recurrence over `K={3,5,7}` and `L={2,3,5}`, while RLVR uses the source optimum `4WK=900`. The two-depth ratios are greater than four for every tested `L`. | PASS — recurrence witnesses |
| C4 — duplicate-state search scaling | Corollary 1 | [`search_grid`](repro/src/verify.py) compares SFT work `W*K*(L+1)` with RLVR work `4*W*K` across increasing `W,K,L`; the ratio grows on the checked grid. The no-duplicate control keeps the exponential SFT exit recurrence. | PASS — finite scaling grid |
| C5 — RLVR-trace distillation transfers backtracking | Theorem 5 and Figure 3 | The verifier checks that teacher traces contain every desired forward/backward transition and that row-wise SFT inherits them; the student transition minimum is `1-1e-12`, matching the source target `900`. Golden-only traces are the negative control. | PASS — finite trace support |

The complete source anchors, scopes, and limitations are in
[`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md). The verifier writes each
claim’s mechanism, negative control, and scope into
[`outputs/verdict.json`](outputs/verdict.json); the independent publication
gate checks that every claim has all three before it passes.

## Reproduce the checks

The repository uses Python 3.12 and NumPy. A clean CPU setup is:

```bash
uv venv --python 3.12
uv pip install numpy
OPENBLAS_NUM_THREADS=1 .venv/bin/python repro/src/verify.py
.venv/bin/python repro/src/publication_gate.py
```

`verify.py` regenerates `outputs/verdict.json`; `publication_gate.py` fails
closed unless all five claims, controls, source anchors, and scope fields are
present.

## Branch organization

This repository currently has one branch: `main`. It is the canonical source,
evidence, and publication surface. There are no `orx/*` or experiment-only
branches to reconcile. The branch-level contract and claim routing are
recorded in [`branch-audit.md`](branch-audit.md).

## Citation

```bibtex
@misc{wei2026provable,
  title         = {Provable Benefits of RLVR over SFT for Reasoning Models: Learning to Backtrack Efficiently},
  author        = {Stanley Wei and Juno Kim},
  year          = {2026},
  eprint        = {2606.22938},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  doi           = {10.48550/arXiv.2606.22938}
}
```

## Thank you

Thank you to Stanley Wei and Juno Kim for making this theoretical construction
and its source available for independent reproduction. The paper’s compact
finite graph makes the distinction between golden-path supervision, on-policy
RLVR exploration, and trace distillation unusually transparent to audit. This
repository is an independent reproduction and does not imply endorsement by
the authors.

## Attribution and license

Repository maintenance and reproduction commits are attributed to
**MachineLearning-Nerd**. The paper is available under the license shown in
its [arXiv record](https://arxiv.org/abs/2606.22938); the paper and source
remain the property of their authors.
