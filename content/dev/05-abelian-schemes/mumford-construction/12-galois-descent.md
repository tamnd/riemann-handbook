---
title: Galois descent
decls:
  - GlobalTheory.T.uniformisationBundle_descends_along_galoisExtension
  - GlobalTheory.Mum.has_of_galAct
  - GlobalTheory.Mum.has_of_galois_action
  - GlobalTheory.T.uniformised_semiAbelian_galois_descent
  - GlobalTheory.Mum.has_of_hasFin
  - GlobalTheory.T.hasSemiAbelianUniformisation_of_finiteExt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Galois descent

This section proves that degeneration data over a base which are realised after a finite extension are realised over the base itself. [Mumford's construction](/entry/has-of-base/) uses this twice: once for the data of unitary PEL type after the labelled cover, and once for the factor $D$ after [the theorem on the idempotent factor](/entry/factor-unif/). The proof enlarges the finite extension to a Galois extension, lets the Galois group act on the realising semi-abelian scheme, and takes the quotient. For Galois theory see [Galois theory](/learn/algebra/#galois-theory) in Volume 1.

Throughout, $R$ is a base with fraction field $K$, and we use group pullbacks and cubical symmetric line bundles as in [the section on even cubical structures](/entry/exists-fin-ext-cp-factor-even/).

### Galois extensions and Galois actions

**Definition 4.12.1 (Galois extension).** Let $\rho : R \to R'$ be a ring map. Let $\operatorname{Gal}(\rho)$ be the group of ring automorphisms $\sigma$ of $R'$ with $\sigma \circ \rho = \rho$. We say that $\rho$ is *Galois* if $\operatorname{Gal}(\rho)$ is finite and every element of $R'$ that is fixed by all $\sigma \in \operatorname{Gal}(\rho)$ lies in $\rho(R)$.

Lean: `GlobalTheory.Mum.IsGal`.

If $\rho$ is a finite extension of normal domains and Galois, then the extension of fraction fields is a Galois extension of fields with group $\operatorname{Gal}(\rho)$, and $R$ is the ring of invariants. For example, $\mathbb{Z}_p \to \mathbb{Z}_p[\zeta_p]$ is Galois with group $(\mathbb{Z}/p)^\times$.

Let $\rho : R \to R'$ be a finite extension, $D$ data over $R$, $D'$ a pullback of $D$ along $\rho$, and $U'$ a uniformisation of $(A', G')$ by $D'$. For $\sigma \in \operatorname{Gal}(\rho)$, $\operatorname{Spec} \sigma$ is an automorphism of $\operatorname{Spec} R'$ over $\operatorname{Spec} R$, and $D'$ and $U'$ can be pulled back along it.

**Definition 4.12.2 (Galois action on a uniformisation).** In this situation, a *Galois action* on $U'$ consists of morphisms $a_\sigma : G' \to G'$, for $\sigma \in \operatorname{Gal}(\rho)$, with these properties.

1. Each $a_\sigma$ makes $G'$ the group pullback of $G'$ along $\sigma$.
2. $a_1 = 1$ and $a_{\sigma \tau} = a_\tau \circ a_\sigma$.
3. For each $\sigma$ there are a structure of pullback of $D'$ along $\sigma$ on $D'$ itself and an isomorphism of $G'$ with its base change along $\operatorname{Spec} \sigma$ whose composite with the projection is $a_\sigma$, such that $U'$ is the pullback of $U'$ under these identifications. The identification of $D'$ with itself fixes the lattice, and it commutes with the projection of the abelian part to the abelian part of $D$.

Lean: `GlobalTheory.Mum.GalAct`.

The order in 2 is the order of $\operatorname{Spec}$, which reverses composition: $a_\sigma$ lies over $\operatorname{Spec} \sigma$, and $\operatorname{Spec}(\sigma \tau) = \operatorname{Spec} \tau \circ \operatorname{Spec} \sigma$ as maps of schemes. Condition 3 says that the action respects the uniformisation and acts trivially on the data that come from $R$.

### Descent with a Galois action

In the next two results, $\rho : R \to R'$ is a finite Galois extension, $D$ data over $R$, $D'$ a pullback of $D$ along $\rho$, $G'$ a commutative semi-abelian scheme over $R'$, $U'$ a uniformisation of $(A', G')$ by $D'$, and $(a_\sigma)$ a Galois action on $U'$. Let $G$ be a commutative semi-abelian scheme over $R$ and $\beta : G' \to G$ a morphism that makes $G'$ the group pullback of $G$ along $\rho$, with $\beta \circ a_\sigma = \beta$ for all $\sigma$.

**Proposition 4.12.3 (Descent of the line bundle).** In this situation there is a cubical symmetric line bundle $P$ on $G$ with a generating isomorphism $L_{U'} \cong \beta^* P$.

Lean: `GlobalTheory.T.uniformisationBundle_descends_along_galoisExtension`.

*Proof.* This is [the theorem on Galois descent of the cubical symmetric line bundle](/entry/exists-cp/), proved in a later section, with the same hypotheses. $\square$

**Proposition 4.12.4 (Realisation from a descended group).** In this situation the data $D$ are realised.

Lean: `GlobalTheory.Mum.has_of_galAct`.

*Proof.* *Step 1: the generic fibre.* The Galois action descends the polarised abelian variety $A'$: there are a polarised abelian variety $A$ over $K$, an isomorphism of group schemes $\gamma : G_K \to A$ and a morphism $\kappa : G'_{K'} \to G_K$ over $\beta$, such that $L_{U'}|_{G'_{K'}} \cong (\gamma \circ \kappa)^* L_A$.

*Step 2: the line bundle.* The previous proposition gives a cubical symmetric $P$ on $G$ with $L_{U'} \cong \beta^* P$.

*Step 3: comparison on the generic fibre.* The line bundles $\gamma^* L_A$ and $P|_{G_K}$ become isomorphic after pullback along $\kappa$, which is the base change along the finite extension $K \to K'$. Line bundles on $G_K$ that become isomorphic after this base change and are compatible with the Galois action are isomorphic, so $\gamma^* L_A \cong P|_{G_K}$.

*Step 4: evenness.* The even cubical trivialisation on the torus of the closed fibre of $G'$, given by $U'$, descends: $P$ is even on the torus.

*Step 5: data for $G$.* By Steps 3 and 4 and the converse stated in [the section on even cubical structures](/entry/exists-fin-ext-cp-factor-even/), there are data $D_1$ over $R$ and a uniformisation $U_1$ of $(A, G)$ by $D_1$ with line bundle $P$. Then $L_{U'} \cong \beta^* L_{U_1}$.

*Step 6: comparison of data.* Since $D'$ is a pullback of $D$, $U'$ uniformises $G'$ with line bundle $\beta^* L_{U_1}$, and the action is trivial on the data from $R$, the data $D$ are a pullback of $D_1$ along the identity of $R$.

*Step 7.* Realised data stay realised under pullback along an injective local map of admissible bases. Since $D_1$ is realised by $(A, G, U_1)$ and $D$ is a pullback of $D_1$ along the identity, $D$ is realised. $\square$

**Theorem 4.12.5 (Galois descent).** Let $\rho : R \to R'$ be a finite Galois extension, $D$ data over $R$, $D'$ a pullback of $D$ along $\rho$, $G'$ a commutative semi-abelian scheme over $R'$, $A'$ a polarised abelian variety over $K'$, $U'$ a uniformisation of $(A', G')$ by $D'$, and $(a_\sigma)$ a Galois action on $U'$. Then $D$ is realised.

Lean: `GlobalTheory.Mum.has_of_galois_action` (also `GlobalTheory.T.uniformised_semiAbelian_galois_descent`, a second name).

*Proof.* By [the theorem on a smooth quotient near the closed fibre](/entry/exists-near-galois-quotient/), there is a smooth model $(U, u)$ of $G'$ near the closed fibre over $\operatorname{Spec} \rho$ (see [the section on descent to the base](/entry/mum-exists-near/)). The multiplication of $G'$ descends to it, and $u$ is equivariant: for every point $(x, s)$ of $U \times_R \operatorname{Spec} R'$, $a_\sigma(u(x, s)) = u(x, \operatorname{Spec} \sigma \circ s)$.

The map $\operatorname{Spec} \rho$ is finite, hence proper. It is surjective, since $R'$ is integral over $R$ and $\rho$ is injective, so every prime of $R$ lies under a prime of $R'$. By [the descent theorem for smooth models](/entry/descend-of-near/), there are a commutative semi-abelian scheme $G$ over $R$, a morphism $\beta : G' \to G$ that makes $G'$ the group pullback of $G$ along $\rho$, and a morphism $i : U \to G$ with $\beta \circ u = i \circ \mathrm{pr}_1$.

For each $\sigma$, the morphisms $\beta \circ a_\sigma$ and $\beta$ from $G'$ to $G$ agree on the image of $u$: for a point $u(x, s)$ both give $i(x)$, by the equivariance of $u$. The image of $u$ contains the closed fibre. The idea of the next step is that two morphisms of this kind which agree near the closed fibre are equal, since $G'$ is semi-abelian and $G$ is separated; so $\beta \circ a_\sigma = \beta$. The previous proposition now shows that $D$ is realised. $\square$

**Theorem 4.12.6 (Descent along finite extensions).** Let $D$ be degeneration data over $R$ that are realised after a finite extension. Then $D$ is realised.

Lean: `GlobalTheory.Mum.has_of_hasFin` (also `GlobalTheory.T.hasSemiAbelianUniformisation_of_finiteExt`, a second name).

*Proof.* Let $\rho : R \to R'$ be a finite extension and $D'$ a realised pullback of $D$ along $\rho$.

*Step 1: a Galois closure.* There is a finite extension $\sigma : R' \to R''$ that is a local map, such that $\sigma \circ \rho$ is a finite extension and Galois. This is the integral closure of $R$ in a Galois closure of the fraction field extension, which is again a complete local domain since $R$ is complete and normal.

*Step 2: pullback of the data.* Along an injective local map every set of degeneration data has a pullback; let $D''$ be a pullback of $D'$ along $\sigma$. Realised data stay realised under pullback along an injective local map of admissible bases, so $D''$ is realised by some $(A'', G'', U'')$ with $G''$ semi-abelian. A pullback of a pullback is a pullback along the composite, so $D''$ is a pullback of $D$ along $\sigma \circ \rho$.

*Step 3: the Galois action.* For a finite Galois extension of a base and a uniformisation of a semi-abelian scheme by pulled back data, there is a Galois action on the uniformisation. The action of $\tau \in \operatorname{Gal}(\sigma \circ \rho)$ comes from the fact that the pullback of $U''$ along $\tau$ is a uniformisation by the same data, since the data come from $R$.

*Step 4.* [The Galois descent theorem](/entry/has-of-galois-action/) shows that $D$ is realised. $\square$

**Remark 4.12.7 (Formalization).** The second names are wrappers, proved by a `first | exact` tactic; the proposition on the line bundle is a wrapper of `GlobalTheory.GaloisPackageDescent.exists_cp`. The Galois action is a right action, $a_{\sigma\tau} = a_\sigma ≫ a_\tau$ in diagrammatic order. In the proof of the proposition on realisation ([HasOfGalAct.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasOfGalAct.lean#L19)), Steps 1, 3, 4 and 6 are `GlobalTheory.T.polarised_generic_fibre_descends_galois`, `GlobalTheory.T.lineBundleIso_genericFibre_descend_finite_ext`, `GlobalTheory.T.evenCubicalTrivialisation_descended_closedTorus` and `GlobalTheory.T.nonempty_degData_iso_of_galoisDescendedGroup`; Step 5 is `GlobalTheory.T.exists_uniformisation_completeLocal_evenOnTorus`, whose clause on the generic isomorphism is dropped at line 25; Step 7 is `GlobalTheory.T.hasSemiAbelianUniformisation_pullback_injective_local` along the identity. We did not open the proofs of these inputs, and the reasons given for Steps 3, 4 and 6 are sketches. In the Galois descent theorem ([UniformisedSemiAbelianGaloisDescent.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformisedSemiAbelianGaloisDescent.lean#L25)) one output of the descent theorem is discarded at line 25, and the invariance $\beta \circ a_\sigma = \beta$ is `GlobalTheory.Mum.comp_eq_of_near`. The statement file of this theorem imports Mathlib twice, at lines 1 and 3. In the last theorem, Step 1 is `GlobalTheory.T.exists_galois_closure_local_domain_extension`, Step 2 uses `GlobalTheory.T.exists_degenerationData_pullback_injective_localHom` and `GlobalTheory.PullDegComp.nonempty_isPullDeg_comp`, and Step 3 is `GlobalTheory.T.exists_galoisAction_on_uniformisedGroup_pulledData`; the reasons given for Steps 1 and 3 are sketches.
