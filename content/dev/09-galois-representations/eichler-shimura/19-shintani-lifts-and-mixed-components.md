---
title: Shintani lifts and mixed components after base change
decls:
  - UpperTheory.Gal.InertialTypesAlt.killsAll_holds
  - UpperTheory.Gal.InertialTypesAlt.L.inflMatch
  - UpperTheory.Gal.InertialTypesAlt.mixType_of
  - UpperTheory.Gal.InertialTypesAlt.mixType_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Shintani lifts and mixed components after base change

This section proves three inputs of Theorems 3.17.8 and 3.17.9. The first is a statement about finite general linear groups: the Shintani lift of a product of cuspidal class functions kills every representation that is orthogonal to the product of the lifted cuspidal functions. The second is inflation matching (Definition 3.17.7), which the development proves outright. The third says that after base change along a chain, a mixed depth-zero component acquires a type with pairwise distinct characters. The third result gives the "Third" step of the proof of Theorem 3.17.8.

We keep the notation of Section 17. For a finite field $F$ we fix an algebraic closure $\overline{F}$, and $q = |F|$.

### Cuspidal class functions and their products

Let $\theta : \overline{F} \to \mathbb{C}$ be a homomorphism of multiplicative monoids that is injective on $\overline{F}^\times$. For $k \geq 0$ and a polynomial $P \in F[X]$ put $s_k(P) = \sum_\alpha \theta(\alpha)^k$, where $\alpha$ runs over the roots of $P$ in $\overline{F}$ with multiplicity.

**Definition 3.20.1 (cuspidal class function).** Let $V$ be a finite-dimensional $F$-vector space and $g \in \operatorname{End}_F(V)$. Define $\psi_k(g)$ by induction on $\dim V$:
$$\psi_k(g) = s_k(\operatorname{charpol} g) - \sum_{W} \psi_k(g|_W),$$
where $W$ runs over the $g$-stable subspaces $W \neq V$ (including $W = 0$). For $m \geq 1$ the *cuspidal function* is $c_{m,k}(x) = (-1)^{m-1} \psi_k(x)$ for $x \in \mathrm{GL}_m(F)$.

Lean: `GlobalTheory.Shin.cusp` (also `GlobalTheory.CuspGL.psi`, `GlobalTheory.CuspGL.rootSum`).

On the zero space $\psi_k = s_k(1) = 0$. So if the characteristic polynomial of $x$ is irreducible with a root $\alpha$, then $x$ has no stable subspace other than $0$ and $c_{m,k}(x) = (-1)^{m-1} \sum_{i=0}^{m-1} \theta(\alpha)^{k q^i}$. This is the value of the character of the cuspidal representation attached to $\theta^k$ on such an element (Green). The function $c_{m,k}$ is a class function.

For class functions $\alpha$ on $\mathrm{GL}_a(F)$ and $\beta$ on $\mathrm{GL}_b(F)$ and $n = a + b$, let $P_{a,b} \subseteq \mathrm{GL}_n(F)$ be the block upper triangular parabolic subgroup. The *Harish-Chandra product* is
$$(\alpha \circ \beta)(x) = \frac{1}{|P_{a,b}|} \sum_{y \in \mathrm{GL}_n(F)} \mathbf{1}_{P_{a,b}}(y^{-1} x y)\, \alpha(p_1)\, \beta(p_2),$$
where $p_1$ and $p_2$ are the two diagonal blocks of $p = y^{-1} x y$. A *twisted* product $\circ_t$ for a field automorphism $t$ uses $y^{-1} x\, t(y)$ in place of $y^{-1} x y$.

For a list $L = ((m_1, k_1), \dots, (m_r, k_r))$ with $m_i \geq 1$ let $\deg L = \sum m_i$ and
$$J_\theta(L) = c_{m_1,k_1} \circ \bigl(c_{m_2,k_2} \circ (\cdots \circ (c_{m_r,k_r} \circ 1))\bigr)$$
on $\mathrm{GL}_{\deg L}(F)$. A pair $(m, k)$ is *regular* for $q$ if $k q^i \not\equiv k \pmod{q^m - 1}$ for $0 < i < m$, that is, if $\theta^k$ is in general position on $\mathbb{F}_{q^m}^\times$.

