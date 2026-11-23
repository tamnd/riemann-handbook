---
title: Limits of towers of frames
decls:
  - GlobalTheory.BKLim.limit_pre_exists
  - GlobalTheory.T.exists_breuilKisin_basis_limit_lattice
  - GlobalTheory.BKLim.limit_frame_exists
  - GlobalTheory.T.exists_deRhamFrame_limitLattice_breuilKisinTower
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Limits of towers of frames

Let $\rho : G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ be a homomorphism that is approximated modulo $\ell^n$, for each $n$, by a quotient of another lattice $\rho'_n$. If every $\rho'_n$ has a frame of one fixed height $N$, then so does $\rho$. This section proves this, first for Breuil-Kisin bases and then for de Rham frames, and it shows that the frame of $\rho$ is crystalline when all frames of the layers are. The point is that $N$ does not grow along the tower: this is why [the theorem on frames of bounded height](/entry/exists-frame-sst/) asks for a height that depends only on the Hodge-Tate jumps. The result is applied in [the theorem on covers](/entry/closed-of-cover/) of the next section, and it is one of the inputs of [the theorem on the core of the Galois row](/entry/core-all-of/). We keep the Breuil-Kisin datum, a Frobenius period $\tau$, and the notions of [Breuil-Kisin basis and frame](/entry/semistable-period-frame/).

**Definition 3.5.1 (The ring $\mathcal{O}_{\mathcal{E}}$).** Let $\mathcal{O}_{\mathcal{E}} \subset W(C^\flat)$ be the set of $w$ such that for each $n \geq 0$ there are $m \geq 0$, $s \in \mathfrak{S}$ and $y \in W(C^\flat)$ with $[\pi^\flat]^m w = \mathrm{ev}(s) + \ell^n y$.

So $w \in \mathcal{O}_{\mathcal{E}}$ when $w$ modulo each $\ell^n$ lies in the image of $(\mathfrak{S}/\ell^n)[1/X]$. This is the $\ell$-adic completion of $\mathfrak{S}[1/X]$ inside $W(C^\flat)$, the ring of Fontaine's theory of étale $\varphi$-modules: a $\mathbb{Z}_\ell$-representation of $G_\infty$ corresponds to a module over $\mathcal{O}_{\mathcal{E}}$ with a Frobenius whose matrix is invertible. It is a subring of $W(C^\flat)$ and contains the image of $\mathfrak{S}$.

**Definition 3.5.2 (Tower and links).** Let $\Gamma$ be a group and $\rho : \Gamma \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ a homomorphism. A *tower* for $\rho$ consists of, for each $n \geq 0$, an integer $d'_n$, a homomorphism $\rho'_n : \Gamma \to \mathrm{GL}_{d'_n}(\mathbb{Z}_\ell)$ and matrices $\Pi_n \in M_{d \times d'_n}(\mathbb{Z}_\ell)$ and $f_n \in M_{d'_n \times d'_{n+1}}(\mathbb{Z}_\ell)$, such that:

1. $\Pi_n \rho'_n(g) \equiv \rho(g) \Pi_n \pmod{\ell^n}$ for all $g$, and $\Pi_n S \equiv 1 \pmod{\ell^n}$ for some $S \in M_{d'_n \times d}(\mathbb{Z}_\ell)$;
2. $f_n \rho'_{n+1}(g) = \rho'_n(g) f_n$ for all $g$, and $\Pi_n f_n \equiv \Pi_{n+1} \pmod{\ell^n}$.

