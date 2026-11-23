---
id: degenerating-family-data-from-base-alg-closed-residue
title: A degenerating family comes from a lower base (statement form)
kind: theorem
decl: GlobalTheory.T.degeneratingFamily_data_from_base_algClosed_residue
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.DegeneratingFamilyDataFromBaseAlgClosedResidueStatement
covers: 444
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`VData.exists_divFrom`](/entry/exists-div-from/), which has the real content. Its one user is [`exists_canon_through`](/entry/exists-canon-through/), as its first step.

## Statement

Use monomial families and admissible bases as in [`exists_taut_through`](/entry/exists-taut-through/), and lower bases and `DivFrom` as in [`exists_canon_through`](/entry/exists-canon-through/).

**Theorem.** Let $V$ be an admissible base with algebraically closed residue field, and $C$ a monomial family over $V$ with parameters $s_1, \dots, s_m$, forms $\delta_1, \dots, \delta_m$ and character group $X_C \neq 0$ of rank $r$ over $\mathcal{O}_E$. Then there are a datum $D'$ of signature $(p - r, q - r)$, a lower base $L$ for $D'$ with ring $W$, a local map $\theta_0 \colon W \to V$ over $F$, a $\mathbb{Z}$-basis $(\varepsilon_k)$ of the balanced forms on $X_L$ indexed by $m + N$ letters, an isomorphism $e \colon X_C \to X_L$ with $e^*\varepsilon_i = \delta_i$ for $i \leq m$, and elements $t_1, \dots, t_{m+N}$ of $V$ such that $t_i$ is associate to $s_i$ for $i \leq m$, the other $t_k$ are units, and `DivFrom L C θ₀ t ε e` holds.

## Proof

The statement is the same as that of `GlobalTheory.VData.exists_divFrom`, and the proof applies it.

## In the Lean code

The theorem is in [DegeneratingFamilyDataFromBaseAlgClosedResidueStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegeneratingFamilyDataFromBaseAlgClosedResidueStatement.lean#L10). The proof is `first | exact @GlobalTheory.VData.exists_divFrom | ...`, a tactic that tries the alias in three forms. The type is copied word for word from the theorem it calls.
