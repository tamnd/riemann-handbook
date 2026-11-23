---
id: exists-hw-of-fon-of-cmp-of
title: Wach and étale families at every prime, from the local construction
kind: theorem
decl: GlobalTheory.HWL.exists_hwOf_fonOf_cmpOf
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsHwOfFonOfCmpOf
covers: 404
status: drafted
drafted_by: writer@claude
---
This theorem puts the local Wach construction at each prime $l$ together into one family over all primes. It is the target of [the statement entry](/entry/exists-hw-of-fon-of-cmp-of-prime/), which has the same statement. The proof is a choice over primes. The local work is in [the local statement](/entry/exists-local-wach-functor/) and [the layer assembly](/entry/exists-wach/).

## Statement

Let $L$ be a local theory and $A$ an $A_{\mathrm{inf}}$ datum at each prime. Assume `LocTied` and `WachEx` at every prime $l$. Then there are $H$ (`HWOf L`), $F$ (`FonOf L A H`) and a comparison in `CmpOf L A H F`. The statement entry explains these hypotheses.

The types `HWOf`, `FonOf` and `CmpOf` are functions of $l$: at each prime they are `LocHW l (L l)`, `LocFon l (L l) (A l) (H l)` and `LocCmpT l (L l) (A l) (H l) (F l)`.

## Proof

1. Fix $l$. Call `exists_local_wach_functor` with `LocTied` and `WachEx` at $l$. Its third hypothesis is `FaithH (A l)`. The proof gets this from `cyclotomicKernel_tilt_invariants_faithful`, which holds for every $A_{\mathrm{inf}}$ datum with no further hypothesis.
2. This gives, for each $l$, some $H_l$, $F_l$ and a comparison. The tactic `choose` turns these into functions of $l$.
3. The comparison at $l$ is taken with `Nonempty.some`.

`FaithH` says: if $g$ in the Galois group of $\mathbb Q_l$ has cyclotomic character $1$ and fixes every element of $\mathcal O_{\mathbb C_l^\flat}$ that the cyclotomic-kernel part of $G_K$ fixes, then $g \in G_K$. Its proof, `TiltFaithful.faithH`, is about 125 lines and uses axioms of `LocAinf` such as `actC_ext` and `actC_norm`. We have not read that proof in full.

## In the Lean code

The theorem is at [ExistsHwOfFonOfCmpOf.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsHwOfFonOfCmpOf.lean#L10). `FaithH` is in [ConvZero.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ConvZero.lean#L12). The fact is stated in [CyclotomicKernelTiltInvariantsFaithfulStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CyclotomicKernelTiltInvariantsFaithfulStatement.lean#L7) and proved in [CyclotomicKernelTiltInvariantsFaithful.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CyclotomicKernelTiltInvariantsFaithful.lean#L260). The types `HWOf`, `FonOf` and `CmpOf` are in [DataNLoc.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DataNLoc.lean#L1245).
