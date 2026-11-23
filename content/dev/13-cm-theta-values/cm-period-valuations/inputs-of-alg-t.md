---
id: inputs-of-alg-t
title: The theta and CM curve inputs, given algebraic translates
kind: theorem
decl: GlobalTheory.ThLoc.inputs_of_algT
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.NormalisedThetaCMCurveTheoremsOfAlgebraicTransla
covers: 907
status: drafted
drafted_by: writer@claude
---
This theorem fills the structure `ThLoc.Inputs`, eight facts about CM elliptic curves and their theta functions. Seven fields are proved theorems; the eighth is the hypothesis `AlgTAll`. Its user is the restatement [`normalisedThetaCMCurveTheorems_of_algebraicTranslates`](/entry/normalised-theta-cmcurve-theorems-of-algebraic-translates/), and through it [`at_of_true_columns`](/entry/at-of-true-columns/). Of the 907 declarations below it, 734 are below [`locJets_all`](/entry/loc-jets-all/).

## Statement

**Theorem.** If `AlgTAll` holds, then `Inputs` holds.

`AlgTAll` is stated in [`servH_row`](/entry/serv-h-row/). Here $d$ is a positive integer, $\omega_K = (1 + i\sqrt d)/2$, and a lattice $L \subset \mathbb C$ *has CM by $d$* (`HasCMBy d L`) if $\omega_K L \subseteq L$. A curve $W$ over $\mathbb C_p$ is *integral* (`IntCurve W`) if its coefficients $a_1, \dots, a_6$ have norm at most 1 and its discriminant has norm 1. A power series has *integral jets* (`JetsIntegral`) if $\kappa!\, a_\kappa$ has norm at most 1 for every coefficient $a_\kappa$. The fields of `Inputs` are:

1. `jInt`: if $d$ is squarefree, $d \equiv 3 \pmod 4$ and $L$ has CM by $d$, then $j(L) = 1728\, g_2^3/(g_2^3 - 27 g_3^2)$ is an algebraic integer.
2. `modelTwo`: if $d$ is squarefree, $d \equiv 7 \pmod 8$, $L$ has CM by $d$ and $\iota \colon \mathbb C \to \mathbb C_2$ is a field isomorphism, then a multiple $cL$ has an integral Weierstrass model $W$ over $\mathbb C_2$ with $g_2, g_3$ equal to $\iota(g_2(cL)), \iota(g_3(cL))$ and $|a_1(W)| = 1$.
3. `jetsOdd`, `jetsTwo`: for a CM datum, a self-dual hermitian lattice $\Lambda$ stable under the CM action, and a theta function $\theta$ of $\Lambda$, a series `thetaLin` built from $\theta$ and mapped to $\mathbb C_p$ has integral jets (with a bound on its pairings `jetPair`). `jetsOdd` (`IntOpLoc`) is for odd $p$ prime to the discriminant, `jetsTwo` (`IntOpTwoLoc`) for $p = 2$.
4. `jetsThree` (`ThetaZJetsThree`): if $d \equiv 7 \pmod 8$, $d \equiv 2 \pmod 3$ and $L$ has CM by $d$, a series `thetaZ` built from $L$ at $p = 3$ has integral jets.
5. `shape`: `EmbSep` implies `ShapeEigenLoc`, a factorization $\exp(\cdots)\, s$ with $s$ of integral jets for the same theta series at a prime $p$ that divides the discriminant.
6. `algT`: `AlgTAll`.
7. `lamExt`: every embedding $\lambda \colon \overline{\mathbb Q} \to \mathbb C_p$ extends to a field isomorphism $\mathbb C \to \mathbb C_p$.

We have not unfolded `thetaLin`, `thetaZ` or `EmbSep`.

## Proof

- `jInt` is `cm1` ([JInvNormLeOne.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JInvNormLeOne.lean#L10)). Its proof reduces to the modular $j(\tau)$ and applies `isIntegral_modularJ_of_mul_mem`. This is the integrality of singular moduli (Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Theorem II.6.1).
- `modelTwo` is `goodOrdinaryModelAtTwo_cmLattice_seven_mod_eight`, a second name for `GoodTwo.goodModelTwo`. The conditions $|a_1| = 1$ and $|\Delta| = 1$ say that $W$ has good ordinary reduction: in characteristic 2 the invariant is $a_1^{12}/\Delta$, and $0$ is the only supersingular invariant (Silverman, *The Arithmetic of Elliptic Curves*, Appendix A). This fits Deuring's criterion, since 2 splits in $\mathbb Q(\sqrt{-d})$ (Deuring, Abh. Math. Sem. Univ. Hamburg 14, 1941).
- `jetsOdd`, `jetsTwo` and `shape` are the three parts of [`locJets_all`](/entry/loc-jets-all/).
- `jetsThree` is `thetaZJetsThree` ([IntSExpMulTranslate.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/IntSExpMulTranslate.lean#L155)).
- `lamExt` is `place_extends_to_iso`, which applies `PadicComplexIso.exists_ringEquiv_extending`.

## In the Lean code

The theorem is at [NormalisedThetaCMCurveTheoremsOfAlgebraicTransla.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/NormalisedThetaCMCurveTheoremsOfAlgebraicTransla.lean#L18). `Inputs` is in [ThetaZJetsThree.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ThetaZJetsThree.lean#L34), and `AlgTAll` in [StatementAlgT.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/StatementAlgT.lean#L9).

The hypothesis `AlgTAll` is only copied into the field `algT`. So `Inputs` is equivalent to `AlgTAll`, and the theorem only puts seven proved facts next to it. `cm1` does not use the hypothesis that $d$ is squarefree (line 11: `intro d L _ hd hL`). The field `shape` is an implication from `EmbSep`, not `ShapeEigenLoc` itself.
