---
id: num-good-of-fam-q
title: The coefficient functional of a CM arc datum has controlled height
kind: theorem
decl: GlobalTheory.ArcCM.numGood_of_famQ
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.CmArcDatumFamilyFunctionalBoundedLinearOnCuspFor
covers: 629
status: drafted
drafted_by: writer@claude
---
This theorem shows that the coefficient functional $\phi_d$ of an arc datum $d$ in the CM family is linear on cusp forms and has controlled size at every place. It reaches [`qat_of_kill_detect`](/entry/qat-of-kill-detect/) through its statement form [`cmArcDatumFamily_functional_bounded_linear_on_cuspForms`](/entry/cm-arc-datum-family-functional-bounded-linear-on-cusp-forms/). The bound at the finite places is [`cmArcDatum_functional_finite_integrality_bound`](/entry/cm-arc-datum-functional-finite-integrality-bound/).

## Statement

Use $K$, $S_\kappa$, $M_\kappa$, $\|F\|_\sigma$, the family `FamQ`, $\phi_d$, $n$, $\Lambda$ and $c_1$ from [the entry for `qat_of_kill_detect`](/entry/qat-of-kill-detect/).

*Metrized lines.* A metrized line $N$ over a number field $K_1$ (`MLine`) is a fractional ideal $I_N$ with a number $n_\sigma(N)$ for each embedding $\sigma \colon K_1 \to \mathbb{C}$. Its normalized degree is $\widehat{\deg}(N) = -[K_1 : \mathbb{Q}]^{-1}\bigl(\log N(I_N) + \sum_\sigma \log n_\sigma(N)\bigr)$. It is good if $I_N \ne 0$ and all $n_\sigma > 0$.

*`NumGood`* $(M, \|\cdot\|, \beta, C_{\mathrm{arch}}, B_{\deg}, K_1, \phi)$. There is a good metrized line $N$ over $K_1$ with $\widehat{\deg}(N) \le B_{\deg}$ and $n_{\bar\sigma} = n_\sigma$, such that for each $F \in M$ with $\phi(F) \neq 0$:

1. for each prime $w$ of $K_1$ over $\lambda$ of $K$: $\operatorname{ord}_w \phi(F) - \operatorname{ord}_w I_N \ge -e(w|\lambda)\,\beta(\lambda)$;
2. for each $\sigma \colon K_1 \to \mathbb{C}$: $\log|\sigma\phi(F)| + \log n_\sigma(N) \le \log\|F\|_{\sigma|_K} + C_{\mathrm{arch}}$.

**Theorem.** Assume `Known` and `GamAt T`, and let $j \in [1, m)$. Let $d$ be an arc datum over $K_1$ in the family. Then there is a $K$-linear $\phi \colon S_\kappa \to K_1$ with $\phi = \phi_d$, and `NumGood` holds on $M_\kappa$ with

$$\beta(\lambda) = A \max\bigl(v_\lambda(d_E), v_\lambda(n)\bigr),\quad C_{\mathrm{arch}} = 4\pi + a\,|\kappa|,\quad B_{\deg} = \bigl(\tfrac12(1 + |\log\Omega|) + \tfrac12 \log\Lambda\bigr)|\kappa|,$$

where $A$ is the total weight of $\kappa$, $a = \tfrac12 \log\max(1, c_1) + \log\Lambda + \log \mathrm{rd}_E + \log r$ and $\log\Omega$ is `logOm` of the size data.

## Proof

1. `cfOf_linear_and_degree` says that $\phi_d$ is linear on the sections of weight $\kappa$, and that $\phi_d(F) \ne 0$ forces $|\mu| = A$. Restrict it to $S_\kappa$ to get $\phi$.
2. If $|\mu| \ne A$, then $\phi = 0$. Take $N$ trivial; conditions 1 and 2 are empty and $\widehat{\deg}(N) = 0 \le B_{\deg}$.
3. If $|\mu| = A$, take for $N$ the line `valLine` $\mu$ of the CM data. `valLine_ndeg_le` shows that $N$ is good and bounds $\widehat{\deg}(N)$; with $A + f r n_\kappa \le |\kappa|$ (`absA_add_le_size`) this is at most $B_{\deg}$. `cmValueLine_length_conj_eq` gives $n_{\bar\sigma} = n_\sigma$.
4. Condition 1 is [`cmArcDatum_functional_finite_integrality_bound`](/entry/cm-arc-datum-functional-finite-integrality-bound/), applied with `modelsAt_of_good_level`.
5. Condition 2 is `arch_all`. For an embedding with `GoodEmb`, `arch_good` uses `norm_cmArcCoefficientFunctional_le` to get $|\sigma\phi(F)|\, n_\sigma(N) \le \|F\|_\sigma e^{C_{\mathrm{arch}}}$. For the other embeddings it applies this to $\bar\sigma$ and uses the symmetry of $\|F\|_\sigma$ (`recB_supN_conj`). Take logarithms.

## In the Lean code

The theorem is in [CmArcDatumFamilyFunctionalBoundedLinearOnCuspFor.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/CmArcDatumFamilyFunctionalBoundedLinearOnCuspFor.lean#L152), with `arch_good` and `arch_all` at [L91](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/CmArcDatumFamilyFunctionalBoundedLinearOnCuspFor.lean#L91) and [L131](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/CmArcDatumFamilyFunctionalBoundedLinearOnCuspFor.lean#L131). `NumGood`, `CMIn` and `valLine` are in [ModelsAt.lean](lean:Development/AbelianVarietyTheory/Definitions/ArchimedeanThetaValues/ModelsAt.lean#L181), `MLine` in [DetIdeal.lean](lean:Formalism/LocalToGlobal/CMDeterminantIdeals/DetIdeal.lean#L10) and `cfOf` in [FunDef.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ArchimedeanQuadraticData/ArcLineFunctions/FunDef.lean#L17). We have not unfolded `CMIn` beyond its fields, the arc ring `ArcS` or `norm_cmArcCoefficientFunctional_le`.

- The hypothesis $j < m$ is not used: it is introduced as `_` at line 153.
- `cfOf` takes a chosen polynomial preimage of the value of $F$ in the arc ring, and $0$ if there is none.
- The facts $f = [E:\mathbb{Q}]/2$ and $p + q = r$ used in step 3 come from `numerics_of_pins`.
