---
title: Theta maps and the Hodge bundle
decls:
  - GlobalTheory.T.theta_map_pull_O1_power
  - GlobalTheory.ThetaPullback.theta_pull_O1_pow
  - GlobalTheory.T.theta_map_pull_O1_power_hodge
  - GlobalTheory.UMin.KeyOne.lbIso_pull_O1_hodge
  - GlobalTheory.T.thetaKeyFormula_normalCover_rational_thetaConstants
  - GlobalTheory.UMin.key_on_cover
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta maps and the Hodge bundle

This section proves that a theta map from $X_F$ to projective space pulls back $\mathcal{O}(1)$ to a power of the Hodge bundle on each model of $X_F$. This gives item 3 of a minimal compactification in Section 2, with the integer $N$. The theta map sends a point to the symmetric functions of its theta constants. On a cover where the theta constants are rational, the key formula for theta functions gives the relation between $\mathcal{O}(1)$ and the Hodge bundle. Then a norm argument descends the relation, and a density argument extends it from the rational components to the whole model. We use the notation of Section 1. $X$ is a moduli scheme for $D$ and $l$ with the universal semi-abelian datum $(G, L)$ and its rigidification, $F$ is a coefficient field, and we put $g = \tfrac{[E:\mathbb{Q}]}{2}(p + q)$. The fibres of $G$ over $X$ are abelian varieties of dimension $g$.

**Definition 7.8.1 (Theta list, theta map).** Let $m \ge 1$ and $N \ge 1$.

1. Let $K$ be a field, $x : \operatorname{Spec} K \to X$ a point and $\theta$ a section of $L$ on the fibre $G_x$. A *theta list* of level $m$ for $\theta$ consists of $N$ distinct points $\mathrm{pt}_1, \dots, \mathrm{pt}_N$ of $G_x$ over $K$ and values $c_1, \dots, c_N \in K$, such that $c_a$ is the theta value of $\theta$ at $\mathrm{pt}_a$ for each $a$, and such that for each algebraically closed field $K' \supseteq K$, each point $P$ of $G_x$ over $K'$ with $P^{m^2} = 1$ is one of the $\mathrm{pt}_a$.
2. A tuple $c \in K^N$ is a *tuple of theta constants* of level $m$ at $x$ if there are a generating section $\theta$ and points $\mathrm{pt}_a$ that form a theta list with values $c$.
3. For $c \in R^N$, the *symmetric tuple* $\operatorname{sym}(c) \in R^N$ has the entries $\operatorname{sym}(c)_k = e_k(c)^{N!/k}$ for $k = 1, \dots, N$, where $e_k$ is the $k$-th elementary symmetric function.
4. Let $o$ be a ring and $n \ge 0$. A map $f : X_F \to \mathbb{P}^n_o$ is a *theta map* of level $m$ if, for each field $K$, each point $x : \operatorname{Spec} K \to X_F$ and each tuple $c \in K^{n+1}$ of theta constants of level $m$ at the image of $x$ in $X$, the point $f \circ x$ has the projective coordinates $\operatorname{sym}(c)$.

Lean: `GlobalTheory.ThMap` (also `GlobalTheory.HasTh`, `GlobalTheory.ThList`, `GlobalTheory.symTup`).

The entry $e_k(c)^{N!/k}$ is homogeneous of degree $N!$ in $c$. So $\operatorname{sym}(c)$ does not depend on the order of the points, and a scalar $\lambda$ multiplies it by $\lambda^{N!}$. A change of the generating section $\theta$ by a unit thus gives the same projective point. The $m^2$-torsion of an abelian variety of dimension $g$ over an algebraically closed field of characteristic prime to $m$ has $m^{4g}$ points. So a theta list of level $m$ has at least $m^{4g}$ entries, and the theorems below take $n + 1 = m^{4g}$.

**Definition 7.8.2 (Hodge bundle).** Let $G \to S$ be a group scheme whose sheaf $\omega_G$ of invariant differentials is a vector bundle of rank $g$. The *Hodge bundle* is the line bundle $\det \omega_G = \bigwedge^g \omega_G$ on $S$.

Lean: `GlobalTheory.SiegelTor.hodge`.

For a model $Y$ of $X_F$ the datum on $Y$ has $\omega_G$ of rank $g$, and its Hodge bundle is isomorphic to $\omega_Y$ of Section 1 when $\omega_Y$ is a line bundle. See [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures) for the Hodge bundle on moduli of abelian varieties.

In the three theorems below, let $o$ be a ring, $m$ an odd integer with $m \ge 3$ that is a unit in $o$, and $n$ an integer with $n + 1 = m^{4g}$. Let $f : X_F \to \mathbb{P}^n_o$ be a theta map of level $m$. Let $Y$ be a model of $X_F$ over $\mathrm{id}_F$, with the open immersion $j$ and the semi-abelian datum $G$, and let $g_Y : Y \to \mathbb{P}^n_o$ be a map with $g_Y \circ j = f$. We write $\omega_G$ for the Hodge bundle of $G$ on $Y$.

