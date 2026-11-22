---
id: u-pre-of-boundary-point-rigid
title: A tautological chart with boundary equations at each boundary point
kind: theorem
decl: GlobalTheory.UCanon.uPre_of_boundary_pointRigid
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTripleChartUnitaryBoundaryPointRigid
covers: 1048
status: drafted
drafted_by: writer@claude
---
At each boundary point $x$ of the blow-up $S$ of [`rigidForFan_of_uStB`](/entry/rigid-for-fan-of-u-st-b/), this theorem gives a formal chart through $x$ with a degenerating family, and the equations of the boundary and of the divisor $B$ in it. This is the condition `UPre` at $x$. It proves [the statement form](/entry/exists-triple-chart-unitary-boundary-point-rigid/), which goes up to `rigidForFan_of_uStB`.

## Statement

Use the data and the hypothesis `UPoinOnX` of [`rigidForFan_of_uStB`](/entry/rigid-for-fan-of-u-st-b/), with $p + q \geq 1$, `IsPolFan` and `NoSelfInt`.

A *monomial family* (`MonoFam`) over a local domain $R$ is a semi-abelian scheme over $\operatorname{Spec} R$ with $\mathcal{O}_E$-action and a uniformization (`PELUnif`), whose generic fibre is classified by a point of $X_F$, with elements $s_1, \dots, s_m$ of the maximal ideal and forms $\delta_i$ in a cone of $\varphi$, and with monomial periods. We have not unfolded `PELUnif` or `IsMonomial`.

Assume `SepB`. Take a monomial family $C$ over a local domain $V$ of the class `Mum.Base`, and $\xi \colon \operatorname{Spec} V \to S$ that extends its generic point. Extend the $s_i$ by units $s_{m+1}, \dots, s_{m+n}$, and the $\delta_i$ to a basis of balanced forms, with matching monomial periods (`TauIn`). Take a geometric point $\mathrm{ev} \colon V \to K$ over $\xi(\text{closed point})$, defined over an algebraically closed subfield $k_0$. Then (`SepAtB`):

- $\mathrm{ev}(s_i) = 0$ for $i \leq m$;
- the abelian part of the degeneration at $\mathrm{ev}$ comes from an abelian scheme over $k_0$;
- if the family comes from a base whose image under $\mathrm{ev}$ lies in $k_0$, then so does each $\mathrm{ev}(s_{m+i})$.

**Theorem.** Let $x \in S \setminus j(X_F)$. Then there are a field $k$, integers $m, e$, a monomial family $C$ over $R = k[[t_1, \dots, t_m, u_1, \dots, u_e]]$, a map $\xi \colon \operatorname{Spec} R \to S$ and $a_1, \dots, a_m \in \mathbb{N}$ with:

1. `IsTaut`: $s_i = t_i$; over $R[1/t_1 \cdots t_m]$ the family is classified by a map to $X_F$; first-order rigidity (`IsRigid`), point rigidity (`PointRigid`), `Inj` and a finite type condition on the residue field; units and forms that extend the coordinates as in `SepB`; and $m + e + \operatorname{trdeg}_F k = \dim D$;
2. the generic point of $C$ followed by $j$ factors through $\xi$, and $\xi$ sends the closed point to $x$;
3. $\mathcal{O}_{S,x} \to R$ is flat, $\mathfrak{m}_x R = \mathfrak{m}_R$, and the residue extension is finite;
4. the ideal of $S \setminus j(X_F)$ pulls back to $(t_1 \cdots t_m)$, and a prime $\mathfrak{p}$ of $R$ maps into $j(X_F)$ if and only if $t_1 \cdots t_m \notin \mathfrak{p}$;
5. $a_i = d\,\varphi(M'\delta_i)$, with $M'$ the integer `l.M'` of the level, and the ideal of $B$ pulls back to $(\prod_i t_i^{a_i})$.

## Proof

1. `T.exists_pointRigid_tautological_chart_unitary_boundary`, proved by [`exists_tautB_chart_at`](/entry/exists-taut-b-chart-at/), gives parts 1 and 2 in the stronger form `IsTautB`: `IsTaut` with point rigidity in the extended coordinates (`HasRigidCoords`).
2. `T.tautologicalChart_isEtaleCompletion_localRing` gives part 3.
3. `T.tautologicalChart_boundary_equations` gives parts 4 and 5.

The proof packs these into `UPre` and drops `HasRigidCoords`.

## In the Lean code

The theorem is in [ExistsTripleChartUnitaryBoundaryPointRigid.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTripleChartUnitaryBoundaryPointRigid.lean#L14). `UPre` and `IsTaut` are in [ExistsMonoFamNontrivial.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsMonoFamNontrivial.lean#L156), `SepB` in [FromBaseAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FromBaseAlt.lean#L45), `IsTautB` in [HasRigidCoords.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasRigidCoords.lean#L126). The three lemmas wrap `UCanon.exists_tautB_chart_at`, `TautEtaleB.tautB_isEtaleCompletion` and `UCanonBd.boundary_eq`.

Part 3 is `IsEtaleCompletion` ([IsProperToroidalModelStructureMap.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsProperToroidalModelStructureMap.lean#L347)). The name says more than the definition: it does not ask that $R$ be the completion of an étale neighbourhood. The hypotheses $p + q \geq 1$, `IsPolFan` and `NoSelfInt` are only passed on to the three lemmas.
