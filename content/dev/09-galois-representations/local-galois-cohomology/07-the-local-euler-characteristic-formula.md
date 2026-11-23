---
title: The local Euler characteristic formula
decls:
  - GroundTheory.ProfCoh.eulerChar_of_forall_eq_bot_or_eq_top
  - GroundTheory.ProfCoh.eulerChar_galois_of_card_eq
  - GroundTheory.ProfCoh.eulerChar_galois
  - GroundTheory.ProfCoh.card_cohomology_mul_div_eq
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local Euler characteristic formula

We now prove the formula of Tate for every finite discrete $G_K$-module whose order is invertible in $K$. The proof runs by induction on the order of $M$. Short exact sequences reduce it to modules with no proper nonzero stable submodule. For such a module, the ramification filtration of a finite Galois extension that trivializes $M$ gives a subgroup to which the coprime theorem of the previous section applies. The formula is used for [every character](/step/every-character/) of the main proof.

We keep the notation of the previous section: $K$ is a nonarchimedean local field, $K^{\mathrm{sep}}$ a separable closure, $G_K = \operatorname{Gal}(K^{\mathrm{sep}}/K)$, and $\chi(M) = \# H^0(G_K, M)\, \# H^2(G_K, M) / \# H^1(G_K, M)$ for a discrete $G_K$-module $M$. Let $p$ be the characteristic of the residue field $k_K$ of $K$.

### Three tools

**Lemma 1.7.1 (multiplicativity).** Let $0 \to M_1 \to M_2 \to M_3 \to 0$ be a short exact sequence of discrete $G_K$-modules with $M_2$ finite of order invertible in $K$. Then
$$\chi(M_2) = \chi(M_1)\, \chi(M_3).$$

Lean: `GroundTheory.ProfCoh.eulerChar_shortExact`.

*Proof.* The orders of $M_1$ and $M_3$ divide the order of $M_2$, so they are invertible in $K$ too. By the finiteness theorem of the previous section, all groups $H^q(G_K, M_i)$ are finite and vanish for $q \geq 3$. The long exact cohomology sequence is then an exact sequence of finite groups of length nine that starts and ends with $0$. The alternating product of the orders of the terms of such a sequence is $1$, which is the claim. $\square$

**Lemma 1.7.2 (positivity).** If $M$ is finite of order invertible in $K$, then $\chi(M) > 0$.

Lean: `GroundTheory.ProfCoh.eulerChar_pos`.

This holds because the three groups are finite and nonempty, so the convention $\# X = 0$ for infinite $X$ never applies.

**Lemma 1.7.3 (restriction to a subgroup of $p$-power index).** Let $H$ be an open normal subgroup of $G_K$ with $G_K/H$ cyclic of order $p^a$, where $p$ is a prime. Let $M$ be a finite discrete $G_K$-module of order invertible in $K$ with $pM = 0$. Then
$$\chi(H, M) = \chi(G_K, M)^{p^a}.$$

Lean: `GroundTheory.ProfCoh.eulerChar_res_eq_pow`.

*Proof.* By Shapiro's lemma, $H^q(H, M) \cong H^q(G_K, \operatorname{CoInd}_H^{G_K} M)$, so $\chi(H, M) = \chi(G_K, C)$ with $C = \operatorname{CoInd}_H^{G_K} M$. Let $s$ be a generator of $G_K/H$ and let $T$ be the endomorphism $s - 1$ of $C$. Since $G_K/H$ is abelian, $T$ commutes with the action of $G_K$. Since $s^{p^a} = 1$ on $C$ and $pC = 0$, we have $T^{p^a} = s^{p^a} - 1 = 0$. Put $D_j = T^j(C)$, a stable submodule, so $D_0 = C$ and $D_{p^a} = 0$. The kernel of $T$ is the set of $s$-fixed vectors of $C$, and it is isomorphic to $M$ as a $G_K$-module. A counting argument with $\# C = (\# M)^{p^a}$ shows that $\ker T \subseteq D_j$ for $j < p^a$. So $T$ gives short exact sequences $0 \to \ker T \to D_j \to D_{j+1} \to 0$, and multiplicativity along the chain gives $\chi(C) = \chi(\ker T)^{p^a} = \chi(M)^{p^a}$. $\square$

**Lemma 1.7.4 (vanishing for a module without inertia invariants).** Let $l$ be a prime with $l \neq p$. Let $V \leq W$ be open subgroups of $G_K$, with $W$ normal in $G_K$ and $V$ normal in $W$, such that $\mu_l \subseteq (K^{\mathrm{sep}})^V$, $[W : V]$ is prime to $l$, and for each $g \in W$ and each integral $x$ in $(K^{\mathrm{sep}})^V$ the element $g x - x$ lies in the maximal ideal. Let $M$ be a finite discrete $G_K$-module with $lM = 0$, on which $V$ acts trivially and with $M^W = 0$. Then $H^i(G_K, M) = 0$ for $i \leq 2$.

