# Status — P3Mnh7mF5a

**State: public and queued; no live evaluator score claimed.**

## Standard audit record

`ALL_FIVE_CLAIMS_VERIFIED_SCOPED_FINITE_AUDIT_NO_LIVE_SCORE`

| Gate | Value |
| --- | --- |
| Publication gate | `passed` |
| Current score claim | `false` |
| Publication authorization | `false` |
| Official author endorsement | `false` |
| Evidence level | Finite, source-faithful CPU audit |

The five claims pass their explicit finite contracts and controls. The
repository does not turn those checks into replacement proofs of the paper's
universal asymptotic statements.

- Paper: [arXiv:2606.22938](https://arxiv.org/abs/2606.22938)
- Authors: Stanley Wei and Juno Kim
- Five anchored claims / ten possible points
- Pinned TeX SHA-256: `2cb8102f2468aabd83a54b187cc7c87ba8f120946053e8c260d0c2d6a198f7b4`
- Local result: C1–C5 pass with explicit finite scopes and negative controls
- Protocol: `W=15`, `K=15`, `L=5`, sign-GD learning rate `0.01`
- Publication gate: passed
- Branches: `main` only; see [`branch-audit.md`](branch-audit.md)

The finite graph, transitions, hitting-time recurrences, and synthetic setting
are fully specified in the public source. The universal asymptotic statements
remain anchored to the paper’s proofs rather than being claimed as consequences
of the finite CPU run alone.
