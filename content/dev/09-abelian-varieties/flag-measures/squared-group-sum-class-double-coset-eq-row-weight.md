---
id: squared-group-sum-class-double-coset-eq-row-weight
title: The squared group sum of one class and one double coset
kind: theorem
decl: GlobalTheory.FamilyNormRational.squaredGroupSum_classDoubleCoset_eq_rowWeight
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.FamilyGroupSumFactorsRowWeightAmplitudeProof
covers: 925
status: drafted
drafted_by: writer@claude
---
Sum the term vectors of one class, at one point, in one rational double coset. The squared norm of this sum, divided by an archimedean factor, is the squared row weight times the squared local amplitude. This is clause 4 of [`familyGroupSumFactorsRowWeightAmplitude`](/entry/family-group-sum-factors-row-weight-amplitude/).

## Statement

Fix $D, X, Y, u, u'$ as in [`rowsPos_typeP`](/entry/rows-pos-type-p/). Each term $t$ of `Y.tO u u'` has a vector $v(t)$, a row $j(t)$, a row weight $w(t)$ (`TermOp.wt`), a point $\pi(t)$ (`ptPN`) and a linear map $\ell(t)$. Its rational double coset is $\nu(t) = N(F_u) \, \ell(t) \, N(F_{u'})$ (`nmlOf`), with $N(F)$ the isometries unipotent along $F$ (`NRat`).

A family is:

- $S \colon \mathrm{Prop} \to \mathrm{Prop}$, $T_S = \{t : G(t) \neq 0,\ S(t \text{ not generic})\}$, and a map $\mathrm{cls}$ on $T_S$ whose classes are rows in each double coset (`FamQ`).
- A point $\gamma$ with a term $t_1 \in T_S$, $\pi(t_1) = \gamma$, $v(t_1) \neq 0$ (`HasPt`).
- A local family $F_m$ (`LocFam`): finite sets $\Omega \subseteq P$ of places, weights $\mathrm{rw}(c)$, and a partial map $\mathrm{dat}$ from (class, coset) to tuples $d = (d_p)_{p \in P}$ of local data. By `FamTie`, $\mathrm{dat}(c, n)$ is defined if and only if some $t \in T_S$ has class $c$, point $\gamma$ and coset $n$; then each such $t$ lies over the local orbits of $d$, and $w(t)^2 = \mathrm{rw}(c)$.

Put $\Sigma(c, n) = \sum v(t)$ over these $t$. Let $J(\nu, z)$ (`Jw`) be a constant times the operator `OO` of $\nu$ at the archimedean point $\gamma_z$ of $z$, and $J^2(\nu, \gamma) = \lVert J(\nu, z) \rVert_{\mathrm{HS}}^2$ for a point $z$ over $\gamma$ with a representative (else $0$). The local amplitude is $A_S(d) = \sum_{A} \prod_{p \in A} a^{N}_p(d_p) \prod_{p \notin A} a^{Z}_p(d_p)$, over $A \subseteq \Omega$ with $S(A \neq \emptyset)$, where $a^N_p, a^Z_p$ are local amplitudes (`LocNG.amp`).

**Theorem.** Assume `Stand`, $4r + 7 \leq k$, `ConcTie`, a pinned family $\nu$ (`NuQPin`), and $s > 0$ with $s(\gamma_z) = g^{-f \lvert \mathrm{FreeE}(z) \rvert}$ at each point $z$ with a representative. Then for each family, class $c$ and coset $n$ (sides `a2F` and `a2W`):
$$\frac{\lVert \Sigma(c, n) \rVert^2}{J^2(s\nu, \gamma)} = \begin{cases} 0 & \mathrm{dat}(c, n) \text{ undefined}, \\ \mathrm{rw}(c) \, \lvert A_S(d) \rvert^2 & \mathrm{dat}(c, n) = d. \end{cases}$$

## Proof

If $\mathrm{dat}(c, n)$ is undefined, the sum is empty and both sides are $0$. Else take a term $t_0$ of the sum, and the base flags $F_{00}, F'_0$ and point $z$ of `FamTie`.

1. `nonGeneric_family_classes_determine_rows` makes $t_1$ relevant, and `terms_at_point_of_relevant_term_relevant_finite` puts all terms at $\gamma$ at $z$. `gPoint_eq_gval` gives $G(F_{00}, F'_0) \neq 0$; `localisedBaseFrames_relevantPair` gives `RelG`.
2. `exists_global_coordinates_rational_flagPair` gives global frames; `term_moves_to_baseFrames_up_to_unitriangular` moves $t_0$ to them.
3. $\Sigma$ runs over the $t$ with the row and coset of $t_0$ and $S(t \text{ not generic})$, by `FamQ`, `doubleCoset_eq_iff_isometry_unipotent_translate` and `flagTerm_invariants_const_on_rationalDoubleCoset`.
4. The lemma `globalAmplitude_eq_localAmplitudes` gives $\lVert A_{\mathrm{glob}} \rVert = \lvert A_S(d) \rvert$. By `row_doubleCoset_sum_norm_sq_bound`,
   $$\lVert \Sigma \rVert^2 = w(t_0)^2 \, \lVert A_{\mathrm{glob}} \rVert^2 \, g^{-2f \lvert \mathrm{FreeE}(z) \rvert} \, \lVert J(\nu, z) \rVert^2.$$
5. `Jw_sc` gives $J^2(s\nu, \gamma) = s(\gamma_z)^2 \lVert J(\nu, z) \rVert^2 = g^{-2f \lvert \mathrm{FreeE}(z) \rvert} \lVert J(\nu, z) \rVert^2$. Here $J(\nu, z) \neq 0$, since else `rowTerm_amplitude_eq_mass_mul_phase` gives $v(t_1) = 0$. Divide, and use $w(t_0)^2 = \mathrm{rw}(c)$.

## In the Lean code

The theorem is in [FamilyGroupSumFactorsRowWeightAmplitudeProof.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/FamilyGroupSumFactorsRowWeightAmplitudeProof.lean#L50). `a2F`, `ampQ` and `FamQ` are in [LocOf.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/LocOf.lean#L16), `a2W` and `LocFam` in [NGLocModel.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/NGLocModel.lean#L80), `FamTie` in [FamDefs.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FamDefs.lean#L91).

- The name `row_doubleCoset_sum_norm_sq_bound` says "bound", but its statement is an equality.
- We have not unfolded `OO`, `FreeE`, `gamW`, `IsPtRep`, `BBne` or `LocNG.amp`.
