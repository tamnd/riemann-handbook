---
title: Levels of an arc and lifting modulo constants
decls:
  - Formalism.ExponentWindows.E.Full.constLift_of_word
  - Formalism.ExponentWindows.E.word_constants_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Levels of an arc and lifting modulo constants

Along an arc of length $\ell_c$, a vector of coordinates is read at each level $s = 0, 1, \dots, \ell_c - 1$ through the distinguished polynomial $p_s = \varphi^s(q)$. At a thin level the vector must be divisible by a power of $p_s$; at an up or a down level it may differ from such a multiple by a term with constant coefficients in a given $\mathcal{O}$-module. This section defines these level conditions, states how the conditions at all levels together describe a vector up to a constant multiple of $\Lambda = \prod_s p_s^{H_s}$, and proves from it that a map of constant vectors that is onto up to $\ell^r$ lifts the level conditions with the loss $\ell^{2a_0}$. This *lifting modulo constants* is the input at each cut of the arc lift from level data, which proves [the full form of Theorem E](/entry/theorem-e-full-form/) in the next section.

Throughout, $\mathcal{O}$ is a discrete valuation ring with uniformizer $\varpi$. For a submodule $U \subseteq \mathcal{O}^r$ write $U[[X]]$ for the $\mathcal{O}[[X]]$-submodule of $\mathcal{O}[[X]]^r$ spanned by the constant vectors in $U$. The module $U$ is *saturated* if $\varpi v \in U$ implies $v \in U$.

**Definition 8.10.1 (Distinguished family).** An element $p \in \mathcal{O}[[X]]$ is a *unit times a distinguished polynomial of degree* $d$ if $p = u E$ with $u$ a unit of $\mathcal{O}[[X]]$ and $E$ a distinguished polynomial of degree $d$ for the ideal $(\varpi)$: monic, with all other coefficients in $(\varpi)$. Two elements $p, p'$ are *coprime up to $\varpi$* if $a p + a' p' = \varpi^N$ for some $a, a' \in \mathcal{O}[[X]]$ and $N \in \mathbb{N}$. A sequence $p_0, \dots, p_{\ell_c - 1}$ is a *distinguished family* for $\ell$ if each $p_s$ is a unit times a distinguished polynomial of degree $\ell^s$ and any two different $p_s$ are coprime up to $\varpi$.

By the Weierstrass preparation theorem every element of $\mathcal{O}[[X]]$ that is not in $\varpi \mathcal{O}[[X]]$ has this form. In the application $p_s = \varphi^s(X + p)$ with $\varphi(X) = (1+X)^p - 1$ up to a unit, which has degree $p^s$, and two of them generate an ideal that contains a power of $p$.

**Definition 8.10.2 (Level conditions).** Let $p \in \mathcal{O}[[X]]$, $H, b \in \mathbb{N}$, a kind (thin, up or down) and $U \subseteq \mathcal{O}^r$. A vector $y \in \mathcal{O}[[X]]^r$ satisfies the *level condition* if for some $N$ and some $c \in U[[X]]$, $z \in \mathcal{O}[[X]]^r$:
$$\varpi^N y = \begin{cases} p^H z & \text{thin}, \\ p^{H-b} c + p^H z & \text{up}, \\ p^H c + p^{H+b} z & \text{down}. \end{cases}$$
Now fix a distinguished family $(p_s)$, numbers $H_s, b_s$, kinds and submodules $U(s) \subseteq \mathcal{O}^r$ for $s < \ell_c$, and put $\Lambda = \prod_{s < \ell_c} p_s^{H_s}$. Let $\mathrm{N}$ be the set of $y$ that satisfy the level condition at every $s < \ell_c$, and let $\mathrm{I}$ be the set of $y$ such that for every $s < \ell_c$ there are $d \in \mathcal{O}^r$ and $k \in \mathbb{N}$ for which $\varpi^k y - \Lambda d$ satisfies the level condition at $s$.

