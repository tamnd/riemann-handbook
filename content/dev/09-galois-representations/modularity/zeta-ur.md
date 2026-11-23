---
id: zeta-ur
title: An Euler system class for an ordinary representation with an unramified source
kind: theorem
decl: UpperTheory.V.Z.Kato.Final.zetaUr
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.KatoQuadraticCharacters.UnramifiedZeta.ZetaUr
covers: 8219
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{ZetaUr}$: an ordinary two-dimensional representation with an unramified modular source has an Euler system class that is not of Greenberg type at $\ell$. [The vanishing theorem for two twists](/entry/two-s/) uses it, through `vanishOrdL_of_zetaUr`, to make Bloch-Kato Selmer groups vanish. The names of its parts refer to Kato's zeta elements. The proof is one line that joins two halves: the existence of the classes with Iwasawa data, and a non-vanishing statement.

## Statement

Let $\ell$ be a prime, $e \ge 1$, $S$ a finite set of places, $A$ a valuation ring of $\overline{\mathbb{Q}}$ above $\ell$ (a choice of place), and $W \colon G_\mathbb{Q} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$.

$\mathrm{Nf}(e, S, A, W)$ is an ordinary normal form: $\ell$ is odd; $W$ is continuous, integral, unramified outside $S \supseteq \{\ell\}$, odd, with $\det^2 = 1$ and irreducible on a subgroup; $W$ is upper triangular on the decomposition group at $A$, its top left entry has some power equal to a power of $\bar\chi^{e}$ on inertia, and on the decomposition group the top left entry is not always $\bar\chi$. Here $\bar\chi$ is the [[cyclotomic character|XSGB5K2KEG]].

$\mathrm{SrcUr}(\iota, e, A, W, g)$ says: $g$ is a newform of weight $2e+1$ and level prime to $\ell$, with $|a_\ell(g)| = 1$, attached to $W \otimes \bar\chi^{-e}(\det W)^{-1}\chi$ for some $\chi$ trivial on $\mu_\ell$, and $W_{11}\,\bar\chi^{e}(\det W)^{-1}\chi = 1$ on inertia at $A$.

$\mathrm{ES}(W, A)$ says: there is an integral cocycle $y$ that is unramified away from $\ell$, that fails the Greenberg condition at $A$, and that has derived classes at all primes $w \notin S'$ with $\ell^n \mid Nw - 1$, for all $n \ge 1$. This has the shape of a Kolyvagin system.

**Theorem.** For all such data, $\mathrm{Nf}(e, S, A, W)$ and $\mathrm{SrcUr}(\iota, e, A, W, g)$ imply $\mathrm{ES}(W, A)$.

## Proof

`zetaUr_of_halves2` reduces $\mathrm{ZetaUr}$ to two statements with the same predicate $\mathrm{Pin7}$:

1. $\mathrm{ExistsZetaEulerSystemIwasawaData}(\mathrm{Pin7})$: there are a class $y$ with derived classes ($\mathrm{Sys}$), a norm compatible system $Z_r$ of classes along the cyclotomic tower ($\mathrm{IwSys2}$, in the sense of [[Iwasawa theory|Y2SPPSQ5D4]]), a link that makes $y$ a limit of twisted sums of the $Z_r$ ($\mathrm{SpLink}$), and the long condition $\mathrm{Pin7}$ on a Frobenius unit, a power series and a Hodge-Tate law. [`kato_global_unit_law_of_smoothed_classes`](/entry/kato-global-unit-law-of-smoothed-classes/) proves it. Its inputs are [`kato_eulerSystem_integrality`](/entry/kato-euler-system-integrality/), [`smoothedZetaClass_hodgeTateLaw`](/entry/smoothed-zeta-class-hodge-tate-law/) and `exists_admissible_hecke_projection_nonvanishing`.
2. $\mathrm{ZetaEulerSystemNonvanishing}(\mathrm{Pin7})$: for any such data, $y$ is not zero at a point $s$ of inertia with $\bar\chi(s) = 1$ and $W_{11}(s) = 1$ ($\mathrm{NzAt}$). `UpperTheory.Kd.C7.pLocu` proves it.

Then `es_of_sys` turns $\mathrm{Sys}$ and $\mathrm{NzAt}$ into $\mathrm{ES}$: the non-vanishing at $s$ shows that $y$ fails the Greenberg condition (`not_gr_of_nzAt`).

## In the Lean code

The theorem is in [ZetaUr.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/UnramifiedZeta/ZetaUr.lean#L9). The statement is in [ZetaUr.lean](lean:Development/AbelianVarietyTheory/Statements/CuspidalUnitaryTwists/ZetaUr.lean#L18) under Statements, and $\mathrm{Nf}$ and $\mathrm{ES}$ are in [FinalTheorems.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/FinalTheorems.lean#L53).

- `GlobalTheory.KZ.zetaUr_of_halves2`, in [ZetaElementsUnramifiedOrdinaryOfEulerSystemInert.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ZetaElementsUnramifiedOrdinaryOfEulerSystemInert.lean#L43).
- `kato_global_unit_law_of_smoothed_classes`.
- `UpperTheory.Kd.K4.kato_eulerSystem_integrality` and `UpperTheory.V.Z.Kato.K5.smoothedZetaClass_hodgeTateLaw`. Each one is equal to a theorem named `top`.
- `GlobalTheory.T.exists_admissible_hecke_projection_nonvanishing`.
- `UpperTheory.Kd.C7.pLocu`, in [NormFactorLeOne.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/NormFactorLeOne.lean#L162).
- $\mathrm{Sys}$, $\mathrm{NzAt}$, $\mathrm{SpLink}$ and `es_of_sys` in [IsLocallyConstantCycMod.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/IsLocallyConstantCycMod.lean#L13).

We have not unfolded the derived classes (`Tame`) in full. The reading of $\mathrm{ES}$ as a Kolyvagin system follows its visible shape. The predicate $\mathrm{Pin7}$ is inferred by Lean from the first half; the code writes `_` for it.
