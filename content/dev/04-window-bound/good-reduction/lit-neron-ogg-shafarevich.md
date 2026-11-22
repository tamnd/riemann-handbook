---
id: lit-neron-ogg-shafarevich
title: The criterion of Néron, Ogg and Shafarevich (second name)
kind: theorem
decl: UpperTheory.Lit.neronOggShafarevich
module: Development.AutomorphicArithmetic.ThetaCorrespondence.GoodReduction.SerreTate
covers: 354
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the criterion of Néron, Ogg and Shafarevich in the namespace `Nos.Nos`](/entry/nos-neron-ogg-shafarevich/), which has the real content. It is the first part of [the theorems of Serre and Tate on good reduction](/entry/serre-tate-good-reduction/).

## Statement

Let $R$ be a discrete valuation ring with perfect residue field $k$ and fraction field $K$, and $I$ an inertia group of $\mathrm{Gal}(K^{\mathrm{sep}}/K)$ above $R$. Let $A$ be an [[abelian variety|R7W03TXRS9]] over $K$. Then these are equivalent:

1. $A$ has good reduction over $R$;
2. $I$ fixes the $m$-torsion of $A$ for each $m$ with $m \neq 0$ in $k$;
3. $I$ fixes the $m$-torsion for infinitely many $m$ with $m \neq 0$ in $k$;
4. $I$ acts trivially on the [[Tate module|4CSMQFTGD8]] $T_\ell(A)$ for some prime $\ell$ with $\ell \neq 0$ in $k$.

The terms are defined in [the parent entry](/entry/serre-tate-good-reduction/). This is Theorem 1 of Serre and Tate (Good reduction of abelian varieties, Ann. of Math. 88, 1968).

## Proof

The proof is one term: `UpperTheory.Lit.Nos.Nos.neronOggShafarevich`. Both have the statement `NeronOggShafarevichSt`.

## In the Lean code

The theorem is at [line 7 of SerreTate.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/SerreTate.lean#L7). Its statement `NeronOggShafarevichSt` is at [line 108 of TateUnramifiedOfTorsionUnramified.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/TateUnramifiedOfTorsionUnramified.lean#L108), as a `List.TFAE` of four Props.

Three declarations use it: `potentialGoodReduction`, `cmPotentialGoodReduction` and `serreTateGoodReduction`, all in the same file. The rename adds no mathematics.
