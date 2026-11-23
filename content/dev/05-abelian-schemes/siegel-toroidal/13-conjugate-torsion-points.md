---
title: Conjugate torsion points
decls:
  - GlobalTheory.T.conjugate_torsion_point_polarised_fibre_image
  - GlobalTheory.Poinc.Sep.conj_fibre_iso
  - GlobalTheory.T.polarisedAbelianPart_fibre_conjugate_iso_mumford
  - GlobalTheory.Poinc.Sep.conj_fibre_core
  - GlobalTheory.T.e8Power_fibre_conjugate_evaluation_iso
  - GlobalTheory.T.theta_series_sharp_reference_sixteen_terms
  - GlobalTheory.Poinc.Sep.sharp_fibre_iso_exists
  - GlobalTheory.T.fibre_eighth_power_theta_object_subfield
  - GlobalTheory.Poinc.Sep.sharp_fibre_theta_object
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Conjugate torsion points

The theorem on [torsion points of the abelian part](/entry/torsion-theta-points-def-over/) needs one input: if the theta terms of a sharp refinement are defined over an algebraically closed subfield $k_0$ of $K$ up to units, then each automorphism $\sigma$ of $K$ over $k_0$ moves the periods $c_Q(a)$ of the abelian part to their images under an isomorphism of fibres. This section proves that input. The idea is classical: an abelian variety with a theta structure of high level is determined by its theta constants, so if the theta constants lie in $k_0$, the abelian variety descends to $k_0$, and $\sigma$ acts on its torsion points through the descended model. We prove five theorems, each one a step closer to the form that the separation argument uses.

We keep the notation of the section on [uniformized members](/entry/exists-u-mem/). For a ring map $\mathrm{ev} : R \to K$ and a scheme $B$ over $R$ we write $B_{\mathrm{ev}}$ for the pullback of $B$ along $\operatorname{Spec} K \to \operatorname{Spec} R$, and $\mathrm{pr} : B_{\mathrm{ev}} \to B$ for the projection. For $\sigma \in \operatorname{Aut}(K)$ we write $\sigma\mathrm{ev} = \sigma \circ \mathrm{ev}$. A point $q : \operatorname{Spec} K \to B_{\mathrm{ev}}$ is a *section* if its composite with $B_{\mathrm{ev}} \to \operatorname{Spec} K$ is the identity. A map $f : B_{\mathrm{ev}} \to B'$ over $\operatorname{Spec} K$ is an *isomorphism of group schemes* over $K$ if $B_{\mathrm{ev}}$ is the group pullback of $B'$ along the identity of $\operatorname{Spec} K$ by $f$.

**Definition 9.13.1 (Data at level $j$).** Let $l$ be an odd prime, $W$ an $8 \times 8$ integer matrix with $W + W^{T}$ positive definite of determinant $1$, and $j \ge 0$. *Data at level $j$* for $(l, W)$ consist of:

