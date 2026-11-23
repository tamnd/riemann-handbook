---
title: Heat operators on the Raynaud extension
decls:
  - GlobalTheory.T.exists_torusInvariant_heatOperator_commuting_periods
  - GlobalTheory.heat_commuting_periods_exists
  - GlobalTheory.T.exists_torusInvariant_heatOperator_polynomial_defect
  - GlobalTheory.HeatEx.exists_basic_heat_polyDefect
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Heat operators on the Raynaud extension

This section and the next three build, on the Raynaud extension of degeneration data over a complete local ring, a heat operator that is invariant under the torus and commutes with the shifts by the periods. [The theorem on the symbol of commuting heat operators](/entry/is-ks-of-heat/) of Section 20 then reads the Kodaira-Spencer matrix of a derivation off the symbol of such an operator, and the boundary charts of a later part of this chapter use it. Here we define heat operators, their Fourier terms and their defect, and we prove that a basic heat operator with defect zero exists. The proof has two steps. A first theorem gives a basic heat operator whose defect is a polynomial in the level $k$. A second step uses that the defect is a cocycle and removes it. Sections 18 and 19 give the inputs of the first theorem.

We fix the following data for Sections 17 to 20. Let $R$ be a complete Noetherian local domain that contains $\mathbb{Q}$. Let $Q$ be degeneration data over $R$, complete along the maximal ideal, with abelian part $A$, line bundle $L$, character lattice $X$, points $c(\chi)$ of $A$ and periods $\psi(\chi)$ for $\chi \in X$, as in Section 2. The line bundle $L$ comes with opens $A_\alpha$ that cover $A$, on which $L$ is trivial, and with transition functions $g_{\alpha\beta}$. Let $O$ be a ring with an involution that acts on $X$ and on $Q$. Let $H$ be a *Raynaud extension* of $Q$: a commutative group scheme over $\operatorname{Spec} R$ with a map $q : H \to A$ and an action of $O$, whose points over $T$ correspond to points of $A$ over $T$ together with coordinates $s_\chi$ for $\chi \in X$. We have not unfolded this correspondence. Let $v_1, \dots, v_n$ be a basis over $R$ of the tangent vectors of $H$ at the origin.

**Definition 7.17.1 (Invariant vector field, lift).** A vector field $\partial$ on $H$ is *invariant* for a tangent vector $v$ if, for each ring map $\varphi : R \to A'$, each point $g$ of $H$ over $\operatorname{Spec} \varphi$ and each function $f$ near $g$, the $\varepsilon$-part of $f$ at the translate $g \cdot \varphi(v)$ is $g^* \partial f$. Let $D : R \to R$ be a map and $W$ an open of $H$. A vector field $d$ on $W$ is a *lift* of $D$ if $d$ of the pullback of $r \in R$ is the pullback of $D r$.

Lean: `GlobalTheory.Heat.IsInv` (also `GlobalTheory.Heat.IsLift`, `GlobalTheory.Heat.IsTr`, `GlobalTheory.Heat.Fld`).

We fix invariant vector fields $\partial_1, \dots, \partial_n$ for $v_1, \dots, v_n$. For a vector field $\delta$ on an open of $H$, write $\operatorname{dlg}_\delta(g_{\alpha\beta}) = \delta(q^* g_{\alpha\beta}) \cdot q^* g_{\alpha\beta}^{-1}$, the logarithmic derivative of the pulled back transition function.

