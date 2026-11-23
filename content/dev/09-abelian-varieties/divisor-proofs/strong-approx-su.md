---
id: strong-approx-su
title: Strong approximation for a special unitary group
kind: theorem
decl: GlobalTheory.StrongApproxSUProof.strongApproxSU
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ImportsTailTer
covers: 523
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `StrongApproxSU`. The entry [strong approximation from the literature](/entry/strong-approx-su-of-literature/) of Volume 8 returns it with no change, and from there it fills a field of the bundles of cited results. The proof chains three closure statements. The real work is in the third, which uses [the case of a plane](/entry/special-unitary-fixing-plane-complement-mem-closure/).

## Statement

Let $E/F$ be a CM extension with complex conjugation $\sigma$, and $J$ a nondegenerate Hermitian matrix of size $M \geq 2$ over $E$. Let $SU(J)(\mathbb{A}_F)$ be the matrices of determinant $1$ in the unitary group of $J$ over $\mathbb{A}_F \otimes_F E$, and $SU(J)(F)$ its rational points. Let $S = S_1 \cup S_2$ be a finite set of infinite and finite places, $\varepsilon \in \mathbb{A}_F$ the idempotent that is $1$ at $S$ and $0$ elsewhere, and $SU(F_S)$ the set of $g$ with $\varepsilon(g - 1) = g - 1$.

**Theorem.** If $SU(F_S)$ is not compact, then $SU(J)(F) \cdot SU(F_S)$ is dense in $SU(J)(\mathbb{A}_F)$.

The parent entry states this in more detail. It has the form of strong approximation for a simply connected group (Platonov and Rapinchuk, Algebraic Groups and Number Theory, chapter 7).

## Proof

Let $g \in SU(J)(\mathbb{A}_F)$. For a finite set $T$ of places with idempotent $\eta$, let $SU(F_T)$ be as above.

1. `T.mem_closure_specialUnitarySupportedAtPlaces`: $g$ lies in the closure of the union of the $SU(F_T)$ over all finite $T$.
2. `T.mem_closure_rational_points_unitary_group`: each $h \in SU(F_T)$ lies in the closure of the set of $1 + \eta(\gamma - 1)$ for $\gamma \in SU(J)(F)$. This is weak approximation at the places of $T$.
3. `T.truncation_specialUnitary_mem_closure_strongApprox`: each $1 + \eta(\gamma - 1)$ with $\gamma$ rational lies in the closure of $SU(J)(F) \cdot SU(F_S)$. It takes two inputs: [the case of a plane](/entry/special-unitary-fixing-plane-complement-mem-closure/), for elements that fix the orthogonal complement of an anisotropic plane, and `T.exists_isotropic_places_alt`, which finds such planes with a norm condition at a nonempty subset of $S$.

Two applications of `closure_minimal` join the three steps: closure of closure is closure.

## In the Lean code

The theorem is at [ImportsTailTer.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ImportsTailTer.lean#L14). The statement `StrongApproxSU` is at [NotIsCompactUnivFv.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/NotIsCompactUnivFv.lean#L33).

The four `T.` lemmas are second names: of `SUTrunc.mem_closure_supp`, `SUWeakApprox.weak_approx_SU`, `SUAssemble.assemble` and `PlaceIso.exists_isotropic_places`. We read their statements, not the proofs of the original lemmas. The hypotheses $M \geq 2$ and non-compactness go only to `T.exists_isotropic_places_alt`.
