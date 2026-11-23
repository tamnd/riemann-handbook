---
title: Strong approximation for special unitary groups
decls:
  - GlobalTheory.PlaceIso.exists_isotropic_places
  - GlobalTheory.T.exists_isotropic_places_alt
  - GlobalTheory.StrongApproxSUProof.strongApproxSU
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Strong approximation for special unitary groups

This section proves strong approximation for the special unitary group of a nondegenerate Hermitian form of rank at least two over a CM extension. The hypothesis is the classical one: the group is not compact at the places of $S$. The proof reduces the statement to the [theorem on planes](/entry/special-unitary-fixing-plane-complement-mem-closure/) of the last section. First, non-compactness gives a place of $S$ where the form is isotropic, and at this place we find rational planes whose norm condition holds. Then a reduction, proved in another part of the development, assembles the plane case into the general case. The theorem is the input [strong approximation for SU](/entry/strong-approx-su-of-literature/), which a later volume takes from the literature; this section proves it.

We keep the notation of the last two sections: $(F, E, \sigma)$ is a CM extension, $J \in M_M(E)$ is nondegenerate Hermitian with form $h$, $\mathbb{A}_E = \mathbb{A}_F \otimes_F E$, $\varepsilon$ is a place idempotent for a set $S = S_1 \cup S_2$ of places, and $\mathrm{SU}_J(F)$, $\mathrm{SU}_J(\mathbb{A}_F)$ and $\mathrm{SU}_J(\varepsilon)$ are the special unitary groups. For a place $u$ of $F$ we write $F_u$ for the completion and $h_u$ for the form $h$ on $(F_u \otimes_F E)^M$.

### An isotropic place

For $x, z \in E^M$ with $h(x, x) \neq 0$ let
$$z_x = z - \frac{h(x, z)}{h(x, x)} \, x$$
be the component of $z$ orthogonal to $x$. Then $h(x, z_x) = 0$, so $x$ and $z_x$ are an orthogonal pair of the kind in the theorem on planes, provided $h(z_x, z_x) \neq 0$.

**Lemma 1.13.1 (Isotropic places).** Let $(F, E, \sigma)$ be a CM extension, $M \geq 2$, and $J \in M_M(E)$ nondegenerate Hermitian. Let $\varepsilon$ be a place idempotent for $(S_1, S_2)$ such that $\mathrm{SU}_J(\varepsilon)$ is not compact. Then there are $S_1' \subseteq S_1$ and $S_2' \subseteq S_2$, not both empty, and a place idempotent $\varepsilon'$ for $(S_1', S_2')$, with the following property. For all $x, y \in E^M$ with $h(x, x) \neq 0$ and $h(y, y) \neq 0$ there is $z \in E^M$ with $h(z, z) \neq 0$ such that:

1. $h(z_x, z_x) \neq 0$, and there is $t \in \mathbb{A}_E$ with $\varepsilon' \bigl( t \sigma(t) + h(x, x)/h(z_x, z_x) \bigr) = 0$;
2. $h(y_z, y_z) \neq 0$, and there is $t \in \mathbb{A}_E$ with $\varepsilon' \bigl( t \sigma(t) + h(z, z)/h(y_z, y_z) \bigr) = 0$.

Lean: `GlobalTheory.T.exists_isotropic_places_alt` (also `GlobalTheory.PlaceIso.exists_isotropic_places`).

So the two pairs $(x, z_x)$ and $(z, y_z)$ satisfy the hypotheses of the theorem on planes with the idempotent $\varepsilon'$. The vector $z$ links $x$ to $y$ through two planes.

*Proof.* We use these facts, proved in another part of the development. We have opened their statements.

