---
title: The norm relation at tame primes
decls:
  - UpperTheory.V.Z.Kato.Sym.symEx
  - UpperTheory.V.Z.Kato.Nb.xi_hecke_prime_relation
  - UpperTheory.V.Z.Kato.Nb.kato_norm_relation_tame_prime
  - UpperTheory.V.Z.Kato.Nb.kato_tame_relation_projected
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The norm relation at tame primes

This section proves the norm relation of Kato's zeta classes at a tame prime $p$, in the form that the [gluing of zeta classes](/entry/k4-top/) uses: a weighted sum of zeta classes at level $p$ is the class at level $1$ times an element $P$ that is congruent to the Euler factor $\det(W(\sigma) - 1)$ at $p$. The proof has three steps. Kato's symbols of Siegel units satisfy six laws. These laws give a relation in cohomology between the classes at level $p$ and the Hecke operators $T_p$ and $\langle p\rangle$ applied to the classes at level $1$. A projection then turns $T_p$ and $\langle p\rangle$ into the Frobenius trace and determinant of Section 5, and so into the Euler factor. We keep the notation of Sections 4 and 5, with the Kummer modules $\mathcal{K}_w(N)$, the twist $\rho$ of $W$, the diamond matrices and the element $\mathrm{eul}_p(a, \delta)$.

### Kato's symbols

Let $c, d > 1$ be integers. For a level $M$ prime to $cd$ and rows $x, y \in (\mathbb{Z}/M)^2$, Kato's construction attaches to the Siegel units $g_c(x)$ and $g_d(y)$ a symbol, and its image in Galois cohomology modulo $l^n$ is a family $w_n^M(s)(x, y) \in K^\times$ for $s \in G_{\mathbb{Q}}$.