**Definition 7.17.2 (Heat operator).** Let $D : R \to R$ be a map. A *heat operator* $h$ for $D$ consists of a symmetric $n \times n$ matrix $\Theta$ over $R$, the *symbol*, a vector $u \in R^n$, opens $W_i$ of $H$ for $i$ in an index set, indices $\alpha(i)$, lifts $d_i$ of $D$ on $W_i$ and functions $p_i, p'_i$ on $W_i$, such that the $W_i$ cover $H$, $W_i \subseteq q^{-1}(A_{\alpha(i)})$, and the following holds. For $k \in \mathbb{N}$ and a function $f$ on an open of $W_i$, put
$$\mathcal{H}_{i,k}(f) = 2k\, d_i f - \sum_{a,b} \Theta_{ab}\, \partial_a \partial_b f + 2 \sum_a u_a\, \partial_a f + (2k^2 p_i + 2k p'_i) f.$$
Then $\mathcal{H}_{i,k}(q^* g^k f) = q^* g^k\, \mathcal{H}_{i',k}(f)$ on each open of $W_i \cap W_{i'}$, with $g = g_{\alpha(i)\alpha(i')}$, for all $k$.

Lean: `GlobalTheory.Heat.Heat` (also `GlobalTheory.Heat.op`, `GlobalTheory.Heat.dlg`).

The gluing condition says that the local operators $\mathcal{H}_{i,k}$ form one operator on the sections of $q^* L^k$. A heat operator *takes* a section $\tau$ of $q^* L^k$ to a section $\tau'$ if $\tau'$ is $\mathcal{H}_{i,k}$ of $\tau$ on each $W_i$, in the trivializations of $L$.

**Definition 7.17.3 (Weight, basic heat operator).** Let $\alpha \in X$ and $f$ a function on an open $V$ of $H$. Then $f$ has *weight $\alpha$* if, for each ring map $R \to A'$, two points $x, x'$ of $H$ over $A'$ in $V$ with $q(x) = q(x')$, and units $c(\chi)$ with $s_\chi(x') = c(\chi)\, s_\chi(x)$ for all $\chi$, we have $f(x') = c(\alpha) f(x)$. A heat operator $h$ is *basic* if each $W_i$ is the preimage of an open of $A$, the functions $p_i$ and $p'_i$ have weight $0$, and each $d_i$ takes functions of weight $\alpha$ on preimages of opens of $A$ in $W_i$ to functions of weight $\alpha$.

Lean: `GlobalTheory.Heat.IsBasic` (also `GlobalTheory.Heat.IsWt`).

So a basic heat operator commutes with the action of the torus. Its terms of weight $\alpha$ come from sections on $A$, as follows. For $k \ge 1$ and $\alpha \in X$, let $\Gamma_{k,\alpha}$ be the module of sections over $A$ of the line bundle $L^{k-1} \otimes T_{c(\alpha)}^* L \otimes L(c(\alpha))^{-1} \otimes L(0)$, where $T_{c(\alpha)}$ is the translation by $c(\alpha)$ and $L(a)$ is the fibre of $L$ at $a$. A section $\tau$ of $q^* L^k$ is the *Fourier term* of $\sigma \in \Gamma_{k,\alpha}$ if $\tau = q^* \sigma \cdot s_\alpha$. Let $K = \operatorname{Frac} R$.

**Definition 7.17.4 (Shift relation, defect).** Let $k \ge 1$, $\mu, \alpha \in X$, $\sigma \in \Gamma_{k,\alpha}$, $\sigma_1, \sigma_2 \in \Gamma_{k,\alpha + k\mu}$ and $c \in R$. The *shift relation* with constant $c$ says that over $A_K$
$$\sigma_1 = u \cdot T_{c(\mu)}^* \sigma + c\, \sigma_2$$
for each generator $u$ of the line bundle that compares the two sides, normalized so that its value at the origin is $\psi(\mu)^k \tau(\mu, \alpha)$ times the $k$-th power of the rigidification. A basic heat operator $h$ *acts* from $\sigma$ to $\sigma'$ in $\Gamma_{k,\alpha}$ if it takes a Fourier term of $\sigma$ to a Fourier term of $\sigma'$. Let $c : \mathbb{N} \times X \times X \to R$. Then $h$ has *defect* $c$ if the following holds for $k \ge 1$, $\mu, \alpha \in X$, $\sigma, \sigma' \in \Gamma_{k,\alpha}$ and $\sigma_1, \sigma'_1 \in \Gamma_{k,\alpha+k\mu}$. If $\sigma_1$ satisfies the shift relation with $\sigma$ and constant $0$, and $h$ acts from $\sigma$ to $\sigma'$ and from $\sigma_1$ to $\sigma'_1$, then $\sigma'_1$ satisfies the shift relation with $\sigma'$, constant $c(k, \mu, \alpha)$ and $\sigma_2 = \sigma_1$.

Lean: `GlobalTheory.Heat.HasDefect` (also `GlobalTheory.Heat.ShiftEq`, `GlobalTheory.Heat.TActs`, `GlobalTheory.Heat.IsTerm`, `GlobalTheory.Heat.Heat.Acts`).

The shift relation with constant $0$ is the relation between the Fourier coefficients of a theta function in [Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction). A heat operator with defect $0$ preserves this relation, so it commutes with the shifts by the periods. We have not unfolded the comparison bundle or the normalization of $u$.

**Definition 7.17.5 (Monomial degeneration data).** Let $t_1, \dots, t_m \in R$ and $\gamma_1, \dots, \gamma_m$ forms on $X$. The data $Q$ are *monomial* in $t$ with exponents $\gamma$ if for each $y \in X$ there are a unit $w$ of $R$ and $n \in \mathbb{N}^m$ with $\gamma_i(y, y) = 2 n_i$ for each $i$, such that the period $\psi(y)$ is $w \prod_i t_i^{n_i}$ in the coordinates of $Q$.

Lean: `GlobalTheory.Toroidal.IsMonomial`.

**Theorem 7.17.6 (Heat operator with polynomial defect).** Let $R$, $Q$, $O$, $H$, $v$ and $\partial$ be as above. Suppose that $Q$ is monomial in nonzero $t_1, \dots, t_m$ with exponents $\gamma$, and let $D$ be a derivation of $R$ with $D(t_i) \in (t_i)$ for each $i$. Then there are a basic heat operator $h$ for $D$, a map $w : X \times X \to R$ that is additive in the second variable, and maps $\pi, \pi' : X \to R$ such that $h$ has defect
$$c(k, \mu, \alpha) = 2k\, w(\mu, \alpha) + 2k^2 \pi(\mu) + 2k\, \pi'(\mu).$$

Lean: `GlobalTheory.HeatEx.exists_basic_heat_polyDefect` (also `GlobalTheory.T.exists_torusInvariant_heatOperator_polynomial_defect`, a second name).

*Proof.* There are three steps.

1. [The theorem on connection matrices](/entry/exists-inv-lift-symm-ks/) of Section 19 gives a symmetric matrix $\Theta$, opens $V_i$ that cover $A$ with $V_i \subseteq A_{\alpha(i)}$, and lifts $d_i$ of $D$ on $q^{-1}(V_i)$ that preserve weights, with $d_i - d_{i'} = \sum_{a,b} \Theta_{ab}\, \operatorname{dlg}_{\partial_b}(g_{\alpha(i)\alpha(i')})\, \partial_a$ on overlaps.
2. A lemma on heat operators from a symmetric relation takes the data of step 1 and the statement of [the theorem on weight-zero cocycles](/entry/exists-weight-zero-cocycle-eq-log-derivative-comb-add-coboundary/) of Section 19 for the cover $q^{-1}(V_i)$. It gives a basic heat operator $h$ for $D$.
3. [The theorem on the polynomial defect](/entry/defect-polynomial/) of Section 18 applies to $h$, with the monomial data and the condition on $D$. It gives $w$, $\pi$ and $\pi'$. $\square$

