---
title: Even cubical structures on the factor
decls:
  - GlobalTheory.Mum.exists_finExt_cp_factor_even
  - GlobalTheory.T.exists_finExt_cubicalSymmetric_even_factor
  - GlobalTheory.Mum.exists_finExt_evenCP_of_factor_extLam
  - GlobalTheory.T.exists_evenCubicalStructure_of_idempotentFactor_biextension
  - GlobalTheory.T.exists_finiteExtension_symmBundle_extension_on_factor
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Even cubical structures on the factor

In the last step of [Mumford's construction](/entry/has-of-base/) the data $D$ are a factor of realised data $D'$, and the factor cuts a semi-abelian scheme $G$ out of the scheme $G'$ that realises $D'$. To show that $G$ realises $D$ after a finite extension, we need a line bundle on $G$ of the right kind. This section constructs it: after a finite extension of the base, $G$ carries a cubical symmetric line bundle whose Mumford bundle is the restriction of the Mumford bundle of $G'$, which is even on the torus of the closed fibre, and which comes from a polarised abelian variety on the generic fibre. [The theorem on the idempotent factor](/entry/semiabelian-uniformization-linear-action-transfer/) uses this line bundle to build degeneration data for $G$. For cubical structures see [the theorem of the cube](/learn/abelian-varieties/#the-theorem-of-the-cube) in Volume 1.

### Group pullbacks and Mumford bundles

Let $\rho : R \to R'$ be a ring map, $G$ a group scheme over $R$ and $G_1$ a group scheme over $R'$. A morphism $\beta : G_1 \to G$ over $\operatorname{Spec} \rho$ makes $G_1$ the *group pullback* of $G$ along $\rho$ if the square formed by $\beta$, the structure maps and $\operatorname{Spec} \rho$ is cartesian and $\beta$ respects the group laws on points. Then $G_1 \cong G \otimes_R R'$ as group schemes. We write $\beta_2 = \beta \times \beta : G_1 \times_{R'} G_1 \to G \times_R G$ for the induced map; a map $\beta_2$ with $\mathrm{pr}_k \circ \beta_2 = \beta \circ \mathrm{pr}_k$ for $k = 1, 2$ is called a *square* over $\beta$.

**Definition 4.9.1 (Mumford bundle).** Let $G$ be a commutative group scheme over a scheme $S$, with group law $m$ and zero section $0$, and let $L$ be a line bundle on $G$. The *Mumford bundle* of $L$ is the line bundle
$$\Lambda(L) = m^* L \otimes \mathrm{pr}_1^* L^{-1} \otimes \mathrm{pr}_2^* L^{-1} \otimes (0 \circ \pi)^* L$$
on $G \times_S G$, where $\pi : G \times_S G \to S$ is the structure map.

Lean: `ReciprocityTheory.ChartRestriction.G.Semi.abelian₂`.

Its fibre at $(x, y)$ is $L_{x + y} \otimes L_x^{-1} \otimes L_y^{-1} \otimes L_0$. For an abelian scheme, the class of $\Lambda(L)$ determines the polarisation $\lambda_L$ of $L$. Two line bundles with isomorphic Mumford bundles have the same polarisation, so $\Lambda(L)$ is the invariant of $L$ that a factor can control.

**Definition 4.9.2 (Cubical symmetric line bundle).** Let $G$ be a commutative group scheme over $S$. A *cubical symmetric line bundle* on $G$ is a line bundle $L$ on $G$ with a rigidification along the zero section, a cubical structure $c$, and a generator $\mathrm{sym}$ of $[-1]^* L \otimes L^{-1}$ that is $1$ at the zero section and is compatible with $c$.

Lean: `GlobalTheory.UU.CP`.

### Evenness on the torus

The closed fibre of a semi-abelian scheme over $R$ is an extension of an abelian variety by a torus. The next definition records such a structure.

**Definition 4.9.3 (Torus quotient structure).** Let $G$ be a commutative group scheme over $S$ and $\mathsf{X}$ a free abelian group of finite rank. A *torus quotient structure* on $G$ with characters $\mathsf{X}$ consists of an abelian scheme $B$ over $S$, a homomorphism $q : G \to B$ that is flat, surjective and affine, and a homomorphism $i : T_{\mathsf{X}} \to G$ from the split torus with character group $\mathsf{X}$, such that $i$ is the kernel of $q$. We require that for each point $b$ of $B$ and each $\chi \in \mathsf{X}$ there are an open $V \ni b$ and a unit $u$ on $q^{-1}(V)$ of weight $\chi$: $u(t g) = \chi(t)\, u(g)$ for points $t$ of $T_{\mathsf{X}}$ and $g$ of $G$.

Lean: `GlobalTheory.UU.TQ`.

