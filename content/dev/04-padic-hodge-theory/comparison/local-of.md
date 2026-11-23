---
id: local-of
title: The local comparison on a small chart, from descent
kind: theorem
decl: CrystallineSemistableComparison.B.local_of
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.ZariskiEtaleLifting.SubsingletonH
covers: 661
status: drafted
drafted_by: writer@claude
---
This theorem proves the local form of a comparison between two sites: the thickenings of a chart over $A_{\mathrm{cris}}/\ell^n$, and the points of the chart on the perfectoid side. On one small étale chart of relative dimension $d$, the pullback map on the cohomology of a filtered sheaf is an isomorphism up to a fixed power of the Rees variable, in each degree up to $j$. It takes one hypothesis, the descent statement `D.Out l`, which [`out`](/entry/out/) proves. `main_of` then glues the local statement over an atlas. This leads to [the geometric steps](/entry/steps-holds/), and `HT.Ex.lvl_all` also uses it as `local_of (D.out l)`. Below it are 661 declarations.

## Statement

Fix a prime $\ell$. Let $F$ be a functor of points over a ring $O$ with a map $\kappa \colon O \to \mathcal{O}_{\mathbb{C}_\ell}$, and let $\varepsilon$ be a compatible system of $\ell$-power roots of unity in the tilt, with $\mu = [\varepsilon] - 1$. `F.Small d` is an étale map $O[T_1, \dots, T_d] \to R$, with the $T_k$ units in $R$, such that $R$ represents $F$. For $n \neq 0$, a flag $k$ and a slow function $\rho$ ($\rho(0) = 0$, $\rho(r+1) \leq \rho(r) + 1$), `flt` is a filtration on the thickening site of $F$ over $A_{\mathrm{cris}}/\ell^n$, built from the divided powers, $\rho$ and $\mu$. `gT` is the functor from the site `El` of points of $F$ over $\kappa$ to that thickening site. We have not unfolded `flt`, `Thick` or the Rees module.

**Theorem.** Assume `D.Out l`. For all $d$ and $j$ there is $N$ such that, for all such $F, \kappa, \varepsilon, k, n, \rho$ with $k = \mathrm{false}$ or $\rho = 0$, and $F$ small of dimension $d$: for each $i \leq j$, the pullback along `gT` on $H^i$ of the Rees module of `flt` is injective and surjective up to $X^N$.

Here "up to $s$" (`UpTo`) means: if $f(x) = 0$ then $s x = 0$, and each $s y$ is in the image of $f$.

## Proof

The proof applies the abstract criterion `P.glue d j`. It needs, on both sites, an action of $\mathbb{Z}^d$ (`Act`), a line object `Line` that is acyclic up to $s$, and a map $\theta$ between the two sides that is equivariant for the actions. It also needs descent up to $s$ (`Desc`) and a statement `NI` on $\theta$. It then gives the comparison up to $s^N$. The inputs on the chart:

1. `P.elift` lifts the étale chart to a chart $\mathcal{L}$ over the divided power base, and `exists_dp` (by `dpFlat`) extends the divided powers along the flat map.
2. `P.tower_ex` gives a tower of $\ell$-power roots $c_k(m)$ of the $T_k$ on the perfectoid side, with $c_k(m+1)^\ell = c_k(m)$ and $c_k(0)^\sharp = T_k$.
3. `P.thick_act` acts by $t_k \mapsto q^{a_k} t_k$ on the thickening side, and `P.tower_act` acts by $c_k \mapsto \varepsilon^{a_k} c_k$ on the tower.
4. `P.theta_ex` gives $\theta$ with $t_j \mapsto [c_j(0)]$, and it commutes with the two actions.
5. `P.line_univ` with `P.thick_line`, and `P.cont_line`, give the two lines. `P.local_ni` gives `NI`.
6. `P.desc hD` gives the descent. This is the only use of `hD`.

We have not unfolded `Act`, `Line`, `Acyc1`, `NI` or `Desc`.

## In the Lean code

The theorem is in [SubsingletonH.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/ZariskiEtaleLifting/SubsingletonH.lean#L32). `Local` and `Main` are defined in [MapUSharp.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/ZariskiEtaleLifting/MapUSharp.lean#L134). The criterion `P.glue` is in [FGlue.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/ZariskiEtaleLifting/FGlue.lean#L44). `D.Out` is in [ObFacts.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/WittExactSequences/ObFacts.lean#L73). In the same file as `local_of`, `global_of` at line 69 passes from `F.Small` to `F.Atlas`, and `main_of` at line 155 gets `Main`.
