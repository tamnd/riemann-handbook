---
title: The window theorem at two and the minus part
decls:
  - UpperTheory.V.Win.thmBab_of_lemmaK
  - UpperTheory.V.Odd.thmBcFree_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The window theorem at two and the minus part

The [window bound](/entry/vwin-of-hypotheses-h-e-alt/) bounds the lengths of Tate-Shafarevich groups of the twists $\mathbb{Q}_l/\mathbb{Z}_l(e)$ over a family of abelian fields. Its proof splits each length into the part at $l = 2$ and, for odd $l$, the two [eigenspaces of complex conjugation](/learn/galois-cohomology/#plus-and-minus-parts). This section proves two of the resulting bounds. The first, Theorem B for windows, bounds the part at $l = 2$ and the parts over cyclotomic layers; it follows from Lemma K, the duality theorems and the theorem of Ferrero and Washington of [Theorem 4.1.11](/entry/ferrero-washington/). The second bounds the minus part, for every odd $l$; it follows from a bound for the eigenspaces of single characters by generalized Bernoulli numbers, which Sections 3 to 5 prove. Both are inputs of the count in [Theorem 8.16.7](/entry/of-four-alt/).

### Abelian fields and lengths

**Definition 4.2.1 (Abelian field data).** An *abelian field datum* $A$ is a modulus $m \geq 1$ and a subgroup $H \subset (\mathbb{Z}/m)^\times$. Its *degree* is the index of $H$. A number field $L$ is an *$A$-field* if there are $N$ with $m \mid N$, an embedding $j : L \to \mathbb{Q}(\zeta_N)$ and a primitive $N$-th root of unity $\zeta$ such that the automorphism $\zeta \mapsto \zeta^a$ fixes $j(L)$ if and only if $a \bmod m$ lies in $H$. The datum *has the $l$-th roots of unity* if $l \mid m$ and every $a$ in $H$ is $1$ modulo $l$; then each $A$-field contains $\mu_l$.

**Definition 4.2.2 (Compositum fields).** Let $A$ be an abelian field datum and let $e, q, d$ be integers. A number field $E$ is a *compositum field* for $(A, e, q, d)$ if there are $N$ divisible by $2^{e + 2}$, $m$, $q$ and $d$, an embedding $j : E \to \mathbb{Q}(\zeta_N)$ and a primitive root $\zeta$ of order $N$ such that $\zeta \mapsto \zeta^a$ fixes $j(E)$ if and only if $a \equiv \pm 1 \pmod{2^{e + 2}}$, $a \bmod m$ lies in $H$, and the Jacobi symbols $(a/q)$ and $(a/d)$ are $1$. The *conductor* $F(E)$ is the least $N$ with an embedding $E \to \mathbb{Q}(\zeta_N)$.

**Definition 4.2.3 (Layers).** Let $l$ be a prime and $j \geq 0$. An extension $L'/L$ is a *layer of height $j$* if $L'$ is generated over $L$ by the $l^k$-th roots of unity for some $k$ and $[L' : L] = l^j$.

**Definition 4.2.4 (Window pairs).** A pair of primes $(q, d)$ is *admissible for $m$* if $q \equiv 3 \pmod 8$, $d \equiv 7 \pmod{16}$ and $qd$ is prime to $m$.

For a number field $E$, a prime $l$, a choice $D$ of local data and $e \geq 1$, let $\ell_l(E, e)$ be the length of the Tate-Shafarevich group of $\mathbb{Q}_l / \mathbb{Z}_l(e)$ over $E$, as in [the window bound](/entry/vwin-of-hypotheses-h-e-alt/). When $E$ is a CM field and $l$ is odd, let $\ell^-_l(E, e)$ be the length of the eigenspace of complex conjugation for the eigenvalue $(-1)^{e + 1}$.

**Definition 4.2.5 (Bounded lengths).** Let $l$ be a prime, $E$ a number field, $t \geq 1$ and $B \in \mathbb{R}$. We say that *$E$ has lengths at most $B$ below $t$ at $l$* if, for every choice of local data, $\ell_l(E, e)$ is finite for $0 < e < t$ and
$$\sum_{e = 1}^{t - 1} \ell_l(E, e) \leq B .$$
For a CM field $E$ we say that *the minus lengths of $E$ below $t$ are at most $B$* if, for every family of local data at all primes, $\ell^-_p(E, e)$ is finite for odd $p$ and $0 < e < t$, and for every finite set $S$ of odd primes
$$\sum_{l \in S} \log l \sum_{e = 1}^{t - 1} \ell^-_l(E, e) \leq B .$$

### Theorem B for windows

**Definition 4.2.6 (Theorem B for windows).** A *constant system* $K$ is a function $R_0$ on abelian field data, a function $R_l$ on primes and abelian field data, and a real $C_K > 0$. For an abelian field datum $M$, a finite set $B'$ of primes and a function $L$ from primes to abelian field data, put
$$R = R_0(M) + \sum_{l \in B'} R_l(L(l)), \qquad J(C_t, \varepsilon) = 2^{R + 2} \Big(\frac{2 C_K C_t}{\varepsilon}\Big)^{R}.$$
A pair of functions $e, t$ from the reals to the integers is *admitted* for $(A_1, C_t)$ if for $x \geq 2$ we have $2 \leq e(x)$, $2^{e(x)} \leq x^{A_1}$, $2 \leq t(x)$ and $t(x) \leq x^{C_t}$. *Theorem B holds for $K$ and $C_t$* if the following is true. Let $M$, $B'$ and $L$ be as above, with each $l \in B'$ an odd prime and $L(l)$ with the $l$-th roots of unity. Let $0 < \varepsilon < 1/52$ and $A_1 \in \mathbb{R}$. There is $X_0$ such that for each admitted pair $(e, t)$, each $X \geq X_0$ and each admissible pair $(q, d)$ for $m(M)$ with $\log(qd) \leq X^{\varepsilon/(4J)}$, there is $Y$ with $X^{1/J} \leq Y$ and $Y^2 \leq X$ such that for each $x \in [Y, Y^2]$:

1. each compositum field $E$ for $(M, e(x), q, d)$ has lengths at most $\exp(x^{4\varepsilon/5})$ below $t(x)$ at $2$;
2. for each $l \in B'$, each $L(l)$-field $L_0$ and each layer $L_1/L_0$ of height $\lfloor \log_l R_l(L(l)) \rfloor + 3$, the field $L_1$ has lengths at most $\exp(x^{4\varepsilon/5})$ below $t(x)$ at $l$.

The next three statements are inputs from the literature, which the window bound takes as hypotheses. Poitou-Tate duality and local Tate duality are in [the global theory](/learn/galois-cohomology/#global-fields) and [the local theory](/learn/galois-cohomology/#local-fields) of Volume 1. Lemma K is the bound for $H^2$ of twisted $\mathbb{Z}_l$ over totally complex fields of [the window bound](/entry/vwin-of-hypotheses-h-e-alt/). Local finiteness is the finiteness of local Galois cohomology with finite coefficients.

**Theorem 4.2.7 (Theorem B for windows).** Assume Poitou-Tate duality, local finiteness, local Tate duality, the [Theorem 4.1.11](/entry/ferrero-washington/) of Ferrero and Washington, and Lemma K for some constant. Then there is a constant system $K$ such that Theorem B holds for $K$ and every $C_t \geq 1$.

Lean: `UpperTheory.V.Win.thmBab_of_lemmaK`.

*Proof.* The proof has two steps. First, a tower bound: for each prime $l$, each totally complex number field $L$ that contains $\mu_l$ (and $\mu_4$ if $l = 2$), and each $R \geq 1$ such that the Iwasawa module of the cyclotomic $\mathbb{Z}_l$-tower of $L$ is generated by $R$ elements over $\mathbb{Z}_l$, the lengths $\ell_l(L_1, e)$ over the layers $L_1$ of $L$ are bounded linearly in $R$ times the height of the layer, plus a term that depends on how close $e$ is $l$-adically to finitely many exceptional values. This uses Poitou-Tate duality, local finiteness and local Tate duality. Second, the theorem of Ferrero and Washington gives the generator bound $R$ uniformly. For $l = 2$, the base fields attached to $(M, q, d)$ are abelian fields with $\mu_4$, and the bounded $2$-rank of the class groups in the tower gives one $R$ for all admissible pairs $(q, d)$. For odd $l \in B'$, the $L(l)$-fields contain $\mu_l$, and the same argument gives $R$. With these bounds, the window statement follows from Lemma K by the choice of $Y$ in the range $[X^{1/J}, X^{1/2}]$, as in [the window bound](/entry/vwin-of-hypotheses-h-e-alt/). $\square$

### The minus part

**Definition 4.2.8 (The minus bound).** For $C \in \mathbb{R}$ and integers $o, n, N, t$ put
$$\begin{aligned} \beta(C; o, n, N, t) &= 3 n t^2 \log(tN) \\ &\quad + C \sum_{l \mid o, \ l \neq 2} l \, n^2 t^2 \log(t l N)^2 . \end{aligned}$$

**Definition 4.2.9 (The minus statement).** The *minus statement* holds if there is $C$ such that for each abelian field datum $M$, each $e \geq 2$, $t \geq 2$, each admissible pair $(q, d)$ for $m(M)$, and each CM compositum field $E$ for $(M, e, q, d)$, the minus lengths of $E$ below $t$ are at most $\beta(C; \deg M, [E : \mathbb{Q}], F(E), t)$.

The input from Sections 3 to 5 is a bound for the eigenspaces of single characters. Let $E$ be an abelian CM field, let $N \geq 1$ and let $\rho : (\mathbb{Z}/N)^\times \to \mathrm{Gal}(E/\mathbb{Q})$ be the cyclotomic action, so that $\rho(a)$ acts on roots of unity in $E$ by $\zeta \mapsto \zeta^a$. For a character $\psi$ of $\mathrm{Gal}(E / \mathbb{Q})$ let $\chi = \psi \circ \rho$, a [Dirichlet character](/learn/l-functions/#dirichlet-characters) modulo $N$.

**Definition 4.2.10 (Generalized Bernoulli numbers).** Let $B_k(X)$ be the $k$-th Bernoulli polynomial. For a function $\Phi$ on $\mathbb{Z}/N$ put $B_k(\Phi) = \sum_{a = 1}^{N} \Phi(a) N^{k - 1} B_k(a / N)$. For a Dirichlet character $\chi$, let $B_{k, \chi}$ be this sum for the primitive character attached to $\chi$, at its conductor. Put $a_{N, k}(\chi) = N \cdot (k + 1)\# \cdot B_{k, \chi}$, where $(k+1)\#$ is the product of the primes up to $k + 1$.

For $l$ prime, $O$ the ring of integers of a finite extension of $\mathbb{Q}_l$ in $\overline{\mathbb{Q}}_l$, $e \geq 1$ and $\psi : \mathrm{Gal}(E/\mathbb{Q}) \to O^\times$, let $\ell_\psi(E, e)$ be the length over $O$ of the $\psi$-eigenspace of the Tate-Shafarevich group of $O \otimes \mathbb{Q}_l/\mathbb{Z}_l$ twisted by $\chi_{\mathrm{cyc}}^{-e}$, over $E$ with its action of $\mathrm{Gal}(E/\mathbb{Q})$.

**Definition 4.2.11 (The character bound).** The *character bound* holds if for each abelian CM field $E$ with cyclotomic action $\rho$ modulo $N$, each odd prime $l$ that does not divide $[E : \mathbb{Q}]$, each $O$ as above, each $e \geq 1$ and each $\psi$ with $\chi(-1) = (-1)^{e + 1}$, and each $a \in O$ equal to $a_{N, e + 1}(\chi)$,
$$\ell_\psi(E, e) \leq v_O(a),$$
where $v_O$ is the normalized valuation of $O$.

**Theorem 4.2.12 (The minus part).** If the character bound holds, then the minus statement holds.

Lean: `UpperTheory.V.Odd.thmBcFree_of` (also `UpperTheory.V.Odd.primeBound_of`, `UpperTheory.V.Odd.stickBound`).

*Proof.* Let $E$ be a CM compositum field for $(M, e, q, d)$, let $n = [E : \mathbb{Q}]$ and $N = F(E)$, and let $S$ be a finite set of odd primes. Split $S$ into the primes that do not divide $n$ and those that divide $n$.

For $l \nmid n$, the group ring $O[\mathrm{Gal}(E/\mathbb{Q})]$ is a product of copies of $O$ after an extension of $O$, so the minus part is the sum of the $\psi$-eigenspaces over the characters $\psi$ with the right parity. The number of characters is at most $n$. The character bound bounds each eigenspace by the valuation of the Bernoulli number $a_{N, e+1}(\chi)$. Summing $\log l$ times these valuations over $l$ and the characters gives
$$\sum_{l} \log l \cdot \ell^-_l(E, e) \leq n \log \beta_0(N, e + 1), \qquad \beta_0(N, k) = 16 N^{k + 1} k!,$$
where $\beta_0(N, k)$ bounds the size of the numbers $a_{N, k}(\chi)$. For $e + 1 \leq t$ one has $\log \beta_0(N, e + 1) \leq (2t + 5) \log(tN)$. Summing over $1 \leq e \leq t - 1$ and using $(t - 1)(2t + 5) \leq 3 t^2$ gives the first term $3 n t^2 \log(tN)$ of $\beta$.

For an odd $l \mid n$, $l$ divides the degree of $M$, since the other factors of $n$ come from the $2$-power part and the quadratic characters of $q$ and $d$. For these primes a Stickelberger bound holds: there is $C \geq 0$ such that for each CM field $E$ inside $\mathbb{Q}(\zeta_N)$, each prime $l$ and each $e \geq 1$,
$$\ell^-_l(E, e) \log l \leq C \, l \, n^2 (e + 1) \log(e l N)^2 .$$
Summing over $1 \leq e \leq t - 1$ gives at most $C l n^2 t^2 \log(t l N)^2$, the term of $\beta$ for $l$. Adding the two parts gives the minus statement. $\square$

**Remark 4.2.13 (Formalization).** In [ThmBabOfLemmaK.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/ThmBabOfLemmaK.lean#L9) the conclusion holds for every $C_t \geq 1$, while the count in [Theorem 8.16.7](/entry/of-four-alt/) uses only $C_t = 401$. The tower bound is `UpperTheory.V.PropA.aBound_of_isTower`, and the Iwasawa module in it is not unfolded here; the generator bounds are `towerTwo` and `towerFixed` in [IsAlgClosureRat.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/QuadraticExtensions/IsAlgClosureRat.lean#L87). The module name of [ThmBcOfPsiBound.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/OddResidueBounds/ThmBcOfPsiBound.lean#L295) names the older statement; the theorem proves the free form `ThmBcFree`, in which $e$ and $t$ are integers and not functions. The divisibility $l \mid \deg M$ is the lemma `deg`, and the inputs `actEx`, `actFacts`, `prodVal`, `atPrime`, `killPow`, `lenPow` and `gen` are not unfolded here. The Stickelberger bound holds under an extra condition on the local data at $l$ (`Procyc`), which is also not unfolded.
