---
id: special-unitary-fixing-plane-complement-mem-closure
title: Strong approximation for elements that fix the complement of a plane, second name
kind: theorem
decl: GlobalTheory.T.specialUnitary_fixing_plane_complement_mem_closure
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SpecialUnitaryFixingPlaneComplementMemClosureStatement
covers: 307
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`PlaneSU.plane_closure`](/entry/plane-closure/). It has no proof of its own. [Strong approximation for a special unitary group](/entry/strong-approx-su/) passes it as an argument to `T.truncation_specialUnitary_mem_closure_strongApprox`.

## Statement

The statement is the same text as that of [`plane_closure`](/entry/plane-closure/), where it is given in full. In short: let $E/F$ be a CM extension, $J$ a nondegenerate Hermitian matrix with form $h$, and $\varepsilon$ the idempotent adele of a nonempty finite set $S$ of places. Let $e_1, e_2$ be orthogonal vectors with $h(e_1, e_1) \neq 0 \neq h(e_2, e_2)$, such that $-h(e_1, e_1)/h(e_2, e_2)$ is a norm from $E$ at each place of $S$. If $g \in SU(J)(\mathbb{A}_F)$ fixes every rational vector orthogonal to $e_1$ and $e_2$, then $g$ lies in the closure of $SU(J)(F) \cdot SU(F_S)$.

## Proof

The proof is one line: `exact @PlaneSU.plane_closure`, inside a `first` combinator.

## In the Lean code

The theorem is at [SpecialUnitaryFixingPlaneComplementMemClosureStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SpecialUnitaryFixingPlaneComplementMemClosureStatement.lean#L8). The real content is in [`plane_closure`](/entry/plane-closure/).
