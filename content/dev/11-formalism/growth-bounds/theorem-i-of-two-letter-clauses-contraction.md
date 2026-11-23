---
id: theorem-i-of-two-letter-clauses-contraction
title: The base-level projection bound from the two-letter map and the contraction
kind: theorem
decl: Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_two_letter_clauses_contraction
module: Formalism.SharpRestriction.GrowthBounds.HermitianTensor.TheoremIOfTwoLetterClausesContraction
covers: 921
status: drafted
drafted_by: writer@claude
---
This theorem reduces `SecondPartClosed D` to four statements: three on an explicit substitution map $\Psi$ and the contraction statement `ContractionStandardLattice`. Its only caller is [the version from the contraction alone](/entry/theorem-i-of-contraction/), which proves the three statements on $\Psi$. The proof builds two intermediate statements and hands them to [the reduction through the explicit minor map](/entry/theorem-i-of-explicit-minor-map/), which holds most of the 921 declarations below.

## Statement

Let $K$ be a field and $m \ge 1$. Let $x_0, \dots, x_m, y_0, \dots, y_m$ be variables, and let $\mathrm{Pol}_{P,Q}$ be the polynomials of degree $P$ in $x$ and $Q$ in $y$ (`PolAB`). Take two $(m+1) \times (m+1)$ matrices of variables $X$ and $X'$. The algebra map $\Psi$ (`PsiXY`) sends $x_i$ to $X_{i0}$ and $y_i$ to the signed minor $(-1)^i \det X'_{\hat\imath}$, where $X'_{\hat\imath}$ drops row $i$ and the last column of $X'$. The two-letter space $V_{P,Q}$ (`twoSp`) is a tensor product of two dual Weyl modules, one in $X$ and one in $X'$.

The three statements are:

1. `ExplicitMapInjective`: $\Psi$ is injective.
2. `ExplicitMapOntoTwoLetters`: $\Psi(\mathrm{Pol}_{P,Q}) = V_{P,Q}$.
3. `TwoLetterLatticeGaussInverse`: over a ring $O$ (setting `RS`), for $g$ invertible and $f \in \mathrm{Pol}_{P,Q}$, $\Psi(f)$ lies in the integral lattice `twoLat` of the column span of $g$ if and only if $f$ lies in the Gauss lattice (coefficients in $O$) moved by $g^{-1}$.

**Theorem.** For each datum $D$, the statements 1, 2, 3 and `ContractionStandardLattice` imply `SecondPartClosed D`.

## Proof

Assume `AdmBE D`. The lemma `tools_of_admitted_statements` extracts the twelve tools `AdmT D`. The proof keeps three of them:

- `GradedLatticeStable D`, which is `CartanDomain` and `CartanOnto`: over a discrete valuation ring with uniformizer $w$, if $w$ divides $FG$ in the sections of weight $\lambda + \mu$ then $w$ divides $F$ or $G$; and the sections of weight $\lambda + \mu$ are spanned by products $FG$;
- `TypeDecompositionsCommute D`, of which it uses `DualHeightInclusion` (not unfolded);
- `PairedPathIndependence D`, of which it uses `ColumnSystems.adm3`: for decreasing $\nu$, the dual Weyl module of weight $\nu$ has dimension $\prod_{i<j} (\nu_i - \nu_j + j - i)/(j - i)$. This is the Weyl dimension formula for $\mathrm{GL}_n$ (Fulton and Harris, *Representation Theory*, Theorem 6.3).

Then:

1. `tiePsi_of` builds `TiePsi` from statements 1, 2, 3, `CartanOnto` and the dimension formula. For $m \ge 2$, `TiePsi` adds that $\Psi$ followed by the merge of the two matrices maps $\mathrm{Pol}_{a,b}$ onto a dual Weyl module, that its kernel lies in $h \cdot \mathrm{Pol}_{a-1,b-1}$ with $h = \sum_i x_i y_i$, and an integral form of these facts.
2. `cloud_maps_of_contraction` builds `RestCloudMaps`, a family of maps $\iota, U_b, L_b$ with $L_a U_b = \delta_{ab}\, p^{k_b} \iota$ and lattice conditions at each edge.
3. `theorem_I_of_explicit_minor_map` takes `TiePsi`, `RestCloudMaps` and `AdmBE D`.

## In the Lean code

The theorem is in [TheoremIOfTwoLetterClausesContraction.lean](lean:Formalism/SharpRestriction/GrowthBounds/HermitianTensor/TheoremIOfTwoLetterClausesContraction.lean#L15). The tools are in [ProjectionLemmaBaseLevel.lean](lean:Formalism/SharpRestriction/GrowthBounds/ProjectionLemmaBaseLevel.lean#L202), `TiePsi` in [ModelIdentificationOfExplicitMap.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/ModelIdentificationOfExplicitMap.lean#L10) and `RestCloudMaps` in [CloudPropOfMapsRetractionBasis.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/CloudPropOfMapsRetractionBasis.lean#L10).

Odd points:

- The name `PairedPathIndependence` ([line 233](lean:Formalism/SharpRestriction/GrowthBounds/ProjectionLemmaBaseLevel.lean#L233)) is a dimension formula and `WeylV`, not a statement on paths. Another namespace defines a different `PairedPathIndependence`, on linear independence of paired paths.
- The tools are hypotheses here, taken out of `AdmBE D` at $C_c = 4$. [The pairing version](/entry/theorem-i-of-pairing-gl/) takes `CartanOnto` out of the same hypothesis at $C_c = 0$.
