---
id: aprime-inf-of-grp
title: The archimedean orbit constant, from the group chart and the Jacobian at each place
kind: theorem
decl: PI.AprimeInfAsm.aprimeInf_of_grp
module: Formalism.PeriodIntegrals.UnitaryGroupMassFormula.ArchimedeanOrbitMeasures.Assembly
covers: 468
status: drafted
drafted_by: writer@claude
---
This theorem proves `AprimeInf`, the value of the constant $a'$ in the disintegration of the Haar measure of $G_\infty$ along the orbit of a frame. It reduces it to four inputs: compact stabilizers, a volume limit for a chart of the group, the Lebesgue form of the measure on Hermitian matrices, and a Jacobian at each real place. Its caller [`aprimeInf_of_hinfCompact`](/entry/aprime-inf-of-hinf-compact/) proves the last three and states `AprimeInf` in full.

## Statement

Keep the notation of [`aprimeInf_of_hinfCompact`](/entry/aprime-inf-of-hinf-compact/). Let $Y_0$ be the frame of $u'$, and let $\mu_\infty$, $\nu_\infty$ be the self-dual measures on tuples and on Hermitian matrices of size $2r+1$ at infinity. The hypotheses are:

- `HinfCompact`: each stabilizer $H_\infty(u)$ is compact.
- `GrpStd`: for a standard conjugation $c$, a set $S_v$ of indices at each place, and a linear isometry $L$ from a Euclidean space onto the matrices $M_v$ with $M_v^* J_v + J_v M_v = 0$ and $(M_v)_{ij} = 0$ for $i, j \in S_v$, the chart $\kappa_0$ built from $c$ and $L$ satisfies `GrpLim`: $\mu_G(\mathrm{Tube}(\kappa_0(B_\rho)))/\operatorname{vol}(B_\rho)$ tends to a fixed value `gVal X` as $\rho \to 0$.
- `NuBridge`: there are orthonormal real coordinates on the Hermitian matrices at all infinite places in which $\nu_\infty$ is Lebesgue measure.
- `PlaceJacAll`: a statement of linear algebra. Let $w_v$ be an $n \times m$ matrix with zero rows in $S_v$ and $w_v^* J_v w_v$ invertible, let $c_v$ be unitary for $J_v$, and let $L$, $H$ be isometries onto the Lie algebra complement and onto the Hermitian $m \times m$ matrices. Then the real linear map
$$(z_1, z_2) \mapsto \Bigl(c_v\bigl(L(z_1)_v w_v + \tfrac12 w_v (w_v^* J_v w_v)^{-1} H(z_2)_v\bigr)\Bigr)_v$$
is an isomorphism, and it multiplies Lebesgue measure by $\prod_v 2^{nm} / \lvert \det(w_v^* J_v w_v) \rvert^{\lvert S_v \rvert}$.

**Theorem.** These four hypotheses imply `AprimeInf`.

## Proof

1. `lamDet_of_open` gives `LamDet`. It calls `lamDet_of` with `NuBridge`, `PlaceJacAll` and five proved facts: `betaIso_holds`, `muBridge_holds`, `dKForm_holds`, `rowsZ_holds` and `detT_holds`. `LamDet` says that the linear map `LamMap`, built from the derivative at $0$ of the orbit map `KapOrb`, multiplies Lebesgue measure by a constant $D > 0$, with $\sqrt{\lvert \det M \rvert}/(D c_\nu) = $ `tVal X u'` for the matrix $M$ = `matI X`.
2. `tupStd_of_sm` with `kapSm_holds` (the orbit map is $C^1$ at $0$) turns `LamDet` into `TupStd`: a chart of the tuples that satisfies the Jacobian condition `TupJac`.
3. `aprimeInf_of_std` combines `GrpStd` and `TupStd` into `GoodChartEx` by `goodChartEx_of_witt`.
4. `aprimeInf_of_good` builds `JacOneC` from the charts and closes with `aprimeInf_of_leaves`. Compactness of $H_\infty$ is used there through `pushLFin_of_compact`, `orbUniq_of_compact`, `fibOrbAt_of_compact`, `pushCont_of_compact` and `hinfFin_of`.

We have not unfolded the proofs of steps 3 and 4.

## In the Lean code

The theorem is in [Assembly.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/Assembly.lean#L47). The hypotheses are stated in [GoodChartExOfStd.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/GoodChartExOfStd.lean#L52) (`GrpStd`) and [LamCut.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/LamCut.lean#L26) (`NuBridge`, `PlaceJacAll`). `GrpLim` is in [JacGlue.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/JacGlue.lean#L21).

The lemmas it calls:

- `lamDet_of_open` and `aprimeInf_of_std`, in the same file;
- `tupStd_of_sm` in PolarMapContDiffAtBase.lean;
- `kapSm_holds` in ContinuousThetaInf.lean.

The hypotheses `GrpStd`, `NuBridge` and `PlaceJacAll` are proved in the code, so the theorem is a step of assembly with no hypothesis left open.
