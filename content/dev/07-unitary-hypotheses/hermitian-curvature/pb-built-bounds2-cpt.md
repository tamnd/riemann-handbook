---
id: pb-built-bounds2-cpt
title: The built bounds at the infinite places, restated
kind: theorem
decl: Formalism.FourierDecayAlt.Final.pb_builtBounds2Cpt
module: Formalism.HermitianCurvature.JcRadialModuleFormOfParts
covers: 1014
status: drafted
drafted_by: writer@claude
---
This theorem proves the proposition `BuiltBounds2Cpt` with no hypothesis. It is a renaming: its proof is the name of another theorem, and the two theorems below it only pass proofs along. The real content is in [the built bounds from the head formula](/entry/built-bounds-compact-of-head-top/). [The carrier needs](/entry/carrier-needs-from-d/) uses this theorem as the third part of a conjunction. That chain goes up through [the carrier statement](/entry/carrier-p/) to the step [the hypotheses are not empty](/step/nonempty-hyps/).

## Statement

`BuiltBounds2Cpt` is an implication. Its premise is the proposition `ThmPActualCpt`, which we do not unfold here. The conclusion: for each real $C_b$ there are reals $C_c$ and $C_4 \ge 1$ with this property. Let $E$ be a CM number field. For each infinite place $v$ of $E$, let $W_p(v)$ and $W_q(v)$ be finite-dimensional complex inner product spaces. Let $S$ be a setting: an enumeration of the $f$ infinite places of $E$ with complex embeddings, global size data, grids, and data at each place. Let $p$ be data at each place, $f_v$ a function from matrices to maps $W_q(v) \to W_p(v)$ for each place, $\chi \colon \mathbb{R} \to \mathbb{R}$ and $A_0 \in \mathbb{R}$. Suppose that the condition `IsLeadingFormSetting` holds for $C_b, C_c, S, p, f, \chi, A_0$. This is a list of conditions on $E$, $\chi$ and the grids, a lower bound for $A_0$ in terms of $C_c$ and the sizes of $S$, and at each place a match of $p_v$ with $S$ and regularity of $f_v$. Then:

1. at each place, for each $\varepsilon > 0$, each level $i \le r + 1$ and each word, the local Gram matrix is positive semidefinite on each finite set of points (`ThmPPos`);
2. a property `IntAll` holds at each place (not unfolded);
3. there are weights $\Lambda$ such that a norm at level $i$ is at most a factor $\prod_v \Lambda_i(v)^K$ times an average, with probability weights, of norms at level $i - 1$, and $0 \le \Lambda_i(v) \le \mathrm{sz}_i(v)$ (`WaveByPlaces`, `HidaCurvatureBarriers`);
4. there are weights $\Lambda, \Lambda'$ with bounds of the same shape for the off-diagonal blocks and for the top diagonal, and with upper thresholds (`LiftBelowTop`, `LiftTopDiag`, `ThresholdsLift`);
5. a sum form holds with a constant $M \le C_4^{fs} \prod_{s' < s} \mathrm{vol}(s')$ (`SumFormConcrete`).

## Proof

The proof is the term [`built_bounds_compact`](/entry/built-bounds-compact/). That theorem applies [`pb_builtBounds2Cpt_of_mkTop`](/entry/pb-built-bounds2-cpt-of-mk-top/) to `top_truncation_of_averages`, a proof of `MkTop` that applies `CutMK.mkTop_of_avgs` to a right and a left average formula. Then `pb_builtBounds2Cpt_of_mkTop` turns `MkTop` into `HeadTop` by `pb_headTop_of_mkTop`, and gives it to `built_bounds_compact_of_head_top`. The rest is bookkeeping.

## In the Lean code

The theorem is in [JcRadialModuleFormOfParts.lean](lean:Formalism/HermitianCurvature/JcRadialModuleFormOfParts.lean#L24). `BuiltBounds2Cpt` is in [ArchimedeanUniformConstantsCompactSupport.lean](lean:Formalism/HermitianCurvature/ArchimedeanUniformConstantsCompactSupport.lean#L13). The last theorem of the chain is in [BuiltBoundsCompactOfHeadTop.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompactOfHeadTop.lean#L14).

The premise `ThmPActualCpt` stays in the statement. The caller `carrierNeedsFromD` proves it separately, with `actual_compact_theorem`.

The file name says "radial module form of parts", but the file has twenty imports and this one renaming. The setting structure is named `HidaSetting` ([StatementC.lean](lean:Formalism/HermitianCurvature/StatementC.lean#L60)). Its fields do not mention Hida families.