### The Shintani lift

Let $F'/F$ be an extension of degree $l$ and $s \in \operatorname{Gal}(F'/F)$. For $\delta \in \mathrm{GL}_n(F')$ the *norm* is $N_s(\delta) = \delta\, s(\delta) \cdots s^{l-1}(\delta)$. The *Shintani lift* of a function $f$ on $\mathrm{GL}_n(F)$ is the function on $\mathrm{GL}_n(F')$ with $\mathrm{Sh}_s f(\delta) = f(\gamma)$ if $N_s(\delta)$ is conjugate in $\mathrm{GL}_n(F')$ to some $\gamma \in \mathrm{GL}_n(F)$ (for a chosen such $\gamma$), and $\mathrm{Sh}_s f(\delta) = 0$ if there is no such $\gamma$.

For $q$, $l$ and a list $L$, the *lifted list* $L^{(l)}$ replaces each pair $(m, k)$ by
$$\begin{aligned} &(m/l, k), (m/l, kq), \dots, (m/l, kq^{l-1}) && \text{if } l \mid m,\\ &\bigl(m,\ k(1 + q^m + q^{2m} + \cdots + q^{(l-1)m})\bigr) && \text{if } l \nmid m. \end{aligned}$$
So $\deg L^{(l)} = \deg L$.

**Definition 3.20.2 (killing).** Let $G$ be a group and $\phi, Y : G \to \mathbb{C}$ with finite support. Then $\phi$ *kills the complement of* $Y$ if for every finite-dimensional complex representation $\rho$ of $G$ with $\sum_g \overline{Y(g)} \operatorname{tr} \rho(g) = 0$ we have $\sum_g \overline{\phi(g)}\, \rho(g) = 0$.

Lean: `GlobalTheory.Shin.Kills`.

**Theorem 3.20.3 (the Shintani lift kills).** Let $F'/F$ be an extension of finite fields of prime degree $l$, $s \neq 1$ in $\operatorname{Gal}(F'/F)$, $\iota : \overline{F} \to \overline{F'}$ an $F$-embedding and $\theta : \overline{F'} \to \mathbb{C}$ a monoid homomorphism injective on $\overline{F'}^\times$. Let $L$ be a list of pairs $(m, k)$ with $m \geq 1$ and $(m, k)$ regular for $q$, and $n = \deg L$. Then $\mathrm{Sh}_s J_{\theta \circ \iota}(L)$ kills the complement of $J_\theta(L^{(l)})$ on $\mathrm{GL}_n(F')$.

Lean: `UpperTheory.Gal.InertialTypesAlt.killsAll_holds` (also `GlobalTheory.T.shintani_lift_kills_product_of_cusp_forms`, `GlobalTheory.Shin.DescentAll.kills_liftAll`).

