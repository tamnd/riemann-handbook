---
id: holomorphic-arc-main
title: Each formal arc at the boundary has a holomorphic arc
kind: theorem
decl: GlobalTheory.HolomorphicArc.main
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.HolomorphicDegenerationArcOfUniformisation
covers: 717
status: drafted
drafted_by: writer@claude
---
This theorem proves the toroidal archimedean condition from the laws of abelian schemes and the analytic uniformisation. It says that a formal arc into a compactified model is the expansion of an analytic family on a half plane. It is the real content of [its second name](/entry/holomorphic-degeneration-arc-of-uniformisation/) and of [`arcClause_closed`](/entry/arc-clause-closed/).

## Statement

**Theorem.** Assume `Out.Laws`, `Out.Laws2` and `ThetaUnifAV`. Then `ToroidalArchimedeanCondition` holds. That is, take:

- a CM field $E$ with host data $H$, a datum $D$ (a finite projective $\mathcal{O}_E$-module with a unimodular alternating form), a level $l$ and a fine moduli scheme $X_o$;
- a model $Y$ over a ring $O$ with a dense open immersion $j$ of the moduli space and a semi-abelian scheme;
- a ring map $b_F \colon F \to \mathbb{C}$, arc data $a$, a formal arc $\chi \colon \operatorname{Spec}\mathbb{C}[[X]] \to Y$ with a witness $W$, and a family uniformisation $F_u$ of type $ty$.

Assume that $b_F$ sends a fixed element to $H.\mathrm{rt0}$, that $ty$ is a type function for the signature of $D$, that $O$ holds lifts of $H.\mathrm{rt0}$ and of a root of unity of order $l.A$, that $\chi$ lies over $b_F$, and that each point of $\chi$ off $X = 0$ is in the image of $j$. Then a `HolArc` exists. Its main fields are:

- an index $i$, a bound $T$ and maps $P_w = P_0 + wN$ from the lattice to $\mathbb{C}^g$, with $P_w$ a period map for $\operatorname{Im} w > T$;
- a surjective additive map $z \mapsto ex_0(z)$ from $\mathbb{C}^g$ to points of a degeneration, holomorphic, $\mathcal{O}_E$-linear for $ty$, and zero exactly at the $P_0(v)$ with $y(v) = 0$;
- `shift`: $ex_0(wN v)$ is the torus point with coordinates $e^{2\pi i w b(y v, x)}$;
- `levelA`, `levelM`: level structures at the points $l^{-1}P_0(v)$;
- `point`: for each function $f$ regular along $\chi$, the power series of $f$ along $\chi$ converges at $w$ for large $\operatorname{Im} w$ to the value of $f$ at the point $u_i(P_w)$ of the family;
- `riemann`, `diff` and `theta`, conditions on the form, on first order deformations and on theta values. We have not unfolded these.

## Proof

The proof calls one lemma per step. We list them and have not unfolded them.

1. `ArcModel.nonempty_gtAn` gives a value $\Lambda$ of a type `GtAn` for the arc data $a$. This is the only use of `ThetaUnifAV`.
2. `T.nonempty_chain_arc_witness_universal_family` gives a chain $C$ from $\Lambda$, $\chi$ and the universal family.
3. `GtRep.exists_rep_and_shift` picks lattice representatives of the level points for $l.A$ and $l.M$. `ArcPts.chain_levels` gives level facts for $C$.
4. `ArcThetaSpaces.sections_theta` gives finiteness. `ConstRational.rational` proves `C.Φ.Rational`.
5. `T.exists_germs_localRing_convergent_divisible` gives rings of convergent Laurent germs. `ArcPts.Special.specPts_nonempty` gives points $\Psi$ with a map $w \mapsto \Psi(w)$.
6. `ArcPts.exists_isFactor` gives the linear part. `SpecFibre.specPts_isFibAt` gives $T_1$ such that $\Psi$ is holomorphic and satisfies `IsFibAt` for $\operatorname{Im} w > T_1$. `SpecLevel.level_on_fibre` gives the same for the two levels.
7. `ArcPts.finrank_V_eq` fixes the dimension. `isHolTo_halfPlane_mono` shrinks the half plane to $\operatorname{Im} w > \max(T_1, T_A, T_M)$.
8. `ArcPts.exists_cmp` gives a comparison $K$ between $\Psi$ and the family $F_u$. `ArcPts.nonempty_holArc` assembles the `HolArc`.

## In the Lean code

The theorem is at [HolomorphicDegenerationArcOfUniformisation.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/HolomorphicDegenerationArcOfUniformisation.lean#L29). The condition `ToroidalArchimedeanCondition` and the structure `HolArc` are in [HasArcDataIff.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/HasArcDataIff.lean#L109).

The `intro` line names the hypothesis $b_F(\rho) = H.\mathrm{rt0}$ with `_`, and no later line uses it. The callers still supply it. `Out.Laws` and `Out.Laws2` are passed to almost every step.
