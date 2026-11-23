---
id: seesaw-level-prime-law-all-tuples
title: The twist place law for all tuples, a second name
kind: theorem
decl: GlobalTheory.T.seesaw_levelPrime_law_all_tuples
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.SeesawLevelPrimeLawAllTuplesStatement
covers: 583
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`lawLevelPrime_all`](/entry/law-level-prime-all/). It is step 1 of [the finite integral laws from pinned level data](/entry/pins-finite-integrals/): from a lattice shape that fits the level data off the twist places, it chooses the twist operators once and gives the law `TLaw` at the twist places for every tuple. The mathematics is in `lawLevelPrime_all` and in the two lemmas that its helper [`exists_choice`](/entry/exists-choice/) calls.

## Statement

**Theorem.** For every datum $D$, `TOfShape D` holds.

`TOfShape D` says: let $c$ be a common datum, $v$ level data with twist places $P_T$, $k$ a nonarchimedean local field and $o$ a lattice shape datum over $k$ with split points $p_i$ ($i \in I$). Assume `c.Is`, `v.Is` and `ShapeOff v o`. Then there are units $\varepsilon_j(i)$ of $\mathcal{O}_k$, operators $\mathrm{op}_j$, reals $r_j(i) > 0$ and integers $e_j(i)$ such that the modified level data $v' = $ `v.withT (o.S ε) op` satisfy `Is`, and `TLaw v' w` holds for each tuple $t$ with decoration $w$ that satisfies `Is`, `WeilOK`, is unramified at $P_T$ (`UnrOn`, `UnrK`) and has $c_T(j) = \prod_i r_j(i)\, \chi(\varpi_i)^{e_j(i)}$. The law and the operators are described in [`lawLevelPrime_all`](/entry/law-level-prime-all/).

## Proof

The proof is one call to `LevPrimeAll.lawLevelPrime_all`. There is no other step.

## In the Lean code

The theorem is at [SeesawLevelPrimeLawAllTuplesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeesawLevelPrimeLawAllTuplesStatement.lean#L6). `TOfShape` is in [VacOfShape.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/VacOfShape.lean#L114).
