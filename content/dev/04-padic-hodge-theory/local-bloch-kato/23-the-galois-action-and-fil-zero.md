---
title: The Galois action on potentials and the zeroth filtration
decls:
  - GlobalTheory.BKGal.gal_sub_value_sigma_sub_y_mem_filZero
  - GlobalTheory.T.galois_sub_value_mem_filZero_of_monodromy_zero
  - GlobalTheory.BKGal.gb_sub_b_mem_filZero
  - GlobalTheory.T.galoisAction_sub_mem_filtrationZero_of_monodromy
  - GlobalTheory.BKGal.coboundary_mem_lattice_of_mon_eq_zero
  - GlobalTheory.T.galois_coboundary_mem_lattice_inv_l_of_monodromy_eq_zero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Galois action on potentials and the zeroth filtration

Let $y$ be a vector of a Breuil-Kisin datum with monodromy class $0$, and let $b$ be a potential of $y$ in $B_{\mathcal{O}} \otimes T$. This section proves that for $g$ in the Galois group of the tame field, the difference $g b - b$ lies in the zeroth step of the de Rham filtration, and then, with the theorem of Fontaine, that a power of $\ell$ times $g b - b$ lies in $1 \otimes T$. This is the part of the construction of Galois classes that uses the vanishing of the monodromy class. It is used in [the next section](/entry/class-of-of-mon-eq-zero/), which turns potentials into crystalline cocycles.

We keep the notation of [the section on packs](/entry/exists-pack-is-of-type/) and of [the previous section](/entry/lifting-theorem-phi-modules-exact-triple/). So $\ell$ is a prime, $e + 1 = \ell^a$, $\varpi$ is a system of roots, $K_\varpi$ is the tame field, and $L$ is a finite extension of $\mathbb{Q}_\ell$ with tame descent data and ring of integers $\mathcal{O}$, free of finite rank over $\mathbb{Z}_\ell$. Let $D$ be a Breuil-Kisin datum of heights $(\eta, H)$ with $\varphi$-module $P$, let $T$ be an $\mathcal{O}$-lattice of $G_{\mathbb{Q}_\ell}$, and let $(j, j_B)$ be a Galois datum for $(D, T)$. Here $B_{\mathcal{O}} = \mathcal{O} \otimes_{\mathbb{Z}_\ell} B_{\mathrm{cris}}$, and $G_{\mathbb{Q}_\ell}$ acts on $B_{\mathcal{O}} \otimes_{\mathcal{O}} T$ through both factors. We write $N = X \nabla_P$, and $N$ also for the operator $X\, d/dX$ on series.

**Definition 7.23.1 (Correction term).** For a vector $y$, the *correction term* is
$$\zeta(y) = -\sum_{j \ge 1} (\ell \varphi)^j N y,$$
the sum taken as a limit coefficient by coefficient.

Formally, $\zeta(y) - \ell\varphi(\zeta(y)) = -\ell \varphi(N y)$. So $\zeta(y)$ is the solution of a Frobenius equation, given by a geometric series. The monodromy class of [the previous section](/entry/lifting-theorem-phi-modules-exact-triple/) is $\mathrm{Mon}(y) = [E N y - E \zeta(y)]$ modulo $M_R$.

**Definition 7.23.2 (Zeroth filtration).** Let $C$ be a core of period rings, with its map $\iota : B_{\mathrm{cris}} \to B_{\mathrm{dR}}$, as in [the section on monodromy](/entry/jumps-of-m-main/). Let $\mathrm{Fil}^0_C(T)$ be the $\mathcal{O}$-submodule of $B_{\mathcal{O}} \otimes T$ spanned by the elements $(1 \otimes \beta) \otimes x$ with $\beta \in B_{\mathrm{cris}}$, $\iota(\beta) \in \mathrm{Fil}^0 B_{\mathrm{dR}}$, and $x \in T$.

**Definition 7.23.3 (Crystalline value).** Let $w \in W_{\mathcal{O}}^\iota$ and $b \in B_{\mathcal{O}} \otimes T$. Then $b$ is a *crystalline value* of $w$ if there are $m \in A_{\mathcal{O}}$ and $c \in A_{\mathcal{O}}^\iota$ such that the image of $m$ in $B_{\mathcal{O}}$ is a unit, $m w = c$ in $W_{\mathcal{O}}^\iota$, and $m\, b = j_B(c)$ in $B_{\mathcal{O}} \otimes T$.

