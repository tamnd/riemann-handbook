---
id: depth-below-one-of-hodge-tate-chart-form
title: The minor bound LemmaBT from the Hodge-Tate chart bound (restatement)
kind: theorem
decl: GlobalTheory.T.depthBelowOne_of_hodgeTate_chart_form
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.DepthBelowOneOfHodgeTateChartFormStatement
covers: 473
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement. It gives [`PowGerm.lemmaBT_of_hodgeTate_chart`](/entry/lemma-bt-of-hodge-tate-chart/) a name in the namespace `GlobalTheory.T`. The real content is in [`PowGerm.lemmaBT_of_characters`](/entry/lemma-bt-of-characters/), which that theorem applies. The caller is [`LevelPrimePoint.least_value_le`](/entry/least-value-le/), which uses it in step 5 of its proof.

## Statement

`HTFSt p` says the following. Let $T$ be a complete noetherian local domain of characteristic $0$ in which $p$ is not a unit. Let $G$ be a commutative group over $T$ with a uniformisation and a chart by a formal group law $F$ of dimension $d$. Let $C$ be an algebraically closed field of characteristic $0$ with a valuation $v$, ring of integers $O$, and a local map $T \to O$. Then there are characters $u_1, \dots, u_N$ of $F$ over $O$ such that each $c \in O$ with $v(c)^{p-1} \le v(p)$ satisfies $c\, O^d \subseteq \mathrm{span}_O(\mathrm{dl}(u_k))$.

**Theorem.** If `HTFSt p` holds for every prime $p$, then `LemmaBT` holds.

`LemmaBT` gives power data and bounds the valuation $\rho$ of the value of a product of minors of degree $\deg$: $\rho \le \rho_g \deg/(g-1) + n_1 r\Phi/(4g') + 2\deg^2\Phi/g'$.

## Proof

The statement is the same text as the statement of `PowGerm.lemmaBT_of_hodgeTate_chart`. The proof is that theorem. There is no other step.

## In the Lean code

The theorem is in [DepthBelowOneOfHodgeTateChartFormStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthBelowOneOfHodgeTateChartFormStatement.lean#L19). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, and the file sets `maxHeartbeats` to 1000000. `HTFSt` is in [StChartF.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/PlaceDivisors/StChartF.lean#L133) and `LemmaBT` is in [JetsOnCopiesCompatibleFrames.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/JetsOnCopiesCompatibleFrames.lean#L551). We have not unfolded `dl` or `IsCh`.

The name speaks of "depth below one", but we found no notion of depth in `HTFSt` or `LemmaBT`. The bound $v(c)^{p-1} \le v(p)$ has the shape of the bound $p^{1/(p-1)}$ on the cokernel of the Hodge-Tate map of a $p$-divisible group. We have not checked that `HTFSt` is that published theorem.
