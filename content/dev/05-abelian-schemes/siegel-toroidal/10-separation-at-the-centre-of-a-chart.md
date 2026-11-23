---
title: Separation at the centre of a chart
decls:
  - GlobalTheory.T.chartSeparationData_defined_over_centre_field
  - GlobalTheory.Poinc.Sep.sepSt
  - GlobalTheory.T.torsion_theta_values_abelianPart_defined_over
  - GlobalTheory.Poinc.Sep.torsion_theta_points_defOver
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Separation at the centre of a chart

A pre-chart at a point $x$ of the normalized blowup $S$ needs the map $\mathcal{O}_{S,x} \to R$ to be an étale completion. This section proves the separation statement behind that clause. Take a local domain $V$ over $S$ with Mumford data $Q$ whose periods are monomials in elements $s_i$ of $V$, and a map $\mathrm{ev} : V \to K$ to an algebraically closed field that sends $\operatorname{Spec} K$ to the image of the closed point and is defined over an algebraically closed subfield $k_0$. Then the boundary parameters vanish under $\mathrm{ev}$, the torsion points of the abelian part are defined over $k_0$, and each $\mathrm{ev}(s_i)$ lies in $k_0$ when $Q$ comes from a base whose values lie in $k_0$. The statement is used for the [centre of a tautological chart](/entry/tautological-chart-centre-is-completed-etale-local-map/), and through it for the [theorem on charts](/entry/chart-st5-holds/).

We keep the notation of the previous sections. $F$ is a Siegel family of genus $g$ and level $n$ over $\Lambda_n$, with base $s : X \to \operatorname{Spec}\Lambda_n$ and universal datum $(A, P, \ell)$. $V$ is a local domain and $Q$ is Mumford data over $V$.

**Definition 9.10.1 (Defined over a subfield).** Let $k_0$ be a subfield of a field $K$ and $p : \operatorname{Spec} K \to Y$ a map of schemes. Then $p$ is *defined over* $k_0$ if $p$ factors as $\operatorname{Spec} K \to \operatorname{Spec} k_0 \to Y$.

Lean: `GlobalTheory.Poinc.Sep.DefOver`.

**Definition 9.10.2 (Periods from parameters).** A *system of generators* $\tau_0$ for $Q$ gives for all $a, b \in Y_Q$ a section $\tau_0(a, b)$ of the bundle on $\operatorname{Spec} K_V$ in which $\tau_Q(a, b)$ lies. Let $s_1, \dots, s_N \in V$ and let $\varepsilon_1, \dots, \varepsilon_N$ be bilinear forms on $Y_Q$. The periods of $Q$ are *given by* $(s, \varepsilon)$ over $\tau_0$ if each $\tau_0(a, b)$ is generating and
$$\tau_Q(a, b) = \prod_i s_i^{\varepsilon_i(a, b)} \cdot \tau_0(a, b).$$
Let $\iota : W_0 \to V$ be a ring map. The data $Q$ *come from* $W_0$ over $\tau_0$ if there are an abelian scheme $B_0$ over $W_0$ with a line bundle $M_0$, sections $c_0(a)$ of $B_0$ and generating sections $\tau_1(a, b)$ of the corresponding bundles over $W_0$, such that $B_Q$ is the group pullback of $B_0$ along $\operatorname{Spec}\iota$ by some $\beta$, $\Lambda(M_Q) \cong (\beta \times \beta)^* \Lambda(M_0)$ by a generating isomorphism $w$, $\beta \circ c_Q(a) = c_0(a) \circ \operatorname{Spec}\iota$, and $\tau_0(a, b) = w \cdot \tau_1(a, b)$.

Lean: `GlobalTheory.Poinc.Sep.TauIn` (also `GlobalTheory.Poinc.Sep.Gens`, `GlobalTheory.Poinc.Sep.FromBase`).

