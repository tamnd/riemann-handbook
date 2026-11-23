---
title: The local identity for a split vector
decls:
  - Formalism.HermitianLattices.Ext.L3.LIOrb.main_term
  - Formalism.HermitianLattices.Ext.L3.liRatio
  - Formalism.HermitianLattices.Ext.L3.PinD.core
  - Formalism.HermitianLattices.Ext.L3.liPin
  - Formalism.HermitianLattices.Ext.L3.liStat
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local identity for a split vector

This section computes, at one prime $\mathfrak{p}$, the local factor $\psi_{\mathfrak{p}}$ that appears when one passes from a lattice $L$ in $V$ to the lattices of the orthogonal complement of a vector $x_0$. The result is the local identity: $\psi_{\mathfrak{p}}$ equals the local representation density of $n = h(x_0, x_0)$ by $L$, divided by the local density of $L$ and multiplied by a standard factor. The proof has two parts. A ratio identity shows that the quotient of $\psi_{\mathfrak{p}}$ by the density of $n$ is the same for all integral lattices. A computation for one good lattice fixes the value of the quotient. The next section uses the local identity at each prime to prove the induction step of the mass formula. We keep the notation of the last section: $K$ is an unramified CM field with real subfield $K^+$, $h$ is a totally positive definite Hermitian form on $V$ of dimension $m$, and $(x_0, \iota)$ is a split vector with $\iota \colon V' \to V$ and $h' = h \circ (\iota \times \iota)$.

### The local factors

**Definition 6.6.1 (Standard factor and local mass factor).** For $j \geq 0$ let
$$\alpha^{\mathrm{std}}_{\mathfrak{p}}(j) = \prod_{i = 1}^{j} \bigl(1 - \eta(\mathfrak{p})^i q^{-i}\bigr).$$
For a lattice $T$ in a Hermitian space $(W, h_W)$ of dimension $j$, let
$$\lambda_{\mathfrak{p}}(h_W, T) = \frac{\alpha^{\mathrm{std}}_{\mathfrak{p}}(j)\, q^{j\, v_{\mathfrak{p}}(T)}}{\alpha_{\mathfrak{p}}(T)} = \frac{\alpha^{\mathrm{std}}_{\mathfrak{p}}(j)}{\nu_{\mathfrak{p}}(T)}.$$

