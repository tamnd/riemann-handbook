---
title: Laws at a joint site
decls:
  - GlobalTheory.TwV.Xc.AwayInd.away_of_pos_pair
  - GlobalTheory.T.kernelSite_away_of_positive_pair
  - GlobalTheory.TwV.away_of_dict
  - GlobalTheory.T.kernelSite_series_independent_away_from_place_over_p
  - GlobalTheory.XiGen.xiEx_theta_general
  - GlobalTheory.TwV.site_law_xiIn
  - GlobalTheory.T.kernelSite_law_and_fixedCoordinateStabiliserLaw
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Laws at a joint site

This section proves three laws of the theta family of a joint site: the kappa law, the stabilizer law and the local factorization at each place over $p$. The local factorization says that, at a place $v$ over $p$, the series of a pair of lattice tuples is a fixed function of the local lattices at $v$, times explicit units and a power of $p$. Its key input is the *away property*: the data of the site do not change when the lattice tuples change only at $v$. We prove the away property first, from the dictionary of the joint. Section 5 feeds the three laws into the admissibility of the system at $p$.

### The data of a site

Let $J$ be a joint with standard data, and let $\mathcal{S}$ be a joint site for it, as in Section 2. Let $p$ be the residue characteristic and $X$ the formal group system of the site. For each level $j \le m$ the system has components $c$ and lattice tuples $L$. A pair $L_a = (c, L)$ is a lattice tuple at level $j$ with component $c$. At each place $v$ of $X$ over $p$ we have the local ring $W_v$, a map $\rho_v$ from $E$ to the completion at $v$, and the local lattice $\Lambda_v(L)$ of a tuple. The frame data of the site attach to $L_a$ a frame matrix $\varphi_j(L_a)_v$ at each place $v$, and a kernel lattice $N_j(L_a)$, which is an $\mathcal{O}_E$-lattice in $E^{N(j)}$. To a pair $(L_a, L_a')$ at the levels $j$ and $j+1$ they attach a theta kernel $\theta(L_a, L_a')$ of the pair of kernel lattices with a datum $\xi_j(L_a, L_a')$, a scalar $s_j(L_a, L_a')$, a character factor $\chi(L_a, L_a')$ and a power $P_j(L_a, L_a')$ of $p$. The *theta family* $\Theta_j(L_a, L_a')$ of the site is the power series over $\mathbb{C}_p$ obtained from these data. It is the image under $\lambda$ of the Taylor series of $s_j \chi^{-1} \theta$, times $P_j$, read through the frames.

We use the following conditions on a site.

**Definition 5.3.1 (Conditions on a site).** Let $\mathcal{S}$ be a joint site.
1. *Dictionary.* For each level $j \le m$ and each lattice tuple $L_a$, there is a chart point $q$ over $L_a$. It has the form $q = \gamma\, y_{c}\, \kappa$ with $\gamma$ a rational unitary element, $y_c$ the class point of the class of $L_a$, and $\kappa$ in the level group. The kernel lattice $N_j(L_a)$ is the lattice of $q$, and the determinant of $L_a$ is $\det q$.
2. *Pair condition.* For $j < m$ and lattice tuples $L_a, L_a'$ at the levels $j, j+1$: the kernel lattices are admitted, $\theta(L_a, L_a')$ is holomorphic with algebraic Taylor coefficients, $s_j$ and $\chi$ are algebraic, $\chi \ne 0$, the frame matrices have unit determinants, and at each place $v$ the $W_v$-span of $\rho_v(N_j(L_a))$ is the image of $\Lambda_v(L)$ under the frame.
3. *Positions.* The embeddings of $E$ at the places over $p$ match the positions of the system.
4. *Moves.* An element $\gamma$ of the level group of a component moves the frame, the kernel lattice, the datum $\xi$ and the scalar by a unitary matrix $e$ with $e e^* = 1$ and an algebraic constant, with total factor $\kappa_G(\gamma)^{-1}$.
5. *Away property.* For every place $v$ over $p$ and every $j < m$ the condition below holds.

