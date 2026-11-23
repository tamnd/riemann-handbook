---
id: models-at-of-part
title: Local models from a column part
kind: theorem
decl: GlobalTheory.Svd.modelsAt_of_part
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.TuplesHaveLocalModelsOfStandardColumnObjects
covers: 2850
status: drafted
drafted_by: writer@claude
---
This theorem proves the local model condition `ModelsAt` for an object that comes from a column datum. It joins three lemmas: one that makes the joint data, one that proves trivial stabilisers at step zero, and [`thetaLocalModels_of_splitUnramified_joints`](/entry/theta-local-models-of-split-unramified-joints/), which turns these into good local models. Its statement is restated as [`tuplesHaveLocalModels_of_standardColumnObjects`](/entry/tuples-have-local-models-of-standard-column-objects/), and [`modelsAt_bpt`](/entry/models-at-bpt/) uses that form. Above it, [`servH_row`](/entry/serv-h-row/) uses `ModelsAt` to prove the first half (`RowTwU`) of the service row. Of the 2,850 declarations below this theorem, 2,341 are below `thetaLocalModels_of_splitUnramified_joints`.

## Statement

Assume the two statements `AdmAtEnt2` and `CurveEx`. They are described in [`site_cmpLite_siteAdm`](/entry/site-cmp-lite-site-adm/), the only place below this theorem where they are used.

Let $B$ be a base, $f$ a frame of $B$ and $T$ twist data over $B$. Let $w$ be a column datum (`ColW B f T`): a column input $I$ with the frame $f$, together with laws, pins and field data. Let $Z$ be a later stage of $w$, and let $D = w.D(Z)$ be the datum of type `D7` that $I$, its laws and $Z$ build. Let $O$ be an object over $D$, with lattice instances $G_x$, $G_y$, ties `gatT`, division data $X$ and extra data `ex`. A *part* of $O$ at $(w, Z)$ (the structure `Part`) is a column pin, a column $C$ at $Z$, and equalities that tie $O$ to $C$: the error data of $O$ is the one of $C$, the tuple data of $O$ has the map $\xi$ of $I$, the set $Q_p$ of $X$ is the one of $I$, and the ties, the comparison, the twisted forms and the kernel family of $O$ are those of $C$.

**Theorem.** If $O$ has a part at $(w, Z)$, then `ModelsAt D O` holds. That is: if the lattice instances of $O$ are tied (`LatTied gatT Gx Gy`) and

$$2\, r_G(\varepsilon) \le k, \qquad r_G(\varepsilon) = \left\lceil \frac{8\,(4 + 8\varepsilon)}{\varepsilon} \right\rceil + 1,$$

where $\varepsilon$ is the scale of the size data of $O$ and $k$ is the field `D.R.k`, then `ModelsOK D Gy ex.cmp X ex.tw` holds. `ModelsOK` is described in [`modelsOK_of_joints`](/entry/models-ok-of-joints/).

## Proof

Introduce the two hypotheses of `ModelsAt`.

1. `jointsAt_all_std` takes the part and the tie of the lattice instances. It gives a tied kernel entry $t$ of `ex` with `JointsAt t μ` for every tuple $\mu$, and the equality $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ of the twisted forms for each word $u$. Its proof opens the part with `Part.kerTie` and calls `kernel_relation_true_columns_joints_all_tuples`, which we have not opened.
2. `stepZero_trivial_stabilisers_trueColumns` gives `Stab0 D`: at step zero, every class has a stabiliser of one element. It uses only the column input, its laws and the level data of $O$.
3. [`thetaLocalModels_of_splitUnramified_joints`](/entry/theta-local-models-of-split-unramified-joints/) takes $t$, the joints (only at the used tuples), the equality, `Stab0 D` and the bound $2\, r_G \le k$, and gives `ModelsOK`.

## In the Lean code

The theorem is at [TuplesHaveLocalModelsOfStandardColumnObjects.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/TuplesHaveLocalModelsOfStandardColumnObjects.lean#L11). `ModelsAt` and `Part` are in [HasPartAnd.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/HasPartAnd.lean#L13). The lemmas it calls:

- `GlobalTheory.Svd.jointsAt_all_std` in [JointsAtAllStd.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JointsAtAllStd.lean#L11).
- `GlobalTheory.Pdv.stepZero_trivial_stabilisers_trueColumns` in [StepZeroTrivialStabilisersTrueColumns.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/StepZeroTrivialStabilisersTrueColumns.lean#L89).
- `GlobalTheory.T.thetaLocalModels_of_splitUnramified_joints`.

`ModelsAt` is an implication, so the proof introduces two more hypotheses (`hL`, `hk`) than the statement shows. `Part` is a structure in `Type 1`, so the theorem takes data, not a proof. The hypotheses `AdmAtEnt2` and `CurveEx` are only passed on. `stepZero_trivial_stabilisers_trueColumns` takes the pins `TC.Pins` as an argument but does not use them (line 91: `intro B X I h _ l Z lev`).
