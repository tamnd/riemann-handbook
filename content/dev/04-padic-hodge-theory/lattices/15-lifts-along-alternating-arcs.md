---
title: Lifts along alternating arcs
decls:
  - Formalism.MainNotions.N.Ln17.sum_alt
  - Formalism.MainNotions.N.Ln17.sumAltW
  - Formalism.MainNotions.N.FrobeniusPowerSeries.arc_proposition_alternative
  - Formalism.MainNotions.N.FrobeniusPowerSeries.arc_length_three_theorem
  - Formalism.MainNotions.N.FrobeniusPowerSeries.arc_length_three_case_d
  - Formalism.MainNotions.N.FrobeniusPowerSeries.arc_length_three_exists_liftsAt_scalar_mul
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lifts along alternating arcs

Part (a) of [the local Theorem B](/entry/thm-b-at/) needs an exponent $e$ and a small set $Z$ of finite cocycles of $T_2$ such that $p^e$ moves every finite cocycle of $T_2$ into $\operatorname{Im}_F + \operatorname{span} Z$. This section gives them when the signs alternate. At each cut of the arcs, a Wach vector of $T_2$ is lifted to $T_1$ with a bounded exponent, by a case split on the length of the arc, which is at most $3$.

We keep the notation of the first sections: the Wach datum with $\Lambda$, $E$, $\varphi$, $\pi_0$, $q = \pi_0 + p$, $\Delta$, the modules $N(T) \subseteq D(T)$ and $N_i(T)$, the setting of Theorem B with $b, w, S, \eta, m$, $\mathrm{up}$ and $\mathrm{size}$, and $p = \ell$. A letter $i$ is thick if $b \le \mathrm{size}_i \le b + \eta$. Put $\lambda_g = \log_\ell(2 h_B)$ and
$$\Sigma = \frac{h_B}{\ell^2} + \frac{w + S + \eta}{\ell} + \lambda_g + 1 .$$
Let $C_b \ge 2$, and let $\beta \in \{0, 1\}$ be the indicator of the band condition with the constant $C_b$. Since $\lambda_g \ge 0$, we have $\lambda_g + 1 \le \Sigma$ and $\Sigma \ge 1$.

**Definition 8.15.1 (Alternating signs).** The data have *alternating signs* if for every letter $i$ we have $\mathrm{up}_{i+1} \ne \mathrm{up}_i$, and the three letters $i, i+1, i+2$ are not all thick.

**Definition 8.15.2 (Arc datum of the setting).** The *arc datum of the setting* $A_B$ is the [arc datum](/entry/class-split-along-arcs/) with $G_0 = w + S$, the numbers $S$ and $\eta$, $h = h_B$ and $j = 1$, in which the letter $i$ is up of size $\mathrm{size}_i$ if $\mathrm{up}_i$ holds and down of size $\mathrm{size}_i$ otherwise. The cuts are the letters $c$ such that $c + 1$ is not thick, and the length $\ell_c$ is the least $d \ge 1$ such that $c - d + 1$ is not thick.

So the arc of a cut $c$ is $c, c - 1, \dots, c - \ell_c + 1$, the letter $c - \ell_c + 1$ is the only letter of the arc that is not thick, and no letter of $A_B$ is thin. Alternating signs give $\ell_c \le 3$, and $\ell_c = 1$ if no letter is thick. Write $c' = c - \ell_c$, and let $\Lambda_c$ and the arc condition be as in the section on arcs.

**Definition 8.15.3 (Lift at a cut).** Let $c$ be a cut, let $b_1, \dots, b_d$ be a horizontal basis of $T_2$ at $c'$ with its solutions, let $k_0 \le d$ and $f \in E$.

