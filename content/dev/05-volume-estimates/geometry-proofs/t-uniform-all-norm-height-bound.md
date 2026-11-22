---
id: t-uniform-all-norm-height-bound
title: The slope minus a cost is at most the volume slope, restated
kind: theorem
decl: GlobalTheory.T.uniform_all_norm_height_bound
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.UniformAllNormHeightBoundStatement
covers: 1113
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the comparison of slope and volume slope](/entry/slope-sub-cost-le-comp-vol-slope/), which has the real content, through the second renaming [`Relay.uniform_all_norm_height_bound`](/entry/relay-uniform-all-norm-height-bound/). Its one user is [`top_meanAll`](/entry/top-mean-all/). That proof applies it to each component $Z$ with the bound $B$ of the weight, takes the mean over the components and bounds the cost term by `cost_two_log_bound`.

## Statement

The statement is the same as that of [`slope_sub_cost_le_compVolSlope`](/entry/slope-sub-cost-le-comp-vol-slope/). In short: let $T$ be a root tower with a good origin and a full intersection system, and let $u$ be a strictly decreasing weight that is regular with gap $g$, with $B \ge B_0(u,g)$. Then for each component $Z$,
$$\mathrm{slope}_T(\lfloor B \rfloor, Z, u) - 2\,\mathrm{cost}(l,B)\,\|u\|_1 \le \mu_{\mathrm{vol}}(Z,u),$$
where $\mu_{\mathrm{vol}}$ is the volume slope of the sections that are small at the places of the mixed valuations. The hypotheses are the asymptotic Riemann-Roch statement `NefRR`, the inputs `Top.Given` and the volume inequality `BirationalPullbackPushforwardFormula`. The linked entry gives all of them.

## Proof

The statement is the same as that of `Relay.uniform_all_norm_height_bound`, and the proof applies it.

## In the Lean code

The theorem is in [UniformAllNormHeightBoundStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/UniformAllNormHeightBoundStatement.lean#L16). The proof is

```
first | exact @GlobalTheory.CompanionTheory.Relay.uniform_all_norm_height_bound | ...
```

The name says "height bound", but the conclusion compares a slope with a volume slope. No height appears in the statement except through the cost term.
