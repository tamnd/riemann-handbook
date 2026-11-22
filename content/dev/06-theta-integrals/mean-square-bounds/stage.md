---
id: stage
title: Few primes in a progression give bad quadratic twists
kind: theorem
decl: QH.stage
module: Development.AutomorphicArithmetic.MeanSquareBounds.StagePow
covers: 705
status: drafted
drafted_by: writer@claude
---
This theorem says that, among the primes $q$ of an arithmetic progression, at most a share $\eta$ give a twist $\xi \cdot (\tfrac{\cdot}{q})$ that fails `Box`. It is the core of `stage1` and `stage2`, and so of [`pair_share`](/entry/pair-share/).

## Statement

Let $P$ be the set of primes $q \in (U^{1/2}, U]$ with $q \equiv a_0 \pmod{m_0}$. With $\Lambda$ the [[von Mangoldt function|087EMZTHWN]], let

$$S(Z, y, q, \kappa) = \sum_{n \le Z} \Lambda(n) \min\Bigl(1, \frac{y}{n}\Bigr) \kappa(n) \Bigl(\frac{n}{q}\Bigr).$$

`admitted ε Y U m0 a0` says $8 \mid m_0$, $\gcd(a_0, m_0) = 1$, $\tfrac14 \log^2 Y \log m_0 \le \log U$ and $Y^{\varepsilon/6} \le \log U \le Y^{\varepsilon/5}\log^2 Y$. `Box Q C τ Y X χ` says: $\chi \ne 1$, the level of $\chi$ is at most $Q$, $L(s, \chi) \neq 0$ for $\operatorname{Re} s > 1 - \tfrac1{400}$ and $|\operatorname{Im} s| \le Q$, $|\tfrac{L'}{L}(1, \chi)| \le C \log Y$, and $|g_\chi(y)| \le y^{1/2 + \tau}$ for $y \in [Y, X]$, with $g_\chi$ as in [`pairEx`](/entry/pair-ex/).

**Theorem.** There is $C > 0$ such that for all $\varepsilon \in (0, \tfrac14]$, $\tau > 0$, $K \ge 1$, $\eta > 0$ and $R \in \mathbb{N}$ there is $Y_0$ with this property. Let $Y \ge Y_0$, let `admitted ε Y U m0 a0` hold, let $1 \le F \le U^{1/2}$, and let $\Xi$ be a set of at most $R$ primitive [[Dirichlet characters|JR4QSEFXWF]] of level at most $F$. Let each prime $p \mid m_0$ have $p \le Y^{\varepsilon/5}$ or $p > Y^{400K}$. Then $P \ne \emptyset$. If $B \subseteq P$ and for each $q \in B$ some $\xi \in \Xi$ has a primitive character induced by $\xi \cdot (\tfrac{\cdot}{q})$ that fails `Box (FU) C τ Y Y^K`, then $|B| \le \eta |P|$.

## Proof

1. `count_a` gives $|P| \ge U^{9/10}$. It uses [`pnt_progressions_relative_weak_holds`](/entry/pnt-progressions-relative-weak-holds/) and `excBound`, which is Siegel's bound $\beta \le 1 - c(\delta) k^{-\delta}$ for a real zero $\beta$ of $L(s, \chi)$, $\chi$ real and nontrivial modulo $k$ (Siegel, Acta Arith. 1, 1935).
2. Let $q \in B$ with its $\xi$ of level $f$. Then $q > U^{1/2} \ge F \ge f$, so $q \nmid f$. By `twist_prim` and `ind_unique`, the character of the hypothesis is $\psi = \xi \cdot (\tfrac{\cdot}{q})$, primitive of level $fq \le FU$, and $\psi \ne 1$.
3. By `box_of_S`, `Box (FU) C τ Y Y^K ψ` holds if $\psi$ has the zero-free box of height $FU$ and $|S(Y^{400K}, y, q, \xi)| \le y^{1/2+\tau}/2$ for $y \in [Y, Y^K]$. So $B \subseteq B_1 \cup \bigcup_{\xi} B_2(\xi)$. For $q \in B_1$ some twist has a zero in the box. For $q \in B_2(\xi)$, $S$ is large at some $y$.
4. `count_bad`, a zero density bound, gives $|B_1| \le |C_b| U^{3/8} \le \tfrac{\eta}{2}|P|$ for large $U$.
5. `meanSqK` gives $\sum_{q \in P} |S(Y^{400K}, y, q, \kappa)|^2 \le C_m\, y \log y\, |P|$ for $|\kappa| \le 1$ and $y \in [Y, Y^K]$. So `bad_share` gives $|B_2(\xi)| \le \tfrac{\eta}{2(R+1)} |P|$, and the sum over $\Xi$ is at most $\tfrac{\eta}{2}|P|$.

## In the Lean code

The theorem is in [StagePow.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/StagePow.lean#L41). `admitted`, `S`, `Box` and `BoxAll` are in [PrimeSetTwoBounds.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PrimeSetTwoBounds.lean#L18). We have not unfolded `meanSqK` or `count_bad`, so we do not name the results behind them.

In Lean the bad condition is `∃ M ≠ 0, ¬ BoxAll (F * U) C τ Y (Y ^ K) (ξ · J q) M`. Step 2 shows that this changes nothing. $C$ is the constant of `box_of_S`. An element of $\Xi$ is a pair $(N, \xi)$ with $\xi$ modulo $N + 1$.