1. The index $k_0$ is *admissible* if for every step $s < \ell_c$ at which $c - s$ is up of size $b_s$, the image of $\varphi^{\ell_c}(b_{k_0})$ in $D_{\mathrm{cris}}(V_2)$ lies in $\varphi^s\bigl(\mathrm{Fil}^{b_s}\bigr)$ of the part at the letter $c - s$.
2. The element $f$ is an *admissible coordinate* if $f$ has fraction $1/\prod_{s} \varphi^s(q)^{b_s}$ at $c$, with the product over the up steps of the arc, and if for every down step $s$ of size $b_s$ there are $\kappa$ and $x \in \mathcal{O}$ such that $p^\kappa f - e_c x$ has fraction $\varphi^s(q)^{b_s + S} / \prod_{s'} \varphi^{s'}(q)^{b_{s'}}$ at $c$.
3. The map $F$ *lifts at* $c$ *with exponent* $e$ on $(b, k_0, f)$ if there are $w_1 \in D(T_1)$ and $z \in D(T_2)$ such that $w_1$ is a Wach vector of $T_1$ at $c$, a product of elements $\varphi^s(q)$ moves $w_1$ into $N_c(T_1)$, $F(w_1)$ satisfies the arc condition at $c$, $z \in \pi_0 N_c(T_2)$, and $F(w_1) - z$ has, in the basis $b$, the coordinate $p^e f$ at $b_{k_0}$ and $0$ at the other basis vectors, up to an error in $\pi_0 \Lambda_c^2 P_{c', \ell_c}(T_2)$.

A lift with exponent $e$ is a lift with every larger exponent. Lifts on $f$ and $f'$ with one exponent add to a lift on $f + f'$, a lift on $f$ gives one on $t f$ for $t \in \mathcal{O}$, and a lift on $p^k f$ with exponent $e$ is a lift on $f$ with exponent $e + k$.

The lemmas below are stated in the *arc setting* at a cut $c$: we are in the setting of Theorem B with $\ell \ge 11$, we assume the inputs on Wach modules listed in the remark at the end, $A_B$ is good, $T_1$ and $T_2$ are in its window, $\sigma \le 3\Sigma$ for the number $\sigma$ of $A_B$, and there is $r \le 3 \Sigma$ such that at every cut $c''$, $p^r N_{c''}(T_2)^\Delta \subseteq F\bigl(N_{c''}(T_1)\bigr)$. We fix $b$ and an admissible $k_0$. For a letter $i$ let $a_i = \lceil s_i / (\ell - 1) \rceil$, where $s_i$ is the least $k$ such that $\varpi^k N_i(T_2) \subseteq F(N_i(T_1))$.

**Proposition 8.15.4 (Scalar lift at a short middle step).** In the arc setting, assume alternating signs, $40 \Sigma \le b/4$, $\ell_c = 3$, $\mathrm{up}_{c-2}$ false, and
$$\mathrm{size}_{c-1} < \ell \bigl(\mathrm{size}_{c-2} + S + \eta\bigr).$$
Let $f_2 \in E$ have fraction $\varphi^2(q)^{\mathrm{size}_{c-2} + S} / \varphi(q)^{\mathrm{size}_{c-1}}$ at $c$, and assume that there are $\kappa_0$ and $X_0 \in \mathcal{O}$ such that $p^{\kappa_0} f_2 - e_c X_0$ has fraction $q^{\mathrm{size}_c + S} / \varphi(q)^{\mathrm{size}_{c-1}}$ at $c$. Then there are $e \le 6 \Sigma$ and $t_3 \in \mathcal{O}$ with $v(t_3) \le 14 \Sigma$ such that $F$ lifts at $c$ with exponent $e$ on $t_3 f_2$.

Lean: `Formalism.MainNotions.N.FrobeniusPowerSeries.arc_length_three_exists_liftsAt_scalar_mul`

*Proof.* There are five steps, each a lemma proved from the inputs.

1. *The constant term.* The valuation of $X_0$ is at least
$$\mathrm{size}_{c-2} + S - \mathrm{size}_{c-1} + \frac{\mathrm{size}_c + S}{\ell} - \frac{\mathrm{size}_c + S}{\ell^2} - 2 - \lambda_g + \kappa_0 .$$
2. *A vector near the basis.* There are $\lambda \in P_{c', 2}(T_2)$, a number $\kappa$ and a truncated horizontal sum $H$ for $b_{k_0}$ such that $\gamma\lambda - \lambda$ and a power of $p$ times $p^\kappa \lambda - p^\sigma \varphi^2(H)$ are small at the level of $\varphi(J)$, for the killing element $J$ of the datum.
3. *The first level.* There are $n_1 \in N_{c-1}(T_1)$ and $E_0 \le 8 \Sigma$ with $F(n_1) = p^{E_0} s \lambda$, where $q^{\mathrm{size}_{c-1}} s = \varphi(q)^{\mathrm{size}_{c-2} + S}$.
4. *The first lift.* There are a Wach vector $y_1$ of $T_1$ at $c$ with $q^{\mathrm{size}_c + S} y_1 \in N_c(T_1)$ and $\sigma_1 \le (\mathrm{size}_c + S)/(\ell - 1) + 1$ such that $p^{\mathrm{size}_{c-1} + \kappa} F(y_1)$ is congruent to $p^{\sigma_1 + E_0 + \sigma + \mathrm{size}_{c-2} + S} \varphi^3(H)$ modulo $q^{\mathrm{size}_c + S} P_{c-1, 1}(T_2)$, after a power of $p$ and a product of elements $\varphi^k(q)$ with $k \ge 1$.
5. *The combination.* The relations of the steps 1 to 4 give $e \le 6\Sigma$, $t_3$ with $v(t_3) \le 14\Sigma$, and the lift on $t_3 f_2$. $\square$

**Theorem 8.15.5 (Arcs of length three with a short middle step).** In the arc setting, assume alternating signs, $40 \Sigma \le b/4$, $\ell_c = 3$, $\mathrm{up}_{c-2}$ false and $\mathrm{size}_{c-1} < \ell(\mathrm{size}_{c-2} + S + \eta)$. Then for every admissible coordinate $f$ there is $e_1 \le 22 \Sigma + 1 + \eta \beta$ such that $F$ lifts at $c$ with exponent $e_1$ on $f$.

Lean: `Formalism.MainNotions.N.FrobeniusPowerSeries.arc_length_three_case_d`

*Proof.* A descent lemma gives $t_2, X_2 \in \mathcal{O}$ and $f_2 \in E$ with
$$v(t_2) \le (\eta + 2 + \lambda_g)\, \beta, \qquad t_2 f = e_c X_2 + f_2,$$
such that $f_2$ satisfies the two fraction conditions of the last proposition. The proposition gives $e \le 6\Sigma$ and $t_3$ with $v(t_3) \le 14\Sigma$ and a lift on $t_3 f_2$ with exponent $e$. By a lemma on constant terms, $F$ lifts with exponent $r + \sigma$ on $e_c t_3 X_2$. Put $e_2 = \max(e, r + \sigma)$. Both lifts hold with exponent $e_2$, so their sum is a lift with exponent $e_2$ on
$$e_c t_3 X_2 + t_3 f_2 = t_3 t_2 f .$$
Let $N$ be the least integer with $v(t_3) + v(t_2) \le N$. Then $v(p^N / (t_3 t_2)) \ge 0$, so $p^N = t' t_3 t_2$ with $t' \in \mathcal{O}$. Multiplying by $t'$ gives a lift on $p^N f$ with exponent $e_2$, hence a lift on $f$ with exponent $e_1 = e_2 + N$.

It remains to bound $e_1$. Since $r \le 3\Sigma$ and $\sigma \le 3\Sigma$, we have $e_2 \le 6\Sigma$. Since $\beta \le 1$ and $2 + \lambda_g \le \Sigma + 1$,
$$N < v(t_3) + v(t_2) + 1 \le 14 \Sigma + \eta\beta + \Sigma + 2 .$$
So $e_1 < 21 \Sigma + \eta \beta + 2 \le 22 \Sigma + 1 + \eta\beta$, since $\Sigma \ge 1$. $\square$

**Theorem 8.15.6 (Arcs of length three, last step down).** In the arc setting, assume alternating signs, $40 \Sigma \le b/4$, $\ell_c = 3$ and $\mathrm{up}_{c-2}$ false. Then for every admissible coordinate $f$ there is $e_1 \le 22\Sigma + 1 + \eta\beta$ such that $F$ lifts at $c$ with exponent $e_1$ on $f$.

Lean: `Formalism.MainNotions.N.FrobeniusPowerSeries.arc_length_three_theorem`

*Proof.* If $\mathrm{size}_{c-1} < \ell(\mathrm{size}_{c-2} + S + \eta)$, apply the last theorem. Otherwise a lemma for a long middle step gives a lift with $e_1 \le 13 \Sigma + 1$, which is at most $22 \Sigma + 1 + \eta \beta$. $\square$

**Theorem 8.15.7 (Lift at a cut).** In the arc setting, assume alternating signs, and assume $\ell_c \le 2$ or $40 \Sigma \le b/4$. Then for every admissible coordinate $f$ there is $e_1 \le 40\Sigma + \eta \beta$ such that $F$ lifts at $c$ with exponent $e_1$ on $f$.

Lean: `Formalism.MainNotions.N.FrobeniusPowerSeries.arc_proposition_alternative`

*Proof.* The arc datum is good, so $\ell_c \ge 1$, and the signs alternate, so $\ell_c \le 3$. Each case gives a bound of the form $k\Sigma + 1 + \eta\beta$ or $k \Sigma + 1$ with $k \le 34$, and $k \Sigma + 1 \le 40 \Sigma$ since $\Sigma \ge 1$.

If $\ell_c = 1$, the lemma for a single sign gives $6\Sigma + 1$. If $\ell_c = 2$, alternating signs give $\mathrm{up}_{c-1} \ne \mathrm{up}_c$. Four lemmas, split by $\mathrm{up}_c$ and by a comparison of $\mathrm{size}_c$ with $\ell(\mathrm{size}_{c-1} + S + \eta) + \eta$ or of $\mathrm{size}_{c-1}$ with $a_{c-1} + \eta + 1$, give $12\Sigma + 1$, $9\Sigma + 1 + \eta\beta$, $9\Sigma + 1$ and $15\Sigma + 1 + \eta\beta$. If $\ell_c = 3$, then $40\Sigma \le b/4$ by hypothesis. If $\mathrm{up}_{c-2}$ fails, the last theorem gives $22\Sigma + 1 + \eta\beta$. If it holds, two lemmas, split by $\mathrm{size}_{c-2} < a_{c-2} + \eta + 2\sigma + 2$, give $34\Sigma + 1 + \eta\beta$ and $18 \Sigma + 1$. $\square$

**Theorem 8.15.8 (Sum along alternating arcs for a Wach datum).** Let the Wach datum satisfy the core inputs of the local theory. Let the data be in the setting of Theorem B with $\ell \ge 11$, $20w \le b$, $20\eta \le b$, $20S \le b$ and a letter that is not thick. Assume alternating signs, $C_b \ge 2$, and either that no letter is thick or that $40\Sigma \le b/4$. Then there are $e \in \mathbb{N}$ and a finite set $Z \subseteq Z^1_f(T_2)$ with
$$e \le 55 \Sigma + 13 S + \eta \beta, \qquad |Z| \le 4nm,$$
such that $p^e c \in \operatorname{Im}_F + \operatorname{span}_{\mathcal{O}} Z$ for every $c \in Z^1_f(T_2)$.

Lean: `Formalism.MainNotions.N.Ln17.sumAltW`

*Proof.* The setup lemma gives the arc setting, $\sum_{c} \ell_c = n$, $\ell_c \le 3$, and the window and killing conditions for the extensions of $\mathbf{1}$ by $T_2$ defined by cocycles. Put $E_1 = \lfloor 40\Sigma + \eta\beta \rfloor \ge \sigma$. If no letter is thick, every arc has length $1$. So the last theorem and monotonicity give a lift with exponent $E_1$ on every admissible $(b, k_0, f)$ at every cut.

At each cut $c$, the length bound for arcs, with the universal part, gives a finite set $Z_c \subseteq H^1_f(T_2)$ with $|Z_c| \le m \rho_c (\ell_c + 1)$, where $\rho_c$ is the number of thick kinds on the arc. It also gives, for every Wach vector $w$ at $c$ with the arc condition and the pole condition and every $\rho$-class $x$ of $w$,
$$p^{\sigma + \kappa_c + E_1} x \in F_* H^1_f(T_1) + \operatorname{span} Z_c, \qquad \kappa_c = \ell_c + \sum_{i \in J_c \setminus \{0\}} \bigl( \ell_c + 1 + v_\ell(i) \bigr).$$
Here $J_c$ is the union over the steps $s < \ell_c$ of $[-b_s - S, -b_s)$ at up steps and $[b_s, b_s + S)$ at down steps. A counting lemma for alternating arcs of length at most $3$ gives $\kappa_c \le 13 S + 3\lambda_g + 3$. Let $\kappa = \max_c \kappa_c$ and $E = \sigma + \kappa + E_1$.

The [splitting along arcs](/entry/split-case-a-final/) writes $p^{r + 2\sigma}$ times a finite class of $T_2$ as a signed sum of the classes $x_{c}$ of Wach vectors at the cuts. So $p^{r + 2\sigma + E}$ moves every class of $H^1_f(T_2)$ into $F_* H^1_f(T_1) + \operatorname{span} \bigcup_c Z_c$. Finally, a lemma on representatives replaces the classes by finite cocycles: there is $Z \subseteq Z^1_f(T_2)$ with $|Z| \le |\bigcup_c Z_c|$ and with the exponent $e = r + 2\sigma + E$.

The numbers: $e = r + 3\sigma + \kappa + E_1 \le 3\Sigma + 9\Sigma + 13S + 3\lambda_g + 3 + 40\Sigma + \eta\beta$, and $3\lambda_g + 3 \le 3\Sigma$, so $e \le 55\Sigma + 13 S + \eta\beta$. Since $\rho_c \le \ell_c \le 3$, we have $\rho_c(\ell_c + 1) \le 4 \ell_c$, so $|Z| \le \sum_c 4m\ell_c = 4nm$. $\square$

**Theorem 8.15.9 (Sum along alternating arcs).** Assume the admitted bounds of the local theory and the inputs on the jumps. Let $\ell$ be a prime, $(K, L)$ good at level $1$ in case A, and take the Wach datum at $(\ell, K, L)$. Let the data be as in the last theorem, with alternating signs, $C_b \ge 2$, and no thick letter or $40\Sigma \le b/4$. Then the conclusion of the last theorem holds with $p = \ell$.

Lean: `Formalism.MainNotions.N.Ln17.sum_alt`

*Proof.* The prime of the period datum at $K$ is $\ell$, and the setting gives $\ell \ge 11$. The ring of $L$ is complete for its maximal ideal. The admitted bounds and the inputs on the jumps give the core inputs at $(\ell, K, L)$, and the last theorem applies. $\square$

**Remark 8.15.10 (Formalization).** The setting is `HypB` and alternating signs are `Alt`, with $\Sigma$ = `Sg`, $\beta$ = `bandI` and the arc datum `arcOf` ([AdmBoundsBOfAdm.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/AdmBoundsBOfAdm.lean#L22)). The lift at a cut is `LiftsAt`, with `InLpp` and `InFF` ([ArcGamLiftCore.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/ArcGamLiftCore.lean#L31)). The core inputs are the 35 fields of `CoresW` (ExistsGaloisExtendingAlgHom.lean line 30), made by `coresAt` ([LogbHBNonneg.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/LogbHBNonneg.lean#L334)) from `AdmBoundsB` and `UsedJ`; each arc lemma takes about thirty of them as arguments. The five steps of the scalar lift are `arc_length_three_le_valuation_constant_term`, `arc_length_three_exists_lambda_near_horizontal`, `arc_length_three_first_level`, `arc_length_three_first_lift` and `arc_length_three_final_bound`. In `arcOf` no letter is thin, so $\rho_c = \ell_c$. In `arc_proposition_alternative` the term $+1$ of the case bounds is absorbed by $\Sigma \ge 1$, which is proved again inside that proof (ArcPropositionAlternative.lean line 160) although `one_le_Sg` (LogbHBNonneg.lean line 77) states it. The proof of `arc_length_three_case_d` ends with one `nlinarith` call over nine facts (ArcLengthThreeCaseD.lean line 110).
