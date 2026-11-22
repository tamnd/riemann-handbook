---
id: orbit-entry-bounds-hold
title: The orbit entry bounds from the letter bounds
kind: theorem
decl: Formalism.MainNotions.DIV.Lemmas.OrbitEntryBounds.orbit_entry_bounds_hold
module: Formalism.SharpRestriction.Divisibility.ChainOperators.OrbitEntryBounds
covers: 446
status: drafted
drafted_by: writer@claude
---
This theorem proves the eight orbit bounds `Core` from the local letter bounds `OrbitLetterBoundsAll C6 C`. It is a pass-through: it proves one input of [the orbit entry bounds of a datum](/entry/orbit-entry-bounds-of-family/) and calls that theorem. The real content is in that entry. Its user is step 4 of [the service bounds](/entry/sum-over-primes-service/), with $C_6 = 11$ and $C = 1$.

## Statement

The data $D$, $L$, $X$, $K$, `Dx`, $E$, `ce` and the conditions `ThetaKernelShapeAtD`, `Shape` and `CLarge` are as in [the orbit entry bounds of a datum](/entry/orbit-entry-bounds-of-family/). `OrbitLetterBoundsAll C6 C` says that each admissible local datum `Lo` satisfies `ThmA C` and `Cor2 Lo C6 C`, and that each admissible datum of the second kind satisfies `ThmOne C`.

**Theorem.** If `OrbitLetterBoundsAll C6 C`, `ThetaKernelShapeAtD E Dx`, `Shape D L X E` and `CLarge C6 C K ce` hold, then `Core D L X K Dx E ce C` holds.

## Proof

`PI.OrbBoundF` turns the letter bounds, `Shape` and `CLarge` into `OrbitValuationBound E X K ce`. Then `orbit_entry_bounds_of_family` gives `Core`.

## In the Lean code

The theorem is in [OrbitEntryBounds.lean](lean:Formalism/SharpRestriction/Divisibility/ChainOperators/OrbitEntryBounds.lean#L49). `PI.OrbBoundF` is in [OrbBoundF.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/OrbBoundF.lean#L3) and is a second name for `PI.OrbBoundFW.prvF_of_orbitLetterBounds`.

- The caller gets `OrbitLetterBoundsAll 11 1` from `split_bound_eleven_one`, which proves `SplitConstantsUniformBound 11 1` ([LocalBoundElevenComparison.lean](lean:Formalism/SharpRestriction/Divisibility/JetPolynomialLogs/LocalBoundElevenComparison.lean#L64)). We have not unfolded `ThmA`, `Cor2` or `ThmOne`.
