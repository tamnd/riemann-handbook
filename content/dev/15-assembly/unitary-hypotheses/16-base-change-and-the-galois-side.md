---
title: Base change and the Galois side
decls:
  - Formalism.MainNotions.AdmissibleThreePrime.theorem_three_prime_holds_alt_alt
  - Formalism.MainNotions.AdmissibleThreePrime.residual_irreducible_of_theorem_three_prime_alt
  - UpperTheory.One.M.unitaryRead_true_alt
  - GlobalTheory.T.unitary_of_local_langlands'
  - UpperTheory.BaseChangeIdentities.aux_of_cgTrue_of_auTrue
  - UpperTheory.BaseChangeIdentities.Conclusion1_alt_alt_alt
  - GlobalTheory.GalLoc.galLoc_triple_at_place_alt
  - GlobalTheory.GalLoc.galois_side_at_place_alt
  - GlobalTheory.T.exists_galSide_cf_eq_cgTrue_at_members
  - GlobalTheory.LiftRef.baseChange_local_compatible_all_places_alt
  - GlobalTheory.T.liftAll_of_parIn_of_mtInput
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Base change and the Galois side

This section proves the last outputs that [the record of hypotheses](/entry/hypotheses-nonempty-of-unramified-exponents-alt/) of Section 1 uses. There are four: residual irreducibility from Theorem 3', [base change](/learn/automorphic-forms/#base-change) from a definite unitary group to $\mathrm{GL}_n$, a Galois side at each layer point, and the local compatibility of the lift at all places. Residual irreducibility enters the admissible datum of Section 13. The other three are statements on the automorphic side and the Galois side of a datum.

We keep the notation of Sections 12 to 15. A datum $D$ has a CM field $E$ over $F$, type primes $g_0$ and $g_1$, ranks $r$, $t$ and $n_V$, and indices $i$ with primes $\ell_i$. For each $i$ of type HG and each residual representation $\bar\rho$ of rank $r$ at $i$, a character $\chi_1$ and a tame element $\gamma_0$ of inertia at the places over $g_k$ are given.

**Definition 8.16.1 (Residual irreducibility of rank $r$).** For $N \ge 1$ and a prime $g$, let $\mathrm{BB}(N, g)$ be the set that contains $g$ and the primes $\ell$ that are exceptional for $g$ and some $d \le N$. The datum $D$ has *residual irreducibility of rank $r$* if for each $i$ of type HG and each residual $\bar\rho$ at $i$:

1. $\bar\rho$ is absolutely irreducible;
2. at each place $v$ over $g_k$ with $g_k \neq \ell_i$, the value $\chi_1(\gamma_0)$ is not a root of the characteristic polynomial of $\bar\rho(\gamma_0)$.

*Theorem 3'* at $D$ says: if $\mathrm{BB}(r, g_0)$ and $\mathrm{BB}(r, g_1)$ are disjoint, then for each $i$ and each eigensystem $\Sigma$ with a parameter, the depth zero degree condition and the good condition, the parameter is cuspidal, and for each $\rho$ that represents $\Sigma$:

1. the reduction of $\rho$ is irreducible;
2. if $\ell_i \notin \mathrm{BB}(r, g_k)$, the reduction is irreducible on each open normal subgroup with solvable quotient that contains the inertia at $g_k$;
3. $\chi_1(\gamma_0)$ is not a root of the characteristic polynomial of the reduction at $\gamma_0$.

