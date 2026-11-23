---
id: one-map-conj5
title: The phase and the class sum identity at a conjugate embedding
kind: theorem
decl: GlobalTheory.ConjRatLiftFive.oneMapConj5
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ConjugatesOfRationalThetaLiftFromCharacterisatio
covers: 406
status: drafted
drafted_by: writer@claude
---
This theorem is a special case of [`oneMap_of_ext_ofFive`](/entry/one-map-of-ext-of-five/), and that entry has the real content. It supplies step 2 of [the conjugate datum computation](/entry/conj-lift5/). Below this theorem are 406 declarations, and 382 of them are below `oneMap_of_ext_ofFive`.

## Statement

**Theorem.** Take the hypotheses of [the conjugate datum computation](/entry/conj-lift5/), in its notation, at the index $i$ and the embedding $\sigma$ over $K$, with representatives $h$ of the classes ($\mathrm{RepsAt}$). Then there are $u$, a central $z \in G$ and $\kappa$ with $|\kappa| = 1$ such that:

1. $u$ is a phase: $|u| = 1$, left invariant under $G_W(F)$, and right invariant under $G_W(\mathbb{R})$ and under the level of $W$;
2. $u(h)\,\phi(g f)(h) = \sigma(\chi(g))\,u(hk)\,\phi(f)(hk)$ whenever $k$ is a level lift of $g \in G$ ($\mathrm{EquivBy}$);
3. for each class sum $(x_0, a, f)$, each $v$ that lifts $v_0$, and each $g$,
$$\kappa \, th_P(j x_0)(\otimes v)(g) = \sum_k \sigma(a_k)\, u(g)\, \phi(z f_k)(g).$$

## Proof

Extend $\sigma$ to the coefficient field of the oscillator model (`exists_ext`). The theta vector condition at the monomial $1$ shows that $f$ is a theta function. Then apply `oneMap_of_ext_ofFive` with the facts from `factsAt_ofFive`.

## In the Lean code

The theorem is in [ConjugatesOfRationalThetaLiftFromCharacterisatio.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ConjugatesOfRationalThetaLiftFromCharacterisatio.lean#L28). `PhaseFun` and `EquivBy` are in [ReadingsExistRow.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ReadingsExistRow.lean#L73). `oneMap_of_ext_ofFive` is in [CoefMapNormEquivariantBasisOfFive.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CoefMapNormEquivariantBasisOfFive.lean#L2760).

The hypothesis $\mathrm{Comparison}_2$ is introduced as `_` at [line 29](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ConjugatesOfRationalThetaLiftFromCharacterisatio.lean#L29) and is never used.
