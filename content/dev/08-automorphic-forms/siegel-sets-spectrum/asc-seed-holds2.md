---
id: asc-seed-holds2
title: The residual spectrum seed, assembled from local subrepresentations
kind: theorem
decl: PositivityTheory.Rg.Rs.ascSeed_holds2
module: Development.WeilBound.RepresentationTheoryGL.ResidualSpectrum.SliceTensors.AscSeedHolds2
covers: 309
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `AscSeed`. It only passes proved lemmas along. It sits below [the step EveryCharacter](/step/every-character/).

## Statement

Let $E$ be a totally complex number field. `AscSeed` is the conjunction of two statements.

- `AscAll`: a discrete subspace $V$ of automorphic forms on $\mathrm{GL}_N$ over $E$, with regular integral infinitesimal character at some $\tau$ (`RegInt`, not unfolded), has a unitary normalised cuspidal $\pi$ on $\mathrm{GL}_a$ and $d$ with `AscEmb V π d`. `AscEmb` asks $N = ad$ and an embedding of $V$ into forms induced from twists of $\pi$ by powers of $|\det|$ (`spehExp`, not unfolded).
- `Clause3Asc`: in that case, at each finite place $w$, the local component of $V$ is the Speh representation of the local component of $\pi$ (`IsSpeh`: the cosocle of the product of the `spehFactor`s).

The shape matches the description of the residual spectrum by Mœglin and Waldspurger ("Le spectre résiduel de GL(n)", Ann. Sci. ENS 22 (1989)). We have not checked the Lean statement against the paper.

## Proof

The file proves two lines:

- `locSub_holds2 : LocSub` is `LsTop.locSub_of` applied to `restrictAtPoint_holds`, `existsProj2` and `frobRecip_holds`. `LocSub` says that the local component of $V$ embeds in the product of the Speh factors.
- `ascSeed_holds2` is `ascSeed_of_locSub locSub_holds2`. That lemma pairs `ascAll_holds` with `clause3Asc_holds`, which uses `LocSub` and `locDual_holds`.

There is no content in this file beyond these two applications. The content is in `ascAll_holds` and `clause3Asc_holds`, which have no entries of their own in this handbook.

## In the Lean code

The theorem is in [AscSeedHolds2.lean](lean:Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/SliceTensors/AscSeedHolds2.lean#L11). `AscSeed`, `LocSub` and `Clause3Asc` are in [Clause3Asc.lean](lean:Development/WeilBound/RepresentationTheoryGL/ResidualSpectrum/SliceTensors/Clause3Asc.lean#L31). There is no `ascSeed_holds` without the suffix 2.
