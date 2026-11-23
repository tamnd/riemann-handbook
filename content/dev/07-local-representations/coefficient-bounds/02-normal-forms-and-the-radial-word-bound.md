---
title: Normal forms and the radial word bound
decls:
  - GlobalTheory.T.wordOperator_radial_pointwise_bound
  - GlobalTheory.HatNF.RadBound.word_bound
  - GlobalTheory.T.basicOperators_polynomialLift_no_inversePower
  - GlobalTheory.HatNF.basicLiftAll_zero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Normal forms and the radial word bound

The local terms of a coefficient are built from derivatives along words of differential operators. To bound them near the boundary hypersurface, we move to the radial picture, where a coefficient becomes a radial function and each word becomes an element of an algebra of radial operators. This section proves two things there. First, a word operator applied to a radial function times a multiplier is bounded at each radial point by explicit negative powers of two distances, times the norms of finitely many fixed operators applied to the function. Second, every basic element of the normal form is the radial part of a differential operator on $G$ with polynomial coefficients, with no inverse power of the boundary function. The next section moves the first bound back to the group, and the second one fixes the exponent $a = 0$ there.

### The radial picture

We keep the place data of the first section. A *radial function* $\Phi$ assigns to each radial point $x = (c, g)$ a Hilbert-Schmidt operator $\Phi(x)$, and $\|\Phi(x)\|$ is its Hilbert-Schmidt norm. Let $\mathcal{A}$ be the algebra of radial operators of the place; it acts on radial functions. A radial point carries two sizes:
$$d_R(x) = \Bigl|\prod_a c_a\, \zeta(g)\Bigr|, \qquad g_R(x) = \Bigl|\prod_a c_a\Bigr|^2 G(g),$$
where $\zeta$ and $G$ are two functions of the place that we have not unfolded. Near the boundary $g_R$ tends to $0$.

For a function $\varphi$ on $(0, \infty)$ and $j \in \mathbb{N}$, let $\vartheta^j \varphi(t)$ be the $j$-th derivative of $u \mapsto \varphi(e^u)$ at $u = \log t$. So $\vartheta = t\,\frac{d}{dt}$, the Euler operator. A *multiplier family* of $\varphi$ is a sequence $W_0, W_1, \dots$ of operators in which $W_q$ multiplies a radial function by $\vartheta^q \varphi(g_R(x))$. The operator $W_0$ is multiplication by $\varphi(g_R)$.

**Definition 5.2.1 (Normal form span).** Let $d$ be normal form data for the actual operators $X$ of the place. It has a set of *basic elements*, a multiplicative monoid $\mathcal{B}(d) \subset \mathcal{A}$ of bounded factors, and two elements $D$ and $g_I$ of $\mathcal{A}$ that multiply the pointwise norm by $d_R(x)^{-1}$ and by $g_R(x)^{-1}$. For a subset $T \subseteq \mathcal{A}$ and $i, j, m \in \mathbb{N}$, the *normal form span* $\mathrm{nfSpan}(d, T, i, j, m)$ is the linear span of the products
$$\beta\, D^{i}\, g_I^{\,j}\, h_1 h_2 \cdots h_m, \qquad \beta \in \mathcal{B}(d),\ h_1, \dots, h_m \in T.$$

The indices $i$ and $j$ count the inverse powers of the two distances. The span is the bookkeeping device of the proof: products and the Leibniz rule move elements between spans with known indices.

For a word $w$ that the place admits, of length $N$, and an index $e$, let $M_{w,e} \in \mathcal{A}$ be the entry $e$ of the first column of the operator matrix of $w$. We have not unfolded the operator matrix of a word or the normal form data.

### The radial word bound

**Theorem 5.2.2 (Radial word bound).** Let the data of the place satisfy the data conditions, and let $d$ be normal form data for its operators. Let $T \subseteq \mathcal{A}$ and $a \in \mathbb{N}$ be such that every basic element of $d$ lies in $\mathrm{nfSpan}(d, T, 0, a, 1)$. Let $w$ be an admitted word of length $N$. Then there are $C \ge 0$, $J \in \mathbb{N}$ and lists $H_1, \dots, H_m$, each of $N$ elements of $T$, such that for every $\varphi$ with $\varphi \circ \exp$ smooth, every multiplier family $W$ of $\varphi$, every radial function $\Phi$, every index $e$ and every radial point $x$,
$$\begin{aligned}\|M_{w,e}(W_0 \Phi)(x)\| \le{}& C\, d_R(x)^{-N}\, g_R(x)^{-aN} \\ &\times \sum_{j=0}^{J} |\vartheta^j \varphi(g_R(x))| \sum_{i=1}^{m} \Bigl\|\Bigl(\prod H_i\Bigr) \Phi(x)\Bigr\| .\end{aligned}$$

Lean: `GlobalTheory.HatNF.RadBound.word_bound` (also `GlobalTheory.T.wordOperator_radial_pointwise_bound`, a second name).

