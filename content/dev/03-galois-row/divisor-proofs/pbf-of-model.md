---
id: pbf-of-model
title: The projective bundle formula from classes on a model of the bundle
kind: theorem
decl: GlobalTheory.PBFc.pbf_of_model
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ChainsIsStrictlyLE
covers: 322
status: drafted
drafted_by: writer@claude
---
This theorem proves the projective bundle formula for a vector bundle $V$ on an arbitrary space $E$, from two inputs: the formula on discrete spaces, and cocycles on an auxiliary space that represent the powers of $c_1(L)$. Its parent [pbf_of_disc](/entry/pbf-of-disc/) supplies the cocycles from the universal line bundle and passes the result to [the formula on any space](/entry/projective-bundle-formula-vector-bundle-any-space/), which goes into the [local steps](/entry/steps-holds/) of the Galois row. Below this theorem are 322 declarations.

## Statement

Spaces, the groups $H^n(E, \mathbb{Z}/q(i))$, the condition "$q$ is invertible on $E$", $\mathbb{P}(V)$ with its line bundle $L$, and the map of the formula (`pbfMap`, `PBF`) are as in [the entry on discrete spaces](/entry/pbf-disc/). Let $F_N$ be the space of unimodular vectors up to a unit (`Fib N`), with its line bundle $L_F$ (`Fib.line`).

*The model.* The bisimplicial space $X = X(E, V)$ (`twX`) has column $p$ equal to $E_p \times F_N$, where $E_p$ is the presheaf of $p$-simplices of $E$. Its simplicial maps act on $F_N$ through the transition matrices of $V$. Its diagonal is isomorphic to $\mathbb{P}(V)$ (`twIso`), and this isomorphism carries the line bundle of the columns to $L$.

**Theorem.** Let $q \geq 1$, let $q$ be invertible on $E$, and let $V \colon E \to B\mathrm{GL}_N$. Let $B$ be a space, and let $\ell \colon X \to B$ be a map from $X$ to the constant bisimplicial space on $B$. For $0 \le j < N$ let $z_j$ be a cocycle of degree $2j$ on $B$ with coefficients $\mathbb{Z}/q(j)$. Suppose that:

1. on the diagonal, the class of $\ell^* z_j$ is $c_1(L)^j$, through `twIso`;
2. on each column $E_a \times F_N$, the class of $\ell_a^* z_j$ is $c_1(L_F)^j$;
3. the formula holds for each bundle on each discrete space on which $q$ is invertible.

Then the formula holds for $V$: for all $n, i$ the map $(a_j) \mapsto \sum_j \pi^* a_j \cup c_1(L)^j$ is bijective.

## Proof

1. Pullback along `twIso` is bijective (`pull_iso_bijective`). The Alexander-Whitney map from the chains of the diagonal of $X$ to the total complex of its double complex of chains is a homotopy equivalence, so it is bijective on cohomology (`pull_awChains_bijective`, from `eilenberg_zilber_homotopy_equivalence`). So it suffices that the induced map $\varphi$ into the cohomology of the total complex is bijective.
2. On cochains, $\varphi$ comes from $\Phi(\alpha) = \sum_j \alpha_j \times \ell^* z_j$, a sum of cross products (`phi`, `crossT`). Hypothesis 1 gives this by `twisted_cocycle_classes_pullback_cup`.
3. `bijective_total_of_terms` is a comparison along the filtration by columns. Its inputs: $\Phi$ commutes with $\delta$ (`phi_δ`, from the Leibniz rule `crossProductTwisted_leibniz_rule` and $\delta z_j = 0$); $\Phi$ respects the filtration (`phi_van`, from `cochain_product_vanishing_above_degree`); and $\Phi$ is bijective on cohomology column by column.
4. The column statement is `twisted_cocycle_simplicial_levels_cup`, whose statement we have opened but not its proof. It takes hypotheses 2 and 3, since each column $E_p \times F_N$ is the trivial bundle over the discrete space $E_p$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ChainsIsStrictlyLE.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChainsIsStrictlyLE.lean#L62). The lemmas:

- `phi_δ`, `phi_van` and `pull_iso_bijective` in the same file (lines 26, 40, 53); `phi` and `crossT` in [CrossTZeroRight.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CrossTZeroRight.lean#L155);
- `GlobalTheory.EZ.pull_awChains_bijective` in [PullAwChainsBijective.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PullAwChainsBijective.lean#L40);
- `GlobalTheory.ColFilt.bijective_total_of_terms` in [BijectiveTotalOfColumns.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/BijectiveTotalOfColumns.lean#L420);
- `GlobalTheory.T.twisted_cocycle_classes_pullback_cup` and `GlobalTheory.T.twisted_cocycle_simplicial_levels_cup`.

`twX`, `twIso` and `Fib` are in [SpanRangeMulVecLe.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SpanRangeMulVecLe.lean#L220). The file is named after the instance `chains_isStrictlyLE` (line 20), which says that the chain complex of a space lives in degrees $\le 0$; `bijective_total_of_terms` needs it. The hypotheses "$q$ invertible on $E$" and 3 are used only in step 4.
