---
title: Data with the same polarisation
decls:
  - GlobalTheory.MumCmp.point_and_compare
  - GlobalTheory.T.exists_orderTwo_point_refinements_compare_unif
  - GlobalTheory.TwistSec.exists_sec_compare
  - GlobalTheory.T.exists_orderTwo_section_translate_refinement
  - GlobalTheory.MumTwist.exists_twist
  - GlobalTheory.T.exists_orderTwo_section_evenTranslate_samePolarisedData
  - GlobalTheory.Mum.samePol_unif_finExt
  - GlobalTheory.T.samePolarisedData_uniformise_finite_extension
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Data with the same polarisation

Two sets of degeneration data can have the same abelian scheme, the same periods and the same polarisation, and still differ in the line bundle $L$ and the trivialisations $\psi$. This section proves that if one of them is realised by a semi-abelian scheme $G$, then the other is realised, after a finite extension, by a group pullback of $G$, with a line bundle whose Mumford bundle is unchanged. The line bundle is a translate of the given one by a section of order two. [The theorem on the idempotent factor](/entry/semiabelian-uniformization-linear-action-descent/) uses this result to replace the data that a line bundle produces by the data $D$ of the factor.

Throughout, $R$ is a base with maximal ideal $\mathfrak{m}$ and fraction field $K$. We use group pullbacks, squares and the Mumford bundle $\Lambda(L)$ as in [the section on even cubical structures](/entry/exists-fin-ext-cp-factor-even/). For a section $a$ of a commutative group scheme $G$ we write $t_a : G \to G$, $x \mapsto a + x$, for the translation by $a$.

### Same polarisation and twists

**Definition 4.10.1 (Same polarisation).** Let $D_0$ and $D$ be degeneration data over $R$. We say that $D_0$ and $D$ have the *same polarisation* if there are polarised degeneration data $Q$ over $R$ and isomorphisms of the character lattices of $D_0$ and of $D$ with that of $Q$, such that both $D_0$ and $D$ refine $Q$.

Lean: `GlobalTheory.Mum.SamePol`.

Polarised degeneration data record an abelian scheme $B_Q$ with a line bundle, a lattice, a map $c$ and the values $\tau$. Data $D$ refine $Q$ if $B$ is isomorphic to $B_Q$ as a group, $\Lambda(L)$ is isomorphic to the Mumford bundle of $Q$ by a rigidified generating isomorphism, $c$ matches the map of $Q$, and $\tau$ matches the values of $Q$ through this isomorphism. So data with the same polarisation have the same $B$, the same $c$, the same Mumford bundle $\Lambda(L)$ and the same $\tau$; they can differ in $L$ and in $\psi$.

A point of the Raynaud extension $\widetilde G$ of $D$ with values in $R$ is a pair $g = (b, s)$ with $b \in B(R)$ and, for each $\chi \in \mathsf{X}$, a generator $s_\chi$ of the fibre of $\Lambda(L)^{-1}$ at $(c(\chi), b)$, with $s_0 = 1$ and $s$ multiplicative through the cubical structure, as for the points over a field in [the section on torsion](/entry/tate-tens/). These points form a group, and we write $2 g = 0$ if $g + g$ is the zero point.

**Definition 4.10.2 (Twist).** Let $D_0$ and $D$ be degeneration data over $R$ and let $g = (b, s)$ be a point of $\widetilde G$ with values in $R$. We say that $D_0$ is the *twist of $D$ by $g$* if there are an isomorphism of groups $\beta : B_0 \to B$ and an isomorphism of lattices $\epsilon : \mathsf{X}_0 \to \mathsf{X}$ with $\beta \circ c_0 = c \circ \epsilon$, and a generating isomorphism
$$L_0 \cong \beta^* t_b^* L \otimes L_b^{-1} \otimes L_0',$$
where $L_b$ and $L_0'$ are the fibres of $L$ at $b$ and at $0$, under which $\psi_0(\chi)$ corresponds to $\psi(\epsilon \chi) \cdot s_{\epsilon \chi}$ for every $\chi \in \mathsf{X}_0$.

Lean: `GlobalTheory.MumCmp.IsTwist`.

