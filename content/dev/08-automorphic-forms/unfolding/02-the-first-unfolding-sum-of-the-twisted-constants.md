---
title: The first unfolding sum of the twisted constants
decls:
  - Formalism.L2.Col.unfoldingNonvanishingDoubleCoset_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The first unfolding sum of the twisted constants

This section applies the theorem of Section 1 to the local constants that the column construction attaches to each prime. At a prime $P$ outside a finite exceptional set, of degree one and unramified, the first unfolding sum of these constants is a twisted Eisenstein coefficient. So its nonvanishing at large depth depends only on the double coset of the element. The result is [the nonvanishing in a double coset](/entry/unfolding-nonvanishing-double-coset-holds/), and it is the first input of [the twisted character index](/entry/twisted-index-first-unfolding-ok/) of Section 3. Through that index it feeds [the existence of members with large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/) of Volume 15.

### The data

We work with column data: ranks $(o, k, m, t)$ as in Section 1, a number field $E$ with an involution, a field $K$ with an embedding $\sigma_0 \colon K \to \mathbb{C}$, a finite set $V$ of primes of $\mathcal{O}_E$ (the exceptional set), a set of admissible primes (the primes of the row), a nonzero element $\xi_0 \in E$, and for each $j < m$ a character $\mu_j$ that gives a value $\mu_j(P) \in K^\times$ at each prime $P \notin V$. Let $q = q(P)$ be the norm of $P$ and $\bar q \in K$ its image.

**Definition 5.2.1 (Twisted local constants).** Let $P \notin V$ and $D = 2m$. Choose $\zeta \in K$ with $\sigma_0(\zeta) = e^{2\pi i / q^{D}}$ and $s \in K$ with $s^2 = \bar q$, when such elements exist. The *twisted additive character* at $P$ is
$$\psi_P(a) = \begin{cases} \zeta^{\,b} & \text{if } q^D a \text{ is integral at } P \text{ and } \xi_0 a - b/q^D \text{ is integral at } P \text{ for an integer } b, \\ 1 & \text{otherwise,} \end{cases}$$
where $b$ is one fixed choice of such an integer. The *multiplier* of step $j$ is $\mu^\flat_j(P) = \mu_{j-1}(P)^{-1}\, \bar q^{-1}$ for $1 \leq j \leq m$, and $\mu^\flat_j(P) = 1$ for $j > m$. The *twisted constants* at $P$ are the depth $D = 2m$, the function $\psi_P$, the square root $s_P = s$, the multipliers $\mu^\flat_j(P)$, and the truncation $A = B = m + 1$.

