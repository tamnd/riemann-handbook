---
id: normalised-kernel-expansion-sum-level-invariant
title: The pairing of points is invariant under the level groups, second name
kind: theorem
decl: GlobalTheory.T.normalisedKernelExpansionSum_levelInvariant
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.NormalisedKernelExpansionSumLevelInvariantStatement
covers: 618
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`levels_invariant`](/entry/levels-invariant/). Its one user is [`twisted_pairing_identity`](/entry/twisted-pairing-identity/), which needs the pairing of points to be invariant under the level groups before it can fold a period into a finite sum over classes.

## Statement

The statement is that of [`levels_invariant`](/entry/levels-invariant/): the pairing of points $P_\tau(x, y)$ (`pairPts`) of an expansion $\tau$ at a coset family $\beta$ in the support does not change when one point moves by its level group, at the inner top vertices, at the base point (if $\Psi$ is right $K^+$-invariant), at the inner row vertices, and at the last vertex.

The arithmetic hypotheses are these:

- the level condition $L.\mathrm{Is}(\mu_0)$;
- $p_{de}$ and $p'_{de}$ are prime to $Q_S\, q$;
- the absolute norm of the ideal $\mathfrak{c}_K$ is in no prime of the finite set $L.Q(t)$.

## Proof

The proof applies `GlobalTheory.ExpansionInvariance.levels_invariant`. The statement is the same.

## In the Lean code

The theorem is in [NormalisedKernelExpansionSumLevelInvariantStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/NormalisedKernelExpansionSumLevelInvariantStatement.lean#L9). The proof is the tactic `first | exact @GlobalTheory.ExpansionInvariance.levels_invariant | ...`.

- The name speaks of a normalised kernel expansion sum. The statement is about `pairPts`, with no normalisation.
- There is no clause for the row vertex $0$. The user `twisted_pairing_identity` gets that case from `first_row_invariant_under_twist`.
- The user passes `Set.mem_univ t` for the hypothesis $t \in U$.
