---
id: cube-add-int-be-biadd
title: The cube relation for the p-adic sigma function and the integral formal group
kind: theorem
decl: GlobalTheory.ThetaCube.cube_addInt_beBiadd
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.ThetaCubeRelationIntegralFormalGroupBiadditive
covers: 410
status: drafted
drafted_by: writer@claude
---
This theorem proves three facts about the formal group of an elliptic curve over $\mathbb{C}_p$ with lattice $\delta\,\mathfrak{c}$ and the logarithm of a $p$-adic sigma series on it. `CMEndo.endo_all` uses them, and through it the integrality fields of [the inputs of the norm bound](/entry/inp-all/). It belongs to the step [nonempty hypotheses](/step/nonempty-hyps/).

## Statement

Fix a datum $D$, a prime $p$, an ideal $\mathfrak{c}$ of norm prime to $p$, a twelfth root $\delta$ of the discriminant, and a record $g$ that satisfies `At D c δ g`. The record gives an embedding $\overline{\mathbb{Q}} \to \mathbb{C}_p$, the lattice $\delta\,\mathfrak{c} \subset \mathbb{C}$, a Weierstrass curve $W$ obtained from a model by a change of variables, its formal logarithm $l$, and a series $\mathrm{ex}$ with $l \circ \mathrm{ex} = X$. The group law is $x \oplus y = \mathrm{ex}(l(x) + l(y))$. Let $\varphi = -\log \Phi_1$, where $\Phi_1$ is the series `ePhi1` built from a $p$-adic sigma series. Write $f \simeq h$ when $f - h$ has constant term $0$ and $\exp(f - h)$ has coefficients of norm at most $1$.

**Theorem.** For each such $D$ and $g$:

1. (cube) $\varphi(x \oplus y \oplus z) - \varphi(x \oplus y) - \varphi(y \oplus z) - \varphi(z \oplus x) + \varphi(x) + \varphi(y) + \varphi(z) \simeq 0$;
2. (addInt) $x \oplus y$ has integral coefficients, and it satisfies the condition `IntegralW` when `ModelOverW` holds;
3. (beBiadd) $b(x, y) = \varphi(x \oplus y) - \varphi(x) - \varphi(y)$ is additive in each variable up to $\simeq$.

## Proof

1. The cube relation is `theorem_of_cube_of_addition_formulas`. It takes two proved identities: the $p$-adic sigma addition formula `T.sigmaStar_addition_formula_padic_modelParameter`, of the shape $\sigma(x+y)\sigma(x-y) = (\dots)\sigma(x)^2\sigma(y)^2$, and the determinant identity `T.pAdicFrobeniusStickelberger_of_d7_datum` in three variables. They give two auxiliary identities, `cube2` and `cube3`, and `cube_of` joins them.
2. `addInt_holds` proves integrality of the group law, by `additive_integral_generation`.
3. `beBiadd_of_cube` deduces biadditivity from the cube relation. Since $\oplus$ comes from a logarithm, it is commutative and associative. Then $b(x \oplus y, z) - b(x, z) - b(y, z)$ is the cube expression, and the same holds in the second variable.

## In the Lean code

The theorem is in [ThetaCubeRelationIntegralFormalGroupBiadditive.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/ThetaCubeRelationIntegralFormalGroupBiadditive.lean#L11). The definitions are in [GL3Theta.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/GL3Theta.lean#L135). The cube relation is assembled in [TheoremOfCubeOfAdditionFormulas.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/GlobalRankLatticeProofs/UnitTraceSumBounds/TheoremOfCubeOfAdditionFormulas.lean#L44). We have not opened the proofs of the two identities or of `cube_of`, and we have not unfolded `IntegralW` or `ModelOverW`.

The series behind `ePhi1` is `sgStar`, an odd entire function with derivative $1$ at $0$ and a quasi-periodicity law. It is chosen by `Classical.epsilon` in [IsDiscriminantTwelfthRootOfIdealLattice.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/GeneralLinearActions/IsDiscriminantTwelfthRootOfIdealLattice.lean#L238), so the statement is about one fixed choice.