So $\mathrm{N}$ is the lattice of vectors that are integral at every level, and $\mathrm{I}$ is the set of vectors that are integral at each level after a correction by a constant multiple of $\Lambda$, a correction that may change from level to level. The factor $\varpi^N$ makes both conditions rational: they only see $y \otimes L$.

The *level model setting* holds if $\ell \ge 2$, $(p_s)$ is a distinguished family for $\ell$, the modules $U_1(s) \subseteq \mathcal{O}^{r_1}$ and $U_2(s) \subseteq \mathcal{O}^{r_2}$ are saturated, and $b_s \le H_s$ at each up step.

**Definition 8.10.3 (Arc words).** The kinds of the steps $s < \ell_c$ form an *arc word* of one of the following five types.

1. *No down*: no step is down.
2. *One down*: one step $s_1$ is down and all others are thin.
3. *Down after up*: $s_0 < s_1$, $s_1$ is down, $s_0$ is up of size $b_{s_0} < \ell b_{s_1}$, all others thin.
4. *Two downs*: $s_0 < s_1$ are down, all others thin, and there are $\rho \in \mathbb{N}$ and $f_\rho \in \mathcal{O}[[X]]$ such that $\rho$ is the least $k$ with $\varpi^k \in (p_{s_1}^{b_{s_1}}, p_{s_0}^{b_{s_0}})$, $f_\rho \in (p_{s_1}^{b_{s_1}})$ and $f_\rho \equiv \varpi^\rho \bmod p_{s_0}^{b_{s_0}}$.
5. *Up after down*: $s_0 < s_1$, $s_1$ is up, $s_0$ is down, all others thin; $P$ maps $U_1(s_1)$ onto $\ell^{2a_0} U_2(s_1)$ in the sense that each $v \in U_2(s_1)$ is $P(v_1)$ for some $v_1 \in U_1(s_1)$ with $P(v_1) = \ell^{2a_0} v$; and there are $c \in \mathbb{N}$ and $\alpha, \beta$ with
$$p_{s_1}^{b_{s_1}} = \varpi^c \alpha + p_{s_0}^{b_{s_0}} \beta, \qquad p_{s_1}^{b_{s_1}} \notin (\varpi^{c+1}, p_{s_0}^{b_{s_0}}).$$

The arc words are the patterns that the [word condition](/entry/crystalline-lifting-second-form/) of Theorem E allows on one arc, with at most two steps that are not thin. The level models below describe $\mathrm{I}$ for each word. We do not prove them here.

**Theorem 8.10.4 (Level models).** Assume the level model setting for $U(s) \subseteq \mathcal{O}^r$, and let $y \in \mathcal{O}[[X]]^r$.

1. For a word with no down step, $y \in \mathrm{I}$ if and only if $y \in \mathrm{N}$.
2. For a word with one down step, or with a down step after an up step, $y \in \mathrm{I}$ if and only if $y = \Lambda \lambda + \nu$ with $\lambda \in \mathcal{O}^r$ and $\nu \in \mathrm{N}$.
3. For a word with two downs and its $\rho$, $f_\rho$: $y \in \mathrm{I}$ if and only if $y = \Lambda \lambda + \Lambda f_\rho \lambda' + \nu$ with $\lambda, \lambda' \in \mathcal{O}^r$ and $\nu \in \mathrm{N}$.
4. For a word with an up step $s_1$ after a down step and its $c, \alpha, \beta$: $y \in \mathrm{I}$ if and only if $y = \Lambda \lambda + \alpha \Lambda' \lambda' + \nu$ with $\lambda \in \mathcal{O}^r$, $\lambda' \in U(s_1)$ and $\nu \in \mathrm{N}$, where $\Lambda' = p_{s_1}^{H_{s_1} - b_{s_1}} \prod_{s \ne s_1} p_s^{H_s}$.

Lean: `Formalism.ExponentWindows.levels_mod_const_iff_of_no_down`, `Formalism.ExponentWindows.descent_estimate_down`, `Formalism.ExponentWindows.descent_estimate_down_up`, `Formalism.ExponentWindows.levels_mod_const_iff_of_down_down`, `Formalism.ExponentWindows.descent_estimate_up_down`.

