---
title: Heat operators at the closed point
decls:
  - GlobalTheory.HeatUConn.uconn
  - GlobalTheory.T.heatOperator_symbolZero_eq_connection
  - GlobalTheory.UnitsEval.units_eval
  - GlobalTheory.T.unitPart_psi_tau_tangent_vector_variation
  - GlobalTheory.UnitsAlong.unitTau_along
  - GlobalTheory.T.unitPart_periods_constant_along_tangent
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Heat operators at the closed point

This section and the next prove the rigidity of the fan charts from the heat operators of Sections 17 to 20. Here we work on a chart ring. A derivation $D$ that preserves the boundary gives a tangent vector $\rho$ of the chart at the closed point. Suppose that $D$ has a basic heat operator with defect $0$ whose symbol lies in the maximal ideal. Then the heat operator is a connection on the closed fibre, and it compares the pullbacks of the degeneration data along $\rho$ and along the constant map. We show that the periods change along $\rho$ only by the factors $1 + \varepsilon \sum_i a_i \gamma_i(y, z)$ of Section 1, with explicit rates $a_i$. Section 23 uses this to prove that the degeneration data are constant along $\rho$, which is the input of the rigid charts in Section 24.

We fix the data. Let $k$ be a field of characteristic $0$ and let $R = k[[u_1, \dots, u_m, v_1, \dots, v_e]]$ be the chart ring of Section 1. It is a complete Noetherian local domain that contains $\mathbb{Q}$, so the data of Section 17 apply. For $r \in R$ we write $r(0) \in k$ for its constant coefficient. Let $t$ be a semi-abelian datum on $\operatorname{Spec} R$ and $P$ a uniformization of $t$ by degeneration data $Q$, with abelian part $A$, line bundle $L$, character lattice $X$, points $c(y)$ of $A$, periods $\psi(y)$ and $\tau(y, z)$, and rigidification $\mathrm{rig}$ of $L$ at the origin. Suppose that $Q$ is monomial in $u_1, \dots, u_m$ with linearly independent exponents $\gamma_1, \dots, \gamma_m$, and that the abelian locus of $G$ is $D(u_1 \cdots u_m)$. Let $H$ be a Raynaud extension of $Q$, $v_1, \dots, v_n$ a basis of its tangent vectors at the origin and $\partial_1, \dots, \partial_n$ invariant vector fields for them. Let $D$ be a derivation of $R$ with $D(u_i) = q_i u_i$ for elements $q_i \in R$, and let $h$ be a basic heat operator for $D$ with defect $0$ whose symbol $\Theta$ has all entries in $\mathfrak{m}_R$.

Let $\rho : R \to k[\varepsilon]$ be the ring map $\rho(r) = r(0) + \varepsilon\, (D r)(0)$, and let $\bar\rho(r) = r(0)$ be the constant map that $\rho$ gives modulo $\varepsilon$. Since $D(u_i) = q_i u_i$, we have $\rho(u_i) = 0$.

A *comparison* for $\rho$ consists of a group scheme $B'$ over $k[\varepsilon]$, maps $\pi_1, \pi_2 : B' \to A$ and sections $c'(y)$ of $B'$ over $k[\varepsilon]$ for $y \in X$, such that:

1. $B'$ with $\pi_1$ is the pullback of the group $A$ along $\operatorname{Spec} \rho$, and $B'$ with $\pi_2$ is its pullback along $\operatorname{Spec} \bar\rho$;
2. $\pi_1 x = \pi_2 x$ for each point $x$ of $B'$ that lies over $\operatorname{Spec} k$, the closed subscheme $\varepsilon = 0$;
3. $\pi_1 c'(y) = c(y) \circ \operatorname{Spec} \rho$ and $\pi_2 c'(y) = c(y) \circ \operatorname{Spec} \bar\rho$ for each $y$.

Let $w : \pi_1^* L \to \pi_2^* L$ be an isomorphism of line bundles. All values of sections below are taken in trivializations of $L$ from its cover, and the identities hold for each such choice. For a point $s$ of $B'$, write $w(s)$ for the unit by which $w$ acts at $s$ in the trivializations at $\pi_1 s$ and $\pi_2 s$. For a generator $\theta$ of a fibre of a tensor combination of $L$ at points of $A$ over $\operatorname{Spec} R$, write $\theta(\rho)$ and $\theta(\bar\rho)$ for its pullbacks along $\operatorname{Spec} \rho$ and $\operatorname{Spec} \bar\rho$, read as units of $k[\varepsilon]$.

