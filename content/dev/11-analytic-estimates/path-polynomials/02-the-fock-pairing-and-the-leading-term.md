---
title: The Fock pairing and the leading term
decls:
  - Formalism.GM.leadingTermLemmas.real_mono
  - Formalism.GM.gamma_leading_term
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Fock pairing and the leading term

This section sets up the polynomial objects of the chapter: letters, the Fock pairing with its monomial factorials, and the tie operators $E$, $F$ and $\Phi$ that join a vector letter to a covector letter. It then proves the leading term theorem. A tie joins a vector letter of degree $o$ to a new covector letter of degree $n$; the Fock pairing of $\Phi(f)$ with $f'$, suitably normalized, is a polynomial in $n$, and its top coefficient is a Fock pairing of the initial parts of $f$ and $f'$. This is used by [the theorem on the mean of the ratios](/entry/mean-gam-x/).

We use [binomial coefficients, factorials and divided powers](/learn/combinatorics/#binomial-coefficients-factorials-and-divided-powers), [polynomials](/learn/algebra/#polynomials-and-power-series) and [the Fock model](/learn/theta/#the-fock-model) as motivation.

**Definition 7.2.1 (Letters and polynomials of a multidegree).** A *word of letters* of length $N$ is a sequence of letters $0, \dots, N - 1$; each letter $i$ is a *vector* or a *covector* letter and has a degree $d_i \in \mathbb{N}$. Fix $r \geq 1$. To letter $i$ we attach the variables $x_{i,0}, \dots, x_{i,r-1}$. A monomial $x^m$ has *multidegree* $(d_i)$ if $\sum_c m(i, c) = d_i$ for every $i$. We write $\operatorname{Pol}(L)$ for the $\mathbb{Q}_p$-span of these monomials, and $|L| = \sum_i d_i$ for the total degree.

A polynomial in $\operatorname{Pol}(L)$ is a multihomogeneous polynomial function of $N$ vectors of $\mathbb{Q}_p^r$, of degree $d_i$ in the $i$-th one. The group $\mathrm{GL}_r$ acts on vector letters by the standard representation and on covector letters by its dual. For $j \leq N$ and $c, d < r$ the operator
$$E^{(j)}_{cd} = \sum_{i < j,\ i \text{ vector}} x_{i,c} \partial_{i,d} - \sum_{i < j,\ i \text{ covector}} x_{i,d} \partial_{i,c}$$
is the action of the matrix unit $e_{cd} \in \mathfrak{gl}_r$ on the first $j$ letters.

**Definition 7.2.2 (Fock pairing).** For polynomials $F = \sum_m F_m x^m$ and $G = \sum_m G_m x^m$ over a field $K$ of characteristic zero, put
$$\langle F, G \rangle = \sum_m F_m G_m\, m!, \qquad m! = \prod_{k} m(k)!.$$
For $F, G \in \operatorname{Pol}(L)$ the *normalized pairing* is $\langle F, G \rangle_L = \langle F, G \rangle / \prod_i d_i!$.

The weight $m!$ is the squared norm of $x^m$ in the Fock model. It makes multiplication by $x_k$ adjoint to $\partial / \partial x_k$:
$$\langle x_k F, G \rangle = \langle F, \partial_k G \rangle.$$
Indeed, both sides pair $x^m$ with $x^{m + e_k}$ with weight $(m(k) + 1)\, m! = (m + e_k)!$.

**Definition 7.2.3 (Tie operators).** Let $w = (w_c)_{c < r}$ and $e = (e_c)_{c < r}$ be two disjoint families of $r$ distinct variables. Put
$$E = \sum_{c} x_{w_c} x_{e_c}, \qquad F = \sum_c \partial_{w_c} \partial_{e_c},$$
where $E$ acts by multiplication. For $o, n, z \in \mathbb{N}$ the *tie operator* is
$$\Phi_{o,n,z} = \sum_{j=0}^{o} \frac{(-1)^j}{(j!)^2 \binom{o + n + r + z - 1}{j}} E^j F^j.$$

Think of $w$ as the variables of a vector letter of degree $o$ and $e$ as those of a covector letter of degree $n$. Then $E$ is the invariant pairing of the two letters, $F$ is the contraction, and $F$ is the adjoint of $E$ for the Fock pairing. The parameter $z$ is a shift; it comes from an extra pair of scalar variables in Section 3.

**Lemma 7.2.4 (Action on levels).** Let $K$ have characteristic zero and $r \geq 1$. Let $o, n, z, l \in \mathbb{N}$ with $l \leq o$ and $l \leq n$, and let $u$ be a polynomial with $F u = 0$ whose monomials all have degree $o - l$ in the $w$ variables and $n - l$ in the $e$ variables. Then
$$\Phi_{o,n,z}(E^l u) = \frac{\binom{z + l}{l}}{\binom{o + n + r + z - 1}{l}}\, E^l u.$$

Lean: `Formalism.GM.levelAct`.

*Proof.* On a polynomial $u$ with $Fu = 0$ of bidegree $(a, b)$, the operators $E$, $F$ and the degree operator form an $\mathfrak{sl}_2$-triple, and $F E^{k} u = k(a + b + r + k - 1) E^{k-1} u$. So $F^j E^l u$ is $0$ for $j > l$ and is an explicit product of these factors times $E^{l - j} u$ for $j \leq l$. Inserting this in the definition of $\Phi$ gives a finite alternating sum of products of binomial coefficients. This sum equals $\binom{z + l}{l} / \binom{o + n + r + z - 1}{l}$ by an alternating binomial identity. $\square$

The factor is $1$ for $l = 0$ and is never $0$, so $\Phi_{o,n,z}$ rescales each level $E^l u$ by a nonzero number. The same computation shows that the operator with $\binom{o + n + r - 2}{j}$ in place of $\binom{o + n + r + z - 1}{j}$ (formally $z = -1$) is the harmonic projection: it fixes the polynomials $u$ with $F u = 0$ and kills the vectors $E^l u$ with $l \geq 1$. For instance, for $l = 1$ we have $F E u = (o + n + r - 2) u$, so $E u - \frac{1}{o + n + r - 2} E F E u = 0$.

**Definition 7.2.5 (Freezing).** Let $L$ be a word of $N + 1$ letters whose last letter $N$ is a vector letter, and fix $\rho < r$. For $n \geq |L|$ let $L^{+n}$ be the word $L$ followed by a covector letter of degree $n$. The *freezing* of $f \in \operatorname{Pol}(L)$ is the polynomial
$$\operatorname{frz}_n(f) = x_{N,\rho}^{\,n - |L|}\, f(\theta)$$
in the variables of the first $N + 1$ letters (the new letter carries the index $N + 1$ in $L^{+n}$, and $x_{N,c}$ are the variables of the last letter of $L$). Here $f(\theta)$ substitutes, for a vector letter $i$, $x_{i,\rho} \mapsto \sum_{c'} x_{i,c'} x_{N,c'}$ and $x_{i,c} \mapsto x_{N,\rho} x_{i,c}$ for $c \neq \rho$; and for a covector letter $i$, $x_{i,\rho} \mapsto x_{N,\rho} x_{i,\rho}$ and $x_{i,c} \mapsto x_{N,\rho} x_{i,c} - x_{i,\rho} x_{N,c}$ for $c \neq \rho$.

**Definition 7.2.6 (The ratio $\Gamma$).** Let $L$, $\rho$ be as above, $o = d_N$ the degree of the last letter, $S = |L|$ and $z \in \mathbb{N}$. For $f, f' \in \operatorname{Pol}(L)$ and $n \in \mathbb{N}$ put
$$\Gamma_n(f, f') = \frac{\binom{o + n + r + z - 1}{o} \,\bigl\langle \Phi_{o,n,z}(\operatorname{frz}_n f),\ \operatorname{frz}_n f' \bigr\rangle}{(n - S)!\, S!\, \prod_i d_i!},$$
where $\Phi$ is the tie operator between the last letter of $L$ (degree $o$) and the new letter (degree $n$), and $n - S$ is truncated at $0$.

A polynomial $f$ has *order* $e$ in the variable $x_{N,\rho}$ if every monomial of $f$ has degree at least $e$ in $x_{N,\rho}$, and some monomial has degree exactly $e$. Its *initial part* $\operatorname{in}_e f$ is the sum of the terms of $f$ with degree exactly $e$ in $x_{N,\rho}$.

**Lemma 7.2.7 (Monomials over the reals).** Let $r \geq 1$, let the last letter $N$ of $L$ be a vector letter, $z, e \in \mathbb{N}$, and let $x^m, x^{m'}$ be monomials of multidegree $L$ with $e \leq m(N, \rho)$ and $e \leq m'(N, \rho)$. Over $K = \mathbb{R}$,
$$\lim_{n \to \infty} \frac{\Gamma_n(x^m, x^{m'})}{n^{S + o - e}} = \frac{e!\, \binom{z + e}{e}\, \langle \operatorname{in}_e x^m, \operatorname{in}_e x^{m'} \rangle}{o!\, S!\, \prod_i d_i!}.$$

Lean: `Formalism.GM.leadingTermLemmas.real_mono`.

*Proof.* Expand $\Phi_{o,n,z} = \sum_{j \leq o} c_j(n) E^j F^j$ and use the adjointness of $E$ and $F$: the $j$-th term is $c_j(n) \langle F^j \operatorname{frz}_n x^m, F^j \operatorname{frz}_n x^{m'} \rangle$. The contraction $F$ acts on the power $x_{N,\rho}^{n - S}$ and on the substituted variables; each application costs a factor of size $O(n)$ when it hits the high power of $x_{N,\rho}$. The factorial weight of $x_{N,\rho}^{n - S + k}$ in the Fock pairing is $(n - S + k)!$, and after division by $(n - S)!$ it grows like $n^{k}$. Collecting the powers of $n$, each term of the sum is a real rational function of $n$, and the term of top degree $S + o - e$ comes from the monomials of degree exactly $e$ in $x_{N,\rho}$. The sum over $j$ of the top coefficients is an alternating sum of binomial coefficients equal to $e! \binom{z + e}{e} / o!$. $\square$

**Theorem 7.2.8 (Leading term).** Let $r \geq 1$, let the last letter $N$ of $L$ be a vector letter, $\rho < r$ and $z, e \in \mathbb{N}$. Let $f, f' \in \operatorname{Pol}(L)$ over $\mathbb{Q}_p$ both have order $e$ in $x_{N,\rho}$. Let $P \in \mathbb{Q}_p[T]$ satisfy $\Gamma_n(f, f') = P(n)$ for all $n \geq S$. Then the coefficient of $T^{S + o - e}$ in $P$ is
$$\frac{e!\, \binom{z + e}{e}\, \langle \operatorname{in}_e f, \operatorname{in}_e f' \rangle}{o!\, S!\, \prod_i d_i!}.$$

Lean: `Formalism.GM.gamma_leading_term`.

*Proof.* Expand $f$ and $f'$ in monomials. By bilinearity $\Gamma_n(f, f') = \sum_{m, m'} f_m f'_{m'} \gamma_{m,m'}(n)$, where $\gamma_{m,m'}(n) = \Gamma_n(x^m, x^{m'})$ computed over $\mathbb{Q}$. Each $\gamma_{m,m'}$ is a rational number, since all operators and weights have rational coefficients. The coefficients $f_m f'_{m'}$ are $p$-adic, so we pass to rational numbers: for each $\mathbb{Q}$-linear map $\psi : \mathbb{Q}_p \to \mathbb{Q}$, the function $n \mapsto \psi(\Gamma_n(f, f'))$ is $\sum f_m f'_{m'}$ replaced by $\psi$-images, and it agrees for $n \geq S$ with the polynomial $\psi(P)$ with rational coefficients. Its quotient by $n^{S + o - e}$ has, over $\mathbb{R}$, the limit given by the [Lemma (Monomials over the reals)](/entry/real-mono/) term by term. Since all monomials of $f, f'$ have degree at least $e$ in $x_{N,\rho}$, the lemma applies to all of them, and the terms of degree exactly $e$ give $\langle \operatorname{in}_e f, \operatorname{in}_e f' \rangle$. If a rational polynomial $R$ satisfies $R(n)/n^{D} \to \lambda$, then $R$ has degree at most $D$ and its $D$-th coefficient is $\lambda$. So the coefficient of $T^{S + o - e}$ in $\psi(P)$ is $\psi$ of the claimed value. Two elements of $\mathbb{Q}_p$ with the same image under every $\mathbb{Q}$-linear map to $\mathbb{Q}$ are equal. $\square$

**Remark 7.2.9 (Formalization).** The lemma over the reals asks only $e \leq m(N, \rho)$; the initial part `inMono` of a monomial is zero when the degree is larger than $e$, and the statement covers this case. The real and rational versions of $\Gamma$ are a second definition `gamK` next to `tieGam`, with the same formula. The step from limits to coefficients is `coeff_of_tendsto` ([GamLead.lean](lean:Formalism/MahlerMeasure/MahlerMeasureProofs/GamLead.lean#L1241)). We did not read the proof of the lemma over the reals line by line; the sketch above gives its structure. The proof of the level lemma is `levelAct_of alternatingChooseSum`, with the alternating binomial identity as a separate result.
