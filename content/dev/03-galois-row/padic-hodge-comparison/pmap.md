---
id: pmap
title: The period map for smooth models with tautological lines
kind: theorem
decl: CrystallineSemistableComparison.Pb.pmap
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.PerfectoidPullbacks.SumCoord
covers: 360
status: drafted
drafted_by: writer@claude
---
This theorem builds the period map `PMap` for smooth models, with the tautological lines as line data. It is part 3 of [`pSeam`](/entry/p-seam/), and it is the part with content. Most fields come from one existing map $\kappa$. The new work is the Chern class field `c1`: the $d$-th power of a first Chern class pairs to a unit of $B_{\mathrm{dR}}^+$. That field uses [the nonvanishing of $c^d$](/entry/pow-k-ne-zero/). Below it are 360 declarations.

## Statement

Let $\ell$ be a prime and $K$ finite over $\mathbb{Q}_\ell$. Let `per l K` be the period data: $A_{\mathrm{cris}}$, $B_{\mathrm{dR}}$, the image $P$ of $B_{\mathrm{dR}}^+$, and the map $o \colon K \to B_{\mathrm{dR}}$. For a smooth model $M$ with a tautological line $a$, let $H^j(a)$ be the $A_{\mathrm{cris}}$-module of the line data `dat Amp`. We have not unfolded it. A `PMap` gives additive pairings
$$\kappa_a \colon H^j(a) \to \mathrm{Hom}\bigl(\mathrm{Hom}_K(H^j_{\mathrm{dR}}(M_K), K),\ B_{\mathrm{dR}}\bigr),$$
with `HdR` written as $H^j_{\mathrm{dR}}$. It also gives a cup product `cupR` on `HdR`. The fields say: `HdR` is finite-dimensional and its filtration `FilR` is bounded; `cupR` respects `FilR`; $\kappa$ is linear in both sides, commutes with the Galois action and with pullback, respects the filtrations, and takes cup products to `cupR`. The last field `c1`: for $M$ connected of dimension $d$, there are $x$, $z$ and $\varphi$ with $x$ a first Chern class (`c1H`), $z = x^d$, and $\kappa_a(z)(\varphi)$ a unit of $B_{\mathrm{dR}}^+$.

**Theorem.** For $K$ finite over $\mathbb{Q}_\ell$, a `PMap Model.Sm (dat Amp)` exists.

## Proof

`crystalline_deRham_firstChern_exists` gives a map $L$ with $\kappa$ and its linearity, Galois, naturality, filtration and cup fields. It also gives `hL`: for a first Chern class $x$ of $a$ and a de Rham first Chern class $c$ of the line on $M_K$, $\kappa(x)(\varphi) = o(\varphi(c))$. The fields `cupR`, `fin`, `top` and `cupR_fil` come from `cupR`, `m_fin`, `m_top` and `cupR_fil`. The `cup` field is `L.cup` after `cupR_eq`.

For `c1`, let $M$ be connected of dimension $d$.

1. `isTwistingSheaf_pullback` shows that the line on $M_K$ is tautological.
2. `firstChern_acris_family_exists` gives $x$, and `isFirstChernDeRham_exists` gives $c$.
3. `pow_ex` gives $z = x^d$.
4. By `powK_ne_zero`, $c^d \neq 0$. `Module.Projective.exists_dual_eq_one` then gives $\varphi$ with $\varphi(c^d) = 1$.
5. `kap_pow` proves $\kappa(x^k)(\varphi) = o(\varphi(c^k))$ by induction on $k$, with `hL`, the cup field, and the sum over bases `sum_coord`.

So $\kappa(z)(\varphi) = o(1) = 1$, a unit.

## In the Lean code

The theorem is in [SumCoord.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/SumCoord.lean#L58). `PMap` is in [ThetaSetupAlgebraMaps.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/BocksteinBaseChange/ThetaSetupAlgebraMaps.lean#L147). The map $L$ comes from [CrystallineDeRhamFirstChernExists.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/LevelChainValuations/CrystallineDeRhamFirstChernExists.lean#L29). The property of `hL` is named `LieComplementChartContDiffAt`, in [LieComplementChartContDiffAt.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/LieComplementChartContDiffAt.lean#L20). The name has no relation to its content.
