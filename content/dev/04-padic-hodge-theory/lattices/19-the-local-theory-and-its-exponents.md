---
title: The local theory and its exponents
decls:
  - Formalism.MainNotions.LiftingTheory.local_parts_of_admitted
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local theory and its exponents

The local theory is a list of statements on Wach modules and on lifts of finite classes. Each statement is asked at every prime and for every pair of local fields. This section states the list with four constants $C$, $C_A$, $C_B$ and $C_K$. It proves the statements on Wach modules from the admitted inputs with $C = 10$, and the bounds on the lifting exponents with $C_A = 23$ and $C_B = C_K = 32$. The lifting exponent of [the local Theorem B](/entry/thm-b-at/) is the exponent of case A here. The next section proves the lifting statements and the whole local theory, which is used in [the local constants from the admitted local Galois statements](/entry/local-constants-from-admitted-local-galois-statements-alt/).

We keep the notation of the first sections: the period datum with prime $p$, the fields $K_0 \subseteq K$ with $n = [K_0 : \mathbb{Q}_p]$, the letters $i \in \mathbb{Z}/n$, the coefficient field $L$ with ring $\mathcal{O}$ and valuation $v$, $v(p) = 1$, and the Wach datum $W$ with level $s$, ring of letters $\Lambda$, element $\pi_0$ and finite group $\Delta$. For a prime $\ell$, finite extensions $K$ and $L$ of $\mathbb{Q}_\ell$ and a level $s$ at which $(K, L)$ is good, the data of the chapter give such a Wach datum with $p = \ell$. A statement *holds everywhere* if it holds for all these Wach data. We put $X_s = \varphi^{s-1}(X)$ and $q = \pi_0 + p$, read in every letter, and $u_\gamma = \chi_\Gamma(\gamma) \in \mathcal{O}^\times$. For a lattice $T$ and a letter $i$, $e_i N(T)$ is the part of the Wach module at $i$, and $N_i(T)$ is its part fixed by $\Delta$.

**Definition 8.19.1 (Cases).** The Wach datum is in *case A* if $K_0 \to K$ is a bijection, $s = 1$ and $p \ne 2$. It is in *case B* if every $g \in G$ has $v(\chi(g) - 1) \ge s$, with $\chi$ the cyclotomic character, and $[K : K_0] = (p - 1) p^{s-1}$. It is in the *intermediate case of index* $e$ if $s = 1$, $p \ne 2$ and $[K : K_0] = e$.

**Definition 8.19.2 (Admissible map, killing exponents).** Let $M, h \colon \mathbb{Z}/n \to \mathbb{N}$. A map of lattices $F \colon T_1 \to T_2$ is *admissible for* $(M, h)$ if $T_1$ and $T_2$ are crystalline, $F$ is onto, and the jumps of $T_1$ are bounded by $(M, h)$. Put $H = \max_i (M_i + h_i)$, $M^* = \max_i M_i$, $h^* = \max_i h_i$, and let $J$ be the set of jumps of $T_1$ in $[-M^*, h^*]$. Write $F$ also for the map $D(T_1) \to D(T_2)$. An element $a \in \Lambda$ *kills* $F$ at the letter $i$ if $a y \in F(e_i N(T_1))$ for all $y \in e_i N(T_2)$, and *kills $F$ at $i$ on invariants* if this holds for all $y \in N_i(T_2)$. Let $s_i$ be the least $k$ such that $X^k$ kills $F$ at $i$, put $A_i = \lceil s_i/(p-1) \rceil$, and let $r_i$ be the least $r$ such that $p^r$ kills $F$ at $i$ on invariants.

So $s_i$ and $r_i$ measure, letter by letter, how far $F$ is from being onto on Wach modules, in the variable $X$ and in $p$.

**Definition 8.19.3 (Exponents).** Let $e_W$, $J^{+M}$, $e_U$ and the lifting exponent be as in [the local Theorem B](/entry/thm-b-at/). For a prime $l$ and $s, H, M \in \mathbb{N}$ put
$$e_{WB}(l, s, H) = 2Hs + v_l\bigl((2H)!\bigr), \qquad c_H(l, H) = \bigl\lceil 1 + \log_l (H + 1) \bigr\rceil,$$
and for a finite set $J \subseteq \mathbb{Z}$
$$e_{UB}(l, M, s, J) = \sum_{j \in J^{+M}} \bigl(s + v_l(j)\bigr) + Ms + v_l(M!).$$
For $F$ admissible for $(M, h)$ the exponents of the two cases are
$$e'_A = 2 e_W(p, H) + e_U(p, M^*, J), \qquad e'_B = 2 e_{WB}(p, s, H) + e_{UB}(p, M^*, s, J).$$

