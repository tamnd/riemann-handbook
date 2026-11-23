---
title: Gluing flat schemes and abelian schemes
decls:
  - GlobalTheory.FerrandGlue.ferrand_glue_artinian
  - GlobalTheory.T.ferrand_glue_flat_artinian_fibreProduct
  - GlobalTheory.GlueAb.main_of_nontrivial
  - GlobalTheory.GlueAb.main
  - GlobalTheory.T.abelianScheme_glue_artinian_local_fibreProduct
  - GlobalTheory.ArtinGlue.lem_ab
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gluing flat schemes and abelian schemes

The Siegel problem of the first section is representable, and the proof in this chapter goes through deformation theory. One shows that a smooth family classifies Siegel objects over every Artinian local ring, and the step from one Artinian ring to a larger one needs a gluing property of the moduli problem in the sense of Schlessinger ("Functors of Artin rings", Trans. Amer. Math. Soc. 130 (1968), 208 to 222, §2). This section proves the first part of that property. Let $P = R_1 \times_{R_0} R_2$ be a local Artinian ring that is a fibre product along two surjections. A flat scheme over $R_1$ and a flat scheme over $R_2$ that agree over $R_0$ glue to a flat scheme over $P$, and two [abelian schemes](/learn/abelian-varieties/#abelian-schemes) that agree over $R_0$ glue to an abelian scheme over $P$. The gluing of schemes is the pinching construction of Ferrand ("Conducteur, descente et pincement", Bull. Soc. Math. France 131 (2003), 553 to 585). For modules it is the patching of Milnor (*Introduction to Algebraic K-Theory*, Annals of Math. Studies 72, §2).

### Artinian fibre products

**Definition 8.2.1 (Artinian fibre product).** An *Artinian fibre product* is a commutative square of rings with maps $f_1 : P \to R_1$, $f_2 : P \to R_2$, $g_1 : R_1 \to R_0$ and $g_2 : R_2 \to R_0$, such that $g_1 f_1 = g_2 f_2$, the square is cartesian, so that $P = \{(r_1, r_2) : g_1(r_1) = g_2(r_2)\}$, the ring $P$ is local and Artinian, and $g_1$ and $g_2$ are surjective.

In this section we fix an Artinian fibre product. Since $P$ is cartesian, two elements $x, y \in P$ with $f_1(x) = f_1(y)$ and $f_2(x) = f_2(y)$ are equal. Since $P$ is Artinian, it is noetherian, its maximal ideal $\mathfrak{m}$ is nilpotent, and $\mathfrak{m}$ is its only prime ideal (Atiyah and Macdonald, *Introduction to Commutative Algebra*, Chapter 8). See also [local rings and dimension](/learn/commutative-algebra/#local-rings-and-dimension).

**Lemma 8.2.2 (Nilpotent kernels).** Suppose that $g_2$ is surjective and $R_0 \neq 0$. Then $f_1$ is surjective and the kernel of $g_1$ is a nilpotent ideal. Also, for every ring map $f : P \to R$ with $R \neq 0$ the kernel of $f$ is nilpotent and $\operatorname{Spec} f$ is surjective.

Lean: `GlobalTheory.FerrandGlue.kernel_nilpotent` (also `GlobalTheory.GlueAb.pullback_elem`, `GlobalTheory.GlueAb.isNilpotent_ker`, `GlobalTheory.GlueAb.surjective_spec_map`).

*Proof.* Let $r \in R_1$. Since $g_2$ is surjective, there is $s \in R_2$ with $g_2(s) = g_1(r)$. Then $(r, s)$ is an element of $P$, and $f_1(r, s) = r$. So $f_1$ is surjective. Let $J = f_1^{-1}(\ker g_1)$. Since $g_1(1) = 1 \neq 0$ in $R_0$, we have $1 \notin J$, so $J \subseteq \mathfrak{m}$. Choose $n$ with $\mathfrak{m}^n = 0$. Since $f_1$ is surjective, $\ker g_1 = f_1(J)$, and so $(\ker g_1)^n = f_1(J^n) \subseteq f_1(\mathfrak{m}^n) = 0$. For the second claim, $\ker f$ is a proper ideal since $R \neq 0$, so $\ker f \subseteq \mathfrak{m}$ and $(\ker f)^n = 0$. The space $\operatorname{Spec} R$ is not empty, and $\operatorname{Spec} P$ has one point. So $\operatorname{Spec} f$ is surjective. $\square$

**Lemma 8.2.3 (Thickenings).** Let $g : R_1 \to R_0$ be a surjective ring map with nilpotent kernel, let $Y_1$ be a scheme over $R_1$, and let $i : Y_0 \to Y_1$ be the base change of $\operatorname{Spec} g$ to $Y_1$. Then $i$ is a closed immersion and it is surjective.

Lean: `GlobalTheory.FerrandGlue.thickening_of_isPullback`.

*Proof.* The map $\operatorname{Spec} g$ is a closed immersion since $g$ is surjective. Let $\mathfrak{p}$ be a prime of $R_1$ and $a \in \ker g$. Then $a^n = 0 \in \mathfrak{p}$ for some $n$, so $a \in \mathfrak{p}$. Thus every prime of $R_1$ contains $\ker g$, and $\operatorname{Spec} g$ is surjective. Closed immersions and surjective maps are stable under base change. $\square$

### Gluing flat schemes

We use three results on the pinching of schemes. We state them as we use them.

1. (Pushout of thickenings.) Let $i_1 : Y_0 \to Y_1$ and $i_2 : Y_0 \to Y_2$ be closed immersions that are surjective, such that on every affine open the kernel of the map of rings of functions is nilpotent. Then there are a scheme $Y$ and closed immersions $j_1 : Y_1 \to Y$ and $j_2 : Y_2 \to Y$ with $j_1 i_1 = j_2 i_2$, such that the square is a pushout of schemes and, for every open $V$ of $Y$, the ring $\mathcal{O}_Y(V)$ is the fibre product of $\mathcal{O}_{Y_1}(j_1^{-1}V)$ and $\mathcal{O}_{Y_2}(j_2^{-1}V)$ over $\mathcal{O}_{Y_0}((j_1 i_1)^{-1}V)$. This is in Ferrand's paper. The kernel condition on affine opens follows from the second lemma above and from the nilpotence of $\ker g_1$ and $\ker g_2$.
2. (Flatness of the pushout.) Suppose that $\ker g_1$ and $\ker g_2$ are nilpotent. Let $Y_1$ be flat over $R_1$ and $Y_2$ be flat over $R_2$, let $Y_0$ be a scheme over $R_0$ with maps $i_1$, $i_2$ that identify $Y_0$ with $Y_1 \times_{R_1} R_0$ and with $Y_2 \times_{R_2} R_0$, and let $Y$ be the pushout of result 1, with its map $y : Y \to \operatorname{Spec} P$. Then $Y$ is flat over $P$, and $j_1$ and $j_2$ identify $Y_1$ with $Y \times_P R_1$ and $Y_2$ with $Y \times_P R_2$. On affine opens this is the statement for modules of Schlessinger (§3) and Milnor (§2).
3. (Zero ring.) The conclusion of the theorem below holds if $R_0 = 0$. In that case $P = R_1 \times R_2$ is local, so $R_1 = 0$ or $R_2 = 0$, and the other ring is $P$.

**Theorem 8.2.4 (Ferrand gluing over an Artinian fibre product).** Let $P = R_1 \times_{R_0} R_2$ be an Artinian fibre product. Let $Y_1$ be a flat scheme over $R_1$, $Y_2$ a flat scheme over $R_2$, and $Y_0$ a scheme over $R_0$, with maps $i_1 : Y_0 \to Y_1$ and $i_2 : Y_0 \to Y_2$ that identify $Y_0$ with $Y_1 \times_{R_1} R_0$ and with $Y_2 \times_{R_2} R_0$. Then there are a flat scheme $Y$ over $P$ and maps $j_1 : Y_1 \to Y$ and $j_2 : Y_2 \to Y$ that identify $Y_1$ with $Y \times_P R_1$ and $Y_2$ with $Y \times_P R_2$, such that $Y$ is the pushout of $i_1$ and $i_2$.

Lean: `GlobalTheory.FerrandGlue.ferrand_glue_artinian` (also `GlobalTheory.T.ferrand_glue_flat_artinian_fibreProduct`).

*Proof.* If $R_0 = 0$, result 3 gives the claim. Suppose that $R_0 \neq 0$. The first lemma, applied to the square and to the square with the two sides exchanged, shows that $\ker g_1$ and $\ker g_2$ are nilpotent. The second lemma shows that $i_1$ and $i_2$ are closed immersions and surjective. Result 1 gives the pushout $Y$ with $j_1$ and $j_2$. The maps $Y_1 \to \operatorname{Spec} R_1 \to \operatorname{Spec} P$ and $Y_2 \to \operatorname{Spec} R_2 \to \operatorname{Spec} P$ agree on $Y_0$, since $g_1 f_1 = g_2 f_2$. So they give a map $y : Y \to \operatorname{Spec} P$ by the universal property of the pushout. Result 2 shows that $Y$ is flat over $P$ and that the two squares are cartesian. $\square$

### Gluing abelian schemes

**Definition 8.2.5 (Group pullback).** Let $f : S' \to S$ be a map of schemes, $G$ a group scheme over $S$ and $G'$ a group scheme over $S'$. A map $\varphi : G' \to G$ is a *group pullback* along $f$ if it identifies $G'$ with $G \times_S S'$ and, for every scheme $T$ over $S'$ and all $x, y \in G'(T)$, we have $\varphi(xy) = \varphi(x)\varphi(y)$ in $G(T)$.

An abelian scheme over $S$ is a commutative group scheme over $S$ that is smooth, proper and geometrically connected. We use two more results.

4. (Glued group law.) In the theorem above, suppose that $Y_1$ and $Y_2$ are commutative group schemes and that $i_1$ and $i_2$ are group pullbacks. Then $Y$ has a structure of commutative group scheme over $P$ for which $j_1$ and $j_2$ are group pullbacks.
5. (Finite presentation.) Let $P$ be noetherian, $f_1 : P \to R_1$ surjective with nilpotent kernel, and $Y$ a scheme over $P$ such that $Y \times_P R_1$ is locally of finite presentation over $R_1$. Then $Y$ is locally of finite presentation over $P$.
6. (Lifting properness.) Let $\pi : R \to R'$ be surjective with nilpotent kernel and $X$ a smooth scheme over $R$ such that $X \times_R R'$ is proper and geometrically connected over $R'$. Then $X$ is proper and geometrically connected over $R$.

**Lemma 8.2.6 (Smoothness on fibres).** Consider a cartesian square of schemes with $p : Y \to X$ the base change of $p' : Y' \to X'$ along $\pi : X \to X'$. If $\pi$ is surjective, $p'$ is flat and locally of finite presentation, and $p$ is smooth, then $p'$ is smooth.

Lean: `GlobalTheory.smooth_of_isPullback_of_surjective_of_flat`.

*Proof.* A flat map locally of finite presentation is smooth if all its fibres are smooth (EGA IV$_4$, Théorème 17.5.1). Let $y' \in X'$ and choose $y \in X$ with $\pi(y) = y'$. The fibre of $p$ over $y$ is the base change of the fibre of $p'$ over $y'$ along the field extension $\kappa(y') \to \kappa(y)$. It is smooth since $p$ is smooth, and smoothness over a field descends along a field extension (EGA IV$_4$, §17). $\square$

**Lemma 8.2.7 (Gluing abelian schemes, case $R_1 \neq 0$).** Let $P = R_1 \times_{R_0} R_2$ be an Artinian fibre product with $R_1 \neq 0$. Let $A_1$ and $A_2$ be abelian schemes over $R_1$ and $R_2$, let $A_0$ be a group scheme over $R_0$, and let $\psi_1 : A_0 \to A_1$ and $\psi_2 : A_0 \to A_2$ be group pullbacks along $g_1$ and $g_2$. Then there are an abelian scheme $A$ over $P$ and group pullbacks $\varphi_1 : A_1 \to A$ along $f_1$ and $\varphi_2 : A_2 \to A$ along $f_2$ with $\varphi_1 \psi_1 = \varphi_2 \psi_2$.

Lean: `GlobalTheory.GlueAb.main_of_nontrivial`.

*Proof.* Smooth maps are flat, so the theorem above applies to $A_1$, $A_2$ and $A_0$. It gives a flat scheme $A$ over $P$ with $j_1$, $j_2$ as there. Result 4 makes $A$ a commutative group scheme and $j_1$, $j_2$ group pullbacks. Put $\varphi_1 = j_1$ and $\varphi_2 = j_2$. Since $g_2$ is surjective, $f_1$ is surjective by the first lemma, and $\ker f_1$ is nilpotent since $R_1 \neq 0$. The ring $P$ is noetherian, and $A_1$ is locally of finite presentation over $R_1$, so result 5 shows that $A$ is locally of finite presentation over $P$. The map $\operatorname{Spec} f_1$ is surjective, $A$ is flat over $P$, and $A \times_P R_1 = A_1$ is smooth. The lemma on fibres shows that $A$ is smooth over $P$. Result 6 shows that $A$ is proper and geometrically connected over $P$. $\square$

**Theorem 8.2.8 (Gluing abelian schemes over an Artinian fibre product).** Let $P = R_1 \times_{R_0} R_2$ be an Artinian fibre product. Let $A_1$ and $A_2$ be abelian schemes over $R_1$ and $R_2$, let $A_0$ be a group scheme over $R_0$, and let $\psi_1 : A_0 \to A_1$ and $\psi_2 : A_0 \to A_2$ be group pullbacks along $g_1$ and $g_2$. Then there are an abelian scheme $A$ over $P$ and group pullbacks $\varphi_1 : A_1 \to A$ along $f_1$ and $\varphi_2 : A_2 \to A$ along $f_2$ with $\varphi_1 \psi_1 = \varphi_2 \psi_2$.

Lean: `GlobalTheory.GlueAb.main` (also `GlobalTheory.T.abelianScheme_glue_artinian_local_fibreProduct`, `GlobalTheory.ArtinGlue.lem_ab`).

*Proof.* If $R_1 \neq 0$, the lemma gives the claim. Suppose that $R_1 = 0$. Then $R_2 \neq 0$: otherwise $f_1(0) = f_1(1)$ and $f_2(0) = f_2(1)$, so $0 = 1$ in $P$, but $P$ is local. Apply the lemma to the square with the indices $1$ and $2$ exchanged. $\square$

The theorem does not ask that $A_0$ is an abelian scheme. This follows from the hypotheses, since $A_0$ is the base change of $A_1$.

**Remark 8.2.9 (Formalization).** The case $R_0 = 0$ of the Ferrand gluing is a separate input, called at [FerrandGlueFlatArtinianFibreProduct.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FerrandGlueFlatArtinianFibreProduct.lean#L60). The lemma on nilpotent kernels takes only the surjectivity of $g_2$, not of $g_1$: [FerrandGlueFlatArtinianFibreProduct.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FerrandGlueFlatArtinianFibreProduct.lean#L18). The gluing of abelian schemes first treats $R_1 \neq 0$ and then exchanges the indices: [AbelianSchemeGlueArtinianLocalFibreProduct.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeGlueArtinianLocalFibreProduct.lean#L82). In that file $A_0$ is only a group object. A group pullback is a cartesian square together with multiplicativity on $T$-points: [IsGrpPullback.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/IsGrpPullback.lean#L25). The statement wrappers call the proofs through a `first` tactic with a raised heartbeat limit: [FerrandGlueFlatArtinianFibreProductStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FerrandGlueFlatArtinianFibreProductStatement.lean#L10). The name `GlobalTheory.ArtinGlue.lem_ab` is a second name for the gluing theorem of abelian schemes. We read the statements of results 1 to 6, not their proofs.
