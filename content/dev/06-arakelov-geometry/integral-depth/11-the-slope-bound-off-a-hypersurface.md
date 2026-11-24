---
title: The slope bound off a hypersurface
decls:
  - GlobalTheory.HSShort.SlopeTop.slopeBound
  - GlobalTheory.T.slopeLowerBound_topLattice_offHypersurface
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The slope bound off a hypersurface

This section proves the lower bound for the degree of the top lattice $M_T$ of a hermitian system. The method is the determinant method. We choose $d = \dim V_T$ elements of $V_T$ that are products of short sections and of linear forms in $D + 1$ groups of variables. Their determinant in a short basis of $M_T$ is a nonzero polynomial. The flat structures of [the previous section](/entry/flat-at-of-simple-at/) show that a high power of the Chow form $f$ divides it. A comparison of heights then bounds $\deg M_T$ from below. The bound is the third input of [the arithmetic Hilbert-Samuel bound](/entry/geo-bound-of-quoted-prime/) ([hermitian lattices and slopes](/learn/arakelov/#hermitian-lattices-and-slopes)).

We use [hermitian systems](/entry/flat-at-of-simple-at/) and flat structures as defined in the previous section. Let $S$ be a hermitian system over a number field $F$.

**Definition 3.11.1 (Lattice frame).** Let $\Lambda \in \mathbb{R}$. The matrix $w$ and the frames $\mathrm{fr}_\sigma$ form a *lattice frame* with constant $\Lambda$ if $N > 0$, the columns $w_1, \dots, w_n$ of $w$ span $F^N$, each $\mathrm{fr}_\sigma$ is invertible, the norm $|\sigma(w_k)|_{\mathrm{fr}_\sigma}$ of each column with respect to the frame is at most $\Lambda$, and $1 \le \Lambda$. Put
$$c(n, \Lambda) = \log(n \Lambda) + \tfrac12 (\log n + 1).$$

The frame defines a height $\mathrm{ht}(G)$ of every polynomial $G$ in $D + 1$ groups of $N$ variables over $F$ ([heights](/learn/arakelov/#heights)). We use two facts on it, both proved in the development: for nonzero multihomogeneous $G$ and $G'$ we have $\mathrm{ht}(G G') = \mathrm{ht}(G) + \mathrm{ht}(G')$ and $\mathrm{ht}(c) = 0$ for constants $c \ne 0$; and if $G \ne 0$ is multihomogeneous of total degree $e$, then $\mathrm{ht}(G) \ge -c(n, \Lambda)\, e$.

**Definition 3.11.2 (Hypotheses of a hermitian system).** The *hypotheses* hold for $S$ if:

1. $1 \le D$ and $D + 1 \le T$;
2. $w$ and $\mathrm{fr}$ form a lattice frame with constant $\Lambda$;
3. the endomorphisms $\mu(u)$ commute with each other;
4. $M_j$ is a full lattice in $V_j$ for $j \le T$;
5. for $j < T$, every column $w_k$ and every $x \in M_j$, the element $\mu(w_k) x$ lies in $M_{j+1}$;
6. for $j < T$, every $\sigma$ and every $u \in \mathbb{C}^N$, multiplication by $u$ from $V_j \otimes_\sigma \mathbb{C}$ to $V_{j+1} \otimes_\sigma \mathbb{C}$ has norm at most $\sqrt\beta\, |u|_{\mathrm{fr}_\sigma}$;
7. $1 \le \beta$, $1 \le \Lambda_0$, $1 \le \Lambda_D$ and $1 \le \Lambda_T$;
8. for $j = 0$, $j = D$ and $j = T$, the space $V_j$ has a basis over $F$ that lies in $M_j$ and whose elements have norm at most $\Lambda_j$ at every $\sigma$.

**Definition 3.11.3 (Slope claim).** Let $T, D \in \mathbb{N}$ and let $n$, $\Lambda$, $\beta$, $\Lambda_0$, $\Lambda_D$, $\Lambda_T$, $\delta$, $h$, $d$, $\deg$ be real numbers. Put $c = c(n, \Lambda)$ and $z = 1 - \binom{T-1}{D}\delta/d$. The *slope claim* $\mathrm{SC}(T, D, n, \Lambda, \beta, \Lambda_0, \Lambda_D, \Lambda_T, \delta, h, d, \deg)$ says that $0 \le z \le 1$ and
$$\begin{aligned}
&(1 - z)\bigl(T h - D(D+1) c - \log \Lambda_0 - \tfrac{T}{2}\log\beta\bigr) \\
&\quad - z\bigl(T c + \tfrac{T}{2}\log\beta + \log\Lambda_D + \log\Lambda_T\bigr) \le \frac{\deg}{d}.
\end{aligned}$$

The two brackets have the same meaning as in [the Hilbert-Samuel claim](/entry/geo-bound-of-quoted-prime/): the first is the gain per section of the deep part, the second is the loss per section of the rest.

**Theorem 3.11.4 (Slope bound for the top lattice).** Let $S$ be a hermitian system over a number field $F$ for which the hypotheses hold. Let $\delta \ge 1$, let $f$ be an irreducible polynomial over $F$ in $D + 1$ groups of $N$ variables that is homogeneous of degree $\delta$ in each group, and let $Q \ne 0$ be a polynomial over $F$ in $D N$ variables. Assume that $S$ is flat at $s$ for $(\delta, f)$ for every $s \in F^{D \times N}$ with $Q(s) \ne 0$. Put $d = \dim_F V_T$. Then $d > 0$ and
$$\mathrm{SC}\Bigl(T, D, n, \Lambda, \beta, \Lambda_0, \Lambda_D, \Lambda_T, \delta, \frac{\mathrm{ht}(f)}{(D+1)\delta}, d, \deg M_T\Bigr).$$

Lean: `GlobalTheory.HSShort.SlopeTop.slopeBound` (also `GlobalTheory.T.slopeLowerBound_topLattice_offHypersurface`, a second name).

Before the proof we fix the objects. Write the $D + 1$ groups of variables as $u_1, \dots, u_D$ and $u_0$; a section $s$ is put in $u_1, \dots, u_D$, and $u_0$ stays free. A *column* is a quadruple $\kappa = (j, t, \beta, x)$ with $j + t = T$, a map $\beta : \{1, \dots, t\} \to \{0, 1, \dots, D\}$ and $x \in V_j$. Let $c_1, \dots, c_d$ be linear forms on $A$ that restrict on $V_T$ to the coordinates in a basis $b$ of $V_T$. For $d$ columns $\kappa_1, \dots, \kappa_d$ put
$$\Delta(u) = \det\bigl[c_i\bigl(\mu(u_{\beta_k(1)}) \cdots \mu(u_{\beta_k(t_k)})\, x_k\bigr)\bigr]_{i, k}.$$
Each entry is a polynomial in the variables, multihomogeneous, of total degree $t_k$. So $\Delta$ is multihomogeneous of total degree $\sum_k t_k$. Put
$$e = \sum_{a = 0}^{T - D - 1} \binom{a + D - 1}{D - 1} (T - a).$$
The number $\binom{a + D - 1}{D - 1}$ is the number of monomials of degree $a$ in $D$ variables, and $\sum_{a < T - D} \binom{a + D - 1}{D - 1} = \binom{T - 1}{D}$.

*Proof.* We follow the steps of the determinant method.

*A short basis.* By hypothesis 8 there is a basis $b_1, \dots, b_d$ of $V_T$ in $M_T$ with norms at most $\Lambda_T$. Take $c_1, \dots, c_d$ as above.

*A section of largest deep rank.* For $s \in F^{D \times N}$ let the *deep rank* $r(s)$ be the dimension of $\sum_{|\alpha| = T - D} s^\alpha V_D$. Since $Q \ne 0$ and $F$ is infinite, there is $s_1$ with $Q(s_1) \ne 0$. For every $s$ with $Q(s) \ne 0$, an input lemma on the deepest step of a flat structure gives $r(s) \le d$. So the deep ranks of these $s$ are bounded, and we choose $s_0$ with $Q(s_0) \ne 0$ whose deep rank $r = r(s_0)$ is the largest.

*The columns.* An input lemma, applied to a flat structure at $s_0$, gives $d$ columns with entries in the lattices and with $\Delta \ne 0$, of three kinds.

1. For each $a < T - D$, each monomial $\alpha$ of degree $a$ and each point $p \le \delta$, one column with $j = 0$, $t = T$ and $x = m_p \in M_0$, in which $\alpha_i$ factors come from the group $u_i$ ($1 \le i \le D$) and the other $T - a$ factors from $u_0$. There are $\binom{T - 1}{D}\delta$ of them.
2. Exactly $r$ columns with $j = D$, $t = T - D$, whose factors all come from $u_1, \dots, u_D$.
3. The other columns, with $j = T$ and $t = 0$.

The element $x$ of each column has norm at most $\Lambda_0$, $\Lambda_D$ or $\Lambda_T$, according to its kind. In particular $\binom{T-1}{D}\delta + r \le d$.

*Divisibility.* Let $s$ with $Q(s) \ne 0$, and take a flat structure at $s$ with points $y_1, \dots, y_\delta$ and the constant $c' \ne 0$ of the factorization of $f(s)$. An input lemma on determinants of rational sections uses the symbols of the flat structure and $r(s) \le r$. It gives $\gamma$ with
$$\Delta(s, l) = \gamma \prod_{p = 1}^{\delta} \langle l, y_p \rangle^{e}$$
for all $l \in F^N$, where $u_0 = l$. Since $f(s, l) = c' \prod_p \langle l, y_p \rangle$, this is $\Delta(s, l) = (\gamma / c'^{e}) f(s, l)^{e}$. The columns of kind 1 explain the exponent: the symbol at $p$ of a column of degree $a$ contributes $\langle l, y_p \rangle^{T - a}$. An input lemma on specializations now gives $f^{e} \mid \Delta$, since $f$ is irreducible, multihomogeneous of degree $\delta \ge 1$ in each group, and the relation holds for all $s$ off the hypersurface $Q = 0$. Write $\Delta = f^{e} G'$. Then $G' \ne 0$ is multihomogeneous, and its total degree is
$$\deg G' = \tbinom{T-1}{D}\delta T + r (T - D) - (D + 1)\delta e.$$

*Heights.* By the facts on heights,
$$\mathrm{ht}(\Delta) = e\, \mathrm{ht}(f) + \mathrm{ht}(G'),$$
with $\mathrm{ht}(f) \ge -c(n, \Lambda)(D + 1)\delta$ and $\mathrm{ht}(G') \ge -c(n, \Lambda) \deg G'$.

*The determinant inequality.* For each column $\kappa_k$ put $B_k = \sqrt\beta^{\,t_k}\Lambda_{j_k}$, where $\Lambda_{j_k}$ is $\Lambda_0$, $\Lambda_D$ or $\Lambda_T$. By hypotheses 5 and 6, the coefficients of the column lie in $M_T$ and its values on vectors of unit norm have norm at most $B_k$. An input lemma, a determinant form of the slope inequality, gives
$$\mathrm{ht}(\Delta) - \sum_{k = 1}^{d} \log B_k \le \deg M_T.$$
The sum of the $\log B_k$ splits over the three kinds of columns:
$$\begin{aligned}
\sum_k \log B_k &= \tbinom{T-1}{D}\delta \bigl(\tfrac{T}{2}\log\beta + \log\Lambda_0\bigr) \\
&\quad + r\bigl(\tfrac{T-D}{2}\log\beta + \log\Lambda_D\bigr) \\
&\quad + \bigl(d - \tbinom{T-1}{D}\delta - r\bigr)\log\Lambda_T.
\end{aligned}$$

*The numbers.* We have $n \ge 1$, since the $n$ columns of $w$ span $F^N$ and $N > 0$. A numerical lemma combines the last inequalities with $(D + 1)e = \binom{T - 1}{D}(T + D(D + 1))$ and $\binom{T-1}{D}\delta + r \le d$. It uses $1 \le \Lambda$, $\beta$, $\Lambda_0$, $\Lambda_D$, $\Lambda_T$ to bound the terms of $r$ and of the columns of kind 3 by the second bracket of the claim, and it gives $d > 0$ and the slope claim with $h = \mathrm{ht}(f)/((D + 1)\delta)$. $\square$

The proof does not need the deep rank $r$ in the final claim. The choice of $s_0$ with the largest deep rank is what makes the divisibility hold at every $s$ off $Q = 0$: at such $s$ the deep part has dimension at most $r$, so the $r$ columns of kind 2 are enough to fill it.

**Example 3.11.5.** Take $D = 1$ and $T = 2$. There is one monomial of degree $0$, so there are $\delta$ columns of kind 1, each of the form $c_i(\mu(u_0)^2 m_p)$, and $e = 2$. The flat structure at a line $s$ gives $\Delta(s, l) = \gamma \prod_p \langle l, y_p \rangle^2$: each of the $\delta$ columns contributes the square of the linear form of its point. So $f^2 \mid \Delta$, and $(D + 1)e = 4 = \binom{1}{1}(2 + 2)$.

**Remark 3.11.6 (Formalization).** The largest deep rank is chosen as the largest $y \le d$ that is the deep rank of some $s$ with $Q(s) \ne 0$ ([SlopeLowerBoundTopLatticeOffHypersurface.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SlopeLowerBoundTopLatticeOffHypersurface.lean#L106)). The hypothesis $1 \le \Lambda_0$ is stored under a name that refers to the hermitian system and not to $\Lambda_0$, and the constant $\Lambda$ is stored under the name `abelian₂` ([HermSysHypOneLeLambdaZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HermSysHypOneLeLambdaZero.lean#L159)). The slope claim writes $1 - z$ as $1 - (1 - \binom{T-1}{D}\delta/d)$. We have not unfolded the height of a polynomial, the arithmetic degree or the norm of a complex combination; hypothesis 6 is our reading of the bound on these norms. The second name is a wrapper.