**Theorem 8.6.1 (Kato's symbols).** Let $X$ be a tower, $l$ a prime, and $c, d > 1$ prime to $6$. There is a family $w_n^M(s)(x, y)$, for $n, M \geq 0$, $s \in G_{\mathbb{Q}}$ and rows $x, y$ modulo $M$, such that for each $M > 0$ prime to $cd$:

1. (Cocycle law.) $w_n^M$ is a cocycle modulo $l^n$-th powers and is locally constant in $s$.
2. (Reduction law.) $w_{n+1}^M$ and $w_n^M$ agree modulo $l^n$ up to a coboundary.
3. (Level law.) $w_n^{kM}$ at the lifts of $x, y$ agrees with $w_n^M$ at $x, y$ up to a coboundary.
4. (Distribution law.) The sum of $w_n^{kM}$ over the fibres of the reduction to level $M$ agrees with $w_n^M$ up to a coboundary.
5. (Isogeny law.) The push of $w_n^{kM}$ along $\mathrm{diag}(k, 1)$ is cohomologous to the image of $w_n^M$ under $\mathrm{diag}(k, 1)$.
6. (Top law.) If $kM \mid M'$ and $l^n \mid M'$, and $s$ fixes $\mu_{M'}$, then the image of $w_n^M(s)(x, y)$ under $\mathrm{diag}(k, 1)$ is the Kummer element of level $l^n$ of the pair of Siegel units at lifts $x', y' \in \mathbb{Q}^2$ of $x, y$, up to a coboundary and an $l^n$-th power.

Lean: `UpperTheory.V.Z.Kato.Sym.symEx`.

*Proof.* The family is Kato's family of symbols of Siegel units, as in K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), Chapter II. Each law is proved separately. The cocycle law and the reduction law come from the Kummer theory of $K^\times$. The level law and the distribution law come from the distribution relations of Siegel units. The isogeny law and the top law come from the action of $\mathrm{GL}_2^+(\mathbb{Q})$ on Siegel units. The theorem collects these laws for one family. $\square$

### The norm relation at a tame prime

Let $p$ be a prime with $p \nmid lNcd$. For a level $M_0$, rows $x, y$ modulo $M_0$ and a family $a$ of classes, let $\Xi_{M_0}(x, y; t)$ be the Kummer class of weight $w$ attached to $a$ and to the pieces of the units modulo $M$ above $t$ in a quotient $A$ of $(\mathbb{Z}/M)^\times$. We write $\sim$ for equality of cohomology classes with the character $\pi \circ \varepsilon_M$, up to coboundaries modulo $l^n$.

**Theorem 8.6.2 (Hecke relation for shifted classes).** Let $p$ be prime to $M$ and $l$, let $M' = N p M_0$, and let $x, y$ be rows modulo $M_0$ such that $(x, y)$ and $(px, py)$ are admissible. Let $q \in (\mathbb{Z}/M)^\times$ be the class of $p$. Then, for the symbols $w$ of Kato,
$$
\begin{aligned}
p\, \Xi_{pM_0}(\tilde x, \tilde y; t) \sim {}& p\, \Xi_{M_0}(px, py; t) - T_p\, \Xi_{M_0}(px, py; t q^{-1}) \\
&+ p^w \langle p\rangle\, \Xi_{M_0}(px, py; t q^{-2}),
\end{aligned}
$$
where $\tilde x$ and $\tilde y$ are the lifts of $x$ and $y$ to level $pM_0$ shifted by the rows $(1, 0)$ and $(0, 1)$ of order $p$.

Lean: `UpperTheory.V.Z.Kato.Nb.xi_hecke_prime_relation`.

*Proof.* Expand $T_p$ by its $p + 1$ cosets. The $p$ upper triangular cosets, applied to the class at $(px, py)$, give by the level law and the distribution law the sum of the classes at level $pM_0$ over the lifts. All lifts except the shifted lift $(\tilde x, \tilde y)$ give the class at level $M_0$ again, by the distribution law, and this term is $p\,\Xi_{M_0}(px, py; t)$. The last coset $\gamma\,\mathrm{diag}(p, 1)$ with a diamond matrix $\gamma$ gives, by the isogeny law and a third relation for the action of $\gamma$, the term $p^w\langle p\rangle\,\Xi_{M_0}(px, py; tq^{-2})$. Here $\gamma$ lies in $\Gamma_0(N) \cap \Gamma_0(l)$, and the unit $\nu$ with $\nu \equiv \gamma_{11}$ modulo $N$, $\nu \equiv 1$ modulo $l^n$ and $\pi(\nu) = 1$ moves the index $t$ by $q^{-1}$ at each step. $\square$

For the zeta classes $Y_0(s, y)$ at level $N l^{r+n}$ and the classes $Y_T(s, (a, y))$ at level $pNl^{r+n}$ of the gluing of zeta classes, the relation reads as follows.

**Theorem 8.6.3 (Norm relation at a tame prime).** Let $l$ be odd, $N \geq 1$, $c, d$ and $g$ as in the hypotheses of Kato's classes, and let $p$ be a prime prime to $lNcd$. Assume that a family of Kato's symbols exists. Then for all $n, r$, with the character $\varepsilon_r^{-1}$,
$$
\begin{aligned}
p \sum_{a} Y_T(s, (a, y)) \sim {}& p\, Y_0(s, y) - T_p\, Y_0(s, y p^{-1}) \\
&+ p^w \langle p\rangle\, Y_0(s, y p^{-2}).
\end{aligned}
$$

Lean: `UpperTheory.V.Z.Kato.Nb.kato_norm_relation_tame_prime`.

*Proof.* For $n = 0$ every relation holds modulo $l^0$. Let $n \geq 1$. Choose rows at level $N l^{r+n}$ that are compatible with the Hecke operator at $p$, and choose the diamond matrix and the unit $\nu$ as above. The reduction of $\nu$ modulo $l^j$ is $1$ for $j \leq r + n$. The cyclotomic characters at the two levels $Nl^{r+n}$ and $pNl^{r+n}$, followed by the reduction to $(\mathbb{Z}/l^r)^\times$, are both $\varepsilon_r$, and the inverse of the image of $p$ in $(\mathbb{Z}/l^r)^\times$ is $p^{-1}$. Apply the Hecke relation for shifted classes. The top law relates the classes $\Xi$ at the two levels to $Y_0$ and $Y_T$. The sum over $a$ of $Y_T(s, (a, y))$ is the push of the class at level $pNl^{r+n}$ along the reduction, because the sum over a fibre of a projection is a sum over a filter. Combine the four relations by linearity of $\sim$. $\square$

### The tame relation for a weighted sum

Let $c_w \colon \mathbb{Z}/N \to \mathcal{O}$ be weights with some $c_w(x) \neq 0$, and let $Y$ be a weighted zeta system with exponent $c_0$, as in Section 4. For $u \in (\mathbb{Z}/l^r)^\times$ let $\eta(u) = \langle u\rangle^{-e}\chi_K(u)$, where $\chi_K$ is the character of the twist, and put $\mathrm{spec}_\eta(Z)(s) = \sum_u \eta(u)\, Z(s, u)$. A homomorphism $\psi_w \colon G_{\mathbb{Q}} \to \mathbb{Z}/l^n$ *kills $\mu_{q}$* if it is trivial on the elements that fix $\mu_q$.

**Theorem 8.6.4 (Tame relation for a weighted zeta system).** Let $W$ be in normal form for $(e, S, A)$ with entries in $\mathcal{O}$, with $l$ odd, $l \nmid N$ and $e \geq 1$, and let the data be admissible with weights $c_w$. There are $k \geq 0$ and a finite set $S'$ of places, with inertia at each place over $w \notin S'$ in the kernel of $W$, such that the following holds. Let $n \geq 1$, let $w \notin S'$ with $l^n \mid Nw - 1$, and let $\psi_w \colon G_{\mathbb{Q}} \to \mathbb{Z}/l^n$ be surjective and kill $\mu_{Nw}$. Then there are cocycles $Y^w_r$ on $G_{\mathbb{Q}}$ with values in $\mathcal{O}^2$, indexed by $\mathbb{Z}/l^n \times (\mathbb{Z}/l^r)^\times$, for $\rho$ and $(\psi_w, \varepsilon_r^{-1})$, continuous and compatible in $r$, and $P \in \mathcal{O}$, a unit $u$ and $b_r \in \mathcal{O}^2$, such that
$$
\Bigl|\sum_{a} \mathrm{spec}_\eta(Y^w_r(\cdot, (a, \cdot))) - P\, l^k\, \mathrm{spec}_\eta(Y_r) - (W b_r - b_r)\Bigr| \leq |l^r|
$$
on $G_{\mathbb{Q}}$, and $P \equiv u\,\det(W(\sigma) - 1) \bmod l^n$ for each Frobenius $\sigma$ at $Nw$.

Lean: `UpperTheory.V.Z.Kato.Nb.kato_tame_relation_projected`.

*Proof.* Fix $x_0$ with $c_w(x_0) \neq 0$. A lemma on zeta systems at a higher level, which uses Kato's symbols and the norm relations in the twist tower and the level tower, gives $c_1$ such that for each $x$ and each prime $p \nmid lNcd$ there is a zeta system $Y'_x$ at level $Np$ with exponent $c_0 + c_1$. For each $x$ with $c_w(x) \neq 0$ there is an integer $m(x)$ that bounds the denominators of the projection, and the classes are integral.

Let $S'$ be the set of the [Frobenius traces theorem](/entry/s-euler/) for $x_0$. Inertia at places over $w \notin S'$ lies in the kernel of $W$, since $W$ is unramified outside $S \subseteq S'$. For $w \notin S'$ put $p = Nw$ and take $a$ and $\delta$ from that theorem. Put $P = \mathrm{eul}_p(a, \delta)$. By the remark after that theorem in Section 5, $P \in \mathcal{O}$ and $P \equiv \det(W(\sigma) - 1) \bmod l^n$, so we can take $u = 1$.

For each $x$ and $r$, compare $Y_x$ and $Y'_x$ with the classes $Y_0$ and $Y_T$ of Kato. Sum the norm relation at the tame prime $p$ over the matrices $g_m(r_0)$. Apply $\mathrm{pr}$: the Hecke operator $T_p$ becomes $a$ and the diamond operator becomes $\delta$. The twist by $\eta$ turns the shifts $y p^{-1}$ and $y p^{-2}$ into the factors $p^{-(e+1)}$ and $p^{-2}$ in $\mathrm{spec}_\eta$, so the relation becomes the relation with the factor $P$. Put $M = \max_x m(x)$ and $Y^t = \sum_x c_w(x)\, l^M Y'_x$. Push $Y^t$ along $\psi_w$: since $\psi_w$ kills $\mu_p$ and $(\mathbb{Z}/p)^\times$ maps onto $\mathbb{Z}/l^n$, this gives cocycles $Y^w_r$ with the sum over $a$ equal to the sum over $(\mathbb{Z}/p)^\times$. Take $k = M + c_1$, and build $b_r$ from the coboundary terms. $\square$

**Remark 8.6.5 (Formalization).** The tame relation for a weighted zeta system has two hypotheses that are never used, $g_m(r_0) \in \Gamma_1(N)$ and the holomorphy of $j$; they are bound at [KatoTameRelationProjected.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/EulerFactorBounds/KatoTameRelationProjected.lean#L52) and appear again only in a `clear` at line 86. The holomorphy is in any case a field of every tower. The Hecke relation for shifted classes is a private theorem ([KatoNormRelationTamePrime.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/EulerFactorBounds/KatoNormRelationTamePrime.lean#L78)). The statement of Kato's symbols asks that $c$ and $d$ be prime to $6$ but not to $l$, and its proof is one application of an assembly lemma to eight lemmas ([SymEx.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SymmetricPowerSymbols/SymEx.lean#L12)).
