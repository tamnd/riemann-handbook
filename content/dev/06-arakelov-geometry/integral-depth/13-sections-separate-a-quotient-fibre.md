---
title: Sections separate a quotient fibre
decls:
  - GlobalTheory.QuotSep.sections_separate_quotient_fibre
  - GlobalTheory.T.sections_separate_quotient_generic_fibre_descends
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Sections separate a quotient fibre

Let $X$ be a smooth projective variety over a number field and let $q : X' \to W$ be a finite map from a modification $X'$ of $X$. This section shows that the sections of an adjoint bundle $K_X \otimes B$ separate the complex points of one fibre of $q$, when one of these points is very general and $B$ is a large multiple of a nef and big bundle that comes from $W$. Separation means that no nontrivial linear combination of the values at these points vanishes on all sections. The result is used in [the separation of orbits by cusp forms](/entry/separate-orbits-by-cusp/).

The proof rests on three published results. We state them in the form in which they are used and cite them in the notes at the end of the chapter.

**Definition 3.13.1 (Published inputs).** We assume:

1. *Nadel vanishing with non-klt centres.* The Nadel vanishing theorem for multiplier ideals and the existence of divisors whose non-klt locus is isolated at given points, as in the method of Angehrn and Siu ([$L^2$ estimates](/learn/positivity-resolution/#l2-estimates)).
2. *Numerics of nef bundles.* The numerical properties of nef and big line bundles: pullbacks under projective maps, and ampleness at the generic point of a bundle whose pullback is big.
3. *Principalization.* Principalization of ideal sheaves on smooth varieties in characteristic $0$ (Hironaka).

We do not unfold these statements.

Let $F$ be a number field and $\sigma : F \to \mathbb{C}$ an embedding. For a scheme $Y$ over $F$, a *complex point over $\sigma$* is a morphism $v : \mathrm{Spec}\,\mathbb{C} \to Y$ whose composite with $Y \to \mathrm{Spec}\,F$ is the map defined by $\sigma$. For a line bundle $\mathcal{L}$ on $Y$, a complex point $v$ and a trivialization of $\mathcal{L}$ on an open set that contains the image of $v$, every section $g$ of $\mathcal{L}$ has a *value* $g(v) \in \mathbb{C}$.

**Theorem 3.13.2 (Sections separate a quotient fibre).** Assume the three published inputs. Let $F$ be a number field and $\sigma : F \to \mathbb{C}$. Let $X$, $X'$ and $W$ be integral schemes over $F$, with:

1. $X$ smooth of dimension $n \ge 1$, projective and geometrically connected over $F$;
2. a morphism $\varphi : X' \to X$ such that $X'$ is projective over $F$;
3. $W$ projective over $F$ and a finite surjective morphism $q : X' \to W$ over $F$;
4. a scheme $V$ with open immersions $\ell : V \to X'$ and $i = \varphi \circ \ell : V \to X$.

Let $K$ be a canonical bundle of $X$. Let $\delta$, $N'$ and $B$ be line bundles on $X$ and $N$ a line bundle on $W$ such that $q^* N = \varphi^* \delta$ in the Picard group of $X'$, $\delta$ is nef and big, and $N'$ is nef. Let $m \in \mathbb{N}$ with
$$m > \binom{n + 1}{2}, \qquad B = m\,\delta + N' \ \text{in } \mathrm{Pic}(X).$$
Let $J$ be a finite set and $v_j$ ($j \in J$) pairwise distinct complex points of $V$ over $\sigma$ such that $q \ell v_j$ is the same point of $W$ for all $j$, and such that for some $j$ the point $i v_j$ lies over the generic point of $X$. Fix trivializations of $K \otimes B$ near the points $i v_j$. If $a \in \mathbb{C}^J$ satisfies
$$\sum_{j \in J} a_j\, g(i v_j) = 0 \quad \text{for all } g \in H^0(X, K \otimes B),$$
then $a = 0$.

Lean: `GlobalTheory.QuotSep.sections_separate_quotient_fibre` (also `GlobalTheory.T.sections_separate_quotient_generic_fibre_descends`, a second name).

The bound $m > \binom{n+1}{2}$ has the shape of the bound of Angehrn and Siu for the separation of points by adjoint bundles. Up to the nef part $N'$, the bundle $B$ is $m$ times a pullback from $W$, and all the points $v_j$ have the same image in $W$.

*Proof.* The proof replaces $X$ by a smooth modification on which $q$ becomes a morphism, proves the separation there, and pushes the sections down.

*A resolved modification.* By principalization there are a smooth projective geometrically connected variety $W'$ over $F$ of dimension $n$, a modification $\pi : M \to X$ that is an isomorphism over a dense open $U \subset X$, with $M$ smooth and projective, a surjective morphism $f : M \to W'$, a line bundle $N_W$ on $W'$ with $f^* N_W = \pi^* \delta$ in $\mathrm{Pic}(M)$, and complex points $z_j$ of $M$ with $\pi z_j = i v_j$. The points $f z_j$ are all equal, and some $z_j$ lies over the generic point. This is an input lemma; it uses only principalization.

*Positivity on $M$ and $W'$.* By the numerics of nef bundles, $\pi^*\delta$ and $\pi^* N'$ are nef. Since $\pi$ is an isomorphism over a dense open set, $\pi^*\delta$ is big. Then $N_W$ is nef, since its pullback under the surjective projective map $f$ is nef, and $f^* N_W = \pi^*\delta$ is big.

*Generic data.* Since $M$ and $W'$ have the same dimension and $f$ is surjective, the residue field extension at the generic point is finite, so $f$ is generically finite. The numerics of nef bundles then show that $N_W$ is ample at the generic point of $W'$, and there is an open set $U_W$ that contains the generic point of $W'$ and over which $f$ is étale.

*Pushing sections.* Let $K_M$ be the canonical bundle of $M$. An input lemma on canonical bundles of modifications gives a linear map
$$\Psi : H^0(M, K_M \otimes \pi^* B) \to H^0(X, K \otimes B)$$
and, for each $j$ and a chart of $K_M \otimes \pi^* B$ near $z_j$, a constant $\lambda_j \ne 0$ such that $\Psi(g')(i v_j) = \lambda_j\, g'(z_j)$ for every section $g'$ on $M$. The lemma uses that $\pi$ is an isomorphism over $U$ and that the points $z_j$ lie over $U$.

*Separation on $M$.* In $\mathrm{Pic}(M)$ we have $\pi^* B = m\, f^* N_W + \pi^* N'$. The points $z_j$ are distinct, lie over $\sigma$, have the same image in $W'$, and the common image lies in $U_W$ where $N_W$ is ample. An input lemma on separation over number fields, which uses Nadel vanishing and the numerics of nef bundles, applies to $M$, $W'$, $f$, $N_W$, $\pi^*N'$ and $m$. It shows: if $b \in \mathbb{C}^J$ and $\sum_j b_j g'(z_j) = 0$ for all $g' \in H^0(M, K_M \otimes \pi^*B)$, then $b = 0$.

*Conclusion.* Put $b_j = a_j \lambda_j$. For every $g'$ on $M$,
$$\sum_j b_j\, g'(z_j) = \sum_j a_j\, \Psi(g')(i v_j) = 0$$
by the hypothesis on $a$. So $b = 0$, and $a = 0$ since $\lambda_j \ne 0$. $\square$

**Remark 3.13.3 (Formalization).** The three published inputs are hypotheses of the theorem; principalization is used only to build the modification, and Nadel vanishing only in the separation on $M$ ([SectionsSeparateQuotientGenericFibreDescends.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SectionsSeparateQuotientGenericFibreDescends.lean#L405)). Values of sections are taken in fixed charts of the line bundle, and the statement quantifies over the choice of charts at the points. The condition that one point lies over the generic point is the form of "very general" used here. The bundle $N'$ needs only to be nef. We have not unfolded the published statements, nor the lemmas on resolved modifications, on canonical bundles of modifications and on separation over number fields. The second name is a wrapper.