1. *Compactness from anisotropy.* If at every $u \in S$ the unitary matrices over $F_u \otimes_F E$ have their entries in a compact set, then $\mathrm{SU}_J(\varepsilon)$ is compact.
2. *Anisotropic forms.* Let $K$ be a proper nontrivially normed field that is an $F$-algebra. If $h(u, u) = 0$ implies $u = 0$ for $u \in (K \otimes_F E)^M$, then the unitary matrices over $K \otimes_F E$ have their entries in a compact set.
3. *Rational planes.* Let $K$ be a complete nontrivially normed field that contains $F$ as a dense subfield, $M \geq 2$, and assume that there is a nonzero $u \in (K \otimes_F E)^M$ with $h(u, u) = 0$. Then for all $x, y \in E^M$ with $h(x, x) \neq 0$ and $h(y, y) \neq 0$ there is $z \in E^M$ with $h(z, z) \neq 0$ such that $h(z_x, z_x) \neq 0$, $h(y_z, y_z) \neq 0$, and $t \sigma(t) + h(x, x)/h(z_x, z_x) = 0$ and $t' \sigma(t') + h(z, z)/h(y_z, y_z) = 0$ for some $t, t' \in K \otimes_F E$.
4. *From one place to the adeles.* Let $\varepsilon'$ be the place idempotent of a single place $u$, and $c \in E$. If $t \sigma(t) + c = 0$ for some $t \in F_u \otimes_F E$, then $\varepsilon' \bigl( t \sigma(t) + c \bigr) = 0$ for some $t \in \mathbb{A}_E$.
5. Every pair of finite sets of places has a place idempotent.

Assume that $h_u$ is anisotropic at every $u \in S$. Each completion $F_u$ is a proper nontrivially normed field, so fact 2 applies at each $u \in S$, and fact 1 makes $\mathrm{SU}_J(\varepsilon)$ compact. This contradicts the hypothesis. So there is $u \in S$ and a nonzero $w \in (F_u \otimes_F E)^M$ with $h_u(w, w) = 0$.

Let $S'$ be $\{u\}$, as a set of infinite places if $u \in S_1$ and as a set of finite places if $u \in S_2$, and let $\varepsilon'$ be its place idempotent from fact 5. Then $S' \subseteq S$ and $S'$ is nonempty. The field $F$ is dense in $F_u$. Let $x, y$ be given. Fact 3 with $K = F_u$ gives $z$, with the two norm equations over $F_u \otimes_F E$. Fact 4 turns each of them into an equation over $\mathbb{A}_E$ times $\varepsilon'$. $\square$

A unitary group over a local field is compact if and only if the form is anisotropic there. The lemma uses only the direction "anisotropic implies compact", in the form of facts 1 and 2.

### Strong approximation

**Theorem 1.13.2 (Strong approximation for SU).** Let $(F, E, \sigma)$ be a CM extension, $M \geq 2$, and $J \in M_M(E)$ nondegenerate Hermitian. Let $\varepsilon$ be a place idempotent for $(S_1, S_2)$ such that $\mathrm{SU}_J(\varepsilon)$ is not compact. Then every $g \in \mathrm{SU}_J(\mathbb{A}_F)$ lies in the closure of
$$\{ \gamma h : \gamma \in \mathrm{SU}_J(F), \ h \in \mathrm{SU}_J(\varepsilon) \}.$$

Lean: `GlobalTheory.StrongApproxSUProof.strongApproxSU`.

*Proof.* Let $Y$ be the set in the statement. We use three more facts from another part of the development, whose statements we have opened.

1. *Finite support.* Every $g \in \mathrm{SU}_J(\mathbb{A}_F)$ lies in the closure of the union of the sets $\mathrm{SU}_J(\eta)$, over all place idempotents $\eta$.
2. *Weak approximation.* Let $\eta$ be a place idempotent for $(T_1, T_2)$. Every $h \in \mathrm{SU}_J(\eta)$ lies in the closure of the set of $x \in U_J(\mathbb{A}_F)$ with $x = 1 + \eta (\gamma - 1)$ for some $\gamma \in \mathrm{SU}_J(F)$.
3. *Assembly.* Assume the theorem on planes and the lemma on isotropic places. Let $M \geq 2$ and let $\varepsilon$ be a place idempotent with $\mathrm{SU}_J(\varepsilon)$ not compact. Then for every place idempotent $\eta$ and every $\gamma \in \mathrm{SU}_J(F)$, each $x \in U_J(\mathbb{A}_F)$ with $x = 1 + \eta(\gamma - 1)$ lies in the closure of $Y$.

