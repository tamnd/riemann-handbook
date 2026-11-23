---
id: exists-finite-unramified-representing-polarized-homs
title: Homomorphisms that respect two line bundles form a finite unramified scheme (statement)
kind: theorem
decl: GlobalTheory.T.exists_finite_unramified_representing_polarizedHoms
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFiniteUnramifiedRepresentingPolarizedHomsStatement
covers: 471
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [the finiteness of polarized homomorphisms](/entry/exists-finite-unramified/). Its proof only calls that theorem. [The scheme of adjoint actions](/entry/exists-act-rep-finite/) uses it for maps $A \to A^r$, and keeps only the finiteness.

## Statement

Let $S$ be a locally noetherian scheme and $A$, $B$ abelian schemes over $S$. Let $L$ be a line bundle on $A$ and $M$ one on $B$. Suppose both are rigidified (trivial along the zero section) and relatively ample over $S$ (the Lean predicate `Out.RelAmple`).

For $T \to S$, consider homomorphisms $\Phi \colon A_T \to B_T$ with $\Phi^*M_T \cong L_T$. A *representing object* for them (the Lean structure `HomFixRep A B L M`) is a scheme $\pi \colon H \to S$ with such a homomorphism $\Phi_H \colon A_H \to B_H$, with this property: for each $T \to S$ and each such $\Phi$ on $A_T$, there is a unique $S$-map $h \colon T \to H$ such that identifications $A_T \cong h^*A_H$ and $B_T \cong h^*B_H$ carry $\Phi$ to $h^*\Phi_H$.

**Theorem.** A representing object exists with $\pi$ [[finite|N9C4X7XKE4]] and [[formally unramified|1JQX6HD8E5]].

## Proof

The proof is one tactic line that applies `GlobalTheory.EndLoc.HomFixFinite.exists_finite_unramified`, which has the same type. The content is in [that entry](/entry/exists-finite-unramified/).

## In the Lean code

The theorem is in [ExistsFiniteUnramifiedRepresentingPolarizedHomsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteUnramifiedRepresentingPolarizedHomsStatement.lean#L11). The structure `HomFixRep` is in [NonemptyHomFixRepTrivial.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NonemptyHomFixRepTrivial.lean#L14). Its universal property asks for uniqueness of $h$ only, not of the identifications. "Rigidified" is `Out.Rigidified`: the pullback of the bundle along the zero section has a nowhere vanishing section.
