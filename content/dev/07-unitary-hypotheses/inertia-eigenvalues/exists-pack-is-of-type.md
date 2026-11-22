---
id: exists-pack-is-of-type
title: A tame Breuil-Kisin module for each good lattice
kind: theorem
decl: GlobalTheory.BKGal.exists_pack_isOfType
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsBreuilKisinModuleTameDescentGoodLattice
covers: 1017
status: drafted
drafted_by: writer@claude
---
This theorem attaches to each good lattice a Breuil-Kisin module with a tame descent datum, and it controls the type of that module. It is the proof behind the wrapper [`exists_breuilKisinModule_tameDescent_goodLattice`](/entry/exists-breuil-kisin-module-tame-descent-good-lattice/), which [`liftF_of_isGood`](/entry/lift-f-of-is-good/) calls once for each lattice of a short exact sequence.

## Statement

The setting is that of [`liftF_of_isGood`](/entry/lift-f-of-is-good/): a prime $\ell \ne 2$, $e + 1 = \ell^a$, a coefficient field $L$ that contains the unramified extension of degree $a$ and a primitive $e$-th root of unity, a system of roots $\varpi$, the tame field $K_\varpi$, and standard period rings. A lattice $T$ of $G_{\mathbb{Q}_\ell}$ is *good* for $(\Sigma, U)$ (`IsGood`) if it is crystalline over $K_\varpi$, of tame type $\Sigma$, and has its Hodge-Tate jumps in $U$.

A *pack* (`Pack`) with heights $(\eta, H)$ for $T$ has four parts:

1. a rank $n$;
2. a datum `BKDat`. This is a $\varphi$-module $P$ over power series with coefficients in $\mathcal{O}_L$ (one matrix for each $i \in \mathbb{Z}/a$, invertible after $E = X^e + \ell$ is inverted), with a descent datum for the tame Galois group, a connection that preserves the module, and two height conditions. With $M$ the module and $L$ the span of the columns of the matrices, they are $E^H M \subset L$ and $E^\eta L \subset M$;
3. a datum `GalDat`: an identification of $P$ with $T$ over Witt vectors, a comparison with $T \otimes B$, and conditions of Galois descent, stability and horizontality;
4. the property `IsBK`: the identification restricted to $G_{K_\varpi}$ comes from a prismatic F-crystal.

The pack is *of type* $(\Sigma, U)$ (`IsOfType`) if the characters of the descent datum lie in $\Sigma$ and the jumps of $P$ lie in $U$.

**Theorem.** Assume `BhattScholzeCrystallineLattices` and `FontaineBcris`. Let $U \subset [-\eta, H]$. Then each lattice $T$ that is good for $(\Sigma, U)$ has a pack with heights $(\eta, H)$ of type $(\Sigma, U)$.

## Proof

1. `nonempty_crysBKFunctorOL_of_bhattScholze` turns `BhattScholzeCrystallineLattices` into a functor $F$ (`CrysBKFunctorOL`). It sends each lattice of $G_{K_\varpi}$ that is crystalline to a Breuil-Kisin module (`BKMod`) with the property `IsBK`. Apply $F$ to the restriction of $T$. This gives $n$, $P$, the identification and `IsBK`.
2. `integralConnection_taylorFormula_tameBreuilKisin` (uses $\ell \ne 2$) gives a connection that preserves the module.
3. `breuilKisin_bcris_comparison_frobenius_naturality` gives the comparison with $T \otimes B$. `galois_fixes_crystalline_image_descentDatum` gives horizontality.
4. `breuilKisin_tensorAinf_galoisStable_kummerFixed`, `kummerTowerGalois_preserves_breuilKisinModule` and `exists_galoisDescentDatum_and_stable` give the descent datum and stability.
5. `breuilKisin_lattice_stable_and_hodgeTate_jumps` (uses `FontaineBcris`) gives the condition `EN_mem` (the operator $E N$ maps $M$ into a submodule `Man`, which we did not unfold) and, with the jump part of `IsGood`, that the jumps lie in $U$. With $U \subset [-\eta, H]$, `PhiMod.jumps_subset_Icc_iff` gives the two height conditions.
6. `tameInertiaCharacters_subset_tameType` and the tame type part of `IsGood` give that the characters lie in $\Sigma$.
7. These parts make up `BKDat` and `GalDat`, and so the pack.

## In the Lean code

The theorem is in [ExistsBreuilKisinModuleTameDescentGoodLattice.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsBreuilKisinModuleTameDescentGoodLattice.lean#L21). `Pack` and `GalDat` are in [IsPotential.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsPotential.lean#L130), and `BKDat` and `IsOfType` in [ExistsAlgebraMapEqRoot.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ExistsAlgebraMapEqRoot.lean#L14). Each lemma in the proof is imported from a "Statement" file. We did not open their proofs, and we did not unfold `IsStd`, `IsCrisCmp`, `IsGalDesc` or `IsHoriz`. $H$ enters only through $U \subset [-\eta, H]$.
