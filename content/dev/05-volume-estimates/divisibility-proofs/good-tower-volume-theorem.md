---
id: good-tower-volume-theorem
title: A good tower exists and the volume theorem holds (statement form)
kind: theorem
decl: GlobalTheory.T.good_tower_volume_theorem
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.GoodTowerVolumeTheoremStatement
covers: 17797
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [the good tower and the volume theorem](/entry/good-tower-and-volume/), which has the real content, and its proof applies that theorem. Its one user is [`goodTower_volume_of_reduced`](/entry/good-tower-volume-of-reduced/), which builds the six inputs from published statements and passes them in. The two conclusions go to Step 4 of [the Weil bound](/proof/weil-bound/).

## Statement

**Theorem.** Assume the following six statements:

1. `Top.Given`, a conjunction of fourteen statements from the literature;
2. `PtsIntegrableStatement`, the integrability of a fibre sum of densities built from $\log\|s\|$ and hermitian metrics;
3. `AvoidStatement`, prime avoidance in large multidegree for multihomogeneous primes;
4. `Out.WeilSt`, the existence and the basic laws of the Weil pairing on torsion points of a polarized abelian scheme;
5. `Num.FamilyExistsPos`, the existence of local lattice families on Hodge components at good primes;
6. `Cmp.CmpPair`, the invariance of arithmetic intersection numbers under a twist of the Shimura variety.

Then `GoodTowerExistsX` and `VolumeTheoremX` hold: a root tower with a good origin exists, and each good root tower satisfies the six conclusions of the volume theorem.

The [entry of the real theorem](/entry/good-tower-and-volume/) states each hypothesis and each conclusion in more detail.

## Proof

The statement is that of `GlobalTheory.CompanionTheory.Ar.Top.goodTower_and_volume`, and the proof applies it.

## In the Lean code

The theorem is in [GoodTowerVolumeTheoremStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerVolumeTheoremStatement.lean#L26). The proof is

```
first | exact @GlobalTheory.CompanionTheory.Ar.Top.goodTower_and_volume | exact ... | (intros; apply ... <;> assumption)
```

The two statements are written the same way, so the first branch is enough. The file imports `GoodTowerVolumeTheorem` and a dozen statement files, and `import Mathlib` appears twice.
