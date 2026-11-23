---
title: The edge class congruence
decls:
  - GlobalTheory.EdgeLoc.edge_dlog
  - GlobalTheory.pair_edge_dlog
  - GlobalTheory.T.siegelUnit_edgeClass_kummer_dlog_congruence
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The edge class congruence

Two units $a$, $b$ give two Kummer characters $x$, $y$, and their cup product $x \cup y$ is a class in degree $2$. When $x \cup y$ vanishes on the geometric Galois group, a choice of trivialisation $\eta$ gives, for each Galois element $\sigma$, a Kummer class on the geometric group: the *edge class*. This section computes the logarithmic $q$-expansion of that edge class modulo $p^n$, up to a coboundary. First this is done in the local setting of [Section 6.11.8](/entry/h1-geometric-level-coboundary/), for units with logarithmic coordinates. Then it is done for two smoothed Siegel units in a tower of modular functions, where the answer is a product of two Eisenstein series of weight $1$. The result is used in [the edge congruence for translated Siegel units](/entry/one/) of the Kato chapter, which feeds case I of [the window bound](/proof/vwin/).

We keep the notation of Section 11: an odd prime $p$, the ring $\mathcal{O}$, a closure $\Omega$ with a tower $(\zeta_m, q_m)$, the groups $G$, $G_L$ and $G_{\mathrm{geo}}$, integrality, congruences modulo $p^n$, Kummer characters, and reparametrizations. Kummer characters are the finite level form of the characters of [Tate modules](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules).

**Definition 6.12.1 (Level $L$ coordinate ring).** Let $\mathcal{O}_L = \mathcal{O}[X, Y]/(\Phi_{p^L}(X), Y^{p^L} - q)$, where $\Phi_{p^L}$ is the cyclotomic polynomial. An *embedding* is an $\mathcal{O}$-algebra map $\iota : \mathcal{O}_L \to \Omega$ with $\iota(X) = \zeta_L$ and $\iota(Y) = q_L$.

**Definition 6.12.2 (Logarithmic coordinates).** Let $w, \alpha, \beta \in \mathcal{O}_L$. Then $(\alpha, \beta)$ are *logarithmic coordinates* of $w$ if, in the module of Kähler differentials of $\mathcal{O}_L$ over $\mathcal{O}$,
$$
XY\, dw = wX\alpha\, dY + wY\beta\, dX.
$$

Formally this says $d\log w = \alpha\, d\log Y + \beta\, d\log X$. The term $\alpha\beta' - \beta\alpha'$ for two units is the coefficient of $d\log w \wedge d\log w'$ on $d\log Y \wedge d\log X$.

**Definition 6.12.3 (Evaluation of a series).** Let $\psi$ be a reparametrization at level $L$ and $\vartheta = q\frac{d}{dq}$ on $\mathbb{Z}_p((q))$. Let $c : \mathbb{Z} \to \Omega$ and $w, w' \in \Omega$. The triple $(c, w, w')$ is an *evaluation* if there are finitely many $e_t \in \Omega$, integral and algebraic over $\mathbb{Z}_p$, and $a_t \in \mathbb{Z}_p((q))$ with
$$
c(r) = \sum_t e_t\, a_{t,r}, \qquad w = \sum_t e_t\, \psi(a_t), \qquad w' = \sum_t e_t\, \psi(\vartheta a_t).
$$

So $w$ is a series in $q_L$ with coefficients $c(r)$, and $w'$ is its derivative $q_L \frac{d}{dq_L}$. The quotient $w'/w$ is the logarithmic derivative of $w$ in the parameter $q_L$.

**Definition 6.12.4 (Edge cochain).** Let $\Gamma$ be a group, $x, y : \Gamma \to \mathbb{Z}/p^n$ homomorphisms and $\eta : \Gamma \to \mathbb{Z}/p^n$. For $\sigma, h \in \Gamma$ put
$$
e_\sigma(h) = \eta(\sigma h \sigma^{-1}) - \eta(h) - x(h)y(\sigma) + x(\sigma)y(h).
$$
For a subgroup $\Delta$, we say that $\eta$ *trivialises $x \cup y$ on $\Delta$* if $x(g)y(h) = \eta(h) - \eta(gh) + \eta(g)$ for all $g, h \in \Delta$.

