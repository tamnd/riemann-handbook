---
id: strict-henselisation-enlarge-good-at-origin
title: The base can be enlarged until the torsor is good, a second name
kind: theorem
decl: GlobalTheory.T.strictHenselisation_enlarge_good_at_origin
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.StrictHenselisationEnlargeGoodAtOriginStatement
covers: 467
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`enlarge_good`](/entry/enlarge-good/), with the same statement. It is step 1 of [the torsor point over a noetherian normal model](/entry/torsor-point-of-ess-finite-type/): it replaces the noetherian base by a larger one over which the torsor is good.

## Statement

In short: take the data $(A, E_A, Q_A, j_A, \psi_A, D_A)$ of [the torsor point theorem](/entry/torsor-point-of-ess-finite-type/), with $R = (E_A)_{Q_A}$. Then there are data $(A', E_A', Q_A', j_A', \psi_A', D_A')$ of the same kind (but with no map $A' \to T$), with $R' = (E_A')_{Q_A'}$, such that:

- there is a retraction $\rho' \colon R' \to A'$ of $A' \to R'$ with kernel $(X)$;
- the torsor $D_A'$ is good for $\rho'$;
- there are maps $\beta \colon R_K \to R'_K$ and $h \colon D_A \to D_A'$ with $\psi_A' \circ \beta = \psi_A$ and $h$ over $\beta$.

[The entry of the proof](/entry/enlarge-good/) gives the statement in full.

## Proof

The proof applies `GlobalTheory.KeyOriginEnlarge.enlarge_good`. The real content is in [that entry](/entry/enlarge-good/), and below it.

## In the Lean code

The theorem is in [StrictHenselisationEnlargeGoodAtOriginStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/StrictHenselisationEnlargeGoodAtOriginStatement.lean#L9). Its statement is a copy, symbol for symbol, of the statement of `enlarge_good`. The proof is a `first` tactic that applies that theorem in one of three ways. The file imports `Mathlib` twice and raises `maxHeartbeats`.
