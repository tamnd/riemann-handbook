---
title: Arc lifts from level data and the full form of Theorem E
decls:
  - Formalism.ExponentWindows.E.theorem_E_full_form
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Arc lifts from level data and the full form of Theorem E

The assembled form of Theorem E, proved two sections back, needs one hypothesis that is hard to check: each arc vector of the target lifts at each cut with a bounded exponent. This section derives that hypothesis from *level data*: at each level $s$ of the arc, a module in which the arc vectors are read, with lattices that measure integrality at $p_s$. The step from the level data to the level conditions of the previous section is a bridge, and the lifting modulo constants of the previous section closes the argument. The result is the *full form* of Theorem E, used in [the primitive form](/entry/theorem-e-primitive-form/).

We keep the notation of the two previous sections: a Frobenius base $B$ over $\mathcal{O}$ with $\ell$ and $p_s = \varphi^s(X + \ell)$, lattices $V$ over $B$ with $n$ letters, a set of cuts $\mathcal{C}$, and $\Lambda \colon \mathbb{Z}/n \to \mathcal{O}[[X]]$. For a cut $c$ with previous cut $c' = c - \ell_c$, put
$$W_c(V) = \bigl(\mathrm{Pull}(c', \ell_c) : \Lambda_c\bigr), \qquad \Theta_g = \prod_{s < \ell_c} p_s^g .$$
So the arc vectors at $c$ are the elements of $W_c(V)$ that are $\gamma$-congruent at $c$. For a polynomial $P = \sum_k a_k T^k$ over $\mathcal{O}$ and an additive map $\gamma$ write $P(\gamma) w = \sum_k a_k \gamma^k(w)$. For an additive subgroup $D$ and a submodule $S$ write $e \in D + S$ if $e - d \in S$ for some $d \in D$.

**Definition 8.11.1 (Level data).** Let $V$ be a lattice over $B$, $c$ a cut and $r \in \mathbb{N}$. A *level datum* for $V$ at $c$ of rank $r$ is an $\mathcal{O}[[X]]$-module $E$ and, for each $s \in \mathbb{N}$: an additive map $g_s \colon E \to E$ with $g_s(a e) = \gamma(a) g_s(e)$; $\mathcal{O}[[X]]$-linear maps $\mathrm{loc}_s \colon W_c(V) \to E$ and $\mathrm{loc}'_s \colon \mathcal{O}[[X]]^r \to E$; submodules $N^\ell_s$, $N^b_s$ and $F_s$ of $E$; and an additive subgroup $D_s \subseteq E$. Let $g, \sigma \in \mathbb{N}$ and let $P$, $P'$ be polynomials over $\mathcal{O}$. We use the following conditions, each for all $s < \ell_c$.

1. (*Equivariance*) $\mathrm{loc}_s(\gamma_c w) = g_s(\mathrm{loc}_s w)$ whenever $w$ and $\gamma_c w$ lie in $W_c(V)$.
2. (*Invariants*) If $g_s(\mathrm{loc}_s w) - \mathrm{loc}_s w \in N^\ell_s$, then $\mathrm{loc}_s w \in D_s + N^\ell_s$.
3. (*Comparison*) $N^b_s \subseteq (N^\ell_s : p_s^g)$ and $N^\ell_s \subseteq (N^b_s : p_s^g)$.
4. (*The polynomial $P$*) If $e \in D_s + (N^b_s : p_s^g)$, then $P(g_s) e \in D_s + N^b_s$.
5. (*The polynomial $P'$*) If $e \in D_s + (N^\ell_s : p_s^g)$, then $P'(g_s) e \in D_s + N^\ell_s$.
6. (*Constants*) $g_s$ fixes each element of $D_s$ and maps $N^\ell_s$ into itself.
7. (*Partners with* $\sigma$) For each $w \in W_c(V)$ there is $y \in \mathcal{O}[[X]]^r$ with $\mathrm{loc}'_s y - \ell^\sigma \mathrm{loc}_s w \in F_s$ for all $s < \ell_c$; for each $y$ there is $w \in W_c(V)$ with $\mathrm{loc}_s w - \ell^\sigma \mathrm{loc}'_s y \in F_s$ for all $s < \ell_c$.
8. (*Errors*) $F_s \subseteq N^\ell_s \cap N^b_s$.
9. (*Divisibility*) $(N_c : \Theta_g) \subseteq W_c(V)$, and $x \in W_c(V)$ lies in $(N_c : \Theta_g)$ if and only if $\mathrm{loc}_s x \in (N^\ell_s : p_s^g)$ for all $s < \ell_c$.
10. (*Multiples of* $X$) $x \in W_c(V)$ lies in $X N_c$ if and only if $x \in X W_c(V)$ and $\mathrm{loc}_s x \in N^\ell_s$ for all $s < \ell_c$.
11. (*Bridge*) For numbers $H_s, b_s$, kinds and submodules $U(s) \subseteq \mathcal{O}^r$ as in the previous section: $y \in \mathrm{N}$ if and only if $\mathrm{loc}'_s y \in N^b_s$ for all $s < \ell_c$, and $y \in \mathrm{I}$ if and only if $\mathrm{loc}'_s y \in D_s + N^b_s$ for all $s < \ell_c$.

Here $\mathrm{loc}_s$ reads an arc vector at the level $s$, and $\mathrm{loc}'_s$ reads a vector of coordinates there; condition 7 says that both readings agree up to $\ell^\sigma$ and an error in $F_s$. The lattice $N^\ell_s$ is the integral lattice at the level $s$, and $N^b_s$ is a second lattice that differs from it by at most $p_s^g$ in both directions. Condition 11 ties the lattice $N^b_s$ and the constants $D_s$ to the level conditions $\mathrm{N}$ and $\mathrm{I}$ of the previous section. Condition 9 says that divisibility by $\Theta_g$ in $N_c$ can be read level by level, and condition 10 does the same for $X N_c$.

**Definition 8.11.2 (Level map).** Let $h \colon V_1 \to V_2$ be a map of lattices, and let $E_1$, $E_2$ be level data for $V_1$, $V_2$ at $c$ of ranks $r_1$, $r_2$. A *level map* is an $\mathcal{O}[[X]]$-linear map $\pi \colon E_1 \to E_2$ with an $\mathcal{O}$-linear map $P_0 \colon \mathcal{O}^{r_1} \to \mathcal{O}^{r_2}$, extended to power series coefficientwise, such that for all $s < \ell_c$
$$\pi\bigl(\mathrm{loc}_s w\bigr) = \mathrm{loc}_s\bigl(h(w)\bigr), \qquad \pi\bigl(\mathrm{loc}'_s y\bigr) = \mathrm{loc}'_s\bigl(P_0(y)\bigr),$$
whenever $w \in W_c(V_1)$ and $h(w) \in W_c(V_2)$. It *preserves errors* if $\pi(F_s) \subseteq F_s$ for all $s < \ell_c$. The map $h$ *lifts divisible vectors with* $r$ at $c$ if for every $x \in (N_c(V_2) : \Theta_g)$ there is $x_1 \in (N_c(V_1) : \Theta_g)$ with $h(x_1) = \ell^r x$.

The polynomials $P$ and $P'$ are the factors of a congruence: they *have value* $\kappa$ if $P(1) P'(1) = \varepsilon \ell^k$ for a unit $\varepsilon \in \mathcal{O}^\times$ and some $k \le 2\kappa$.

**Theorem 8.11.3 (Arc lift from level data).** Let $h \colon V_1 \to V_2$ be a map of lattices over $B$, $c$ a cut, $g, \sigma, r, a_0, \kappa \in \mathbb{N}$, and let $E_1$, $E_2$ be level data at $c$ with a level map $(\pi, P_0)$, numbers $H_s, b_s$, kinds, submodules $U_1(s)$, $U_2(s)$ and polynomials $P$, $P'$ with value $\kappa$. Assume:

1. $\Lambda_c = \prod_{s < \ell_c} p_s^{H_s}$;
2. $\gamma(X) \in (X)$, and $\gamma_c(v) - v \in X N_c(V_2)$ for $v \in N_c(V_2)$;
3. for $k = 1, 2$, $\gamma_c(w) - w \in X W_c(V_k)$ for every $w \in W_c(V_k)$;
4. $E_1$ satisfies conditions 1, 3, 5, 6, 7, 8, 9, 10 and 11 (for $U_1$), and $E_2$ satisfies conditions 1, 2, 3, 4, 7, 8, 9, 10 and 11 (for $U_2$);
5. the level map preserves errors, and $h$ lifts divisible vectors with $r$;
6. $P_0$ lifts modulo constants with $a_0$.

Then for each arc vector $w$ of $V_2$ at $c$ there are an arc vector $w'$ of $V_1$ at $c$, a number $k \le 2\kappa$ and a unit $\varepsilon$ with
$$h(w') - \varepsilon\, \ell^{2\sigma + 2a_0 + r + k}\, w \in X N_c(V_2).$$

Lean: `Formalism.ExponentWindows.E.arc_lift_of_localization_data`.

*Proof.* Let $P(1) P'(1) = \varepsilon \ell^k$ with $k \le 2\kappa$. We first note two facts in $V_2$. By hypothesis 2, $\gamma_c$ maps $N_c$ into $N_c$, and $\gamma_c(X v) = \gamma(X) \gamma_c(v) \in X N_c$; so $X N_c$ is stable under $\gamma_c$. Hence, if $w$ is $\gamma$-congruent, then $\gamma_c^k w - w \in X N_c$ for all $k$ by induction, and
$$P(\gamma_c) w - P(1) w \in X N_c(V_2). \tag{$*$}$$
By hypothesis 3, $W_c(V_k)$ is stable under $\gamma_c$.

*Step 1: in $V_2$.* Let $w$ be an arc vector of $V_2$ and $x' = P(\gamma_c) w \in W_c(V_2)$. By $(*)$, $x' - P(1) w \in X N_c$. Since $\gamma_c$ commutes with constants, $\gamma_c(x') - x'$ is the sum of $\gamma_c(u) - u$ with $u = x' - P(1) w$ and $P(1)(\gamma_c w - w)$, so $x'$ is $\gamma$-congruent. Now fix $s < \ell_c$. Since $\gamma_c w - w \in X N_c$, condition 10 and equivariance give $g_s(\mathrm{loc}_s w) - \mathrm{loc}_s w \in N^\ell_s$. Condition 2 gives $\mathrm{loc}_s w \in D_s + N^\ell_s$, which lies in $D_s + (N^b_s : p_s^g)$ by condition 3. Condition 4 and equivariance give $\mathrm{loc}_s x' = P(g_s) \mathrm{loc}_s w \in D_s + N^b_s$.

*Step 2: to the coordinates and back.* Let $y$ be a partner of $x'$ in $\mathcal{O}[[X]]^{r_2}$. Since $\ell^\sigma D_s \subseteq D_s$ and $F_s \subseteq N^b_s$, we get $\mathrm{loc}'_s y \in D_s + N^b_s$ for all $s$, so $y \in \mathrm{I}_2$ by the bridge. Lifting modulo constants gives $y_1 \in \mathrm{I}_1$ and $\nu \in \mathrm{N}_2$ with $\ell^{2a_0} y = P_0(y_1) + \ell^{2a_0} \nu$. By the bridges, $\mathrm{loc}'_s y_1 \in D_s + N^b_s$ in $E_1$ and $\mathrm{loc}'_s \nu \in N^b_s$ in $E_2$. Let $x_1 \in W_c(V_1)$ be a partner of $y_1$, and put $\Delta = \ell^{2\sigma + 2a_0} x' - h(x_1) \in W_c(V_2)$. With the two rules of the level map,
$$\begin{aligned} \mathrm{loc}_s \Delta = &- \ell^{\sigma + 2a_0} \bigl( \mathrm{loc}'_s y - \ell^\sigma \mathrm{loc}_s x' \bigr) - \pi\bigl( \mathrm{loc}_s x_1 - \ell^\sigma \mathrm{loc}'_s y_1 \bigr) \\ &+ \ell^{\sigma + 2a_0} \mathrm{loc}'_s \nu . \end{aligned}$$
The first term lies in $F_s \subseteq N^b_s$, the second in $\pi(F_s) \subseteq F_s \subseteq N^b_s$, and the third in $N^b_s$. By condition 3, $\mathrm{loc}_s \Delta \in (N^\ell_s : p_s^g)$ for all $s$, so $\Delta \in (N_c(V_2) : \Theta_g)$ by condition 9. Since $h$ lifts divisible vectors, there is $\Delta_1 \in (N_c(V_1) : \Theta_g)$ with $h(\Delta_1) = \ell^r \Delta$, and $\Delta_1 \in W_c(V_1)$ by condition 9. Put $z = \ell^r x_1 + \Delta_1$. Then
$$h(z) = \ell^r h(x_1) + \ell^r \bigl( \ell^{2\sigma + 2a_0} x' - h(x_1) \bigr) = \ell^{2\sigma + 2a_0 + r} x' .$$
Let $d \in D_s$ with $\mathrm{loc}'_s y_1 - d \in N^b_s$. Then $\mathrm{loc}_s z - \ell^{r + \sigma} d$ is the sum of $\ell^r (\mathrm{loc}_s x_1 - \ell^\sigma \mathrm{loc}'_s y_1)$, in $F_s \subseteq N^\ell_s$; of $\ell^{r + \sigma}(\mathrm{loc}'_s y_1 - d)$, in $N^b_s \subseteq (N^\ell_s : p_s^g)$; and of $\mathrm{loc}_s \Delta_1$, in $(N^\ell_s : p_s^g)$ by condition 9. So $\mathrm{loc}_s z \in D_s + (N^\ell_s : p_s^g)$ for all $s$.

*Step 3: in $V_1$.* Put $w' = P'(\gamma_c) z \in W_c(V_1)$. By condition 5 and equivariance, $\mathrm{loc}_s w' = P'(g_s) \mathrm{loc}_s z \in D_s + N^\ell_s$; let $d \in D_s$ with $\mathrm{loc}_s w' - d \in N^\ell_s$. Since $g_s(d) = d$,
$$\mathrm{loc}_s(\gamma_c w' - w') = g_s(\mathrm{loc}_s w' - d) - (\mathrm{loc}_s w' - d),$$
which lies in $N^\ell_s$ by condition 6. Since also $\gamma_c w' - w' \in X W_c(V_1)$ by hypothesis 3, condition 10 gives $\gamma_c w' - w' \in X N_c(V_1)$. So $w'$ is an arc vector of $V_1$.

*Step 4: the congruence.* Since $h$ commutes with $\gamma_c$ and $\gamma_c$ commutes with constants, $h(w') = P'(\gamma_c) h(z) = \ell^{2\sigma + 2a_0 + r} P'(\gamma_c) x'$. With $P'(1) P(1) = \varepsilon \ell^k$,
$$\begin{aligned} h(w') - \varepsilon \ell^{2\sigma + 2a_0 + r + k} w = \ell^{2\sigma + 2a_0 + r} \Bigl( &\bigl( P'(\gamma_c) x' - P'(1) x' \bigr) \\ &+ P'(1) \bigl( x' - P(1) w \bigr) \Bigr). \end{aligned}$$
The first bracket lies in $X N_c(V_2)$ by $(*)$ for the $\gamma$-congruent vector $x'$, and the second by Step 1. $\square$

The exponent $2\sigma + 2a_0 + r + k$ collects the four losses: $\ell^\sigma$ twice for the partners, $\ell^{2a_0}$ for the lift of constants, $\ell^r$ for the divisible part, and $\ell^k$ for the two polynomials. The polynomial $P$ moves an arc vector into the part where the constants $D_s$ describe the levels, and $P'$ moves the lift back to an arc vector.

**Theorem 8.11.4 (Full form of Theorem E).** Let $\mathcal{O}$ be a discrete valuation ring with uniformizer $\varpi$. Take the setting and the hypotheses 1 to 4 of the assembled form: $B$, $\mathcal{C}$, $\Lambda$, $j, M, g, \sigma, r, a_0, \kappa$, the map $h \colon V_1 \to V_2$, $e_0 \in V_0$ and $Z_1$, $Z_2$. Assume also $r \le 2a_0$, and that for each cut $c$ there are level data $E_1$, $E_2$ for $V_1$, $V_2$ at $c$ of ranks $r_1$, $r_2$, a level map $(\pi, P_0)$, numbers $H_s, b_s$, kinds, submodules $U_1(s)$, $U_2(s)$ and polynomials $P$, $P'$ such that:

1. the hypotheses 1 and 3 to 5 of the arc lift from level data hold, and $P$, $P'$ have value $\kappa$;
2. the level model setting holds for $\varpi$, the number $\ell$ of the base, the family $(p_s)_{s < \ell_c}$ and $U_1$, $U_2$;
3. $P_0$ lifts with $r$, and the kinds form an arc word for $P_0$ and $a_0$.

Then for every $\kappa' \in Z_2$ there is $\kappa_1 \in Z_1$ such that $\ell^{2r + 4\sigma + 2a_0 + 2\kappa} \kappa' - h(\kappa_1)$ is a coboundary of $V_2$.

Lean: `Formalism.ExponentWindows.E.theorem_E_full_form`.

*Proof.* This is the assembled form; we check its arc lifting hypothesis at each cut $c$ with the arc lift from level data. Its hypothesis 2 holds: $\gamma(X) \in (X)$ is the first condition of a good base, and $\gamma_c(v) - v \in X N_c(V_2)$ for $v \in N_c(V_2)$ is the first condition of the good lattice $V_2$. Its hypothesis 6 holds by lifting modulo constants from the word (previous section), applied with the level model setting, the lift with $r$, $r \le 2a_0$ and the arc word. The other hypotheses are assumed. $\square$

**Remark 8.11.5 (Formalization).** The level data are `LevelData`, their conditions `Equiv`, `K2iii`, `RD`, `K3a2`, `K3a4`, `DcFix`, `Partner`, `P3`, `DivisibleIff`, `XMulIff` and `Bridge`, the level map `LevelMap` with `MapFl`, and the lift of divisible vectors `LiftsDivisible` ([ArcLiftOfLocalizationData.lean](lean:Formalism/DistinguishedUnitIdeals/ArcLiftOfLocalizationData.lean#L46)); the condition names follow the written proof. The level data are abstract: $E$, the maps and the lattices are free, and nothing in these files constructs them. The first hypothesis of the arc lift, $\Lambda_c = \prod p_s^{H_s}$, is not used in its proof (it is bound to `_` at [line 282](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ArcLiftOfLocalizationData.lean#L282)); the full form still asks for it, as the first of the 27 conditions of `ArcProps` (WordConsts.lean line 63). The three steps of the proof are `step2`, `step3` and `step4`. The full form is the statement `ThmEFull` (WordConsts.lean line 86). The arc word of a cut carries the constants of the words with two downs and with an up after a down as data, although the word constants lemma of the previous section shows that they exist.
