---
id: j-abdd-op-qq-of-ssn-rep
title: The bounded operators from the fibre maps
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.JA.jABddOpQQ_of_ssnRep
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutJABddDone
covers: 372
status: drafted
drafted_by: writer@claude
---
This theorem proves `JABddOpQQ` from `SSnRep`: each element of the bounded set of the model algebra acts, through the transfer, as an operator of order zero with polynomially bounded coefficients. Its only user is [model places from the gauge transfer and the fibre maps](/entry/formalism-fourier-decay-alt-p-cut-mp-model-place-built2-of-ssn-rep-2/); the result is used in the adjoint relation `JAdj` of [`modelPlaceBuilt2_of_hat`](/entry/model-place-built2-of-hat/). `SSnRep` is stated in [model places from the radial polynomial relation](/entry/model-place-built2-of-poly-s/).

## Statement

Let $L$ be model level data, with $c_1, \dots, c_r$, $\bar c_1, \dots, \bar c_r$, $\zeta$, $\bar\zeta$ and the shifts $S_i$. Put $D_r = c_1 \cdots c_r$, $\bar D_r = \bar c_1 \cdots \bar c_r$, $D = D_r \zeta$ and $\bar D = \bar D_r \bar\zeta$. The *bounded set* of $L$ (`MA.bddSet`) is the union of four classes:

1. scalar: $\zeta^{-1}$, $\bar\zeta^{-1}$, $D \bar D^{-1}$, $\bar D D^{-1}$;
2. the diagonal operators $\kappa(f)$, for all functions $f$ of the type $\rho$ (class $\kappa$);
3. $\bar D_r D_r^{-1} S_i$ for $1 \le i \le k - 1$;
4. the adjoints of class 3.

**Theorem.** If `SSnRep` holds, then there are $C_c$ and $C_b \ge 0$ with this property. Let a setting be built with $C_c$ (`BuiltOW`: `IsBuiltPlace`, each place `Ok`, and the sequences $\delta$, $\delta'$ are words). Let $v$ be a place, $e$ a frame with `IsFrame`, `IsGauge` and `IsGaugeQQ`, and $L$ model level data. Then for each $b$ in the bounded set of $L$ there is a differential operator $\Theta$ on the group with:

- order $0$;
- smooth coefficients on $G_f > 0$, and there it commutes with the action of each element $p$ with `inSS` (`IsAAOp`);
- for $\varepsilon > 0$ and $m \in \mathbb{N}$, on $\{G_f \ge \varepsilon\}$ the derivatives of order at most $m$ of its coefficients and of their adjoints are bounded by $C \cdot N(g)^{C_b (r+1) m}$, where $N$ is the function `B.gN` (`CutCoef`);
- $\Theta$ and its adjoint map the space `Q.FFl` into itself;
- $b \cdot \mathrm{trJ}(J) = \mathrm{trJ}(\Theta J)$ for each $J$ in `Q.FFl`.

The transfer `trJ` is defined in the entry for [`modelPlaceBuilt2_of_bdd`](/entry/model-place-built2-of-bdd/).

## Proof

`jABddOpQQ_of_bddLeaves` proves the statement for each class with its own threshold $K_i$, and takes $C_c = C_b = \max_i K_i$.

1. Scalar class: `bounded_scalar_transfer_holds`, a tactic proof of the version without `IsGaugeQQ`, which `bddClassOpQQ_of` extends.
2. The $\kappa$ class: `kappa_quadratic_bound_holds`, from `jABddKapQQ_of_shared` with four proved lemmas.
3. Classes 3 and 4, the shifts and their adjoints: `jABddSSnQQ_of_leaves` and `jABddSSnStarQQ_of_leaves`, each with `chain_bound_holds`, `second_shift_geometry_holds` and the hypothesis `SSnRep`. Both go through `sSnRealiser_of`, which composes the fibre maps of `SSnRep` with a geometric datum (`SSnGeom`) and a chain rule bound for smooth functions of the coefficients (`ChainBd`).

We have not unfolded `B.gN`, `SSnRealiser`, `IsDatum` or the proofs of the four classes.

## In the Lean code

The theorem is in [CutJABddDone.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJABddDone.lean#L17). `JABddOpQQ` and `jABddOpQQ_of_bddLeaves` are in [CutJABddOp.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJABddOp.lean#L88), `bddSet` in [StatementMA.lean](lean:Formalism/HermitianCurvature/StatementMA.lean#L611).

`SSnRep` is used only for classes 3 and 4. In the Lean statement, `Q.FFl` appears as `smoothFormsPositiveCone`, which [CutJA.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJA.lean#L19) defines as `Q.FFl … 0 (OmP S T v)`, with no positivity condition. The name does not match the definition.
