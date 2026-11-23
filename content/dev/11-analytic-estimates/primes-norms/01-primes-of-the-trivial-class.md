---
title: Primes of the trivial class in short intervals
decls:
  - GlobalTheory.Hk.ShortInt.trivialClass_shortInterval
  - GlobalTheory.T.exists_lam_zero_sum_shortInterval_ge
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Primes of the trivial class in short intervals

This section proves a lower bound for a weighted count of prime ideals of the trivial class in a short interval $(X, X(1+h)]$. It works with an axiomatic family of partial zeta functions, so that the argument does not depend on the field. The bound is polynomial in the size $B$ of the family, and the interval can be as short as $h = \exp(-c\sqrt{\log X})$. The result is used in Section 3 to prove [the lower bound for primes represented by norms](/entry/norm-primes-short-interval-lower/), which is applied in Volume 8 as [the short interval norm theorem](/entry/short-norm/).

**Definition 2.1.1 (Family of ray class type).** A *family of ray class type* consists of a finite abelian group $G$, written additively, real numbers $B$ and $\kappa$, and two functions $a, \lambda : G \times \mathbb{N} \to \mathbb{R}$, with the following properties. Here $\Lambda$ is the [[von Mangoldt function|0NK8JTE1NN]].

1. $B \geq 4$, $|G| \leq B$ and $1/B \leq \kappa \leq 4$.
2. $a(g, n) \geq 0$ and $a(g, 0) = 0$ for all $g$ and $n$; $a(0, 1) = 1$, and $a(g, 1) = 0$ for $g \neq 0$.
3. For each $g$ and each real $x \geq 1$, $\bigl|\sum_{1 \leq n \leq x} a(g, n) - \kappa x\bigr| \leq 10\sqrt{x}$.
4. For each $g$ and each $t$ with $0 < t \leq 1$, $\bigl|\sum_{n \geq 0} a(g, n) e^{-tn} - \kappa/t\bigr| \leq B^{10} t$.
5. $\lambda(g, n) \geq 0$ and $\sum_{g} \lambda(g, n) \leq 2\Lambda(n)$ for all $g$ and $n$.
6. For each $g$ and $n$, $a(g, n)\log n = \sum_{h \in G} \sum_{de = n} \lambda(h, d)\, a(g - h, e)$.
7. Put $A(n) = \sum_g a(g, n)$. For each character $\chi : G \to \mathbb{C}^\times$ with $\chi^2 = 1$, put $A_\chi(n) = \sum_g \mathrm{Re}\,\chi(g)\, a(g, n)$. Then for every $n$,
$$0 \leq \sum_{de = n} A(d) A_\chi(e) \quad \text{and} \quad A(n) \leq \sum_{de = n^2} A(d) A_\chi(e).$$

The model is a number field $K$ with a modulus $M$. There $G$ is the ray class group modulo $M$, $a(g, n)$ is the number of ideals of norm $n$ in the class $g$, and $\lambda(g, n)$ is the sum of $\log N\mathfrak{p}$ over the prime powers $\mathfrak{p}^k$ of norm $n$ in the class $g$. Property 3 is a count of ideals in a class, with an error of the size of a lattice point count. Property 6 is the factorization $\log N\mathfrak{a} = \sum_{\mathfrak{p}^k \mid \mathfrak{a}} \log N\mathfrak{p}$, sorted by classes. Section 2 makes this model precise for imaginary quadratic fields.

**Definition 2.1.2 (L-functions of a family).** Fix a family and a character $\chi$ of $G$. Put
$$a_\chi(n) = \sum_g \chi(g)\, a(g, n), \qquad \lambda_\chi(n) = \sum_g \chi(g)\, \lambda(g, n),$$
and let $r_\chi = \kappa |G|$ if $\chi = 1$ and $r_\chi = 0$ otherwise. For $\mathrm{Re}\, s > 1/2$ put
$$m_\chi(s) = \int_1^\infty \Bigl(\sum_{1 \leq n \leq x} a_\chi(n) - r_\chi x\Bigr) x^{-s-1}\, dx,$$
and let $F_\chi(s) = r_\chi s + (s-1)s\, m_\chi(s)$ if $\chi = 1$, and $F_\chi(s) = s\, m_\chi(s)$ otherwise. Finally put
$$\psi_\chi(x) = \sum_{1 \leq n \leq x} \lambda_\chi(n), \qquad \ell(t) = \log\bigl(B(|t| + 2)\bigr).$$

