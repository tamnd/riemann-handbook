---
id: iwasawa-integration-formula-constant
title: The constant of the flag integration formula (statement)
kind: theorem
decl: GlobalTheory.T.iwasawa_integration_formula_constant
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.IwasawaIntegrationFormulaConstantStatement
covers: 327
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`IwConst.iwasawa_constant`](/entry/iwasawa-constant/). It has the same statement, and its proof is that lemma. Its one user is [`iwasawaFormula`](/entry/iwasawa-formula/), which joins it with the formula up to a constant. The mathematics is in [`iwasawa_constant`](/entry/iwasawa-constant/).

## Statement

Take the setting of [`iwasawaFormula`](/entry/iwasawa-formula/): the group $G = \mathrm{U}(p,q)$ with its Haar measure $\mu_G$, an isotropic flag with steps $j_1, \dots, j_a \ge 1$, the subgroups $N$, $M$, $K$, gauge measures $\mu_N$ and $\mu_M$, a left $K$-invariant probability measure $\mu_K$ on $K$, and the factor $\delta$.

**Theorem.** Let $c$ be a gauge constant for $\mu_G$ and $\kappa \in [0, \infty]$. Suppose that for every measurable $\varphi \colon G \to [0,\infty]$,
$$\int_G \varphi\, d\mu_G = \kappa \int_N \int_M \delta(m) \int_K \varphi(umk)\, d\mu_K\, d\mu_M\, d\mu_N.$$
Then $c\,\kappa = c_{Iw}(p,q,j)$.

## Proof

The proof is one line: it applies `GlobalTheory.IwConst.iwasawa_constant` to the same arguments.

## In the Lean code

The theorem is in [IwasawaIntegrationFormulaConstantStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/IwasawaIntegrationFormulaConstantStatement.lean#L6). The proof is the tactic `first | exact @GlobalTheory.IwConst.iwasawa_constant | ...`, The statement is copied word for word from `iwasawa_constant`, so the first branch suffices.
