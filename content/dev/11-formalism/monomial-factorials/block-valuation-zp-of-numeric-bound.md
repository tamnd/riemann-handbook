---
id: block-valuation-zp-of-numeric-bound
title: Dual families from a numeric valuation bound
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.block_valuation_Zp_of_numeric_bound
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.BlockValuationZpOfNumericBound
covers: 304
status: drafted
drafted_by: writer@claude
---
This theorem gives `BlockBoundIntegers` from `HI` and the numeric bound `RestValNum`. It changes the form of the valuation hypothesis and calls `block_valuation_Zp_of_valuation_bound`. [`block_valuation_over_Zp_holds`](/entry/block-valuation-over-zp-holds/) proves `RestValNum` and calls this theorem. Below it are 304 declarations.

## Statement

The notation is as in [`block_valuation_over_Zp_holds`](/entry/block-valuation-over-zp-holds/). `RestVal` and `RestValNum` both ask for
$$v_p(\mathrm{lvC}_\ell \cdot \mathrm{degFact}_\ell) + 2U \le v_p\Bigl(\prod_k \mu_k!\Bigr) + \mathrm{Loss}$$
for each top, $a_+$, kept block and level $\ell$. They differ in the range of $\mu$:

- `RestVal`: $\mu$ is a monomial of some element of the lattice `SSZ`.
- `RestValNum`: $\mu$ is any monomial whose weights `wL` are equal to `dLvl` of some level $(j', j'_+)$ with `LevelOK`.

**Theorem.** Let $C_{Yb} \ge 1$, $C_{E1}, C_{E2} \ge 0$, and let $X$ satisfy `HI` and `RestValNum`. Then `BlockBoundIntegers` holds for $X$.

## Proof

1. `restVal_of_num` turns `RestValNum` into `RestVal`. By `SSZ_support`, each monomial of an element of `SSZ` has the weights of some level with `LevelOK`.
2. `block_valuation_Zp_of_valuation_bound` gives `BlockBoundIntegers` from `HI` and `RestVal`. It uses `restLL_proved` ($p^U x \in$ `SSZ` for $x$ in a second lattice `PSZ`) and then `block_valuation_Zp_of_lattice_inclusion`.

## In the Lean code

The theorem is in [BlockValuationZpOfNumericBound.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BlockValuationZpOfNumericBound.lean#L31), with `RestValNum` at line 13 and `restVal_of_num` at line 26. `RestVal` is in [BlockValuationZpOfLatticeInclusion.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BlockValuationZpOfLatticeInclusion.lean#L44), and `SSZ_support` is in [SLetCastSucc.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/SLetCastSucc.lean#L133).

The proof passes `hCYb`, `hCE1`, `hCE2` and `hH` to the next lemma without change. `RestValNum` is stronger than `RestVal`: it asks for the bound at all monomials of the right weights, not only at monomials that occur in `SSZ`. We have not unfolded `PSZ` or `block_valuation_Zp_of_lattice_inclusion`.