Translating a cubical $L$ by $b$ does not change $\Lambda(L)$ (see the proof of the theorem below), so a twist keeps the Mumford bundle of the data. Input (a) in the next proof is a converse: data with the same polarisation are twists of each other.

Let $G$ be a group scheme over $R$ and $U$ a uniformisation of $(A, G)$ by $D$. For $e \geq 0$, $U$ identifies $G \otimes_R R/\mathfrak{m}^{e+1}$ with $\widetilde G \otimes_R R/\mathfrak{m}^{e+1}$. Let $a$ be a section of $G$ over $R$ and $g = (b, s)$ a point of $\widetilde G$ with values in $R$. We say that *$a$ lifts $g$* if, for every $e \geq 0$, the restriction $a_e$ of $a$ to $R/\mathfrak{m}^{e+1}$, read in $\widetilde G \otimes_R R/\mathfrak{m}^{e+1}$, is the reduction of $g$: the image of $a_e$ in $B$ is $b \bmod \mathfrak{m}^{e+1}$, and for each $\chi$ the value at $a_e$ of the generator of the uniformisation for $\chi$ corresponds to $s_\chi \bmod \mathfrak{m}^{e+1}$.

### The results

**Lemma 4.10.3 (A point of order two that compares the data).** Let $D_0$ and $D$ be degeneration data over $R$ with the same polarisation. Let $G$ be a commutative semi-abelian scheme over $R$, $A$ a polarised abelian variety over $K$ and $U$ a uniformisation of $(A, G)$ by $D$. Then there is a point $g$ of $\widetilde G$ with values in $R$ and $2 g = 0$ with the following property. Let $a$ be a section of $G$ with $2 a = 0$ that lifts $g$, let $A_2$ be a polarised abelian variety over $K$, $D_2$ degeneration data over $R$ and $U_2$ a uniformisation of $(A_2, G)$ by $D_2$ with a generating isomorphism $L_{U_2} \cong t_a^* L_U$. Then there are a finite extension $\rho : R \to R'$ that is a local map, a pullback $D_1$ of $D_0$ along $\rho$ and a pullback $D_2'$ of $D_2$ along $\rho$, such that $D_2'$ is a pullback of $D_1$ along the identity of $R'$.

Lean: `GlobalTheory.MumCmp.point_and_compare` (also `GlobalTheory.T.exists_orderTwo_point_refinements_compare_unif`, a second name).

*Proof.* We use three inputs on twists.

(a) If $D_0$ and $D$ have the same polarisation, there is a point $g$ of $\widetilde G$ with values in $R$, with $2 g = 0$, such that $D_0$ is the twist of $D$ by $g$.

(b) If $U$ and $U_2$ are uniformisations of $G$ by $D$ and by $D_2$, $a$ is a section with $2a = 0$ that lifts a point $g$ with $2 g = 0$, and $L_{U_2} \cong t_a^* L_U$, then $D_2$ is the twist of $D$ by $g$.

(c) Two twists of $D$ by the same point are isomorphic: each is a pullback of the other along the identity.

Take $g$ from (a). Given $a$ and $U_2$, input (b) shows that $D_2$ is the twist of $D$ by $g$, and (c) shows that $D_2$ is a pullback of $D_0$ along the identity of $R$. Now take $R' = R$ and $\rho = 1$, which is a finite extension and a local map. Every set of data is a pullback of itself along the identity, so we can take $D_1 = D_0$ and $D_2' = D_2$. $\square$

The idea of input (b) is this: the translate $t_a^* L_U$ restricted to the thickenings of the closed fibre is the translate of the pullback of $L$ to $\widetilde G$ by $g$, and its periods are the periods of $U$ multiplied by $s$.

**Lemma 4.10.4 (A section of order two that compares the data).** Let $D_0$, $D$, $G$, $A$ and $U$ be as in the previous lemma. Then there is a section $a$ of $G$ with $2 a = 0$ with the following property. Let $A_2$ be a polarised abelian variety over $K$, $D_2$ degeneration data over $R$ and $U_2$ a uniformisation of $(A_2, G)$ by $D_2$ with a generating isomorphism $L_{U_2} \cong t_a^* L_U$. Then there are a finite extension $\rho : R \to R'$ that is a local map and a pullback $D_1$ of $D_0$ along $\rho$, such that every pullback $D'$ of $D_2$ along $\rho$ is a pullback of $D_1$ along the identity of $R'$.

