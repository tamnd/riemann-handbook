---
title: Curves with complex multiplication at the prime two
decls:
  - Formalism.L2.Th1.B.KFin.Th0TwoFinal_of
  - Formalism.L2.Th1.B.LCm.theta_zero_two_adic_trace
  - Formalism.L2.Th1.B.LCm.theta_zero_two_complex_mult
  - Formalism.L2.Th1.B.th0TwoCM
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Curves with complex multiplication at the prime two

The [last section](/entry/th0-two-analytic/) proved that the theta function of a half period $\omega_0/2$ has integral transport at $2$, under conditions on the points of the fibre of $\alpha$ over $\omega_0/2$. Here we derive these conditions from good reduction, and we replace the conditions on $\alpha$ by conditions on its trace and norm. The final form is for a lattice with complex multiplication by the ring of integers of $\mathbb{Q}(\sqrt{-d})$ with $d \equiv 7 \pmod 8$, where $2$ splits. It is used in the [next section](/entry/integral-operator-two-orthogonal/) to prove integrality of the jets of theta at $2$.

We keep the notation of the last section: $L$ is a lattice, $\iota : \mathbb{C} \to \mathbb{C}_2$ a field isomorphism, $W$ a Weierstrass curve over $\mathbb{C}_2$ uniformized by $L$ through $\iota$, and $P_t$ the point of $W$ attached to $t \in \mathbb{C}$. Then $t \mapsto P_t$ is a homomorphism $\mathbb{C} \to W(\mathbb{C}_2)$ with kernel $L$.

