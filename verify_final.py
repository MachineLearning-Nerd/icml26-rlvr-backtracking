#!/usr/bin/env python3
"""Verify the public documentation, branch namespace, and commit identity."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPOSITORY = "MachineLearning-Nerd/icml26-rlvr-backtracking"
CANONICAL = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"
OVERALL_STATUS = "ALL_FIVE_CLAIMS_VERIFIED_SCOPED_FINITE_AUDIT_NO_LIVE_SCORE"
REQUIRED_FILES = {
    "README.md",
    "STATUS.md",
    "CLAIM_EVIDENCE.md",
    "SOURCE_AUDIT.md",
    "docs/SOURCE_AUDIT.md",
    "ENVIRONMENT.md",
    "REPORT.md",
    "branch-audit.md",
    "repro/src/verify.py",
    "repro/src/publication_gate.py",
    "outputs/verdict.json",
    "outputs/publication_gate.json",
    "claims.json",
    "reproduction_verdicts.json",
    "AUTONOMOUS_STATE.json",
    "CITATION.cff",
    "AUTHOR_THANK_YOU.md",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
}


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def main() -> None:
    missing = sorted(path for path in REQUIRED_FILES if not (ROOT / path).exists())
    assert not missing, f"missing required files: {missing}"
    assert not git("status", "--porcelain"), "working tree is not clean"
    assert not git("for-each-ref", "--format=%(refname)", "refs/original"), "refs/original remains"

    remote = git("remote", "get-url", "origin").removesuffix(".git")
    assert remote.endswith(REPOSITORY), remote
    branch_lines = git("ls-remote", "--heads", "origin").splitlines()
    remote_branches = {
        line.split("\t", 1)[1].removeprefix("refs/heads/")
        for line in branch_lines
        if "\t" in line
    }
    assert remote_branches == {"main"}, remote_branches
    assert git("symbolic-ref", "--short", "refs/remotes/origin/HEAD") == "origin/main"

    identities = set(git("log", "--all", "--format=%an <%ae> | %cn <%ce>").splitlines())
    assert identities == {f"{CANONICAL} | {CANONICAL}"}, identities
    assert "Co-authored-by:" not in git("log", "--all", "--format=%B")

    claims = json.loads((ROOT / "claims.json").read_text())
    assert claims["overall_status"] == OVERALL_STATUS
    assert [claim["id"] for claim in claims["claims"]] == ["C1", "C2", "C3", "C4", "C5"]
    assert {claim["status"] for claim in claims["claims"]} == {"VERIFIED_SCOPED"}
    state = json.loads((ROOT / "AUTONOMOUS_STATE.json").read_text())
    assert state["overall_status"] == OVERALL_STATUS
    assert state["current_score_claim"] is False
    assert state["publication_allowed"] is False

    print(
        "FINAL_AUDIT=VERIFIED "
        f"branches={len(remote_branches)} commits={git('rev-list', '--all', '--count')} "
        "claims=C1:C5_verified_scoped historical_score=none "
        "current_score_claim=false publication_allowed=false"
    )


if __name__ == "__main__":
    main()
