---
title: Reference towers and the bound I1
decls:
  - RootFieldNumerics.Ref.level
  - RootFieldNumerics.global_model_real_tower_smooth
  - GlobalTheory.T.good_tower_real_I6
  - GlobalTheory.CompanionTheory.Relay.good_tower_real_I6
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reference towers and the bound I1

The condition I1 of [the tower conditions](/entry/full-intersection-tower-i8-identity/) says that the top intersection numbers of a tower at a level $B$ differ from those of a fixed reference model by at most $C \log B$. This section proves the input for I1 for good towers: the realisations of a good tower are linked to fixed reference realisations, with a smooth correction line and a vertical error whose weighted sum over the primes is at most $C \log B$. The proof compares, at each level and each component, the root model of the tower with the reference root model of the origin, in common coordinates. The local input at each prime of $S_B$ is again the sandwich from the Fargues comparison. The result is used in [the volume theorem](/entry/volume-theorem-x-of-inputs/), where it gives I1 together with the [statement on real towers](/entry/volume-theorem-x-of-inputs/).

We keep the setting of [the previous section](/entry/i5-and-i6-of-is-global-of-good-origin/): a CM field $E$ with host $H$, a datum $D$ of signature $(p, q)$, an integral model $Y$, a root tower $T$ of type $(\Psi, p + q)$ with a good origin, and an intersection system $\mathrm{II}$. Write $N = p + q$.

**Definition 9.7.1 (Real tower).** A real tower over a root tower $T$ gives, for each component $c$, an analytic system $\mathrm{Sys}_c$ and an integer $n_c$, and, for each level $B$ and component $c$, a tie: a realisation $\mathrm{Re}$ of the model $M_{B,c}$ in the analytic system $\mathrm{Sys}_c$. The realisation carries reference lines $\mathrm{ref}(a)$ for the labels $a$ and twisted lines $\mathrm{line}(a, t)$ for small $t > 0$. The tie fixes the degree as $n_c$ times the degree of the model, it fixes the fundamental reference lines by the rule that $\mathrm{ref}(\tau, i)$ has coefficients $-\sum_{k \le i}$ of the coordinate degrees, it asks that the metrics of the fundamental lines are logarithmic, and it asks that the reference line of the empty label is the ample line $A$. A good origin gives a real tower in a canonical way.

For a realisation $\mathrm{Re}$ we write $\mathrm{Re}.\mathrm{PB}$ for the family of top intersection numbers of its twisted lines in $\mathrm{II}$, as a function of the weight.

**Definition 9.7.2 (Vertical closeness).** Let $P$ be a coordinate ideal, let $S$ be a finite set of primes and let $\alpha \colon \mathbb{N} \to \mathbb{R}$. Two hermitian lines $A$ and $B$ on the same coordinates are vertically close for $P$, $S$ and $\alpha$ if there are multihomogeneous polynomials $f$ and $g$, not in $P$, such that

1. the multidegrees satisfy $\deg f - \deg g = A.a - B.a$;
2. at the complex points, $\|f\|_B = \|g\|_A$;
3. over the fibres of characteristic not in $S$, the divisors of $f$ and $g$ are equal;
4. over the fibres of characteristic $\ell \in S$, the difference of the divisors of $f$ and $g$ is bounded by $\alpha(\ell)$ times the divisor of $\ell$.

So two vertically close lines have the same archimedean metrics after a change of section, and differ only at the primes of $S$, by a bounded amount.

**Definition 9.7.3 (Reference linked).** A real tower $R$ over $T$ is reference linked for $\mathrm{II}$ if there are a constant $C$, a smooth potential $\theta_c$ and a fixed family $\mathrm{P}^{\mathrm{fix}}_c$ for each component, such that for every level $B \ge 2$ and every component $c$ there are coordinates with a coordinate ideal $P$, two realisations $\mathrm{Re}$ and $\mathrm{Re}'$, a finite set $S$ of primes, a function $\alpha \ge 0$ on $S$ and a hermitian line $H$ with:

1. $\mathrm{Re}.\mathrm{PB} = $ the numbers of the tie of $R$ at $(B, c)$, and $\mathrm{Re}'.\mathrm{PB} = \mathrm{P}^{\mathrm{fix}}_c$, with equal degrees;
2. $H$ smooth, with potential the pullback of $\theta_c$;
3. $\mathrm{Re}.\mathrm{line}(a, t)$ and $\mathrm{Re}'.\mathrm{line}(a, t)$ vertically close for $P$, $S$ and $\alpha$, for every label $a$ and $0 < t \le t_0$;
4. $H$, $\mathrm{ref}(a) + H$ for $\mathrm{Re}$, and $\mathrm{ref}(a) + H$ for $\mathrm{Re}'$ nef at every $\ell \in S$;
5. $\sum_{\ell \in S} \alpha(\ell) \log \ell \le C \log B$.

The intuition is that the numbers at level $B$ are computed on a model that agrees with a fixed model at the archimedean places and at the primes outside $S$, and differs at the primes of $S$ by a vertical divisor of total size $C \log B$. The [statement on real towers](/entry/volume-theorem-x-of-inputs/) turns this into I1: the top numbers change by the arithmetic degree of the vertical difference, which is bounded by $\sum \alpha(\ell)\log \ell$ times a geometric degree.