**Theorem 6.12.5 (Local edge congruence).** Let $p$ be an odd prime. There is $c \geq 0$ with the following property. Let $\Omega$ be a closure of $\mathcal{O}$ with a tower, $1 \leq n \leq L$, $\psi$ a reparametrization at level $L$, $\iota$ an embedding of $\mathcal{O}_L$, and $H = G_{\mathrm{geo}} \cap G_L$. Let $u, v$ be units of $\mathcal{O}_L$ with logarithmic coordinates $(\alpha, \beta)$ and $(\alpha', \beta')$. Let $r, s \in \Omega$ with $r^{p^n} = \iota(u)$ and $s^{p^n} = \iota(v)$, let $x$, $y$, $\lambda_\zeta$ be Kummer characters of $r$, $s$, $\zeta_{L+n}$ on $G_L$, and let $\eta : G \to \mathbb{Z}/p^n$ trivialise $x \cup y$ on $H$ and be locally constant on $H$. Then there is an integral $o$ fixed by $H$ with the following property. Let $\sigma \in G_L$ and $\theta, \kappa, a, a', b, b' \in \Omega$ with:

1. $e_\sigma$ is a Kummer character of $\theta$ on $H$;
2. $\kappa \neq 0$ is algebraic over $\mathbb{Z}_p$, and $\theta^{p^n} b = \kappa a$;
3. $(c_a, a, a')$ and $(c_b, b, b')$ are evaluations for some $c_a$, $c_b$;
4. $a, b \neq 0$, and $a^{-1}$, $b^{-1}$ are integral.

Then
$$
p^c\Bigl(\frac{a'}{a} - \frac{b'}{b}\Bigr) \equiv \sigma^{-1}(o) - o - p^c\, \iota(\alpha\beta' - \beta\alpha')\, \lambda_\zeta(\sigma) \pmod{p^n}.
$$

Lean: `GlobalTheory.EdgeLoc.edge_dlog`.

Here $\lambda_\zeta(\sigma)$ is the cyclotomic character of $\sigma$ at level $L + n$, divided by $p^L$, modulo $p^n$. The theorem says that the logarithmic derivative of the edge class is, up to a coboundary $\sigma^{-1}(o) - o$, the wedge term $\alpha\beta' - \beta\alpha'$ times this character.

*Proof.* Let $\lambda_q$ be a Kummer character of $q_{L+n}$ on $G_L$. Four facts are used, each with its own constant.

- (A) The $2$-cochain $(g, h) \mapsto p^{c_1}\bigl(x(g)y(h) + \iota(\alpha\beta' - \beta\alpha')\lambda_\zeta(g)\lambda_q(h)\bigr)$ is a locally constant coboundary modulo $p^n$ on $G_L$.
- (B) Given (A) and $\eta$, there is an integral $o_1$ fixed by $H$ such that, for each $\sigma \in G_L$, the cochain $h \mapsto p^{c_2}e_\sigma(h) - \bigl(\sigma^{-1}(o_1) - o_1 - p^{c_2} f\lambda_\zeta(\sigma)\bigr)\lambda_q(h)$, with $f = \iota(\alpha\beta' - \beta\alpha')$, is a coboundary modulo $p^n$ on $H$.
- (C) If $(c_w, w, w')$ is an evaluation with $w \neq 0$, $w^{-1}$ integral, $\rho^{p^n} = w$, and $k_w$ is a Kummer character of $\rho$ on $H$, then $p^{c_3}k_w - p^{c_3}(w'/w)\lambda_q$ is a coboundary modulo $p^n$ on $H$.
- (D) The second theorem of Section 11, with constant $c_4$.

Let $c = c_2 + c_3 + c_4$ and $o = p^{c_3 + c_4} o_1$. Fix $\sigma$ and the data 1 to 4. Choose $p^n$-th roots $\rho_a$ of $a$ and $\rho_b$ of $b$, with Kummer characters $k_a$ and $k_b$ on $H$; they exist since $a$ and $b$ are fixed by $H$. The element $\theta\rho_b/\rho_a$ is a $p^n$-th root of $\kappa$, so it is algebraic over $\mathbb{Z}_p$ and fixed by $H$. Hence $e_\sigma \equiv k_a - k_b$ on $H$. Put
$$
Z = p^{c_3}\bigl(\sigma^{-1}(o_1) - o_1 - p^{c_2} f\lambda_\zeta(\sigma)\bigr) - p^{c_2 + c_3}\Bigl(\frac{a'}{a} - \frac{b'}{b}\Bigr).
$$
It is integral and fixed by $H$. Combining (B) with (C) for $a$ and for $b$ shows that $Z\lambda_q$ is a coboundary modulo $p^n$ on $H$. By (D), $p^{c_4} Z \equiv 0 \pmod{p^n}$. This is the claim. $\square$

