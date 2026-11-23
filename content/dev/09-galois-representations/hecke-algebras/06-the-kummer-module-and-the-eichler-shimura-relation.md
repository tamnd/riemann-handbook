---
title: The Kummer module and the Eichler and Shimura relation
decls:
  - GlobalTheory.T.eichlerShimura_frobenius_quadratic_mod_prime_pow
  - GlobalTheory.cayleyHamilton_galV
  - GlobalTheory.T.cayleyHamilton_heckeEigenvector_every_galois_element
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Kummer module and the Eichler and Shimura relation

This section builds an $l$-adic module from the Kummer classes of modular functions, with an action of the Hecke operators and of $\mathrm{Gal}(\Omega/\mathbb{Q})$. It plays the role of the étale cohomology of a modular curve with coefficients in a symmetric power. On this module a Frobenius element at $q$ satisfies the Eichler and Shimura congruence relation $\mathrm{Frob}_q^2 - T_q \mathrm{Frob}_q + q^{w+1}\langle q \rangle = 0$ modulo every power of $l$, outside a finite set of primes depending on the power. From this and the Chebotarev density theorem we get a Cayley and Hamilton relation for every Galois element on Hecke eigenvectors. The relation is the key input of [the Galois image theorem](/entry/hecke-proj-main/), which builds a two dimensional Galois representation on the eigenspace.

Fix a tower of modular functions $(K, \exp, |, s, \mathrm{an}, j_K)$ over $(\Omega, \varepsilon)$ as in [the existence theorem for towers](/entry/tower-exists/), with $\Omega$ an algebraic closure of $\mathbb{Q}$. Fix a prime $l$ and integers $N \geq 1$, $w \geq 0$.

**Definition 6.6.1 (Kummer module).** Let $K^\times_l = \mathbb{Z}_l \otimes_{\mathbb{Z}} K^\times$, written additively, and let $\widehat{K}_l$ be its $l$-adic completion, $\widehat{K}_l = \varprojlim_n K^\times_l / l^n$. For $f \in K^\times$ let $[f]_n$ be the class of $1 \otimes f$ in $K^\times_l / l^n$.

1. For $m \geq 1$, let $\mathrm{Un}(m)$ be the set of $f \in K^\times$ such that, for every valuation ring $W$ of $K$ that contains $\Omega$ and $j_K$, there is $g \in K^\times$ with $f/g^m$ a unit of $W$.
2. Let $\mathcal{A}$ be the $\mathbb{Z}_l$-span of the $a \in \widehat{K}_l$ such that for every $n$ there is $f \in \mathrm{Un}(l^n)$ with $a \equiv [f]_n$ modulo $l^n$.

So $f \in \mathrm{Un}(l^n)$ means that the divisor of $f$ on the curve over the $j$-line, away from the cusps, is divisible by $l^n$. By Kummer theory, such an $f$ gives a class in the étale cohomology $H^1(Y, \mu_{l^n})$ of the open modular curve $Y$. So $\mathcal{A}$ is an $l$-adic model of $\varprojlim_n H^1(Y, \mu_{l^n})$ over all levels at once.

**Definition 6.6.2 (Polynomial coefficients and the action).** Let $\mathcal{F}$ be the $\mathbb{Z}_l$-module of maps $\mathbb{Z}_l^2 \to \widehat{K}_l$. Let $\mathrm{Pol}_w \subseteq \mathcal{F}$ be the set of maps
$$
b(u_0, u_1) = \sum_{i=0}^{w} u_0^i u_1^{w-i} c_i \qquad \text{with } c_i \in \mathcal{A}.
$$
An integer matrix $m$ with positive determinant acts on $\mathcal{F}$ by $(m_* b)(u) = (b(m u))|m$, where $m u$ is the product of a matrix and a column vector, and $|m$ is induced on $\widehat{K}_l$ by the automorphism $f \mapsto f|m$ of $K$. Let $\Gamma = \Gamma_1(N) \cap \Gamma_0(l)$. The *Kummer module* $\mathcal{B}$ is the $\mathbb{Z}_l$-span of the $b \in \mathrm{Pol}_w$ with $\gamma_* b = b$ for all $\gamma \in \Gamma$.

