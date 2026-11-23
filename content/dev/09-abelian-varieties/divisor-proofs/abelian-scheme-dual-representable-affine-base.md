---
id: abelian-scheme-dual-representable-affine-base
title: The dual abelian scheme exists over an affine base (second name)
kind: theorem
decl: GlobalTheory.T.abelianScheme_dual_representable_affine_base
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AbelianSchemeDualRepresentableAffineBaseStatement
covers: 671
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`DualCon.hasRep_affine`](/entry/has-rep-affine/), with the same statement. Its only user is [`hasRep_affineOpen`](/entry/has-rep-affine-open/), which moves the result from $\operatorname{Spec} \Gamma(S, V)$ to an affine open $V$ of a scheme $S$. The mathematics is in [`hasRep_affine`](/entry/has-rep-affine/).

## Statement

**Theorem.** Let $R$ be a commutative ring, $A \to \operatorname{Spec} R$ an abelian scheme, and $g \ge 0$. If $A \to \operatorname{Spec} R$ is smooth of relative dimension $g$, then $A$ has a dual of dimension $g$ over $\operatorname{Spec} R$.

"Has a dual of dimension $g$" is `HasRep A g`, defined in [the entry above](/entry/has-rep-affine-open/): there is a scheme $B$, proper, smooth of relative dimension $g$ and geometrically connected over $\operatorname{Spec} R$, with an additive line bundle $P$ on $A \times B$ that represents the additive line bundles on $A \times T$ for all $T$ over $\operatorname{Spec} R$.

## Proof

The proof is the single tactic

```
first | exact @GlobalTheory.DualCon.hasRep_affine | ...
```

so the theorem is `hasRep_affine` under another name.

## In the Lean code

The theorem is at [AbelianSchemeDualRepresentableAffineBaseStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeDualRepresentableAffineBaseStatement.lean#L10). It has the option `maxHeartbeats 1000000`, which a one-line proof does not need. The name says "representable", but the conclusion also asks that the representing scheme be proper, smooth of relative dimension $g$ and geometrically connected.