Let $T \in M_d(W(C^\flat))$, $T' \in M_{d'}(W(C^\flat))$, $\Pi \in M_{d \times d'}(\mathbb{Z}_\ell)$ and $n, r \geq 0$. We say that $T$ is *linked* to $T'$ through $\Pi$ modulo $\ell^n$ with defect $r$ if there are $R \in M_{d \times d'}(\mathfrak{S})$ and $G \in M_{d' \times d}(\mathfrak{S})$ with
$$\Pi T' \equiv T R \pmod{\ell^n W(C^\flat)}, \qquad RG \equiv \ell^r \pmod{\ell^n \mathfrak{S}}.$$

Read $\Pi_n$ as a map from $\mathbb{Z}_\ell^{d'_n}$ to $\mathbb{Z}_\ell^d$. Condition 1 says that it is equivariant and onto modulo $\ell^n$, so $\rho \bmod \ell^n$ is a quotient of $\rho'_n \bmod \ell^n$. Condition 2 says that the layers map to each other compatibly. A link says that, modulo $\ell^n$, the image under $\Pi$ of the vectors $T'$ lies in the $\mathfrak{S}$-span of the columns of $T$, and that it fills this span up to the factor $\ell^r$.

**Theorem 3.5.3 (Limit of Breuil-Kisin bases).** Let $\tau$ be a Frobenius period, $N \geq 0$, $\rho : G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ a homomorphism with a tower $(\rho'_n, \Pi_n, f_n)$, and for each $n$ let $T_n$ be a Breuil-Kisin basis of height $N$ for $\rho'_n$. Then there are a Breuil-Kisin basis $T$ of height $N$ for $\rho$ and an integer $r \geq 0$ such that for every $n$ there is $m \geq n$ for which $T$ is linked to $T_m$ through $\Pi_m$ modulo $\ell^n$ with defect $r$.

Lean: `GlobalTheory.BKLim.limit_pre_exists` (also `GlobalTheory.T.exists_breuilKisin_basis_limit_lattice`, a second name).

The proof has three stages. First we pass to the limit over $\mathcal{O}_{\mathcal{E}}$, where Frobenius is invertible. Then we cut out an $\mathfrak{S}$-lattice by an integrality condition over $A_{\mathrm{inf}}$, twisted by $\tau^N$. Last we compare the lattice with the layers.

**Lemma 3.5.4 (Étale limit).** In the situation of the theorem, there are $T_0 \in \mathrm{GL}_d(W(C^\flat))$ and, for each $n$, matrices $R_n \in M_{d \times d'_n}(\mathcal{O}_{\mathcal{E}})$ and $R'_n \in M_{d'_n \times d}(\mathcal{O}_{\mathcal{E}})$ with $\Pi_n T_n \equiv T_0 R_n$ and $R_n R'_n \equiv 1$ modulo $\ell^n$.

Lean: `GlobalTheory.T.exists_etale_basis_limit_lattice_tower`.

**Lemma 3.5.5 (The étale limit is invariant).** Let $T_0$ be as in the last lemma. Then $\rho(g) \, g(T_0) = T_0$ for $g \in G_\infty$, and $\varphi(T_0) = T_0 A_0$ for some $A_0 \in \mathrm{GL}_d(\mathcal{O}_{\mathcal{E}})$.

Lean: `GlobalTheory.T.limit_breuilKisin_basis_invariant_etale`.

So the columns of $T_0$ span the étale $\varphi$-module over $\mathcal{O}_{\mathcal{E}}$ of the restriction of $\rho$ to $G_\infty$.

**Lemma 3.5.6 (The integral lattice).** Let $T_0 \in \mathrm{GL}_d(W(C^\flat))$ and $V \in \mathrm{GL}_d(\mathcal{O}_{\mathcal{E}})$, and assume that $\tau^N T_0 V$ has entries in $A_{\mathrm{inf}}$. Then there are $Y \in M_d(A_{\mathrm{inf}})$, invertible in $M_d(W(C^\flat))$, and $W_0 \in \mathrm{GL}_d(\mathcal{O}_{\mathcal{E}})$ with $Y = \tau^N T_0 W_0$, such that every $y \in A_{\mathrm{inf}}^d$ of the form $\tau^N T_0 w$ with $w \in \mathcal{O}_{\mathcal{E}}^d$ is $Y \mathrm{ev}(c)$ for some $c \in \mathfrak{S}^d$.

Lean: `GlobalTheory.T.saturatedAinfLattice_free_over_breuilKisin`.

In words: the vectors of the étale module $T_0 \mathcal{O}_{\mathcal{E}}^d$ that become integral over $A_{\mathrm{inf}}$ after multiplication by $\tau^N$ form a free $\mathfrak{S}$-module of rank $d$, with basis $W_0$. This is the analogue of Kisin's construction of a Breuil-Kisin module inside an étale $\varphi$-module.

**Lemma 3.5.7 (Breuil-Kisin basis from an étale basis).** Let $\rho : G_K \to M_d(\mathbb{Z}_\ell)$ be a map and $T \in \mathrm{GL}_d(W(C^\flat))$ with $\varphi(T) = TA$ for some $A \in \mathrm{GL}_d(\mathcal{O}_{\mathcal{E}})$ and $\rho(g) \, g(T) = T$ for $g \in G_\infty$. Assume that $Y = \tau^N T$ has entries in $A_{\mathrm{inf}}$ and that $YY' = \tau^{2N}$ for some $Y' \in M_d(A_{\mathrm{inf}})$. Then $T$ is a Breuil-Kisin basis of height $N$ for $\rho$.

Lean: `GlobalTheory.T.breuilKisin_basis_of_etale_invariant_bounded_poles`.

The reason is the relation $\varphi(\tau) = E\tau$: from $\varphi(Y) = \varphi(\tau)^N \varphi(T) = E^N \tau^N T A = E^N Y A$, we get $Y^{-1} \varphi(Y) = E^N A$. So the matrix of $E^N \varphi$ in the basis $T$ is $Y^{-1} \varphi(Y) = \tau^{-2N} Y' \varphi(Y)$, and the content of the lemma is that this matrix, and $E^N A^{-1}$, have entries in $\mathfrak{S}$.

**Lemma 3.5.8 (Right inverses).** For each $M \geq 0$ there is $r \geq 0$ with the following property. Let $R \in M_{d \times d'}(\mathfrak{S})$, $a \in M_{d' \times d}(A_{\mathrm{inf}})$ and $n \geq 0$ with $\mathrm{ev}(R) \, a \equiv \tau^M \pmod{\ell^n}$. Then there is $G \in M_{d' \times d}(\mathfrak{S})$ with $RG \equiv \ell^r \pmod{\ell^n}$.

Lean: `GlobalTheory.T.exists_right_inverse_mod_pow_of_ev`.

*Proof of the theorem.* The lemma on the étale limit gives $T_0$, $R_n$ and $R'_n$, and the next lemma shows that $T_0$ is $G_\infty$-invariant with $\varphi(T_0) = T_0 A_0$, $A_0 \in \mathrm{GL}_d(\mathcal{O}_{\mathcal{E}})$. Consider the images $R_m \mathrm{ev}(\mathfrak{S}^{d'_m})$ modulo $\ell^n$. The transition matrices $f_m$ of the tower relate them for different $m$, and these images satisfy the Mittag-Leffler condition: for each $n$ there is $m \geq n$ such that every element of the image at level $m$ lifts, modulo $\ell^n$, to a vector $v$ that lies in the images at all levels $k$ modulo $\ell^k$. Every such limit vector $v$ lies in $\mathcal{O}_{\mathcal{E}}^d$, and $\tau^N T_0 v$ lies in $A_{\mathrm{inf}}^d$. The limit vectors contain a basis $V \in \mathrm{GL}_d(\mathcal{O}_{\mathcal{E}})$. The lemma on the integral lattice, applied to $T_0$ and $V$, gives $Y$ and $W_0$. Put $T = T_0 W_0$. Comparing the integral lattice with the layers gives, for each $n$, some $m \geq n$ and $R \in M_{d \times d'_m}(\mathfrak{S})$, $Q \in M_{d'_m \times d}(A_{\mathrm{inf}})$ with
$$\Pi_m T_m \equiv T R, \qquad Y \, \mathrm{ev}(R) \, Q \equiv \tau^{2N} \pmod{\ell^n}.$$
Since this holds for every $n$ and $Y$ is invertible over $W(C^\flat)$, there is $Y' \in M_d(A_{\mathrm{inf}})$ with $YY' = \tau^{2N}$. Since $W_0$ is a unit over $\mathcal{O}_{\mathcal{E}}$, $T$ is again $G_\infty$-invariant with $\varphi(T) = TA_1$ for some $A_1 \in \mathrm{GL}_d(\mathcal{O}_{\mathcal{E}})$. The lemma on Breuil-Kisin bases from étale bases now shows that $T$ is a Breuil-Kisin basis of height $N$ for $\rho$.

For the links, let $r$ be given by the lemma on right inverses for $M = 2N$. Fix $n$, and take $m$, $R$ and $Q$ as above. The element $\tau$ is nonzero and a unit in $W(C^\flat)$, so from $Y \mathrm{ev}(R) Q \equiv \tau^{2N}$ and $YY' = \tau^{2N}$ we get $\mathrm{ev}(R) \, QY \equiv \tau^{2N} \pmod{\ell^n}$. The lemma on right inverses gives $G$ with $RG \equiv \ell^r \pmod{\ell^n}$. Together with $\Pi_m T_m \equiv TR$, this is the link. $\square$

Next we add the Galois action on all of $G_K$.

**Theorem 3.5.9 (Limit of de Rham frames).** Let $\tau$, $N$, $\rho$ and the tower be as in the last theorem. For each $n$ let $F_n$ be a de Rham frame of height $N$ for $\rho'_n$, with basis $T_n$. Then there are a de Rham frame $F$ of height $N$ for $\rho$, with basis $T$, and $r \geq 0$ such that $F$ is crystalline if every $F_n$ is crystalline, and for every $n$ there is $m \geq n$ for which $T$ is linked to $T_m$ through $\Pi_m$ modulo $\ell^n$ with defect $r$.

Lean: `GlobalTheory.BKLim.limit_frame_exists` (also `GlobalTheory.T.exists_deRhamFrame_limitLattice_breuilKisinTower`, a second name).

Fix $T$ and $r$, and assume that for every $n$ there is $m \geq n$ for which $T$ is linked to $T_m$ through $\Pi_m$ modulo $\ell^n$ with defect $r$. The following three lemmas use only these links.

**Lemma 3.5.10 (Frames from links).** If $T$ is a Breuil-Kisin basis of height $N$ for $\rho$ linked to the frames $F_n$ in this way, then $T$ extends to a frame of height $N$ for $\rho$.

Lean: `GlobalTheory.T.exists_breuilKisinLatticeFrame_of_linked_preframe`.

**Lemma 3.5.11 (De Rham through links).** If $F$ is a frame of height $N$ for $\rho$ whose basis is linked to the frames $F_n$ in this way, and every $F_n$ is de Rham, then $F$ is de Rham.

Lean: `GlobalTheory.T.isDR_of_links'`.

**Lemma 3.5.12 (Crystalline through links).** If $F$ is as in the last lemma and every $F_n$ is crystalline, then $F$ is crystalline.

Lean: `GlobalTheory.T.breuilKisinFrame_isCr_of_linked_tower`.

*Proof of the theorem.* The theorem on limits of Breuil-Kisin bases, applied to the bases of the $F_n$, gives $T$ and $r$ with the links. The lemma on frames from links extends $T$ to a frame $F$ with the same basis, so the links still hold. The last two lemmas show that $F$ is de Rham, and crystalline if every $F_n$ is. $\square$

**Remark 3.5.13 (Formalization).** The Frobenius period $\tau$ is a hypothesis of both theorems, but in the proof of the second it is only passed to the first; the three lemmas on links do not take it. A tower is the structure `BKLim.Tower`, the condition of 1 is `BKLim.Onto`, a link is `BKLim.Link`, and $\mathcal{O}_{\mathcal{E}}$ is `BK.OE`. The Mittag-Leffler step of the proof uses five lemmas that we have not opened beyond their statements (`approximatingLattices_transitionMatrix_modPow`, `latticeApproximation_mittagLeffler`, `mittagLeffler_image_breuilKisin_modPow`, `limitVector_mem_OE_and_ainf`, `limitVectors_invertible_basis_over_OE`); the comparison with the layers is `twisted_matrix_congruence_lift_sequence`, the matrix $Y'$ comes from `ainf_exists_mul_eq_pow_smul_of_mod_lPow`, the change of basis by $W_0$ from `invariantEtaleBasis_change_by_OE_unit`, and the step from $Y\mathrm{ev}(R)Q$ to $\mathrm{ev}(R)QY$ from `ainf_rightInverse_up_to_pow_mod_lPow` and `breuilKisin_period_isUnit_wittTilt_and_ne_zero`. None of the lemmas of this section is unfolded. The identification of $\mathcal{O}_{\mathcal{E}}$ with Fontaine's ring, the reading of the integral lattice as Kisin's construction, and the explanation after the lemma on Breuil-Kisin bases from étale bases are ours. In the theorem on limits of Breuil-Kisin bases the frames of the layers play no role; only their bases are used. The second names have the same types as the theorems and are proved by applying them.
