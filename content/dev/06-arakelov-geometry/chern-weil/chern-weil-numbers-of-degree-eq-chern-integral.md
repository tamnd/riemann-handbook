---
id: chern-weil-numbers-of-degree-eq-chern-integral
title: The Chern-Weil formula from the degree formula for line bundles (restatement)
kind: theorem
decl: GlobalTheory.T.chernWeilNumbers_of_degree_eq_chernIntegral
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ChernWeilNumbersOfDegreeEqChernIntegralStatement
covers: 762
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`ChernCalc.chernWeilNumbers_of_chernDegreeComplex`](/entry/chern-weil-numbers-of-chern-degree-complex/), and that entry has the real content. Its only caller is [`ChernDegree.chernWeilNumbers_holds`](/entry/chern-weil-numbers-holds/), which supplies the hypothesis.

## Statement

**Theorem.** $\mathrm{ChernDegreeComplex}$ implies $\mathrm{ChernWeilNumbers}$.

$\mathrm{ChernDegreeComplex}$ says: for a smooth projective variety $Y$ of dimension $n$ over $\mathbb{C}$, a divisor $\Delta$ given by rational sections of a line bundle $L$, and a smooth hermitian metric $\varphi$ on $L$, the form $c_1(L, \varphi)^n$ is integrable on $Y(\mathbb{C})$ with integral $\Delta^n$. $\mathrm{ChernWeilNumbers}$ says: for a smooth hermitian metric $H$ on a family $E$ of vector bundles on $X$, and a full flag of $E$ on $Y$ with graded divisors $x_{\tau,i}$, the integral of $R(c(E, H))$ over $X(\mathbb{C})$ is $\int_Y R(x)\, \varpi$. Both are stated in more detail in [the entry that proves the hypothesis](/entry/chern-weil-numbers-holds/) and in [the restatement of the conclusion](/entry/chern-numbers-eq-integral-chern-forms-smooth-metric/).

So the theorem passes from line bundles over $\mathbb{C}$ to vector bundles over any field $F$ with an embedding $\sigma \colon F \to \mathbb{C}$.

## Proof

The proof is `first | exact @GlobalTheory.ChernCalc.chernWeilNumbers_of_chernDegreeComplex | ...`. The first branch closes the goal.

## In the Lean code

The theorem is in [ChernWeilNumbersOfDegreeEqChernIntegralStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChernWeilNumbersOfDegreeEqChernIntegralStatement.lean#L11). The proof that it names is in [ChernWeilNumbersOfDegreeEqChernIntegral.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChernWeilNumbersOfDegreeEqChernIntegral.lean#L21). The statement $\mathrm{ChernDegreeComplex}$ is in [ChernDegreeComplex.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/ChernDegreeComplex.lean#L12).
