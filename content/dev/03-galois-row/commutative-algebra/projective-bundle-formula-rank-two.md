---
id: projective-bundle-formula-rank-two
title: The projective bundle formula for the projective line
kind: theorem
decl: UpperTheory.projectiveBundleFormula_rank_two
module: Development.AutomorphicArithmetic.CommutativeAlgebra.ProjectiveBundleFormulaRankTwo
covers: 347
status: drafted
drafted_by: writer@claude
---
This theorem is the case $N = 2$ of the projective bundle formula: the cohomology of $\mathbb{P}^1_E$. [The induction on the rank](/entry/pbf-all/) uses it as a base case, after rank 0 and rank 1. Ranks above 2 come from [the induction step](/entry/projective-bundle-formula-succ-of-forall/), which also gives the notation used here.

## Statement

Let $q \ge 1$ and let $E$ be a simplicial presheaf on schemes on which $q$ is invertible. Let $\pi \colon \mathbb{P}^1_E \to E$ be the trivial $\mathbb{P}^1$-bundle and $\xi = c_1(\mathcal{L}) \in H^2(\mathbb{P}^1_E, \mathbb{Z}/q(1))$. Then for all $n, i \in \mathbb{Z}$ the map

$$H^n(E, \mathbb{Z}/q(i)) \oplus H^{n-2}(E, \mathbb{Z}/q(i-1)) \to H^n(\mathbb{P}^1_E, \mathbb{Z}/q(i)), \qquad (a_0, a_1) \mapsto \pi^* a_0 + \pi^* a_1 \cup \xi,$$

is bijective. This is `PBF q E 2`.

## Proof

The proof is Mayer-Vietoris for the two standard charts of $\mathbb{P}^1$.

1. **Charts.** `tri_pullback` identifies $\mathbb{P}^1_E$ with $E \times \mathrm{Dv}_2$, where $\mathrm{Dv}_2$ is the nerve of the groupoid of unimodular pairs up to units. For $b = 0, 1$, the map $f_b \colon E \times \mathbb{A}^1 \times \mathrm{Dv}_1 \to \mathbb{P}^1_E$ (`gch b`) sends $t$ to the pair with $1$ in place $b$ and $t$ in the other place. The two maps cover $\mathbb{P}^1_E$ (`gch_cover`).
2. **The charts are trivial.** Each $\pi \circ f_b$ is the projection to $E$, and it is an isomorphism on cohomology. For the factor $\mathbb{A}^1$ this is homotopy invariance (`tateTwist_affineLine_projection_equiv`). For the factor $\mathrm{Dv}_1$ it is the rank 1 formula (`projectiveBundleFormula_rank_one_of_homotopyInvariant`).
3. **The intersection.** The fibre product of $f_0$ and $f_1$ is $E \times \mathbb{G}_m \times \mathrm{Dv}_1$, with $\mathbb{G}_m$ over $\mathbb{Z}[1/q]$ (`over_pullback`). By `bijective_cohomology_gm_product_kummer_cup`, its cohomology is $H^*(E) \oplus H^{*-1}(E) \cup \kappa$, where $\kappa \in H^1(\mathbb{G}_m, \mathbb{Z}/q(1))$ is the Kummer class of the coordinate $t$ (`kappa`).
4. **The boundary.** $\mathcal{L}$ is trivial on each chart, and the two trivializations differ by $t$ on the intersection. So the Mayer-Vietoris boundary sends $\kappa$ to $\pm\xi$ (`kummer_cocycle_mayerVietoris_of_cover`).
5. **Assembly.** `P2.core` combines steps 2 to 4 into the bijectivity of $(a_0, a_1) \mapsto \pi^* a_0 + \pi^* a_1 \cup \xi$. `P2.lh2` turns this into the form `LH` that `PBF` asks for.

## In the Lean code

The theorem is in [ProjectiveBundleFormulaRankTwo.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/ProjectiveBundleFormulaRankTwo.lean#L104). The charts are in [TwoChart.lean](lean:Development/AutomorphicArithmetic/CupPullbacks/TwoChart.lean#L136), and `core` and `lh2` are in [TwoCore.lean](lean:Development/AutomorphicArithmetic/CupPullbacks/TwoCore.lean#L193). The private lemmas `eqv_fst` and `kun` in the same file adapt the rank 1 formula and the $\mathbb{G}_m$ computation to the shapes that `core` needs.

`kummer_cocycle_mayerVietoris_of_cover` states a disjunction: the boundary of $\kappa$ is $\xi$ or $-\xi$. Its proof gives the second case. `core` accepts either sign, so the sign does not matter here.
