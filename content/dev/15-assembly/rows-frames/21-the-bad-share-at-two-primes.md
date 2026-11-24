---
title: The bad share at two primes
decls:
  - UpperTheory.Win.badShare_win
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The bad share at two primes

This section proves the bound for the bad share at two auxiliary primes, in the form that [the definite good share](/entry/definite-good-share/) of Volume 8 uses. A representation of a product of general linear groups over two finite fields is cut by the idempotent of a level datum. The good part of the series characters keeps almost all of this rank, and the loss is at most $e^{-x^{z/7}}$ for a size parameter $x$. The result feeds the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). The work is the bad rows share bound of an earlier volume. This section only checks that its error term is small for the sizes of the run.

### The setting

For a prime $g$ and an integer $N$ let $G_g = \mathrm{GL}_N(\mathbb{F}_g)$. For a function $e$ on a finite group $H$ and a representation $\rho$ of $H$ on a finite dimensional complex space $M$, let $\rho(e) = \sum_\gamma e(\gamma) \rho(\gamma)$ and let $\operatorname{rk}_\rho(e)$ be the rank of $\rho(e)$. Let $a * b$ be the convolution on $H$. For functions $e_v$ on groups $H_v$, let $\bigotimes_v e_v$ be the product function on $\prod_v H_v$.

A *level datum* $L$ for $G_g$ is a pair of integers $s, k$ with $s + k < N$, a flag that says whether the datum is sharp, a nontrivial additive character $\psi$ of $\mathbb{F}_g$ and units $c_a \in \mathbb{F}_g^\times$. It defines a set of upper unipotent matrices, which have extra zero entries in a block when the datum is sharp, and a character $\chi_L$ of these matrices built from $\psi$ and the entries $c_a u_{ab}$ on the edges of the datum. Let $e_L$ be the normalized function $\chi_L^{-1}$ on this set, extended by zero.

A *series* for $G_g$ is a map $\tau$ from the set of squarefree monic polynomials $F \in \mathbb{F}_g[X]$ of degree $N$ with $F(0) \neq 0$ to class functions on $G_g$. It is injective, and each $\tau(F)$ is the character of an irreducible generic representation $V_F$ with

$$\dim V_F \cdot |T_F| = \prod_{i = 1}^{N} (g^i - 1),$$

where $T_F$ is the torus of $F$. For a class function $\chi$ let $z(\chi) = \chi(1)\, \chi(\gamma^{-1}) / |G_g|$ be its central idempotent.

Let $\iota$ be a finite index set, $\tau_v$ a series for each $v \in \iota$, and $\mathrm{ch}_v$ an $m$-tuple of units of $\mathbb{F}_g$ for each $v$. A tuple $(F_v)$ of polynomials is *good* if it is good for the units $\mathrm{ch}$ and for their inverses. Put

$$e_{\mathrm{good}}(\tau, \mathrm{ch}) = \sum_{(F_v)\ \mathrm{good}} \bigotimes_{v \in \iota} z\bigl(\tau_v(F_v)\bigr).$$

Let $\rho$ be a representation of $H = G_{g_1}^{\iota_1} \times G_{g_2}^{\iota_2}$ on $M$. It has an *exact count* if there is $c > 0$ such that, for every self adjoint idempotent $e$ on $H$ whose support lies in the tuples that are unipotent on the first factor or on the second factor,

$$\operatorname{rk}_\rho(e) = c\, \operatorname{Re} e(1).$$

A prime $g$ is *admissible* for two primes $q$ and $d$ if $q$ and $d$ are odd and distinct, $16 \leq \max(q, d)$, $16 q d$ divides $g - 1$, and $2^{12} \leq g$.

### The bound

For real numbers $g, f, m, N, Q$ put

