---
id: theta-kernel-basic-properties
title: The basic properties of the theta kernel of a unitary pair
kind: theorem
decl: GlobalTheory.ThKBasic.theta_kernel_basic_properties
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.ThetaKernelFundamentalProperties
covers: 332
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThetaBasic`: the theta function of a unitary dual pair is continuous, invariant under rational points, of moderate growth, and continuous in the archimedean test function. The proof joins three facts that come from [`ThetaLocalInputs`](/step/theta-local-inputs-def/). It sits below [the tower of square constants](/entry/tower-alt-bis/). Below this theorem are 332 declarations.

## Statement

Let $F$ and $E$ be number fields with $E$ over $F$, and let $\sigma$ be an $F$-automorphism of $E$. Take a hermitian space $X$ of dimension $n$ and a skew-hermitian space $W$ of dimension $d$, a model $M$, characters $\chi_X, \chi_W$ and a Weil representation $\omega$ of $U(X)(\mathbb{A}) \times U(W)(\mathbb{A})$, such that `IsPair` holds. For a test function $\Phi$ on $\mathbb{A}_F^{n \times d}$ put

$$\theta_\Phi(g, h) = \sum_{\xi \in F^{n \times d}} \bigl(\omega(g, h)\Phi\bigr)(\xi).$$

**Theorem.** Assume `ThetaLocalInputs`. Then for each $\Phi$ in the space `schA` (spanned by products of an archimedean Schwartz function and a finite Schwartz-Bruhat function):

1. $\theta_\Phi$ is continuous on $U(X)(\mathbb{A}) \times U(W)(\mathbb{A})$;
2. $\theta_\Phi(\gamma g, \gamma' h) = \theta_\Phi(g, h)$ for rational points $\gamma, \gamma'$ (`ratU`);
3. there are $C$ and $k$ with $|\theta_\Phi(g, h)| \le C\,(\mathrm{ht}(g)\,\mathrm{ht}(h))^k$.

Also, for each finite Schwartz-Bruhat $\varphi$ and each $g, h$, the map $f \mapsto \theta_{f \otimes \varphi}(g, h)$ is continuous on the archimedean Schwartz space. We have not unfolded `IsPair`, `Model` or `ht`.

Part 2 is the classical invariance of Weil (Acta Math. 111, 1964).

## Proof

1. The Weil representation of the pair is a unitary splitting (`IsUSplitting`). The lemma `exists_admissibleForm_adelicThetaSum` gives an admissible functional $l$ that is the theta sum on `schA`.
2. The field `cont` of the splitting gives part 1.
3. `theta_pair_sum_rational` gives part 2, after $\omega(\gamma g, \gamma' h) = \omega(\gamma, \gamma')\,\omega(g, h)$.
4. `theta_pair_moderate_growth` gives part 3.
5. The field `adm` gives the last claim.

## In the Lean code

The theorem is at [ThetaKernelFundamentalProperties.lean line 14](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaKernelFundamentalProperties.lean#L14). `ThetaBasic` is in [CTSmallCone.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/CTSmallCone.lean#L138). `theta` is in [WeilTensorModels.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/WeilTensorModels.lean#L286). `thetaSum` and `IsUSplitting` are in [HilbertNinetyQuotientHomEqIff.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HilbertNinetyQuotientHomEqIff.lean#L107).

Odd points:

- `GlobalTheory.T.theta_kernel_fundamental_properties` at line 42 is a `first | exact` renaming of this theorem.
- The lemmas of steps 3 and 4 are also `first | exact` wrappers, of `ThetaRatPair.theta_sum_omega_rational` and `ThetaModGrowthPair.theta_moderate_growth`. We did not unfold these.
