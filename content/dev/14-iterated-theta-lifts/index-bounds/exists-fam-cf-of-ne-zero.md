---
id: exists-fam-cf-of-ne-zero
title: A nonzero low Fourier-Jacobi coefficient gives a CM arc datum that sees it
kind: theorem
decl: GlobalTheory.ArcDetect.exists_fam_cfOf_ne_zero
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.ExistsFamilyMemberFunctionalNeZero
covers: 797
status: drafted
drafted_by: writer@claude
---
This theorem turns a nonzero low Fourier-Jacobi coefficient of a cusp form $F$ into a member $d$ of the CM family with $\phi_d(F) \neq 0$. It is the proof of [`exists_familyMember_functional_ne_zero`](/entry/exists-family-member-functional-ne-zero/), which [`detectQ_of_known`](/entry/detect-q-of-known/) uses. The proof finds a good split point, builds CM arc data there, and reads the coefficient off the arc.

## Statement

Let $E$ be a CM field, $X_o$ and $c$ a moduli datum and a coefficient datum with field $K = c.F$, and $U$ a uniformisation of rank $r$ along $K \subset \mathbb{C}$. Let $k$ be a component of $U$, with lattice data $X$ (`DataX`) over $U.X_k$. For a section $F$ of weight $(a', n)$, let $\rho_{k'}(F)$ be its reading at $k'$, of weight $\lambda_{k'} = $ `laU U a' n k'`. The sets $\mathrm{SS}(\lambda)$ and $\mathrm{SS}_{>c_1}(\lambda)$ are as in [`detectQ_of_known`](/entry/detect-q-of-known/).

**Theorem.** Assume `Known` and:

- `ModelsAt Xo c`, `IsUnf U`, $A = 1$ for the level, $r \ge 3$, and `HasPrinc U M`;
- $(a', n)$ is dominant (`Dom`), and the character of weight $\lambda_{k'}$ is trivial on $\Gamma_{k'}$ for all $k'$;
- a nonzero fractional ideal $\mathfrak{A}$ of $E$ with $\Lambda = \mathfrak{A} L'$ in $X$, and $g = M$;
- $c_1 > 0$ and $|a'| + \tfrac12 [E:\mathbb{Q}]\, n + r \le w$.

Let $\rho_{k'}(F) \in \mathrm{SS}(\lambda_{k'})$ for all $k'$ and $\rho_k(F) \notin \mathrm{SS}_{>c_1}(\lambda_k)$. Then there are a number field $K_1$ over $K$ and an arc datum $d$ over $K_1$ with `Fam (nQ …) (LaQ …) c₁ d` and $\phi_d(F) \neq 0$.

## Proof

1. **A split point.** [`exists_split`](/entry/exists-split/) calls `FJDetect.exists_fj_ne_zero_at_split_point'`. It gives an isotropic $\xi$, an exponent $\nu$ with $\sum_\tau \nu_\tau \le c_1$, a point $x$ with split data at the scale `LaQ …`, and $\mathrm{fj}_{\xi,\nu}(\rho_k F)(x) \neq 0$. The weight hypotheses enter through `laU_dominant` and `sum_spread_le`.
2. **The frequency.** `FjFreq.freq_real_nonneg_integral` gives $\nu_0 \in E$, fixed by complex conjugation, with $\nu_\tau = \operatorname{Re} \tau(\nu_0)$. `sum_re_cmType_eq_half_trace` turns $\sum \nu_\tau \le c_1$ into $\tfrac12 \operatorname{Tr}_{E/\mathbb{Q}} \nu_0 \le c_1$.
3. **CM arc data.** `nonempty_unfWit_of_isUnf` and `transvIn_of_hasPrinc` supply the inputs of `exists_cmArcData_at_splitIsotropicPoint`. It gives $K_1$, an arc, letters, a theta section, an exponent $j_0$ and a CM input $s$ with $s.\nu_0 = \nu_0$, tied to $(\xi, x)$ by `Comparison₂`.
4. **The arc datum.** `exists_place 2` gives a valuation ring of $\mathbb{C}$ in which $2$ is not a unit, and `ModelsAt` gives a model there. `ArcDatumExists.exists_arcDatum`, with `cmLetters_isLieBasis_along_arc`, builds $d$ and proves `Std d`.
5. **The coefficient.** `detect_of_tie` calls `exists_coeff_ne_zero_of_fourierJacobi_arcDatum`. It gives a monomial $\mu$ with a nonzero coefficient at $(\mu, j_0)$. Put $\mu$ into $d$. Then $\phi_d(F) \neq 0$.

## In the Lean code

The theorem is in [ExistsFamilyMemberFunctionalNeZero.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/ExistsFamilyMemberFunctionalNeZero.lean#L178), with the helpers of steps 1, 4 and 5.

- The monomial of an arc datum is a free field. The proof builds $d$ with monomial $0$ and then replaces it. So `Fam` puts no condition on $\mu$.
- The prime $2$ in step 4 is a free choice.
- We have not unfolded `SplitData` or `Comparison₂`.
