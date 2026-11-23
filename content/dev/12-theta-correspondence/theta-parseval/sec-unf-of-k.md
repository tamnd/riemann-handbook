---
id: sec-unf-of-k
title: The unfolding of the second orbit term from absolute convergence
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Act.secUnf_of_k
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ThetaParseval.ThetaKernels.SecUnfOfCLawK
covers: 318
status: drafted
drafted_by: writer@claude
---
This theorem proves the unfolding `SecUnf_k` of the second orbit term from `AbsConv_k`. Its user is [`ctSplit_of_k`](/entry/ct-split-of-k/), which applies it to `absConv_k` and then gets the law of the second term with `secLaw_of_k`. The theorem is a pass-through. It fills one hypothesis of [`secUnf_of_cLaw_k`](/entry/sec-unf-of-c-law-k/), and that entry describes the argument. Below it are 318 declarations.

## Statement

**Theorem.** If `AbsConv_k` holds, then `SecUnf_k` holds.

`AbsConv_k` is item 3 of [the parent entry](/entry/ct-split-of-k/). `SecUnf_k` says: for $\operatorname{Re} z$ large and for fundamental domains with compact closure, there are an element $w_1$, a map $c_M$ and a measure $\kappa$ that satisfy the law `CLaw_k`, and a constant $K$, such that for each $x$

$$c_2(x) = K \sum_{q'} \int_{\mathcal{G}'} \Bigl(\int \varphi_z\bigl(w_1\, c_M(c)\, j(q'\, n'(\beta))\, x\bigr)\, d\kappa(c)\Bigr)\, \psi\bigl(-\operatorname{tr}(T'\beta)\bigr)\, d\lambda'(\beta).$$

Here $c_2$ is `secondOrbitSection`, the sum over the cosets outside `FirstOrbit`. The sum over $q'$ runs over the cosets of the lower rank problem, and $\varphi_z(x) = \mathrm{Ht}(x)^{z - s_1} f(x)$ is `phz_k`.

## Proof

The proof is `secUnf_of_cLaw_k hA cLawEx_k`. The lemma `cLawEx_k` gives the element $w_1$, the map $c_M$ and the measure $\kappa$. We have not opened its proof.

## In the Lean code

The theorem is in [SecUnfOfCLawK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SecUnfOfCLawK.lean#L30). `SecUnf_k` and `CLaw_k` are in [SiegelWeilActCut.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilActCut.lean#L48), and `cLawEx_k` in [CLawExK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/CLawExK.lean#L29). The theorem is a copy of [`secUnf_of`](/entry/sec-unf-of/) with `_k` added to each name.
