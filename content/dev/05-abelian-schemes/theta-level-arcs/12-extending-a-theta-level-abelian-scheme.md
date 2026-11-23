---
title: Extending a theta-level abelian scheme
decls:
  - GlobalTheory.T.semiAbelianScheme_uniformisation_exists_geometric
  - GlobalTheory.ZH.GeoHalf.zhGeo
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Extending a theta-level abelian scheme

In this section we prove the extension theorem. Let $S$ be a big theta system with a realisation $\rho$ by an abelian scheme $A$ over $\operatorname{Spec} R$, let $Z$ be a normal projective model of $\Omega$ with an admissible open set $U_0$, and let $E$ be a lattice system fixed by tests. Then $A$ over $U_0$ extends to a semi-abelian scheme $G$ over $Z$ with a symmetric cubical line bundle, theta sections that immerse $G$ in projective space, and uniformisations over complete local rings. The proof puts together [the set-up of the closure](/entry/base-facts-has-geo-exists-clos/), [the pre-extension](/entry/exists-semi-abelian-group-scheme-cubical-bundle-closure/) and ten more results of the Lean development. The theorem is used in [the geometric half of the extension theorem](/entry/zh-geo-of-semistable-reduction/), which proves its hypotheses except semistable reduction. We keep the notation of the two previous sections.

### The statement

Write $\mathcal{L}'^N$ for the $N$-th power of a line bundle $\mathcal{L}'$ on $G$, and $(s_l)_{l \in J}$ for the basis of sections of $L^N$ that comes with $\rho$. A section of a power of $\mathcal{L}'$ *extends* a section of the same power of $L$ if the two agree at the generic points of $u_0^* A$ through the given isomorphism of line bundles.

**Definition 6.12.1 (Extension of $\rho$).** An *extension* of $\rho$ over $(M, U_0, E)$ consists of a pre-extension $(u_0, G, \mathcal{L}')$ of $\rho$ such that $\mathcal{L}'$ satisfies the symmetry hypothesis, with these properties.

1. Each endomorphism of the generic fibre of $G$ extends uniquely to an endomorphism of $G$. Isomorphisms on the generic fibre between linear combinations, with coefficient sum $0$, of pullbacks of $\mathcal{L}'$ along homomorphisms $G \times G \to G$ extend to isomorphisms over $Z$.
2. The abelian locus of $G$ is the set of $z$ with $T(z) = 0$. Over each open set in the abelian locus, $\mathcal{L}'$ is relatively ample with trivial group $K(\mathcal{L}')$.
3. For each $z$ and each $a \in H(z)$, the torsion section $P_a$ extends to a section of $G$ over a neighbourhood of $z$.
4. For a complete noetherian normal local domain $R'$ of characteristic $0$ and a map $\xi : \operatorname{Spec} R' \to Z$ that meets the abelian locus, $\xi^* G$ has a uniformisation by degeneration data whose line bundle is isomorphic to $\xi^* \mathcal{L}'$, with $\psi$ a unit on the preimage of the abelian locus.
5. If $W$ is open and $\vartheta(x_0)$ divides all theta values at every point of $W$, then there is a section of $\mathcal{L}'$ over $G_W$ that extends $\theta_1 / \vartheta(x_0)$ and does not vanish at some point over each geometric point of $W$. For $v \in E(z)$ for all $z \in W$, there is a section of $\mathcal{L}'^N$ over $G_W$ that extends $\sum_l v_l s_l / \vartheta(x_0)$.
6. If also the rows $b_i$ of a matrix $b$ span $E(z)$ for all $z \in W$, then there are sections $\sigma_i$ of $\mathcal{L}'^N$ over $G_W$ that extend $\sum_l b_{il} s_l / \vartheta(x_0)$, have no common zero on the fibre over any geometric point of $W$, and are linearly independent there. Every such family $(\sigma_i)$ immerses $G_W$ into projective space over $W$.

Lean: `GlobalTheory.ZH.ZHOut`.

**Definition 6.12.2 (Extension statement).** The *extension statement* says: for every arithmetic base $o \subset \Omega$, every big theta system $S$ with a realisation $\rho$, every model $M$ of $\Omega$ with an admissible open set $U_0$, and every lattice system $E$ fixed by tests, if there are vectors $G_1, \dots, G_n \in \Omega^J$ and $a \in \mathbb{N}$ such that for every $z$ and $x_0$ with $\vartheta(x_0) \mid \vartheta$ at $z$ the $\mathcal{O}_z$-span of the $G_k / \vartheta(x_0)^a$ is the dual of $E(z)$, then $\rho$ has an extension.

