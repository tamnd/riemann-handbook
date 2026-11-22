---
id: lemma-k-lit-n-alt
title: The bound on the second Galois cohomology, from the literature hypothesis
kind: theorem
decl: UpperTheory.V.ZK.lemmaK_litN_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.KFinal
covers: 2836
status: drafted
drafted_by: writer@claude
---
This theorem gives the constant $C_K$ of Lemma K, the bound on $H^2$ that [the window from hypotheses H](/entry/vwin-of-hypotheses-h-e-alt/) uses as `hK`. It only passes its hypothesis along. The largest part of its proof is [the rank bound for odd degrees](/entry/b-odd/), which in turn is a new name for [`bOdd_zk`](/entry/b-odd-zk/).

## Statement

Let $l$ be a prime and $L$ a totally complex number field that contains a primitive root of unity of order $l$ (of order 4 if $l = 2$). Let $S$ be the set of places of $L$ above $l$, let $G_S$ be the Galois group of the maximal extension of $L$ unramified outside $S$ and the infinite places, and let $\chi \colon G_S \to \mathbb{Z}_l^\times$ be the $l$-adic [[cyclotomic character|XSGB5K2KEG]]. Put $n = [L : \mathbb{Q}]$ and $D = |\mathrm{disc}\, L|$. `LemmaK` $C_K$ says: for each $e \ge 1$ the [[Galois cohomology|9MPCZ3EAJM]] group $H^2(G_S, \mathbb{Z}_l(\chi^{e+1}))$ is finite, and
$$\log \# H^2\bigl(G_S, \mathbb{Z}_l(\chi^{e+1})\bigr) \le \exp\bigl((2en)^{C_K} \log(2D)\bigr).$$

**Theorem.** If `LiteratureRankNHypothesis` holds, then there is $C_K$ with `LemmaK` $C_K$.

## Proof

The proof is one line, `lemmaK_of_litN_alt hN bOdd`. The theorem `lemmaK_of_litN_alt` is itself one line: it calls `lemmaK` with `bOdd` and with three statements taken from the hypothesis: Poitou-Tate duality (`pt_s hN`), local finiteness `hN.coh.lfK` and local Tate duality `hN.coh.ltK`. Then `lemmaK` calls `lemmaK_of_steps` with these and about twenty further step lemmas. The only input that is proved here and not taken from the hypothesis is `bOdd`.

## In the Lean code

- The theorem is in [KFinal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/KFinal.lean#L11). `LemmaK` is in [LemmaK.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GeneratorCountTuples/LemmaK.lean#L13).
- `lemmaK_of_litN_alt` is in [DenseThresholdCases/LemmaKOfLitN.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LemmaKOfLitN.lean#L12), and `lemmaK` in a file of the same name, [ClassCounting/LemmaKOfLitN.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/LemmaKOfLitN.lean#L28).
- So the theorem is a wrapper around a wrapper. We have not unfolded `lemmaK_of_steps`.
