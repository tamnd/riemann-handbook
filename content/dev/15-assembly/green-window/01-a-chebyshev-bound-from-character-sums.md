---
title: A Chebyshev bound from character sums
decls:
  - Deduction.ch_core
  - UpperTheory.Comparison₂.core_gm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A Chebyshev bound from character sums

This section proves the analytic core of the chapter. A weighted sum of smoothed [[Chebyshev functions|B8AKSVBE5Z]] over the characters of a finite abelian group is at most $x^{1/2 + O(\varepsilon)}$, if a gap between two prime sums is small on average over a coset. The second theorem moves this bound to the sum $G_\Lambda$ of a level of primitive Dirichlet characters. The next section turns the bound on windows into zero-free half-planes, and so the result feeds [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/).

**Definition 3.1.1 (Groups and characters).** Let $E_0 = (\mathbb{Z}/2)^2$, let $H$ be a finite abelian group, and let $G = E_0 \times H$. Let $\Phi \subset G$ be the subgroup of the $g = ((g_1, g_2), h)$ with $g_1 = 0$, and let $f = |\Phi|$. Put $\sigma = ((1,0),0)$. A character of $G$ is a homomorphism $\psi : G \to \mathbb{C}^\times$, written additively on $G$; $\psi = 0$ is the trivial character. Let $\chi_C$ be the character with $\chi_C(g) = 1$ if $g_1 = 0$ and $\chi_C(g) = -1$ otherwise. For a subgroup $A_0 \le H$, let $\Psi(A_0)$ be the set of characters $\psi$ with $\psi(0, s) = 1$ for all $s \in A_0$.

**Definition 3.1.2 (Arithmetic data).** Arithmetic data $D$ on $H$ are two numbers $q_1, d \in \mathbb{N}$, a subgroup $I_p \le G$ for each $p \in \mathbb{N}$ (the inertia), and an element $F_p \in G$ for each $p$ (the Frobenius). For a finite set $S$ of numbers, $D$ is *split on* $S$ if $d$ is prime, $2 \in S$, $q_1 \in S$, $d \notin S$, $I_p = 0$ for each prime $p \notin S$ with $p \neq d$, $I_p \subseteq \Phi$ and $F_p \in \Phi$ for $p \in S$, and $I_d = \{0, \sigma\}$.

For a character $\psi$ and $n \ge 1$ put

$$\pi_D(\psi, n) = \prod_{p \mid n} \frac{1}{|I_p|} \sum_{g \in I_p} \psi\bigl(v_p(n) F_p + g\bigr),$$

the product over the primes $p \mid n$ of the mean of $\psi$ on the coset $v_p(n) F_p + I_p$. When the data come from an abelian field, $\pi_D(\psi, \cdot)$ is meant to be the Dirichlet character attached to $\psi$.

**Definition 3.1.3 (Smoothed Chebyshev functions).** Let $\Lambda(n)$ be the [[von Mangoldt function|0NK8JTE1NN]] and $\gamma$ the [[Euler-Mascheroni constant|00C5P9JZBK]]. For real $y$ put

$$G_0(y) = \sum_{1 \le n \le y} \Lambda(n) \Bigl(\frac{y}{n} - 1\Bigr) - y(\log y - 1 - \gamma).$$

Let $\ell$ be a map from characters of $G$ to $\mathbb{C}$. It plays the part of $L'/L(1)$. For $\psi = 0$ put $G_\psi = G_0$. For $\psi \neq 0$ put

$$G_\psi(y) = \sum_{1 \le n \le y} \Lambda(n)\, \pi_D(\psi, n) \Bigl(\frac{y}{n} - 1\Bigr) + y\, \ell(\psi).$$

For a finite set $K'$ of characters and a real $c$, let $w_c(\psi) = 1$ if $\psi(0, h) = 1$ for all $h \in H$, and $w_c(\psi) = c$ otherwise. Put

$$G_{K'}(c, y) = \sum_{\psi \in K'} w_c(\psi) \operatorname{Re} G_\psi(y), \qquad \Sigma_{A_0, K'}(y) = \sum_{\psi \in \Psi(A_0) \setminus K'} |G_\psi(y)| .$$

