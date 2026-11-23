---
id: thm-pactual-cpt-of-spec
title: The compact form of Theorem P from the spectral identity
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutSE.thmPActualCpt_of_spec
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutSE_TopSpec
covers: 981
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThmPActualCpt`, the compact form of Theorem P, from one hypothesis, `RDIdentSpec`. It is a pass-through. It turns the hypothesis into a radial decay bound and proves two smoothness facts, then calls [the compact form of Theorem P from three leaf facts](/entry/thm-pactual-cpt-of-leaves/). Its only user is [the compact form of Theorem P from the radial operators](/entry/thm-pactual-cpt-of-r/), which proves `RDIdentSpec` and describes it.

## Statement

Use the setting of [the compact form of Theorem P](/entry/actual-compact-theorem/). `RDIdentSpec` says: there are a real $Y$ with $Y, Y + 1$ in `st.inv` and four differential operators with `RDOpsProp`, which act on restrictions to the radial space as four given radial operators and their adjoints.

**Theorem.** `RDIdentSpec` implies `ThmPActualCpt`.

## Proof

1. `radDecay_of_spec` turns `RDIdentSpec` into `RadDecay`. It uses `radial_identity_of_spectral_data` to get `RDIdentABQ`, then `radDecay_of_ABQ`.
2. `spectral_radial_locality` proves `JSRadLoc`. From it, `leibniz_class` proves `LeibnizCls` and `density_smooth_class` proves `DensSmoothCls`. Both go through the same lemma `jSliceGenC_of_radLoc`.
3. `one_letter_density_estimate` turns `LeibnizCls` and `DensSmoothCls` into `OneLetterDens`.
4. `thmPActualCpt_of_leaves` takes `OneLetterDens`, `DensSmoothCls` and `RadDecay`.

So the hypothesis enters only through `RadDecay`. The other two leaf facts are proved here with no hypotheses.

## In the Lean code

The theorem is at [CutSE_TopSpec.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSE_TopSpec.lean#L13), with `leibniz_class` at line 9 and `density_smooth_class` at line 11. `radDecay_of_spec` is in [RadialIdentityOfSpectralData.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/RadialIdentityOfSpectralData.lean#L25). `RDIdentSpec` is in [RadialIdentityOfQuadratic.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/RadialIdentityOfQuadratic.lean#L239). `spectral_radial_locality` is in [CutSEJSRadLoc.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSEJSRadLoc.lean#L165). We have not unfolded `RDIdentABQ` or `JSRadLoc`.
