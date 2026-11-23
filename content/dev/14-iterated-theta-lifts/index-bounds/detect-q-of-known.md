---
id: detect-q-of-known
title: The CM family functionals detect the low Fourier-Jacobi coefficients
kind: theorem
decl: GlobalTheory.ArcCM.detectQ_of_known
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.CmFamilyFunctionalsDetectLowCoefficients
covers: 802
status: drafted
drafted_by: writer@claude
---
This theorem says that the coefficient functionals $\phi_d$ of the CM arc data see every low Fourier-Jacobi coefficient of a cusp form. It is the proof of [`cmFamilyFunctionals_detect_lowCoefficients`](/entry/cm-family-functionals-detect-low-coefficients/), below [`inputsNet_recPlus`](/entry/inputs-net-rec-plus/). The real content is in [`exists_familyMember_functional_ne_zero`](/entry/exists-family-member-functional-ne-zero/).

## Statement

Let $T$ be a core record for $D$, with laws $h$. Fix $j$ with `InR D j` and $j < m$, a weight $\kappa$, and reals $C_R$, $T_t$, $c$. Let $c_1 = $ `c1 D C_R T_t c j`, $n = $ `nAt D j κ C_R T_t c` and $\Lambda = $ `LaAt D j κ C_R T_t c`. A *family member* is an arc datum $d$ over a number field with `Fam n Λ c₁ d`: `Std d` holds and a CM input for $d$ exists. Its functional is $\phi_d$, as in [`cfOf_fin_bound`](/entry/cf-of-fin-bound/).

For a component $k$ of $U = $ `T.U j σ₀`, let $\rho_k(F)$ be the reading of $F$ at $k$ (`rdU`), of weight $\lambda_k$. A function $P$ is in $\mathrm{SS}_{>c_1}(\lambda_k)$ (`SSgt`) if it is a cusp form of weight $\lambda_k$ and $\mathrm{fj}_{\xi,\nu}(P) = 0$ for every isotropic $\xi$ and every exponent $\nu$ with $\sum_\tau \nu_\tau \le c_1$.

**Theorem.** Assume `Known`, `GamAt T`, $r \ge 3$, $T_t > 0$ and $c > 0$. Let $F$ be a cusp form of weight $\kappa$ at level $j$. If $\phi_d(F) = 0$ for every family member $d$, then $F \in$ `MggK`, that is, $\rho_k(F) \in \mathrm{SS}_{>c_1}(\lambda_k)$ for every $k$.

## Proof

`mem_forms_low_coeffs_vanish_iff_fourierJacobi` says that each $\rho_k(F)$ is a cusp form, and that $F \in$ `MggK` if and only if $\rho_k(F) \in \mathrm{SS}_{>c_1}(\lambda_k)$ for all $k$. If this fails at one $k$, `exists_familyMember_functional_ne_zero` gives a family member $d$ with $\phi_d(F) \ne 0$, a contradiction. Its inputs come from these lemmas:

1. `exists_dataX_discr_absNorm` gives lattice data at $k$ with $N_A = |d_E|$, $N_C = N(\mathfrak{c})$, $g = M$ and the lattice $\mathfrak{A} L'$ for the ideal `D.host.AA`.
2. `PinNum.numerics_of_pins` gives the level conditions, and `modelsAt_of_good_level` gives `ModelsAt`.
3. `absA_add_le_size` gives $A + \tfrac12 [E:\mathbb{Q}]\, n \le$ `κ.size`, so the size bound holds with $w = $ `κ.size` $+ r$.
4. `lowExponentBound_pos_below_last_index` gives $c_1 > 0$ for $j < m$.

The lemma returns `Fam (nQ …) (LaQ …) c₁ d`. After the rewrites of $M$, $N_A$, $N_C$ and $q$, this is `Fam n Λ c₁ d`.

## In the Lean code

The theorem is in [CmFamilyFunctionalsDetectLowCoefficients.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/CmFamilyFunctionalsDetectLowCoefficients.lean#L92), with the helpers of steps 3 and 4. `DetectQ`, `FamQ`, `nAt` and `LaAt` are in [CarchAt.lean](lean:Development/AbelianVarietyTheory/Definitions/ArchimedeanThetaValues/CarchAt.lean#L34). `SSgt` is in [ModerateCoefficientPositivity.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FundamentalDomains/ModerateCoefficientPositivity.lean#L61).

- The proof builds `FactPrincipalDatum` and passes it to `exists_dataX_discr_absNorm`, which ignores it.
- We have not unfolded `MggK`. We use it only through `mem_forms_low_coeffs_vanish_iff_fourierJacobi`.
