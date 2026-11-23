---
id: elliptic-side-direct
title: The trace of a test operator is its elliptic part
kind: theorem
decl: GlobalTheory.PsCo.Plug.ellipticSideDirect
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.EllTraceOfMiddleX
covers: 824
status: drafted
drafted_by: writer@claude
---
This theorem gives the geometric side of the trace formula that the [comparison of cuspidal multiplicities](/entry/unitary-theory-of-harish-chandra-langlands-alt/) uses. For a test function of the special form there, the trace of the right regular operator is the integral of the elliptic part of the kernel. The result $\mathrm{EllTraceX}$ is the fourth input of [`multEq_of_sides`](/entry/mult-eq-of-sides/). Below this theorem are 824 declarations.

## Statement

Let $V$ be a hermitian space of odd rank over the CM field $E/F$ of a datum $D$, with [[unitary group|0R9R0Y1HDK]] $G = G_V$. Let $\mu$ be a right invariant Haar measure on $G(\mathbb{A})$ that is the restricted product of $\mu_\infty$ and $\mu_f$. Call $(\lambda, M, T, U, f_\infty, f_f)$ *test data* if each $\lambda_\rho$ has large gaps, $M$ has parameters $\lambda$, $T$ has no fixed points, $f_\infty$ is an archimedean test function for $M$ and $f_f$ is a finite test function for $(T, U)$. Let $f = f_\infty \otimes f_f$.

**Theorem.** Suppose that $R_{\mathrm{cusp}}(h)$ is trace class for each smooth compactly supported $h$ on $G(\mathbb{A})$. Then for all test data, $R(f)$ has trace

$$\operatorname{tr} R(f) = \int_{G(F) \backslash G(\mathbb{A})} \sum_{\delta} f(x^{-1} \delta x) \, dx,$$

where $\delta$ runs over the $\delta \in G(F)$ whose characteristic polynomial is irreducible.

## Proof

The proof is `ellTrace_of_middleX` with eight inputs.

1. The constant terms of $f$ along the proper parabolics vanish (`parabolicT`). By the hypothesis and `cuspidalOperators_vanishingRadicalIntegrals_unitaryGroup`, $R(f)$ is then a cuspidal trace class operator, and its trace is the integral of its kernel on the diagonal.
2. A rational $\delta$ with $f(x^{-1}\delta x) \neq 0$ is regular semisimple, because of the Iwahori condition in $f_f$ (`iwahoriEigenvalues`).
3. Regroup the kernel by rational conjugacy classes. Only finitely many classes meet the support (`siegel_implies_regular_class_finite`), and each class kernel is integrable (`regClassInt_holds`). So integral and sum commute.
4. A class with reducible characteristic polynomial gives $0$. If it is of non-field anisotropic type, use `nonFieldT`. If not, `hyperZero_of_intX` conjugates $\gamma$ into a standard Levi subgroup. There the centralizer is noncompact at an archimedean place, so the archimedean orbital integral of $f_\infty$ is $0$.
5. The classes that remain have irreducible characteristic polynomial. Their sum is the elliptic kernel.

## In the Lean code

The theorem is in [EllTraceOfMiddleX.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EllTraceOfMiddleX.lean#L186). The statement $\mathrm{EllTraceX}$ and the test data `IsTestDataX` are in [TestFnConstTermVanishX.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/TestFnConstTermVanishX.lean#L267). The hypothesis is `CuspTraceClass`, in [CuspDiscreteDecompositionOfTraceClass.lean](lean:PublishedTheorems/TwistedTraceFormula/CuspDiscreteDecompositionOfTraceClass.lean#L21). The elliptic kernel is `ellKernel`.

The lemmas it calls:

- `ellTrace_of_middleX`, `hyperX` and `hyperZero_of_intX`, in the same file.
- `parabolicT` and `nonFieldT`, in NonFieldTypeVanishingX.lean.
- `cuspidalOperators_vanishingRadicalIntegrals_unitaryGroup`, `regularSemisimple_unitaryGroup_concrete`, `iwahoriEigenvalues`, `regClassInt_holds` and `siegel_implies_regular_class_finite`.

`ellTrace_of_middleX` takes the hypothesis `RegularSemisimple` as `_hRS` and does not use it ([line 92](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EllTraceOfMiddleX.lean#L92)). The same fact is used through `hyperZero_of_intX`. The call passes `CompanionTheory.Prw.siegelCore_holds`, of type `CompanionTheory.ThKR.SiegelCore`, where `siegel_implies_regular_class_finite` asks for `PositivityTheory.ThKR.SiegelCore`. These are two copies of one definition, with the same text, in [SiegelCore.lean](lean:Development/WeilBound/ThetaLifts/Reductions/SiegelCore.lean#L37) and in a second SiegelCore.lean under `CompanionTheory/ThickeningEstimates`. The call type checks because the two bodies agree.
