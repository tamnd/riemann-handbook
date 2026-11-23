---
id: aux-of-bloch-kato-tate-duality-euler-char
title: Theorem TB from Bloch-Kato, Tate duality and the Euler characteristic
kind: theorem
decl: GlobalTheory.TheoremTBRecords.aux_of_blochKato_tateDuality_eulerChar
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TheoremTbOfLocalBlochKatoDualityEuler
covers: 626
status: drafted
drafted_by: writer@claude
---
This theorem proves the local torsion bounds `Conclusion4` from three published local theorems. It is the proof of [its second name](/entry/theorem-tb-of-local-bloch-kato-duality-euler/). The proof only assembles inputs. The content is in [the good case](/entry/twisted-torsion-class-theorem-good-case/) and the entries below it.

## Statement

The hypotheses are `BlochKatoLocal`, `LocalTateDualityK` and `LocalEulerCharK`. The last two are Tate's local duality and Euler characteristic formula (Serre, *Galois Cohomology*, II.5.2 and II.5.7). `BlochKatoLocal` says that, for local data tied together, a dimension formula, a rational duality and an integral duality hold at each $K$. We have not unfolded these three parts.

**Theorem.** Under these hypotheses, for each datum $D$ and all local data $HW$, $F$, $Cm$, `Conclusion4 D HW F` holds. That is, at each prime $\ell$ and good triple $(K, s, L)$, with $\chi$ the cyclotomic character:

1. (`TBat`) Let $0 \to Y \to \tilde{Y} \to Z \to 0$ be an exact sequence of lattices, with $Z$ of rank one and trivial action, and $\tilde{Y}$ crystalline on $G_{K_s}$. Let $V_e$ have rank one with action $\chi^{-e}$. Let $f$ be the cochain of a lift $\tilde{y}$ of a generator of $Z$, and let $\varphi$ be an equivariant map from $Y$ to $V_e / L_e$. Under a hypothesis `HypW` on $Y$, a power $\ell^c$ times $\varphi \circ f$ is a finite class. We have not unfolded `HypW` or the exponent `cTB`.
2. (`TBeAt`) For $V_e$ as above, the $\ell^n$-torsion of divisible classes modulo finite classes has length at most $([K:\mathbb{Q}_\ell] + 1)\, n$ times the length of $\mathcal{O}/\ell$. If $e > 0$, every finite class is a coboundary. If $e = 0$, a class is finite if and only if it is divisible and a coboundary on inertia.

## Proof

1. `ties_and_inputs_of_duality_euler` takes Tate duality and the Euler characteristic and gives `admitted D HW F`, nine local facts. Two of them are the two hypotheses.
2. `blochKatoLocal_all_of_tateDuality_eulerChar` takes all three hypotheses and gives `Conclusion5 D`, the Bloch-Kato facts at each $K$.
3. [The good case](/entry/twisted-torsion-class-theorem-good-case/) turns `admitted` and `Conclusion5` into `Conclusion4`.

## In the Lean code

The theorem is in [TheoremTbOfLocalBlochKatoDualityEuler.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremTbOfLocalBlochKatoDualityEuler.lean#L12). `TBat` and `TBeAt` are in [LocalSituation.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalSituation.lean#L165).

The argument $Cm$ is unused (it is `_Cm`). Step 1 also gives a witness of `Ties`, and the proof drops it (it is `_J`). `BlochKatoLocal` enters only through `Conclusion5`.