We first prove a comparison in common coordinates. Let $M$ be a root model over a finite set $S$ of primes, with a root origin $o$, and let $R$ be a reference root model with a root origin $o_0$ over the empty set of primes, in the same analytic system and fixed data. Let $i$ be a field map from the field of $R$ to the field of $M$ that is compatible with the two origins.

**Theorem 9.7.4 (Common realisation).** Assume the resolution statement for residue fields, let $\mathrm{II}$ be a full intersection system, and let $o$, $o_0$ and $i$ be as above. Assume:

1. both realisations are on the full coordinate ideal, and the flag degree of $o_0$ is $1$;
2. every point of the analytic space has a neighbourhood with a holomorphic lift, a nonzero multiple of the fixed point map;
3. there are sections $s_1, \dots, s_L$ of the chart lattice of $R$ of weight $e A - 1$ that do not all vanish at any complex point;
4. $n$ bounds the negatives of the coefficients of the reference lines of $o_0$;
5. $M$ is nef at every prime of $S$ for every dominant weight;
6. $q, m > 0$, every prime factor of $m$ lies in $S$, and the valuation bounds hold: for every root $r$ and every valuation ring $W$ on which the normalised coordinates of $M$ and of $R$ are integral, the two elements
$$
\begin{aligned}
&m \Big(\frac{i(y_R^{x_r} e_0(r))}{y_M^{x_r} e(r)}\Big)^q, \\
&m \Big(\frac{y_M^{x_r} e(r)}{i(y_R^{x_r} e_0(r))}\Big)^q
\end{aligned}
$$
lie in $W$, where $y^{x_r}$ is the monomial of the coordinate degrees of $r$ and $e(r)$, $e_0(r)$ are the root constants.

Then there are coordinates with a coordinate ideal $P$, realisations $\mathrm{Re}$ and $\mathrm{Re}'$ and a hermitian line $H$ such that $\mathrm{Re}.\mathrm{PB} = o.\mathrm{PB}$, $\mathrm{Re}'.\mathrm{PB} = o_0.\mathrm{PB}$, $\mathrm{Re}'$ and $\mathrm{Re}$ have the same degree, $H$ is smooth with potential the pullback of $n e$ times the theta potential of the empty label, the twisted lines of $\mathrm{Re}$ and $\mathrm{Re}'$ are vertically close for $P$, $S$ and $\alpha(\ell) = v_\ell(m^N)/q$ for $0 < t \le t_0$, and $H$ and $\mathrm{ref}(a) + H$ for both realisations are nef at every prime of $S$.

Lean: `RootFieldNumerics.Ref.level`

*Proof.* We describe the construction. The coordinates are joined: there is one block for each block of $M$, one for each block of $R$, and one more block for the sections $s_1, \dots, s_L$. The coordinate vector is $y_M$ on the blocks of $M$, $i(y_R)$ on the blocks of $R$ and $i(s)$ on the last block. Each block has a nonzero coordinate: for $M$ and $R$ by arithmeticity, and for the last block since the sections do not all vanish at a complex point of $R$. The joined vector is birational, since $y_M$ already is, and so the block function field is the whole field.

The resolution statement gives a coordinate ideal $P$ for the joined coordinates of the right degree. The realisations $\mathrm{Re}$ and $\mathrm{Re}'$ are the pullbacks of the realisations of $o$ and $o_0$ to the joined coordinates; pullback compatibility of realisations gives $\mathrm{Re}.\mathrm{PB} = o.\mathrm{PB}$ and $\mathrm{Re}'.\mathrm{PB} = o_0.\mathrm{PB}$, and the degrees agree since the flag degree of $o_0$ is $1$. The line $H$ is the line of the last block with $n$ times the degree $e$; its potential is the pullback of $n e$ times the theta potential, and it is smooth by the local lifts of hypothesis 2.

For vertical closeness, a twisted line of $\mathrm{Re}$ and the matching line of $\mathrm{Re}'$ have the same weight, so their quotient is a ratio of monomials in the coordinates of $M$ and of $R$ times the root constants. The valuation bounds of hypothesis 6 say that $m$ times the $q$-th power of this ratio and of its inverse are integral at every valuation ring. So the divisors of the two lines differ by at most $v_\ell(m^N)/q$ times the divisor of $\ell$ at each prime $\ell$; at primes not dividing $m$, in particular at primes outside $S$, they agree. For the empty label and for the other labels the development has two separate steps. Nefness of $H$ and of $\mathrm{ref}(a) + H$ at primes of $S$ comes from hypothesis 5 by pullback and by a step lemma for sums with the bound $n$. $\square$

**Theorem 9.7.5 (Good towers are reference linked).** Assume the top level inputs. Let $E$ be a CM field, abelian over $\mathbb{Q}$, let $Y$ be an integral model of $X_o(l)$, let $T$ be a root tower of type $(\Psi, p + q)$ with a good origin $o$, and let $\mathrm{II}$ be an intersection system. Assume that $Y$ is global, that the origin satisfies the extra conditions, that $\mathrm{II}$ is full and that $p, q \ge 1$. Then the real tower of the origin is reference linked for $\mathrm{II}$.

