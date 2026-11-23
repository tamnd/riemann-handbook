---
id: g-unif-of
title: Complex uniformisation of the generic moduli models
kind: theorem
decl: UpperTheory.Gal.W2.gUnif_of
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.SphericalCoordinates.PGUnif
covers: 534
status: drafted
drafted_by: writer@claude
---
This theorem proves `GUnif` from five named inputs. Its parent [GUnif_holds](/entry/gunif-holds/) only supplies those five inputs. Thus the geometry of the parent is done here: the moduli scheme over a $\mathbb{Q}$-algebra is smooth, quasi-compact and separated, and its complex points have a uniformisation by marked period lattices. The result feeds [the fixed points over the integral base](/entry/fixed-points-int-base-holds/). Below this theorem are 534 declarations.

## Statement

```lean
theorem gUnif_of : ModelEx → GenCmp → GenPts → BaseC → GFine → GUnif
```

`GUnif` is in [LevelChange.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/LevelChange.lean#L20). Take a PEL datum $D$ with $a = m = 1$ and all $\tau_i$ equal to one $t_0$. Take $\rho$ with `IsSigD`, a base point $g_b$ with `IsStd` (so $g_b.\rho = D.\rho_c$ and $g_b.t = D.\tau$), a level $N \ge 3$ prime to $p$, and $X$ : `GenModel gb N`. Then:

- $X.s$ is smooth of relative dimension $n-1$, quasi-compact and separated;
- the family `gfam X.univ` is `FineAt` level $N$ for the class set `D.Cls N`;
- a `Unif` exists: a finite list of marked lattices with uniformising maps that cover the complex points, are disjoint, and are holomorphic.

The five inputs, at lines 219 to 233 of the same file, are: an integral `Model` exists (`ModelEx`); `X` embeds by an open and closed immersion in the complex fibre of the model (`GenCmp`); this embedding is a bijection on complex points (`GenPts`); a complex base point $b$ matches $g_b$ (`BaseC`); and `FineAt` passes from the model to `X` (`GFine`).

## Proof

The proof is in [PGUnif.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/PGUnif.lean#L15).

1. `BaseC` gives $b$ over $\mathbb{C}$ with the same $\rho$ and $t$ as $g_b$. `ModelEx` gives a model $M$ over $\mathbb{C}$.
2. `GenCmp` gives an open and closed immersion $j$ from $X.X$ into $M.X \times_{\mathbb{C}} \mathbb{C}$. `GenPts` makes $j$ bijective on complex points.
3. `model_uniformised` gives two facts about $M$ that later steps need. Its own `Unif` output is discarded.
4. `complexPoints_classify_markedPeriods` gives `FineAt` for $M$. `GFine` moves it to $X$.
5. `M.smooth` has relative dimension $a(n-1) = n-1$. Base change and the open immersion $j$ carry it to $X.s$. Quasi-compactness comes from the quasi-projectivity `M.qproj`. Separation comes from `M.qproj` and `isProper_str`.
6. `complexUniformisation_of_markedPeriods_family` gives the `Unif`. It uses $\eta^N = 1$ (`GObj.eta_nsmul`) and the full marking `Datum.Cls.fullMark`.

## In the Lean code

The five inputs are proved in [FixedPointsIntBaseHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/FixedPointsIntBaseHolds.lean#L164). `ModelEx` comes from [model_nonempty](/entry/model-nonempty/). In step 3 the proof discards a full `Unif` for $M$ and then computes `FineAt` again in step 4. I have not unfolded the proofs of `complexPoints_classify_markedPeriods` or `unif_of_fineAt`, which carry the analytic content.
