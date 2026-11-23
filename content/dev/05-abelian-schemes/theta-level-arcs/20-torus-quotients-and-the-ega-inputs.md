---
title: Torus quotients and the EGA inputs
decls:
  - GlobalTheory.SS.MaxTorus.exists_quot_no_cocharacter
  - GlobalTheory.LN.ega_of_laws
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Torus quotients and the EGA inputs

This last section proves two separate results. The first is on a smooth connected group $G$ over an algebraically closed field $k$. There is a split torus $T \subset G$ with a quotient $B = G/T$ that has no nontrivial cocharacter: every homomorphism $\mathbb{G}_m \to B$ is trivial. In the semi-abelian case $T$ is the torus part and $B$ is the abelian quotient. The result is used to find torus extensions in special fibres. The second result states the four inputs from EGA that the chapter uses: algebraization of formal schemes with line bundles, of morphisms and of sections, and a description of line bundles of degree zero on abelian schemes. It derives them from the first two bundles of laws. Both results enter the main proof at [the step on every character](/step/every-character/).

### Split tori and quotients

Let $S$ be a scheme. For a free abelian group $X$ of finite rank, the *split torus* $T_X$ over $S$ is $\operatorname{Spec} \mathcal{O}_S[X]$, with character group $X$. A homomorphism $\varphi : Y \to X$ gives a homomorphism $T_\varphi : T_X \to T_Y$. We write $\mathbb{G}_m = T_{\mathbb{Z}}$.

**Definition 6.20.1 (Good open set).** Let $G$ be a group scheme over $S$ and $i : T_X \to G$ a homomorphism. An open set $V$ of $G$ is *good* for $i$ if $V$ is affine, $V$ is stable under the action of $T_X$ by $i$, and there is a homomorphism $\chi \mapsto u_\chi$ from $X$ to the units on $V$ such that each $u_\chi$ has weight $\chi$: $u_\chi(i(t) g) = \chi(t) u_\chi(g)$ for all points $t$ of $T_X$ and $g$ of $V$.

Lean: `GlobalTheory.SS.GoodOpen`.

**Definition 6.20.2 (Torus quotient).** A pair of homomorphisms $i : T \to G$ and $q : G \to B$ of group schemes over $S$ is a *torus quotient* if $q$ is flat, surjective and affine, the square of $i$, $q$ and the unit of $B$ is a pullback square, and $B$ is smooth and connected.

Lean: `GlobalTheory.SS.IsQuot`.

So $i$ is the kernel of $q$. In particular $i$ is a monomorphism, since the unit of $B$ is one, and $q \circ i = 1$.

### Inputs

In the inputs, $k$ is a field and $G$ is a smooth connected group over $k$.

**Theorem 6.20.3 (Quotient by a good torus).** Let $i : T_X \to G$ be a homomorphism such that every point of $G$ lies in a good open set for $i$. Then there is a torus quotient $i, q : G \to B$. If $G$ has dimension $g$, then $B$ has dimension $a$ with $g = a + \operatorname{rank} X$.

Lean: `GlobalTheory.T.exists_smooth_torus_quotient_of_goodOpen_cover`.

