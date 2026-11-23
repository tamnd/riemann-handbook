---
title: Formal algebraization
decls:
  - GlobalTheory.formalAlgebraisation
  - GlobalTheory.T.algebraisation_properFormalScheme_ampleBundle
  - GlobalTheory.FormalAlg.formalAlgebraisation_schemes
  - GlobalTheory.T.exists_veryAmple_compatible_sections_thickeningTower
  - GlobalTheory.FormalAlg.TowerVA.exists_veryAmple_compatible
  - GlobalTheory.T.exists_uniform_lift_sections_thickeningTower
  - GlobalTheory.FormalAlg.exists_lift_sections_tower
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Formal algebraization

This section proves Grothendieck's algebraization theorem for proper formal schemes with an ample line bundle, in the form used in this chapter. Over a complete noetherian ring, a compatible system of proper schemes over the quotients $R/I^{e+1}$, with a compatible system of line bundles that is ample on the first member, comes from one proper scheme over $R$ with a relatively ample line bundle. The proof embeds the whole system in one projective space by compatible sections. The theorem is used in the next section, to lift a root of a Mumford bundle from the closed fibre of an abelian scheme over a complete local ring. Volume 3 has a parallel treatment in [Theorem 7.6.3 of Volume 3](/entry/t-formal-algebraisation-schemes/).

