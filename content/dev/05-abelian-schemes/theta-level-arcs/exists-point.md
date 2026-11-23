---
id: exists-point
title: A moduli point over a power series ring that realises an arc
kind: theorem
decl: GlobalTheory.ArcPoint.exists_point
module: Development.AbelianVarietyTheory.Proofs.DegenerationProofs.ExistsExtendValuation
covers: 480
status: drafted
drafted_by: writer@claude
---
This theorem builds, from an arc $a$ over $O'$, a point of the moduli space over the fraction field of a finite normal extension of $O'[[X]]$. At each point of small absolute value it is the abelian variety that $a$ gives by uniformisation, and its theta null values are integral. It is the first step of [`arcFam`](/entry/arc-fam/), which adds the theta frames.

## Statement

The inputs and the data $E$, $D$, $l$, $X_o$, $c$, $W_0$, $Y$, $O'$, $b$, $\varpi$, $a$ are those of [`arcFam`](/entry/arc-fam/), and $O'$ is a field or a complete discrete valuation ring (`ArcBase`).

**Theorem.** There are a domain $R_1$, a finite injective map $g \colon O'[[X]] \to R_1$ with $R_1$ integrally closed, and a point $y_1 \colon \operatorname{Spec} \operatorname{Frac} R_1 \to X_{o,F}$ over $b$, such that:

1. `RealAt`: let $C$ be a complete, algebraically closed, non-archimedean field over $\operatorname{Frac} O'$ and $\gamma \colon \operatorname{Frac} R_1 \to C$ a map with $|\gamma(R_1)| \le 1$ and $u = \gamma(X)$ of absolute value less than 1. Then the full-level object at $\gamma \circ y_1$ is realised by a lift of $a$ to $C$, with parameter $u$ and a compatible system of roots of $u$ (`Realises`);
2. `ThetaInt`: there is a full-level object at $y_1$ over an algebraic closure of $\operatorname{Frac} R_1$ whose theta null values $v$ at each level $n^j$ ($n$ an odd prime invertible in $O'$, $j \ge 1$) are integral over $R_1$ at each valuation, have a unit among them, and have a unit in each coset of $n^{j-1}$ where $X$ is a unit (`IntFam`).

## Proof

Let $K_0 = \operatorname{Frac} O'[[X]]$ and $K$ an algebraic closure.

1. `T.exists_arcSeries_integral_algebraic_over_powerSeries` gives a series datum $S$ (`Ser`): theta values $v$ and theta coordinates $w$ in $K$, algebraic over $O'[[X]]$, that agree up to a scalar with those of the uniformised variety at each point $\gamma$ as in `RealAt`.
2. `exists_prime_unit` gives an odd prime $n$, invertible in $O'$, not dividing the prime $d$ of the CM datum $H$.
3. `T.exists_object_with_thetaPoint_of_degenerationSeries` gives, for each $j \ge 2$, a full-level object over $K$ with theta values $v(n^j)$. `T.thetaPoints_allPrimePowerLevels_of_single_object` gives one object $o_0$ for all $j$.
4. `T.power_series_algebraic_closure_compatible` gives an object $o$ that matches $S$ at all odd levels.
5. `exists_extend_valuation` extends $V \to K_0$ to the coefficient field $F$. Then `T.fullTorsionObject_existsUnique_moduliPoint` turns $o$ into a point $y \colon \operatorname{Spec} K \to X_{o,F}$.
6. `exists_finite_factor` descends $y$ to a finite extension $L$ of $K_0$. `exists_normal_order` takes $R_1$ to be the integral closure of $O'[[X]]$ in $L$.
7. `RealAt` follows from `realises_of_has` and the uniqueness part of step 5. `ThetaInt` follows from `T.fullTorsionPolarizedCMObject_extends_algClosed` and `intFam_map`.

The rest is bookkeeping with fraction fields and algebraic closures.

## In the Lean code

The theorem is in [ExistsExtendValuation.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsExtendValuation.lean#L180). The same file proves `exists_finite_factor`, `exists_normal_order`, `exists_extend_valuation`, `exists_prime_unit`, `realises_of_has` and `intFam_map`. `RealAt`, `ThetaInt`, `Ser` and `AllA` are in [AdmissibleBaseOfCompleteDvr.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/AdmissibleBaseOfCompleteDvr.lean#L155).

The real work is in step 1 and step 3, whose statements we read but whose proofs we did not open. We have not unfolded `Full`, `Lift`, `Realises`, `FullAt` or `Theta`. Step 2 uses only that $O'$ is local: of two distinct primes larger than $d + 2$, one is a unit in $O'$.
