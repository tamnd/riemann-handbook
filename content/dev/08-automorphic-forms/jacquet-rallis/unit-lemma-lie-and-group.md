---
id: unit-lemma-lie-and-group
title: The unit lemma for self-adjoint and unitary elements, from the Jacquet-Rallis fundamental lemma
kind: theorem
decl: GlobalTheory.UnitLemma.unitLemma_lie_and_group
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.UnitLemmaLieAlgebraUnitaryGroupOfJacquetRallis
covers: 547
status: drafted
drafted_by: writer@claude
---
This theorem proves two lattice-counting identities, one for self-adjoint elements and one for unitary elements, from the Jacquet-Rallis fundamental lemma for unit functions in all ranks. It is the proof of [its statement form](/entry/unit-lemma-lie-algebra-unitary-group-of-jacquet-rallis/), which has the same type. That theorem is below the step [EveryCharacter](/step/every-character/). Below this theorem are 547 declarations of the proof.

## Statement

Let $O$ be a complete discrete valuation ring with fraction field $E$ of characteristic $0$ and residue field of order $q^2$. Let $c$ be an involution of $E$ that keeps $O$ and acts nontrivially on the residue field. Let $A$ be a finite commutative $E$-algebra with a ring involution $\sigma$ that extends $c$, and let $g \in A$. Let $P$ be the characteristic polynomial of multiplication by $g$.

For a unit $x \in A$ with $\sigma(x) = x$, put $h_x(y, z) = \operatorname{Tr}_{A/E}(x\,y\,\sigma(z))$. Let $N(x)$ be the number of $g$-stable $O$-lattices $L \subset A$ that are self-dual for $h_x$, counted modulo the group $T = \{t : t\,\sigma(t) = 1\}$, each orbit weighted by a stabilizer index. Let $S(A, g) = \sum_x N(x)$, where $x$ runs over the classes of such $x$ modulo $x \sim x\,u\,\sigma(u)$. For two such data $(A_1, g_1)$ and $(A_2, g_2)$, let $\kappa$ be the same sum for $A_1 \times A_2$, with each class weighted by $\eta(\det h_{x_1}) = (-1)^{v(\det h_{x_1})}$. The identity is

$$(-q)^{-v(\operatorname{Res}(P_1, P_2))}\,\kappa = S(A_1, g_1)\,S(A_2, g_2).$$

**Theorem.** Assume $\mathrm{UnitMatch}(r)$ for all $r \ge 0$. Then:

1. (Lie algebra form) the identity holds when $\sigma(g_i) = g_i$ and $P_1 P_2$ is separable;
2. (group form) the identity holds when $2$ is a unit in $O$, $g_i\,\sigma(g_i) = 1$ and $P_1 P_2$ is separable.

$\mathrm{UnitMatch}(r)$ is the matching of orbital integrals of unit functions in rank $r$, stated in [the Jacquet-Rallis fundamental lemma for unit functions](/entry/unit-match-all/), which also proves it.

## Proof

The Lie algebra form comes from three statements by `unitLemmaLie_of`:

- `CountIdentity`, from the hypothesis by `countIdentity_of_unitMatch`. For self-adjoint regular $g$, it equates a signed count of $\sigma$-stable lattices on the linear side with the number of self-dual lattices that contain a given unit.
- `UnitaryLimit` (`unitaryLimit`, proved outright): a limit formula that recovers $N(x)$ from these counts.
- `LinearDescent` (`linearDescent`, proved outright): an identity between the limits on the linear side for $A_1$, $A_2$ and $A_1 \times A_2$.

Then `unitLemmaGroup_of_lie` derives the group form from the Lie algebra form. It splits into two cases. If $g_1$ and $g_2$ are integral over $O$, it calls `identity_integral`. If not, both sides of the identity are $0$.

## In the Lean code

The theorem is in [UnitLemmaLieAlgebraUnitaryGroupOfJacquetRallis.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnitLemmaLieAlgebraUnitaryGroupOfJacquetRallis.lean#L14). The proof is two lines, and it calls the five lemmas above through their statement forms in the namespace `T`. The real content is in them:

- `unitLemmaLie_of` in [UnitLemmaSelfAdjointLieOfCountLimitDescent.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnitLemmaSelfAdjointLieOfCountLimitDescent.lean#L137);
- `countIdentity_of_unitMatch` in [RelativeFundamentalLemmaCountIdentityOfUnitMatch.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RelativeFundamentalLemmaCountIdentityOfUnitMatch.lean#L328);
- `unitaryLimit` in [UnitaryLatticeCountRatioTendsto.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnitaryLatticeCountRatioTendsto.lean#L16);
- `linearDescent` in [LinearLatticeCountDescentProof.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LinearLatticeCountDescentProof.lean#L106);
- `unitLemmaGroup_of_lie` in [UnitLemmaUnitaryGroupOddResidueOfLie.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnitLemmaUnitaryGroupOddResidueOfLie.lean#L143).

`UnitLemmaLie`, `UnitLemmaGroup` and `InvAlg.Identity` are in [UnitLemmaGroup.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/UnitLemmaGroup.lean#L153). The three intermediate statements are in [LinearDescent.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LinearDescent.lean#L45). The hypothesis is used only by `countIdentity_of_unitMatch`. The sums in `Identity` are `finsum`, which is $0$ when the support is infinite. We have not unfolded `identity_integral` or the proofs of the five lemmas.