So $\psi_P(a)$ is $e^{2\pi i b / q^{2m}}$ when $\xi_0 a \equiv b / q^{2m}$ modulo $\mathcal{O}_{(P)}$. It is the standard [additive character](/learn/class-field-theory/#additive-characters) of $q^{-2m}\mathcal{O}_{(P)}/\mathcal{O}_{(P)}$, twisted by $\xi_0$. At the primes of $V$ the constants are fixed in another way, with depth $1$; we do not use them here.

**Definition 5.2.2 (Good twisted constants).** The twisted constants are *good* if for every prime $P \notin V$ in the row, of degree one and unramified:

1. $\psi_P(x + y) = \psi_P(x)\psi_P(y)$ whenever $q^{2m}x$ and $q^{2m}y$ are integral at $P$;
2. $\psi_P(x) = 1$ for $x$ integral at $P$;
3. $\psi_P(x) \neq 0$ for all $x$;
4. $s_P^2 = \bar q$ in $K$;
5. $\sigma_0(\psi_P(a)) = e^{2\pi i b/q^{2m}}$ whenever $q^{2m} a$ is integral and $\xi_0 a - b/q^{2m}$ is integral at $P$ for an integer $b$;
6. $\xi_0$ is integral at $P$ and its reduction modulo $P$ is not $0$.

**Definition 5.2.3 (Column coefficient).** For $P \notin V$ in the row, $i \geq 0$, $g_0 \in \mathrm{GL}(V_i)$ and $h \in \mathrm{GL}(V_{i+1})$, the *column coefficient* $\mathcal{E}^{\mathrm{col}}_{A,B}(g_0, h)$ is the first unfolding sum of Section 1 formed with the twisted constants at $P$: the character $\psi_P$, the set $\mathcal{V}_{A,B}$, the weight $\bar q^{-B}$, and the transform $\omega(g_0, h)$ of the test function, with $\mu = \mu_{c_q, \xi^{-1}}$ for $c_q = \mu^\flat_{i+1}(P)$ and $\xi$ the residue character of the column at $P$, and with $s = s_P$. Bounded elements and double cosets are as in Section 1, with the lattices $\Lambda_j$ and level groups $J_j$ of the column at $P$.

### The comparison

**Lemma 5.2.4 (The column coefficient is a twisted Eisenstein coefficient).** Let $P \notin V$ be in the row. Then for all $A, B$, all $i$ and all $g_0$, $h$, the column coefficient $\mathcal{E}^{\mathrm{col}}_{A,B}(g_0, h)$ equals the twisted Eisenstein coefficient $\mathcal{E}_{A,B}(g_0, h)$ of Section 1 with $\psi = \psi_P$, $s = s_P$, $c_q = \mu^\flat_{i+1}(P)$ and $\xi$ the residue character at $P$. Off $V$, the lattices of the column are the standard lattices $\Lambda_j$ and the level groups of the column are the groups $J_j$.

*Proof.* Off $V$ the twisted constants are the ones listed above, and the column lattices and level groups are defined by the same formulas as $\Lambda_j$ and $J_j$. So both sides are the same sum. $\square$

The lemma also gives the hypotheses of the theorem of Section 1. Conditions 1 and 2 are the first two clauses of admissibility at depth $2m$. The third clause holds by the definition of $\psi_P$: if $q^{2m}x$ is not integral, the first case of the definition fails and $\psi_P(x) = 1$. The multiplier $\mu^\flat_{i+1}(P)$ is not $0$, since it is a product of inverses of nonzero elements, or $1$. The square root is not $0$, since $s_P^2 = \bar q$ and $\bar q \neq 0$ in the case that matters.

### The theorem

**Theorem 5.2.5 (Nonvanishing in a double coset).** Let the column data have $m = m_2 + 2$, and let the twisted constants be good. Let $i < m_2$ and let $P \notin V$ be a prime of the row, of degree one and unramified. Let $g_0 \in \mathrm{GL}(V_i)$ be bounded at step $i$, and let $h, h' \in \mathrm{GL}(V_{i+1})$ be bounded at step $i + 1$ and in the same double coset $R_1 h J_{i+1}$. If the column coefficient $\mathcal{E}^{\mathrm{col}}(g_0, h)$ is nonzero at large depth, then $\mathcal{E}^{\mathrm{col}}(g_0, h')$ is nonzero at large depth.

Lean: `Formalism.L2.Col.unfoldingNonvanishingDoubleCoset_holds`.

*Proof.* By the lemma, the two coefficients are twisted Eisenstein coefficients, and the bounded elements and double cosets are those of Section 1. Since $i < m_2$ and $m = m_2 + 2$, we have $i + 3 \leq m$. The function $\psi_P$ is admissible of depth $2m$ by conditions 1 and 2 and the remark after the lemma. The multiplier and the square root are nonzero by the same remark and condition 4. This is [the nonvanishing theorem for twisted Eisenstein coefficients](/entry/twisted-eisenstein-nonvanishing/) applied to these data, and that theorem is the theorem of Section 1 with its three hypotheses proved. $\square$

The square root $s_P$ enters the transform $\omega$ through the powers $s^{v(\det h) a}$. With $s_P^2 = \bar q$, these powers are the half integral powers of $q$ that normalize the induced representation. The choice of $\zeta$ and the condition 5 tie $\psi_P$ to the standard character $x \mapsto e^{2\pi i x}$ of $\mathbb{Q}_q / \mathbb{Z}_q$ after the embedding $\sigma_0$; they are not used in this section, but Section 3 uses them.

**Remark 5.2.6 (Formalization).** Of the six conditions of good twisted constants, only 1, 2 and 4 are used in this proof; conditions 3, 5 and 6 are carried for Section 3. The integer $b$ in $\psi_P$, the root of unity $\zeta$ and the square root $s_P$ are chosen with Hilbert's choice operator; when $\zeta$ or $s_P$ does not exist, the choice is arbitrary, and the good conditions then cannot hold. The multiplier is $1$ for $j > m$ by a fallback in its definition. We did not unfold the column data (the row, the exceptional set, the residue character) beyond the facts used above. See [UnfoldingNonvanishingDoubleCosetHolds.lean](lean:Formalism/LocalToGlobal/Columns/UnfoldingNonvanishingDoubleCosetHolds.lean#L81).
