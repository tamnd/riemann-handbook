---
title: Reciprocity on Lubin-Tate extensions
decls:
  - GroundTheory.LocalField.reciprocity_frobenius_lubinTate
  - GroundTheory.LocalField.reciprocity_lubinTate
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reciprocity on Lubin-Tate extensions

We compute the reciprocity map $r_U$ of the previous section on the abelian extensions cut out by a Lubin-Tate tower and an unramified extension. The answer is the explicit law of Lubin and Tate: an element that acts on the $\pi^n$-torsion by $[u^{-1}]_f$ and on $K^{\mathrm{nr}}$ by the $k$-th power of Frobenius corresponds to $u\pi^k$. The main proof uses this law for [every character](/step/every-character/), through the explicit reciprocity law over $\mathbb{Q}_p$ and the existence theorem of the formal-group approach to [[local class field theory|SHEN158T3M]].

We keep the notation of the previous section: $K$ is a nonarchimedean local field with $q$ residue elements, $\Omega$ a separable closure, $G = \operatorname{Gal}(\Omega/K)$, $d : G \to \widehat{\mathbb{Z}}$ the degree map, $\pi$ a uniformizer, $f$ a Lubin-Tate series for $\pi$, $F_f[\pi^n]$ the $\pi^n$-torsion of the Lubin-Tate group and $L_n = K(F_f[\pi^n])$.

### The open subgroups

Both theorems of this section are about an open normal subgroup $U$ of $G$ with
$$G_{L_n} \cap \ker d \;\leq\; U \;\leq\; G_{L_n}. \tag{$\ast$}$$
The fixed field $\Omega^U$ contains $L_n$ and lies in the compositum $L_n K^{\mathrm{nr}}$.

**Example 1.2.1.** Let $K_s$ be the unramified extension of degree $s$ of $K$ in $\Omega$. Then $U = G_{L_n K_s}$ is open and normal, and it satisfies $(\ast)$, because $\ker d = G_{K^{\mathrm{nr}}}$ is contained in $G_{K_s}$. Its fixed field is the finite abelian extension $L_n K_s$.

The first lemma makes the elements that the theorems are about.

**Lemma 1.2.2 (Frobenius elements on the tower).** Let $n \geq 1$ and $w \in \mathcal{O}_K^\times$. There is $\sigma \in G$ with $d(\sigma) = 1$ and $\sigma(x) = [w^{-1}]_f(x)$ for each $x \in F_f[\pi^n]$.

Lean: `GroundTheory.LocalField.exists_lubinTate_frobenius`.

*Proof.* By the isomorphism $\operatorname{Gal}(L_n/K) \cong (\mathcal{O}_K/\pi^n)^\times$ of the previous section, there is $\rho_0 \in \operatorname{Gal}(L_n/K)$ that acts on $F_f[\pi^n]$ by $[w^{-1}]_f$. Extend it to $\rho \in G$. The extension $L_n/K$ has residue degree $1$, so $d$ maps $G_{L_n}$ onto $\widehat{\mathbb{Z}}$. Choose $\rho_1 \in G_{L_n}$ with $d(\rho_1) = 1 - d(\rho)$ and put $\sigma = \rho \rho_1$. Then $d(\sigma) = 1$, and $\sigma$ acts on $L_n$ as $\rho_0$. $\square$

### The value on a Frobenius element

**Theorem 1.2.3 (reciprocity at a Frobenius element).** Let $m \geq 0$, and let $U$ be an open normal subgroup of $G$ with $G_{L_{m+1}} \cap \ker d \leq U \leq G_{L_{m+1}}$. Let $w \in \mathcal{O}_K^\times$ and $\sigma \in G$ with $d(\sigma) = 1$ and $\sigma(x) = [w^{-1}]_f(x)$ for each $x \in F_f[\pi^{m+1}]$. Then
$$r_U(\sigma U) = w\pi \cdot N_{\Omega^U/K}\bigl((\Omega^U)^\times\bigr).$$

Lean: `GroundTheory.LocalField.reciprocity_frobenius_lubinTate`.

*Proof.* Let $\Sigma$ be the fixed field of the closure of $\langle \sigma \rangle (U \cap \ker d)$. By the Proposition on the value on a Frobenius lift in the previous section, it is enough to find $y \in \Sigma$ of valuation $1$ in $\Sigma$ with $N_{\Sigma/K}(y) = w\pi$.

Step 1 (a root). By the Lemma on Eisenstein generators, $L_{m+1} = K(l)$ for a root $l$ of $P_{\pi, m}$. Two Lubin-Tate series for $\pi$ give formal groups that are isomorphic over $\mathcal{O}_K$, by an isomorphism that commutes with each $[a]$ and with the action of $G$. So $\sigma(l) = [w^{-1}](l)$ also holds for the endomorphism $[w^{-1}]$ of $F_{g_\pi}$. The fixed root [Lemma 1.1.8](/entry/exists-fixed-root-lt-eisenstein/) gives a root $x$ of $P_{w\pi, m}$ with $\sigma(x) = x$, such that each $\tau \in G$ that fixes $K^{\mathrm{nr}}$ and $l$ fixes $x$.

Step 2 ($x$ lies in $\Sigma$). The element $\sigma$ fixes $x$. Let $\tau \in U \cap \ker d$. Then $\tau$ fixes $K^{\mathrm{nr}}$, since $\ker d = G_{K^{\mathrm{nr}}}$, and $\tau$ fixes $l \in L_{m+1}$, since $U \leq G_{L_{m+1}}$. So $\tau$ fixes $x$. The stabilizer of $x$ is closed, so it contains the closure of $\langle \sigma \rangle (U \cap \ker d)$, and $x \in \Sigma$.