Throughout, $R$ is a noetherian ring, $I \subseteq R$ is an ideal and $R_e = R/I^{e+1}$. We use [completion](/learn/commutative-algebra/#completion), [coherent cohomology](/learn/commutative-algebra/#coherent-cohomology) and [formal functions](/learn/commutative-algebra/#formal-functions-and-grothendiecks-existence-theorem).

**Definition 9.2.1 (Tower of thickenings).** A *tower of thickenings* over $(R, I)$ is a sequence of schemes $Y_e$ over $\operatorname{Spec} R_e$, for $e \ge 0$, with maps $\beta_e : Y_e \to Y_{e+1}$ over $\operatorname{Spec} R_{e+1}$ such that the square formed by $\beta_e$ and the structure maps is cartesian:
$$Y_e \cong Y_{e+1} \times_{\operatorname{Spec} R_{e+1}} \operatorname{Spec} R_e.$$

A *line bundle on the tower* is a family of line bundles $N_e$ on $Y_e$ with isomorphisms $v_e : N_e \cong \beta_e^* N_{e+1}$. A family of sections $\sigma_e \in \Gamma(Y_e, N_e)$ is *compatible* if $v_e(\sigma_e) = \beta_e^* \sigma_{e+1}$ for each $e$.

Let $X$ be a scheme over $R$. For each $e$ let $X_e = X \times_R R_e$. A tower of the form $(X_e)$, with the closed immersions $X_e \to X_{e+1}$, is the formal completion of $X$ along $X_0$.

**Definition 9.2.2 (Very ample family).** Let $R'$ be a ring, let $f : Y \to \operatorname{Spec} R'$ and let $H$ be a line bundle on $Y$. Sections $s_0, \dots, s_m$ of $H$ are a *very ample family* if the open sets $Y_{s_i} = \{s_i \ne 0\}$ cover $Y$, each $Y_{s_i}$ is affine, and for each $i$ the ring map $R'[x_0, \dots, x_m] \to \Gamma(Y_{s_i}, \mathcal{O})$ that sends $x_j$ to $s_j / s_i$ is surjective.

Lean: `GlobalTheory.AbLaw.VeryAmpleBy`.

So a very ample family defines a closed immersion $Y \to \mathbb{P}^m_{R'}$ with $H$ the pullback of $\mathcal{O}(1)$.

**Lemma 9.2.3 (Uniform lifting of sections).** Let $(Y_e, \beta_e)$ be a tower of thickenings over $(R, I)$. Let $H_0$ be a line bundle on $Y_0$ with a very ample family $s_0, \dots, s_m$. Then there is $k_0$ with the following property. Let $k \ge k_0$, let $(L_e, u_e)$ be a line bundle on the tower with $L_0 \cong H_0^{k}$, and let $\sigma_0 \in \Gamma(Y_0, L_0)$. Then there is a compatible family $\sigma_e \in \Gamma(Y_e, L_e)$ that starts with $\sigma_0$.

Lean: `GlobalTheory.FormalAlg.exists_lift_sections_tower` (also `GlobalTheory.T.exists_uniform_lift_sections_thickeningTower`, a wrapper).

*Proof.* The very ample family gives standard affine charts $Y_{s_i}$ on $Y_0$, and hence on each $Y_e$, since $Y_e$ and $Y_0$ have the same underlying space. On these charts, a uniform bound for the first Čech cohomology of the tower gives $k_0$: for each $k \ge k_0$ and each $e$, the obstruction to lifting a section of a bundle isomorphic to $H_0^k$ on $Y_0$ from level $e$ to level $e+1$ vanishes. The obstruction lies in the first cohomology of $I^{e+1}\mathcal{O}_{Y_{e+1}} \otimes L_{e+1}$, a coherent sheaf on $Y_0$ twisted by $H_0^k$ ([coherent cohomology](/learn/commutative-algebra/#coherent-cohomology)). Let $\gamma_e : Y_0 \to Y_e$ be the composite of $\beta_0, \dots, \beta_{e-1}$. By induction on $e$, using $u_e$, we get $\gamma_e^* L_e \cong H_0^k$ for each $e$. So the lifting step applies at each level. We choose a lift $\sigma_{e+1}$ of $\sigma_e$ for each $e$, by recursion on $e$. $\square$

**Lemma 9.2.4 (Compatible very ample sections).** Let $(Y_e, \beta_e)$ be a tower of thickenings over $(R, I)$, and let $(N_e)$ be line bundles on $Y_e$ with $N_0$ relatively ample over $R_0$. Then there is $a \ge 1$ with the following property. Let $c \in \{a, a+1\}$ and let $v_e : N_e^c \cong \beta_e^* N_{e+1}^c$ be isomorphisms. Then there are $m$ and compatible families $s_{e,0}, \dots, s_{e,m}$ of sections of $N_e^c$ such that, for each $e$, the family $(s_{e,j})_j$ is very ample on $Y_e$.

Lean: `GlobalTheory.FormalAlg.TowerVA.exists_veryAmple_compatible` (also `GlobalTheory.T.exists_veryAmple_compatible_sections_thickeningTower`, a wrapper).

*Proof.* Since $N_0$ is relatively ample, there is $d \ge 1$ such that $N_0^d$ and $N_0^{d+1}$ are both very ample, with very ample families. Apply the lemma on uniform lifting to $H_0 = N_0^{d}$ and to $H_0 = N_0^{d+1}$. This gives bounds $k_1$ and $k_2$. Let $K = \max(k_1, k_2)$ and set
$$a = d\bigl(1 + (d+1)K\bigr), \qquad a + 1 = (d+1)(1 + dK).$$
The second identity holds because $(d+1)(1+dK) - d(1 + (d+1)K) = 1$. So $N_0^a$ is the power $(N_0^d)^{k}$ with $k = 1 + (d+1)K \ge k_1$, and $N_0^{a+1}$ is the power $(N_0^{d+1})^{k'}$ with $k' = 1 + dK \ge k_2$.

Let $c = a$; the case $c = a+1$ is the same. A power of a very ample family is a very ample family, so the products of $k$ sections of the very ample family of $N_0^d$ are a very ample family $s_{0,0}, \dots, s_{0,m}$ of $N_0^a$. By the lemma on uniform lifting, each $s_{0,j}$ extends to a compatible family $(s_{e,j})_e$. It remains to see that $(s_{e,j})_j$ is very ample on $Y_e$ for $e \ge 1$. The map $Y_0 \to Y_e$ is a closed immersion defined by a nilpotent ideal, since $I^{e+1}$ is nilpotent in $R_e$. The sections $s_{e,j}$ restrict to the very ample family on $Y_0$. A family of sections whose restriction along a closed immersion with nilpotent ideal is very ample is very ample: the open sets $Y_{e, s_{e,i}}$ have the same underlying sets as on $Y_0$, they are affine because their reductions are affine, and the ring maps are surjective by Nakayama's lemma for the nilpotent ideal. $\square$

**Theorem 9.2.5 (Algebraization of formal schemes).** Let $R$ be noetherian and $I$-adically complete. Let $(Y_e, \beta_e)$ be a tower of thickenings over $(R, I)$ with each $Y_e$ proper over $R_e$. Let $N_e$ be line bundles on $Y_e$ with $N_e \cong \beta_e^* N_{e+1}$ for each $e$, and with $N_0$ relatively ample over $R_0$. Then there are a scheme $X$ proper over $R$, a relatively ample line bundle $M$ on $X$, and maps $b_e : Y_e \to X$ such that:

1. each square formed by $b_e$, $Y_e \to \operatorname{Spec} R_e$, $X \to \operatorname{Spec} R$ and $\operatorname{Spec} R_e \to \operatorname{Spec} R$ is cartesian;
2. $b_{e+1} \circ \beta_e = b_e$ for each $e$;
3. $N_e \cong b_e^* M$ for each $e$.

Lean: `GlobalTheory.FormalAlg.formalAlgebraisation_schemes` (also `GlobalTheory.T.algebraisation_properFormalScheme_ampleBundle`, a wrapper).

This is EGA III$_1$, Théorème 5.4.5 (A. Grothendieck, *Éléments de géométrie algébrique III*, Publ. Math. IHÉS 11, 1961), in the special case of a formal scheme given by a tower over an adic noetherian ring.

*Proof.* Fix isomorphisms $v_e : N_e \cong \beta_e^* N_{e+1}$. They induce isomorphisms of all powers $N_e^c \cong \beta_e^* N_{e+1}^c$, whose local transition units are the $c$-th powers of those of $v_e$. Take $a$ from the lemma on compatible very ample sections. It gives compatible very ample families $s$ of $N_e^a$ and $s'$ of $N_e^{a+1}$.

The family $s$ embeds each $Y_e$ in $\mathbb{P}^m_{R_e}$, compatibly in $e$. By the existence theorem for closed subschemes of projective space over the complete ring $R$, these embeddings come from a closed subscheme $X \subseteq \mathbb{P}^m_R$. This gives $X$, a line bundle $H'$ on $X$ (the restriction of $\mathcal{O}(1)$) with a very ample family, maps $b_e$ with the cartesian squares in 1 and the identities in 2, and isomorphisms $b_e^* H' \cong N_e^a$ that match the sections. Since $X$ is projective over $R$, it is proper.

In the same way, the compatible sections $s'$ of $N_e^{a+1}$, which generate each $N_e^{a+1}$, give a line bundle $M_2$ on $X$ with $b_e^* M_2 \cong N_e^{a+1}$, again matching the sections. The local transition units of these isomorphisms are compatible with the powers of $v_e$. So the two systems of isomorphisms are compatible, and we can cancel powers: set $M = M_2 \otimes H'^{-1}$. Then $H' \cong M^a$ and, for each $e$,
$$b_e^* M = b_e^* M_2 \otimes b_e^* H'^{-1} \cong N_e^{a+1} \otimes N_e^{-a} = N_e.$$
Finally $M^a \cong H'$ has a very ample family, so $M$ is relatively ample. $\square$

**Theorem 9.2.6 (Formal algebraization).** Let $R$ be noetherian and $I$-adically complete.

1. (Morphisms.) Let $X$ be proper over $R$ and let $Z$ be separated, quasi-compact and locally of finite type over $R$. Let $(Y_e, \beta_e)$ be a tower over $(R, I)$ with maps $b_e : Y_e \to X$ such that each $Y_e = X \times_R R_e$ via $b_e$, and $b_{e+1} \circ \beta_e = b_e$. Let $f_e : Y_e \to Z$ be maps over $R$ with $f_{e+1} \circ \beta_e = f_e$. Then there is a unique map $g : X \to Z$ over $R$ with $g \circ b_e = f_e$ for each $e$.
2. (Schemes.) The conclusion of the theorem on algebraization of formal schemes holds.

Lean: `GlobalTheory.formalAlgebraisation`.

This is EGA III$_1$, Théorème 5.4.1 for part 1 and Théorème 5.4.5 for part 2.

*Proof.* Part 1 is [Theorem 1.20.2](/entry/formal-algebraisation-morphisms/). Part 2 is the theorem on algebraization of formal schemes. $\square$

**Remark 9.2.7 (Formalization).** The two lemmas on towers do not assume that $R$ is $I$-adically complete; only the algebraization theorems do ([ExistsVeryAmpleCompatibleSectionsThickeningTower.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsVeryAmpleCompatibleSectionsThickeningTower.lean#L52), [ExistsUniformLiftSectionsThickeningTower.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUniformLiftSectionsThickeningTower.lean#L15)). Line bundles are given by Čech cocycles, and the compatibility of sections is a relation `Rel` that we have not unfolded; nor have we unfolded `RelAmple`. The steps "a uniform bound for the first Čech cohomology", "existence of closed subschemes of projective space", "algebraization of a generated system" and "cancel powers" are lemmas that we cite by their statements; the sketch of the obstruction in the uniform lifting proof explains the bound and is not a description of that lemma. In the lemma on compatible very ample sections, the very ampleness at level $e \ge 1$ comes from a lemma on closed immersions with nilpotent ideal and a lemma named `tower`; the explanation given above is ours.
