---
id: exists-deg-data-unif
title: Degeneration data and a uniformisation for a semi-abelian degeneration
kind: theorem
decl: GlobalTheory.UU.exists_degData_unif
module: Development.AbelianVarietyTheory.Proofs.UniformizationProofs.ExistsDegenerationDataUniformisationOfTorsionCou
covers: 822
status: drafted
drafted_by: writer@claude
---
This theorem gives degeneration data and a uniformisation for a semi-abelian scheme over a complete discrete valuation ring whose generic fibre is a polarized abelian variety. The [statement entry](/entry/exists-degeneration-data-uniformisation-of-torsion-count/) is a second name for it. This theorem is an assembly of three lemmas.

## Statement

There are three hypotheses. The first is the torsion count: an abelian variety of dimension $g$ over an algebraically closed field has exactly $n^{2g}$ points of order dividing $n$ when $n$ is invertible (Mumford, *Abelian Varieties*, §4, Application 2). The second is `Laws`, a structure of 24 facts about abelian schemes (cube, square, rigidity, Weil pairing, ampleness, quotients and others). The third is `Laws2`, four more facts.

Let $V$ be a complete discrete valuation ring of characteristic $0$ with maximal ideal $\mathfrak m$ and fraction field $K$. Let $A$ be a polarized abelian variety over $K$ and $G$ a commutative group scheme over $V$. A setting $s$ (the structure `HidaSetting`) gives: $G$ semi-abelian, an isomorphism $G_K \cong A$, a rigidified symmetric line bundle $L$ on $G$ with a cubical structure, a lattice $X$, and a torus extension with character group $X$ on the special fibre.

**Theorem.** Under the three hypotheses, for each such $s$ there are degeneration data $D$ over $(V, \mathfrak m)$ and a uniformisation $U$ of $G$ by $D$, with the line bundle, the isomorphism and the cubical structure of $s$.

The data $D$ (`DegData`) are an abelian scheme over $V$ with a cubical line bundle, a map $c \colon X \to B(V)$, and trivializations $\psi(\chi)$ over $K$. The conditions are: $\psi$ is even, the pairing $\tau$ made from $\psi$ is bimultiplicative, $\psi(\chi) \in \mathfrak m$ for $\chi \neq 0$, and $\psi(\chi) \to 0$ $\mathfrak m$-adically. The uniformisation `Unif` asks that, for every $k \geq 1$, Fourier expansion along $X$ is a bijection from sections of $L^k$ over $K$ to families of coefficients. The shape is that of Mumford (Compositio Math. 24, 1972) and Faltings-Chai (*Degeneration of Abelian Varieties*, 1990, Chapters II and III). We have not checked that the Lean conditions match theirs.

## Proof

1. `exists_uniformisation_data_before_choice` uses the torsion count and `Laws`. It gives pre-data and a pre-uniformisation with the data of $s$.
2. `exists_degenerationData_functionalEquation_degree_one` uses `Laws` and `Laws2`. It gives a pre-uniformisation over true degeneration data that satisfies the functional equation in degree $1$.
3. `unif_assembly` calls `exists_uniformisation_of_functionalEquation_degreeOne`, which makes a `Unif` that matches it, and passes the three equalities along.

## In the Lean code

The theorem is at [ExistsDegenerationDataUniformisationOfTorsionCou.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsDegenerationDataUniformisationOfTorsionCou.lean#L21). The assembly is [UnifAssembly.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/UnifAssembly.lean#L20). `HidaSetting` is in [IsCPPullback.lean](lean:Development/AbelianVarietyTheory/Definitions/Uniformization/IsCPPullback.lean#L35), `DegData` in [ThickTransComp.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/ThickTransComp.lean#L109), and `Unif` in [DegExp.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/DegExp.lean#L140).

The hypotheses are not open: `exists_degData_unif_unconditional` in [ExistsDegenerationDataUniformisationUnconditiona.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsDegenerationDataUniformisationUnconditiona.lean#L22) proves all three. The name `HidaSetting` is misleading, since nothing in the structure is about Hida theory.