So a crystalline value is $j_B(c/m)$: it is defined when $w$ is an integral period up to a factor that becomes a unit in $B_{\mathcal{O}}$. Let $M[1/E]$ and $M[1/\ell]$ be the vectors whose entries lie in $\mathfrak{S}_{\mathcal{O}}[1/E]$ and in $\mathfrak{S}_{\mathcal{O}}[1/\ell]$, and $\mathcal{M}[1/\ell]$ the divided power lattice with $\ell$ inverted. There are $\mathcal{O}$-linear maps $\iota_W : M[1/E] \to W_{\mathcal{O}}^\iota$ and $\iota_B : \mathcal{M}[1/\ell] \to B_{\mathcal{O}}^\iota$, defined by the embeddings of the base rings into the period rings; we do not unfold them.

**Definition 7.23.4 (Potential).** Let $y$ be a vector. An element $b \in B_{\mathcal{O}} \otimes T$ is a *potential* of $y$ if $y \in M[1/E]$ and there are:

1. $m_0 \in W_{\mathcal{O}}^\iota$ with $\varphi_W(m_0) - m_0 = \iota_W(y)$;
2. $\sigma \in \mathcal{M}[1/\ell]$, fixed by the descent datum, with $N \sigma = \zeta(y)$;
3. a crystalline value $b_0$ of $\varphi_W(m_0)$;

such that $b = j_B(\iota_B(\sigma)) - b_0$.

The two halves of a potential solve two different equations: $m_0$ solves the Frobenius equation over Witt vectors, and $\sigma$ solves the differential equation over the divided power ring. Their difference is the period whose Galois coboundary gives a cocycle of $T$.

**Lemma 7.23.5 (Crystalline values are additive).** If $b$ is a crystalline value of $w$ and $b'$ is a crystalline value of $w'$, then $b - b'$ is a crystalline value of $w - w'$.

*Proof.* Let $m w = c$, $m b = j_B(c)$ and $m' w' = c'$, $m' b' = j_B(c')$, with $m, m'$ units in $B_{\mathcal{O}}$. Then $m m'$ is a unit in $B_{\mathcal{O}}$, $m m'(w - w') = m' c - m c'$, and, since $j_B$ is $B_{\mathcal{O}}$-linear, $m m'(b - b') = m' j_B(c) - m j_B(c') = j_B(m' c - m c')$. $\square$

We take the following results as given. They are proved in other parts of the development, and we read their statements, not their proofs.

**Theorem 7.23.6 (Horizontal approximation).** Let $L$ be complete. Let $v$ be a vector with $E^n v \in M_R$ for some $n$ and $E N v \in M_R$. Then for every $m \ge 0$ there is $w \in M[1/\ell]$ such that $v - \xi(w) \in M_R$ and, for every $\tau$ and every coordinate $i$, $\ell^k N(w_{\tau, i}) = E^m h$ for some $k \ge 0$ and $h \in \mathfrak{S}_{\mathcal{O}}$.

Here $\xi(w)_\tau = \xi_\tau w_\tau$, with the matrix $\xi_\tau$ that conjugates $d/dX$ to $\nabla_P$. So $\xi(w)$ is nearly horizontal when $N w$ is divisible by a high power of $E$.

**Theorem 7.23.7 (Galois action on horizontal vectors).** Let $\ell \ne 2$. There is $m_0 \ge 0$ with the following property. Let $w \in M[1/\ell]$ be such that, for every $\tau$ and $i$, $\ell^k N(w_{\tau, i}) \in E^{m_0} \mathfrak{S}_{\mathcal{O}}$ for some $k$, and assume $\xi(w) \in \mathcal{M}[1/\ell]$. Then for every $g \in G_{K_\varpi}$ and every core $C$,
$$g\, j_B\big(\iota_B \xi(w)\big) - j_B\big(\iota_B \xi(w)\big) \in \mathrm{Fil}^0_C(T).$$

**Theorem 7.23.8 (Horizontal vectors in the divided power lattice).** For every vector $w$, $\xi(w) \in \mathcal{M}[1/\ell]$ if and only if the entries of $w$ lie in $\mathcal{S}[1/\ell]$.

**Theorem 7.23.9 (Values in the zeroth filtration).** Let $\ell \ne 2$, $\sigma \in \mathcal{M}[1/\ell]$ and $y \in M[1/E]$ with $\sigma - y \in M_R$. Let $b_2$ be a crystalline value of $\iota_W(y)$. Then $j_B(\iota_B \sigma) - b_2 \in \mathrm{Fil}^0_C(T)$ for every core $C$.

**Theorem 7.23.10 (Stability).** For every core $C$, the module $\mathrm{Fil}^0_C(T)$ is stable under $G_{\mathbb{Q}_\ell}$.

