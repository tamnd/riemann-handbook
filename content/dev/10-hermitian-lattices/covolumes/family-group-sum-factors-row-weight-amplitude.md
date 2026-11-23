---
id: family-group-sum-factors-row-weight-amplitude
title: Group sums of a family factor as row weight times local amplitude
kind: theorem
decl: GlobalTheory.FamilyNormRational.familyGroupSumFactorsRowWeightAmplitude
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.FamilyGroupSumFactorsRowWeightAmplitudeProof
covers: 933
status: drafted
drafted_by: writer@claude
---
This theorem proves the proposition `FamilyGroupSumFactorsWeightAmplitude`. It chooses a rescaling $s$ of the archimedean measures and then calls [`squaredGroupSum_classDoubleCoset_eq_rowWeight`](/entry/squared-group-sum-class-double-coset-eq-row-weight/), which has the content. Two theorems use it: `rowGen1P_of_siegelWeil_of_points` directly, and `rowNGP_of_formNGVanish` through the renaming `familyGroupSumFactorsRowWeightAmplitude_proof`. Both are below the step [HypsAlt is nonempty](/step/nonempty-hyps/).

## Statement

For all reals $C_g, c_b, C_w, c_T, C_T, C_0$ there are $C_{\mathrm{St}} \geq 0$ and thresholds $C'_0, C_{l,0}$ with the following property. Let $C' \geq C'_0$ and $C_l \geq C_{l,0}$. Let $D$, size data with base $b$, a Hida setting $X$, a choice $Y$ (`Full X`) and words $u, u'$ satisfy the context `Ctx` of these constants. Take mass data that satisfy `MassDataTie` and `MassDataAdmissible`, and a family $\nu$ of measures on the archimedean group $G_\infty$ that is `Pinned`. Then there is $s \colon G_\infty \to \mathbb{R}_{\geq 0}$ such that:

1. $s(\gamma) = 1$ at each $\gamma$ with `RegX`;
2. $s(\gamma) > 0$ for all $\gamma$;
3. $s(\gamma)^2 \leq b^{\,C_{\mathrm{St}} (2r + 2)^3 f}$ for all $\gamma$;
4. for each family $(S, T_S, \mathrm{cls}, \gamma, F_m)$ that satisfies `FamQ`, `HasPt` and `FamTie`, and for each class $c$ and double coset $n$, the identity $a_F(s\nu; c, \gamma, n) = a_W(c, n)$ of [the entry below](/entry/squared-group-sum-class-double-coset-eq-row-weight/) holds.

Here $r$ and $f$ are `D.R.rS` and `D.R.f`, and $s\nu$ is the family $\gamma \mapsto s(\gamma)\,\nu(\gamma)$ (`sc s ν`).

## Proof

Take $C_{\mathrm{St}} = 0$ and both thresholds $0$. The theorem `exists_scale_normalised_localReading` gives $s$ with clauses 1 and 2, with $s \leq 1$, and with $s(\gamma_z) = g^{-f \lvert \mathrm{FreeE}(z) \rvert}$ at the archimedean point $\gamma_z$ of each point $z$ that has a representative. Clause 3 with $C_{\mathrm{St}} = 0$ reads $s(\gamma)^2 \leq 1$, which follows from $0 \leq s \leq 1$. The lemma `four_rank_add_seven_le_k` gets $4r + 7 \leq k$ from `Ctx`. Clause 4 is [`squaredGroupSum_classDoubleCoset_eq_rowWeight`](/entry/squared-group-sum-class-double-coset-eq-row-weight/) with this $s$.

## In the Lean code

The theorem is in [FamilyGroupSumFactorsRowWeightAmplitudeProof.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/FamilyGroupSumFactorsRowWeightAmplitudeProof.lean#L183). The proposition is in [FamilyGroupSumFactorsWeightAmplitude.lean](lean:Development/AbelianVarietyTheory/Statements/CuspFrameWeights/FamilyGroupSumFactorsWeightAmplitude.lean#L45).

- The proof takes $C_{\mathrm{St}} = 0$, so clause 3 is the weak bound $s^2 \leq 1$, and the size data enter only through $b^0 = 1$.
- Many hypotheses are not used: the mass data (`hb`, `X0`, `ψ`, `MassDataTie`, `sd`, `C`, `Th`, `F0`, `vR`, `Q`, `i0`, `i0'`, `νq`, `Irat`, `Ire`, `MassDataAdmissible`) and the first half of `Pinned` (`NuQOK`). `Ctx` is the conjunction of `Hyp0`, `Stand` and `ConcTie`. The proof uses `Hyp0` only for $4r + 7 \leq k$; the constants $C_g, \dots, C_0, C', C_l$ play no other role.
- We have not unfolded `RegX`, `FreeE` or the integer $g$ (`X.B.g`).
