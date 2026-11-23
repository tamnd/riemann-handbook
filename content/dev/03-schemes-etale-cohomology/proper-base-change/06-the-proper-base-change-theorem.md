---
title: The proper base change theorem
decls:
  - UpperTheory.Et.E2.towers
  - UpperTheory.Et.E2.main
  - UpperTheory.Et.proper_base_change
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The proper base change theorem

We now prove the proper base change theorem for the coefficients $\mathbb{Z}/q(i)$. The proof puts together the results of the previous four sections. It first reduces the theorem to AIC schemes. Then a form of Chow's lemma replaces a proper map by a tower of curves over projective lines, and the fibre criterion climbs the tower one step at a time. The [Galois row](/proof/galois-row/) uses the theorem through the step [Steps holds](/entry/steps-holds/), and the finiteness theorem of the next section uses it as a hypothesis.

**Theorem 3.6.1 (Proper base change).** Let $A$ be a strictly henselian local ring with residue field $\kappa$, and let $q \geq 1$ be an integer that is a unit in $A$. Let $p : X \to \operatorname{Spec} A$ be a proper map, and let $X_0 = X \times_{\operatorname{Spec} A} \operatorname{Spec} \kappa$ be the closed fibre. Then for all $n$ and $i$ the restriction
$$H^n(X, \mathbb{Z}/q(i)) \to H^n(X_0, \mathbb{Z}/q(i))$$
is bijective.

