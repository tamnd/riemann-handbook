---
id: stmt-e-of-last
title: The closed form of the valuation bound, from the plane step
kind: theorem
decl: Formalism.MainNotions.PairMembershipBlocks.stmtE_of_last
module: Formalism.SharpRestriction.GrowthBounds.PlaneCoefficients
covers: 1727
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `ClosedFormOfAdmitted D` from three hypotheses. Two of them are proved elsewhere, so in effect it reduces the statement to the one hypothesis `RestPl`. It builds the membership input `RestMEM` and gives it to [the theorem with the real content](/entry/stmt-e-of-mem/). Its only user is [the version with `RestPl` alone](/entry/stmt-e-of-pl/), which supplies the other two hypotheses. The chain goes up to [`stmtE`](/entry/stmt-e/) and then to [`loc_proved`](/entry/loc-proved/).

## Statement

Let $D$ be a datum of type `D7` (a record with ranks, a host, spaces, rows and words). For real constants $C_\Lambda, C_k, C_{rk}, C_{\deg}$, let $\mathrm{adm}(D; C_\Lambda, C_k, C_{rk}, C_{\deg})$ be the conjunction of 37 named conditions on $D$ (`admitted`). Let $\mathrm{Concl}$ be the statement: there is $C_0 > 0$ such that for each $C \ge C_0$ the bound `aux₃ D C` holds. The bound `aux₃ D C` says that for each prime $p \ge 13$ with an unramified quadratic setting of discrete valuation rings, each orbit and weight datum that meets a list of numerical conditions in terms of $C$, and each $t$ above an explicit bound `tBound`, the lattice property `LPprime` holds. We have not unfolded `UnramifiedQuadraticSetting` or the inner part `LPprimeAt` of `LPprime`.

**Theorem.** Assume:

1. `NoOpStep`: a rule for derivative and multiplication operators acting on plane coefficients `planeCoeff`;
2. `RestPl`: a lower bound on the valuations of the plane coefficients `zPl` along chains of signed data;
3. there is $C_1 > 0$ such that `RestArithStep C CLa` holds for all $C \ge C_1$ and all $C_\Lambda$.

Then for all constants, $\mathrm{adm}(D; \dots)$ implies $\mathrm{Concl}$.

## Proof

The proof is one term. The lemma `restMEM_of_last` builds `RestMEM D` for all four constants, in two parts.

1. `rest5aMono_of_cut` takes `RestPl`, the arithmetic hypothesis and the proved facts `restT`, `restN D`, `restTh`, `restSP`. It gives `Lemma5aMonomial`. Then `lemma5a_of_monomial` turns this into `Lemma5aTheoremII`.
2. `opSteps_of` adds `NoOpStep` to nine proved operator facts (`trDerPl`, `plMul`, `geoTouch` and others). It gives `OpSteps`. Then `restWord_of_steps` gives `RestWord`.

`memCondition_of_theoremII` combines the two parts into `RestMEM`. It takes the maximum of the two thresholds. Then `stmtE_of_mem` gives the conclusion. The rest is bookkeeping.

## In the Lean code

The theorem is in [PlaneCoefficients.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients.lean#L42), and `restMEM_of_last` is at [line 34](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients.lean#L34).

- Hypothesis 1 is proved as `noOpStep` in [Lam1SPderivAndXMulLeAddIndicator.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialSupport/Lam1SPderivAndXMulLeAddIndicator.lean#L38).
- Hypothesis 3 holds with $C_1 = 1$ by `arithCondition_of_one_le` in [FortyEightBoundArith.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients/FortyEightBoundArith.lean#L51). `stmtE_of_pl` passes exactly these two.

Odd points:

- The conclusion does not depend on $D$. `aux₃` ignores its first argument (it is written `_D`) in [TableLineDegreeFive.lean](lean:Formalism/SharpRestriction/GrowthBounds/TableLineDegreeFive.lean#L30). So $D$ enters only through the hypothesis $\mathrm{adm}$.
- `NoOpStep` quantifies over a `D7` that its body does not use ([NoOpStep.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients/NoOpStep.lean#L91)). The theorem `restN` takes an argument $D$, but its statement `RestN` does not mention it.
