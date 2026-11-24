---
title: Chow form heights and small sections
decls:
  - ChowFormHeightComparison₂.chow_form_height_comparison
  - PositivityTheory.Xj7N.weil_height_archimedean_contribution
  - PositivityTheory.Xj7N.small_sections_injective
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Chow form heights and small sections

[The height lower bound](/entry/height-lower-bound-general-alt/) uses two *volume estimate hypotheses*, listed as the first group of [the covolume bound](/entry/top-covol-g-alt-alt/). The first bounds the arithmetic self-intersection of a shifted hermitian line bundle on an integral model of a lattice by the degree and the height of the image of the lattice. The second bounds the number of small cusp forms of weight $8i$ times a given weight by the number of small sections of the $8i$-th power of the line bundle. This section proves both. The first is a statement about Chow forms ([heights](/learn/arakelov/#heights)): the self-intersection of a line bundle with a Fubini-Study metric is the height of the Chow form of the image. The second rests on a pointwise bound for cusp forms at the archimedean places, which compares a small cusp form with the frame of the lattice.

Throughout, $K$ is a number field, $V$ a $K$-vector space and $W \subset V$ an $\mathcal{O}_K$-submodule. A family of norms $N = (N_\sigma)$ on $V$, indexed by the complex embeddings $\sigma$ of $K$, *has a Gram form* if each $N_\sigma$ comes from a positive definite hermitian form. Let $\Omega$ be a field over $K$ and $\mathrm{ev} \colon V \to \Omega$ a $K$-linear map. We say that $\mathrm{ev}$ *generates by ratios* if $\mathrm{ev} \ne 0$ and the quotients $\mathrm{ev}(v)/\mathrm{ev}(w)$ generate $\Omega$ over $K$. In a basis of $V$, the map $\mathrm{ev}$ defines a projective variety, the image, cut out by the ideal of relations among the values of the basis.

**Definition 2.17.1 (Frame of a lattice).** Let $b = (b_1, \dots, b_N)$ be a basis of $V$. A *frame* of $(W, N)$ on $b$ is a matrix $g \in K^{N \times n}$ and a family of matrices $A_\sigma \in \mathbb{C}^{N \times N}$ such that the vectors $\sum_j g_{j k} b_j$ span $W$ over $\mathcal{O}_K$, the columns of $g$ span $K^N$, each $A_\sigma$ is invertible, the family $A$ is compatible with complex conjugation, and for every $x \in V$ with coordinates $(x_j)$ in $b$,
$$N_\sigma(x) = \Bigl(\sum_i \Bigl|\sum_j (A_\sigma)_{j i} \, \sigma(x_j)\Bigr|^2\Bigr)^{1/2}.$$

So $A_\sigma$ carries the coordinates in $b$ to coordinates in an orthonormal basis of $N_\sigma$. For $y \in \mathbb{C}^N$ we write $\|A_\sigma^{\mathsf T} y\|$ for the right side with $\sigma(x_j)$ replaced by $y_j$.

**Definition 2.17.2 (Image degree and image height).** Let $D \ge 0$. The *image degree* $\delta$ of $\mathrm{ev}$ in dimension $D$ is the degree of an integral Chow form in $D + 1$ groups of $N$ variables of the image, and $0$ if there is none. The *image height* $h$ of $(W, N, \mathrm{ev})$ is defined by
$$(D + 1) \, \delta \, h = h_{\mathrm{Chow}}(f; g, A),$$
where $f$ is such a Chow form and $h_{\mathrm{Chow}}(f; g, A)$ is its height with respect to a frame, and $h = 0$ if there is none.

Let $X$ be an integral scheme, projective over $\operatorname{Spec} \mathcal{O}_K$, with a hermitian line bundle $\bar L$ ([hermitian line bundles](/learn/arakelov/#hermitian-line-bundles)), a map of fields $\psi \colon \Omega \to K(X)$ and a map $s$ from $W$ to the sections of $L$. The tuple $(X, \bar L, \psi, s)$ is a *model* of $(W, N, \mathrm{ev})$ in dimension $D$ if $X$ is a normal arithmetic variety of dimension $D$, the sections $s(w)$ match the values $\psi(\mathrm{ev}(w))$ with the same ratios, $\psi$ is compatible with the base, the sections generate $L$, and the metric is the Fubini-Study metric of a frame,
$$-\log |\cdot|^2 = \log \sum_i \Bigl|\sum_j c_{j} (A_\sigma)_{j i} \, s(b_j)\Bigr|^2$$
up to the normalization of the sections. For $t \in \mathbb{R}$ write $\bar L(t)$ for $\bar L$ with its metric multiplied by $e^{-t}$ at every place.

**Theorem 2.17.3 (Self-intersection and Chow form height).** Assume the published Hodge bundle theorems. Let $K$ have no real embeddings, let $N$ have a Gram form with $N_{\bar\sigma} = N_\sigma$, let $W$ be finitely generated and span $V$, let $\mathrm{ev}$ generate by ratios, and let the image degree $\delta$ in dimension $D$ be positive. Let $(X, \bar L, \psi, s)$ be a model in dimension $D$ and let $a$ be the arithmetic self-intersection of $\bar L(t)$ ([arithmetic intersection numbers](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers)). Then
$$a \le [K : \mathbb{Q}] (D + 1) \, \delta \, (h + t).$$

Lean: `ChowFormHeightComparison₂.chow_form_height_comparison`.

*Proof.* The published list gives the *Chow form height statement*: the self-intersection of a line bundle with the Fubini-Study metric of a frame is $[K : \mathbb{Q}]$ times the height of the Chow form of the image. It is derived from an archimedean statement on the charts and from a Mahler measure statement for sections. Now fix the data. The model gives a rational point of the generic fibre, so $X$ is a rational model of $\Omega$, and it is proper. The frame gives $b$, $g$ and $A$ with a model matrix, and the sections $s(b_j)$ give a generating family of $L$, compatible with the ratios of $\mathrm{ev}$. A volume statement compares the self-intersection with the height of the Chow form, and the Fubini-Study isometry shows that the model is isometric to the image with the metric of the frame, shifted by $t$. The self-intersection is unique, so $a$ is the value computed on the image, and
$$a = [K : \mathbb{Q}] \bigl(h_{\mathrm{Chow}}(f; g, A) + (D + 1) \delta t\bigr) = [K : \mathbb{Q}](D + 1) \delta (h + t).$$
In particular the inequality holds. $\square$

The proof gives an equality. The inequality is the form in which the result enters the height lower bound.

Now the cusp forms. Let $D$ be a family with a core, $Y$ a deep good cover at level $j$ with $[E : \mathbb{Q}]/2 > 2$, $Z$ a component and $\Omega_Z$ its function field. Let $u$ be a weight with associated weight $G$, and let $S_G(Z)$ and the generic value $f(\eta) \in \Omega_Z$ be as in [the section on birationality](/entry/bir-on-of-weight-gaps-large/). The lattice $\Lambda_Z(G)$ of [the section on good covers](/entry/covering-regular-at-domain/) carries the Petersson norms. For a good embedding $\sigma$ and a frame $y$ on $Z$ let $|f|_y$ be the pointwise norm and $\beta_Z(y)$ the Bergman kernel of weight $G$, as in [the section on the Bergman kernel](/entry/theta-function-le-bergman-kernel-alt/).

**Definition 2.17.4 (Small cusp forms).** Let $\tau \ge 1$ and $t \in \mathbb{R}$. The set $\mathcal{L}(\tau, t)$ of *small cusp forms* consists of the $f \in S_{\tau G}(Z)$ with $v(f) \ge \tau \operatorname{depth}_Z(v)$ at every recording valuation $v$, and
$$|f|_y^2 \le e^{2 \tau t} \beta_Z(y)^\tau$$
at every good $\sigma$ and every frame $y$ on $Z$.

The *nonvanishing hypothesis* NV says: for every CM field, datum, level and coefficient field with $p + q \ge 1$, every complex framed point $y$ and every dominant exponent $a$, there is a dominant exponent $a'$ with sections $g$ of exponent $a'$ and $f$ of exponent $a + a'$ such that $g(y) \ne 0$ and $f(y) \ne 0$.

**Theorem 2.17.5 (Archimedean bound for small cusp forms).** Assume NV and the published Hodge bundle theorems. Let $G$ be good on $Z$ and birational on $Z$, assume that $G$ has no base points on $Z$ and that the degree of $u$ on $Z$ is positive. Let $b$ be a basis of $S_G(Z)$ with a frame $(g, A)$ of $\Lambda_Z(G)$, let $\sigma$ be an embedding of the coefficient field and $\rho \colon \Omega_Z \to \mathbb{C}$ a map of fields over $\sigma$. Then for every $\tau \ge 1$ and every $f \in \mathcal{L}(\tau, t)$,
$$\bigl|\rho(f(\eta))\bigr| \le e^{\tau t} \, \bigl\|A_\sigma^{\mathsf T} \bigl(\rho(b_i(\eta))\bigr)_i\bigr\|^\tau.$$

Lean: `PositivityTheory.Xj7N.weil_height_archimedean_contribution`.

*Proof.* The flag space has dimension at least $1$, because $p + q = r \ge 2$. The published list gives a toroidal flag bundle. The key step is a spanning statement: for every good $\sigma$, every holomorphic section $P$ of the model weight of $G$ agrees on the frames of $Z$ with a complex combination of cusp forms of weight $G$. To see it, NV makes the local unit map surjective: on the frames of $Z$, $P$ is a combination of finitely many sections that extend and vanish on the boundary. Each such section has a matching cusp form of weight $G$ with the same values on the frames. So $P$ agrees on the frames with the same combination of the matching cusp forms.

With the spanning statement, a general estimate for small sections applies. In the frame $A$, the functions $\sum_j (A_\sigma)_{j i} b_j$ form an orthonormal basis of $S_G(Z)$ at $\sigma$, and, as the holomorphic sections are spanned by cusp forms on the frames, the Bergman kernel $\beta_Z$ is the sum of their squared norms. The bound $|f|_y^2 \le e^{2\tau t} \beta_Z(y)^\tau$ then passes to the complex point $\rho$ of the generic point, and gives the inequality. $\square$

Let $d$ be the dimension of the flag space. Let $(X, \bar L, \psi, s)$ be a model of $(\Lambda_Z(G), \text{Petersson norms}, f \mapsto f(\eta))$ in dimension $d$, over the ring of integers of the coefficient field. A section of a power of $\bar L(t)$ is *small* if its pointwise norm is at most $1$ at every complex point.

**Theorem 2.17.6 (Small sections).** Assume NV and the published Hodge bundle theorems, and the hypotheses on $G$ of the previous theorem. Let $(X, \bar L, \psi, s)$ be a model in dimension $d$ as above, and $t \in \mathbb{R}$. Then for every $i \ge 1$,
$$\#\mathcal{L}(8 i, t) \le \#\bigl\{\text{small sections of } \bar L(t)^{\otimes 8 i}\bigr\},$$
as cardinals in $\mathbb{N} \cup \{\infty\}$.

Lean: `PositivityTheory.Xj7N.small_sections_injective`.

*Proof.* The result is the composition of three statements. The first is the archimedean bound of the previous theorem. The second turns it into a comparison of Weil heights: through $\psi$, a cusp form $f \in \mathcal{L}(8 i, t)$ gives a section $s_f$ of $L^{\otimes 8 i}$, and the norm of $s_f$ in the Fubini-Study metric of the frame is $|f(\eta)|$ divided by the $8 i$-th power of $\|A_\sigma^{\mathsf T}(b_j(\eta))\|$, read at each complex point. By the previous theorem this is at most $e^{8 i t}$, so $s_f$ is small for $\bar L(t)^{\otimes 8 i}$. The third statement says that $f \mapsto s_f$ is injective, since $\psi$ is a map of fields and $f$ is determined by its generic value. An injective map gives the inequality of cardinals. $\square$

The factor $8$ matches the weights $8 k u_1$ and $8 k u_1'$ of the height lower bound, where the carrying section has exponent $a = 8$.

**Remark 2.17.7 (Formalization).** In the archimedean bound the hypotheses `NoBase` and `0 < Y.dg u Z` are introduced as `_` and never used ([WeilHeightArchimedeanContribution.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/WeilHeightArchimedeanContribution.lean#L27)); the estimate itself is `norm_small_le` (NormGenValLe.lean, line 69), whose proof we did not read, so the explanation above of how it applies is ours; the spanning step uses `local_unit_map_surjective` and `extVan_section_has_cusp_form_match`. In `weil_height_inequality`, which proves the Chow form theorem from `chow_form_height_bound`, four hypotheses (no real embeddings, the Gram form, conjugation invariance and finite generation) are introduced as `_` ([WeilHeightInequality.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/WeilHeightInequality.lean#L11)), and the proof ends with `le_of_eq` at line 31, so the inequality is an equality. The small sections theorem is a term that composes `weil_height_archimedean_contribution`, `weil_height_comparison_of_degree_bound` and `small_sections_injective_of_self_intersection_bound`; we read only the first, and the description of the other two follows their names and the definitions of `smallL`, `smallSec` and `IsModelOf`. The Chow form height statement is `ChowFormHeight` (VuSelfKnownTheorem.lean, line 12), proved from the field `p4` of the published list. The definitions of the image degree and height are `imageDeg` and `imageHeight` (AevalEqZeroOfMemConeIdeal.lean, lines 203 and 240), and the frame is `IsFrame` (line 220). We have not unfolded `formHeight`, `IsChowFormInt`, `homN` or `bergOn`.
