---
id: twist-all-powers-of-galois-cohomology-class-field
title: Good twists for all coprime powers, from Galois cohomology and class field theory
kind: theorem
decl: GlobalTheory.TwExportTop.twistAllPowers_of_galoisCohomology_classField
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TwistAllPowersOfGaloisCohomologyClassField
covers: 1405
status: drafted
drafted_by: writer@claude
---
This theorem gives, at each twist index $i$ of a datum $D$, a character $\psi'$ such that each power $\psi'^a$ with $a$ prime to $\ell_i$ is a good twist. [The local export condition](/entry/export-at-of-bundles-alt/) gets its good twists from it. It goes up to the step [the hypotheses are not empty](/step/nonempty-hyps/).

## Statement

The theorem has 13 published hypotheses.

- `Cheb`: for an open normal subgroup $U$ of the Galois group, an element $g$ and a finite set $A$ of places, there is a place $v \notin A$ of degree one, unramified, with a Frobenius in $gU$. This is a Chebotarev density statement.
- `LocalFiniteness`, `LocalTateDuality`, `LocalEulerChar`, `GlobalFiniteness`, `GlobalEulerChar`, `UnramifiedOrthogonality` and `GreenbergWiles`: statements about finite Galois modules over $\mathbb{Z}/\ell^r$. The names are those of the standard theorems (finiteness, local Tate duality, Euler characteristics, Greenberg-Wiles). We have not compared each clause with a textbook form.
- `PoitouTateTotallyComplex`, `CohDimTwo`, `TameLocal`: not unfolded.
- `Gen.ArchimedeanSignatureMatching`: six statements on Galois cohomology (see below).
- `RayCharacterArtin`: a statement on ray class characters and the Artin map.

Fix $D$, a Hecke datum $E$ over $D$ and integers $N_0(i)$. Assume 22 further conditions on $D$ and $E$, among them local conditions (`Conclusion5`, `adm1` to `adm10`), conditions on the characters (`IsUnivChar`, `OffRange`, `ThURel`) and conditions on the Hecke side (`UnivSup`, `CommG`, `HkSS` and others). We have not unfolded them.

**Theorem.** For each twist index $i$ with a nonzero index place, `goodTwistExistsAllCoprimePowers` holds at $i$. That is: if `SetHyp` holds at $i$, then for each $\varepsilon' > 0$, if the sets $\Sigma_{i,j,b}$ have full rank, then for all bases of them and each finite set $A$ of places, there are a finite set $Q$, an integer $k'$ and a homomorphism $\psi'$ from the ray class group of $Q$ to $(O_{i,k'})^\times$ such that $\psi'^a$ is a good twist for each $a$ prime to $\ell_i$.

A good twist (`GoodTw`) asks, among other things: the places of $Q$ are split of degree one and avoid $A$; $\psi'$ has values in $\langle\zeta\rangle$ and ramifies exactly at $Q$; index bounds that sum to at most $\varepsilon'$; Selmer lengths at most $\nu + \varepsilon_T$; and a nonzero theta value of bounded valuation.

## Proof

The proof applies `twistTheorem_allPowers_of_selmer_supLattice` to five inputs.

1. `selmerPresentationMatrix_of_galois_cohomology` gives `ThmS`: a square matrix $\Phi$ that computes the Selmer data (`Computes`, not unfolded), with no unit entry.
2. `residualSelmerBound_of_auxiliaryPrimes_odd`, which also uses `GreenbergWiles`, gives the order bound when $\nu = 0$.
3. `boundModTwoUniformizerAtTwo_of_chebotarev` gives `ThmC`, the order bound $v(\ell^\nu)$ when $\nu > 0$.
4. `AdmACD` is built from `adm1`, `adm2`, `adm9`, `adm10`, `Gen.ArchimedeanSignatureMatching` and `duality_dim_of_localTheorem` applied to `Conclusion5`.
5. `delUTie_of_isUnivChar` gives `DelUTie`. It uses `exists_admissible_family`, which needs `RayCharacterArtin`.

The other hypotheses pass unchanged. The called theorem gets the Selmer bound at auxiliary primes, the index bound for all powers and the isotypic direct sum, and ends with `exportAll_of_six_inputs`.

## In the Lean code

The theorem is in [TwistAllPowersOfGaloisCohomologyClassField.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistAllPowersOfGaloisCohomologyClassField.lean#L20). The main lemma is in [TwistTheoremAllPowersOfSelmerSupLattice.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistTheoremAllPowersOfSelmerSupLattice.lean#L24), and the Selmer statements are in [GaloisSideTwistedSelmerAuxiliaryPrimes.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/GaloisSideTwistedSelmerAuxiliaryPrimes.lean#L46). The conclusion is defined in [AdmissibleIndexBoundAllPowers.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/AdmissibleIndexBoundAllPowers.lean#L23). Each hypothesis is used.

The name `Gen.ArchimedeanSignatureMatching` is misleading. In [BlochKatoPhases.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BlochKatoPhases.lean#L400) it is a conjunction of a Poitou-Tate cokernel statement, a Sha statement, an $H^2$ duality statement and three local statements (finiteness, Tate duality, Euler characteristic). Nothing in it is archimedean. `SetHyp` ([line 327](lean:Formalism/SharpRestriction/LevelLetterCocycles/BlochKatoPhases.lean#L327)) begins with a conjunct `True`. The name `boundModTwoUniformizerAtTwo_of_chebotarev` speaks of the prime 2, but `ThmC` is the case $\nu > 0$; we have not checked if this means $\ell = 2$.
