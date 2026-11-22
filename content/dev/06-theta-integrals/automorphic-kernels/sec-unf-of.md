---
id: sec-unf-of
title: The unfolding of the second orbit term from absolute convergence
kind: theorem
decl: PositivityTheory.SiegelWeilFormula.Act.secUnf_of
module: Development.WeilBound.CoreStatements.AutomorphicKernels.SiegelWeilFormula.SiegelWeilActions.SecUnfOfCLaw
covers: 319
status: drafted
drafted_by: writer@claude
---
This theorem proves the unfolding `SecUnf` of the second orbit term from `AbsConv`. Its user is [`ctSplit_of`](/entry/ct-split-of/), which applies it to the theorem `absConv` and gets the law of the second term with `secLaw_of`. The theorem is a pass-through. It fills one hypothesis of [`secUnf_of_cLaw`](/entry/sec-unf-of-c-law/), and the real content is in [the unfolding lemma](/entry/unf/). Below it are 319 declarations.

## Statement

**Theorem.** If `AbsConv` holds, then `SecUnf` holds.

`AbsConv` is stated in [the entry below](/entry/sec-unf-of-c-law/). `SecUnf` says: for $\operatorname{Re} z$ large, for coefficient data on $d$ and on $L$ and for `UData`, all with fundamental domains of compact closure, and for $T$, $T'$ with `IsSub`, there are $w_1$, $c_M$ and $\kappa$ with the law `CLaw`, and a constant $K$, such that for each $x$

$$c_2(x) = K \sum_{q'} \int_{\mathcal{G}'} \Bigl(\int \varphi_z\bigl(w_1\, c_M(c)\, j(q'\, n'(\beta))\, x\bigr)\, d\kappa(c)\Bigr)\, \psi_{T'}(\beta)\, d\lambda'(\beta).$$

Here $c_2$ is the second orbit term `sec2`, as in [the unfolding lemma](/entry/unf/).

## Proof

The proof is `secUnf_of_cLaw hA cLawEx`. The theorem `cLawEx` constructs $w_1$, $c_M$, $\kappa$ and $\delta$, with $a = 1$ and $b = \varepsilon$ (the sign of $R$) in the frame matrix of $w_1$ in `CLawEx`. We have not opened the lemmas `CL.ptEx'`, `CL.measEx'` and `CL.deltaEx'` that its proof calls.

## In the Lean code

The theorem is in [SecUnfOfCLaw.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/SecUnfOfCLaw.lean#L23). `SecUnf` is in [CtSplitOfParts.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/CtSplitOfParts.lean#L52), and `cLawEx` in [ContSingle.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/ContSingle.lean#L35). The hypothesis `AbsConv` is itself proved, as `absConv` in [ParabolicUnipotents.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilActions/ParabolicUnipotents.lean#L33), so `SecUnf` holds outright. The copy [`secUnf_of_k`](/entry/sec-unf-of-k/) has the same form.
