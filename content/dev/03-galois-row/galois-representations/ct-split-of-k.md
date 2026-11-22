---
id: ct-split-of-k
title: The constant term split from five properties of the unfolded integral
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Act.ctSplit_of_k
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ThetaParseval.ThetaKernels.SiegelWeilActTop
covers: 460
status: drafted
drafted_by: writer@claude
---
This theorem proves the constant term split `CTSplit_k`. Its user is [the Siegel-Weil formula of the Galois row](/entry/siegel-weil-std-k/), which gives the result to [`siegelWeilStd_of_ct_k`](/entry/siegel-weil-std-of-ct-k/). `CTSplit_k` is the input of the induction on the rank $n$ in Step 5 of the [Siegel-Weil chapter](/proof/siegel-weil/). The theorem has two hypotheses, and it does not use them. Its proof puts five lemmas into `ctSplit_of_parts_k`. Below it are 460 declarations.

## Statement

**Theorem.** If `SiegelWeilDatumProperties` and `CoefEx_k` hold, then `CTSplit_k` holds.

[The constant term entry](/entry/siegel-weil-std-of-ct-k/) states `CTSplit_k` in words. The proof does not use the two hypotheses, so the theorem says only that `CTSplit_k` holds.

## Proof

The proof is `ctSplit_of_parts_k` applied to five lemmas. For $\operatorname{Re} z$ large, these lemmas say this about the integral over $\mathcal{U}$ of the $T$-th Fourier coefficient of the Eisenstein series:

1. `indepDom_k`: it does not depend on the fundamental domains $\mathcal{G}$ and $\mathcal{U}$. The lower rank term `first_k` does not depend on $\mathcal{G}'$.
2. `cptDom_k`: there are fundamental domains with compact closure.
3. `absConv_k`: on such domains, each term `kq_k` of the unfolded integral is integrable, and the norms of the terms are summable over the cosets of `par2` in `rat2`.
4. `firstEq_k`: the sum over the cosets in `FirstOrbit` is the lower rank term `first_k`. A coset $\gamma$ is in `FirstOrbit` when, in the frame, the entries $(i, i_0)$ of the lower left block of $\gamma$ are 0 for each $i$.
5. `secLaw_of_k (secUnf_of_k absConv_k)`: the sum $c_2$ over the other cosets, `secondOrbitSection`, has the law $c_2(\iota_w(y)\,x) = e^{\tau(n - 2z)} c_2(x)$ for each $y$ with `IsDil` of parameter $\tau$ (not unfolded here). `secLaw_of_k` gets this law from the unfolding [`secUnf_of_k`](/entry/sec-unf-of-k/).

`ctSplit_of_parts_k` takes the maximum of the three bounds on $\operatorname{Re} z$ and moves to compact domains with (2) and (1). There it writes the integral as a sum over cosets with `lhs_eq_tsum_k` and (3). It splits the sum into `FirstOrbit` and its complement. Then (4) gives the first part. The second part is $c_2$, and (5) gives its law.

## In the Lean code

The theorem is in [SiegelWeilActTop.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilActTop.lean#L17). The proof has the form `fun _ _ => …`. The five statements and `ctSplit_of_parts_k` are in [SiegelWeilActCut.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilActCut.lean#L126), and `FirstOrbit` and `secondOrbitSection` in [SiegelWeilActDefs.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilActDefs.lean#L19). The lemmas are in [IndepDomK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/IndepDomK.lean#L22), [AbsConvK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/AbsConvK.lean#L22) and [PsiTContPerK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/PsiTContPerK.lean#L149). We have not opened their proofs. The theorem is a copy of [`ctSplit_of`](/entry/ct-split-of/), which also ignores its two arguments.