**Definition 3.1.4 (The gap).** Call a prime $p$ *inert* for $D$ if $p \neq 2, q_1, d$ and $F_p \notin \Phi$. Let $a > 0$, $t \in H$, $N \in \mathbb{N}$, and let $w$ be a positive function on $G$. Let $\rho_t(g) = ((1,1),0) + g + (0, t)$. Put

$$\mathrm{ASK}(a, t, w) = \sum_{p \le N \text{ inert}} 2 \log p \sum_{\substack{1 \le i \le N \\ i F_p \notin \Phi}} \Bigl(\frac{a}{p^i} - w(\rho_t(i F_p))\Bigr)^{+} + \log d \sum_{i=1}^{N} \sum_{\substack{g - i F_d \in I_d \\ g \notin \Phi}} \Bigl(\frac{a}{d^i} - w(\rho_t(g))\Bigr)^{+},$$

where $u^+ = \max(u, 0)$, and

$$\mathrm{MAIN}(a, w) = a \Bigl( \log a - 1 - \gamma + \ell(\chi_C) - \frac{1}{f} \sum_{\rho \in \Phi} \log w(\rho) \Bigr).$$

For points $a : H \to \mathbb{R}$, a finite set $T \subseteq H$, $m \in \mathbb{N}$ and weights $w(u, j, \cdot)$ for $u \in H$ and $j < m$, the gap at $u$ is $\sum_{t \in T} \sum_{j < m} \bigl( \mathrm{ASK}(a(t), t, w(u,j)) - \operatorname{Re} \mathrm{MAIN}(a(t), w(u,j)) \bigr)$.

**Theorem 3.1.5 (Chebyshev bound on a coset).** Let $C \ge 0$, $\varepsilon > 0$, $C_E$, $K_o$, $M$ and $c$ be reals with $|c| \le 1$. There is $x_1$ with this property. Let $x \ge x_1$. Let $H$, $m$, arithmetic data $D$ split on a set $S$, a map $\ell$, $N \in \mathbb{N}$, finite sets $T, T_2 \subseteq H$, points $a$, weights $w$, reals $b > 0$, $b'$, $k > 0$, $a_E \ge 0$, $\eta$, $X'$, $\theta$, a subgroup $A_0 \le H$ and a finite set $K'$ of characters be given. Assume:

1. $m \le x^{1/2 + \varepsilon/2}$ and $x m \le k$;
2. the size conditions: $\eta \ge 0$, $X' > 0$, $b' > 0$, $b' X' \le x b$, $\theta \ge 0$, $|a(t)/b - x| \le 1$ for $t \in T$, and for $u \in A_0$ and $\rho \in \Phi$: $w(u,j,\rho) > 0$, $b \le w(u,j,\rho) \le b + \eta + 1$ where $T_2$ is thick at $(u, \rho)$, $w(u,j,\rho) \le 2b'$ elsewhere, and $a(t)/w(u,j,\rho) \le N$ for $t \in T$;
3. thin scales: $|G_\psi(y)| \le \theta y$ for each $\psi$ and each $y \ge X'/3$;
4. cost windows: $2f(x+1)\theta \le 1/x$ and $6f(x+1)(\eta+1) \le b/x$;
5. rest sizes: $a_E \le 2xb$, $x^{-\varepsilon/8} |H|/2 \le |T|$, $x^{-\varepsilon} \le |T_2|/|H|$, $x^{1/2 - \varepsilon} \le m$ and $k \le |H|^2 x^{1/2-\varepsilon}$;
6. $T_2 \subseteq A_0$;
7. the character conditions: $0 \in K'$; each $\psi \in K'$ lies in $\Psi(A_0)$ and has $\psi(\sigma) = 1$; $|\Psi(A_0)| \le M$; for each $\psi \in K'$ that is not trivial on $0 \times H$,
$$\Bigl| \sum_{t \in T} \psi(0,t) - c|T| \Bigr| \le M x^{-1+\varepsilon} |T| ;$$
$|\ell(\psi)| \le K_o$ for $0 \neq \psi \in K'$; and $|\ell(\psi)| \le C_E \log x$ for $\psi \in \Psi(A_0) \setminus K'$;
8. for each $u \in A_0$, the gap at $u$ is at most $x^{C\varepsilon} E$, with
$$\begin{aligned} E = {} & |T|\, a_E \Bigl(1 + \frac{m^2}{k}\Bigr) \\ & + m \Bigl( 2|H|\, m\, b\, x^{\varepsilon} + \frac{|T_2|\, k\, b\, x^{\varepsilon}}{|H| \cdot |H| x^{-\varepsilon}} \Bigr). \end{aligned}$$

