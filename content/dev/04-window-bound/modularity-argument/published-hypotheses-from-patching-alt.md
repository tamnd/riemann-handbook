---
id: published-hypotheses-from-patching-alt
title: The package of published hypotheses, from the literature hypothesis and descent
kind: theorem
decl: UpperTheory.V.HV.DescentVanishingReductions.published_hypotheses_from_patching_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.PublishedHypothesesFromPatching
covers: 3449
status: drafted
drafted_by: writer@claude
---
This theorem builds the package $\mathrm{HypothesesH'}$ from the literature hypothesis $\mathrm{LiteratureRankNHypothesis}$ and a weak descent statement $\mathrm{DescWeak}$. [The window bound from automorphy](/entry/v-window-of-automorphy-csd-ss-mono-odd/) passes the package to [VWin from the hypotheses H and E](/proof/vwin/). The proof is a structure literal: it fills each field with a theorem proved elsewhere. The 3,449 declarations below it are the proofs of those theorems. The largest are the descent `RankTwoDescent.descS` and `clozelConjC`.

## Statement

**Theorem.** If $\mathrm{LiteratureRankNHypothesis}$ and $\mathrm{DescWeak}$ hold, then $\mathrm{HypothesesH'}$ holds.

$\mathrm{HypothesesH'}$ is a structure. Its fields, grouped by purpose:

- The literature hypothesis itself (`litN`).
- Cohomology and conjugation of automorphic representations over a totally complex field: a cuspidal $\pi$ whose infinitesimal character matches an algebraic representation is cohomological for it (`cohC`); the conjugate of a regular algebraic $\pi$ by $\sigma \in \operatorname{Aut}(\mathbb{C})$ is again automorphic (`conjC`); the number of cohomological $\pi$ with fixed vectors under an open compact $U$ is at most the dimension of the cohomology (`borelC`).
- $\mathrm{GL}_2$ over a totally real field: Galois representations for regular algebraic polarized $\pi$ (`galR`), strong multiplicity one (`smoR`), a nondegenerate invariant pairing (`gkR`), admissibility (`admR`), and semisimplicity of the cusp forms (`ssR`).
- Base change and descent: quadratic base change for $\mathrm{GL}_2$ from a totally real field to a totally complex quadratic extension (`bc`); cyclic base change and descent of prime degree (`cyc`); descent for $\mathrm{GL}_2$ from an imaginary quadratic field to $\mathbb{Q}$ (`cyc2`); descent from $\mathrm{GL}_n$, $2 \le n \le 4$, to a unitary group at split places (`descU`).
- Classical forms: the representation of $\mathrm{GL}_2$ over $\mathbb{Q}$ attached to a newform of weight $k \ge 2$, with its infinitesimal character and Hecke polynomial (`newform`).
- A quaternion algebra over each totally real field of even degree (`quat`).

## Proof

The proof fills the fields:

| field | theorem |
|---|---|
| `cohC` | `clozelCohC_alt hN` |
| `conjC`, `borelC` | `Z.Coh.clozelConjC`, `Z.Coh.borelInjC` |
| `galR` | `galois_rep_exists_totally_real_rank_two_of_base_change hN quadBC2 admissibleReal` |
| `smoR`, `gkR`, `admR` | `strongMultOneReal`, `gelfandKazhdanReal strongMultOneReal`, `admissibleReal` |
| `bc` | `Br.quadBC0_of_two quadBC2` |
| `newform` | `newformRepOf cuspSemisimpleReal admissibleReal` |
| `descU` | the hypothesis $\mathrm{DescWeak}$ |
| `cyc`, `cyc2` | `cycC_holds`, `Or.inl RankTwoDescent.descS` |
| `quat`, `ssR` | `defQuatExists`, `cuspSemisimpleReal` |

This is a pass-through. Only `cohC` and `galR` use the literature hypothesis. All other fields are proved outright.

## In the Lean code

The theorem is in [PublishedHypothesesFromPatching.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PublishedHypothesesFromPatching.lean#L98). The structure is in [AfDesc.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/AfDesc.lean#L17). It extends `Hypotheses'` in [AutomorphicFormHyp.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/AutomorphicFormHyp.lean#L12).

The caller passes `UpperTheory.V.Z.Tf.SR.descWeak` for $\mathrm{DescWeak}$. A second theorem `descWeak` with a different hypothesis exists in the trace formula folder. The field `cyc2` is a disjunction, and the proof takes the left side. `gelfandKazhdanReal` takes strong multiplicity one as its argument. We have not unfolded `DefQuat`.
