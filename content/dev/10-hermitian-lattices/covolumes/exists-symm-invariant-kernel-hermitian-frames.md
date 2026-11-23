---
id: exists-symm-invariant-kernel-hermitian-frames
title: A symmetric invariant kernel on the terms of one type, statement form
kind: theorem
decl: GlobalTheory.T.exists_symm_invariant_kernel_hermitian_frames
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.ExistsSymmInvariantKernelHermitianFramesStatement
covers: 400
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`exists_symm_invariant_kernel`](/entry/exists-symm-invariant-kernel/). Its only user is [`amp_le_mass`](/entry/amp-le-mass/), which applies it at $j = J - 1$. The content is in [`exists_symm_invariant_kernel`](/entry/exists-symm-invariant-kernel/).

## Statement

The notation ($q$, the frames record $S$, the group $N_0 = N \cap N'$, terms, the phase $\omega$ and the family $\mathcal{F}$) is as in [the entry for `amp_le_mass`](/entry/amp-le-mass/).

**Theorem.** Let $k \ge 4r + 7$, $j \in \{0, \dots, r - 1\}$, $\beta, \beta_J \in \mathbb{N}$ and a datum $d$. Let $P = \mathcal{F}(\beta, j + 1, \beta_J)$, the terms $\Lambda$ of $d$ with `InFF` at these values. Then there is a function $K$ on pairs of lattices with real values such that, for all $x, y$ in $P$ and all $g \in N_0$:

1. $K(gx, gy) = K(x, y)$;
2. only finitely many $y$ with $P$ have $K(x, y) \ne 0$;
3. $K(x, y) \ge 0$ and $K(x, y) = K(y, x)$;
4. $\bigl\lvert \sum_{y} K(x, y) - 1 \bigr\rvert \le \tfrac{24}{7} q^{2r+4-k}$;
5. $\bigl\lvert \sum_{y} K(x, y)\,\omega(y) \bigr\rvert \le \tfrac{24}{7} q^{2r+4-k}$.

The sums run over the $y$ in $P$.

## Proof

The proof is the term `GlobalTheory.HL.exists_symm_invariant_kernel`. There is nothing else.

## In the Lean code

The theorem is at [ExistsSymmInvariantKernelHermitianFramesStatement.lean line 9](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsSymmInvariantKernelHermitianFramesStatement.lean#L9). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The two statements are the same, so the first alternative fits.
