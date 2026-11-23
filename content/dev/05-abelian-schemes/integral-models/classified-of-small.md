---
id: classified-of-small
title: A classifying map lifts over a small extension
kind: theorem
decl: GlobalTheory.SmallClassify.classified_of_small
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ClassifiedOfSmall
covers: 319
status: drafted
drafted_by: writer@claude
---
This theorem is the step of the induction in [the classification over local Artinian rings](/entry/siegel-artin-main/). If the family classifies principal objects over $C/(e)$, it classifies those over $C$: lift the point by smoothness, then correct it by a tangent vector. [Its statement form](/entry/exists-sieg-pb-lift-of-quotient-lift/) repeats it.

## Statement

Use $B_n = \mathbb{Z}[\zeta_n, 1/n]$ and the family $(X, s, u)$ of [the classification over local Artinian rings](/entry/siegel-artin-main/).

**Theorem.** Let $g \geq 1$, $n \geq 3$ odd, and $(X, s, u)$ a family of genus $g$ and level $n$. Let $C$ be local Artinian with maximal ideal $\mathfrak{m}$ and residue field $k$, and $e \in \mathfrak{m}$ with $\mathfrak{m} e = 0$. Write $\pi \colon C \to C/(e)$. Let $\beta \colon B_n \to C$ be a ring map and $c$ principal over $\operatorname{Spec} C$. Suppose that each pullback $c_0$ of $c$ to $\operatorname{Spec} C/(e)$ is the pullback of $u$ along a map over $\pi \circ \beta$. Then $c$ is the pullback of $u$ along some $f \colon \operatorname{Spec} C \to X$ with $s \circ f = \operatorname{Spec}\beta$.

## Proof

Let $c_0$ be a pullback of $c$ to $C/(e)$, classified by $x_0 \colon \operatorname{Spec} C/(e) \to X$. If $e = 0$, $x_0$ gives $f$. Let $e \neq 0$; then $e^2 = 0$ and $(e) \cong k$.

1. **Lift by smoothness.** `lift_lemma` applies `GlobalTheory.exists_local_lift_of_smooth` to the square-zero thickening by $C \to C/(e)$. The open set of the lift contains the closed point, so it is all of $\operatorname{Spec} C$. This gives $x_1$ over $\beta$ that restricts to $x_0$; $x_1^* u$ and $c$ agree over $C/(e)$ only.
2. **The pinch ring.** `ring_lemma` builds $P = \{(a, y) \in C \times k[\varepsilon] : \bar a = y_0\}$, with projections $p \colon P \to C$ and $q \colon P \to k[\varepsilon]$. Let $\varphi \colon k \to C$ be $\bar a \mapsto ae$, and $\sigma(a, y) = a + \varphi(y_1)$. Then $P$ is local and Artinian, $P = C \times_k k[\varepsilon]$ through $(p, q)$, and $P = C \times_{C/(e)} C$ through $(p, \sigma)$. This is an isomorphism of Schlessinger (Functors of Artin rings, Trans. Amer. Math. Soc. 130 (1968), 208 to 222).
3. **Glue.** `exists_principalSiegelObject_glue_artinFibreProduct` glues $x_1^* u$ (along $p$) and $c$ (along $\sigma$) to a principal object $e'$ over $P$.
4. **The tangent vector.** `siegelObject_dualNumber_classified` classifies $q^* e'$ by $v \colon \operatorname{Spec} k[\varepsilon] \to X$.
5. **Glue the maps.** Over $k$, the maps $x_1$ and $v$ classify the same object, so they agree there by the uniqueness field `inj`. `spec_fibreProduct_localArtinian_glue_existsUnique` (Spec of this fibre product is a pushout) gives $w \colon \operatorname{Spec} P \to X$ over $B_n$ that restricts to $x_1$ and $v$.
6. **Compare.** $w^* u$ and $e'$ agree along $p$ and $q$. `principalSiegelObject_determined_over_artinianPinch` gives $w^* u \cong e'$.
7. $f = w \circ \operatorname{Spec}\sigma$ classifies $\sigma^* e' \cong c$.

The rest is bookkeeping with pullbacks.

## In the Lean code

The theorem is in [ClassifiedOfSmall.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClassifiedOfSmall.lean#L211). `lift_lemma`, `isPullback_of_bij`, `ring_lemma` and `pull_ex` are in the same file, proved in full. `GlobalTheory.exists_local_lift_of_smooth` is in [BijectiveRestrictPointsOfEtaleOfHenselian.lean](lean:Development/AbelianVarietyTheory/Proofs/HomogeneousIdeals/BijectiveRestrictPointsOfEtaleOfHenselian.lean#L139). The four lemmas of steps 3 to 6 are statement forms in `GlobalTheory.T`; we have not opened their proofs.

Of the family, the proof uses `smooth` (not the relative dimension), `inj`, `univ` and `princ`. The hypothesis $g \geq 1$ goes only to `siegelObject_dualNumber_classified`.
