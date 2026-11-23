---
id: true-geometry-row-pair-relation-alt-alt-alt
title: The rescaling data of a geometric family exist, second name
kind: theorem
decl: GlobalTheory.T.true_geometry_row_pair_relation_alt_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.DatExistsStatement
covers: 486
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`QuadraticExtensionData.dat_exists`](/entry/dat-exists/), which has the real content. Its only user is [the column side of a geometric family](/entry/col-side-alt/), at step 2 there. Below this theorem are 486 declarations, one more than below the copy.

## Statement

**Theorem.** Let $W$ be a real package with `AllFamilyConditions W`, $u$ a word, and $a$ a geometric family for $W$ and $u$ with `a.Is` and `a.True`. Assume that the top matrix $i_A$ of the geometry of $a$ at the top level $m$ is the identity. Then there is $C \colon \mathbb{N} \to \mathbb{C}$ with $C_j \neq 0$ for $j < m$ such that, for each $t$ and each quadratic extension datum $J$ at $t$ with `J.Reads`, there are $s$, $\zeta$, $\rho$ with `J.Dat C s ζ ρ`.

The objects and the condition `Dat` are explained in [the copy](/entry/dat-exists/).

## Proof

The proof applies `GlobalTheory.Fam.QuadraticExtensionData.dat_exists` to the same arguments. There is nothing else.

## In the Lean code

The theorem is in [DatExistsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DatExistsStatement.lean#L17). Its type is the type of the copy. The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`.

The name differs from `true_geometry_row_pair_relation_alt_alt` only by one `_alt`, but that lemma has a different statement: it gives the $C_j$ and a rational datum for the part of $\xi$ off the twist places, with no $s$, $\zeta$ or $\rho$. The copy calls it as its first step.
