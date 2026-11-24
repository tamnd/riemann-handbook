---
title: Key values along deformations
decls:
  - GlobalTheory.T.transfer_of_rule4'
  - GlobalTheory.MBLow.KeyTop.transfer_of_rule4
  - GlobalTheory.T.thetaKeyValue_two_fibres_local_ring
  - GlobalTheory.MBLow.keyValue_twoFibres
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Key values along deformations

The statement that [every character of the literature has the required property](/step/every-character-of-literature/) uses a rule that assigns a number to a polarized abelian variety with extra data, the *key value*. This section proves that a rule with four basic properties is determined by analytic data: if the theta constants and first jets of a key datum over a complete nonarchimedean field are the values of convergent power series, and the same power series at a small complex argument give a complex key datum with key value $k$, then the key value of the first datum is $k$ as well. The proof joins the two data by a family over a local domain and compares the key values on the two fibres.

### Key data and rules

Let $R$ be a commutative ring. A *key datum* $x$ over $R$ consists of:

1. a polarized abelian scheme $P$ over $R$ of dimension $g \geq 1$, with its line bundle $L$;
2. a generator $\rho$ of the fibre of $L$ at the origin, the *rigidification*;
3. a section $\theta$ of $L$ that is nonzero on all fibres;
4. a basis $v_1, \dots, v_g$ of the Lie algebra of $P$.

A *rule* $\kappa$ assigns to every key datum $x$ over a field $K$ of characteristic zero a unit $\kappa(x) \in K^\times$. We use four properties of a rule.

1. *Homogeneity*: if $x'$ differs from $x$ only by $\theta' = a\theta$ and $v' = M v$, with $a \in K^\times$ and $M \in \mathrm{GL}_g(K)$, then $a^8 \kappa(x') = \det(M)^4 \kappa(x)$.
2. *Functoriality*: $\kappa$ commutes with pullback along field homomorphisms.
3. *Normalization*: over $\mathbb{C}$, if $P = \mathbb{C}^g / (\mathbb{Z}^g + \tau \mathbb{Z}^g)$, $\theta$ is a theta function with half integral characteristics, and $v_i = (2\pi i)^{-1}\partial_i$, then $\kappa(x) = 1$.
4. *Family units*: for every noetherian integrally closed domain $S$ of characteristic zero and every key datum $y$ over $S$, there is a unit $u \in S^\times$ such that $\kappa(x) = f(u)$ for every field $K$, every $f \colon S \to K$ and every pullback $x$ of $y$ along $f$.

A rule with these four properties satisfies *Rule 4*.

Let $m$ be odd and $(p_a)_{a}$ a family of points of order dividing $m^2$. The *theta constants and first jets* of $x$ at level $m$ are the numbers $\vartheta_a$ and $J_{a j}$ defined as follows. The translate of $\theta^{m^2}$ by a symmetric lift of $p_a$ to the theta group of $L^{m^2}$ is a section $t_a$ of $L^{m^2}$, and in a trivialization near the origin,
$$\begin{aligned} t_a(\varepsilon v_j) &= \rho^{m^2}\bigl(\vartheta_a + \varepsilon\, (J_{a j} + c_j \vartheta_a)\bigr), \qquad \varepsilon^2 = 0, \end{aligned}$$
for some constants $c_j$. The constants $c_j$ express that the first jets are only defined up to adding a multiple of the theta constants.

### Comparison on two fibres

**Theorem 7.38.1 (Key values on two fibres).** Let $\kappa$ satisfy Rule 4. Let $W$ be a noetherian integrally closed local domain of characteristic zero, $K_0$ a field and $K_1$ an algebraically closed field, both of characteristic zero, $i_0 \colon W \to K_0$ injective, and $i_1 \colon W \to K_1$ such that every $a$ with $i_1(a) \neq 0$ is a unit. Let $P$ be a polarized abelian scheme of dimension $g$ over $W$, $m \geq 3$ odd, and $(q_a)$ points of $P$ with $q_a^{m^2} = 1$. Let $x_0$ over $K_0$ and $x_1$ over $K_1$ be key data whose abelian varieties and line bundles are the pullbacks of $P$ along $i_0$ and $i_1$, and $p_{0,a}$ and $p_{1,a}$ the images of $q_a$, such that the $p_{1,a}$ are all the points of order dividing $m^2$. Let $\vartheta_a$, $J_{a j}$ and $k$ be elements of $W$ such that $i_0(\vartheta_a), i_0(J_{a j})$ are the theta constants and first jets of $x_0$, and $i_1(\vartheta_a), i_1(J_{a j})$ those of $x_1$. If $\kappa(x_0) = i_0(k)$, then $\kappa(x_1) = i_1(k)$.

Lean: `GlobalTheory.T.thetaKeyValue_two_fibres_local_ring` (also `GlobalTheory.MBLow.keyValue_twoFibres`).

*Proof.* We follow the Lean proof.

