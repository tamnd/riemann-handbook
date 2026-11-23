---
id: div-set-holds
title: A small subrepresentation from a dense set of killing polynomials
kind: theorem
decl: UpperTheory.Gal.Int.Div.divSet_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.ZetaCharacterDivisibility.DivisionOneGeometricRepresentation
covers: 495
status: drafted
drafted_by: writer@claude
---
This theorem proves `DivSet`. Its user is [divOne_holds](/entry/div-one-holds/), which gives `DivSet` a dense set of Frobenius elements. `DivSet` is the group theory behind the cut: from a representation $\rho$ and a dense set of elements $g$ with a monic polynomial of degree $a$ that kills $\rho(g)$, it gives a subrepresentation $r$ of dimension $a$. The proof only specializes a statement about compact groups, `DivWCoreLac`, to the Galois group $G_E$. That statement has no entry of its own. Below it are 495 declarations.

## Statement

Let $E$ be a number field, $\ell$ a prime, $a, dd \in \mathbb{N}$, and $\rho : G_E \to \mathrm{GL}_{dd}(\overline{\mathbb{Q}}_\ell)$ continuous and semisimple with `HTRichEx ρ a`. Let $\psi : G_E \to \overline{\mathbb{Q}}_\ell^\times$ be a continuous character. Suppose that the set of $g$ with a monic $Q$ of degree $a$ such that $Q(\rho(g)) = 0$ and $\psi(g) = (-1)^a Q(0)$ is dense.

**Theorem.** There is a continuous semisimple $r : G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ with `Inside r ρ` and `Covers r ρ`, such that the set of $g$ where the characteristic polynomial of $r(g)$ is separable is open and dense.

`HTRichEx ρ a` asks for one place above $\ell$ where the Hodge-Tate jumps of $\rho$ contain a lacunary set of $a$ integers. A family $e_1, \dots, e_n$ is lacunary (`IsLac`) if $|B| \sum_A e_i \neq |A| \sum_B e_i$ for all disjoint nonempty sets $A, B$ of indices.

## Proof

The proof is `divSet_of` applied to `goal_holds`, `senWLac_holds`, `lacBridge_of` and `inFacts_of`. In `divSet_of`:

1. `LacBridge` turns `HTRichEx ρ a` into `HTLac ρ a`.
2. `SenWLac` gives a matrix $X$ over a larger algebraically closed field $K'$. $X$ is in the Lie algebra of the Zariski closure of $\rho(G_E)$ (`InLieZar`), and its characteristic polynomial has $a$ distinct lacunary roots. We have not opened the proof of `SenWLac`.
3. For each $g$ in the dense set, it picks a polynomial $P(g)$ by choice.
4. `DivWCoreLac` applied with $\Gamma = G_E$ gives $r$. It keeps the claims on `Inside`, `Covers`, and the separable set.

`DivWCoreLac` also gives $\det r = \psi$ and the characteristic polynomials of $r$ on the dense set. `divSet_of` drops these claims. [divAll_holds](/entry/div-all-holds/) proves $\det r = \psi$ again with `DivDet`.

## In the Lean code

The theorem is in [DivisionOneGeometricRepresentation.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/DivisionOneGeometricRepresentation.lean#L52). `divSet_of` is in [PDivSet.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PDivSet.lean#L16). It does not use its `InFacts` argument. `DivSet` is in [PhiOfDivOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PhiOfDivOf.lean#L121). `DivWCoreLac` is in [DivWCoreLacUseType.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/CocharacterLieDivisors/DivWCoreLacUseType.lean#L90), and `SenWLac` in [StGalW.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/CocharacterLieDivisors/StGalW.lean#L26). `goal_holds` in [GoalHolds.lean](lean:Development/EtaleCohomology/DivisorCycles/GoalHolds.lean#L19) proves `DivWCoreLac` from 13 lemmas. Each of them has the name `intersectionNumber_baseChange`, but their types are the parts `SpecLie`, `Key`, `Rep`, `FinPoly` and so on that `goal_of` asks for. We found no intersection numbers in these types.