$$\begin{aligned} B(g, f, m, N, Q) ={} & \frac{3 f}{g} + \frac{23 f \log g}{\sqrt{g}} + 2 f m \Bigl( \frac{1}{4 Q} + \frac{1 + \log N}{g - 1} \Bigr) \\ & + \frac{N}{2} \Bigl(\frac{7}{8}\Bigr)^{f} + \exp\Bigl( - \frac{f}{10 \log N} \Bigr). \end{aligned}$$

This is the error term of the bad rows share bound at one prime.

**Theorem 7.21.1 (Bad share at two primes).** Let $0 < \varepsilon \leq 1$ and $C \in \mathbb{R}$. There is $x_0$ with the following property. Let $x \geq x_0$ and $z \leq \varepsilon$. Let $g_1, g_2$ be primes, $q, d$ primes and $N, m, f$ integers, with index sets $\iota_1, \iota_2$ of $f$ elements, such that:

1. $g_1$ and $g_2$ are admissible for $q$ and $d$, and $e^{8 x^\varepsilon} \leq g_i$;
2. $x^2 \leq f \leq x^C$, $m \leq x^C$ and $x^\varepsilon \leq N \leq x^C$;
3. $2 f m / \min(q, d) \leq e^{-x^{z/7}}$.

Let $L_{i, v}$ be level data, $\tau_{i, v}$ series and $\mathrm{ch}_{i, v}$ tuples of $m$ units for $G_{g_i}$ and $v \in \iota_i$. Let $\rho$ be a representation of $H$ with an exact count, and put

$$\begin{aligned} e_L &= \Bigl(\bigotimes_{v} e_{L_{1, v}}\Bigr) \otimes \Bigl(\bigotimes_{v} e_{L_{2, v}}\Bigr), \\ e_{\mathrm{good}} &= e_{\mathrm{good}}(\tau_1, \mathrm{ch}_1) \otimes e_{\mathrm{good}}(\tau_2, \mathrm{ch}_2). \end{aligned}$$

Then there is $\delta$ with $0 \leq \delta \leq e^{-x^{z/7}}$ and

$$(1 - \delta)\, \operatorname{rk}_\rho(e_L) \leq \operatorname{rk}_\rho(e_{\mathrm{good}} * e_L).$$

Lean: `UpperTheory.Win.badShare_win`.

*Proof.* We take the steps in order.

1. The numerical lemma for the bad bound gives $x_0'$ such that, for $x \geq x_0'$ and real $g, f, m, N, Q$ with $e^{8 x^\varepsilon} \leq g$, $x^2 \leq f \leq x^C$, $0 \leq m \leq x^C$, $x^\varepsilon \leq N \leq x^C$ and $e^{x^{\varepsilon/6}} \leq Q$, we have

$$\begin{aligned} 100000 &\leq N, \\ 0 &\leq B(g, f, m, N, Q), \\ 6\, B(g, f, m, N, Q) &\leq e^{-x^{\varepsilon/7}}. \end{aligned}$$

