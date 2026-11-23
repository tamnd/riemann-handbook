---
title: The primitive form of Theorem E
decls:
  - Formalism.ExponentWindows.E.theorem_E_primitive_form
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The primitive form of Theorem E

The full form of Theorem E asks for a good base, good lattices, good extensions and a level model setting at each cut. The *primitive form* replaces these derived conditions by conditions on $\varphi(X)$, $\gamma(X)$ and the Wach modules $N_i$: bounds for the Frobenius in both directions, freeness, and completeness of $\mathcal{O}$. It also fixes $M$ and $a_0$ in terms of the other numbers. The primitive form is used in [the final form](/entry/theorem-e-final-form/), and the arc data at each cut are checked in [the arc condition of the final form](/entry/prim-arc/).

We keep the notation of the previous sections: $B$ is a Frobenius base with $\ell$, $q = X + \ell$ and $p_s = \varphi^s(q)$; $\mathcal{C}$ is a set of cuts with lengths $\ell_c$; for a lattice $V$ and a cut $c$ with previous cut $c' = c - \ell_c$, $W_c(V) = (\mathrm{Pull}(c', \ell_c) : \Lambda_c)$; and $\Theta_g = \prod_{s<\ell_c} p_s^g$.

**Definition 8.12.1 (Parameters).** For $\ell, t, g, \sigma, r, \ell_{\max}, \kappa \in \mathbb{N}$ put
$$\begin{aligned} M &= \Bigl\lfloor \frac{t + 2g}{\ell - 1} \Bigr\rfloor + 1, \qquad A = 2\sigma + r + 2 g\, \ell_{\max}, \\ E &= 2r + 4\sigma + 2A + 2\kappa . \end{aligned}$$
For a map $H \colon \mathcal{C} \times \mathbb{N} \to \mathbb{N}$ put $\Lambda^H_c = \prod_{s < \ell_c} p_s^{H(c,s)}$.

So $M$ is the least integer with $t + 2g < (\ell - 1) M$, and $E$ is the exponent of the full form with $a_0 = A$.

**Definition 8.12.2 (Primitive conditions).** Let $\mathcal{O}$ be a discrete valuation ring with uniformizer $\varpi$, and $e \in \mathbb{N}$.

1. (*Base*) The base is *primitive* for $\varpi$ and $e$ if $\ell$ is a prime with $\ell \ge 3$, $e \ge 1$, $\ell$ and $\varpi^e$ are associated in $\mathcal{O}$, $\mathcal{O}$ is complete for the $\ell$-adic topology, and for some units $u$, $\epsilon$ of $\mathcal{O}[[X]]$,
$$\varphi(X) = u\, X\, q^{\ell - 1}, \qquad \gamma(X) = X\,(1 + \epsilon\, q).$$
2. (*Numbers*) Let $j, g, G, t, \sigma, \ell_{\max} \in \mathbb{N}$. The numbers are *primitive* if $G \le g \le t$, $1 \le j \le \ell_c \le \ell_{\max}$ for each cut $c$, and
$$(3 g \ell^{j-1} + M)\, \ell \le \sigma\, \ell^{j-1} (\ell - 1)^2 .$$
3. (*Lattice*) A lattice $V$ is *primitive* for $\mathcal{C}$, $j$, $G$, $t$ if: $\gamma_i(v) - v \in X N_i$ for $v \in N_i$; $q^t \varphi_i(N_{i-1}) \subseteq N_i$ for all $i$; $q^G \varphi_i(N_{i-1}) \subseteq N_i$ at the letters $i = c + k$ with $c$ a cut and $1 \le k \le j$; each $N_i$ is free; each $N_c$ with $c$ a cut has a basis $e_1, \dots, e_r$ such that the images of the $e_a$ under the $j$-fold Frobenius $\varphi_{c+j} \circ \dots \circ \varphi_{c+1}$ are linearly independent over $\mathcal{O}[[X]]$; and $\ell v = 0$ implies $v = 0$.
4. (*Unit*) An element $e_0$ of a lattice $V_0$ is a *unit* if $\varphi_i(e_0) = \gamma_i(e_0) = e_0$ and $N_i(V_0) = \mathcal{O}[[X]]\, e_0$ for all $i$, and $a e_0 = 0$ implies $a = 0$.
5. (*Extension*) An extension $Y$ of $V_0$ by $V_2$ is *primitive* with $r$ and $H$ if: for each cut $c$ some element of $N_c(Y)$ maps to $\ell^r e_0$; $Y$ satisfies the first condition of a primitive lattice; $\iota(u) \in N_i(Y)$ implies $u \in N_i(V_2)$; $q^G \varphi_i(N_{i-1}(Y)) \subseteq N_i(Y)$ at the letters $c + k$, $1 \le k \le j$; $Y$ has bases at the cuts as in 3; and the Frobenius of $Y$ is *cobounded along each arc*: for each cut $c$ and $s < \ell_c$, and each $v \in N_{c-s}(Y)$,
$$q^{H(c,s)}\, v \in \mathcal{O}[[X]] \cdot \varphi_{c-s}\bigl(N_{c-s-1}(Y)\bigr).$$
6. (*Classes*) Two additive groups $Z_1$, $Z_2$ of pairs for $V_1$, $V_2$ are *primitive* if $Z_1$ is stable under multiplication by $\mathcal{O}$, $Z_1$ contains every $\rho$-cocycle (with $M$ as above) of every arc vector of $V_1$ for $\Lambda^H$ at every cut, and every element of $Z_2$ is represented at $e_0$ by a primitive extension with $r$ and $H$.

