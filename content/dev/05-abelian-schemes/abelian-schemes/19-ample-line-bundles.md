---
title: Ample line bundles
decls:
  - GlobalTheory.ProjNormal.exists_relAmple_of_affine
  - GlobalTheory.PolBundleLoc.exists_descent_two
  - GlobalTheory.PolBundleLoc.exists_ample_root
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Ample line bundles

This section proves two existence results for ample line bundles. The first is fact 1 of the section on the reduced case: an abelian scheme over a noetherian normal domain has a relatively ample line bundle as soon as some affine open set meets every fibre (Theorem (Ample bundles over normal domains)). The second works over an algebraically closed field $K$. A line bundle $P$ on $A \times A$ that is trivial on the axes, symmetric, and has ample restriction to the diagonal is the Mumford bundle $\Lambda(L)$ of an ample line bundle $L$ (Theorem (Ample root)). In the language of polarizations, a symmetric homomorphism $\lambda : A \to A^\vee$ whose pullback of the Poincaré bundle along $(1, \lambda)$ is ample is of the form $\varphi_L$ for an ample $L$ (see [polarizations](/learn/abelian-varieties/#polarizations-and-zarhins-trick)). The proof descends a line bundle along the doubling map $[2]$ (Proposition (Descent along doubling)). These results are used on the way to [EveryCharacter](/step/every-character/): the first in the construction of the dual abelian scheme, the second to show that each geometric point of a family of polarized abelian schemes carries an ample root.

We keep the notation of the earlier sections. Line bundles on schemes over a base are given by Čech data, $\mathrm{Pic}$ is written additively, and relative ampleness is Definition (Relatively ample) of the section on additive line bundles. Over a field, an abelian scheme is an abelian variety, and a line bundle is relatively ample if and only if it is ample. For a commutative group scheme $A$ with group law $m$ and projections $p_1$, $p_2$ on $A \times A$, the Mumford bundle of $L$ is $\Lambda(L) = m^* L - p_1^* L - p_2^* L + 1^* L$. Let $[2] : A \to A$ be the doubling map $x \mapsto x + x$, $\Delta = (\mathrm{id}, \mathrm{id}) : A \to A \times A$ the diagonal and $\sigma = (p_2, p_1)$ the swap of the factors.

**Theorem 1.19.1 (Ample bundles over normal domains).** Let $R$ be a noetherian integrally closed domain and $A$ an abelian scheme over $\mathrm{Spec}\, R$. Let $V$ be an affine open set of $A$ that meets every fibre of $A \to \mathrm{Spec}\, R$. Then $A$ has a relatively ample line bundle.

Lean: `GlobalTheory.ProjNormal.exists_relAmple_of_affine`.

This is a form of a theorem of Raynaud: an abelian scheme over a normal base is projective locally on the base (see the Notes and references). The condition on $V$ is the one used in the section on the reduced case.

We use two facts.

1. (Divisors.) Let $R$ and $A$ be as in the theorem and $V$ an affine open set of $A$ that meets every fibre. Then there are a line bundle $M$ on $A$ and a global section $s$ of $M$ whose nonvanishing locus is $V$.
2. (Ampleness from one section.) Let $R$ be noetherian and $A$ an abelian scheme over $\mathrm{Spec}\, R$. Let $M$ be a line bundle on $A$ and $s$ a global section of $M$ whose nonvanishing locus is affine and meets every fibre. Then $M$ is relatively ample.

Fact 1 is where normality enters: the complement of $V$ is to be the zero set of a section of a line bundle. Fact 2 needs only that $R$ is noetherian.

*Proof.* Fact 1 gives $M$ and $s$ with nonvanishing locus $V$. This locus is affine and meets every fibre, so fact 2 shows that $M$ is relatively ample. $\square$

We turn to the case of an algebraically closed field $K$. Let $A$ be an abelian variety over $K$. The doubling map is finite, flat and surjective, so it is a cover for descent. Let $A \times_{[2], A, [2]} A$ be the fibre product of $[2]$ with itself, with projections $q_1$ and $q_2$; its points are the pairs $(x, y)$ with $2x = 2y$.

**Proposition 1.19.2 (Descent along doubling).** Let $K$ be an algebraically closed field and $A$ an abelian scheme over $K$, with its group law commutative. Let $M$ be a line bundle on $A$ with $q_1^* M \cong q_2^* M$ on $A \times_{[2], A, [2]} A$. Then there is a line bundle $L$ on $A$ with $M^{\otimes 2} \cong [2]^* L$.

Lean: `GlobalTheory.PolBundleLoc.exists_descent_two`.

The hypothesis does not say that $M$ descends along $[2]$: an isomorphism $q_1^* M \cong q_2^* M$ need not satisfy the cocycle condition. The proposition says that the defect of the cocycle condition is killed by passing to $M^{\otimes 2}$.

*Proof.* The map $[2]$ is finite, by the finiteness of multiplication by a nonzero integer on an abelian variety. As a finite endomorphism of the abelian variety $A$ that respects the group law, it is flat and surjective. Let $\varphi : q_1^* M \to q_2^* M$ be an isomorphism. On the triple fibre product $A \times_A A \times_A A$ of $[2]$, the cocycle condition for $\varphi$ fails by a global unit $D$, the *defect*. The defect is a cocycle on the triple fibre product. For the doubling map of an abelian variety over an algebraically closed field, such a cocycle is killed after squaring: there is a unit $u$ on $A \times_A A$ that turns the square of $D$ into $1$. Changing $\varphi^{\otimes 2}$ by $u$ gives an isomorphism $\psi$ for a bundle $M_2 \cong M^{\otimes 2}$ that satisfies the cocycle condition. So $(M_2, \psi)$ is a descent datum along the finite flat surjection $[2]$, and descent gives $L$ with $[2]^* L \cong M_2 \cong M^{\otimes 2}$. $\square$

A line bundle $P$ on $A \times A$ is *biadditive* if for all points $x, x', y$ of $A$ with values in any $K$-scheme $T$,
$$P(x + x', y) = P(x, y) + P(x', y), \qquad P(y, x + x') = P(y, x) + P(y, x'),$$
in $\mathrm{Pic}(T)$, where $P(x, y) = (x, y)^* P$.

**Theorem 1.19.3 (Ample root).** Let $K$ be an algebraically closed field and $A$ an abelian scheme over $K$, with its group law commutative. Let $P$ be a line bundle on $A \times A$ such that:

1. $P$ is trivial on $\{1\} \times A$ and on $A \times \{1\}$;
2. $P \cong \sigma^* P$;
3. $\Delta^* P$ is relatively ample.

Then there is a relatively ample line bundle $L$ on $A$ with $\Lambda(L) \cong P$.

Lean: `GlobalTheory.PolBundleLoc.exists_ample_root`.

For $P = (1 \times \lambda)^* \mathcal{P}$, with $\mathcal{P}$ the Poincaré bundle and $\lambda$ a symmetric homomorphism to the dual, the conditions say that $\lambda$ is symmetric and that $\Delta^* P = (1, \lambda)^* \mathcal{P}$ is ample. The conclusion is $\lambda = \varphi_L$.

We use the following facts, for $A$ and $P$ as in the theorem. Write $M = \Delta^* P$.

1. (Laws.) The laws of abelian schemes of the earlier sections hold, among them the constancy of global functions after base change.
2. (Biadditivity.) If $M$ is relatively ample and $P$ is trivial on both axes, then $P$ is biadditive.
3. (Finite schemes.) Every line bundle on a finite affine scheme is trivial.
4. (Roots of biadditive bundles.) Let $P$ be biadditive with $P(x, y) = P(y, x)$ for all points, and $L$ a line bundle with $M^{\otimes 2} \cong [2]^* L$. Then $\Lambda(L) \cong P$.
5. (Powers.) A line bundle $L$ on a proper $K$-scheme is ample if and only if $L^{\otimes 2}$ is ample.

*Proof.* By facts 1 and 2, $P$ is biadditive, and by hypothesis 2, $P(x, y) = P(y, x)$. With $x = 1$, biadditivity gives $P(1, y) = P(1, y) + P(1, y)$, so $P(1, y) = 0$. Also $M(x) = \Delta^* P (x) = P(x, x)$.

First, $P(t, t) = 0$ for each point $t$ with $2t = 1$. The kernel $N$ of $[2]$ is a finite affine scheme, since $[2]$ is finite. A point $t$ with $2t = 1$ factors through $N$, and $M|_N$ is trivial by fact 3. So $P(t, t) = M(t) = 0$.

Second, $q_1^* M \cong q_2^* M$. Let $x = q_1$ and $y = q_2$, the two projections of $A \times_{[2], A, [2]} A$, and $t = y - x$. Then $2x = 2y$, so $2t = 1$. Biadditivity gives
$$\begin{aligned} M(y) = P(x + t, x + t) &= P(x, x) + P(t, x) + P(x, t) + P(t, t) \\ &= M(x) + 2 P(t, x) + P(t, t), \end{aligned}$$
using $P(x, t) = P(t, x)$. Here $2 P(t, x) = P(2t, x) = P(1, x) = 0$, and $P(t, t) = 0$ by the first step. So $M(y) = M(x)$, which is $q_2^* M \cong q_1^* M$.

By Proposition (Descent along doubling) there is $L$ with $M^{\otimes 2} \cong [2]^* L$, and fact 4 gives $\Lambda(L) \cong P$. It remains to show that $L$ is ample. Since $K$ is a field, $L(1)$ is trivial, so $\Lambda(L)(x, y) = L(x + y) - L(x) - L(y)$. Then
$$M = \Delta^* P = \Delta^* \Lambda(L) = [2]^* L - 2L.$$
From $2M = [2]^* L$ we get $2M = M + 2L$, so $M = 2L$ in $\mathrm{Pic}(A)$, that is $L^{\otimes 2} \cong M$. Since $M$ is ample, fact 5 shows that $L$ is ample. $\square$

**Remark 1.19.4 (Formalization).** Facts 1 and 2 of the first theorem are `GlobalTheory.T.exists_section_nonzeroLocus_eq_affineOpen` and `GlobalTheory.T.relAmple_of_affine_nonzeroLocus_abelianScheme_noetherian`; they are cited by their statements, and the sentence on where normality enters is a reading of these statements. The file of the first theorem has no `import Mathlib` line, unlike the other files of this part ([ExistsRelAmpleOfAffineOpenMeetsFibres.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRelAmpleOfAffineOpenMeetsFibres.lean#L1)). In the proof of the Proposition, the steps are `GlobalTheory.MulFinite.isFinite_mul`, `GlobalTheory.flat_and_surjective_of_isFinite_abelianEnd`, `GlobalTheory.LBDescent.descCompat_of_lbIso`, `GlobalTheory.T.exists_descentCocycleDefect_of_compatible`, `GlobalTheory.T.descentCocycleDefect_isTripleCocycle`, `GlobalTheory.T.exists_unit_killing_square_tripleFibreCocycle_mulTwo`, `GlobalTheory.T.exists_squareBundle_descent_of_defect_killed` and `GlobalTheory.T.exists_lineBundle_descent_finiteFlat`; their proofs were not read, and the sentences of the proof describe what their statements give. In the Theorem (Ample root), fact 1 is `GlobalTheory.lawsAndExpansions.1.1`, the laws `Out.Laws` of [UniformizationLawsAndExpansionStatements.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/UniformizationLawsAndExpansionStatements.lean#L24), which the proof uses only through its part on global functions and in fact 4. Facts 2 to 5 are `GlobalTheory.LamOfDouble.biadd_of_axes`, `GlobalTheory.exists_isGen_of_finite`, `GlobalTheory.SymBiextHalf.lam_iso` and `isAmpleLB_pow_iff`; the symmetry $P(x, y) = P(y, x)$ is `GlobalTheory.PolBundleLoc.ev_symm`. The same file proves `GlobalTheory.PolBundleLoc.exists_rigLB_cubical` (a cubical structure on a line bundle over a local base) and `GlobalTheory.PolBundleLoc.root_geom` (the root at each geometric point of a Siegel family, from the Theorem); they are not part of this section. Relative ampleness over a field is compared with ampleness by `relAmple_iff_isAmpleLB_of_isAffine`.
