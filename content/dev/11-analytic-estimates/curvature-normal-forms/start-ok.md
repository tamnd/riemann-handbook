---
id: start-ok
title: The start data at a model level
kind: theorem
decl: Formalism.FourierDecayAlt.P.MAx1.startOK
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CoordinateCommuteRaisingConstant
covers: 508
status: drafted
drafted_by: writer@claude
---
This theorem says that explicit start data satisfy the ten conditions `IsLevelStart` at each model level. It is the content of [the start data fit each model level](/entry/start-admissible/), which only restates it. The proof is an assembly. It checks the ten fields from five proved facts. The largest of them is [the start matrix is a start](/entry/start-is-start/).

## Statement

Let $P$ be parameters with `P.OK`, with $k$ and the interlacing tuples $\pi$ with entries $\rho_i(\pi)$. Let $D$ be an algebra with the laws `D.Laws P.TT`, and let $\kappa$ be the diagonal map from functions of $\pi$ to the operator algebra. Let $L$ be level data whose fields are the model operators (`IsModelLevel`). For $l \in \mathbb{N}$, put $s = (-1)^{k-l}$ and $x_0(\pi, Y) = s\prod_{i=1}^{k-1}(Y + \rho_i(\pi))$. The start data `startM P D l` are:

- the matrix $Q(Y) = s\,\begin{pmatrix} t_{11}(Y) & t_{12}(Y) \\ t_{21}(Y) & t_{22}(Y)\end{pmatrix}$ of model operators,
- the scalar $q(Y) = -T T'\prod_{i=1}^{k}(Y + \tfrac12 + u_i)(Y + \tfrac12 + u'_i)$,
- $x(Y) = \kappa(x_0(\cdot, Y))$ and $\xi(Y) = \kappa(x_0(\cdot, Y)^{-1})$,
- a fixed operator $e(Y)$ (`eeA`), and the set of $Y$ where no factor $Y + \rho_i(\pi)$ is zero.

**Theorem.** `IsLevelStart L (startM P D l)` holds.

## Proof

The ten fields come from these facts.

1. $Q$ and $q$ form a start (`IsStart`). This is [the start matrix is a start](/entry/start-is-start/).
2. The entries $Q_{21}(Y)$ and $Q_{21}(Y')$ commute. This is `lower_left_commute`, with the sign $s$ moved out.
3. $x\xi = \xi x = 1$ where $x_0$ has no zero, $x(Y)$ and $x(Y')$ commute, and $x$ commutes with the scalar functions of $L$ and with $\nabla$. These hold because $\kappa$ is an algebra map into diagonal operators.
4. $x(Y)$ is self-adjoint for real $Y$, by `coordinate_real`.
5. $e(Y)$ commutes with the scalar functions. This uses `sSScalar`: the shifts commute with them.
6. $Q_{22}(Y) = G\,x(Y)$, by `kappa_sign_coordinate`. Here $G$ is the scalar operator of $L$ (`GG`).
7. $Q_{21}(Y) = G\,x(Y)\big(l_0(Y) + \bar\zeta\,\zeta^{-1}G^{-1}e(Y)\big)$ where $x_0$ has no zero. This uses `low_sum` with `sSShift` and `rho_raise`, and the identity `fn_cancel`.

The fact `sSShift` says $\kappa(g)S_l = S_l\kappa(f)$ for the shift $S_l$ when $g(\pi') = f(\pi)$ for each $\pi'$ that raises $\pi$ at place $l$. We have not unfolded `low_sum`.

## In the Lean code

The theorem is at [CoordinateCommuteRaisingConstant.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CoordinateCommuteRaisingConstant.lean#L6102). It is `startAssemble` (line 5774), which is `startOK_of` (line 5453), applied to the five facts. `startM` is in [StatementMA.lean](lean:Formalism/HermitianCurvature/StatementMA.lean#L160) and `IsLevelStart` in [StatementFr.lean](lean:Formalism/HermitianCurvature/StatementFr.lean#L188).
