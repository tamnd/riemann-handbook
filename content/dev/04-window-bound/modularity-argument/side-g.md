---
id: side-g
title: The twisted trace on forms on a definite unitary group in three variables
kind: theorem
decl: UpperTheory.V.Z.Sym.Glob.sideG
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.SymmetricPowerTransfer.GlobalUnitaryForms.ScalarTuples.AdmissibleTraceRegular
covers: 890
status: drafted
drafted_by: writer@claude
---
This theorem computes the trace of a twisted Hecke operator on forms on a definite $U_3$ as a sum over $\tau \in F$. It is the first of the three trace computations in [`tFId0`](/entry/t-fid0/), where it gives the $U_3$ side $c_G(\Sigma_S + e\,\Sigma_K)$. The proof is a twisted trace formula, followed by a count of the conjugacy classes over each $\tau$.

## Statement

Let $F$, $\Delta$, the data $\mathcal{D}$ with `D.Ok`, the set $\Sigma$, the cone of parameters $t$, the test function $f_G^t$ and the sums $\Sigma_S(t)$, $\Sigma_K(t)$ be as in [`tFId0`](/entry/t-fid0/).

**Theorem.** Assume `D.Ok`. There are reals $c_G > 0$ and $e$ with this property. Let $V$ be a finite dimensional complex space, $c$ a function on $F$, and $B$ a space of forms on $U_3$ with weight $V$ and twist $s$ that satisfy `IsBG` for $c$. Then for each $t$ in the cone
$$\operatorname{tr}\bigl(R_s(f_G^t) \mid B\bigr) = c_G\bigl(\Sigma_S(t) + e\,\Sigma_K(t)\bigr).$$

The condition `IsBG` fixes the level `D.UG`, makes the central character and the subgroup $\Gamma_0$ trivial, and makes the twist the involution $\theta$. Its last field says that $\operatorname{tr}(W(\delta) \circ \Theta \mid V) = c(\tau)$ when $\delta$ has invariant $\tau$.

## Proof

The constants are explicit:
$$c_G = \frac{1}{4} \Bigl(\prod_{v \in \Sigma} c_G(v)\Bigr) \cdot \#\mathrm{Sel}(1), \qquad e = (-1)^{[F:\mathbb{Q}]}.$$
Here $c_G(v) > 0$ are local constants of $\mathcal{D}$, and $\mathrm{Sel}(y)$ is the set of totally positive classes $c \in F^\times / F^{\times 2}$ with the condition `D.Ev` on $cy$. By `selCard`, $\mathrm{Sel}(1)$ is finite and not empty. The sign comes from `basePt` as $(-1)^{\#\{F \to \mathbb{R}\}}$, which is $(-1)^{[F:\mathbb{Q}]}$ because $F$ is totally real.

1. **Trace formula.** By `finG`, $B$ is finite and $f_G^t$ is a test function. So `Tf.trace` applies: if $(\delta_i)_{i \in I}$ meets each twisted conjugacy class in the support of the kernel exactly once, then $\operatorname{tr} R_s(f) = \sum_i \mathrm{term}(f, \delta_i)$, a finite sum.
2. **Classes.** The index set has pairs $(\tau, x)$. Here $\tau$ is good and integral at each $v \notin \Sigma$, and $x \in F^\times / F^{\times 2} \times F^\times / N E_\tau^\times$ admits a model $\delta_x$ (`Models`). Different pairs give classes that are not conjugate (`sideGTau`, `conjG`, `cls_eq`). Each class in the support is one of them (`tauEx`, `sideGSupp`, `classG`, `sg_out`).
3. **Terms.** `term_eq` gives $\mathrm{term}(f_G^t, \delta_x) = \tfrac{1}{2}\bigl(\prod_{v \in \Sigma} c_G(v)\bigr)\, c(\tau)\, m(\tau)\, n_L(x)$, where $n_L$ is a product of local counts. It uses `sideGTerm`, `gqG`, `modelFacts` and the last field of `IsBG`.
4. **Inner sum.** `weight_eq` turns "there is a model" into $\mathbf{1}[x_1 \in \mathrm{Sel}(2 - \tau)] \cdot \mathbf{1}[x_2 \text{ totally positive}]$. With the identity of `basePt`, `sg_inner` sums $n_L$ over $x$ and gets $\#\mathrm{Sel}(1) \cdot \tfrac{1}{2}(n_S(\tau) + e\, n_K(\tau))$.
5. **Integrality.** `sum_GI` drops the integrality condition on $\tau$: if $\tau$ is not integral at some $v \notin \Sigma$, then $n_S(\tau) = n_K(\tau) = 0$ by `sg_vanish`. This uses $\tau^2 - 4 \ne 0$ (`aux_statement_10`).

We have not unfolded `gOrb`, `lcount`, `kapSum`, `D.Ev`, `Models` or the masses.

## In the Lean code

The theorem is in [AdmissibleTraceRegular.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/ScalarTuples/AdmissibleTraceRegular.lean#L156). Its statement `SideG` and the sums are in [SymbolEx.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/SymbolEx.lean#L81). The lemmas:

- `basePt` in [BasePt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/ScalarTuples/BasePt.lean#L274);
- `Tf.trace` in [ResidualAutomorphyOfLinkedEnds.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/TraceFormulaEigenvalues/TraceFibreCardinality/ResidualAutomorphyOfLinkedEnds.lean#L171), with its statement in [FormsFin.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/TraceFormulaEigenvalues/FormsFin.lean#L27);
- `sg_inner` and `sg_vanish` in [SideGLoc.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/IntegralStabilizers/SideGLoc.lean#L121);
- `Sel` and $n_L$ in [HodgeTateFromSandwich.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/HodgeTateFromSandwich.lean#L56);
- the private `GI`, `sum_GI`, `term_eq` and `weight_eq`, in the file of the theorem.

The statement `SideG` leaves $e$ free, but the proof gives $e = (-1)^{[F:\mathbb{Q}]}$. So the sign of $b$ in [`tFId0`](/entry/t-fid0/) is known.
