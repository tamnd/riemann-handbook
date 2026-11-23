---
title: q-expansions of Kummer classes
decls:
  - GlobalTheory.CyclotomicQExpansion.thN_hecke
  - GlobalTheory.T.cuspFunctionalModPrimePow_commutes_hecke_diamond
status: drafted
drafted_by: writer@claude-opus-5-5
---
## $q$-expansions of Kummer classes

The Kummer module $\mathcal{B}$ of [Section 6.6.5](/entry/eichler-shimura-frobenius-quadratic-mod-prime-pow/) is built from classes of modular units modulo powers of $l$. This section attaches to an element of $\mathcal{B}$ and a power $l^n$ a $q$-expansion modulo $l^n$: the logarithmic derivative of a unit that represents one coefficient of the element. It proves that this map turns the Hecke operators on $\mathcal{B}$ into the usual operators on $q$-expansions: $T_q$ into $U_q + q^{w+1} V_q$ with a diamond twist, $U$ into $U_l$ with one more power of $l$, and $\langle a \rangle$ into a change of the twist. This is the step that lets the Euler system argument read off Hecke eigenvalues on Kummer classes from $q$-expansions. It is used in [the joint theta operator theorem](/entry/th-op/) of the Kato chapter.

We keep the tower $(K, \exp, |, s, \mathrm{an}, j_K)$ over $(\Omega, \varepsilon)$ of [Section 6.1.5](/entry/tower-exists/), with $\Omega$ an algebraic closure of $\mathbb{Q}$, and the notation of Section 6 for $\widehat{K}_l$, $[f]_n$, $\mathcal{F}$ and $\mathcal{B}$. Fix a prime $l$, a level $N$ with $l \nmid N$, and a valuation ring $A$ of $\Omega$ whose maximal ideal contains $l$. For $x, y \in \Omega$ write $x \equiv y \pmod{l^n A}$ when $x - y \in l^n A$. For Hahn series, congruence is meant coefficient by coefficient.

**Definition 6.8.1 (Operators on $q$-expansions).** For $\varphi = \sum_r a_r q^r \in \Omega((q^{\mathbb{Q}}))$ let $\theta\varphi = \sum_r r a_r q^r$. For a prime $q$ put
$$
U_q \varphi = \frac{1}{q}\sum_{j=0}^{q-1} \sum_r e_\Omega\!\left(\frac{r j}{q}\right) a_r\, q^{r/q}, \qquad V_q\varphi = \sum_r a_r q^{q r}, \qquad U'_q\varphi = \sum_{r \in \mathbb{Z}} a_{q r} q^r.
$$
For a series with integer exponents, $U_q\varphi = \sum_r a_{qr} q^r = U'_q\varphi$. In general $U_q$ also keeps the terms $a_r q^{r/q}$ with $r \notin \mathbb{Z}$ for which the root of unity sum does not vanish, while $U'_q$ drops all exponents that are not integers.

The operator $U_q$ is the action of $\sum_j \begin{pmatrix} 1 & j \\ 0 & q \end{pmatrix}$ on $q$-expansions, by law 6 of a tower, divided by $q$. So $U_q$ and $V_q$ are the classical operators on $q$-expansions of weight $2$ forms.

**Definition 6.8.2 (Logarithmic derivative modulo $l^n$).** A Hahn series is *primitive* for $A$ if its coefficients lie in $A$ and one of its nonzero coefficients is a unit of $A$. Let $f \in K^\times$ and $\varphi \in \Omega((q^{\mathbb{Q}}))$. We say that $\varphi$ is a *logarithmic derivative of $f$ modulo $l^n$* if the coefficients of $\varphi$ lie in $A$, and there are $a, b \in K$ and $\kappa \in \Omega^\times$ with $f b = \kappa a$, $\exp a$ and $\exp b$ primitive, and
$$
\varphi \cdot \exp a \cdot \exp b \equiv \theta(\exp a)\cdot \exp b - \exp a \cdot \theta(\exp b) \pmod{l^n A}.
$$

Formally $\varphi = \theta(\exp a)/\exp a - \theta(\exp b)/\exp b = \theta \log \exp(f)$, as $\theta$ kills constants. The definition avoids division, and the primitivity of $\exp a$ and $\exp b$ makes the congruence meaningful.

**Definition 6.8.3 (The $q$-expansion of a Kummer class).** Let $b \in \mathcal{F}$, $n \geq 0$. A series $\varphi$ is a *$q$-expansion of $b$ modulo $l^n$* if there is $f \in K^\times$ such that:

1. $f$ is fixed by $\Gamma_1(N l^n)$;
2. $b(1, 0) \equiv [f]_n$ modulo $l^n$;
3. for every $\delta \in \Gamma_1(N)$ with $-\delta \in \Gamma(l^n)$, the product $f \cdot (f|\delta)$ is $g^{l^n}$ for some $g \in K$ fixed by $\Gamma_1(N l^n)$;
4. $\varphi$ is a logarithmic derivative of $f$ modulo $l^n$.

For $d$ prime to $N$ let $\vartheta_{n,d}(b)$ be a $q$-expansion of $(\sigma_d)_* b$ modulo $l^n$ with only integer exponents, chosen once and for all, if one exists, and $0$ if none exists. Here $\sigma_d$ is the diamond matrix of [Section 6.5.4](/entry/ss-pot-b-at-newform/).

The value $b(1,0)$ is the coefficient of $u_0^w$ in $b$. Condition 3 says that $f$ is, up to an $l^n$-th power, odd under the matrices $\delta$ that act as $-1$ on the $l^n$-torsion, as the class of an odd weight coefficient should be.

