---
title: The theta kernel identity at every tuple
decls:
  - GlobalTheory.KerTup.kernel_identity_tuple
  - GlobalTheory.T.thetaKernelIdentity_at_every_tuple
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The theta kernel identity at every tuple

This section applies [the theta kernel at split places](/entry/theta-kernel-eq-jet-th-c/) to the column chain of a twisted tower. Each step of the chain has a theta kernel between the representatives of two classes. We prove that this kernel, times the volume of the level group, is the core constant of the step times a linear form: a jet of the classical theta function of the cell datum, scaled by two characters. This is the core law of [the kernel class datum](/entry/cls-kl-is/) in the next section, which feeds [the column condition](/entry/cls-pin-d-of-fam-col-of-true-w/) of the open orbit chapter.

**Setting.** As in [Section 2.17.2](/entry/kernel-keeps-ram-t/), let $I$ be a valid twisted tower with pinned data, laws $l$, a word $u$ and an index $a$. Its column chain has hermitian spaces $X_0, \dots, X_m$ of ranks $N_0, \dots, N_m$, with classes $\mathrm{Cl}_i$ at step $i$. Each class $c$ has a representative with lattices $N(c) \subset E^{N_i}$. Let $\xi_i(c, c')$ be the *cell datum* of a pair of classes: a function on the maps $E^{N_i} \to E^{N_{i+1}}$ with values in a number field, read in $\mathbb{C}$ by a fixed embedding. The tower gives a level $c_\ell > 0$, a finite set $SS$ of places, the constants $\delta$ and $s_c$ of [Section 2.19.4](/entry/reads-datum-eq-th-c/), and nonzero scalars $c_D(\tau)$ at the infinite places. Let $\mathcal{E}(N, N')$ be the *moved Gaussian* of a pair of lattices: a fixed character value times the classical theta function of the moved vacuum. The *theta datum* of $(c, c')$ is
$$\mathrm{th}_i(c, c') = \mathrm{th}_C\big(\xi_i(c, c'), \mathcal{E}(N(c), N(c'))\big).$$

**Definition 2.21.1 (Twist datum).** A *twist datum* $A$ gives, for each step $j$ and each character $\alpha$ in a set $\mathrm{Ch}^0_j$, a compact open subgroup $U_j(\alpha)$, finite adelic representatives $h_j(\alpha, c)$ of the classes $c$ over $\alpha$, an element $x_j(\alpha)$, an idempotent $e$ of the places of $SS$, and a character $\chi_{j+1}$ of $\mathbb{A}_E^\times$. Its *linear form* at a pair of classes is
$$\mathrm{ab}_i(c, c') = \rho_i(c)\, \rho'_i(c')\ J\big(\mathrm{th}_i(c, c')\big),$$
where $\rho_i$ and $\rho'_i$ are the characters of the classes and $J(G)$ is the linear form $P \mapsto \sum_k P_k\, \prod c_D^{k} \partial^k G(0)$ on polynomials.

Let $\iota_j$ map a set $\mathrm{Ch}_j$ of column characters into $\mathrm{Ch}^0_j$. *Pin data* give an additive character $\psi$, standard of sign $-1$, an infinite family $\theta$, vacua $f_j$ for the integral lattices of the steps, and nonzero constants $c_0(j)$ that give the reading of each moved vacuum. A *pinned column* for $(A, \iota)$ adds:

1. Weil data $\omega_j$ of the steps for the characters $\chi_{j+1}$;
2. for each $j$, $\alpha \in \mathrm{Ch}_j$ and $\gamma \in \mathrm{Ch}_{j+1}$, a finite combination $d_j(\alpha, \gamma)$ of Heisenberg translates and a weight $w_j(\alpha, \gamma)$, such that the combination of $d_j(\alpha, \gamma)$ applied to $f_j$ is the theta function at $e$ of a half Schwartz-Bruhat function $\Phi$ with $\Phi(e\gamma) = w_j(\alpha, \gamma)\, \xi_j(\alpha, \gamma)(\gamma)$;
3. constants $c_K(j)$ such that, if $\xi_j(\alpha, \gamma)$ is not zero,
$$c_K(j) = \mathrm{vol}(U_j(\iota\alpha))\ w_j(\alpha, \gamma)\ c_0(j)\ \frac{\chi_{j+1}(x_j(\iota\alpha))}{\chi_{j+1}(x_{j+1}(\iota\gamma))}.$$

Here $\xi_j(\alpha, \gamma)$ is the cell datum at the base classes of $\alpha$ and $\gamma$.

**Theorem 2.21.2 (Theta kernel identity).** Let $I$ be a valid twisted tower with pinned data, $A$ a twist datum and $\iota$ live maps, with pin data and a pinned column. Let $i + 1 \leq m$ and $s \in \mathbb{C}$, and assume that $(P \cdot f)(0) = j_s(\xi(f), P)$ for every holomorphic $f$ on the Weil space of $(X_i, X_{i+1})$. Let $\alpha \in \mathrm{Ch}_i$ and $\gamma \in \mathrm{Ch}_{i+1}$, let $c$ be a class over $\iota_i \alpha$ and $c'$ a class over $\iota_{i+1} \gamma$, and let $P$ be a polynomial. Let $F = d_i(\alpha, \gamma) \cdot f_i$. Then
$$\mathrm{vol}(U_i(\iota\alpha))\ \theta_K\big(\omega_i, h_i(c), h_{i+1}(c')\big)(P \cdot F) = c_K(i)\ \mathrm{ab}_i(c, c')\big(P_s\big),$$
where $P_s$ is $P$ with each variable at $\tau$ scaled by $s / c_D(\tau)$.

Lean: `GlobalTheory.KerTup.kernel_identity_tuple` (also `GlobalTheory.T.thetaKernelIdentity_at_every_tuple`, a second name).

*Proof.* We collect the inputs of the kernel theorem of [Section 2.20.2](/entry/theta-kernel-eq-jet-th-c/), and then treat two cases.

1. *Standard pairs.* By the theorem on the true column steps, each pair $(X_i, X_{i+1})$ is a standard pair, the embeddings of the tower are the CM embeddings, $c_D(\tau) \neq 0$, and every group element has a root of its determinant.
2. *The moved datum.* By the theorem on the moved datum of a representative pair, $h_i(c)$ and $h_{i+1}(c')$ move the integral lattices to $N = N(c)$ and $N' = N(c')$. For every scalar $p$ with $\Phi = p\, \xi_i(\alpha, \gamma)$ on rational points, it gives $\Phi(h_{i+1}(c')^{-1} (e\gamma) h_i(c)) = p\ \xi_i(c, c')(\gamma)$.
3. *The moved vacuum.* By the pin data and the theorem on the characters of the chain moves,
$$\xi\big(\omega_i(h_i(c), h_{i+1}(c')) f_i\big) = c_0(i)\, \frac{\chi_{i+1}(x_i(\iota\alpha))}{\chi_{i+1}(x_{i+1}(\iota\gamma))}\, \rho_i(c)\, \rho'_i(c')\ \mathcal{E}(N, N').$$
4. *Level and lattices.* The level $c_\ell$ is positive and odd, and the places of $SS$ are prime to $Q_S\, q\, d$. The cell datum lies in a box, so it vanishes unless $c_\ell x$ maps $N_P$ into $N'_P$ at the places of $SS$, and it is invariant under $c_\ell$ times such maps. The lattice facts hold for $(N, N')$, by the smoothness of the tower.
5. *The jet.* For every $G$, $j_s(G, P) = J(G)(P_s)$, by the theorem on Fock jets as rescaled linear forms.
6. *Case $w_i(\alpha, \gamma) \neq 0$ and $\xi_i(\alpha, \gamma) \neq 0$.* Write $w = w_i(\alpha, \gamma)$. Apply the kernel theorem with $\Xi = w\, \xi_i(c, c')$, with $\kappa$ the constant of step 3 times $w$, and with $\mathcal{E}' = w^{-1} \mathcal{E}(N, N')$. Since $\mathrm{th}_C(p\Xi, \vartheta) = \mathrm{th}_C(\Xi, p\vartheta)$, we get $\mathrm{th}_C(w \xi_i(c, c'), w^{-1}\mathcal{E}) = \mathrm{th}_i(c, c')$. So by step 5 the kernel is $\kappa\ J(\mathrm{th}_i(c, c'))(P_s)$. Multiply by the volume and use the constant law 3 of the pinned column. The product of the volume, $w$, $c_0(i)$ and the two characters is $c_K(i)$, and $\rho_i(c) \rho'_i(c') J(\mathrm{th}_i(c, c'))$ is $\mathrm{ab}_i(c, c')$.
7. *Other cases.* Then the function $w\, \xi_i(c, c')$ is zero. If $w = 0$ this is clear. Otherwise $\xi_i(\alpha, \gamma) = 0$, and step 2 with $p = 0$ and with $p = 1$ gives $\xi_i(c, c') = 0$. The kernel theorem, with $\Xi = 0$ and $\mathcal{E}$ the moved vacuum of step 3, gives $\kappa\, j_s(\mathrm{th}_C(0, \cdot), P) = 0$, so the left side is $0$. On the right side, if $\xi_i(\alpha, \gamma) \neq 0$, then $w = 0$ and $c_K(i) = 0$ by the constant law. If $\xi_i(\alpha, \gamma) = 0$, then $\xi_i(c, c') = 0$, so $\mathrm{th}_i(c, c') = 0$ and $\mathrm{ab}_i(c, c') = 0$. $\square$

The constant law is used only when the cell datum at the base classes is not zero. When it is zero, both sides vanish for every choice of $c_K(i)$.

**Remark 2.21.3 (Formalization).** The theorem is at [ThetaKernelIdentityAtEveryTuple.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaKernelIdentityAtEveryTuple.lean#L78), with the jet lemma of step 5 at line 15 and the box lemma of step 4 at line 47. It runs under a limit of four million heartbeats (line 74). The second name is in [ThetaKernelIdentityAtEveryTupleStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaKernelIdentityAtEveryTupleStatement.lean#L9), by a `first | exact` block. The twist datum and its linear form are in [LevChiEqOne.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/LevChiEqOne.lean#L73), with the pin data at line 94, and the pinned column is in [PinColL.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PinColL.lean#L26). In step 7 the proof shows $\xi_i(c, c') = 0$ by applying the moved datum theorem twice, to the same function $\Phi$ with the scalars $0$ and $1$ (lines 125 to 129). Both applications are valid because $\Phi = 0$ on rational points in that case, so the trick is sound but indirect. We have read the statements, not the proofs, of the theorems on true column steps, moved data, chain characters, the level, the smoothness of the tower and Fock jets. We have not unfolded the cell datum, the moved Gaussian, the vacuum law of the pin data or the box condition.