The product $\alpha^{\mathrm{std}}_{\mathfrak{p}}(j)$ is the form that the local density of a unimodular lattice of rank $j$ takes at an unramified prime. So $\lambda_{\mathfrak{p}}$ compares the density of $T$ with the unimodular one. The [Siegel mass formula](/learn/groups/#hermitian-lattices-and-the-mass-formula) expresses a mass as a constant times the product of the $\lambda_{\mathfrak{p}}$.

**Definition 6.6.2 (Fibres and the local fibre sum).** Let $L$ be a lattice in $V$. For a lattice $T$ of $V'$, let $f_{\mathfrak{p}}(L, T)$ be the number of $\mathcal{O}_K$-lattices $\Lambda \subseteq V$ with four properties: $\Lambda_{\mathfrak{p}} = \Lambda$; $\Lambda = g L_{\mathfrak{p}}$ for some isometry $g$ of $(V, h)$; $x_0 \in \Lambda$; and $\iota^{-1}(\Lambda) = T_{\mathfrak{p}}$. A finite set $s$ of lattices of $V'$ is a *local system of representatives* for $L$ if each $T \in s$ has $T_{\mathfrak{p}} = T$, $h'(T, T) \subseteq \mathcal{O}_{K, \mathfrak{p}}$ and $f_{\mathfrak{p}}(L, T) \neq 0$, and if each $T$ with these three properties is the image of exactly one $T_0 \in s$ under an isometry of $(V', h')$. If such an $s$ exists, let
$$\psi_{\mathfrak{p}}(L) = \sum_{T \in s} f_{\mathfrak{p}}(L, T)\, \lambda_{\mathfrak{p}}(h', T),$$
and let $\psi_{\mathfrak{p}}(L) = 0$ otherwise.

A lattice $\Lambda$ counted by $f_{\mathfrak{p}}(L, T)$ is a local copy of $L$ that contains $x_0$ and cuts out $T$ on the complement. So $\psi_{\mathfrak{p}}(L)$ is the local mass factor of the complement, weighted by the number of ways to extend each complement lattice by $x_0$. For integral $L$ a local system of representatives exists. For an integral lattice $L$ and $n \in \mathcal{O}_{K^+}$, $n \neq 0$, let
$$R_{\mathfrak{p}}(L, n) = \frac{q^{(m - 1) v_{\mathfrak{p}}(L)}\, \alpha_{\mathfrak{p}}(L, n)}{\alpha_{\mathfrak{p}}(L)}.$$
Let $v_{\mathfrak{p}}(n)$ be the largest $e$ with $n \in \mathfrak{p}^e$.

### The main term of the count

**Lemma 6.6.3 (Main term).** Let $L$ and $M_2$ be integral lattices, $n \in \mathcal{O}_{K^+}$ with $n \neq 0$ and $h(x_0, x_0) = n$, and assume $x_0 \in M_{2, \mathfrak{p}}$. Let $s$ be a local system of representatives for $L$. Then for all large $J$, and then for all large $k$,
$$N_k(L, n) = \kappa_{J, k}(M_{2, \mathfrak{p}})\, q^{v_{\mathfrak{p}}(L)}\, \nu_{\mathfrak{p}}(L) \sum_{T \in s} \frac{f_{\mathfrak{p}}(L, T)}{\nu_{\mathfrak{p}}(T)}.$$

Lean: `Formalism.HermitianLattices.Ext.L3.LIOrb.main_term`.

*Proof.* Let $\mathcal{M}$ be the set of lattices $g L_{\mathfrak{p}}$, with $g$ an isometry of $(V, h)$, that contain $x_0$. The group of maps $\hat g'$, with $g'$ an isometry of $(V', h')$, acts on $\mathcal{M}$. There is a finite set $\mathcal{R}$ of representatives of the orbits. For $J$ and $k$ large, the classes counted by $N_k(L, n)$ fall into the tubes around the orbit of $x_0$ in the lattices $M \in \mathcal{R}$, one tube for each $M$. This gives
$$N_k(L, n) = \sum_{M \in \mathcal{R}} c_k\bigl(M, n, \Omega_J(M)\bigr).$$
By definition, $c_k(M, n, \Omega_J(M)) = \kappa_{J, k}(M)\, q^{v(M)} \nu(M)\, o(M) / \nu(M')$. By the [independence of the tube factor](/entry/kap-eq/), $\kappa_{J, k}(M) = \kappa_{J, k}(M_{2, \mathfrak{p}})$ for each of the finitely many $M \in \mathcal{R}$. Each $M$ is $g L_{\mathfrak{p}}$ for an isometry $g$, and $v_{\mathfrak{p}}$ and $\nu_{\mathfrak{p}}$ do not change under isometries, so $q^{v(M)} \nu(M) = q^{v(L)} \nu(L)$. Finally, grouping the $M \in \mathcal{R}$ by the class of their cut gives
$$\sum_{M \in \mathcal{R}} \frac{o(M)}{\nu(M')} = \sum_{T \in s} \frac{f_{\mathfrak{p}}(L, T)}{\nu(T)},$$
by orbit counting: the lattices $\Lambda$ counted by $f_{\mathfrak{p}}(L, T)$ are the members of the orbits of those $M$ whose cut is isometric to $T$, and $o(M)$ counts the members of the orbit of $M$ with a given cut. $\square$

### The ratio and the pin

**Theorem 6.6.4 (Ratio identity).** Let $L, L_0$ be integral lattices in $V$ and $n \in \mathcal{O}_{K^+}$ with $n \neq 0$ and $h(x_0, x_0) = n$. Then
$$\psi_{\mathfrak{p}}(L)\, R_{\mathfrak{p}}(L_0, n) = \psi_{\mathfrak{p}}(L_0)\, R_{\mathfrak{p}}(L, n).$$

Lean: `Formalism.HermitianLattices.Ext.L3.liRatio`.

*Proof.* Assume first that some integral lattice $M_2$ has $x_0 \in M_{2, \mathfrak{p}}$. Choose local systems of representatives $s$ for $L$ and $s_0$ for $L_0$, and let $\sigma(L) = \sum_{T \in s} f_{\mathfrak{p}}(L, T)/\nu_{\mathfrak{p}}(T)$. Since $\lambda_{\mathfrak{p}}(h', T) = \alpha^{\mathrm{std}}_{\mathfrak{p}}(m - 1)/\nu_{\mathfrak{p}}(T)$, we have $\psi_{\mathfrak{p}}(L) = \alpha^{\mathrm{std}}_{\mathfrak{p}}(m - 1)\, \sigma(L)$, and the same for $L_0$. Choose $J$ and $k$ so large that the [main term lemma](/entry/main-term/) holds for $L$ and for $L_0$ with the same $M_2$, and that $k \geq 2 v_{\mathfrak{p}}(L) + 2 v_{\mathfrak{p}}(n) + 2$ and the same for $L_0$. For such $k$ the representation density is already reached: $\alpha_{\mathfrak{p}}(L, n) = N_k(L, n)/q^{k(2m - 1)}$. With $\kappa = \kappa_{J, k}(M_{2, \mathfrak{p}})$ and $\nu(L) = \alpha(L)/q^{m v(L)}$ the lemma gives
$$R_{\mathfrak{p}}(L, n) = \frac{q^{(m-1) v(L)}\, \kappa\, q^{v(L)}\, \nu(L)\, \sigma(L)}{q^{k(2m - 1)}\, \alpha(L)} = \frac{\kappa\, \sigma(L)}{q^{k(2m - 1)}}.$$
The same holds for $L_0$ with the same $\kappa$. So both sides of the identity equal $\alpha^{\mathrm{std}}_{\mathfrak{p}}(m - 1)\, \kappa\, \sigma(L) \sigma(L_0)/q^{k(2m-1)}$. If no such $M_2$ exists, then no lattice $g L_{\mathfrak{p}}$ contains $x_0$, the set $\mathcal{R}$ in the proof of the lemma is empty, $N_k(L, n) = 0$ for large $k$, and $R_{\mathfrak{p}}(L, n) = 0$. The same holds for $L_0$, and both sides are $0$. $\square$

**Theorem 6.6.5 (Pin).** Let $n \in \mathcal{O}_{K^+}$ with $n \neq 0$ and $h(x_0, x_0) = n$. Then there is an integral lattice $L_0$ in $V$ with $R_{\mathfrak{p}}(L_0, n) \neq 0$ and
$$\psi_{\mathfrak{p}}(L_0) = q^{(m - 1) v_{\mathfrak{p}}(n)}\, \alpha^{\mathrm{std}}_{\mathfrak{p}}(m - 1)\, R_{\mathfrak{p}}(L_0, n).$$

Lean: `Formalism.HermitianLattices.Ext.L3.liPin` (also `Formalism.HermitianLattices.Ext.L3.PinD.core`, the same statement for forms written as $n h_0$ and $n h_0'$).

*Proof.* Write $h = n h_0$ and $h' = n h_0'$. Then $(x_0, \iota)$ is a split vector for $(h_0, h_0')$ with $h_0(x_0, x_0) = 1$. Since $x_0$ has unit length for $h_0$, there is an $h_0$-integral lattice $L_0$ with $x_0 \in L_0$, $v_{\mathfrak{p}}(L_0) \leq 1$ and $L_0 = \mathcal{O}_K x_0 \oplus \iota(L_0')$, where $L_0'$ is its cut; then $v_{\mathfrak{p}}(L_0') = v_{\mathfrak{p}}(L_0)$. For this orthogonal sum the local density splits as
$$\alpha_{\mathfrak{p}}(h_0, L_0) = \alpha_{\mathfrak{p}}(h_0, L_0, 1)\, \alpha_{\mathfrak{p}}(h_0', L_0').$$
Next we find $\psi_{\mathfrak{p}}(L_0)$. The set $\{L'_{0, \mathfrak{p}}\}$ is a local system of representatives for $L_0$, and $f_{\mathfrak{p}}(L_0, L'_{0, \mathfrak{p}}) = 1$. Hence $\psi_{\mathfrak{p}}(L_0) = \lambda_{\mathfrak{p}}(n h_0', L'_{0, \mathfrak{p}})$. The scaling by $n$ changes the invariants in a known way: with $e = v_{\mathfrak{p}}(n)$ and $j$ the dimension,
$$\alpha_{\mathfrak{p}}(n h_0, L, n) = q^{e}\, \alpha_{\mathfrak{p}}(h_0, L, 1), \quad \alpha_{\mathfrak{p}}(n h_0, L) = q^{e j^2} \alpha_{\mathfrak{p}}(h_0, L), \quad v_{\mathfrak{p}}(n h_0, L) = v_{\mathfrak{p}}(h_0, L) + j e.$$
Write $v_0 = v_{\mathfrak{p}}(h_0, L_0) = v_{\mathfrak{p}}(h_0', L_0')$ and $\alpha' = \alpha_{\mathfrak{p}}(h_0', L_0')$. With $j = m - 1$ for $V'$ and $j = m$ for $V$, and the splitting of $\alpha_{\mathfrak{p}}(h_0, L_0)$, we get
$$\begin{aligned} \psi_{\mathfrak{p}}(L_0) &= \frac{\alpha^{\mathrm{std}}_{\mathfrak{p}}(m-1)\, q^{(m-1)(v_0 + (m-1)e)}}{q^{(m-1)^2 e}\, \alpha'} = \frac{\alpha^{\mathrm{std}}_{\mathfrak{p}}(m-1)\, q^{(m-1) v_0}}{\alpha'}, \\ R_{\mathfrak{p}}(L_0, n) &= \frac{q^{(m-1)(v_0 + m e)}\, q^{e}\, \alpha_{\mathfrak{p}}(h_0, L_0, 1)}{q^{m^2 e}\, \alpha_{\mathfrak{p}}(h_0, L_0, 1)\, \alpha'} = \frac{q^{(m-1)(v_0 - e)}}{\alpha'}. \end{aligned}$$
The quotient is $\alpha^{\mathrm{std}}_{\mathfrak{p}}(m-1)\, q^{(m-1)e}$, as claimed. Finally $R_{\mathfrak{p}}(L_0, n) \neq 0$, since $\alpha_{\mathfrak{p}}(h_0, L_0, 1) \neq 0$ by the splitting and the positivity of local densities. $\square$

### The local identity

**Theorem 6.6.6 (Local identity).** Let $L$ be an integral lattice in $V$ and $n \in \mathcal{O}_{K^+}$ with $n \neq 0$ and $h(x_0, x_0) = n$. Then
$$\psi_{\mathfrak{p}}(L) = q^{(m - 1)(v_{\mathfrak{p}}(n) + v_{\mathfrak{p}}(L))}\, \frac{\alpha^{\mathrm{std}}_{\mathfrak{p}}(m - 1)\, \alpha_{\mathfrak{p}}(L, n)}{\alpha_{\mathfrak{p}}(L)}.$$

Lean: `Formalism.HermitianLattices.Ext.L3.liStat` (also `Formalism.HermitianLattices.Ext.L3.liStat_of`, the deduction from the two theorems).

*Proof.* Let $L_0$ be the lattice of the [pin theorem](/entry/li-pin/). By the [ratio identity](/entry/li-ratio/) for $L$ and $L_0$, and the pin,
$$\psi_{\mathfrak{p}}(L)\, R_{\mathfrak{p}}(L_0, n) = q^{(m-1) v(n)}\, \alpha^{\mathrm{std}}_{\mathfrak{p}}(m - 1)\, R_{\mathfrak{p}}(L_0, n)\, R_{\mathfrak{p}}(L, n).$$
Cancel $R_{\mathfrak{p}}(L_0, n) \neq 0$ and insert the definition of $R_{\mathfrak{p}}(L, n)$. $\square$

The local identity is the statement LIStat that the [induction step of the mass](/entry/mass-const-succ/) takes as input. That step serves the step [theta local matching](/step/theta-local-matching/) of the proof.

**Remark 6.6.7 (Formalization).** The local identity is the proposition `LIStat` of [LocalDensityRatio.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/LocalDensityRatio.lean#L121), proved in [LiStatOf.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/LiStatOf.lean#L24). The second case of the ratio identity ([RepRatioEqZero.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/RepRatioEqZero.lean#L84)) never occurs: if $L'$ is an $h'$-integral lattice of $V'$, then $\mathcal{O}_K x_0 \oplus \iota(L')$ is integral and contains $x_0$. The local fibre sum is set to $0$ when no system of representatives exists (lines 96 to 100 of LocalDensityRatio.lean), and $f_{\mathfrak{p}}$ is a `Nat.card` (line 81), which is $0$ for an infinite set; neither convention is reached for integral lattices. The factor $\eta(\mathfrak{p})$ is defined as $1$ also at ramified primes, which the hypotheses exclude. The pin is proved as `PinD.core` in [LiPin.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/LiPin.lean#L20) for scaled forms, and `liPin` (line 104) only writes $h$ and $h'$ in that form. The steps of the main term lemma are the lemmas `exists_mReps`, `nkCount_eq_sum`, `sum_oM` of NkCountEqSum.lean and `nu_gmap_locF` of NuGmapLocF.lean; we give their content from their statements.
