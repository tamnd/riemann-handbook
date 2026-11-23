---
id: euler-fin-holds
title: The finite adelic twisted orbital integral is a product of local ones
kind: theorem
decl: PositivityTheory.Rg.BcB.G8.Fin.eulerFin_holds
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.ThetaNormCommutation.LocalComparisonSplitting.EulerFactorLevels.FinLevelHolds
covers: 331
status: drafted
drafted_by: writer@claude
---
This theorem proves `EulerFin`: the twisted orbital integral over the finite adeles of a product function is the product of the local twisted orbital integrals at the places of $S$. It is step 5 of [the finite half](/entry/fin-half-holds/), which is used in [the global character formula](/entry/global-character-holds/). The proof only passes six inputs to a lemma that we have not opened.

## Statement

We use the notation of [the finite half](/entry/fin-half-holds/): $E$, $S$, $G_f$ with its twist $\theta$, $K_f$, the test functions $\phi_1, \phi_2$, and the product function $\Phi_f$. Let $\delta_1, \delta_2$ be rational with elliptic norm polynomials.

**Theorem.** The twisted orbital integral of $\Phi_f$ at $\delta = (\delta_1, \delta_2)$ over $K_f$ is the product over $w \in S$ of the local twisted orbital integrals $TO_w(\delta_1, \delta_2)$.

At a split $w$ the local element is $\delta\,\theta(\delta)$ and the local function is the convolution of $\phi_{1,w}$ and $\phi_{2,w}$. At a non-split $w$ they are $\delta$ and $\phi_{1,w}$.

## Proof

`finite_euler_product_of`, of type `EulerFinOf'`, takes six inputs. `CjEx` gives a continuous conjugation on each algebra $\prod_{w \mid v} E_w$, for $v$ a place of $F$. `RestrV` makes $G_f$ the restricted product of the local groups at the places $v$. `Regroup` writes $\Phi_f$ as a product of local factors $f_v$. `LocCompare`, from an inert and a split case, says that the orbital integral of $f_v$ is $TO_w$ for the place $w \in S$ above $v$. `LocHyp` gives the local finiteness and almost-everywhere unramified conditions. `Reindex` turns a product over $S$ into a product over the places of $F$.

## In the Lean code

The theorem is in [FinLevelHolds.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ThetaNormCommutation/LocalComparisonSplitting/EulerFactorLevels/FinLevelHolds.lean#L30). `EulerFin` is in [EulerFinOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ThetaNormCommutation/LocalComparisonSplitting/EulerFactorLevels/EulerFinOf.lean#L98). The six inputs are stated in [LocCompareSplit.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ThetaNormCommutation/LocalComparisonSplitting/EulerFactorLevels/LocCompareSplit.lean#L100). Each name in `GlobalTheory.T` is a one-line wrapper of a lemma in `GlobalTheory.CompanionTheory`, for example `EulerAsm.eulerFinOf'`.

Two names are misleading. `finite_restriction_vanishing` states a restricted product structure, not a vanishing. `aux_statement_21` gives no hint of its content. The same file `EulerFinOf.lean` defines a second route, `EulerFinOf` (line 106), with inputs `RestrTw` and `SplitConv`. This proof does not use it.
