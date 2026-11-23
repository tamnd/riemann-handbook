---
title: The exact sequence for Φ of τ × σ
decls:
  - GlobalTheory.CompanionTheory.BZPhiPG.phiPG
  - GlobalTheory.CompanionTheory.BZPhiPG.phiPG_core
  - GlobalTheory.T.open_evaluation_induced
  - GlobalTheory.CompanionTheory.BZPhiPG.MemO.eO_mem
  - GlobalTheory.CompanionTheory.BZPhiPG.MemO.memOAlt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The exact sequence for Φ of τ × σ

When $\tau$ lives on a mirabolic group of positive rank, $\Phi(\tau \times \sigma)$ is no longer a single product but an extension of two. This section proves that $\Phi(\tau \times \sigma)$ has a subrepresentation isomorphic to $\Phi\tau \times \sigma$ with quotient $\Psi\tau \times \sigma|_P$. It is one of the six inputs to the Leibniz rule, [Theorem 7.5.2](/entry/leibniz-ord/), next to the rank zero case of the previous sections. The proof cuts the mirabolic group into a closed set and its open complement: functions on the closed set give the quotient, and functions on the open set give the subrepresentation. The part of the cell argument proved in this section is the statement that the open evaluation map lands in $\Phi\tau \times \sigma$.

We keep the notation of the earlier sections: $G_n$, $P_n$, $U_n$, $u(y)$, $\theta_\psi$, $\Phi$, $\Psi$, compact induction, $Q_{m,l}$, $H_{n,t}$ and the products $\rho \times \tau$ and $\tau \times \sigma$. Throughout, $n \geq 2$, $s \geq 1$, $\tau$ is a smooth representation of $P_n$ on $V$, $\sigma$ is a smooth representation of $G_s$ on $W$, and $\psi$ is a continuous character of $k$. Write $\iota : P_{N-1} \to P_N$ for $m \mapsto \mathrm{diag}(m,1)$.

**Theorem 1.8.1 (Bernstein and Zelevinsky).** Let $\psi \neq 1$. There is an exact sequence of representations of $P_{n+s-1}$
$$0 \to \Phi\tau \times \sigma \to \Phi(\tau \times \sigma) \to \Psi\tau \times \sigma|_{P_s} \to 0.$$

This is one of the exact sequences in Bernstein and Zelevinsky (Ann. Sci. ENS (4) 10 (1977), Section 4). We prove it in the form of a subrepresentation and a quotient.

**Theorem 1.8.2 (Φ of τ × σ).** Let $\psi$ be continuous and $\psi \neq 1$. Then $\Phi(\tau \times \sigma)$ has a subrepresentation $S$ with $S \cong \Phi\tau \times \sigma$ and $\Phi(\tau \times \sigma)/S \cong \Psi\tau \times \sigma|_{P_s}$.

Lean: `GlobalTheory.CompanionTheory.BZPhiPG.phiPG`.

### The two evaluation maps

Let $X = \tau \times \sigma = \operatorname{c-Ind}_{H_{n,s}}^{P_{n+s}}\sigma_X$ with $\sigma_X = \tau\nu^{s/2} \otimes \sigma\nu^{-n/2}$. Let $q_C : V \otimes W \to V_{U_n,1} \otimes W$ and $q_O : V \otimes W \to V_{U_n,\theta_\psi} \otimes W$ be the quotient maps on the first factor. For $d \in k^s$ let $u(0,d) \in U_{n+s}$ have zeros in the first $n-1$ places and $d$ in the last $s$. Let $w \in G_{n+s-1}$ be the permutation matrix that exchanges the last coordinate with the block of $s$ coordinates before it, viewed in $P_{n+s}$ through $\iota$. Integrals over $k^s$ are for a fixed Haar measure and are finite sums, as in the previous section.

**Definition 1.8.3 (Closed set and evaluation maps).** The *closed cell* $\mathrm{Cl} \subseteq P_{n+s}$ is the set of $p$ such that the entries of $p^{-1}$ in row $n+s-1$ and columns $1, \dots, n-1$ vanish. For $f \in X$ and $m \in P_{n+s-1}$ put
$$e_C f(m) = \nu(m)^{-1/2}\, q_C \int_{k^s} \psi(d_s)^{-1} f\big(u(0,d)\,\iota(m)\big)\,dd,$$
$$e_O f(m) = \nu(m)^{-1/2}\, q_O \int_{k^s} f\big(u(0,d)\, w\, \iota(m)\big)\,dd.$$

