---
id: reads-exists-alt
title: Quadratic extension data with all readings exist
kind: theorem
decl: GlobalTheory.Fam.readsExists_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ReadsExists
covers: 350
status: drafted
drafted_by: writer@claude
---
For a geometric family $a$ and each index $t$, this theorem gives a quadratic extension datum $J$ that meets the 17 conditions of `J.Reads`. Through the restatement [`exists_quadratic_extension_reads_of_true`](/entry/exists-quadratic-extension-reads-of-true/), [the column side of a geometric family](/entry/col-side-alt/) uses it in step 2 to fix $J(t)$ for each $t$.

## Statement

Let $W$, $u$ and $a$ be as in [the column side](/entry/col-side-alt/). Quadratic extension data $J$ are described in [the rational datum of the off part](/entry/rat-datum-xi-off-common-alt/); we write $E_i$ for the local datum `QExt` at the place $\mathrm{pl}_i$.

**Theorem.** Assume `AllFamilyConditions W`, `a.Is`, `a.True`, and that the commuting datum `commOf (pk_z W) u a.g` is good. Then for each $t$ there is $J$ with `J.Reads`.

The three sets of conditions share eleven fields: $J.A$ is good, the places $\mathrm{pl}_i$ list `Q t` without repetition and $P_i$ lies over $\mathrm{pl}_i$, the characters of $J.A$ are the characters `chrK_alt`, the signs are $\pm 1$, $\mathrm{Ch}_0(m)$ has one element, and conditions on restriction, twist, the exponent $M$ and representatives. Each also asks that $\iota$ be a section of $\pi$, and that the level element $k_b$ be standard below level $m$. They differ as follows ($m - 1$ is the penultimate level).

- `ReadsLow` does not ask for the section property at $j = m - 1$. It asks that $\iota_0$ and $\iota_m$ be onto, that $\iota_j$ be one to one at each level $j \neq m - 1$, and that $\xi_j(\alpha, \gamma) = 0$ when $j + 2 \neq m$ and $\gamma$ is not in the image of $\iota_{j+1}$.
- `ReadsStd` drops these. It asks that the coset `cos` of each $E_i$ be in the same orbit as the coset read from $J.A$ (`orb`), and two more conditions, `cosG` and `live`.
- `Reads` asks for equality of the cosets (`cos`) in place of `orb`. It drops the standard level condition at $j = m - 1$ and asks there for a factorization $k_A = k_0 h$ instead (`pen`).

## Proof

1. `exists_quadratic_extension_reads_low_of_true` gives $J$ with `ReadsLow`.
2. `true_geometry_commutation_identity_alt` turns it into $J'$ with `ReadsStd`.
3. `true_geometry_commutation_property_alt` turns that into $J''$ with `Reads`.

## In the Lean code

The theorem is at [ReadsExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ReadsExists.lean#L21). `Reads` is in [QuadraticExtensionData.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/QuadraticExtensionData.lean#L42), and `ReadsStd`, `ReadsLow` in [ReadsLow.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ReadsLow.lean#L23). The three lemmas are themselves second names:

- `exists_quadratic_extension_reads_low_of_true` for `LowJoin.exists_quadratic_extension_readsLow`;
- `true_geometry_commutation_identity_alt` for `PenChart.exists_readsStd_alt`;
- `true_geometry_commutation_property_alt` for `Fam.readsOfStd_alt`, in the file `PenMovedOfReadsStdAtLast`.

We have not opened their proofs. The names "commutation identity" and "commutation property" say nothing about the statements, which move from one set of reading conditions to the next.
