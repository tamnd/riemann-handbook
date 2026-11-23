---
id: qat-of-kill-detect
title: The quotient index bound from a family of functionals that cuts out the kernel
kind: theorem
decl: GlobalTheory.ArcCM.qat_of_kill_detect
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.QuotientBoundOfKillDetectConstantRoom
covers: 811
status: drafted
drafted_by: writer@claude
---
This theorem proves the quotient index bound `QAt` from a family of linear functionals on cusp forms whose common kernel is the subspace $\mathcal{K}$. It reaches [`qAt_run`](/entry/q-at-run/) through its statement form [`quotientBound_of_kill_detect_constantRoom`](/entry/quotient-bound-of-kill-detect-constant-room/). The arithmetic of each functional is in [`numGood_of_famQ`](/entry/num-good-of-fam-q/).

## Statement

Use $K$, $S_\kappa$, $M_\kappa$, $\|F\|_\sigma$, $\mathcal{K}$, $\rho$, $P(C, A)$ and `QAt` from [the entry for `qAt_run`](/entry/q-at-run/). Here $K$ is the field `T.Q.c.F` of the coefficient datum of $T$.

*The family.* Let $K_1 \supseteq K$ be a number field and let $d$ be an arc datum (`ArcDatum`): a model of the moduli space, a formal arc into it over $K_1[[t]]$, a framed point $y_F$ on that arc, a monomial $x^\mu$ in the arc letters and an integer $j_0$. Its functional is $\phi_d(F) = $ `cfOf` $y_F\, \mu\, j_0\, F$, the coefficient of $x^\mu t^{j_0}$ in the expansion of $F$ at $y_F$. The datum is in the family (`FamQ`) if it is standard (`Std`) and has CM input data `CMIn` with the parameters $n = $ `nAt`, $\Lambda = $ `LaAt` and $c_1$.

- `KillQ`: $\phi_d$ vanishes on $\mathcal{K}$ for each $d$ in the family.
- `DetectQ`: if $\phi_d(F) = 0$ for all $d$ in the family, then $F \in \mathcal{K}$.
- `RoomAt` $(C, A)$: $C_{\mathrm{arch}} \le P(C, A)|\kappa|$, $B_{\deg} \le P(C, A)|\kappa|$ and $\log|d_E| + \log n \le P(C, A)$, where $C_{\mathrm{arch}}$ (`CarchAt`) and $B_{\deg}$ (`BdegAt`) are the archimedean and degree constants of [`numGood_of_famQ`](/entry/num-good-of-fam-q/).

**Theorem.** Under the hypotheses listed in [the statement form](/entry/quotient-bound-of-kill-detect-constant-room/), `QAt` holds with $C_c = C_h + 3C_0 + C_d$ and $A_c = \max(A_h, A_0, A_d)$.

## Proof

Fix the hypotheses of `QAt`. Let $A$ be the total weight `absA` of $\kappa$; then $A \le |\kappa|$ (`absA_add_le_size`).

1. `Obound` gives $0 \le \log d_K \le C_h z^{A_h}$, so $C_h \ge 0$.
2. Put $\beta(\lambda) = A \max(v_\lambda(d_E), v_\lambda(n))$ (`beOf`). `beSum_holds` gives that $\beta$ has finite support and $d_K^{-1}\sum_\lambda \beta(\lambda)\ell(\lambda) \le (\log|d_E| + \log n) A$. With `RoomAt` this is at most $C_0 z^{A_0} |\kappa|$.
3. `log₂`: $\log \rho \le \log \dim_K S_\kappa$, since $\rho$ is the rank of a quotient of a lattice in $S_\kappa$.
4. `room_of_bounds` adds the bounds: $P(C_h, A_h)|\kappa| + C_{\mathrm{arch}} + B_{\deg} + \tfrac12 \log \rho \le P(C_c, A_c)|\kappa|$, and the bound of step 2 also holds with $(C_c, A_c)$.
5. For each $F \notin \mathcal{K}$ we need a functional $\phi$ that kills $\mathcal{K}$, has $\phi(F) \neq 0$ and satisfies `NumGood`. Suppose there is none. Let $d$ be in the family. If $\phi_d(F) \ne 0$, then [`cmArcDatumFamily_functional_bounded_linear_on_cuspForms`](/entry/cm-arc-datum-family-functional-bounded-linear-on-cusp-forms/) makes $\phi_d$ a linear map with `NumGood`, and `KillQ` says it kills $\mathcal{K}$: a contradiction. So $\phi_d(F) = 0$ for all $d$, and `DetectQ` gives $F \in \mathcal{K}$, again a contradiction.
6. `qbridge_of_numGood` joins steps 2 to 5 into `QBridgeAt`, and `qat_of_bridge'` turns `QBridgeAt` into `QAt`.

## In the Lean code

The theorem is in [QuotientBoundOfKillDetectConstantRoom.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/QuotientBoundOfKillDetectConstantRoom.lean#L51). `FamQ`, `KillQ`, `DetectQ`, `CarchAt`, `BdegAt` and `RoomAt` are in [CarchAt.lean](lean:Development/AbelianVarietyTheory/Definitions/ArchimedeanThetaValues/CarchAt.lean#L25). The lemmas it calls:

- `room_of_bounds` ([L16](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/QuotientBoundOfKillDetectConstantRoom.lean#L16)), monotonicity of $z^A$ in $A$ for $z \ge 1$, and `log₂` ([L40](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/QuotientBoundOfKillDetectConstantRoom.lean#L40)), from `rank_QuotMW`.
- `beSum_holds`, with `beOf` in [BeSumStatement.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ArchimedeanQuadraticData/FinitePlaceArcs/BeSumStatement.lean#L19).
- `qbridge_of_numGood` in [QbridgeOfNumGood.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/QbridgeOfNumGood.lean#L33) and `qat_of_bridge'` in [QatOfBridgeAlt.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ArchimedeanQuadraticData/QatOfBridgeAlt.lean#L11), which uses `quotLocal_holds` and `lenDescent_holds`. We have not opened their proofs.

Step 5 is a proof by contradiction, so the functional is not built explicitly. The parameter $C_k$ appears only in a hypothesis of `QAt`, which the proof passes on.