**Definition 5.3.2 (Away property at $v$ and $j$).** Two pairs $(L_a, L_a')$ and $(L_b, L_b')$ at the levels $j, j+1$ have the *same class away from $v$* if they have the same components and their tuples agree outside the coordinate of $v$. The away property at $(v, j)$ says that there is a prime $\mathfrak{P}$ of $\mathcal{O}_E$ with the following properties.
1. $\mathfrak{P}$ is split. The inverse half different is trivial at $\mathfrak{P}$. Neither $\mathfrak{P}$ nor $\bar{\mathfrak{P}}$ is in the bad set $S$, and neither contains the level $\ell$.
2. $\mathfrak{P}$ is the prime under $v$: for $x \in \mathcal{O}_E$ we have $\rho_v(x) \in W_v$, and $x \in \mathfrak{P}$ if and only if $p \mid \rho_v(x)$. Also $\rho_v(\mathcal{O}_E)$ is dense in $W_v$ modulo every power of $p$.
3. There are units $u, u'$ of valuation $0$ such that, whenever $(L_a, L_a')$ and $(L_b, L_b')$ are pairs of lattice tuples with the same class away from $v$: the kernel lattices agree off $\mathfrak{P}$, the frame matrices agree, the data $\xi_j$ agree, and
$$P_j(L_a, L_a')\,\lambda(s_j(L_a, L_a'))\,u^{n_v(L_b)} u'^{n_v(L_b')} = P_j(L_b, L_b')\,\lambda(s_j(L_b, L_b'))\,u^{n_v(L_a)} u'^{n_v(L_a')}.$$
Here $n_v$ is the length of a tuple at $v$.

### The away property

**Theorem 5.3.3 (Away property from positions and pairs).** Let $\mathcal{S}$ be a joint site whose joint has a dictionary and satisfies the split condition. Assume that every value of the seam embedding $\sigma_0$ of $t$ lies in the image of the field $L$. If the positions and the pair condition hold, then the away property holds at every $(v, j)$ with $j < m$.

Lean: `GlobalTheory.TwV.Xc.AwayInd.away_of_pos_pair` (also `GlobalTheory.T.kernelSite_away_of_positive_pair`)

*Proof.* Fix $v$ and $j < m$. The dictionary and the split condition give that the level $\ell$ is prime to $p$, and that the bad set avoids the primes over $p$. A lemma on the place over $p$ gives a prime $\mathfrak{P}$ under the first factor at $v$, with the properties of item 2. A lemma on the good data of the joint shows that $\mathfrak{P}$ is not stable under complex conjugation. It gives elements $a$ and $b = \bar{a}$ of $\mathcal{O}_E$ that witness that $\mathfrak{P}$ is split. Since $p$ is unramified, the inverse half different is trivial at $\mathfrak{P}$. Neither $\mathfrak{P}$ nor $\bar{\mathfrak{P}}$ is in the bad set. Since $\ell$ and $p$ are coprime in $\mathbb{Z}$, they generate the unit ideal of $\mathcal{O}_E$, so no prime over $p$ contains $\ell$.

For item 3 there are two cases. If the levels $j$ and $j + 1$ both have a component, choose a norm-one idele $\pi$ that has order one at $v$ and is trivial at the other places. With the positions and the pair condition, $\pi$ gives two units $u, u'$ of valuation $0$. Now let two pairs have the same class away from $v$. The kernel lattices agree off $\mathfrak{P}$, by a lemma on kernel lattices of tuples that agree away from $v$. The frame matrices depend only on the component, so they agree. The data $\xi_j$ agree by a lemma on moved data. The identity of the scalars is a lemma on the scalars of a site, which uses the pair condition and $\pi$. If one of the two levels has no component, there are no lattice tuples at that level. Then item 3 is empty, and we take $u = u' = 1$. $\square$

**Corollary 5.3.4 (Away property from the dictionary).** Let $\mathcal{S}$ be a joint site whose joint has a dictionary and satisfies the split condition. Then the away property holds at every $(v, j)$ with $j < m$.

Lean: `GlobalTheory.TwV.away_of_dict` (also `GlobalTheory.T.kernelSite_series_independent_away_from_place_over_p`)

*Proof.* The joint gives the algebraicity of $\sigma_0$. A lemma on sites says that the place of the site induces the position embeddings, so the positions hold. A second lemma says that, given the dictionary, the pairs of lattice tuples are admissible, so the pair condition holds. The previous theorem now applies. $\square$

### The local factorization

