---
title: Block forms and symbol forms
decls:
  - Formalism.MainNotions.ColumnSystems.Pf.restBlockForm_of
  - Formalism.MainNotions.ColumnSystems.Pf.symbol_form_of_block_parts
  - Formalism.MainNotions.ColumnSystems.Pf.restForm_of_oplus
  - Formalism.MainNotions.ColumnSystems.Pf.restForm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Block forms and symbol forms

This section proves the symbol form at every datum. It says that, after a twisted substitution into the big ring, the Fock pairing of the symbols of two global theories is, up to a known power of $p$ and modulo $w^c$, a nonzero multiple of the product of the segment pairings when the theories agree, and is divisible by $w^c$ when they differ. The proof goes through a block form, the same statement for one block of one segment, and combines it with an orthogonality of distinct blocks. The symbol form is one of the three inputs, with the Witt identification and a raw tail statement, of the paired lifts, from which the extended closed form on column systems follows; that closed form is the second item of the local record of [the first theorem with constants](/entry/first-theorem-with-constants/) of Section 16. The reduction from the paired lifts is not unfolded here.

### Setting

We use the notation of the chapter on path polynomials: a local datum $X$ with prime $p$, rank $m$, precision $c$, top letters $\mathcal{T}$ and sizes $a_t, b_t$ for $t \in \mathcal{T}$; its segments $j$ with words $L_j$, positions $\mathrm{pos}_j(i)$ for $i < s_j$ and next letter $\mathrm{next}_j$; a discrete valuation ring $O$ with uniformizer $w$ over $p$ and fraction field $K$; the big ring $R_H$ and the maps $\iota_j$; the blocks of a segment, the kept blocks, the block lattices and the standard lattice $\mathcal{S}$; the Fock pairing $\langle\cdot,\cdot\rangle$; and global theories $\beta$, which attach a block $\beta_j$ to each segment. The degrees $h(x)$ for $x = (t, \varepsilon) \in \mathcal{T} \times \{0, 1\}$ are the degrees of the symbols at the pair $x$.

