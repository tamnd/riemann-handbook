---
id: fl-at-one
title: The lattice modification lemma in degree one
kind: theorem
decl: GlobalTheory.PMon.FLOne.flAt_one
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.FundamentalLemmaLatticeDegreeOne
covers: 575
status: drafted
drafted_by: writer@claude
---
This theorem proves `FLAt 1`. It finds a Frobenius-fixed matrix over $B_{\mathrm{cris}}$ whose $B_{\mathrm{dR}}^+$-lattice is a given lattice with one column divided by $t$ and another multiplied by $t$. [`fundamentalLemmaLattice_degreeOne`](/entry/fundamental-lemma-lattice-degree-one/) renames it, and [`flAt_all`](/entry/fl-at-all/) gets the case of general $r$ from it.

## Statement

Let $P$, $A_{\inf}$ be period data with a tie to Fontaine's rings (see [[Fontaine's period rings|K6HW8YWCQJ]]). So $B = B_{\mathrm{cris}}$ with Frobenius $\varphi$, $\iota \colon B \to B_{\mathrm{dR}}$, $t \in B$ is a unit, and $\mathrm{Fil}^0 = B_{\mathrm{dR}}^+$. For $r \ge 1$, `FLAt r` says the following. Let $U_0, \dots, U_{r-1} \in \mathrm{GL}_n(B_{\mathrm{dR}})$ with $U_m, U_m^{-1}$ in $M_n(B_{\mathrm{dR}}^+)$. Let $x = (x_1, x_2) \ne y$ in $\{0, \dots, r-1\} \times \{1, \dots, n\}$. Assume: if $c \in (\mathbb{Q}_\ell^{\mathrm{ur}})^n$ is fixed by $\mathrm{Fr}^r$ and $\sum_i c_i (U_{x_1})_{i x_2} \in \mathrm{Fil}^1$, then $c = 0$. Then there is $A \in \mathrm{GL}_n(B)$ with $\varphi^r(A) = A$ and, for each $m < r$, some $W_m \in \mathrm{GL}_n(B_{\mathrm{dR}}^+)$ with

$$\iota(\varphi^m(A)) = U_m \operatorname{diag}\bigl(t^{\varepsilon(m,j)}\bigr)_j W_m,$$

where $\varepsilon(m,j)$ is $-1$ at $x$, $+1$ at $y$ and $0$ else. This theorem is the case $r = 1$. Write $U = U_0$.

## Proof

Let $h$ be the size $n$. Then $h \ge 2$, as $x_2 \ne y_2$. For $a \in B^h$ write $M(a) = (\varphi^i(a_j))_{i,j < h}$.

1. **Column $x_2$.** Let $\lambda$ be column $x_2$ of $U$. The hypothesis with $c \in \mathbb{Q}_\ell^n$ makes $\lambda$ linearly independent over $\mathbb{Q}_\ell$ modulo $\mathrm{Fil}^1$, so some $\lambda_k$ is a unit of $B_{\mathrm{dR}}^+$. `exists_secondKind_matrix_moore_det_ne_zero` gives $a$ with $\varphi^h(a_j) = \ell a_j$, $\iota\varphi^i(a_j) \in B_{\mathrm{dR}}^+$, $\iota(M(a))\lambda \in (\mathrm{Fil}^1)^h$ and $\det M(a) \ne 0$. By `det_mem_one`, $\iota \det M(a) \in \mathrm{Fil}^1$. Then `mooreDeterminant_eq_unramified_mul_period` gives $\det M(a) = \kappa t$ with $0 \ne \kappa \in \mathbb{Q}_\ell^{\mathrm{ur}}$. So $M(a)$ is invertible.
2. **A new lattice.** Let $D_x$ be diagonal with $t^{-1}$ at $x_2$ and $1$ else. Column $x_2$ of $\iota(M(a))U$ lies in $\mathrm{Fil}^1$, so $U' = \iota(M(a))\,U D_x$ has entries in $B_{\mathrm{dR}}^+$. Its determinant is $\kappa \det U$, a unit. So $U' \in \mathrm{GL}_n(B_{\mathrm{dR}}^+)$ (`unitM_of`).
3. **Row $y_2$.** Let $V = U'^{-1}$ and $\mu$ its row $y_2$. Some $\mu_k \notin \mathrm{Fil}^1$, as $(VU')_{y_2 y_2} = 1 \notin \mathrm{Fil}^1$ (`one_not_mem`). `existsIndependentFrobSolutionsCris_proof` (the statement `ExI`) gives $b$ in $B_{\mathrm{cris}}^+$, linearly independent over $\mathbb{Q}_\ell$, with $\varphi^h(b_j) = \ell b_j$ and $\mu\,\iota(M(b)) \in (\mathrm{Fil}^1)^h$. `mooreDeterminant_crisPlus_ne_zero` gives $\det M(b) \ne 0$. As in step 1, $\det M(b) = \kappa' t$. With $D_y$ like $D_x$ at $y_2$, $W = D_y V \iota(M(b))$ lies in $\mathrm{GL}_n(B_{\mathrm{dR}}^+)$.
4. **Assembly.** Let $C$ be the companion matrix with $1$ above the diagonal and $\ell$ in the bottom left corner. Then $\varphi(M(a)) = C M(a)$ and $\varphi(M(b)) = C M(b)$ (`moore_map`), so $\varphi(M(a)^{-1}M(b)) = M(a)^{-1}M(b)$ (`inv_mul_fixed`). Since $D_x = \operatorname{diag}(t^{\varepsilon}) D_y$,
$$\iota(M(a)^{-1}M(b)) = \iota(M(a))^{-1} U' V \iota(M(b)) = U D_x V \iota(M(b)) = U \operatorname{diag}(t^{\varepsilon}) W.$$

The rest is bookkeeping with the bijection $n \simeq \{0, \dots, h-1\}$.

## In the Lean code

The theorem is in [FundamentalLemmaLatticeDegreeOne.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FundamentalLemmaLatticeDegreeOne.lean#L164). The helpers `det_mem`, `adj_mem`, `det_mem_one`, `unitM_of`, `comp`, `moore_map` and `inv_mul_fixed` are in the same file. The filtration facts come from `deRhamPeriodRing_field_tPow_filtration_units`, and $\iota\varphi^i(b_j) \in B_{\mathrm{dR}}^+$ from `bcrisPlus_frobeniusStable_subring_in_filZero`. We have not unfolded the proofs of the four lemmas that build $a$, $b$ and the determinants.

The proof uses the hypothesis on $c$ only for $c$ with entries in $\mathbb{Q}_\ell$.
