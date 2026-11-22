---
id: slope-sub-cost-le-comp-vol-slope
title: The slope of a tower, less a cost at the bad primes, is at most the volume slope
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Plug.SlopeVolM.slope_sub_cost_le_compVolSlope
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.UniformAllNormHeightBound
covers: 1111
status: drafted
drafted_by: writer@claude
---
This lemma compares two slopes of one component. The first is the slope of a root tower, an intersection number divided by a volume. The second is the volume slope, read from the growth of the number of small sections. The first, less a cost at the bad primes, is at most the second. Through two renamings, [`Relay.uniform_all_norm_height_bound`](/entry/relay-uniform-all-norm-height-bound/) and [`T.uniform_all_norm_height_bound`](/entry/t-uniform-all-norm-height-bound/), it goes to [`top_meanAll`](/entry/top-mean-all/), which takes the mean over the components. It is the inequality of Step 5 of [the Weil bound chapter](/proof/weil-bound/).

## Statement

Let $E$ be a CM field, Galois over $\mathbb{Q}$, with a host, a datum, a level $l$, a moduli space and coefficients with number field $F$. For each $\sigma\colon F \to \mathbb{C}$ fix an unfolding $U_\sigma$, with a generic frame and component rules that satisfy `CompLaws` and `Ref.UnifAll`. Suppose that $\|\tau(\xi_0)\| = x$ for each good $\sigma$ and each $\tau$. Let $T$ be a root tower with a good origin, matched to the components by $\kappa$, and $II$ a full intersection system. Suppose that $T$ is proportional and satisfies `T1` (nef and semipositive near $0$, with two limits of degrees). Let $Z$ be a component, $u$ a weight with strictly decreasing rows that is regular with gap $g > 0$ (`WeightHyp`), and $B \ge B_0(u,g) = 4\,|\Psi|\,N^2(1 + \|u\|/g)$.

Assume `NefRR` (asymptotic Riemann-Roch for the chart lattices), `Top.Given` ([the inputs](/entry/given-of-inputs/)) and `BirationalPullbackPushforwardFormula`. Then
$$\mathrm{slope}_T(\lfloor B \rfloor, \kappa Z, u) - 2\,\mathrm{cost}(l,B)\,\|u\|_1 \le \mu_{\mathrm{vol}}(Z,u).$$

Here:

- $\mathrm{slope}_T$ is the intersection number `PPc` of the $(D+1)$-th power of the line bundle of $u$, divided by $(D+1)\,\mathrm{vol}(\kappa Z)\,\deg_{\mathrm{flag}}(u)$. We have not unfolded `PPc`.
- $\|u\|_1 = \sum |u_{\tau,i}|$, and $\mathrm{cost}(l,B) = \sum_{p \in S} e_2(p) \log p$. The set $S$ has the primes $p \le B$ and $p \mid 2\,|d_E|\,M'_l$. Also $e_2(p) = \frac{1}{p-1} + \frac{40\,v_p(d_E)}{[E:\mathbb{Q}]}$, plus $1$ when $p = 2$.
- $\mu_{\mathrm{vol}} = \inf_t \bigl(\mathrm{vol}(t)/\delta - t\bigr)$, with $\delta$ the top degree. Here $\mathrm{vol}(t) = \limsup_k D!\,\log N(8k) / ([F:\mathbb{Q}]\,(8k)^{D+1})$, and $N(\tau)$ counts the sections of weight $\tau u$, integral for the mixed valuations, with norm at most $e^{\tau t}$ at each frame.

## Proof

1. `uniform_norm_degree_bound` gives $\delta = \mathrm{vol}(\kappa Z)\,\deg_{\mathrm{flag}}(u) > 0$. It uses `NefRR`.
2. `generic_frame_component_bound` gives $k_0$ with $8 \mid k_0$, $R_0 > 0$, and $d$ small model sections $f_i$ of weight $k_0 u$ with a nondegenerate trace pairing.
3. By `le_compVolSlope_iff`, it is enough to show $\delta(s + t - \varepsilon) \le \mathrm{vol}(t)$ for all $t$ and $\varepsilon > 0$, with $s$ the left side.
4. `full_intersection_weight_bound` at $t' = t - 2\,\mathrm{cost}\,\|u\|_1 - \varepsilon$ bounds $\delta(\mathrm{slope} + t')$ by the volume of model sections of norm at most $e^{\tau t'}$. It uses `BirationalPullbackPushforwardFormula`.
5. `modelSmall_encard_le` maps a model section $s$ to the traces of $s f_i$, times $\prod_{p \in S} p^{\lceil 2 e_2(p)\|\tau u\|_1 \rceil}$, which clears the denominators at $S$. The map is injective. So for large $\tau$ the count is at most $N(\tau + k_0)^d$, because $\tau\varepsilon$ absorbs the constants.
6. `count_volume_power_comparison` turns the counts into volumes. The rest is bookkeeping.

## In the Lean code

The lemma is in [UniformAllNormHeightBound.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/UniformAllNormHeightBound.lean#L300), with the helpers `clearN_le`, `clear_integral` and `modelSmall_encard_le`. The volume slope is in [IsHomogeneousCompIdeal.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsHomogeneousCompIdeal.lean#L280).

The name `BirationalPullbackPushforwardFormula` ([ArithmeticHilbertSamuelLowerBound.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ArithmeticHilbertSamuelLowerBound.lean#L126)) is misleading. It bounds $II(A^{D+1})$ by an arithmetic volume of small sections. It has no pullback and no pushforward.