**Theorem 7.8.3 (Key formula on a normal cover).** Let $\Omega$ be a field of characteristic $0$ over $F$, $M$ a model over $(F, \Omega)$ with $Z_M$ normal, $\pi : Z_M \to Y$ a map, $y : \operatorname{Spec} \Omega \to X_F$ a point with $\pi \circ \mathrm{pt}_M = j \circ y$, and $d \in \Omega^{n+1}$ a tuple of theta constants of level $m$ at $y$. Then
$$\pi^* \big( g_Y^* \mathcal{O}(1) \big)^{\otimes 8} \cong \pi^* \omega_G^{\otimes 4 (n+1)!}.$$

Lean: `GlobalTheory.UMin.key_on_cover` (also `GlobalTheory.T.thetaKeyFormula_normalCover_rational_thetaConstants`, a second name).

*Proof.* Pull the datum $G$ back to a datum $t$ on $Z_M$.

1. Since $f$ is a theta map, the point $g_Y \circ \pi \circ \mathrm{pt}_M = f \circ y$ has projective coordinates $\operatorname{sym}(d)$. Then $M$ has divisors for $\operatorname{sym}(d)$ in the sense of Section 7, and so $M$ has divisors for $d$, because $Z_M$ is normal and $\operatorname{sym}(d)$ consists of powers of the symmetric functions of $d$.
2. The tuple $d$ gives a map $h : Z_M \to \mathbb{P}^n_F$ with coordinates $d$ at $\mathrm{pt}_M$. Since $\operatorname{sym}$ is homogeneous of degree $(n+1)!$, we get $(g_Y \circ \pi)^* \mathcal{O}(1) \cong h^* \mathcal{O}(1)^{\otimes (n+1)!}$.
3. The theta constants and the principal polarization of dimension $g$ move along the maps of semi-abelian data from $X_F$ to $Y$ and from $Y$ to $Z_M$. So $d$ is a tuple of theta constants for $t$ at $\mathrm{pt}_M$, and the fibre of $t$ at $\mathrm{pt}_M$ is principally polarized of dimension $g$. As $m \ge 3$, $m$ is a unit in $F$. A lemma then gives a section $\sigma$ of the pullback of $\mathcal{O}(1)$ by $h$ whose coordinates are theta functions.
4. The abelian locus of $t$ is the preimage of $j(X_F)$. It is open, it contains $\mathrm{pt}_M$, and the polarization is principal on it. The group $t$ is smooth of relative dimension $g$, by base change from $Y$. The scheme $Z_M$ is locally noetherian, its ring of global sections has characteristic $0$, and each residue field has cardinality at most that of $\mathbb{C}$, because $F \subseteq \mathbb{C}$.
5. If $g \ge 1$, the key formula for theta functions applies to $t$, $\sigma$ and $h$, and it gives $h^* \mathcal{O}(1)^{\otimes 8} \cong \omega_t^{\otimes 4}$. If $g = 0$, then $n = 0$, the class of $\omega_t$ in the Picard group is $0$, and so is the class of $\mathcal{O}(1)$ on $\mathbb{P}^0_F$. So the isomorphism holds again.
6. The Hodge bundle of $t$ is $\pi^* \omega_G$. With step 2, in the Picard group of $Z_M$ we get
$$\begin{aligned} 8 \, [\pi^* g_Y^* \mathcal{O}(1)] &= 8 \,(n+1)! \, [h^* \mathcal{O}(1)] \\ &= 4 \,(n+1)! \, [\omega_t] = 4 \,(n+1)! \, [\pi^* \omega_G]. \end{aligned}$$

This is the claim. $\square$

