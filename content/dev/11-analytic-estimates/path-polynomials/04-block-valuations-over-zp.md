---
title: Block valuations over the p-adic integers
decls:
  - Formalism.MainNotions.G.SymmetricFormBlocks.block_valuation_Zp_of_lattice_inclusion
  - Formalism.MainNotions.G.SymmetricFormBlocks.restLL_of
  - Formalism.MainNotions.G.SymmetricFormBlocks.restLL_proved
  - Formalism.MainNotions.G.SymmetricFormBlocks.block_valuation_Zp_of_valuation_bound
  - Formalism.MainNotions.G.SymmetricFormBlocks.block_valuation_Zp_of_numeric_bound
  - Formalism.MainNotions.G.SymmetricFormBlocks.block_valuation_over_Zp_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Block valuations over the p-adic integers

This section proves the block valuation bound. For every block of an instance, and every depth $D \geq 0$, the standard lattice $\mathcal{S}$ contains a family of dual pairs for the Fock pairing with one exponent $e$, and $e$ is at most the valuation of the monomial factorial of every monomial of $\mathcal{S}$, plus $D$, plus an explicit loss. The number of pairs misses the total rank of the level lattices by at most the sum of the bad counts. The proof combines the good pairs of Section 3 with two inputs: the projected lattice is close to the standard lattice, and the binomial factors of the Fock block decomposition have small valuation. The bound is the first part of the open conditions in Section 6.

**Definition 7.4.1 (Instances and their blocks).** An *instance* $X$ carries a prime $p$, a rank $r \geq 1$, a length $s$, a number $N_t$, a size $a \geq 1$, a parameter $Y$, and a finite window $A \subseteq \mathbb{N}$; these come with constants $C_0, C_{E1}, C_{E2}$ and the segment data of [Theorem 5.11.3](/entry/theorem-a-closed-form-holds/), which also fix a number $t \leq s$ of ties. For every box point $a_{\mathrm{top}} \in A^{s}$, every $a_+ \in A$ and every *kept* segment block $b$, there is a block $G = G(a_{\mathrm{top}}, a_+, b)$ in the sense of Section 3, on $2s + 1$ letters with $t$ ties. Its set of levels does not depend on $a_+$. We write $\mathcal{S}(G)$, $\mathcal{P}(G)$, $\Lambda_{j,j_+}(G)$ and $\beta_{j,j_+}$ for the objects of Section 3.

**Definition 7.4.2 (Loss and exponents).** Put $\lambda_A = \log_p(8a + r) + 1$ and $\kappa_0 = 2 N_t (r + 1) \log_p a$. The *level passage loss* is
$$\ell(X) = 10 (s + 1)(r + 1)\, \lambda_A + \kappa_0.$$
Put $a_{\mathrm{big}} = (3s + 2) a$. For a block $G$ with $t$ ties, the *lattice exponent* is $U(G) = (t + 1) \lceil (r + 1)\, \lambda'(p, a_{\mathrm{big}}, r) \rceil$, where $\lambda'$ is a logarithmic size function of the same kind as $\lambda_A$. The *level exponent* $M(G)$ is the largest value of $v_p\bigl(\lambda_{j,j_+} \prod_a d_a(L_{j,j_+})!\,(B - j_+)!\bigr)$ over the levels of $G$, with $\lambda_{j,j_+}$ as in Section 3.

**Definition 7.4.3 (Block bad count).** The *block bad count* at depth $D$ is $\operatorname{bad}_G(D) = \sum_{(j,j_+)} \operatorname{bad}(\beta_{j,j_+}, \Lambda_{j,j_+}(G), D)$, summed over the levels of $G$.

