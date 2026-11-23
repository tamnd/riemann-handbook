---
id: good-vectors-definite
title: Free counts and a large good share on the definite space
kind: theorem
decl: GlobalTheory.DefFree.goodVectorsDefinite
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.IsNilpotentSubOneOfFullBlockUnipotent
covers: 346
status: drafted
drafted_by: writer@claude
---
This theorem counts multiplicity spaces on the last weight space $W_{m-1}$, which is positive definite. It shows that the level group acts freely and that the good vectors fill almost all of the space at each level. It is one of the inputs of [the bundles with large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/). Its only hypothesis is `GreenCuspidal`, a published input. The general setting is in [the unitary hypotheses](/proof/unitary-hypotheses/).

## Statement

`GoodVectorsDefinite` is `DefiniteFree ∧ DefiniteGoodShare`. Both quantify over a datum $D$, size data $L$ with a parameter choice, a family $A$, real data $R$ and a face $F$ that form a `HidaSetting` (seven fields: levels, group, family, models, chain, theta, scalars), and the last index $i$ with $i + 1 = m$.

- `DefiniteFree`: `PrincipalCount R i` holds. The classes are finite and nonempty, every arithmetic group $\Gamma_c$ is trivial, and $d_K = \#\mathrm{Cls} \cdot \dim \rho \ge 1$. For each level $b$, the level group $P_b$ acts freely: the reduction map is onto $P_b$, and an element that fixes a class has trivial reduction. The representation on the multiplicity space is free over $\mathbb{C}[P_b]$, and $\#P_b \cdot d_0 = d_K$ with $d_0 \ge 1$.
- `DefiniteGoodShare`: for each $\varepsilon > 0$ there is $x_0$ such that, when $L$ has exponent $\varepsilon$ and size $x \ge x_0$, we have $(1 - \delta) d_0 \le d_{\mathrm{good}}$ and $(1 - \delta) d_0 > 0$, with $\delta = \exp(-x^{e_z/7})$.

Here $d_0$ is the dimension of all multiplicity vectors at level $b$, and $d_{\mathrm{good}}$ is the dimension of the good part $R.\mathrm{Wat}$.

## Proof

Free part (`definiteFree`). The prime choice gives $g_k > [E:\mathbb{Q}]\, r + 1$ at each type prime. An element of the definite group that fixes a class has finite order (`isOfFinOrder_of_conj_mem_selfDualLatticeStabilizer`). If its reduction at a place of this large residue characteristic is unipotent, it is $1$ (`eq_one_of_unipotent`). So each $\Gamma_c$ is trivial (`gam_last`). When all $\Gamma_c$ are trivial, the space of algebraic modular forms has dimension $\#\mathrm{Cls} \cdot \dim \rho$, as in Gross, "Algebraic modular forms", Israel J. Math. 113 (1999). The Lean proof is `principal_count`, which also shows that an element moving every class has trace $0$. Trace $0$ off the identity gives a free $\mathbb{C}[P_b]$-module (`free_monoidAlgebra_of_character_vanishes_off_one`).

Share part (`definiteGoodShare`). Take a generic series $\tau$ with squarefree labels (`exists_genericSeries_squarefreeLabels`, from `GreenCuspidal`). The idempotent $e_0$ splits as a tensor product of two good idempotents, which is a central idempotent $c$ (`coeff_e0_eq_eGood_mul_eGood`, `central_tens2`). The good space is the image of $c$. The trace vanishing gives a count condition (`countAt_of_trace_eq_zero`). The bound `badShare_win` then gives $\delta$, and the size record turns it into the stated form. The rest is bookkeeping.

## In the Lean code

The theorem is on [line 436 of IsNilpotentSubOneOfFullBlockUnipotent.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/IsNilpotentSubOneOfFullBlockUnipotent.lean#L436). The definitions are in [DefiniteIndexDimensionCounts.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/DefiniteIndexDimensionCounts.lean#L101). The lemmas:

- `definiteFree` (line 359), `definiteGoodShare` (line 366).
- `principal_last` (line 229), `free_last` (line 335), `principal_count` (line 124).
- `UpperTheory.Win.badShare_win` in BadShareWin.lean. We have not unfolded its proof.

Odd points. For $\varepsilon > 1$ the share part is vacuous: the proof takes $x_0 = 0$ and gets a contradiction from `L.sc.eps_lt` (lines 368 to 370). The module is named after the helper `isNilpotent_sub_one_of_full_block_unipotent` (line 74), not after this theorem. The free part needs no hypothesis.
