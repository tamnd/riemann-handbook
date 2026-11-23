---
title: Period matrices over A_cris
decls:
  - GlobalTheory.SstPer.sst_periods
  - GlobalTheory.T.exists_semistable_lattice_periods_acris
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Period matrices over $A_{\mathrm{cris}}$

Let $\rho : G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ be a homomorphism such that $V = \mathbb{Q}_\ell^d$ is semistable. This section writes the comparison between $V$ and $D_{\mathrm{st}}(V)$ as a pair of matrices $Z, Z'$ over $A_{\mathrm{cris}}$ with $ZZ' = t^{2N}$. The Frobenius acts on $Z$ through a matrix over $W$, the group $G_K$ acts through an explicit cocycle $\kappa$ built from the monodromy, and $Z$ is matched with a matrix $X$ over $\mathfrak{S}$ modulo a power of the filtration. These are the data from which [the next section](/entry/semistable-period-frame/) builds a lattice over $\mathfrak{S}$. The main input is [the logarithm of a power of $[\pi^\flat]$](/entry/exists-log-flat-pow-bst/). We keep the notation of the previous section and fix a Breuil-Kisin datum for $K$. We write $\iota_{\mathrm{cris}} : B_{\mathrm{cris}} \to B_{\mathrm{dR}}$ for the natural map. A matrix over $W$ or $\mathfrak{S}$ is viewed over $A_{\mathrm{inf}}$, $A_{\mathrm{cris}}$, $B_{\mathrm{dR}}^+$ or $B_{\mathrm{dR}}$ through $\mathrm{ev}$, $\iota$ and the natural maps, a matrix over $B_{\mathrm{cris}}$ is viewed over $B_{\mathrm{dR}}$ through $\iota_{\mathrm{cris}}$, and $G_K$ and $\varphi$ act on matrices entrywise.

**Definition 3.2.1 (de Rham and Hodge-Tate jumps).** Let $V$ be a representation of $G_K$ on a finite-dimensional $L$-vector space. Put $D_{\mathrm{dR}}(V) = (V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{dR}})^{G_K}$, and for $a \in \mathbb{Z}$ let $\mathrm{Fil}^a(V) = V \otimes_{\mathbb{Q}_\ell} \mathrm{Fil}^a B_{\mathrm{dR}}$ inside $V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{dR}}$. For an embedding $\tau : K \to L$, let $D_{\mathrm{dR},\tau}(V)$ be the subspace of $D_{\mathrm{dR}}(V)$ where $K$ acts through $\tau$. The *multiplicity* of $a$ at $\tau$ is
$$m_\tau(V, a) = \dim_L \big(D_{\mathrm{dR},\tau}(V) \cap \mathrm{Fil}^a(V)\big) - \dim_L \big(D_{\mathrm{dR},\tau}(V) \cap \mathrm{Fil}^{a+1}(V)\big).$$
The integers $a$ with $m_\tau(V, a) > 0$ are the *Hodge-Tate jumps* of $V$ at $\tau$. The representation is *de Rham* if $\dim_L D_{\mathrm{dR}}(V) = [K : \mathbb{Q}_\ell] \dim_L V$, and *crystalline* if the same holds with $B_{\mathrm{cris}}$ and $K_0$ in place of $B_{\mathrm{dR}}$ and $K$.

