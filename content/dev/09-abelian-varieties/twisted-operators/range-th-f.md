---
id: range-th-f
title: The theta lift from the definite side onto the cusp forms of each row
kind: theorem
decl: GlobalTheory.AdSpan.range_thF
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ThetaSpanAndGoodRange
covers: 998
status: drafted
drafted_by: writer@claude
---
This theorem says that the [[theta lift|6WB6TKE70H]] `thF` from the definite hermitian space $V_i$ to the space $W_i$ of row $i$ is onto the space of cusp forms of the given type and level on the [[unitary group|0R9R0Y1HDK]] of $W_i$. It has two users in the same file, `spanAt` (the theta translates span this space) and `goodRangeAt`. Their paths meet only at the last node of the trunk, [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/), which is therefore its parent. The work is in [`value_mem_span`](/entry/value-mem-span/).

## Statement

Let $R$ be a record `RealDat D A Ks`. For each row $i < m$ it carries a hermitian space $V_i$ = `Vc D i`, positive definite at the infinite places, a space $W_i$ = `Wc D i` of rank $r$, a [[Weil representation|H3Q2703KKV]] $\omega_{i,t}$ of $U(V_i)(\mathbb{A}) \times U(W_i)(\mathbb{A})$, a model `MW i σ₀` of a discrete series of $U(W_i)$ at the archimedean places, and:

- the space $\mathcal{A}_i$ = `R.Wall i σ₀`: the span of the maps $T$ from the smooth vectors of the model to functions on $U(W_i)(\mathbb{A})$ such that each $T(v)$ is an automorphic [[cusp form|SV5EEBF861]] with level $J$ and character $\chi$, and $T$ is equivariant and continuous (`IsMultMap`);
- a finite-dimensional Hilbert space `HV i t` and a linear map $\theta_{i,t}$ = `R.thF i t` from it to these maps.

Assume:

1. `CuspRapidDecay`: cusp forms decay rapidly in the height. It is a hypothesis named after a published result.
2. `SizeOK D`: $8 f r + 4 \le n_V$, where $n_V = \operatorname{rank} V_i$ and $2f = [E : \mathbb{Q}]$. So $V_i$ is large compared with $W_i$.
3. `R.toLevCh.Is A.μ0`, `R.IsFam`, `R.IsModels` and `R.IsThP`: the record is built as the proof requires.

Then for each $i$ and $t$, $\operatorname{im} \theta_{i,t} = \mathcal{A}_i$.

## Proof

The inclusion $\subseteq$ is the field `thF_mem` of `IsThP`. For $\supseteq$:

1. `IoExtremal.ioExt` (it uses `IsFam`) gives an extremal vector $u$, a unit vector of the lowest $K$-type at each archimedean place, and a vector $w_0$ with `ioP i (⊗u) w₀ = Delta i`.
2. **Evaluation at $u$ is injective on $\mathcal{A}_i$.** `IsModels` gives a Hilbert space `HW` and an injective map $e$ onto $\mathcal{A}_i$. The norm of $y$ is a constant times the number $c$ with $\int_{\mathcal{F}} |e(y)(v)|^2 \, d\nu = c \prod_\rho \|v_\rho\|^2$ for all $v$ (`ipM`, an integral over a fundamental set $\mathcal{F}$). If $e(y)(u) = 0$, take $v = u$: then $c = 0$, so $y = 0$ (`eq_zero_of_value`).
3. **The value at $u$ is a sum of theta series.** For $T \in \mathcal{A}_i$, [`value_mem_span`](/entry/value-mem-span/) puts $T(u)$ in the span of the functions $g \mapsto \omega_{i,t}(h, g)\varphi_P(0)$.
4. **Each such function is a lift.** `thetaSeries_eq_thetaLift_definiteGroup_form` gives $x$ with $\theta_{i,t}(x)(u) = \omega_{i,t}(h, g)\varphi_P(0)$ as functions of $g$.
5. **Linear algebra.** `mem_range_of_value` concludes: $\theta$ maps into $\mathcal{A}_i$, evaluation at $u$ is injective on $\mathcal{A}_i$, and each spanning function is the evaluation of some $\theta(x)$, so $T \in \operatorname{im}\theta$.

## In the Lean code

The theorem is in [ThetaSpanAndGoodRange.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ThetaSpanAndGoodRange.lean#L319). The lemmas it calls: `value_mem_span` (line 257), `eq_zero_of_value` (line 126), `mem_range_of_value` (line 302) and `evAtVec`, all in the same file, with `GlobalTheory.IoExtremal.ioExt` and `GlobalTheory.T.thetaSeries_eq_thetaLift_definiteGroup_form`. The hypothesis `hF` is used only by `ioExt`, and `hP` and `hsz` only by `value_mem_span`. We have not unfolded `IsFam` or the condition `Lift.IsThetaP` that `IsThP` puts on `thF`, so we do not say which theta integral `thF` is.