So $q^t$ moves $\varphi_i(N_{i-1})$ into $N_i$ at every letter, and the smaller $q^G$ does so at the $j$ letters after each cut. The cobounded condition in 5 is a bound in the other direction, along each arc.

**Definition 8.12.3 (Primitive words and arc data).** The kinds $\mathrm{kind}_s$ of the steps $s < \ell_c$ and sizes $b_s$ form a *primitive word* for $a_0$ if they form a word with no down step, with one down step, or with a down after an up as in the arc words; or two down steps $s_0 < s_1$ and all other steps thin; or a down step $s_0$ and an up step $s_1 > s_0$, all other steps thin, with $2 b_{s_0} \le \ell b_{s_1}$ and $2 a_0 < b_{s_1}$. Let $h \colon V_1 \to V_2$ be a map of lattices and $c$ a cut. *Primitive arc data* at $c$ for $H$, $g$, $\sigma$, $r$, $a_0$, $\kappa$ are level data $E_1$, $E_2$ for $V_1$, $V_2$ at $c$ with $\Lambda_c = \prod_{s<\ell_c} p_s^{H_s}$, a level map $(\pi, P_0)$, sizes $b_s$, kinds, submodules $U_1(s)$, $U_2(s)$ and polynomials $P$, $P'$ such that:

1. $\gamma_c(w) - w \in X W_c(V_k)$ for $w \in W_c(V_k)$ and $k = 1, 2$;
2. $E_1$ satisfies the level data conditions 1, 3, 5, 6, 7, 8, 9, 10 and 11, and $E_2$ satisfies 1, 2, 3, 4, 7, 8, 9, 10 and 11, with $P$ in 4 and $P'$ in 5;
3. in $E_2$, if $\mathrm{loc}'_s y \in F_s$, then $\varpi^N y = p_s^{H_s} z$ for some $N$ and $z$;
4. the level map preserves errors, and $h$ lifts divisible vectors with $r$;
5. $P_0$ lifts with $r$, and $P_0$ maps $U_1(s)$ into $U_2(s)$ at each up step;
6. $P$ and $P'$ have value $\kappa$;
7. each $U_k(s)$ is saturated: $\varpi v \in U_k(s)$ implies $v \in U_k(s)$;
8. $b_s \le H_s$ at each up step, and $g < b_s$ at each step that is not thin;
9. the kinds and sizes form a primitive word for $a_0$.

So the primitive arc data are the arc data of the full form without the level model setting, the constants of the words, and the lift of $U(s_1)$ at an up after a down; condition 3 and the bound $g < b_s$ are used to produce them.

**Theorem 8.12.4 (Primitive form of Theorem E).** Let $\mathcal{O}$ be a discrete valuation ring with uniformizer $\varpi$, $B$ a Frobenius base, $e \in \mathbb{N}$, $\mathcal{C}$ a set of cuts for $n$, $H \colon \mathcal{C} \times \mathbb{N} \to \mathbb{N}$, and $j, g, G, t, \sigma, r, \kappa, \ell_{\max} \in \mathbb{N}$. Let $h \colon V_1 \to V_2$ be a map of lattices, $e_0 \in V_0$, and $Z_1$, $Z_2$ additive groups of pairs for $V_1$, $V_2$. Assume that the base is primitive for $\varpi$ and $e$, the numbers are primitive, $V_1$ and $V_2$ are primitive lattices, $e_0$ is a unit, $Z_1$ and $Z_2$ are primitive, and at each cut $c$ there are primitive arc data for $H(c, \cdot)$, $g$, $\sigma$, $r$, $A$, $\kappa$. Then for every $\kappa' \in Z_2$ there is $\kappa_1 \in Z_1$ such that
$$\ell^{E}\, \kappa' - h(\kappa_1)$$
is a coboundary of $V_2$, with $E = 2r + 4\sigma + 2A + 2\kappa$.

Lean: `Formalism.ExponentWindows.E.theorem_E_primitive_form`.

The proof applies the full form with $M$, $a_0 = A$ and $\Lambda = \Lambda^H$. It uses results of other files, which we state now; we read their statements and not their proofs.

