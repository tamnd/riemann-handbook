---
id: mean-count-box
title: The mean number of rational vectors in an adelic box
kind: theorem
decl: GlobalTheory.CompanionTheory.SW.MeanCount.mean_count_box
module: CompanionTheory.SpectralGeometry.LocalGlobalProofs.AdelicAnalysis.ThetaMeasureNonzeroVectorsBound
covers: 327
status: drafted
drafted_by: writer@claude
---
This theorem bounds the average, over the automorphic quotient of a unitary group, of the number of nonzero rational vectors in an adelic box, by a polynomial in the radius. Every compact set lies in a box, so the theta measure of the nonzero vectors is finite on compact sets. The theorem is published under a second name, [`theta_measure_nonzero_vectors_bound`](/entry/theta-measure-nonzero-vectors-bound/), which is used below [EveryCharacter](/step/every-character/).

## Statement

Let $E/F$ be a CM extension of number fields: $F$ is totally real, $E$ is totally complex, $[E:F] = 2$, and $\sigma$ is the automorphism of $E/F$ that acts as complex conjugation under every embedding $E \to \mathbb{C}$. Let $d_0 = [F:\mathbb{Q}]$. Let $J$ be an $M \times M$ matrix over $E$ with $\sigma(J_{ji}) = J_{ij}$ and $\det J \neq 0$, and let $h(x, y) = \sigma(x)^{\mathsf T} J y$ be its hermitian form. Let $H(\mathbb{A}_F)$ be the group of $g \in \mathrm{GL}_M(\mathbb{A}_F \otimes_F E)$ with $\sigma(g)^{\mathsf T} J g = J$, and $H(F)$ the image of the group of such $g$ over $E$. Let $\mu$ be a Haar measure on $H(\mathbb{A}_F)$ and $\mathcal{F}$ a fundamental domain for the left action of $H(F)$.

Fix a basis $b$ of $E$ over $F$ and an integer $N \geq 1$. For $r > 0$ let $B(N, r) \subset (\mathbb{A}_F \otimes_F E)^M$ be the set of $Y$ such that, at each finite place $v$, the $b$-coordinates of $N Y_v$ lie in $\mathcal{O}_{F_v}$, and such that the sum of the absolute values of the $b$-coordinates of $Y_\infty$, over all entries and all infinite places, is at most $r$. The *theta measure* of a set $S \subseteq E^M$ is

$$\theta_S(B) = \mu(\mathcal{F})^{-1} \sum_{X \in S} \mu\{h \in \mathcal{F} : h^{-1} X \in B\}.$$

**Theorem.** Suppose $M \geq 3$. There is a constant $C$ such that for all $r > 0$,

$$\theta_{E^M \setminus 0}\bigl(B(N, r)\bigr) \leq C\,\bigl(r^{d_0 M} + r^{2 d_0 M}\bigr).$$

## Proof

By `theta_measure_integral_formula`, the left side is $\mu(\mathcal{F})^{-1} I(r)$, where $I(r) = \int_{\mathcal{F}} \#\{X \neq 0 : h^{-1}X \in B(N, r)\}\, d\mu(h)$. The box is compact (`adelic_boxes_compact_exhaust`), and $\mu(\mathcal{F}) \neq 0$ (`haar_fundamental_domain_exists_unitary`).

1. **Small $r$.** `small_box_gram_scalar_zero` gives $r_0 > 0$ such that, if $Y \in B(N, r_0)$ and $h(Y, Y) = t$ with $t \in F$, then $t = 0$. For $X \in E^M$ the value $h(X, X)$ lies in $F$ (`rational_gram_adelic_compact_finite`), and $H(\mathbb{A}_F)$ preserves $h$. So for $r \leq \min(r_0, 1)$ only isotropic vectors $X$ count. `isotropic_vector_count_box_bound` bounds their contribution by $C_1 r^{2 d_0 (M-1)}$. As $r \leq 1$ and $d_0 M \leq 2 d_0 (M-1)$, this is at most $C_1 r^{d_0 M}$.
2. **Large $r$.** For $r \geq \min(r_0, 1)$, `counting_vectors_bounded_large_radius` gives $I(r) \leq C_2 r^{2 d_0 M}$.

Take $C = \mu(\mathcal{F})^{-1}(|C_1| + |C_2|)$. The rest is bookkeeping.

## In the Lean code

The theorem is in [ThetaMeasureNonzeroVectorsBound.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/ThetaMeasureNonzeroVectorsBound.lean#L36). Each lemma named in the proof is a statement in its own file in the same folder, and a second name for a lemma that we have not opened (for example `isotropic_vector_count_box_bound` for `mean_isotropic_box` and `counting_vectors_bounded_large_radius` for `CntLarge.cnt_large`). The proof also calls `adelic_unitary_group_locally_compact`, for the invariance of $h$, and two lemmas on the topology of $\mathbb{A}_F$ and $\mathbb{A}_F \otimes_F E$.

The definitions are in [SWXSDefs.lean](lean:Formalism/UnipotentAdelicQuotients/SWXSDefs.lean#L55) and, for `thetaMeas` and `box`, in [IsEulerProd.lean](lean:CompanionTheory/SpectralGeometry/CountingDefinitions/AdelicEulerProducts/IsEulerProd.lean#L84) and [HypJ.lean](lean:CompanionTheory/SpectralGeometry/CountingDefinitions/AdelicEulerProducts/HypJ.lean#L21).

The statement allows a basis indexed by any $d$, but a basis of $E$ over $F$ forces $d = 2$. The term $r^{d_0 M}$ is weaker than what the proof gives for small $r$, namely $r^{2 d_0 (M-1)}$. The hypothesis $M \geq 3$ is only passed on to the two counting lemmas; the comparison of exponents needs only $M \geq 2$.
