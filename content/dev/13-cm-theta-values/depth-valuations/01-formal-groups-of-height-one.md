---
title: Formal groups of height one
decls:
  - GlobalTheory.ConvSer.HeightOne.exists_iso_multiplicative
  - GlobalTheory.ConvSer.HeightOneInt.htOneIsGm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Formal groups of height one

This section proves that a one-dimensional formal group law of height one over the integers of $\mathbb{C}_p$ is isomorphic to the multiplicative formal group $\hat{\mathbb{G}}_m$. The isomorphism has integral coefficients and a unit linear coefficient. The proof does not use Lazard's classification. It builds the isomorphism from the torsion points of the formal group, as in the theory of Lubin and Tate. The result is used in the [next section](/entry/exists-m-chart/) to put a multiplicative chart on the formal group of a CM elliptic curve at a split prime.

### Height one and isomorphisms with the multiplicative group

Let $R$ be a commutative ring and let $F(X, Y) \in R[[X, Y]]$ be a one-dimensional formal group law ([formal group laws](/learn/formal-groups/#formal-group-laws)). The multiplicative formal group law is $\hat{\mathbb{G}}_m(X, Y) = X + Y + XY$.

**Definition 4.1.1.** The *$n$-series* of $F$ is the sequence of power series $[n]_F(X) \in R[[X]]$ with $[0]_F = 0$ and $[n+1]_F(X) = F([n]_F(X), X)$.

**Definition 4.1.2.** A power series $f \in R[[X]]$ is an *isomorphism from $F$ to $\hat{\mathbb{G}}_m$* if $f(0) = 0$, the coefficient of $X$ in $f$ is a unit of $R$, and
$$f(F(X, Y)) = f(X) + f(Y) + f(X) f(Y).$$

The last identity says that $f$ is a homomorphism from $F$ to $\hat{\mathbb{G}}_m$. A homomorphism with a unit linear coefficient has an inverse series, so it is an isomorphism.

Let $p$ be a prime. Let $\mathbb{C}_p$ be the completion of an algebraic closure of $\mathbb{Q}_p$, with its absolute value $\|\cdot\|$ and its ring of integers $\mathcal{O}_{\mathbb{C}_p}$, the elements of absolute value at most $1$ ([$p$-adic numbers](/learn/number-fields/#p-adic-numbers-and-local-fields)). A series over a valued field is *integral* if all its coefficients have absolute value at most $1$.

**Definition 4.1.3.** A formal group law $F$ over $\mathcal{O}_{\mathbb{C}_p}$ has *height one* if the coefficient of $X^p$ in $[p]_F(X)$ has absolute value $1$, and the coefficient of $X^k$ in $[p]_F(X)$ has absolute value less than $1$ for every $k < p$.

So the reduction of $[p]_F$ modulo the maximal ideal starts with a unit times $X^p$. This is the condition of [height](/learn/formal-groups/#height) one on the reduction. The law $\hat{\mathbb{G}}_m$ satisfies it, because $[p](X) = (1 + X)^p - 1$.

### The theorem over a complete field

**Theorem 4.1.4 (height one is multiplicative).** Let $K$ be a field of characteristic $0$ with a complete ultrametric absolute value, and assume $K$ is algebraically closed. Let $p$ be a prime. Let $F$ be a one-dimensional formal group law over $K$ with integral coefficients. Assume that the coefficient of $X^p$ in $[p]_F(X)$ has absolute value $1$, and that the coefficient of $X^k$ has absolute value less than $1$ for every $k < p$. Then there is an integral power series $f \in K[[X]]$ with $f(0) = 0$, with the coefficient of $X$ of absolute value $1$, and with
$$f(F(X, Y)) = f(X) + f(Y) + f(X) f(Y).$$

Lean: `GlobalTheory.ConvSer.HeightOne.exists_iso_multiplicative`.

*Proof.* We build $f$ from the torsion points of $F$. All series below converge on the open unit disc of $K$, because their coefficients are integral.

Step 1 (a torsion tower). There are points $t_0, t_1, t_2, \dots$ of $K$ with $\|t_n\| < 1$, $t_0 = 0$, $t_1 \neq 0$ and $[p]_F(t_{n+1}) = t_n$ for all $n$. To find $t_{n+1}$, solve $[p]_F(X) = t_n$. The height condition and the Weierstrass preparation theorem give $p$ roots in the open disc, counted with multiplicity. The field $K$ is algebraically closed, so the roots lie in $K$.

Step 2 (a tower of roots of unity). There are roots of unity $\zeta_1, \zeta_2, \dots$ in $K$ with $\zeta_1$ a primitive $p$-th root of unity and $\zeta_{n+1}^p = \zeta_n$. So $\zeta_n$ is a primitive $p^n$-th root of unity.

Step 3 (exact order). For integers $i, j \geq 0$, we have $[i]_F(t_n) = [j]_F(t_n)$ if and only if $i \equiv j \pmod{p^n}$. So the set $G_n = \{[j]_F(t_n) : 0 \leq j < p^n\}$ has exactly $p^n$ elements. It is a cyclic group under $F$, and $G_n \subseteq G_{n+1}$.

Step 4 (absolute values). We have $\|t_1\|^{p-1} = \|p\| < 1$. For $p^n \nmid j$ we have $\|t_1\| \leq \|[j]_F(t_n)\|$. The product of $\|[j]_F(t_n)\|$ over $1 \leq j < p^n$ equals $\|p\|^n$. This is the Newton polygon of $[p^n]_F$: its nonzero roots are the points $[j]_F(t_n)$, and its linear coefficient is $p^n$.

Step 5 (interpolation at level $n$). For each $n$ there is a polynomial $g_n$ with integral coefficients and $g_n([j]_F(t_n)) = \zeta_n^j$ for all $j$. The bounds of Step 4 control the denominators of the Lagrange interpolation.

Step 6 (the limit). The sets $G_n$ grow with $n$, their nonzero points satisfy $\|t_1\| \leq \|x\| < 1$, and the product of the absolute values of the nonzero points of $G_n$ tends to $0$. Under these conditions an integral power series $\varphi$ exists that agrees with $g_n$ on $G_n$ for every $n$. Put $f = \varphi - 1$. Then $f([j]_F(t_n)) = \zeta_n^j - 1$ for all $n$ and $j$. In particular $f(0) = 0$, and $f$ is integral.

Step 7 (the linear coefficient). The coefficient of $X$ in $f$ has absolute value at most $1$. Assume it is less than $1$. Compare $f(t_1) = \zeta_1 - 1$ with the expansion of $f$ at $t_1$. The bound $\|p\| \leq \|\zeta_1 - 1\|^{p-1}$, valid for a primitive $p$-th root of unity, and Step 4 give a contradiction. So the coefficient has absolute value $1$.

Step 8 (the homomorphism law). Put
$$H(X, Y) = f(F(X, Y)) - f(X) - f(Y) - f(X) f(Y).$$
It is an integral series in two variables. For $x = [i]_F(t_n)$ and $y = [j]_F(t_n)$ we have $F(x, y) = [i + j]_F(t_n)$, so
$$f(F(x, y)) + 1 = \zeta_n^{i+j} = (f(x) + 1)(f(y) + 1).$$
So $H$ vanishes on $G_n \times G_n$ for every $n$. An integral series in two variables that vanishes on all the products $G_n \times G_n$ is zero, by the same size estimates as in Step 6. So $H = 0$. $\square$

### The statement over the integers of $\mathbb{C}_p$

**Corollary 4.1.5 (height one over $\mathcal{O}_{\mathbb{C}_p}$).** Let $p$ be a prime and let $F$ be a one-dimensional formal group law over $\mathcal{O}_{\mathbb{C}_p}$. Assume that the coefficients of $F$ lie in a finite extension of $\mathbb{Q}_p$ inside $\mathbb{C}_p$, and that $F$ has height one. Then there is an isomorphism $f \in \mathcal{O}_{\mathbb{C}_p}[[X]]$ from $F$ to $\hat{\mathbb{G}}_m$.

Lean: `GlobalTheory.ConvSer.HeightOneInt.htOneIsGm`.

*Proof.* Map $F$ to $\mathbb{C}_p$ by the inclusion $\mathcal{O}_{\mathbb{C}_p} \subset \mathbb{C}_p$. The image has integral coefficients, and its $p$-series is the image of $[p]_F$, so it satisfies the hypotheses of the theorem. The field $\mathbb{C}_p$ is complete, ultrametric, algebraically closed and of characteristic $0$. The theorem gives an integral series $f$ over $\mathbb{C}_p$ with $f(0) = 0$, a linear coefficient of absolute value $1$, and the homomorphism law. Its coefficients lie in $\mathcal{O}_{\mathbb{C}_p}$. An element of $\mathcal{O}_{\mathbb{C}_p}$ of absolute value $1$ is a unit. The homomorphism law holds over $\mathcal{O}_{\mathbb{C}_p}$, because the inclusion into $\mathbb{C}_p$ is injective. $\square$

The proof does not use the hypothesis on the field of coefficients.

**Remark 4.1.6 (Formalization).** The formal group laws are those of the Mathlib type `FormalGroup`. We did not open its definition, so we did not check which axioms it contains. The corollary takes the hypothesis on the coefficients as an argument but does not use it ([IsIsoGmOfMap.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/IsIsoGmOfMap.lean#L57)). Steps 1 to 8 are separate lemmas of the same module.
