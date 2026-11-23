---
id: unitary-compactification-exists-boundary-ideal
title: A boundary ideal on an integral compactification, stated
kind: theorem
decl: GlobalTheory.T.unitaryCompactification_exists_boundary_ideal
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnitaryCompactificationExistsBoundaryIdealStatement
covers: 460
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`uIdealSt_holds`](/entry/u-ideal-st-holds/). [The normalized blowup with separation](/entry/u-poin-st-x-sep/) cites it in step 2, where it gives $d$ and the boundary ideal $J_0$ that is blown up. Below it are 460 declarations.

## Statement

The statement is the proposition `UIdealSt`.

**Theorem.** Let $E$ be a CM field and $H$ a host. Take a datum of signature $(p, q)$ with $p + q \geq 1$. Let $\varphi$ satisfy `IsPolFan` for $\min(p, q)$. Let $X$ be the moduli scheme at a level, with coefficient field $F$, and let $Z_o$ be an integral compactification (`UCompact`) with the map $i \colon X_F \to Z_o$. Then there are $d \geq 1$ and an ideal sheaf $J$ on $Z_o$ such that:

1. the support of $J$ misses $i(X_F)$;
2. $J$ has the valuations of $d\varphi$ (`UValOn`): for every complete discrete valuation ring $W$ with uniformizer $\varpi$, every map $\chi \colon \operatorname{Spec} W \to Z_o$ whose generic point comes from $X_F$, and every form $\beta$ of a monomial degeneration at $\chi$, the pullback of $J$ along $\chi$ is $(\varpi^n)$ with $n = d\,\varphi(\beta)$.

[The proof entry](/entry/u-ideal-st-holds/) says more on `UValOn`.

## Proof

The proof is the term `GlobalTheory.UPoinc.uIdealSt_holds`.

## In the Lean code

The theorem is in [UnitaryCompactificationExistsBoundaryIdealStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryCompactificationExistsBoundaryIdealStatement.lean#L13). The proof is `first | exact @GlobalTheory.UPoinc.uIdealSt_holds | ...`. `UIdealSt` is in [ExistsRatPointOfFiniteType.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsRatPointOfFiniteType.lean#L533). It asks only `IsPolFan`, not `NoSelfInt`.
