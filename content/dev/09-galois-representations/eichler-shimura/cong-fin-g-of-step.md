---
id: cong-fin-g-of-step
title: The congruence statement from the step statement
kind: theorem
decl: UpperTheory.Gal.Int.Cong.congFinG_of_step
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.CongruenceOddLevel.CongFinOddOfLvLac
covers: 420
status: drafted
drafted_by: writer@claude
---
This theorem gives the congruence statement `CongFinG` from the step statement `StepSt`. Its user is [`congFinG_of_ex`](/entry/cong-fin-g-of-ex/), which proves `StepSt` from lacunary weights. The result goes on to [`congFinOdd_of_ex`](/entry/cong-fin-odd-of-ex/) and the [Galois row](/proof/galois-row/). The theorem is a pass-through. It fills three hypotheses of [`congUWG_of`](/entry/cong-uwg-of/), which has the real content. Below it are 420 declarations.

## Statement

**Theorem.** If `StepSt` holds, then `CongFinG` holds.

`CongFinG` is `CongUWG TyEll (GenOf DGen) WtLac`. The entry [`congUWG_of`](/entry/cong-uwg-of/) states `CongUWG` and `StepSt`. The parameters are conditions on the approximating representations $U'$:

- `TyEll`: at $w_0$, an open compact subgroup $J$ acts on a vector of $U'$ by a character $\chi \circ \theta$ with $\chi \neq 1$, and each smooth irreducible representation with such a vector is cuspidal.
- `GenOf DGen`: at each $z \in Z$, each ordering $\alpha$ of the Satake parameters has $D_a(\alpha) \neq 0$. The integer polynomial $D_a$ is a product of factors $X_i^{c+1} - X_j^{c+1}$, $X_i X_k - X_j^2$ and differences of monomials of degree $a$.
- `WtLac`: $U'$ has the weight of $U$ off $w_0$ and $v'$, and its weight at one $\tau_0$ over $v'$ is lacunary (`GapJ`).

## Proof

The proof is `congUWG_of H finU_holds DGen dGen_ne_zero`. Here `finU_holds` proves `FinU`, and `dGen_ne_zero` proves $D_a \neq 0$. We have not opened their proofs.

## In the Lean code

The theorem is in [CongFinOddOfLvLac.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/CongFinOddOfLvLac.lean#L11). `DGen` and `WtLac` are in [LimWPhi.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/LimWPhi.lean#L14), and `TyEll` and `GenOf` in [GenOf.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/GenOf.lean#L14). The word "step" in the name refers to the hypothesis `StepSt`, not to a step of the written proof.
