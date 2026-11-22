---
id: leaf-a6nat-xy7-v2-cut-goal-of
title: Naturality of the cup product, the unit, the first Chern class and the Kummer class
kind: theorem
decl: LateralTheory.E.LeafA6nat_xy7V2Cut.goal_of
module: Development.EtaleCohomology.EtaleSheaves.EtaleFirstChernClassRepresentedByChernCocycle
covers: 366
status: drafted
drafted_by: writer@claude
---
This theorem proves that four constructions in étale cohomology with coefficients $\mathbb{Z}/q(i)$ commute with pullback: the cup product, the unit class, the first Chern class and the Kummer class. Its only use is as [s0](/entry/s0/), which four lines of [the power-sum construction](/entry/s57/) use. Below it are 366 declarations.

## Statement

The spaces $E$, the groups $H^n(E, \mathbb{Z}/q(i))$ and line bundles $L$ are as in [the power-sum entry](/entry/s57/). The generators $g_i(\zeta)$, the resolutions $I_i$ and the cup product are as in [the associativity entry](/entry/cup-product-tensor-holds-of/), and the unit class $1$ is as in [the unit law](/entry/s38/).

The Lean code chooses maps $t_U$ from units on $U$ to degree $0$ sections of $I_1$, compatible with restriction, with $t(\zeta v) = t(v) + g_1(\zeta)$ for each primitive root $\zeta$. Let $\lambda(x)$ be the unit that $L$ gives on a $1$-simplex $x$. Then $c_1(L) \in H^2(E, \mathbb{Z}/q(1))$ is the class of a $2$-cocycle with value $0$ on $0$-simplices, value $d\, t(v)$ on a $1$-simplex $x$ when $v^q = \lambda(x)$, and value $t(v) + t(w) - t(vw)$ on a $2$-simplex with edges $x_{01}, x_{12}$ when $v^q = \lambda(x_{01})$ and $w^q = \lambda(x_{12})$. The Kummer class $\kappa(u) \in H^1(X, \mathbb{Z}/q(1))$ of a unit $u$ on a scheme $X$ is similar, with value $d\, t(v)$ for $v^q = u$. Each class is $0$ if no such cocycle exists.

**Theorem.** For each $q \geq 1$:

1. $f^*(a \cup b) = f^* a \cup f^* b$ for each map $f \colon E \to E'$;
2. $f^* 1 = 1$ if $q$ is invertible on $E'$;
3. $f^* c_1(L) = c_1(f^* L)$ if $q$ is invertible on $E'$;
4. $f^* \kappa(u) = \kappa(f^* u)$ for a map of schemes $f \colon Y \to X$, if $q$ is a unit on $X$.

## Proof

Each class is the class of any cocycle with a local property, and the pullback of such a cocycle has the property again.

1. `LeafNatCup_of cupSpec`. By `cupSpec`, $[\alpha] \cup [\beta]$ is the class of any cocycle that satisfies the Alexander-Whitney formula with $\alpha$ and $\beta$. This formula is about simplices, so it survives pullback.
2. `LeafNatOne_of oneSpec`. The pullback of a unit cocycle is a unit cocycle, and $q$ is invertible on $E$ because each $0$-simplex of $E$ maps to one of $E'$.
3. `etale_first_chern_class_natural_of_spec`. The input `etaleFirstChernClass_represented_by_chern_cocycle` says that the cocycle above exists when $q$ is invertible. Its pullback has the three properties for $f^* L$, because $\lambda$ commutes with pullback (`lineUnit_comp`).
4. `natKum`, a part of `EtaleKummerClassExplicitCocycle.holds_of`. We have not unfolded it.

## In the Lean code

The theorem is in [EtaleFirstChernClassRepresentedByChernCocycle.lean](lean:Development/EtaleCohomology/EtaleSheaves/EtaleFirstChernClassRepresentedByChernCocycle.lean#L43), with `oneSpec`, `etaleFirstChernClass_represented_by_chern_cocycle` and `natKum`. The lemmas are in [LeafNatCupPf.lean](lean:Development/EtaleCohomology/EtaleSheaves/LeafNatCupPf.lean#L71), [LeafNatOnePf.lean](lean:Development/EtaleCohomology/EtaleSheaves/LeafNatOnePf.lean#L37), [FirstChernNaturality.lean](lean:Development/EtaleCohomology/EtaleSheaves/FirstChernNaturality.lean#L52) and [HoldsOf.lean](lean:Development/EtaleCohomology/TateTwists/HoldsOf.lean#L23). `IsKum`, `kumT`, `kum`, `lineUnit` and `c1` are in [PullHlComp.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/PullHlComp.lean#L130). The cocycle description of $c_1$ uses five lemmas on the cochain over edges, triangles and tetrahedra, and `LeafRootLoc_of` on local roots. We have not unfolded them. The module name describes one input, not the theorem.