**Definition 8.19.4 (The local theory).** Let $C, C_A, C_B, C_K \in \mathbb{R}$. The *local theory with constants* $(C, C_A, C_B, C_K)$ holds if the following eight statements hold everywhere. In each of them $F$ is admissible for $(M, h)$, $i$ is a letter, and $c_H = c_H(p, H)$.

1. *Interpolation.* The conclusion of the lemma below holds for $\mathcal{O}$.
2. *Killing.* $X_s^H$ kills $F$ at $i$. In case B, $p^{e_{WB}(p, s, H)}$ kills $F$ at $i$. In case A, $p^{e_W(p, H)}$ kills $F$ at $i$. In the intermediate case of index $e$, put $c = \lceil eH/(p-1) \rceil$; then $\pi'^c$ kills $F$ at $i$ on invariants for every $\pi' = u X^{\lfloor (p-1)/e \rfloor}$ with $u$ a unit of $\Lambda$, and $p^{2c + v_p((2c)!)}$ kills $F$ at $i$.
3. *Annihilator.* In case A, if $a, j \in \mathbb{N}$ and $(s_i - j) p/(p-1)^2 + c_H \le a$, then $p^a X^j$ kills $F$ at $i$.
4. *Recursion.* In case A, $s_{i-1} \le M_i + h_i + c_H + 3 + s_i/(p-1)$.
5. *Bounds with constant $C$.* In case A: $s_i \le \sum_{a \ge 0} (M_{i+a+1} + h_{i+a+1} + c_H + 3)(p-1)^{-a}$; the elements $\pi_0^{A_i}$, $p^{r_i}$ and $q^{A_i + r_i}$ kill $F$ at $i$ on invariants; $r_i \le s_i p/(p-1)^2 + c_H$; $A_i \le H/(p-1) + 1$; $A_i + r_i \le H(2p-1)/(p-1)^2 + c_H + 1$, and $A_i + r_i \le \theta H + c_H + 1$ with $\theta = 0.57$, $0.37$, $0.21$ for $p = 5$, $7$, $11$; and for $j \in \mathbb{N}$ and real $\beta \ge 0$ with $M_{i+a} + h_{i+a} \le 2\beta$ for $1 \le a \le j$,
$$r_i \le C \Bigl( \frac{\beta}{p} + \frac{H}{(p-1)^{j+1}} + 1 + \log (H + 1) \Bigr).$$
6. *The $\gamma$-equation.* In case A, for crystalline $T$ and $u_1 = u_\gamma^{p-1}$: for $x \in N_i(T)$ and $r \in \mathbb{N}$ there is $x' \in N_i(T)$ with $\gamma(\pi_0^r x) - \pi_0^r x = (u_1^r - 1)\pi_0^r x + \pi_0^{r+1} x'$; $v(u_1^r - 1) = 1 + v_p(r)$ for $r \ge 1$; $r + v_p(r!) \le rp/(p-1)$; and the solutions of the $\gamma$-equation along a basis of $N_i(T)$ have coefficients of valuation at least $-(r + v_p(r!))$ in degree $r$, as stated below.
7. *Truncation.* In case A, with $p_k = \varphi^k(q)$: $p_k = pa + \pi_0^{p^k} b$ with $a, b \in \Lambda^\Delta$; $\varphi^j(\pi_0)^r = u\, \pi_0^r \prod_{k < j} p_k^{(p-1)r}$ with $u$ a unit of $\Lambda^\Delta$; and two expansions of $c\, \varphi^j(\pi_0)^r$, stated below.
8. *Lifting.* (a) In case A, $F$ lifts with exponent $e'_A$. (b) In case B, $F$ lifts with exponent $e'_B$. (c) For crystalline $T_1$ with jumps bounded by $(M, h)$: in case B, $\prod_{j \in J^{+M^*}} (1 - u_\gamma^{-j})$ is associated in $\mathcal{O}$ to a power of $p$; in case A, $\prod_{j \in J^{+M^*}} \bigl( -(1 - u_\gamma^{-j})/p \bigr) = w p^k$ with $w \in \mathcal{O}^\times$ and $k \in \mathbb{Z}$. (d) In case A, $e'_A \le C_A \bigl( 2 + H/p + \log_p(H+1) \bigr)$; in case B, $e'_B \le C_B (Hs + 1)$, and if also $s = 1$, then $e'_B \le C_K H$. (e) Descent, stated below.

