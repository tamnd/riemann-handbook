---
id: crystalline-cech-de-rham-relations-total-detect-zero
title: The comparison relations are total and detect zero (statement form)
kind: theorem
decl: GlobalTheory.T.crystallineCechDeRham_relations_total_detect_zero
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CrystallineCechDeRhamRelationsTotalDetectZeroStatement
covers: 329
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`PDForm.rel_total_zero`](/entry/rel-total-zero/), which has the real content. Its one user is [the comparison of crystalline and de Rham cohomology](/entry/crystalline-smooth-lift-of-relations/), which turns the relations into linear isomorphisms.

## Statement

We use the notation of [the comparison theorem](/entry/crystalline-smooth-lift-of-relations/). For each datum $D$ and each lift $\Lambda$ of $D$, and for $q = 1$ and $q = 2$, the relation $\mathrm{Rel}_q \subseteq H^q_{\mathrm{cris}}(D) \times H^q_{\mathrm{dR}}(X)$ of $\Lambda$ has three properties:

1. each $c$ is related to some $h$;
2. each $h$ is related to some $c$;
3. if $c$ is related to $h$, then $c = 0$ if and only if $h = 0$.

## Proof

The proof is the term `GlobalTheory.PDForm.rel_total_zero`.

## In the Lean code

The theorem is in [CrystallineCechDeRhamRelationsTotalDetectZeroStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CrystallineCechDeRhamRelationsTotalDetectZeroStatement.lean#L7). The proof is a `first` tactic whose first branch, `exact @GlobalTheory.PDForm.rel_total_zero`, closes the goal. The statement repeats the type of `rel_total_zero` word for word.
