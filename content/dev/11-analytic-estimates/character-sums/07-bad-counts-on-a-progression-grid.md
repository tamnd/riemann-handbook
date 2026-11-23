---
title: Bad counts on a progression grid
decls:
  - Formalism.InvariantFactorPaths.MC.gram_hypothesis_of_log_bound
  - Formalism.InvariantFactorPaths.MC.meanGamX
  - Formalism.InvariantFactorPaths.MC.tieOpsX_main
  - Formalism.InvariantFactorPaths.MC.theoremMXB
  - Formalism.InvariantFactorPaths.MC.theoremMV7Of
  - Formalism.InvariantFactorPaths.MC.theoremMV7
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bad counts on a progression grid

This section proves a $p$-adic mean value theorem. A space of polynomials in $r$ colours carries a pairing built from tie operators. We count the rank that fails to pair well, average over a grid of degrees in arithmetic progression, and bound the mean by small fractions of the dimension. The bound feeds [the averaged bad count theorem](/entry/top-theorem-mv7/) of the chapter on sharp restriction bounds. The tools are Smith forms over the [[discrete valuation ring|MGM3CNJW9V]] $\mathbb{Z}_p$ (see [lattices over discrete valuation rings](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices)) and [[highest weight|C5W8BE1DRY]] vectors (see [highest weights](/learn/representations/#highest-weights-and-branching)).

Throughout, $p$ is a prime, $|x|$ is the $p$-adic norm, $r \geq 2$ and $\rho = r - 1$ is the last colour.

**Definition 6.7.1 (Letters and polynomial spaces).** *Letters* $L$ of length $N$ give each row $j < N$ a sign $v_j \in \{+, -\}$ and a degree $d_j \in \mathbb{N}$; put $|L| = \sum_j d_j$. Let $x_{j,c}$ ($j < N$, $c < r$) be variables. $\mathrm{Pol}(L) \subseteq \mathbb{Q}_p[x]$ is spanned by the monomials $x^m$ with $\sum_c m(j, c) = d_j$ for each $j$, and $\mathrm{Pol}_{\mathbb{Z}}(L) = \mathrm{Pol}(L) \cap \mathbb{Z}_p[x]$. For $j \leq N$ and colours $c, d$ put
$$e^{(j)}_{cd} = \sum_{i < j,\ v_i = +} x_{i,c}\,\partial_{i,d} - \sum_{i < j,\ v_i = -} x_{i,d}\,\partial_{i,c},$$
and give $x^m$ the weight $\mathrm{wt}_j(c, m) = \sum_{i < j} \pm m(i, c)$, with the sign $v_i$.

Lean: `Formalism.GM.M.Pol` (also `Formalism.GM.M.glAct`).

**Definition 6.7.2 (Constrained spaces).** *Tie data* $T$ give positions $\mathrm{pos}_i$ and shifts $z_i$ ($i < t$), and thresholds $(J_k, M_k)$ ($k < q$) with $M_k \in \mathbb{Z} \cup \{\infty\}$. $\mathrm{YCond}(j, M)$ is the largest subspace stable under all $e^{(j)}_{cd}$ and spanned by monomials with $\mathrm{wt}_j(0, m) \leq M$. Put
$$Y(L) = \mathrm{Pol}(L) \cap \bigcap_k \mathrm{YCond}(J_k, M_k), \qquad Y_{\mathbb{Z}}(L) = Y(L) \cap \mathrm{Pol}_{\mathbb{Z}}(L).$$
$T$ is *admissible* for $L$ if $\mathrm{pos}$ is strictly increasing and, for each $i$, $\mathrm{pos}_i + 1 < N$, $v_{\mathrm{pos}_i} = +$, $v_{\mathrm{pos}_i + 1} = -$ and $\mathrm{pos}_i + 1 = J_k$ for some $k$. $T^{(i)}$ keeps the thresholds with $J_k \leq \mathrm{pos}_i + 1$ and sets the others to $\infty$.

Lean: `Formalism.GM.M.Y` (also `Formalism.GM.M.YZ`, `Formalism.GM.M.TieData.Admissible`).

**Definition 6.7.3 (Fock pairing and tie operators).** Put $\langle F, G\rangle = \sum_m F_m G_m\, m!$ with $m! = \prod_v m(v)!$, and $\langle F, G\rangle_L = \langle F, G\rangle / \prod_j d_j!$. For the tie $i$ let $a = \mathrm{pos}_i$, $b = a + 1$, $o = d_a$ and $n = d_b$. Let $E_i$ multiply by $\sum_c x_{a,c}x_{b,c}$ and $F_i = \sum_c \partial_{a,c}\partial_{b,c}$. Put
$$\varphi_i = \sum_{j=0}^{o} \frac{(-1)^j}{(j!)^2\binom{o + n + r + z_i - 1}{j}}\,E_i^j F_i^j, \qquad \Phi = \varphi_0 \circ \dots \circ \varphi_{t-1},$$
and $\beta_L(F, G) = \langle \Phi F, G\rangle_L$.

Lean: `Formalism.GM.M.fockN` (also `Formalism.GM.tiePhi`, `Formalism.GM.TM.TieData.phis`).

$\langle\,,\rangle$ is the Bombieri inner product (Beauzamy, Bombieri, Enflo and Montgomery, J. Number Theory 36 (1990)) over $\mathbb{Q}_p$.

**Definition 6.7.4 (Bad count).** Let $\Lambda$ be a $\mathbb{Z}_p$-lattice with a form $\beta$ and let $D \in \mathbb{Z}$. $\mathrm{good}(\Lambda, D)$ is the largest $n$ such that there are $x_1, \dots, x_n, y_1, \dots, y_n \in \Lambda$ with $\beta(x_a, y_b) = p^D\delta_{ab}$. Put $\mathrm{bad}(\Lambda, D) = \max(\mathrm{rk}\,\Lambda - \mathrm{good}(\Lambda, D), 0)$.

Lean: `Formalism.GM.M.bad` (also `Formalism.GM.M.goodCount`).

**Definition 6.7.5 (Grid).** For $n \in \mathbb{N}^t$, $L_n$ is $L$ with $d_{\mathrm{pos}_i + 1} = n_i$. Given $n_{0,i}$, $\delta_i > 0$ and $Y_i \geq 1$, the grid is $G = \prod_i \{n_{0,i} + \delta_i j : 0 \leq j < Y_i\}$, with top $n^{\mathrm{top}}_i = n_{0,i} + \delta_i(Y_i - 1)$. $S_i(L) = \sum_{a \leq \mathrm{pos}_i} d_a$, and $S_i = S_i(L_{n^{\mathrm{top}}})$. For $a \geq 1$ and $s, E$ put
$$\lambda = \log_p(8a + r) + 1, \qquad \kappa = 3(s + 2)r^2\lambda, \qquad \varepsilon_i = \frac{2S_i}{Y_i} + \frac{1}{E}\Bigl(2\kappa + \frac{2S_i\lambda}{Y_i}\Bigr).$$

Lean: `Formalism.GM.TM.Letters.setTies` (also `Formalism.CountingSumsFrames.epsSeg`).

**Definition 6.7.6 (Three hypotheses).** Let $e_1 \in \mathbb{N}$.

1. $\mathrm{HypP}(L, \rho, e_1)$: for each $j \leq N$, each colour set $C$ equal to all colours or all but $\rho$, and each set of weights saturated in $C$, there is a projector onto the isotypic parts of those weights for the $e^{(j)}_{cd}$ ($c, d \in C$), along the others. It is self-adjoint for $\langle\,,\rangle$ and $p^{e_1}P$ maps $\mathrm{Pol}_{\mathbb{Z}}(L)$ into $\mathbb{Z}_p[x]$. These projectors commute.
2. $\mathrm{HypW}(L, e_1)$: for each $j \leq N$ and weight $\lambda'$, if $x \in \mathrm{Pol}(L) \cap \mathbb{Z}_p[x]$ lies in the $\lambda'$-isotypic part, then $p^{e_1}x$ lies in the sum of the Weyl lattices of the integral highest weight vectors $h \in \mathrm{Pol}(L)$ of weight $\lambda'$. The Weyl lattice of $h$ is the smallest $\mathbb{Z}_p$-lattice that contains $h$ and is stable under $(e^{(j)}_{cd})^k/k!$, $c \neq d$.
3. $\mathrm{Gram}(L, J, M, \rho, \kappa_4)$, for $L$ with $K + 1$ rows: let $\mathcal{M}(w)$ be the vectors of $Y(L)$ of weight $w$ for $e^{(K)}$ that are highest weight vectors for the colours other than $\rho$, and $\mathcal{M}_{\mathbb{Z}}(w) = \mathcal{M}(w) \cap \mathbb{Z}_p[x]$. $\mathrm{gr}_e(w)$ is spanned by the parts of degree $e$ in $x_{K,\rho}$ of the $f \in \mathcal{M}_{\mathbb{Z}}(w)$ all of whose monomials have degree at least $e$ in $x_{K,\rho}$. The hypothesis says: for each $w$, $e$ and each $\mathbb{Z}_p$-basis $g_1, \dots, g_k$ of $\mathrm{gr}_e(w)$, $p^{-\kappa_4 k} \leq |\det(\langle g_a, g_b\rangle_L)|$.

Lean: `Formalism.GM.M.GramDeterminantGradedHypothesis` (also `Formalism.GM.M.HypP`, `Formalism.GM.M.HypW`).

**Lemma 6.7.7 (Gram bound from logarithms).** Let $K \in \mathbb{N}$, $L$ letters of length $K + 1$ with $v_K = +$, and $J, M$ any thresholds. Let $\lambda', \kappa_4$ be real with $\lfloor\log_p(|L| + r - 1)\rfloor \leq \lambda'$, $\lfloor\log_p(4|L| + r - 1)\rfloor \leq \lambda'$ and $(K + 7)\,r^2\lambda'/2 \leq \kappa_4$. Then $\mathrm{Gram}(L, J, M, \rho, \kappa_4)$ holds.

Lean: `Formalism.InvariantFactorPaths.MC.gram_hypothesis_of_log_bound`.

*Proof.* Put $\kappa_C = \binom{r}{2}\lfloor\log_p(|L| + r - 1)\rfloor$; since $\binom{r}{2} \leq r^2/2$, $\kappa_C \leq r^2\lambda'/2$. If $K = 0$, a graded bound for saturated lattices gives the determinant bound from $\kappa_C$, and $7r^2\lambda'/2 \leq \kappa_4$ is enough. If $K \geq 1$, a graded bound through the highest weight projection gives exponent $(K + 3)\kappa_C + 2c_0$, with $c_0 = 2\binom{r}{2}\lfloor\log_p(4|L| + r - 1)\rfloor \leq r^2\lambda'$. Its input is a restricted saturation bound. The exponent is at most $(K + 3)r^2\lambda'/2 + 2r^2\lambda' = (K + 7)r^2\lambda'/2 \leq \kappa_4$. $\square$

**Lemma 6.7.8 (Mean count of small invariant factors).** Let $L$ have $K + 1$ rows with $v_K = +$, and let $z$, $w$ be given. For $n \geq |L|$ and $f, f' \in \mathrm{Pol}(L)$ put
$$\Gamma_n(f, f') = \binom{d_K + n + r + z - 1}{d_K}\frac{\langle \varphi\,\mathrm{fr}_n f,\ \mathrm{fr}_n f'\rangle}{(n - |L|)!\,|L|!\,\prod_j d_j!},$$
where a new row $K + 1$ of sign $-$ and degree $n$ is added, $\varphi$ is the tie operator of rows $K, K + 1$ with shift $z$, and $\mathrm{fr}_n f$ is $x_{K+1,\rho}^{n - |L|}$ times a substitution that couples the variables $x_{i,\rho}$ of the $+$ rows to the new row. Let $f_1, \dots, f_{n_0}$ be a $\mathbb{Z}_p$-basis of $\mathcal{M}_{\mathbb{Z}}(w)$ such that $f_b$ has exact order $\mathrm{ord}(b)$ in $x_{K,\rho}$ and, for each $e$, the $f_b$ with $\mathrm{ord}(b) \geq e$ span the elements of order at least $e$. Let $E \geq 1$, $\ell \geq 1$, $\delta > 0$ prime to $p$, and $s \geq |L|$. Let $X$ satisfy $2|L| \leq X$, $z + d_K \leq X$, $\ell \leq X$, $r \leq X$, $\lfloor\log_p X\rfloor + 1 \leq \lambda'$, and let $((K + 4)r + 6)\lambda' \leq \kappa$ and $\mathrm{Gram}(L, J, M, \rho, \kappa_4)$ hold. For $j < \ell$ suppose $(p^{\lceil\kappa\rceil}\Gamma_{s + \delta j}(f_a, f_b))_{a,b} = U_j\,\mathrm{diag}(g_j)\,V_j$ with $U_j, V_j$ integral and of unit determinant. Then
$$\frac{1}{\ell}\sum_{j < \ell}\#\{b : |g_j(b)| < p^{-E}\} \leq n_0\Bigl(\frac{2|L|}{\ell} + \frac{\kappa + 3\lambda' + \kappa_4 + 2|L|\lambda'/\ell}{E}\Bigr).$$

Lean: `Formalism.InvariantFactorPaths.MC.meanGamX` (also `Formalism.InvariantFactorPaths.MC.MeanGamX`, `Formalism.GM.M.tieGam`).

*Proof (outline).* First, $\Gamma_n(f, f')$ is a polynomial in $n$ of degree at most $|L| + d_K - \max(e, e')$ when $f, f'$ have orders $e, e'$. Second, if $e = e'$ its top coefficient is an explicit multiple of $\langle \mathrm{in}_e f, \mathrm{in}_e f'\rangle$, where $\mathrm{in}_e$ is the part of order $e$. So the determinant of $(\Gamma_n(f_a, f_b))$ has a leading coefficient built from the Gram determinants of the $\mathrm{gr}_e(w)$, and the Gram hypothesis bounds it below. Third, $p^{c}\Gamma_n$ is a $\mathbb{Z}_p$-combination of the $\binom{n}{i}$ for some $c \leq \kappa$. Fourth, a window lemma bounds the mean number of small Smith factors of such a matrix along a progression by $n_0(\Delta/\ell + (\Lambda_0 + \Delta\lambda'/\ell)/E)$, with $\Delta = 2|L|$ and $\Lambda_0 = \kappa + 3\lambda' + \kappa_4$. $\square$

**Proposition 6.7.9 (Tie operators).** Let $p \neq 2$, $N \geq 1$, $T$ admissible for $L$, $E \geq 1$ and $n \in \mathbb{N}^t$ with $S_i(L_n) \leq n_i$. Let all degrees of $L_n$ be at most $X$, $\lfloor\log_p X\rfloor + 1 \leq \lambda'$, $(N + 2)r^2\lambda' \leq \kappa$, and let $\mathrm{HypP}(L_n, \rho, e_1)$ and $\mathrm{HypW}(L_n, e_1)$ hold. For each $i$ and $w$ let $L^{(i)}$ be the first $\mathrm{pos}_i + 1$ rows of $L_n$, let $f_{i,w}$ be a $\mathbb{Z}_p$-basis of $\mathcal{M}_{\mathbb{Z}}(w)$ for $L^{(i)}$ and $T^{(i)}$, and let $(p^{\lceil\kappa\rceil}\Gamma_{n_i}(f_{i,w,a}, f_{i,w,b})) = U\,\mathrm{diag}(g_{i,w})\,V$ as above, with shift $z_i$. Let $h_{i,w} \in \mathcal{M}(w)$ be nonzero when $\mathcal{M}(w) \neq 0$. Write $Y = Y(L_n)$ and $Y^{(i)}$ for $Y(L_n)$ with thresholds $T^{(i)}$. Then for each $i$ there are linear maps $T_i, \pi_i$ and $K \leq e_1(N + 2)$ with:

1. $T_i Y \subseteq Y$, and $p^K T_i$ maps $Y_{\mathbb{Z}}(L_n)$ into $\mathbb{Z}_p[x]$;
2. $\langle \varphi_i u, T_i u'\rangle_{L_n} = p^{\lfloor E\rfloor}\langle \pi_i u, u'\rangle_{L_n}$ for $u \in Y^{(i)}$, $u' \in Y$;
3. $\pi_i\varphi_j u = \varphi_j\pi_i u$ for $j > i$ and $u \in Y^{(i)}$;
4. $\dim Y - \dim(Y \cap \ker(\pi_i - 1)) \leq \sum_w \#\{b : |g_{i,w}(b)| < p^{-E}\}\,\dim Y_i(h_{i,w})$,

where $Y_i(h)$ is a space generated from $h$ in $\mathrm{Pol}(L_n)$.

Lean: `Formalism.InvariantFactorPaths.MC.tieOpsX_main` (also `Formalism.InvariantFactorPaths.MC.TieOpsX`).

*Proof (outline).* $p^{\lceil\kappa\rceil}\Gamma_{n_i}(f, f')$ is a constant times $\langle \varphi_i \tilde f, \tilde f'\rangle$, where $\tilde f$ is the lift of $f$ to all $N$ rows; the constant is integral since $(\mathrm{pos}_i + 2)r\log_p X \leq \lceil\kappa\rceil$. The Smith form gives dual bases $f', f''$ with $\langle \varphi_i \tilde f'_a, \tilde f''_b\rangle$ proportional to $\delta_{ab}g_{i,w}(a)$, for the finitely many weights $w$ that occur. $\pi_i$ projects onto the span of the parts with $|g_{i,w}(a)| \geq p^{-E}$, and $T_i$ sends the dual vectors there with the factor $p^{\lfloor E\rfloor}/g_{i,w}(a)$. The projectors of $\mathrm{HypP}$ and the Weyl lattices of $\mathrm{HypW}$ carry this from highest weight vectors to $Y$, at a cost of a power of $p^{e_1}$. This gives $K = e_1(\mathrm{pos}_i + 4) \leq e_1(N + 2)$. $\square$

**Theorem 6.7.10 (Mean bad count, general form).** Let $p \neq 2$, $N \geq 1$, $T$ admissible for $L$, $E \geq 1$, and for each $i$ let $Y_i \geq 1$, $\delta_i > 0$ prime to $p$ and $S_i \leq n_{0,i}$. Let $X, \kappa, \kappa_4, \lambda', e_1$ satisfy: every degree of $L_{n^{\mathrm{top}}}$ is at most $X$; $2S_i \leq X$, $Y_i \leq X$ and $z_i + d_{\mathrm{pos}_i}(L_{n^{\mathrm{top}}}) \leq X$ for each $i$; $r \leq X$; $\lfloor\log_p X\rfloor + 1 \leq \lambda'$; $\frac32(N + 2)r^2\lambda' \leq \kappa$; $e_1(N + 2) \leq \kappa$; $3\lambda' + \kappa_4 \leq \kappa$. At each $n \in G$ let $\mathrm{HypP}(L_n, \rho, e_1)$, $\mathrm{HypW}(L_n, e_1)$ and $\mathrm{Gram}(L^{(i)}, J, T^{(i)}, \rho, \kappa_4)$ hold for all $i$. Put $D = \lfloor t(E + \kappa) + \kappa\rfloor$. Then
$$\begin{aligned} \frac{1}{|G|}\sum_{n \in G}\mathrm{bad}\bigl(Y_{\mathbb{Z}}(L_n), D\bigr) &\leq \sum_{i < t}\Bigl(\frac{2S_i}{Y_i} + \frac{2\kappa + 2S_i\lambda'/Y_i}{E}\Bigr) \\ &\qquad \times \frac{1}{|G|}\sum_{n \in G}\dim Y\bigl(L_{n[i \mapsto n^{\mathrm{top}}_i]}\bigr), \end{aligned}$$
with $\mathrm{bad}$ taken for $\beta_{L_n}$.

Lean: `Formalism.InvariantFactorPaths.MC.theoremMXB` (also `Formalism.InvariantFactorPaths.MC.TheoremMXB`).

*Proof (outline).* Fix $n \in G$. The tie operators give a saturated sublattice $\Lambda_1 \subseteq Y_{\mathbb{Z}}(L_n)$ whose primitive vectors $u$ have a partner $u'$ with $|\beta(u, u')| \geq p^{-D}$. A bad count criterion gives
$$\mathrm{bad}(Y_{\mathbb{Z}}(L_n), D) \leq \sum_i\sum_w \#\{b : |g_{i,w}(b)| < p^{-E}\}\,\dim Y_i(h_{i,w}).$$
Average over $n_i$ with the other coordinates fixed. The truncation $L^{(i)}$ has $|L^{(i)}| = S_i(L_n) \leq S_i$, so the previous lemma gives the mean count at most $n_0(2S_i/Y_i + (2\kappa + 2S_i\lambda'/Y_i)/E)$, using $\kappa + 3\lambda' + \kappa_4 \leq 2\kappa$. A monomial count and the monotonicity of highest weight dimensions bound $\sum_w n_0(w)\dim Y_i(h_{i,w})$ by $\dim Y(L_{n[i \mapsto n^{\mathrm{top}}_i]})$. $\square$

**Theorem 6.7.11 (Mean bad count with explicit constants).** Let $p \neq 2$, $L$ letters of length $2s + 1$ with $v_j = +$ exactly for even $j$, $T$ admissible for $L$ with each $J_k$ equal to $2s + 1$ or to some $\mathrm{pos}_i + 1$. Let $a \geq 1$, $E \geq 1$, and for each $i$ let $Y_i \geq 1$, $\delta_i > 0$ prime to $p$, $S_i \leq n_{0,i}$. Assume that $|L_{n^{\mathrm{top}}}| \leq 8a + r$ and, for each $i$, that $d_{\mathrm{pos}_i} + d_{\mathrm{pos}_i + 1} + r + z_i + 1$, $Y_i$ and $2S_i + 1$ are at most $8a + r$, all for $L_{n^{\mathrm{top}}}$. Assume that at each $n \in G$, $\mathrm{HypP}(L_n, \rho, \lfloor r^2\lambda\rfloor)$, $\mathrm{HypW}(L_n, \lfloor r^2\lambda\rfloor)$ and $\mathrm{Gram}(L^{(i)}, J, T^{(i)}, \rho, (s + 4)r^2\lambda)$ hold. Then
$$\frac{1}{|G|}\sum_{n \in G}\mathrm{bad}\bigl(Y_{\mathbb{Z}}(L_n), \lfloor t(E + \kappa) + \kappa\rfloor\bigr) \leq \sum_{i < t}\varepsilon_i\,\frac{1}{|G|}\sum_{n \in G}\dim Y\bigl(L_{n[i \mapsto n^{\mathrm{top}}_i]}\bigr).$$

Lean: `Formalism.InvariantFactorPaths.MC.theoremMV7Of` (also `Formalism.CountingSumsFrames.TheoremMV7Of`).

*Proof.* Apply the general form with $N = 2s + 1$, $X = \lfloor 8a + r\rfloor$, $\lambda' = \lambda$, $\kappa$ as above, $\kappa_4 = (s + 4)r^2\lambda$ and $e_1 = \lfloor r^2\lambda\rfloor$. The size conditions follow at once, and $\frac32(2s + 3)r^2\lambda \leq 3(s + 2)r^2\lambda$, $(2s + 3)\lfloor r^2\lambda\rfloor \leq \kappa$, and $3\lambda + (s + 4)r^2\lambda \leq \kappa$ since $r^2 \geq 4$. $\square$

**Theorem 6.7.12 (Mean bad count on a progression grid).** Under the hypotheses of the previous theorem without the three hypotheses at the points of $G$, the same bound holds.

Lean: `Formalism.InvariantFactorPaths.MC.theoremMV7` (also `Formalism.CountingSumsFrames.TheoremMV7`).

*Proof.* We check the three hypotheses at each $n \in G$. $\mathrm{HypP}$ and $\mathrm{HypW}$ hold with $e_1$ whenever $\binom{r}{2}\lfloor\log_p(|L_n| + r - 1)\rfloor \leq e_1$. Since $|L_n| \leq |L_{n^{\mathrm{top}}}| \leq 8a + r$, we have $\lfloor\log_p(|L_n| + r - 1)\rfloor \leq \lambda$, and $\binom{r}{2} \leq r^2$ gives the bound with $e_1 = \lfloor r^2\lambda\rfloor$. For $\mathrm{Gram}$ apply the Gram lemma to $L^{(i)}$, which has $K + 1$ rows with $K = \mathrm{pos}_i$ and $v_K = +$. Here $|L^{(i)}| \leq S_i$ and $2S_i + 1 \leq 8a + r$, so $4|L^{(i)}| + r - 1 \leq p(8a + r)$ and both logarithms are at most $\lambda$. Finally $\mathrm{pos}_i + 7 \leq 2(s + 4)$, so $(\mathrm{pos}_i + 7)r^2\lambda/2 \leq (s + 4)r^2\lambda$. Apply the previous theorem. $\square$

**Remark 6.7.13 (Formalization).** All six theorems are in [GramHypothesisOfLogBound.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/PartnerMeanProofs/GramHypothesisOfLogBound.lean#L11), except `tieOpsX_main` in [GammaZeroIntegral.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/PartnerMeanProofs/GammaZeroIntegral.lean#L78). The statements are in [TheoremMXB.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/TheoremMXB.lean#L7) and [ChainOrderLetters.lean](lean:Formalism/PolynomialDimension/ChainOrderLetters.lean#L19); the objects are in [GoodCount.lean](lean:Formalism/MahlerMeasure/GoodCount.lean#L7), [StatementT.lean](lean:Formalism/MahlerMeasure/StatementT.lean#L7) and [CsSaturated.lean](lean:Formalism/MahlerMeasure/CsSaturated.lean#L46). In `meanGamX` and `theoremMXB` each input is chosen by `first | exact` among several names (lines 11 to 26). We did not open the proofs of `meanGamX_of`, `theoremMXB_of_point`, the window lemma, the graded and restricted saturation bounds, `PW.Top.dischargeP`, `PW.Top.dischargeW` or `tie_core`, so those outlines follow statements only; `freeze` and `YYsp` are not unfolded. In `theoremMV7Of` the sign and shape hypotheses enter as `hch` and `hcond` at line 126 and are never used. In `TheoremMV7`, $\rho$ occurs only in a hypothesis. In `tieOpsX_main` the hypothesis `_hp2` ($p \neq 2$) at line 79 is unused. `bad` is a difference of natural numbers, and `goodCount` is a supremum in $\mathbb{N}$. The definition of `YCond` tests colour $0$, while $\rho$ is the last colour.
