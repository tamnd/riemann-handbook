---
id: one-use
title: A form congruent to 1 in a large weight
kind: theorem
decl: UpperTheory.V.Lit.oneUse
module: Development.AutomorphicArithmetic.AutomorphicVarieties.GaussSumFiltrations.ExistsHilbertModularFormCongrOne
covers: 584
status: drafted
drafted_by: writer@claude
---
This theorem gives, for each totally real field $F$, odd prime $p$ and bound $B$, a holomorphic Hilbert modular form of level one and weight $k \geq B$, with $p - 1 \mid k$, whose $q$-expansion is $p$-adically close to $1$. It fills the field `one` of the hypotheses `Hypotheses4Z'` that [the case II seed](/entry/seed-iis-alt/) builds. It only passes facts along: the real content is in [`hilbertOne`](/entry/hilbert-one/).

## Statement

Fix an isomorphism $\iota \colon \overline{\mathbb{Q}}_p \to \mathbb{C}$.

**Theorem** (`OneUse`). For each $B$ there are $k \geq B$ with $k > 0$ and $p - 1 \mid k$, and a form $\varphi$ with $q$-expansion coefficients $c_0(y)$ and $c(\mathfrak{m})$ (`HasExp φ k c₀ c`), such that $\varphi$ is holomorphic of parallel weight $k$, level exponent $0$ at every place and trivial central character (`IsHol k (fun _ => 0) 1 φ`), and
$$\|\iota^{-1}(c_0(y)) - 1\| < 1 \text{ for all } y, \qquad \|\iota^{-1}(c(\mathfrak{m}))\| < 1 \text{ for all } \mathfrak{m} \neq 0.$$

## Proof

[`exists_hilbertModularForm_congr_one`](/entry/exists-hilbert-modular-form-congr-one/) gives an $N$ such that the same form exists in every weight $k > 0$ with $(p-1)p^N \mid k$. The proof `oneUse_of` takes $k = (p-1)p^N(B+1)$. Then $k > 0$, $k > B$ and $p - 1 \mid k$.

## In the Lean code

The theorem is in [ExistsHilbertModularFormCongrOne.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/ExistsHilbertModularFormCongrOne.lean#L8). `OneUse` and `oneUse_of` are in [OneUseOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/OneUseOf.lean#L9), and `Hypotheses4Z'` is in [Hypotheses4Z.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/Hypotheses4Z.lean#L9).

`OneUse` and `HilbertOne` have the same conclusion. Only the condition on $k$ is different.