**Theorem 8.16.2 (Theorem 3').** Let $D$ be a datum with the label tie and the admissibility of the residual tame eigenvalues. Then Theorem 3' holds at $D$.

Lean: `Formalism.MainNotions.AdmissibleThreePrime.theorem_three_prime_holds_alt_alt`.

*Proof.* Let $\Sigma$ and $\rho$ be as in the statement. The label tie gives the cuspidal parameter. Since $\mathrm{BB}(r, g_0)$ and $\mathrm{BB}(r, g_1)$ are disjoint, $\ell_i$ is outside one of them, say $\mathrm{BB}(r, g_k)$. At this $k$, the local parameter at the place over $g_k$ is tame of depth zero with a regular part of degree $r$. Its eigenvalues on $\gamma_0$ generate an extension of $\mathbb{F}_{\ell_i}$ of degree at least the length of each orbit of Frobenius, since $\ell_i$ is not exceptional for $g_k$ and $d \le r$. So any invariant subspace of the reduction would have a degree that no orbit allows, and the reduction is irreducible, also on the open normal subgroups of the statement. The tame eigenvalue condition gives part 3. $\square$

**Corollary 8.16.3 (Residual irreducibility).** Let $D$ be a datum with the label tie, the admissibility of the residual tame eigenvalues, the fifth admissibility condition, the Brauer-Nesbitt input, the global residual condition and the depth zero condition. Then $D$ has residual irreducibility of rank $r$.

Lean: `Formalism.MainNotions.AdmissibleThreePrime.residual_irreducible_of_theorem_three_prime_alt`.

*Proof.* The *Brauer-Nesbitt input* says: if two representations have the same characteristic polynomials and one is irreducible, so is the other. The fifth admissibility condition gives the disjointness of $\mathrm{BB}(r, g_0)$ and $\mathrm{BB}(r, g_1)$ and, by Chebotarev density, a representation $\rho$ of $\Sigma$ with the same characteristic polynomials as $\bar\rho$. The Theorem (Theorem 3') makes the reduction of $\rho$ irreducible, and the Brauer-Nesbitt input moves this to $\bar\rho$. Part 2 is part 3 of Theorem 3'. $\square$

Now base change. Let $\mathrm{AU}_j$ be the automorphic representations of the unitary group $U(V_j)$ of the datum. An *automorphic side* $A$ of $D$ classifies $\mathrm{AU}_j$ by cuspidal data; it is *realized* if for each $\pi$ and each split place $w$ the local component $\pi_w$ corresponds under $h_L$ and the Weil-Deligne tie $T$ to the local component of its class. The *unitary reading* says: for each $j$ and each $\pi \in \mathrm{AU}_j$ there is an automorphic $U$ on $\mathrm{GL}_{n_V}$ over $E$ such that

$$\begin{aligned} &\pi_w \text{ corresponds to } U_w \text{ at each split } w, \\ &\text{the Satake parameters agree at each nonsplit spherical } w, \\ &\text{the infinitesimal character of } \pi_\tau \text{ is that of a weight } \lambda \text{ at each } \tau. \end{aligned}$$

**Theorem 8.16.4 (The unitary reading).** Let $h_L$ witness [the local Langlands recursion](/step/rect-exists-def/), let $D$ be a datum, $T$ a Weil-Deligne tie and $A$ a realized automorphic side. Then the unitary reading holds.

Lean: `UpperTheory.One.M.unitaryRead_true_alt` (also `GlobalTheory.T.unitary_of_local_langlands'`, a second name).

*Proof.* Let $\pi \in \mathrm{AU}_j$. The automorphic side is surjective, so $\pi$ comes from a class $\pi_0$. The finite adelic points of $U(V_j)$ have a presentation, and the dictionary of the CM field gives an automorphic $U$ on $\mathrm{GL}_{n_V}(\mathbb{A}_E)$ with the class of $\pi_0$. At split places the realization gives the local components. At nonsplit spherical places the Satake parameters of $\pi$ and $U$ agree, since both are read off the same class. The weight comes from the contragredient of the algebraic representation at $\tau$. $\square$

The base change conclusion needs three inputs from the representation theory of $\mathrm{GL}_n$. The *generic unitary dual* says that a generic unitary representation of $\mathrm{GL}_n$ is a fully induced product of segments. The *standard cosocle* says that a standard module has a unique irreducible quotient, as in the Langlands classification of $\mathrm{GL}_n$. The *definite base change input* says: for a CM field $E$ with $E/E^+$ unramified at all finite places and $n \ge 1$, each automorphic $\pi$ of $U(n)$ has base change data, a partition of $n$ with cusp forms on $\mathrm{GL}_{N_i}$, local components and infinitesimal characters.

**Definition 8.16.5 (The first conclusion).** The *first conclusion* at $D$ says: if $E$ is generated by $F$ and a CM field $K$ and the CM hypothesis holds, then for each $j$ with $V_j$ definite and $n_V \ge 1$, each $\pi \in \mathrm{AU}_j$ that is spherical and inert has a base change.

**Theorem 8.16.6 (Base change from the definite group).** Assume the definite base change input, the generic unitary dual of $\mathrm{GL}_n$ and the standard cosocle. Let $h_L$, $D$, $T$ and $A$ be as above, and assume that the cuspidal data of $D$ are realized under $h_L$ and $T$. Then the first conclusion holds at $D$.

Lean: `UpperTheory.BaseChangeIdentities.Conclusion1_alt_alt_alt`, `UpperTheory.BaseChangeIdentities.aux_of_cgTrue_of_auTrue`.

*Proof.* For a totally complex field the normalized cusp forms of $\mathrm{GL}_N$ embed in the discrete spectrum, and their Speh components exist. The generic unitary dual and the standard cosocle give three recursion laws for the local Langlands recursion: for products, for Speh representations and for Satake parameters. The realization of the cuspidal data reads each cusp form through the recursion. The Theorem (The unitary reading) gives the reading of each $\pi$. The definite base change input, the three laws, the reading of the cusp forms and the unitary reading give the base change of a spherical inert $\pi$. $\square$

The *cuspidal data realized* condition says: there is an embedding $e$ of the cuspidal data of rank $a$ of $D$ into the cusp forms of $\mathrm{GL}_a(\mathbb{A}_E)$, onto the good ones, compatible with $h_L$ at the good places, with twists, with infinitesimal characters and with conjugate self-duality. A *Galois side* of a datum is a record of a Weil-Deligne tie $T$, label truth, a character frame with its character side, the Galois triple condition, a $\lambda$ datum with its tie, the bound $r \ge 100$ and $2r \le g_k$.

**Theorem 8.16.7 (The Galois triple at layer points).** Assume the published inputs of the third layer and the local Selmer input. Let $h_L$ be as above, and assume four properties at every layer point: eigenvalue truth and occurrence on the rows with localization, a coefficient field with the roots of unity of order $g_k(g_k - 1)$ that is closed under complex conjugation, parameters on the rows, and commutation and fullness. Then at every layer point the datum satisfies the Galois triple condition.

Lean: `GlobalTheory.GalLoc.galLoc_triple_at_place_alt`.

*Proof.* Properties at every layer point join, and the residual ties of the third layer inputs hold at every layer point. At a point, the four properties and the residual ties give a Hecke character at each index that reads the twist, then the Galois triple with localization. It comes from the [[Galois representation|JQEYEQJY2G]]s of the cusp forms of the point, a generic type that meets the good forms, the eigensystem of the good part, and the export of eigenvalues by Chebotarev density and Artin reciprocity. $\square$

**Theorem 8.16.8 (The Galois side at layer points).** Assume the published inputs of the third layer and the local Selmer input. Let $h_L$ be as above. Then at every layer point there is a Galois side $G$ of the datum whose character frame and $\lambda$ frame are the frame of the point, and whose Weil-Deligne tie has realized cuspidal data under $h_L$.

Lean: `GlobalTheory.GalLoc.galois_side_at_place_alt` (also `GlobalTheory.T.exists_galSide_cf_eq_cgTrue_at_members`, a second name).

*Proof.* The four properties of the Theorem (The Galois triple at layer points) hold at every layer point by the third layer inputs and the local Selmer input, so the Galois triple condition holds. Eventually the sizes, the congruences, the host facts and the column choices hold at every layer point. With rank at least $100$, a joined model gives the Galois side. $\square$

**Definition 8.16.9 (The lift at all places).** Let $D$ be a datum and $R_w$ a row side. The *lift at all places* says: for each $j$ and each $\sigma$ with nonzero isotypic part there are $\pi$ and $\mu$ such that $\pi$ is conjugate self-dual, unramified and spherical where $\sigma$ is, the infinitesimal character of $\pi$ is the shift of that of $\sigma$ by $\mp\frac12$, and at each split place

$$\pi_w \cong \bigl(\mathrm{lp}(\sigma_w) \boxplus \mathrm{Speh}(\mu, t)\bigr) \otimes \eta^{-1},$$

where $\mathrm{lp}$ is the local lift of the parameter and $\eta$ the infinitesimal twist.

**Theorem 8.16.10 (Base change compatible at all places).** Assume the published inputs of the third layer. Let $h_L$ be as above. At every layer point, for each row side $R_w$ with the parity conditions and each choice of members with the stability and input conditions, the lift at all places holds.

Lean: `GlobalTheory.LiftRef.baseChange_local_compatible_all_places_alt` (also `GlobalTheory.T.liftAll_of_parIn_of_mtInput`, a second name).

*Proof.* Four facts at every layer point join: the infinitesimal characters at $\tau$ and $\bar\tau$ are $-\frac12$ and $\frac12$; base change is compatible with local Langlands at the trivial twist; the spherical inert classes are kept under isomorphism of types; and base change is compatible with infinitesimal characters. At each $\sigma$ they give $\pi$, $\mu$ and the local formula. $\square$

**Remark 8.16.11 (Formalization).** Theorem 3' is at [TheoremThreePrimeHolds.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TheoremThreePrimeHolds.lean#L12) and the corollary at [ResidualIrreducibleOfTheoremThreePrime.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ResidualIrreducibleOfTheoremThreePrime.lean#L12); the key lemma is `Formalism.CyclotomicNorms.irreducibility_of_good_tuple`, and we did not unfold the exceptional primes `Exc`. The unitary reading is at [UnitaryReadTrue.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/UnitaryReadTrue.lean#L20). It takes an argument of type `TrivialCondition`, which is `True` ([SwOn.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SwOn.lean#L5)), and its second name at [UnitaryOfLocalLanglands.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/UnitaryOfLocalLanglands.lean#L15) passes `trivial`; that name speaks of local Langlands, but no such input is taken. Base change is at [Auxiliary.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Auxiliary.lean#L16) and [BciNarrowAux.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BciNarrowAux.lean#L38); the input `BernsteinUnitaryProductIrreducible` of the top theorem is not used, and the embedding of cusp forms `AscComp` is proved as `ascComp`. The realized conditions are `CGTrueT` and `AutomorphicSideRealised`, and the Galois side is `GalSideAlt`. The Galois results are at [GalLocTripleWithLocalization.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GalLocTripleWithLocalization.lean#L65), lines 65, 115 and 133; in the first, the local Selmer input is a hypothesis that the proof does not use. We did not unfold `IsGaloisTriple`. The lift at all places is `LiftAll` with `LiftAt` (CenLocOfCenReal.lean, line 62), and the theorem is at [BaseChangeLocalCompatibleAllPlaces.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BaseChangeLocalCompatibleAllPlaces.lean#L20), lines 20 and 35.
