---
id: sec-unf-of-c-law
title: The unfolding of the second orbit term from a Weyl element and a change of variables
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Act.secUnf_of_cLaw
module: Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.SiegelWeilActions.SecUnfOfCLaw
covers: 306
status: drafted
drafted_by: writer@claude
---
This theorem proves the unfolding statement `SecUnf` from absolute convergence `AbsConv` and the existence statement `CLawEx`. Its user is [`secUnf_of`](/entry/sec-unf-of/), which proves `CLawEx` with the theorem `cLawEx`. The theorem only repackages its hypotheses for [the unfolding lemma](/entry/unf/) `C5.unf`, which has the real content. Below it are 306 declarations.

## Statement

**Theorem.** If `AbsConv` and `CLawEx` hold, then `SecUnf` holds.

`SecUnf` is stated in [the parent entry](/entry/sec-unf-of/). `AbsConv` says: for $\operatorname{Re} z$ large and for fundamental domains $\mathcal{G}$, $\mathcal{U}$ with compact closure, each term of the second orbit term $c_2$ is absolutely integrable, and the absolute integrals are summable over the cosets. `CLawEx` says that for each $d$, $R$ and $L$ there are $w_1$, $c_M$ and $\kappa$ with these properties:

- $w_1$ is rational, with the frame matrix of `C5.Hyp` (the block $\begin{pmatrix} 0 & a \\ b & 0 \end{pmatrix}$ at the two positions $i_0$, $a, b \neq 0$);
- $c_M$ is continuous, $\kappa$ is an additive Haar measure, and for some $\delta \neq 0$ each $c_M(u, r)$ has the block upper triangular shape of `C5.Hyp`;
- the law `CLaw`. For each $y$ with `IsDil` of parameter $\tau$ (not unfolded here): $j(g)$ commutes with $\iota_w(y)$; $w_1 \iota_w(y) = p\, w_1$ with `IsPar p t`, $\lvert \det t \rvert = e^{-2\tau}$ and $\chi(\det t) = 1$; and $c_M(c)\, \iota_w(y) = \iota_w(y)\, c_M(s(c))$ for a change of variables $s$ with $s_* \kappa = e^{2n\tau} \kappa$.

## Proof

Take the bound on $\operatorname{Re} z$ from `AbsConv`. Take $w_1$, $c_M$, $\kappa$ and $\delta$ from `CLawEx`. Put the matrix shapes, the shape of $u_M$ from `UData` and the two `IsNMap` facts from `CoefData` into the structure `C5.Hyp`. Then `C5.unf` gives $K$ and the formula. `CLaw` is not an input of `C5.unf`. It goes to the conclusion unchanged, and `secLaw_of` uses it later.

## In the Lean code

The theorem is in [SecUnfOfCLaw.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/SecUnfOfCLaw.lean#L13). `AbsConv`, `CLaw` and `SecUnf` are in [CtSplitOfParts.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/CtSplitOfParts.lean#L28), and `CLawEx` in [ContSingle.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/ContSingle.lean#L18).

- The hypothesis `hk'` (the closure of $\mathcal{G}'$ is compact) is introduced and not used. The hypotheses `hk` and `hkU` are used only to call `AbsConv`.
- The choice of $w_1$, $c_M$, $\kappa$ from `CLawEx` does not depend on $f$, $z$ or the fundamental domains.
- The copy [`secUnf_of_cLaw_k`](/entry/sec-unf-of-c-law-k/) has the same form.
