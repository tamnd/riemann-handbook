---
id: uniform-all-tower-bound
title: The finite-place bound for tower sections, restated
kind: theorem
decl: GlobalTheory.T.uniform_all_tower_bound
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.UniformAllTowerBoundStatement
covers: 311
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`vs_fin`](/entry/vs-fin/) with one more hypothesis, which the proof does not use. Its one user is [`descent_small`](/entry/descent-small/). There it gives the last clause: the section $f$ of the moduli space read off a small section $s$ of the tower has a bounded denominator at each finite place. The content is in [`vs_fin`](/entry/vs-fin/).

## Statement

The statement is that of [`vs_fin`](/entry/vs-fin/), with the extra hypothesis `GeoRead Rd` on the reading $\mathrm{Rd}$. In short: let $s$ be a section of the root tower of weight $u$ that is integral on each chart, and let $f$ be a section of weight $u$ on the component $Z$ whose value at the generic frame is the trace of $s$ divided by a gauge. Then for each prime $p$, each prime $\lambda$ of $F$ above $p$ and each valuation $v$ at $\lambda$ from an integral point,
$$v(f) \ge -v_\lambda(p)\, \varepsilon_p\, \|u\|_1,$$
where $\varepsilon_p = 0$ if $p$ is a good prime of the tower at level $B$.

`GeoRead Rd` says that there is a frame $y'$ over the field of the tower that is the image of the generic frame of $Z$ under $\mathrm{Rd}.\varphi$, and that $y'$ and the base frame $\mathrm{Fr}.y_0$ differ by the torus element $\mathrm{Rd}.t$.

## Proof

The proof applies `vs_fin` and drops `GeoRead Rd`.

## In the Lean code

The theorem is in [UniformAllTowerBoundStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/UniformAllTowerBoundStatement.lean#L17). The proof is the usual `first | exact @… | …` pattern. The first two branches fail because of the extra argument, and the third (`intros; apply vs_fin <;> assumption`) succeeds. `GeoRead` is in [GeoRead.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/GeoRead.lean#L16). The caller `descent_small` has `GeoRead Rd` as a hypothesis and passes it here, so the hypothesis does no work on this branch.
