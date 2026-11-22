---
id: relay-uniform-all-norm-height-bound
title: The relay copy of the slope and volume slope comparison
kind: theorem
decl: GlobalTheory.CompanionTheory.Relay.uniform_all_norm_height_bound
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.UniformAllNormHeightBound
covers: 1112
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives the lemma [`slope_sub_cost_le_compVolSlope`](/entry/slope-sub-cost-le-comp-vol-slope/), which has the real content, a second name. Its one user is the next renaming, [`T.uniform_all_norm_height_bound`](/entry/t-uniform-all-norm-height-bound/), which goes to [`top_meanAll`](/entry/top-mean-all/).

## Statement

The statement is word for word that of [`slope_sub_cost_le_compVolSlope`](/entry/slope-sub-cost-le-comp-vol-slope/): under `NefRR`, `Top.Given` and `BirationalPullbackPushforwardFormula`, for a root tower $T$ with a good origin, a component $Z$ and a weight $u$ that meets the weight hypotheses with $B \ge B_0(u,g)$,
$$\mathrm{slope}_T(\lfloor B \rfloor, Z, u) - 2\,\mathrm{cost}(l,B)\,\|u\|_1 \le \mu_{\mathrm{vol}}(Z,u).$$

## Proof

The proof is the term `slope_sub_cost_le_compVolSlope`. Nothing else happens.

## In the Lean code

The theorem is at the end of [UniformAllNormHeightBound.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/UniformAllNormHeightBound.lean#L376), in the same file as the lemma that it renames. The proof is

```
GlobalTheory.CompanionTheory.Ar.Plug.SlopeVolM.slope_sub_cost_le_compVolSlope
```

With `T.uniform_all_norm_height_bound` above it, the same statement has three names in a chain of two renamings.