For $\alpha \in X$ let $\phi_0, \dots, \phi_3$ be the maps of $A$ to itself given by the identity, the translation by $c(\alpha)$, the constant map with value $c(\alpha)$ and the constant map with value $c(0)$. For $e \ge 1$ put $(\epsilon_0, \dots, \epsilon_3) = (e - 1, 1, -1, 1)$. These are the four factors of the bundle of $\Gamma_{e,\alpha}$ in Section 17, with their exponents.

**Theorem 7.22.1 (Heat operator at the closed point).** Let the data be as above, with a comparison $(B', \pi_1, \pi_2, c')$ for $\rho$ and an isomorphism $w$. Then there are units $\kappa_e \in k[\varepsilon]^\times$ and additive maps $\ell_e : X \to k$ for $e \in \mathbb{N}$ with the following property. Let $e \ge 1$, $\alpha \in X$ and $\sigma, \sigma' \in \Gamma_{e,\alpha}$ such that $h$ acts from $\sigma$ to $\sigma'$. Let $x$ be a point of $B'$ and $x_0, \dots, x_3$ points of $B'$ over the same point of $\operatorname{Spec} k[\varepsilon]$ with $\pi_1 x_j = \phi_j(\pi_1 x)$ and $\pi_2 x_j = \phi_j(\pi_2 x)$. Then
$$\sigma(\pi_1 x) \prod_{j=0}^{3} w(x_j)^{\epsilon_j} = \kappa_e\, \bigl(1 + \varepsilon\, \ell_e(\alpha)\bigr) \Bigl(\sigma(\pi_2 x) + \frac{\varepsilon}{2e}\, \sigma'(\pi_2 x)\Bigr).$$

Lean: `GlobalTheory.HeatUConn.uconn` (also `GlobalTheory.T.heatOperator_symbolZero_eq_connection`, a second name).

The left side transports $\sigma$ from the pullback along $\rho$ to the pullback along $\bar\rho$ by $w$. The right side is the first-order Taylor expansion of $\sigma$ along $D$, as the heat equation $2e\, D \sigma = \mathcal{H} \sigma$ gives it when the symbol vanishes.

*Proof.* Let $A_0$ be the closed fibre of $A$, the pullback along $\operatorname{Spec}$ of $r \mapsto r(0)$, with its map $m_0 : A_0 \to A$. Since $\bar\rho$ factors through $k$, the map $\pi_2$ factors as $m_0 \circ \mathrm{pr}$ for a map $\mathrm{pr} : B' \to A_0$ over the inclusion $k \to k[\varepsilon]$. The pullback of $B'$ to $\operatorname{Spec} k$ maps onto $B'$, so condition 2 gives $\pi_1 = \pi_2$ on the underlying points. Fix $e \ge 1$. There are three steps.

1. A lemma on the closed fibre uses that $\Theta \in \mathfrak{m}_R$. It gives opens $V_i$ of $A$ with $W_i = q^{-1}(V_i)$, functions $\eta_i$ on $m_0^{-1}(V_i)$, and maps $\nabla$ from functions on an open $W$ of $A$ to functions on $m_0^{-1}(W)$, which form a connection on the closed fibre along the derivation $r \mapsto$ the $\varepsilon$-part of $\rho(r)$, with connection forms $\eta_i$. If $\pi_1^* f = \pi_2^* f + \varepsilon\, \mathrm{pr}^* \nabla f$ for each function $f$, the lemma also gives an additive map $c_e : X \to k$ such that for all $\sigma, \sigma'$ as in the theorem
$$m_0^* \sigma' = 2e \Bigl(\nabla \sigma + m_0^* \sigma \cdot \bigl(\textstyle\sum_j \epsilon_j\, T_j^* \eta_{i(j)} + c_e(\alpha)\bigr)\Bigr)$$
on the closed fibre, where $T_j$ lifts $\phi_j$ to $A_0$ and $i(j)$ indexes the trivialization used for the $j$-th factor.
2. A second lemma, on the identification of the connection with the derivation, gives the hypothesis $\pi_1^* f = \pi_2^* f + \varepsilon\, \mathrm{pr}^* \nabla f$ of step 1, and a unit $\kappa$ of $k[\varepsilon]$ such that $w$ is $\kappa\, (1 + \varepsilon\, \mathrm{pr}^* \eta_i)$ on $\pi_2^{-1}(V_i)$.
3. Put $\kappa_e = \kappa^e$ and $\ell_e = -c_e$. By step 2, $\sigma(\pi_1 x) = \sigma(\pi_2 x) + \varepsilon\, (\nabla \sigma)(\mathrm{pr}\, x)$ and $w(x_j) = \kappa\, (1 + \varepsilon\, \eta_{i(j)}(T_j\, \mathrm{pr}\, x))$. Since $\sum_j \epsilon_j = e$ and $\varepsilon^2 = 0$, the left side of the claim is
$$\kappa^e \Bigl(\sigma(\pi_2 x) + \varepsilon \bigl(\nabla \sigma + \sigma \textstyle\sum_j \epsilon_j\, T_j^* \eta_{i(j)}\bigr)(\mathrm{pr}\, x)\Bigr).$$
By step 1 the $\varepsilon$-part is $\sigma'(\pi_2 x) / 2e - c_e(\alpha)\, \sigma(\pi_2 x)$. With $(1 - \varepsilon c_e(\alpha))(s + \varepsilon s') = s + \varepsilon (s' - c_e(\alpha) s)$ this is the claim.

For $e = 0$ any $\kappa_0$ and $\ell_0$ will do, since the claim asks $e \ge 1$. $\square$

The next theorem evaluates the units of the periods. A *unit part* of $\psi(\mu)$ is a pair of $n \in \mathbb{N}^m$ with $\gamma_i(\mu, \mu) = 2 n_i$ and a generator $\psi_0$ with $\psi(\mu) = \psi_0 \prod_i u_i^{n_i}$. A *unit part* of $\tau(y, z)$ is a generator $\tau_0$ with $\tau(y, z) = \tau_0 \prod_i u_i^{\gamma_i(y, z)}$ over $\operatorname{Frac} R$. By the monomial condition, each $\psi(\mu)$ has a unit part.

**Theorem 7.22.2 (Units of the periods along a tangent vector).** Let the data be as in the previous theorem. Then there is a map $\lambda : \mathbb{N} \times X \to k$ with the following property. Let $\mu, \alpha \in X$, let $(n, \psi_0)$ be a unit part of $\psi(\mu)$ and $\tau_0$ a unit part of $\tau(\mu, \alpha)$, and put $U = \psi_0^e\, \tau_0\, \mathrm{rig}^e$. Then there is $e_0$ such that for each $e \ge e_0$
$$U(\rho) = \frac{w(c'(\mu))^{e-1}\, w(c'(\mu + \alpha))}{w(c'(\alpha))\, w(c'(0))^{e-1}} \Bigl(1 + \varepsilon \bigl(\lambda(e, \mu) - \textstyle\sum_i (e n_i + \gamma_i(\mu, \alpha))\, q_i(0)\bigr)\Bigr)\, U(\bar\rho).$$

Lean: `GlobalTheory.UnitsEval.units_eval` (also `GlobalTheory.T.unitPart_psi_tau_tangent_vector_variation`, a second name).

*Proof.* Let $\kappa_e$ and $\ell_e$ be as in the previous theorem, and put $\lambda(e, \mu) = e\, \ell_e(\mu)$. Write $N_i = e n_i + \gamma_i(\mu, \alpha)$ and $s = \sum_i N_i\, q_i(0)$. There are five steps.

1. A lemma on the torus chart gives $e_1$ such that for $e \ge e_1$ there is $\sigma \in \Gamma_{e,\alpha}$ whose value at $\pi_2 c'(\mu)$ is a unit.
2. A lemma on shifted sections gives $e_2$ such that for $e \ge e_2$ each $N_i \ge 0$, and each $\sigma \in \Gamma_{e,\alpha}$ has $\sigma_1, \sigma_1^u \in \Gamma_{e,\alpha + e\mu}$ with the following properties: $\sigma_1$ satisfies the shift relation with $\sigma$ and constant $0$; $\sigma_1 = u^N \sigma_1^u$ with $u^N = \prod_i u_i^{N_i}$; and $\sigma_1^u(c(0)) = U \cdot \sigma(c(\mu))$ at each point of $\operatorname{Spec} R$.
3. Let $e \ge e_0 = \max(e_1, e_2, 1)$ and let $\sigma$ be as in step 1. Since $h$ is basic, it acts from $\sigma$ to some $\sigma'$. Step 2 for $\sigma$ and for $\sigma'$ gives $\sigma_1, \sigma_1^u$ and $\sigma'_1, \sigma'^u_1$. A lemma on heat operators and monomials uses the defect $0$ and $D(u^N) = (\sum_i N_i q_i)\, u^N$. It shows that $h$ acts from $\sigma_1^u$ to $\sigma''$ with $\sigma'' = \sigma'^u_1 - 2e\, (\sum_i N_i q_i)\, \sigma_1^u$.
4. The previous theorem, at $x = c'(\mu)$ with $(x_0, \dots, x_3) = (c'(\mu), c'(\mu + \alpha), c'(\alpha), c'(0))$, gives
$$\sigma(\pi_1 c'(\mu))\, W = \kappa_e (1 + \varepsilon \ell_e(\alpha))\, S, \qquad S = \sigma(\pi_2 c'(\mu)) + \tfrac{\varepsilon}{2e}\, \sigma'(\pi_2 c'(\mu)),$$
with $W = w(c'(\mu))^{e-1} w(c'(\mu + \alpha))\, w(c'(\alpha))^{-1} w(c'(0))$. At $x = c'(0)$ with $(c'(0), c'(\alpha + e\mu), c'(\alpha + e\mu), c'(0))$ and the pair $\sigma_1^u, \sigma''$, the $w$-factors give $w(c'(0))^e$. By step 2 and condition 3, the values of $\sigma_1^u$ and $\sigma'^u_1$ at $\pi_1 c'(0)$ and $\pi_2 c'(0)$ are $U(\rho)$ or $U(\bar\rho)$ times the values of $\sigma$ and $\sigma'$ at $\pi_1 c'(\mu)$ and $\pi_2 c'(\mu)$. Since $\bar\rho(q_i) = q_i(0)$, this gives
$$U(\rho)\, \sigma(\pi_1 c'(\mu))\, w(c'(0))^e = \kappa_e \bigl(1 + \varepsilon \ell_e(\alpha + e\mu)\bigr)\, U(\bar\rho)\, \bigl(S - \varepsilon s\, \sigma(\pi_2 c'(\mu))\bigr).$$
5. Since $\sigma(\pi_2 c'(\mu))$ is a unit, so is $S$, and $S - \varepsilon s\, \sigma(\pi_2 c'(\mu)) = (1 - \varepsilon s)\, S$. We divide the second identity of step 4 by the first. With $\ell_e(\alpha + e\mu) - \ell_e(\alpha) = e\, \ell_e(\mu)$ we get $U(\rho) = W\, w(c'(0))^{-e}\, (1 + \varepsilon(\lambda(e, \mu) - s))\, U(\bar\rho)$. This is the claim. $\square$

**Theorem 7.22.3 (Periods along a tangent vector).** Let the data be as in the first theorem, with a comparison $(B', \pi_1, \pi_2, c')$ for $\rho$ but without $w$. Then there are a rational $c \neq 0$ and an isomorphism $w : \pi_1^* L \to \pi_2^* L$ such that for all $y, z \in X$ and each unit part $\tau_0$ of $\tau(y, z)$
$$\tau_0(\rho) = \frac{w(c'(y + z))\, w(c'(0))}{w(c'(y))\, w(c'(z))} \Bigl(1 + \varepsilon \textstyle\sum_i c\, q_i(0)\, \gamma_i(y, z)\Bigr)\, \tau_0(\bar\rho).$$

Lean: `GlobalTheory.UnitsAlong.unitTau_along` (also `GlobalTheory.T.unitPart_periods_constant_along_tangent`, a second name).

*Proof.* A lemma on constant deformations uses conditions 1 and 2 of the comparison. It gives an isomorphism $w : \pi_1^* L \to \pi_2^* L$. Let $\lambda$ be as in the previous theorem for this $w$, and take $c = -1$. Let $y, z \in X$ and $\tau_0$ a unit part of $\tau(y, z)$. Choose a unit part $(n, \psi_0)$ of $\psi(y)$. A lemma on unit parts gives a unit part $\tau_1$ of $\tau(y, 0)$ whose value is $1$ at every point. The previous theorem for $(y, z, \tau_0)$ and for $(y, 0, \tau_1)$ gives $e_1$ and $e_2$. Let $e = \max(e_1, e_2)$. Since $\gamma_i(y, 0) = 0$, the two identities read
$$\begin{aligned} (\psi_0^e \tau_0\, \mathrm{rig}^e)(\rho) &= w(c'(y))^{e-1} w(c'(y+z))\, w(c'(z))^{-1} w(c'(0))^{1-e}\, (1 + \varepsilon(\lambda - s - t))\, (\psi_0^e \tau_0\, \mathrm{rig}^e)(\bar\rho), \\ (\psi_0^e\, \mathrm{rig}^e)(\rho) &= w(c'(y))^{e}\, w(c'(0))^{-e}\, (1 + \varepsilon(\lambda - s))\, (\psi_0^e\, \mathrm{rig}^e)(\bar\rho), \end{aligned}$$
with $\lambda = \lambda(e, y)$, $s = \sum_i e n_i\, q_i(0)$ and $t = \sum_i \gamma_i(y, z)\, q_i(0)$. All factors are units of $k[\varepsilon]$, which is commutative. We divide the first identity by the second. This gives the claim with $1 - \varepsilon t = 1 + \varepsilon \sum_i c\, q_i(0)\, \gamma_i(y, z)$. $\square$

So the periods are constant along $\rho$ up to the coboundary of $w \circ c'$ and the factors of the condition in Section 1, with rates $a_i = -q_i(0)$. The term $\lambda(e, y)$ of the abelian part cancels in the quotient.

**Remark 7.22.4 (Formalization).** The proofs are in [HeatOperatorSymbolZeroEqConnection.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeatOperatorSymbolZeroEqConnection.lean#L303), [UnitPartPsiTauTangentVectorVariation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitPartPsiTauTangentVectorVariation.lean#L179) and [UnitPartPeriodsConstantAlongTangent.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitPartPeriodsConstantAlongTangent.lean#L36). The `T.*` names are wrappers, at line 16, line 18 and line 16 of the matching `Statement` files, that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. The first file has a helper `core` (line 125) for step 3, and the case $e \ge 1$ starts at line 335. The four maps $\phi_j$ and the exponents $\epsilon_j$ are `DegPre.famφB` and `DegPre.famε`. A unit part of $\psi(\mu)$ is `LogKSChart.IsUnitPart` and a unit part of $\tau$ is `RigChart.IsUnitTau`. The division of step 5 is the lemma `alg_eval` (line 98) of the second file, and the division in the last proof is `UnitsAlong.alg` (line 24). The inputs are `T.heatOperator_connection_closedFibre`, `T.connection_closedFibre_eq_derivation_identification`, `T.exists_bundleSection_unit_at_closedPoint_torusChart`, `T.exists_shifted_section_div_monomial_over_chart`, `T.heatOperator_shift_div_monomial`, `ConstDefSym.lbIso_pull_of_const`, `UnitPart.exists_isUnitPart` and `T.exists_unitPartPeriodTau_zero_value_one`. They have no entries in this chapter, and we use only their statements. The last theorem states "there is a rational $c \neq 0$", but the proof always takes $c = -1$ (`refine ⟨-1, by norm_num, w, hw, ?_⟩`, line 41 of the third file). The sections $c'(y)$ enter the first theorem only through the lemma of step 1; its conclusion speaks of arbitrary points $x$ and $x_j$. In the second theorem the exponents $N_i$ are natural numbers through `Int.toNat`, and the proof uses that they are nonnegative for $e \ge e_2$.
