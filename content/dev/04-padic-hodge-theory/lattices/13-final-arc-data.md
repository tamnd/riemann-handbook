---
title: Final arc data give primitive arc data
decls:
  - Formalism.ExponentWindows.E.JumpSetWindowBounds.primArc
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Final arc data give primitive arc data

The primitive form of Theorem E asks, at each cut, for primitive arc data: two level data, a level map, two polynomials with a value, and a word. The final form replaces these by the [final arc data](/entry/final-arc-holds/) of the section on level steps, which come from level models with filtrations whose jumps lie in windows. This section proves that final arc data give primitive arc data, when the base, the numbers and the lattices satisfy the final conditions below. The polynomials are explicit products over two sets of integers built from the windows, and their value is computed from the valuation of $u^m - 1$. The result is used in [the final form of Theorem E](/entry/theorem-e-final-form/).

We keep the notation of the previous section: a Frobenius base $B$ over $\mathcal{O}$ with $\ell$, $q = X + \ell$, $p_s = \varphi^s(q)$, cuts $\mathcal{C}$ with lengths $\ell_c$, the numbers $t$, $M$, $A$, $E$ and the primitive conditions. From the section on level steps we keep the final arc data at a cut $c$: level models with filtrations $\mathrm{Fil}_k(s)$, bases $e_k$ of $N_{c'}(V_k)$ with $c' = c - \ell_c$, bases $\lambda_k$ of the spaces $D_k$, submodules $U_k(s) \subseteq \mathcal{O}^{r_k}$, the window $W(s)$ of a step, and a level map with linear part $P_0 \colon \mathcal{O}^{r_1} \to \mathcal{O}^{r_2}$. The step $s$ of the arc at $c$ is the letter $c - s$, with kind $k_s$ and size $b_s$.

**Definition 8.13.1 (Final conditions).** Let $\mathcal{O}$ be a discrete valuation ring with uniformizer $\varpi$ and fraction field $L$, let $e \in \mathbb{N}$ and $u, x \in \mathcal{O}^\times$. Let each letter $i$ have a kind and a size $b_i$, and let $j, g, G_0, S, \eta, t, \sigma, r, \kappa, \ell_{\max} \in \mathbb{N}$. Put $h_J(i) = G_0$, $b_i + S$ or $\eta$ for $i$ thin, up or down, and let the *height* of the step $s$ of the arc at $c$ be $H(c, s) = g + h_J(c - s)$.

1. (*Base*) The base is *final* if it is primitive for $\varpi$ and $e$, $u = 1 + \ell x$, and $L$ is the fraction field of $\mathcal{O}$.
2. (*Numbers*) The numbers are *final* if $G_0, S, \eta \le g \le t$; $g < b_i$ and $b_i + S \le t$ at each letter $i$ that is not thin; $1 \le j \le \ell_c \le \ell_{\max}$ and the letters $c + k$ with $1 \le k \le j$ are thin, for each cut $c$; the inequality of primitive numbers holds; for each cut $c$ the kinds and sizes of its arc form a *text word* for $A$; and $\nu_{\ell_c - 1}(J_c) \le \kappa$ and $\nu_{\ell_c - 1}(J'_c) \le \kappa$ for each cut $c$, with the sets and numbers of the next definition.
3. (*Lattice*) A lattice $V$ is *final* if it is primitive for $\mathcal{C}$, $j$, $G_0$, $t$, the elements $X$ and $p_s$ for all $s$ act bijectively on $V$, and at each letter $i$ the Frobenius is cobounded with $h_J(i)$: $q^{h_J(i)} v \in \mathcal{O}[[X]] \cdot \varphi_i(N_{i-1})$ for all $v \in N_i$.
4. (*Cuts*) A map $h \colon V_1 \to V_2$ satisfies the *$W'$-condition* with $r$ if for each cut $c$ and each $x \in N_c(V_2)$ there is $y \in N_c(V_1)$ with $h(y) = \ell^r x$.

The kinds $k_s$ and sizes $b_s$ of the steps $s < \ell_c$ form a *text word* for $a_0$ if at most two steps are not thin, and for all $s_0 < s_1 < \ell_c$: if $s_1$ is down and $s_0$ is up, then $b_{s_0} < \ell b_{s_1}$; if $s_1$ is up and $s_0$ is down, then $2 b_{s_0} \le \ell b_{s_1}$ and $2 a_0 < b_{s_1}$. This is the word condition of Theorem E in lifting form, with the bound on thick letters.

**Definition 8.13.2 (Windows and killing polynomials).** For a step of kind $k$ and size $b$ put
$$\begin{aligned} W_2 &= \begin{cases} [-g, -1] & k \text{ thin}, \\ [-b-g, -b-1] \cup [-g, -1] & k \text{ up}, \\ [-g, -1] \cup [b-g, b-1] & k \text{ down}, \end{cases} \\ W_4 &= \begin{cases} [-G_0-g, G_0-1] & k \text{ thin}, \\ [-b-S-g, -b-1] \cup [-\eta-g, \eta-1] & k \text{ up}, \\ [b-g, b+S-1] \cup [-\eta-g, \eta-1] & k \text{ down}, \end{cases} \end{aligned}$$
as sets of integers. For a cut $c$ let $J_c$ and $J'_c$ be the unions of the sets $W_2$ and $W_4$ of the steps $s < \ell_c$. For a finite set $J \subseteq \mathbb{Z}$ and $E \in \mathbb{N}$ put
$$\begin{aligned} P_{E,J}(T) &= \prod_{i \in J,\, i \ne 0} \bigl(T^{\ell^E} - u^{i \ell^E}\bigr) \cdot \sum_{k < \ell^E} T^k, \\ \nu_E(J) &= E + \sum_{i \in J,\, i \ne 0} \bigl(1 + E + v_\ell(i)\bigr). \end{aligned}$$
We call $P_{E,J}$ the *killing polynomial* of $J$.

The set $W_4$ of a step contains $-v - z$ for every jump $v$ in the window $W(s)$ of the step and every $1 \le z \le g$. For example, at an up step a jump $v \in [b, b+S]$ gives $-v - z \in [-b-S-g, -b-1]$, and a jump $v \in [-\eta, \eta]$ gives $-v - z \in [-\eta-g, \eta-1]$. The set $W_2$ is the set that the level condition 4 asks the killing polynomial to cover at the step.

**Lemma 8.13.3 (Value of the killing polynomials).** Let $\mathcal{O}$ be a local ring, $\ell$ a prime with $\ell \ge 3$ that is not a unit in $\mathcal{O}$, and $u = 1 + \ell x$ with $x \in \mathcal{O}^\times$. Then for each integer $m \ne 0$ there is a unit $\varepsilon$ with
$$1 - u^m = \varepsilon\, \ell^{1 + v_\ell(m)} .$$
For finite sets $J, J' \subseteq \mathbb{Z}$ and $E, \kappa \in \mathbb{N}$, if $\nu_E(J) + \nu_E(J') \le 2\kappa$, then $P_{E,J}$ and $P_{E,J'}$ have value $\kappa$.

Lean: `Formalism.ExponentWindows.E.factorial_valuation_holds` (also `Formalism.ExponentWindows.E.polynomial_evaluation_valuation`, `Formalism.ExponentWindows.E.polynomial_valuation_holds`)

*Proof.* Let $m > 0$ and write $m = \ell^a m'$ with $\ell \nmid m'$. Since $\ell$ lies in the maximal ideal and $m'$ is prime to $\ell$, $m'$ is a unit of $\mathcal{O}$. If $w = 1 + \ell^k y$ with $k \ge 1$ and $y$ a unit, then $w^{m'} - 1 = \ell^k y (m' + \ell^k z)$ for some $z$, and $m' + \ell^k z$ is a unit. Also
$$w^\ell - 1 = \ell^{k+1} y + \binom{\ell}{2} \ell^{2k} y^2 + \dots + \ell^{k\ell} y^\ell = \ell^{k+1} y\, (1 + \ell z')$$
for some $z'$, since $\ell$ divides $\binom{\ell}{i}$ for $0 < i < \ell$ and $k \ell \ge k + 2$ for $\ell \ge 3$. By induction on $a$, $u^{\ell^a} = 1 + \ell^{a+1} y_a$ with $y_a$ a unit, and then $u^m - 1 = \ell^{a+1} \varepsilon'$ with a unit $\varepsilon'$. For $m < 0$ use $1 - u^m = -u^m (1 - u^{-m})$. Now $P_{E,J}(1) = \ell^E \prod_{i} (1 - u^{i \ell^E})$, and $v_\ell(i \ell^E) = v_\ell(i) + E$, so $P_{E,J}(1)$ is a unit times $\ell^{\nu_E(J)}$. The product $P_{E,J}(1) P_{E,J'}(1)$ is then a unit times $\ell^k$ with $k = \nu_E(J) + \nu_E(J') \le 2\kappa$. $\square$

**Lemma 8.13.4 (Lift of constant coordinates).** Let $h \colon V_1 \to V_2$ be a map of lattices, $c'$ a letter, $e_1$ a family that spans $N_{c'}(V_1)$, and $e_2$ a basis of $N_{c'}(V_2)$ over $\mathcal{O}[[X]]$. Let $P_0 \colon \mathcal{O}^{r_1} \to \mathcal{O}^{r_2}$ be $\mathcal{O}$-linear with matrix $(P_{lk})$, and assume
$$h(e_{1,k}) - \sum_l P_{lk}\, e_{2,l} \in X N_{c'}(V_2)$$
for each $k$. If for each $x \in N_{c'}(V_2)$ there is $y \in N_{c'}(V_1)$ with $h(y) = \ell^r x$, then $P_0$ lifts with $r$: for each $v \in \mathcal{O}^{r_2}$ there is $v_1 \in \mathcal{O}^{r_1}$ with $P_0 v_1 = \ell^r v$.

Lean: `Formalism.ExponentWindows.E.JumpSetWindowBounds.lLift_of`

*Proof.* Let $v \in \mathcal{O}^{r_2}$ and $x = \sum_l v_l e_{2,l} \in N_{c'}(V_2)$. Take $y \in N_{c'}(V_1)$ with $h(y) = \ell^r x$, and write $y = \sum_k a_k e_{1,k}$ with $a_k \in \mathcal{O}[[X]]$. Let $v_1 \in \mathcal{O}^{r_1}$ be the vector of constant terms $a_k(0)$, so that $a_k - v_{1,k} = X a'_k$. Then
$$a_k h(e_{1,k}) - v_{1,k} \sum_l P_{lk} e_{2,l} = a_k \Bigl( h(e_{1,k}) - \sum_l P_{lk} e_{2,l} \Bigr) + X a'_k \sum_l P_{lk} e_{2,l}$$
lies in $X N_{c'}(V_2)$. Summing over $k$, $\ell^r x - \sum_l (P_0 v_1)_l e_{2,l} = X w$ with $w \in N_{c'}(V_2)$. Write $w = \sum_l b_l e_{2,l}$. Then
$$\sum_l \bigl( \ell^r v_l - (P_0 v_1)_l - X b_l \bigr) e_{2,l} = 0 ,$$
so each coefficient is $0$ since $e_2$ is a basis. The constant term of the coefficient of $e_{2,l}$ gives $\ell^r v_l = (P_0 v_1)_l$. $\square$

**Lemma 8.13.5 (Divisible vectors lift).** Let $h \colon V_1 \to V_2$ be a map of lattices, $c$ a letter, and $\Theta_g = \prod_{s < \ell} p_s^g$. If $\Theta_g$ acts bijectively on $V_1$ and on $V_2$, and for each $x \in N_c(V_2)$ there is $y \in N_c(V_1)$ with $h(y) = \ell^r x$, then $h$ lifts divisible vectors with $r$ at $c$.

Lean: `Formalism.ExponentWindows.E.partner_fourth_fourth_form`

*Proof.* Let $\Theta_g x \in N_c(V_2)$. Take $y \in N_c(V_1)$ with $h(y) = \ell^r \Theta_g x$, and let $x_1 \in V_1$ be the element with $\Theta_g x_1 = y$. Then $x_1 \in (N_c(V_1) : \Theta_g)$, and $\Theta_g h(x_1) = h(y) = \Theta_g\, \ell^r x$. Since $\Theta_g$ is injective on $V_2$, $h(x_1) = \ell^r x$. $\square$

**Proposition 8.13.6 (Final arc data give primitive arc data).** Assume the final base for $\varpi$, $e$, $u$, $x$, final numbers, final lattices $V_1$ and $V_2$, and the $W'$-condition with $r$ for $h \colon V_1 \to V_2$. Let $c$ be a cut, and assume final arc data at $c$ for the heights $H(c, \cdot)$, with $M$, $g$, $G_0$, $S$, $\eta$ and the kinds and sizes of the arc. Then primitive arc data exist at $c$ for $H(c, \cdot)$, $g$, $\sigma$, $r$, $A$ and $\kappa$, with the polynomials $P = P_{\ell_c - 1, J_c}$ and $P' = P_{\ell_c - 1, J'_c}$.

Lean: `Formalism.ExponentWindows.E.JumpSetWindowBounds.primArc`

*Proof.* We take the level data, the level map and the submodules $U_k(s)$ of the final arc data, and check the nine conditions of primitive arc data.

*Numbers.* Since the base is primitive, $\ell \ge 3$, $\varpi$ divides $\ell$, and $\ell$ is not a unit. By the first lemma, $1 - u^m = \varepsilon \ell^{1 + v_\ell(m)}$ for $m \ne 0$. Since $\mathcal{O} \to L$ is injective, $\ell \ne 0$ and $\varpi \ne 0$ in $L$. By the definition of $M$, $t + 2g < (\ell - 1) M$. If the step $s$ is not thin, then $b_s + S \le t$, and $s < \ell_c - j$: otherwise $c - s = c' + k$ with $1 \le k \le j$, and this letter is thin by the condition at the previous cut $c'$.

*Partners.* With these numbers, the bijectivity of $X$ and of the $p_s$, the first condition of a primitive lattice, the cobounded Frobenius with $h_J$, and the conditions on the level models, the partner theorem of the level models applies to $V_1$ and to $V_2$. It gives conditions 1 and 3 of primitive arc data, and the level conditions 7 and 8 with $\sigma$ and 9 and 10 with $g$.

*The level conditions.* Level condition 1 is part of the final arc data. For level condition 2 on $E_2$, the level maps fix the elements of finite order, and $u^m \ne 1$ in $L$ for $m \ne 0$ by the first lemma, since $\ell \ne 0$ in $L$. Level condition 3 follows from the filtrations, $G_0, S, \eta \le g < b_s$ and the jumps in $W(s)$, by a rounding of filtrations. Level condition 4 on $E_2$ holds with $P_{\ell_c - 1, J_c}$, since $J_c$ contains the set $W_2$ of each step. Level condition 5 on $E_1$ holds with $P_{\ell_c - 1, J'_c}$: the level maps commute with $\varphi$ and $\Gamma$, the filtrations decrease, and $J'_c$ contains $-v - z$ for every jump $v$ and $1 \le z \le g$, as remarked above. Level condition 6 holds for every level datum with a level model. Level condition 11 follows from the bases $\lambda_k$, the description of $U_k(s)$ and the fact that $L$ is the fraction field.

*The map.* The level map preserves errors by the final arc data. Since $\Theta_g$ is a product of the $p_s$, it acts bijectively on $V_1$ and $V_2$, and the third lemma with the $W'$-condition at $c$ shows that $h$ lifts divisible vectors with $r$. The second lemma, with the bases $e_k$ of $N_{c'}(V_k)$, the fourth condition of final arc data and the $W'$-condition at the cut $c'$, shows that $P_0$ lifts with $r$. The map $P_0$ sends $U_1(s)$ into $U_2(s)$ at the up steps by the final arc data. So conditions 4 and 5 of primitive arc data hold.

*Value, saturation and word.* The bounds $\nu(J_c) \le \kappa$ and $\nu(J'_c) \le \kappa$ and the first lemma give condition 6. For condition 7, $v \in U_k(s)$ if and only if $\sum_m v_m \lambda_{k,m}$ lies in an $L$-subspace; if $\varpi v \in U_k(s)$, then $\varpi \sum_m v_m \lambda_{k,m}$ lies in it, and $\varpi \ne 0$ in $L$. At an up step $H(c, s) = g + b_s + S \ge b_s$, and $g < b_s$ at steps that are not thin, which is condition 8. Last, a text word for $A$ is a primitive word for $A$. If no step is down, this is the first case. Otherwise let $s_d$ be a down step; all steps other than $s_d$ and one more step $s_o$ are thin. If $s_o$ is thin or equal to $s_d$, there is exactly one down step. If $s_o$ is down, there are two down steps. If $s_o$ is up and $s_o < s_d$, the first clause of the text word gives a down after an up with $b_{s_o} < \ell b_{s_d}$. If $s_o$ is up and $s_o > s_d$, the second clause gives $2 b_{s_d} \le \ell b_{s_o}$ and $2A < b_{s_o}$. This is condition 9. $\square$

**Remark 8.13.7 (Formalization).** The conditions are `FinalBase`, `FinalNum`, `FinalLat`, `WPrimeCuts`, `FinalLevels`, `ArcData`, `FinalArcProps` and `FinalArc` ([FinalArcProps.lean](lean:Formalism/DistinguishedUnitIdeals/FinalArcProps.lean#L53)), the text word is `TextWord` (line 47), and $W_2$, $W_4$, $J_c$, $J'_c$ are `win2`, `win4`, `jumpWindows`, `wideWindows` (lines 26 to 41). The killing polynomial is `PPoly` (ExistsConstOfInvariantMod.lean line 83) and $\nu_E$ is `kapExp` (PhiFreeOfBasis.lean line 23). The proof of `primArc` is in [ThmEFinal.lean](lean:Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/ThmEFinal.lean#L417), with the helpers `primWord`, `thick_lt`, `ppval`, `partModel`, `rd`, `factV`, `sat`, `bridge` and `inv_Th` of the same file. The partner theorem is `partners_model_holds`, and the level conditions come from `graded_third_clause_holds`, `reduction_degree_holds` with `filtration_rounding`, `constant_term_second_form`, `constant_term_fourth_form`, `descent_fixed_points_holds` and `lattice_transfer_holds`. Condition 6 of level data is trivial here: the statement `DcFixOf` takes the level model as `_R` and does not use it (ExistsConstOfInvariantMod.lean line 317). Not unfolded here: the level models, `K1b`, `HasU`, `UnitsAt`, `Compl`, `LocReg`, `FlDef`, `LocLIs` and `IsFilt`. The field `ind` of `FinalLevels` (independence of $e_k$) is used only for $V_2$, and `hP.lev₁.ind` is not used.
