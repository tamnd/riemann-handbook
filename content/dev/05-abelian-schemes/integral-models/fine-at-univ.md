---
id: fine-at-univ
title: The complex points of the integral model are classified by marked period lattices
kind: theorem
decl: GlobalTheory.UPel.HT.Model.fineAt_univ
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ComplexPointsClassifyMarkedPeriods
covers: 430
status: drafted
drafted_by: writer@claude
---
This theorem says that the complex points of the integral model $M$ of the Harris-Taylor moduli problem are classified by marked period lattices. The proof moves each fact from objects over $\operatorname{Spec}\mathbb{C}$ to the universal object, with the representing property of $M$. Its statement form is [complexPoints_classify_markedPeriods](/entry/complex-points-classify-marked-periods/), which feeds [the complex uniformisation of the generic models](/entry/g-unif-of/).

## Statement

The hypotheses are those of [the statement form](/entry/complex-points-classify-marked-periods/). We explain the conclusion. A *period lattice* $D'$ (`PLat`) is a free $O$-module $\Lambda'$ of finite rank with a nondegenerate alternating form $E'$ for which $O$ acts by adjoints. A *period map* $P \colon \Lambda' \to \mathbb{C}^g$ (`IsPeriod`) is $O$-linear through $\rho$ and injective, with a discrete image that spans $\mathbb{C}^g$ over $\mathbb{R}$, and $E' = \operatorname{Im} H$ on the image for a positive definite Hermitian $H$.

`UnifAt` $(D', t, P, y, e)$ says: the point $y$ lies over $\sigma$, and $e \colon \mathbb{C}^g \to A_y$ is a holomorphic surjective homomorphism with kernel $P(\Lambda')$ (`IsExp`). Also $e$ matches $\rho$ with the $O$-action, the Weil pairing of $e(P a / k)$ and $e(P b / k)$ is $\exp(-2\pi i E'(a,b)/k)$, and the level structure is $\eta(a) = e(P(t a)/N)$.

The class `D.Cls N` $(D', t)$ says that the marking $t \colon \Lambda \to \Lambda'$ comes from a family of similitudes modulo each $n$ prime to $p$ (`Genus`), and that $E' = 2E_1$ with $E_1$ perfect up to an integer prime to $p$ (`HalfPerf`).

**Theorem.** `FineAt` holds for `M.univ.fam h hL`:

1. (`pts`) each $y$ over $\sigma$ has `UnifAt` for some $(D', t, P, e)$ of class `D.Cls N`;
2. (`occ`) each $(D', t)$ of class `D.Cls N` with a period map $P$ has `UnifAt` at some $y$;
3. (`sep`) if `UnifAt` holds at $y$ and $y'$, and an $O$-isometry $w$ of lattices respects the markings mod $N$ and carries $P$ to $P'$ up to a $\mathbb{C}$-linear map, then $y = y'$.

## Proof

1. (`tr`) Let $o$ be an object over $\operatorname{Spec}\mathbb{C}$ with a map $o \to$ `M.univ` over $y$. Then `UnifAt` holds for $o$ at the identity if and only if it holds for `M.univ` at $y$, with the same $(D', t, P)$. This is `unifAt_correspond_of_cartesian`, fed with the cartesian square, the $O$-action, the bundle and the level structure of the map.
2. `pts`. Pull `M.univ` back along $y$ to $o$. `exists_complexUniformisation_harrisTaylor` gives `UnifAt` for $o$ with a class in `D.Cls N`. Step 1 moves it to $y$.
3. `occ`. `exists_harrisTaylor_object_of_period` builds $o$ over $\mathbb{C}$ from $(D', t, P)$. `M.rep` gives the point $y$ that classifies $o$. Step 1 moves `UnifAt` to $y$.
4. `sep`. Pull back along $y$ and $y'$ to $o_1$ and $o_2$. Step 1 gives `UnifAt` for both. `nonempty_moduliMap_of_marked_period_isometry` gives a map $o_1 \to o_2$ over the identity. With $o_2 \to$ `M.univ` over $y'$, both $y$ and $y'$ classify $o_1$. Uniqueness in `M.rep` gives $y = y'$.

The analytic side is the classical theory of complex abelian varieties as tori with a Riemann form (D. Mumford, Abelian Varieties, Chapter I).

## In the Lean code

The theorem is in [ComplexPointsClassifyMarkedPeriods.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ComplexPointsClassifyMarkedPeriods.lean#L20). `PLat`, `IsPeriod`, `UnifAt` and `FineAt` are in [IsHolPeriods.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsHolPeriods.lean#L13), and `Datum.Cls` in [Uniformised.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/Uniformised.lean#L34). The lemmas used are aliases of `Unif.exists_unifAt`, `exists_obj_unifAt_of_period`, `HTIso.nonempty_objMap_of_markedIsom` and `GlobalTheory.unifAt_correspond_of_cartesian`. We have not unfolded their proofs. The theorem needs only $0 < N$, not $N \geq 3$.