Step 3 ($\Sigma = K(x)$). The polynomial $P_{w\pi, m}$ is Eisenstein, hence irreducible, so it is the minimal polynomial of $x$, and $[K(x) : K] = (q - 1) q^m$. On the other side, let $S$ be the closure of $\langle \sigma \rangle (U \cap \ker d)$. Then $d(S) = \widehat{\mathbb{Z}}$, since $d(\sigma) = 1$, and $S \cap \ker d = U \cap \ker d$. So $[G : S]$ is the index of $U \cap \ker d$ in $\ker d$. By $(\ast)$, $U \cap \ker d = G_{L_{m+1}} \cap \ker d$, and the index of this group in $\ker d$ is the ramification index of $L_{m+1}/K$, which is $[L_{m+1} : K] = (q - 1) q^m$. So $[\Sigma : K] = [K(x) : K]$, and $K(x) \subseteq \Sigma$ gives $K(x) = \Sigma$.

Step 4 (the norm). Put $y = -x \in \Sigma$. The norm of a generator of $K(x)$ is $(-1)^{e}$ times the constant term of its minimal polynomial, where $e$ is the degree. The minimal polynomial of $-x$ is $(-1)^e P_{w\pi, m}(-X)$, with constant term $(-1)^e w\pi$, so
$$N_{\Sigma/K}(-x) = (-1)^e (-1)^e w\pi = w\pi.$$
Since $w\pi$ has valuation $1$ in $K$ and $\Sigma/K$ is totally ramified (its residue degree is $1$, because $d$ is onto on its Galois group), $-x$ has valuation $1$ in $\Sigma$. The value on a Frobenius lift gives the claim. $\square$

The proof shows more: the field $\Sigma$ attached to $\sigma$ is generated by a root of the Eisenstein polynomial of the uniformizer $w\pi$. This is the field-theoretic content of the theorem.

### The explicit law

**Theorem 1.2.4 (Lubin-Tate reciprocity).** Let $n \geq 1$, and let $U$ be an open normal subgroup of $G$ with $G_{L_n} \cap \ker d \leq U \leq G_{L_n}$. Let $u \in \mathcal{O}_K^\times$, $k \in \mathbb{Z}$, and $\tau \in G$ with $d(\tau) = k$ and $\tau(x) = [u^{-1}]_f(x)$ for each $x \in F_f[\pi^n]$. Then
$$r_U(\tau U) = u\pi^k \cdot N_{\Omega^U/K}\bigl((\Omega^U)^\times\bigr).$$

Lean: `GroundTheory.LocalField.reciprocity_lubinTate`.

*Proof.* Write $n = m + 1$. By the Lemma on Frobenius elements, there are $\sigma_u, \sigma_1 \in G$ of degree $1$ such that $\sigma_u$ acts on $F_f[\pi^n]$ by $[u^{-1}]_f$ and $\sigma_1$ acts trivially. So $\sigma_1 \in G_{L_n}$. Put $\rho = (\sigma_u \sigma_1^{k-1})^{-1} \tau$. Then $\rho$ fixes $L_n$: on $F_f[\pi^n]$ the element $\sigma_1^{k-1}$ acts trivially, and $\tau$ and $\sigma_u$ act in the same way. Also $d(\rho) = k - 1 - (k - 1) = 0$. So $\rho \in G_{L_n} \cap \ker d \leq U$, and
$$\tau U = \sigma_u \sigma_1^{k-1} U.$$
Apply the theorem on Frobenius elements to $\sigma_u$ with $w = u$, and to $\sigma_1$ with $w = 1$. Since $r_U$ is a homomorphism,
$$r_U(\tau U) = r_U(\sigma_u U)\, r_U(\sigma_1 U)^{k-1} = u\pi \cdot \pi^{k-1} = u\pi^k$$
modulo norms. $\square$

**Remark 1.2.5.** In the classical form, the theorem says: for the local Artin map $\operatorname{Art}_K$ in the arithmetic normalization, $\operatorname{Art}_K(u\pi^k)$ acts on $L_n$ by $[u^{-1}]_f$ and on $K^{\mathrm{nr}}$ as the $k$-th power of the Frobenius. The statement here is the inverse direction: it computes the map $G/U \to K^\times/N$ of abstract class field theory, on each finite layer $\Omega^U$ of $L_n K^{\mathrm{nr}}$ that contains $L_n$. Taking $U = G_{L_n K_s}$ as in the Example gives the law on the finite abelian extensions $L_n K_s$.

**Remark 1.2.6 (Formalization).** Both theorems ask for $U$ to be normal as a subgroup of the open subgroup $G$ of $G$, an instance argument, and both need a raised heartbeat limit ([LubinTateReciprocity.lean](lean:GroundTheory/LocalFields/LubinTateReciprocity.lean#L159)). The value in $K^\times/N$ is written through an identification of the $G$-invariants of $\Omega^\times$ with $K^\times$ (`GroundTheory.LocalField.baseUnitsEquiv`) and the element $u\pi^k$ is `GroundTheory.LocalField.unitUniformizerPow`. Step 1 of the first proof is `GroundTheory.LocalField.apply_root_eq_psEval`, and Step 4 uses `GroundTheory.LocalField.norm_neg_gen_eq_coeff_zero`.