In 6, a *basis* of $N_i(T)$ is a family $b_1, \dots, b_d \in N_i(T)$ such that every $x \in N_i(T)$ is $\sum_m a_m b_m$ for unique $a_m$ in the $i$-th factor of $\Lambda^\Delta$. Let $z \in \pi_0 N_i(T)$. A *solution* with right side $z$ is a sequence $c_r \in L^d$ such that whenever $y_r = p^k c_r$ lies in $\mathcal{O}^d$ for $r < R$, the element $(\gamma - 1)\bigl(\sum_{r < R} \pi_0^r \sum_m y_{r,m} b_m\bigr) - p^k z$ lies in $\pi_0^R N_i(T)$. Statement 6 asks: for each $c_0 \in \mathcal{O}^d$ there is a solution starting with $c_0$; every such solution has $v(c_{r,m}) \ge -(r + v_p(r!))$; and the same bound holds for the coefficients of the inverse of the matrix $\bigl(\sum_r c^{(k)}_{r,m} X^r\bigr)_{m,k}$ of solutions $c^{(k)}$ with $z = 0$ that start with the unit vectors.

In 7, let $j \ge 1$, $y, M' \in \mathbb{N}$, $c \in L$ with $v(c) = -rp/(p-1)$, $\mathcal{J} = \pi_0^{M'} \prod_{k<j} p_k^y$ and $\sigma = (y + M'/p^{j-1})\, p/(p-1)^2 + 1$. Then $c\, \varphi^j(\pi_0)^r = x_1 + \mathcal{J} x_2$ in $\prod_i L[[X]]$, with $x_2 \in \Lambda^\Delta[1/p]$ and $x_1 = d a$ for some $a \in \Lambda^\Delta$ and $d \in L$ with $v(d) \ge -\sigma$. For each $N$, if $r$ is large enough, one can also take $x_1 \in p^N \Lambda^\Delta$.

In 8(e), let $K' \subseteq K$ with $G_K$ normal in $G_{K'}$, and put $g = [K : K']$. For a map $F$ of lattices of $G_{K'}$ whose restriction to $G_K$ is admissible: in case A, $F$ lifts over $K'$ with exponent $e'_A + v_p(g)$; in case B, with exponent $e'_B + v_p(g)$; and in case B with $s = 1$ and $K_0 \subseteq K'$, $v_\ell(g) = 0$.

**Definition 8.19.5 (Admitted inputs).** The *admitted inputs* are 23 conditions (A1) to (A23) on the local data, each asked everywhere. They are statements on Wach modules, on the Herr complex, on extensions and corestriction, and on the jumps, of the kind that the first sections of the chapter take from the literature. We refer to them by number; the Remark gives their names.

