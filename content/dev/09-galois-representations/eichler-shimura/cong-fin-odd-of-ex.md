---
id: cong-fin-odd-of-ex
title: The congruence statement for odd rank from lacunary weights
kind: theorem
decl: UpperTheory.Gal.Int.Cong.congFinOdd_of_ex
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.CongruenceOddLevel.CongFinOddOfLvLac
covers: 495
status: drafted
drafted_by: writer@claude
---
This theorem proves `CongFinOdd` from `WtLacEx`, the existence of lacunary weights. `CongFinOdd` is the second hypothesis of [coreAll_of](/entry/core-all-of/), and the user of this theorem is [galoisLocalGlobal_of_geometry_lift](/proof/galois-row/). It passes `wtLacEx_holds` as the argument. The theorem is a pass-through. It changes the form of the statement that [congFinG_of_ex](/entry/cong-fin-g-of-ex/) proves, and that entry has the real content. Below it are 495 declarations.

## Statement

**Theorem.** If `WtLacEx` holds, then `CongFinOdd` holds.

`CongFinOdd` is `CongUW4 Odd TyEll (GenOf DGen) WtLac`. `CongFinG` is `CongUWG TyEll (GenOf DGen) WtLac`. The entry [congUWG_of](/entry/cong-uwg-of/) states `CongUWG` in words. `CongUW4` differs from `CongUWG` in three points:

- it has a hypothesis `Rk a` on the rank $a$, here `Odd a`;
- the places of its second finite set $W$ must lie above $\ell$;
- the approximating $U'$ must be generic at the places of $W$ too, and not only at the places of $Z$.

## Proof

The proof is `CongUWG.congUW4 (congFinG_of_ex H) Odd`. The lemma `CongUWG.congUW4` applies `CongUWG` with the set $Z \cup W$ in place of $Z$. This gives genericity at the places of $W$. The extra hypothesis that $W$ lies above $\ell$ is dropped.

## In the Lean code

The theorem is in [CongFinOddOfLvLac.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/CongFinOddOfLvLac.lean#L15). `CongUWG.congUW4` is in [NotApartOfOverPair.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/NotApartOfOverPair.lean#L252). `CongUW4` and `CongFinOdd` are in [LimWU4OfLimWU3.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/LimWU4OfLimWU3.lean#L37), and `CongUWG` and `CongFinG` in [ApartOfNotMem.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/ApartOfNotMem.lean#L12). The lemma `congUW4` takes any predicate `Rk` and never uses the hypothesis `Rk a`. So the congruence holds for every rank $a \geq 1$. The hypothesis `Odd a` does no work here. It gives `CongFinOdd` the same form as `SeedFinOdd`.
