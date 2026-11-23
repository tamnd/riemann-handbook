---
id: k-twins
title: Kleiman's positivity facts on products of projective spaces, from axioms for intersection numbers
kind: theorem
decl: PositivityTheory.HtPt.Ktw.k_twins
module: Development.WeilBound.CoreStatements.HodgeTatePoints.KTwins
covers: 725
status: drafted
drafted_by: writer@claude
---
This theorem proves three positivity facts for subvarieties of a product of projective spaces: nef products have nonnegative intersection numbers, nef plus a positive multiple of the base degree is very ample after scaling, and a lower bound for the number of sections. It assumes five rules for intersection numbers in a single projective space. It is a step of [EveryCharacter from the literature and VWin](/step/every-character-of-literature/). The proof proves the single projective space versions from the rules, and then moves them to the product through models. One of the transfers uses [`a18`](/entry/a18/).

## Statement

The hypothesis `GenericPointSectionInput` is about a field $k$, a point $x$ of $\mathbb{P}^N$ with coordinates in a field $\Omega$, line bundles $L_i$ on the closure of $x$, and subvarieties given by prime ideals $\mathfrak p$. It says that the intersection number $\operatorname{interNum}_{\mathfrak p}(L_1,\dots,L_n)$ on an $n$-dimensional subvariety:

1. is eventually equal to the coefficient sum `interSum`;
2. does not change when the $L_i$ are permuted;
3. is additive in each $L_i$;
4. can be computed by cutting with a section $s$ of the last bundle, as the sum over the minimal primes $\mathfrak q$ of $\mathfrak p+(s)$ of the multiplicity times $\operatorname{interNum}_{\mathfrak q}(L_1,\dots,L_{n-1})$;
5. is the residue degree when $n=0$.

The conclusions are about a point $y$ with coordinates indexed by $\coprod_{k\in K}\iota_k$, that is, a point of $\prod_k\mathbb{P}^{\iota_k}$, and multidegrees $\mu\colon K\to\mathbb{Z}$.

**Theorem.** If `GenericPointSectionInput` holds, then:

1. (`NefProductNonneg`) if $\mu_1,\dots,\mu_d$ are nef and the ideal of $y$ has relative dimension $d$, then $\operatorname{intNum}(\mu_1,\dots,\mu_d)\ge0$;
2. (`VeryAmpleNefPlusAmple`) for a model with base index $k_0$, a nef $\mu$ and $t>0$, `MultipleVeryAmple y μ (baseDeg k₀) t` holds;
3. (`SectionCount`) for a model with base index $k_0$ of relative dimension $d+1$, a very ample $\nu$ and $q\ge1$, there is $C$ with
$$\Bigl(\nu^{d+1}-(d+1)\,\nu^{d}\cdot q\,b\Bigr)\frac{n^{d+1}}{(d+1)!}-Cn^{d}\le\dim H^0\bigl(n(\nu-q\,b)\bigr)\quad(n\ge1),$$
where $b$ is the base degree at $k_0$.

Part 1 is Kleiman's theorem (S. Kleiman, Ann. of Math. 84, 1966; Lazarsfeld, *Positivity I*, Thm. 1.4.9). Part 3 has the form of Siu's inequality (Lazarsfeld, *Positivity I*, §2.2). I have not unfolded `MultipleVeryAmple`; part 2 is the multiprojective form of "nef plus ample is ample" (Lazarsfeld, Cor. 1.4.10) only if that predicate means what its name says.

## Proof

The proof is `⟨a64 hR, a73 hR, a77 hR⟩`.

1. `a64`: `a63` proves the single projective space statement `Kleiman.NefProductNonneg` from the rules. `unfolding_matrix_of_form` moves it to the product with `a28`, which realizes the multiprojective data in one projective space by the Segre coordinates $\prod_a y_{a,i(a)}$.
2. `a73`: `a72` proves `Kleiman.VeryAmpleNefPlusAmple` from the rules. An equivalence `VeryAmpleNefPlusAmple.equiv`, with the model facts `a65` and `a71`, turns it into the multiprojective version.
3. `a77`: `Kleiman.SectionCount.assembled` proves the single space count from the rules. `SectionCount.equiv` turns it into the multiprojective version; one of its inputs is `a18`.

`a63` and `a72` take the same list of proved inputs: `a39`, `a43`, `a48`, `a51`, `a55`, `a61`, `a62` and `PointGenerated.proof`.

## In the Lean code

The theorem and `a64`, `a73`, `a77` are in [KTwins.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/KTwins.lean#L40). `a63` and `a72` are in [A53.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/A53.lean#L90), and `a28` in [A28.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/A28.lean#L72).

- The hypothesis and the single space statements are in [GenericPointSectionHypotheses.lean](lean:GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/GenericPointSectionHypotheses.lean#L202).
- The multiprojective statements are in [IsFieldSubalgebraSelf.lean](lean:GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/IsFieldSubalgebraSelf.lean#L298).
- `SegreRealise` is in [ImportsTailRest.lean](lean:GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/ImportsTailRest.lean#L10), `unfolding_matrix_of_form` in [KleimanNefF.lean](lean:GroundTheory/HeightsAndTheta/Heights/SemipositiveHeights/KleimanNefF.lean#L42), and `VeryAmpleNefPlusAmple.equiv` in [ExistsNeZeroOfIsSubvarAlt.lean](lean:GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/ExistsNeZeroOfIsSubvarAlt.lean#L25).

The hypothesis is proved as `kleiman_input_universe_zero` in [KleimanInputUniverseZero.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/KleimanInputUniverseZero.lean#L18), from `interNumEventual`, `interNumAdditive`, a cutting lemma and `interNumPointDeg`.

The name `unfolding_matrix_of_form` does not describe the lemma: it is a transfer of `NefProductNonneg` along a Segre realization.
