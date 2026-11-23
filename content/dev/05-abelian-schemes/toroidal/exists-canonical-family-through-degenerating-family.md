---
id: exists-canonical-family-through-degenerating-family
title: A canonical family through each degenerating family (statement form)
kind: theorem
decl: GlobalTheory.T.exists_canonical_family_through_degenerating_family
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsCanonicalFamilyThroughDegeneratingFamilyStatement
covers: 609
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`exists_canon_through`](/entry/exists-canon-through/), which has the real content and defines the objects below. Its one user is [`exists_taut_through`](/entry/exists-taut-through/), which uses it as the first step: it gets a chart family, then makes it rigid and maps it to the compactification.

## Statement

Use the moduli scheme $X^\circ_F$, the fan function $\varphi$, monomial families and admissible bases as in [`exists_taut_through`](/entry/exists-taut-through/), and the predicates `Canon` and `Through` as in [`exists_canon_through`](/entry/exists-canon-through/).

**Theorem.** Let $V$ be an admissible base with algebraically closed residue field, and $C$ a monomial family over $V$ with nonzero character group. Then there are a field $k$, integers $m, e$, a monomial family $C_1$ over $R = k[[s_1, \dots, s_m, u_1, \dots, u_e]]$ and a ring map $\theta \colon R \to V$ such that $C_1$ has a canonical structure, the parameters of $C_1$ are $s_1, \dots, s_m$, $\theta$ is local, and $C$ is the pullback of $C_1$ along $\theta$ in the sense of `Through`.

The statement has no hypothesis on the signature, on $\varphi$ or on a compactification.

## Proof

The statement is the same as that of `GlobalTheory.UCanon.exists_canon_through`, and the proof applies it.

## In the Lean code

The theorem is in [ExistsCanonicalFamilyThroughDegeneratingFamilyStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCanonicalFamilyThroughDegeneratingFamilyStatement.lean#L10). The proof is `first | exact @GlobalTheory.UCanon.exists_canon_through | ...`, a tactic that tries the alias in three forms. The type is copied word for word from the theorem it calls.
