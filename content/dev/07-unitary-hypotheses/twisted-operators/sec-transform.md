---
id: sec-transform
title: The Hecke transform of a section
kind: theorem
decl: GlobalTheory.HeckeEx.secTransform
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.HeckeTransformOfPointLaws
covers: 378
status: drafted
drafted_by: writer@claude
---
This theorem builds the Hecke operator at a split-off prime on sections of the moduli space. It is the content of [the Hecke transforms from the point laws](/entry/hecke-transform-of-point-laws/).

## Statement

Sections are rules in the style of Katz. A framed point $y$ over a $c.F$-algebra $S$ is a point $x$ of the moduli space $X$ over $S$, with an eigenbasis of the tangent space and a generator $s$ of the theta line. A rule $f$ gives a value $f(y) \in S$ for each framed point over each test ring, that is, a reduced finitely generated $c.F$-algebra. A section of weight $(a, n)$ is a rule that commutes with base change and changes by the character of weight $(a, n)$ under a change of the eigenbasis by a Borel element.

For a geometric point $y$ over an algebraically closed $\Omega$, the Hecke kernels at $(\mathfrak{P}, p, i)$ are subgroups $C$ with the `HeckeKer` property. The term at $C$ is $f(z)$, where $z$ is a framed point reached from $y$ by a Hecke isogeny with kernel $C$ that respects the tangent bases and carries the theta generators by the trace (`hkTr`). It is $0$ if there is no such $z$.

Assume `HeckePointLaws`. Let $1 \le p + q$, let $\mathfrak{P}$ be split off at $p$, let $i \le p + q$, and let $n$ be even. Then for every section $f$ of weight $(a, n)$ there is a section $g$ of the same weight with
$$g(y) = c_q\, (N\mathfrak{P})^{-in/2} \sum_C \mathrm{term}(f, y, C)$$
at every geometric point $y$. The scalar is `hkScal` ([LiftLaSpec.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/LiftLaSpec.lean#L57)).

## Proof

1. The split-off condition makes $(\mathfrak{P}, p)$ admitted. `HeckeTotal` gives a target point for every kernel.
2. A test ring is reduced, since its ideal is radical. On each test ring and each framed point $y$, the [sum lemma](/entry/exists-sum/) gives a value $g(y)$ whose image at each geometric point is the sum of the terms.
3. An element of a reduced finitely generated algebra is fixed by its values at geometric points (`GeometricValues.eq_zero_of_forall_algClosed`). So naturality of $g$ follows from `bc_exists` and `frMap_trans`. The weight law follows from `heckeKernel_value_sum_weight_triangular_frame`, which uses `HeckeSingleValued`.
4. Take $\mathrm{hkScal} \cdot g$. Each geometric point comes from a test ring (`framedPoint_reduced_from_testRing`), so the relation holds.

## In the Lean code

The theorem is on [line 225 of HeckeTransformOfPointLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeTransformOfPointLaws.lean#L225). `SecTransform` and `HasTransform` are in [SplitOffDetection.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/SplitOffDetection.lean#L76). `HasTransform` is `HkEx` of [HeckeStabSet.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/HeckeStabSet.lean#L72).

The intro pattern on line 226 drops the hypotheses $i \le p + q$ and "$n$ even" with `_`. The laws `HeckeFinite` and `PointsDetect` are not used: reducedness does the work of detection. We have not unfolded `HeckeKer` or `IsThetaTrace`.
