---
id: rel-total-zero
title: The comparison relations are total, onto, and detect zero
kind: theorem
decl: GlobalTheory.PDForm.rel_total_zero
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CrystallineCechDeRhamRelationsTotalDetectZero
covers: 328
status: drafted
drafted_by: writer@claude
---
This theorem proves that, for each smooth lift, the relation between crystalline classes and de Rham classes in degrees 1 and 2 is the graph of a bijection that sends zero to zero. Its statement form is [`crystallineCechDeRham_relations_total_detect_zero`](/entry/crystalline-cech-de-rham-relations-total-detect-zero/), and [the comparison theorem](/entry/crystalline-smooth-lift-of-relations/) turns the relations into linear isomorphisms.

## Statement

We use the notation of [the comparison theorem](/entry/crystalline-smooth-lift-of-relations/). Let $\mathrm{KK}$ (`KK D.κ D.t`) be the complex of functors on $\mathrm{Thick}(D)$ that sends a thickening $(B, J, \delta)$ to $B \to \Omega^1 \to \Omega^2 \to \Omega^3$, where $\Omega^j$ is the module of $j$-forms of $B$ over $R$ modulo the forms that `rel` makes zero, so that $d$ is compatible with $\delta$. We have not unfolded `rel`. Its cohomology $H^q(\mathrm{KK})$ is the cohomology of the total complex of cochains on chains of morphisms with values in $\mathrm{KK}$.

Let $\Lambda$ be a lift of $D$. Say that $c \in H^1_{\mathrm{cris}}(D)$ and $h \in H^1_{\mathrm{dR}}(X)$ are related ($\mathrm{Rel}_1$) if there is a cocycle $k$ of $\mathrm{KK}$ such that the function part of $k$ represents $c$, and the restriction of $k$ along $\Lambda$ is, through the isomorphisms $\mathcal{O}(U) \cong B_{\Lambda(U)}$, a cocycle that represents $h$ (`Lift.Res1`). $\mathrm{Rel}_2$ is the same in degree 2.

**Theorem.** For each $D$, each $\Lambda$ and $q \in \{1, 2\}$: each $c$ is related to some $h$; each $h$ is related to some $c$; and if $c$ is related to $h$, then $c = 0$ if and only if $h = 0$.

## Proof

The proof uses three facts, for $q = 1, 2$.

- (a) Forgetting the forms gives a bijection $H^q(\mathrm{KK}) \to H^q_{\mathrm{cris}}(D)$ (`fnMap_pullbackBijective12_kk_and_res`).
- (b) Restriction along $\Lambda$ gives a bijection from $H^q(\mathrm{KK})$ to $H^q$ of $\mathrm{KK} \circ \Lambda$ on the affine opens of $X$ ([`lift_restriction_bijective_low_degrees`](/entry/lift-restriction-bijective-low-degrees/)).
- (c) The cochains of $\mathrm{KK} \circ \Lambda$ correspond one to one with the Čech-de Rham cochains of $X$, and the correspondence keeps cocycles and coboundaries (`compatibleFormsCochains_eq_deRhamCochains_smoothLift`).

*Total.* Let $c = [f]$. By (a), some cocycle $k$ of $\mathrm{KK}$ has function part $f + d g$. By (c), the restriction of $k$ is a cocycle $w$, and $c$ is related to $[w]$.

*Onto.* Let $h = [w]$. By (c), $w$ comes from a cocycle $k_0$ of $\mathrm{KK} \circ \Lambda$. By (b), $k_0$ is cohomologous to the restriction of a cocycle $k$ of $\mathrm{KK}$. By (c) again, the restriction of $k$ gives a cocycle $w_1$ with $w_1 - w$ a coboundary. Then the class of the function part of $k$ is related to $h$.

*Detect zero.* The function part of $k$ is a coboundary if and only if $[k] = 0$, by (a); if and only if the restriction of $k$ is a coboundary, by (b); if and only if $w$ is a coboundary, by (c).

Degree 2 is the same argument. The rest is bookkeeping.

## In the Lean code

The theorem is in [CrystallineCechDeRhamRelationsTotalDetectZero.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CrystallineCechDeRhamRelationsTotalDetectZero.lean#L191). It is the pair of `crystallineCechDeRham_degreeOne_relation_total` (L105) and `crystallineCechDeRham_degreeTwo_relation_total` (L147) in the same file. The lemmas they call:

- `GlobalTheory.T.fnMap_pullbackBijective12_kk_and_res`, for (a);
- `GlobalTheory.T.lift_restriction_bijective_low_degrees`, for (b);
- `GlobalTheory.T.compatibleFormsCochains_eq_deRhamCochains_smoothLift`, for (c);
- the small lemmas `single_H1_mk_eq_zero_iff`, `single_H2_mk_eq_zero_iff` and `smoothLiftThickenings_restrictionOne_sub` of the same file.

We have not unfolded the proofs of (a) and (c).
