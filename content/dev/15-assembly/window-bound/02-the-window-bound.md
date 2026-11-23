---
title: The window bound
decls:
  - UpperTheory.V.HV.thmHV_of_counts
  - UpperTheory.V.HV.jointWin_of_counts
  - UpperTheory.V.HV.vwin_of_counts
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The window bound

This section proves the statement VWin of [the proof chapter on VWin](/proof/vwin/) from the counts of the last section and two more bounds: a bound at the prime $2$ and on cyclotomic layers on a window, and a bound on the minus part. This is Step 7 of that chapter. The result is used by [the theorem with four counts](/entry/of-four-alt/), which proves the two bounds and the count for Z, and so reduces VWin to Lemma K and four counts. VWin is one of the two inputs of [GRH for Dirichlet L-functions](/step/every-character-of-literature/).

We keep the notation of the last section: hosts $h = (\psi, m, q, d)$, their modulus $N_h$, the fields of $h$, the bad primes $B_\psi$, the fields $L_\psi(l) = \mathbb{Q}(\zeta_{l N_\psi})$, the layer bound $\Lambda$, and the plus, minus and $l$-bounds. Let $\mathfrak{f}_E$ be the conductor of an abelian field $E$, the least $N$ with $E \subseteq \mathbb{Q}(\zeta_N)$.

Fix *window constants* $K$: functions $R_0$ and $R_l$ from abelian fields to $\mathbb{N}$, and a number $C_K > 0$. Let $c_t > 0$ be a time exponent. For a primitive $\psi$ and $\varepsilon > 0$ put $R = R_0(\mathbb{Q}(\psi)) + \sum_{l \in B_\psi} R_l(L_\psi(l))$, where $\mathbb{Q}(\psi)$ is the fixed field of the kernel of $\psi$, and

$$J_\psi(\varepsilon) = 2^{R+2} \left( \frac{2 C_K c_t}{\varepsilon} \right)^{R} .$$

A pair of functions $m, t : \mathbb{R} \to \mathbb{N}$ is *admitted* with exponent $A_1$ if $m(x) \geq 2$, $2^{m(x)} \leq x^{A_1}$ and $2 \leq t(x) \leq x^{c_t}$ for all $x \geq 2$. Write $\beta(x) = \exp(x^{4\varepsilon/5})$.

**Definition 2.2.1 (Window).** Let $\psi$ be primitive, $\varepsilon > 0$, $(m, t)$ admitted, $q, d$ primes and $X > 0$. Put $J = J_\psi(\varepsilon)$. A number $Y$ is a *window* if $X^{1/J} \leq Y$, $Y^2 \leq X$, and for each $x \in [Y, Y^2]$:

1. each field of the host $(\psi, m(x), q, d)$ has $2$-bound $\beta(x)$ below $t(x)$;
2. $\Lambda(\psi, l, j_l, t(x), \beta(x))$ holds for each $l \in B_\psi$, with $j_l = \lfloor \log_l R_l(L_\psi(l)) \rfloor + 3$.

**Definition 2.2.2 (Window theorem).** The *window theorem* for $K$ and $c_t$ says: for each primitive $\psi$, each $\varepsilon \in (0, \tfrac{1}{52})$ and each $A_1$ there is $X_0$ such that for each admitted $(m, t)$, each $X \geq X_0$, and each pair of primes $q \equiv 3 \pmod 8$, $d \equiv 7 \pmod{16}$ prime to $N_\psi$ with $\log(qd) \leq X^{\varepsilon/(4J)}$, there is a window $Y$.

The *minus bound* says: there is $C$ such that for each host $(\psi, m, q, d)$ and $t \geq 2$, each field $E$ of the host has minus bound $\mu_C(o, [E : \mathbb{Q}], \mathfrak{f}_E, t)$ below $t$, where $o = [\mathbb{Q}(\psi) : \mathbb{Q}]$ and

$$\begin{aligned} \mu_C(o, n, N, t) = {}& 3 n t^2 \log(tN) \\ &+ C \sum_{l \mid o,\ l \neq 2} l \, n^2 t^2 \log(t l N)^2 . \end{aligned}$$

Lean: `UpperTheory.V.ThmBab` (also `UpperTheory.V.IsBWindow`, `UpperTheory.V.ThmBcFree`, `UpperTheory.V.minusBound`).

**Theorem 2.2.3 (Plus bound on a window).** Assume the counts for I, II, III, V$_\leq$ and Z, Poitou-Tate duality, the finiteness of local cohomology, local Tate duality, and Lemma K with some constant. Let $K$ be window constants and $c_t > 0$. For each primitive $\psi$ there are $C$ and primes $r_1, r_2$ such that for each $\varepsilon \in (0, \tfrac{1}{52})$ and $A_1$ there is $X_0$ with this property. Let $(m, t)$ be admitted, $X \geq X_0$, and $q, d$ primes as above with $2X^{c_t} + 1 < q, d$ and with each of $N_\psi, o_\psi, p_K, h^*, p_1, r_1, r_2$ less than $q$ and $d$. Let $Y$ be a window. Then for each $x \in [Y, Y^2]$, each CM field $E$ of the host $(\psi, m(x), q, d)$ has plus bound $(\mathfrak{f}_E \, t(x))^C + C \beta(x)$ below $t(x)$.