The bound has three factors. The powers of $d_R$ and $g_R$ come from the word and from the basic elements. The derivatives of $\varphi$ come from commuting the multiplier past the word. The last factor uses only the fixed operators in $T$.

*Proof.* Say that a function of $x$ is *bounded with weight $\omega$* if it is at most $C\,\omega(x)$ times a finite sum of norms $\|(\prod H)\Phi(x)\|$ with $H$ a list in $T$. Such bounds add.

Step 1. Each element of $\mathrm{nfSpan}(d, T, i, j, m)$ is bounded with weight $d_R^{-i} g_R^{-j}$. By linearity it is enough to treat one generator $\beta D^i g_I^j h_1 \cdots h_m$. The factor $\beta$ is a bounded factor, so it changes the norm by at most a constant. The factors $D$ and $g_I$ multiply the norm by exactly $d_R(x)^{-1}$ and $g_R(x)^{-1}$. The product $h_1 \cdots h_m$ is a list in $T$.

Step 2. The algebraic hypotheses on $d$ hold for the actual operators. With the hypothesis on the basic elements, each hat letter lies in $\mathrm{nfSpan}(d, T, 0, a, 1)$. A product of $N$ hat letters then lies in $\mathrm{nfSpan}(d, T, 0, aN, N)$.

Step 3. A Leibniz rule writes (product of $N$ hat letters)$\,\cdot W_0$ as a sum of terms $W_q \cdot$(product of $N$ hat letters) with $q \le N(r+1)$. It uses the commutation relations of the radial multipliers with the normal form. The operator $W_q$ multiplies by $\vartheta^q \varphi(g_R)$. With $J = N(r+1)$ each term is bounded with weight $\sum_{j \le J} |\vartheta^j \varphi(g_R)|\, g_R^{-aN}$, by Step 1 and Step 2.

Step 4. The column entry $M_{w,e}$ lies in the span of products of $D^N$ with $N$ hat letters. Applying Step 1 to the outer factor adds the weight $d_R^{-N}$.

Take the sum of the constants over all indices $e$ to get one constant for all $e$. $\square$

### Basic elements as polynomial lifts

A radial operator is useful only if it comes from the group. The next definition says that it does, with control of the degrees.

**Definition 5.2.3 (Polynomial lift).** Let $o, \kappa \in \mathbb{N}$. A differential operator $\Theta$ on coefficients is *polynomial of type $(o, \kappa)$* if it is a finite sum of terms, each a word of length at most $o$ in derivatives times a scalar polynomial in the matrix entries of degree at most $\kappa$. A radial operator $\theta \in \mathcal{A}$ is a *polynomial lift of type $(o, \kappa)$* if there is such a $\Theta$ whose radial part is $\theta$: for each compactly supported coefficient $F$ of the place and each radial function $\Phi$ of $F$, $\theta \Phi$ is a radial function of $\Theta F$.

**Definition 5.2.4 (Lifting of basic elements).** Let $a : \mathbb{N} \to \mathbb{N}$. We say that *the basic elements lift with loss $a$* if, for all place data that satisfy the data conditions and all normal form data $d$, every basic element of $d$ lies in
$$\mathrm{nfSpan}\bigl(d, \{\theta : \theta \text{ is a polynomial lift of type } (n, 8(r+1)n)\}, 0, a(r), 1\bigr).$$

The loss $a(r)$ is the number of factors $g_I$ that a lift may need. With $a = 0$, no inverse power of the boundary function appears.

**Proposition 5.2.5 (Basic elements lift without loss).** The basic elements lift with loss $0$.

Lean: `GlobalTheory.HatNF.basicLiftAll_zero` (also `GlobalTheory.T.basicOperators_polynomialLift_no_inversePower`, a second name).

*Proof.* A basic element is of one of four kinds: the radial part of a shifted operator, a mirror Toda radial operator, a conjugated last minor times a radial pair term, and a combination of dual operators. For each kind there is an earlier result of the development that gives a polynomial lift of type $(n, 8(r+1)n)$. Every polynomial lift $\theta$ lies in $\mathrm{nfSpan}(d, T, 0, 0, 1)$: take $\beta = 1$, no factor $D$ or $g_I$, and the list $[\theta]$. $\square$

So the hypothesis of the radial word bound holds with $T$ the set of polynomial lifts and $a = 0$.

**Remark 5.2.6 (Formalization).** The radial word bound is in [WordOperatorRadialPointwiseBound.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/WordOperatorRadialPointwiseBound.lean#L178). Its statement only says that $J$ exists; the proof takes $J = N(r+1)$ (line 248). The proposition is in [BasicOperatorsPolynomialLiftNoInversePower.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/BasicOperatorsPolynomialLiftNoInversePower.lean#L20). It is close to trivial: each basic element is itself a lift, so the span condition holds with the trivial product. The four lifting results are cited, not opened here. We have not unfolded the radial algebra `RA`, the data conditions `P5.IsData`, the normal form data `IsNF`, or $\zeta$ and $G$.
