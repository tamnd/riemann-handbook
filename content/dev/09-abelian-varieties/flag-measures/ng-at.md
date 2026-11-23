---
id: ng-at
title: The local non-generic bound for a pair of Hermitian frames
kind: theorem
decl: GlobalTheory.HL.AbstractBound.ngAt
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.HermitianDoubleCosetAmplitudeBoundLocal
covers: 452
status: drafted
drafted_by: writer@claude
---
This theorem proves the local bound `NGAt` for a pair of Hermitian frames over a $p$-adic field, by moving to coordinates (`Frames`). The main estimate is [`ampSq_nonzero_defect`](/entry/amp-sq-nonzero-defect/). Its statement form [`hermitianDoubleCoset_amplitude_bound_local`](/entry/hermitian-double-coset-amplitude-bound-local/) feeds [`local_nongeneric_bound_record_family`](/entry/local-nongeneric-bound-record-family/).

## Statement

Let $F$ be a nonarchimedean local field of characteristic $0$ with residue field of size $q$, and $E$ a reduced rank-$2$ $F$-algebra with conjugation $x \mapsto \bar x$ and integers $\mathcal{O}$. A local model $M$ adds a Haar measure and an optional splitting; $\theta_M$ is $1$ if $M$ is not split, else a uniformizer $\varpi$.

Let $H$ be a nondegenerate Hermitian $E$-space of dimension $k + 2r + 1$. A frame is $f_0, \dots, f_r$ with $h(f_a, f_b) = 0$ except $h(f_r, f_r) = -T$, plus isotropic dual vectors $e_0^*, \dots, e_{r-1}^*$, a unipotent subgroup $N$ of the [[unitary group|0R9R0Y1HDK]] and a character $\psi_\theta$ of $N$. For a frame pair $P = (A, B)$, let $D_l$ be the leading $l \times l$ minor of $(h(f^B_b, f^A_a))_{a,b}$ and $G_P = D_{r+1} \bar D_{r+1} - T_A T_B D_r \bar D_r$. `RelG θ` asks: the spans of the frames meet in $0$; $D_{r+1}$ is a unit and each $D_l$ is $0$ or a unit; $G_P \neq 0$; $\psi^A_\theta = \psi^B_\theta$ on $N_A \cap N_B$; and conditions on $T_A, T_B$. The height is $H_P = \bigl(|\theta_M| \, |\det \mathrm{Gram}| \prod_l |D_l \bar D_l|\bigr)^{-1/2}$, over the $l \geq 1$ with $D_l$ a unit.

A term $t$ is a lattice with frames, attached to a datum $d$, with mass $\mu(t)$ and phase $\omega(t) = \psi^A(t) \psi^B(t)^{-1}$. For a set $S$ of terms, $a(d, S) = \sum_{t \in S} \mu(t) \omega(t)$ over representatives modulo $N_A \cap N_B$. With weights $w(d_0, d)$, let
$$\Sigma(S) = \sum_d w(d_0, d) \, |a(d, S)|^2, \qquad n = \sum_d w(d_0, d) \sum_t \mu(t).$$
$\mathrm{BB}$ is the set of terms whose lattice meets the $E$-span of the frame vectors of $t$ outside their $\mathcal{O}$-span.

**Theorem.** If $C \geq 39$, $4r + 7 \leq k$, `M.OK` and `RelG` $\theta_M$ hold, then for all representatives and $d_0$:

1. $\Sigma(\mathrm{BB}) \leq H_P^{C(r+1)^2} q^{-(k - 2r - 5)} \, n$;
2. $\Sigma(\text{not } \mathrm{BB})$ and $\Sigma(\text{all})$ are at most $H_P^{C(r+1)^2} n$;
3. if $M$ is not split and $G_P$ and the $D_l$ are units (`PrimeTo`), then $H_P = 1$ and $\Sigma(\text{not } \mathrm{BB}) = \Sigma(\text{all}) = n$.

## Proof

1. **Coordinates.** `exists_coord` gives a `Frames` datum $S$ and an isometry $H \cong E^{k+2r+1}$ carrying $P$ to $S$.
2. **Comparison.** `hermitianLocalSums_eq_const_mul_coordinateSums` gives one $\kappa \geq 0$ such that the three sums $\Sigma$ and $n$ are $\kappa$ times their analogues for $S$, where $\mathrm{BB}$ becomes "nonzero defect". `framePairCoordinates_localHeight_eq_residueCard` gives $H_P = H_S$ and $q = q_S$.
3. **Bounds in coordinates.** [`ampSq_nonzero_defect`](/entry/amp-sq-nonzero-defect/) and `ampSq_le_height_mul_mass` give items 1 and 2 with $39$ in place of $C$.
4. **From $39$ to $C$.** `raise` uses $H_S \geq 1$ when a term exists (`exponents_and_defect`); otherwise the mass is $0$.
5. **Good places.** Under `PrimeTo`, `GoodPlace.equality` gives $H_S = 1$, defect zero for every term, and the sum over all terms equal to the mass. So the defect-zero sum equals it too (`ampSq_BBzero_eq`).

## In the Lean code

The theorem is in [HermitianDoubleCosetAmplitudeBoundLocal.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermitianDoubleCosetAmplitudeBoundLocal.lean#L54). `NGAt`, `RelG` and `theta` are in [IsTermOver.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/IsTermOver.lean#L202); `Frames` is in [ComplementReferenceCompactSubgroup.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/ComplementReferenceCompactSubgroup.lean#L14). It calls (namespace `GlobalTheory`):

- `HL.CoordExist.exists_coord`;
- `T.hermitianLocalSums_eq_const_mul_coordinateSums`, `T.framePairCoordinates_localHeight_eq_residueCard`;
- `HL.NonzeroDefect.ampSq_nonzero_defect`, `HL.NoCancellation.ampSq_le_height_mul_mass`;
- `HL.GoodPlace.equality`, `HL.Defect.exponents_and_defect`;
- `raise`, `nn_eq_zero`, `ampSq_BBzero_eq` in the same file.

The hypothesis $C \geq 39$ is used only in `raise`. We have not unfolded `Reps`, `Datum.wt` or $\psi_\theta$. No file we opened explains "non-generic".