These are the notions of [the Background](/learn/galois-representations/#crystalline-de-rham-and-potentially-semistable-representations). With these conventions $\mathbb{Q}_\ell(1)$ has the jump $-1$.

**Theorem 3.2.2 (Period matrices of a semistable lattice).** Let $\rho : G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ be a homomorphism such that $V = \mathbb{Q}_\ell^d$, with $G_K$ acting through $\rho$, is semistable. Then there are integers $N, c_1, c_2, c_3, k_0 \geq 0$, matrices $F, F' \in M_d(W)$, $X, X' \in M_d(\mathfrak{S})$, $Z, Z' \in M_d(A_{\mathrm{cris}})$ and a map $\kappa : G_K \to M_d(A_{\mathrm{cris}})$ with the following properties.

1. $FF' = \ell^{c_3}$, $XX' = \ell^{c_2} E^{2N}$ and $ZZ' = t^{2N}$.
2. $t^N \ell^{c_1} \varphi(Z) = \varphi(t)^N Z F$.
3. $t^N \ell^{k_0} \rho(g) \, g(Z) = g(t)^N Z \kappa(g)$ for all $g \in G_K$.
4. $\kappa(g) = \ell^{k_0}$ for all $g \in G_\infty$.
5. The entries of $j(ZX)$ and of $j(X'Z')$ lie in $\mathrm{Fil}^{2N} B_{\mathrm{dR}}^+$.
6. For each $m \geq 0$ there are $k \geq 0$ and $\Lambda \in M_d(\mathfrak{S})$ with $\Lambda \equiv \ell^k \pmod{E}$ entrywise, such that the entries of $j\big(\kappa(g) \, g(\Lambda) - \ell^{k_0} \Lambda\big)$ lie in $\mathrm{Fil}^m B_{\mathrm{dR}}^+$ for all $g \in G_K$.

Lean: `GlobalTheory.SstPer.sst_periods` (also `GlobalTheory.T.exists_semistable_lattice_periods_acris`, a second name).

In 1, a scalar stands for the scalar matrix. Read 2 and 3 as follows. The columns of $Z$, divided by $t^N$, are $d$ vectors of $V \otimes A_{\mathrm{cris}}[1/t]$. Up to the factors $\ell^{c_1}$ and $\ell^{k_0}$, Frobenius acts on them by the matrix $F$ over $W$ and $g$ acts by $\kappa(g)$. Property 5 says that $X$ moves these vectors into the lattice $V \otimes \mathrm{Fil}^{2N} B_{\mathrm{dR}}^+$, up to the twist by $t^N$. Property 6 says that $\kappa$ is a coboundary modulo each $\mathrm{Fil}^m$, after scaling by powers of $\ell$.

The proof assembles six results. The first two are general facts about semistable and de Rham representations.

**Lemma 3.2.3 (Semistable implies de Rham).** A semistable representation of $G_K$ on a finite-dimensional $\mathbb{Q}_\ell$-vector space is de Rham.

Lean: `GlobalTheory.sst_isDR`.

**Definition 3.2.4 (Hodge basis).** Let $\xi \in A_{\mathrm{inf}}$ and let $\rho : G_K \to M_a(\Omega)$ be a map, where $\Omega$ is viewed inside $B_{\mathrm{dR}}^+$. A *Hodge basis* of $\rho$ over a finite extension $K' \supseteq K$ is a matrix $V_H \in \mathrm{GL}_a(B_{\mathrm{dR}}^+)$, integers $p_1, \dots, p_a, q \geq 0$, and the matrix $Q \in M_a(B_{\mathrm{dR}})$ with $\xi^q Q_{ij} = \xi^{p_j} (V_H)_{ij}$ for all $i, j$, such that $\rho(g) \, g(Q) = Q$ for all $g \in G_K \cap G_{K'}$.

If $\xi$ generates $\ker \theta$, then $\xi$ is a unit of $B_{\mathrm{dR}}$ and the $j$-th column of $Q$ is $\xi^{p_j - q}$ times the $j$-th column of $V_H$. So the columns of $Q$ are Galois invariant vectors, and the $j$-th column lies exactly in filtration degree $p_j - q$. The integers $p_j - q$ are the jumps of the basis.