**Definition 4.9.4 (Even cubical trivialisation).** Let $L$ be a cubical symmetric line bundle on $G$ with cubical structure $c$, and let $i : H \to G$ be a homomorphism. A *cubical trivialisation* of $L$ along $i$ is a generator $\sigma$ of $i^* L \otimes (0 \circ \pi)^* L^{-1}$ that satisfies the cube relation
$$\begin{aligned} \sigma(x + y + u)\, \sigma(x)\, \sigma(y)\, \sigma(u) &= c(ix, iy, iu)\, \sigma(x + y)\, \sigma(x + u)\, \sigma(y + u) \end{aligned}$$
for all points $x, y, u$ of $H$. It is *even* if $\sigma(-x) = \mathrm{sym}(i x)\, \sigma(x)$ for all points $x$ of $H$.

Lean: `GlobalTheory.UU.CubTriv` (also `GlobalTheory.UU.CubTriv.Even`, the evenness).

Over a field every line bundle on a split torus is trivial, so on the closed fibre a generator along $i$ exists; the conditions ask that it can be chosen compatible with the cubical and the symmetric structure. Degeneration data have even trivialisations $\psi$, and this is the matching condition on the side of the group.

**Definition 4.9.5 (Even on the torus).** Let $R$ be a local domain with maximal ideal $\mathfrak{m}$, let $G$ be a commutative group scheme over $R$ and $P$ a cubical symmetric line bundle on $G$. We say that $P$ is *even on the torus* if there are a free abelian group $\mathsf{X}$ of finite rank, a torus quotient structure $(B_0, q, i)$ with characters $\mathsf{X}$ on the closed fibre $G_0 = G \otimes_R R/\mathfrak{m}$, a cubical symmetric line bundle $P_0$ on $G_0$ that is the restriction of $P$ with all its structure, and an even cubical trivialisation of $P_0$ along $i$.

Lean: `GlobalTheory.Mum.EvenOn`.

This is the condition under which a line bundle on a semi-abelian scheme gives degeneration data. Let $G$ be semi-abelian over a base $R$, let $P$ be a cubical symmetric line bundle on $G$ that is even on the torus, and let $\gamma : G_K \to A$ be an isomorphism of group schemes with a polarised abelian variety $A$ over $K$, with $\gamma^* L_A \cong P|_{G_K}$. Then there are degeneration data $D$ and a uniformisation of $(A, G)$ by $D$ whose line bundle is $P$ and whose generic isomorphism is $\gamma$. The later sections use this converse to pass from line bundles to data.

**Definition 4.9.6 (Extension of the Mumford bundle).** Let $G$ be a commutative group scheme over $R$, let $L$ be a line bundle on the generic fibre $G_K$, and let $M$ be a line bundle on $G \times_R G$. We say that $M$ *extends* $\Lambda(L)$ if for every morphism $\kappa_2 : G_K \times_K G_K \to G \times_R G$ that is a square over $G_K \to G$ there is a generating isomorphism $\Lambda(L) \cong \kappa_2^* M$.

Lean: `GlobalTheory.Mum.ExtLam`.

### The factor situation

