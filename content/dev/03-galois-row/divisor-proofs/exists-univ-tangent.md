---
id: exists-univ-tangent
title: The tangent space of a Harris-Taylor representing family
kind: theorem
decl: GlobalTheory.UPel.HT.RepTangent.exists_univ_tangent
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUniversalTangentHarrisTaylorRepresentingFa
covers: 331
status: drafted
drafted_by: writer@claude
---
This theorem computes the relative tangent space of a representing family of the Harris-Taylor moduli problem at each geometric point: it has dimension $a(n-1)$. It moves [the universal first-order deformation](/entry/exists-universal-first-order-deformation-harris-taylor/) of one object to the scheme that represents the moduli problem. Its statement form is [exists_universal_tangent_harrisTaylor_representingFamily](/entry/exists-universal-tangent-harris-taylor-representing-family/), and its user is [the smoothness of a representing family](/entry/smooth-of-relative-dimension/), which gets relative dimension $a(n-1)$ from it.

## Statement

Use the datum $D$, the base $b$ over $R$ and the objects of level $N$ of [the integral model entry](/entry/model-nonempty/). A *representing family* $F$ is a scheme $X$ with $s \colon X \to \operatorname{Spec} R$ and an object $u_F$ over $X$ such that each object over a scheme $S$ is the pullback of $u_F$ along a unique map $S \to X$. Let $d = a(n-1)$, $V = k^d$, and let $k[V] = k \oplus V$ and $k[\varepsilon] = k \oplus k$ be the square-zero extensions.

**Theorem.** Let $R$ be noetherian, $N \geq 3$ with $\gcd(N, p) = 1$, and $F$ a representing family with $X$ quasi-projective and smooth over $R$. Let $k$ be an algebraically closed field and $x \colon \operatorname{Spec} k \to X$. Then there is $u \colon \operatorname{Spec} k[V] \to X$ such that:

1. $u$ restricts to $x$ on $\operatorname{Spec} k$, and $s \circ u$ is $s \circ x$ composed with the projection $\operatorname{Spec} k[V] \to \operatorname{Spec} k$;
2. for each $v \colon \operatorname{Spec} k[\varepsilon] \to X$ that restricts to $x$ and has $s \circ v$ constant in the same sense, there is a unique $k$-linear $c \colon V \to k$ with $v = u \circ \operatorname{Spec}(\mathrm{id} \oplus c)$.

So the tangent vectors at $x$ relative to $R$ are the elements of $V^\vee$, a space of dimension $d$.

## Proof

1. Pull $u_F$ back along $x$ to an object $o_0$ over $k$ (`exists_harrisTaylorObject_pullback_along`).
2. [The universal first-order deformation](/entry/exists-universal-first-order-deformation-harris-taylor/) gives $o$ over $k[V]$ that restricts to $o_0$, with its universal property for deformations over $k[\varepsilon]$.
3. Let $u$ be the map that classifies $o$. Both $x$ and $u|_{\operatorname{Spec} k}$ classify $o_0$, so they are equal by uniqueness.
4. Let $v$ be as in clause 2. Pull $u_F$ back along $v$ to $o'$. By `objMap_comp_cancel`, $o'$ is a deformation of $o_0$. Step 2 gives a unique $c$ with $o' \to o$ over $\operatorname{Spec}(\mathrm{id} \oplus c)$. Then $v$ and $u \circ \operatorname{Spec}(\mathrm{id} \oplus c)$ both classify $o'$, so they are equal.
5. If $v = u \circ \operatorname{Spec}(\mathrm{id} \oplus c')$, then `objMap_comp_cancel` gives $o' \to o$ over $\operatorname{Spec}(\mathrm{id} \oplus c')$, so $c' = c$ by step 2.

The rest is bookkeeping with the identities `spMap_comp_spMap` and `spMap_id'` of the same file.

## In the Lean code

The theorem is in [ExistsUniversalTangentHarrisTaylorRepresentingFa.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUniversalTangentHarrisTaylorRepresentingFa.lean#L21). `RepFam` is in [ToRepFam.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ToRepFam.lean#L12). The lemmas it calls:

- `GlobalTheory.T.exists_harrisTaylorObject_pullback_along`, an alias of `Pull.exists_objMap`;
- `GlobalTheory.T.exists_universal_firstOrder_deformation_harrisTaylor`;
- `GlobalTheory.UPel.HT.objMap_comp_cancel`: maps of objects compose, and a map over $g \circ f$ with a map over $g$ gives a map over $f$.

The hypotheses that $X$ is quasi-projective and smooth are introduced as `_` and never used. The noetherian hypothesis on $R$ is not used either. The theorem holds for any representing family. The smoothness hypothesis matters for the user: [the smoothness entry](/entry/smooth-of-relative-dimension/) proves `Smooth F.s` first and then passes it here.
