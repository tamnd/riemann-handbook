---
title: Proposition 5
decls:
  - Formalism.MainNotions.Proposition5Numerics.pickStep_all
  - Formalism.MainNotions.Proposition5Numerics.restPick
  - Formalism.MainNotions.Proposition5Numerics.membership_of_three_parts
  - Formalism.MainNotions.Proposition5Numerics.restMemb
  - Formalism.MainNotions.Proposition5Numerics.proposition5_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Proposition 5

This section proves Proposition 5: a test polynomial $G$ on the side of the source lattices pairs with a sum of one-sided elements to a value whose valuation is at most $D_X = O(|T|(m+1)^2\log_p a)$. The proof has three steps. A pick step writes the pairing of $G$ with an assembled polynomial as a multiple of a plane Gram pairing. A membership step shows that the assembled polynomials are sums of one-sided elements. A numerics step checks the hypotheses of [the plane Gram theorem](/entry/stmt/) with $C_H = 26$. Proposition 5 is the main input of the [reduction](/entry/stmt-e-of-mem/) of Statement E in Section 5. We use the notation of Sections 1 to 3.

### The data and the conclusion

Let the unramified quadratic setting of Section 3 be given, with the numbers $T$, $L_1$, $L_2$, $\delta$, $h$, $x$, $\lambda_0$, $a$, $Y$, $c_{pp}$, $c_0$, $D_p$, $c^*$ of Statement E. Let $K \geq 1$ with $m + 1 = r + K$. Write $N_1$ for the window count, $G'$ for the good exponent and $c_P$ for the derived precision $c'(n', r, |T|, c_0, c_{pp}, c^*)$. Put $d = d(T, \lambda_0)$, the multidegree of the test polynomials, and
$$\kappa = \sum_s (m+1)\lfloor\log_p d_s\rfloor.$$

**Definition 5.4.1 (Data of the second kind).** With a constant $C$ and a constant $C_{La}$, *data of the second kind* consist of the setting above, frames $\mathcal{F}$ of rank $r$, and a family $B_1, \dots, B_{n_b}$ in a polynomial ring over $\mathcal{O}$ in $n' \times (r + K)$ variables, such that: the hypotheses of Statement E hold with $C$; the frames are compatible with $T$, $L_1$, $L_2$, $N_1$ and $G'$; there is a degree bound $E'$ with $E'_t \leq E_0$ and $E'_t$ at most the flat degree of $\lambda_0$ for $t \in T$, and each $B_i$ is a generator of the symbol space with these parameters; the $B_i$ are linearly independent; and their span has a complement.

The symbol spaces and their generators belong to the second part of the selection (Section 8). Each $B_i$ gives a polynomial $\mathrm{sym}(B_i)$ in the variables of $n'$ matrices of size $(m+1) \times (m+1)$, by a twisted substitution at precision $c_P$ and exponent $p^{G'}$.

**Definition 5.4.2 (Operator closure).** Let $M$ be a space of polynomials and let $c_0 \geq 0$. The *operator closure* $\mathrm{Op}_{c_0}(M)$ is the span of the polynomials $\omega f$, where $f \in M$ and $\omega$ is a word in the operators attached to the letters of $T$ that uses each letter at most $c_0$ times.

**Definition 5.4.3 (Weight level).** A polynomial $P$ over $K$ has *$w$-level at least $j$* if every coefficient of $P$ lies in $w^j\mathcal{O}$.

**Definition 5.4.4 (Valuation window).** Let $D \geq 0$. An element $x \in K$ is *$p^D$-bounded* if $x \in \mathcal{O}$ and $x$ divides $p^D$ in $\mathcal{O}$. Equivalently, $0 \leq v(x) \leq D\,v(p)$.

**Definition 5.4.5 (Proposition 5 at level $C$).** Let $C$, $C_D$, $C_{La}$ and the plane Gram constants $(C_H, C_E, C_6, C_{18})$ be given. *Proposition 5 at level $C$* says: for all data of the second kind there is an integer
$$D_X \leq C_D\,|T|\,(m+1)^2\log_p a$$
such that every $G$ with the four properties below satisfies the conclusion below. The properties are: $G$ lies in the operator closure $\mathrm{Op}_{c_0}$ of the span of the $\mathrm{sym}(B_i)$; $G$ has multidegree $d$; $G$ has $w$-level $0$ but not $w$-level $1$; and $G$ satisfies the membership condition of Section 5. The conclusion is: there are signed chain data $\mathcal{D}_t$ and an admissible input $F_2$ with $v_{\mathrm{BB}}(F_2) = 0$, which satisfy the slope hypothesis with $C_H$ and the size hypothesis, such that for every pair $(G_p, R)$ with the five output properties of the [projection derivative estimate](/entry/stmt/) there are one-sided elements $\sigma_1, \dots, \sigma_n$ of multidegree $d$ for which
$$\frac{p^\kappa\,\langle G, \sigma_1 + \dots + \sigma_n\rangle}{\prod_s d_s!}\ \text{ is } p^{D_X}\text{-bounded}.$$