By property 3 and the orthogonality of characters, the integrand of $m_\chi$ is at most $10|G|\sqrt{x}\, x^{-\mathrm{Re}\, s - 1}$ in absolute value. So $m_\chi$ is holomorphic for $\mathrm{Re}\, s > 1/2$, and so is $F_\chi$. For $\mathrm{Re}\, s > 1$ partial summation gives $L_\chi(s) := \sum_n a_\chi(n) n^{-s} = r_\chi s/(s-1) + s\, m_\chi(s)$. Thus $F_\chi(s) = (s-1)L_\chi(s)$ for $\chi = 1$ and $F_\chi(s) = L_\chi(s)$ for $\chi \neq 1$. The factor $s - 1$ removes the pole, so the zeros of $F_\chi$ near $1$ are the zeros of $L_\chi$. Property 6, multiplied by $\chi(g)$ and summed over $g$, gives $a_\chi(n)\log n = \sum_{de = n} \lambda_\chi(d) a_\chi(e)$. In terms of Dirichlet series this is
$$-\frac{L_\chi'(s)}{L_\chi(s)} = \sum_{n \geq 1} \lambda_\chi(n) n^{-s} \qquad (\mathrm{Re}\, s > 1).$$
So $\psi_\chi$ plays the part of the Chebyshev function $\psi(x, \chi)$ of a [[Dirichlet L-function|24GAZHVTGB]], and $\ell(t)$ plays the part of $\log(q(|t| + 2))$.

**Definition 2.1.3 (Exceptional set).** Let $c > 0$. A finite set $Z \subset \mathbb{R}$ is an *exceptional set of level $c$* for $\chi$ if

1. $Z$ has at most one element;
2. each $\beta \in Z$ satisfies $1 - c/\ell(0) \leq \beta < 1$, $F_\chi(\beta) = 0$ and $F_\chi'(\beta) \neq 0$;
3. each $s \in \mathbb{C}$ with $\mathrm{Re}\, s \geq 1 - c/\ell(\mathrm{Im}\, s)$ and $F_\chi(s) = 0$ is an element of $Z$.

So $Z$ is empty, or it is a simple real zero, and all other zeros of $F_\chi$ lie to the left of the curve $\sigma = 1 - c/\ell(t)$.

We use four results on these families. They are the analogues of the classical facts on zeros of Hecke L-functions (see Notes and references). We do not prove them in this chapter.

**Theorem 2.1.4 (Zero-free region).** There is $c > 0$ with the following property. Let a family, a character $\chi$ of $G$ and $s \in \mathbb{C}$ satisfy $\mathrm{Re}\, s \geq 3/4$ and $F_\chi(s) = 0$, and suppose that $\chi^2 \neq 1$ or $\mathrm{Im}\, s \neq 0$. Then $\mathrm{Re}\, s < 1 - c/\ell(\mathrm{Im}\, s)$.

Lean: `GlobalTheory.T.rayClassLFunction_zero_free_region`.

**Theorem 2.1.5 (Uniqueness of the exceptional zero).** There is $c > 0$ with the following property. Let $\chi$ and $\psi$ be characters of $G$ with $\chi^2 = \psi^2 = 1$, and let $\beta, \beta'$ be real with $\beta, \beta' \geq 3/4$, $\beta, \beta' \geq 1 - c/\ell(0)$, $F_\chi(\beta) = 0$ and $F_\psi(\beta') = 0$. Then $\chi = \psi$, $\beta = \beta'$ and $F_\chi'(\beta) \neq 0$.

Lean: `GlobalTheory.T.rayClassLFunction_unique_simple_exceptional_zero`.

**Theorem 2.1.6 (Prime sums with an exceptional zero).** For each $c_0$ with $0 < c_0 \leq 1/20$ there are $c, C > 0$ with the following property. Let $Z$ be an exceptional set of level $c_0$ for $\chi$, and let $u \geq 2$ with $\log B \leq \sqrt{\log u}$. Let $\delta_\chi = 1$ if $\chi = 1$ and $\delta_\chi = 0$ otherwise. Then
$$\Bigl|\psi_\chi(u) - \delta_\chi u + \sum_{\beta \in Z} \frac{u^\beta}{\beta}\Bigr| \leq C u\, e^{-c\sqrt{\log u}}.$$