The element $1 + \eta(\gamma - 1)$ agrees with $\gamma$ at the places of $T = T_1 \cup T_2$ and is $1$ elsewhere. Fact 2 says that $\mathrm{SU}_J(F)$ is dense in $\mathrm{SU}_J(F_T)$, which is weak approximation.

By fact 3, applied with the theorem on planes and the lemma on isotropic places, each truncation $1 + \eta(\gamma - 1)$ lies in the closure of $Y$. Let $\eta$ be a place idempotent and $h \in \mathrm{SU}_J(\eta)$. By fact 2, $h$ lies in the closure of a set of truncations, which is contained in the closed set $\overline{Y}$, so $h \in \overline{Y}$. So the union of the sets $\mathrm{SU}_J(\eta)$ is contained in $\overline{Y}$. By fact 1, $g$ lies in the closure of this union, hence in $\overline{Y}$. $\square$

**Remark 1.13.3 (Classical form).** Strong approximation for a simply connected, absolutely almost simple group $G$ over $F$ says that $G(F) \, G(F_S)$ is dense in $G(\mathbb{A}_F)$ when $\prod_{v \in S} G(F_v)$ is not compact (M. Kneser, "Starke Approximation in algebraischen Gruppen. I", *J. reine angew. Math.* 218 (1965); V. Platonov and A. Rapinchuk, *Algebraic Groups and Number Theory*, Chapter 7). For $M \geq 2$ the special unitary group of a nondegenerate Hermitian form is such a group, and $\mathrm{SU}_J(\varepsilon)$ is $\prod_{v \in S} \mathrm{SU}_J(F_v)$. So the theorem is the classical statement for $\mathrm{SU}_J$, with the same hypothesis. The density of $\mathrm{SU}_J(F) \, \mathrm{SU}_J(F_S)$ is here stated as: each element is in the closure of the set of products. The proof reduces the theorem to binary subspaces, where the last section identified $\mathrm{SU}$ with the norm-one group of a quaternion algebra.

**Remark 1.13.4 (Formalization).** The theorem proves the proposition `GlobalTheory.Published.StrongApproxSU`, defined in [NotIsCompactUnivFv.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/NotIsCompactUnivFv.lean#L33); its proof is in [ImportsTailTer.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ImportsTailTer.lean#L14). A second proof of the same proposition, `GlobalTheory.CompanionTheory.Hypotheses₂.strongApproxSU` at [ImportsBis.lean](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/ImportsBis.lean#L16), uses a different route. The facts of the lemma are `GlobalTheory.T.isCompact_specialUnitary_supportedAtPlaces`, `GlobalTheory.T.exists_compact_set_unitary_hermitian_real`, `GlobalTheory.T.exists_rational_vector_isotropic_nondegenerate_planes_at_place`, `GlobalTheory.T.exists_norm_solution_adelic_from_archimedean`, `GlobalTheory.T.idempotent_adelic_norm_eq_of_local_norm_eq` and `GlobalTheory.Published.StrongApprox.exists_isPlacesIdem`; the density of $F$ in an archimedean completion is `GlobalTheory.PlaceIso.denseRange_algebraMap_completion`, in the same file as the lemma. The facts of the theorem are `GlobalTheory.T.mem_closure_specialUnitarySupportedAtPlaces`, `GlobalTheory.T.mem_closure_rational_points_unitary_group` and `GlobalTheory.T.truncation_specialUnitary_mem_closure_strongApprox`; the last takes the theorem on planes and the lemma on isotropic places as hypotheses, and it wraps `GlobalTheory.SUAssemble.assemble`, whose proof we have not opened. The lemma always returns a single place: in [ExistsIsotropicPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsIsotropicPlaces.lean#L27) the sets $S_1'$ and $S_2'$ are $\{u\}$ and $\emptyset$, or $\emptyset$ and $\{u\}$. The wrapper `GlobalTheory.T.exists_isotropic_places_alt` restates `GlobalTheory.PlaceIso.exists_isotropic_places` without change.