**Theorem 7.4.4 (Block valuation bound over $\mathbb{Z}_p$).** Let $X$ be an instance with constants satisfying $C_{Yb} \geq 1$, $C_{E1} \geq 0$, $C_{E2} \geq 0$ and the window hypotheses of [Theorem 5.11.3](/entry/theorem-a-closed-form-holds/). Let $a_{\mathrm{top}} \in A^{s}$, $a_+ \in A$, let $b$ be a kept block, $G = G(a_{\mathrm{top}}, a_+, b)$, and let $D \geq 0$ be an integer. Then there are $n \geq 0$, an integer $e$ and $x_1, \dots, x_n, y_1, \dots, y_n \in \mathcal{S}(G)$ such that:

1. $\langle x_k, y_l \rangle = p^{e} \delta_{kl}$ for all $k, l$;
2. $e \leq v_p(\mu!) + D + \ell(X)$ for every $z \in \mathcal{S}(G)$ and every monomial $\mu$ of $z$;
3. $\sum_{(j,j_+)} \operatorname{rk} \Lambda_{j,j_+}(G) \leq n + \operatorname{bad}_G(D)$.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.block_valuation_over_Zp_holds`.

We prove the theorem in three reductions. The first one is the heart of the matter.

**Proposition 7.4.5 (From the lattice inclusion and the valuation bound).** Let $X$ be an instance with $r \geq 1$. Assume:

1. (Lattice inclusion.) $p^{U(G)} \mathcal{P}(G) \subseteq \mathcal{S}(G)$ for every block $G = G(a_{\mathrm{top}}, a_+, b)$ as above.
2. (Valuation bound.) For every such block, every level $(j, j_+)$ of $G$, every $z \in \mathcal{S}(G)$ and every monomial $\mu$ of $z$,
$$v_p\bigl(\lambda_{j,j_+} \textstyle\prod_a d_a(L_{j,j_+})!\,(B - j_+)!\bigr) + 2 U(G) \leq v_p(\mu!) + \ell(X).$$

Then the three conclusions of the theorem hold for all $a_{\mathrm{top}}, a_+, b, D$.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.block_valuation_Zp_of_lattice_inclusion`.

*Proof.* Apply the [Theorem (Good pairs in the standard lattice)](/entry/blk-z-gen/) with $U = U(G)$ and $M = M(G)$; its hypotheses are condition 1 and the definition of $M(G)$. It gives the dual pairs with exponent $e = D + 2U + M$ and the rank bound 3. For conclusion 2, the set of levels is not empty (it contains the zero level), so $M$ is attained at some level $(j, j_+)$. Condition 2 at this level gives $M + 2U \leq v_p(\mu!) + \ell(X)$, and adding $D$ gives $e \leq v_p(\mu!) + D + \ell(X)$. $\square$

**Proposition 7.4.6 (The lattice inclusion).** Let $X$ satisfy the hypotheses of the theorem. Assume that every block $G(a_{\mathrm{top}}, a_+, b)$ satisfies two conditions of the lattice level theory for blocks: a joining condition on its ties and a unit condition. Then condition 1 of the previous proposition holds. Both conditions hold for every block, so condition 1 holds for every instance with these hypotheses.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.restLL_of` (also `Formalism.MainNotions.G.SymmetricFormBlocks.restLL_proved`, which supplies the two conditions).

*Proof.* Under the window hypotheses, the degrees of the letters of every kept block, the number $B$ and the shifts are bounded in terms of $a_{\mathrm{big}} = (3s + 2) a$. The lattice level theorem for blocks, applied with the joining and unit conditions and these degree bounds, gives $p^{U(G)} \mathcal{P}(G) \subseteq \mathcal{S}(G)$; the exponent $U(G)$ has one term $\lceil (r + 1) \lambda'(p, a_{\mathrm{big}}, r) \rceil$ for each of the $t + 1$ projections $P_i$ and $P_+$. The two conditions follow from the conditions on a block in Section 3. $\square$

**Proposition 7.4.7 (From the valuation bound).** Let $X$ satisfy the hypotheses of the theorem, and assume condition 2 of the first proposition. Then the conclusions of the theorem hold.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.block_valuation_Zp_of_valuation_bound`.