Two facts from the development are used. *Existence:* if $l \neq 2$, $N \geq 5$, $w$ is odd, $d$ is prime to $N$ and $b \in \mathcal{B}$, then $(\sigma_d)_* b$ has a $q$-expansion modulo $l^n$ with only integer exponents, so $\vartheta_{n,d}(b)$ is one of them. *Uniqueness:* if $l \neq 2$ and $l \nmid N$, any two $q$-expansions of the same $b$ modulo $l^n$ are congruent modulo $l^n A$. The proof of uniqueness compares the two units $f$, $f'$: their classes agree modulo $l^n$, so $f' = f u^{l^n}$ for some $u \in K^\times$. Conditions 1 and 3 for $f$ and $f'$ then control $u$ under translations, and this makes the logarithmic derivatives of $f$ and $f'$ agree modulo $l^n A$.

**Theorem 6.8.4 ($q$-expansions of Kummer classes and Hecke operators).** Let the tower be such that $j_K$ has a holomorphic germ. Let $l \neq 2$ be a prime, $N \geq 5$ with $l \nmid N$, and $A$ a valuation ring of $\Omega$ with $l$ in its maximal ideal. Let $n \geq 0$, $w$ odd, $d$ prime to $N$, and $b \in \mathcal{B}$. Then:

1. for every prime $q \nmid N l$,
$$
\vartheta_{n,d}(T_q b) \equiv U_q\, \vartheta_{n,d}(b) + q^{w+1} V_q\, \vartheta_{n,dq}(b) \pmod{l^n A};
$$
2. $\vartheta_{n,d}(U b) \equiv U'_l\, \vartheta_{n+1,d}(b) \pmod{l^n A}$;
3. for every $a$ prime to $N$, $\vartheta_{n,d}(\langle a \rangle b) \equiv \vartheta_{n,da}(b) \pmod{l^n A}$.

Lean: `GlobalTheory.CyclotomicQExpansion.thN_hecke` (also `GlobalTheory.T.cuspFunctionalModPrimePow_commutes_hecke_diamond`, a second name).

*Proof.* The admitted letters $T_q$ for $q \nmid Nl$, $U$ and $\langle a \rangle$ for $a$ prime to $N$ map $\mathcal{B}$ into itself. So by existence, the left side of each congruence is a $q$-expansion modulo $l^n$ of the element $(\sigma_d)_*(T b)$, for the letter $T$ in question. By uniqueness it is enough to show that the right side is also a $q$-expansion modulo $l^n$ of the same element. This is a separate statement for each letter.

*The letter $T_q$.* Let $f_1$ and $f_2$ be the units behind $\vartheta_{n,d}(b)$ and $\vartheta_{n,dq}(b)$. By the definition of $T_q$ on $\mathcal{F}$, the coefficient $((\sigma_d)_* T_q b)(1, 0)$ is, modulo $l^n$, the class of a product of the functions $f_1 | \begin{pmatrix} 1 & j \\ 0 & q \end{pmatrix}$ for $j < q$ and of a power of $f_2 | \begin{pmatrix} q & 0 \\ 0 & 1 \end{pmatrix}$, where the exponent $q^w$ comes from evaluating $u_0^w$ at $q u_0$. A logarithmic derivative turns products into sums. By law 6 of a tower, the matrices $\begin{pmatrix} 1 & j \\ 0 & q \end{pmatrix}$ act on $q$-expansions by $q^r \mapsto e_\Omega(rj/q) q^{r/q}$, and $\theta$ divides the exponent by $q$, which gives $U_q \vartheta_{n,d}(b)$. The matrix $\mathrm{diag}(q, 1)$ acts by $q^r \mapsto q^{qr}$, and $\theta$ multiplies the exponent by $q$, which gives $q^{w+1} V_q \vartheta_{n,dq}(b)$. Here $q$ is a unit in $A$, as $q \neq l$.

*The letter $U$.* The same computation with the matrices $\begin{pmatrix} 1 & j \\ 0 & l \end{pmatrix}$ applies to the unit behind $\vartheta_{n+1,d}(b)$, which is fixed by $\Gamma_1(N l^{n+1})$. The sum over $j$ of roots of unity kills the non integral exponents, so $U'_l$ appears. One power of $l$ is lost through the division by $l$, which is why level $n + 1$ is needed on the right.

*The letter $\langle a \rangle$.* The matrices $\sigma_a \sigma_d$ and $\sigma_{da}$ lie in the same coset of $\Gamma_1(N) \cap \Gamma_0(l)$, and $b$ is invariant under this group. So $(\sigma_d)_* \langle a \rangle b = (\sigma_{da})_* b$ and a $q$-expansion of one is a $q$-expansion of the other. $\square$

The congruences are the $q$-expansion form of the Hecke relations for weight $w + 2$ forms of character $\chi$: the coefficient of $q^r$ in $T_q h$ is $a_{qr}(h) + \chi(q) q^{w+1} a_{r/q}(h)$. Here the character is replaced by the change of the twist from $d$ to $dq$.

**Remark 6.8.5 (Formalization).** Unlike the rest of the chapter, this theorem writes the holomorphy hypothesis on $j_K$ in the order "germ, then holomorphy" ([CuspFunctionalModPrimePowCommutesHeckeDiamond.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/CuspFunctionalModPrimePowCommutesHeckeDiamond.lean#L83)). This matches the tower field it duplicates, and the only user passes that field. The selection $\vartheta_{n,d}$ is made by `choose`, with junk value $0$ when no $q$-expansion exists ([ThNSpec.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ThNSpec.lean#L17)); the existence fact shows that the junk value is not reached on $\mathcal{B}$. The second name is a wrapper under `maxHeartbeats 1000000`. The existence fact and the three per letter statements were read as statements; the computations sketched above are the expected ones, not a transcript of the Lean proofs. The uniqueness argument is in the same file.