Then

$$G_{K'}(c, x) \le x^{1/2 + (C+3)\varepsilon} + \Sigma_{A_0, K'}(x).$$

Lean: `Deduction.ch_core`

*Proof.* The proof has six steps.

1. There is $C_d \ge 0$, for all $H$, $D$ and $\ell$, with $|G_\psi(y) - G_\psi(z)| \le |y - z| (\log \max(y,z) + C_d + |\ell(\psi)|)$ for $\psi \neq 0$ and $|G_0(y) - G_0(z)| \le C_d |y - z|$, for $y, z \ge 1$. This is a proved lemma on the derivative of the error in the [[explicit formula|72WNRWJQC1]]. It gives the bound $|G_\psi(y) - G_\psi(x)| \le \log(x+1) + C_d + |\ell(\psi)|$ for $|y - x| \le 1$ and the trivial bound $|G_\psi(x)| \le x(\log x + C_d + |\ell(\psi)|)$.
2. Fix $t \in T$. By the orthogonality of characters on $G$ and on the coset $A_0$, the sum over $u \in A_0$ of the terms of the gap equals $|A_0|\, b\, (\delta_2/2)$ times a sum over $\psi \in \Psi(A_0)$ of $\psi((1,0), t)$ times values of $G_\psi$, with $\delta_2 = |T_2|/|H|$. The values are at the points $a(t)/w$.
3. By the size conditions, each point $a(t)/w$ is close to $x$ on the thick part and is at least $X'/3$ elsewhere. The bound of thin scales, the Lipschitz bound of step 1 and the cost windows bound the error of the move to $x$ by $2f(3(x+1)(\eta+1) + (x+1) b \theta)$ for each term.
4. For each $\psi \in K'$, the character conditions with $\rho = |M| x^{-1+\varepsilon}$ give a lower bound for the contribution of $\psi$ in terms of $w_c(\psi) \operatorname{Re} G_\psi(x)$. The characters outside $K'$ contribute at most $\Sigma_{A_0, K'}(x)$. The constant of these bounds is $A_1 = 5 + C_d + |K_o| + |M|(4 + C_d + |K_o|) + 4|C_E|$, and $x^{3\varepsilon/8} \ge 26$ for large $x$.
5. Steps 2 to 4 and hypothesis 8 give
$$|T|\, m\, b\, \frac{\delta_2}{2} \bigl( Y - 4 x^{1/2 + \varepsilon} \bigr) \le x^{C\varepsilon} E + \frac{2 |T| m b}{x}, \qquad Y = G_{K'}(c,x) - \Sigma_{A_0,K'}(x).$$
6. A proved size lemma says that this inequality, with the rest sizes, gives $Y \le x^{1/2 + (C+3)\varepsilon}$.

$\square$

The second theorem applies the first one to the group of a host. A *level* $\Lambda$ is a number $o \in \mathbb{N}$, a finite set $K_\Lambda$ of primitive [[Dirichlet characters|JR4QSEFXWF]] that contains $1$ and is closed under inverse, and an optional real exceptional character $\psi_\Lambda$. Put $w_\Lambda(\psi) = 1$ if $\psi = \psi_\Lambda$, and $w_\Lambda(\psi) = (3o+1)^{-1}$ otherwise. For a primitive $\chi \neq 1$ let $G_\chi(y) = \sum_{n \le y} \Lambda(n) \chi(n) (y/n - 1)^+ + y\, L'(1,\chi)/L(1,\chi)$, and let $G_1 = G_0$. The level sum is

$$G_\Lambda(y) = G_0(y) + \sum_{\psi \in K_\Lambda \setminus \{1\}} w_\Lambda(\psi) \operatorname{Re} G_\psi(y).$$

A *frame* $\varphi$ is a finite abelian group $A$ with a subgroup $A_0$, and host axioms $H$ on $\varphi$ give arithmetic data on $A$. The *explicit formula conditions* $E_\Lambda(H, T, x, \varepsilon, C)$ say: the order of the host is $o$; the kept characters of the host are the characters of $K_\Lambda$; the exceptional characters agree; $T$ has the shares of the frame up to $\delta = x^{-1+\varepsilon}$; a bound on $G_0$ holds; and $|L'(1,\chi)/L(1,\chi)| \le C \log x$ for the characters that the host bounds. The *core conditions* at $(x, \varepsilon)$ with exponents $e_D, e_L$ and constants $K, c_{HH}, e_K$ say: there are a map $\ell$ that equals $L'/L(1,\chi)$ at each $\psi \neq 0$ whose values $\pi(\psi, n)$ are those of a primitive $\chi$, data with $x$ and $\varepsilon$ as given, constants with division exponent at most $e_D$, loss exponent at most $e_L$ and $c_{HH}$-constant at most $c_{HH}$, a covering of $A_0$, the identities that tie the data to $\mathrm{ASK}$, the error windows, and the conditions 2 to 6 of the theorem above.

**Theorem 3.1.6 (The level bound at one point).** Let $\Lambda$ be a level, and let $e_D, e_L, K, c_{HH}, e_K, C$ and $\varepsilon > 0$ be reals. There is $x_1$ such that for each $x \ge x_1$, each frame $\varphi$, each host $H$ on $\varphi$ and each finite $T \subseteq A$: if $E_\Lambda(H, T, x, \varepsilon, C)$ and the core conditions hold at $x$, then

$$G_\Lambda(x) \le x^{1/2 + (e_D + e_L + 7)\varepsilon}.$$

Lean: `UpperTheory.Comparison₂.core_gm`

*Proof.* Apply the [Chebyshev bound on a coset](/entry/ch-core/) with the constant $\max(e_D + e_L, 0) + 3$ in place of $C$, with $C_E = C$, $K_o = \sum_{\psi \in K_\Lambda} |L'(1,\psi)/L(1,\psi)|$, $c = (3o+1)^{-1}$ and $M = 4o$. The host facts give that the data are split on a set $S$. The explicit formula conditions give the character conditions. The error windows give hypothesis 8, through a gap bound with the exponent $e_D + e_L + 3$. For large $x$ also $\log x \le x^{\varepsilon}$ and $x^{\varepsilon} \ge 1 + 4o$. Two identities finish the proof. First, $G_{K'}((3o+1)^{-1}, y) = G_\Lambda(y)$ for the kept characters $K'$ of the host. Second, $\Sigma_{A_0,K'}(x) \le 4o\, x^{1/2+\varepsilon}$. So $G_\Lambda(x) \le x^{1/2 + (e_D+e_L+6)\varepsilon} + 4o\,x^{1/2+\varepsilon} \le x^{\varepsilon} \cdot x^{1/2 + (e_D+e_L+6)\varepsilon}$. $\square$

**Remark 3.1.7 (Formalization).** The first theorem is in [ChCore.lean](lean:Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChCore.lean#L343). Its proof needs `set_option maxHeartbeats 1600000` (line 342). The helper `th_le` (line 75) takes a hypothesis `_hb'` that it never uses. The bracket $E$ of hypothesis 8 is `errorBracketSizeWindows`, defined in a file named `ErrorFormsWeakWindowsFalse.lean`; the definition is only the formula above. The split condition `HostFactsS` does not ask that $q_1$ is prime. The predicates `IsThickAt`, `ErrWindows`, `SizeData₂`, `IdentU` and `BNBoundsU` are not unfolded here. In `core_gm` (CoreGm.lean line 12) the constant $C$ of the explicit formula conditions is passed as $C_E$, and the exponent $e_D + e_L + 7$ is one $\varepsilon$ more than the exponent $e_D + e_L + 6$ of the first theorem. The extra $\varepsilon$ absorbs the sum over the characters outside $K'$.
