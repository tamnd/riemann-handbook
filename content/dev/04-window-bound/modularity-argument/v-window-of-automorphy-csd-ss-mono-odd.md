---
id: v-window-of-automorphy-csd-ss-mono-odd
title: The window bound from the literature hypotheses, through the extended hypotheses
kind: theorem
decl: UpperTheory.V.HV.DescentVanishingReductions.v_window_of_automorphy_csd_ss_mono_odd
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.WindowBoundOfLiteratureLevel
covers: 55093
status: drafted
drafted_by: writer@claude
---
This theorem proves the window bound $\mathrm{VWin}$ from the rank $n$ literature hypotheses. It is Step 4 of the chapter [The window bound VWin](/proof/vwin/). [The theorem above it](/proof/vwin/) only calls it. The proof composes two theorems. The real content is in [the four counts](/proof/vwin/) and in [the builder of the extended hypotheses](/entry/published-hypotheses-from-patching-alt/).

## Statement

**Theorem.** Suppose that the structure $\mathrm{LiteratureRankNHypothesis}$ holds. Then $\mathrm{VWin}$ holds.

$\mathrm{VWin}$ is the bound on the lengths of Tate-Shafarevich groups that the [step VWin](/step/vwin-def/) states. $\mathrm{LiteratureRankNHypothesis}$ has four fields: local statements on $\mathrm{GL}_n$ of a local field, global automorphy statements (the Galois row enters here as the field `aut.gal`), statements on [[Galois cohomology|9MPCZ3EAJM]], and the CM inputs.

## Proof

The structure $\mathrm{HypothesesH'}$ extends $\mathrm{LiteratureRankNHypothesis}$. The theorem `published_hypotheses_from_patching_alt` builds it from the literature hypotheses and one descent statement $\mathrm{DescWeak}$. It keeps them as the field `litN` and adds Clozel's statements on cohomology, Galois representations for totally real fields in rank 2, strong multiplicity one, quadratic base change, newforms, cyclotomic statements and a definite quaternion algebra. The descent statement is the theorem `descWeak`, proved from `descWeakAll`. Then `vwin_of_hypotheses_H_E_alt` proves $\mathrm{VWin}$ from $\mathrm{HypothesesH'}$, through Lemma K and the four counts. The rest is bookkeeping.

## In the Lean code

The theorem is in [WindowBoundOfLiteratureLevel.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/WindowBoundOfLiteratureLevel.lean#L30). The proof is one line:

```
vwin_of_hypotheses_H_E_alt (published_hypotheses_from_patching_alt hN UpperTheory.V.Z.Tf.SR.descWeak)
```

The lemmas it calls:

- `vwin_of_hypotheses_H_E_alt`, in the same file at line 25.
- `published_hypotheses_from_patching_alt`, in [PublishedHypothesesFromPatching.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PublishedHypothesesFromPatching.lean#L98).
- `UpperTheory.V.Z.Tf.SR.descWeak`, in [HasOfSplit.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/SplitRigidity/HasOfSplit.lean#L29). We have not unfolded $\mathrm{DescWeak}$.

Lines 33 and 34 define `UpperTheory.V.v_window_of_literal_automorphy_n` as this theorem, so the two names are one theorem. The name "automorphy csd ss mono odd" does not describe the statement.