**Theorem 6.20.4 (Image of a torus).** Let $k$ be algebraically closed and $i : T_X \to G$ a homomorphism. Then there are a free abelian group $X'$ of finite rank, a homomorphism $i' : T_{X'} \to G$ such that every point of $G$ lies in a good open set for $i'$, and a surjective homomorphism $\rho : T_X \to T_{X'}$ with $i' \circ \rho = i$.

Lean: `GlobalTheory.T.splitTorus_image_factor_quotient_goodOpen`.

**Theorem 6.20.5 (Lifting cocharacters).** Let $k$ be algebraically closed and let $i, q : G \to B$ be a torus quotient with $i : T_X \to G$. Every homomorphism $f : \mathbb{G}_m \to B$ lifts to a homomorphism $j : \mathbb{G}_m \to G$ with $q \circ j = f$.

Lean: `GlobalTheory.T.exists_lift_oneParameter_quotient_torus`.

### Lemmas on tori

**Lemma 6.20.6 (Monomorphisms of tori).** Let $S$ be nonempty and $\varphi : Y \to X$ a homomorphism. If $T_\varphi : T_X \to T_Y$ is a monomorphism, then $\varphi$ is surjective.

Lean: `GlobalTheory.SS.MaxTorus.surjective_of_mono`.

*Proof.* Let $\pi : X \to X / \varphi(Y)$. Then $\pi \circ \varphi = 0 \circ \varphi$, so $T_\varphi \circ T_\pi = T_\varphi \circ T_0$. Since $T_\varphi$ is a monomorphism, $T_\pi = T_0$. As $S$ is nonempty, $\psi \mapsto T_\psi$ is injective, so $\pi = 0$ and $\varphi$ is surjective. $\square$

**Lemma 6.20.7 (Surjections of lattices).** Let $X$ and $Y$ be free abelian groups of finite rank with $\operatorname{rank} Y \leq \operatorname{rank} X$. Then a surjective homomorphism $\varphi : Y \to X$ is injective.

Lean: `GlobalTheory.SS.MaxTorus.injective_of_surjective`.

*Proof.* Surjectivity gives $\operatorname{rank} X \leq \operatorname{rank} Y$, so the ranks are equal and $Y \cong X$. A surjective endomorphism of a finitely generated module over a commutative ring is injective. $\square$

**Lemma 6.20.8 (Inverses of tori).** Let $S$ be connected, and let $\sigma : T_X \to T_Y$ be a homomorphism and a monomorphism, with $\operatorname{rank} Y \leq \operatorname{rank} X$. Then there is $\tau : T_Y \to T_X$ with $\sigma \circ \tau = \mathrm{id}$.

Lean: `GlobalTheory.SS.MaxTorus.exists_inv`.

*Proof.* Over a connected base, every homomorphism of split tori is $T_\varphi$ for a homomorphism $\varphi : Y \to X$. By the two lemmas above, $\varphi$ is bijective. Let $\tau = T_{\varphi^{-1}}$. $\square$

### The maximal torus quotient

**Theorem 6.20.9 (Quotient with no cocharacter).** Let $k$ be an algebraically closed field and let $G$ be a smooth connected group over $k$. Then there are a free abelian group $X$ of finite rank, a group scheme $B$ over $k$, and a torus quotient $i : T_X \to G$, $q : G \to B$, such that every homomorphism $f : \mathbb{G}_m \to B$ equals $1$.

Lean: `GlobalTheory.SS.MaxTorus.exists_quot_no_cocharacter`.

*Proof.* The scheme $G$ is connected, so it has a dimension $g$. For $n \in \mathbb{N}$, let $P(n)$ say that there is a homomorphism $i : T_X \to G$ with $\operatorname{rank} X = n$ such that every point of $G$ lies in a good open set for $i$. If $P(n)$ holds, then the theorem on quotients by a good torus gives $g = a + n$, so $n \leq g$. The theorem on the image of a torus, applied to the trivial torus, gives some $n_0$ with $P(n_0)$. Let $n$ be the greatest $n \leq g$ with $P(n)$, and let $i : T_X \to G$ be a homomorphism for it. The theorem on quotients by a good torus gives a torus quotient $i, q : G \to B$.

Let $f : \mathbb{G}_m \to B$ be a homomorphism. The theorem on lifting cocharacters gives $j : \mathbb{G}_m \to G$ with $q \circ j = f$. Let $\phi : T_{X \times \mathbb{Z}} = T_X \times \mathbb{G}_m \to G$ be the homomorphism $(t, u) \mapsto i(t) j(u)$. The theorem on the image of a torus gives $X'$, $i' : T_{X'} \to G$ and a surjective $\rho$ with $i' \circ \rho = \phi$. By the choice of $n$, $\operatorname{rank} X' \leq \operatorname{rank} X$.

Let $\sigma : T_X \to T_{X'}$ be $\rho$ on the first factor. Then $i' \circ \sigma = i$. Since $i$ is a monomorphism, so is $\sigma$. The lemma on inverses of tori gives $\tau$ with $\sigma \circ \tau = \mathrm{id}$, so $i' = i \circ \tau$. Now $j$ is $\phi$ on the second factor, so $j = i' \circ \rho'$ for $\rho'$ the restriction of $\rho$ to $\mathbb{G}_m$. Hence $f = q \circ j = q \circ i \circ \tau \circ \rho' = 1$, since $q \circ i = 1$. $\square$

### The EGA inputs

In this part, $R$ is a noetherian local domain and $I \neq R$ is an ideal such that $R$ is complete for $I$ and for its maximal ideal. Let $R_e = R / I^{e+1}$.

**Definition 6.20.10 (Algebraization of schemes).** *Algebraization of schemes* holds if, for all such $R$ and $I$, the following is true. Let $Y_e$ be smooth over $R_e$ with maps $Y_e \to Y_{e+1}$ that make $Y_e$ the pullback of $Y_{e+1}$ to $R_e$, and let $N_e$ be line bundles on $Y_e$ with isomorphisms between $N_e$ and the pullback of $N_{e+1}$, with $N_0$ relatively ample. Then there are a projective smooth scheme $B$ over $R$ with a relatively ample line bundle $M$ and maps $b_e : Y_e \to B$ that make $Y_e$ the pullback of $B$ to $R_e$, compatible with the maps $Y_e \to Y_{e+1}$, with $N_e \cong b_e^* M$.

Lean: `GlobalTheory.LN.AlgSt`.

**Definition 6.20.11 (Algebraization of morphisms).** *Algebraization of morphisms* holds if, for all such $R$ and $I$ and all projective $Y$ and $Z$ over $R$ with $Y$ smooth, every compatible system of maps $f_e : Y \otimes R_e \to Z$ over $R$ comes from a unique map $Y \to Z$.

Lean: `GlobalTheory.LN.MorAlgSt`.

**Definition 6.20.12 (Algebraization of sections).** *Algebraization of sections* holds if, for every domain $R$ complete for an ideal $I$, every smooth projective $Y$ over $R$ and every line bundle $N$ on $Y$, a compatible system of sections of $N$ over the $Y \otimes R_e$ comes from a unique section of $N$, where compatibility is tested in local frames.

Lean: `GlobalTheory.LN.SecAlgSt`.

**Definition 6.20.13 (Degree zero condition).** The *degree zero condition* holds if, for every noetherian local ring $A$, every principally polarized abelian scheme $(P, \mathcal{L})$ over $A$ and every line bundle $\mathcal{O}$ on $P$ whose second-order cube bundle on $P \times P$ is trivial, there is a point $x$ of $P$ with $\mathcal{O} \cong t_x^* \mathcal{L} \otimes \mathcal{L}^{-1}$.

Lean: `GlobalTheory.LN.PicardZeroDegenerationCondition`.

**Definition 6.20.14 (The EGA inputs).** The *EGA inputs* hold if algebraization of schemes, of morphisms and of sections and the degree zero condition hold.

Lean: `GlobalTheory.LN.Ega`.

**Theorem 6.20.15 (Schemes from the laws).** If the first two bundles of laws hold, then algebraization of schemes holds.

Lean: `GlobalTheory.T.compatible_line_bundles_formal_thickening`.

**Theorem 6.20.16 (Morphisms from the laws).** If the first two bundles of laws hold, then algebraization of morphisms holds.

Lean: `GlobalTheory.T.existsUnique_hom_of_thickenings'`.

**Theorem 6.20.17 (Sections).** Algebraization of sections holds.

Lean: `GlobalTheory.SecAlg.existsUnique_sec`.

**Theorem 6.20.18 (Degree zero from the laws).** If the first two bundles of laws hold, then the degree zero condition holds.

Lean: `GlobalTheory.T.exists_section_primitiveBundle_translate_localRing`.

**Theorem 6.20.19 (EGA from the laws).** If the first two bundles of laws hold, then the EGA inputs hold.

Lean: `GlobalTheory.LN.ega_of_laws`.

*Proof.* Combine the theorems on schemes, morphisms, sections and degree zero above. $\square$

**Remark 6.20.20 (Formalization).** The theorems are in [ExistsTorusQuotientNoCocharacter.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsTorusQuotientNoCocharacter.lean#L54) and [EgaBundleFromLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/EgaBundleFromLaws.lean#L20). The algebraization of sections uses no law, so the hypotheses of the second theorem are needed only for three of its four parts. The statement form of the second theorem has the name `GlobalTheory.T.extension_of_abelian_schemes`, which does not describe it. The statement form of the first, `GlobalTheory.T.exists_torusQuotient_no_cocharacter`, is not in this chapter's list. We did not unfold the second-order cube bundle `abelian₂`, the frames `Good` of the algebraization of sections, or the two bundles of laws.

## Notes and references

The second part of this chapter gives [the geometric half of the extension theorem](/entry/zh-geo/), which enters the proof through [the extension theorem under semistable reduction](/entry/zh-geo-of-semistable-reduction/). The third part gives [the neutral group model](/entry/exists-neutral-group-model/), [the semistable reduction statement](/entry/semistable-reduction-st/), [the quotient with no cocharacter](/entry/exists-quot-no-cocharacter/) and [the EGA inputs](/entry/ega-of-laws/). These results enter the proof at [the step on every character](/step/every-character/) and at [EveryCharacter from the literature](/step/every-character-of-literature/).

- S. Bosch, W. Lütkebohmert, M. Raynaud, *Néron Models*, Ergebnisse der Mathematik 21, Springer, 1990, Chapters 3 to 5.
- A. Grothendieck, *Modèles de Néron et monodromie*, Exposé IX in SGA 7 I, Lecture Notes in Mathematics 288, Springer, 1972.
- A. Grothendieck, J. Dieudonné, *Éléments de géométrie algébrique III*, Publ. Math. IHÉS 11, 1961, §5.
- D. Mumford, *Abelian Varieties*, Tata Institute of Fundamental Research Studies in Mathematics 5, Oxford University Press, 1970.
- G. Faltings, C.-L. Chai, *Degeneration of Abelian Varieties*, Ergebnisse der Mathematik 22, Springer, 1990.
- L. Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque 129, 1985.