The key formula of step 5 is the *formule clé* of Moret-Bailly (L. Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque 129, 1985). It compares the determinant of the theta sections with the Hodge bundle, see [the algebraic theory of theta functions](/learn/theta-functions-cm/#the-algebraic-theory-of-theta-functions).

**Theorem 7.8.4 (Theta map and the Hodge bundle on rational components).** Let $\Omega$ be a field over $F$, $M$ a model over $(F, \Omega)$ and $i_M : Z_M \to Y$ an open immersion over $F$. Then
$$i_M^* \big( g_Y^* \mathcal{O}(1) \big)^{\otimes 8 (n+1)!} \cong i_M^* \omega_G^{\otimes 4 (n+1)! (n+1)!}.$$

Lean: `GlobalTheory.UMin.KeyOne.lbIso_pull_O1_hodge` (also `GlobalTheory.T.theta_map_pull_O1_power_hodge`, a second name).

*Proof.* The field $\Omega$ has characteristic $0$, since $F$ does. The scheme $Z_M$ is normal, as an open subscheme of the normal scheme $Y$.

1. The generic point of $Z_M$ maps into $j(X_F)$, so $i_M \circ \mathrm{pt}_M = j \circ y$ for a point $y : \operatorname{Spec} \Omega \to X_F$. The fibre of $G$ at $y$ is principally polarized of dimension $g$, so it has a generating section $\theta$ that stays generating under each field extension.
2. A lemma on theta constants gives a finite Galois extension $\Omega'$ of $\Omega$ whose degree divides $(n+1)!$, with a theta list for $\theta$ over $\Omega'$ with values $d \in \Omega'^{n+1}$.
3. The normalization of $Z_M$ in $\Omega'$ gives a model $M'$ over $(F, \Omega')$ with $Z_{M'}$ normal and a finite map $\pi : Z_{M'} \to Z_M$ of models.
4. The theorem on the key formula on a normal cover, for $M'$, $i_M \circ \pi$, the point $y$ over $\Omega'$ and $d$, gives $\pi^* i_M^* (g_Y^* \mathcal{O}(1))^{\otimes 8} \cong \pi^* i_M^* \omega_G^{\otimes 4(n+1)!}$.
5. A norm lemma says that for line bundles $A, B$ on the normal scheme $Z_M$, an isomorphism $\pi^* A \cong \pi^* B$ gives $A^{\otimes k} \cong B^{\otimes k}$ when the degree of $\Omega'$ over $\Omega$ divides $k$. With $k = (n+1)!$, this gives the claim. $\square$

**Theorem 7.8.5 (Pullback of $\mathcal{O}(1)$ by a theta map).** Suppose that $\omega_Y$ is a line bundle. Then
$$\big( g_Y^* \mathcal{O}(1) \big)^{\otimes 8 (n+1)!} \cong \omega_Y^{\otimes 4 (n+1)! (n+1)!}.$$

Lean: `GlobalTheory.ThetaPullback.theta_pull_O1_pow` (also `GlobalTheory.T.theta_map_pull_O1_power`, a second name).

*Proof.* $Y$ is projective over $F$, so it is proper over $F$, and it is normal, separated, locally of finite type and quasi-compact. Both sides of the theorem on rational components are line bundles. A lemma on rational components says the following. Let $k$ be a field of characteristic $0$ and $Y$ such a scheme over $k$. If two line bundles $A$ and $B$ on $Y$ become isomorphic after pullback along each open immersion $i_M : Z_M \to Y$ over $k$ from a model $M$ over $(k, \Omega)$, then $A \cong B$. The previous theorem gives these isomorphisms with $A = (g_Y^* \mathcal{O}(1))^{\otimes 8(n+1)!}$ and $B = \omega_G^{\otimes 4(n+1)!(n+1)!}$. So $A \cong B$. Since $\omega_Y$ is a line bundle, it is isomorphic to the Hodge bundle $\omega_G$. So $B \cong \omega_Y^{\otimes 4(n+1)!(n+1)!}$. $\square$

In Section 9 this theorem gives item 3 of a minimal compactification with $N = 4 (n+1)! (n+1)!$.

**Remark 7.8.6 (Formalization).** The proofs are in [ThetaKeyFormulaNormalCoverRationalThetaConstants.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyFormulaNormalCoverRationalThetaConstants.lean#L53), [ThetaMapPullO1PowerHodge.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaMapPullO1PowerHodge.lean#L81) and [ThetaMapPullO1Power.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaMapPullO1Power.lean#L20). The `T.*` names are wrappers that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. `ThMap`, `HasTh`, `ThList` and `symTup` are in [SymTupOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SymTupOne.lean#L18), and `hodge` is the abbreviation `VB.det (LieVB.omega G) g` in [SiegelToroidalIntegral.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/SiegelToroidalIntegral.lean#L134). The index of `symTup` runs over `Fin N`, so the entry $k$ in the text is the Lean entry $k - 1$. In `key_on_cover` the hypothesis that $m$ is a unit in $o$ is introduced as `hmu` at line 54 and not used; line 76 gets that $m$ is a unit in $F$ from $3 \le m$. The case $g = 0$ is done by hand at lines 94 to 105. The key formula is `KeySmall.key_sab` of [MemRangeOfSmallTraits.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MemRangeOfSmallTraits.lean#L322), whose hypotheses include a bound on the cardinality of points by that of $\mathbb{C}$. The proofs also apply `T.hasDiv_of_hasDiv_thetaSymmetricFunctionsDegreeFactorial`, `T.model_hasDiv_of_genericPoint_projectiveCoords`, `T.exists_projectiveSpace_map_of_model_hasDiv`, `T.symmetric_coordinates_O1_factorial_power`, `T.theta_coordinates_section_exists`, `T.abelianLocus_eq_preimage_moduli_and_principal`, `T.modelSemiAbelian_relDim_cotangent_vectorBundle`, `T.principallyPolarisedFibre_exists_generator_stable`, `T.theta_constants_listed_finite_galois_extension`, `T.exists_normalization_model_finiteExtension`, `T.lineBundleIso_pow_multiple_degree_descends_normal`, `T.lineBundleIso_of_iso_on_rational_model_components` and `T.detInvariantDiff_iso_hodgeLineBundle`. They have no entries in this chapter, and we use only their statements. We have not unfolded `ThG`, `IsGenSec`, `PCrd`, `PolFib`, `LBIso` or `NzFib`. "Theta value" in the definition stands for `ThG`.
