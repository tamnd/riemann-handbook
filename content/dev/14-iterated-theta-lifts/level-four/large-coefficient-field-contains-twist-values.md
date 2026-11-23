---
id: large-coefficient-field-contains-twist-values
title: A large coefficient field contains the twist values and the Hecke eigenvalues
kind: theorem
decl: GlobalTheory.Mem.R3.OkVals.large_coefficientField_contains_twist_values
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.LargeCoefficientFieldContainsTwistValues
covers: 304
status: drafted
drafted_by: writer@claude
---
This theorem says that once the coefficient field $L_B$ of a base contains a certain finite set of algebraic numbers, it holds the values of the twisting characters and the Hecke eigenvalues that the column families need. It is used in the proof of [membership and bundles at the stronger parameters](/entry/member-bundles-large-unramified-exponents-alt/). Below it are 304 declarations of the proof.

## Statement

Let $B$ be a base with frame $f$ and twist datum $T$. Let $I$ be column input data over $B$ that satisfies `I.Ok`, has frame $f$, and whose characters $\xi_a$ form the set $\{1, \delta, \delta'\} \cup \{\xi_T(w)\}$ of twists of $T$.

**Theorem.** Eventually in the context, at all large bases (`EvLg`), the following hold for each such $I$.

1. `ValsIn I`: for each $a$ and each prime $P$ where $\xi_a$ is unramified, the value $\xi_a(P)$ is the image of an element of $L_B$; and for each $a$ and each $P$ in the set $Q_a$, the field $L_B$ has a primitive root of unity of order $N(P)$.
2. For each set $U$ of indices, each finite set $X_g$ of absolutely irreducible characters and each trace datum, the level 3 column family `famC I hX U Xg tr` satisfies `Ok3 1`: the family, its row parts and its lift parts each satisfy their `Ok` condition. We did not unfold these conditions.

## Proof

`exists_algebraicRoots_coeffFieldContainsTwistValues`, a second name of `Col2.exists_roots_valsIn`, gives finite sets $S_v$ of algebraic numbers with this property: if $S_v \subset L_B$, then `ValsIn I` holds. `exists_coefficientField_contains_heckeEigenvalues`, a second name of `HFld.heckeFields`, gives finite sets $S_o$ such that $S_o \subset L_B$ puts the Hecke eigenvalues of the row and lift points in $L_B$. The largeness condition is taken to be $S_v \cup S_o \subset L_B$, with no other condition.

Part 1 is then the property of $S_v$. For part 2, `colFam3_ok` proves `Ok3 1` from the hypothesis `ColHyp3`. Its inputs are: the infinite place of the embedding $L_B \to \mathbb{C}$ satisfies `IsConjAt`, by the star structure of $L_B$ (`isConjAt_embLL`), the characters in $X_g$ are absolutely irreducible, the Hecke operators commute (`heckeOperators_commute` and `rowsLifts_heckeOperators_commute`), and the Hecke eigenvalues lie in $L_B$ (from $S_o$). The rest is bookkeeping.

## In the Lean code

The theorem is in [LargeCoefficientFieldContainsTwistValues.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LargeCoefficientFieldContainsTwistValues.lean#L27). `colFam3_ok` is in [HeckeCSDICommTrRep.lean](lean:Formalism/LocalToGlobal/Divisibility/HeckeCSDICommTrRep.lean#L167).

- "Eventually in the context" is trivial here. The lemma `ev_of_forall` ([line 23](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LargeCoefficientFieldContainsTwistValues.lean#L23)) proves it for every context.
- Of the conditions of `large₂`, only the set $S_2 = S_v \cup S_o$ is used. The sets $S_1$, $P_1$ and $A$ are empty, so the conditions on the places of $T$ are empty.
- The hypotheses `I.C = f` and the equation for the range of $\xi$ serve only to rewrite $S_v \cup S_o$ in terms of $B$.