Lean: `GlobalTheory.TwistSec.exists_sec_compare` (also `GlobalTheory.T.exists_orderTwo_section_translate_refinement`, a second name).

*Proof.* Take $g$ from the previous lemma. Since $G$ is semi-abelian over the complete ring $R$ and $2 g = 0$, the point $g$ lifts to a section of $G$: there is a section $a$ with $2 a = 0$ that lifts $g$. Given $U_2$, the previous lemma gives $\rho$, $D_1$ and a pullback $D_2'$ of $D_2$ along $\rho$ with $D_2'$ a pullback of $D_1$ along the identity. Let $D'$ be another pullback of $D_2$ along $\rho$. Two pullbacks of the same data along the same map are pullbacks of each other along the identity, so $D'$ is a pullback of $D_2'$ along the identity. A composite of pullbacks along injective maps is a pullback along the composite, so $D'$ is a pullback of $D_1$ along the identity. $\square$

**Proposition 4.10.5 (An even translate of order two).** Let $D_0$, $D$, $G$, $A$ and $U$ be as before. Then there are a section $a$ of $G$ with $2a = 0$, a cubical symmetric line bundle $P$ on $G$, a polarised abelian variety $A_2$ over $K$ and an isomorphism of group schemes $\gamma_2 : G_K \to A_2$, with these properties:

1. there is a generating isomorphism $P \cong t_a^* L_U$, and $P$ is even on the torus;
2. there is a generating isomorphism $\gamma_2^* L_{A_2} \cong P|_{G_K}$;
3. for all degeneration data $D_2$ over $R$ and every uniformisation $U_2$ of $(A_2, G)$ by $D_2$ with line bundle $P$, there are a finite extension $\rho : R \to R'$ that is a local map and a pullback $D_1$ of $D_0$ along $\rho$, such that every pullback $D'$ of $D_2$ along $\rho$ is a pullback of $D_1$ along the identity of $R'$.

Lean: `GlobalTheory.MumTwist.exists_twist` (also `GlobalTheory.T.exists_orderTwo_section_evenTranslate_samePolarisedData`, a second name).

*Proof.* Take $a$ from the previous lemma. A translate of the line bundle of a uniformisation by a section of order two carries a cubical symmetric structure that is even on the torus: there is a cubical symmetric $P$ with $P \cong t_a^* L_U$ that is even on the torus. Its restriction to the generic fibre is the line bundle of a polarised abelian variety: there are $A_2$ and $\gamma_2$ with property 2. For property 3, a uniformisation $U_2$ with line bundle $P$ satisfies $L_{U_2} = P \cong t_a^* L_U$, and the previous lemma applies. $\square$

The order two of $a$ is what makes the translate symmetric: $[-1]^* t_a^* L = t_{-a}^* [-1]^* L$, and $-a = a$.

**Theorem 4.10.6 (Data with the same polarisation).** Let $D_0$ and $D$ be degeneration data over $R$ with the same polarisation. Let $G$ be a commutative semi-abelian scheme over $R$, $A$ a polarised abelian variety over $K$ and $U$ a uniformisation of $(A, G)$ by $D$. Then there are a finite extension $\rho : R \to R'$, a pullback $D_1$ of $D_0$ along $\rho$, a group scheme $G_1$ over $R'$ with a morphism $\beta : G_1 \to G$ that makes it the group pullback of $G$ along $\rho$, a square $\beta_2$ over $\beta$, a polarised abelian variety $A_1$ over the fraction field of $R'$ and a uniformisation $U_1$ of $(A_1, G_1)$ by $D_1$, with a generating isomorphism $\Lambda(L_{U_1}) \cong \beta_2^* \Lambda(L_U)$.

Lean: `GlobalTheory.Mum.samePol_unif_finExt` (also `GlobalTheory.T.samePolarisedData_uniformise_finite_extension`, a second name).