*Proof.* The rank $r$ of an instance is at least $1$. Apply the [Proposition (From the lattice inclusion and the valuation bound)](/entry/block-valuation-zp-of-lattice-inclusion/), with condition 1 from the [Proposition (The lattice inclusion)](/entry/rest-ll-of/). $\square$

The valuation bound is about all monomials of all elements of $\mathcal{S}(G)$. It reduces to a statement about the monomials of one level at a time.

**Proposition 7.4.8 (From the numeric bound).** Let $X$ satisfy the hypotheses of the theorem. Assume that for every block $G$, every level $(j, j_+)$, every level $(j', j'_+)$ and every monomial $\mu$ whose multidegree is the multidegree of the generators of $\mathcal{S}(G)$ at level $(j', j'_+)$,
$$v_p\bigl(\lambda_{j,j_+} \textstyle\prod_a d_a(L_{j,j_+})!\,(B - j_+)!\bigr) + 2 U(G) \leq v_p(\mu!) + \ell(X).$$
Then the conclusions of the theorem hold.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.block_valuation_Zp_of_numeric_bound`.

*Proof.* Every monomial of an element of $\mathcal{S}(G)$ is a monomial of one of the generators, and the generators of level $(j', j'_+)$ are homogeneous of one multidegree. So the assumption gives condition 2 of the first proposition, and the [Proposition (From the valuation bound)](/entry/block-valuation-zp-of-valuation-bound/) applies. $\square$

*Proof of the theorem.* It remains to prove the numeric bound. Under the window hypotheses the degrees of the block are bounded by multiples of $a$, the number of ties satisfies $0 \leq t \leq s$, and $r \geq 4$. Bound $v_p$ of the factorials $j_i!$, $j_+!$, $z_i!$, $z_+!$, of the binomial coefficients in $\lambda_{j,j_+}$ and of the degree factor by multiples of $\lambda_A$. This bounds the left side by
$$\bigl((2s + 2) r + 3(t + 1)\bigr) L_1 + 2U, \qquad 0 \leq L_1 \leq \lambda_A, \quad U \leq (t + 1)\bigl((r + 1)(\lambda_A + 1) + 1\bigr).$$
The elementary inequality $\bigl((2s + 2) r + 3(t + 1)\bigr) L_1 + 2U \leq 10 (s + 1)(r + 1) \lambda_A + \kappa_0$, valid for $0 \leq t \leq s$, $r \geq 4$, $\lambda_A \geq 1$ and $\kappa_0 \geq 0$, finishes the proof, since $v_p(\mu!) \geq 0$. Then apply the [Proposition (From the numeric bound)](/entry/block-valuation-zp-of-numeric-bound/). $\square$

**Remark 7.4.9 (Formalization).** The blocks `gB`, the set of kept blocks `Kept`, the window hypotheses `HI`, the size function `lgV2` in the exponent `expU`, and the conditions `HypJoin` and `HypU` with their proofs `hypTie_proved` and `hypU_proved` were not unfolded; the proofs of the lattice inclusion and of the numeric bound above give the structure of the Lean proofs (`gB_deg_le`, the level lattice theorem `KP.Top.levelLattice`, `hiFacts`, `val_gen`, and the inequality `loss_num` of [BlockValuationOverZpHolds.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BlockValuationOverZpHolds.lean#L9)) as far as we read them. That inequality has room: its constant $10$ is larger than the argument needs. The independence of the levels from $a_+$ is a definitional equality (`lv_eq`). `block_valuation_Zp_of_valuation_bound` takes $r \geq 1$ from the instance (`X.hm`), not from its own hypotheses; the hypotheses $C_{Yb} \geq 1$, $C_{E1}, C_{E2} \geq 0$ are passed on to `restLL_of`. The theorem is the field `BlockBoundIntegers` of the open conditions.
