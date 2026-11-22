---
id: all-good-prime-depth-data-exist-proof
title: The packages at all points from the chart statement (statement form)
kind: theorem
decl: GlobalTheory.T.allGoodPrimeDepthDataExist_proof
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.AllGoodPrimeDepthDataExistProofStatement
covers: 3595
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`goodPrime_packages`](/entry/good-prime-packages/), which has the real content. Its one user is [`leafDepthGood_of_chartForm`](/entry/leaf-depth-good-of-chart-form/), which applies it once for each index $j$ to the moduli scheme $X_{\iota(j)}$ and the coefficient field of a core.

## Statement

**Theorem.** Assume `UpFSt p` for all primes $p$. Let $E$ be a CM field, `H` a host datum for $E$, `Dw` a lattice datum, `lv` a level, $X$ a moduli scheme for `Dw` and `lv`, and $F$ a coefficient field for `lv`. Fix an involution on $\mathcal{O}_E$. Then `PkgSt X F` holds.

`PkgSt` is the conjunction of seven package statements, one for each class of good primes, at all integral points of $X$. [The entry for `goodPrime_packages`](/entry/good-prime-packages/) states `UpFSt`, the objects and `PkgSt`.

## Proof

The statement is the same as that of `GlobalTheory.goodPrime_packages`, and the proof applies it.

## In the Lean code

The theorem is in [AllGoodPrimeDepthDataExistProofStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/AllGoodPrimeDepthDataExistProofStatement.lean#L9). The proof is `first | exact @GlobalTheory.goodPrime_packages | ...`, a tactic that tries the alias in three forms, under `set_option maxHeartbeats 1000000`.

The names do not match the files. The theorem with `_proof` in its name is in the file `AllGoodPrimeDepthDataExistProofStatement.lean` and is only an alias. The theorem with the proof, `goodPrime_packages`, is in `AllGoodPrimeDepthDataExistProof.lean`. The name says "depth data", but the conclusion is `PkgSt`. Its packages, for example `RF.PkgInert` in [RestNonneg.lean](lean:Formalism/LocalToGlobal/CharacterGerms/RestNonneg.lean#L59), are records with a row family, a set of representatives, weights and two reals $T$ and $\nu$. We read them only to that level.
