---
id: covolume-n
title: The covolume of the integral unipotent radical
kind: theorem
decl: GlobalTheory.SnMass.VolN.covolume_N
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.CovolumeIntegralUnipotentRadicalRealPoints
covers: 375
status: drafted
drafted_by: writer@claude
---
This theorem computes the volume of a fundamental domain for the integral points of a unipotent radical over all infinite places. It has [a renaming](/entry/covolume-integral-unipotent-radical-real-points/). [`CovDom.main`](/entry/cov-dom-main/) applies it to the global datum, for [the closed formula](/entry/cov-nformula-pf-main/) of the step [nonempty hypotheses](/step/nonempty-hyps/).

## Statement

Let $E/F$ be a CM extension with involution $\sigma$, with $\mathcal O_E$ unramified over $\mathcal O_F$. Let $n = 2r + k + 1$. The model form $H$ on $\mathbb C^n$ pairs $e_a$ with $e^*_a = e_{2r+k-a}$ for $a < r$, and is $\mathrm{diag}(1, \dots, 1, -1)$ on the $k+1$ middle vectors. The model group $N$ is the set of $H$-unitary matrices that fix each $e_a$ modulo the earlier $e_b$, and fix each middle vector modulo the span of all $e_a$.

The data satisfy these conditions:
- $J$ is Hermitian with $\det J \ne 0$, and $\Lambda$ is self-dual for $J$;
- $P$ is a frame: $P^* J P = \mathrm{diag}(0, \dots, 0, -T)$;
- $f$ is dual to $P$, with $\langle f_b, p_a\rangle = \delta_{ab}$ and $f^* J f = 0$;
- the lattice spanned by $\mathfrak d^{-(r-b)} p_b$ and $\mathfrak d^{\,r-b} f_b$ lies in $\Lambda$, with $\mathfrak d$ the different of $E$;
- $A_w^* H A_w = w(J)$ at each infinite place $w$;
- $A_w\, w(p_a) = s_a e_a$ and $A_w\, w(f_a) = s_a^{-1} e^*_a$, with all $s_a > 0$.

Let $\Gamma$ be the set of $J$-unitary $\gamma$ over $E$ that preserve $\Lambda$ and act on the frame like an element of $N$. A domain is a measurable set $\mathcal D$ such that every family $(x_w)$ in $N^{\{w\}}$ has exactly one $\gamma \in \Gamma$ with $(A_w\, w(\gamma)\, A_w^{-1} x_w)_w \in \mathcal D$.

**Theorem.** A domain exists. Every domain has measure
$$|d_F|^{-(k+1)r^2 - 4(r^3 - r)/3 - 3r/2}\Bigl(\prod_{a<r} s_a^{\,4(r-a)+2k}\Bigr)^{\#\{w\}}$$
for the product of the Lie algebra Haar measures with scale 1 on $N$.

## Proof

1. $\Gamma$ is a group. It acts faithfully on $N^{\{w\}}$ by left multiplication with $A_w\,w(\gamma)\,A_w^{-1}$.
2. Write an element of $N$ in four kinds of block coordinates: the upper entries $x(e_a, e_b)$ with $a < b$; the rows $x(e_a, \cdot)$ on the middle space; the corner entries $x(e_a, e^*_b)$ with $a < b$; and the imaginary parts of $x(e_a, e^*_a)$. The integral points in each block form a lattice built from powers of $\mathfrak d^{-1}$, scaled by $s_a/s_b$, $s_a s_b$ or $s_a^2$. Four lemmas give each covolume in terms of $|d_F|$, 2 and the scales.
3. `existsUnique_layered_strictFundamentalDomain` builds a strict fundamental domain layer by layer from the block domains. The inputs: block entries add under products at enough depth, integral entries lie in the block lattices, and lattice points lift to $\Gamma$.
4. `strictFundamentalDomain_measure_eq`: all strict fundamental domains of a countable group acting by measure-preserving maps have the same measure.
5. `measure_unipotent_tuples_free_entry_blocks` gives the measure of the layered domain as a power of 2 times the product of the block covolumes. `unipotentRadical_blockCovolumes_prod` does the arithmetic.

The powers of 2 cancel. A hand check for $r \le 2$ gives the same exponent of $|d_F|$.

## In the Lean code

The theorem is at [CovolumeIntegralUnipotentRadicalRealPoints.lean line 88](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CovolumeIntegralUnipotentRadicalRealPoints.lean#L88). The conditions are bundled as `IsVolData`, and the domain condition is `IsDomN` at [NCoords.lean line 73](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/NCoords.lean#L73). `AllSome` means that a domain exists and that all domains satisfy the formula. `IsDomN` does not ask that $\mathcal D$ lie in $N^{\{w\}}$. The Haar measure lives on $N$, so this does no harm. The block covolume and lifting lemmas are not unfolded here.
