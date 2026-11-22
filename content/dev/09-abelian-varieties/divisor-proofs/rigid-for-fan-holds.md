---
id: rigid-for-fan-holds
title: Rigid boundary charts for a fan
kind: theorem
decl: GlobalTheory.RigChart.rigidForFan_holds
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.RigidBoundaryChartsForFanUnitaryDatum
covers: 2769
status: drafted
drafted_by: writer@claude
---
This theorem proves `RigidForFan`: smooth projective compactifications of the unitary moduli schemes, with rigid charts at the boundary. Through [a citation](/entry/rigid-boundary-charts-for-fan-unitary-datum/), it goes to [the toroidal compactification theorem](/entry/toroidal-for-fan-ks/). Below it are 2,769 declarations.

## Statement

- $E$ is a CM field with a host $H$ (`Host`), with a prime $d \equiv 7 \pmod{16}$.
- $D$ is a projective $\mathcal{O}_E$-module of rank $p + q \geq 1$, with a unimodular alternating form such that $\langle a x, y \rangle = \langle x, \bar a y \rangle$, of signature $(p, q)$.
- $\varphi$ is a function on real forms on the modules $\mathcal{O}_E^r$ that does not change under surjections (`InvFun`). It satisfies `IsPolFan` and `NoSelfInt` in rank at most $\min(p, q)$.
- $X$ is `Moduli D l` for a level $l$, $F \subset \mathbb{C}$ is a coefficient field, and $n = \tfrac{[E:\mathbb{Q}]}{2}\, p q$.
- A model of $X_F$ (`Model`) is a normal flat projective $F$-scheme with a dense open immersion of $X_F$. It carries a semi-abelian scheme that extends the universal object and is abelian exactly over $X_F$.

**Theorem.** There are a model $Y$, an effective Cartier divisor $B$ on $Y$ and integers $d, k \geq 1$ with:

1. $Y$ is smooth of relative dimension $n$, and its boundary is a strict normal crossings divisor;
2. the support of $B$ lies in the boundary;
3. each boundary point $x$ has a fan chart (`HasChartOf`);
4. if $\omega_Y$ is a line bundle, then $\omega_Y^{k}(-B)$ is ample;
5. each closed boundary point $x$ has a rigid chart (`HasRigidChart`).

Each chart is a map $\xi \colon \operatorname{Spec} k'[[t_1, \dots, t_m, u_1, \dots, u_e]] \to Y$ that sends the closed point to $x$. The map of local rings is flat, generates the maximal ideal and gives a finite residue extension. The boundary pulls back to $(t_1 \cdots t_m)$. The degeneration data are monomial in the $t_i$, with forms $\gamma_i$.

- In a fan chart, $\gamma_i = M'\delta_i$ for a cone $(\delta_i)$ of $\varphi$, and $B$ pulls back to $\prod t_i^{d\varphi(\gamma_i)}$.
- In a rigid chart, the $\gamma_i$ are part of a basis, and `IsRigid` holds. Let $\rho$ be a map to dual numbers $k''[\varepsilon]$ that kills each $t_i$ and sends the maximal ideal into $\varepsilon k''$. Suppose that $\rho$ pulls back the degeneration data to the same data as its constant part $\rho_0$, up to units $1 + \varepsilon \sum_i a_i \gamma_i$ (`IsConstAlong`). Then $\rho = \rho_0$.

## Proof

The proof composes two theorems.

1. [The separation statement](/entry/unitary-toroidal-separation-of-base/) proves `UStB`, a normalized blowup with a separation property.
2. [Rigid charts from separation](/entry/rigid-boundary-charts-for-fan-of-unitary-separation/) proves `UStB → RigidForFan`.

## In the Lean code

The theorem is in [RigidBoundaryChartsForFanUnitaryDatum.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RigidBoundaryChartsForFanUnitaryDatum.lean#L19). Its proof is one line.

The statement is in [RigidForFan.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RigidForFan.lean#L70). `HasChartOf` is in [ToroidalChartsForFan.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ToroidalChartsForFan.lean#L17). We have not unfolded `IsMonomial`.

[HasRigidChart.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasRigidChart.lean#L67) has a different `RigidForFan`, in `GlobalTheory.LogKSChart`. Its rigidity uses `IsUnitPart`, not `IsUnitTau`.