Lean: `RootFieldNumerics.global_model_real_tower_smooth` (also `GlobalTheory.T.good_tower_real_I6` and `GlobalTheory.CompanionTheory.Relay.good_tower_real_I6`, second names)

*Proof.* From the top level inputs we take the Fargues comparison and the resolution statement. By [the bound M1](/entry/volume-theorem-x-of-inputs/) for good towers, the models $M_{B,c}$ are nef at the primes of $S_B$ for dominant weights.

For each component $a$ a valuation bound gives a constant $C_0(a)$ with the following property. For every finite set $S$ of primes that contains the primes dividing the discriminant of $E$, every root model $M$ over $S$ with a root origin compatible with the reference origin of $a$ by a field map $i$, and with a sandwich at every prime of $S$, there are $q, m > 0$ with all prime factors of $m$ in $S$, the valuation bounds of the common realisation theorem, and

$$
\log m \le q\Big(C_0(a) + \sum_{\ell \in S} w_\ell \log \ell\Big), \qquad w_2 = 2,\ w_\ell = \frac{1}{\ell - 1} \text{ for } \ell \ne 2.
$$

The origin is ample: for each $a$ it gives $e$, $L$ and sections $s$ as in hypothesis 3. Each reference model has finitely many reference coefficients, so there is $n_a$ as in hypothesis 4. A counting bound for the origin gives $C_3$ with

$$
\sum_{\ell \in S_B} \Big(w_\ell + 2 v_\ell(\operatorname{disc} E)\Big)\log \ell \le C_3 \log B
$$

for every $B \ge 2$. Put $C_1 = \sum_a |C_0(a)|$ and

$$
C = N\Big(\frac{C_1}{\log 2} + C_3\Big).
$$

The potentials are $n_a e_a$ times the theta potential of the empty label, and the fixed family for $a$ is the family of numbers of the reference origin.

Fix $B \ge 2$ and a component $a$. A comparison lemma gives a field map $i$ from the reference model to $M_{B,a}$, compatible with the origins. The primes of $S_B$ are prime, and every prime dividing the discriminant lies in $S_B$, since $S_B$ contains the bad primes and these include the prime divisors of $2 \operatorname{disc}(E)$ times a further factor. At each $\ell \in S_B$ the Hodge component of the origin is Hodge-Tate free, so the Fargues comparison gives a sandwich, as in [the previous section](/entry/i5-and-i6-of-is-global-of-good-origin/). The valuation bound now gives $q$ and $m$.

The common realisation theorem applies, with the local lifts from the extra conditions, the smoothness and degree conditions of the origin, the sections and $n_a$ from above, and nefness from M1. It gives $P$, $\mathrm{Re}$, $\mathrm{Re}'$ and $H$ with conditions 1 to 4 of reference linked, for $S = S_B$ and $\alpha(\ell) = v_\ell(m^N)/q \ge 0$.

It remains to check condition 5. Since all prime factors of $m$ lie in $S_B$,

$$
\sum_{\ell \in S_B} \frac{v_\ell(m^N)}{q} \log \ell = \frac{N \log m}{q}.
$$

Since $\log 2 \le \log B$, we have $C_1 \le (C_1/\log 2) \log B$, and the counting bound gives $\sum_{\ell \in S_B} w_\ell \log \ell \le C_3 \log B$. With $C_0(a) \le C_1$,

$$
\log m \le q\Big(\frac{C_1}{\log 2} + C_3\Big)\log B,
$$

and multiplying by $N/q$ gives $\sum \alpha(\ell)\log\ell \le C \log B$. $\square$

The constant $C$ does not depend on $B$, since the reference models are fixed and the sets $S_B$ grow only through the counting bound. The factor $N = p + q$ comes from the power $m^N$ in the valuation bounds.

**Remark 9.7.6 (Formalization).** The name of the second and third declarations speaks of I6, but the conclusion is that the real tower is reference linked, which the volume theorem uses for I1. The two other names are relays with the same statement. The Fargues comparison and the resolution statement are taken from the top level inputs by position, as the seventh part and as a field of the tenth part ([GlobalModelRealTowerSmooth.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/GlobalModelRealTowerSmooth.lean#L177)). That $Y$ is global is used only for M1, and of the extra conditions only the local holomorphic lifts are used; $q \ge 1$ is used only through M1, and $p \ge 1$ is used for M1 and to get $p + q > 0$ for the Fargues step. In the common realisation theorem the joined coordinates have the index type $(K_M \sqcup K_R) \sqcup \{\ast\}$ ([GlobalModelRealTowerSmooth.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/GlobalModelRealTowerSmooth.lean#L45)). We have not unfolded the valuation bound, the counting bound, the comparison lemma, the resolution statement or the definitions of sandwich and nefness at a prime; the intuition given for reference linked and for vertical closeness is our reading of the definitions, not a statement of the development.
