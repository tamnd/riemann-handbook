---
id: root-flat-on-hodge
title: A flat section of near record height on each root model
kind: theorem
decl: RootFieldNumerics.rootFlatOnHodge
module: Development.WeilBound.CoreStatements.FlagImmersions.GlobalModelTowerFinalCondition
covers: 359
status: drafted
drafted_by: writer@claude
---
This theorem proves `RootFlatOnHodge`: on a root model over a global model, each CM type carries a flat section whose height is close to a record value. Its proof joins six proved ingredients through `rootFlatOnHodge_of`. Its one user is [`global_model_tower_final_condition`](/entry/global-model-tower-final-condition/), which applies it to each component of a good tower.

## Statement

Let $E$ be a CM field, abelian over $\mathbb{Q}$, with host datum $H$, and let $D$ have signature $(p,q)$. Let $\mathrm{rd}_E = |d_E|^{1/[E:\mathbb{Q}]}$, and let $L_H = \operatorname{Re} L'(1,\chi)/L(1,\chi)$ for the quadratic character $\chi$ modulo the prime $d_H$.

A *flat root datum* $R$ on a root model $M$ at a CM type $\tau$ (`RootFlat M τ`) consists of a number field $F$ with an embedding into the field of $M$, a smooth hermitian line $A$ with $\deg A = \sum_i \deg x_{\tau,i}$, a flat section $s$ of $A$ over $F$, and smooth functions $v_t$, invariant under scaling each block, with $\prod_i h_{x_t(\tau,i)} = h_A e^{-v_t}$ for $t > 0$ and an integral of $v_t$ that tends to $0$ as $t \to 0^+$. Its height is the height of $s$. We have not unfolded `FlatHerm` or the integral `ptsIntegral`.

A real $h$ is *near record* for $N$, a finite set $\mathcal{B}$ of primes, $\mathrm{rd}$ and $L$ (`NearRecord`) if $h = h_{\mathrm{rec}} + \sum_{\ell \in \mathcal{B}} d_\ell$ with $|h_{\mathrm{rec}}| \le N(\tfrac32 \log \mathrm{rd} + |L|/2)$, and there are $v_\ell \ge 0$ with $|d_\ell| \le (N/(\ell-1) + N v_\ell)\log \ell$ and $\sum_{\ell \in \mathcal{B}} v_\ell \log \ell \le \log \mathrm{rd}$.

**Theorem.** Assume `FlatDegree` (proved in [`flatDegree`](/entry/flat-degree/)) and `Given`. Let $Y$ be a global model, $M$ a root model of length $p + q$, and $o$ a root origin of $M$ over $Y$ whose Hodge component is Hodge-Tate free at its primes (`OmVB`). Let $\mathcal{B}$ be the set of primes dividing $2 d_E M'_l$, where $M'_l$ is a positive integer attached to the level $l$ (an lcm, not unfolded). If $p, q \ge 1$, then for each $\tau$ there is a flat root datum on $M$ at $\tau$ whose height is near record for $p + q$, $\mathcal{B}$, $\mathrm{rd}_E$ and $L_H$.

## Proof

The proof applies `rootFlatOnHodge_of` to six ingredients, each proved in its own file.

1. `CptEx` gives a clopen irreducible component $U$ of $Y$ with the generic point of the Hodge component.
2. `exists_norms` builds adelic log norms on $U$ from `Given`, `FlatDegree`, `PeriodOf` (the points of $U$ are periods of a uniformization) and `ChiEx` (a Kronecker character $\chi$ with $\operatorname{Re}\log\Omega(E,\chi) = \gamma + \log 2\pi - \log \mathrm{rd}_E - L_H$).
3. `core` uses `SmoothLine`, `LocalCmp`, `Numerics` and `FarguesHodgeTate`. `LocalCmp` compares the local norms with valuations: exactly at $\ell \notin \mathcal{B}$, and with error $(p+q)(c_\ell \log \ell - \log\|\cdot\|)$ at $\ell \in \mathcal{B}$, where $c_\ell = 1/(\ell-1)$ and $c_2 = 2$. `Numerics` turns these comparisons and the degree $\tfrac{p-q}{2}(\gamma + \log 2\pi - \log \mathrm{rd}_E - L_H)$ into the near record bound. `local_system_split_fibres` gives the fibres outside $\mathcal{B}$.
4. `flat_herm_root_line_degree`, with the part `PB.Inputs` of `Given`, packs the section into a flat root datum.

## In the Lean code

The theorem is in [GlobalModelTowerFinalCondition.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/GlobalModelTowerFinalCondition.lean#L28). The assembly is in [RootFlatOnHodgeOf.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/RootFlatOnHodgeOf.lean#L30), the six statements in [FibSandwich.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/FibSandwich.lean#L23), and the target in [NearRecordOfValue.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/NearRecordOfValue.lean#L13). `LocalCmp` is itself built from `PointEx`, `ValuePhi`, `IntFrames` and `FibSandwich`.