Lean: `UpperTheory.V.HV.thmHV_of_counts` (also `UpperTheory.V.HV.thmHV`, `UpperTheory.V.ThmHV`).

*Proof.* Apply the [Theorem 2.1.10](/entry/point-hv-of-counts/) on the plus bound at a point to $\psi$ and $j(l) = j_l$, and keep its $C, r_1, r_2$. Put $X_0 = 2^J$ with $J = J_\psi(\varepsilon)$. Let $x \in [Y, Y^2]$. Then $x \geq Y \geq X^{1/J} \geq 2$, so $m(x) \geq 2$ and $t(x) \leq x^{c_t} \leq X^{c_t}$, since $x \leq Y^2 \leq X$. So $2 t(x) + 1 < q$ and $< d$, and the host $h = (\psi, m(x), q, d)$ is large for $t(x)$. Part 2 of the window gives the layer bounds with $B = \beta(x) \geq 0$. The plus bound at a point gives the plus bound $(N_h t(x))^C + C \beta(x)$ for each field $E$ of $h$.

It remains to show $\mathfrak{f}_E = N_h$. The field $E$ embeds in $\mathbb{Q}(\zeta_{N_h})$, so $\mathfrak{f}_E \mid N_h$. Let $p$ be a prime factor of $N_h$. We find $a \equiv 1 \pmod{N_h/p}$ with $a \notin H_h$. For $p = 2$ take $a \equiv 1 + 2^{m+1} \pmod{2^{m+2}}$, which is not $\pm 1$ modulo $2^{m+2}$ since $m \geq 2$. For $p = q$ or $p = d$ take $a$ a non-square modulo $p$. For an odd $p \mid N_\psi$, $\psi$ is not trivial on the classes that are $1$ modulo $N_\psi/p$, since $\psi$ is primitive. So $E$ is not fixed by $a$, and $E \not\subseteq \mathbb{Q}(\zeta_{N_h/p})$. Hence $\mathfrak{f}_E = N_h$. $\square$

The next statement puts the two windows together. The window theorem gives a window $Y$, and on this window both the bound at $2$ and the plus bound hold.

**Theorem 2.2.4 (Joint window).** Assume the hypotheses of the last theorem with $c_t = 401$, and the window theorem for $K$ and $c_t = 401$. Let $\psi$ be primitive, $\varepsilon \in (0, \tfrac{1}{52})$, and $(m, t)$ admitted with exponent $A_1$. Then there are $J > 0$, $C$, $P$ and $X_0$ such that for each $X \geq X_0$ and each pair of primes $q \equiv 3 \pmod 8$, $d \equiv 7 \pmod{16}$ prime to $N_\psi$, with $2X^{401} + 1 < q, d$, $P < q, d$ and $\log(qd) \leq X^{\varepsilon/(4J)}$, there is $Y$ with $X^{1/J} \leq Y$, $Y^2 \leq X$ and, for each $x \in [Y, Y^2]$ and each field $E$ of $(\psi, m(x), q, d)$: $E$ has $2$-bound $\beta(x)$ below $t(x)$, and if $E$ is a CM field, it has plus bound $(\mathfrak{f}_E \, t(x))^C + C \beta(x)$ below $t(x)$.

Lean: `UpperTheory.V.HV.jointWin_of_counts` (also `UpperTheory.V.jointWin_of`, `UpperTheory.V.JointWin`).

*Proof.* Take $J = J_\psi(\varepsilon)$, which is positive since $C_K > 0$ and $\varepsilon > 0$. Let $X_B$ come from the window theorem, and $C, r_1, r_2, X_H$ from the last theorem. Put $X_0 = \max(X_B, X_H)$ and $P = N_\psi + o_\psi + p_K + h^* + p_1 + r_1 + r_2$. Each of the seven numbers is at most $P$, so each is less than $q$ and $d$. Let $Y$ be the window from the window theorem. Part 1 of the window gives the bound at $2$, and the last theorem gives the plus bound. $\square$

**Theorem 2.2.5 (VWin).** Assume the hypotheses of the joint window theorem and the minus bound. Let $\psi$ be primitive, $0 < \varepsilon < \tfrac{1}{52}$, and $e : \mathbb{R} \to \mathbb{N}$ with $x^{2 + 8\varepsilon} \leq 2^{e(x)} \leq 2 x^{2+8\varepsilon}$ for $x \geq 1$. Then there are $J \geq 1$ and $X_0$ such that for each $X \geq X_0$ and each pair $(q, d)$ in the set of pairs of [the proof chapter](/proof/vwin/) at $X^{1/J}$, there is $Y$ with $X^{1/J} \leq Y$ and $Y^2 \leq X$, such that for each $x \in [Y, Y^2]$ and each field $E$ of the host $(\psi, e(x), q, d)$:

