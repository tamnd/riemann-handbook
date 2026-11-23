---
id: value-mem-span
title: The value of a cusp form at an extremal vector is a sum of theta series
kind: theorem
decl: GlobalTheory.AdSpan.value_mem_span
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ThetaSpanAndGoodRange
covers: 991
status: drafted
drafted_by: writer@claude
---
This theorem is the analytic step of [`range_thF`](/entry/range-th-f/). It takes an element $T$ of the space $\mathcal{A}_i$ of cusp forms of row $i$ and an extremal vector $u$, and puts the function $T(u)$ on $U(W_i)(\mathbb{A})$ in the span of theta series from the definite space $V_i$. Its proof checks that $T(u)$ is bounded, of the right level and holomorphic up to a factor, and then calls [`span_any`](/entry/span-any/), which does the work.

## Statement

Use the notation of [`range_thF`](/entry/range-th-f/): the record $R$, the spaces $V_i$ and $W_i$, the [[Weil representation|H3Q2703KKV]] $\omega_{i,t}$ and the space $\mathcal{A}_i$ = `R.Wall i σ₀`. For a polynomial $P$ in the Fock variables let $\varphi_P$ = `R.ptP i t P` be the vector `pureTensorO` built from $P$ and the finite vector `R.vP i t`. Let $\Delta_i$ = `RealDat.Delta i`, a fixed polynomial `delta` given by the signature of $W_i$.

Assume `CuspRapidDecay`, `SizeOK D`, `R.toLevCh.Is A.μ0`, `R.IsModels` and `R.IsThP`. Let $u$ be an extremal vector of the model `MW i σ₀` (`IsExtVec`: at each $\rho$, a unit vector in the lowest $K$-type `lowT` with the weight `extWt`). Let $w_0$ satisfy $\iota(\otimes u)(w_0) = \Delta_i$, where $\iota$ = `R.ioP i`. Then for each $T \in \mathcal{A}_i$,

$$T(u) \in \operatorname{span}_{\mathbb{C}} \bigl\{\, g \mapsto \omega_{i,t}(h, g)\varphi_P(0) \;:\; h \in U(V_i)(\mathbb{A}),\ P \in \operatorname{im} \iota(\otimes u) \,\bigr\}.$$

The functions on the right are theta series: $\omega(h, g)\varphi(0)$ is `thetaKO` in the Lean code.

## Proof

Let $\varphi = T(u)$.

1. **Set-up.** $V_i$ is positive definite at the infinite places (`vpos`), so it has an orthogonal frame (`StdFrame.exists_orthFrame`). Its rank $n_V$ is even, $\operatorname{rank} W_i = r$, $r \le n_V$, and `SizeOK` gives $4([E:\mathbb{Q}]\, r) + 4 \le n_V$.
2. **Holomorphy and weights.** `extremalVector_values_lowering_and_torus` shows that the lowering operators kill $\varphi$ (`LowKilled`). It also shows that each element `torAt ρ s` of a torus acts on $\varphi_{\Delta_i}$ and on $\varphi$ (from the right) by the same scalar.
3. **Level.** `levelCharacter_places_odd_and_principal_level` gives the principal level groups. On them `weilFiniteVector_fixed_principalLevel_coeffSpace` fixes `vP`, and the level field of $T$ makes $\varphi$ right invariant.
4. **Automorphy and bound.** $\varphi$ is left invariant under $U(W_i)(\mathbb{Q})$. It is bounded by `CuspDecay.bounded_of_cuspForm`, from `CuspRapidDecay` and the cuspidality of $T(u)$.
5. **Stability.** By the field `ioP` of `IsThP`, $\omega(h, 1)$ for archimedean $h$ maps $\varphi_P$ with $P \in \operatorname{im}\iota(\otimes u)$ to some $\varphi_{P'}$ with $P'$ in the same image.

With these facts, [`span_any`](/entry/span-any/) gives the conclusion. It changes to a standard frame and calls [`span_std`](/entry/span-std/), whose main step is `mem_span_thetaSeries_of_boundedHolomorphic`: a bounded automorphic function of this level that is holomorphic up to a factor lies in the span of these theta series.

## In the Lean code

The theorem is in [ThetaSpanAndGoodRange.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ThetaSpanAndGoodRange.lean#L257). The lemmas it calls:

- `span_any` (line 158), `pureTensorO_one` (line 224), `onBasis_pos` (line 232) and `ranks` (line 241), in the same file.
- `GlobalTheory.T.extremalVector_values_lowering_and_torus`, `GlobalTheory.T.levelCharacter_places_odd_and_principal_level` and `GlobalTheory.T.weilFiniteVector_fixed_principalLevel_coeffSpace`.
- `GlobalTheory.CuspDecay.bounded_of_cuspForm` and `GlobalTheory.MultMem.mem_mult_iff`.

The conclusion is about the value at one vector $u$, not about $T$. The hypothesis on $w_0$ is used only to know that $\Delta_i \in \operatorname{im}\iota(\otimes u)$. `CuspRapidDecay` is used only for boundedness. We have not unfolded `pureTensorO`, `delta` or `LowKilled`.
