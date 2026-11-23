---
id: tb-assembled
title: The two local torsion statements, put together
kind: theorem
decl: GlobalTheory.TheoremTB.tb_assembled
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TwistedTorsionClassTheoremGoodCase
covers: 624
status: drafted
drafted_by: writer@claude
---
This theorem proves `Conclusion4`, a pair of local statements at every prime $\ell$, from the local inputs `admitted` and the Bloch-Kato statement `Conclusion5`. It is the proof of [the twisted torsion class theorem in the good case](/entry/twisted-torsion-class-theorem-good-case/), which has the same statement. That chain goes up to the trunk step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). The proof only pairs two theorems. The first, [the crystalline extension class bound](/entry/crystalline-extension-class-bound/), carries almost all of the 624 declarations below this one.

## Statement

Let $D$ be a datum of type `D7`, and let $HW$ and $F$ be local data over it (types `HWOf` and `FonOf`: Wach module data and comparison data at each prime, which we do not unfold). Let $\ell$ be a prime, $K$ and $L$ finite extensions of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$, and $s \geq 1$, with `Good K s L` (see [the class bound](/entry/class-bound/)). From these the code builds a local situation $S$: the group $G_K$, the period data of $D$ at $\ell$ and $K$, and the coefficients $L$ and $\mathcal{O}_L$.

**Theorem.** If `admitted D HW F` and `Conclusion5 D` hold, then for all $\ell, K, s, L$ as above, `TBat S E` and `TBeAt S` hold.

- `admitted` is nine local inputs. Among them are local Tate duality, Tate's local Euler characteristic formula, and statements of Fontaine type on the period data.
- `Conclusion5` says that five Bloch-Kato statements (`bkAll`) hold for the period data at each $\ell$ and $K$.
- `TBat` bounds the push-forward of a crystalline extension class. It is stated in full in [the class bound](/entry/class-bound/).
- `TBeAt` is about a lattice $T$ in a line $V$ on which $G_K$ acts by $\chi^{-e}$, with $\chi$ the cyclotomic character. It says three things. The $\ell^n$-torsion of $H^1(K, V/T)$ modulo $H^1_f$ has length at most $([K:\mathbb{Q}_\ell]+1)\, n$ times the length of $\mathcal{O}_L/\ell$. If $e > 0$, every $H^1_f$ cocycle is a coboundary. If $e = 0$, a function $G_K \to V/T$ is in $H^1_f$ if and only if it is a locally constant cocycle and its restriction to the inertia subgroup `IK` is a coboundary.

## Proof

The proof is a pair. `TBat` comes from `crystalline_extension_class_bound`, which uses `admitted` only. `TBeAt` comes from `weight_good_reduction_at_prime`, which takes both hypotheses. We have not opened its proof.

## In the Lean code

The theorem is in [TwistedTorsionClassTheoremGoodCase.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistedTorsionClassTheoremGoodCase.lean#L12). `Conclusion4`, `Conclusion5` and `admitted` are in [LocalSituation.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalSituation.lean#L590). The lemmas it calls:

- `GlobalTheory.T.crystalline_extension_class_bound`;
- `GlobalTheory.T.weight_good_reduction_at_prime`, in WeightGoodReductionAtPrimeStatement.lean.

`Conclusion5` goes only into the second part.