**Lemma 3.2.5 (Hodge basis of a de Rham lattice).** Let $\xi \in A_{\mathrm{inf}}$ generate $\ker \theta$, and let $\rho : G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ be a homomorphism with $V = \mathbb{Q}_\ell^d$ de Rham. There is a Hodge basis of $\rho$ for $\xi$ over $K$ such that, for each $N \geq 0$ with $D_{\mathrm{dR}}(V) \subseteq \mathrm{Fil}^{-N}(V)$ and $D_{\mathrm{dR}}(V) \cap \mathrm{Fil}^{N+1}(V) = 0$, we have $|p_i - q| \leq N$ for all $i$.

Lean: `GlobalTheory.T.exists_hodge_basis_deRham_lattice`.

The next four lemmas carry out the comparison. Let $b$ and $c$ be as in [the theorem on the logarithm](/entry/exists-log-flat-pow-bst/).

**Lemma 3.2.6 (Period matrix at log zero).** Let $\rho$ be as in the theorem, and let $b \in B_{\mathrm{cris}}$ and $c : G_K \to \mathbb{Z}_\ell$ satisfy $g(X + b) = X + b + c(g) t$ in $B_{\mathrm{st}}$ for all $g \in G_K$ and $\varphi(X + b) = \ell(X + b)$. There are $U, U' \in M_d(B_{\mathrm{cris}})$ with $UU' = 1$, integers $c_1, c_3, k \geq 0$, and $F, F', M \in M_d(W)$ with $FF' = \ell^{c_3}$, $\ell^{c_1} \varphi(U) = UF$, $M^d = 0$ and
$$\rho(g) \, g(U) = U \sum_{i=0}^{d-1} \frac{(c(g) t)^i}{i! \, \ell^{k i}} M^i \quad \text{for all } g \in G_K.$$

Lean: `GlobalTheory.T.semistable_periodMatrix_at_log_zero`.

Since $M^d = 0$, the sum is $\exp(c(g) t M / \ell^k)$. The name says what one does: a basis of $D_{\mathrm{st}}(V)$ is a polynomial in $X$ with coefficients in $B_{\mathrm{cris}}$, and one evaluates it where the logarithm $X + b$ vanishes. The monodromy then appears in the exponential.

**Lemma 3.2.7 (A logarithm in $B_{\mathrm{dR}}^+$).** Let $b$ and $c$ have the three properties of [the theorem on the logarithm](/entry/exists-log-flat-pow-bst/). There is $\lambda \in B_{\mathrm{dR}}^+$ with $g(\lambda) = \lambda + c(g) \, j(t)$ for all $g \in G_K$, such that for each $m$ there are $k$ and $s \in \mathfrak{S}$ with $E \mid s$ and $\iota(\mathrm{ev}(s)) - \ell^k \lambda \in \mathrm{Fil}^m B_{\mathrm{dR}}^+$.

Lean: `GlobalTheory.T.exists_log_uniformizerTilt_bdRPlus_cocycle`.

