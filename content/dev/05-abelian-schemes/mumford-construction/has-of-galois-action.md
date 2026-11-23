---
id: has-of-galois-action
title: A Galois action on a uniformised semi-abelian scheme gives a uniformisation over the base
kind: theorem
decl: GlobalTheory.Mum.has_of_galois_action
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.UniformisedSemiAbelianGaloisDescent
covers: 377
status: drafted
drafted_by: writer@claude
---
This theorem descends a uniformised semi-abelian scheme from a finite Galois extension $R'$ of $R$ to $R$. It first descends an open part of the group near the closed fibre, then the whole group, and then checks that the Galois action is trivial on the descended group. It is restated as [`uniformised_semiAbelian_galois_descent`](/entry/uniformised-semi-abelian-galois-descent/), the last step of [`has_of_hasFin`](/entry/has-of-has-fin/).

## Statement

The hypotheses are those of the [statement entry](/entry/uniformised-semi-abelian-galois-descent/): $R$ with `Base R`, a finite Galois map $\rho \colon R \to R'$ with group $\Gamma$, data $D$ over $R$ with a pullback $D'$ over $R'$, and a semi-abelian $G'$ over $R'$ with a uniformisation $U'$ by $D'$. The action `GalAct ρ hD U'` consists of:

- for each $\gamma \in \Gamma$, a map $a_\gamma \colon G' \to G'$ over $\operatorname{Spec}(\gamma)$ that makes $G'$, as a group, the pullback of itself along $\operatorname{Spec}(\gamma)$;
- $a_1 = \mathrm{id}$ and $a_{\gamma\delta} = a_\delta \circ a_\gamma$;
- for each $\gamma$, an identification of $D'$ with its pullback along $\gamma$ that fixes the lattice and is compatible with $D$ (`PullOver`), under which $a_\gamma$ carries $U'$ to $U'$ (`IsPullUnif`).

**Theorem.** Under these hypotheses, `Has D`.

## Proof

Write $\pi = \operatorname{Spec}(\rho) \colon \operatorname{Spec} R' \to \operatorname{Spec} R$.

1. `exists_near_galois_quotient`: there is a datum `N : Near π G'` with `N.Law`. It is a smooth, separated, quasi-compact scheme $V$ over $R$ with an open immersion $u \colon V \times_R R' \to G'$ over $R'$, whose image contains every point of $G'$ above the closed point of $\operatorname{Spec} R$. `N.Law` says that the group law of $G'$ restricts to a group law on $V$ near the closed fibre. The action $a_\gamma$ corresponds on $V \times_R R'$ to the action of $\gamma$ on the second factor.
2. $\pi$ is finite, so proper. It is surjective, since $\rho$ is injective and integral.
3. `descend_of_near`: there is a semi-abelian $G$ over $R$ with a map $\beta \colon G' \to G$ that makes $G'$ the group pullback of $G$ along $\pi$, and an open immersion $V \to G$ compatible with $u$ and $\beta$.
4. `comp_eq_of_near`: for each $\gamma$, $\beta \circ a_\gamma = \beta$. The two maps agree on the image of $u$, by step 1 and the compatibility of $u$ with $\beta$. That image is dense, because $G'$ is smooth with geometrically connected fibres, hence irreducible, and the image contains the identity point of the closed fibre. $G'$ is reduced and $G$ is separated, so the two maps are equal.
5. `has_of_galAct`: a semi-abelian $G$ over $R$ with a $\Gamma$-invariant pullback map $\beta$ gives `Has D`.

## In the Lean code

The theorem is in [UniformisedSemiAbelianGaloisDescent.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformisedSemiAbelianGaloisDescent.lean#L18). `Near` and `GalAct` are in [QuasiCompact.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/QuasiCompact.lean#L13). The lemmas it calls:

- `exists_near_galois_quotient` in [ExistsNearGaloisQuotient.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsNearGaloisQuotient.lean#L19);
- `descend_of_near` in [SemiAbelianDescendsOfDescendsNearClosedFibre.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianDescendsOfDescendsNearClosedFibre.lean#L14);
- `comp_eq_of_near` in [SpMapClosedPointOfFinite.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SpMapClosedPointOfFinite.lean#L35);
- `has_of_galAct` in [HasOfGalAct.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasOfGalAct.lean#L19).

We read the proof of `comp_eq_of_near` and the statements of the other three lemmas, not their proofs. The output of `descend_of_near` that the map $V \to G$ is an open immersion is not used. Of `Base R`, step 3 uses only the first part (noetherian, normal, complete).
