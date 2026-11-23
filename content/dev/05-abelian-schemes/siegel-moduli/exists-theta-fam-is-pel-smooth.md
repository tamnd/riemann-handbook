---
id: exists-theta-fam-is-pel-smooth
title: A theta family for the PEL class, with smooth generic fibre
kind: theorem
decl: GlobalTheory.ZM.exists_thetaFam_isPEL_smooth
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.ExistsThetaFamilyPelSmoothGenericFibre
covers: 557
status: drafted
drafted_by: writer@claude
---
This theorem builds, for a unitary PEL datum and an odd prime $n$, a family of abelian schemes with theta level structure of level $n^{2j}$, with a PEL structure and a smooth generic fibre. It is the proof of [its statement form](/entry/exists-theta-family-pel-smooth-generic-fibre/), the first step of [`topAmpExists`](/entry/top-amp-exists/). Its dominator in the written proof is the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/).

## Statement

**The objects.** A base of level $N$ (`TBase`) is a ring $o$ in which $N$ is a unit, with a unit $\zeta$ that is a primitive $N$-th root of unity in each field quotient. An object `TObj` over $S \to \operatorname{Spec} o$ is an abelian scheme $A/S$ of relative dimension $g$ with a symmetric, rigidified, relatively ample line bundle, a basis $P_1, \dots, P_{2g}$ of $A[N]$ with Weil pairings $\zeta^{\omega(i,k)}$ for the standard symplectic form $\omega$, and endomorphisms $\alpha_j$, $j \in J$. A theta family for a class $C$ of complex objects (`ThetaFam`) is a reduced, flat, quasi-projective $o$-scheme $M$ with a universal object. Its points are the theta null values that satisfy the polynomial relations of those of $C$. The points from $C$ are dense, $M$ represents reduced families with dense $C$-points, and $M$ is unramified on first-order deformations.

**Theorem.** Assume inputs 2, 3, 8, 9 and 10 of [`topAmpExists`](/entry/top-amp-exists/). Let $E$, $H$ be as there, $D$ a PEL datum of signature $(p, q)$ with $p + q \ge 1$, $(e_i)$ a symplectic basis of its lattice, and $a \colon J \to \mathcal{O}_E$ a finite family of ring generators with $a(w) = w_0$, $a(w') = \bar w_0$. Let $n$ be an odd prime. There is $j_0$ such that for $j \ge j_0$, each base of level $n^{2j}$ over a Dedekind domain $o$ of finite type over $\mathbb{Z}$ with an embedding $o \hookrightarrow \mathbb{C}$ (`ArBase`), and each $\rho \in o$ that maps to the root $\rho_0$ of $-d$, there are a theta family $F$ for `PELClass` (the complex objects with a PEL structure of type $(D, a, (e_i), \rho)$) and a PEL structure $\tau$ on its universal object (`IsPEL`). The generic fibre of $F$ over $o$ is smooth of relative dimension $\dim D = \tfrac{[E:\mathbb{Q}]}{2}\,pq$.

## Proof

1. `T.isGoodThetaComplexClass_unitaryFullLevel` (inputs 2, 3, 9, 10) gives $j_1$ above which `PELClass` is a good class of dimension $\dim D$: closed under isomorphism, of a fixed shape, and covered by finitely many holomorphic families of theta null values on open connected subsets of $\mathbb{C}^{\dim D}$.
2. `T.nonempty_thetaObject_family_open_closure` (inputs 2, 3, 8) gives $j_2$ above which each good class has a theta family. Take $j_0 = \max(j_1, j_2)$.
3. `thetaFam_isPEL` (inputs 2, 3, 9) gives $\tau$.
4. `ThetaFam.smooth_genericFibre` (inputs 2, 3) gives smoothness of relative dimension $\dim D$, if the tangent space at each complex point of each open affine chart $\operatorname{Spec} R \to M$ has dimension at most $\dim D$.
5. For this bound, restrict the universal object and $\tau$ to the chart (`tObj_pull`, `PELPull.isPEL_pull`). $R$ is of finite type over $o$ since $M$ is quasi-projective. The helper `ThetaFam.unram_of_mono` carries the unramified condition to the chart. Then [`T.finrank_tangent_PEL_family_le_symmetricDomain`](/entry/finrank-tangent-pel-family-le-symmetric-domain/) gives $\dim_{\mathbb{C}} \operatorname{Der}_o(R, \mathbb{C}) \le \dim D$.

## In the Lean code

The theorem is in [ExistsThetaFamilyPelSmoothGenericFibre.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsThetaFamilyPelSmoothGenericFibre.lean#L41), with `ThetaFam.unram_of_mono` at [L24](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsThetaFamilyPelSmoothGenericFibre.lean#L24). `TBase`, `TObj`, `GoodClass` and `ThetaFam` are in [GoodClass.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/GoodClass.lean#L96); `IsPEL`, `PELClass` and `ArBase` in [ExistsArBaseAway.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/ExistsArBaseAway.lean#L22). `Datum.dim` uses natural division ([PushInvertible.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/PushInvertible.lean#L24)). We have not unfolded the proofs of steps 1 to 4.