We now pass to modular functions. Let $(K_X, \exp, |, s, \mathrm{an}, j_K)$ be a tower of modular functions over $(\Omega_0, \varepsilon)$ as in [Section 6.1.5](/entry/tower-exists/), with $\Omega_0$ an algebraic closure of $\mathbb{Q}$. Write $\zeta_m = e_{\Omega_0}(1/m)$ and $\zeta_{p^m}$ for $e_{\Omega_0}(1/p^m)$. Let $K_X(M)$ be the subfield of $f \in K_X$ with $f|\begin{pmatrix} 1 & M \\ 0 & 1 \end{pmatrix} = f$.

**Definition 6.12.6 (Smoothed Siegel units and Eisenstein series).** Let $M \geq 1$, $c \geq 1$ and $(A_1, a_2) \in \mathbb{Z}^2$. Let $g_c(A_1, a_2)$ be the element of $K_X$ whose analytic germ is the smoothed Siegel function ${}_c g_{(A_1/M, a_2/M)}$ of the development, or $0$ if there is none. For $N \mid M$ put $u_c(A_1, a_2) = g_c(A_1, a_2)|\mathrm{diag}(N, 1)$. Let $E(A_1, a_2)$ be the sequence with, for $m \geq 1$,
$$
E(A_1, a_2)_m = \sum_{k \mid m}\Bigl([m/k \equiv A_1]\, \zeta_M^{a_2 k} - [-m/k \equiv A_1]\, \zeta_M^{-a_2 k}\Bigr),
$$
with congruences modulo $M$, and with constant term $\frac{1}{2}\frac{1 + \zeta_M^{a_2}}{1 - \zeta_M^{a_2}}$ if $M \mid A_1$ and $\frac12 - \frac{A_1 \bmod M}{M}$ otherwise. Put $F_c(A_1, a_2) = c^2 E(A_1, a_2) - c\, E(cA_1, ca_2)$.

The sequence $E(A_1, a_2)$ is the $q$-expansion of an Eisenstein series of weight $1$ and level $M$, in the parameter $q^{1/M}$, and $F_c$ is its $c$-smoothed form. For two sequences, $F \ast F'$ is the Cauchy product $(F \ast F')_m = \sum_{i \leq m} F_i F'_{m-i}$. For $r \in \mathbb{Q}$ let $[q^r]_L F$ be $F_{rp^L}$ if $rp^L$ is a nonnegative integer, and $0$ otherwise.

