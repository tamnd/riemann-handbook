---
id: lemma-k-of-lit-n-alt
title: Lemma K from the literature hypothesis and the odd rank bound
kind: theorem
decl: UpperTheory.V.ZK.lemmaK_of_litN_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.LemmaKOfLitN
covers: 636
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. It takes three Galois cohomology statements out of `LiteratureRankNHypothesis` and gives them to [`lemmaK`](/entry/lemma-k/), which holds the content. Its only user is [the bound on $H^2$ from the literature hypothesis](/entry/lemma-k-lit-n-alt/), which supplies `BOdd` from [`bOdd`](/entry/b-odd/).

## Statement

**Theorem.** If `LiteratureRankNHypothesis` holds and `BOdd` holds, then there is a constant $C_K$ with `LemmaK` $C_K$.

`LemmaK` $C_K$ is the bound $\log \# H^2(G_S, \mathbb{Z}_l(\chi^{e+1})) \le \exp((2en)^{C_K} \log(2D))$, stated in full in [the parent entry](/entry/lemma-k-lit-n-alt/). `BOdd` is a bound on the rank of a span of classes in the group homology of $\mathrm{GL}_n(\mathcal{O}_L)$; see [`lemmaK`](/entry/lemma-k/).

## Proof

The proof is one term: `lemmaK hB (pt_s hN) hN.coh.lfK hN.coh.ltK`. The three inputs are:

- `pt_s hN`: Poitou-Tate duality, from the normalized form `hN.coh.pt` through `poitouTateDuality_of_normalised`;
- `hN.coh.lfK`: local finiteness;
- `hN.coh.ltK`: local Tate duality.

## In the Lean code

The theorem is in [DenseThresholdCases/LemmaKOfLitN.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LemmaKOfLitN.lean#L12). `pt_s` is in [HVFinalU.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/HVFinalU.lean#L11).

Its subtree has 636 declarations, and `lemmaK` alone has 635. So the theorem adds only itself. The module of `lemmaK` in `ClassCounting` has the same name, `LemmaKOfLitN`, but `lemmaK` does not take the literature hypothesis.
