---
id: exists-symm-invariant-kernel
title: The move kernel is symmetric, invariant and nearly stochastic
kind: theorem
decl: GlobalTheory.HL.exists_symm_invariant_kernel
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.ExistsSymmInvariantKernelHermitianFrames
covers: 399
status: drafted
drafted_by: writer@claude
---
This theorem names the kernel that [`amp_le_mass`](/entry/amp-le-mass/) needs and collects five facts about it from other lemmas. Its statement form is [`exists_symm_invariant_kernel_hermitian_frames`](/entry/exists-symm-invariant-kernel-hermitian-frames/), where the statement is given in full. The proof only assembles; the work is in the five lemmas below.

## Statement

The same as [`exists_symm_invariant_kernel_hermitian_frames`](/entry/exists-symm-invariant-kernel-hermitian-frames/): for $k \ge 4r + 7$, $j < r$ and $P = \mathcal{F}(\beta, j + 1, \beta_J)$, there is a kernel $K$ that is $N_0$-invariant, finitely supported in each row, nonnegative and symmetric, with row sums within $\tfrac{24}{7} q^{2r+4-k}$ of $1$ and twisted row sums $\sum_y K(x, y)\,\omega(y)$ of size at most $\tfrac{24}{7} q^{2r+4-k}$.

## Proof

The kernel is $K(\Lambda, \Lambda_1) = \mathrm{kern}(\beta, j + 1, \beta_J, d, \Lambda, \Lambda_1)$. By definition,

$$\mathrm{kern}(\Lambda, \Lambda_1) = \frac{q^{a} \beta}{\beta_J}\, \mathrm{Re} \int \mathbf{1}\bigl[w \text{ moves } \Lambda \text{ to } \Lambda_1\bigr]\, dw .$$

Here $a$ is an integer of the frames record. The variable is $w = (x, x', u, t) \in V^3 \times E$, and the integral (`cint`) is a finite sum, normalized so that a group $A_\Lambda$ of such tuples has volume $1$. Put $s = h(u, u)/2 + t$. Then $w$ *moves* $\Lambda$ to $\Lambda_1$ (`MvTo`) if it meets the conditions `IsMove` at level $j + 1$ and $\Lambda_1 = \{v : E_w(v) \in \Lambda\}$, with

$$E_w(v) = v + h(v, u)\,x - h(v, x)\,(u + s x).$$

We have not unfolded `IsMove` beyond this shape.

Each clause comes from one lemma:

1. Invariance: `frameMovesKernel_commonStabilizer_smul_eq`. It holds for all levels and all $\Lambda_1$, not only those with $P$.
2. Finite support: `hermDoubleCosetMoves_finite_targets_split`, which says that $\{\Lambda_1 : K(\Lambda, \Lambda_1) \ne 0\}$ is finite.
3. Nonnegativity: the same lemma. Symmetry: `hermDoubleCosetMoveKernel_symm`.
4. Row sum: `hermitianDoubleCoset_kernel_row_sum_near_one`.
5. Twisted row sum: `hermitianDoubleCoset_kernel_bound_by_weight`.

Only items 4 and 5 use $k \ge 4r + 7$.

## In the Lean code

The theorem is in [ExistsSymmInvariantKernelHermitianFrames.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsSymmInvariantKernelHermitianFrames.lean#L17), and `kern` in [NoLeak.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/NoLeak.lean#L54). The proof first replaces $P$ by its definition (`subst`), then fills the five clauses. The five lemmas are statement forms of `kern_smul_eq`, `moves_split_by_target`, `kern_symm`, `kern_row_sum` and `kernel_weight`. The quantified "for all $P$ with $P \iff \dots$" form of the statement adds nothing: $P$ is determined by the other arguments.
