---
id: projective-bundle-formula-succ-of-forall
title: The projective bundle formula, from rank N to rank N+1
kind: theorem
decl: UpperTheory.projectiveBundleFormula_succ_of_forall
module: Development.AutomorphicArithmetic.CommutativeAlgebra.ProjectiveBundleFormulaSuccOfForall
covers: 382
status: drafted
drafted_by: writer@claude
---
This theorem is the induction step of the projective bundle formula in étale cohomology with coefficients $\mathbb{Z}/q(i)$. [The induction on the rank](/entry/pbf-all/) uses it for each $N \ge 2$; rank 2 is [a separate theorem](/entry/projective-bundle-formula-rank-two/). The step blows up $\mathbb{P}^N$ at a point.

## Statement

The spaces $E$ are simplicial presheaves on schemes (`Spc`). Fix $q \ge 1$. Then $q$ is invertible on $E$ (`Inv q E`) if $q$ is a unit on each scheme over which $E$ has a $0$-simplex. $H^n(E, \mathbb{Z}/q(i))$ is `Ht q E n i`, étale cohomology with coefficients in the sheaf `tw q i`, which is built from the primitive $q$-th roots of unity.

Let $\mathbb{P}^{N-1}$ be the nerve of the groupoid of unimodular vectors $v \in A^N$, with maps $v \to w$ the units $\lambda$ with $v = \lambda w$ (for each ring $A$). Let $\pi \colon \mathbb{P}^{N-1}_E \to E$ be the trivial bundle with this fibre: in Lean, the fibre product of the trivial map $E \to B\mathrm{GL}_N$ (`triv`) and `PGL.pr N`. The unit $\lambda$ gives a line bundle $\mathcal{L}$ on $\mathbb{P}^{N-1}_E$ (`PGL.line`). Let $\xi = c_1(\mathcal{L}) \in H^2(\mathbb{P}^{N-1}_E, \mathbb{Z}/q(1))$. Then $\mathrm{PBF}_N(E)$ (`PBF q E N`) says: for all $n, i \in \mathbb{Z}$, the map

$$\bigoplus_{j=0}^{N-1} H^{n-2j}(E, \mathbb{Z}/q(i-j)) \to H^n(\mathbb{P}^{N-1}_E, \mathbb{Z}/q(i)), \qquad (a_j) \mapsto \sum_j \pi^* a_j \cup \xi^j,$$

is bijective.

**Theorem.** Let $N \ge 2$. If $\mathrm{PBF}_N(E)$ holds for each $E$ on which $q$ is invertible, then $\mathrm{PBF}_{N+1}(E)$ holds for each such $E$.

## Proof

`projBundleFormula_iff_pglForm` replaces $\mathrm{PBF}_M$ by an equivalent form `Pbf` on the groupoid `XC M` of unimodular vectors modulo scalars. Let $B$ (`BC N`) be the groupoid of pairs $(x, (a, b))$ of unimodular vectors of lengths $N$ and 2, with two maps:

- $p \colon B \to \mathbb{P}^{N-1}$, $(x, (a,b)) \mapsto x$ (`pC`);
- $\beta \colon B \to \mathbb{P}^N$, $(x, (a,b)) \mapsto (a x_1, \dots, a x_N, b)$ (`βC`).

So $\beta$ is a model of the blow-up of $\mathbb{P}^N$ at $(0 : \dots : 0 : 1)$, and $p$ is a $\mathbb{P}^1$-bundle. Let $Q_1 \subseteq \mathbb{P}^N$ be the locus where the last coordinate is a unit, and $Q_2$ the locus where the first $N$ coordinates generate the unit ideal. Let $\eta$ and $\xi$ be the classes $c_1(\mathcal{L})$ on $\mathbb{P}^{N-1}_E$ and $\mathbb{P}^N_E$.

1. Leray-Hirsch for $p$ with the classes $1, \beta^*\xi$, chart by chart on the loci of $\mathbb{P}^{N-1}$ where one coordinate is a unit (`cohomology_lift_of_lift_on_unit_cube_faces`, `leraHirsch_chernPowers_on_unitChart`).
2. $\beta^*\xi$ restricts to $0$ over $Q_1$ (`chernClass_pullback_blowupFirstLocus_eq_zero`). Over $Q_2$ it agrees with $p^*\eta$ (`chernClass_pullback_blowupSecondLocus_eq`). From these, `cpow_succ_eq_cup_of_two_cover` gives $(\beta^*\xi)^{j+1} = (p^*\eta)^j \cup \beta^*\xi$ for all $j$.
3. Injectivity for $\mathbb{P}^N$ (`leray_hirsch_of_pullback_square`) follows from $\mathrm{PBF}_N$ and steps 1 and 2.
4. Surjectivity (`leray_hirsch_of_two_covers_pullback_square`) is Mayer-Vietoris for the cover $Q_1, Q_2$ and its pullback to $B$. The inputs: $Q_1 \to E$ and $\beta^{-1}(Q_1) \to \mathbb{P}^{N-1}_E$ are isomorphisms on cohomology (`eqv_twist_unimodularUnitLocus`, `leraHirsch_unit_on_blowupChart`); so is $\beta$ over $Q_2$ (`eqv_twist_blowupRestriction`) and over the intersection (`pullback_cube_faces_equiv_tate_twist`).

The rest is bookkeeping, with the naturality of $c_1$ (`firstChernClassTateTwist_cocycle_unique_natural_additive`).

## In the Lean code

The theorem is in [ProjectiveBundleFormulaSuccOfForall.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/ProjectiveBundleFormulaSuccOfForall.lean#L36). `PBF` and `LH` are in [ConstCompSingle.lean](lean:Development/AutomorphicArithmetic/CupPullbacks/ConstCompSingle.lean#L28). `XC`, `BC`, `pC`, `βC`, `Q1`, `Q2` and `Pbf` are in [SpanScale.lean](lean:Development/AutomorphicArithmetic/BlowupCategories/SpanScale.lean#L273).

The proof uses the hypothesis $N \ge 2$ only to get $N \ge 1$, which is all that the called lemmas ask for. We have not checked why rank 2 has its own proof.
