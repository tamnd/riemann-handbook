---
id: toroidal-for-fan-ks-of-rigid-for-fan
title: Rigid boundary charts give the log Kodaira-Spencer isomorphism
kind: theorem
decl: GlobalTheory.RigChart.toroidalForFanKS_of_rigidForFan
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ToroidalFanKodairaSpencerOfRigidBoundaryCharts
covers: 2265
status: drafted
drafted_by: writer@claude
---
This theorem turns the statement `RigidForFan` (a toroidal model for each fan, with rigid charts at the closed boundary points) into the statement `ToroidalForFanKS` (the same model, with the log Kodaira-Spencer isomorphism). It proves [the statement form](/entry/toroidal-fan-kodaira-spencer-of-rigid-boundary-charts/). Above that, [`toroidalForFanKS`](/entry/toroidal-for-fan-ks/) applies it to [`rigidBoundaryChartsForFan_unitaryDatum`](/entry/rigid-boundary-charts-for-fan-unitary-datum/), and the literature layer uses the result as `toroidal_for_fan_ks_of_literature` (see [the step](/step/every-character-of-literature/)). The proof only moves data; the content is in [`hasLogKS`](/entry/has-log-ks/).

## Statement

Fix a CM field $E$ with `Host E`, a hermitian datum $D$ of signature $(p, q)$ with $p + q \geq 1$, and an invariant function $\varphi$ with `IsPolFan` and `NoSelfInt` in rank $\min(p, q)$. Fix a level $l$, the moduli scheme $X^\circ$ and a coefficient field $F$. Both statements below quantify over all of these.

`RigidForFan` says: there are a model $Y$ of $X^\circ_F$ over $F$ (`Model`: a normal flat projective $F$-scheme $Y$ with a dense open immersion of $X^\circ_F$ and a semi-abelian scheme $G$ with $\mathcal{O}_E$-action and cubical structure, abelian exactly on $X^\circ_F$), effective Cartier data $B$ on $Y$ and integers $d, k \geq 1$, such that

1. $Y$ is smooth over $F$ of relative dimension $\tfrac{[E:\mathbb{Q}]}{2} p q$;
2. the boundary $Y \setminus X^\circ_F$ is a simple normal crossings divisor (`Snc`);
3. the support of $B$ lies in the boundary;
4. each boundary point has a chart of type $\varphi$, $B$, $d$ (`HasChartOf`);
5. if $\det \omega$ is a line bundle, then the polarization `polOf Y k B` is ample;
6. each closed boundary point has a rigid chart (`HasRigidChart`).

`ToroidalForFanKS` says the same with clause 6 replaced by `HasLogKS` for $G$ over $Y$ with interior $X^\circ_F$: on each framed affine open, the Kodaira-Spencer map is an isomorphism from log derivations onto balanced symmetric matrices. See [`hasLogKS`](/entry/has-log-ks/) for the full statement.

**Theorem.** `RigidForFan` implies `ToroidalForFanKS`.

## Proof

Fix the data and take $Y, B, d, k$ and the six clauses from `RigidForFan`. Keep $Y, B, d, k$ and clauses 1 to 5. For the new clause, apply `logKodairaSpencer_iso_smooth_snc_toroidalModel` to $Y$ with $p + q \geq 1$, clause 1, clause 2 and clause 6. The rest is bookkeeping.

## In the Lean code

The theorem is in [ToroidalFanKodairaSpencerOfRigidBoundaryCharts.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ToroidalFanKodairaSpencerOfRigidBoundaryCharts.lean#L16). `RigidForFan` is in [RigidForFan.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RigidForFan.lean#L70) and `ToroidalForFanKS` in [ToroidalCompactificationBis.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/ToroidalCompactificationBis.lean#L45). It calls one lemma, [`logKodairaSpencer_iso_smooth_snc_toroidalModel`](/entry/log-kodaira-spencer-iso-smooth-snc-toroidal-model/). Clauses 3, 4 and 5 pass through unused. The rigid charts are used only at the closed points of the boundary.
