---
id: has-rep-affine
title: The dual abelian scheme over an affine base, from a base of finite type over the integers
kind: theorem
decl: GlobalTheory.DualCon.hasRep_affine
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AbelianSchemeDualRepresentableAffineBase
covers: 670
status: drafted
drafted_by: writer@claude
---
This theorem gives the dual of an abelian scheme over $\operatorname{Spec} R$ for any commutative ring $R$. It reduces to a ring of finite type over $\mathbb{Z}$: the abelian scheme descends to such a subring, the dual exists there, and its base change is a dual over $R$. The result goes to [`abelianScheme_dual_representable_affine_base`](/entry/abelian-scheme-dual-representable-affine-base/), which is a second name of this theorem. The finite type case is [`hasProperSmoothDualRepresentative_finiteType`](/entry/has-proper-smooth-dual-representative-finite-type/).

## Statement

**Theorem.** Let $R$ be a commutative ring, $A \to \operatorname{Spec} R$ an abelian scheme, and $g \ge 0$. If $A \to \operatorname{Spec} R$ is smooth of relative dimension $g$, then $A$ has a dual of dimension $g$ over $\operatorname{Spec} R$.

"Has a dual of dimension $g$ over $S'$" is `HasRep A g S'`, defined in [`hasRep_affineOpen`](/entry/has-rep-affine-open/). Here $S' = \operatorname{Spec} R$.

## Proof

1. `AbelianLimit.abelianScheme_descends_to_fg_subring`, with the empty set of extra elements, gives a subring $R_0 \subseteq R$ of finite type over $\mathbb{Z}$, an abelian scheme $B \to \operatorname{Spec} R_0$, smooth of relative dimension $g$, and a map $\varphi \colon A \to B$ that makes $A$ the group pullback of $B$ along $\operatorname{Spec} R \to \operatorname{Spec} R_0$. A group pullback (`IsGrpPullback`) is a cartesian square of schemes in which $\varphi$ respects the group laws.
2. [`hasProperSmoothDualRepresentative_finiteType`](/entry/has-proper-smooth-dual-representative-finite-type/) gives a dual of $B$ over $\operatorname{Spec} R_0$.
3. `T.baseChangeBis` says that a dual over $S'$ gives a dual over each $S''$ with a map $S'' \to S'$. Apply it to $\operatorname{Spec} R \to \operatorname{Spec} R_0$: $B$ has a dual over $\operatorname{Spec} R$, seen as a scheme over $\operatorname{Spec} R_0$.
4. `T.hasProperSmoothDualRepresentative_grpPullback_iff` turns this into a dual of $A$ over $\operatorname{Spec} R$.

Step 1 is a limit argument of the kind in EGA IV, §8 (Grothendieck, Publ. Math. IHÉS 28, 1966). We have not read its Lean proof.

## In the Lean code

The theorem is at [AbelianSchemeDualRepresentableAffineBase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeDualRepresentableAffineBase.lean#L16). The lemmas it calls:

- `GlobalTheory.AbelianLimit.abelianScheme_descends_to_fg_subring`, in [AbelianSchemeDescendsToFinitelyGeneratedSubring.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeDescendsToFinitelyGeneratedSubring.lean#L144). Another theorem with the same last name, `GlobalTheory.CompanionTheory.Ar.Approx.abelianScheme_descends_to_fg_subring`, is in `Development/AutomorphicSpectrum/Proofs/GeometryProofs/AbelianSchemeSpreadsOutFiniteTypeSubring.lean`; it does not give the relative dimension, and this proof does not use it.
- `GlobalTheory.T.hasProperSmoothDualRepresentative_finiteType`.
- `GlobalTheory.T.baseChangeBis`, a second name of `DualCon.HasRep.baseChange`, and `GlobalTheory.T.hasProperSmoothDualRepresentative_grpPullback_iff`, a second name of `DualCon.hasRep_baseChange_iff`. We read their statements, not their proofs.

The proof discards one output of the descent lemma: the inclusion of the extra elements in $R_0$, which is empty here.
