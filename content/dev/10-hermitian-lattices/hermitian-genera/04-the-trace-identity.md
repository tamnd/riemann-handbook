---
title: The trace identity for definite forms
decls:
  - GlobalTheory.LKDef.Regroup.regroup
  - GlobalTheory.T.bi_invariant_test_function_sum
  - GlobalTheory.LKDef.trace_definite_forms_identity
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The trace identity for definite forms

This section proves the main identity of the chapter. A weighted sum of the terms $T(P)$ over classes of definite pairs equals a sum of traces of Hecke operators on spaces of automorphic forms, one space for each class of definite forms. The proof has two steps. First, the sum over pairs is regrouped. A pair is a form $\beta$ together with a conjugacy class in the similitude group of $\beta$, and the term of the pair is a sum over the centralizer of that class. Second, the trace of each Hecke operator is expanded over the same conjugacy classes, and the two sides are compared term by term. The finiteness theorem of the last section makes the regrouping legal.

We keep the notation of the first section, with $r = 1$. As in the last section, $K^p$ is a level, $f$ is a test function for $(\mathrm{id}, K^p, K^p)$ with $f(k g k') = f(g)$ for $k, k' \in K^p$, and $\varphi$ is a test function for $(\sigma, K_1, K')$ with $\varphi(k g k') = \varphi(g)$ for $k, k' \in K'$. We call these the *standing assumptions*, together with $a = 1$. Let $H = G(\mathbb{A}^p) \times G_1$, $K_H = K^p \times K'$ and $F_H(h) = f(h_1)\, \varphi(h_2)$.

### Definite forms and their groups

**Definition 6.4.1 (Definite form).** A *definite form* is $B = \beta \in C^\times$ with $\beta^* = \beta$, a trivialization $(x, t)$, and condition 4 of a definite pair. Two forms are *related* if $\beta' = s\, y \beta y^*$ with $y \in C^\times$ and $s \in \mathbb{Q}$, $s > 0$. We fix a representative of each class and a trivialization $(x_B, t_B)$ of each form. A definite pair $P$ gives the form $\beta_P$.

Lean: `GlobalTheory.LKDef.DForm` (also `GlobalTheory.LKDef.DForm.Rel`, the relation).

For a form $B$, let
$$\Gamma_B = \{ (y, s) \in C^\times \times \mathbb{Q}^\times : y \beta y^* = s \beta,\ s > 0 \}.$$
Let $\iota_B \colon \Gamma_B \to H$ be the map $(y, s) \mapsto \bigl( (x_B y x_B^{-1}, s), \lambda(y, s) \bigr)$, where $\lambda(y, s)$ is taken in $G_1$. For $y \in \Gamma_B$, write $P_y$ for the minimal polynomial over $F$ of the first coordinate of $y$. We say $y$ is *regular* if $P_y$ has degree $n$ and is separable and irreducible.

**Definition 6.4.2 (Centralizer sum).** For $y \in \Gamma_B$ with centralizer $Z(y) \subseteq \Gamma_B$, let
$$S_B(y) = \sum_{[g]} |\mathrm{St}(g) \cap Z(y)|^{-1}\, f\bigl(g_1^{-1} \iota_B(y)_1\, g_1\bigr)\, \varphi\bigl(g_2^{-1} \iota_B(y)_2\, g_2\bigr),$$
over the double cosets $[g] \in \iota_B(Z(y)) \backslash H / K_H$, each with a fixed representative $g$, where $\mathrm{St}(g)$ is the group of the point sum.

Lean: `GlobalTheory.LKCount.centSum`.

**Definition 6.4.3 (Hecke trace).** Let $\xi$ be a [[representation|WYGRXCG2RN]] of $C^\times \times \mathbb{Q}^\times$ on a complex vector space $V$. Let $\mathcal{A}_B(\xi)$ be the space of $\phi \colon H \to V$ with $\phi(\iota_B(y) h) = \xi(y) \phi(h)$ for $y \in \Gamma_B$ and $\phi(h k) = \phi(h)$ for $k \in K_H$ ([automorphic forms](/learn/automorphic-forms/#automorphic-forms-on-adelic-groups)). A linear map $T$ of $\mathcal{A}_B(\xi)$ is a *Hecke operator* for $F_H$ if
$$(T\phi)(g) = \sum_{h \in H / K_H} F_H(h)\, \phi(g h)$$
for all $\phi$ and $g$, with a fixed representative $h$ of each coset. The *trace* of $B$ is the [[trace|0KZDNGA561]] of a chosen Hecke operator if one exists, and $0$ otherwise. The *trace sum* is $\sum_{[B]} \operatorname{tr}(B)$ over the classes of definite forms.

Lean: `GlobalTheory.LKDef.DForm.trace` (also `GlobalTheory.LKDef.dTrace`, the trace sum).

**Definition 6.4.4 (Weighted sum).** For $\mathrm{wt} \colon F[X] \to \mathbb{C}$, the *weighted sum* is
$$\Sigma(\mathrm{wt}) = \sum_{[P]} \mathrm{wt}(P_\gamma)\, T(P),$$
over the classes of definite pairs whose representative $P$ has irreducible $P_\gamma$.

Lean: `GlobalTheory.LKDef.dSumIrr`.

**Definition 6.4.5 (Orbital sum).** For $\delta \in H$ with centralizer $Z_H(\delta)$, let
$$O(\delta) = \sum_{[g]} \mathrm{vol}\bigl(Z_H(\delta) \cap K_H,\ Z_H(\delta) \cap g K_H g^{-1}\bigr)^{-1} F_H(g^{-1} \delta g),$$
over $[g] \in Z_H(\delta) \backslash H / K_H$, where $\mathrm{vol}(A, A') = [A' : A \cap A'] / [A : A \cap A']$, and an infinite index counts as $0$.

Lean: `GlobalTheory.LKCount.orbK`.

### Inputs

The next four results are inputs. They are proved in other parts of the development.

**Theorem 6.4.6 (Positive factor).** Let $B$ be a definite form, $y \in C^\times$ and $s \in \mathbb{Q}$ with $y \beta y^* = s \beta$. Then $s > 0$.

Lean: `GlobalTheory.LKDef.DFormPos.sim_pos`.

*Proof.* This is proved in the development at one infinite place, from the sign of the form of $\beta^{-1}$; we take it as an input. $\square$

**Theorem 6.4.7 (Term as a centralizer sum).** Let $P$ be a definite pair with $(\gamma, c) \in \Gamma_{\beta_P}$, $f$ a test function for $(\mathrm{id}, K^p, K^p)$ and $\varphi$ a test function for $(\sigma, K_1, K')$. Then $T(P) = S_{\beta_P}(\gamma, c)$, where $\iota_{\beta_P}$ uses the fixed trivialization of $P$.

Lean: `GlobalTheory.T.definitePair_term_eq_centraliser_orbit_sum` (also `GlobalTheory.LKDef.TermPair.term_eq_centSum`).

*Proof.* This is an input from the development. $\square$

**Theorem 6.4.8 (Trace as a sum over classes).** Under the standing assumptions, let $V$ be finite dimensional. For each definite form $B$,
$$\operatorname{tr}(B) = \sum_{[y]} \operatorname{tr} \xi(y)\, S_B(y),$$
over the conjugacy classes $[y]$ of $\Gamma_B$, each with a fixed representative $y$.

Lean: `GlobalTheory.T.heckeTrace_definiteForm_eq_sum_conjClasses` (also `GlobalTheory.HeckeTrace.dform_trace_eq`).

*Proof.* This is an input from the development. $\square$

**Theorem 6.4.9 (Vanishing).** Under the standing assumptions, let $B$ be a definite form and $y \in \Gamma_B$. If $O(\iota_B(y)) = 0$, then $S_B(y) = 0$.

Lean: `GlobalTheory.T.centSum_eq_zero_of_orbitalIntegral_eq_zero` (also `GlobalTheory.LKDef.DForm.centSum_eq_zero_of_orbK`).

*Proof.* This is an input from the development. $\square$

### Regrouping

**Theorem 6.4.10 (Regrouping).** Under the standing assumptions, for each $\mathrm{wt} \colon F[X] \to \mathbb{C}$,
$$\Sigma(\mathrm{wt}) = \sum_{[B]} \sum_{[y]} \mathbf{1}[y \text{ regular}]\, \mathrm{wt}(P_y)\, S_B(y),$$
where $[B]$ runs over the classes of definite forms and $[y]$ over the conjugacy classes of $\Gamma_B$, with fixed representatives.

Lean: `GlobalTheory.LKDef.Regroup.regroup`.

*Proof.* Let $I$ be the set of pairs $([B], [y])$ with $y$ regular. For such a pair, $(\beta, y_1, y_2)$ is a definite pair $P(B, y)$: the form gives conditions 1, 3 and 4, and regularity gives condition 2. Let $e([B], [y]) = [P(B, y)]$.

*The map $e$ is injective.* Let $P(B, y) \sim P(B', y')$, with $\beta' = s\, z \beta z^*$ and $y'_1 = z y_1 z^{-1}$. Then $B \sim B'$, so $B = B'$ as representatives. The element $(z, s^{-1})$ lies in $\Gamma_B$. The two pairs have the same $c$ by the lemma on related pairs in the first section, so $(z, s^{-1})$ conjugates $y$ to $y'$. Hence $[y] = [y']$.

*The image contains every class with irreducible polynomial.* Let $P$ be the representative of such a class, and $B$ the representative of the class of the form $\beta_P$, with $\beta_B = s\, z \beta_P z^*$. Let $w = (z \gamma z^{-1}, c)$. Then $w_1 \beta_B w_1^* = c\, \beta_B$, and $c > 0$ by the theorem on the positive factor, so $w \in \Gamma_B$. Conjugate elements have the same minimal polynomial, so $w$ is regular. The pair $P$ is related to $P(B, w)$, and $P(B, w)$ is related to $P(B, w')$ for the representative $w'$ of $[w]$. So $e([B], [w])$ is the class of $P$.

*The terms agree.* Let $Q$ be the representative of $e([B], [y])$. Then $Q \sim P(B, y)$. By the lemma on related pairs, $P_{\gamma_Q} = P_y$ and $T(Q) = T(P(B, y))$. By the theorem on the term as a centralizer sum, $T(P(B, y)) = S_B(y)$. So the summand of $\Sigma(\mathrm{wt})$ at $e([B], [y])$ is $\mathrm{wt}(P_y)\, S_B(y)$.

*Finiteness.* The summands of $\Sigma(\mathrm{wt})$ vanish outside the classes with irreducible polynomial and nonzero term, and these are finite in number by the corollary on finiteness for the trace. So the double sum on the right has finitely many nonzero terms, it is the sum over $I$, and by the three steps above it is the sum of $\Sigma(\mathrm{wt})$ over the image of $e$. $\square$

**Theorem 6.4.11 (The sum as a sum over centralizers).** Under the standing assumptions, the identity of the theorem on regrouping holds.

Lean: `GlobalTheory.T.bi_invariant_test_function_sum`.

*Proof.* This is the theorem on regrouping. $\square$

### The identity

**Theorem 6.4.12 (Definite pairs and automorphic traces).** Assume $a = 1$. Let $V$ be a finite dimensional complex vector space, $\xi$ a representation of $C^\times \times \mathbb{Q}^\times$ on $V$ and $\mathrm{wt} \colon F[X] \to \mathbb{C}$. Assume that $\operatorname{tr} \xi(y) = \mathrm{wt}(P_y)$ for each definite form $B$ and each $y \in \Gamma_B$ whose $P_y$ has degree $n$ and is separable. Let $K^p$, $f$, $K'$ and $\varphi$ satisfy the standing assumptions. Assume that for each definite form $B$, each trivialization $(x, t)$ of $\beta$ and each $y \in \Gamma_B$ that is not regular, the orbital sum $O$ vanishes at the image of $y$ under the map $\iota_B$ built from $(x, t)$. Then
$$\Sigma(\mathrm{wt}) = \sum_{[B]} \operatorname{tr}(B).$$

Lean: `GlobalTheory.LKDef.trace_definite_forms_identity`.

*Proof.* By the theorem on regrouping, the left side is the double sum over $[B]$ and $[y]$. By the theorem on the trace as a sum over classes, the right side is $\sum_{[B]} \sum_{[y]} \operatorname{tr}\xi(y)\, S_B(y)$. We compare the summands for each $[B]$ and $[y]$. If $y$ is regular, then $P_y$ has degree $n$ and is separable, so $\operatorname{tr}\xi(y) = \mathrm{wt}(P_y)$ and the summands agree. If $y$ is not regular, the summand on the left is $0$. The vanishing assumption, at the fixed trivialization of $B$, gives $O(\iota_B(y)) = 0$, so $S_B(y) = 0$ by the theorem on vanishing, and the summand on the right is $0$. $\square$

This is the [trace identity for definite forms](/entry/cnt-trace-definite-forms-identity/) used in Volume 9.

**Remark 6.4.13 (Formalization).** In [LieModelBaseChangeMap.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LieModelBaseChangeMap.lean#L14) the theorem proves the proposition `TraceDefinitePairsEqAutomorphicTrace` of [TraceDefinitePairsEqAutomorphicTrace.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/TraceDefinitePairsEqAutomorphicTrace.lean#L87). The module name has no relation to its content. The vanishing hypothesis is stated for every trivialization, but the proof uses it only at the trivialization chosen by `Exists.choose`. All sums are `finsum`, which is $0$ when the support is infinite. The trace of a form is defined with `Exists.choose` of a Hecke operator and is $0$ if none exists. The inverse of the cardinality of an infinite group is $0$, and the trace of a map of an infinite dimensional space is $0$ in Mathlib. With these conventions the identity is a true statement in all cases, but it says nothing when the sums are infinite. The theorem on regrouping, in RelIndexPrincipalCongruenceNeZero.lean (a name unrelated to its content), is one application of `GlobalTheory.LKDef.Regroup.regroup_main` in DformRelEquivalence.lean (line 260), which takes the positive factor, the finiteness corollary and the term theorem as hypotheses. The map $e$ is `toCls` (line 85), its injectivity is `toCls_injective` (line 90) and the image is `mem_range_toCls` (line 123). The wrapper `GlobalTheory.T.bi_invariant_test_function_sum` has a name about test functions, but it states the regrouping. The input theorems on the term, the trace and vanishing are wrappers whose proofs we did not open. The theorem on the positive factor is in FlatZeroFromResolutionAndGaga.lean, a name unrelated to its content.
