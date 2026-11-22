---
id: zarhin-geometric-of-semistable-reduction
title: The theta-level extension from semistable reduction (statement)
kind: theorem
decl: GlobalTheory.T.zarhinGeometric_of_semistableReduction
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.ZarhinGeometricOfSemistableReductionStatement
covers: 1258
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`zhGeo_of_semistableReduction`](/entry/zh-geo-of-semistable-reduction/). Its proof only calls that theorem. The real content is two levels lower, in [`ZH.GeoHalf.zhGeo`](/entry/zh-geo/). Several theorems of this volume use it, for example `zh_of_semistableReduction`, `topAmpExists_of_semistableReduction` and `SiegJoin.minor_model`. No single declaration below the top lies on every path to it, so its place in the proof is under [EveryCharacter from the Galois row](/step/every-character/).

## Statement

**Theorem.** If `SemistableReductionSt` holds, then `ZHGeoSt` holds.

`SemistableReductionSt` says this. Let $p$ be a prime, $K$ a finite extension of $\mathbb{Q}_p$ inside a fixed algebraic closure, and $(A, L)$ a polarized abelian variety over $K$ (the structure `PolAV`: an abelian scheme with a rigidified, symmetric, relatively ample line bundle). Then there are a finite extension $K' \supseteq K$ and a semi-abelian scheme $G$ over the integral closure $\mathcal{O}_{K'}$ of $\mathbb{Z}_p$ in $K'$ whose generic fibre is isomorphic to $A_{K'}$ as a group scheme. This is Grothendieck's semistable reduction theorem (SGA 7 I, Exposé IX, Théorème 3.6), in the special case of a polarized abelian variety over a $p$-adic field.

`ZHGeoSt` says that an abelian scheme with a theta structure of level $rN$ over an open set $U_0$ of a normal projective model $Z$ extends to a semi-abelian scheme over $Z$, with a cubical line bundle and theta sections that embed it in projective space. The [entry for `zhGeo`](/entry/zh-geo/) unfolds it.

## Proof

The proof is `zhGeo_of_semistableReduction`.

## In the Lean code

The theorem is in [ZarhinGeometricOfSemistableReductionStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ZarhinGeometricOfSemistableReductionStatement.lean#L14). The proof is the tactic `first | exact @GlobalTheory.zhGeo_of_semistableReduction | ...`. The two statements are identical, so the first `exact` closes the goal. `SemistableReductionSt` is in [SemistableReductionSt.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/SemistableReduction₂/SemistableReductionSt.lean#L15).

The hypothesis is not idle: it goes down to `zhGeo_of`, which uses it. The Lean code also proves it, as `GlobalTheory.SS.semistableReductionSt` in [SemistableReductionPpavPadicField.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/SemistableReductionPpavPadicField.lean#L19), so the callers can remove it.

The name says "Zarhin". The statement does not mention Zarhin, and we do not know what the letters ZH in `ZHGeoSt` stand for.
