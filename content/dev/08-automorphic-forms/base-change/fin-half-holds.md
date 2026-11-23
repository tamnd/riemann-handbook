---
id: fin-half-holds
title: The finite part of an elliptic term is a mass times local orbital integrals
kind: theorem
decl: PositivityTheory.Rg.BcB.G8.Fin.finHalf_holds
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.ThetaNormCommutation.LocalComparisonSplitting.EulerFactorLevels.FinLevelHolds
covers: 476
status: drafted
drafted_by: writer@claude
---
This theorem proves `FinHalf`, the finite-place half of the term identity in [the global character formula](/entry/global-character-holds/). For a pair of rational twisted classes with elliptic norms, it writes a sum over double cosets of the finite adelic group as two masses times a product of local twisted orbital integrals. The product formula itself is [`eulerFin_holds`](/entry/euler-fin-holds/).

## Statement

Let $E$ be a CM field in which each finite place is unramified over $F$, and let $S$ be a set of finite places of $E$ with one place above each finite place of $F$. Let $G_f = \mathrm{GL}_a(\mathbb{A}_{E,f}) \times \mathrm{GL}_b(\mathbb{A}_{E,f})$ with the twist $\theta$ given by $\theta_E$ on each factor over the finite adeles, and let $K_f$ be the product of the groups $\mathrm{GL}_a(\mathcal{O}_w) \times \mathrm{GL}_b(\mathcal{O}_w)$ over all finite $w$. Let $\phi_1, \phi_2$ be test functions as in `G4`, and let $\Phi_f(y) = \prod_{w \in S} \phi_{1,w}(y_w)\, \phi_{2,w}(\theta(y)_w)$, where the second factor is present only at split $w$.

Let $\delta_1 \in \mathrm{GL}_a(E)$, $\delta_2 \in \mathrm{GL}_b(E)$ have norm polynomials that are separable with all roots of absolute value $1$. Let $\Gamma$ be the set of rational points of $G_f$ in the twisted centralizer of $\delta = (\delta_1, \delta_2)$. Put $F(x) = \Phi_f(x^{-1}\delta\theta(x))$.

**Theorem.** Only finitely many double cosets $\Gamma q K_f$ meet the support of $F$. Each group $\Gamma \cap x K_f x^{-1}$ is finite. And

$$\sum_{q \in \Gamma \backslash G_f / K_f} \frac{1}{|\Gamma \cap q K_f q^{-1}|} \int_{K_f} F(qk)\, dk = m(\delta_1)\, m(\delta_2) \prod_{w \in S} TO_w(\delta_1, \delta_2),$$

with $m$ and $TO_w$ as in [the global character formula](/entry/global-character-holds/). The integral is the average over $K_f$.

## Proof

The proof applies `finite_half_of_twist`, of type `FinHalfOf`, to seven facts:

1. `DcCount_pf`: under finiteness conditions, a sum of this form over $\Gamma \backslash G / K$ equals the mass of $\Gamma$ times the twisted orbital integral over $K$.
2. `finite_mass_product_formula`: the mass of a product is the product of the masses.
3. `rational_finite_places`: the finiteness conditions of step 1 hold for $\Gamma$ and $K_f$.
4. `suppFin_holds`: the support of $F$ meets finitely many double cosets.
5. [`eulerFin_holds`](/entry/euler-fin-holds/): the twisted orbital integral over $K_f$ is the product of the local ones.
6. `kfOC_holds` and `finLevel_holds`: $K_f$ is open and compact, and $\Phi_f$ has an open level.

## In the Lean code

The theorem is in [FinLevelHolds.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ThetaNormCommutation/LocalComparisonSplitting/EulerFactorLevels/FinLevelHolds.lean#L33). `FinHalf` is in [GlobalCharacterOfInputs.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ThetaNormCommutation/LocalComparisonSplitting/GlobalCharacterOfInputs.lean#L62), and `FinHalfOf` is in [EulerFinOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/ThetaNormCommutation/LocalComparisonSplitting/EulerFactorLevels/EulerFinOf.lean#L104). The names in `GlobalTheory.T` are one-line wrappers of lemmas in `GlobalTheory.CompanionTheory`, for example `FinHalfAsm.finHalfOf`. We have not opened that proof.