*Proof.* The previous proposition gives $a$, $P$, $A_2$ and $\gamma_2$. Since $G$ is semi-abelian, $P$ is even on the torus and $\gamma_2^* L_{A_2} \cong P|_{G_K}$, there are degeneration data $D_2$ and a uniformisation $U_2$ of $(A_2, G)$ by $D_2$ with line bundle $P$; this is the converse stated in [the section on even cubical structures](/entry/exists-fin-ext-cp-factor-even/). Property 3 gives a finite extension $\rho : R \to R'$, local, and a pullback $D_1$ of $D_0$ along $\rho$.

Base change of the uniformisation $U_2$ along $\rho$ gives a pullback $D'$ of $D_2$ along $\rho$, a polarised abelian variety $A'$ and a uniformisation $U'$ of $(A', G_1)$ by $D'$, where $G_1 = G \otimes_R R'$ with its projection $\beta : G_1 \to G$; the line bundle of $U'$ is the pullback of $P$. By property 3, $D'$ is a pullback of $D_1$ along the identity, and a uniformisation by $D'$ transfers to a uniformisation $U_1$ of $(A', G_1)$ by $D_1$ with the same line bundle. The projection $\beta$ makes $G_1$ the group pullback of $G$, and there is a square $\beta_2$ over it with $\Lambda(\beta^* M) \cong \beta_2^* \Lambda(M)$ for line bundles $M$ on $G$.

It remains to compare the Mumford bundles. For a cubical line bundle $L$, a section $a$ and a line bundle $N \cong t_a^* L$, we have $\Lambda(N) \cong \Lambda(L)$: the fibres $L_{x + y + a} \otimes L_{x + a}^{-1} \otimes L_{y + a}^{-1} \otimes L_a$ and $L_{x + y} \otimes L_x^{-1} \otimes L_y^{-1} \otimes L_0$ are identified by the cubical structure applied to $(x, y, a)$. So
$$\begin{aligned} \Lambda(L_{U_1}) &= \Lambda(\beta^* P) \cong \beta_2^* \Lambda(P) \\ &\cong \beta_2^* \Lambda(t_a^* L_U) \cong \beta_2^* \Lambda(L_U). \end{aligned}$$
$\square$

**Remark 4.10.7 (Formalization).** The second names are wrappers, proved by a `first | exact` tactic. In the first lemma ([ExistsOrderTwoPointRefinementsCompareUnif.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsOrderTwoPointRefinementsCompareUnif.lean#L28)) the finite extension is the identity of $R$, so the finite extensions in all four results are the identity; the statements hide this. The inputs (a), (b) and (c) are `GlobalTheory.T.exists_twoTorsion_twist_of_same_polarisedData`, `GlobalTheory.T.uniformisationData_translate_orderTwo_isTwist` and `GlobalTheory.T.nonempty_isPullDeg_of_same_torus_twist`; they are bound by `have` at lines 18 to 20, before the variables are introduced. The lift of $g$ is `GlobalTheory.T.exists_twoTorsion_section_lift_torusExtension`; the even translate is `GlobalTheory.T.exists_evenCubicalSymmetricBundle_translate_orderTwo`; and property 2 is `GlobalTheory.T.exists_principal_polarisation_genericFibre_twoTorsion_translate` ([ExistsOrderTwoSectionEvenTranslateSamePolarisedD.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsOrderTwoSectionEvenTranslateSamePolarisedD.lean#L21)), whose name says "principal polarisation", while its conclusion gives only the isomorphism of line bundles. In the theorem, the fact $2a = 0$ is dropped at [SamePolarisedDataUniformiseFiniteExtension.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SamePolarisedDataUniformiseFiniteExtension.lean#L24); the converse is `GlobalTheory.T.exists_uniformisation_completeLocal_evenOnTorus`, the translation invariance is `GlobalTheory.T.mumfordBundle_translate_iso_cubical`, and the square is `GlobalTheory.T.exists_mumfordBundle_pullback_grpPullback`. We did not unfold the definition of refinement beyond the properties listed after the definition of the same polarisation.
