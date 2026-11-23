---
id: block-valuation-over-zp-holds
title: Dual families in a block lattice over the p-adic integers
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.block_valuation_over_Zp_holds
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.BlockValuationOverZpHolds
covers: 330
status: drafted
drafted_by: writer@claude
---
This theorem proves `BlockBoundIntegers` for each instance $X$ that satisfies `HI`. [`openE_of_open4`](/entry/open-e-of-open4/) uses it to get the bound `BlockBoundUniformiser`. The theorem itself is a short chain: it gives a numeric valuation bound to [`block_valuation_Zp_of_numeric_bound`](/entry/block-valuation-zp-of-numeric-bound/). The new work in this file is the proof of that numeric bound. Below it are 330 declarations.

## Statement

Instances $X$, the window $A$, $s$, $r$, $a$ and the number $t$ of ties are as in [`openE_of_open4`](/entry/open-e-of-open4/). For a top $a_\bullet$, a value $a_+$ and a kept block $b$, `gB` gives block data $G$. Its lattice `SSZ` is the $\mathbb{Z}_p$-span of the generators `gens` of all levels $(j, j_+)$ with `LevelOK`. The Fock pairing is $\langle F, G \rangle = \sum_m F_m G_m \prod_k m_k!$ (`fockK`). The loss is
$$\mathrm{Loss} = 10(s+1)(r+1)\lambda + \kappa_0, \qquad \lambda = \log_p(8a+r) + 1,$$
with $\kappa_0$ = `kappaZeroExponent` $\ge 0$.

**Theorem.** Let $C_{Yb} \ge 1$, $C_{E1}, C_{E2} \ge 0$, and let $X$ satisfy `HI`. Then for each $a_\bullet$, $a_+$, kept $b$ and integer $D \ge 0$, there are $n$, elements $x_1, \dots, x_n, y_1, \dots, y_n$ of `SSZ` and $e \in \mathbb{Z}$ with:

- $\langle x_i, y_j \rangle = p^e \delta_{ij}$;
- $e \le v_p(\prod_k \mu_k!) + D + \mathrm{Loss}$ for each monomial $\mu$ of each element of `SSZ`;
- $\sum_\ell \operatorname{rk} L_\ell \le n + \mathrm{badness}(D)$, a sum over the levels $\ell$ of the block.

## Proof

The file proves `RestValNum` (`restValNum_proved`). Fix $a_\bullet$, $a_+$, $b$, a level $\ell$, a second level $(j', j'_+)$ and a monomial $\mu$ whose weights are those of $(j', j'_+)$. Put $A = (3s+2)a$ (`aBig`).

1. `gB_deg_le` bounds the degrees of $G$ by $2A$. Then `val_gen` gives $v_p(\mathrm{lvC} \cdot \mathrm{degFact}) \le v_p(\prod_k \mu_k!) + ((2s+2)r + 3(t+1))\, L_1$ with $L_1 = \lfloor \log_p(8A+r) \rfloor$.
2. `hiFacts` gives $r \ge 4$, $2s+2 \le r$, $(r+1)^2 \le p$ and $a \ge 1$. So $3s+2 \le p$ and $p \ge 25$.
3. Since $8A + r \le (3s+2)(8a+r)$ and $\log_p(3s+2) \le 1$, we get $L_1 \le \lambda$ and $\lambda \ge 1$.
4. The exponent $U$ = `expU` is $(t+1)\lceil (r+1)(\log_p(8A+r)+1) \rceil$. So $U \le (t+1)((r+1)(\lambda+1)+1)$.
5. `loss_num`: if $0 \le t \le s$, $r \ge 4$, $\lambda \ge 1$, $0 \le L_1 \le \lambda$, $U$ is as in step 4 and $\kappa_0 \ge 0$, then
$$((2s+2)r + 3(t+1)) L_1 + 2U \le 10(s+1)(r+1)\lambda + \kappa_0.$$
The left side is at most $((2s+2)r + 3(s+1))\lambda + 2(s+1)(2r+3)\lambda = (s+1)(6r+9)\lambda$, because $(r+1)(\lambda+1)+1 \le (2r+3)\lambda$ when $\lambda \ge 1$.

Steps 1 and 5 give $v_p(\mathrm{lvC} \cdot \mathrm{degFact}) + 2U \le v_p(\prod_k \mu_k!) + \mathrm{Loss}$. This is `RestValNum`.

## In the Lean code

The theorem is in [BlockValuationOverZpHolds.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BlockValuationOverZpHolds.lean#L115), with `loss_num` at line 9 and `restValNum_proved` at line 31. `BlockBoundIntegers` and `levelPassageLoss` are in [BlockBoundUniformiser.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BlockBoundUniformiser.lean#L107). `SSZ` is in [WithMargin.lean](lean:Formalism/MahlerMeasure/WithMargin.lean#L66), and `HIFacts` is in [CountingStatementReduction.lean](lean:Formalism/SharpRestriction/GrowthBounds/CountingStatementReduction.lean#L1620).

The constant 10 has slack: the proof needs only $6r + 9 \le 10(r+1)$. The parameter $r$ is `X.L.m` (an `abbrev` in [FlipOneThree.lean](lean:Formalism/SharpRestriction/GrowthBounds/FlipOneThree.lean#L59)). We have not unfolded `lvC`, `gB` or `kappaZeroExponent` beyond $\kappa_0 \ge 0$.
