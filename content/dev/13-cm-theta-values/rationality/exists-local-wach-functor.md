---
id: exists-local-wach-functor
title: Statement of the local Wach construction at one prime
kind: theorem
decl: GlobalTheory.T.exists_local_wach_functor
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsLocalWachFunctorStatement
covers: 394
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It has the same statement as [the layer assembly](/entry/exists-wach/), and its proof only points to it. [The family over all primes](/entry/exists-hw-of-fon-of-cmp-of/) calls it once for each prime.

## Statement

Fix a prime $l$, a local datum $P$ (`LocPrime l`) and an $A_{\mathrm{inf}}$ datum $A$ (`LocAinf l P`). Assume:

1. `LocTied`: the period rings of $P$ are isomorphic to $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$, compatibly with their structure.
2. `FaithH`: an element of $G_{\mathbb Q_l}$ in the cyclotomic kernel that fixes the right elements of the tilt lies in $G_K$.
3. `WachEx`: every étale layer has a Wach lattice.

**Theorem.** There are $H$ (`LocHW l P`), a family of Wach modules over every good triple $(K, s, L')$, then $F$ (`LocFon l P A H`), étale modules over the same triples, and a comparison in `LocCmpT l P A H F`.

A triple is good (`Good K s L'`) when $s \geq 1$, $s \geq 2$ if $l = 2$, $K$ lies in $K_0(\mu_{l^s})$, and $L'$ contains every conjugate of that field.

## Proof

The proof is the tactic `first | exact @GlobalTheory.HWL.Assembly.exists_wach | ...`. The statements are the same, so no mathematics happens here.

## In the Lean code

The theorem is at [ExistsLocalWachFunctorStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsLocalWachFunctorStatement.lean#L7). The target is at [ExistsLocalWachFunctor.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsLocalWachFunctor.lean#L16). `LocHW`, `LocFon` and `LocCmpT` are in [DataNLoc.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DataNLoc.lean#L1227), and `Good` is at line 477 of the same file.
