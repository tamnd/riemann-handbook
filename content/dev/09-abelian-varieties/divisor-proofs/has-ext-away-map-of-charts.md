---
id: has-ext-away-map-of-charts
title: Extension over Spec R from charts and an ample divisor
kind: theorem
decl: GlobalTheory.Desc.hasExt_awayMap_of_charts
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExtendsToSemiAbelianAwayOfCharts
covers: 635
status: drafted
drafted_by: writer@claude
---
This theorem extends an abelian scheme over $\operatorname{Spec} R_f$ to a semi-abelian scheme over $\operatorname{Spec} R$, given a chart at each point. It is the proof of [`extendsToSemiAbelian_away_of_charts`](/entry/extends-to-semi-abelian-away-of-charts/). It builds the data of a `Setup` (an ample divisor on $A$ and its closure on each chart) and passes it to [`hasExt_of_setup`](/entry/has-ext-of-setup/), which does the gluing.

## Statement

Let $R$ be a noetherian integrally closed domain and $f \in R$, $f \neq 0$. Let $A$ be an abelian scheme over $\operatorname{Spec} R_f$ with a relatively ample line bundle $L$. Suppose that $A$ has a chart at each point of $\operatorname{Spec} R$.

**Theorem.** Then $A$ extends to a semi-abelian scheme over $\operatorname{Spec} R$.

Charts and extensions are defined in [`hasExt_opensRange`](/entry/has-ext-opens-range/). For a chart at $x$ we write $R_x$ for its complete regular local ring and $G_x$ for its semi-abelian scheme.

## Proof

1. $R_f$ is a domain and $A$ is integral (`isIntegral_left_of_isAbelianScheme`).
2. `GlobalTheory.SymDiv.exists_ampleDiv_symm`: there is a Cartier divisor $D$ on $A$ that is ample and symmetric, that is $[-1]^* \mathcal{O}(D) \cong \mathcal{O}(D)$. Here "ample" (`AmpleDiv`) means: each point of $A$ lies in an affine open that is the locus where some section of $kD$, $k \geq 1$, generates.
3. Choose a chart at each $x$. `chart_part` puts it in a standard form: $\xi$ is $\operatorname{Spec}$ of a flat ring map $\rho_x \colon R \to R_x$; $V_x \subseteq G_x$ is the open where $\rho_x(f)$ is a unit; there is a map $\varphi_x \colon V_x \to A$ with $V_x = A \times_{\operatorname{Spec} R} \operatorname{Spec} R_x$; $\varphi_x$ agrees with the generic identification of the chart; and there is a map of function fields $\theta_x \colon K(A) \to K(G_x)$ compatible with $\varphi_x$.
4. `exists_cartierDiv_closure`: the pullback of $D$ to $V_x$ extends to a Cartier divisor $D_{1,x}$ on $G_x$ whose local equation is $1$ at each codimension one point of $G_x$ over $V(f)$. So $D_{1,x}$ has no vertical component. This needs the local rings of $G_x$ to be factorial. `ufm_stalk_of_smooth_regularLocal` gives that: $G_x$ is smooth over the regular local ring $R_x$, so its local rings are regular, and regular local rings are factorial (Auslander and Buchsbaum, Proc. Nat. Acad. Sci. USA 45, 1959).
5. `ampleDiv_closure_on_chart`: $D_{1,x}$ is ample on $G_x$. It uses the symmetry of $D$, the completeness and characteristic 0 of $R_x$, and $\rho_x(f) \neq 0$.
6. The data $R, f, A, D, (\rho_x, V_x, \varphi_x, \theta_x, D_{1,x})_x$ form a `Setup`. [`hasExt_of_setup`](/entry/has-ext-of-setup/) gives the extension.

## In the Lean code

The theorem is at [ExtendsToSemiAbelianAwayOfCharts.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExtendsToSemiAbelianAwayOfCharts.lean#L32). The structure `Setup` is in [SubsetSpanBy.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SubsetSpanBy.lean#L123). The lemmas it calls:

- `GlobalTheory.SymDiv.exists_ampleDiv_symm`;
- `GlobalTheory.Desc.chart_part`, in ExistsIsoPreimageBasicOpen.lean;
- `GlobalTheory.Desc.exists_cartierDiv_closure` and `ufm_stalk_of_smooth_regularLocal` (same file);
- `GlobalTheory.Desc.ampleDiv_closure_on_chart`, in IsAbelianSchemePullbackOfIsPullback.lean;
- `GlobalTheory.Desc.hasExt_of_setup`.

We read the statements of these lemmas, not their proofs. The line bundle $L$ and its relative ampleness are used only in step 2. The charts are chosen with `Classical.choice` (`(hC x).some`), so the `Setup` depends on a choice of chart at each point.