At a place $v$ over $p$ and a level $j$, let $\mathbf{1}_{v,j}(L, L')$ be the indicator function of the set of matrices over the completion at $v$ that map the local lattice $\Lambda_v(L)$ into $\Lambda_v(L')$. It is a function with values in $\mathbb{Q}$. Let $\mathrm{vol}_v(L, L')$ be the volume exponent of this set, and let $n'_v$ be the even local rank.

**Definition 5.3.5 (Local factorization at $v$ and $j$).** A family $\Theta_j$ of power series *factors locally* at $(v, j)$ if there are units $u, u'$ of valuation $0$ and, for each class $\alpha$ away from $v$, an additive map $\Xi_\alpha$ from the $\mathbb{Q}$-valued functions on matrices to power series, such that for all lattice tuples $L_a, L_a'$ at the levels $j, j+1$:
$$\Theta_j(L_a, L_a') = u^{n_v(L)}\, u'^{n_v(L')}\, p^{-(n'_v/2)\mathrm{vol}_v(L, L')}\; \Xi_{\alpha(L_a, L_a')}\bigl(\mathbf{1}_{v,j}(L, L')\bigr).$$

So the series depends on the coordinate at $v$ only through a scaling and the local indicator function.

**Theorem 5.3.6 (Local factorization of the theta family).** Let $D$ be a datum, $\mathfrak{c}$ a curve ideal, $\delta \ne 0$ a twelfth root of the discriminant of its lattice, $B$ a base with its lattice and vector laws, and $\chi$ a character of the right type. Assume that the curve has models at the split places and that the moves at split places compose. Let $S$ be a finite set of primes of $\mathcal{O}_E$ that contains no conjugate of its members, and $\ell > 0$. Let $X$ be a formal group system at a prime $p$, with an embedding into $\mathbb{C}_p$, positions, frame data, a ring map $\lambda$, data $\Xi_0$, characters and local maps $\rho$. Assume the pair condition. Let $v$ be a place over $p$ and $j < m$, and assume the away property at $(v, j)$. Then the theta family $\Theta$ built from these data factors locally at $(v, j)$.

Lean: `GlobalTheory.XiGen.xiEx_theta_general`

*Proof.* Take $\mathfrak{P}$, $u$ and $u'$ from the away property. For lattice tuples $L_a, L_a'$ put
$$k(L_a, L_a') = u^{n_v(L)}\, u'^{n_v(L')}\, p^{-(n'_v/2)\mathrm{vol}_v(L, L')}.$$
This is nonzero, since $u, u' \ne 0$ and $p \ne 0$ in the base field. Fix a class $\alpha$ away from $v$, and let $I_\alpha$ be the set of pairs of lattice tuples in the class $\alpha$. We claim: if rational numbers $c_i$ satisfy $\sum_i c_i \mathbf{1}_{v,j}(i) = 0$ over a finite subset of $I_\alpha$, then $\sum_i c_i\, k(i)^{-1} \Theta_j(i) = 0$. Given the claim, there is an additive map $\Xi_\alpha$ with $\Xi_\alpha(\mathbf{1}_{v,j}(i)) = k(i)^{-1}\Theta_j(i)$ for all $i \in I_\alpha$, and this is the factorization.

We prove the claim. Fix a base pair $i_0 = (L_{a,0}, L_{a,0}')$ in the subset. By the away property, every pair $i$ in the class has the same frames and the same datum $\xi$ as $i_0$, and its kernel lattices agree with those of $i_0$ off $\mathfrak{P}$. A lemma on split places gives an isomorphism $\phi$ of the completion of $E$ at $\mathfrak{P}$ with the completion at $v$. Under $\phi$ and the frames of $i_0$, the indicator function of the set $Y_{\mathfrak{P}}(i)$ of matrices over $E_{\mathfrak{P}}$ that map the kernel lattices of $i$ into each other becomes $\mathbf{1}_{v,j}(i)$. The same lemma gives the volume ratio
$$\sqrt{\mathrm{vol}\bigl(Y_{\mathfrak{P}}(i_0)\bigr)/\mathrm{vol}\bigl(Y_{\mathfrak{P}}(i)\bigr)} = r_i = p^{(n'_v/2)(\mathrm{vol}_v(i) - \mathrm{vol}_v(i_0))}.$$
So the relation $\sum c_i \mathbf{1}_{v,j}(i) = 0$ becomes the relation $\sum c_i \mathbf{1}_{Y_\mathfrak{P}(i)} = 0$ of indicator functions over $E_\mathfrak{P}$. The theorem on theta kernels at a split prime turns a relation of indicator functions into a relation of theta kernels. It gives
$$\sum_i c_i\, r_i\, \chi(i)^{-1}\, \theta(i) = 0$$
as functions, where all kernels use the datum $\xi$ of $i_0$. We take Taylor coefficients. The Taylor series is linear, and its coefficients are algebraic by the pair condition. So we may apply $\lambda$ to the coefficients. By the away property, $P_j(i)\lambda(s_j(i)) = Q_0 \cdot w_i$, with $Q_0$ fixed and $w_i$ the unit part of $k(i)$. A computation with $r_i$ then shows that the coefficients of $\sum_i c_i\, k(i)^{-1} G_i$ vanish, where $G_i$ is the series of $i$ before the frame substitution. Last, the substitution of the frames is linear and the same for all $i$ in the class. Hence $\sum_i c_i\, k(i)^{-1}\Theta_j(i) = 0$. $\square$

### The three laws

The *kappa law* of a site says that the theta family transforms under the level groups by the characters $\kappa_G$. The *stabilizer law* says: for $j < m$, a representative $(c, L_0)$ at level $j$, a lattice tuple $L_a'$ at level $j+1$, and $\varepsilon$ in the level group with $\varepsilon L_0 = L_0$, the action of $\varepsilon$ fixes the series:
$$\kappa_G(\varepsilon)^{-1} \cdot \bigl(\varepsilon \cdot \Theta_j((c, L_0), L_a')\bigr) = \Theta_j((c, L_0), L_a').$$
The *local factorization law* says that the theta series of the pending tuple of the site factor locally at every $(v, j)$ with $j < m$.

**Theorem 5.3.7 (The three laws at a site).** Let $\mathcal{S}$ be a joint site. Assume the pair condition, the positions, the moves and the away property. Then the kappa law, the stabilizer law and the local factorization law hold.

Lean: `GlobalTheory.TwV.site_law_xiIn` (also `GlobalTheory.T.kernelSite_law_and_fixedCoordinateStabiliserLaw`)

*Proof.* The entry $t$ gives its base data: $\delta \ne 0$ and the lattice and vector laws of $B$. The joint gives $\ell > 0$ and the fact that the bad set contains no conjugate of its members. The ranks of the system of the site are the ranks of $D$, so its top level is $m$.

The kappa law is a theorem on the theta family read from the adelic datum. Its inputs are the data above, the pair condition, the positions and the moves.

For the stabilizer law, fix $j < m$, a representative $(c, L_0)$, $L_a'$ and $\varepsilon$ with $\varepsilon L_0 = L_0$. The representative is a lattice tuple, since the classes are finite. The stabilizer part of the kappa law gives the identity.

For the local factorization law, fix $v$ and $j < m$. A lemma on pending tuples says that the theta series of the pending tuple factor locally at $(v, j)$ if the theta family does, given the kappa law. The theorem on the local factorization of the theta family applies, with the models at split places and the composition of moves from the datum $D$, the pair condition, and the away property at $(v, j)$. $\square$

**Remark 5.3.8 (Formalization).** Several facts about the Lean code:
1. The names `GlobalTheory.T.kernelSite_away_of_positive_pair`, `GlobalTheory.T.kernelSite_series_independent_away_from_place_over_p` and `GlobalTheory.T.kernelSite_law_and_fixedCoordinateStabiliserLaw` are second names, each proved by the tactic `first | exact @… | …` under `maxHeartbeats 1000000`.
2. The away theorem quantifies over `Sites` (IsUnifAt.lean:59), which adds the dictionary and the split condition `Spl J` to the quantifier `AllSites`. The away property is `AwayTie` (NatCastMemOfPlace.lean:85). The branch with an empty level takes $u = u' = 1$ and is vacuous (KernelSiteAwayOfPositivePair.lean:47).
3. The name `kernelSite_law_and_fixedCoordinateStabiliserLaw` mentions only two of the three conclusions: it omits the local factorization law `XiIn`. The away hypothesis is used only for this third conclusion (KernelSiteLawAndFixedCoordinateStabiliserLaw.lean:20).
4. The local factorization is `XiEx`. The additive maps $\Xi_\alpha$ come from `GlobalTheory.exists_addMonoidHom_of_linear_relations` through `Classical.choose`, so they are not explicit (XiExThetaGeneral.lean:86). The file also proves seven small helper lemmas on `lamC`, `resV` and `subBG`.
5. The name `kernelSite_series_independent_away_from_place_over_p` describes the away property, which is the conclusion. The positions and the pair condition are obtained inside the proof from `site_place_induces_position_embeddings` and `kernelSite_latticeTuplePairs_admissible`.
