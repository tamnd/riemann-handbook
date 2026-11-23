---
id: dat-exists
title: A rescaling by roots of unity that makes the twisted phases trivial
kind: theorem
decl: GlobalTheory.Fam.QuadraticExtensionData.dat_exists
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.DatExists
covers: 485
status: drafted
drafted_by: writer@claude
---
For a geometric family with top matrix the identity, this theorem gives nonzero constants $C_j$ and, for each quadratic extension datum, a rescaling $s$ by roots of unity that makes each local value $\xi_j$ a rational datum with trivial phase. Through its second name [`true_geometry_row_pair_relation_alt_alt_alt`](/entry/true-geometry-row-pair-relation-alt-alt-alt/), [the column side](/entry/col-side-alt/) uses $s$ to rescale the tuples.

## Statement

Let $W$, $u$ and the geometric family $a$ be as in [the column side](/entry/col-side-alt/), with `a.Is`, `a.True` and top matrix $i_A = 1$ at level $m$. A *quadratic extension datum* $J$ at $t$ has a twist datum $A$, places $w_1, \dots, w_r$ in the twist set $Q(t)$ and a quadratic extension $E_i$ at each $w_i$. The characters at level $j$ are tuples $\alpha = (\alpha_i)$ with $\alpha_i$ a character of $E_i$, and $\mathrm{wt}_j(\alpha) = \prod_i \mathrm{wt}_{E_i}(\alpha_i)$. Among its seventeen fields, `J.Reads` says that $i \mapsto w_i$ is a bijection onto $Q(t)$, that the characters $\chi_{j+1}$ of $A$ are those of the package, and that level $m$ has one character. Write $x_j(\alpha)$ for `J.A.xr j (J.ι j α)`.

**Theorem.** There is $C$ with $C_j \neq 0$ for $j < m$ such that, for each $t$ and each $J$ at $t$ with `J.Reads`, there are $s$, $\zeta$, $\rho$ with:

1. each $s_j(\alpha)$ and each $\rho_j$ is a root of unity, and $s_0 = 1$;
2. for $j + 1 \le m$ and characters $\alpha$ at level $j$, $\gamma$ at level $j + 1$, the function $z \mapsto C_j\, \mathrm{wt}_j(\alpha)\, \zeta_j(\alpha, \gamma)\, \xi_j(\alpha, \gamma)(z)$ is a rational datum (`IsRatDatum`, for the idempotent of $A$) for the vector $\mathrm{vac}_j$ and its image under $d_Q^s\, d_G\, d_T$. Here $d_Q^s$ is $s_j(\alpha)\, s_{j+1}(\gamma)^{-1}\, \mathrm{wt}_j(\alpha)$ times the combination of the local operators of the $E_i$;
3. $\zeta_j(\alpha, \gamma)\, \chi_{j+1}(x_j(\alpha))\, \chi_{j+1}(x_{j+1}(\gamma))^{-1} = \rho_j$.

We have not unfolded `IsRatDatum`, the operators or $\xi_j$.

## Proof

1. `true_geometry_row_pair_relation_alt_alt` gives $C$ with $C_j \neq 0$ and $C_j\, \xi^{\mathrm{off}}_j$ a rational datum at each idempotent sum over $v_T(u) \cup v_G$.
2. `true_geometry_twist_quadratic_level_alt` splits the idempotent of $A$ as $e_0 + \sum_i e_i$, with $e_0$ such a sum.
3. `true_geometry_row_pair_property_alt` uses $i_A = 1$. It gives $p_j(\alpha)$, $q_j(\gamma)$ such that $a_j(\alpha) = p_j(\alpha)\chi_{j+1}(x_j(\alpha))$ and $b_j(\gamma) = q_j(\gamma)\chi_{j+1}(x_{j+1}(\gamma))^{-1}$ are roots of unity, $a_0 = c_0$ is a constant root of unity, and $b_j(\gamma)\, a_{j+1}(\gamma) = k_j$ is a constant root of unity for $j + 1 < m$. It also moves a rational datum at $e_0$ to one at $e_0 + \sum_i e_i$, at the cost of a factor $p_j q_j \prod_i \xi^{\mathrm{loc}}_{i}$ and of the local operators of the $E_i$.
4. `true_geometry_twist_quadratic_value_alt` gives $\xi_j = \xi^{\mathrm{off}}_j \prod_i \xi^{\mathrm{loc}}_{i}$.

Now put $\tilde c_j = c_0 \prod_{i < j} k_i$, $s_0 = 1$ and $s_{j+1}(\gamma) = \tilde c_j\, b_j(\gamma)$ for $j < m$ (`chartRescale`). By induction, $s_j(\alpha)\, a_j(\alpha) = \tilde c_j$. Each $s_j(\alpha)$ is a root of unity (`datRoot_mul`, `datRoot_prod`). Put $\zeta_j(\alpha, \gamma) = s_j(\alpha)\, s_{j+1}(\gamma)^{-1}\, p_j(\alpha)\, q_j(\gamma)$ and $\rho = 1$. Then the phase in clause 3 is $s_j(\alpha)\, a_j(\alpha)\, b_j(\gamma) / (\tilde c_j\, b_j(\gamma)) = 1$. For clause 2, multiply the datum of step 1 at $e_0$ by the constant $s_j(\alpha)\, s_{j+1}(\gamma)^{-1}\, \mathrm{wt}_j(\alpha)$ (`isRatDatum_const_mul`), apply the transfer of step 3, and rewrite with steps 2 and 4.

## In the Lean code

The theorem is in [DatExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DatExists.lean#L22). `QuadraticExtensionData`, `Reads` and `Dat` are in [QuadraticExtensionData.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/QuadraticExtensionData.lean#L23).

The proof takes $\rho = 1$, so the statement with $\rho = 1$ also holds. The hypotheses `AllFamilyConditions W`, `a.Is` and `a.True` are only passed to the four lemmas. The helpers `chartRescale` and `datRoot_mul`, and a parallel copy `GlobalTheory.Fam.QJ.dat_exists`, are in [DatExists.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DatExists.lean#L66).