**Lemma 3.2.8 (Invariant basis over $B_{\mathrm{dR}}^+$).** Let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ be a map, $c : G_K \to \mathbb{Z}_\ell$, $U \in M_d(B_{\mathrm{cris}})$, $k \geq 0$ and $M \in M_d(W)$ with $M^d = 0$ and with the formula for $\rho(g) g(U)$ of the last but one lemma. Let $\lambda$ have the two properties of the last lemma. There is $\Lambda_0 \in M_d(B_{\mathrm{dR}}^+)$ such that $\rho(g) \, g(U \Lambda_0) = U \Lambda_0$ in $M_d(B_{\mathrm{dR}})$ for all $g \in G_K$, and for each $m$ there are $k'$ and $\Lambda, \Lambda' \in M_d(\mathfrak{S})$ with $\Lambda \Lambda' = \ell^{2k'}$ and $\iota(\mathrm{ev}(\Lambda)) - \ell^{k'} \Lambda_0 \in M_d(\mathrm{Fil}^m B_{\mathrm{dR}}^+)$.

Lean: `GlobalTheory.T.semistable_invariant_bdRPlus_basis_approx`.

Here one should think of $\Lambda_0$ as $\exp(-\lambda M/\ell^k)$, which cancels the exponential in $\rho(g) g(U)$.

**Lemma 3.2.9 (Integral coefficients of the exponential).** Write $d! = \ell^{e'} m'$ with $\ell \nmid m'$, let $k \geq 0$ and put $k_0 = e' + k d$. Then $\ell^{k_0} / (i! \, \ell^{k i}) \in \mathbb{Z}_\ell$ for $0 \leq i < d$.

Lean: `GlobalTheory.SstPer.ecoefQ_norm_le`.

*Proof.* For $i < d$ the $\ell$-adic valuation of $i! \, \ell^{ki}$ is $v_\ell(i!) + ki \leq v_\ell(d!) + kd = k_0$. $\square$

With $k_0$ as in this lemma, define
$$\kappa(g) = \sum_{i=0}^{d-1} \frac{\ell^{k_0}}{i! \, \ell^{k i}} \, (c(g) t)^i M^i \in M_d(A_{\mathrm{cris}}).$$
This is $\ell^{k_0} \exp(c(g) t M/\ell^k)$, and its coefficients are integral by the lemma. So $\kappa$ takes values in $A_{\mathrm{cris}}$, not only in $B_{\mathrm{cris}}$.

**Lemma 3.2.10 (Periods over $A_{\mathrm{cris}}$).** Let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ be a map, and let $U, U'$, $c_1$, $F$, $k$, $M$, $c$ satisfy $UU' = 1$, $\ell^{c_1} \varphi(U) = UF$ and the formula for $\rho(g) g(U)$ in the lemma on the period matrix at log zero. Let $k_0$ be such that $\ell^{k_0}/(i!\,\ell^{ki}) \in \mathbb{Z}_\ell$ for $i < d$, and define $\kappa$ as above. There is $N_0$ such that for all $N \geq N_0$ and all $X, X' \in M_d(\mathfrak{S})$ for which the entries of $U X$ and of $X' U'$ lie in $\mathrm{Fil}^N B_{\mathrm{dR}}$, there are $Z, Z' \in M_d(A_{\mathrm{cris}})$ with $ZZ' = t^{2N}$ that satisfy properties 2, 3 and 5 of the theorem.

Lean: `GlobalTheory.T.semistable_periods_over_Acris`.

**Lemma 3.2.11 (Modification at $E$).** Assume that $B_{\mathrm{dR}}^{G_{K'}} = K'$ for every finite extension $K'$ of $\mathbb{Q}_\ell$ in $\Omega$. Let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ be a map with a Hodge basis for $\xi = \mathrm{ev}(E)$ over $K$. Let $U, U' \in M_d(B_{\mathrm{dR}})$ with $UU' = 1$, and let $\Lambda_0 \in M_d(B_{\mathrm{dR}}^+)$ have the two properties in the conclusion of the lemma on the invariant basis (with $U$ in place of $\iota_{\mathrm{cris}}(U)$). For each $N_0$ there are $N \geq N_0$, $c_2 \geq 0$ and $X, X' \in M_d(\mathfrak{S})$ with $XX' = \ell^{c_2} E^{2N}$ such that the entries of $U X$ and of $X' U'$ lie in $\mathrm{Fil}^N B_{\mathrm{dR}}$.

Lean: `GlobalTheory.T.exists_twisted_modification_at_E`.

**Lemma 3.2.12 (The cocycle is a coboundary modulo the filtration).** Let $k$, $k_0$, $M$ and $\kappa$ be as in the lemma on periods over $A_{\mathrm{cris}}$, with $M^d = 0$, and let $c$ have property 3 of [the theorem on the logarithm](/entry/exists-log-flat-pow-bst/). Then property 6 of the theorem holds for $\kappa$.

Lean: `GlobalTheory.T.semistable_exp_cocycle_coboundary_mod_fil`.

*Proof of the theorem.* By the lemma that semistable implies de Rham, $V$ is de Rham. By item 6 of the Breuil-Kisin datum, $\mathrm{ev}(E)$ generates $\ker \theta$, so the lemma on Hodge bases gives a Hodge basis of $\rho$ for $\xi = \mathrm{ev}(E)$ over $K$. The theorem on [the logarithm of a power of $[\pi^\flat]$](/entry/exists-log-flat-pow-bst/) gives $b \in B_{\mathrm{cris}}$ and $c : G_K \to \mathbb{Z}_\ell$ with its three properties.

The lemma on the period matrix at log zero, applied to $b$ and $c$, gives $U$, $U'$, $F$, $F'$, $M$, $c_1$, $c_3$ and $k$. The lemma on a logarithm in $B_{\mathrm{dR}}^+$ gives $\lambda$, and then the lemma on the invariant basis gives $\Lambda_0$. Write $d! = \ell^{e'} m'$ with $\ell \nmid m'$ and put $k_0 = e' + kd$. By the integrality lemma, $\kappa$ is defined. The lemma on periods over $A_{\mathrm{cris}}$ gives $N_0$. By Fontaine's theorem, $B_{\mathrm{dR}}^{G_{K'}} = K'$ for every finite extension $K'$ of $\mathbb{Q}_\ell$. So the lemma on modification at $E$ applies to $\iota_{\mathrm{cris}}(U)$, $\iota_{\mathrm{cris}}(U')$ and $\Lambda_0$, whose product is $1$ because $UU' = 1$. It gives $N \geq N_0$, $c_2$, $X$ and $X'$ with $XX' = \ell^{c_2} E^{2N}$ and with $UX$ and $X'U'$ in $\mathrm{Fil}^N$. Then the lemma on periods over $A_{\mathrm{cris}}$, applied to $N$, $X$ and $X'$, gives $Z$ and $Z'$ with $ZZ' = t^{2N}$ and properties 2, 3 and 5.

For 4, let $g \in G_\infty$. Then $c(g) = 0$ by property 2 of the logarithm, so only the term $i = 0$ of $\kappa(g)$ remains, and it is $\ell^{k_0}$. Property 6 is the lemma on the coboundary modulo the filtration, applied with property 3 of the logarithm. $\square$

**Remark 3.2.13 (Formalization).** The theorem has no continuity hypothesis on $\rho$; $\rho$ is any homomorphism. The seven input lemmas of the proof (`semistable_periodMatrix_at_log_zero`, `exists_log_uniformizerTilt_bdRPlus_cocycle`, `semistable_invariant_bdRPlus_basis_approx`, `semistable_periods_over_Acris`, `exists_twisted_modification_at_E`, `semistable_exp_cocycle_coboundary_mod_fil`, `exists_hodge_basis_deRham_lattice`) are not unfolded in this chapter, and the readings of $U$ and $\Lambda_0$ as "evaluation at log zero" and "$\exp(-\lambda M/\ell^k)$" are ours. The matrix $\kappa$ is the function `SstPer.kap`; it uses the coefficient $\ell^{k_0}/(i!\,\ell^{ki})$ when its norm is at most $1$ and $0$ otherwise, and the integrality lemma shows that the first case always holds for $i < d$. Semistability is measured with the abstract period data and the ring $B_{\mathrm{st}}$ of the previous section, while $Z$ and $\kappa$ live in the concrete ring $A_{\mathrm{cris}}$; the two are matched by the datum `Fits`. Fontaine's theorem $B_{\mathrm{dR}}^{G_{K'}} = K'$ is not proved: it is the field `invdR` of `Fits`, read off by `MemLoc.fits_inv`. The lemmas on the invariant basis, on periods over $A_{\mathrm{cris}}$ and on modification at $E$ take $\rho$ as an arbitrary map to $M_d(\mathbb{Z}_\ell)$. The Hodge basis lemma is applied here only to get the basis; its bound on the jumps is used in [the main theorem](/entry/exists-frame-sst/).
