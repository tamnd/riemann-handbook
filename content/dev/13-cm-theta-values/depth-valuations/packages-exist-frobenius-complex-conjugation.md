---
id: packages-exist-frobenius-complex-conjugation
title: Packages at the primes where Frobenius is complex conjugation (statement form)
kind: theorem
decl: GlobalTheory.T.packages_exist_frobeniusComplexConjugation
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.PackagesExistFrobeniusComplexConjugationStatement
covers: 319
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`packages_conj`](/entry/packages-conj/), which has the real content. Its one user is [`goodPrime_packages`](/entry/good-prime-packages/), which takes from it two of the seven parts of `PkgSt`: `PkgPhiCSt` and `PkgZeroCSt`.

## Statement

Use the CM field $E$, the host $H$, the datum `Dw`, the level `lv`, the moduli scheme $X$ and the coefficient field $F$ of [the entry for `goodPrime_packages`](/entry/good-prime-packages/). That entry also states the chart statement `UpFSt p` and the predicate `AllPts`.

**Theorem.** Assume `UpFSt p` for all primes $p$. Then for all $E$, $H$, `Dw`, `lv`, $X$, $F$ and each involution on $\mathcal{O}_E$, the statements `PkgPhiCSt X F` and `PkgZeroCSt X F` hold.

Both statements are about the residue characteristics $\ell$ with `PhiC N ℓ`: $\ell$ is in the inert class of the numerical datum $N$, and the invariant `N.hP ℓ` is $0$. Under this condition the shift of places at $\ell$ fixes each place. Then the Frobenius condition of `PlaceTie` gives $\bar\tau(x) \equiv \tau(x)^\ell$ modulo the prime $\lambda$ for each chosen embedding $\tau$: on these embeddings, Frobenius acts as complex conjugation. [The entry for `packages_conj`](/entry/packages-conj/) states the two package statements in full.

## Proof

The proof is one line: `first | exact @GlobalTheory.PkgConj.packages_conj | ...`. The statement is the same as that of `packages_conj`, word for word.

## In the Lean code

The theorem is in [PackagesExistFrobeniusComplexConjugationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PackagesExistFrobeniusComplexConjugationStatement.lean#L9). It calls `GlobalTheory.PkgConj.packages_conj` in [PackagesExistFrobeniusComplexConjugation.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PackagesExistFrobeniusComplexConjugation.lean#L84). `PhiC`, `PkgPhiCSt` and `PkgZeroCSt` are in [DepthNumbersThresholdEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/DepthNumbersThresholdEq.lean#L44). The name fits the content: the fact that Frobenius acts as complex conjugation is what `PhiC` gives to the proof below.
