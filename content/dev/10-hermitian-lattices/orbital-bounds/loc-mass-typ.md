---
id: loc-mass-typ
title: The local mass of congruent pairs of frames at a split place
kind: theorem
decl: locMassTyp
module: Formalism.PeriodIntegrals.OrbitalBoundsConclusion.LocMassTyp
covers: 384
status: drafted
drafted_by: writer@claude
---
This theorem proves `TypLocAt` for all its arguments. `TypLocAt` is a local volume identity at a finite place $v$ of degree one that splits in $E$. It computes the mass of pairs of frame tuples that are congruent modulo the prime $g$ below $v$. It lies below the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/). It is a pass-through. The real content is in `local_mass_type_formula`, which has no entry in the outline.

## Statement

Fix a CM extension $E/F$, standard frames $P, P'$ with Grams $T, T'$, and an $\mathcal O_E$-lattice $\Lambda$ that is self-dual at the finite place $v$. Assume:

- $v$ is unramified, $g$ is prime, $g \in v$ and $N(v) = g$;
- $v$ splits in $E$ (`etaV v = 1`);
- some $\kappa \in K_v$ moves the flag tuple of $P'$ to within $g\Lambda_v$ of the flag tuple of $P$;
- $\mu_G$, $\mu_S$, $\mu_{S'}$ are Haar measures, and $\mu_S$, $\mu_{S'}$ are tied to $\mu_G$ by `LocTieW`;
- both flag tuples are primitive in $\Lambda_v$.

**Theorem.** Let $\Omega$ be the set of pairs of primitive tuples that are congruent modulo $g\Lambda_v$. Then
$$\frac{M_v(T, T'; \Omega)}{\operatorname{vol}(U_g)} = \frac{\mu_G(K_v)\,\mu_G(K^\natural_v)}{\mu_S(S \cap K_v)\,\mu_{S'}(S' \cap K_v)},$$
where $M_v$ is the product of the fibre measures over the two Grams, $U_g$ is the deep congruence set `deepCongruenceVolume`, and $K^\natural_v$ is `Knatv`. We have not unfolded `LocTieW`, `Knatv` or the fibre measures `omAt`.

## Proof

The proof passes two proved inputs to `local_mass_type_of_parts`: `right_invariant_compact` (Haar measure on $G_v$ is right invariant under $K_v$) and `kUnip1_of split_reduction` (built from the splitting $F_v \otimes E \cong F_v \times F_v$).

## In the Lean code

The theorem is in [LocMassTyp.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/LocMassTyp.lean#L7). `TypLocAt` is in [LocVol.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/LocVol.lean#L303), and `OmTyp` at line 103 of that file. The companion `OrdLocAt`, at line 292, is the same kind of identity for the set `OmOrd` of all primitive pairs. `local_mass_type_of_parts` is in [LocalMassTypeOfParts.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalMassType/LocalMassTypeOfParts.lean#L76).