Lean: `GlobalTheory.ZH.ZHGeoSt`.

A pre-extension $(u_0, G, \mathcal{L}')$ has *extended torsion sections* if property 3 holds for $G$. It has *theta model sections* for $E$ if, for each affine open $W$ and each matrix $b$ whose rows span $E$ on $W$, there are a line bundle $\mathcal{O}$ on $G_W$ and sections $\tau_i$ with no common zero, equal at generic points to $\sum_l b_{il} s_l$ up to a common scalar, linearly independent on the fibres over closed points, and with $\mathcal{O}$ relatively ample over the abelian part of $W$. It has *the right abelian locus* if the abelian locus is $\{z : T(z) = 0\}$ and $G$ is proper over every open set inside it. The Lean names are `GlobalTheory.ZH.ZHPre.Sec`, `GlobalTheory.ZH.ZHPre.SecO` and `GlobalTheory.ZH.ZHPre.Ab`.

### Inputs

The hypotheses of the theorem are: homomorphisms of semi-abelian schemes over a discrete valuation ring extend uniquely from the generic fibre; the semistable reduction statement for polarized abelian varieties over finite extensions of $\mathbb{Q}_p$; the uniformisation statement; the five bundles of laws; and the torsion statement for uniformisations. The inputs below hold under some of these hypotheses. In all of them $Q$ is a closure of $\rho$ with an extension, $C$ is its core, and the base facts hold.

**Theorem 6.12.3 (Uniformised tests).** Under semistable reduction, the uniformisation statement, the first two bundles of laws and the torsion statement, $S$ has tests and $\rho$ has uniformised tests.

Lean: `GlobalTheory.T.thetaSystem_hasTests_of_real_point`.

**Theorem 6.12.4 (Theta data and torsion sections).** If $S$ is big and $\rho$ has geometric tests, then there are theta data on $C$ whose line bundle is isomorphic to the pullback of $L$. If also $C$ has the fibre property, then $C$ has torsion sections of order $rN$.

Lean: `GlobalTheory.ZH.ThetaData.exists_theta` (also `GlobalTheory.ZH.TorsionValue.torsSec`, the torsion sections).

**Theorem 6.12.5 (Torsion sections on the closure).** For each $z$ and $a \in H(z)$ there are a neighbourhood $W$ of $z$ and a section $h : W \to G_Q$ whose value at each point over $U_0$ is the image of $P_a$.

Lean: `GlobalTheory.ZH.TorsionSection.exists_section`.

**Theorem 6.12.6 (Independent sections).** If $S$ is big and $\rho$ has geometric tests, then for each $\lambda$ and each closed point $z \in W_\lambda$, the sections $\sigma_\lambda$ of the closure are linearly independent on the fibre of $G_Q$ over a point onto $z$.

Lean: `GlobalTheory.T.thetaSections_independent_on_closed_fibre`.

**Theorem 6.12.7 (Abelian locus).** If $S$ is big, $\rho$ has geometric tests and $C$ has the fibre property, then the set of $z$ with $T(z) = 0$ is open, every closed point of $P$ over it lies in $G_Q$, and over each closed $z$ with $T(z) \neq 0$ there is a test whose special fibre is not proper.

Lean: `GlobalTheory.ZH.AbelianLocus.abelian_locus`.

**Theorem 6.12.8 (Abelian locus of a pre-extension).** Let a pre-extension have group scheme $G_Q$, with the same $u_0$ and the same map from $u_0^* A$. If $C$ has a group law, tests and charts, and the three conclusions of the theorem on the abelian locus hold, then the pre-extension has the right abelian locus.

Lean: `GlobalTheory.T.abelianLocus_eq_trivial_torus_locus_proper`.

**Theorem 6.12.9 (Theta model sections).** For a pre-extension as in the last theorem with the right abelian locus, if the sections $\sigma_\lambda$ are independent on closed fibres, then it has theta model sections.

Lean: `GlobalTheory.T.thetaModel_coordinates_local_basis`.

**Theorem 6.12.10 (Uniformisation over complete local domains).** Assume the five bundles of laws. Let $R'$ be a complete noetherian normal local domain of characteristic $0$, $G$ a semi-abelian scheme over $R'$ with a symmetric rigidified cubical line bundle that satisfies the symmetry hypothesis, with split closed fibre and a section that does not vanish at some point of the closed fibre. If $W$ is a nonempty open set equal to the abelian locus, $G$ is proper over $W$, and the line bundle is relatively ample with trivial $K$ over $W$, then $G$ has a uniformisation by degeneration data with this line bundle and with $\psi$ a unit on $W$.

Lean: `GlobalTheory.T.exists_uniformisation_completeLocalNormalDomain`.

**Theorem 6.12.11 (Four properties).** Assume the extension of homomorphisms, the uniformisation over complete local domains, semistable reduction, the uniformisation statement, the first two bundles of laws and the torsion statement. Let $S$ be big, $U_0$ admissible and $E$ fixed by tests. A pre-extension with group scheme $G_Q$ as above that has extended torsion sections, local theta sections, theta model sections and the right abelian locus gives an extension of $\rho$.

Lean: `GlobalTheory.T.nonempty_of_fourProperties_groupScheme`.

### The theorem

**Lemma 6.12.12 (Torsion sections through an identification).** If a pre-extension has group scheme $G_Q$ through an isomorphism $e$ that respects the maps to $Z$, $u_0$ and the map from $u_0^* A$, then the sections of the theorem on torsion sections on the closure give extended torsion sections of the pre-extension.

Lean: `GlobalTheory.ZH.GeoHalf.sec_of_iso`.

*Proof.* Compose each section $h : W \to G_Q$ with $e^{-1}$. It is still a section over $W$, since $e$ respects the maps to $Z$. At the generic point, a point $x'$ of $u_0^* A$ over the generic point of $U_0$ maps to the generic point of $\operatorname{Spec} R$, because $u_0$ is the identity there. So the condition on $x'$ in the definition of extended torsion sections is the condition in the theorem on torsion sections on the closure, and $h$ agrees with the image of $P_a$. Composing with $e$, which is a monomorphism into $P$, gives the equality for $h \circ e^{-1}$. $\square$

**Theorem 6.12.13 (Extension of a theta-level abelian scheme).** Assume that homomorphisms of semi-abelian schemes over a discrete valuation ring extend uniquely from the generic fibre, the semistable reduction statement, the uniformisation statement, the five bundles of laws and the torsion statement for uniformisations. Then the extension statement holds.

Lean: `GlobalTheory.T.semiAbelianScheme_uniformisation_exists_geometric` (also `GlobalTheory.ZH.GeoHalf.zhGeo`, a second name).

*Proof.* Fix $o \subset \Omega$, a big $S$ with realisation $\rho$, $M$, an admissible $U_0$ and $E$ fixed by tests.

*Step 1.* By the theorem on uniformised tests, $\rho$ has uniformised tests. By [the set-up](/entry/base-facts-has-geo-exists-clos/), the base facts hold, $\rho$ has geometric tests, and there are a closure $Q$ and an extension of $Q$ whose core $C$ has tests, independence, fibres and charts.

*Step 2.* By the theorem on theta data and torsion sections, $C$ has torsion sections of order $rN$ and theta data whose line bundle is isomorphic to the pullback of $L$. By [the group scheme on the closure](/entry/exists-semi-abelian-group-scheme-cubical-bundle-closure/), there is a pre-extension with group scheme $G_Q$, with the same $u_0$ and the same map from $u_0^* A$, that has local theta sections, and $C$ has a group law.

*Step 3.* The theorem on the abelian locus gives its three conclusions, and the theorem on the abelian locus of a pre-extension shows that the pre-extension has the right abelian locus. The theorem on independent sections and the theorem on theta model sections give theta model sections. The lemma and the theorem on torsion sections on the closure give extended torsion sections.

*Step 4.* The theorem on four properties, with the uniformisation over complete local domains, gives an extension of $\rho$. $\square$

**Remark 6.12.14 (Formalization).** The theorem is proved in [SemiAbelianSchemeUniformisationExistsGeometric.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/SemiAbelianSchemeUniformisationExistsGeometric.lean#L31) by applying `zhGeo_of` in [SecOfIso.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/SecOfIso.lean#L52) to twelve theorems, and the lemma is at line 23 of that file. The statement form is a `first | exact ...` block in [SemiAbelianSchemeUniformisationExistsGeometricStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/SemiAbelianSchemeUniformisationExistsGeometricStatement.lean#L19), and the extension statement is in [ImmersedBy.lean](lean:Development/AbelianVarietyTheory/Statements/SemistableTorsion/ImmersedBy.lean#L109). The hypothesis on dual lattices in the extension statement is never used: `zhGeo_of` introduces it as `_` (line 66). Only the second part of the theorem on uniformised tests is used, so the tests of $S$ are dropped. The name of the theorem speaks of uniformisation, but its conclusion is the whole extension. The five bundles of laws are packed into one hypothesis `GlobalTheory.UT.LL` for the inputs that need them. We did not unfold `abLocus`, `DegData`, `Unif`, `PsiUnitOn`, `GenVal`, `ImmersedBy`, `HypS` or the semistable reduction statement.