This is the proper base change theorem of M. Artin in SGA 4, Exposé XII, §5, for the constant coefficients $\mathbb{Z}/q(i)$ (see also J. S. Milne, *Étale Cohomology*, Chapter VI, §2, and the [Background](/learn/geometry/#tale-cohomology)). It is the axiom E2 of the first section.

Lean: `UpperTheory.Et.proper_base_change` (also `UpperTheory.Et.E2.main`, the same statement under the hypothesis record).

**Remark 3.6.2.** The published theorem holds for every torsion sheaf, and it does not need the torsion order to be invertible on $A$. We prove the special case of the sheaves $\mathbb{Z}/q(i)$ with $q$ a unit in $A$, for the cohomology of the model of the first section.

### Towers

We need three more facts about maps.

1. *Integral maps.* If $A$ is strictly henselian, $q$ is a unit in $A$ and $p : X \to \operatorname{Spec} A$ is integral, then $\mathrm{PB}_{q,i}(p)$ holds. Indeed an integral map is affine, so $X = \operatorname{Spec} C$ with $C$ integral over $A$. Since $A$ is henselian, the pair $(C, \mathfrak{m} C)$ is henselian, and axiom E1 gives the claim.
2. *Descent.* Let $A$ be local and $p : P \to \operatorname{Spec} A$ a map. Assume that for every integral map $h : X \to P$ there is an integral surjective $k : Y \to X$ with $\mathrm{PB}_{q,i}(p \circ h \circ k)$. Then $\mathrm{PB}_{q,i}(p)$ holds. This is descent along integral surjective maps, from axiom B4.
3. *Stein factorization.* Let $g : Z \to S$ be quasi-compact and quasi-separated, with $Z$ an AIC scheme. Then $g = k \circ c$ with $c : Z \to T$ dominant, $T$ an AIC scheme and $k : T \to S$ integral. Here $T$ is the normalization of $S$ in $Z$, the relative spectrum of the integral closure of $\mathcal{O}_S$ in $g_* \mathcal{O}_Z$.

From descent and [Theorem 3.4.7](/entry/e2-n9/) we get the *reduction*: if $p : P \to \operatorname{Spec} A$ is qcqs, $q$ is a unit in $A$, and $\mathrm{PB}_{q,i}(p \circ h)$ holds for every integral $h : Z \to P$ with $Z$ an AIC scheme, then $\mathrm{PB}_{q,i}(p)$ holds. Indeed, let $h : X \to P$ be integral. Then $p \circ h$ is qcqs, and each integral $k' : Z \to X$ from an AIC scheme gives the integral map $h \circ k'$, so the hypothesis of [Theorem 3.4.7](/entry/e2-n9/) holds for $p \circ h$. It gives an integral surjective $k : Y \to X$ with $\mathrm{PB}_{q,i}(p \circ h \circ k)$, which is the hypothesis of descent.

**Definition 3.6.3 (Tower).** Let $S$ be a scheme. The class of *towers* over $S$ is the smallest class of maps $p : X \to S$ such that

1. every integral map $p : X \to S$ is a tower, and
2. if $k : T \to S$ is a tower and $c : X \to T$ is integral over a line, then $k \circ c$ is a tower.

So a tower is a composite $X = X_m \to X_{m-1} \to \cdots \to X_1 \to X_0 \to S$, where $X_0 \to S$ is integral and each other step is integral over a projective line. Towers are stable under base change and under composition with an integral map on the source. Each tower is quasi-compact and quasi-separated.

**Lemma 3.6.4 (Curves over a line).** Let $A$ be strictly henselian, $q$ a unit in $A$, and $p : X \to \operatorname{Spec} A$ integral over a line. Then $\mathrm{PB}_{q,i}(p)$ holds.

Lean: `LateralTheory.E.t_E2Cut.line`.

*Proof.* By the reduction, it is enough to prove $\mathrm{PB}_{q,i}(p \circ h)$ for every integral map $h : Z \to X$ with $Z$ an AIC scheme. The map $p \circ h$ is again integral over a line. Let $Z_0$ be its closed fibre. We use the equivalence test of the previous section: it is enough that $H^0(Z) \to H^0(Z_0)$ is bijective and that $Z$ and $Z_0$ are acyclic. The scheme $Z_0$ is connected by [Theorem 3.3.2](/entry/n52/), so the first fact on AIC schemes gives the bijection on $H^0$. The scheme $Z$ is a qcqs AIC scheme, so it is acyclic. For $Z_0$, we have $H^1(Z_0) = 0$ by [Theorem 3.3.5](/entry/n74/), and $H^n(Z_0) = 0$ for $n \geq 2$ by the third fact on such curves (see the last remark after [Theorem 3.3.5](/entry/n74/)). $\square$

**Theorem 3.6.5 (Proper base change for towers).** Assume the axioms A1 to A5, A7 to A10, B1 to B5 and E1. Let $B$ be a strictly henselian local ring, $q$ a unit in $B$, and $r : Y \to \operatorname{Spec} B$ a tower. Then $\mathrm{PB}_{q,i}(r)$ holds.

Lean: `UpperTheory.Et.E2.towers`.

*Proof.* We prove a stronger statement by induction on the tower $p : X \to \operatorname{Spec} B$: for every integral map $v : W \to X$, $\mathrm{PB}_{q,i}(p \circ v)$ holds. The theorem is the case $v = \mathrm{id}$.

If $p$ is integral, then $p \circ v$ is integral, and the first fact gives the claim.

Let $p = k \circ c$ with $k : T \to \operatorname{Spec} B$ a tower and $c : X \to T$ integral over a line, and assume the claim for $k$. Let $v : W \to X$ be integral. By the reduction, it is enough to prove $\mathrm{PB}_{q,i}(p \circ v \circ h)$ for every integral $h : Z \to W$ with $Z$ an AIC scheme. Apply Stein factorization to $c \circ v \circ h : Z \to T$. It gives $c \circ v \circ h = k' \circ c'$ with $c' : Z \to T'$ dominant, $T'$ an AIC scheme and $k' : T' \to T$ integral. Since $c \circ v \circ h$ is integral over a line and $k'$ is integral, also $c'$ is integral over a line. Then
$$p \circ v \circ h = k \circ k' \circ c'.$$
We apply the [fibre criterion](/entry/proper-base-change-fibre/) to $c'$ and $k \circ k'$. Its hypothesis holds: for a strictly henselian point $t$ of $T'$, the base change of $c'$ to $t$ is integral over a line, so the lemma on curves over a line gives the closed fibre condition. So $\mathrm{PB}_{q,i}(k \circ k' \circ c')$ holds if and only if $\mathrm{PB}_{q,i}(k \circ k')$ holds. The latter is the induction hypothesis for $k$ and the integral map $k'$. $\square$

### Proof of the theorem

The last input is a form of Chow's lemma. Let $p : X \to \operatorname{Spec} A$ be proper and let $h : Z \to X$ be integral with $Z$ an AIC scheme. Then there is a dominant map $c : Z' \to Z$ from an AIC scheme $Z'$ such that $c$ and $p \circ h \circ c$ are towers. We take this form as given. It comes from Chow's lemma (A. Grothendieck, EGA II, Théorème 5.6.1), which dominates $X$ by a projective scheme, and from normalization.

*Proof of the theorem.* Let $A$, $q$ and $p : X \to \operatorname{Spec} A$ be as in the theorem. A proper map is qcqs, so by the reduction it is enough to prove $\mathrm{PB}_{q,i}(p \circ h)$ for every integral $h : Z \to X$ with $Z$ an AIC scheme.

Chow's lemma gives $c : Z' \to Z$ dominant, with $Z'$ an AIC scheme, such that $c$ and $p \circ h \circ c$ are towers. By [Theorem 3.6.5](/entry/towers/), $\mathrm{PB}_{q,i}(p \circ h \circ c)$ holds.

We apply the [fibre criterion](/entry/proper-base-change-fibre/) to $c : Z' \to Z$ and $p \circ h : Z \to \operatorname{Spec} A$. Both are qcqs, and $Z'$ and $Z$ are AIC schemes. For a strictly henselian point $t$ of $Z$, the base change of $c$ to $t$ is a tower, so its closed fibre condition holds by [Theorem 3.6.5](/entry/towers/). The criterion then turns $\mathrm{PB}_{q,i}(p \circ h \circ c)$ into $\mathrm{PB}_{q,i}(p \circ h)$. $\square$

**Remark 3.6.6 (Formalization).** The theorem `UpperTheory.Et.E2.main` takes the axioms A1 to A5, A7 to A10, B1 to B5 and E1 as one record, and `UpperTheory.Et.proper_base_change` fills it with theorems proved elsewhere; E1 is [Theorem 3.12.2](/entry/affine-proper-base-change/), after O. Gabber, Israel J. Math. 87 (1994). The schemes are in the smallest universe. The statement has no hypothesis $q \neq 0$ and needs none. The file of the record has an unused second proof, whose statement bundles 25 axioms and whose proof discards 10 of them ([LineHigh.lean](lean:Development/EtaleCohomology/EtaleSheaves/LineHigh.lean#L234)). The facts on integral maps, descent, Stein factorization, Chow's lemma and $H^n$ for $n \geq 2$ on curves over a line are `proper_base_change_integral_pullback`, `UpperTheory.Et.E2.n1`, `proper_base_change_stein_factorization`, `e2Cut_chow` and `proper_base_change_affine_space`. We checked them from their statements.