1. (*Good base*) If $\varphi(X)$ and $\gamma(X)$ have the two shapes of a primitive base and $3g \le (\ell - 1) M$, then the base is good for $j$, $M$, $g$.
2. (*Shape of $\gamma$*) If $\varpi \mid \ell$, $\ell$ is a prime, $\ell \ge 3$ and $\gamma(X) = X(1 + \epsilon q)$, then there is $u_1 \in \mathcal{O}$ with $\gamma(X) = X(u_1 + X a)$ for some $a$ and, for every $r \ge 1$, $u_1^r - 1 = \varepsilon\, \ell^{1 + v_\ell(r)}$ for a unit $\varepsilon$.
3. (*Good lattice*) Let $\varpi \mid \ell$, $\ell \ne 0$ in $\mathcal{O}$, $\ell$ a prime $\ge 3$, $j \ge 1$, $\varphi(X)$ of the shape above and $\gamma(X)$ as in 2, $G \le g$, and let the inequality of primitive numbers hold. Let $\gamma_i(v) - v \in X N_i$ on $N_i$, let $q^{M_i} \varphi_i(N_{i-1}) \subseteq N_i$ with $M_i < (\ell - 1) M$ for all $i$ and $M_{c+k} \le G$ for the letters after the cuts, and let $V$ have the bases of 3 at the cuts. If each $N_i$ is complete for the $(\ell, X)$-adic topology, $X v = 0$ implies $v = 0$ in $N_i$, and $\ell v = 0$ implies $v = 0$, then $V$ is good.
4. (*Completeness and regularity*) If $\mathcal{O}$ is $\ell$-adically complete and each $N_i$ is free, then each $N_i$ is complete and $X$ is regular on $N_i$.
5. (*Arc span*) If $q^{t_s} N_{c-s} \subseteq \mathcal{O}[[X]] \cdot \varphi_{c-s}(N_{c-s-1})$ and $t_s \le H_s$ for $s < m$, then $N_c \subseteq \bigl(\mathrm{Pull}(c - m, m) : \prod_{s < m} p_s^{H_s}\bigr)$.
6. (*Lemma C*) Let $\ell \sim \varpi^e$ with $e \ge 1$, let the level model setting hold, and let the level data satisfy conditions 3, 7, 8, 9 and 11, with condition 3 of the primitive arc data in $E_2$, a level map that preserves errors, and an $h$ that lifts divisible vectors with $r$. Let $s_0 < s_1$ be a down and an up step with all other steps thin, let $P_0$ map $U_1(s_1)$ into $U_2(s_1)$, and let $2\sigma + r + 2 g \ell_c \le a_0$, $2a_0 < b_{s_1}$ and $2 b_{s_0} \le \ell b_{s_1}$. Then each $v \in U_2(s_1)$ has $v_1 \in U_1(s_1)$ with $P_0(v_1) = \ell^{2a_0} v$.

*Proof of the primitive form.* We check the hypotheses of the full form with $M$, $a_0 = A$ and $\Lambda = \Lambda^H$.

*Numbers.* $M \ge 1$, and $t + 2g < (\ell - 1) M$ since $\ell \ge 2$; so $3g \le t + 2g < (\ell - 1) M$, as $g \le t$. Also $r \le 2A$.

*The base.* By result 1 and $3g \le (\ell - 1) M$, the base is good for $j$, $M$, $g$.

*The lattices.* Let $V$ be $V_1$ or $V_2$. Since $\ell \sim \varpi^e$ with $e \ge 1$, $\varpi \mid \ell$ and $\ell \ne 0$. Result 2 gives the shape of $\gamma(X)$ needed in result 3. Put $M_i = G$ if $i = c + k$ for a cut $c$ and $1 \le k \le j$, and $M_i = t$ otherwise. Then $q^{M_i} \varphi_i(N_{i-1}) \subseteq N_i$ by the two Frobenius bounds, and $M_i \le t < (\ell - 1) M$ since $G \le g \le t$. Result 4 gives completeness and regularity from the freeness of the $N_i$. So $V$ is good by result 3.

*The unit and the classes.* These hypotheses are assumed.

