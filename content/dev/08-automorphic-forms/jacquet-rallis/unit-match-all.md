---
id: unit-match-all
title: The Jacquet-Rallis fundamental lemma for unit functions in all ranks
kind: theorem
decl: GlobalTheory.JR.unitMatch_all
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.JacquetRallisUnitMatchAllRanks
covers: 1357
status: drafted
drafted_by: writer@claude
---
This theorem proves the Jacquet-Rallis fundamental lemma for unit functions in every rank, with no hypothesis. It puts the existence of the quadratic Weil representation into [unit matching from the quadratic Weil representation](/entry/jacquet-rallis-unit-match-of-weil-rep-quadratic/). The induction on the rank is in [the entry for that proof](/entry/unit-match-of-weil-field/). The result goes up through [its statement file](/entry/jacquet-rallis-unit-match-all-ranks/). Below this theorem are 1,357 declarations of the proof.

## Statement

For every $r \geq 0$, $\mathrm{UnitMatch}(r)$ holds.

Here $E/F$ is an unramified quadratic extension of $p$-adic fields. $\mathrm{UnitMatch}(r)$ says that the orbital integrals of $\mathbf{1}_{\mathfrak{gl}_{r+1}(\mathcal{O}_F)}$ under $\mathrm{GL}_r(F)$, weighted by the sign $\omega$ (the transfer factor), equal the orbital integrals of the unit function on Hermitian $(r+1) \times (r+1)$ matrices under $U_r$ at regular elements with the same invariants. The first vanish at regular invariants that no Hermitian element has. The objects are defined in full in [the entry with the proof](/entry/unit-match-of-weil-field/).

## Proof

The proof is one line:

```
jacquetRallisUnitMatch_of_weilRep_quadratic weilRepresentation_quadraticField_exists
```

The first lemma proves $\mathrm{UnitMatch}(r)$ for all $r$ from $\mathrm{WeilField}$. The second, `weilRepresentation_quadraticField_exists`, proves $\mathrm{WeilField}$. Let $K/F$ be a finite field extension with $L = K \otimes_F E$ a field, and let $x \in K^\times$. It builds the [Weil representation](/learn/theta/#the-weil-representation) of $\mathrm{SL}_2(K)$ on test functions on $L$ for the form $x N_{L/K}$. We read the top of its proof, `WeilQuad.weilField_main`, but not its lemmas. It defines the operators for $n(z)$, $m(s)$ and $w$. The operator for $w$ is the Fourier transform, divided by a Gauss integral $G_1$ with $G_1^2 = 1$. It checks the relations between these operators (for example `rel_ww`, `rel_wm`, `rel_wnw`) and gets the representation from a presentation of $\mathrm{SL}_2(K)$.

## In the Lean code

The theorem is at [JacquetRallisUnitMatchAllRanks.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetRallisUnitMatchAllRanks.lean#L9). The lemmas it calls:

- `GlobalTheory.T.jacquetRallisUnitMatch_of_weilRep_quadratic`, a second name for `unitMatch_of_weilField`;
- `GlobalTheory.T.weilRepresentation_quadraticField_exists`, a second name for `WeilQuad.weilField_main` in [WeilRepresentationQuadraticFieldExists.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WeilRepresentationQuadraticFieldExists.lean#L189).

The hypothesis `WeilField` is used two times in the induction: for the Weil representation on all étale algebras, and for the matching of Fourier transforms. This theorem discharges both.
