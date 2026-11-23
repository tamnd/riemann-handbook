---
id: theorem-i-closed-form-holds
title: The base-level projection bound for large constants
kind: theorem
decl: Formalism.MainNotions.flipOneThree.Pf.theorem_I_closed_form_holds
module: Formalism.SharpRestriction.GrowthBounds.HermitianTensor
covers: 1319
status: drafted
drafted_by: writer@claude
---
This theorem proves `SecondPartClosed D` for each datum $D$ and fills the field `p13B` of the records `Loc8` and `Loc8All`, beside [the averaged bad-share bound](/entry/theorem-a-closed-form-holds/) in `p13A`. Both reach the trunk step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/), where `first_theorem_with_constants` supplies the hypothesis.

## Statement

Fix natural numbers $p, n', m, G', N_1, c_{\mathrm{cl}}, D_p, c_*$, a set $T \subset \mathbb{Z}/n'$ and reals $Y, Y_b, a, b', b_l, b_u$. Put $k = m + 1$, $\ell_a = C_0 N_1^2 \log a$, and let $I_a = \mathbb{Z} \cap [a, a + a/(kY)]$ and $I_b = \mathbb{Z} \cap [b_l, b_u]$. The hypothesis `HypI` is about twenty inequalities among these numbers and constants $C_0, C_H$, for example $1 \le Y$, $k^2 Y^2 \le p$, $b_l \le b' \le b_u$, $C_H |T| \ell_a^2 \le k$, and no odd power of $p$ lies in $[(1 - 2\delta) a/b', (1 + 2\delta) a/b']$, where $\delta$ is the number `deI`.

`Conclusion2` $(C_0, C_H, C)$ says: for all parameters with `HypI`, there is a function $\kappa \colon \mathbb{Z}^T \times \mathbb{Z}^T \to \mathbb{R}_{\ge 0}$ with

$$ \frac{1}{|I_a|^{|T|} |I_b|^{|T|}} \sum_{\alpha \in I_a^T} \sum_{\beta \in I_b^T} \kappa(\alpha, \beta) \le \frac{C |T| N_1}{Y}, $$

such that for each `UnramifiedQuadraticSetting` (discrete valuation rings $W \subset Q$, $O \subset K$, an embedding $\iota \colon Q \to K$, $\sigma \in \operatorname{Aut} Q$ with $\sigma^{n'} = 1$, and $w \in O$ with $w^2 = p$), for each weight $(a_w, b_w, \lambda_0)$ in the window (`WeightI`), and for each integer $t \ge t_I$ (the bound `tI`), `LPprime` holds with $\kappa(a_w, b_w)$. `LPprime` says that $4(D_p + 1) \le c_*$ and that at each $W$-lattice $L \subset Q^{k}$ there are vectors $F_i \in V(\lambda_0)$, on edges ending at $L$, whose pairings have rank at least $(1 - \kappa) \dim V(\lambda_0)$ up to $p^{D_p}$. We have not unfolded `Nsrc`, `Re` and `be`.

**Theorem.** For a datum $D$ (`D7`), assume `AdmBE D`: for each $C_c \ge 0$ there is $T_0 > 0$; for each $C_0 \ge T_0$ there is $T_1 > 0$; for all $C_{E1}, C_{E2}, C_m \ge T_1$ there is $T_2 > 0$; for each $C_H \ge T_2$ there are positive $C_A, C_\kappa, C_t, C_s$ with `AdmB D` at these ten constants. Then there is $T_0 > 0$ such that for each $C_0 \ge T_0$ there are $T_2, C > 0$ with `Conclusion2` $(C_0, C_H, C)$ for all $C_H \ge T_2$.

`AdmB` has five conjuncts: `PathPairCorrespondence` (`Conclusion1` for each instance), `admB2` (a bound `RhoGE` at each edge), `admB3` (a rank bound by segment ranks), `ColumnFamilyLowerSet` (a bound on block orders), and `AdmT D`, twelve tool statements.

## Proof

The proof is `theorem_I_of_pairing_GL D qPh_proved`, where `qPh_proved : QPh` is `qPh_of tauP smithP bilinP detFactsP numP detDivP` (through `qPh_of_rest`). The inputs `tauP` and `smithP` carry the weight: an equivariant map between polynomial spaces of dual weights, onto on the integral lattices, and an invariant bilinear form with dual bases on which it takes the values $p^{k_b}$. The rest of the work is in [the base-level bound from a $\mathrm{GL}$-invariant pairing](/entry/theorem-i-of-pairing-gl/).

## In the Lean code

The theorem is in [HermitianTensor.lean](lean:Formalism/SharpRestriction/GrowthBounds/HermitianTensor.lean#L18), with `qPh_proved` at line 9. The statement is in [ProjectionLemmaBaseLevel.lean](lean:Formalism/SharpRestriction/GrowthBounds/ProjectionLemmaBaseLevel.lean#L260). The records are filled in [AdmissibleFamilyNoKernel.lean](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleFamilyNoKernel.lean#L63) and [TensorOfPairLift.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/TensorOfPairLift.lean#L612).

Odd points:

- The conclusion does not depend on $D$: `Conclusion2` takes it as `_D`. So do several tools in `AdmT`.
- Other modules of this folder also define `AdmB`, `AdmT`, `GradedLatticeStable` and `SecondPartClosed`, in other namespaces. We use those of `flipOneThree`.
