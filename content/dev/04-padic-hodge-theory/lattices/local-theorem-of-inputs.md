---
id: local-theorem-of-inputs
title: The local lifting theorem for crystalline lattices, from local inputs
kind: theorem
decl: Formalism.MainNotions.N.Ln03.local_theorem_of_inputs
module: Formalism.SharpRestriction.LevelLetterCocycles.LocalTheoremOfInputs
covers: 1668
status: drafted
drafted_by: writer@claude
---
This theorem proves the local lifting theorem `Conclusion1 D 800`: along a surjection of crystalline lattices with Hodge-Tate jumps in given windows, $\ell^e$ times each finite cocycle lifts, for an explicit $e$. It assumes local hypotheses on Wach modules. Its only user is [the corollary with one constant](/entry/corollary-local-exists-constant/), which adds the colength bound.

## Statement

Say that $f \colon T_1 \to T_2$ *lifts with exponent* $e$ (`LiftF`) if $\ell^e$ kills each finite cocycle of $T_2$ modulo the image of the finite cocycles of $T_1$ plus coboundaries.

**Theorem.** Let $D$ be a datum with local data $HW$, $F$, $C_m$, and let $C$ be real. Assume:

- the Wach lattice lemmas `P3`, `P4`, `P5`, `P6`, `P9`, `Pr2a` and `lem3`;
- `adm3`, `adm7` to `adm10`, and `WachResultConstant C`;
- `adm14`: for a surjection $T_1 \to T_2$, each jump of $T_2$ is a jump of $T_1$; in a short exact sequence the jumps of the middle term are those of the ends; a trivial representation has only the jump $0$;
- `DdREqDcris` for unramified $K$, `LocalSituation.adm9`, and `LitFont` (the Wach functor is fully faithful and exact, with an operator $\psi$);
- for unramified $K$ and $\ell \ge 5$, the Wach module has a unit generator (`UnitGen`).

Then `Conclusion1 D 800` holds, that is:

1. (`ThmELiftAt`) Let $\ell \ge 5$ and let $\mathrm{emb} \colon \mathbb{Z}/n \to \mathrm{Hom}(K_0, L)$ satisfy the letter condition `Letters`: $K = K_0$, $n = [K_0 : \mathbb{Q}_\ell]$, $\mathrm{emb}$ is a bijection with $\mathrm{emb}(i+1) \circ \sigma = \mathrm{emb}(i)$ for the Frobenius $\sigma$, $L$ is finite over $\mathbb{Q}_\ell$ and $v(\ell) = 1$. Let $f \colon T_1 \to T_2$ be a surjection of crystalline lattices with `GoodCoeffs`. Suppose the jumps of $T_1$ lie in windows (thin, up or down) and in $[-h, h]$, and the cut data meet `SizesOK`, `CutsOK`, `ThickLe2` and `WordOK`. Then $f$ lifts with exponent $e = \mathrm{ePar}(\ldots)$, an explicit integer.
2. (`ThmEBound 800`) $e \le 800\bigl(h/(\ell-1)^{j+1} + g \cdot \mathrm{ellMax} + \log_\ell h\bigr)$, where $j$ is the cut length, $g$ the window size and $\mathrm{ellMax}$ the largest arc length.

We have not unfolded most hypotheses, `GoodCoeffs`, or the conditions on the cut data.

## Proof

Part 2 is the numerical inequality `thmEBound_holds`; it does not use the hypotheses. Part 1 is `local_theorem_of_cyclotomic_lift`. It passes to a larger field `richLL` that contains a primitive $\ell^{[K_0:\mathbb{Q}_\ell]}$-th root of unity, proves the statement there, and comes back by base change (`thmELiftAt_bc`, with `base_change_every_theory`).

In that case the proof calls `crystalline_lifting_second_form`. Its input is a record `BrHyp2`, built by `brHyp2_of_rec` from the hypotheses. Only the last field needs work. It takes the unit generator from `UnitGen`, the extension statement from `bkExt_holds` (which uses `LocalSituation.adm9` and `LitFont`), and the realisation statement from `realised2_pf`, which uses the tie data of $C_m$, nine hypotheses, `complMax_holds` and `uTieRec_holds`. The rest is bookkeeping.

## In the Lean code

The theorem is at [LocalTheoremOfInputs.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalTheoremOfInputs.lean#L26). `Conclusion1` is `LiftingTheoremLocalTheory` in [WachCoordinates.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/WachCoordinates.lean#L287), with `ThmELiftAt` at [line 123](lean:Formalism/SharpRestriction/LevelLetterCocycles/WachCoordinates.lean#L123). `local_theorem_of_cyclotomic_lift` is at [LocalCorollaryOfDeRham.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalCorollaryOfDeRham.lean#L103), and `thmEBound_holds` at [BoundedNumeratorPowerSummability.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BoundedNumeratorPowerSummability.lean#L154).

- The constant $C$ appears only in the hypothesis `WachResultConstant C`. The conclusion has 800 for every $C$, from the numerical part 2.
- The name `ArchimedeanSignatureMatching` has three meanings in this folder, none about archimedean signatures: `WachResultConstant C` in [WachCoordinates.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/WachCoordinates.lean#L326), `lem3` in RamifiedCoefficientChains.lean and `LiftTheoremAllCases` in ElementDenominator.lean.
- The letter condition asks $K = K_0$, so part 1 says nothing about ramified $K$.
- `base_change_every_theory` is in the namespace `UnusedSlot80`, but it is used here.
