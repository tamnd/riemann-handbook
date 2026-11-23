---
id: ar-calc-direct
title: The arithmetic intersection calculus from Poincaré-Lelong and resolution
kind: theorem
decl: GlobalTheory.ArithmeticHeightTower.ArakelovDirectHeights.arCalc_direct
module: Development.WeilBound.CoreStatements.TemperedRepresentationTheory.ArakelovCycleHeights.CycleHeightFormulas.CycleHeightsDirect
covers: 869
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{ArCalc}$, the seven rules of arithmetic intersection theory, from two hypotheses: an arithmetic Poincaré-Lelong formula and a form of resolution of singularities. It is a second route to the statement of [ArCalc from principalisation](/entry/ar-calc-of-principalisation/), which lists the seven rules. Its callers sit in [the step EveryCharacter of literature](/step/every-character-of-literature/). They supply both hypotheses, so $\mathrm{ArCalc}$ there holds without assumptions.

## Statement

The hypotheses are:

- `PoincareLelong`, which is `ArithmeticPoincareLelongFormula`. We have not unfolded it.
- `ResKStatement`: resolution of singularities with projective coordinates (`IsResInput`). We have not unfolded it in full.

**Theorem.** `PoincareLelong` and `ResKStatement` imply $\mathrm{ArCalc}$.

## Proof

The proof has three steps.

1. `arith_intersection_system_of_poincare_lelong` turns the two hypotheses into an arithmetic intersection system $H$ (`ArithIntersectionSystemStatement`).
2. Three lemmas give statements on closed integral subschemes $X$ of a multiprojective space over $\mathbb{Z}$, for hermitian line bundles pulled back from it:
   - `formZ_direct` gives `FormZ`: an arithmetic intersection functional $\Phi$ exists (`IsArFun`).
   - `mixZ_direct` gives `MixZ`: the mixed formula `MixOn` holds.
   - `projQ_direct` gives `ProjQ`: for the projection $q$ off one factor, $h'(y) = \deg(y/q(y))\,h(q(y))$, where $h$ is a height and $h'$ is the height of the pullback bundle, and the degree is the residue degree at the generic point.
3. `Read1.bridge3` turns these into `ArFormExists`, `ArMix` and `HeightProjection`. Then `arithIntersectionCalculus_of_form_mixed_projection` gives $\mathrm{ArCalc}$.

Each of the three lemmas in step 2 uses $H$ through `height_eq_direct`. That lemma says that a height of a point equals the intersection number of $H$ on the closure of the point. The lemmas also use many results of the form `GlobalTheory.T.mixed_cycle_*`, which we have not opened.

The rules have the shape of the theory of Bost, Gillet and Soulé (J. Amer. Math. Soc. 7, 1994). We have not compared the Lean rules with the paper.

## In the Lean code

The theorem is in [CycleHeightsDirect.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/ArakelovCycleHeights/CycleHeightFormulas/CycleHeightsDirect.lean#L138). The same file proves `cycleHeights_direct` at line 144, by `cycleHeights_of_arCalc`. `FormZ`, `MixZ` and `ProjQ` are in [QpSndStr.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/ArakelovCycleHeights/QpSndStr.lean#L36). `bridge3` is in [HeightsOfFormMix.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/ArakelovCycleHeights/HeightsOfFormMix.lean#L25). `ArCalc` is in [EqOfIsometricTrivShift.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/EqOfIsometricTrivShift.lean#L161).

The callers are in `EveryCharacterOfLiteratureOfVWin.lean`, at lines 250, 252 and 348. They pass `Tls2.Pl.poincareLelong` and `ResPlug.FromRes.resK`. So $\mathrm{ArCalc}$ fills the field `p4` of [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/), and `CycleHeights` fills `q11`. The caller `ar_calc_of_literature` ignores its argument $O$.