1. The polarized abelian scheme $P$ carries a key datum $y$ over $W$, and $y$ has theta constants $\vartheta'_a$ and first jets $J'_{a j}$ in $W$ at the points $q_a$. Here $m$ is a unit in $W$, since $i_1(m) \neq 0$.
2. The pullbacks of $y$ along $i_0$ and $i_1$ are key data $y_0$ and $y_1$ with the same abelian varieties and line bundles as $x_0$ and $x_1$, and their theta constants and first jets are the images of $\vartheta'$ and $J'$.
3. Two nonzero sections of the same line bundle differ by a scalar, and two bases of the Lie algebra by a matrix. So $\theta(x_r) = a_r\, \theta(y_r)$ and $v(x_r) = M_r\, v(y_r)$ for $r = 0, 1$, with $a_r \neq 0$ and $M_r$ invertible.
4. The change of section and basis changes the jets as follows: for $r = 0, 1$ there are $c_r$ with
$$\begin{aligned} i_r(\vartheta_a) &= a_r\, i_r(\vartheta'_a), & i_r(J_{a j}) &= a_r \sum_l (M_r)_{j l}\, i_r(J'_{a l}) + c_{r, j}\, i_r(\vartheta'_a). \end{aligned}$$
5. Since $m \geq 3$ and the points $p_{1,a}$ are all the points of order dividing $m^2$, the theta constants and first jets of $y_1$ are linearly independent over $K_1$: if $c_0 \vartheta'_a + \sum_j c_j J'_{a j}$ vanishes in $K_1$ for all $a$, then all $c$ vanish.
6. By the family unit property there is $u \in W^\times$ with $\kappa(y_0) = i_0(u)$ and $\kappa(y_1) = i_1(u)$. By homogeneity,
$$\begin{aligned} a_0^8\, \kappa(x_0) &= \det(M_0)^4\, i_0(u), & a_1^8\, \kappa(x_1) &= \det(M_1)^4\, i_1(u). \end{aligned}$$
7. The scalars and matrices lift to $W$: there are $a \in W$ and $M \in \mathrm{Mat}_g(W)$ with $i_r(a) = a_r$ and $i_r(M) = M_r$ for $r = 0, 1$. To see this, write $\vartheta$ and $J$ in terms of the family $(\vartheta', J')$. By step 5 the coordinates are unique over $K_1$, and by step 4 they exist over $K_0$; a lemma on coordinates with linearly independent reduction then shows that they are integral, that is, in $W$, and that they map to the coordinates over $K_1$. The coordinate of $\vartheta$ along $\vartheta'$ is $a$. The coordinates of $J_{\cdot j}$ along $J'_{\cdot l}$ are $a M_{j l}$, and since $i_1(a) = a_1 \neq 0$, $a$ is a unit and $M$ is obtained by dividing by $a$.
8. In $W$ we have $a^8 k = \det(M)^4 u$, since the images under the injective map $i_0$ agree by step 6 and $\kappa(x_0) = i_0(k)$. Applying $i_1$ and comparing with step 6 gives $a_1^8\, i_1(k) = a_1^8\, \kappa(x_1)$, and $a_1 \neq 0$.

So $\kappa(x_1) = i_1(k)$. $\square$

Functoriality and normalization are not used in this proof; only homogeneity and family units are.

### Transfer along deformations

Let $C$ be a complete, algebraically closed, nonarchimedean valued field of characteristic zero, and $e \colon C \to \mathbb{C}$ a field homomorphism; it need not be continuous. Let $x$ be a key datum over $C$ of dimension $g$, $m$ odd, $\zeta \in C^\times$, and a level structure of $x$ of level $m^2$ for $\zeta$, with the points $p_a$ indexed by $a \in (\mathbb{Z}/m^2)^{2g}$. A *deformation* of $x$ with value $k \in C$ consists of power series $\Theta_a(T)$ and $\Gamma_{a j}(T)$ over $C$ with coefficients bounded by some $b$, an element $\pi \in C$ with $|\pi| < 1$, and $\varepsilon > 0$, such that:

1. $\Theta_a(\pi)$ and $\Gamma_{a j}(\pi)$ are the theta constants and first jets of $x$ at level $m$;
2. for every $u \in \mathbb{C}$ with $0 < |u| < \varepsilon$, the series $\Theta^e_a(u)$ and $\Gamma^e_{a j}(u)$, with coefficients mapped by $e$, converge absolutely, and they are the theta constants and first jets of a complex key datum $x_u$ of dimension $g$, with a level structure of level $m^2$ for $e(\zeta)$, and with $\kappa(x_u) = e(k)$.

**Theorem 7.38.2 (Transfer of key values).** Let $\kappa$ satisfy Rule 4. For every $g$ and every odd prime $n$ there is $j_0$ such that for all $j \geq j_0$, all $C$ and $e$ as above, and every key datum $x$ over $C$ of dimension $g$ with a level structure of level $n^{2j}$ and a deformation with value $k$ at $m = n^j$, we have $\kappa(x) = k$.

Lean: `GlobalTheory.T.transfer_of_rule4'` (also `GlobalTheory.MBLow.KeyTop.transfer_of_rule4`).

*Proof.* Let $j_1$ be the bound for which theta constants of level $n^j$, $j \geq j_1$, determine a family; we take $j_0 = \max(j_1, 1)$. Let $j \geq j_0$ and $m = n^j$; then $m$ is odd and $m \geq 3$.

1. Collect the power series $\Theta_a$ and $\Gamma_{a j}$ into one family $\Phi$ and the numbers $\zeta, k$ into one pair. There are a complex number $u$ with $0 < |u| < \varepsilon$, a field $o$ of characteristic zero with an embedding $o \to C$ through which $\zeta$ and $k$ factor, and a noetherian integrally closed local domain $W$ of characteristic zero with:
   - a map $\beta \colon o \to W$, an injective map $i_0 \colon W \to \mathbb{C}$ and a map $i_1 \colon W \to C$, compatible with $e$ and the embedding of $o$, such that the elements with nonzero image under $i_1$ are units and the only primes of $W$ are the kernels of $i_0$ and $i_1$;
   - elements $\varphi_a$ of $W$ with $i_0(\varphi_a) = \Phi^e_a(u)$ and $i_1(\varphi_a) = \Phi_a(\pi)$.
   So $W$ is a local ring of dimension one with generic point in $\mathbb{C}$ and closed point in $C$, and the series become one element of $W$ each.
2. The deformation at $u$ gives a complex key datum $x_u$ with $\kappa(x_u) = e(k) = i_0(\beta(k_0))$, where $k_0 \in o$ maps to $k$.
3. Theta constants and first jets of odd level determine the points of the level structure as theta points, both for $x_u$ and for $x$.
4. By the choice of $j_1$, there is a polarized abelian scheme $P$ over $W$ with points $q_a$ of order dividing $m^2$ whose fibres under $i_0$ and $i_1$ are $x_u$ and $x$ with their level structures. This is the step where the level is large.
5. The level structure of $x$ exhausts the points of order dividing $m^2$, since $C$ is algebraically closed.
6. The theorem on two fibres applies to $W$, $i_0$, $i_1$, $P$, $x_u$ and $x$, with $\vartheta$ and $J$ the elements $\varphi$ and with $\beta(k_0)$ in place of $k$. It gives $\kappa(x) = i_1(\beta(k_0)) = k$.

This proves the theorem. $\square$

The point of the theorem is that $e$ need not be continuous, so the complex data $x_u$ and the nonarchimedean datum $x$ have no direct relation. The ring $W$ is the algebraic replacement: it holds the values of the power series at both arguments, and the two fibres of one family over $W$ carry the two data. Steps 1 and 4 are cited results whose proofs we have not opened. Step 4 is the classical theorem of Mumford that theta constants of sufficiently high level give a closed embedding of the moduli of polarized abelian varieties with level structure; this is a classical reference and not the Lean proof.

**Remark 7.38.3 (Formalization).** The relay `transfer_of_rule4'` is at line 12 of [KeyRuleConstantAlongDeformationOfClausesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeyRuleConstantAlongDeformationOfClausesStatement.lean#L12), under `maxHeartbeats 1000000`, and its target `transfer_of_rule4` is at line 35 of [KeyRuleConstantAlongDeformationOfClauses.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeyRuleConstantAlongDeformationOfClauses.lean#L35). The two helpers `levelPoint_cast` (line 17) and `exhaust` (line 21, step 5) are in a block of the namespace `GlobalTheory.MBLow.KeyTop` that is closed at line 31 and opened again at line 33. Step 1 is `exists_deformation_base_ring_local_domain` (line 63), step 3 is `isThetaPt_of_thetaConstantsAndFirstJets`, and step 4 is `exists_family_localDomain_of_twoFibres` (lines 37 and 92). `Rule4`, `Deform` and `Transfer` are at lines 78, 104 and 117 of [IsPolAVSectionInverseImage.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsPolAVSectionInverseImage.lean#L78), and the four properties are in [KeyRootOfKeyFormula.lean](lean:Development/AbelianVarietyTheory/Definitions/KeyFormula/KeyRootOfKeyFormula.lean#L13). The relay `thetaKeyValue_two_fibres_local_ring` is at line 12 of [ThetaKeyValueTwoFibresLocalRingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyValueTwoFibresLocalRingStatement.lean#L12), under `maxHeartbeats 1000000`, and its target `keyValue_twoFibres` is at line 97 of [ThetaKeyValueTwoFibresLocalRing.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyValueTwoFibresLocalRing.lean#L97). It discards functoriality and normalization with `obtain ⟨hHom, -, -, hFam⟩ := hκ` at line 100. Step 7 is `frame_coords_lift` (line 22), built on the cited `coordinates_integral_of_linearly_independent_reduction`, and step 4 is `thJet_frameChange_castDim` (line 84). Steps 1, 2, 3 and 5 cite `exists_keyDatum_polarisedAbelian_localDomain`, `exists_thetaConstantsJets_localDomain`, `exists_keyDatum_fibre_of_grpPullback`, `thetaConstantsJets_baseChange_polarisedDatum`, `exists_scalar_matrix_between_keyData` and `thetaConstants_firstJets_linearIndependent`, whose proofs were not opened.