Throughout the rest of the section we fix the following data, as in the proof of [Mumford's construction](/entry/has-of-base/). $R$ is a base; $D$ and $D'$ are degeneration data over $R$; $F$ is a factor of $D'$ onto $D$, with ring $\mathcal{O}$ and elements $e, f \in \mathcal{O}$, as in [the section on unitary factors](/entry/exists-unitary-peltype-factor-deg-data/). $G'$ is a commutative semi-abelian scheme over $R$, $A'$ a polarised abelian variety over $K$, and $U'$ a uniformisation of $(A', G')$ by $D'$ with line bundle $L'$. There are actions of $\mathcal{O}$ on $A'$ and on $G'$ for which $U'$ is linear. Finally $G$ is a commutative semi-abelian scheme over $R$ with homomorphisms $i : G \to G'$ and $p : G' \to G$ such that $p \circ i = 1$ and $i \circ p = [e]$. We call this the *factor situation* and put
$$\Lambda_F = \bigl(i \times [f] \circ i\bigr)^* \Lambda(L')$$
on $G \times_R G$. On the abelian parts this is the bundle that the factor $F$ identifies with $\Lambda(L)$ for the line bundle $L$ of $D$.

### The theorems

**Proposition 4.9.7 (A line bundle on the factor).** In the factor situation, let $A$ be a polarised abelian variety over $K$ and $\gamma : G_K \to A$ an isomorphism of group schemes, such that $\Lambda_F$ extends $\Lambda(\gamma^* L_A)$. Let $W$ be a complete discrete valuation ring of characteristic $0$ and $\varphi : R \to W$ an injective local map. Let $G_W$ be a commutative group scheme over $W$ with a morphism $\beta_W : G_W \to G$ that makes it the group pullback of $G$ along $\varphi$, let $D_W$ be degeneration data over $W$, $A_W$ a polarised abelian variety over the fraction field of $W$, and $U_W$ a uniformisation of $(A_W, G_W)$ by $D_W$. Let $\kappa : (G_W)_{K_W} \to G_K$ be a morphism over $\beta_W$ with $L_{U_W}|_{(G_W)_{K_W}} \cong \kappa^* \gamma^* L_A$. Then there are a finite extension $\rho : R \to R'$, a group scheme $G_1$ over $R'$ with a morphism $\beta : G_1 \to G$ that makes it the group pullback of $G$ along $\rho$, a morphism $\kappa_1 : (G_1)_{K'} \to G_K$ over $\beta$, and a line bundle $L_1$ on $G_1$ with $L_1|_{(G_1)_{K'}} \cong \kappa_1^* \gamma^* L_A$.

Lean: `GlobalTheory.T.exists_finiteExtension_symmBundle_extension_on_factor`.

*Proof.* Since $\Lambda_F$ extends $\Lambda(\gamma^* L_A)$ and $G$ is semi-abelian over the admissible base $R$, the line bundle $\gamma^* L_A$ on $G_K$ extends to a line bundle $L_1$ on $G$. Take $R' = R$, $\rho = 1$, $G_1 = G$, $\beta = 1$ and $\kappa_1 = 1$. $\square$

The extension of $\gamma^* L_A$ to $G$ is an input of this chapter; its proof lies outside the part of the development covered here.

**Proposition 4.9.8 (Even structure from an extended Mumford bundle).** In the factor situation, let $\rho_1 : R \to R_1$ be a finite extension, $G_1$ a commutative group scheme over $R_1$ with $\beta_1 : G_1 \to G$ that makes it the group pullback of $G$ along $\rho_1$, and $\beta_{12}$ a square over $\beta_1$. Let $A_1$ be a polarised abelian variety over the fraction field $K_1$ of $R_1$ and $\gamma_1 : (G_1)_{K_1} \to A_1$ an isomorphism of group schemes, such that $\beta_{12}^* \Lambda_F$ extends $\Lambda(\gamma_1^* L_{A_1})$. Then there are a finite extension $\rho_0 : R \to R_0$, a commutative group scheme $G_0$ over $R_0$ with $\beta_0 : G_0 \to G$ that makes it the group pullback of $G$ along $\rho_0$, a square $\beta_{02}$ over $\beta_0$, a cubical symmetric line bundle $P$ on $G_0$, a polarised abelian variety $A_0$ over the fraction field $K_0$ of $R_0$, and an isomorphism of group schemes $\gamma_0 : (G_0)_{K_0} \to A_0$, with these properties:

1. $G_0$ is semi-abelian;
2. there is a generating isomorphism $\Lambda(P) \cong \beta_{02}^* \Lambda_F$;
3. $P$ is even on the torus;
4. there is a generating isomorphism $\gamma_0^* L_{A_0} \cong P|_{(G_0)_{K_0}}$.

Lean: `GlobalTheory.Mum.exists_finExt_evenCP_of_factor_extLam` (also `GlobalTheory.T.exists_evenCubicalStructure_of_idempotentFactor_biextension`, a second name).

*Proof.* We use three inputs.

First, a finite extension $\rho_2 : R \to R_2$ puts us in a new factor situation over $R_2$, with data $D_2, D_2'$, a factor $F_2$, a uniformised $G_2'$ and a semi-abelian factor $G_2$ of $G_2'$, where $\beta_2 : G_2 \to G$ makes $G_2$ the group pullback of $G$ along $\rho_2$, with a square $\beta_{22}$. In it there are a polarised abelian variety $A_2$ with $\gamma_2 : (G_2)_{K_2} \cong A_2$ such that $\Lambda_{F_2}$ extends $\Lambda(\gamma_2^* L_{A_2})$, a generating isomorphism $\Lambda_{F_2} \cong \beta_{22}^* \Lambda_F$, and a uniformised trait: a complete discrete valuation ring $W$ with $\varphi : R_2 \to W$ and data $(G_W, \beta_W, D_W, A_W, U_W, \kappa)$ as in the previous proposition.

Second, the previous proposition, applied to this situation, gives a finite extension $\rho_3 : R_2 \to R_3$, a group pullback $G_3$ of $G_2$ and a line bundle $L_3$ on $G_3$ that extends $\gamma_2^* L_{A_2}$ along $\kappa_3$.

Third, a result on even cubical structures turns the extended bundle into the required structure. Let $G_2$ be semi-abelian over the base $R_2$, with $\gamma_2$ and a bundle $M$ that extends $\Lambda(\gamma_2^* L_{A_2})$, a uniformised trait over $G_2$, and a line bundle $L_3$ as above. Then there are a finite extension $\rho : R_2 \to R_9$, a group pullback $\beta_9 : G_9 \to G_2$ with a square $\beta_{92}$, and $P$, $A_9$, $\gamma_9$, such that $G_9$ is semi-abelian, $\Lambda(P) \cong \beta_{92}^* M$, $P$ is even on the torus, and $\gamma_9^* L_{A_9} \cong P|_{(G_9)_{K_9}}$. We apply it with $M = \Lambda_{F_2}$.

Now put $\rho_0 = \rho \circ \rho_2$, $G_0 = G_9$, $\beta_0 = \beta_2 \circ \beta_9$ and $\beta_{02} = \beta_{22} \circ \beta_{92}$. A composite of finite extensions is a finite extension: $R_9$ is an admissible base, the composite of injective maps is injective, and finite over finite is finite. A composite of group pullbacks is a group pullback, and the composite of squares is a square. For property 2,
$$\begin{aligned} \Lambda(P) &\cong \beta_{92}^* \Lambda_{F_2} \\ &\cong \beta_{92}^* \beta_{22}^* \Lambda_F = \beta_{02}^* \Lambda_F. \end{aligned}$$
Properties 1, 3 and 4 come from the third input. $\square$

**Theorem 4.9.9 (Even cubical structure on the factor).** In the factor situation, assume that the factor $F$ is algebraic. Then the conclusion of the previous proposition holds: there are a finite extension $\rho_0 : R \to R_0$, a commutative group scheme $G_0$ over $R_0$ with $\beta_0 : G_0 \to G$ that makes it the group pullback of $G$ along $\rho_0$, a square $\beta_{02}$ over $\beta_0$, a cubical symmetric line bundle $P$ on $G_0$, a polarised abelian variety $A_0$ over $K_0$ and an isomorphism of group schemes $\gamma_0 : (G_0)_{K_0} \to A_0$, such that $G_0$ is semi-abelian, $\Lambda(P) \cong \beta_{02}^* \Lambda_F$, $P$ is even on the torus, and $\gamma_0^* L_{A_0} \cong P|_{(G_0)_{K_0}}$.

Lean: `GlobalTheory.Mum.exists_finExt_cp_factor_even` (also `GlobalTheory.T.exists_finExt_cubicalSymmetric_even_factor`, a second name).

*Proof.* We use a result on the pairing of an algebraic factor. Recall that the algebraic condition makes $e^* f e$ positive and symmetric, as a polarisation is. The result says: in the factor situation with $F$ algebraic there are a finite extension $\rho_1 : R \to R_1$, a group pullback $G_1$ of $G$ with a square $\beta_{12}$, a polarised abelian variety $A_1$ over $K_1$ and an isomorphism of group schemes $\gamma_1 : (G_1)_{K_1} \to A_1$ such that $\beta_{12}^* \Lambda_F$ extends $\Lambda(\gamma_1^* L_{A_1})$. The previous proposition then gives the result. $\square$

**Remark 4.9.10 (Formalization).** The second names are wrappers, proved by a `first | exact` tactic. The proposition on a line bundle is a wrapper of `GlobalTheory.Mum.exists_finExt_lbExt_of_factor`, whose proof ([ExistsFiniteExtensionSymmBundleExtensionOnFactor.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteExtensionSymmBundleExtensionOnFactor.lean#L18)) applies `GlobalTheory.T.symmetricPrincipalPolarisation_extends_semiAbelian` and takes $\rho$ to be the identity. So the trait $W$, $\varphi$, $G_W$, $D_W$, $A_W$, $U_W$, $\kappa$ and the whole factor situation are unused. Its name says "symmBundle", but $L_1$ is a bare line bundle, with no cubical or symmetric structure. In the proof of the second proposition ([ExistsEvenCubicalStructureOfIdempotentFactorBiex.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsEvenCubicalStructureOfIdempotentFactorBiex.lean#L21)) the first input is `GlobalTheory.T.exists_finiteExtension_idempotentFactor_trait_unif` and the third is `GlobalTheory.T.exists_evenCubicalStructure_of_genericPolarisation_extension`; the extension $\rho_3$ is passed in, but the final base is reached through $\rho \circ \rho_2$, and the finite extension property of the composite is built by hand at line 36. The given $\rho_1$, $G_1$ and $A_1$ are used only by the first input. The algebraic condition of the theorem is used only by `GlobalTheory.T.factorPairing_mumfordBundle_principal_polarisation` ([ExistsFinExtCubicalSymmetricEvenFactor.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFinExtCubicalSymmetricEvenFactor.lean#L20)), whose name says "principal polarisation", while its conclusion gives only the extension of the Mumford bundle. The converse quoted after the definition of evenness on the torus is `GlobalTheory.T.exists_uniformisation_completeLocal_evenOnTorus`. None of these inputs is in the outline of this chapter.
