---
id: exists-lower-base-of-trait-abelian-part
title: The abelian part of a trait comes from a lower base (statement form)
kind: theorem
decl: GlobalTheory.T.exists_lower_base_of_trait_abelian_part
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsLowerBaseOfTraitAbelianPartStatement
covers: 312
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`exists_lowBase_of_trait`](/entry/exists-low-base-of-trait/), which has the real content. Its one user is [`exists_degFrom_of_trait`](/entry/exists-deg-from-of-trait/), as step 1 of its proof.

## Statement

Let $n \geq 3$ be odd, $V$ a complete discrete valuation ring of characteristic zero, $b \colon \mathbb{Z}[\zeta_n, 1/n] \to V$ a ring map, $P$ a polarised abelian scheme over $V$ of dimension $h$, and $c \colon \mathbb{Z}^r \to P(V)$ an additive map.

**Theorem.** There are a lower base $L$ (`LowBase`, see [`exists_degFrom_of_trait`](/entry/exists-deg-from-of-trait/)) of genus $h$ with abelian scheme $B$ over $W$, a finite injective local extension $f \colon V \to V'$ of the same kind, a local map $\kappa \colon W \to V'$ with $\kappa \circ b_L = f \circ b$, and an isomorphism $e \colon \mathbb{Z}^{r_L} \to \mathbb{Z}^r$, such that $P \otimes_f V'$ and $B \otimes_\kappa V'$ are one abelian scheme $B'$ with the same Mumford bundle, and for each $a$ there is a section of $B'$ that maps to $c(e(a))$ in $P$ and to $c_0(na)$ in $B$.

## Proof

The statement is the same as that of `GlobalTheory.TChart.exists_lowBase_of_trait`, and the proof applies it.

## In the Lean code

The theorem is in [ExistsLowerBaseOfTraitAbelianPartStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLowerBaseOfTraitAbelianPartStatement.lean#L12). The proof is `first | exact @GlobalTheory.TChart.exists_lowBase_of_trait | ...`. The type is copied word for word from [ExistsLowerBaseOfTraitAbelianPart.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLowerBaseOfTraitAbelianPart.lean#L17). The name says "trait", but no trait occurs in the statement: only a discrete valuation ring, a polarised abelian scheme and points on it.
