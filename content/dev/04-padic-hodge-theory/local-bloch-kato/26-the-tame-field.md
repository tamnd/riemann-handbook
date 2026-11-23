---
title: The tame field
decls:
  - GlobalTheory.GoodLatt.main
  - GlobalTheory.T.exists_tameField_goodLattice_potentiallyCrystalline
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The tame field

This section proves the theorem that Step 4 of the proof of [Theorem T](/entry/theorem-tclosing-main/) uses. Theorem T is stated with a set $\Sigma$ of characters of an inertia group $I$ attached to a finite extension $K'$. The lifting estimate is stated with a set $\Sigma' \subseteq \mathbb{Z}/e$ of exponents of the tame character $\omega$. The theorem builds $\Sigma'$ from $\Sigma$ with the same period. It also shows that every potentially crystalline lattice whose inertia acts through $\Sigma$ is crystalline over the tame field $K_\varpi$ and has tame type $\Sigma'$. Most of the work is a lemma in group theory, which we prove in full.

We keep the notation of [Theorem T](/entry/theorem-tclosing-main/) for the inertia data: a finite extension $K'$ of $\mathbb{Q}_\ell$ with maximal unramified subfield $K'_0$, the group $I$ of elements of $G_{\mathbb{Q}_\ell}$ that fix $K'_0$ in $B_{\mathrm{cris}}$, a Frobenius $\mathrm{Fr}$, Frobenius stable sets $\Sigma$ of characters $I \to L^\times$, potentially crystalline lattices, inertia that acts through $\Sigma$, the orbit length of a character, and the period $r'(\Sigma)$. We keep the notation of [the section on packs](/entry/exists-pack-is-of-type/) for the tame character $\omega$ and the tame type, and of [the section on lifting](/entry/lift-f-of-is-good/) for the period $r(\Sigma')$ of a subset of $\mathbb{Z}/e$. Let $I_{\mathbb{Q}_\ell} \subseteq G_{\mathbb{Q}_\ell}$ be the inertia group. An *arithmetic Frobenius* is an element $\Phi \in G_{\mathbb{Q}_\ell}$ with $|\Phi(x) - x^\ell| < 1$ for every $x$ in the maximal unramified extension with $|x| \le 1$.

The potentially crystalline data give a space $D_{\mathrm{pcris}}(V)$ for a representation $V$. Its definition is not unfolded here; a given theorem below identifies it with $D_{\mathrm{cris}}(V|_{G_{K'}})$.

**Lemma 7.26.1 (Characters of a Frobenius stable set).** Let $G$ be a group, $L$ a field, $I_0 \subseteq I$ subgroups of $G$, and $H$ a normal subgroup of $G$. Let $W$ be a relation between elements of $G$ and elements of $L$. Let $\ell, a, e, N$ be integers with $a \ge 1$, $e \ge 1$, $e + 1 = \ell^a$, and $k \mid a$ for $1 \le k \le N$. Let $\mathrm{Fr} \in G$, and let $\Sigma$ be a finite set of characters $I \to L^\times$. Assume:

1. $F^{-1} g F \in I$ for all $F \in G$ and $g \in I$, and $F^{-1} g F \in I_0$ for all $F \in G$ and $g \in I_0$;
2. for every $g \in I$ there is $s \in I_0$ with $s^{-1} g \in H$;
3. $\Sigma$ is Frobenius stable for $\mathrm{Fr}$, $1 \in \Sigma$, $|\Sigma| \le N$, and every $\chi \in \Sigma$ is trivial on $I \cap H$;
4. if $\chi \in \Sigma$, $h \in I_0$ and $g = \mathrm{Fr}^{-1} h\, \mathrm{Fr}$, then $\chi(h) = \chi(g)^\ell$;
5. for every $g \in I_0$ there is $w$ with $W(g, w)$ and $w^e = 1$, and there are $g_0 \in I_0$ and $w_0$ with $W(g_0, w_0)$ such that $w_0$ is a primitive $e$-th root of unity;
6. if $\chi \in \Sigma$ and $\chi^e = 1$ on $I_0$, then there is $c \in \mathbb{Z}/e$ with $\chi(g) = w^c$ whenever $g \in I_0$ and $W(g, w)$.

Then there is $\Sigma' \subseteq \mathbb{Z}/e$ with $\ell \Sigma' \subseteq \Sigma'$, $0 \in \Sigma'$, $|\Sigma'| \le N$ and $r(\Sigma') = r'(\Sigma)$, such that for every $\chi \in \Sigma$ there is $c \in \Sigma'$ with $\chi(g) = w^c$ whenever $g \in I_0$ and $W(g, w)$.

*Proof.* *Step 1: orbits.* Let $\chi \in \Sigma$. By Frobenius stability there is $b \in \Sigma$ with $b(g) = \chi(\mathrm{Fr}^{-1} g\, \mathrm{Fr})$ for $g \in I$, and condition 4 gives $\chi(g) = b(g)^\ell$ for $g \in I_0$. Iterating, we get $b_0 = \chi, b_1, b_2, \dots$ in $\Sigma$ with $b_n^{\ell^n} = \chi$ on $I_0$. Among $b_0, \dots, b_{|\Sigma|}$ two are equal, say $b_i = b_j$ with $i < j \le |\Sigma|$. Then $b_i^{\ell^{j-i}} = b_i$ on $I_0$, so $\chi^{\ell^k} = \chi$ on $I_0$ with $k = j - i$ and $1 \le k \le |\Sigma| \le N$.

*Step 2: exponents.* Since $k \mid a$, Step 1 gives $\chi^{\ell^a} = \chi$ on $I_0$. As $\ell^a = e + 1$ and $L^\times$ is a group, $\chi^e = 1$ on $I_0$. By condition 6 choose $c(\chi) \in \mathbb{Z}/e$ with $\chi(g) = w^{c(\chi)}$ whenever $g \in I_0$ and $W(g, w)$. Put $\Sigma' = \{c(\chi) : \chi \in \Sigma\}$. Then $|\Sigma'| \le |\Sigma| \le N$, and the last claim holds. Since $w_0$ is primitive, $w_0^c$ determines $c \in \mathbb{Z}/e$. From $1 = w_0^{c(1)}$ we get $c(1) = 0$, so $0 \in \Sigma'$.

*Step 3: stability under $\ell$.* Let $\chi \in \Sigma$, and take $b = b_{a-1}$ from Step 1. Then $b(g_0) = b(g_0)^{\ell^a} = \big(b(g_0)^{\ell^{a-1}}\big)^\ell = \chi(g_0)^\ell$, so $w_0^{c(b)} = w_0^{\ell c(\chi)}$ and $c(b) = \ell\, c(\chi)$. So $\ell \Sigma' \subseteq \Sigma'$.

*Step 4: orbit lengths.* Let $\chi_1, \chi_2 \in \Sigma$, $\psi = \chi_1 \chi_2^{-1}$ and $d = c(\chi_1) - c(\chi_2)$. Then $\psi(g) = w^d$ whenever $g \in I_0$, $W(g, w)$ and $w^e = 1$. The character $\psi$ satisfies condition 4 and is trivial on $I \cap H$. By induction on $k$, using condition 1, $\psi(g) = \psi(\mathrm{Fr}^{-k} g\, \mathrm{Fr}^k)^{\ell^k}$ for $g \in I_0$. We claim that for $k \ge 1$, $\psi(\mathrm{Fr}^{-k} g\, \mathrm{Fr}^k) = \psi(g)$ for all $g \in I$ if and only if $\ell^k d = d$. If the first holds, then at $g_0$ we get $w_0^d = \psi(g_0)^{\ell^k} = w_0^{\ell^k d}$, so $\ell^k d = d$. Conversely, let $\ell^k d = d$ and $g \in I$. By condition 2 write $g = s u$ with $s \in I_0$ and $u \in H$, and put $s_k = \mathrm{Fr}^{-k} s\, \mathrm{Fr}^k \in I_0$ and $u_k = \mathrm{Fr}^{-k} u\, \mathrm{Fr}^k$. Since $H$ is normal, $u_k \in H$, so $\psi(u) = \psi(u_k) = 1$. Take $w$ with $W(s_k, w)$ and $w^e = 1$. Then $\psi(s) = \psi(s_k)^{\ell^k} = w^{\ell^k d} = w^d = \psi(s_k)$. So $\psi(g) = \psi(s_k u_k) = \psi(\mathrm{Fr}^{-k} g\, \mathrm{Fr}^k)$. This proves the claim. So the orbit length of $\psi$ is the least $k \ge 1$ with $\ell^k d = d$, which is the least period of $d$ under $x \mapsto \ell x$; such $k$ exist since $\ell^a = 1$ in $\mathbb{Z}/e$.

*Step 5: periods.* The period $r'(\Sigma)$ is the largest orbit length of $\chi_1 \chi_2^{-1}$ over pairs in $\Sigma$, and $r(\Sigma')$ is the largest least period of $c(\chi_1) - c(\chi_2)$ over the same pairs. By Step 4 the two maxima agree. $\square$

**Lemma 7.26.2 (Eigenvalues kill crystalline periods).** Let $V$ be a representation whose inertia acts through $\Sigma$. Let $g \in I$ and $p \in L[x]$ with $p(\chi(g)) = 0$ for every $\chi \in \Sigma$. Then $p(g)$ kills $D_{\mathrm{pcris}}(V)$.

*Proof.* Since the inertia acts through $\Sigma$, $D_{\mathrm{pcris}}(V)$ is the sum of the $\chi$-eigenspaces of $I$ for $\chi \in \Sigma$. On a vector $y$ of the $\chi$-eigenspace, $g y = \chi(g) y$, so $p(g) y = p(\chi(g)) y = 0$. The kernel of $p(g)$ is a subspace that contains every eigenspace, so it contains their sum. $\square$

We use the following results. We read their statements, not their proofs.

**Theorem 7.26.3 (Tame inertia characters).** Let $L$ contain the unramified field of degree $a$, with tame descent data, and let $\varpi$ be a system of roots. Then:

1. for every $g \in I_{\mathbb{Q}_\ell}$ there is $w \in L$ with $w \varpi_0 = g(\varpi_0)$ and $w^e = 1$;
2. there are $g_0 \in I_{\mathbb{Q}_\ell}$ and $w_0 \in L$ with $w_0 \varpi_0 = g_0(\varpi_0)$, and $w_0$ is a primitive $e$-th root of unity;
3. let $\chi : I_{\mathbb{Q}_\ell} \to L^\times$ be a character with open kernel and order prime to $\ell$. If $\Phi$ is an arithmetic Frobenius and $g = \Phi^{-1} h \Phi$ with $g, h \in I_{\mathbb{Q}_\ell}$, then $\chi(h) = \chi(g)^\ell$. If $\chi^e = 1$, there is $c \in \mathbb{Z}/e$ with $\chi(g) = w^c$ whenever $w \varpi_0 = g(\varpi_0)$.

**Theorem 7.26.4 (Inertia groups).** $I_{\mathbb{Q}_\ell} \subseteq I$, and $I_{\mathbb{Q}_\ell}$ and $I$ are stable under conjugation by $G_{\mathbb{Q}_\ell}$. Every $g \in I$ has the form $s u$ with $s \in I_{\mathbb{Q}_\ell}$ and $u \in G_{K'}$.

**Theorem 7.26.5 (A Frobenius up to inertia).** For standard period data and a Frobenius $\mathrm{Fr}$, there is an arithmetic Frobenius $\Phi$ with $\Phi^{-1} \mathrm{Fr} \in I$.

**Theorem 7.26.6 (Potentially crystalline periods).** $D_{\mathrm{pcris}}(V) = D_{\mathrm{cris}}(V|_{G_{K'}})$, and $V$ is potentially crystalline if and only if $V|_{G_{K'}}$ is crystalline.

**Theorem 7.26.7 (Crystalline descent).** Assume the theorem of Fontaine, and fix standard period data. Let $K'$ and $F$ be finite extensions of $\mathbb{Q}_\ell$ with $G_{K'}$ normal in $G_{\mathbb{Q}_\ell}$, and let $T$ be a lattice with $V|_{G_{K'}}$ crystalline. Then:

1. if every $g \in I_{\mathbb{Q}_\ell} \cap G_F$ fixes $D_{\mathrm{cris}}(V|_{G_{K'}})$, then $V|_{G_F}$ is crystalline;
2. if $g \in I_{\mathbb{Q}_\ell}$, $p \in L[x]$, and $p(g)$ kills $D_{\mathrm{cris}}(V|_{G_{K'}})$, then $p(g)$ kills $D_{\mathrm{cris}}(V|_{G_F})$.

**Theorem 7.26.8 (The tame field).** Assume the theorem of Fontaine. Let $\ell$ be a prime, $a = (\ell - 1)!$, $e \ge 1$, $\varpi$ a system of roots, and $L$ a finite extension of $\mathbb{Q}_\ell$ that contains the unramified field of degree $a$, with tame descent data. Fix standard period data, and let $K'$ be as in Theorem T. Let $\Sigma$ be a finite set of characters $I \to L^\times$, $\mathrm{Fr}$ a Frobenius and $N \ge 0$. Assume that $\Sigma$ is Frobenius stable, $1 \in \Sigma$, $|\Sigma| \le N < \ell$, every $\chi \in \Sigma$ is trivial on $I \cap G_{K'}$, and every $\chi \in \Sigma$ has order prime to $\ell$. Then there is $\Sigma' \subseteq \mathbb{Z}/e$ with $\ell \Sigma' \subseteq \Sigma'$, $0 \in \Sigma'$, $|\Sigma'| \le N$ and $r(\Sigma') = r'(\Sigma)$, such that every $\mathcal{O}$-lattice $T$ that is potentially crystalline and whose inertia acts through $\Sigma$ is crystalline over $K_\varpi$ and has tame type $\Sigma'$.

Lean: `GlobalTheory.GoodLatt.main` (also `GlobalTheory.T.exists_tameField_goodLattice_potentiallyCrystalline`, a second name).

*Proof.* *Step 1: the data of the first lemma.* Take $G = G_{\mathbb{Q}_\ell}$, $I_0 = I_{\mathbb{Q}_\ell}$, $H = G_{K'}$, and let $W(g, w)$ mean $w \varpi_0 = g(\varpi_0)$. The tame descent data give $e + 1 = \ell^a$. For $1 \le k \le N$ we have $k \le \ell - 1$, since $N < \ell$, so $k$ divides $(\ell - 1)! = a$. Conditions 1 and 2 are the theorem on inertia groups, condition 3 is a hypothesis, and condition 5 is parts 1 and 2 of the theorem on tame characters.

For conditions 4 and 6, let $\chi \in \Sigma$, and let $\chi_0$ be its restriction to $I_{\mathbb{Q}_\ell}$. The kernel of $\chi_0$ contains $I_{\mathbb{Q}_\ell} \cap G_{K'}$, which is open since $K'$ is finite over $\mathbb{Q}_\ell$, and the order of $\chi_0$ divides the order of $\chi$, so it is prime to $\ell$. For condition 4, let $h \in I_{\mathbb{Q}_\ell}$ and $g = \mathrm{Fr}^{-1} h\, \mathrm{Fr}$. Choose $\Phi$ with $j = \Phi^{-1} \mathrm{Fr} \in I$. Then $\Phi^{-1} h \Phi \in I_{\mathbb{Q}_\ell}$ and $\Phi^{-1} h \Phi = j g j^{-1}$. Part 3 of the theorem on tame characters gives $\chi(h) = \chi(j g j^{-1})^\ell$, and $\chi(j g j^{-1}) = \chi(g)$ since $L^\times$ is commutative. For condition 6, if $\chi^e = 1$ on $I_{\mathbb{Q}_\ell}$, then $\chi_0^e = 1$, and part 3 gives $c$. The first lemma now gives $\Sigma'$ with the four properties, and for each $\chi \in \Sigma$ an exponent $c \in \Sigma'$ with $\chi(g) = w^c$ whenever $g \in I_{\mathbb{Q}_\ell}$ and $w \varpi_0 = g(\varpi_0)$.

*Step 2: the lattice over $K'$.* Let $T$ be potentially crystalline with inertia acting through $\Sigma$. By the theorem on potentially crystalline periods, $V|_{G_{K'}}$ is crystalline and $D_{\mathrm{cris}}(V|_{G_{K'}}) = D_{\mathrm{pcris}}(V)$. So the second lemma applies to $D_{\mathrm{cris}}(V|_{G_{K'}})$ for every $g \in I_{\mathbb{Q}_\ell}$, since $I_{\mathbb{Q}_\ell} \subseteq I$.

*Step 3: crystalline over $K_\varpi$.* Let $g \in I_{\mathbb{Q}_\ell} \cap G_{K_\varpi}$. Then $g(\varpi_0) = \varpi_0$, so $W(g, 1)$ holds and $\chi(g) = 1^c = 1$ for every $\chi \in \Sigma$. The second lemma with $p = x - 1$ shows that $g$ fixes $D_{\mathrm{cris}}(V|_{G_{K'}})$. Part 1 of crystalline descent with $F = K_\varpi$ shows that $V|_{G_{K_\varpi}}$ is crystalline.

*Step 4: the tame type.* Let $g \in I_{\mathbb{Q}_\ell}$ and $w = \omega(g)$, so that $w \varpi_0 = g(\varpi_0)$. Put $p = \prod_{c \in \Sigma'} (x - w^c)$. For $\chi \in \Sigma$, Step 1 gives $c \in \Sigma'$ with $\chi(g) = w^c$, so $p(\chi(g)) = 0$. By the second lemma $p(g)$ kills $D_{\mathrm{cris}}(V|_{G_{K'}})$, and part 2 of crystalline descent with $F = K_\varpi$ shows that $p(g)$ kills $D_{\mathrm{cris}}(V|_{G_{K_\varpi}})$. This is the tame type condition for $\Sigma'$. $\square$

For example, if $\Sigma = \{1\}$, then $\Sigma' = \{0\}$ and $r(\Sigma') = r'(\Sigma) = 1$. The tame type condition then says that $I_{\mathbb{Q}_\ell}$ acts trivially on $D_{\mathrm{cris}}(V|_{G_{K_\varpi}})$.

**Remark 7.26.9 (Formalization).** The inputs are `tame_inertia_characters_powers_of_omega`, `inertia_Ql_le_inertia_of_finite_extension`, `exists_frob_inv_mul_mem_inertia`, `conj_mem_inertia_of_mem`, `conj_mem_Iner`, `InertiaDecomp.iner_decomp`, `PcRes.main` and `crystalline_of_inertia_trivial_on_crystallinePeriods`. We read their statements, not their proofs. Part 2 of crystalline descent has no hypothesis that relates $F$ to $K'$; we use it as stated, with $F = K_\varpi$. The first lemma is `chars_main` ([ExistsTameFieldGoodLatticePotentiallyCrystalline.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsTameFieldGoodLatticePotentiallyCrystalline.lean#L113)), with Step 1 in `orbit_pow` (line 20) and the identification of the least period in `sInf_eq_frobPeriod` (line 71); the second lemma is `dpcris_ann` (line 312). The space $D_{\mathrm{pcris}}$, the inertia group $I$ and the group $H$ are fields of the potentially crystalline data `pc`, which we did not unfold. The main theorem sets `maxHeartbeats` to 1000000 (line 336). The hypothesis that $G_{K'}$ is normal is given for $G_{K'}$ as a subgroup of the Galois group of $\mathbb{Q}_\ell$; the proof rebuilds normality in $G_{\mathbb{Q}_\ell}$ as `hNK'` (line 410), by showing that every element fixes $\mathbb{Q}_\ell$. The second name is a wrapper that sets `maxHeartbeats` to 1000000.
