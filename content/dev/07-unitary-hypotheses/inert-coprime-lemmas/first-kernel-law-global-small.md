---
id: first-kernel-law-global-small
title: The first kernel law at inert primes, from complex multiplication
kind: theorem
decl: Formalism.L2.KerInert.KGLt.first_kernel_law_global_small
module: Formalism.LocalToGlobal.InertKernelTheory.InertCoprimeLemmas.FirstKernelSmallOfFrameTwist
covers: 355
status: drafted
drafted_by: writer@claude
---
This theorem proves the first kernel law `TranslatesOfInertKernelAtPlace` under the hypothesis `CM2`. It gives three of the 13 conditions of `admitted` (`adm2`, `adm2b`, `adm3`) for the pending datum built from theta kernels at an inert prime $p \ge 5$. Its only user is [`admissible_entries_small_chain`](/entry/admissible-entries-small-chain/). The integrality of the kernels comes from [`kernels_integral_inert`](/entry/kernels-integral-inert/).

## Statement

Assume `CM2`, as in the parent entry.

**Theorem.** `TranslatesOfInertKernelAtPlace` holds.

That statement says: let $p \ge 5$ be prime and $X$ a system over $p$. Assume `CurveIn` ($p$ inert, a good model over the Witt vectors, and the conditions on $c$, $\delta$, $\chi$, $\lambda$) and the theta series hypotheses below the maximal level (`AdmGLt`, `ClAway`, `XiAwayLt`, `ScalGLt`, and a frame map $\rho$ with `LamPosG`, `MInv` and `FrameLatMapLt`). Then `adm2`, `adm2b` and `adm3` hold for $Y$ = `pendT X ... (FrecG ...)`.

## Proof

1. `first_kernel_small_of_frame_twist` gives `FirstKernelLawLocalPowerSeries`: for $j < m$, a representative $L_0$ at level $j$, a lattice tuple $L'$ at level $j + 1$ and a frame $\varphi$, the series of $Y$ satisfies `ExtensionGeneratorCondition`. That is, it is $\exp(-\Phi) U$ with $U$ integral and $\Phi$ a sum of values of the series $b$ = `beLT` up to $\simeq$.
2. `adm_two_pendant_iff_representative` turns this into `adm2b`, which asks the same for all lattice tuples, not only representatives.
3. `admissible_second_of_variant` gives `adm2` from `adm2b`.
4. `admissible_third_of_second_eleventh` gives `adm3` from `adm2b` and `admissible_eleventh_inert`.

Step 1 has the real work. The twist lemma replaces the coefficients $\Xi_0$ by $\Xi_1$, which are $0$ off the representatives. This turns `XiAwayLt` into `XiAway`. Then `first_kernel_small_of_frame` writes the family as a linear substitution of scaled theta kernels. It checks `BeProp`, `CombAtLt`, `OnbExLt`, `LamTraceLt` and `FrameHypLt`, and applies `K1_representatives_LT_of_dictionary` with `curve_dictionary` and `kernels_integral_inert`.

## In the Lean code

The theorem is at [FirstKernelSmallOfFrameTwist.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/FirstKernelSmallOfFrameTwist.lean#L124). The statement is in [TranslatesOfInertKernelAtPlace.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/TranslatesOfInertKernelAtPlace.lean#L20), and `FirstKernelLawLocalPowerSeries` in [DefsRepLt.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/DefsRepLt.lean#L22).

- `CM2` enters as `variable [Fact CM2] in` at line 122. Its only use is through `kernels_integral_inert` in `first_kernel_small_of_frame`.
- The name says "global" and "small". The statement is local at one prime, and "small" matches nothing in it. The suffix "Lt" in the hypotheses means that they are asked only for levels $j < m$.
- We have not opened the proofs of the lemmas in steps 2 to 4.
