---
id: uniformised-semi-abelian-galois-descent
title: Galois descent of a uniformised semi-abelian scheme (statement)
kind: theorem
decl: GlobalTheory.T.uniformised_semiAbelian_galois_descent
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.UniformisedSemiAbelianGaloisDescentStatement
covers: 378
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`Mum.has_of_galois_action`](/entry/has-of-galois-action/), which has the real content. Its proof only calls that theorem. It is used once, in the last step of [`Mum.has_of_hasFin`](/entry/has-of-has-fin/).

## Statement

Let $R$ be a local domain with `Base R` (noetherian, integrally closed, complete, characteristic zero). Let $\rho \colon R \to R'$ be a finite injective map to a local domain $R'$ that is again noetherian, normal and complete (`FinExt ρ`). Suppose that $\rho$ is Galois (`IsGal ρ`): the group $\Gamma$ of ring automorphisms of $R'$ that fix $\rho(R)$ is finite, and its fixed ring is $\rho(R)$.

Let $D$ be degeneration data over $R$, and $D'$ a pullback of $D$ over $R'$. Let $G'$ be a commutative semi-abelian group scheme over $R'$ and $A'$ a polarised abelian variety over the fraction field of $R'$, with a uniformisation $U'$ of $G'$ by $D'$. Suppose that $\Gamma$ acts on $G'$ compatibly with $U'$ (`GalAct`; the [entry for `has_of_galois_action`](/entry/has-of-galois-action/) unfolds it).

**Theorem.** Then `Has D`: degeneration data $D$ come from a semi-abelian scheme over $R$ with a uniformisation.

## Proof

The proof is `Mum.has_of_galois_action`.

## In the Lean code

The theorem is in [UniformisedSemiAbelianGaloisDescentStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformisedSemiAbelianGaloisDescentStatement.lean#L14). The proof is the tactic `first | exact @GlobalTheory.Mum.has_of_galois_action | ...`. The two statements are identical, so `exact` with that theorem closes the goal. The file imports `Mathlib` twice (lines 1 and 3); this has no effect.
