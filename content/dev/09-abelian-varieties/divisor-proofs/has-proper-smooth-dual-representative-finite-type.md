---
id: has-proper-smooth-dual-representative-finite-type
title: The dual abelian scheme over a ring of finite type over the integers (second name)
kind: theorem
decl: GlobalTheory.T.hasProperSmoothDualRepresentative_finiteType
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasProperSmoothDualRepresentativeFiniteTypeStatement
covers: 666
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`DualConFT.hasRep_of_finiteType`](/entry/has-rep-of-finite-type/), with the same statement. Its only user is [`DualCon.hasRep_affine`](/entry/has-rep-affine/).

## Statement

**Theorem.** Let $R$ be a commutative ring of finite type over $\mathbb{Z}$, let $A \to \operatorname{Spec} R$ be an abelian scheme, and let $g \ge 0$. If $A \to \operatorname{Spec} R$ is smooth of relative dimension $g$, then $A$ has a dual of dimension $g$ over $\operatorname{Spec} R$.

"Has a dual of dimension $g$" is `HasRep A g`, defined in [`hasRep_affineOpen`](/entry/has-rep-affine-open/). In words: there is a scheme $B$ over $\operatorname{Spec} R$, proper, smooth of relative dimension $g$ and geometrically connected, with an additive line bundle $P$ on $A \times B$ that represents the additive line bundles on $A \times T$ for each $T$ over $\operatorname{Spec} R$.

## Proof

The proof is the single tactic

```
first | exact @GlobalTheory.DualConFT.hasRep_of_finiteType | ...
```

so the theorem is `hasRep_of_finiteType` under another name.

## In the Lean code

The theorem is at [HasProperSmoothDualRepresentativeFiniteTypeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasProperSmoothDualRepresentativeFiniteTypeStatement.lean#L10). It has the option `maxHeartbeats 1000000`, which a one-line proof does not need. The hypothesis "of finite type over $\mathbb{Z}$" is the instance `Algebra.FiniteType ℤ R`.
