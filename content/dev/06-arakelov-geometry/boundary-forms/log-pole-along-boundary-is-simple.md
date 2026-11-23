---
id: log-pole-along-boundary-is-simple
title: The Kodaira-Spencer form has a simple pole along the boundary
kind: theorem
decl: GlobalTheory.LogPole.log_pole_along_boundary_is_simple
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.ExistsSimpleLogPoleAlongBoundary
covers: 320
status: drafted
drafted_by: writer@claude
---
This theorem says that the Kodaira-Spencer form $\omega_0$ on the interior of a flag cover has a pole of order exactly one along the boundary: for each reduced local equation $t$ of the boundary, $t\,\omega_0$ is a local unit. Its one user is the renaming [`T.exists_simple_log_pole_along_boundary`](/entry/exists-simple-log-pole-along-boundary/). The local construction is in [`exists_log_pole_along_boundary`](/entry/exists-log-pole-along-boundary/).

## Statement

Let $E$ be a CM field, with a host, a datum, a level, a moduli space $X_o$ and a coefficient field $F$. Let $Y_0$ be the open part of a toroidal flag cover over the closure of a component $Z$ (`Y₀`), and let $U_0 \subseteq Y_0$ be its dense interior (`U₀`). The boundary is $Y_0 \setminus U_0$. Assume:

1. `Hypotheses''`, a bundle of 17 published statements, and `GrothendieckDeformation`;
2. $F$ is algebraically closed in the function field of each component (`FnAlgClosed`);
3. at each framed point over each field, the tangent vectors correspond one to one to Kodaira-Spencer data (`KSIso`);
4. $Y_0$ is smooth of relative dimension $\dim$ of the flag space, projective and geometrically connected over $F$ (`IsVariety₀`).

Let $K$ be the line bundle of top forms on $Y_0$ and $\mathcal{L}_\kappa$ the automorphic line bundle of the weight $\kappa$ (`FlagTan.kap`). Let $\omega_0$ be a nowhere zero section of $K \otimes \mathcal{L}_\kappa^{-1}$ over $U_0$ with the Kodaira-Spencer normalization (a `CanId`).

**Theorem.** Let $y \in Y_0 \setminus U_0$, $V \ni y$ open, and $t \in \mathcal{O}(V)$ such that the germ $t_z$ is a unit exactly when $z \in U_0$, and $t_z$ divides $f_z$ for each $f$ on an open $W \subseteq V$ that vanishes at all boundary points of $W$. Then there are an open $V' \ni y$ in $V$, charts of $K$ and of the $\mathcal{L}$'s that contain $V'$, and $u \in \mathcal{O}(V')$ with all germs units, such that $t_z \, (\omega_0)_z = u_z$ at each $z \in V' \cap U_0$, where $(\omega_0)_z$ is the germ of the coefficient of $\omega_0$ in the charts.

## Proof

The child lemma gives one reduced equation $\delta$ near $y$ and a unit $u$ with $\delta\,\omega_0 = u$ at all field points of $U_0$. The stalk at $y$ is a domain, because the flag cover is normal. Both $t$ and $\delta$ are reduced equations, so each divides the other in the stalk. Then `exists_unit_mul` gives $t = b\,\delta$ near $y$ with $b$ a unit. An identity at all field points is an identity of sections (`FlagMod.ext_ev_field`). Hence $t\,\omega_0 = b u$.

## In the Lean code

The theorem is in [ExistsSimpleLogPoleAlongBoundary.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ExistsSimpleLogPoleAlongBoundary.lean#L135). The lemmas:

- [`exists_log_pole_along_boundary`](/entry/exists-log-pole-along-boundary/), in the same file.
- `exists_unit_mul` and `ger_ne_zero` in [KodairaSpencerCanonicalDivisor.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KodairaSpencerCanonicalDivisor.lean#L40).

Two hypotheses are never used: `GrothendieckDeformation` and $y \notin U_0$ are both introduced as `_`. So the statement holds at all points of $Y_0$. The same file KodairaSpencerCanonicalDivisor.lean has `simple_pole` ([L240](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KodairaSpencerCanonicalDivisor.lean#L240)), with the same proof text and the bundle `Hypotheses₂` in place of `Hypotheses''`.
