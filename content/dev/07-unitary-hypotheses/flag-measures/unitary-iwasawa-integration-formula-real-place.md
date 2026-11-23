---
id: unitary-iwasawa-integration-formula-real-place
title: The integration formula for an isotropic flag of U(p, q), a second name
kind: theorem
decl: GlobalTheory.T.unitary_iwasawa_integration_formula_real_place
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.UnitaryIwasawaIntegrationFormulaRealPlaceStatement
covers: 330
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`iwasawaFormula`](/entry/iwasawa-formula/). That entry has the statement and the proof. Its user is [the bound for one flag class](/entry/bound/), which applies it at each real place and multiplies the results with `iwasawaNMKIntegration_pi_product`.

## Statement

**Theorem.** `IwasawaFormula` holds.

`IwasawaFormula` says the following. Let $G = U(p,q)$, let $W$ be an isotropic flag in $\mathbb{C}^{p+q}$ with steps $j_i$, and let $G = NMK$ be the decomposition along $W$. Normalize the Haar measures of $G$, $N$, $M$ by the volume of small Hilbert-Schmidt balls, and give $K$ the probability measure. Then

$$c \int_G \varphi = c_{\mathrm{Iw}}(p,q,j) \int_N \int_M \delta(m) \int_K \varphi(umk)$$

for every measurable $\varphi \ge 0$, with $\delta(m)$ an explicit product of powers of $|\det m|$ on the pieces $W_i/W_{i-1}$. The exact hypotheses are in [`iwasawaFormula`](/entry/iwasawa-formula/), and the constant $c_{\mathrm{Iw}}$ is in [`iwasawa_constant`](/entry/iwasawa-constant/).

## Proof

The proof applies `GlobalTheory.FlagMeas.iwasawaFormula`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [UnitaryIwasawaIntegrationFormulaRealPlaceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/UnitaryIwasawaIntegrationFormulaRealPlaceStatement.lean#L6). The statement `IwasawaFormula` is in [SameKindIsometric.lean](lean:Development/AbelianVarietyTheory/Statements/CuspFrameWeights/SameKindIsometric.lean#L60). The proof is a `first | exact ... | ...` combinator with three tries, and each try applies the same lemma. The file sets `maxHeartbeats 1000000`, which is not needed. The words "real place" in the name are not in the statement: it is about one group $U(p,q)$, with no number field.