*Proposition 5 for a datum $\mathcal{D}$* with plane Gram constants $(C_H, C_E, C_6, C_{18})$ says: if $\mathcal{D}$ is admissible, then there are $C_D, C_1 > 0$ such that Proposition 5 at level $C$ holds for all $C \geq C_1$.

The conclusion is shaped to meet the plane Gram theorem. It hands over chain data and an input $F_2$, and it accepts any output of the projection derivative estimate for them.

### The three steps

The three steps use two further objects that we do not unfold: an assembly map $\mathrm{asm}_{\rho, N_0}$, which takes a plane polynomial $A$ of degree $d_{\mathrm{Pl}}$ and a norm polynomial $N_0$ to a polynomial in the variables of the test side, and a block condition on the digit pattern $\rho$ and on the plane and norm degrees $d_{\mathrm{Pl}}$, $d_{\mathrm{No}}$. A *norm test* $N_0$ is an integral polynomial of degree $d_{\mathrm{No}}$ whose lowest weights on certain letter sets are bounded by $k_{j,u} + 4c_P$ for shifts $k$.

**Definition 5.4.6 (Pick step).** Let $C_n > 0$ and put $D_n = C_n|T|(m+1)^2\log_p a$. The *pick step* at level $C$ says: for all data of the second kind and every $G$ of multidegree $d$ with $w$-level $0$ but not $1$ that satisfies the membership condition, there are signed chain data $\mathcal{D}_t$ with degree condition, a digit pattern $\rho$ with the block condition, an admissible input $F_2$ with $v_{\mathrm{BB}}(F_2) = 0$, a norm test $N_0$ and a scalar $k_0$ with
$$v(k_0) \leq v_p\Big(\prod_s d_s!\Big) - n_0 + D_n$$
and, for every integral plane polynomial $A$ of degree $d_{\mathrm{Pl}}$,
$$v\big(\langle G, \mathrm{asm}_{\rho, N_0}(A)\rangle - k_0\langle F_2, A\rangle_\gamma\big) \geq c_P + v_p\Big(\prod_s d_s!\Big) - \kappa.$$

**Definition 5.4.7 (Membership step).** The *membership step* says: for all data of the second kind, all signed chain data with degree condition, every $\rho$ with the block condition and every norm test $N_0$, every integral $G_p$ with the output conditions for $(24, 60)$ and with $\phi$ mapping its monomials into $\mathrm{Pol}(r, d_O)$ satisfies
$$\mathrm{asm}_{\rho, N_0}(\phi G_p) = \sigma_1 + \dots + \sigma_n$$
with one-sided elements $\sigma_q$ of multidegree $d$.

**Definition 5.4.8 (Numerics step).** Let $C_m > 0$ and put $\ell = |T|(m+1)^2\log_p a$. The *numerics step* says: for all data of the second kind, $1 \leq \ell$, $\kappa \leq C_m\ell$, and for all signed chain data with degree condition and all $\rho$ with the block condition, the slope hypothesis with $26$ and the size hypothesis hold, $\kappa(d_O) \geq 0$, and $D_m + D_l + 3\kappa(d_O) \leq C_m\ell$.

**Theorem 5.4.9 (Pick step).** There are $C_n, C_1 > 0$ such that the pick step holds at every level $C \geq C_1$, for every $C_{La}$. In particular, for every datum $\mathcal{D}$ and all constants, the pick step holds with constants independent of $\mathcal{D}$, whether or not $\mathcal{D}$ is admissible.

Lean: `Formalism.MainNotions.Proposition5Numerics.pickStep_all` (also `Formalism.MainNotions.Proposition5Numerics.restPick`, the form for a datum).

*Proof.* A size lemma gives $C_n$ and $C_1$, and for $C \geq C_1$ it gives size bounds, a block condition and the precision bound for all data of the second kind. Fix such data. The setting gives a uniformizer of $\mathcal{O}$, an admissible ring in the Hida setting, and characteristic $0$ of the fraction field. The hypotheses of Statement E give $p \geq 13$, $r \geq 2$, and the frames give $J \geq 1$ segments. Outside $T$ the degrees $d_s$ vanish. The pick construction then needs four local facts, which hold for the setting: digit facts for the frames, a choice of shifts and of a projector for each chain datum, a bound for the norm test from the digit absolute values, and the unit $\gamma$ with its digit approximation. With these, the construction gives $\mathcal{D}_t$, $\rho$, $F_2$, $N_0$ and $k_0$ as required. For a datum, the admissibility hypothesis is not needed. $\square$

