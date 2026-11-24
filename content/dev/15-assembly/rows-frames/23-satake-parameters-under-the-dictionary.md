---
title: Satake parameters under the dictionary
decls:
  - UpperTheory.One.M.Sph.satAgree
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Satake parameters under the dictionary

This section proves the comparison of Satake parameters at the inert places that [the unitary reading](/entry/unitary-read-true-alt/) of the chapter on the unitary hypotheses uses. There an automorphic representation $\pi$ of a definite unitary group, given on a presented group, is moved by the dictionary of the CM field to a space $U$ of automorphic functions on the concrete unitary group. At a nonsplit place the reading needs two facts. If $\pi$ is spherical, then $U$ is unramified. A Satake parameter of $\pi$ for an inert datum is a Satake parameter of $U$. The proof is a comparison of the Hecke eigenvalues on the two sides.

### The setting

Let $L$ be a CM field with maximal real subfield $L^+$, and let $n \geq 1$. Let $U_n(\mathbb{A}_L)$ be the adelic points of the unitary group of rank $n$ for $L/L^+$, and let $U_n^{\mathrm{fin}}$ be the subgroup of points that are trivial at the archimedean places. A *presentation* $F$ consists of a ring isomorphism $\kappa$ from the tensor product of $L$ with the finite adeles of $L^+$ to the finite adeles of $L$, compatible with $L$ and with the completions, and a group map $j$ from a presented group $G_f$ onto $U_n^{\mathrm{fin}}$, whose local entries at each place $w$ are the entries of the matrix under $\kappa$.

Let $\pi$ be an automorphic representation of $G_f$, realized on a space $\pi_S$ of functions with values in a vector space $W$. Let $U$ be a space of functions on $U_n(\mathbb{A}_L)$. The pair $(\pi, U)$ is in the *dictionary* for $F$ if $U$ is an automorphic representation of the unitary group, and the pull back of $U$ along $j$ is spanned by the scalar functions $x \mapsto \lambda(f(x))$ for $f \in \pi_S$ and $\lambda$ a linear form on $W$.

Let $v$ be a finite place of $L^+$ and $w$ a place of $L$ over $v$. The representation $\pi$ is *spherical* at $v$ if it has a nonzero vector fixed by the maximal compact subgroup at $v$. The space $U$ is *unramified* at $w$ if it has a nonzero function fixed by the local points at $w$ whose matrices lie in $\mathrm{GL}_n(\mathcal{O}_w)$.

Let $s$ be a ring endomorphism of $L_w$ that extends the complex conjugation of $L$, let $\varpi \in L_w$ and $q \in \mathbb{N}$. The triple is an *unramified involution* if $s$ is an involution, $\varpi$ is a uniformizer fixed by $s$, and $q$ is the size of the residue field. An *inert datum* at $(v, w)$ is the local unitary group at $w$ in its standard form, with an involution $\sigma_w$ and a uniformizer $\varpi$. A vector $\alpha \in \mathbb{C}^{\lfloor n/2 \rfloor}$ is a *Satake parameter* of $\pi$ at an inert datum if a spherical vector of $\pi$ is an eigenvector of the spherical Hecke algebra with the eigenvalues of $\alpha$.

For $U$ the Satake parameter has a concrete form. A tuple $\alpha' \in (\mathbb{C}^\times)^{\lfloor n/2 \rfloor}$ is a *Satake parameter of $U$ at $w$* for $(s, \varpi, q)$ if there are $b \in \mathrm{GL}_n(\mathcal{O}_w)$ with

$$s(b)^{\mathsf{T}}\, b = J,$$

where $J$ is the antidiagonal form, the induced map $p$ from the local points of the unitary group at $w$ to the unitary group of $J$, given by $p(x) = b^{-1} x b$, and an irreducible smooth representation $\sigma$ of the unitary group of $J$ that occurs in $U$ along $p$ and is unramified with Satake parameter $\alpha'$ for $\varpi$ and $q$.

### The comparison

**Theorem 7.23.1 (Satake parameters agree under the dictionary).** Let $L$ be a CM field, $n \geq 1$, $F$ a presentation, and $(\pi, U)$ in the dictionary for $F$. Let $v$ be a finite place of $L^+$ and $w$ a place of $L$ over $v$. Then:

