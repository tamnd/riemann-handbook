---
id: amp-le-mass
title: Cancellation in one family of second-type terms
kind: theorem
decl: GlobalTheory.HL.AmpCancel.amp_le_mass
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.AmplitudeLeMassSecondTypeFamily
covers: 407
status: drafted
drafted_by: writer@claude
---
This theorem bounds the oscillating sum $a(d, P)$ over one family of second-type terms by $7 q^{2r+4-k}$ times the mass $m(d, P)$ of the same terms. Its statement form is [`amplitude_le_mass_secondType_family`](/entry/amplitude-le-mass-second-type-family/), which [`family_bound`](/entry/family-bound/) uses for each datum. The cancellation comes from the kernel of [`exists_symm_invariant_kernel_hermitian_frames`](/entry/exists-symm-invariant-kernel-hermitian-frames/).

## Statement

We use the notation of [the entry for `ampSq_nonzero_defect`](/entry/amp-sq-nonzero-defect/): the frames record $S$ of type `Frames L r k`, with a nondegenerate [[Hermitian form|48P4A1CX85]] on $V = E^{k+2r+1}$ over a quadratic algebra $E$ of a local field $F$ with $q$ residue elements; the unipotent groups $N, N'$ and $N_0 = N \cap N'$; the terms $\Lambda$ of a datum $d$, with mass $\mu(\Lambda)$ and phase $\omega(d, \Lambda)$ of absolute value $1$; and the sums over $N_0$-orbits

$$a(d, P) = \sum_{[\Lambda]} \mu(\Lambda)\,\omega(d, \Lambda), \qquad m(d, P) = \sum_{[\Lambda]} \mu(\Lambda).$$

Let $\mathcal{F}(\beta, J, \beta_J)$ be the second-type terms (`TypeBe`) with defect index $\beta$, largest level $J$ and $\beta_J$ cosets at level $J$ (`InFF`), as in [the entry for its mean square](/entry/hermitian-double-coset-second-type-family-amp-sq-le/). We have not unfolded the level function `lev`.

**Theorem.** If $k \ge 4r + 7$, then for all $\beta, J, \beta_J$ and $d$, with $P = \mathcal{F}(\beta, J, \beta_J)$,

$$\lvert a(d, P) \rvert \le 7\, q^{\,2r + 4 - k}\, m(d, P).$$

## Proof

By `hermitianDoubleCoset_mass_le_and_finite`, there are finitely many orbits of terms.

**Case $1 \le J \le r$.** [`exists_symm_invariant_kernel_hermitian_frames`](/entry/exists-symm-invariant-kernel-hermitian-frames/) at $j = J - 1$ gives a symmetric $N_0$-invariant kernel $K \ge 0$ on the terms in $P$ with $\lvert \sum_y K(x, y) - 1 \rvert \le e$ and $\lvert \sum_y K(x, y)\,\omega(y) \rvert \le e$, where $e = \tfrac{24}{7} q^{2r+4-k}$. The abstract lemma `norm_orbit_sum_le_of_symm_kernel` gives $\lvert a \rvert \le 2e\, m$. Its proof writes

$$\sum_x \mu(x)\omega(x) = \sum_x \mu(x) \sum_y K(x, y)\,\omega(y) - \sum_x \mu(x)\,\omega(x)\Bigl(\sum_y K(x, y) - 1\Bigr),$$

which needs an exchange of $x$ and $y$ in the double sum. The exchange uses the symmetry and invariance of $K$ and an identity between $\mu$ and indices of stabilizers. As $\lvert \omega \rvert = 1$, each sum is at most $e \sum_x \mu(x)$. Last, $2e = \tfrac{48}{7} q^{2r+4-k} \le 7 q^{2r+4-k}$.

The other inputs are: $N_0$ keeps $P$ and $\omega$ (`hermitianFrames_stabilizer_acts_on_terms`), $\mu$ is constant on orbits with finite indices (`commonStabilizer_stabilizers_commensurable_volume`), and $\lvert \omega \rvert = 1$ (`witness_independence`).

**Case $J = 0$ or $J > r$.** No term satisfies $P$, so $a(d, P) = 0$. For $J > r$, the type bounds all levels by $r$. For $J = 0$, all levels are $0$, and `term_exponents_nonneg_and_defect_group_bound` shows that the lattice $M(d, \Lambda)$ built from the frames of $\Lambda$ is all of $\Lambda \cap (\langle f \rangle + \langle f' \rangle)$. The type excludes this.

## In the Lean code

The theorem is in [AmplitudeLeMassSecondTypeFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplitudeLeMassSecondTypeFamily.lean#L31), the definitions in [ComplementReferenceCompactSubgroup.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/ComplementReferenceCompactSubgroup.lean#L14), and the abstract lemma in [NormOrbitSumLeOfSymmKernel.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/NormOrbitSumLeOfSymmKernel.lean#L83). The bound is in $[0, \infty]$. The constant $7$ is not sharp: the proof gives $48/7$. Only the kernel uses $k \ge 4r + 7$.