So modulo the integral lattice $\mathrm{N}$, the set $\mathrm{I}$ is spanned by at most two families of constant vectors, multiplied by $\Lambda$ and by one more fixed series.

**Definition 8.10.5 (Lifting modulo constants).** Let $P \colon \mathcal{O}^{r_1} \to \mathcal{O}^{r_2}$ be $\mathcal{O}$-linear, and extend it to $\mathcal{O}[[X]]^{r_1} \to \mathcal{O}[[X]]^{r_2}$ coefficientwise. Let $r, a_0 \in \mathbb{N}$. The map $P$ *lifts with* $r$ if every $v \in \mathcal{O}^{r_2}$ satisfies $P(v_1) = \ell^r v$ for some $v_1$. The map $P$ *lifts modulo constants with* $a_0$ if for every $y \in \mathrm{I}_2$ there are $y_1 \in \mathrm{I}_1$ and $\nu \in \mathrm{N}_2$ with
$$\ell^{2a_0} y = P(y_1) + \ell^{2a_0} \nu.$$
Here $\mathrm{I}_k$, $\mathrm{N}_k$ are the sets above for the modules $U_k(s)$.

**Proposition 8.10.6 (Lifting modulo constants from the word).** Assume the level model setting, that $P$ lifts with $r$, that $r \le 2a_0$, and that the kinds form an arc word. Then $P$ lifts modulo constants with $a_0$.

Lean: `Formalism.ExponentWindows.E.Full.constLift_of_word` (also `Formalism.ExponentWindows.E.CL.lifts_mod_const_of_words`, the five cases).

*Proof.* First, for every $v \in \mathcal{O}^{r_2}$ there is $v_1$ with $P(v_1) = \ell^{2a_0} v$: take $v'$ with $P(v') = \ell^r v$ and $v_1 = \ell^{2a_0 - r} v'$. We go through the five words, with the level models above.

No down step: $y \in \mathrm{I}_2$ lies in $\mathrm{N}_2$, so $y_1 = 0$ and $\nu = y$ work, since $0 \in \mathrm{I}_1$.

One down step, or a down step after an up step: write $y = \Lambda \lambda + \nu$ with $\nu \in \mathrm{N}_2$. Take $\lambda_1$ with $P(\lambda_1) = \ell^{2a_0} \lambda$ and $y_1 = \Lambda \lambda_1$. By the level model for $U_1$, read from right to left with $\nu = 0$, we have $y_1 \in \mathrm{I}_1$. Since $P$ acts on coefficients and $\Lambda$ is a scalar, $P(y_1) = \Lambda \ell^{2a_0} \lambda$, so $\ell^{2a_0} y = P(y_1) + \ell^{2a_0} \nu$.

Two downs: write $y = \Lambda \lambda + \Lambda f_\rho \lambda' + \nu$, lift $\lambda$ and $\lambda'$ to $\lambda_1$ and $\lambda'_1$, and put $y_1 = \Lambda \lambda_1 + \Lambda f_\rho \lambda'_1$, which lies in $\mathrm{I}_1$ by the level model.

