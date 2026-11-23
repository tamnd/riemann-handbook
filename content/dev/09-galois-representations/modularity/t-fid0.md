---
id: t-fid0
title: A trace identity between twisted U(3) and the quaternion groups
kind: theorem
decl: UpperTheory.V.Z.Sym.Glob.tFId0
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.SymmetricPowerTransfer.GlobalUnitaryForms.ScalarTuples.TFId0
covers: 1416
status: drafted
drafted_by: writer@claude
---
This theorem writes the trace of a twisted Hecke operator on forms on a definite $U(3)$ as a positive multiple of a sum of traces on the norm one quaternion group $D^1$, plus a multiple of a trace on $D^\times$. [The dichotomy over a totally real field](/entry/spec-f/) separates characters in this identity. The proof here is only algebra: it combines three trace computations, `sideG`, `split_side_identity_unitary` and `sideK`, which hold the content.

## Statement

Let $F$ be a totally real field, $\Delta \in F$ totally negative, $E = F(\sqrt{\Delta})$. Let $U_3$, $D^\times$, $D^1$, the spaces of forms and the conditions `IsBG`, `IsBS`, `IsBK` be as in [the dichotomy](/entry/spec-f/). Let $\mathcal{D}$ be data with `D.Ok`: a nonempty finite set $\Sigma$ of places of $F$ where $\Delta$ is a square, local data there, and a character $\chi$. For $t = (t_v)_{v \in \Sigma}$ in the cone `D.Cone`, there are test functions $f_G^t$ on $U_3(\mathbb{A}_f)$, $f_S^t$ on $D^\times(\mathbb{A}_f)$ and $f_K^t$ on $D^\times(\mathbb{A}_f)$. Each is a product of local functions: given by $t_v$ at $v \in \Sigma$, and the unit of the spherical Hecke algebra (or a $\chi$ variant for $f_K$) elsewhere. Put $f_S^{t,x}(g) = f_S^t(x^{-1} g x)$ on $D^1(\mathbb{A}_f)$.

**Theorem.** Let $x_0$ be a finite adele of $D^\times$ with $(x_0)_v = 1$ for $v \in \Sigma$. There are $n$, finite adeles $x_0, x_1, \dots, x_n$ (the first one the given $x_0$), all equal to 1 on $\Sigma$, and reals $a > 0$ and $b$ with this property. Let $c$ be a function on $F$, let $B_G$ (with twist $\theta$), $B_{S,i}$ and $B_K$ be spaces of forms with finite dimensional weights that satisfy `IsBG`, `IsBS` at $x_i$, and `IsBK` for $c$. Then for each $t$ in the cone
$$\operatorname{tr}\bigl(R_\theta(f_G^t) \mid B_G\bigr) = a \sum_{i=0}^n \operatorname{tr}\bigl(R(f_S^{t,x_i}) \mid B_{S,i}\bigr) + b\, \operatorname{tr}\bigl(R(f_K^t) \mid B_K\bigr).$$
The numbers $n$, $x_i$, $a$, $b$ depend only on $\mathcal{D}$ and $x_0$.

## Proof

The three lemmas compare each side with two sums over $\tau \in F$:
$$\Sigma_S(t) = \sum_{\tau \text{ good}} c(\tau)\, m(\tau)\, n_S(\tau), \qquad \Sigma_K(t) = \sum_{\tau \text{ good}} c(\tau)\, m(\tau)\, n_K(\tau).$$
Here $\tau$ is good if $\sigma(\tau^2 - 4) < 0$ for each real embedding $\sigma$ and a local condition holds at $\Sigma$, $m(\tau)$ is a mass, and $n_S$, $n_K$ are products of local orbital integrals off $\Sigma$. We have not unfolded these.

1. `sideG`: the $U_3$ trace is $c_G(\Sigma_S + e\,\Sigma_K)$ with $c_G > 0$.
2. `split_side_identity_unitary`: it gives $x_0, \dots, x_n$, and the sum of the $D^1$ traces is $c_S\,\Sigma_S$ with $c_S > 0$.
3. `sideK`: the $D^\times$ trace is $c_K\,\Sigma_K$ with $c_K > 0$.

Then $a = c_G/c_S$ and $b = c_G e / c_K$. The private lemma `alg` checks the algebra.

## In the Lean code

The theorem is in [TFId0.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/ScalarTuples/TFId0.lean#L16). `TFId0` is in [HodgeTateFromSandwich.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/HodgeTateFromSandwich.lean#L199).

- `sideG` is in [AdmissibleTraceRegular.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/ScalarTuples/AdmissibleTraceRegular.lean#L156), `split_side_identity_unitary` in [QuaternionStableSideTraceIdentity.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/ScalarTuples/QuaternionStableSideTraceIdentity.lean#L41), and `sideK` in [QuotSumCongr.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/ScalarTuples/QuotSumCongr.lean#L307). Their statements `SideG`, `SideK` and the sums are in SymbolEx.lean.
- `TFId0` is `TFId` of SymbolEx.lean with $x_0$ given, in place of $x_0 = 1$.
- The sign of $b$ is the sign of $e$, which `SideG` leaves free.
- The identity has the shape of a comparison of trace formulas, but the Lean statement names no published result, and we do not name one.
