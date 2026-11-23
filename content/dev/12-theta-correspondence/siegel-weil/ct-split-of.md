---
id: ct-split-of
title: The constant term split of the Siegel Eisenstein series
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Act.ctSplit_of
module: Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.SiegelWeilActions.CtSplitOf
covers: 464
status: drafted
drafted_by: writer@claude
---
This theorem proves the constant term split `CTSplit`, the input of the induction on the rank $n$ in Step 5 of the [Siegel-Weil chapter](/proof/siegel-weil/). Its user is [`siegelWeilStd`](/proof/siegel-weil/), which gives it to [`siegelWeilStd_of_ct`](/entry/siegel-weil-std-of-ct/). The theorem has two hypotheses and does not use them. Its proof puts five lemmas into `ctSplit_of_parts`. Below it are 464 declarations.

## Statement

**Theorem.** If `AuxiliaryPrimeFunction` and `CoefEx` hold, then `CTSplit` holds.

[`siegelWeilStd_of_ct`](/entry/siegel-weil-std-of-ct/) states `CTSplit` in words: for $\operatorname{Re} z$ large, the integral over $\mathcal{U}$ of the $T$-th Fourier coefficient of the [[Eisenstein series|3NZBZXYWAJ]] is the $T'$-th coefficient of a lower rank Eisenstein series plus a term $c_2$ with $c_2(\iota_w(y)\,x) = e^{\tau(n - 2z)} c_2(x)$. Since the hypotheses are unused, the theorem says only that `CTSplit` holds.

## Proof

The proof is `ctSplit_of_parts` applied to five lemmas, all for $\operatorname{Re} z$ large:

1. `indepDom`: the integrals do not depend on the choice of the [[fundamental domains|WEGEXJBX26]] $\mathcal{G}$, $\mathcal{U}$ and $\mathcal{G}'$.
2. `cptDom`: there are fundamental domains with compact closure.
3. `absConv`: on such domains, each term of the unfolded integral is integrable, and the norms are summable over the cosets of `par2` in `rat2`.
4. `firstEq`: the sum over the cosets $\gamma$ with `LagrangianCondition` (the entries $(i, i_0)$ of the lower left block of $\gamma$ in the frame are 0) is the lower rank term `first`.
5. `secLaw_of (secUnf_of absConv)`: the sum `sec2` over the other cosets has the law of $c_2$. The unfolding is [`secUnf_of`](/entry/sec-unf-of/).

`ctSplit_of_parts` moves to compact domains with (1) and (2), writes the integral as a sum over cosets with `lhs_eq_tsum` and (3), and splits the sum into the two sets of cosets. Then (4) and (5) give the two terms.

## In the Lean code

The theorem is in [CtSplitOf.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/CtSplitOf.lean#L10). Its proof begins `fun _ _ =>`, so `siegelWeilStd` passes `kfour.auxEx` and `kfour.coefEx` for nothing. The five statements and `ctSplit_of_parts` are in [CtSplitOfParts.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/CtSplitOfParts.lean#L137), and `LagrangianCondition`, `sec2` and `first` in [LagrangianCondition.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/LagrangianCondition.lean#L19). We have not opened the proofs of `indepDom`, `absConv` and `firstEq`. The copy [`ctSplit_of_k`](/entry/ct-split-of-k/) has the same form.
