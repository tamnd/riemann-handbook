---
id: kato-global-unit-law-of-smoothed-classes
title: Zeta classes with Iwasawa data, from Kato's classes and the smoothed Hodge-Tate law
kind: theorem
decl: UpperTheory.V.Z.Kato.Joint.kato_global_unit_law_of_smoothed_classes
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.KatoQuadraticCharacters.FrobeniusHodgeTateLaws.KatoGlobalUnitLawOfSmoothedClasses
covers: 2662
status: drafted
drafted_by: writer@claude
---
This theorem proves the first half of [the zeta element theorem](/entry/zeta-ur/): for an ordinary representation with an unramified source, there are zeta classes with Iwasawa data that satisfy the condition $\mathrm{Pin7}$. Its three hypotheses are filled in by the theorem above it. The proof applies one large lemma, `glue2`, to the three hypotheses and to 19 further proved statements. The work is in `glue2` and in the three inputs.

## Statement

**Theorem.** Assume the following three statements.

1. $\mathrm{KatoEulerSystemIwasawaClassStatement}$. Given an ordinary normal form $W$ with an unramified source $g$, and a modular tower with admissible data, there are classes $Y_r$ on the tower (cocycles for a twist of $W$, norm compatible, continuous and integral), and a class $y$ that is a limit of their specialisations. The class $y$ has derived classes and is linked to the $Y_r$ as in $\mathrm{Sys}$, $\mathrm{IwSys2}$ and $\mathrm{SpLink}$.
2. $\mathrm{SmoothedZetaClassHodgeTateLawStatement}$. Under the same data, the smoothed classes $Y_r - d_0\,Y_r(\cdot\, d_0)$ satisfy a Hodge-Tate law: sums over primitive characters $\psi$ modulo $\ell^m$ of their values are congruent, modulo $\ell^{m - c_0}$, to an explicit term with a Gauss sum, a factor $1 - d_0\psi^{-1}(d_0)$ and a functional $\lambda$.
3. $\mathrm{AdmTop2}$. From a Hecke idempotent with projections and sections on the cohomology of the tower, and a functional with Hecke eigen congruences, one gets an equivariant integral projection to $\overline{\mathbb{Q}}_\ell^2$ with the right Hecke eigenvalues.

Then $\mathrm{ExistsZetaEulerSystemIwasawaData}(\mathrm{Pin7})$ holds.

The conclusion is stated in [the zeta element entry](/entry/zeta-ur/).

## Proof

1. `admissibleHeckeAlgebra_of_generated` weakens $\mathrm{AdmTop2}$ to $\mathrm{AdmTop}$. It only drops the first part of the conclusion (a condition on diamond operators).
2. [`kato_global_admissibility_of_admissible`](/entry/kato-global-admissibility-of-admissible/) turns $\mathrm{AdmTop}$ into $\mathrm{AdmFR}$, a projection from the tower to the newform part with an admissible functional.
3. `glue2` proves the conclusion from these and from 19 proved inputs. In order: it picks a tower, a Dirichlet character and an Eisenstein eigensystem; $\mathrm{AdmFR}$ gives the projection and the functional; statement 1 gives the classes $Y_r$ and $y$; statement 2, with $d_0 = \ell + 1$, gives the Hodge-Tate law; then it shows that the Frobenius unit $\nu$ is trivial on inertia with $|\nu(\mathrm{Frob})| = 1$, proves a non-vanishing of a smoothed sum, and assembles $\mathrm{Pin7}$.

## In the Lean code

The theorem is in [KatoGlobalUnitLawOfSmoothedClasses.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/KatoGlobalUnitLawOfSmoothedClasses.lean#L8). The three hypotheses and $\mathrm{Glue2}$ are in [SmoothedZetaClassHodgeTateLawStatement.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/SmoothedZetaClassHodgeTateLawStatement.lean#L11). The proof is one application of `glue2`.

- `glue2` and `admissibleHeckeAlgebra_of_generated`, in [AdmissibleHeckeAlgebraOfGenerated.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/AdmissibleHeckeAlgebraOfGenerated.lean#L17). `glue2` is a tactic proof of about 210 lines.
- `kato_global_admissibility_of_admissible`.
- The proved inputs: `towerEx`, `ordinaryEisensteinEigenfunctional_exists`, `meas3`, `jEx`, `coefUb`, `mono`, `psiEx`, `frobU`, `detIne`, `hatW`, `pinOf`, `smNz`, `gmEx`, `explSmul`, `avgEq`, `avgMF`, `rhsEq`, `smSys`, `chiFix`. We have not opened them.

The hypothesis $\mathrm{AdmTop2}$ is stronger than what the proof uses: only its weakening $\mathrm{AdmTop}$ reaches `glue2`. The name says "unit law", but the conclusion is the existence of classes with Iwasawa data. A unit appears only inside $\mathrm{Pin7}$, as the condition $|\nu(\mathrm{Frob})| = 1$.