Take $x_0 = \max(x_0', 1)$, and fix $x \geq x_0$.
2. Since $x \geq 1$ and $z \leq \varepsilon$, we have $x^{z/7} \leq x^{\varepsilon/7}$, so $e^{-x^{\varepsilon/7}} \leq e^{-x^{z/7}}$.
3. The term $B$ depends on $Q$ only through $f m / (2 Q)$. So, with $Q_0 = e^{x^{\varepsilon/6}}$ and $Q = \min(q, d)$,

$$B(g, f, m, N, Q) = B(g, f, m, N, Q_0) + \frac{1}{4} \cdot \frac{2 f m}{Q} - \frac{f m}{2 Q_0}.$$

The last term is at most $0$. Step 1 and step 2 bound the first term by $e^{-x^{z/7}}/6$, and hypothesis 3 bounds the second by $e^{-x^{z/7}}/4$. So $\max(0, B(g_i, f, m, N, Q)) \leq e^{-x^{z/7}}/2$ for $i = 1, 2$.
4. The bad rows share bound at two primes, with the count error $0$ and $100000 \leq N$ from step 1, gives

$$\Bigl(1 - \sum_{i = 1}^{2} \max\bigl(0, B(g_i, f, m, N, \min(q, d))\bigr)\Bigr)\, \operatorname{rk}_\rho(e_L) \leq \operatorname{rk}_\rho(e_{\mathrm{good}} * e_L).$$

Here $f = |\iota_1| = |\iota_2|$. With a count error $\epsilon_c$ the sum carries the factor $(1 + \epsilon_c)/(1 - \epsilon_c)$, which is $1$ for an exact count.
5. Let $\delta$ be the sum in step 4. Then $\delta \geq 0$, and $\delta \leq e^{-x^{z/7}}$ by step 3.

This proves the theorem. $\square$

### The sizes of the run

At the definite good share the theorem is applied with $C = 5$ and the size data of the run. There $x$ is the size parameter, $z$ is the exponent $\varepsilon_z$ of the size data, $f$ is the degree factor and $m$ is the rank of the datum. The primes $q$ and $d$ are the two odd primes of the host. Hypothesis 3 then comes from a separate numerical lemma: if $x \geq e^{209}$, $z > 0$, $P \leq x^{c + 1}$, $P \leq x^{10}$, $x^{c + 5} < Q$ and $x^{z/5 - z/100} \leq \log Q$, then

$$\frac{2 P}{Q} \leq e^{-x^{z/7}}.$$

It is applied with $P = f m$ and $Q = \min(q, d)$. The bounds on $P$ come from $f \leq k$ and $m + 3 \leq k$ together with the size bounds of $k$ and $t$, and the bounds on $Q$ come from the size bounds on $q$ and $d$. The proof splits into the cases $x^{z/7} \leq 3 \log x$ and $x^{z/7} \geq 3 \log x$. In the first case the bound $x^{c+5} < Q$ is enough. In the second case $x^{z/7} \geq 625$, and the bound on $\log Q$ is enough.

The rank $\operatorname{rk}_\rho(e_L)$ counts the vectors of the level datum, and the convolution with $e_{\mathrm{good}}$ keeps the part on which every coordinate lies in a good series. So the theorem says that at most a fraction $e^{-x^{z/7}}$ of the vectors of the level datum lie outside the good series. This fraction is far smaller than any power of $x^{-1}$, and the definite good share needs only that.

**Remark 7.21.2 (Formalization).** The theorem `badShare_win` is at line 79 of [BadShareWin.lean](lean:Development/AutomorphicArithmetic/ExponentialBounds/BadShareWin.lean#L79). Its witness $\delta$ is the sum of the two terms `max 0 (badBound ...)`, and the bound of step 3 is the local claim `one`, proved by the identity `e` and `linarith`. The numerical lemma `two_mul_div_le_exp` at line 13 and its use `fm_div_min_le` at line 52 are in the same file but are not used by `badShare_win`; the caller uses `fm_div_min_le` at line 425 and `badShare_win` at line 371 of [IsNilpotentSubOneOfFullBlockUnipotent.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/IsNilpotentSubOneOfFullBlockUnipotent.lean#L371). The bound $B$ is `badBound` at line 43 of [SamePartIffOfNeZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/SamePartIffOfNeZero.lean#L43), and the numerical lemma of step 1 is `badBound_numbers` at line 64 of [LogDivSqrtLeFourExp.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/LogDivSqrtLeFourExp.lean#L64). The share bound is the statement `T.badRows_share_bound_two_primes`, a `first | exact` wrapper of `BadShare.ShareThm.bad_share`. The level data `Lev`, the series `IsSeries`, the idempotent `eGood`, the count `CountAt` and the condition `PrimeOK` are in [StandardFiveNontrivial.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/StandardFiveNontrivial.lean#L38), from line 38 to line 82. The theorem asks for `CountAt ρ 0`, an exact count, while the share bound allows any error below $1$. The hypothesis $z \leq \varepsilon$ puts no lower bound on $z$.
