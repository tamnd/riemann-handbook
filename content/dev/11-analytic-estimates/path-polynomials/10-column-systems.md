---
title: Column systems
decls:
  - Formalism.MainNotions.ColumnSystems.Pf.colsAt_of
  - Formalism.MainNotions.ColumnSystems.Pf.restCols
  - Formalism.MainNotions.ColumnSystems.Pf.lemmaRData
  - Formalism.MainNotions.ColumnSystems.Pf.preAt_of
  - Formalism.MainNotions.ColumnSystems.Pf.restPre
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Column systems

The path polynomials of Section 9 are products of column polynomials, one for each column where the height changes. This section turns that factorization into the data used by the local matching of theta integrals. For every segment of a local datum, and every path polynomial of a standard pair that meets the thresholds of the segment, we build a *column system*: the column factors, each with a monomial twist and a lift of known order, and with the twists and orders adding up to explicit totals. Then we assemble the column systems of all segments with the tie factors, the monomial factors and one rigid factor into a *pre-system*, whose product has the target degrees and the target order. Both constructions hold for large constants. They are the two inputs of the step [theta local matching](/step/theta-local-matching/) that this chapter supplies, besides the theorem on admissible words.

We use the paths, column polynomials and path polynomials of Section 9 and [partitions](/learn/combinatorics/#partitions-and-young-tableaux). A horizontal strip has at most one box in each column; this is the combinatorial fact behind the first construction.

**Definition 7.10.1 (Local data and segments).** A *local datum* $X$ carries a prime $p$, a rank $m$, a number $c \geq 1$, exponents $G'$ and $n'$, and a finite set of top letters $\mathcal{T}$. Its letters are split into segments $j$; segment $j$ has a length $s_j$, a word $L_j$ on $2 s_j + 1$ letters whose letter $a$ is a vector if and only if $a$ is even, a gap $g_j$, distances $d_{j,i}$, and constants $A_0$, $Q_j$, $P_i$ and $\sigma \leq s_j$ attached to its segment block. Let $O$ be a discrete valuation ring with a uniformizer $w$ over $p$ and fraction field $K$. The *big ring* $R_H$ is the polynomial ring over $K$ in $m + 1$ variables for each pair $(t, \varepsilon) \in \mathcal{T} \times \{0, 1\}$, and segment $j$ comes with an algebra map $\iota_j$ from the polynomials of $L_j$ (and its tie variables) to $R_H$. A *global theory* $\beta$ attaches a block $\beta_j$ to each segment, with entries $sg_i$, $w_i$, $o_i$, $rz_{i,c}$, $ry_{i,0}$ and $o_+$. A *level datum* $L$ for $\beta$ gives the words $L_j$, levels $\ell_{j,i}$, exponents $j_{+,j}$ and standard polynomials $\operatorname{std}_j$.

**Definition 7.10.2 (Lifts of given order).** Let $f, \sigma \in R_H$ and $o \in \mathbb{N}$. Then $f$ is a *lift of order $o$ with symbol $\sigma$* if $f$ and $\sigma$ are integral, the substitution of $g f$ for every invertible matrix $g$ is divisible by $w^{o}$, and the substitution of $f$ is congruent to $w^{o} \sigma$ modulo $w^{o+1}$. A polynomial is *homogeneous of weight $o$* if every monomial in its support has weight $o$ for the fixed additive weight on the monomials of $R_H$.

**Definition 7.10.3 (Column systems).** Let $j$ be a segment and $G$ a polynomial of $L_j$ over $K$. A *column system* for $G$ is a finite family of factors $K_a$ with multidegrees $d_a$, monomials $\pi_a$ of $R_H$, lifts $f_a$ with orders $o_a$ and degrees $\deg_a$, and a number $a_0 \in \mathbb{N}$, such that:

1. each $K_a$ is integral, of multidegree $d_a$ with every digit $d_a(i) \leq 1$, $\sum_a d_a(i) = \deg L_j(i)$ for each letter $i$, and $\prod_a K_a = G$;
2. each $f_a$ is a lift of order $o_a$ with symbol $\pi_a \cdot \iota_j(K_a)$, the symbol is homogeneous of weight $o_a$, and both have multidegree $\deg_a$;
3. the degrees of $\pi_a$ and $\deg_a$ are at most $p^{G'}$ in every letter, and $\deg_a$ vanishes on the covector end letters of all segments;
4. $a_0 + \sum_{i < \sigma} sg_i \leq A_0$;
5. the twists and orders add up:
$$\sum_a \pi_a = Q_j a_0\, e_{\mathrm{start}} + \sum_{i < s_j} P_i \bigl(\bar a_i - \omega_i\bigr) e_{\mathrm{odd}(i)}, \qquad \sum_a o_a = \sum_{i < s_j} P_i \deg L_j(2i) + \deg L_j(2 s_j),$$
where $e_{\mathrm{start}}$ and $e_{\mathrm{odd}(i)}$ are the first variables of the start letter and of the odd letter $i$ of the segment, $\bar a_i$ is the coarse entry of the block at $i$, and $\omega_i = w_i$ for $i < \sigma$ and $\omega_i = o_i$ otherwise.

**Definition 7.10.4 (Column numerics).** The *column numerics* at constants $C$ say: for every local datum satisfying the standing hypotheses, every $m_m \in \{0, 12 c\}$, every $1 \leq n \leq c$, every segment $j$ and every block $b$ admissible at level $(c - n) \kappa_1$, where $\kappa_1 = \kappa_1(X) \geq 0$, the two inequalities
$$\sum_{l < \sigma} sg_l \leq \bigl\lfloor A_0 - (m_m + n \kappa_1) \bigr\rfloor, \qquad \sum_{l \leq i} w_l + \sum_{l < \sigma} sg_l \leq \bigl\lfloor A_0 - (m_m + n \kappa_1) \bigr\rfloor \quad (i < \sigma)$$
hold. The *column property* at constants $C$ says: under the same quantifiers, for every global theory $\beta$ whose blocks are admissible at level $(c - n)\kappa_1$, every level datum $L$ at height $m_m + n \kappa_1$, every segment $j$ and every standard pair $y$ of $L_j$ meeting the thresholds of the segment, the path polynomial $\Psi(y)$ over $K$ has a column system.

**Proposition 7.10.5 (Column systems from the numerics).** If the column numerics hold at constants $C$, so does the column property.

Lean: `Formalism.MainNotions.ColumnSystems.Pf.colsAt_of`.

*Proof.* Let $y = (\mu, I)$. Index the factors by the set of columns $c$ where the height of $\mu$ changes, and put $K_c = K_c^{(2 s_j + 1)}(I_c)$, the column polynomial of Section 9. The product of the $K_c$ is $\Psi(y)$, since the other columns contribute the factor $1$. At each letter $i$ the path changes by a horizontal strip, which has at most one box in each column, so the height at $c$ changes by at most $1$ and $K_c$ has degree $d_c(i) \in \{0, 1\}$ in letter $i$. The number of columns whose height changes at letter $i$ is the size of the strip, which is $\deg L_j(i)$; this is condition 1, and the integrality of $K_c$ holds because column polynomials have integer coefficients. The parity of the letters matches the convention of Section 9, so wedges and contractions occur as there. For condition 4, put $a_0 = \lfloor A_0 - (m_m + n\kappa_1) \rfloor - \sum_{l < \sigma} sg_l$, which is $\geq 0$ by the first inequality; then $a_0 + \sum_{l < \sigma} sg_l \leq A_0$ because $m_m + n \kappa_1 \geq 0$. The twists $\pi_c$, the lifts $f_c$, their orders and degrees are given column by column by the segment lemma, whose hypotheses are the two inequalities of the column numerics and the bound $2 s_j + 1 < m$ from the standing hypotheses; conditions 2, 3 and 5 are its conclusions. $\square$

**Theorem 7.10.6 (Column systems).** For large constants, the column property holds.

Lean: `Formalism.MainNotions.ColumnSystems.Pf.restCols`.

Here *for large constants* means, as in Section 6: for every $C_c \geq 0$ there is $T_0 > 0$ such that for all $C_0 \geq T_0$ there is $T_1 > 0$ such that for all $C_{E1}, C_{E2} \geq T_1$ there is $T_2 > 0$ such that the property holds for all remaining constants $\geq T_2$.

*Proof.* For large constants, the standard constant bounds hold, and they give the column numerics: both sums are controlled by partial sums of the block entries, bounded through $\sigma \leq s_j \leq N_1$ by a fraction of $A_0$, and the margin $m_m + n \kappa_1 \leq 12 c + c \kappa_1$ is absorbed by the rest. The [Proposition (Column systems from the numerics)](/entry/cols-at-of/) applies at each choice of constants. $\square$

**Definition 7.10.7 (Pre-systems).** Let $L$ be a level datum, $G_j$ a polynomial of $L_j$ for each segment $j$, and $\operatorname{Std}$ a monomial of $R_H$. A *pre-system* for $(G_j)$ and $\operatorname{Std}$ consists of:

1. a column system for each $G_j$, without the number $a_0$, with the additional property that the twists $\pi_a$ have degree $0$ on the covector end letters;
2. for each segment $j$ and tie $i$ of its block, a lift $f_{H,j,i}$ of order $o_{H,j,i}$ with symbol $\iota_j(\hat E_{j,i})$, where $\hat E_{j,i}$ is the tie generator, homogeneous and of a degree vanishing on the covector end letters;
3. a finite family of monomial factors: lifts $f_{M,a}$ of order $o_{M,a}$ with symbol a monomial $\alpha_a$ of weight $o_{M,a}$, with multiplicities $k_a$;
4. a rigid factor: an integral $f_R$, a monomial $R$, an order $o_R$ and a degree $d_R$, such that the substitution of $f_R$ is $w^{o_R} \prod_j \iota_j(E_{+,j})^{j_{+,j}} \cdot R$, and this product is integral, homogeneous of weight $o_R$ and of degree $d_R$;

such that all degrees are at most $p^{G'}$, and, with $F = f_R \prod_{j,a} f_{a} \prod_{j,i} f_{H,j,i}^{\ell_{j,i}} \prod_a f_{M,a}^{k_a}$:
$$\operatorname{Std} = R + \sum_{j,a} \pi_{j,a} + \sum_a k_a \alpha_a, \qquad o_R + \sum_{j,a} o_{j,a} + \sum_{j,i} \ell_{j,i}\, o_{H,j,i} + \sum_a k_a\, o_{M,a} = \operatorname{ord},$$
the degrees add up in the same way to the target degrees, $F$ lies in the polynomials of the target degrees, and at every invertible $g$ that moves the rational plane of $X$ the substitution of $g F$ is divisible by $w^{\operatorname{ord} + c}$. Here $\operatorname{ord}$ is the order of the family attached to $X$ and $\beta$.

**Definition 7.10.8 (Room).** For $a_0 = (a_0(j))_j$ and segments $j_0, j$, the *used amount* is
$$u(a_0, j_0, j) = p^{g_j} a_0(j) + p^{g_j} \sum_i sg_i + \sum_i p^{d_{j,i}} \Bigl(\sum_{c < m} rz_{i,c+1} + ry_{i,0}\Bigr) + c\, m\, (p^{g_j} - 1) + [j = j_0]\, c,$$
with the entries of $\beta_j$. The *room property* says: for every local datum satisfying the standing hypotheses, every $1 \leq n \leq c$, every global theory with blocks admissible at level $(c - n) \kappa_1$, every $a_0$ with $a_0(j) + \sum_{i < \sigma} sg_i \leq A_0$ for all $j$, and all $j_0, j$, we have $u(a_0, j_0, \rho(j)) \leq a_+(j) - o_+(j)$, where $\rho$ is the rotation of the segments and $a_+(j)$ is the top entry of segment $j$. The *pre-system property* says: under the quantifiers of the column property, for all nonzero $G_j$ with column systems and every $\operatorname{Std}$ with $\operatorname{Std} = \prod_j \operatorname{std}_j$ as monomials, a pre-system exists.

**Construction (Pre-system data).** Let column systems for nonzero $G_j$, a segment $j_0$ and a monomial $\operatorname{Std}$ be given, with $\operatorname{Std} = R(a_0, j_0) + \sum_{j,a} \pi_{j,a} + \sum_a k_a \alpha_a$, where $R(a_0, j_0)$ is the rigid monomial and $\alpha_a$, $k_a$ are the standard monomial factors and multiplicities. Take the columns from the column systems; the tie factors $f_{H,j,i} = h_{\mathrm{top}}(x_{j,i})^{P_{j,i}}$ with the top lift $h_{\mathrm{top}}$ and the exponents $x_{j,i}$, $P_{j,i}$ from the level datum, of order $P_{j,i}$; the monomial factors from the soft family; the rigid factor with $R = R(a_0, j_0)$ and $o_R = \sum_j j_{+,j}$. These data form a pre-system.

Lean: `Formalism.MainNotions.ColumnSystems.Pf.lemmaRData`.

*Proof.* The column data carry over. The twists vanish on the covector end letters because the degrees $\deg_a$ of condition 3 do and the symbol contains $\pi_a$; the tie degrees vanish there for the same reason, being multiples of the degrees of the top lifts. The tie factors are lifts by the soft height bound for segment powers, the monomial factors by the soft family, and the rigid factor by its product formula, being a product of top lifts and a monomial. The degree bounds come from $g_j \leq G'$. The sum of the degrees, the clean order at $g$ moving the rational plane, the membership of $F$ and the sum of the orders are four separate counting lemmas, each fed with the identity for $\operatorname{Std}$. $\square$

**Proposition 7.10.9 (Pre-systems from room).** If the room property holds at constants $C$, so does the pre-system property.

Lean: `Formalism.MainNotions.ColumnSystems.Pf.preAt_of`.

*Proof.* Take the numbers $a_0(j)$ of the column systems; condition 4 makes them admissible for the room property. Take $j_0$ to be the first segment, which exists since there are at least two. Since the entries $sg_i$ vanish for $i \geq \sigma$, the room inequality and the identity $\operatorname{Std} = \prod_j \operatorname{std}_j$ give $\operatorname{Std} = R(a_0, j_0) + \sum_j \bigl(Q_j a_0(j) e_{\mathrm{start}} + z_j\bigr) + \sum_a k_a \alpha_a$, with $z_j$ the second part of the twist sum of condition 5. By condition 5 this is the identity required by the [Construction (Pre-system data)](/entry/lemma-rdata/), which gives the pre-system. $\square$

**Theorem 7.10.10 (Pre-systems).** For large constants, the pre-system property holds.

Lean: `Formalism.MainNotions.ColumnSystems.Pf.restPre`.

*Proof.* For large constants, $C_{E1}, C_{E2} \geq 17$ and the standard constant bounds hold, and these give the room property: each term of $u$ is bounded by a multiple of the block entries and of $p^{g_j}$, and their sum fits under $a_+(j) - o_+(j)$ with the margin coming from the constants $17$. The [Proposition (Pre-systems from room)](/entry/pre-at-of/) applies at each choice of constants. $\square$

**Remark 7.10.11 (Formalization).** The column property is `ColsAt` and the column system is `ColSys` in [ColsDef.lean](lean:Formalism/SharpRestriction/GrowthBounds/StandardPolynomials/ColsDef.lean#L9); the pre-system is `PreSys` (PreSys.lean, line 9), the room property `RoomAt` (RestRoom.lean, line 16) and the pre-system property `PreAt` (PreDef.lean, line 9). The lifts of given order are `IsFac`, the homogeneity is `HomW (ndHom X)`, and the maps $\iota_j$ are `ioD`; we did not unfold `ioD`, `lift1`, `BDk`, `LvDat`, `BLk`, `HIext` or the segment lemma `ph_seg`, and the proofs of the counting lemmas in `lemmaRData` (`multidegree_sum_eq_target_degrees`, `cleaned_product_order_family_eq`, `total_product_mem_polynomials`, `order_sum_eq_order_family`) and of the room bound `room_of_std` were not read; the proofs above for them are outlines. The quantifier `TransportedAlt` ([Transported.lean](lean:Formalism/SharpRestriction/GrowthBounds/BinomialRatio/Transported.lean#L9)) has ten constant slots, and the properties `RestCols`, `RestPre` and `RestRoom` leave the slot `Cm` unused (`_`). `preAt_of` ignores its hypothesis on $m_m$ (an anonymous `_` in the `intro`) and always takes $j_0 = 0$ (ColumnPolynomialCovectorZero.lean, line 127). The column numerics come from `threshold_standard_one`, the room from `threshold_standard_seventeen`, which also asks $C_{E1}, C_{E2} \geq 17$. `restPre` is at line 138 of ColumnPolynomialCovectorZero.lean and `restCols` at line 90 of ColTop.lean. In `colsAt_of`, the parity of the letters is `col_lamS_vec` and $m_m + n\kappa_1 \geq 0$ uses `column_kappa_nonneg`.