Lean: `GroundTheory.ProfCoh.subsingleton_cohomology_of_inertia`.

The condition on $W$ says that its image in $\operatorname{Gal}((K^{\mathrm{sep}})^V/K)$ lies in the inertia group. We use the lemma without proof here.

### Simple modules

Let $M$ be a finite discrete $G_K$-module. Choose an open normal subgroup $V$ of $G_K$ that acts trivially on $M$ and on $\mu_l$ for the prime $l$ in question, and let $L = (K^{\mathrm{sep}})^V$, a finite Galois extension of $K$. Write $G_0 \supseteq G_1$ for the inertia group and the wild inertia group of $\operatorname{Gal}(L/K)$, that is, the lower ramification groups of indices $0$ and $1$. Recall that $G_1$ is a $p$-group, $G_0/G_1$ is cyclic of order prime to $p$, and $\operatorname{Gal}(L/K)/G_0$ is cyclic ([decomposition groups](/learn/galois-representations/#decomposition-groups-inertia-and-frobenius)). For a subgroup $S$ of $\operatorname{Gal}(L/K)$ we write $\widetilde{S}$ for its preimage in $G_K$. For a normal subgroup $W$ of $G_K$ the fixed vectors $M^W$ form a stable submodule.

**Theorem 1.7.5 (simple modules).** Let $M$ be a nonzero finite discrete $G_K$-module of order invertible in $K$ whose only $G_K$-stable subgroups are $0$ and $M$. Then
$$\chi(M) = \frac{1}{\#(\mathcal{O}_K/\# M\, \mathcal{O}_K)}.$$

Lean: `GroundTheory.ProfCoh.eulerChar_of_forall_eq_bot_or_eq_top` (also `GroundTheory.ProfCoh.fixedSubmodule`).

*Proof.* Let $l$ be a prime that divides $\# M$. The kernel of multiplication by $l$ is a nonzero stable subgroup, so it is $M$, and $\# M = l^d$ for some $d \geq 1$. Since $\# M$ is invertible in $K$, so is $l$. Choose $V$ and $L$ as above. We use two facts about a simple $M$ several times: if $W$ is a normal subgroup of $G_K$ with $M^W \neq 0$, then $M^W = M$, so $W$ acts trivially; and if a finite $l$-group acts on a nonzero $\mathbb{F}_l$-vector space, it fixes a nonzero vector.

Case $l = p$. Then $K$ has characteristic $0$. The group $\widetilde{G_1}$ acts on $M$ through the $p$-group $G_1$, so $M^{\widetilde{G_1}} \neq 0$ and $\widetilde{G_1}$ acts trivially. Let $C \subseteq \operatorname{Gal}(L/K)$ be the preimage of the prime-to-$p$ part of the cyclic group $\operatorname{Gal}(L/K)/G_0$, and let $U = \widetilde{C}$, with fixed field $E$. Then $G_K/U$ is cyclic of order $p^a$ for some $a$, and $[U : \widetilde{G_1}]$ is prime to $p$. The $p$-th roots of unity lie in the fixed field of $\widetilde{G_1}$, because $G_1$ is a $p$-group and $\operatorname{Aut}(\mu_p)$ has order $p - 1$. Let $\#(\mathcal{O}_K/p\mathcal{O}_K) = p^{n_K}$ and $\#(\mathcal{O}_E/p\mathcal{O}_E) = p^{n_E}$. Since $[E : K] = p^a$, we have $n_E = n_K p^a$. The coprime theorem of the previous section, for $U$ and $\widetilde{G_1}$, gives $\chi(U, M) = (\# M)^{-n_E}$. The restriction lemma gives $\chi(U, M) = \chi(M)^{p^a}$. So
$$\chi(M)^{p^a} = \bigl((\# M)^{-n_K}\bigr)^{p^a}.$$
Both bases are positive, by the positivity lemma, so $\chi(M) = (\# M)^{-n_K}$. Finally $\#(\mathcal{O}_K/p^d\mathcal{O}_K) = p^{d n_K} = (\# M)^{n_K}$.

Case $l \neq p$. Then $\# M = l^d$ is a unit in $\mathcal{O}_K$, and the right side is $1$. Let $B \subseteq G_0$ be the preimage of the prime-to-$l$ part of the cyclic group $G_0/G_1$. Its order is prime to $l$, since $G_1$ is a $p$-group. The group $\widetilde{B}$ is normal in $G_K$.

If $M^{\widetilde{B}} = 0$, apply the vanishing lemma with $W = \widetilde{B}$ and $V$. Elements of $\widetilde{B}$ lie in the inertia group, and $[\widetilde{B} : V] = \# B$ is prime to $l$. So $H^0$, $H^1$ and $H^2$ vanish, and $\chi(M) = 1$.

Otherwise $\widetilde{B}$ acts trivially on $M$. Let $A \subseteq \operatorname{Gal}(L/K)$ be the preimage of the $l$-primary part of the cyclic group $\operatorname{Gal}(L/K)/G_0$. Then $A/B$ is an $l$-group, so $M^{\widetilde{A}} \neq 0$, and $\widetilde{A}$ acts trivially. The index $[G_K : \widetilde{A}]$ is prime to $l$. The extension $K(\mu_l)/K$ is unramified, because $l \neq p$, and its degree divides $l - 1$, so $\mu_l$ lies in the fixed field of $\widetilde{A}$. The coprime theorem with $U = G_K$, $V = \widetilde{A}$ and $n = 0$ gives $\chi(M) = 1$. $\square$

### The general formula

**Theorem 1.7.6 (local Euler characteristic formula, by order).** Let $n \geq 1$. For every finite discrete $G_K$-module $M$ with $\# M = n$ and $n$ invertible in $K$,
$$\chi(M) = \frac{1}{\#(\mathcal{O}_K/n\mathcal{O}_K)}.$$

Lean: `GroundTheory.ProfCoh.eulerChar_galois_of_card_eq`.

*Proof.* Strong induction on $n$. If $M = 0$, both sides are $1$. If $M$ has no stable subgroup other than $0$ and $M$, this is the [Theorem 1.7.5](/entry/euler-char-of-forall-eq-bot-or-eq-top/) on simple modules. Otherwise let $N$ be a stable subgroup with $0 \neq N \neq M$. The sequence $0 \to N \to M \to M/N \to 0$ is exact, and $\# N$, $\# (M/N)$ are smaller than $n$, divide $n$, and so are invertible in $K$. By multiplicativity and induction,
$$\chi(M) = \chi(N)\, \chi(M/N) = \frac{1}{\#(\mathcal{O}_K/\# N\,\mathcal{O}_K)\; \#(\mathcal{O}_K/\# (M/N)\,\mathcal{O}_K)}.$$
For nonzero $a, b \in \mathcal{O}_K$ the sequence $0 \to \mathcal{O}_K/a \xrightarrow{b} \mathcal{O}_K/ab \to \mathcal{O}_K/b \to 0$ is exact, so $\#(\mathcal{O}_K/ab) = \#(\mathcal{O}_K/a)\,\#(\mathcal{O}_K/b)$. With $\# N \cdot \#(M/N) = n$ this gives the claim. $\square$

**Theorem 1.7.7 (local Euler characteristic formula).** Let $M$ be a finite discrete $G_K$-module whose order is invertible in $K$. Then
$$\chi(M) = \frac{\# H^0(K, M)\, \# H^2(K, M)}{\# H^1(K, M)} = \frac{1}{\#(\mathcal{O}_K/\# M\,\mathcal{O}_K)}.$$

Lean: `GroundTheory.ProfCoh.eulerChar_galois` (also `GroundTheory.ProfCoh.card_cohomology_mul_div_eq`).

*Proof.* Apply the [Theorem 1.7.6](/entry/euler-char-galois-of-card-eq/) by order with $n = \# M$. The second form is the [statement](/entry/card-cohomology-mul-div-eq/) with the three orders written out, by the definition of $\chi$. $\square$

**Example 1.7.8.** Let $K$ be a finite extension of $\mathbb{Q}_p$ of degree $N$ and let $M = \mu_p$. Then $\#(\mathcal{O}_K/p\mathcal{O}_K) = p^N$, so $\# H^1(K, \mu_p) = p^N \cdot \# H^0(K, \mu_p) \cdot \# H^2(K, \mu_p)$. By Kummer theory $H^1(K, \mu_p) = K^\times/(K^\times)^p$, and $H^2(K, \mu_p)$ is the $p$-torsion of the Brauer group, of order $p$. So $\# K^\times/(K^\times)^p = p^{N + 1}\, \# \mu_p(K)$, the classical count.

**Remark 1.7.9.** If $K$ has characteristic $0$ and $[K : \mathbb{Q}_p] = N$, then $\#(\mathcal{O}_K/\# M\,\mathcal{O}_K) = p^{N\, v_p(\# M)}$, and the theorem is the classical form $\chi(M) = p^{-N v_p(\# M)}$. If $p$ does not divide $\# M$, in any characteristic, the right side is $1$. The single hypothesis that $\# M$ is invertible in $K$ covers both cases.

**Remark 1.7.10 (Formalization).** The Euler characteristic is a rational number defined with `Nat.card`, so the statement includes finiteness of the three groups only through the finiteness theorem of the previous section ([EulerCharDefs.lean](lean:GroundTheory/ProfiniteCohomology/EulerCharDefs.lean#L47)). The theorem by order fixes $n$ before $M$ so that strong induction on $n$ can be used. The $G_K$-modules are representations over `ULift ℤ`. The subgroups $C$, $B$ and $A$ of the proof for simple modules are `GroundTheory.ProfCoh.coprimeQuotientPreimage`, `GroundTheory.ProfCoh.coprimeRelPreimage` and `GroundTheory.ProfCoh.primaryQuotientPreimage` ([GroupStructureDefs.lean](lean:GroundTheory/ProfiniteCohomology/LocalEulerCharacteristic/GroupStructureDefs.lean#L14)), each defined through the subgroup generated by the elements of the right orders. The restriction lemma is proved through coinduction, in `GroundTheory.ProfCoh.eulerChar_coind_res_eq_pow`.

## Notes and references

The results of this chapter feed the main proof in two places. The Euler characteristic formula of the last section is used for [every character](/step/every-character/), where it bounds the cohomology of finite Galois modules over local fields. The local reciprocity map of Sections 3 to 5 gives the norm index computation behind the [statement](/entry/mul-mem-range-norm/) that the product of two non-norms in a quadratic extension is a norm.

The Lubin-Tate construction of Sections 1 and 2 is due to Lubin and Tate (see also Neukirch, Chapter V, §§5 and 6), who used formal groups to build the maximal totally ramified abelian extension attached to a uniformizer and to make the reciprocity map explicit on it. The cohomological approach to the local symbol in Section 3, through the invariant map of the Brauer group and the cup product with $\delta\chi$, follows Serre, *Local Fields*, Chapter XIV, §1, with the Brauer group of a local field as in Chapter XII. The reciprocity isomorphism and the norm index are the content of the class field axiom of Serre, *Local Fields*, Chapter XIII, and the norm computations in unramified extensions are those of Chapter V, §2. The existence theorem of Section 4 is proved here through Kummer extensions of exponent $n$, in the spirit of Neukirch, *Algebraic Number Theory*, Chapter V, §1. In this development it is stated for subgroups of finite index, which in characteristic $0$ is the same as open subgroups of finite index. The local Artin map of Section 5 is assembled from the finite layers, as in Serre, *Local Fields*, Chapter XIII, §4.

The Euler characteristic formula is due to Tate, announced at the 1962 International Congress. Serre gives a proof in *Galois Cohomology*, Chapter II, §5.7, Theorem 5, with the reduction to the elementary case in §5.5 and the finiteness and dimension results in §§5.2 to 5.3. Milne, *Arithmetic Duality Theorems*, Chapter I, §2, and Neukirch, Schmidt and Wingberg, Chapter VII, §3, give proofs through local duality. The proof here avoids duality: the coprime case is a direct computation with Kummer theory and a normal basis lattice, and the reduction to it uses the ramification filtration of a finite trivializing extension and an induction on the order of the module.

1. J. Lubin and J. Tate, *Formal complex multiplication in local fields*, Ann. of Math. 81 (1965), 380 to 387.
2. J.-P. Serre, *Local Fields*, Graduate Texts in Mathematics 67, Springer, 1979. Chapter V, §2; Chapter XII; Chapter XIII; Chapter XIV, §1.
3. J.-P. Serre, *Galois Cohomology*, Springer Monographs in Mathematics, Springer, 1997. Chapter II, §§5.2, 5.3, 5.5 and 5.7.
4. J. Neukirch, *Algebraic Number Theory*, Grundlehren der mathematischen Wissenschaften 322, Springer, 1999. Chapter IV, §§4 and 5; Chapter V, §§1, 5 and 6.
5. J. Neukirch, A. Schmidt and K. Wingberg, *Cohomology of Number Fields*, second edition, Grundlehren der mathematischen Wissenschaften 323, Springer, 2008. Chapter VII, §3.
6. J. S. Milne, *Arithmetic Duality Theorems*, second edition, BookSurge, 2006. Chapter I, §2.
7. J. Tate, *Duality theorems in Galois cohomology over number fields*, Proc. Internat. Congr. Mathematicians (Stockholm, 1962), Inst. Mittag-Leffler, 1963, 288 to 295.