**Theorem 7.23.11 (Frobenius potentials).** Let $\ell \ne 2$, $y \in Y_\eta \cap M[1/E]$, and $m_0 \in W_{\mathcal{O}}^\iota$ with $\varphi_W(m_0) - m_0 = \iota_W(y)$. Then $m_0$ has a crystalline value $b_1$ with $g b_1 - b_1 \in \mathrm{Fil}^0_C(T)$ for every $g \in G_{K_\varpi}$ and every core $C$.

**Theorem 7.23.12 (Frobenius invariance).** Let $y \in Y_\eta$, let $b$ be a potential of $y$, and let $g \in G_{K_\varpi}$. Then $(\varphi \otimes 1)(g b - b) = g b - b$.

**Theorem 7.23.13 (Fixed vectors of $\varphi$ in the zeroth filtration).** Assume the theorem of Fontaine. Let $T$ be an $\mathcal{O}$-lattice of a group, $C$ a core, and $z \in \mathrm{Fil}^0_C(T)$ with $(\varphi \otimes 1) z = z$. Then $\ell^n z = 1 \otimes x$ for some $n \ge 0$ and $x \in T$.

The last theorem is the integral form of the fact that $B_{\mathrm{cris}}^{\varphi = 1} \cap \mathrm{Fil}^0 B_{\mathrm{dR}} = \mathbb{Q}_\ell$, part 3 of the theorem of Fontaine. Finally, a core of period rings exists for every prime $\ell$.

**Lemma 7.23.14 (A horizontal correction).** Let $L$ be complete. Let $y \in Y_\eta$ with $\mathrm{Mon}(y) = 0$, let $\sigma \in \mathcal{M}[1/\ell]$ with $N \sigma = \zeta(y)$, and let $m \ge 0$. Then there is $w \in M[1/\ell]$ with $\sigma - y - \xi(w) \in M_R$ and, for every $\tau$ and $i$, $\ell^k N(w_{\tau, i}) \in E^m \mathfrak{S}_{\mathcal{O}}$ for some $k$.

*Proof.* Put $v = \sigma - y$. We have $E^\eta y \in M \subseteq M_R$, and $E^\eta \sigma$ has entries in $\mathcal{S}[1/\ell]$ by the height bound $E^\eta \varphi^* M \subseteq M$, so $E^\eta \sigma \in M_R$ since $\mathcal{S}[1/\ell] \subseteq R$. So $E^\eta v \in M_R$. Next, $E N v = E \zeta(y) - E N y$, which lies in $M_R$ because $\mathrm{Mon}(y) = 0$. The theorem on horizontal approximation with $n = \eta$ gives $w$. $\square$

**Theorem 7.23.15 (The Galois action on the value of $\sigma$).** Let $\ell \ne 2$. Let $y \in Y_\eta \cap M[1/E]$ with $\mathrm{Mon}(y) = 0$. Let $\sigma \in \mathcal{M}[1/\ell]$ be fixed by the descent datum, with $N \sigma = \zeta(y)$. Let $b_2$ be a crystalline value of $\iota_W(y)$, let $g \in G_{K_\varpi}$, and let $C$ be a core. Put $u = j_B(\iota_B \sigma) - b_2$. Then $g u - u \in \mathrm{Fil}^0_C(T)$.

Lean: `GlobalTheory.BKGal.gal_sub_value_sigma_sub_y_mem_filZero` (also `GlobalTheory.T.galois_sub_value_mem_filZero_of_monodromy_zero`, a second name).

