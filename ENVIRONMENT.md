# Environment and reproduction contract

## Commands

```bash
uv venv --python 3.12
uv pip install numpy
OPENBLAS_NUM_THREADS=1 .venv/bin/python repro/src/verify.py
.venv/bin/python repro/src/publication_gate.py
```

The run is CPU-only and uses no external data, model weights, GPU, quantum
hardware, or hosted job. `verify.py` writes `outputs/verdict.json`; the gate
fails closed unless all five claims carry source anchors, mechanisms, scopes,
and negative controls.

## Reproduction boundary

The source setting is `W=15`, `K=15`, `L=5`, sign-policy-gradient learning rate
`0.01`, and `1200` updates. The finite graph and all transitions are explicit
in the source and repository. A passing finite contract is recorded as scoped
evidence, not as a replacement for the paper's theorem proofs.