Lean: `GlobalTheory.T.rayClassFamily_psi_with_exceptional_zero`.

**Theorem 2.1.7 (Real zeros are not too close to 1).** There are $A, c > 0$ such that for every family, every $\chi$ with $\chi^2 = 1$ and every real $\beta \geq 3/4$ with $F_\chi(\beta) = 0$, we have $c/B^A \leq 1 - \beta$.

Lean: `GlobalTheory.T.exists_rayClassLFunction_real_zero_far_from_one`.

The last bound is polynomial in $B$. It is much weaker than Siegel's theorem, but it is effective, and it is all that a polynomial lower bound needs.

**Lemma 2.1.8 (Choice of the exceptional sets).** There are $c_0 \in (0, 1/20]$, $A > 0$ and $c \in (0, 1]$ such that every family has sets $Z_\chi$, one for each character $\chi$, with these properties: each $Z_\chi$ is an exceptional set of level $c_0$ for $\chi$; if $\beta \in Z_\chi$ and $\beta' \in Z_\psi$, then $\chi = \psi$ and $\beta = \beta'$; and each $\beta \in Z_\chi$ satisfies $\beta \geq 3/4$ and $c/B^A \leq 1 - \beta$.

*Proof.* Let $c_4$ and $c_5$ be the constants of the zero-free region and of the uniqueness theorem, and put $c_0 = \min(1/20, c_4, c_5)$. Since $\ell \geq \log 8 > 2$, we have $1 - c_0/\ell(t) > 3/4$ for every $t$. Let $Z_\chi$ be the set of real zeros $\beta$ of $F_\chi$ with $\beta \geq 1 - c_0/\ell(0)$, if $\chi^2 = 1$, and the empty set otherwise. Let $s$ be a zero of $F_\chi$ with $\mathrm{Re}\, s \geq 1 - c_0/\ell(\mathrm{Im}\, s)$. Then $\mathrm{Re}\, s > 3/4$, and the zero-free region with $c_4 \geq c_0$ excludes the case $\chi^2 \neq 1$ or $\mathrm{Im}\, s \neq 0$. So $\chi^2 = 1$, $s$ is real, and $s \in Z_\chi$. The uniqueness theorem with $c_5 \geq c_0$ shows that the sets $Z_\chi$ together contain at most one zero, and that this zero is simple. The last theorem gives $c/B^A \leq 1 - \beta$, and in particular $\beta < 1$. $\square$

**Lemma 2.1.9 (Orthogonality).** For every family and every real $u$, $\sum_\chi \psi_\chi(u) = |G| \sum_{1 \leq n \leq u} \lambda(0, n)$, where the sum runs over all characters of $G$.

*Proof.* We have $\sum_\chi \chi(g) = |G|$ if $g = 0$ and $0$ otherwise. Exchange the sums in $\sum_\chi \sum_{n \leq u} \sum_g \chi(g) \lambda(g, n)$. $\square$

**Lemma 2.1.10 (Contribution of the exceptional zero).** Let $X \geq e$, $h \geq 0$, $\beta \geq 3/4$ and $0 < \delta \leq 1 - \beta$. Then
$$\frac{(X(1+h))^\beta}{\beta} - \frac{X^\beta}{\beta} \leq hX\Bigl(1 - \frac{\delta}{2}\Bigr).$$

*Proof.* Since $0 < \beta \leq 1$, Bernoulli's inequality gives $(1 + h)^\beta \leq 1 + \beta h$. So the left side is at most $hX^\beta = hX \cdot X^{\beta - 1}$. Since $\beta - 1 \leq -\delta$ and $X \geq e$, we get $X^{\beta - 1} \leq e^{-\delta} \leq 1 - \delta/2$, because $0 < \delta \leq 1/4$. $\square$

The proof of the theorem compares the prime sums at $X$ and at $X(1 + h)$. The main terms differ by $hX$. The exceptional term can cancel at most the part $hX(1 - \delta/2)$ of it, by the last lemma. What is left, $hX\delta/2$, is larger than the error terms when $h$ is not too small.

