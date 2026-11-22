---
id: sec-unf-of-c-law-k
title: The unfolding of the second orbit term from a Weyl element and a change of variables
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Act.secUnf_of_cLaw_k
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ThetaParseval.ThetaKernels.SecUnfOfCLawK
covers: 305
status: drafted
drafted_by: writer@claude
---
This theorem proves the unfolding `SecUnf_k` from absolute convergence `AbsConv_k` and the existence statement `CLawEx_k`. Its user is [`secUnf_of_k`](/entry/sec-unf-of-k/), which proves `CLawEx_k` with `cLawEx_k`. The theorem only repackages its hypotheses for the lemma `C5.unf_k`. The real content is in `C5.unf_k` and `cLawEx_k`. Below it are 305 declarations.

## Statement

**Theorem.** If `AbsConv_k` and `CLawEx_k` hold, then `SecUnf_k` holds.

`SecUnf_k` is stated in [the parent entry](/entry/sec-unf-of-k/). `CLawEx_k` says that each datum has $w_1$, $c_M$ and $\kappa$ with these properties:

- $w_1$ is rational. In the frame it is the identity, except that the block at the two positions $i_0$ is $\begin{pmatrix} 0 & a \\ b & 0 \end{pmatrix}$ with $a, b \neq 0$ in $E$.
- $c_M$ is continuous, and $\kappa$ is an additive Haar measure.
- For some $\delta \neq 0$ in $E$, each $c_M(u, r)$ is block upper triangular, with upper left block $1 + \sum_j u_j\, e_{i_0, e(j)}$ and upper right block $r \delta\, e_{i_0 i_0}$.
- The law `CLaw_k`. For each $y$ with `IsDil` of parameter $\tau$: $y$ commutes with the embedding $j$; $w_1 \iota_w(y) = p\, w_1$ with `IsPar p t`, $\lvert \det t \rvert = e^{-2\tau}$ and $\chi(\det t) = 1$; and $c_M(c)\, \iota_w(y) = \iota_w(y)\, c_M(s(c))$ for a change of variables $s$ with $s_* \kappa = e^{2n\tau} \kappa$.

## Proof

Take the bound on $\operatorname{Re} z$ from `AbsConv_k`, and $w_1$, $c_M$, $\kappa$, $\delta$ from `CLawEx_k`. Put the matrix shapes, the shape of $u_M$ from `UData` and the two `IsNMap` facts into the structure `C5.Hyp_k`. Then `C5.unf_k` gives $K$ and the formula. Its factor `C5.th'_k T' β` is $\psi(-\operatorname{tr}(T'\beta))$. `CLaw_k` is not an input of `C5.unf_k`. It goes to the conclusion unchanged. We have not opened the proof of `C5.unf_k`.

## In the Lean code

The theorem is in [SecUnfOfCLawK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SecUnfOfCLawK.lean#L21). `CLawEx_k` is in [CLawExK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/CLawExK.lean#L20), `C5.Hyp_k` in [EisensteinSecondTerm.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/EisensteinSecondTerm.lean#L20), and `C5.unf_k` in [UnfK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/UnfK.lean#L32). The hypothesis that the closure of $\mathcal{G}'$ is compact is introduced at [L24](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SecUnfOfCLawK.lean#L24) and not used. The theorem is a copy of [`secUnf_of_cLaw`](/entry/sec-unf-of-c-law/).