Only step 3 uses the monomial data and the condition $D(t_i) \in (t_i)$.

**Theorem 7.17.7 (Heat operator commuting with the periods).** Let the data be as in the previous theorem. Then there is a basic heat operator for $D$ with defect $0$.

Lean: `GlobalTheory.heat_commuting_periods_exists` (also `GlobalTheory.T.exists_torusInvariant_heatOperator_commuting_periods`, a second name).

*Proof.* There are four steps.

1. The previous theorem gives a basic heat operator $h$ for $D$ with defect $c(k, \mu, \alpha) = 2k\, w(\mu, \alpha) + 2k^2 \pi(\mu) + 2k\, \pi'(\mu)$.
2. A lemma on period defects shows that the defect of a basic heat operator is a cocycle: $c(k, \mu + \mu', \alpha) = c(k, \mu, \alpha) + c(k, \mu', \alpha + k\mu)$ for $k \ge 1$.
3. Since $R$ contains $\mathbb{Q}$, it has characteristic $0$. A lemma on polynomial cocycles compares the coefficients of $k$ and $k^2$ in the identity of step 2, with $w(\mu', \alpha + k\mu) = w(\mu', \alpha) + k\, w(\mu', \mu)$. It gives that $w$ is additive in the first variable and symmetric, that $\pi'$ is additive, and that $\pi(\mu + \mu') = \pi(\mu) + \pi(\mu') + w(\mu', \mu)$.
4. A lemma on period defects takes $h$, $w$, $\pi$, $\pi'$ and the identities of step 3. It gives a basic heat operator $h'$ for $D$ with defect $0$. $\square$

The theorem does not say that the symbol of $h'$ is the matrix $\Theta$ of step 1 of the previous proof. Section 20 links the symbol to the Kodaira-Spencer matrix of $D$ by a separate argument.

**Remark 7.17.8 (Formalization).** The proofs are in [ExistsTorusInvariantHeatOperatorPolynomialDefect.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTorusInvariantHeatOperatorPolynomialDefect.lean#L25) and [ExistsTorusInvariantHeatOperatorCommutingPeriods.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTorusInvariantHeatOperatorCommutingPeriods.lean#L19). The `T.*` names are wrappers, at line 16 of the matching `Statement` files, that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. The definitions are in [HasDefect.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasDefect.lean#L58): `IsInv` at line 34, `IsLift` at 39, `dlg` at 44, `op` at 53, `Heat` at 58, `Heat.Acts` at 88, `IsTerm` at 115, `IsWt` at 119, `IsBasic` at 128, `TActs` at 133, `ShiftEq` at 138 and `HasDefect` at 147. The Raynaud extension is `GlobalTheory.RayEv.Ray` in [IsLinearHomPull.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsLinearHomPull.lean#L25); its `Nonempty` instance (line 40) is built from the theorem `GlobalTheory.allSixLaws`. `IsMonomial` is in [IsProperToroidalModelStructureMap.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsProperToroidalModelStructureMap.lean#L191). In `Heat` the map $D$ is any function $R \to R$; the theorems apply it to a derivation. In `HasDefect` the hypothesis on $\sigma_1$ is `ShiftEq Q k mu α σ σ₁ 0 σ₁`, so $\sigma_2 = \sigma_1$ is a dummy term with coefficient $0$. The lemma of step 2 of the first proof, `T.exists_torus_invariant_heat_operator_of_symmetric_relation`, receives the weight-zero cocycle theorem as a hypothesis, and its conclusion is only that a basic heat operator exists: it does not say that the symbol of $h$ is $\Theta$, and $\Theta$ is not in the conclusion of either theorem. The characteristic $0$ of step 3 is `charZero_of_injective_algebraMap` (line 23). The proofs apply `T.exists_torus_invariant_heat_operator_of_symmetric_relation`, `T.heatOperator_period_defect_isCocycle`, `T.cocycle_polynomialDefect_bilinear_additive_parts` and `T.exists_heatOperator_period_defect_zero`. They have no entries in this chapter, and we use only their statements. The module Gamma_{k,\alpha} `DegPre.SecB`, with the maps `famφB` and exponents `famε`. We have not unfolded `GtPt`, `deltaφ`, `famMult` or `PsiCoord`.
