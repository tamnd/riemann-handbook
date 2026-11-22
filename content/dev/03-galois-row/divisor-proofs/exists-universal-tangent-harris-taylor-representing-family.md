---
id: exists-universal-tangent-harris-taylor-representing-family
title: The tangent space of a Harris-Taylor moduli scheme at a geometric point has dimension a(n-1)
kind: theorem
decl: GlobalTheory.T.exists_universal_tangent_harrisTaylor_representingFamily
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUniversalTangentHarrisTaylorRepresentingFaStatement
covers: 332
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [the universal tangent of the representing family](/entry/exists-univ-tangent/). It is a second name of that theorem, with the same statement. [The smoothness of the moduli scheme](/entry/smooth-of-relative-dimension/) uses it to fix the relative dimension.

## Statement

Use the representing family $(X, s, u)$ of level $N$ over a noetherian ring $R$ from [the smoothness statement](/entry/smooth-of-relative-dimension-rep-fam-of-is-qproj-over/), and let $d = a(n-1)$. For a field $k$, let $k[\varepsilon] = k \oplus k\varepsilon$ be the dual numbers and $k \oplus k^d$ the trivial square-zero extension of $k$ by $k^d$.

**Theorem.** Let $N \geq 3$, $\gcd(N, p) = 1$, $s$ quasi-projective and smooth. Let $k$ be algebraically closed and $x \colon \operatorname{Spec} k \to X$. Then there is $u_x \colon \operatorname{Spec}(k \oplus k^d) \to X$ that restricts to $x$ and is constant over $\operatorname{Spec} R$, with this property. For each $v \colon \operatorname{Spec} k[\varepsilon] \to X$ that restricts to $x$ and is constant over $\operatorname{Spec} R$, there is a unique $k$-linear $c \colon k^d \to k$ with $v = u_x \circ \operatorname{Spec}(1 \oplus c)$.

So the relative tangent space at $x$ has dimension $d$.

## Proof

The proof is `exact GlobalTheory.UPel.HT.RepTangent.exists_univ_tangent`. The real content is in that theorem, which takes the universal first-order deformation of the object $x^* u$ from [the universal first-order deformation](/entry/exists-universal-first-order-deformation-harris-taylor/) and moves it to $X$ by the universal property.

## In the Lean code

The theorem is in [ExistsUniversalTangentHarrisTaylorRepresentingFaStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUniversalTangentHarrisTaylorRepresentingFaStatement.lean#L8).

The hypotheses `IsQProjOver F.s` and `Smooth F.s` are not used. In [ExistsUniversalTangentHarrisTaylorRepresentingFa.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUniversalTangentHarrisTaylorRepresentingFa.lean#L22) the proof introduces them as `_ _` and never refers to them. The file imports `Mathlib` twice.