$$\sum_{l \in S} \log l \sum_{k=1}^{\lfloor x^{401} \rfloor - 1} \ell_l(E, k) \leq \exp\!\big(\tfrac12 x^{\varepsilon}\big)$$

for each finite set $S$ of primes, with finite terms.

Lean: `UpperTheory.V.HV.vwin_of_counts` (also `UpperTheory.V.vwin_of_joint`, `UpperTheory.V.vwinAt_of_joint`, `UpperTheory.Top.VWin`).

*Proof.* Put $t(x) = \lfloor x^{401} \rfloor$ and $m = e$. For $x \geq 2$ we have $2^{e(x)} \geq x^2 \geq 4$, so $e(x) \geq 2$, and $2^{e(x)} \leq 2x^{3} \leq x^4$, and $2 \leq t(x) \leq x^{401}$. So $(e, t)$ is admitted with $A_1 = 4$. The joint window theorem gives $J, C, P, X_J$. Replace $J$ by $J' = \max(J, 1)$.

A pair $(q, d)$ of the proof chapter at $W = X^{1/J'}$ has $\tfrac12 W^{\varepsilon/5} < \log q$, and $d + 1$ is divisible by every odd prime up to $W^{\varepsilon/5}$. So for $X$ large, $q$ and $d$ exceed $2X^{401} + 1$ and $\max(P, N_\psi)$. Then $q$ and $d$ are prime to $N_\psi$. Also $\log(qd) \leq W^{\varepsilon/4}$ for $W$ large, and $W^{\varepsilon/4} = X^{\varepsilon/(4J')} \leq X^{\varepsilon/(4J)}$. The joint window theorem now gives $Y$ with $X^{1/J} \leq Y$, so $X^{1/J'} \leq Y$.

Let $x \in [Y, Y^2]$ and let $E$ be a field of $(\psi, e(x), q, d)$. It is a CM field, as in the last section. For an odd prime $l$ we have $\ell_l = \ell^+_l + \ell^-_l$. So the sum in the statement is at most $\beta(x) \log 2 + B_- + B_+$, where $B_-$ and $B_+$ are the minus and plus bounds. The conductor satisfies $\mathfrak{f}_E \leq 2^{e(x)+2} N_\psi q d$ and $[E : \mathbb{Q}] \leq \mathfrak{f}_E$. With $2^{e(x)} \leq 2x^3$, $t(x) \leq x^{401}$ and $\log(qd) \leq x^{\varepsilon/4}$ this gives $\log(\mathfrak{f}_E \, t(x)) \leq 2 x^{\varepsilon/4}$ for $x$ large. Then each term of $\mu_C$ is a power of $\log(\mathfrak{f}_E t)$ times $\mathfrak{f}_E^2 t^3 l$, so $B_- \leq K' \exp(8 x^{\varepsilon/4})$ for a constant $K'$. With $u = \mathfrak{f}_E t(x)$,

$$\beta(x) \log 2 + K' e^{8 x^{\varepsilon/4}} + u^C + C \beta(x) \leq \exp\!\big(\tfrac12 x^\varepsilon\big)$$

for $x$ large, because $\log u \leq 2x^{\varepsilon/4}$ and the exponents $\tfrac45 \varepsilon$ and $\tfrac14 \varepsilon$ are less than $\varepsilon$. Choose $X_0$ so that $X^{1/J'}$ is beyond all these thresholds. $\square$

**Remark 2.2.6 (Formalization).** The minus bound and the window theorem are stated in the code for any abelian field given by a modulus and a subgroup of $(\mathbb{Z}/N)^\times$, a finite set $B'$ of odd primes, and fields $L(l)$ with $l$-th roots of unity; the proof applies them to $\mathbb{Q}(\psi)$, $B_\psi$ and $L_\psi$. The minus bound is used in the form `ThmBc 401`, obtained from `ThmBcFree` by `thmBc_iff`. That lemma needs $1 \leq c_t$ only in one direction. The window is `IsBWindow` in [PrimeSetBoundDataOfPrimitiveChar.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PrimeSetBoundDataOfPrimitiveChar.lean#L42). In the plus bound on a window, the code asks for the window but uses only part 2. In `thmHV` ([ThmHV.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/ThmHV.lean#L14)) the hypotheses $\log(qd) \leq X^{\varepsilon/(4J)}$ and $\varepsilon < \tfrac{1}{52}$ are bound to `_` and not used. The constants $K$ enter only through $J_\psi$ and the window. In `jointWin_of` ([PrimeSetBoundDataOfPrimitiveChar.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PrimeSetBoundDataOfPrimitiveChar.lean#L145)) the facts that $r_1$ and $r_2$ are prime are dropped with `-`; only their size enters, through $P$. The equality $\mathfrak{f}_E = N_h$ is `hostCond`. The estimates of the last proof are `admissible_of_pageN`, `eventually_winPair_gt_power`, `log_mul_le_rpow_of_winPair`, `conductor_bounds_of_isChiField`, `log_conductor_mul_height_le_of_pageN`, `minusBound_le_exp_of_log_le` and `error_terms_le_sqrt_exp_rpow`; we read their statements, not their proofs. The sum of the three parts is `vvle_of_parts`.