**Theorem 5.4.10 (Membership step).** For every datum $\mathcal{D}$ and all constants, if $\mathcal{D}$ is admissible, then there is $C_1 > 0$ such that the membership step holds at all levels $C \geq C_1$.

Lean: `Formalism.MainNotions.Proposition5Numerics.restMemb` (also `Formalism.MainNotions.Proposition5Numerics.membership_of_three_parts`, the reduction to three local statements).

*Proof.* The statement follows from four local statements: a decomposition of the assembled polynomial into pieces, an algebraic identity, a degree count and a label count. The decomposition in turn follows from three local statements at every uniformized ring, for frames with the main frame hypothesis and for all chain data. The first is a valuation bound and a support condition for the norm part and the plane part. The second says that the degree condition on chain data gives the admissible input condition for the norm degrees. The third is a condition on the divided derivatives of the plane part. Each of these local statements, and three auxiliary facts used by the decomposition, holds, and none of them depends on $\mathcal{D}$. $\square$

**Theorem 5.4.11 (Proposition 5).** Let $\mathcal{D}$ be a datum with constants $C_{La}$, $C_k$, $C_{rk}$, $C_{\deg}$. Then Proposition 5 holds for $\mathcal{D}$ with the plane Gram constants $(26, 2, 24, 60)$.

Lean: `Formalism.MainNotions.Proposition5Numerics.proposition5_holds`.

*Proof.* Let $\mathcal{D}$ be admissible. By [the pick step](/entry/pick-step-all/), [the membership step](/entry/rest-memb/) and a numerics lemma we get constants $(C_n, C_1)$, $C_2$ and $(C_m, C_3)$ for the three steps. Put
$$C_D = C_n + 2C_m + 1, \qquad C_1' = \max(C_1, C_2, C_3, C_n + 3C_m).$$
Let $C \geq C_1'$, take data of the second kind and a test polynomial $G$ with the four properties. The pick step gives $\mathcal{D}_t$, $\rho$, $F_2$, $N_0$ and $k_0$. The numerics step gives the slope hypothesis with $26$ and the size hypothesis for $\mathcal{D}_t$, so these are the chain data of the conclusion. Let $(G_p, R)$ be an output of the projection derivative estimate for $\mathcal{D}_t$ and $F_2$. The membership step writes $\mathrm{asm}_{\rho, N_0}(\phi G_p)$ as a sum of one-sided elements $\sigma_q$ of multidegree $d$. Then $\langle G, \sum_q\sigma_q\rangle = \langle G, \mathrm{asm}_{\rho, N_0}(\phi G_p)\rangle$, and the pick step compares it with $k_0\langle F_2, \phi G_p\rangle_\gamma$ up to an error of valuation at least $c_P + v_p(\prod_s d_s!) - \kappa$. The projection derivative estimate with $C_E = 2$ bounds the valuation of $\langle F_2, \phi(G_p + R)\rangle_\gamma$ by $D_m + D_l + 3\kappa(d_O) + n_0$. The numerics step bounds $D_m + D_l + 3\kappa(d_O)$ and $\kappa$ by $C_m\ell$, and the pick step bounds $v(k_0)$ by $v_p(\prod_s d_s!) - n_0 + C_n\ell$. These bounds combine to the bound $D_X \leq (C_n + 2C_m + 1)\ell$, and the condition $C \geq C_n + 3C_m$ enters this combination. $\square$

**Remark 5.4.12 (Formalization).** The pick step for a datum (`restPick`, DiagonalSupport/GramExponentArithmetic.lean:223) discards the admissibility hypothesis with `intro _`, and `pickStep_all` takes a datum `D` that it uses only to call the local facts `restJP`, `noAt`, `digAbs` and `gaAt`. The three local statements of the membership step (`RestValBdG`, `RestXXG`, `RestDdG`, DiagonalSupport/RestValBdG.lean:79 to 101) do not mention a datum. The function `twiceValuationFactorialProduct` (DiagonalSupport/TwiceValuationFactorialProduct.lean:16) is $v_p(\prod_s d_s!)$, not twice that value. The parameter list of Proposition 5 at level $C$ has both $m + 1 = r + K$ and $r \leq m + 1$; the second follows from the first (TwistedSubstitution/Proposition5Gram.lean:63). The assembly map `asm`, the block condition `BlockOK`, the one-sided elements `OneSidedLemma4Element`, the symbol spaces, the operator words `opWord`, the size lemma `sizeStep`, the construction `pickAt_of`, the numerics lemma `restNum` and the combination `proposition5_at_of_three_parts` were not unfolded; the proof of Proposition 5 lists the bounds that the combination uses and its constants, not its steps. The name "Proposition 5" has no source that we could find.
