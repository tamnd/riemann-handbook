---
id: core-holds
title: The cotangent length bound in normal form
kind: theorem
decl: UpperTheory.V.Alg.M.core_holds
module: Development.AutomorphicArithmetic.AutomorphicVarieties.CommutativeAlgebra.GradedModulesLength.AlgMemCoef
covers: 487
status: drafted
drafted_by: writer@claude
---
This theorem is the main step of [the length bound for graded algebras](/entry/main-holds/). The parent puts the equations in a normal form and finds a chart. This theorem then proves the bound $\sum c_i \le 2 \sum_{\xi \in T} v(\xi(a))$. It does so by an Euler characteristic count on a Rees-type algebra, with a lower bound and an upper bound for large degree.

## Statement

Use the notation of the [parent entry](/entry/main-holds/): the graded algebra $A$ over $\mathcal{O}$ with augmentation $x$, the equations $F_0, \dots, F_r$, $G_i$, $E_i$, $E'_i$, $Z_i$ with ideal $I$, the set $\mathfrak{s}$, the field $K$ with valuation $v$, and the conditions $M_2$ to $M_5$. Suppose also:

1. $\varphi$ is a chart of $A$ in power series over the fraction field of $\mathcal{O}$ (`IsChart0`): it respects the weights, its constant terms are given by $x$, and each variable is hit by a linear term. It has $r$, $s$, $r'+1$ and $s'+1$ variables of weights $-1$, $-2$, $1$, $2$, and none of weight $0$. Also $\varphi(Z_i) = 0$ and $r \ge 1$;
2. $\varpi$ is a uniformizer, $y_i \in A_{-1}$ and $F_i - \varpi^{c_i} y_i \in \mathfrak{s}$ for $i < r$, and $F_r \in \mathfrak{s}$;
3. the $F_i$ and the $G_i$ span the weight $-1$ and $-2$ parts of the cotangent lattice up to nonzero scalars;
4. $\varphi(a) \ne 0$, and $T$ is a covering set of two-signed points.

**Theorem.** $\sum_{i < r} c_i \le 2 \sum_{\xi \in T} v(\xi(a))$.

## Proof

1. `fg_holds` shows that three $A_0$-submodules of $A$ are finitely generated: (roughly) the weight $-2$ part, the weight $2$ part, and the span of $F_r^2$ with the triple products of weights $-2, -2, 2$ (`mN`). From them the proof builds a Rees-type algebra $R$, graded by $\mathbb{Z}^3$. It is a subalgebra of polynomials in three variables over $A$. `std_holds` gives the standard conditions on this grading.
2. Let $J$ be the ideal of elements of $R$ whose coefficients lie in $\ker \varphi$. The $Z_i$ lie in $J$ (`alg_mem_coef`). `admissibility_holds` shows that a list of homogeneous sections (squares of the $F_i$, the $G_i$, squares of the $E_i$, the $E'_i$ and $F_r^2$), followed by $a$, is admissible for $J$. Since $\varphi(a) \ne 0$ and power series over a field have no zero divisors, $a$ is a nonzerodivisor modulo $J$.
3. For a $\mathbb{Z}^3$-graded module $M$, a list of homogeneous elements and a degree $d$, `chi` is defined by recursion: for the empty list it is the length of $M_d$, and for a list $(s, t_2, \dots)$ it is $\chi(t_2, \dots; M/sM) - \chi(t_2, \dots; \operatorname{ann}_M(s))$, with a shift of grading. For all large $d$:
   - `low_holds`: $2^{r+r'} \sum c_i \le \chi(\text{sections}, (R/J)/a)$;
   - the private lemma `chain`: this is at most $\chi(a, R/(J + \text{sections}))$;
   - `up_holds`: this is at most $2^{r+1+r'} \sum_{\xi \in T} v(\xi(a))$.
4. Pick one $d$ for which all three hold, and divide by $2^{r+r'}$.

We have not unfolded `admitted` or `std_holds`.

## In the Lean code

The theorem is in [AlgMemCoef.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/AlgMemCoef.lean#L92). `low_holds` is in [AdmissibleMonoIdeal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/AdmissibleMonoIdeal.lean#L191), `up_holds` in [TwoSigned.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/TwoSigned.lean#L17), and the Rees algebra (`rees`, `coefIdeal`, `mN`, `ts`) in [ToDegInjective.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/ToDegInjective.lean#L24). `chi` and the structure `HidaSetting` are in [EulerVanishingBelowDimension.lean](lean:Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/EulerVanishingBelowDimension.lean#L66).

The structure that holds the Rees algebra is called `HidaSetting`. It is not the Hida setting of the Galois side: here it is a graded algebra over a local ring.
