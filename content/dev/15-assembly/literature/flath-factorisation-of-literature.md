---
id: flath-factorisation-of-literature
title: Flath factorisation with one-dimensional spherical lines, from the literature
kind: theorem
decl: UpperTheory.LiteratureTheorems.flath_factorisation_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 775
status: drafted
drafted_by: writer@claude
---
This theorem gives the factorisation of an irreducible unitary representation of an adelic unitary group into local pieces. It takes the argument $O$ of type [OpenLiteratureStatements](/step/open-literature-statements-def/) and ignores it. It is one of the cited results that the main theorem [every character of the literature](/step/every-character-of-literature/) uses. Unlike its neighbours it is not a pure renaming: it joins two cited statements with a short argument of its own. Its result fills the field `flath` of three bundles: `published_results_analytic`, [UnitaryGroupThirdPlaceHypotheses](/step/published-results-eigen/) and [ThetaLocalInputs](/step/published-results-first/).

## Statement

Let $E/F$ be a CM extension, $J$ a nondegenerate Hermitian matrix of size $n$, and $G = U(J)$. Let $\pi$ be an irreducible unitary representation of $G(\mathbb{A}_F)$ on a Hilbert space $H$. Then there are, for each place $v$, an irreducible unitary representation $R_v$ of $G(F_v)$ and a vector $\xi_v$, and a map $B$ from the family of local vectors to $H$, such that:

1. $B$ identifies $\pi$ with the restricted tensor product of the $R_v$ with respect to the $\xi_v$;
2. at each finite place, the smooth part of $R_v$ is irreducible and admissible;
3. for each lattice $L$, for almost all finite $v$, the vectors of $R_v$ fixed by the stabilizer of $L$ in $G(F_v)$ form the line $\mathbb{C}\,\xi_v$.

This has the form of the theorem of Flath (Proc. Sympos. Pure Math. 33, part 1, 1979) for unitary groups.

## Proof

The proof is `PositivityTheory.Prw.flathFactorisation_of` applied to two other theorems of the same file. They also ignore $O$:

- `flath_tensor_product_of_literature` gives the factorisation in part 1 only. It cites `CompanionTheory.Rg.Fl.B.flathTensorProduct`.
- `unitary_irreducible_admissible_of_literature` says that, at a finite place, the fixed vectors of a compact open subgroup in an irreducible unitary representation form a finite-dimensional space. It cites `CompanionTheory.Rg.Fl.B.unitaryIrreducibleAdmissible`.

The bridge `flathFactorisation_of` is the theorem `GlobalTheory.flathFactorisation_of_tensorProduct`. Its proof has three steps:

1. The second input and `GlobalTheory.T.unitary_irreducible_smooth_admissible` make the smooth part of each finite factor irreducible and admissible.
2. The factorisation gives $\lVert \xi_v \rVert = 1$ and $\xi_v$ fixed by the stabilizer of $L$, for almost all $v$. So the fixed space contains the nonzero smooth vector $\xi_v$.
3. For almost all $v$, `GlobalTheory.T.eventually_exists_doubleCoset_antiInvolution_unitary` gives an anti-involution that fixes each double coset of the stabilizer. Then `GlobalTheory.T.gelfand_pair_spherical_vector_unique` (Gelfand's trick) says that the fixed space is at most one-dimensional. So it is the line $\mathbb{C}\,\xi_v$.

I have not unfolded the two cited statements of step 3.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L377). The statement `FlathFactorisation` is at [ExistsFactorisationCuspidal.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/ExistsFactorisationCuspidal.lean#L36). The bridge is at [FlathFactorisationOfTensorProduct.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/FlathFactorisationOfTensorProduct.lean#L15).

- The argument $O$ is not used.
- The two inputs are at lines 373 and 375 of the same file.
- `IsFactorisation` is the restricted tensor product condition `IsRestrTensor`. I have not unfolded it.
