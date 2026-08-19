# Audit report

This repository is an independent CPU reproduction of **Provable Benefits of
RLVR over SFT for Reasoning Models: Learning to Backtrack Efficiently**.

All five registered claims pass their finite source-faithful contracts and
negative controls. The verifier exactly solves the finite edge-state Markov
quotient, checks the published recurrences and transition dynamics, and
reproduces the Figure-3 setting. It does not train a language model, use
external data or weights, or replace the paper's universal asymptotic proofs.

The detailed claim ledger is in [`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md), the
source boundary is in [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md), and branch routing
is in [`branch-audit.md`](branch-audit.md). The publication gate passed, but no
live evaluator score is claimed.
