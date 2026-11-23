---
id: fold-okc-holds-of
title: The folding statement from five local steps
kind: theorem
decl: Formalism.L2.SG.Pf.foldOKC_holds_of
module: Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.UnitaryHaarProducts.InHHClosed
covers: 388
status: drafted
drafted_by: writer@claude
---
This theorem proves `FoldOKC`: the Poincaré series data of each Hida setting can be folded over a fundamental domain, with finite multiplicity integrals. It takes five hypotheses and passes them, with three proved facts, to `foldOK_of_steps`. Its only user is [the folding conditions for the Poincaré series](/entry/fold-okc-holds/), which proves the five hypotheses. In the written proof this sits under [the local matching of theta integrals](/step/theta-local-matching/).

## Statement

Fix a Hida setting $X$ and a word $u$. Let $S$, $N$ and $H$ be the groups `SfinU`, `NfinU` and `Hfin` of $u$, with partners at the infinite places. Let $K$ be the set `Kset`. The five hypotheses, for all $X$ and $u$, are:

- `KsetSplit`: if $n \in N_f$ and $nh \in K$, then $h \in K$.
- `UnipotentConjugateInLevel`: for $n \in N_f \cap K$, $x_u^{-1} n x_u$ lies in $K_2$ and $\chi_2$ of it is $\psi_f(n)$.
- `RatLevi`: a rational $\gamma$ in $S$ is $\nu \eta$ with $\nu$ rational in $N$ and $\eta$ in `Gam`.
- `PsiProd`: $\psi_\infty(\nu_\infty)\, \psi_f(\nu_f) = 1$ for rational $\nu$ in $N$.
- `IUnfold`: if `MultPoly`, `WuDecay` and `PhWellDef` hold, then the multiplicity integral of `Ph` over each compact $\Omega$ and fundamental domain is finite.

`FoldOK` says: $S_{rat}$ has a fundamental domain, and there are a compact $\Omega_0 \ni 1$ and $a \ge 0$ such that `Ph` is a fold datum for each compact $\Omega \supseteq \Omega_0$, with finite multiplicity integrals.

**Theorem.** The five hypotheses imply `FoldOKC`: for each $X$, full datum $Y$ and $u$, if the level subgroup is normalized and `WuDecay` holds, then `FoldOK` holds.

## Proof

It calls `foldOK_of_steps` with the five hypotheses and with `foldReadyX_holds`, `sratFund_holds` and `MultPoly_holds`. That lemma proves `PhWellDef` from the first two, then the properties of `Ph`, the finite integrals and the reproducing bound.

## In the Lean code

The theorem is at [InHHClosed.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHClosed.lean#L14). `foldOK_of_steps` is in [InHHAlg.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHAlg.lean#L839). `FoldOK` is in [WuDecay.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/WuDecay.lean#L36). [A polynomial bound on the folding multiplicity](/entry/mult-poly-holds/) gives `MultPoly_holds`. We have not unfolded `IsFoldDatum` or the multiplicity integral.
