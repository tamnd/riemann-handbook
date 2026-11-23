---
id: xi-exists-of-in
title: A majorant for matrix coefficient integrals, from the Heisenberg inputs
kind: theorem
decl: ReciprocityTheory.ChartRestriction.DS.Xi.xiExists_of_in
module: ReciprocityTheory.ReductiveGroups.DiscreteSeries.TailIntegrals.XiExistsOfIn
covers: 941
status: drafted
drafted_by: writer@claude
---
This theorem proves `XiExists` from one hypothesis, a list of 27 facts on Haar measures and Heisenberg subgroups. The theorem [`xiExists`](/entry/xi-exists/) proves the 27 facts and applies this theorem, and its result goes to the [unitary hypotheses node](/step/nonempty-hyps/). Below this theorem are 941 declarations; `xiExists` adds one.

## Statement

Let $k \geq 1$ and $r \geq 0$, and let $n = 2r + k + 1$. Let $H$ be the Hermitian form on $\mathbb{C}^n$ with $r$ hyperbolic planes and a diagonal block $\operatorname{diag}(1, \dots, 1, -1)$ of size $k + 1$. Let $G = \{g : g^* H g = H\}$, a group $\mathrm{U}(r + k, r + 1)$. Write $\|g\|$ for the Frobenius norm, and $A_B = 2(k + r)(r + 1) + 1$. A *real place datum* $D$ (`RealPlaceData`) carries Haar measures on $G$, on a unipotent subgroup $N$ and on two stabilizers $W_z$, $W_{z'}$ of vectors $z, z'$ in the diagonal block, a real function $\lambda_z$ on $N$, and more data (representations, a section, a cutoff) that the statement does not use.

**Theorem.** Assume `InductiveHeisenbergInputs`. Let $D$ be a real place datum for finite-dimensional Hilbert spaces $W_p, W_q$, and let $A \geq A_B$. Then there is $\Xi \colon G \to \mathbb{R}_{\geq 0}$ with two properties.

1. (`CoefBound`) There is $C$ such that for all measurable $F, F' \colon G \to \operatorname{Hom}(W_q, W_p)$ with $\|g\|^A \|F(g)\| \leq c$ and $\|g\|^A \|F'(g)\| \leq c'$ on $G$, and all $x, y \in G$,
$$\int_G \|F(x^{-1} g y)\| \, \|F'(g)\| \, dg \leq C c c' \, \Xi(x) \Xi(y).$$
2. (`XiInt`) $\Xi$ is measurable, and $\int_{W_z \times N} \Xi(n w) (1 + |\lambda_z(n)|)^{-2} \, d(w, n) < \infty$, and the same for $z'$.

## Proof

The function is explicit: $\Xi_s(x) = \prod_{l=0}^{r} \Delta_l(x)^{-s_l}$, where $\Delta_l(x)^2$ is the Gram determinant of the first $l + 1$ vectors $x\varphi_0, \dots, x\varphi_l$ of a fixed family of vectors. The exponent $s$ is close to $s^0 = (2, \dots, 2, k)$ from below: $0 < s^0_l - s_l \leq \tfrac{1}{10}$.

`xiExists_of_induction_steps` reduces the theorem to six facts. Four are the base cases and steps of two inductions on $r$. The integral $\int_G \|g\|^{-A} F_s(g)\,dg$ is finite (`AAt`, from `aStepBase_of` and `aStepSucc_of`), where $F_s$ is a product of powers of minors of Hermitian products. The integral $\int_N \Xi_s(n)(1 + |\lambda_z(n)|)^{-\delta}\,dn$ is finite (`BAt`, from `bStepBase_of` and `bStepSucc_of`); the step to $r' + 1$ uses the bound at $r'$ with $\delta / 4$. Then `coefStep_of` turns the first into `CoefBound` for $\Xi_s$, and `xiIntH` turns the second, with $\delta = \tfrac12$, into `XiInt`.

The step lemmas use an Iwasawa-type decomposition (`iwB`), Heisenberg coordinates (`formulaF_all`) and an oscillatory integral bound (`oscillatoryBound'`). We have not unfolded them past their statements.

## In the Lean code

The theorem is in [XiExistsOfIn.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/XiExistsOfIn.lean#L13). Its proof is one term. `XiExists`, `CoefBound` and `XiInt` are in [StatementB.lean](lean:Formalism/HermitianCurvature/StatementB.lean#L439). The hypothesis and the step statements are in [InductiveHeisenbergInputs.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/InductiveHeisenbergInputs.lean#L60), and the two inductions in [XiExists2.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/XiExists2.lean#L37).

- The hypothesis is not a real assumption. `heisenbergHaarFacts_hold` proves all 27 conjuncts, and `xiExists` uses it at once.
- The name `XiExists` has two other, unrelated definitions in the code base, in `UnitaryDeterminantRoot.lean` and `ModelMoves.lean`.
