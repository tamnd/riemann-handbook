---
id: integrality-from-metric-of-orth-basis-lat
title: Adding the symmetry of the block pairing to the window count
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.integralityFromMetric_of_orthBasisLat
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.IntegralityFromMetricOfOrthBasisLat
covers: 2669
status: drafted
drafted_by: writer@claude
---
This theorem is the fourth link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_orthogonal_splitting`](/entry/closed-of-orthogonal-splitting/) calls it. It adds a proved symmetry fact to the window count `RestWinE D` and passes the rest on to [`closed_of_orthogonal_basis`](/entry/closed-of-orthogonal-basis/). It has no mathematical content of its own.

## Statement

Write $\mathcal{T}(P)$ for the nest of quantifiers `TransportedAlt P`: for each $C_c \ge 0$ there is $T_0 > 0$; for each $C_0 \ge T_0$ there is $T_1 > 0$; for all $C_{E1}, C_{E2} \ge T_1$ there is $T_2 > 0$; for all $C_{Yb}, C_{de}, C_k, C_D, C_b \ge T_2$ the statement $P$ holds.

For an instance $X$ and constants $C_0, C_{E1}, C_{E2}$, the code indexes a family of block data by triples $(d, a_{\mathrm{top}}, x)$. Each index gives a $\mathbb{Z}_p$-lattice $\Lambda$ (`Ljj`, a span of products of polynomials) and two $\mathbb{Q}_p$-valued pairings on it, $\beta_\Phi$ (`bePhi`) and $\beta_{a_+}$ (`bejj`, which depends on a further $a_+ \in A$). Both are a Fock pairing after a linear map, divided by a product of factorials. We have not unfolded them further. Let $\delta = D_1(C_M)$ be the real number `D1r`.

- `RestWin` $C_M$: for each index and each $\mathbb{Z}_p$-linearly independent family $e_1, \dots, e_{n}$ in $\Lambda$ that is orthogonal for $\beta_\Phi$, with $\beta_\Phi(e_a, e_a) \ne 0$ and $v_p(\beta_\Phi(e_a,e_a)) \le \lfloor \delta \rfloor$,
$$ \sum_{a_+ \in A} \mathrm{bad}\bigl(\beta_{a_+}, \operatorname{span}(e), \lfloor Y\delta \rfloor\bigr) \le |A| \cdot \frac{5n}{Y}. $$
- `RestSymm`: $\beta_\Phi(u,v) = \beta_\Phi(v,u)$ on each $\Lambda$.
- `RestWinE D`: $\mathcal{T}$ of the statement "for all $C_\kappa, C_s$, all $C_M \ge 1$ and each $X$ with `AdmNoK` and `HI`, `RestWin` $C_M$ holds".

Here $\mathrm{bad}(\beta, L, e) = \operatorname{rk} L - g(\beta, L, e)$, with the good count $g$ of [`closed_of_splitting_matrix`](/entry/closed-of-splitting-matrix/).

**Theorem.** For each datum $D$, `OrthBasisLat`, `GoodLeSmall` and `RestWinE D` imply `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `symmetric_dims_of_windows` proves `SymmetryWindowOnAdmissible D` from `RestWinE D`. That statement is the same nest with the conclusion "`HI` implies `RestSymm` and `RestWin` $C_M$". The proof opens the nest and adds `RestSymm` from `symmCondition`, which holds for all $X$ and all constants with no hypothesis. Then `closed_of_orthogonal_basis` is applied. The rest is bookkeeping.

## In the Lean code

The theorem is in [IntegralityFromMetricOfOrthBasisLat.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/IntegralityFromMetricOfOrthBasisLat.lean#L29), with `RestWinE` at line 10 and `symmetric_dims_of_windows` at line 15. `RestWin` is in [BejjSmulLeft.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BejjSmulLeft.lean#L129), `RestSymm` in [BePhiAddLeft.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BePhiAddLeft.lean#L21), and `symmCondition` in [CommCondition.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/CommCondition.lean#L35). `symmCondition` is `restSymm_of commCondition`: a commutation of tie operators gives the symmetry.

The hypotheses `hB` and `hG` pass through unchanged. The name says "of orthBasisLat", but the only step here concerns `RestWinE`. The name `symmetric_dims_of_windows` mentions dimensions, but its conclusion has no dimension condition. That condition is added later, by `windows_of_symmetric_dims` in [`closed_of_symmetric_dims`](/entry/closed-of-symmetric-dims/).
