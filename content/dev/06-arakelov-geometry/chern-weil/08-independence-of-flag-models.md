---
title: Independence of flag models
decls:
  - GlobalTheory.T.flag_model_value_independent
  - GlobalTheory.CompanionTheory.CommAlg.FlagModelValue.main
  - GlobalTheory.T.flag_further_term_independent_statement
  - GlobalTheory.CompanionTheory.Ar.Num.flag_further_term_independent
  - GlobalTheory.T.flag_independence
  - GlobalTheory.CompanionTheory.CommAlg.FlagIndependence.main
  - GlobalTheory.T.exists_heckeCorrespondence_on_integral_shimuraModel
  - GlobalTheory.CompanionTheory.CommAlg.SegreFlag.segreFlagClosureCut
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Independence of flag models

Let $E$ and $E'$ be two bundles on a model over $O$ with the same generic fibre. The Chern numbers of the pair $(E, E')$ in [the Chern number relations](/entry/top-rel-relations/) are computed with a flag model: a refinement of the model on which both bundles have full flags with line bundle quotients, and vertical divisors that compare the two flags. This section proves that the number does not depend on the flag model. It is the splitting principle of [Section 20.3 of Volume 1](/learn/positivity-resolution/#chern-weil-forms) in a relative form over a discrete valuation ring. We keep the notation of Section 7 for models, divisors and the numbers $v(W; a_1, \dots, a_n)$.

### Flag pairs and their numbers

Let $x$ be coordinates in $\Omega$ that give a model of relative dimension $d$, as in Section 5, and let $E$, $E'$ be bundles of rank $N$ on $x$ with generic fibre $V$.

**Definition 5.8.1 (Flag pair).** A flag pair for $(E, E')$ consists of a full flag $0 = V_0 \subset V_1 \subset \dots \subset V_N = V$, vectors $\mathrm{gen}_i, \mathrm{gen}'_i \in V_{i+1}$ and degrees $m_i, m'_i \in \mathbb{Z}^K$, and forms $f_i, g_i$, such that:
1. $E$ has a graded frame for the flag with generators $\mathrm{gen}_i$ and degrees $m_i$: on each chart, locally, $E$ has a basis $b$ with $b_i - u\, t^{m_i} \mathrm{gen}_i \in V_i$ for a unit $u$ and the chart monomial $t^{m_i}$; and $E'$ has the same property with $\mathrm{gen}'_i$ and $m'_i$;
2. $\mathrm{gen}'_i - (f_i/g_i)(x)\, \mathrm{gen}_i \in V_i$;
3. $f_i/g_i$ is a vertical divisor of degree $m_i - m'_i$ on $x$.

Lean: `GroundTheory.Heights₂.Heights.IndefiniteRowSideFullHecke.NumbersDVR.Bundles.FlagPair` (also `FullFlag` and `IsGradedFrame`).

So the $i$-th graded piece of $E$ is $\mathcal{O}(m_i)$, that of $E'$ is $\mathcal{O}(m'_i)$, and $f_i/g_i$ is the map between them; it is an isomorphism on the generic fibre. A flag model of $(E, E')$ is a refinement $(x, z)$ of $x$ that is a model of relative dimension $d$ with the same function field, with a flag pair for the pull backs of $E$ and $E'$.

**Definition 5.8.2 (Intersection family).** Let $k$ be a field. An intersection family on the multiprojective spaces over $k$ assigns an integer $I(V; a_1, \dots, a_n)$ to each ideal $V$ and degrees $a_j \in \mathbb{Z}^K$, such that $I(V) $ is the degree of the point $V$ when $V$ is a point, and
$$I(V; a_1, \dots, a_n, a) = \sum_W \operatorname{ord}^V_W(f/g)\, I(W; a_1, \dots, a_n)$$
when $V$ is a projective variety of dimension $n + 1$ and $f/g$ is a rational section of $\mathcal{O}(a)$ on $V$.

Lean: `ReciprocityTheory.ChartRestriction.G.AI.I1.IsFieldIntersection`.

For a polynomial $H = \sum_\mu h_\mu X^\mu$ in variables $X_s$ with degrees $\deg_s$, put $I(V; H) = \sum_\mu h_\mu I(V; \deg^\mu)$, where $\deg^\mu$ lists each $\deg_s$ exactly $\mu_s$ times, and a term is $0$ when the list does not have length $\dim V$.

**Definition 5.8.3 (Pair number).** Let $X_1, \dots, X_r$ carry degrees $y_l$ and a second copy $X'_1, \dots, X'_r$ carry degrees $y'_l$. For $G \in \mathbb{Z}[X_1, \dots, X_r]$ and $l \le r$ let $\partial_l G$ be the divided difference that sends $X^\mu$ to
$$\Bigl(\prod_{j < l} X'^{\mu_j}_j\Bigr) \frac{X_l^{\mu_l} - X'^{\mu_l}_l}{X_l - X'_l} \Bigl(\prod_{j > l} X_j^{\mu_j}\Bigr).$$
For a model $P$ and vertical divisors $f_l/g_l$ the pair number is
$$\langle G \rangle = \sum_{l} \sum_{W} \operatorname{ord}_W(f_l/g_l)\, I(\overline W; \partial_l G),$$
where $\overline W$ is the special fibre of $W$.

Lean: `GroundTheory.Heights₂.Heights.IndefiniteRowSideFullHecke.NumbersDVR.Bundles.pairNum` (also `divDiff` and `polyNum`).

The divided differences telescope: $G(X) - G(X') = \sum_l (X_l - X'_l)\, \partial_l G$. Since $\operatorname{div}(f_l/g_l)$ has class $y_l - y'_l$, the pair number is the difference "$G(y) - G(y')$" of two intersection numbers, written as a sum of terms supported on the special fibre. The value of a flag model $F$ for $G$ symmetric in $N$ variables, extra vertical divisors $f_l/g_l$ of degree $y_l - y'_l$ on $x$, and $Q$ in $r$ variables, is the pair number on $F$ with the degrees $m \sqcup y$ and $m' \sqcup y'$, the forms $f \sqcup f$, and the polynomial $G(X_1, \dots, X_N)\, Q(X_{N+1}, \dots, X_{N+r})$.

Lean: `GroundTheory.Heights₂.Heights.IndefiniteRowSideFullHecke.NumbersDVR.Bundles.FlagModel.value` (also `FlagModel`).

### Independence

**Theorem 5.8.4 (Independence of the flag model).** Let $x$ be a model of relative dimension $d$, and let $E$, $E'$ be bundles on $x$ with the same generic fibre. Let $F_1$, $F_2$ be flag models of $(E, E')$, and let $I_1$, $I_2$ be intersection families over the residue field for their coordinates. Let $G$ be symmetric and homogeneous of degree $c \le d + 1$, let $f_l/g_l$ ($l \le r$) be vertical divisors of degree $y_l - y'_l$ on $x$, and let $Q$ be homogeneous of degree $d + 1 - c$. Then the value of $F_1$ with $I_1$ equals the value of $F_2$ with $I_2$.

Lean: `GlobalTheory.CompanionTheory.CommAlg.FlagModelValue.main` (also `GlobalTheory.T.flag_model_value_independent`, a second name).

*Proof.* Two flag models have a common refinement, the model given by the joined coordinates of both, and the flag pairs of $F_1$ and $F_2$ pull back to flag pairs on it. The value does not change under this pull back, and an intersection family is unique where it is defined. So it suffices to compare two flag pairs on one model. The pair number splits into the terms with $l \le N$, which come from the flags, and the terms with $l > N$, which come from the extra divisors. The first part does not depend on the flag pair by [the theorem on flag independence](/entry/flag-independence-main/) below, and the second part by the theorem on further terms. $\square$

**Theorem 5.8.5 (Further terms).** Let $x$, $E$, $E'$ be as above, let $\varphi_1$, $\varphi_2$ be two flag pairs for $(E, E')$ on $x$, and let $I$ be an intersection family. Let $G$, $c$, $f_l/g_l$ and $Q$ be as in the theorem above. Then for each $l \le r$ the term of index $N + l$ of the pair number of $G \cdot Q$,
$$\sum_W \operatorname{ord}_W(f_l/g_l)\, I\bigl(\overline W; \partial_{N+l}(G \cdot Q)\bigr),$$
computed with the degrees of $\varphi_1$, equals the same term computed with the degrees of $\varphi_2$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.flag_further_term_independent` (also `GlobalTheory.T.flag_further_term_independent_statement`, a second name).

*Proof.* In the term of index $N + l$ the flag variables are all in the second copy, so the term is $\sum_W \operatorname{ord}_W(f_l/g_l)\, I(\overline W; G(m') R)$ with $R$ the divided difference of $Q$. Each component $W$ of $\operatorname{div}(f_l/g_l)$ has a special fibre $\overline W$ that is a projective variety of dimension $d$, and a full flag of $E'$ restricts to a full flag on it. On a projective variety over a field, for a symmetric $G$ homogeneous of degree $c$ and two full flags with degrees $m'$ and $u'$, $\sum_\mu G_\mu I(\overline W; (m')^\mu, Y) = \sum_\mu G_\mu I(\overline W; (u')^\mu, Y)$: this is the splitting principle, since a symmetric polynomial in the roots is a polynomial in the Chern classes. $\square$

### Flag pairs on a point model

For the theorem on flag independence we use a second form of flag pairs, on the model $P_y$ given by the kernel of evaluation at a point $y$. Let $B$, $B'$ be bundles of rank $N$ on $y$ with the same generic fibre: on each chart, each vector of $B$ times a power of $\varpi$ lies in $B'$, and conversely. A flag pair $(w, w', x, x', f, g)$ consists of flag frames $w$ of $B$ with degrees $x_i$ and $w'$ of $B'$ with degrees $x'_i$, such that $w'_i$ lies in the span of $w_1, \dots, w_i$, $f_i/g_i$ is a vertical divisor of degree $x_i - x'_i$, and $(f_i/g_i)(y)$ is the $i$-th coordinate of $w'_i$ in the basis $w$. A pair expansion of $G$ homogeneous of degree $m$ is a family $G_1, \dots, G_N$ of forms of degree $m - 1$ with
$$G(X) - G(X') = \sum_i (X_i - X'_i)\, G_i.$$
For a list $Q$ of degrees put $\langle G_\bullet \rangle_Q = \sum_i \sum_W \operatorname{ord}_W(f_i/g_i) \sum_\mu G_{i,\mu}\, v(W; (x \sqcup x')^\mu, Q)$.

Lean: `GroundTheory.Heights₂.Heights.NumbersDVR.IsFlagPair` (also `IsPairExpansion` and `pairNum`).

We do not unfold the flag frames. The divided differences give one pair expansion.

**Theorem 5.8.6 (Flag independence).** Let $P_y$ be a model of relative dimension $d$, and let $B$, $B'$ be as above. Let $(w, w', x, x', f, g)$ and $(v, v', u, u', f_2, g_2)$ be two flag pairs. Let $G$ be symmetric and homogeneous of degree $m$, with pair expansions $G_\bullet$ for the first and $H_\bullet$ for the second. Then for every list $Q$ with $|Q| + m = d + 1$ the numbers $\langle G_\bullet \rangle_Q$ for the first pair and $\langle H_\bullet \rangle_Q$ for the second are equal.

Lean: `GlobalTheory.CompanionTheory.CommAlg.FlagIndependence.main` (also `GlobalTheory.T.flag_independence`, a second name).

*Proof.* By the commutativity of vertical divisors, which follows from [the theorem on cuts](/entry/cut-closed-main/), the number does not depend on the pair expansion. The products $h_\lambda$ of complete homogeneous symmetric polynomials span the symmetric polynomials of degree $m$ over $\mathbb{Z}$, and the number is linear in $G$, so we may take $G$ of the form $h_a$ times a polynomial in other divisors. For such $G$ we compute the number on the projective bundle. For $1 \le k \le N$ let $\mathcal{P}_k$ be the closure in $\mathbb{P}(B) \times \mathbb{P}(B')$ of the point given by a generic vector of $\operatorname{span}(w_1, \dots, w_k)$. It is a model of relative dimension $d + k - 1$. The theorem on Segre cuts below moves the number from $\mathcal{P}_{k+1}$ to $\mathcal{P}_k$, and a pull back lemma relates numbers on $\mathcal{P}_k$ to numbers on $P_y$. The result is a formula for the number with $h_a$ that depends on the classes of $\mathcal{O}_{\mathbb{P}(B)}(1)$ and $\mathcal{O}_{\mathbb{P}(B')}(1)$ only, and so not on the flag pair. $\square$

**Theorem 5.8.7 (Segre cut).** Keep the notation above. Let $\varphi$, $\varphi'$ be twisted dual generators of $B$ and $B'$ of twists $a_0$, $a'_0$, let $t_1, \dots, t_N$ be algebraically independent over $\Omega$, and let $\mathcal{P}_k$ be the closure model of the generic vector of $\operatorname{span}(w_1, \dots, w_k)$ with coefficients $t_i$, with new classes $\zeta$ of $\mathcal{O}_{\mathbb{P}(B)}(1)$ and $\zeta'$ of $\mathcal{O}_{\mathbb{P}(B')}(1)$. Let $k < N$. Let $f_1/g_1$ be a vertical divisor of degree $\zeta - \zeta'$ on $\mathcal{P}_{k+1}$ that is $1$ at the generic point, and if $k > 0$ let $f_2/g_2$ be one on $\mathcal{P}_k$. Let $z_j/z'_j$ be further vertical divisors on $P_y$. Let $A$ be homogeneous of degree $m$ in the variables $X_0$ (for $\zeta$), $X_1, \dots, X_N$ and $n$ more, let $A_\bullet$ be a pair expansion of $(X_0 + X_{1+k}) A$, and $B_\bullet$ one of $A$. Then for $|Q| + m + 1 = d + k + 1$,
$$\langle A_\bullet \rangle^{\mathcal{P}_{k+1}}_Q = \begin{cases} 0, & k = 0, \\ \langle B_\bullet \rangle^{\mathcal{P}_k}_Q, & k > 0, \end{cases}$$
where both numbers use the degrees $(\zeta, x, z)$, $(\zeta', x', z')$ and the forms $(f_1, f, f_z)$, $(g_1, g, g_z)$, and $(f_2, f, f_z)$, $(g_2, g, g_z)$ on $\mathcal{P}_k$.

Lean: `GlobalTheory.CompanionTheory.CommAlg.SegreFlag.segreFlagClosureCut` (also `GlobalTheory.T.exists_heckeCorrespondence_on_integral_shimuraModel`, a second name).

*Proof.* The closures $\mathcal{P}_k$ and $\mathcal{P}_{k+1}$ are models, and they carry vertical divisors of degree $\zeta - \zeta'$ that are $1$ generically. There is a form $s/h$ of degree $\zeta' + x'_k$ on $\mathcal{P}_{k+1}$ whose value is the $k$-th coordinate of the generic vector; on the generic fibre its divisor is $\mathcal{P}_k$ when $k > 0$ and $0$ when $k = 0$. Apply [the theorem on cuts](/entry/cut-closed-main/) with $s/h$. Its horizontal part gives the number on $\mathcal{P}_k$, or $0$ when $k = 0$. Its vertical part vanishes: a contraction lemma says that on each vertical component of the divisor of $s/h$ the numbers $v(W; l)$ vanish for lists $l$ that have no $\zeta'$ term. Last, the pair number does not depend on the chosen expansion, by the commutativity of vertical divisors. $\square$

**Remark 5.8.8 (Formalization).** The Chern number $c_k$ of Section 5 is defined with the power sum $p_k = \sum_i X_i^k$, not with the elementary symmetric polynomial ([InstFintypeSumElim.lean](lean:GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers/InstFintypeSumElim.lean#L249)). So it is the $k$-th power sum of the Chern roots, that is $k!\,\mathrm{ch}_k$. It uses a flag model and an intersection family chosen by the axiom of choice (lines 63 and 249), and the root number does the same (line 259); the theorem on independence makes the choice harmless. There are two parallel definitions of flag pairs and pair numbers, one with intersection families and one with the numbers $v(W; \cdot)$. The second name of the Segre cut speaks of Hecke correspondences on Shimura models, which have nothing to do with its statement ([ExistsHeckeCorrespondenceOnIntegralShimuraModelStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/ExistsHeckeCorrespondenceOnIntegralShimuraModelStatement.lean#L5)). The second names call the first with `first | exact @…`. We do not unfold the flag frames, the twisted dual generators, or the reduction of the general symmetric $G$ to $h_a$; the last step of the proof of flag independence is given at the level of the statements it combines.
