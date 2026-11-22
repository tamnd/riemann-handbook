---
id: bloch-kato-top-of-local-tate-duality-euler-char-alt
title: The top local theorem from Tate duality and the Euler characteristic
kind: theorem
decl: GlobalTheory.TopClosing.blochKatoTop_of_localTateDuality_eulerChar_alt
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.BlochKatoTopOfLocalTateDualityEulerChar
covers: 1649
status: drafted
drafted_by: writer@claude
---
This theorem proves the 24 local hypotheses of [the twisted lattice cohomology theorem](/entry/twisted-lattice-cohomology-theorem-top/) and applies it. Two of the 24 are local Tate duality and the local Euler characteristic formula, which it takes as hypotheses. The other 22 are proved by lemmas of the development. Its user is its [second name](/entry/bloch-kato-top-of-local-tate-duality-euler-char/), which [the congruence bound along a family](/entry/nlink-e-main-alt-alt/) calls.

## Statement

**Theorem.** Assume `BlochKatoLocal`, `LocalTateDualityK` and `LocalEulerCharK`. Then for each datum $D$ and all local data $HW$, $F$, $Cm$ over it, the statement `aux₃ D HW F` holds.

The three hypotheses are statements of local [[Galois cohomology|9MPCZ3EAJM]] over finite extensions $K$ of $\mathbb{Q}_\ell$:

- `LocalTateDualityK`: for each $r > 0$ and each finite discrete $\mathbb{Z}/\ell^r$-module $M$ with a continuous action, $H^2(K, \mu_{\ell^r}) \cong \mathbb{Z}/\ell^r$, and the cup products $H^i(K, M) \times H^{2-i}(K, M^\vee(1)) \to H^2(K, \mu_{\ell^r})$ are perfect;
- `LocalEulerCharK`: $\#H^1(K, M) = \#H^0(K, M) \cdot \#H^2(K, M) \cdot (\#M)^{[K:\mathbb{Q}_\ell]}$;
- `BlochKatoLocal`: a dimension formula, a rational duality and an integral duality for the Bloch-Kato subspaces $H^1_f$.

The first two are the local duality theorem and the Euler characteristic formula of Tate (J.-P. Serre, *Galois Cohomology*, Chapter II, 5.2 and 5.7).

The conclusion `aux₃ D HW F` is stated in full in [the twisted lattice cohomology theorem](/entry/twisted-lattice-cohomology-theorem-top/).

## Proof

The proof builds a proof of `admitted D HW F Cm`, the conjunction of 24 local statements, and applies `GlobalTheory.TopBridge.twistedLatticeCohomology_theoremTOP`, which says that `admitted` implies `aux₃`. The 24 parts come as follows.

1. Parts 1 to 15 and the last two come from `T.wachLattice_laterClauses_hold`. It gives a conjunction of 17 statements on Wach lattices. The proof keeps 15 of them, drops the 16th, and turns the 17th into parts 23 and 24 with `tableLineDegreeTwo.ainf_clauses_of_theorem`.
2. Part 16, a statement on Herr lattices, comes from `InvariantsGenerators.herr_lattice_of_fon`, fed with `HerrFull.herr_part_a_every_record`, `T.invariants_statement_holds` (from `Decompl.fontaine_and_decompletion`) and `T.fontaine_fullFaithful_exact_psi`.
3. Part 17 comes from `herr_lattice_rest_iff`, `EtaleSub.exists_lattice_of_pow_mem` and `ExtDict.extension_rule`.
4. Part 18 is the pair of hypotheses (Tate duality, Euler characteristic).
5. Part 19, the dimension formula for $H^1_f$ of crystalline representations, comes from `FiltrationJumpMultiplicity.blochKato_dimension_saturation_unramified`.
6. Parts 20, 21 and 22 come from `T.crystalline_characters_given_jumps_unramified_twists`, `SenMult.stmtSen` (fed with parts 2, 4, 5, 9 and 11) and `CrysFormalism.crysLit_all`.

## In the Lean code

The theorem is in [BlochKatoTopOfLocalTateDualityEulerChar.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BlochKatoTopOfLocalTateDualityEulerChar.lean#L25). We have not unfolded the statements of parts 1 to 17 and 20 to 24.

- The hypothesis `BlochKatoLocal` is never used. Line 28 introduces it as `_`. Part 19, the Bloch-Kato dimension formula, comes from a lemma of the development and not from this hypothesis. So the name "blochKatoTop" does not match the use of the hypotheses.
- The datum $Cm$ is used in the proof (parts 1 to 15 and part 21), but the conclusion `aux₃ D HW F` does not mention it.
- Part 18 is `tableLineDegreeTwo.adm18`, which ignores its argument $D$ and is just the pair (Tate duality, Euler characteristic). So the two literature hypotheses enter as a field of `admitted`.