**Definition 9.10.3 (Uniformized over a point).** Let $j : X \to S$ and $\xi : \operatorname{Spec} V \to S$. The data $Q$ are *uniformized over* $\xi$ if $V$ is a CN domain and for each local CN domain $R'$ with an injective finite map $\rho : V \to R'$ and all degeneration data $D$ over $R'$ that refine $Q$ along $\rho$ and some $Y_D \cong Y_Q$, there are a semi-abelian group $G'$ over $R'$, a uniformization of $G'$ by $D$ and some $A'$, and $y' : \operatorname{Spec} K_{R'} \to X$ with $j \circ y' = \xi \circ \operatorname{Spec}\rho \circ \iota_{R'}$, such that $A'$ is the group pullback of $A$ along $y'$ with the bundle of $A'$ isomorphic to the pullback of $\Lambda(P)$.

Lean: `GlobalTheory.Poinc.Sep.UnifOver`.

**Definition 9.10.4 (Separated).** Let $s : \{1, \dots, m\} \sqcup \{1, \dots, N\} \to V$, let $\mathrm{ev} : V \to K$ be a map to a field and $k_0 \subseteq K$ a subfield. Write $p_V = \operatorname{Spec}\mathrm{ev}$. Then $(Q, \tau_0, s)$ is *separated* at $\mathrm{ev}$ over $k_0$ if:

1. $\mathrm{ev}(s_{\mathrm{inl}\,i}) = 0$ for each $i \le m$;
2. for each Siegel family $F'$ of level $n' \ge 1$, with base $s' : X' \to \operatorname{Spec} o'$ and universal datum $(A', P', \ell')$, each $\lambda : \operatorname{Spec} V \to X'$ and $\beta$ such that $B_Q$ is the group pullback of $A'$ along $\lambda$ by $\beta$, with $\Lambda(M_Q)$ isomorphic to the pullback of $\Lambda(P')$, if $s' \circ \lambda \circ p_V$ is defined over $k_0$, then $\beta \circ c_Q(a) \circ p_V$ is defined over $k_0$ for each $a \in Y_Q$;
3. for each ring map $\iota : W_0 \to V$ such that $Q$ comes from $W_0$ over $\tau_0$ and $\mathrm{ev}(\iota(W_0)) \subseteq k_0$, every $\mathrm{ev}(s_i)$ lies in $k_0$.

Lean: `GlobalTheory.Poinc.Sep.SepAt`.

The next theorem is clause 2 for Mumford data that sit under an eighth power with theta terms. The *sharp refinement* $(D, e)$ of $Q$ along $\rho$ and the theta terms of level $N_1$ are defined in the section on [uniformized members](/entry/exists-u-mem/); here we use them only through the theorem.

**Theorem 9.10.5 (Torsion points of the abelian part).** Let $l$ be an odd prime and $W$ an $8 \times 8$ integer matrix with $W + W^{T}$ positive definite of determinant $1$. Then there is $j_0$ such that the following holds for each $j \ge j_0$. Let $V$ be a domain, $V_1$ a local CN domain in which $l$ is a unit, $Q$ Mumford data over $V$ with abelian part of dimension at most $g$, and $\rho : V \to V_1$ injective. Let $(D, e)$ be a sharp refinement of $Q$ along $\rho$ for $W$, with $e : Y_Q^8 \cong Y_D$. Let $u(\mu, c)$ and $\mathrm{mo}(\mu)$ be elements of $V_1$ with $\mathrm{mo}(\mu) \ne 0$ and some $u(\mu, c)$ a unit for each $\mu$, such that the products $u(\mu, c)\,\mathrm{mo}(\mu)$ are theta terms of $D$ of level $(l^j)^2$. Let $\mathrm{ev} : V_1 \to K$ be a map to an algebraically closed field and $k_0 \subseteq K$ an algebraically closed subfield such that $\mathrm{ev}(u(\mu, c)) \in k_0 \cdot \mathrm{ev}(u(\mu, c'))$ whenever $u(\mu, c')$ is a unit. Then clause 2 of separation holds for $Q$ and the map $\mathrm{ev} \circ \rho$.

Lean: `GlobalTheory.Poinc.Sep.torsion_theta_points_defOver` (also `GlobalTheory.T.torsion_theta_values_abelianPart_defined_over`, a wrapper).

*Proof.* A theorem on conjugate torsion points gives $j_0$. Let $p_V = \operatorname{Spec}(\mathrm{ev} \circ \rho)$, fix $F'$, $\lambda$, $\beta$ as in clause 2 and $a \in Y_Q$. A lemma on base change gives the pullback square of $B_Q$ along $p_V$. Let $p$ be the point of the pullback of $B_Q$ over $\operatorname{Spec} K$ given by $c_Q(a) \circ p_V$. For each automorphism $\sigma$ of $K$ over $k_0$, the theorem on conjugate torsion points shows that the conjugate of $p$ by $\sigma$ is again the image of $p$ under an identification of the fibre of $F'$ at $s' \circ \lambda \circ p_V$, which is defined over $k_0$. A lemma on Siegel fibres shows that there are only finitely many such identifications. So the orbit of $\beta \circ c_Q(a) \circ p_V$ under the automorphisms of $K$ over $k_0$ is finite. As $k_0$ is algebraically closed, a lemma on finite orbits shows that the point is defined over $k_0$. $\square$

**Theorem 9.10.6 (Separation at the centre).** Let $g \ge 1$ and $n \ge 3$ odd. Let $(Z, z, i)$ be a theta compactification of $F$, and $\varphi$ a polarization function of rank $g$ with no self-intersections. Let $d \ge 1$, $J$ an ideal sheaf on $Z$ whose support does not meet $i(X)$ and which has valuation $d\varphi$ along traits through $i$, $\pi : S \to Z$ a normalized blowup of $J$ and $j : X \to S$ with $\pi \circ j = i$. Let $Q$ be Mumford data over a local domain $V$, uniformized over $\xi : \operatorname{Spec} V \to S$. Let $s : \{1, \dots, m\} \sqcup \{1, \dots, N\} \to V$, let $\varepsilon$ be a basis of the balanced forms on $Y_Q$ indexed in the same way, and $\tau_0$ a system of generators for $Q$. Assume:

1. $Y_Q$ has rank at most $g$, the $\varepsilon_{\mathrm{inl}\,k}$ are a cone for $\varphi$, and for each $y \ne 0$ some $\varepsilon_{\mathrm{inl}\,k}(y, y) > 0$;
2. each $s_{\mathrm{inl}\,k}$ is a nonzero element of $\mathfrak{m}_V$ and each $s_{\mathrm{inr}\,k}$ is a unit;
3. the periods of $Q$ are given by $(s, n\varepsilon)$ over $\tau_0$.

Let $\mathrm{ev} : V \to K$ be a map to an algebraically closed field and $k_0 \subseteq K$ an algebraically closed subfield such that $\xi \circ \operatorname{Spec}\mathrm{ev}$ has image $\xi(\mathfrak{m}_V)$ and is defined over $k_0$. Then $(Q, \tau_0, s)$ is separated at $\mathrm{ev}$ over $k_0$.

Lean: `GlobalTheory.Poinc.Sep.sepSt` (also `GlobalTheory.T.chartSeparationData_defined_over_centre_field`, a wrapper; the statement is `GlobalTheory.Poinc.Sep.SepSt`).

*Proof.* Step 1 (the chart data). Put $t_k = s_{\mathrm{inl}\,k}$ and $\delta_k = n\varepsilon_{\mathrm{inl}\,k}$. The $\delta_k$ are symmetric, $\delta_k(y, y) \ge 0$, and for each $y \ne 0$ some $\delta_k(y, y) > 0$. As the $s_{\mathrm{inr}\,k}$ are units, $Q$ has monomial periods $t^\delta$. Composing with $\pi$, $Q$ is uniformized over $\pi \circ \xi$ for $i$.

Step 2 (the level). Let $l$ be the least prime factor of $n$, so $l$ is odd. The previous theorem gives $j_1$, and a lemma on theta coefficients of the eighth power gives $j_2$, both for the genus of $Q$, $l$ and the matrix $W$ of the theta compactification.

Step 3 (a chart member). The theorem on [Fourier term systems with traits](/entry/exists-chart-member-traits-r/) at $\max(j_1, j_2, 1)$ gives $j \ge \max(j_1, j_2, 1)$, a Fourier term system $\Phi$ of level $N_1 = (l^j)^2$ over a stalk of a theta setup, an index $y$ and $\rho : V \to V_y$ such that $\Phi$ has the traits property and $y$ is a chart member for $(Q, \pi \circ \xi, t, \delta)$, with a sharp refinement $(D, e)$ and theta terms $u(\mu, c)\,\mathrm{mo}(\mu)$ of $D$.

Step 4 (values). A lemma on stalk elements gives $\mathrm{ev}_1 : V_y \to K$ with $\mathrm{ev}_1 \circ \rho = \mathrm{ev}$ and approximations of the leading terms by elements with values in $k_0$. As $\varphi$ is a polarization function, it has integral supports of some order $d_0$. A lemma on Poincaré approximations, which uses that $\varphi$ has no self-intersections, then gives three facts on the values of $\Phi$ at $\mathrm{ev}_1$: each $\mathrm{ev}_1(t_k)$ is $0$, the ratios of the $u(\mu, c)$ have values in $k_0$, and certain ratios of products of units have values in $k_0$.

Step 5 (clause 1). This is the first fact, as $t$ corresponds to the parameters of $\Phi$ at $y$.

Step 6 (clause 2). The number $n$ is a unit in $V$, as $V$ lies over $\Lambda_n$, so $l$ is a unit in $V_y$. The previous theorem at $j$, with the second fact, gives clause 2.

Step 7 (clause 3). Let $Q$ come from $\iota : W_0 \to V$ with $\mathrm{ev}(\iota(W_0)) \subseteq k_0$. For $s_{\mathrm{inl}\,i}$ the value is $0 \in k_0$. Fix $k$ and consider $s_{\mathrm{inr}\,k}$. The lemma on theta coefficients gives, for each $\mu, c$, an element $r \in k_0$ with $\mathrm{ev}_1(u(\mu, c)) = r \prod_{k'} \mathrm{ev}(s_{\mathrm{inr}\,k'})^{q_W(n\varepsilon_{\mathrm{inr}\,k'})(\mu)}$, where $q_W(\beta)(\mu) = \sum_{u, v} W_{uv}\,\beta(\mu_u, \mu_v)$. Choose a linear form $\lambda$ on the bilinear forms that is a positive multiple $c_0$ of the coordinate of $\varepsilon_{\mathrm{inr}\,k}$ on balanced forms; it kills each $\delta_{k'}$. The third fact gives two products of unit terms whose ratio has value in $k_0$ and whose exponents of $s_{\mathrm{inr}\,k'}$ differ by $M n c_0$ for $k' = k$ and by $0$ otherwise, with $M n c_0 > 0$. So some positive power of $\mathrm{ev}(s_{\mathrm{inr}\,k})$ lies in $k_0$, and $\mathrm{ev}(s_{\mathrm{inr}\,k}) \in k_0$ as $k_0$ is algebraically closed. $\square$

**Remark 9.10.7 (Formalization).** The proof of `sepSt` unpacks the theta compactification as `⟨hproj, hnorm, hoi, hiz, hdense, W, hE8, hTI⟩` and works with its matrix $W$ ([ChartSeparationDataDefinedOverCentreField.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChartSeparationDataDefinedOverCentreField.lean#L146)); the hypothesis of no self-intersections is used only in the lemma on Poincaré approximations. The level $l$ is `n.minFac`, and the last step of clause 3 is the helper `mem_of_ratio` ([ChartSeparationDataDefinedOverCentreField.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChartSeparationDataDefinedOverCentreField.lean#L80)). The theorem `torsion_theta_points_defOver` takes its $j_0$ from `T.conjugate_torsion_point_polarised_fibre_image`, which is proved in the next part ([TorsionThetaValuesAbelianPartDefinedOver.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TorsionThetaValuesAbelianPartDefinedOver.lean#L19)). The wrappers use `first | exact @X | ...` under `maxHeartbeats 1000000` ([ChartSeparationDataDefinedOverCentreFieldStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChartSeparationDataDefinedOverCentreFieldStatement.lean#L12)). The predicates `IsThetaCompact`, `Elements`, `Values`, `Refines` and `IsGrpPullback`, and the lemmas on stalk elements, Poincaré approximations, theta coefficients, base change, Siegel fibres and finite orbits, have no entries in this part; we use only their statements.