The Hecke letters of [the previous section](/entry/ss-pot-b-at-newform/) act on $\mathcal{F}$ by the same matrix sums: $T_q$ by $\sum_{j<q} \begin{pmatrix} 1 & j \\ 0 & q \end{pmatrix}_* + \bigl(\sigma_q \begin{pmatrix} q & 0 \\ 0 & 1 \end{pmatrix}\bigr)_*$, $U$ by $\sum_{j<l} \begin{pmatrix} 1 & j \\ 0 & l \end{pmatrix}_*$, and $\langle d \rangle$ by $(\sigma_d)_*$.

**Definition 6.6.3 (Galois action).** Let $\chi_l : \mathrm{Gal}(\Omega/\mathbb{Q}) \to \mathbb{Z}_l^\times$ be the [cyclotomic character](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules). For $s \in \mathrm{Gal}(\Omega/\mathbb{Q})$ and $b \in \mathcal{F}$ put
$$
(s_* b)(u_0, u_1) = s\bigl(b(u_0, \chi_l(s) u_1)\bigr),
$$
where $s$ acts on $\widehat{K}_l$ through its action on $K$.

**Definition 6.6.4 (Frobenius element).** Let $q$ be a prime. An element $s \in \mathrm{Gal}(\Omega/\mathbb{Q})$ is a *Frobenius at $q$* if there is a valuation ring $V$ of $\Omega$ with $q$ in its maximal ideal such that $s(V) \subseteq V$ and $s(x) \equiv x^q$ modulo the maximal ideal for all $x \in V$.

