---
id: field-outright
title: The l-adic character of a Hecke character is de Rham, with no hypotheses
kind: theorem
decl: HodgeLocalDeRhamField.HLdR.field_outright
module: Development.WeilBound.CoreStatements.PublishedTheorems.HeckeLAdicCharacters.Outright
covers: 532
status: drafted
drafted_by: writer@claude
---
This theorem proves `HeckeLAdicCharacterDeRham` with no hypotheses. It fills the two hypotheses of [the l-adic character of a Hecke character is de Rham, from two period facts](/entry/field-of-leaves/) with two theorems about Lubin-Tate periods. It has two users, one on each side of [EveryCharacter from the Galois row](/step/every-character/). On the Galois side, `UpperTheory.Gal.TP.Sub.charEx` uses it twice to build a Galois character. On the literature side, `UpperTheory.Lit.heckeLAdicCharacterDeRham` is a second name for it, and the [literature structure](/step/every-character-of-literature/) reaches it through that name. Below this theorem are 532 declarations.

## Statement

Let $E$ be a number field, $\ell$ a prime, $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$ an isomorphism and $\chi$ an algebraic Hecke character of $E$ with infinity type $n$. Let $\mu$ be a continuous $\ell$-adic Galois character attached to $\chi$ through a global Artin map. Then at each finite place $w$, the restriction of $\mu$ to the decomposition group is de Rham, and at each embedding $\tau$ its only Hodge-Tate jump is $-n(\iota \circ \tau)$.

The [parent entry](/entry/field-of-leaves/) states this in more detail. We have not unfolded the predicates `IsdRAt` and `IsJumpsAt`.

## Proof

The proof is one application of `field_of_leaves` to two theorems:

- `LTPer.Tilt.tilt_period` proves `TiltLeaf`. Given Lubin-Tate data for a character of the Galois group of a finite extension $K$ of $\mathbb{Q}_\ell$, it gives a nonzero compatible system $v_n$ in the tilt on which Galois acts through the Lubin-Tate power series. Its statement is the body of `TiltLeaf`, word for word.
- `T.lubin_tate_period_not_filtered` proves `ProductLeaf`: under a norm condition, a pre-period $t_\mu$ is not in $\mathrm{Fil}^2$ when $\mu$ is the inclusion of $K$, and not in $\mathrm{Fil}^1$ otherwise. It is a second name for `LTPer.exact_degrees_of_product`.

The mathematics is in `field_of_leaves` and in these two theorems. This theorem only joins them.

## In the Lean code

The theorem is in [Outright.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/HeckeLAdicCharacters/Outright.lean#L7). The statement `HeckeLAdicCharacterDeRham` is in [HeckeLAdicCharacterDeRham.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/HeckeLAdicCharacterDeRham.lean#L11). The two inputs are in [FrobPowRead.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FrobPowRead.lean#L139) and [LubinTatePeriodNotFilteredStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LubinTatePeriodNotFilteredStatement.lean#L11). The users are in [SubtractHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/SplitLineSubtraction/SubtractHolds.lean#L53) and [HeckeDeRham.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GaloisRepresentations/HeckeDeRham.lean#L3).

The module is in a folder named `PublishedTheorems`, but the proof does not take a published result as a hypothesis. It uses only theorems that the Lean code proves. The file name `Outright` matches this: the theorem has no hypotheses.