**Definition 8.5.1 (Good reduction, formal points).** Let $K$ be a field with an ultrametric absolute value. A Weierstrass curve $W$ over $K$ has *good reduction* if $|a_k| \leq 1$ for all $k$ and $|\Delta| = 1$ ([reduction and minimal models](/learn/elliptic-curves/#reduction-and-minimal-models)). A point $P$ of $W$ is a *formal point* if $P = O$ or $|x(P)| > 1$.

For a curve with good reduction, the formal points are the kernel of reduction. They form a subgroup, it is the group of points of the formal group, and it has no torsion of order prime to the residue characteristic (Silverman, Ch. IV, Prop. 3.2, and Ch. VII, Prop. 2.2). A point that is not formal has $|x(P)| \leq 1$.

**Lemma 8.5.2 (Points of order two at $2$).** Let $K$ be a field with an ultrametric absolute value, $|2| = 1/2$, and $W$ a curve over $K$ with good reduction and $|a_1| = 1$. Then:

1. a formal point $P \neq O$ with $2P = O$ has $|x(P)| = 4$, and there is at most one such point;
2. if $|x(P)| \geq 4$ and $2P \neq O$, then $|x(2P)| > 4$;
3. if $2^k P = O$ for some $k$ and $2P \neq O$, then $|x(P)| < 4$;
4. if $W$ has $|a_k| \leq 1$ for all $k$, then for $x \in K$ with $|x| = 4$ we have $|3(x + b_2/12)^2 - g_2(W)/4| = 16$, and for $|x| < 4$ this value is less than $16$.

Lean: `Formalism.L2.Th1.B.KNorm.two_torsion_kernel_unique_holds`, `Formalism.L2.Th1.B.KNorm.torsion_norm_bound_holds`, `Formalism.L2.Th1.B.KNorm.kappa_norm_holds` (item 2 is `Formalism.L2.Th1.B.DupBig`).

*Proof.* Put $g(x) = 4x^3 + b_2 x^2 + 2b_4 x + b_6$. Since $b_2 = a_1^2 + 4a_2$ and $|a_1| = 1$, we have $|b_2| = 1$, and $|b_4|, |b_6|, |b_8| \leq 1$. For item 1, a point of order two satisfies $2y + a_1 x + a_3 = 0$, so $g(x) = 0$. If $|x| > 1$, the terms of $g(x)$ have sizes $|x|^3/4$, $|x|^2$, at most $|x|/2$ and at most $1$. Two of them must have the largest size, so $|x|^3/4 = |x|^2$ and $|x| = 4$. Since $|a_1| = 1$, the reduction is ordinary, so the formal group has height $1$ ([height](/learn/formal-groups/#height)) and its kernel of $[2]$ has order $2$. This gives the uniqueness. For item 2, use the duplication formula $x(2P) = (x^4 - b_4 x^2 - 2b_6 x - b_8)/g(x)$ (Silverman, Ch. III, §2). For $|x| \geq 4$ the numerator has size $|x|^4$ and $|g(x)| \leq |x|^3/4$, so $|x(2P)| \geq 4|x| > 4$. For item 3, assume $|x(P)| \geq 4$ and let $j \geq 1$ be such that $2^j P$ has order $2$. By item 2 and induction, $|x(2^i P)| > 4$ for $1 \leq i \leq j$, so $2^j P$ is a formal point of order two with $|x| > 4$. This contradicts item 1. For item 4, $3(x + b_2/12)^2 - g_2(W)/4 = g'(x)/4 = 3x^2 + \tfrac{1}{2} b_2 x + \tfrac{1}{2} b_4$. The three terms have sizes $|x|^2$, $2|x|$ and at most $2$, since $b_4 = 2a_4 + a_1 a_3$. For $|x| = 4$ the first term has size $16$ and the others are smaller. For $|x| < 4$ all three are less than $16$. $\square$

**Lemma 8.5.3 (Sum of $\kappa$ over a kernel).** Let $\alpha \neq 0$ with $\alpha L \subseteq L$, and let $S$ be a set of kernel representatives for $\alpha$. Then
$$
\sum_{P \in S} \big( 3 \wp(P)^2 - \tfrac{g_2(L)}{4} \big) = \frac{(\alpha^4 - 1) \, g_2(L)}{20} .
$$

Lean: `Formalism.L2.Th1.B.KSum.kappa_sum_holds`.

*Proof.* In the identity $\alpha^2 \wp(\alpha z) = \sum_{P \in S \cup \{0\}} \wp(z + P) - \sum_{P \in S} \wp(P)$ from the [last section](/entry/th0-two-analytic/), compare the coefficients of $z^2$. Since $\wp(z) = z^{-2} + \frac{g_2}{20} z^2 + \cdots$, the left side gives $\alpha^4 g_2/20$. On the right, $\wp(z + P)$ gives $\wp''(P)/2 = 3\wp(P)^2 - g_2/4$, and the term $P = 0$ gives $g_2/20$. $\square$

**Proposition 8.5.4 (Kernel points are not formal).** Let $W$ have good reduction and $|a_1| = 1$. Let $\alpha \neq 0$ with $\alpha L \subseteq L$ and $\iota(\alpha) = b \in \mathbb{Z}_2$ with $|b| = 1$. Then:

1. if $\alpha t \in L$ and $t \notin L$, then $P_t$ is not a formal point;
2. if $P_t$ is a formal point, then so is $P_{\alpha t}$.

Lean: `Formalism.L2.Th1.B.KKer.KernelIntegral_of`, `Formalism.L2.Th1.B.KFin.kernel_stable_of_integral_kernel`.

*Proof.* The integers $T = \alpha + \bar\alpha$ and $n = \alpha \bar\alpha$ exist since $\alpha$ is an algebraic integer that preserves $L$. Write $n = 2^a m$ with $m$ odd. For item 1, assume that $P_t$ is formal. Since $n t = (T - \alpha) \alpha t \in L$ and formal points have no odd torsion, $2^a P_t = O$. So some $Q = 2^j P_t$ is a formal point of order exactly $2$. Since $\alpha 2^j t \in L$, there is $u_0 \in S$ with $Q = P_{u_0}$. By the lemma on points of order two, $|x(Q)| = 4$. Every other $u \in S$ has $|x(P_u)| < 4$: by uniqueness if $P_u$ is formal of order two, by item 3 if $P_u$ is formal of order more than two, and by $|x| \leq 1$ otherwise. Since $W$ is uniformized by $L$, $\iota(3\wp(u)^2 - g_2(L)/4) = 3(x(P_u) + b_2/12)^2 - g_2(W)/4$. By item 4, the image under $\iota$ of the sum in the last lemma has one term of size $16$ and all others smaller, so it has size $16$. But $b^4 \equiv 1 \pmod{16}$, $|g_2(W)| = |c_4/12| \leq 4$ and $|20| = 1/4$, so the right side has size at most $1$. This is a contradiction. For item 2, assume that $P_t$ is formal with $t \notin L$. By item 1, $\alpha t \notin L$. The isogeny identity at $z = t$ reads
$$
\begin{aligned}
x(P_t) = {} & b^2 \, x(P_{\alpha t}) - (1 - b^2) \tfrac{b_2}{12} \\
& - \textstyle\sum_{u \in S} \big( x(P_{t + u}) - x(P_u) \big) .
\end{aligned}
$$
The points $P_u$ and $P_{t+u}$ are not formal, by item 1 and the group law, so their $x$ have size at most $1$. Also $|1 - b^2| \leq 1/4$ and $|b_2/12| \leq 4$. If $|x(P_{\alpha t})| \leq 1$, then $|x(P_t)| \leq 1$, which is false. $\square$

**Proposition 8.5.5 (Points over a half period).** Let $W$ have good reduction and $|a_1| = 1$. Let $\alpha \neq 0$ with $\alpha L \subseteq L$, $\iota(\alpha) = b$ and $\iota(\bar\alpha) = b'$ with $b, b' \in \mathbb{Z}_2$, $|b| = 1$, $|b'| < 1$. Let $\omega_0 \in L$ with $\bar\alpha \omega_0/2 \notin L$. Then $P_{\omega_0/2}$ is not formal, $P_Q$ is not formal whenever $\alpha Q - \omega_0/2 \in L$, and $2z \notin L$ whenever $\alpha z - \omega_0/2 \in L$.

Lean: `Formalism.L2.Th1.B.KFin.PointsTwoFinal_of`.

*Proof.* Since $|b'| < 1$, the norm $n = \alpha \bar\alpha$ is even. So $\bar\alpha \alpha z = (n/2)(2z) \in L$ whenever $2z \in L$, and $\bar\alpha L \subseteq L$. Third claim: if $\alpha z - \omega_0/2 \in L$ and $2z \in L$, then $\bar\alpha \omega_0/2 = \bar\alpha \alpha z - \bar\alpha(\alpha z - \omega_0/2) \in L$, which is false. First claim: if $P_{\omega_0/2}$ is formal, then so is $P_{\alpha\omega_0/2}$, and $\alpha \omega_0/2 \notin L$ by the last proposition. Both are formal points of order two, so they are equal, and $\alpha\omega_0/2 - \omega_0/2 \in L$. As before this gives $\bar\alpha \omega_0/2 \in L$, which is false. Second claim: if $P_Q$ is formal, then so is $P_{\alpha Q}$, and $P_{\omega_0/2} = P_{\alpha Q} - P_{\alpha Q - \omega_0/2}$ is formal, which is false. $\square$

**Theorem 8.5.6 (Theta of a half period, split case).** Let $L$, $\iota$ and $W$ be as above, with $W$ of good reduction and $|a_1| = 1$. Let $\alpha, \omega_0 \in \mathbb{C}$ and $b, b' \in \mathbb{Z}_2$ with $\alpha \neq 0$, $\alpha L \subseteq L$, $\iota(\alpha) = b$, $\iota(\bar\alpha) = b'$, $|b| = 1$, $|b'| < 1$, $\omega_0 \in L$ and $\bar\alpha \omega_0/2 \notin L$. Then:

1. the [even sigma logarithm](/entry/cube-e-of/) $\varphi_E$ of $W$ for $s_2 = \iota(s_2(L))$ and $x_T = x(P_{\omega_0/2})$ satisfies $\varphi_E \simeq 0$;
2. the transport $\theta_{\omega_0/2}^{\iota}$ has constant term $1$ and integral coefficients;
3. for every $s \in \mathbb{C}$ with $N s \in L$ for some odd $N > 0$, the transport of $z \mapsto \theta_{\omega_0/2}(z + s) \exp(-\pi H(z, s) - \pi H(s, s)/2)$ has integral coefficients, and one of them has absolute value $1$.

Lean: `Formalism.L2.Th1.B.KFin.Th0TwoFinal_of`.

*Proof.* By the last proposition, $\omega_0/2 \notin L$ (else $\bar\alpha \omega_0/2 \in L$), and the points $P_{\omega_0/2}$ and $P_Q$ for $Q$ in the fibre are not formal, so their $x$-coordinates have size at most $1$. The third claim of the last proposition is the remaining hypothesis of the [theorem of the last section](/entry/th0-two-analytic/), which gives items 1 and 2. Item 3 follows from item 2 by the result on translates of a theta function by points of order prime to $2$ (Lean: `Formalism.L2.Th1.E.shiftAnalyticW`). $\square$

**Theorem 8.5.7 (Theta of a half period, trace form).** Let $L$, $\iota$ and $W$ be as above, with $W$ of good reduction and $|a_1| = 1$. Let $\alpha, \omega_0 \in \mathbb{C}$ and $T, N \in \mathbb{Z}$ with $\alpha L \subseteq L$, $\alpha + \bar\alpha = T$, $\alpha \bar\alpha = N$, $T$ odd, $N$ even, $\omega_0 \in L$, $\alpha \omega_0/2 \notin L$ and $\bar\alpha \omega_0/2 \notin L$. Then items 1 to 3 of the last theorem hold.

Lean: `Formalism.L2.Th1.B.LCm.theta_zero_two_adic_trace`.

*Proof.* Since $T$ is odd, $\alpha \neq 0$. The polynomial $X^2 - TX + N$ is $X(X - T)$ modulo $2$, with simple roots. By Hensel's lemma it has roots $b, b' \in \mathbb{Z}_2$ with $|b| = 1$ and $|b'| < 1$ ([p-adic numbers](/learn/number-fields/#p-adic-numbers-and-local-fields)). The numbers $\iota(\alpha)$ and $\iota(\bar\alpha)$ are the two roots of the same polynomial in $\mathbb{C}_2$. If $\iota(\alpha) = b$, apply the last theorem to $\alpha$. Otherwise $\iota(\bar\alpha) = b$ and $\iota(\alpha) = b'$; then $\bar\alpha L \subseteq L$, since $\bar\alpha = T - \alpha$, and we apply the last theorem to $\bar\alpha$, using $\alpha\omega_0/2 \notin L$. $\square$

For $d \in \mathbb{N}$ put $\omega_d = (1 + \sqrt{-d})/2$. If $d \equiv 3 \pmod 4$ is squarefree, then $\mathbb{Z}[\omega_d]$ is the ring of integers of $\mathbb{Q}(\sqrt{-d})$, and we say that $L$ has *complex multiplication by $\omega_d$* if $\omega_d L \subseteq L$ ([complex multiplication](/learn/elliptic-curves/#complex-multiplication)).

**Theorem 8.5.8 (Theta of a half period, complex multiplication).** Let $d \in \mathbb{N}$ with $d \equiv 7 \pmod 8$, and let $L$ be a lattice with $\omega_d L \subseteq L$. Let $\iota$ and $W$ be as above, with $W$ of good reduction and $|a_1| = 1$. Let $\omega_0 \in L$ with $\omega_d \omega_0/2 \notin L$ and $\bar\omega_d \omega_0/2 \notin L$. Then items 1 to 3 hold for $\omega_0$.

Lean: `Formalism.L2.Th1.B.th0TwoCM` (also `Formalism.L2.Th1.B.LCm.theta_zero_two_complex_mult`, a second name).

*Proof.* Write $d = 8k + 7$. Then $\omega_d + \bar\omega_d = 1$ is odd and $\omega_d \bar\omega_d = (1 + d)/4 = 2k + 2$ is even. This is the trace form applied to $\alpha = \omega_d$, $T = 1$, $N = 2k + 2$. $\square$

The condition $d \equiv 7 \pmod 8$ says that $2$ splits in $\mathbb{Q}(\sqrt{-d})$: the two factors of $X^2 - X + (1+d)/4$ over $\mathbb{Z}_2$ give the two primes above $2$, and $\omega_d$ is a unit at one of them and not at the other (Cox, §5).

**Remark 8.5.9 (Formalization).** The proofs of the four items of the lemma on points of order two and of the sum of $\kappa$ were not unfolded; the arguments above are the classical ones and match the statements. The proof of item 3 of the split case is the cited result on translates, which was also not unfolded. In the complex multiplication theorem, $\omega_d L \subseteq L$ is all that is assumed; $d$ need not be squarefree. The [split case](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/LatticePointInKernelSubgroup.lean#L269) passes only $|a_k| \leq 1$ to the theorem of the last section, and uses good reduction for the points and for item 3. The name of the trace form speaks of a $2$-adic trace, but no trace map is used: the hypotheses are the integers $T$ and $N$.
