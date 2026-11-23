---
id: jac-gauge-of-rhs-w
title: The Jacobian disintegration from the limit on the small group
kind: theorem
decl: Formalism.L2.SG.Pf.jacGauge_of_rhsW
module: Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedLocalOrbits.GaugeLatticeShifts.BruhatHaarProved
covers: 430
status: drafted
drafted_by: writer@claude
---
This theorem proves `JacGauge` from one hypothesis, `RhsWLim`, a limit of ball volumes on a small unitary group. Its only user is [the Jacobian disintegration under the limit instance](/entry/jac-gauge/), which states `JacGauge` and gets `RhsWLim` from an instance. The proof here is one line, but the chain below it does the work: two integration formulas and a constant identity.

## Statement

Let $U_b$ be the group `UWb` of elements that fix all $e_a$ and $e^*_a$, let $v(\rho)$ be the volume of the ball of radius $\rho$ in its Lie algebra, and let $B_\rho$ be the image of that ball under $\exp$. Fix data `WbData`: $z, z'$ in the middle block, Haar measures $\mu_W, \mu_{W'}$ of masses $a, a'$ and a section $\mu_{sec}$. Let $m_0 = \mathrm{embWb}(\mu_{sec}(2\sqrt{T T'}))$. `RhsWLim` says

$$\frac{\mathrm{rhsW}(\mathbf 1_{m_0 B_\rho})}{v(\rho)} \to \mathrm{wbConst}^{-1} \quad (\rho \to 0^+),$$

where $\mathrm{rhsW}(\varphi) = \int \mathrm{zWeight}(\zeta) \int\int \varphi(h\, \mathrm{embWb}(\mu_{sec}(\zeta))\, h'^{-1})\, d\mu_{W'}\, d\mu_W$ and $\mathrm{wbConst} = 2V_k^2 / ((T T')^k V_{k-1}\, a a')$.

**Theorem.** `RhsWLim` implies `JacGauge`.

## Proof

1. `BH.sandwich'` proves `Sandwich`: for small $\rho$, the ball condition on $w_0\, n\, \mathrm{bigCell}(c, 1)\, m\, n'^{-1}$ lies between two conditions $Q_f < ((1 \pm \varepsilon)\rho)^2$ on a quadratic form.
2. `VL.volLim` proves `VolLim`: the volume of $\{Q_f < s^2\}$, divided by the gauge volume, tends to $2^{-r}$.
3. `existsGaugeNormalizedStabilizer` gives a gauge measure on $U_b$ for each rank.
4. From these, `JacConstAll.lean` derives three facts. `BruhatHaar` writes a gauge measure on $U(H)$ as $2^r$ times an integral of $\varphi(n\, \mathrm{bigCell}(c, 1)\, m\, n'^{-1})$ over $n, n' \in N$, $m \in U_b$ and $c$, with weight `cWeight`. `WbHaar` writes a gauge measure on $U_b$ as $\mathrm{wbConst} \cdot \mathrm{rhsW}$. `GaugeExists` gives gauge measures on $U(H)$ and on $U_b$.
5. `Jac.jacGauge_of` puts `WbHaar` inside `BruhatHaar`. It uses $\mathrm{bcWeight} = \mathrm{cWeight} \cdot \mathrm{zWeight}$ and $2^r \cdot \mathrm{wbConst} = \mathrm{jacConst} \cdot \kappa^2$.

## In the Lean code

The theorem is at [BruhatHaarProved.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/BruhatHaarProved.lean#L9). `RhsWLim` is in [JacConstWbB.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/JacConstWbB.lean#L59). `Sandwich` and `VolLim` are in [JacConstBHR.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/JacConstBHR.lean#L25). The final step is in [JacConstPf.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/JacConstPf.lean#L356). The path goes through `jacGauge_of_sandwich_rhsWLim`, `jacGauge_of_hearts3` and `jacGauge_of_sandwich_gaugeMeasure`. Each only adds a proved input. We have not unfolded `rhsHaar`, `rhsWHaar`, `gaugeShift` or `gaugeShiftW`.