1. if $\pi$ is spherical at $v$, then $U$ is unramified at $w$;
2. let $(s, \varpi, q)$ be an unramified involution of $L_w$ that extends the complex conjugation of $L$. Then there is an inert datum at $(v, w)$ with $\sigma_w = s$ and the uniformizer $\varpi$. For each such inert datum and each Satake parameter $\alpha$ of $\pi$ there, every entry of $\alpha$ is nonzero, and $\alpha$ is a Satake parameter of $U$ at $w$ for $(s, \varpi, q)$.

Lean: `UpperTheory.One.M.Sph.satAgree`.

*Proof.* We take the steps in order.

1. The dictionary carries a spherical vector of $\pi$ to a nonzero function of $U$. By the local entries of the presentation, the maximal compact subgroup at $v$ goes to the points of $\mathrm{GL}_n(\mathcal{O}_w)$ in the unitary group at $w$. So this function is fixed by these points, and $U$ is unramified at $w$. This is part 1.
2. Let $(s, \varpi, q)$ be an unramified involution that extends the complex conjugation. Since $s$ is a nontrivial involution of $L_w$ over the completion of $L^+$, the place $w$ is inert and unramified over $v$, and $q$ is the residue size at $w$. The involution and the uniformizer give an inert datum with $\sigma_w = s$ and the uniformizer $\varpi$.
3. Fix such an inert datum and a Satake parameter $\alpha$ of $\pi$ there. The parameter comes with a spherical vector, so $\pi$ is spherical at $v$, and step 1 makes $U$ unramified at $w$.
4. The local unitary group at an unramified inert place of a definite unitary group has an unramified component in $U$. This gives a matrix $b$ and a representation $\sigma$ as in the definition, with a Satake parameter $\alpha_0$.
5. The spherical Hecke algebras on both sides are matched by the presentation. The Hecke eigenvalues of $\alpha$ for $\pi$ and of $\alpha_0$ for $\sigma$ agree, since both come from the same eigenvector through the dictionary.
6. The Satake transform of $\alpha_0$ is that of the unit tuple of an unramified character. Two tuples with the same transform have nonzero entries at the same time, so the entries of $\alpha$ are nonzero.
7. Let $\alpha'$ be the tuple of units with $\alpha'_i = \alpha_i$. The data $b$, $p$ and $\sigma$ of step 4 have the Hecke eigenvalues of $\alpha_0$, and by step 5 these are those of $\alpha'$. So $\alpha'$ is a Satake parameter of $U$ at $w$.

This proves the theorem. $\square$

In the unitary reading the involution and the uniformizer are produced at each inert place of the host field, which is unramified over its real subfield. The theorem then gives the inert datum, and the Satake parameter of $\pi$ at it becomes the Satake parameter of $U$. Part 1 is not used there, since the reading gets the parameter of $\pi$ from its own laws.

**Remark 7.23.2 (Formalization).** The theorem `satAgree` is at line 23 of [SphRead.lean](lean:Development/AutomorphicArithmetic/Foundations/UnitarySphericalFixing/SatakeParameters/SphRead.lean#L23). It restates `GlobalTheory.T.inert_satake_parameters_agree_under_dictionary` with the hypothesis `SphAtG π v`, which is `π.SphAt v` together with the goodness of $\pi$ at the split places when no split place lies over $v$; only the first part is used, by `hs.1`. The statement is a `first | exact` wrapper at line 11 of [InertSatakeParametersAgreeUnderDictionaryStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/InertSatakeParametersAgreeUnderDictionaryStatement.lean#L11) of `satake_agree` at line 18 of [InertSatakeParametersAgreeUnderDictionary.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/InertSatakeParametersAgreeUnderDictionary.lean#L18). Steps 1 to 7 are `isUnramified_of_sphericalVector_dictionary`, `inert_of_unramifiedIsometricInvolution`, `exists_inertDatum_of_involution_uniformizer`, `exists_satakeParameter_of_unramified_inert_definiteUnitary`, `inertSatake_heckeEigenvalues_algebraic_automorphic` and `satakeParameter_ne_zero_of_sameTransform`; we did not unfold them. The presentation `FinIso` and the dictionary `Dict` are at lines 14 and 29 of [FinIso.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/FinIso.lean#L14), and `IsUnramU` and `HasSatAt` are at lines 130 and 133 of [BaseChangeDefiniteUnitary.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/BaseChangeDefiniteUnitary.lean#L130). The caller at line 42 of [UnitaryReadTrue.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/UnitaryReadTrue.lean#L42) drops part 1 by the pattern `⟨-, hI⟩`.