The closed map integrates against $\psi^{-1}$ and keeps the untwisted coinvariants of $\tau$; the open map integrates with no character and keeps the twisted ones. So $e_C f$ takes values in the space of $(\Psi\tau) \otimes \sigma$ and $e_O f$ in the space of $(\Phi\tau) \otimes \sigma$. Let
$$C = \Psi\tau \times \sigma|_{P_s} = \operatorname{c-Ind}_{Q_{n-1,s}}^{P_{n+s-1}}\big((\Psi\tau)\nu^{s/2} \otimes \sigma|_{P_s}\nu^{-(n-1)/2}\big),$$
$$O = \Phi\tau \times \sigma = \operatorname{c-Ind}_{H_{n-1,s}}^{P_{n+s-1}}\big((\Phi\tau)\nu^{s/2} \otimes \sigma\nu^{-(n-1)/2}\big),$$
and write $\sigma_O$ for the representation of $H_{n-1,s}$ that is induced in $O$.

### The open evaluation map

The step of the cell argument proved here is that $e_O f$ lies in $O$ when $f$ vanishes on $\mathrm{Cl}$. We first state the facts it uses. We take them as given; they are proved elsewhere in the development.

**Theorem 1.8.4 (Facts on the open cell).**
- (i) For $h \in H_{n-1,s}$ with projection $(a', w') \in P_{n-1} \times G_s$, the element $\eta = w\,\iota(h)\,w^{-1}$ lies in $H_{n,s}$, with projection $(\iota(a'), w')$.
- (ii) For such $h$ and $d \in k^s$ there are $c \in H_{n,s}$ and $u \in U_n$ with $\theta_\psi(u) = 1$, such that $c$ projects to $(u, 1)$ and $u(0,d)\,\eta = \eta\, c\, u(0, w'^{-1}d)$.
- (iii) Regard $\sigma_X$ and $\sigma_O$ as representations of $P_n \times G_s$ and $P_{n-1} \times G_s$. For $u \in U_n$ with $\theta_\psi(u) = 1$, $q_O \circ \sigma_X(u,1) = q_O$; and $q_O \circ \sigma_X(\iota(a'), w') = \nu(a')^{1/2}\nu(w')^{-1/2}\,\sigma_O(a',w') \circ q_O$ for $a' \in P_{n-1}$, $w' \in G_s$.
- (iv) For a locally constant function $F$ of compact support on $k^s$ and $w' \in G_s$, $\int F(w'^{-1}d)\,dd = |\det w'|\int F(d)\,dd$.
- (v) For $h$ as in (i), $\nu(h)^{-1/2}\,|\det w'|\,\nu(a')^{1/2}\,\nu(w')^{-1/2} = 1$.
- (vi) For $f \in X$ and $y \in P_{n+s}$, the function $d \mapsto f(u(0,d)y)$ is locally constant with compact support.
- (vii) For $f \in X$, the set of $g \in P_{n+s-1}$ with $e_O f(mg) = e_O f(m)$ for all $m$ is open.
- (viii) If $f \in X$ vanishes on $\mathrm{Cl}$, there is a compact set $K \subseteq P_{n+s}$ disjoint from $\mathrm{Cl}$ with $f = 0$ outside $H_{n,s}K$.
- (ix) Every point off $\mathrm{Cl}$ has a neighbourhood on which a continuous map $\mu$ to $P_{n+s-1}$ gives $x = h\,u(0,d)\,w\,\iota(\mu(x))$ with $h \in H_{n,s}$ and $d \in k^s$.
- (x) If $u(0,d)\,w\,\iota(r) = h\,u(0,d')\,w$ with $h \in H_{n,s}$, then $r \in H_{n-1,s}$.

Fact (v) is a computation with determinants: $\det h = \det a' \det w'$, so the left side is $\nu(a')^{-1/2}\nu(w')^{-1/2}\,\nu(w')\,\nu(a')^{1/2}\nu(w')^{-1/2} = 1$. Fact (iv) is the change of variables for a linear map.

**Lemma 1.8.5 (Open evaluation).** Let $\psi$ be any character of $k$ and let $\tau$, $\sigma$ be any representations, not assumed smooth. If $f \in X$ vanishes on $\mathrm{Cl}$, then $e_O f \in O$.

Lean: `GlobalTheory.CompanionTheory.BZPhiPG.MemO.memOAlt`.

*Proof.* There are three things to check: the transformation law under $H_{n-1,s}$, smoothness, and compact support modulo $H_{n-1,s}$.

*The transformation law.* Let $h \in H_{n-1,s}$ with projection $(a', w')$, let $m \in P_{n+s-1}$ and put $y = w\,\iota(m)$. Then $w\,\iota(hm) = \eta y$ with $\eta$ as in (i). By (ii),
$$f\big(u(0,d)\,\eta y\big) = \sigma_X(\eta)\,\sigma_X(c)\,f\big(u(0, w'^{-1}d)\,y\big).$$
Apply $q_O$. By (iii) the factor $\sigma_X(c) = \sigma_X(u,1)$ disappears and $\sigma_X(\eta) = \sigma_X(\iota(a'), w')$ becomes $\nu(a')^{1/2}\nu(w')^{-1/2}\sigma_O(h)$; the linear map $\sigma_O(h)$ commutes with the integral, which is a finite sum. The function $d \mapsto q_O f(u(0,d)y)$ is locally constant with compact support by (vi), so (iv) applies to the integral over $d$ and gives a factor $|\det w'|$. With the factor $\nu(hm)^{-1/2} = \nu(h)^{-1/2}\nu(m)^{-1/2}$ in front, (v) shows that all the scalars cancel, and $e_O f(hm) = \sigma_O(h)\,e_O f(m)$.

*Smoothness.* This is (vii).

*Support.* Let $K$ be as in (viii). Cover $K$ by the neighbourhoods of (ix) and take a finite subcover; the images of the pieces under the maps $\mu$, taken over closed neighbourhoods inside them, give a compact set $N \subseteq P_{n+s-1}$ with every $x \in K$ of the form $h\,u(0,d)\,w\,\iota(m)$, $h \in H_{n,s}$, $m \in N$. Now let $e_O f(g) \neq 0$. Then $f(u(0,d)\,w\,\iota(g)) \neq 0$ for some $d$, so $u(0,d)\,w\,\iota(g) = h_1 x$ with $h_1 \in H_{n,s}$, $x \in K$, and $x = h_2\,u(0,d_2)\,w\,\iota(m_2)$ with $m_2 \in N$. Hence
$$u(0,d)\,w\,\iota(g m_2^{-1}) = h_1h_2\,u(0,d_2)\,w,$$
and by (x), $gm_2^{-1} \in H_{n-1,s}$. So $e_O f$ vanishes outside $H_{n-1,s}N$. $\square$

**Theorem 1.8.6 (Open evaluation lands in the product).** If $f \in X$ vanishes on $\mathrm{Cl}$, then $e_O f \in \Phi\tau \times \sigma$.

Lean: `GlobalTheory.CompanionTheory.BZPhiPG.MemO.eO_mem` (also `GlobalTheory.T.open_evaluation_induced`, the same statement).

*Proof.* This is the lemma, since $O = \Phi\tau \times \sigma$. $\square$

### The cell argument

We take the following abstract result as given; it is proved elsewhere in the development. Let $G$ be a topological group, $H \leq G$, $\sigma_0$ a representation of $H$ on $Z$, $Y = \operatorname{c-Ind}_H^G\sigma_0$, $U \leq G$ a normal subgroup and $\theta$ a character of $U$ with open kernel, such that any two compact subgroups of $U$ lie in a third. Say that $f \in Y$ *averages to zero at* $p \in G$ if there are a compact subgroup $L \leq U$ and $g \in Y$ such that $f - g$ lies in the span of the $lf' - \theta(l)f'$ with $l \in L$, $l g = \theta(l)g$ for $l \in L$, and $g(pu) = 0$ for all $u \in U$.

**Theorem 1.8.7 (Closed and open cells).** Let $M$ be a group, $\iota : M \to G$ and $\chi : M \to \mathbb{C}^\times$ homomorphisms, and $\rho$ the representation of $M$ on $Y_{U,\theta}$ with $\rho(m)[f] = \chi(m)[\iota(m)f]$. Let $D \subseteq G$ be closed with $HD \subseteq D$ and $DU \subseteq D$. Let $\pi_C$ and $\pi_O$ be representations of $M$, embedded injectively and equivariantly in representations $A_C$ and $A_O$, and let $e_C : Y \to A_C$ and $e_O : Y \to A_O$ be linear maps such that:
- (1) $e(uf) = \theta(u)e(f)$ for $u \in U$, for $e = e_C$ and $e = e_O$;
- (2) $m \cdot e(f) = \chi(m)\,e(\iota(m)f)$ for $m \in M$, for $e = e_C$ and $e = e_O$;
- (3) $e_C$ takes values in $\pi_C$, and $e_O$ does so in $\pi_O$ on the functions that vanish on $D$;
- (4) $e_C$ maps $Y$ onto $\pi_C$, and $e_O$ maps the functions that vanish on $D$ onto $\pi_O$;
- (5) $e_C f = 0$ if $f$ vanishes on $D$;
- (6) if $e_C f = 0$ then $f$ averages to zero at every $p \in D$, and if $e_O f = 0$ then $f$ averages to zero at every $p \notin D$.

Then $\rho$ has a subrepresentation isomorphic to $\pi_O$ with quotient isomorphic to $\pi_C$.

In the intended reading, the subrepresentation is the image of the functions that vanish on $D$, and the averaging conditions make $e_O$ and $e_C$ injective on the relevant coinvariants.

**Theorem 1.8.8 (The extension for induced spaces).** Let $\psi$ be continuous. Then $\Phi X$ has a subrepresentation isomorphic to $O$ with quotient isomorphic to $C$.

Lean: `GlobalTheory.CompanionTheory.BZPhiPG.phiPG_core`.

*Proof.* Apply the theorem on closed and open cells with $G = P_{n+s}$, $H = H_{n,s}$, $\sigma_0 = \sigma_X$, $U = U_{n+s}$, $\theta = \theta_\psi$, $M = P_{n+s-1}$, $\iota$ as above, $\chi = \nu^{-1/2}$ and $D = \mathrm{Cl}$. By definition $\Phi X(m)[f] = \nu(m)^{-1/2}[\iota(m)f]$, which is the required form of $\rho$. Take $\pi_C = C$ and $\pi_O = O$, both embedded in the space of functions on $P_{n+s-1}$ with right translation, and $e_C$, $e_O$ the evaluation maps. The data of the cell structure ($U$ normal, $\ker\theta_\psi$ open, $\mathrm{Cl}$ closed and stable under $H_{n,s}$ on the left and $U$ on the right, compact subgroups of $U$ directed) and the conditions (1), (3) for $e_C$, (4), (5) and (6) are taken as given. Condition (3) for $e_O$ is the theorem above. Condition (2) is a direct computation: right translation by $\iota(m)$ commutes with the integrals, and $\nu(xm)^{-1/2} = \nu(x)^{-1/2}\nu(m)^{-1/2}$, so $e f(xm) = \nu(m)^{-1/2}\, e(\iota(m)f)(x)$. $\square$

*Proof of the theorem on Φ of τ × σ.* The spaces $X$, $C$ and $O$ are by definition $\tau \times \sigma$, $\Psi\tau \times \sigma|_{P_s}$ and $\Phi\tau \times \sigma$, so the previous theorem is the claim. $\square$

The hypothesis $\psi \neq 1$ was not used.

**Remark 1.8.9 (Formalization).** The theorems are in [PhiPgCommutationHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PhiPgCommutationHolds.lean#L175): the extension for induced spaces at L175 and the main theorem at L231. Here $P_n$ is `Mir k (n-1)`, so $\tau$ lies on `Mir k (i+1)` with $n = i + 2$ and $\sigma$ on $\mathrm{GL}_{t+1}$ with $s = t + 1$, and the main theorem casts the index $(i+1)+t$ to $i+t+1$. The identifications of $X$, $C$ and $O$ with the products are `xr_eq`, `rc_eq` and `ro_eq` (L88 to L95), proofs by `rfl` that need `maxHeartbeats 1000000`, and the extension theorem also sets `maxHeartbeats 1000000`. The abstract theorem on cells is the input `twisted_jacquet_closed_open_sequence`, proved by `Glue.extension` in [TwistedJacquetClosedOpenSequence.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/TwistedJacquetClosedOpenSequence.lean#L259). The set $\mathrm{Cl}$, the matrix $w$ and the maps $e_C$, $e_O$ are `Cl`, `wEl`, `eC` and `eO` in [AvgVanish.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/AvgVanish.lean#L52), where averaging to zero is `AvgVanish`. The other conditions are the inputs `mirabolic_cell_structure_data`, `evaluation_maps_linear`, `closed_evaluation_equivariant`, `open_evaluation_equivariant`, `closed_evaluation_induced`, `closed_evaluation_surjective`, `open_evaluation_surjective`, `closed_evaluation_vanishing_on_open`, `average_vanishes_closed_cell` and `average_vanishes_open_cell`; condition (2) is `aC_eCl` and `aO_eOl`. We read the statements of these inputs, not their proofs. The lemma on open evaluation is in [OpenEvaluationInduced.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/OpenEvaluationInduced.lean#L179), with the transformation law `eO_equiv` (L85), the support bound `eO_supp` (L145) and the compactness step `exists_compact_cell` (L29). The facts (i) to (x) come from `weyl_conj_parabolic_proj`, `unipotent_factorization_character_trivial`, `coinvariant_unipotent_character_trivial`, `twisted_coinvariant_levi_action`, `integral_mulVec_change_modulus`, `modulus_characters_product_one`, `fibre_isLocallyConstant_hasCompactSupport`, `isOpen_right_invariance_orbit_coefficient`, `support_compact_mod_parabolic_off_closed`, `exists_continuous_local_section_of_not_mem_Cl` and `open_cell_double_coset_uniqueness`. The theorem `eO_mem` (L197) takes the continuity of $\psi$ and the smoothness of $\tau$ and $\sigma$ as hypotheses and discards all three before calling `memOAlt`. The main theorem `phiPG` (L231) receives $\psi \neq 1$ and discards it, and the extension theorem does not take it. The input on vanishing off the open cell does not take the continuity of $\psi$. The character $\nu$ is built from the normalized absolute value `nabs`, which we did not unfold.
