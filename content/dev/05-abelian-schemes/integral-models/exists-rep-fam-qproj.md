---
id: exists-rep-fam-qproj
title: The Harris-Taylor moduli problem has a quasi-projective representing family
kind: theorem
decl: GlobalTheory.UPel.HT.exists_repFam_qproj
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsQuasiProjectiveHarrisTaylorFamily
covers: 2131
status: drafted
drafted_by: writer@claude
---
This theorem proves that the moduli problem of [the integral model entry](/entry/model-nonempty/) is represented by a scheme that is quasi-projective over the base. It does so by a reduction to a Siegel moduli problem with an auxiliary level. [Its statement form](/entry/exists-quasi-projective-harris-taylor-family/) repeats it, and the integral model entry then adds smoothness.

## Statement

Use the datum $D$ for a prime $p$, with order $O$, lattice $\Lambda$ and form $E$, the base $b$ over $R$, and the objects of level $N$ from the integral model entry.

**Theorem.** Let $R$ be noetherian and $b$ a base over $R$. If $N \geq 3$ and $\gcd(N, p) = 1$, then there is a scheme $X$, quasi-projective over $R$, with an object $u$ of level $N$ over $X$, such that each object over a scheme $S$ is the pullback of $u$ along a unique map $S \to X$.

## Proof

1. The datum gives $e \in \mathbb{N}$ prime to $p$ with $e\Lambda^\vee \subseteq E(\Lambda)$. Then $e > 0$, since $\gcd(0, p) = p \neq 1$.
2. Take a prime $M \geq p + e + 3$. Then $M \geq 3$, $M$ is odd, and $M$ is prime to $p$ and to $e$.
3. $\operatorname{rank}\Lambda \geq 2$ (`Datum.two_le_finrank_La`): the rank is $mn[F:\mathbb{Q}] \geq 1$, and an alternating form on a lattice of rank 1 is zero, so it is not nondegenerate. So $h = \lfloor \operatorname{rank}\Lambda / 2 \rfloor \geq 1$.
4. [The Siegel representability](/entry/siegel-kernel-bounded-representable-of-coprime/) for $(h, M, e)$ gives a quasi-projective scheme over $\mathbb{Z}[\zeta_M, 1/M]$ that represents abelian schemes with a symmetric rigidified line bundle, polarization kernel killed by $e$, and a symplectic level $M$ structure of genus $h$, over bases on which $e$ is a unit.
5. `GlobalTheory.T.harrisTaylor_auxiliary_symplectic_level_representable` turns this into a quasi-projective scheme that represents the objects of level $N$ together with a symplectic level $M$ structure of genus $h$ on $A$.
6. `GlobalTheory.T.exists_representingFamily_of_auxiliaryRepresentation` removes the auxiliary level and gives the quasi-projective representing family.

## In the Lean code

The theorem is in [ExistsQuasiProjectiveHarrisTaylorFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsQuasiProjectiveHarrisTaylorFamily.lean#L13). The lemmas it calls:

- `Datum.two_le_finrank_La` and `SDRep`, in [TwoLeFinrankLa.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwoLeFinrankLa.lean#L48).
- `GlobalTheory.T.siegelKernelBoundedRepresentable_of_coprime`.
- `GlobalTheory.T.harrisTaylor_auxiliary_symplectic_level_representable`, an alias of `harrisTaylorModuli_symplecticLevel_representable`, whose proof we have not opened.
- `GlobalTheory.T.exists_representingFamily_of_auxiliaryRepresentation`, an alias of `GlobalTheory.HTQuot.exists_representing_family_of_level_structure`, whose proof we have not opened. The name of its module suggests a quotient by the level $M$ group; we have not checked this.

The prime $M$ is used only for the three properties in step 2; any odd $M \geq 3$ prime to $pe$ would do. The genus is the natural number `Module.finrank ℤ D.La / 2`, which floors.
