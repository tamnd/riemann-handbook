---
id: exists-is-gauge-of-is-cmext
title: A gauge family of measures for a CM extension
kind: theorem
decl: GlobalTheory.GaugeEx.exists_isGauge_of_isCMExt
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsIsGaugeOfIsCMExt
covers: 496
status: drafted
drafted_by: writer@claude
---
This theorem builds a gauge family: one measure on each adelic unitary group $U(J)(\mathbb{A}_F)$ of a CM extension $E/F$, such that the measures are Haar, do not depend on the choice of basis, and fit together when one removes one vector. It takes the family of [`exists_std_family`](/entry/exists-std-family/) and multiplies it by one constant for each size. [`exists_isGauge`](/entry/exists-is-gauge/) applies it to the CM extension of the data.

## Statement

We use the words of [`exists_std_family`](/entry/exists-std-family/): `IsCMExt`, `IsHermND`, $H_J$, `StdMeas`, step datum and `IsCompatible`. A gauge family $G$ gives a measure $\mu_{M,J}$ on $H_J$ for each $M$ and each $M \times M$ matrix $J$. `G.IsGauge` is the conjunction of three conditions.

1. `IsHaar`: $\mu_{M,J}$ is a Haar measure when $J$ is Hermitian and nondegenerate.
2. `BasisInv`: if $J' = P^* J P$ with $P \in \mathrm{GL}_M(E)$, there is an isomorphism $e \colon H_J \to H_{J'}$ with $g P = P\, e(g)$, and each such $e$ carries $\mu_{M,J}$ to $\mu_{M,J'}$.
3. `StepCompat`: for each step datum $(J, x, \beta, B, J')$ with $M + 1 \ge 3$, there is a character $\psi$ of $\mathbb{A}_F$ with `IsCharAF`. For each such $\psi$ there is a measure $\nu_X$ on the quadric $q_J(y) = \beta$ with `IsXbetaMeasure`. For each such $\nu_X$ there is a frame isomorphism $e$ from the stabilizer of $x$ onto $H_{J'}$. For each such $e$, $\mu_{M+1,J}$ disintegrates as $\nu_X$ times $e^{-1}_*\mu_{M,J'}$ (`IsCompatible`).

**Theorem.** If `IsCMExt F E σ`, then there is a gauge family $G$ with `G.IsGauge`.

## Proof

1. `nonempty_standardLocalHaarMeasures` gives a standard measure package $s$ for a basis of $E$ over $F$.
2. [`exists_std_family`](/entry/exists-std-family/) gives Haar measures $\mu^0_{M,J}$ with `BasisInv`, and constants $\alpha_{M,J} > 0$ that are invariant under $J \mapsto P^*JP$. The pair $\alpha_{M+1,J}\mu^0_{M+1,J}$, $\alpha_{M,J'}\mu^0_{M,J'}$ satisfies the step relation for every product measure $\nu$ on the quadric built from $s$ (`IsStdX`).
3. `quadricFibreMeasure_eq_smul_normalisedProduct` gives $\kappa_M \neq 0$ such that, when $M \ge 1$, a measure $\nu_X$ is an $X_\beta$ measure if and only if $\nu_X = \kappa_M \nu$.
4. `exists_nontrivial_adeleChar_trivial_on_totallyReal` gives a character $\psi$ with `IsCharAF`.
5. Put $K_M = \prod_{i=0}^{M} \kappa_i$ and $\mu_{M,J} = K_M \alpha_{M,J} \mu^0_{M,J}$.

Then `IsHaar` holds, since $K_M \alpha_{M,J} \neq 0$. `BasisInv` holds, since $K_M$ depends only on $M$ and $\alpha$ is invariant. For `StepCompat`, `existsUnique_stdHermitianFibreProduct_of_rank_ge_three` gives the measure $\nu$, and `unitary_stabilizer_anisotropic_vector_equiv_complement` gives the frame isomorphism. By step 3, the only $X_\beta$ measure is $\kappa_{M+1}\nu$. The lemma `isCompatible_smul` multiplies the relation of step 2 by $K_M$ on the subgroup side and by $\kappa_{M+1}$ on the quadric side. Since $K_{M+1} = \kappa_{M+1} K_M$, this is the relation for $\mu$.

## In the Lean code

The theorem is in [ExistsIsGaugeOfIsCMExt.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsIsGaugeOfIsCMExt.lean#L163), with `isCompatible_smul` at [line 34](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsIsGaugeOfIsCMExt.lean#L34). `GaugeFam` and `IsGauge` are in [FrameTransport.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/GeneralLinearActions/FrameTransport.lean#L11). The four lemmas of steps 1, 3 and 4 and of the `StepCompat` check are in `*Statement` files of the same folder; we have not opened their proofs or unfolded `IsCharAF` and `IsXbetaMeasure`.

The character $\psi$ of step 4 is only a witness. The constant $\kappa_M$ in step 3 depends on $M$ alone, not on $J$, $\beta$ or $\psi$. So the gauge measures do not depend on the character.
