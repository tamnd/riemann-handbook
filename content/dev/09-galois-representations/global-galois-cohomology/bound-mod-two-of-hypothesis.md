---
id: bound-mod-two-of-hypothesis
title: The Selmer order bound when ν is positive, by auxiliary places
kind: theorem
decl: GlobalTheory.StepTwo.Dyadic.bound_mod_two_of_hypothesis
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.BoundModTwoUniformizerAtTwoOfChebotarev
covers: 365
status: drafted
drafted_by: writer@claude
---
This theorem proves the order bound `ThmC` for the Selmer data of a twist system. It chooses auxiliary places one at a time by Chebotarev and controls the determinant of a Selmer presentation at each step. Its second name [`boundModTwoUniformizerAtTwo_of_chebotarev`](/entry/bound-mod-two-uniformizer-at-two-of-chebotarev/) gives step 3 of [good twists for all coprime powers](/entry/twist-all-powers-of-galois-cohomology-class-field/). Below it are 365 declarations.

## Statement

Assume the same eleven published statements as the [second name](/entry/bound-mod-two-uniformizer-at-two-of-chebotarev/), among them `Cheb`: for an open normal subgroup $U$ of $G_F$, an element $g$ and a finite set $A$ of places, there is an unramified place $v \notin A$ of degree one with a Frobenius in $gU$.

Fix a datum $D$, a twist system $X$ and a Bloch-Kato phase datum $\mathrm{bkP}$. Each twist index $i$ has a prime $\ell_i$, a discrete valuation ring $O_i$ and the number
$$\nu_i = \min_{g} v_{\ell_i}\bigl(\varepsilon(g)^n - 1\bigr), \qquad n = t r,$$
where $\varepsilon$ is the $\ell_i$-adic cyclotomic character (`nu`, from `nuOf`; it is $0$ if all $\varepsilon(g)^n = 1$).

**Theorem.** `ThmC bkP` holds: for each $i$ with $\nu_i > 0$, `OrdBound` holds with $\mu = v(\ell_i^{\nu_i})$. That is, for each set $T$ of signs with `GalHyp`, there are $R$, $D_d$ and $M_0$ such that for $M \ge M_0$, each admissible family, each tame inertia element $z$, each open normal subgroup $H'$ and each finite set $A$ of places, there are $2R$ auxiliary places $P$ such that: for each $s \in T$ and each matrix $\Phi$ that computes the Selmer data at $P$, the polynomial $F$ with image $\det \Phi$ has a coefficient of degree at most $D_d$ with valuation at most $v(\ell_i^{\nu_i})$.

## Proof

The proof applies `TwoBound.thmC_of_parts`, an induction that adds one auxiliary place at a time. It needs, for each $i$:

1. `StepAB`: places with a prescribed Frobenius, avoiding $A$. This is `ChosenPrimes.stepAB`, from `Cheb`.
2. `ChooseH`: elements $h_a$ such that each matching set of Frobenius elements gives the Selmer data corank 1 when $\nu_i > 0$ (and 0 when $\nu_i = 0$). This is `ChooseForms.chooseH`, from `GlobalFiniteness`, `spanOdd`, `spanTwo_of_galHyp` and `residual_selmer_finrank_eq_dual` (a residual Selmer group and its dual have equal dimension).
3. For each $s$ with `GalHyp`, three conditions:
   - `Start`: with corank 1, an entry of the adjugate has a unit coefficient of small degree. This is `start_of_resBound`, from `ScalarFrob.firstPlace` and the residual bound `ResOrder.resBound`, which uses the reciprocity law `ResRecip.reciprocity`.
   - `Grow`: one more place keeps these properties, with the degree bound raised by $2r$. This is `Growth.grow`, from `TameLocal` and the presentation `oneMatrix_of_galoisCohomology`.
   - `Step`: a new place $P'$ can be chosen so that the determinant has a coefficient outside the ideal $(\ell_i^{\nu_i})\mathfrak{m}$. This is `NewPrime.step`, from all eleven hypotheses.

## In the Lean code

The theorem is in [BoundModTwoUniformizerAtTwoOfChebotarev.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BoundModTwoUniformizerAtTwoOfChebotarev.lean#L25). `thmC_of_parts` is in [AddValLeOfNotMem.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/AddValLeOfNotMem.lean#L87). `Start`, `Grow` and `Step` are in [Small2.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/Small2.lean#L40). `ThmC` is in [GaloisSideTwistedSelmerAuxiliaryPrimes.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/GaloisSideTwistedSelmerAuxiliaryPrimes.lean#L67).

- The names "mod two", "at two" and the namespace `Dyadic` suggest $\ell = 2$. The statement covers every $\ell_i$ with $\nu_i > 0$. For $\ell_i = 2$ and $n \ge 1$, $\varepsilon(g)$ is odd, so $\nu_i \ge 1$ always. For odd $\ell_i$, $\nu_i > 0$ holds when $\varepsilon(g)^n \equiv 1 \pmod{\ell_i}$ for all $g$. The case $\nu_i = 0$ is `ResidualBoundOddPrimes`. A 2 appears only in the condition $\zeta^{2\ell^M} = 1$ of `Small2` and `StepAB`.
- `GalHyp` ([IsTameInertiaElementAtTwistPrime.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsTameInertiaElementAtTwistPrime.lean#L119)) has a conjunct `True`, and asks $r \ge 100$.
- We did not unfold `Computes`, nor the conditions `SlopeTestRemainingChoices` and `Steps` on the auxiliary places.