*Extensions.* Let $\kappa' \in Z_2$ and let $Y$ be a primitive extension that represents it; we check that $Y$ is good with exponent $r$. The lift of $\ell^r e_0$ and the first condition are assumed. Since $N_i(V_0) = \mathcal{O}[[X]] e_0$ and $a e_0 = 0$ forces $a = 0$, $X$ is regular on $N_i(V_0)$, and with $\iota(u) \in N_i(Y) \Rightarrow u \in N_i(V_2)$ this gives $\iota(u) \in X^k N_i(Y) \Rightarrow u \in X^k N_i(V_2)$. The bound with $G$ after the cuts and $G \le 3g$ give condition 4. Since $\varpi \mid \ell$, $\ell \ne 0$ and $\varphi(X)$ has its shape, $f$ is saturated for $\ell$, and with the bases at the cuts this gives condition 7. Result 5 with $t_s = H_s$ gives $N_c(Y) \subseteq (\mathrm{Pull}_Y(c', \ell_c) : \Lambda^H_c)$. For the last condition we use that the $k$-fold Frobenius of $V_0$ is free with basis $1, X, \dots, X^{\ell^k - 1}$, which follows from the shape of $\varphi(X)$, the completeness of $\mathcal{O}$ and $\ell$ not a unit.

*Arc data.* Let $c$ be a cut. First we build the level model setting. By the shape of $\varphi(X)$, the completeness of $\mathcal{O}$ and $\ell$ not a unit, each $p_s$ with $s < \ell_c$ is a unit times a monic polynomial $E_s$ of degree $\ell^s$ whose lower coefficients are divisible by $\ell$ and whose constant term is associated to $\ell$. Since $\varpi \mid \ell$, each $p_s$ is a unit times a distinguished polynomial of degree $\ell^s$. For $s < s'$ the shape of $\varphi(X)$ shows that $p_s$ divides $\varphi^t(X)$ for $t > s$, and so $p_{s'} = d\, p_s + \ell$ for some $d$. With $\epsilon \ell = \varpi^e$ for a unit $\epsilon$ we get $\epsilon\, p_{s'} - \epsilon d\, p_s = \varpi^e$, so $p_s$ and $p_{s'}$ are coprime up to $\varpi$. Hence $(p_s)$ is a distinguished family for $\ell$. With the saturation of the $U_k(s)$ and $b_s \le H_s$ at up steps, the level model setting holds.

Next the word. A primitive word with no down step, one down step, or a down after an up is an arc word. For two down steps, the word constants lemma gives the constants $\rho$ and $f_\rho$ of a word with two downs. If it has a down step $s_0$ and an up step $s_1 > s_0$, then $g < b_{s_0}$, so $b_{s_0} \ge 1$, and the word constants lemma gives the constants $\alpha$, $\beta$ of a word with an up after a down. Since $\ell_c \le \ell_{\max}$,
$$2\sigma + r + 2 g\, \ell_c \le 2\sigma + r + 2 g\, \ell_{\max} = A,$$
and Lemma C, with $a_0 = A$, $2A < b_{s_1}$ and $2 b_{s_0} \le \ell b_{s_1}$, gives the lift of $U_2(s_1)$ to $U_1(s_1)$ with $\ell^{2A}$. So the kinds form an arc word for $P_0$ and $A$. The other conditions of the full form are among the primitive arc data, and the full form gives the claim, since its exponent is $2r + 4\sigma + 2A + 2\kappa = E$. $\square$

The number $\kappa$ enters only through the value of $P$ and $P'$, and $t$ only through $M$. The next section constructs the arc data from filtered level models.

**Remark 8.12.5 (Formalization).** The statement is `ThmEPrim`, with the conditions `PrimBase`, `PrimNum`, `PrimLat`, `PrimUnit`, `PrimExt`, `PrimBK`, `PrimWord` and `PrimArc` ([FrobeniusCoboundedArc.lean](lean:Formalism/DistinguishedUnitIdeals/FrobeniusCoboundedArc.lean#L12)); $M$, $A$, $E$ are `parM`, `parA`, `parE`, and the inequality of primitive numbers is `SigOK`. The proof ([ThmEPrim.lean](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ThmEPrim.lean#L477)) uses the four parts `baseGood`, `latGood`, `extGood` and `arcHyp` of the same file. The results 1 to 6 are `base_ring_good_holds`, `one_add_unit_pow_formula`, `good_lattice_holds`, `completion_holds` with `X_regular_on_lattice`, `pullback_lemma_holds` and `lemma_C_full_holds`, with statements `BaseGoodOf`, `ExistsGammaXUnitShape`, `LatGoodOf`, `CompleteOf` with `XRegOf`, `LatticeLeArcSpan` (FrobeniusDiffBijective.lean lines 115 to 196) and `LemmaCFull` (LemmaCFull.lean line 26); Lemma C rests on a valuation bound for elements of $(\varpi^k, p_{s_1}^{b_1})$, proved as `lemma_C_valuation_real` (LemmaC.lean line 25). For extensions the proof also uses `saturation_first_form_holds`, `extension_complete_holds`, `lattice_induction_lemma_holds`, `saturation_holds_alt` and `extension_generated_holds`. The inequality $r \le 2A$ is closed by the fallback `first | omega | nlinarith` (ThmEPrim.lean line 490). The cobounded condition of an extension is asked with the exponent $H(c,s)$ itself, so result 5 is used with equal bounds.