*Proof.* The field $L$ is complete, as a finite extension of $\mathbb{Q}_\ell$. Let $m_0$ be the integer of the theorem on horizontal vectors, and let $w$ be given by the lemma on a horizontal correction with $m = m_0$. Since $w \in M[1/\ell]$, its entries lie in $\mathcal{S}[1/\ell]$, so $\xi(w) \in \mathcal{M}[1/\ell]$. Put $\sigma' = \sigma - \xi(w)$. Then $\sigma' \in \mathcal{M}[1/\ell]$ and $\sigma' - y \in M_R$. By the theorem on values in the zeroth filtration, $u' = j_B(\iota_B \sigma') - b_2 \in \mathrm{Fil}^0_C(T)$, and by stability $g u' \in \mathrm{Fil}^0_C(T)$. Since $\iota_B$ and $j_B$ are linear,
$$u = j_B\big(\iota_B \xi(w)\big) + u'.$$
So $g u - u$ is the sum of $g\, j_B(\iota_B \xi(w)) - j_B(\iota_B \xi(w))$, which lies in $\mathrm{Fil}^0_C(T)$ by the theorem on horizontal vectors, and $g u' - u'$. $\square$

**Theorem 7.23.16 (The Galois action on a potential).** Let $\ell \ne 2$. Let $y \in Y_\eta$ with $\mathrm{Mon}(y) = 0$, let $b$ be a potential of $y$, and let $g \in G_{K_\varpi}$. Then there is a core $C$ with $g b - b \in \mathrm{Fil}^0_C(T)$.

Lean: `GlobalTheory.BKGal.gb_sub_b_mem_filZero` (also `GlobalTheory.T.galoisAction_sub_mem_filtrationZero_of_monodromy`, a second name).

*Proof.* Take any core $C$. Write $b = j_B(\iota_B \sigma) - b_0$ as in the definition of a potential, with $\varphi_W(m_0) - m_0 = \iota_W(y)$. By the theorem on Frobenius potentials, $m_0$ has a crystalline value $b_1$ with $g b_1 - b_1 \in \mathrm{Fil}^0_C(T)$. By the lemma on additivity, $b_0 - b_1$ is a crystalline value of $\varphi_W(m_0) - m_0 = \iota_W(y)$. By [the previous theorem](/entry/gal-sub-value-sigma-sub-y-mem-fil-zero/) with $b_2 = b_0 - b_1$, the element $u = j_B(\iota_B \sigma) - b_0 + b_1 = b + b_1$ satisfies $g u - u \in \mathrm{Fil}^0_C(T)$. Then $g b - b = (g u - u) - (g b_1 - b_1) \in \mathrm{Fil}^0_C(T)$. $\square$

**Theorem 7.23.17 (Coboundaries of potentials are integral up to $\ell^n$).** Assume the theorem of Fontaine. Let $\ell \ne 2$. Let $y \in Y_\eta$ with $\mathrm{Mon}(y) = 0$, let $b$ be a potential of $y$, and let $g \in G_{K_\varpi}$. Then there are $n \ge 0$ and $x \in T$ with
$$\ell^n (g b - b) = 1 \otimes x.$$

Lean: `GlobalTheory.BKGal.coboundary_mem_lattice_of_mon_eq_zero` (also `GlobalTheory.T.galois_coboundary_mem_lattice_inv_l_of_monodromy_eq_zero`, a second name).

*Proof.* By [the previous theorem](/entry/gb-sub-b-mem-fil-zero/), $g b - b \in \mathrm{Fil}^0_C(T)$ for a core $C$. By the theorem on Frobenius invariance, $g b - b$ is fixed by $\varphi \otimes 1$. The theorem on fixed vectors of $\varphi$ gives $n$ and $x$. $\square$

In the classical picture, $g b - b$ is fixed by Frobenius, lies in $\mathrm{Fil}^0$, and so lies in $\mathbb{Q}_\ell \otimes T$ by the fundamental exact sequence. The theorem says this with an explicit lattice: $g b - b \in \ell^{-n} (1 \otimes T)$. The exponent $n$ depends on $g$; [the next section](/entry/class-of-of-mon-eq-zero/) bounds it uniformly.

**Remark 7.23.18 (Formalization).** The inputs are `horizontal_mod_breuilKisin_of_eulerNoPole`, `xi_value_galois_sub_mem_filZero`, part 2 of `breuilKisin_section_trivialises_invertPrime_tensor`, `breuilKisin_hat_value_mem_filZero`, `bcrisTensorLattice_filZero_galois_stable`, `value_mem_filtration_zero_tame`, `galoisCoboundary_frobenius_fixed`, `exists_prime_pow_smul_eq_tmul_of_frobenius_fixed_fil_zero` and `nonempty_core`. We read their statements, not their proofs; the maps $\iota_W$, $\iota_B$ and the ring $B_{\mathcal{O}}$ are not unfolded. The lemma on additivity is `IsCrisVal.sub`, and the lemma on a horizontal correction is `sub_sub_xi_mem_Man` ([GaloisSubValueMemFilZeroOfMonodromyZero.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/GaloisSubValueMemFilZeroOfMonodromyZero.lean#L17)). In the first theorem the hypothesis that $\sigma$ is fixed by the descent datum is never used ([line 34](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/GaloisSubValueMemFilZeroOfMonodromyZero.lean#L34)), and the hypothesis $y \in M[1/E]$ is used only to form $\iota_W(y)$. The second theorem only asserts that some core works, although its proof works for every core. The three second names are wrappers that set `maxHeartbeats` to 1000000.