**Theorem 6.12.7 (Edge class of two Siegel units).** Let $p$ be an odd prime. There is $c_0 \geq 0$ with the following property. Assume that $\mathrm{an}(j_K)$ is the germ of a function holomorphic on $\mathcal{H}$. Let $A$ be a valuation ring of $\Omega_0$ with $p$ in its maximal ideal. Let $1 \leq n \leq L$, let $N \geq 1$ be prime to $p$, put $M = Np^L$, and let $c, d > 1$ be prime to $6Np$. Let $A_1, a_2, g, B_1, b_2, h \in \mathbb{Z}$ with $N \mid a_2$, $N \mid b_2$, $a_2 \equiv Ng$ and $b_2 \equiv Nh \pmod{p^L}$, $M \nmid A_1$ and $M \nmid B_1$. Let $F \subseteq K \subseteq \Omega'$ be fields with $K/F$ normal and $\Omega'$ an algebraic closure of $K$, and let $e : K \to K_X(p^L)$ be a ring map. Let $z, a, b \in K$ and $\zeta, \alpha, \beta \in \Omega'$ with
$$
e(z) = \zeta_{p^n}, \quad \zeta = z, \quad e(a) = u_c(A_1, a_2), \quad e(b) = u_d(B_1, b_2), \quad \alpha^{p^n} = a, \quad \beta^{p^n} = b.
$$
Let $x, y : \mathrm{Gal}(\Omega'/F) \to \mathbb{Z}/p^n$ be the Kummer characters of $\alpha$, $\beta$ for $\zeta$, and let $\eta$ trivialise $x \cup y$ on $\mathrm{Gal}(\Omega'/K)$ and be locally constant on it. Then there is $\xi : \mathbb{Q} \to A$ with the following property. Let $s \in \mathrm{Gal}(\Omega_0/\mathbb{Q})$ with $s(A) = A$, $s(\zeta_{p^L}) = \zeta_{p^L}$ and $s(\zeta_{p^{L+n}}) = \zeta_{p^n}^t \zeta_{p^{L+n}}$, such that $s$ fixes $e(F)$. Let $\sigma \in \mathrm{Gal}(\Omega'/F)$ with $\sigma(k) = k'$ whenever $e(k') = s(e(k))$. Let $w \in K$, $w \neq 0$, have a $p^n$-th root in $\Omega'$ whose Kummer character on $\mathrm{Gal}(\Omega'/K)$ is $e_\sigma$. Let $\varphi$ be a logarithmic derivative of $e(w)$ modulo $p^n A$ in the sense of [Section 6.8.4](/entry/th-n-hecke/), with $\vartheta$ replaced by $p^L\vartheta$. Then for every $r \in \mathbb{Q}$,
$$
p^{c_0}\varphi_r \equiv s^{-1}(\xi_r) - \xi_r - p^{c_0}(A_1 h - gB_1)\, t\, [q^r]_L\bigl(F_c(A_1, a_2) \ast F_d(B_1, b_2)\bigr) \pmod{p^n A}.
$$

Lean: `GlobalTheory.pair_edge_dlog` (also `GlobalTheory.T.siegelUnit_edgeClass_kummer_dlog_congruence`, a second name).

*Proof.* Take $c$ from the local theorem and put $c_0 = c + 1$.

*Passage to the local setting.* A lemma gives a closure $\Omega_l$ of $\mathcal{O}$ with a tower and a ring map $j : \Omega_0 \to \Omega_l$ such that $y \in A$ if and only if $j(y)$ is integral, $j(y)$ is algebraic over $\mathbb{Z}_p$, $j(\zeta_{p^m}) = \zeta_m$, and $j(A)$ is dense modulo every $p^k$ among the integral elements algebraic over $\mathbb{Z}_p$. Choose a reparametrization $\psi$ at level $L$, an embedding $\iota$ of $\mathcal{O}_L$, and a map from $K_X(p^L)$ to $\Omega_l$ that sends $f$ to its expansion in $q_L$. Extend the composite $K \to \Omega_l$ to $\Omega' \to \Omega_l$.

*Logarithmic coordinates of Siegel units.* For each of the two Siegel units, a lemma gives a unit $u$ of $\mathcal{O}_L$ whose image under $\iota$ is the image of the Siegel unit, logarithmic coordinates $(\alpha_u, \beta_u)$ of $u$, and an evaluation $(j \circ F_c, z_u, z'_u)$ with
$$
\iota(\alpha_u) \equiv -A_1 z_u \pmod{p^L}, \qquad p\,\iota(\beta_u) \equiv -p\, g\, z_u \pmod{p^L}.
$$
With the corresponding data for $d$, $(B_1, b_2)$ and $h$, this gives $p\,\iota(\alpha\beta' - \beta\alpha') \equiv p(A_1 h - g B_1)\, z_a z_b \pmod{p^L}$, where $z_a$ and $z_b$ are the values for the two units. The extra factor $p$ is the reason for $c_0 = c + 1$.

*Galois side.* The characters $x$, $y$ and the cochain $\eta$ move to $G_L$ and $H$ through the extended embedding, and the edge relation is preserved. The local theorem gives $o$. The element $p\,o$ is integral and fixed by $H$. A lemma shows that it is congruent modulo $p^n$ to the value of an evaluation. The coefficients of this evaluation, pulled back to $A$ by density, give $\xi$.

*Value side.* For $s$ and $\sigma$ as in the statement, a lemma gives $a_w, b_w \in K_X(p^L)$ and $\kappa \neq 0$ with $e(w)\, b_w = \kappa\, a_w$, where the expansions of $a_w$ and $b_w$ have primitive coefficients in $A$. Their images are evaluations with nonzero values whose inverses are integral, so the local theorem applies with $\lambda_\zeta(\sigma) = t$. It gives a congruence of values. Lemmas on series with primitive coefficients turn it into a congruence of coefficients, and the uniqueness of logarithmic derivatives modulo $p^n A$ replaces the chosen quotient by $\varphi$. $\square$

**Remark 6.12.8 (Formalization).** In the proof of the local theorem the block that derives $\theta \neq 0$, defines $\rho = \theta\rho_b/\rho_a$, proves its properties and applies (B) at $\sigma$ is written twice, at [GnFixZeta.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/GnFixZeta.lean#L197) lines 197 to 207 and again at lines 208 to 218; the second copy shadows the first. The sequences $c_a$ and $c_b$ in the local theorem are only passed to the evaluation hypotheses and play no other role. The holomorphy hypothesis on $j_K$ duplicates a field of the tower, as in earlier sections. The Kummer characters $x$, $y$ in the global theorem are given as homomorphisms that agree with a Kummer exponent chosen by `choose`, with junk value $0$ when no exponent exists. The element $g_c(A_1, a_2)$ is chosen by `choose` from its analytic germ, with junk value $0$; we did not unfold the Siegel function. The second name is a wrapper under `maxHeartbeats 1000000` ([SiegelUnitEdgeClassKummerDlogCongruence.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/SiegelUnitEdgeClassKummerDlogCongruence.lean#L457)). Facts (A) to (C), the cusp embedding, the Siegel coordinates and the lemmas of the value side were read as statements.
