---
id: theorem-i-of-explicit-minor-map
title: The base-level projection bound from the explicit minor map
kind: theorem
decl: Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_explicit_minor_map
module: Formalism.SharpRestriction.GrowthBounds.ColumnSpanDensity.TheoremIOfLatticeFunctorComparison
covers: 742
status: drafted
drafted_by: writer@claude
---
This theorem reduces `SecondPartClosed D` to two statements: `TiePsi`, about one explicit map of polynomial rings, and `RestCloudMaps`. Its only caller is [the bound from the two-letter clauses and the contraction](/entry/theorem-i-of-two-letter-clauses-contraction/), which builds both statements. The proof turns `TiePsi` into `TwoLetterModelIdentification` and passes it to [the next reduction](/entry/theorem-i-of-model-identification/).

## Statement

`SecondPartClosed D` says that `AdmBE D` implies the base-level projection bound; see [the parent of the chain](/entry/theorem-i-closed-form-holds/). Let $R$ be an `UnramifiedQuadraticSetting` for $p$ and $n'$, with a discrete valuation ring $O$ and its fraction field $K$, and let $m \ge 2$. Let $x_0, \dots, x_m, y_0, \dots, y_m$ be variables, $h = \sum_i x_i y_i$, and $\mathcal{P}_{a,b}$ the polynomials of bidegree $(a, b)$ in $x$ and $y$. Let $A, B$ be $(m+1) \times (m+1)$ matrices of variables. Define $\Psi$ by

$$ \Psi(x_i) = A_{i0}, \qquad \Psi(y_i) = (-1)^i \det B^{(i)}, $$

where $B^{(i)}$ is $B$ without row $i$ and without its last column. Let $\delta$ set $A = B$. For a weight $\lambda$, let $S_\lambda$ be the column-invariant polynomials of weight $\lambda$ (`dualWeyl`), and $S_\lambda(\Lambda)$ the lattice in it that a lattice $\Lambda \subset K^{m+1}$ defines (`H0`). Put $\omega_{a,b} = (a, 0, \dots, 0, -b)$.

`TiePsi` says, for each setting and each $m \ge 2$:

1. $\Psi$ is injective and maps $\mathcal{P}_{P,Q}$ onto $S_{(P,0,\dots,0)} \otimes S_{(0,\dots,0,-Q)}$ (`twoSp`);
2. $\delta\Psi$ maps $\mathcal{P}_{a,b}$ onto $S_{\omega_{a,b}}$, and if $\delta\Psi(f) = 0$ for $f \in \mathcal{P}_{a,b}$ then $f = hG$ with $G \in \mathcal{P}_{a-1,b-1}$;
3. for each lattice $\Lambda$ there is $g' \in \mathrm{GL}_{m+1}(K)$ such that $\Psi$ and $\delta\Psi$ carry the $g'$-translate of $O[x, y]$ onto the lattices `twoLat` and $S_{\omega_{a,b}}(\Lambda)$.

`RestCloudMaps` gives, at each edge, maps $U_b$ and $L_b$ through a space $V(\lambda_0)$ with $L_a U_b = \delta_{ab}\, p^{k_b} j$ for a fixed map $j$, compatible with the lattices at the edge. We have not unfolded `Re`, `CCL` and `CCL'`, which give these lattices.

**Theorem.** For each datum $D$, `TiePsi` and `RestCloudMaps` imply `SecondPartClosed D`.

## Proof

`model_identification_of_explicit_map` proves `TwoLetterModelIdentification` from `TiePsi`. It takes $\alpha$ to be the inverse of $\Psi$ on $\mathcal{P}_{P,Q}$ and $\beta = \delta\Psi$. The one new fact is $\delta\Psi(h) = 0$. This is `sum_covY`: $\sum_i X_{i0} \cdot (-1)^i \det X^{(i)}$ is the expansion of a determinant with two equal columns. Then `theorem_I_of_model_identification` applies.

## In the Lean code

The theorem is in [TheoremIOfLatticeFunctorComparison.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/TheoremIOfLatticeFunctorComparison.lean#L70). `TiePsi` and `model_identification_of_explicit_map` are in [ModelIdentificationOfExplicitMap.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/ModelIdentificationOfExplicitMap.lean#L10), $\Psi$ (`PsiXY`) and $\delta$ (`deltaB`) in [DeltaPsiH.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/DeltaPsiH.lean#L12), and `RestCloudMaps` in [CloudPropOfMapsRetractionBasis.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/CloudPropOfMapsRetractionBasis.lean#L10). The name "minor map" refers to $\Psi$: it sends $y$ to the signed maximal minors of the first $m$ columns of $B$.
