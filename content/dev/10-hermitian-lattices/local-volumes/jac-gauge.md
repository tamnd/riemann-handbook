---
id: jac-gauge
title: The Jacobian disintegration under the limit instance
kind: theorem
decl: Formalism.L2.SG.Pf.jacGauge
module: Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedLocalOrbits.GaugeLatticeShifts.JacConstFinal
covers: 441
status: drafted
drafted_by: writer@claude
---
This theorem proves `JacGauge`, a disintegration of a gauge measure on a unitary group along a big cell, with an explicit Jacobian constant. It is a pass-through. It reads the limit `RhsWLim` from a `Fact` instance and gives it to [the Jacobian disintegration from the limit on the small group](/entry/jac-gauge-of-rhs-w/), which has the real content. Its only user is [the Jacobian of the double coset decomposition](/entry/jac-gauge-holds/).

## Statement

Use the setting of [the compact form of Theorem P](/entry/actual-compact-theorem/): $n = 2r + k + 1$, the form $H$ and $G = U(H)$. `JacGauge` says: for $k \ge 1$, vectors $z, z'$ in the middle block with $T_z, T_{z'} > 0$, a gauge measure $\mu$ on $G$, Haar measures $\mu_W, \mu_{W'}$ on the subgroups `UWset` of $z, z'$ with total masses $a, a' > 0$, $\kappa > 0$ and a section $\mu_{sec}$, we have

$$\int \varphi\, d\mu = K \int \mathrm{bcWeight}(c, \zeta) \int\int \varphi\big(s\, \mathrm{bigCell}(c, \mu_{sec}(\zeta))\, s'^{-1}\big)\, ds'\, ds$$

with $K = 2^{r+1} V_k^2 / \big((T T')^k V_{k-1}\, a a' \kappa^2\big)$ (`jacConst`). Here $T = T_z$, $T' = T_{z'}$ and $V_j$ is the volume `volU j`. The measure for $s$ is the image of $\mu_W \times \kappa\, \mathrm{haarLie}(N)$ under multiplication, and the same with $\mu_{W'}$ for $s'$.

**Theorem.** If `Fact RhsWLim` holds, then `JacGauge` holds.

## Proof

`WB.rhsWLim'` gets `RhsWLim` from the instance by `Fact.out`. Then `jacGauge_of_rhsW` gives `JacGauge`.

## In the Lean code

The theorem is at [JacConstFinal.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/JacConstFinal.lean#L12), and `WB.rhsWLim'` at line 8. `JacGauge` is in [JacConst.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/JacConst.lean#L60). The instance is proved in [RhsWLimOfLeaves.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RhsWLimOfLeaves.lean#L49), from `rhsWLim` at line 46. That theorem applies `rhsWLim_of_leaves` to seven proved facts on the hyperboloid and on gauge measures of the stabilizers. We have not unfolded these seven facts.