Up after down: write $y = \Lambda \lambda + \alpha \Lambda' \lambda' + \nu$ with $\lambda' \in U_2(s_1)$. Lift $\lambda$ as before. The word gives $\lambda'_1 \in U_1(s_1)$ with $P(\lambda'_1) = \ell^{2a_0} \lambda'$. Then $y_1 = \Lambda \lambda_1 + \alpha \Lambda' \lambda'_1$ lies in $\mathrm{I}_1$ by the level model, and the identity follows as before. $\square$

The proposition is the reason for the hypothesis on $U(s_1)$ in the last word: at an up step after a down step the second family of constants lies in $U(s_1)$, and its lift must stay there.

The constants $\rho, f_\rho$ and $c, \alpha, \beta$ of the last two words always exist.

**Lemma 8.10.7 (Word constants).** Let $\ell \ge 2$, let $(p_s)_{s < \ell_c}$ be a distinguished family for $\ell$, let $b_s \in \mathbb{N}$, and let $s_0 < s_1 < \ell_c$. Then:

1. there are $\rho$ and $f_\rho$ as in the word with two downs;
2. if $b_{s_0} \ge 1$, there are $c$, $\alpha$ and $\beta$ as in the word with an up step after a down step.

Lean: `Formalism.ExponentWindows.E.word_constants_holds` (also `Formalism.ExponentWindows.E.Full.consts_DD`, `Formalism.ExponentWindows.E.Full.consts_UD`, `Formalism.ExponentWindows.E.Full.pow_mem_pair`).

*Proof.* Write $p_1 = p_{s_1}$, $p_0 = p_{s_0}$, $b_1 = b_{s_1}$, $b_0 = b_{s_0}$ and $I = (p_1^{b_1}, p_0^{b_0})$. The two are coprime up to $\varpi$: $a p_1 + a' p_0 = \varpi^N$. Raising to the power $b_1 + b_0$ and expanding, each term is divisible by $p_1^{b_1}$ or by $p_0^{b_0}$, so $\varpi^{N(b_1 + b_0)} \in I$.

1. Let $\rho$ be the least $k$ with $\varpi^k \in I$, and write $\varpi^\rho = x p_1^{b_1} + y p_0^{b_0}$. Then $f_\rho = x p_1^{b_1}$ lies in $(p_1^{b_1})$ and $f_\rho - \varpi^\rho = -y p_0^{b_0}$.

2. First we show that $p_1^{b_1} \notin (\varpi^{c+1}, p_0^{b_0})$ for some $c$; we take $c = N(b_1 + b_0)$ and write $\varpi^c = x p_1^{b_1} + y p_0^{b_0}$. Assume $p_1^{b_1} = u \varpi^{c+1} + v p_0^{b_0}$. Substituting, $\varpi^c (1 - \varpi x u) \in (p_0^{b_0})$. Since $p_0$ is a unit times a distinguished polynomial, divisibility by $p_0^{b_0}$ is not changed by the factor $\varpi^c$, so $1 - \varpi x u = p_0^{b_0} w$ for some $w$. The degree of $p_0$ is $\ell^{s_0} \ge 1$, so the constant term of $p_0$ lies in $(\varpi)$, and $b_0 \ge 1$. Taking constant terms gives $1 \in (\varpi)$, which is false since $\varpi$ is not a unit. Now let $c$ be the least number with $p_1^{b_1} \notin (\varpi^{c+1}, p_0^{b_0})$. If $c = 0$ then $p_1^{b_1} \in (1, p_0^{b_0})$ trivially; if $c > 0$ then $p_1^{b_1} \in (\varpi^c, p_0^{b_0})$ by minimality. In both cases $p_1^{b_1} = \varpi^c \alpha + p_0^{b_0} \beta$. $\square$

**Remark 8.10.8 (Formalization).** The level conditions are `LevelCond`, $\mathrm{N}$ is `NN`, $\mathrm{I}$ is `II`, and the distinguished family is `DistinguishedFamily` ([Statement.lean](lean:Formalism/DistinguishedUnitIdeals/Statement.lean#L23)); the level model setting, the lifting with $r$ (`LLift`), the lifting of $U(s_1)$ (`CLift`) and lifting modulo constants (`ConstLift`) are in ArcLiftOfLocalizationData.lean (lines 134 to 182); the arc words are `ArcWord` (WordConsts.lean line 39). The level models are the statements `MNone`, `MD`, `MDU`, `MDD` and `MUD` (Statement.lean lines 61 to 120); we read the statements and not the proofs. The five cases of the proposition are passed through `ConstLift*`, whose hypotheses are the level models. The fact that divisibility by $p_0^{b_0}$ is not changed by $\varpi^c$ is `mem_span_pow_of_uniformizer_mul`, which we did not open. The word constants are proved, yet the words with two downs and with an up after a down still carry the constants as data; the primitive form of Theorem E supplies them with this lemma.
