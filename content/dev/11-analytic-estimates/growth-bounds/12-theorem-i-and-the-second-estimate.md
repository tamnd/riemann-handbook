---
title: Theorem I and the second estimate
decls:
  - Formalism.MainNotions.flipOneThree.Pf.second_estimate_of_restrictions
  - Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_finer_open_statements
  - Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_lattice_functor_comparison
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem I and the second estimate

Theorem I is the local input of [the first theorem with constants](/entry/first-theorem-with-constants/): at a weight $\lambda_0$ whose first and last coordinates lie in given intervals, it gives property $\mathrm{LP}'$ of Section 3 for edges of rank $1$, with a defect $\kappa$ whose mean over the box of weights is $O(|T|N_1/Y)$. This section states Theorem I with constants and reduces its closed form, in three steps, to two statements on lattices of tensor products: a comparison of the tensor product of two-letter spaces with the flat weights, and a statement on cloud maps. Section 13 reduces the comparison to an explicit model of the two-letter spaces, and Section 14 proves the model and the cloud maps statement.

### The statement

We use the unramified quadratic setting $R = (W, \mathbb{Q}_q, \mathcal{O}, K, \iota, \sigma, j, w)$ of Section 3, the dominant weights $\lambda_0 : \{1, \dots, n'\} \times \{0, \dots, m\} \to \mathbb{Z}$, the spaces $V_\lambda$, the lattices $H(L)$, the edges and the property $\mathrm{LP}'$ of that section, taken with edges of rank $1$. Let $T \subseteq \{1, \dots, n'\}$ and $c \geq 0$. A pair of maps $a_w, b_w$ and a weight $\lambda_0$ form a *base weight* if for $s \in T$ the row $\lambda_{0,s}$ starts with $a_w(s)$, ends with $-b_w(s)$ and has all other entries of absolute value at most $c$, and for $s \notin T$ all entries of $\lambda_{0,s}$ have absolute value at most $c$.

**Definition 5.12.1 (Theorem I with constants).** Let $C_0, C_H, C > 0$. *Theorem I with constants $(C_0, C_H, C)$* is the following statement. Let $(p, n', m, T, G', N_1, Y, Y_b, a, b', b_l, b_u, c, D_p, c^*)$ be parameters with $p$ prime, $k = m + 1$, $\ell_a = C_0N_1^2\log a$, that satisfy the hypotheses of Theorem I: $Y \geq 1$, $k^2Y^2 \leq p$, $T$ has a vector letter and at least two segments with gaps at most $G'$ and sizes at most $N_1 \geq 1$, $2N_1 + 2 \leq m$, $8\log(|T|Y) \leq \ell_a$, $0 < b'$, $b_l \leq b' \leq b_u$, $Y_b|T|\ell_ab'/k \leq b_u - b_l \leq b'/2$, $C_H \leq Y_b$, $2Y_b|T|\ell_a < k$, $kY^2Y_b|T|\ell_a\log a \leq a/b'$, $p < a/b'$, $C_H|T|\ell_a^2 \leq k$, $c \leq \ell_ab'/k$, the bound $\delta_I < 1/6$ and the absence of odd $d$ with $p^d$ within $2\delta_I$ of $a/b'$ in ratio, $C_H|T|Y^2(N_1^5 + k^3)\log_pa \leq D_p$, $8(D_p + 1) \leq c^*$ and $C_Hk^3|T|p^{4G'}(c^* + (|T| + n')c)Y \leq b'$. Then there is a function $\kappa \geq 0$ of $(a_w, b_w)$ whose mean over $I_a^T \times I_b^T$, where $I_a = [a, a + a/(kY)]$ and $I_b = [b_l, b_u]$, is at most $C|T|N_1/Y$, such that for every unramified quadratic setting, every base weight $(a_w, b_w, \lambda_0)$ with $\lambda_0$ dominant and $a_w(s) \in I_a$, $b_w(s) \in I_b$ for $s \in T$, and every $t \geq t_I(a_w, b_w)$, property $\mathrm{LP}'(t, D_p, \kappa(a_w, b_w), c^*)$ holds at $\lambda_0$ for edges of rank $1$.

Here $\delta_I$ is $C_H$ times an explicit multiple of $N_1\ell_a/k + (b_u - b_l)/b'$, and the threshold is
$$\begin{aligned} t_I = {} & \textstyle\sum_y \min\big(b_w(y), a_w(y^-)/p^{d(y)}\big) + C|T|(Q_c + kQ + k\log_pa + c) + 2n'c \\ & + C|T|N_1\big(a/p^2 + b'/p + \ell_aa/(pk) + \ell_ab'/k\big), \end{aligned}$$
with the sum over the covector letters $y \in T$, $y^-$ the letter before $y$, $d(y)$ its distance and $Q = p^{G'}$.

**Definition 5.12.2 (Admissibility for Theorem I).** A datum $\mathcal{D}$ is *admissible for Theorem I* with constants $(C_0, C_H, C_A, C_{E1}, C_{E2}, C_m, C_\kappa, C_t, C_c, C_s)$ if five conditions hold: the path pair correspondence (Theorem I for every instance of $\mathcal{D}$ with these constants), an edge bound, a rank bound $(1 - \kappa_p)\dim \leq \gamma\prod_s \mathrm{rk}_s$ with $\kappa_p \leq C_s|T|N_1/Y$, a lower set bound on the column families, and twelve *tools*: a projection criterion, the closure of column families, the extremal projector, the branching statements, the Schur property of global sections, the span of bracket polynomials, the Cartan statements (a product $FG$ of sections divisible by $w$ has a factor divisible by $w$, and the sections of weight $\lambda + \mu$ are spanned over $\mathcal{O}$ by products), the nested type bound, the commutation of type decompositions (with the dual height inclusion), the test side, the span of saturated lower sets, and the paired path independence (with the Weyl dimension formula). It is *admissible for large constants* if for every $C_c \geq 0$ there is $T_0 > 0$ such that for every $C_0 \geq T_0$ there is $T_1 > 0$ such that for all $C_{E1}, C_{E2}, C_m \geq T_1$ there is $T_2 > 0$ such that for every $C_H \geq T_2$ there are positive $C_A, C_\kappa, C_t, C_s$ with which $\mathcal{D}$ is admissible.

**Definition 5.12.3 (Closed form of Theorem I).** The *closed form of Theorem I* holds for $\mathcal{D}$ if, whenever $\mathcal{D}$ is admissible for Theorem I for large constants, there is $T_0 > 0$ such that for every $C_0 \geq T_0$ there are $T_2, C > 0$ with Theorem I with constants $(C_0, C_H, C)$ for every $C_H \geq T_2$.

### Lower bounds of the second estimate

For a weight $\lambda$ and an edge $e$ of rank $1$, the *cleaned modules* are
$$C(t, c, e) = w^{-t}H(\mathrm{src}\,e) \cap R_e \cap \bigcap_{e'} w^cR_{e'}, \qquad C'(t, c, e) = w^{-t}H(\mathrm{tgt}\,e)^\vee \cap R'_e \cap \bigcap_{e''} w^cR'_{e''},$$
over the other edges $e'$ of rank $1$ with the same source and $e''$ with the same target. We say $\lambda$ has *$\rho$-bound $X$ at $(t, c, D)$* if for every edge $e$ of rank $1$ the pairing $b$ on $C(t, c, e) \times C'(t, c, e)$ has good rank $(n, D)$ at $p$ for some $n \geq X$. Put $d(\lambda) = \dim V_\lambda/\gamma$, with $\gamma$ the Gaussian number of $p^{n'}$ and $m + 1$. For $A, B : T \to \mathbb{N}$ the *flat weight* $\mathrm{fl}(A, B)$ has row $(A_s, 0, \dots, 0, -B_s)$ for $s \in T$ and $0$ for $s \notin T$.

The second estimate uses four statements. *Independence of the setting*: $\mathrm{LP}'$ at $\lambda_0$ in one unramified quadratic setting implies it in every other. The *edge sum bound*: for $m \geq 2$ and $A_s + B_s + 1 \leq 8a$, a $\rho$-bound $X$ for the tensor product $V_{\mathrm{HH}}(A, B)$ of the two-letter spaces gives numbers $n_j$, for $j \leq \min(A, B)$, with $\mathrm{fl}(A - j, B - j)$ of good rank $n_j$ at depth $D + 4|T|\lceil(m + 2)\lambda_a\rceil$ and $\sum_jn_j \geq X$; here $\lambda_a = \log_p(8a + m) + 1$. The *cloud weight bound*: $\rho$-bounds $(1 - \kappa_1)d$ at $\mathrm{fl}(A, B)$ and $(1 - \kappa_2)d$ at $\mathrm{fl}(A + 2c, B + 2c)$, for a base weight with $A = a_w - c$, $B = b_w - c$, give the $\rho$-bound $(1 - \kappa_1 - 2\kappa_2 - 12|T|kc/b')d(\lambda_0)$ at $\lambda_0$, at conductor $c_2 - 2|T|c$ and depth $2D_1 + |T|\lceil m^2\lambda_a\rceil$. The *residue class count*: a $\rho$-bound $(1 - \kappa)d$ at the part of $\lambda_0$ on $T$ gives the same bound at $\lambda_0$, with $t$ raised and $c$ lowered by $2n'c$.

**Theorem 5.12.4 (Second estimate from four bounds).** Assume the independence of the setting, the edge sum bound, the cloud weight bound and the residue class count. Then the closed form of Theorem I holds for every datum.

Lean: `Formalism.MainNotions.flipOneThree.Pf.second_estimate_of_restrictions`.

*Proof.* Let $\mathcal{D}$ be admissible for large constants. Take $C_c = 4$, $C_0 \geq T_0$, $C_{E1} = C_{E2} = C_m = T_1$ and $C_H \geq T_2$; this gives the twelve tools. The last one contains the Weyl dimension formula, and with the third condition on column systems it gives $\dim V_{\mathrm{HH}}(A, B) = \prod_s\dim\mathrm{Pol}_{A_s}\dim\mathrm{Pol}_{B_s}$ and $\dim V_{\mathrm{fl}(A,B)} = \prod_s\dim\mathrm{Har}_{A_s,B_s}$.

Fix one setting $R_0$ and let $\kappa_F(A, B)$ be the infimum of the $\kappa \geq 0$ for which $\mathrm{fl}(A, B)$ has $\rho$-bound $(1 - \kappa)d$ at fixed parameters $(t^*, c_4, D_1)$ in $R_0$. Put
$$\kappa(a_w, b_w) = \kappa_F(a_w - c, b_w - c) + 2\kappa_F(a_w + c, b_w + c) + 12N_1kc/b',$$
where the first term is replaced by $1$ when $a_w - c < a$ or $b_w - c < b_l$ at some $s$.

First, $\mathrm{LP}'$. If $\kappa \geq 1$ there is nothing to prove. Otherwise the cloud weight bound passes from the two flat weights to $\lambda_0$, and the residue class count passes from the part on $T$ to $\lambda_0$; the depth and conductor stay in the range $8D_p < c^*$, $4(D_p + 1) \leq c^*$, so the $\rho$-bound at large conductor, which is proved, gives $\mathrm{LP}'(t, D_p, \kappa, c^*)$ in $R_0$ for $t \geq t_I$. Independence of the setting gives it in every setting.

Second, the mean. The edge sum bound splits the rank of the tensor product over the flat weights $\mathrm{fl}(A - j, B - j)$, the upper bound at small depth, which is proved, gives $n_j \leq d(\mathrm{fl}(A - j, B - j))$, and the rank bound of admissibility gives the tensor rank up to the defect $C_s|T|N_1/Y$. With the dimension formulas, the mean of $\kappa_F$ over the box is at most $(6(C_A + C_s) + 8)|T|N_1/Y$, and the numerical conditions hold for $C_H$ large. $\square$

**Definition 5.12.5 (Lattice functor comparison).** The *lattice functor comparison* holds if for every setting, $m \geq 2$, $T$, $a$ and $A, B$ with $A_s + B_s + 1 \leq 8a$ there are $K$-linear maps $\iota_j : V_{\mathrm{fl}(A - j, B - j)} \to V_{\mathrm{HH}}(A, B)$ and $\pi_j$ back, for $j \leq \min(A, B)$, with $\sum_j\iota_j\pi_j = \mathrm{id}$, such that for every family of lattices $M_s$ both $p^{e}\pi_j$ and $p^{e}\iota_j$ carry the integral tensor lattices into each other, where $e = |T|\lceil(m + 2)\lambda_a\rceil$.

The *cloud maps* statement is stated in Section 14.

**Theorem 5.12.6 (Theorem I from finer statements).** The independence of the setting, the lattice functor comparison and the cloud maps statement imply the closed form of Theorem I.

Lean: `Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_finer_open_statements`.

*Proof.* Take the tools at $C_c = 4$. The lattice functor comparison and the splitting of the blocks, which is proved, give the edge sum bound. The cloud maps, the perfectness of the pairing, the dual height basis and the Weyl dimension give the cloud weight bound. The tensor bound and the order bound, both proved, with the dual height basis and inclusion, give the residue class count. Apply the Theorem (Second estimate from four bounds). $\square$

**Theorem 5.12.7 (Theorem I from the lattice functor comparison).** The lattice functor comparison and the cloud maps statement imply the closed form of Theorem I.

Lean: `Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_lattice_functor_comparison`.

*Proof.* The first part of the nested type bound, a Witt identity, together with the proved isomorphism of the integral structures, gives the independence of the setting. Apply the Theorem (Theorem I from finer statements). $\square$

**Remark 5.12.8 (Formalization).** The function $\kappa$ of the second estimate is built in one setting chosen when the type of settings is nonempty, and moved to the others by the independence of the setting (TheoremIOfIntermediateBounds.lean:28). The step `theorem_I_of_intermediate_bounds`, `rho_sum_bound_of_maps_splitting`, `cloud_bound_of_maps` and the numerical facts were not unfolded, so the proof sketch of the mean bound follows their statements. `tools_of_admitted_statements` specializes the thresholds at $C_c = 4$ (TheoremIOfLatticeFunctorComparison.lean:32). `GradedLatticeStable`, `NestedTypeBound` and `TypeDecompositionsCommute` ignore their datum (ProjectionLemmaBaseLevel.lean:217 to 221). Two theorems are named `second_estimate_of_restrictions`, one in this namespace and one in `SelectionLemmas.Pf` (SegmentDegree.lean:21) with a different statement. The name `PairedPathIndependence` covers the Weyl dimension formula (ProjectionLemmaBaseLevel.lean:233).