*Proof.* Since $l$ is prime and $s \neq 1$, $s$ generates $\operatorname{Gal}(F'/F)$. We use induction on $L$. For $L$ empty, $n = 0$, the group is trivial and both functions are $1$. Let $L = (m, k) :: L'$. Write $A$ for the lifted list of the single pair $(m, k)$. Four facts are used.

1. For one pair, $\mathrm{Sh}_s c_{m,k}$ kills the complement of $J_\theta(A)$. If $l \mid m$ this is the case of a cuspidal function of degree divisible by $l$, which becomes a product of $l$ cuspidal functions of degree $m/l$; if $l \nmid m$ it becomes the single cuspidal function $c_{m, k(1 + q^m + \cdots)}$.
2. The Shintani lift of a Harish-Chandra product of class functions is the twisted product of the lifts: $\mathrm{Sh}_s(\alpha \circ \beta) = \mathrm{Sh}_s \alpha \circ_s \mathrm{Sh}_s \beta$.
3. Lifting keeps the degree and regularity: each pair of $A$ and of $L'^{(l)}$ is regular for $q^l = |F'|$. So $J_\theta(A)$ and $J_\theta(L'^{(l)})$ are characters of representations, and $J_\theta(A \mathbin{+\!\!+} L'^{(l)}) = J_\theta(A) \circ J_\theta(L'^{(l)})$.
4. If $\alpha$ kills the complement of a character $A_0$ and $\beta$ kills the complement of a character $B_0$, then $\alpha \circ_t \beta$ kills the complement of $A_0 \circ B_0$.

By the induction hypothesis $\mathrm{Sh}_s J_{\theta\circ\iota}(L')$ kills the complement of $J_\theta(L'^{(l)})$. Facts 2 and 3 write the two sides for $L$ as a twisted product and a product, and fact 4 with fact 1 gives the claim. $\square$

### Inflation matching

**Theorem 3.20.4 (inflation matching holds).** Inflation matching (Definition 3.17.7) holds. In detail: let $K/k$ be an extension of $p$-adic fields of characteristic zero with continuous inclusion, $r_k : \mathcal{O}_k \to F$ and $r_K : \mathcal{O}_K \to F'$ surjections onto finite fields compatible with $F \subseteq F'$, with $[F' : F] = [K : k]$, and $s \in \operatorname{Gal}(K/k)$ that reduces to the $|F|$-th power map on $F'$. Let $\phi$ be a class function on $\mathrm{GL}_n(F)$, $f$ its inflation to $\mathrm{GL}_n(\mathcal{O}_k)$ (zero outside), and $f'$ the inflation of the Shintani lift of $\phi$. Then:

1. if $N_s(\delta)$ has separable characteristic polynomial equal to that of $\gamma \in \mathrm{GL}_n(k)$, the twisted orbital integral of $f'$ at $\delta$ for $\mathrm{GL}_n(\mathcal{O}_K)$ equals the orbital integral of $f$ at $\gamma$ for $\mathrm{GL}_n(\mathcal{O}_k)$;
2. if $\gamma$ has separable characteristic polynomial and the orbital integral of $f$ at $\gamma$ is nonzero, then the characteristic polynomial of $\gamma$ is that of $N_s(\delta)$ for some $\delta \in \mathrm{GL}_n(K)$.

Lean: `UpperTheory.Gal.InertialTypesAlt.L.inflMatch`.

The equality $[F':F] = [K:k]$ says that $K/k$ is unramified, so this is the statement of Definition 3.17.7.

*Proof.* The residue data make $K/k$ unramified, $s$ a generator of $\operatorname{Gal}(K/k)$, and reduction a bijection between the norm maps over $\mathcal{O}$ and over the residue fields. Call $\gamma$ *integral* if some conjugate of $\gamma$ lies in $\mathrm{GL}_n(\mathcal{O}_k)$. The inflations vanish outside $\mathrm{GL}_n(\mathcal{O})$, so the orbital integral of $f$ at $\gamma$ is zero unless $\gamma$ is integral, and the same holds for $f'$ at $\delta$ through the norm.

For item 1, $\gamma$ is regular semisimple, since its characteristic polynomial stays separable over $K$. Then $\delta$ is a norm of $\gamma$, that is, $N_s(\delta)$ is conjugate to $\gamma$. If $\gamma$ is not integral, both sides vanish. If $\gamma$ is integral, choose $\delta_0 \in \mathrm{GL}_n(\mathcal{O}_K)$ with $N_s(\delta_0) = \gamma$, which exists by a twisted form of Hilbert's Theorem 90 for the unramified extension. The norm map is injective on twisted classes of regular semisimple elements, so $\delta$ is twisted-conjugate to $\delta_0$, and twisted orbital integrals are invariant under twisted conjugation. The twisted centralizer of $\delta_0$ maps onto the centralizer of $\gamma$, and the integral points correspond. On $\mathrm{GL}_n(\mathcal{O}_K)$ the value of $f'$ at a twisted conjugate of $\delta_0$ equals the value of $f$ at the corresponding conjugate of $\gamma$, by the definition of the Shintani lift and reduction. A transfer lemma for orbital integrals with these correspondences gives the equality.

For item 2, a nonzero orbital integral gives a conjugate of $\gamma$ in the support of $f$, so $\gamma$ is integral, and $\delta_0$ above has $N_s(\delta_0) = \gamma$. $\square$

### Mixed components after base change

The next result needs the trace statement from the proof of Theorem 3.17.8.

**Definition 3.20.5 (the trace property at an inert step).** The *trace property* holds if the following is true. Let $E/F$ be a Galois extension of totally complex number fields of prime degree, $n > 0$, $\pi$ a cuspidal representation of $\mathrm{GL}_n(\mathbb{A}_F)$ and $P$ one of $\mathrm{GL}_n(\mathbb{A}_E)$ with $P \cong P^g$ for all $g \in \operatorname{Gal}(E/F)$, and $P$ a weak base change of $\pi$. Let $v$ be a place of $F$ that is unramified and not split in $E$, $w \mid v$, and $\tau = \pi_v$, $\tau' = P_w$. Choose an embedding of residue fields $\kappa_v \subseteq \kappa_w$ compatible with $F_v \subseteq E_w$, and let $s$ be the $|\kappa_v|$-th power map on $\kappa_w$. Then for every class function $f$ on $\mathrm{GL}_n(\kappa_v)$,
$$\sum_\gamma f(\gamma) \operatorname{tr} \tau^{K_1}(\gamma) \neq 0 \implies \sum_\delta \mathrm{Sh}_s f(\delta)\, \tau'^{K_1}(\delta) \neq 0.$$

Lean: `UpperTheory.Gal.InertialTypesAlt.FinTrace`.

Here $\tau^{K_1}$ is the representation of $\mathrm{GL}_n(\kappa_v)$ on the vectors fixed by the kernel $K_1$ of reduction, as in Section 17.

Let $\kappa$ be the residue field of a $p$-adic field $k$. For block sizes $d_1, \dots, d_c \geq 1$ with sum $n$, the *parahoric subgroup* $\mathcal{P}_d$ is the preimage in $\mathrm{GL}_n(\mathcal{O}_k)$ of the block upper triangular subgroup of $\mathrm{GL}_n(\kappa)$. For characters $\theta_1, \dots, \theta_c$ of $\kappa^\times$, a representation $\tau'$ of $\mathrm{GL}_n(k)$ *has a type vector* for $(d, \theta)$ if some $v \neq 0$ satisfies $\tau'(p) v = \prod_b \theta_b(\det \bar p_b)\, v$ for all $p \in \mathcal{P}_d$, where $\bar p_b$ is the $b$-th diagonal block of the reduction of $p$.

**Theorem 3.20.6 (mixed components after base change).** Assume the trace property. Let $E$ be totally complex, $\pi$ cuspidal on $\mathrm{GL}_n(\mathbb{A}_E)$ with $n > 0$, and $(K, \pi_K)$ reached from $(E, \pi)$ by a chain (Definition 3.17.5). Let $A$ lie over places $v$ of $E$ and $w$ of $K$, with $E_v \cong \mathbb{Q}_g$ as topological fields and $K$ fixed by the inertia group of $A$ over $E$. Let $\tau = \pi_v$ and $\tau' = \pi_{K,w}$, suppose that $\tau$ is mixed (Definition 3.17.2), and that $N(w) = g^f$ with $f$ divisible by the size of each member of each support of $\tau$. Then there are $c$, block sizes $d_1, \dots, d_c \geq 1$ with sum $n$ and pairwise distinct characters $\theta_1, \dots, \theta_c$ of $\kappa_w^\times$ such that $\tau'$ has a type vector for $(d, \theta)$.

Lean: `UpperTheory.Gal.InertialTypesAlt.mixType_of` (also `UpperTheory.Gal.InertialTypesAlt.MixType`).

The proof uses *labels*. A label is a triple $a = (q, D, L)$ of an integer $q \geq 2$ and two lists of pairs: $D$ describes characters $\theta^{k} \circ \det$ on blocks of size $m$, and $L$ describes cuspidal functions $c_{m,k}$ with $(m, k)$ regular for $q$. A representation $\tau$ of $\mathrm{GL}_n$ of a local field with residue field of size $q$ *has the label* $a$ if $n$ is the total size and $\tau^{K_1}$ pairs nonzero with the Harish-Chandra product of these functions. The *lift* of $a$ by $l$ replaces $q$ by $q^l$ and $L$ by $L^{(l)}$.

*Proof.* Choose embeddings of the residue fields at $v$ and $w$ into the residue field of $A$ and an injective character $\Theta$ of its multiplicative monoid. Since $\tau$ is mixed, it has a label $a$ for $\Theta$ such that $a$ is *apart* (the exponents of $D$ are distinct and less than $q - 1$, every member of $L$ has size at least $2$, and no two members of $L$ of the same size are Frobenius conjugate) and a support $s$ such that each pair of $L$ has the size of a member of $s$.

The trace property and the Theorem above (the Shintani lift kills) move labels along each step of the chain. So $\tau'$ has a label $b$ that is reached from $a$ by lifts of prime degree. Here $a$ has $q = g$, since $E_v \cong \mathbb{Q}_g$, and $b$ has $q = N(w) = g^f$. Every size in $L$ divides $f$, so $a$ splits over $\mathbb{F}_{g^f}$. Then every member of the cuspidal part of $b$ has size $1$, and the blocks of $b$ over $\mathbb{F}_{g^f}$ (pairs of a size and an exponent modulo $g^f - 1$) are those of $a$. Since $a$ is apart and splits, these exponents are pairwise distinct modulo $g^f - 1$.

A label whose cuspidal part has only size $1$ gives a type vector: there are sizes $d_x$ and exponents $k_x$, listing $D$ and then $L$, such that $\tau'$ has a type vector for $d$ and the characters $\theta_x(u) = \Theta(u)^{k_x}$ of $\kappa_w^\times$. Each $d_x \geq 1$. If $\theta_x = \theta_{x'}$, then $\Theta(\zeta)^{k_x} = \Theta(\zeta)^{k_{x'}}$ for a generator $\zeta$ of $\kappa_w^\times$. Since $\Theta$ is injective, $\zeta^{k_x} = \zeta^{k_{x'}}$, so $k_x \equiv k_{x'} \pmod{g^f - 1}$, and then $x = x'$ by the distinctness. $\square$

**Corollary 3.20.7 (mixed components, from inflation matching).** If inflation matching holds, then the conclusion of the Theorem above holds.

Lean: `UpperTheory.Gal.InertialTypesAlt.mixType_holds`.

*Proof.* Inflation matching implies the trace property, with three further inputs on norms and on the variation of traces that we do not reproduce (see the Remark). Apply [Theorem 3.20.6](/entry/mix-type-of/). $\square$

**Remark 3.20.8 (Formalization).** `killsAll_holds` is a renaming of `shintani_lift_kills_product_of_cusp_forms`, whose proof is `first | exact @GlobalTheory.Shin.DescentAll.kills_liftAll | ...` ([ShintaniLiftKillsProductOfCuspForms.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShintaniLiftKillsProductOfCuspForms.lean#L7)); the induction is in [FormalGermBaseChange.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FormalGermBaseChange.lean#L45). The four facts of its proof are `first | exact` wrappers of lemmas in `GlobalTheory.Shin` that we did not open. In `shLift` the element $\gamma$ is chosen with `Classical.choose`; well-definedness is not needed. `inflMatch` is a full proof; we did not open the helper lemmas `derive`, `redNorm`, `goodDelta`, `normInj`, `latDesc` and `orbTransfer`. `mixType_of` applies `mixType` to `lblTrue_of hT`, `lblMixed_holds`, `sepOf` and six label lemmas, which we did not open. `mixType_holds h` is `mixType_of (L.finTrace_of_matching h)`, and `finTrace_of_matching` is `finTrace_holds h varEx_holds varTrace_holds normInt_holds`, not opened, so the Corollary's proof only records this chain (it ends in `finTrace resEx finAct inflFacts frobFacts (inflTrace h h₁ h₂ h₃)`). Definition 3.17.7 says "unramified"; the Lean form asks instead for $[F':F] = [K:k]$, which implies it.