**Theorem 2.1.11 (Primes of the trivial class in short intervals).** There are $A, c, c' > 0$ with the following property. Let a family be given, let $X \geq 1$, and let $h$ satisfy $\log B \leq c\sqrt{\log X}$ and $e^{-c\sqrt{\log X}} \leq h \leq 1$. Then
$$\frac{c' h X}{B^A} \leq \sum_{\lfloor X \rfloor < n \leq \lfloor X(1+h) \rfloor} \lambda(0, n).$$

Lean: `GlobalTheory.Hk.ShortInt.trivialClass_shortInterval` (also `GlobalTheory.T.exists_lam_zero_sum_shortInterval_ge`, a second name).

*Proof.* Take $c_0$, $A$ and $c_9$ from the lemma on the choice of the exceptional sets, and $c_7, C$ from the theorem on prime sums for this $c_0$. We prove the theorem with the exponent $A + 1$, with
$$c = \min\Bigl(1, \frac{c_7}{2(A + 2)}, \frac{c_7 c_9}{24 C}\Bigr), \qquad c' = \frac{c_9}{4}.$$
Let $Y = X(1+h)$, $L = \sqrt{\log X}$ and $E = e^{-c_7 L}$. Since $B \geq 4$, we have $1 \leq \log B \leq cL \leq L$. So $\log X \geq 1$, $X \geq e$, and $X \leq Y \leq 2X$.

Step 1. Fix the sets $Z_\chi$. The theorem on prime sums applies at $u = X$ and at $u = Y$, since $\log B \leq \sqrt{\log X} \leq \sqrt{\log Y}$. Its error is at most $CXE$ at $X$ and $2CXE$ at $Y$. Sum over the $|G| \leq B$ characters and use orthogonality. Then for $u \in \{X, Y\}$,
$$\begin{aligned} \Bigl| |G| \sum_{n \leq u} \lambda(0, n) - u + \sum_\chi \sum_{\beta \in Z_\chi} \frac{u^\beta}{\beta} \Bigr| \leq B \cdot C u E. \end{aligned}$$

Step 2. Let $S = \sum_{\lfloor X \rfloor < n \leq \lfloor Y \rfloor} \lambda(0, n)$. Subtract the estimate at $X$ from the estimate at $Y$. This gives
$$\begin{aligned} |G|\, S &\geq (Y - X) - \sum_\chi \sum_{\beta \in Z_\chi} \Bigl(\frac{Y^\beta}{\beta} - \frac{X^\beta}{\beta}\Bigr) - 3BCXE. \end{aligned}$$
There is at most one exceptional zero in all the sets $Z_\chi$. Put $\delta = c_9/B^A$. Then $\delta \leq 1 - \beta$ for that zero, and the lemma on the exceptional zero bounds the double sum by $hX(1 - \delta/2)$. So $|G|\, S \geq hX\delta/2 - 3BCXE$.

Step 3. We show $3BCE \leq h\delta/4$. By $h \geq e^{-cL}$ and $B \leq e^{cL}$, it is enough to show $12 C B^{A+1} e^{-c_7 L} \leq c_9 e^{-cL}$. The exponent satisfies $c_7 L - cL - (A + 1)\log B \geq c_7 L - (A + 2)cL \geq c_7 L/2$. Also $L \geq 1/c \geq 24C/(c_7 c_9)$, so $e^{c_7 L/2} \geq c_7 L/2 \geq 12C/c_9$. This proves the claim.

Step 4. Steps 2 and 3 give $hX\delta/4 \leq |G|\, S \leq BS$. So $S \geq (c_9/4) hX/B^{A+1}$. $\square$

**Remark 2.1.12 (Formalization).** The four theorems on zeros are separate formal results, each stated in a file of its own and proved elsewhere in the development. They are below the level of the outline, so this chapter does not link to them, and we have not checked their proofs. In the definition of an exceptional set ([LamIdealOfNotPrimePow.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/LamIdealOfNotPrimePow.lean#L67)), condition 3 has no upper bound on $\mathrm{Re}\, s$, so it also says that $F_\chi$ has no zeros with $\mathrm{Re}\, s \geq 1$. The error in property 4 is $B^{10}t$, which tends to $0$ with $t$; it is not an exponentially small error. The function $m_\chi$ is defined by a Lebesgue integral for every $s$; we use it only where it converges.
