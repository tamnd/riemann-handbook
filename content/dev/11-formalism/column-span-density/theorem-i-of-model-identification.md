---
id: theorem-i-of-model-identification
title: The base-level projection bound from the two-letter model identification
kind: theorem
decl: Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_model_identification
module: Formalism.SharpRestriction.GrowthBounds.ColumnSpanDensity.TheoremIOfLatticeFunctorComparison
covers: 739
status: drafted
drafted_by: writer@claude
---
This theorem reduces `SecondPartClosed D` to `TwoLetterModelIdentification` and `RestCloudMaps`. Its only caller is [the bound from the explicit minor map](/entry/theorem-i-of-explicit-minor-map/), which proves the first statement. The proof is one line: two lemmas turn the model identification into `LatticeFunctorComparison`, and [the next reduction](/entry/theorem-i-of-lattice-functor-comparison/) takes over.

## Statement

The notation is that of [the parent entry](/entry/theorem-i-of-explicit-minor-map/): a setting $R$ with $O \subset K$, $m \ge 2$, the spaces $\mathcal{P}_{a,b}$ of bihomogeneous polynomials in $x, y$, $h = \sum_i x_i y_i$, the spaces $S_\lambda$ with lattices $S_\lambda(\Lambda)$, and $\omega_{a,b} = (a, 0, \dots, 0, -b)$.

`TwoLetterModelIdentification` says: for each setting and each $m \ge 2$ there are

1. $K$-linear isomorphisms $\alpha_{P,Q}$ from $S_{(P,0,\dots,0)} \otimes S_{(0,\dots,0,-Q)}$ onto $\mathcal{P}_{P,Q}$;
2. surjective $K$-linear maps $\beta_{a,b} \colon \mathcal{P}_{a,b} \to S_{\omega_{a,b}}$ whose kernel is $h \cdot \mathcal{P}_{a-1,b-1}$;
3. for each lattice $\Lambda \subset K^{m+1}$, a $g' \in \mathrm{GL}_{m+1}(K)$ such that an element lies in the lattice `twoLat` exactly when its image under $\alpha$ lies in the $g'$-translate of $O[x, y]$, and $\beta$ maps the part of that translate in $\mathcal{P}_{a,b}$ onto $S_{\omega_{a,b}}(\Lambda)$.

**Theorem.** For each datum $D$, `TwoLetterModelIdentification` and `RestCloudMaps` imply `SecondPartClosed D`.

## Proof

1. `single_weight_of_model_identification` proves `SingleWeightLatticeComparison`. Let $P + Q + 1 \le 8a$. The space $S_{(P,0,\dots,0)} \otimes S_{(0,\dots,0,-Q)}$ splits as a sum of copies of $S_{\omega_{P-j,Q-j}}$ for $0 \le j \le \min(P, Q)$, with maps $i_j$ and $\mathrm{pr}_j$ and $\sum_j i_j \circ \mathrm{pr}_j = \mathrm{id}$. Both maps carry lattice to lattice after multiplication by $p^{N}$, with $N = \lceil (m+2)(\log_p(8a + m) + 1) \rceil$. The main step is the lemma `oneTop_abs`, applied to $\alpha$ and $\beta$; its own exponent $(m+2) \lfloor \log_p(P + Q + m + 1) \rfloor$ is at most $N$ by `expo_le`.
2. `functor_comparison_of_single_weight_facts` proves `LatticeFunctorComparison`: the same splitting for a tensor product over a finite set $T$ of indices, with exponent $|T| N$. It calls `functor_comparison_of_single_weight` with three lemmas proved in the same file (`existsIO'`, `existsPR'`, `regroupP`).
3. `theorem_I_of_lattice_functor_comparison` applies.

## In the Lean code

The theorem is in [TheoremIOfLatticeFunctorComparison.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/TheoremIOfLatticeFunctorComparison.lean#L67). `TwoLetterModelIdentification` and step 1 are in [SingleWeightOfModelIdentification.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/SingleWeightOfModelIdentification.lean#L45), `SingleWeightLatticeComparison` in [SingleWeightLatticeComparison.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/SingleWeightLatticeComparison.lean#L18), and step 2 in [FunctorComparisonOfSingleWeightFacts.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/FunctorComparisonOfSingleWeightFacts.lean#L115). We have not opened `oneTop_abs` or `functor_comparison_of_single_weight`. The theorem itself only passes its hypotheses on.