The constants are now ten: the nine constants $C_0, C_{Yb}, C_{de}, C_k, C_D, C_b, C_{E1}, C_{E2}, C_c$ of that chapter and a constant $C_m$. A statement holds *for large constants* if for every $C_c \geq 0$ there is $T_0 > 0$ such that for every $C_0 \geq T_0$ there is $T_1 > 0$ such that for all $C_{E1}, C_{E2}, C_m \geq T_1$ there is $T_2 > 0$ such that the statement holds for all $C_{Yb}, C_{de}, C_k, C_D, C_b \geq T_2$. A local datum is *in range* for the constants if $c \geq 1$, $X$ satisfies the extended standing hypotheses at $C_0, C_{Yb}, C_{de}, C_k, C_D, C_b$, and
$$c \leq C_c\big(c_s + Nk\log_p a + N c_l + n' c_l\big),$$
with the numbers $c_s, N, k, a, c_l$ of the datum. It is *numerically in range* if, in addition, $p$ is a prime with $p \geq 5$ and the exponent $n'$ is even with $n' \geq 2$.

For a segment $j$ put
$$\begin{aligned}\lambda_j &= \lfloor\log_p a_{\mathrm{next}}\rfloor + \lfloor\log_p b_{\mathrm{next}}\rfloor\\ &\quad + \sum_{i < s_j}\big(\lfloor\log_p a_{\mathrm{pos}(i)}\rfloor + \lfloor\log_p b_{\mathrm{pos}(i)}\rfloor\big),\end{aligned}$$
$$F_j = a_{\mathrm{next}}!\,b_{\mathrm{next}}!\prod_{i < s_j}a_{\mathrm{pos}(i)}!\,b_{\mathrm{pos}(i)}!, \qquad z_j = \frac{p^{(m+1)\lambda_j}}{F_j}.$$
For the whole datum put $\kappa_Z = \sum_x (m + 1)\lfloor\log_p h(x)\rfloor$ and $z = p^{\kappa_Z}/\prod_x h(x)!$. The factor $z_j$ scales the Fock pairing of one segment, whose monomial weights are products of factorials of the letter degrees, back to integral size, and $z$ does the same for the whole datum.

### The two forms

**Definition 5.17.1 (Block form).** The *block form* holds at the constants if, for every local datum $X$ in range, every discrete valuation ring $O$ as above (with an unramified quadratic setting over $\mathbb{Z}_p$), every segment $j$ and every kept block $b$ of segment $j$, there are $\kappa \in O$, $\kappa \neq 0$, with
$$v_p(\kappa) \leq (m + 2)\lambda_j,$$
and maps $s, s'$ from the symbols of $b$ to $R_H$ with the following two properties. Both send the block lattice of $b$ at the level attached to $C_m$ into the standard lattice of the block at the level $13$. If $u, u'$ are symbols whose block pairing, scaled by the special constant of the block, is $a \in O$, then
$$z_j\,\big\langle\iota_j(s\,u), \iota_j(s'\,u')\big\rangle = \kappa\,(a + w^cx)$$
for some $x \in O$.

**Definition 5.17.2 (Symbol form).** The *symbol form* holds at the constants if, for every local datum $X$ in range and every $O$ as above, there are $\kappa(\beta) \in O$, $\kappa(\beta) \neq 0$, with $v_p(\kappa(\beta)) \leq 4\kappa_0$ for the number $\kappa_0$ of the datum, and maps $s_\beta, s'_\beta$ into the standard lattices, for each global theory $\beta$ all of whose blocks are kept, with the following property. Let $u = (u_j)_j$ and $u' = (u'_j)_j$ be admissible families of symbols with segment pairings $a_j \in O$. Let $P, Q \in R_H$ be multihomogeneous of degree $h$, with $P$ congruent modulo $w^c$ to the symbol of $\beta$ at $s_\beta u$ and $Q$ congruent to the symbol of $\beta'$ at $s'_{\beta'}u'$. Then
$$z\,\langle P, Q\rangle = \delta_{\beta\beta'}\,\kappa(\beta)\prod_j a_j + w^c\nu$$
for some $\nu \in O$, where $\delta_{\beta\beta'}$ is $1$ if $\beta = \beta'$ and $0$ otherwise.

The block form is the statement for one segment and one block. The symbol form multiplies the block statements over the segments, and its second case, $\beta \neq \beta'$, is new: symbols of distinct theories are orthogonal modulo $w^c$.

### The numerical inputs

Two numerical statements carry the dependence on the constants. Both are about a kept block $b$ of a segment $j$ of a local datum in range.

**Definition 5.17.3 (Orthogonality numerics).** The *orthogonality numerics* hold at the constants if, for every local datum numerically in range, every segment $j$ and every kept block $b$ of segment $j$, the exponent $o_+$ of $b$ is at most the plus size $a_+(j)$ of the segment.

**Definition 5.17.4 ($\kappa$-numerics).** The *$\kappa$-numerics* hold at the constants if, for every local datum numerically in range, every segment $j$ and every kept block $b$ of segment $j$, with the degrees $\mathrm{cd}(x)$ of the block at the pairs $x$ and a positive product $\Phi_b$ of factorials attached to the block,
$$v_p(F_j) \leq (m + 1)\lambda_j + v_p\Big(\Phi_b\prod_x\mathrm{cd}(x)!\Big) \leq (m + 2)\lambda_j + v_p(F_j).$$

So the valuations of $F_j$ and of $\Phi_b\prod_x\mathrm{cd}(x)!$ differ by at most $(m + 1)\lambda_j$ in one direction and $\lambda_j$ in the other. This is what places $v_p(\kappa)$ in the window of the block form. We do not unfold $\Phi_b$; it is a product of the factorials of the base exponents and of the symbol levels of the block.

**Proposition 5.17.5 (Orthogonality numerics).** The orthogonality numerics hold for large constants.

Lean: `Formalism.MainNotions.ColumnSystems.Pf.restOPlus`.

The proof was not unfolded.

**Definition 5.17.6 (Factorial unit decomposition).** For a prime $p \geq 5$, the *factorial unit decomposition* gives, for $q = p^{t+1}$ and $\rho < q$, the identity
$$(\rho + qe)! = \rho!\,e!\,(q!)^e\,c_q(e)\,d_q(e, \rho)$$
in $\mathbb{Q}$, with explicit factors $c_q, d_q$, such that for any finite family of such $(t_k, \rho_k)$ the product $\prod_k c_{q_k}(e_k)d_{q_k}(e_k, \rho_k)$ is a $p$-adic unit for all $e$, and it and its inverse agree modulo $p^c$ with a polynomial of degree at most $4c$ in $e$ (in two forms, one with a polynomial over $\mathbb{Q}$ and one with an integral combination of monomials of degree at most $4c$).

The decomposition says that the factorial of a number with low digits $\rho$ is, up to a unit that depends polynomially on the high digits, the product of the factorials of the digit parts. It is what lets the factorials in $z_j$ be traded for the factorials of the degrees of a block.

### The proofs

**Theorem 5.17.7 (Block form from the factorial decomposition).** Let $D$ be a datum, and assume the factorial unit decomposition and the $\kappa$-numerics for large constants. Then the block form holds for large constants.

Lean: `Formalism.MainNotions.ColumnSystems.Pf.restBlockForm_of`.

*Proof.* The standing thresholds of the chapter on path polynomials hold for large constants. The condition $C_m \geq 17$ holds for large constants as well, with $T_1 = 17$: take $T_0 = 1$ and $T_2 = 1$. The $\kappa$-numerics hold for large constants by assumption. Large constants are closed under finite conjunction and under implication at each tuple of constants, so it suffices to derive the block form at a tuple where all three hold.

At such a tuple the block form follows from the following inputs at one block, combined as in the chapter on path polynomials.

1. The $\kappa$-numerics give a $\kappa \neq 0$ with $v_p(\kappa) \leq (m + 2)\lambda_j$ that matches $z_j$ against the factorials of the block.
2. With the factorial unit decomposition, the factorials of the letter degrees in $F_j$ split into the factorials of the digit parts and a unit. The unit is, modulo $w^c$, a polynomial of degree at most $4c$ in the high digits.
3. The operator attached to such a polynomial, applied in the odd variables of the block, lowers the level of the standard lattice by at most $4c$; this is the step that uses the datum $D$.
4. The Fock pairing commutes with $\iota_j$; the symbols are eigenvectors of the operators of the block; the maps $s, s'$ are homogeneous; a divisibility of the pairing; and a saturation of the block lattice.

The level condition uses $C_m \geq 17$: the block lattice at the level of $C_m$ goes, after the loss of $4c$ in step 3, into the standard lattice at the level $13$. The congruence of the block form then follows from steps 1 and 2, with the unit absorbed into $\kappa$ and the error into $w^cx$. $\square$

**Theorem 5.17.8 (Symbol form from the block parts).** Let $D$ be a datum, and assume the factorial unit decomposition, the $\kappa$-numerics and the orthogonality numerics for large constants. Then the symbol form holds for large constants.

Lean: `Formalism.MainNotions.ColumnSystems.Pf.symbol_form_of_block_parts`.

*Proof.* The block form holds for large constants by the Theorem (Block form from the factorial decomposition). The symbol form follows from it and from the following facts.

1. *Orthogonality.* At all constants, the block pairings of symbols of distinct kept blocks of one segment vanish modulo $w^c$ after the twisted substitution.
2. *Product.* The Fock pairing on $R_H$ of products of polynomials in the disjoint variables of the segments is the product of the pairings.
3. *Symbol degrees.* For large constants, the symbol of a theory all of whose blocks are kept is multihomogeneous of degree $h$. This follows from the orthogonality numerics: the weight of a monomial of the symbol at a pair $x$ is a sum over the segments, and the bound $o_+ \leq a_+(j)$ makes the contribution of segment $j$ equal to $h(x)$ if $\mathrm{next}_j$ or one of the positions of segment $j$ is the letter of $x$, and $0$ otherwise. Summing over the segments gives $h(x)$.
4. *Integrality, numerics and scaling.* The pairings stay in $O$, the products of the $\kappa$ of the blocks satisfy $v_p \leq 4\kappa_0$, and $z$ compares with the product of the $z_j$.

By the product, $z\langle P, Q\rangle$ is modulo $w^c$ a product over $j$ of block pairings. If $\beta = \beta'$ each factor is $\kappa_j(a_j + w^cx_j)$ by the block form; if $\beta \neq \beta'$ some factor pairs distinct blocks and vanishes modulo $w^c$ by orthogonality. $\square$

**Theorem 5.17.9 (Symbol form from the orthogonality numerics).** Let $D$ be a datum, and assume the factorial unit decomposition and the orthogonality numerics for large constants. Then the symbol form holds for large constants.

Lean: `Formalism.MainNotions.ColumnSystems.Pf.restForm_of_oplus`.

*Proof.* We show that the $\kappa$-numerics hold for large constants and then apply the Theorem (Symbol form from the block parts). Take the thresholds $T_0, T_1, T_2$ of the orthogonality numerics; we show that the $\kappa$-numerics hold at every tuple above them. At such a tuple the orthogonality numerics give the true degrees of the block and a coarse multiplicity bound. Together with the factorial unit decomposition, these give the $\kappa$-numerics: the valuation of $F_j$ is computed digit by digit, and the factorials of the block degrees match it up to $(m + 1)\lambda_j$ and $\lambda_j$. These two steps were not unfolded. $\square$

**Theorem 5.17.10 (Symbol form).** For every datum $D$ the symbol form holds for large constants.

Lean: `Formalism.MainNotions.ColumnSystems.Pf.restForm`.

*Proof.* The factorial unit decomposition holds for every prime $p \geq 5$ (its proof, which approximates the unit factors by Mahler expansions, is not unfolded), and the orthogonality numerics hold for large constants by the Proposition (Orthogonality numerics). Apply the Theorem (Symbol form from the orthogonality numerics). $\square$

So the symbol form is unconditional. The only hypothesis of the paired lifts that remains open in this part of the chapter is the raw tail statement; the Witt identification is read off from the admissibility of the datum.

**Remark 5.17.11 (Formalization).** The block form is `BlockFormAt` (CoarseMultiplicity/RestBlockForm.lean:96) and the symbol form is `FormAt` (line 65); `RestBlockForm` and `RestForm` wrap them in `TransportedAlt` (BinomialRatio/Transported.lean:9), the ten-constant quantifier. A different `TransportedAlt` with nine constants is at FlipOneThree.lean:312, and three more definitions with this name are elsewhere in the source. The $\kappa$-numerics `RestKapNum` (BlockForm.lean:15) discard $C_m$ as an unnamed argument, and so do the orthogonality numerics `RestOPlus` (SymbolFormOfOrthogonality.lean:31). `FactorialUnitDecomposition` (CovariantDegrees.lean:188) takes the datum as an unused argument `_D`, and it is proved by `lemma_five_two_first_holds` (GLWeightTheory.lean:99), whose proof was not unfolded. In `restBlockForm_of` (BlockForm.lean:17) the implicit datum is used only by `gThetaAt D` and by `h52`, and `gThetaAt` (GTheta.lean:99) proves a datum-free statement `GThetaAt` (BFDefs.lean:109). The steps `ioFockAt`, `eigAt`, `homAt`, `dvdAt`, `satAt`, `factAt_of`, `kapAt_of`, `blockFormAt_of` (MemIntPolOfCoeff.lean:215), `orthAt` (IoBlockEqSum.lean:128), `prodAt`, `intAt`, `numAt`, `zProdAt`, `restForm_of'`, `trueDegAt_of`, `coarseMultAt_of` and `kapNumAt_of` were not unfolded; the proofs above follow their statements. The symbol degrees are `restSymPol_of` (SymbolFormOfOrthogonality.lean:33), with the weight computation `TD_wLet` (WeightWLet.lean:32). Since `restKapNum_of` (BFFinal.lean:13) derives `RestKapNum` from `RestOPlus`, the hypothesis `hK` of `symbol_form_of_block_parts` (BFFinal.lean:10) is redundant, and `restForm_of_oplus` (line 26) is the form used by `restForm` (CoarseMultiplicity.lean:22). The names mix styles: `restBlockForm_of`, `symbol_form_of_block_parts` and `restForm_of_oplus` are three steps of one argument.
