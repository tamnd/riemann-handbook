---
id: jac-gauge-holds
title: The Jacobian of the double coset decomposition, second name
kind: theorem
decl: Formalism.L2.SG.Closed.JacGauge_holds
module: Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedVolumeStatements.RealBracketHolds
covers: 442
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`jacGauge`](/entry/jac-gauge/). It proves `JacGauge`, an integration formula for a real unitary group, under the instance `RhsWLim`. It is the first input of [`RealBracket_holds`](/entry/real-bracket-holds/). The content is in [`jacGauge_of_rhsW`](/entry/jac-gauge-of-rhs-w/).

## Statement

Let $k \ge 1$ and $G = U(H)$ on $\mathbb C^{2r+k+1}$, with $r$ hyperbolic pairs and the middle block $\operatorname{diag}(1, \dots, 1, -1)$. Let $z, z'$ be vectors in the middle block with $T = -H(z,z) > 0$ and $T' = -H(z',z') > 0$, and let $W$, $W'$ be their stabilizers that also fix the hyperbolic pairs.

**Theorem.** Assume `RhsWLim`. Let $\mu$ be the Haar measure of $G$ with density $1$ at the identity, $\mu_W$, $\mu_{W'}$ of mass $a, a' > 0$, and $\kappa > 0$ the scale of the Haar measure of a unipotent $N$. Then $\mu$ disintegrates over $(WN) \backslash G / (W'N)$, parametrized by a big cell $b(c, m(\zeta))$ with $c \in \mathbb C^r$, $\zeta \in \mathbb C$, with weight $\prod_{a<r} \lvert c_a \rvert^{2(2(r-a)+k-1)} (\lvert \zeta \rvert^2 - TT')^{k-1}$ on $\lvert \zeta \rvert^2 \ge TT'$ and the constant
$$K = \frac{2^{r+1} V_k^2}{(T T')^k\, V_{k-1}\, a\, a'\, \kappa^2}.$$
Here $V_k$ is as in [`AprimeInf_holds`](/entry/aprime-inf-holds/).

## Proof

`JacGauge_holds` is `jacGauge`, and `jacGauge` is `jacGauge_of_rhsW` applied to the instance `RhsWLim`.

## In the Lean code

The theorem is in [RealBracketHolds.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/RealBracketHolds.lean#L16). `JacGauge` is in [JacConst.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/JacConst.lean#L60) and `RhsWLim` in [JacConstWbB.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/JacConstWbB.lean#L59). Its instance is declared in the Development file [RhsWLimOfLeaves.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RhsWLimOfLeaves.lean#L49). We have not unfolded the measures `muS` and `haarLie` on $WN$ and $N$.
