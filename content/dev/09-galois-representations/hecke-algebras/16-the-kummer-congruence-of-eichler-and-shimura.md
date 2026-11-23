---
title: The Kummer congruence of Eichler and Shimura
decls:
  - GlobalTheory.T.eichlerShimura_kummer_function_uniform_exceptional_primes
  - GlobalTheory.KZ.ES.eichlerShimura_unit
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Kummer congruence of Eichler and Shimura

The proof of [the Eichler and Shimura relation modulo prime powers](/entry/eichler-shimura-frobenius-quadratic-mod-prime-pow/) in Section 6 uses a Kummer form of the congruence relation for one function. This section proves it, with a finite set of exceptional primes that depends only on the level and not on the function or on the power of $l$. It is also used directly in [the Eichler and Shimura step](/entry/s-es/) of the modularity chapter. The proof combines Kronecker's congruence for the modular equation, read at a Gauss valuation, with a criterion for a function to be an $l^n$-th power.

We keep the notation of [Section 6.1.5](/entry/tower-exists/) and Section 6: an algebraic closure $\Omega$ of $\mathbb{Q}$, an injective map $\varepsilon : \Omega \to \mathbb{C}$, a tower of modular functions $(K, \exp, |, s, \mathrm{an}, j_K)$ over $(\Omega, \varepsilon)$, the slash action $f \mapsto f|\gamma$ of $\mathrm{GL}_2^+(\mathbb{Q})$, the Galois action $f \mapsto s(f)$ of $\mathrm{Gal}(\Omega/\mathbb{Q})$ on $K$, and the groups $\mathrm{Un}(m)$ of functions whose divisor away from the cusps is divisible by $m$. For $M \geq 1$, $f$ is *of level $M$* if $f|\gamma = f$ for all $\gamma \in \Gamma(M)$.

**Definition 6.16.1 (Hecke product).** Let $M \geq 1$ and let $q$ be a prime. For $f \in K$ put
$$
N_q(f) = \prod_{j=0}^{q-1} f\Big|\begin{pmatrix} 1 & jM \\ 0 & q \end{pmatrix}.
$$

If $q \nmid M$, the numbers $jM$ run over the residues modulo $q$, so $N_q(f)$ is the norm of $f$ along the $q$ upper triangular cosets of the Hecke correspondence $T_q$. The remaining coset is $\begin{pmatrix} q & 0 \\ 0 & 1 \end{pmatrix}$, composed with a diamond matrix.

**Definition 6.16.2 (Diamond matrix and Frobenius for a valuation).** Let $M \geq 1$ and $q$ a prime. A matrix $\gamma \in \mathrm{SL}_2(\mathbb{Z})$ is a *diamond matrix for $q$ modulo $M$* if $\gamma_{12} \equiv 0$, $\gamma_{21} \equiv 0$ and $\gamma_{22} \equiv q$ modulo $M$. Let $V$ be a valuation ring of $\Omega$ with valuation $v$. An element $s \in \mathrm{Gal}(\Omega/\mathbb{Q})$ is a *Frobenius at $q$ for $V$* if $q$ lies in the maximal ideal of $V$, and for every $x \in V$ we have $s(x) \in V$, $s^{-1}(x) \in V$ and $v(s(x) - x^q) < 1$.

