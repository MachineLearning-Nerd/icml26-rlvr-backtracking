# Claim 1 — Golden-path SFT


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_5ac22b8f5e00", "created_at": "2026-07-29T12:37:52+00:00", "title": "Evidence"}
-->
Theorem 2 is checked with exact row-wise cross-entropy dynamics. Golden paths update a and c to one while backward rows b and d remain exactly at pretrained values.

Negative control: removing all backward transitions from the training support freezes those rows, as predicted.
