---
id: theorem-of-literature-hypotheses
title: Local lifting theorem C with constant 25, from five local hypotheses
kind: theorem
decl: Formalism.MainNotions.RamifiedCoefficientChains.Asm.theorem_of_literature_hypotheses
module: Formalism.SharpRestriction.LevelLetterCocycles.FrobeniusLiftLemmasOfAdmitted
covers: 1283
status: drafted
drafted_by: writer@claude
---
This theorem proves the implication "the 19 admitted conditions imply the local colength bound with constant 25" from five hypotheses on Wach modules and crystalline lattices. It has the content of a chain of renamings: [`theoremC_of_admitted_inputs`](/entry/theorem-c-of-admitted-inputs/) restates it, [`ramified_coefficient_chains_of_hypotheses`](/entry/ramified-coefficient-chains-of-hypotheses/) restates that, and [the ramified coefficient bound with constant 25](/entry/ramified-coefficient-chains-prv-twenty-five/) supplies all the premises.

## Statement

Let $D$ be a datum with Wach data $HW$, Fontaine data $F$ and comparison data $C_m$, and let $C_R, C_A, C_B, C_K$ be reals. Assume:

1. (`adm23`) For each prime $\ell$, finite extensions $K, L$ of $\mathbb{Q}_\ell$, and each short exact sequence $0 \to T_0 \to T_1 \to T_2 \to 0$ of crystalline lattices, an integer $a$ is a jump of the Hodge filtration of $T_1$ at an embedding $\tau$ if and only if it is a jump of $T_0$ or of $T_2$ at $\tau$.
2. (`LetterConditionGlobal`) A letter condition on each Wach module $W(K, s, L)$. We have not unfolded `LetterConditionLocal`.
3. (`HerrClassNaturalExtension`) Four statements, not unfolded in full, that compute extension classes through elements of Wach modules, up to a unit.
4. (`adm22`) For each $\ell$, $K$, $L$ and each finite-dimensional representation $V$ over $L$, $\dim_L D_{\mathrm{cris}}(V) \le [K_0 : \mathbb{Q}_\ell] \dim_L V$. This has the shape of Fontaine's inequality for $D_{\mathrm{cris}}$ (Fontaine, Astérisque 223, 1994), but we have not unfolded `Dcris`.
5. (`LitFont`) For $\ell \ne 2$ and $K$ unramified (`CaseA`): the Wach functor is fully faithful, it is exact on short exact sequences of lattices, and there are operators $\psi$ on the coefficient ring and on each module that are left inverses of $\varphi$.

**Theorem.** Under these hypotheses, `Stmt D HW F Cm 25 CR CA CB CK` holds. That is: if the 19 conditions `admitted D HW F Cm CR CA CB CK` hold, then `ConclusionL` holds with constant $25$.

`ConclusionL` is stated in [the entry of the bound with constant 25](/entry/ramified-coefficient-chains-prv-twenty-five/). In short: for a good pair $(K, L)$ with $K$ unramified, $\ell \ge 11$ and Hodge-Tate jumps in given windows, there is an exponent $e$ with an explicit bound that has the term $25(\log_\ell(2H) + 1)$, the colength $\mathrm{col}(F)$ of a surjection of lattices is bounded in terms of $e$, and if $m = 0$ then $\ell^{e + 3S}$ kills each finite cocycle of $T_2$ modulo the image of $T_1$.

## Proof

The proof is `theorem_of_local_lemmas`. It assumes `admitted` and proves three parts:

1. the bound from cocycles to Wach vectors at good extensions, which is `local_lemmas_of_literature` with hypotheses 1, 3, 4 and 5;
2. at each good triple, the lattice bound `lattice_bound_three_six_of`, from `frobenius_lift_lemmas_of_admitted` (with `h2_bound_of_admitted`, `dual_lemma_of_admitted`, `lemmaDN0_L` and `lemmaGs_rec`) and from `steps6_of`;
3. `rhoLift_of_Adm`.

In part 2, only `lemmaGs_rec` uses hypotheses 1 and 2. `stmt_of_lemmas` turns the three parts into `Stmt` through `stmt_of_stepsAdm` and `Theorem_C_of_open`. The last uses admitted conditions 10 and 19 and gives the constant 25. We have not unfolded these lemmas.

## In the Lean code

The theorem is at [FrobeniusLiftLemmasOfAdmitted.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusLiftLemmasOfAdmitted.lean#L292), and `theorem_of_local_lemmas` at [line 272](lean:Formalism/SharpRestriction/LevelLetterCocycles/FrobeniusLiftLemmasOfAdmitted.lean#L272). `admitted` and `Stmt` are at [RamifiedCoefficientChains.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RamifiedCoefficientChains.lean#L392). `stmt_of_lemmas` is at [LatticeBoundsOfThreeParts.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LatticeBoundsOfThreeParts.lean#L592).

- The theorem does not prove the bound outright: its conclusion has the premise `admitted`.
- `LetterConditionGlobal` takes an argument `_F` that it does not use ([LetterConditionGlobal.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LetterConditionGlobal.lean#L29)).
- The fourth admitted condition is named `ArchimedeanSignatureMatching`, but it is the lattice lemma `lem3`.
- [LiftingTheory.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LiftingTheory.lean#L650) has a second `admitted` and a second `Stmt`, with different conditions, next to `adm23`.
- The file is named after the helper `frobenius_lift_lemmas_of_admitted`.
