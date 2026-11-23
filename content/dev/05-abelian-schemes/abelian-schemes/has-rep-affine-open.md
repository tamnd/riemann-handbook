---
id: has-rep-affine-open
title: The dual abelian scheme exists over an affine open of the base
kind: theorem
decl: GlobalTheory.DualExist.hasRep_affineOpen
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsDualAbelianSchemePoincare
covers: 697
status: drafted
drafted_by: writer@claude
---
This theorem gives the dual of an abelian scheme $A \to S$ over one affine open $V$ of $S$. [`exists_dual`](/entry/exists-dual/) applies it on a cover of $S$ where the relative dimension of $A$ is constant, and glues. The proof only moves the problem from $V$ to $\operatorname{Spec} \Gamma(S, V)$; the work is in [the affine case](/entry/abelian-scheme-dual-representable-affine-base/).

## Statement

Let $S$ be a scheme and $A \to S$ an abelian scheme: a commutative group scheme that is smooth, proper and geometrically connected. Let $g \ge 0$ and let $S' \to S$ be an $S$-scheme. Say that *$A$ has a dual of dimension $g$ over $S'$* (`HasRep A g S'`) if there are an $S$-morphism $b \colon B \to S'$ and a line bundle $P$ on $A \times_S B$ such that:

1. $P$ is additive, in the sense of [the dual abelian scheme](/entry/dual-abelian-scheme/);
2. for each $S$-scheme $T$, each $S$-morphism $t \colon T \to S'$ and each additive line bundle $N$ on $A \times_S T$, there is exactly one $x \colon T \to B$ with $b \circ x = t$ and $N \cong (1 \times x)^* P$;
3. $b$ is proper, smooth of relative dimension $g$, and geometrically connected.

So $B$ represents the dual functor of $A \times_S S'$ over $S'$. No group structure on $B$ is asked for.

**Theorem.** Let $A \to S$ be an abelian scheme, $V \subseteq S$ an affine open, and $g \ge 0$. If $A \times_S V \to V$ is smooth of relative dimension $g$, then $A$ has a dual of dimension $g$ over $V$.

## Proof

Let $j \colon \operatorname{Spec} \Gamma(S, V) \to S$ be the canonical map, and let $A' = A \times_S \operatorname{Spec} \Gamma(S, V)$.

1. $A'$ is abelian (`PolPull.isAbelianScheme_of_isGrpPullback`), and smooth of relative dimension $g$, as a base change of $A \times_S V \to V$ along $\operatorname{Spec} \Gamma(S, V) \cong V$.
2. [`abelianScheme_dual_representable_affine_base`](/entry/abelian-scheme-dual-representable-affine-base/) gives a dual of $A'$ over $\operatorname{Spec} \Gamma(S, V)$.
3. `T.hasProperSmoothDualRepresentative_grpPullback_iff` says that a dual of $A'$ over an $S'$ is the same as a dual of $A$ over $S'$, seen as an $S$-scheme through $j$. So $A$ has a dual over $\operatorname{Spec} \Gamma(S, V)$.
4. `hasRep_of_iso` moves the dual along the isomorphism $\operatorname{Spec} \Gamma(S, V) \cong V$ over $S$.

## In the Lean code

The theorem is at [ExistsDualAbelianSchemePoincare.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsDualAbelianSchemePoincare.lean#L41). `HasRep`, `Rep` and `Good` are in [SameIdIff.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SameIdIff.lean#L56).

- `hasRep_of_iso` is in the same file, at [line 23](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsDualAbelianSchemePoincare.lean#L23). It composes $b$ with the isomorphism.
- `T.hasProperSmoothDualRepresentative_grpPullback_iff` is a second name of `DualCon.hasRep_baseChange_iff`. We read its statement, not its proof.
- The hypothesis on the relative dimension is stated for $A \times_S V \to V$, not for $A \to S$. This lets `exists_dual` use a different $g$ on each open of its cover.