So $s$ fixes $V$, and it induces the $q$-th power map on the residue field of $V$. This is a [Frobenius element](/learn/galois-representations/#decomposition-groups-inertia-and-frobenius) at the place of $V$.

**Theorem 6.16.3 (Kummer congruence).** Assume that $\mathrm{an}(j_K)$ is the germ of a function holomorphic on $\mathcal{H}$. Let $l$ be a prime and $M_0 \geq 1$ with $l \mid M_0$. There is a finite set $S$ of primes with the following property. Let $q \notin S$ be a prime, $V$ a valuation ring of $\Omega$, and $s$ a Frobenius at $q$ for $V$. Let $n, k \geq 0$, $M = M_0 l^k$, and let $f \in \mathrm{Un}(l^n)$ be of level $M$. Let $\gamma$ be a diamond matrix for $q$ modulo $M$. Then there is $g \in K^\times$ with
$$
N_q(f)\cdot f\Big|\Bigl(\gamma\begin{pmatrix} q & 0 \\ 0 & 1 \end{pmatrix}\Bigr) = s(f)\cdot\bigl(s^{-1}(f|\gamma)\bigr)^q\cdot g^{l^n}.
$$

Lean: `GlobalTheory.KZ.ES.eichlerShimura_unit` (also `GlobalTheory.T.eichlerShimura_kummer_function_uniform_exceptional_primes`, a second name).

The left side is $f$ under the Hecke correspondence $T_q$ composed with the diamond operator, written multiplicatively. The right side is the Frobenius and its transpose, $s(f)$ and $(s^{-1}f')^q$. So the theorem is the congruence $T_q \equiv \mathrm{Frob}_q + \langle q \rangle\,\mathrm{Frob}_q^{t}$ of Eichler and Shimura, read in the Kummer classes modulo $l^n$. The set $S$ does not depend on $n$, $k$, $f$, $V$ or $s$.

We use two results on functions at a valuation. Let $V$ be a valuation ring of $\Omega$. A valuation ring $W$ of $K$ *dominates the expansions at $V$* if every $f$ whose expansion has all coefficients in $V$ lies in $W$, every $f$ whose coefficients all lie in the maximal ideal of $V$ has $W$-valuation $< 1$, and every $f$ with coefficients in $V$ and one unit coefficient has $W$-valuation $1$. It is a *Gauss valuation for $j_K$ over $V$* if $W \cap \Omega = V$ and $P(j_K)$ has $W$-valuation $1$ for every polynomial $P$ with coefficients in $V$ and one unit coefficient. A lemma gives, for every $V$, a valuation ring $W$ with both properties.

**Proposition 6.16.4 (Kronecker congruence).** Under the hypotheses of the theorem there is a finite set $S_1$ of primes with the following property. Let $q \notin S_1$, let $s$ be a Frobenius at $q$ for $V$, let $W$ dominate the expansions at $V$, and let $f \neq 0$ be of level $M_0 l^k$. Then there are constants $c_1, c_2 \in \Omega$ such that
$$
c_1\frac{N_q(f)}{s(f)} - 1 \quad\text{and}\quad c_2\frac{f|\mathrm{diag}(q, 1)}{\bigl(s^{-1}(f)\bigr)^q} - 1
$$
have $W$-valuation $< 1$.

This is Kronecker's congruence for the modular equation: modulo a place above $q$, the $q + 1$ transforms of $f$ under $T_q$ split into the $q$ transforms that reduce to the Frobenius of $f$ and the one transform that reduces to $f^q$, up to constants. See Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Chapter 7.

**Proposition 6.16.5 (Powers at a Gauss valuation).** Under the hypotheses of the theorem there is a finite set $S_2$ of primes with the following property. Let $q \notin S_2$, let $V$ be a valuation ring of $\Omega$ with $q$ in its maximal ideal, and let $W$ be a Gauss valuation for $j_K$ over $V$. Let $U \in \mathrm{Un}(l^n)$ be of level $M_0 l^k$ with $U - 1$ of $W$-valuation $< 1$. Then $U = g^{l^n}$ for some $g \in K^\times$.

*Proof of the theorem.* Let $S = S_1 \cup S_2 \cup \{\text{primes dividing } M_0\}$. Fix $q$, $V$, $s$, $n$, $k$, $f$ and $\gamma$ as in the statement, and choose $W$ that dominates the expansions at $V$ and is a Gauss valuation for $j_K$ over $V$.

Put $f' = f|\gamma$. Since $\Gamma(M)$ is normal in $\mathrm{SL}_2(\mathbb{Z})$, $f'$ is of level $M$. The Kronecker congruence for $f$ gives $c_1$ with $c_1 N_q(f)/s(f) \equiv 1$, and for $f'$ gives $c_2$ with $c_2 (f'|\mathrm{diag}(q,1))/(s^{-1}f')^q \equiv 1$, both at $W$. Note that $f'|\mathrm{diag}(q, 1) = f|(\gamma\,\mathrm{diag}(q, 1))$.

The group $\mathrm{Un}(l^n)$ contains the nonzero constants and is closed under products, inverses, the slash action and the Galois action. So
$$
U = c_1c_2\,\frac{N_q(f)\cdot f'|\mathrm{diag}(q, 1)}{s(f)\cdot\bigl(s^{-1}(f')\bigr)^q}
$$
lies in $\mathrm{Un}(l^n)$. It is of level $M$: this is clear for the factors $s(f)$ and $s^{-1}(f')$, and for $N_q(f)$ and $f'|\mathrm{diag}(q,1)$ a lemma on Hecke products shows that their product is of level $M$, since $\gamma$ is a diamond matrix and $q \nmid M$. Since $U$ is a product of two elements congruent to $1$ at $W$, also $U - 1$ has $W$-valuation $< 1$. The second proposition gives $U = g_0^{l^n}$. Choose $b \in \Omega$ with $b^{l^n} = (c_1c_2)^{-1}$, and put $g = b\,g_0$. Then $g^{l^n} = U/(c_1c_2)$, which is the claim. $\square$

**Remark 6.16.6.** Section 6 states this congruence with the set $S_f$ allowed to depend on $f$. The theorem here gives one set for all $f$ of level $M_0 l^k$, for all $k$.

**Remark 6.16.7 (Formalization).** The second name is a wrapper of the form `first | exact @… | …`. The set $S$ contains the primes dividing $M_0$ ([EichlerShimuraKummerFunctionUniformExceptionalPr.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/EichlerShimuraKummerFunctionUniformExceptionalPr.lean#L83)), and this is how $q \nmid M$ enters. The holomorphy hypothesis on $j_K$ duplicates a field of the tower, as in earlier sections. The two propositions are `GlobalTheory.T.kronecker_congruence_modularFunctionTower_level` and `GlobalTheory.T.isPow_of_gauss_valuation_congr_one_almost_all_primes`; the existence of $W$ and the level of the Hecke product are `GlobalTheory.KZ.ES.exists_dom_gauss` and `GlobalTheory.KZ.ES.lev_heckeProd`. We read them as statements and did not open their proofs. The Frobenius condition asks also that $s^{-1}$ preserve $V$, which the definition of Section 6 does not ask.
