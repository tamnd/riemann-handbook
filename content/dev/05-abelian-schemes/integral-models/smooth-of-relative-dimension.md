---
id: smooth-of-relative-dimension
title: The smoothness of a Harris-Taylor moduli scheme, by lifting and tangent spaces
kind: theorem
decl: GlobalTheory.UPel.HT.RepFam.smoothOfRelativeDimension
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SmoothOfRelativeDimension
covers: 460
status: drafted
drafted_by: writer@claude
---
This theorem proves that a quasi-projective scheme that represents the Harris-Taylor moduli problem is smooth of relative dimension $a(n-1)$ over the base. It does so in two steps: smoothness by lifting points along square-zero thickenings of Artinian local rings, and the dimension by the tangent space at geometric points. Its statement form is [the smoothness of the moduli scheme](/entry/smooth-of-relative-dimension-rep-fam-of-is-qproj-over/), which goes into [the integral model entry](/entry/model-nonempty/).

## Statement

The statement is that of [its statement form](/entry/smooth-of-relative-dimension-rep-fam-of-is-qproj-over/): let $R$ be noetherian, $b$ a base over $R$, $N \geq 3$ with $\gcd(N, p) = 1$, and $(X, s, u)$ a representing family of level $N$ with $s$ quasi-projective. Then $s$ is smooth of relative dimension $a(n-1)$.

## Proof

1. **Finite type.** By hypothesis $s$ is a quasi-compact immersion $X \to \mathbb{P}^m_R$ followed by the projection. The projection is proper (`isProper_str`), so $s$ is locally of finite type.
2. **Smoothness.** `GlobalTheory.T.smooth_of_artinian_squareZero_lifting_noetherian_base` says: over a noetherian ring, a map locally of finite type is smooth if it has the lifting property for each surjection $\pi \colon C \to C_0$ with $C$ local Artinian and $(\ker \pi)^2 = 0$. Let $x_0 \colon \operatorname{Spec} C_0 \to X$ and $\beta \colon R \to C$ be compatible.
   - `GlobalTheory.T.exists_harrisTaylorObjectPullback` gives the pullback $o_0$ of $u$ along $x_0$, an object over $\operatorname{Spec} C_0$.
   - `GlobalTheory.T.harrisTaylor_formally_smooth_squareZero_lift` lifts $o_0$ to an object $o'$ over $\operatorname{Spec} C$, with $o_0$ the pullback of $o'$. This is the deformation input, and it uses $N \geq 3$ and $\gcd(N, p) = 1$.
   - The universal property gives $x \colon \operatorname{Spec} C \to X$ over $\operatorname{Spec} R$ with $o'$ the pullback of $u$ along $x$.
   - `GlobalTheory.T.harrisTaylorObjectPullback_comp` makes $o_0$ the pullback of $u$ along $x \circ \operatorname{Spec}\pi$. The uniqueness in the universal property for $o_0$ gives $x \circ \operatorname{Spec}\pi = x_0$.
3. **Dimension.** `GlobalTheory.T.smoothOfRelativeDimension_of_universal_firstOrder_tangent` says that a smooth $s$ is smooth of relative dimension $d$ if, at each point $x \colon \operatorname{Spec} k \to X$ with $k$ algebraically closed, the first-order deformations of $x$ over the base are classified by $\operatorname{Hom}_k(k^d, k)$ through a universal one over $k \oplus k^d$. [The universal tangent of the representing family](/entry/exists-universal-tangent-harris-taylor-representing-family/) gives this with $d = a(n-1)$.

## In the Lean code

The theorem is in [SmoothOfRelativeDimension.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SmoothOfRelativeDimension.lean#L15). The lemmas it calls, each a second name of a lemma whose proof we have not opened:

- `smooth_of_artinian_squareZero_lifting_noetherian_base`, for `GlobalTheory.SmoothCrit.smooth_of_artinian_lift`.
- `exists_harrisTaylorObjectPullback`, for `GlobalTheory.UPel.HT.BaseChange.exists_objMap`.
- `harrisTaylor_formally_smooth_squareZero_lift`, for `GlobalTheory.UPel.HT.obj_lift_sqZero`. Its statement asks for $\ker\pi \cdot \ker\pi = 0$ and does not ask $R$ to be noetherian.
- `harrisTaylorObjectPullback_comp`, for `GlobalTheory.UPel.HT.objMap_comp`.
- `smoothOfRelativeDimension_of_universal_firstOrder_tangent`, for `GlobalTheory.SmoothDimTangent.smoothOfRelativeDimension_of_universal_tangent`.
- `GlobalTheory.T.exists_universal_tangent_harrisTaylor_representingFamily`.

Quasi-projectivity is used only to get "locally of finite type". The noetherian hypothesis on $R$ is used only by the lifting criterion.