**Lemma 8.19.6 (Interpolation).** Let $S_1, S_2 \subseteq \mathbb{Z}$ be finite and disjoint, $\sigma_g \in \mathbb{N}$ and $c \colon \mathbb{Z} \to \mathcal{O}$ with $v(c_a - c_b) = \sigma_g + v_p(a - b)$ for distinct $a, b \in S_1 \cup S_2$. Put $P_k = \prod_{b \in S_k} (X - c_b)$. If $E \in \mathbb{N}$ and $v(P_2(c_a)) + v(P_1'(c_a)) \le E$ for every $a \in S_1$, then $p^E$ lies in the ideal $(P_1, P_2)$ of $\mathcal{O}[X]$.

Lean: `Formalism.MainNotions.LiftingTheory.lag_coreL` (also `lattice_clause_every_situation`, the statement everywhere).

*Proof.* The values $c_a$ are distinct, and for $a \in S_1$ the numbers $v(P_2(c_a))$ and $v(P_1'(c_a)) = \sum_{b \in S_1, b \ne a} v(c_a - c_b)$ are finite natural numbers. In $\mathcal{O}$ an element of valuation $k \in \mathbb{N}$ is a unit times $p^k$. So $\lambda_a = p^E / (P_2(c_a) P_1'(c_a))$ lies in $\mathcal{O}$. Put $A = \sum_{a \in S_1} \lambda_a \prod_{b \in S_1, b \ne a} (X - c_b) \in \mathcal{O}[X]$. Then $A(c_a) = \lambda_a P_1'(c_a)$, so $A P_2 - p^E$ vanishes at every $c_a$ with $a \in S_1$. Hence the monic polynomial $P_1$ divides it in $\mathcal{O}[X]$: $A P_2 - p^E = B P_1$, and $p^E = A P_2 - B P_1$. $\square$

**Proposition 8.19.7 (Shapes of the exponents).** Statements 8(c) and 8(d) hold everywhere with $C_A = 23$ and $C_B = C_K = 32$, with no further assumption.

Lean: `Formalism.MainNotions.LiftingTheory.lifting_exponent_shapes` (also `lifting_bracket_units_times_powers`, for 8(c)).

*Proof.* For 8(c), $u_\gamma$ is the image of a unit $z \in \mathbb{Z}_\ell^\times$ with $v(z - 1) = s$, and $s \ge 2$ if $p = 2$. Hence $v(1 - z^{-j}) = s + v_p(j)$ for $j \ne 0$. The set $J^{+M^*}$ does not contain $0$, so the product has valuation $k = |J^{+M^*}|\, s + \sum_j v_p(j)$ and is a unit times $p^k$. Dividing each factor by $-p$ gives the form of case A, with exponent $k - |J^{+M^*}|$.

For 8(d), $M^* \le H$ and $h^* \le H$, so $M^* + h^* \le 2H$, and $e_W$, $e_{WB}$ grow with $H$. We use the size bounds of the lifting exponents: if $M + h \le H'$ and $J \subseteq [-M, h]$, then $2e_{WB}(p, s, H') + e_{UB}(p, M, s, J) \le 16 H' s$, and for $p \ne 2$, $2 e_W(p, H') + e_U(p, M, J) \le \tfrac{15}{2} H'/(p-1) + 8 + 2 \log_p(H' + 1)$. With $H' = 2H$ we get $e'_B \le 32 Hs$, which gives both bounds of case B. In case A, $p \ge 3$ gives $15H/(p-1) \le \tfrac{45}{2} H/p$, and $\log_p(2H + 1) \le 1 + \log_p(H+1)$. So $e'_A \le \tfrac{45}{2} H/p + 10 + 2\log_p(H+1) \le 23\bigl(2 + H/p + \log_p(H+1)\bigr)$. $\square$

**Theorem 8.19.8 (Parts of the local theory).** Assume the admitted inputs. Then statements 1 to 7 of the local theory hold with $C = 10$, and statements 8(c) and 8(d) hold with $C_A = 23$ and $C_B = C_K = 32$.

Lean: `Formalism.MainNotions.LiftingTheory.local_parts_of_admitted`

*Proof.* Statement 1 is the lemma, and 8(c), 8(d) are the proposition. The killing statements 2 follow from (A2), (A9) and (A16): the bound by $X_s^H$ comes from (A16), and the bounds by powers of $p$ in cases A and B come from it with a generator of $\Gamma$ given by (A9), respectively from (A2). Statement 3 follows from (A9) and (A16). For 4 and 5, the inputs (A22) and (A23) first give, in case A, a statement on the jumps of the Wach quotients; with it and the admitted inputs, 4 holds and 5 holds with $C = 10$. Statements 6 and 7 follow from (A9). $\square$

**Remark 8.19.9 (Formalization).** The local theory is `aux₃` and the admitted inputs are `admitted`, the conjunction of `adm1` to `adm23` ([LiftingTheory.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LiftingTheory.lean#L589)). Their names: `WachLatticeFreeGlobal`, `P2`, `P3`, `ArchimedeanSignatureMatching`, `P5`, `P6` (`WachSaturationExactness`), `P7` (`WachCrystallineExtension`), `P8` (`WachMaxJumpBound`), `P9`, `WachCharacterisation`, `gammaSemisimpleQuotientGlobal`, `Pr2a` to `Pr2d` (the four properties of the Herr complex), `lem3` (`WachLatticeLengthLemma`), `coreExt`, `coreExtΔ`, `coreDss`, `coreCor`, `ClNat` with `ClKNat`, `FontaineLe` and `coreJumps`. We have not unfolded most of them, nor `JumpsQuot`, so the text names them only by number. The theorem is at [BaseChangePreservesUnitaryOf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BaseChangePreservesUnitaryOf.lean#L4827); it takes (A9), (A22) and (A23) out of `admitted` by chains of 8, 21 and 22 projections `h.2.2…`. The size bounds are `StatSizeA` and `StatSizeB`, proved in `lifting_size_bounds_all`. In `sI` and `rI` the least element is `sInf`, which is $0$ for an empty set; statement 2 makes the set for $s_i$ nonempty when $s = 1$. In 5 the logarithm is natural, and in 8(d) it is to the base $p$.
