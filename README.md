# Provable Benefits of RLVR over SFT for Reasoning Models

CPU-only, source-faithful reproduction for ICML 2026 paper `P3Mnh7mF5a`
(arXiv `2606.22938`). It exactly solves the paper's finite edge-state Markov
construction and verifies five anchored claims: golden-path SFT freezes
backtracking transitions, RLVR learns them, the inference-time separation,
duplicate-state search scaling, and RLVR-trace distillation.

```bash
uv venv --python 3.12
uv pip install numpy
OPENBLAS_NUM_THREADS=1 .venv/bin/python repro/src/verify.py
.venv/bin/python repro/src/publication_gate.py
```

See [`RESULTS.md`](RESULTS.md) for outcomes, [`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md)
for source anchors, and [`outputs/verdict.json`](outputs/verdict.json) for raw evidence.