1. a domain $V$, a local CN domain $V_1$ in which $l$ is a unit, Mumford data $Q$ over $V$ with abelian part $B_Q$ of relative dimension $g_Q$, and an injective ring map $\rho : V \to V_1$;
2. a sharp refinement $(D, e)$ of $Q$ along $\rho$ for $W$, with $e : Y_Q^8 \cong Y_D$, abelian scheme $A_D$ and line bundle $L_D$;
3. a set $C$ and elements $u(\mu, c)$, $\mathrm{mo}(\mu)$ of $V_1$ for $\mu \in Y_Q^8$ and $c \in C$, with $\mathrm{mo}(\mu) \ne 0$ and some $u(\mu, c)$ a unit for each $\mu$, such that the products $u(\mu, c)\,\mathrm{mo}(\mu)$ are theta terms of $D$ of level $(l^j)^2$;
4. a map $\mathrm{ev} : V_1 \to K$ to an algebraically closed field and an algebraically closed subfield $k_0 \subseteq K$ such that, for all $\mu$, $c$, $c'$ with $u(\mu, c')$ a unit, $\mathrm{ev}(u(\mu, c)) = r\,\mathrm{ev}(u(\mu, c'))$ for some $r \in k_0$.

These are exactly the hypotheses of the theorem on [torsion points of the abelian part](/entry/torsion-theta-points-def-over/). Condition 4 says that the ratios of the theta terms that share an index $\mu$ are defined over $k_0$ at $\mathrm{ev}$. It is the form in which "the theta constants lie in $k_0$" enters.

We also use *theta objects* $t$ of dimension $h$ and level $N$: an abelian scheme $t_A$ with a line bundle $t_L$ over a base, built on a *theta base* $b_T$, with labelled points $t_{\mathrm{lab}}(a)$, a *shape* given by a family of integer $2h \times 2h$ matrices and an integer $\kappa$, a *primitivity* condition at two indices $w, w'$, and *theta values* $v(a)$ indexed by a finite set $\mathrm{Ix}$. We use these objects only through the statements below.

**Theorem 9.13.2 (Theta object over $k_0$).** Let $W$ be as above and $g_Q \ge 0$. There are a finite set $J$, integer $2(8g_Q) \times 2(8g_Q)$ matrices $\mathrm{Mat}_x$ for $x \in J$, an integer $\kappa$ and $w, w' \in J$ with the following property. For each odd prime $l$, each $j \ge 1$ and data at level $j$ for $(l, W)$ with $\dim B_Q = g_Q$, there are a theta base $b_T$ over $k_0$ of level $(l^j)^2$, a theta object $t$ of dimension $8g_Q$ and level $(l^j)^2$ on $b_T$ over $\operatorname{Spec} K \to \operatorname{Spec} k_0$, values $v : \mathrm{Ix} \to k_0$ and $\psi : (A_D)_{\mathrm{ev}} \to t_A$ such that:

1. $t$ has shape $(\mathrm{Mat}, \kappa)$, is primitive at $(w, w')$, and has theta values $v$;
2. $\psi$ is an isomorphism of group schemes over $K$, and $\mathrm{pr}^* L_D \cong \psi^* t_L$;
3. for each $K$-point $y$ of $A_D$ over $\mathrm{ev}$ with $y^{(l^j)^2} = 1$ and each section $q$ of $(A_D)_{\mathrm{ev}}$ with $\mathrm{pr} \circ q = y$, there is a label $a$ with $\psi \circ q = t_{\mathrm{lab}}(a)$.

Lean: `GlobalTheory.Poinc.Sep.sharp_fibre_theta_object` (also `GlobalTheory.T.fibre_eighth_power_theta_object_subfield`, a wrapper).

*Proof.* A theorem on sharp refinements at odd primes gives $J$, $\mathrm{Mat}$, $\kappa$, $w$, $w'$, and then, for the data at level $j$, the theta base $b_T$, the theta object $t$ and $\psi$ with the shape, the primitivity, clause 2 and clause 3. A theorem on the coefficient family of a sharp refinement takes these and the theta terms with condition 4, and gives values $v$ in $k_0$ that are theta values of $t$. We use only the statements of these two theorems. $\square$

**Theorem 9.13.3 (Fibre isomorphism to the conjugate).** Let $g \ge 0$, $l$ an odd prime and $W$ as above. There is $j_0$ such that for each $j \ge j_0$, all data at level $j$ with $\dim B_Q \le g$, and each $\sigma \in \operatorname{Aut}(K)$ that fixes $k_0$ pointwise, there is a map $f : (A_D)_{\mathrm{ev}} \to (A_D)_{\sigma\mathrm{ev}}$ such that:

1. $f$ is an isomorphism of group schemes over $K$;
2. $\mathrm{pr}^* L_D \cong (\mathrm{pr} \circ f)^* L_D$;
3. for each $K$-point $y$ of $A_D$ over $\mathrm{ev}$ with $y^{l^k} = 1$ for some $k$, and each section $q$ of $(A_D)_{\mathrm{ev}}$ with $\mathrm{pr} \circ q = y$, we have $\mathrm{pr} \circ f \circ q = y \circ \operatorname{Spec}\sigma$.

Lean: `GlobalTheory.Poinc.Sep.sharp_fibre_iso_exists` (also `GlobalTheory.T.theta_series_sharp_reference_sixteen_terms`, a wrapper).

*Proof.* For each $g_Q$, the theorem on the theta object over $k_0$ gives $J$, $\mathrm{Mat}$, $\kappa$, $w$, $w'$, and a theorem on descent to the field of theta constants gives a level $j_0(g_Q)$ from which on a theta object with these invariants whose theta values lie in $k_0$ descends to $k_0$. Put $j_0 = 1 + \max_{g_Q \le g} j_0(g_Q)$. Let $j \ge j_0$; then $j \ge 1$ and $j \ge j_0(g_Q)$ for $g_Q = \dim B_Q$. The previous theorem gives $t$, $v$ and $\psi$. Descent gives a theta object $t_0$ over $k_0$ and an isomorphism $\varphi$ from $t_A$ to the base change of $t_{0,A}$ to $K$ that respects the bundles. Since $\sigma$ fixes $k_0$, the base change of $t_0$ along $\sigma$ is again $t_A$ up to $\varphi$, and a lemma on twisting fibres gives $f$ with clauses 1 and 2, such that $f$ sends a section $q$ to its conjugate whenever $\mathrm{pr} \circ q$ comes from a $k_0$-point of $t_0$. For clause 3, let $y$ be an $l^k$-torsion point. A lemma on transfer of torsion points to a fixed model gives an $l^k$-torsion point $y'$ of $t_{0,A}$ over $K$ that matches $y$. As $l$ is a unit in $V_1$, $l^k$ is a unit in $k_0$. Since $k_0$ is algebraically closed, the $l^k$-torsion of the abelian scheme $t_{0,A}$ over $k_0$ is rational over $k_0$, by a lemma on prime-to-characteristic torsion. So $y'$ comes from a $k_0$-point, and $f$ sends $q$ to its conjugate. We use only the statements of the lemmas on descent, twisting, transfer and torsion. $\square$

**Theorem 9.13.4 (Sharp points go to conjugates).** In the setting of the previous theorem, there is $j_0$ such that for $j \ge j_0$ the map $f$ can be chosen with clauses 1 to 3 and also:

4. for each $\mu \in Y_Q^8$ and each section $q$ of $(A_D)_{\mathrm{ev}}$ with $\mathrm{pr} \circ q = c_D(e\mu) \circ \operatorname{Spec}\mathrm{ev}$, we have $\mathrm{pr} \circ f \circ q = \mathrm{pr} \circ q \circ \operatorname{Spec}\sigma$.

Lean: `GlobalTheory.T.e8Power_fibre_conjugate_evaluation_iso` (also `GlobalTheory.Poinc.Sep.sharp_fibre_conj_iso`, the same statement).

*Proof.* Let $j_B$ be the level of the previous theorem and $j_D$ the level of a theorem on sharp points: for $j \ge j_D$, a map $f$ with clauses 1 and 2 that sends the $l^{2j}$-torsion points to their conjugates also satisfies clause 4. Put $j_0 = \max(j_B, j_D)$. The previous theorem gives $f$; its clause 3 with $k = 2j$ gives the hypothesis of the theorem on sharp points, since $l^{2j} = (l^j)^2$. We use only the statement of the theorem on sharp points. $\square$

The periods $c_D(e\mu)$ are not torsion points; clause 4 is the reason for the theta terms of level $(l^j)^2$. We now pass from $A_D$, the eighth power, to its factor $B_Q$. Write $\Lambda(M_Q)$ for the Mumford bundle of $M_Q$ on $B_Q \times B_Q$. For a map $f$ we write $f \times f$ for its square.

**Theorem 9.13.5 (Conjugate isomorphism of the abelian part).** Let $g \ge 0$, $l$ an odd prime and $W$ as above. There is $j_0$ such that the following holds for each $j \ge j_0$, all data at level $j$ with $\dim B_Q \le g$, and each $\sigma \in \operatorname{Aut}(K)$ that fixes $k_0$. Write $p_V = \operatorname{Spec}(\mathrm{ev} \circ \rho)$. Let $a \in Y_Q$ and let $p$ be a section of $(B_Q)_{\mathrm{ev}\rho}$ with $\mathrm{pr} \circ p = c_Q(a) \circ p_V$. Then there are $f : (B_Q)_{\mathrm{ev}\rho} \to (B_Q)_{\sigma\mathrm{ev}\rho}$ and $f_2 = f \times f$ such that:

1. $f$ is an isomorphism of group schemes over $K$;
2. for all maps $\psi_0 = \mathrm{pr} \times \mathrm{pr}$ from $(B_Q)_{\mathrm{ev}\rho}^2$ and $\psi_\sigma = \mathrm{pr} \times \mathrm{pr}$ from $(B_Q)_{\sigma\mathrm{ev}\rho}^2$ to $B_Q^2$, we have $\psi_0^* \Lambda(M_Q) \cong (\psi_\sigma \circ f_2)^* \Lambda(M_Q)$;
3. $\mathrm{pr} \circ f \circ p = \mathrm{pr} \circ p \circ \operatorname{Spec}\sigma$.

Lean: `GlobalTheory.Poinc.Sep.conj_fibre_core` (also `GlobalTheory.T.polarisedAbelianPart_fibre_conjugate_iso_mumford`, a wrapper).

*Proof.* Let $j_0'$ be the level of the previous theorem and put $j_0 = \max(j_0', 1)$. For $j \ge j_0$ the previous theorem gives an isomorphism $f_D$ of the fibres of $A_D$ with clauses 1 to 4. The sharp refinement writes $A_D$ as a product of eight copies of $\rho^* B_Q$, and the periods $c_D(e\mu)$ as products of the periods $c_Q(\mu_a)$. A theorem on factor isomorphisms from sharp torsion (which needs $j \ge 1$) then cuts $f_D$ down to an isomorphism $f$ of the fibres of $B_Q$ that carries $\Lambda(M_Q)$ to itself and sends $p$ to its conjugate. We use only its statement. $\square$

Finally we transport this to a Siegel family. Let $F'$ be a Siegel family of genus $g'$ and level $n'$ over $(o', \zeta')$, with base $s' : X' \to \operatorname{Spec} o'$ and universal datum $(A', P', \ell')$.

**Theorem 9.13.6 (Conjugate torsion points).** Let $g \ge 0$, $l$ an odd prime and $W$ as above. There is $j_0$ such that the following holds for each $j \ge j_0$ and all data at level $j$ with $\dim B_Q \le g$. Let $F'$ be as above with $n' \ge 1$, let $\lambda : \operatorname{Spec} V \to X'$, and let $\beta : B_Q \to A'$ make $B_Q$ the group pullback of $A'$ along $\lambda$, with $\Lambda(M_Q) \cong (\beta \times \beta)^* P'$. Assume that $s' \circ \lambda \circ p_V$ is defined over $k_0$. Let $\varphi_{02} = (\beta \circ \mathrm{pr}) \times (\beta \circ \mathrm{pr})$ on $(B_Q)_{\mathrm{ev}\rho}^2$. Let $\sigma \in \operatorname{Aut}(K)$ fix $k_0$, let $a \in Y_Q$ and let $p$ be a section of $(B_Q)_{\mathrm{ev}\rho}$ with $\mathrm{pr} \circ p = c_Q(a) \circ p_V$. Then there are $x' : \operatorname{Spec} K \to X'$ and $\varphi : (B_Q)_{\mathrm{ev}\rho} \to A'$ such that:

1. $s' \circ x' = s' \circ \lambda \circ p_V$;
2. $\varphi$ makes $(B_Q)_{\mathrm{ev}\rho}$ the group pullback of $A'$ along $x'$;
3. $\varphi_{02}^* P' \cong (\varphi \times \varphi)^* P'$;
4. $\beta \circ \mathrm{pr} \circ p \circ \operatorname{Spec}\sigma = \varphi \circ p$.

Lean: `GlobalTheory.Poinc.Sep.conj_fibre_iso` (also `GlobalTheory.T.conjugate_torsion_point_polarised_fibre_image`, a wrapper).

*Proof.* Take $j_0$ from the previous theorem, and let $f$ be the isomorphism that it gives. Put $x' = \lambda \circ \operatorname{Spec}(\sigma \circ \mathrm{ev} \circ \rho)$ and $\varphi = \beta \circ \mathrm{pr}_\sigma \circ f$, where $\mathrm{pr}_\sigma : (B_Q)_{\sigma\mathrm{ev}\rho} \to B_Q$. Clause 1: since $s' \circ \lambda \circ p_V$ factors through $\operatorname{Spec} k_0$ and $\sigma$ fixes $k_0$, composing with $\operatorname{Spec}\sigma$ does not change it. Clause 2: by base change, $(B_Q)_{\sigma\mathrm{ev}\rho}$ is the group pullback of $A'$ along $x'$ by $\beta \circ \mathrm{pr}_\sigma$, and composing with the isomorphism $f$ of group schemes keeps this property; a lemma on base change of group pullbacks with squares gives this, used three times. Clause 3 is the chain
$$\begin{aligned} \varphi_{02}^* P' &\cong \psi_0^* (\beta \times \beta)^* P' \cong \psi_0^* \Lambda(M_Q) \\ &\cong (\psi_\sigma \circ f_2)^* \Lambda(M_Q) \cong (\varphi \times \varphi)^* P', \end{aligned}$$
with clause 2 of the previous theorem in the middle. Clause 4 is clause 3 of the previous theorem followed by $\beta$. $\square$

In the theorem on [torsion points of the abelian part](/entry/torsion-theta-points-def-over/), $x'$ and $\varphi$ are identifications of the fibre of $F'$ over a point defined over $k_0$. There are only finitely many of these, so the orbit of $\beta \circ c_Q(a) \circ p_V$ under $\operatorname{Aut}(K/k_0)$ is finite.

**Remark 9.13.7 (Formalization).** The predicates for theta bases and theta objects, with their shape, primitivity, theta values and labels, are not unfolded here; we use only the statements in which they appear. In the proof of the theorem on the theta object, $t$ and $\psi$ come from a theorem that does not take the theta terms or condition 4; only the values $v$ use them ([FibreEighthPowerThetaObjectSubfield.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FibreEighthPowerThetaObjectSubfield.lean#L39)). The name `theta_series_sharp_reference_sixteen_terms` mentions sixteen terms, but its statement has nothing about sixteen terms ([ThetaSeriesSharpReferenceSixteenTermsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaSeriesSharpReferenceSixteenTermsStatement.lean#L13)). The wrapper `e8Power_fibre_conjugate_evaluation_iso` first tries `sharp_fibre_conj_iso`, and its fallback branch repeats that proof ([E8PowerFibreConjugateEvaluationIsoStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/E8PowerFibreConjugateEvaluationIsoStatement.lean#L14)). In `conj_fibre_core` the level is replaced by $\max(j_0, 1)$ ([PolarisedAbelianPartFibreConjugateIsoMumford.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PolarisedAbelianPartFibreConjugateIsoMumford.lean#L18)). In `conj_fibre_iso` the hypothesis $1 \le n'$ is not used ([ConjugateTorsionPointPolarisedFibreImage.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ConjugateTorsionPointPolarisedFibreImage.lean#L38)). The wrappers use `first | exact @X | ...` under `maxHeartbeats 1000000`.
