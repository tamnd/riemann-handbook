---
id: unit-lemma-lie-algebra-unitary-group-of-jacquet-rallis
title: The lattice-count identity from unit matching (named form)
kind: theorem
decl: GlobalTheory.T.unitLemma_lieAlgebra_unitaryGroup_of_jacquetRallis
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.UnitLemmaLieAlgebraUnitaryGroupOfJacquetRallisStatement
covers: 549
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`unitLemma_lie_and_group`](/entry/unit-lemma-lie-and-group/), which has the proof. It turns the Jacquet-Rallis fundamental lemma for unit functions in all ranks into an identity between counts of lattices, in a Lie algebra form and a group form. Its place in the spine is below [EveryCharacter](/step/every-character/). Below it are 549 declarations of the proof.

## Statement

If $\mathrm{UnitMatch}(r)$ holds for all $r$, then $\mathrm{UnitLemmaLie}$ and $\mathrm{UnitLemmaGroup}$ hold. $\mathrm{UnitMatch}$ is defined in [unit matching](/entry/unit-match-of-weil-field/), and [its statement file](/entry/jacquet-rallis-unit-match-all-ranks/) proves the hypothesis.

Let $E$ be the fraction field, of characteristic $0$, of a complete discrete valuation ring $\mathcal{O}$ whose residue field has $q^2$ elements. Let $c$ be an involution of $E$ that preserves $\mathcal{O}$ and is not trivial on the residue field, and let $\eta(x) = (-1)^{v(x)}$. Let $B = (A, \sigma, g)$ be a finite commutative $E$-algebra $A$ with a $c$-semilinear involution $\sigma$ and an element $g$. Let $P_B$ be the characteristic polynomial of multiplication by $g$. For a $\sigma$-fixed unit $x$, let $N_B(x)$ count the $g$-stable $\mathcal{O}$-lattices of $A$ that are self-dual for $\operatorname{Tr}_{A/E}(x y \sigma(z))$, up to the unitary group $\{t : t\sigma(t) = 1\}$, with an index as weight. Let $\mathrm{st}(B)$ be the sum of $N_B(x)$ over $x$ in the $\sigma$-fixed units modulo the norms $u\sigma(u)$. The identity for $B_1$, $B_2$ is

$$(-q)^{-v(\operatorname{Res}(P_{B_1}, P_{B_2}))} \sum_{x} \eta(\det \mathrm{Gram}_{B_1}(x_1))\, N_{B_1 \times B_2}(x) = \mathrm{st}(B_1)\,\mathrm{st}(B_2),$$

with $x = (x_1, x_2)$ over the classes of $B_1 \times B_2$ and $\mathrm{Gram}_{B_1}(x_1)$ the Gram matrix of the form for $x_1$ in a basis of $A_1$.

- $\mathrm{UnitLemmaLie}$: the identity holds when $\sigma(g_i) = g_i$ and $P_{B_1} P_{B_2}$ is separable.
- $\mathrm{UnitLemmaGroup}$: the identity holds when $2$ is a unit in $\mathcal{O}$, $g_i \sigma(g_i) = 1$, and $P_{B_1} P_{B_2}$ is separable.

## Proof

The proof is the term `GlobalTheory.UnitLemma.unitLemma_lie_and_group`. Its type is the statement, so Lean accepts it at once.

## In the Lean code

The theorem is in [UnitLemmaLieAlgebraUnitaryGroupOfJacquetRallisStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnitLemmaLieAlgebraUnitaryGroupOfJacquetRallisStatement.lean#L8). The proof is the tactic `first | exact @GlobalTheory.UnitLemma.unitLemma_lie_and_group | ...`, and the first branch closes the goal. The definitions are in [UnitLemmaGroup.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/UnitLemmaGroup.lean#L148).

The theorem has two direct uses: `unitLemma_identity_unconditional` and [`match_principal_congruence_inert`](/entry/match-principal-congruence-inert/). Both apply it to `jacquetRallisUnitMatch_all_ranks` and take only the first part, $\mathrm{UnitLemmaLie}$. The group form here, with its condition that $2$ is a unit, is not used by them. `unitLemma_identity_unconditional` gets the group form for every residue characteristic from the Lie form, by `unitLemma_unitary_group_every_residue_of_lie`.