These are the [Frobenius elements](/learn/galois-representations/#decomposition-groups-inertia-and-frobenius) of Volume 1, for any place of $\Omega$ above $q$, with no condition on inertia.

Four facts about $\mathcal{B}$ are proved in the development and used below. Assume $l \neq 2$, $N \geq 5$, $\gcd(N, l) = 1$ and $w$ odd. Then: $\mathcal{B}$ is a free $\mathbb{Z}_l$-module of finite rank; $\mathcal{B}$ is stable under $s_*$ for every $s$ and under every admitted letter; the admitted letters commute with every $s_*$ on $\mathcal{B}$; and $s \mapsto s_*$ is continuous, in the sense that for each $n$ there is a finite set $E_0 \subset \Omega$ such that $s'_* \equiv 1$ on $\mathcal{B}$ modulo $l^n$ when $s'$ fixes $E_0$.

**Theorem 6.6.5 (Eichler and Shimura relation modulo prime powers).** Let $\Omega$ be an algebraic closure of $\mathbb{Q}$, $\varepsilon : \Omega \to \mathbb{C}$ injective, and fix a tower over $(\Omega, \varepsilon)$ whose $j$-function has a holomorphic germ. Let $l \neq 2$ be a prime, $N \geq 5$ with $\gcd(N, l) = 1$, and $w$ odd. Then for every $n \geq 0$ there is a finite set $S$ of primes such that for every prime $q \notin S$, every Frobenius $s$ at $q$, every $b \in \mathcal{B}$ and every $u \in \mathbb{Z}_l^2$,
$$
\bigl(s_* s_* b - T_q s_* b + q^{w+1} \langle q \rangle b\bigr)(u) \in l^n \widehat{K}_l.
$$

Lean: `GlobalTheory.T.eichlerShimura_frobenius_quadratic_mod_prime_pow`.

*Proof.* *Reduction to generators.* The module $\mathcal{B}$ is finitely generated, so it has a finite set $G$ of generators, each a $\Gamma$-invariant element of $\mathrm{Pol}_w$. It suffices to find, for each $b \in G$, a finite set $S_b$ such that a modified relation holds for $q \notin S_b$:
$$
\bigl(s_* b - T_q b + q^{w+1} (s^{-1})_* \langle q \rangle b\bigr)(u) \in l^n \widehat{K}_l. \tag{$*$}
$$
Indeed, the left side of $(*)$ is linear in $b$, so $(*)$ then holds on all of $\mathcal{B}$ for $q$ outside the union of the $S_b$ and the primes dividing $Nl$. For such $q$ the letter $T_q$ is admitted and commutes with $s_*$. Applying $s_*$ to $(*)$ gives $s_* s_* b - T_q s_* b + q^{w+1} \langle q \rangle b$, and $s_*$ preserves $l^n \widehat{K}_l$.

*Choice of a level.* Write $b = \sum_i u_0^i u_1^{w-i} c_i$. Each $c_i \in \mathcal{A}$ has a representative modulo $l^n$ of the form $[f_i]_n$ with $f_i \in \mathrm{Un}(l^n)$, and each $f_i$ is fixed by some $\Gamma(m_i)$. Put $M = N l \cdot l^n \cdot \prod_i m_i$.

*The Kummer congruence.* The key input is a Kummer form of the Eichler and Shimura congruence for one function. For $f \in \mathrm{Un}(l^n)$ fixed by $\Gamma(M)$, with $l \mid M$, there is a finite set $S_f$ such that for every prime $q \notin S_f$, every Frobenius $s$ at $q$, and every $\sigma \in \mathrm{SL}_2(\mathbb{Z})$ with $\sigma \equiv \begin{pmatrix} * & 0 \\ 0 & q \end{pmatrix}$ modulo $M$, there is $g \in K^\times$ with
$$
\prod_{j=0}^{q-1} f\Big|\begin{pmatrix} 1 & jM \\ 0 & q \end{pmatrix} \cdot f\Big|\sigma \begin{pmatrix} q & 0 \\ 0 & 1 \end{pmatrix} = s(f) \cdot \bigl(s^{-1}(f|\sigma)\bigr)^q \cdot g^{l^n}.
$$
This is the Eichler and Shimura congruence relation, which says that the correspondence $T_q$ on the reduction modulo $q$ of the modular curve is the sum of the Frobenius and its transpose twisted by $\langle q \rangle$, written for functions. Let $S_b$ be the union of the sets $S_{f_i}$ and the primes dividing $M$.

*Comparison.* Let $q \notin S_b$ be prime, and let $s$ be a Frobenius at $q$. As $q \nmid M$, there is $\sigma \in \mathrm{SL}_2(\mathbb{Z})$ with $\sigma \equiv \begin{pmatrix} * & 0 \\ 0 & q \end{pmatrix}$ modulo $M$. Then $\sigma$ is a diamond matrix for $q$, and $\sigma \equiv \begin{pmatrix} q^{-1} & 0 \\ 0 & q \end{pmatrix}$ modulo $l^n$. Since $q \neq l$, $\chi_l(s) = q$. As $\gcd(M, q) = 1$, the numbers $jM$ run over the residues modulo $q$, so the upper triangular matrices of $T_q$ can be replaced by $\begin{pmatrix} 1 & jM \\ 0 & q \end{pmatrix}$, and $\langle q \rangle b = \sigma_* b$. Now evaluate the three terms of $(*)$ at $u$. The term $\begin{pmatrix} 1 & jM \\ 0 & q \end{pmatrix}_* b$ at $u$ is congruent modulo $l^n$ to the coefficients $c_i$ slashed by this matrix, evaluated at $(u_0, q u_1)$, since $jM \equiv 0$. The term $(\sigma \mathrm{diag}(q, 1))_* b$ at $u$ is congruent to the slashed coefficients at $(u_0, q u_1)$, since $\sigma\, \mathrm{diag}(q,1) \equiv \mathrm{diag}(1, q)$. The term $s_* b$ at $u$ is $s$ applied to the coefficients at $(u_0, q u_1)$. The last term uses $q^w b(x) = b(q x)$, as $b$ is homogeneous of degree $w$. So all terms are evaluations of $b$ at the same point $v = (u_0, q u_1)$, up to $l^n$. The Kummer congruence, applied to each $f_i$ and passed to classes modulo $l^n$, kills the sum of their coefficients. This proves $(*)$. $\square$

To pass from Frobenius elements to all of $\mathrm{Gal}(\Omega/\mathbb{Q})$ we extend scalars. Let $E$ be an algebraically closed field with an absolute value and a map $\mathbb{Z}_l \to E$ that preserves the absolute value. Put $\mathcal{B}_E \subseteq E \otimes_{\mathbb{Z}_l} \mathcal{F}$ for the image of $E \otimes \mathcal{B}$, and let the letters and $s_*$ act on $E \otimes \mathcal{F}$ by base change.

**Theorem 6.6.6 (Cayley and Hamilton on Hecke eigenvectors).** Keep the hypotheses of the last theorem, and let $E$ be as above. Let $\lambda$ be an eigensystem with values in $E$, let $t, d : \mathrm{Gal}(\Omega/\mathbb{Q}) \to E$, and let $S_0$ be a finite set of primes. Assume:

1. $t$ and $d$ are uniformly continuous: for every $\delta > 0$ there is a finite $E_0 \subset \Omega$ with $|t(ss') - t(s)| < \delta$ and $|d(ss') - d(s)| < \delta$ whenever $s'$ fixes $E_0$;
2. for every prime $q \notin S_0$ and every Frobenius $s$ at $q$, $t(s) = \lambda(T_q)$ and $d(s) = q^{w+1}\lambda(\langle q \rangle)$.

Let $x \in \mathcal{B}_E$ with $T x = \lambda(T) x$ for every admitted letter $T$. Then for every $s \in \mathrm{Gal}(\Omega/\mathbb{Q})$,
$$
s_* s_* x - t(s)\, s_* x + d(s)\, x = 0.
$$

Lean: `GlobalTheory.cayleyHamilton_galV` (also `GlobalTheory.T.cayleyHamilton_heckeEigenvector_every_galois_element`, a second name).

*Proof.* Choose a $\mathbb{Z}_l$-basis of $\mathcal{B}$ and write $s_*$ as a matrix $A(s)$ with entries in $\mathbb{Z}_l$. Write $x$ in the induced basis of $\mathcal{B}_E$.

*At Frobenius elements.* Let $q \notin S_0 \cup S$ and let $s$ be a Frobenius at $q$, with $S$ the set of the last theorem for a given $n$. Since the letters commute with $s_*$ and $x$ is an eigenvector, $T_q s_* x = s_* T_q x = \lambda(T_q) s_* x$ and $\langle q \rangle x = \lambda(\langle q \rangle) x$. The last theorem, base changed to $E$, gives
$$
\bigl| s_* s_* x - t(s)\, s_* x + d(s)\, x \bigr| \leq |l|^n \cdot C
$$
for a constant $C$ that depends only on $x$, as the entries of $A(s)$ are bounded by $1$.

*Density.* Let $s$ be arbitrary and let $\delta > 0$. Choose $n$ with $|l|^n C < \delta$, and $E_0$ so large that $A(s')\equiv 1$ modulo $l^n$ and $t$, $d$ move by less than $\delta$ when $s'$ fixes $E_0$. By the [Chebotarev density theorem](/learn/galois-representations/#decomposition-groups-inertia-and-frobenius), there are $s'$ fixing $E_0$ and a prime $q \notin S_0 \cup S$ such that $s s'$ is a Frobenius at $q$. Apply the last step to $s s'$ and compare with $s$: each term changes by at most a constant times $\delta$. As $\delta$ is arbitrary, the relation holds for $s$. $\square$

The relation says that on the eigenspace each $s_*$ satisfies the quadratic polynomial $X^2 - t(s) X + d(s)$. When $t$ and $d$ are the trace and determinant of a representation $\rho$, it is the Cayley and Hamilton relation for $\rho(s)$, transported to the eigenspace.

**Remark 6.6.7 (Formalization).** All the theorems of this section assume that $\varepsilon$ is injective and that the germ of $j_K$ is the germ of a holomorphic function ([CayleyHamiltonHeckeEigenvectorEveryGaloisElement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/CayleyHamiltonHeckeEigenvectorEveryGaloisElement.lean#L135)). Both hold automatically: a ring map from a field is injective, and the holomorphy of the germ of $j_K$ is a law of every tower ([ExpUpper.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ExpUpper.lean#L89)). The first theorem is a wrapper of `GlobalTheory.KZ.eichlerShimura_B_mod` under `maxHeartbeats 1000000`. The diamond matrix $\sigma_d$ is chosen in $\Gamma_0(N) \cap \Gamma_0(l)$, while the cocycle operators of Section 3 use $\Gamma_0(Nl)$; for $\gcd(N, l) = 1$ these groups are equal. The Kummer congruence for one function, the four facts on $\mathcal{B}$ and the Chebotarev step (which uses a published density theorem) were read as statements.
