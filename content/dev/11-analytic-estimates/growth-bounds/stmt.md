---
id: stmt
title: The plane Gram estimate at a local ring, with the constants 2, 24 and 60
kind: theorem
decl: Formalism.MainNotions.PlaneGram.stmt
module: Formalism.SharpRestriction.GrowthBounds.MonomialOrderSegments
covers: 542
status: drafted
drafted_by: writer@claude
---
This theorem proves the projection derivative estimate at every local ring that satisfies the six conditions `AdmAt`, for every $C_H \ge 26$, with the constants $C_E = 2$, $C_6 = 24$, $C_{18} = 60$. It gets five local lemmas from `AdmAt` and gives them to [the plane Gram theorem of five lemmas](/entry/plane-gram-theorem-of-five-lemmas/), which has the real content. The chain goes up to [LinkG with five inputs](/entry/link-g-concrete5/).

## Statement

Let $D$ be a datum of type `D7` and let $C_H \ge 26$.

**Theorem.** `Stmt D CH 2 24 60` holds. That is: for each $p$ and each discrete valuation ring $O$ of characteristic $0$ with `HidaSetting p O` and `AdmAt p O`, the estimate `ProjectionDerivativeEstimate p O CH 2 24 60` holds.

`HidaSetting p O` asks for a `UniformizedDVR` structure and an `AdmissibleDVR` for some $n'$. `ProjectionDerivativeEstimate` says: for signed chain data with `Hyp CH` and $4(D_m + D_l + 3k_p) < c$, and each plane polynomial $F$ with `XX` and $v_{BB}(F) = 0$, there are $G$ and $R$ with these properties:

- $G$ is integral and satisfies `YY 24 60`;
- the coefficients of $R$ have valuation at least $c - E$, where $E = D_m + D_l + 2k_p$;
- `ph` sends every monomial of $G$ and $R$ into the degree `d`;
- $v_{BB}(\mathrm{ph}(G + R)) \ge n_0 - k_p$;
- $v(B(F, \mathrm{ph}(G + R))) \le E + 2k_p + n_0 - k_p$.

Here $B(F, H) = \langle F, \gamma H\rangle$ is the Fock pairing twisted by $\gamma$, and $n_0 = v_p(\prod d!)/2$.

## Proof

The proof unpacks `HidaSetting` into $S$ and the admissibility `hG`, and drops the first part of `AdmAt`. It then builds the five lemmas from the other five parts:

- `V2` from `ValuationStabilityAtRing`, by `second_valuation_of_admitted`;
- `SPAN` from `PolynomialSpanAtRing`, by `brSPAN`;
- `PROJ` with $C_0 = 1$ from `FockProjectorAtRing`, by `brPROJ`;
- `DIG` from `FactorialDigitSplitAtRing`, by `brDIG`, which also uses $D$ and `hG`;
- `DER` from `DerivativeCongruenceAtRing`, by `brDER`.

`plane_gram_theorem_of_five_lemmas` turns these into `LiftBoundUniform` with $C_0 = 1$, which has the constants $13, 12, 30, 2$. Then `plane_gram_of_theorem_at` turns it into the estimate with $C_H \ge 26$ and the constants $2, 24, 60$. We have not unfolded this last step.

## In the Lean code

The theorem is in [MonomialOrderSegments.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialOrderSegments.lean#L14). `Stmt`, `AdmAt` and `ProjectionDerivativeEstimate` are in [Lemma5aAt.lean](lean:Formalism/SharpRestriction/GrowthBounds/Lemma5aAt.lean#L316). `plane_gram_of_theorem_at` is in [BrData.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialOrderSegments/BrData.lean#L723) and `brDIG` is in [UnitLevelOne.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialOrderSegments/UnitLevelOne.lean#L42).

The users are `stmtE`, `stmtEF` and `stmtEDF` in the same file, and `plane_gram_of_admitted` in [Closed.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/Closed.lean#L34), an input of [`stmtE_of_OpNS`](/entry/stmt-e-of-op-ns/).

Some points to note:

- The name `stmt` does not say what the theorem is.
- `Stmt` names its first argument `_D` and does not use it. In the proof, $D$ is used only by `brDIG`, through `lemma_five_two_first_holds D`.
- The first part of `AdmAt`, `IsotypicValuationAtRing`, is not used.
- The last bound is written $E + 2k_p + n_0 - k_p$, which is $E + k_p + n_0$.
- `PlaneGramData.ClosedFormOfAdmitted` names its first constant `FormalChartAtZero`. It is a different definition from `tableLineDegreeFive.ClosedFormOfAdmitted`, the target of [`stmtE_of_OpNS`](/entry/stmt-e-of-op-ns/).
