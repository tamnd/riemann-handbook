---
id: hilbert-samuel-estimate-at-level
title: The Hilbert-Samuel estimate on one component at one level
kind: theorem
decl: GlobalTheory.HSShortRun.hilbertSamuel_estimate_at_level
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.ExistsDegreeParametersBound
covers: 769
status: drafted
drafted_by: writer@claude
---
This theorem proves the inequality `HSClaimS` on one component $Z$ of one good cover. It builds the hermitian data of the component from two cusp frames and families of short cusp forms, checks the geometric hypothesis `GeoHyp`, and then applies [the short basis bound](/entry/hilbert-samuel-component-short-basis-bound/). Its user is [hsClaim_short_alt_alt](/entry/hs-claim-short-alt-alt/), which supplies all the inputs from cover statements. Below this theorem are 769 declarations.

## Statement

**The claim.** For $C$, integers $T, D$ and reals $n, j_0, \Lambda, \beta, \Lambda_D, \Lambda_T, J, \delta, h, d, \deg$, put $R = \binom{T-1}{D}$, $z = 1 - R\delta/d$, $\rho = \log\Lambda + C\log\bigl(n D j_0 \delta (2 + |h| + \log\Lambda)\bigr)$ and $G = (D+1)(\log n + 1)/2 + 1$. Then `HSClaimS` says that $0 \le z \le 1$ and

$$\begin{aligned}&{(1 - z)\Bigl(Th - 3(D+1)\lvert h\rvert - J - CD^2\log(e^\rho T) - (T + D + 1)\log\beta - (T + D^2)(G + 2)\Bigr)}\\ &{\quad - z\Bigl(T\log(2e^\rho\sqrt\beta) + \log\Lambda_D + \log\Lambda_T\Bigr) \le \frac{\deg}{d}.}\end{aligned}$$

**Theorem.** Let $Y$ be a good cover at level $j$ with $[E:\mathbb{Q}]/2 > 2$, $Z$ a component, and $P$ a weight parameter with `WtBig`, such that $Y$ is good at each weight $P_i$, $i \le T$. Let $P_P, \kappa \ge 0$ and $N$ = `dimFlag`. Assume `Hypotheses''`, `GrothendieckDeformation`, `Quoted`, `NadelVanishingAndNonKltDivisor`, `Principalisation`, `SiegelToroidalIntegral`, `ToroidalChartsForFan`, `SemiAbelianLieSeminegative`, and:

- cusp frames $f_1$ at the weight $u_1$ and $f_2$ at $u_2$, with all frame norms of $f_1$ at most $\Lambda \ge 1$, and the Bergman bound `BergLe` with $\beta \ge 1$ at $u_1$;
- `BirOn` at $u_1$ and at $u_2$;
- a family of lattice vectors that spans the cusp forms of weight $P_0$, each of Petersson norm at most $e^{N P_P(\kappa/T + 1)}$;
- for each $i \le T$, such a family at weight $P_i$ with Petersson norms at most $e^{P_P\kappa}$.

Then $1 \le n$ and `HSClaimS` holds with $C = 26$, $D = N$, $n$ the size of $f_1$, $j_0 = 1$, $\Lambda_D = \Lambda_T = e^{P_P\kappa}$, $J = N P_P(\kappa/T + 1)$, $\delta$ and $h$ the degree and height at $u_1$, and $d$, $\deg$ the rank and degree of the cusp lattice at $P_T$.

## Proof

1. `exists_weight_hodge_bundle_generated` gives a flag cover, a choice of modification, a canonical identification and the data `Ready`.
2. The constants are $(\Lambda, \beta, e^{P_P\kappa}, e^{P_P\kappa})$. `cuspForm_ratios_generate_at_flagSpace_genericPoint` turns `BirOn` into the birationality of the two frames.
3. `shortFamily_of_spanning` turns the spanning families into `ShortFamily` at levels $0$, $N$ and $T$. Here $N \le T$ comes from `Ready`.
4. `hermitian_geometric_hypothesis_holds` gives `GeoHyp` with $\Lambda_0 = e^{N P_P(\kappa/T + 1)}$.
5. [hilbertSamuel_component_short_basis_bound](/entry/hilbert-samuel-component-short-basis-bound/) gives `HSClaimS` with $J = \log\Lambda_0$, and $d$ the dimension of the cusp space at $P_T$. This is the step with content.
6. `Ready` says that the lattice spans that space, so its rank $\mathrm{rk}_{P_T}(Z)$ is that dimension.

## In the Lean code

The theorem is at [ExistsDegreeParametersBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ExistsDegreeParametersBound.lean#L33). `HSClaimS` is in [HSClaim.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/RealCubicMeans/LogMeanShares/LogMeanStatements/HSClaim.lean#L16) and `GeoHyp` in [HermSysHypOneLeLambdaZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HermSysHypOneLeLambdaZero.lean#L253).

- The section `th` is $0$ (line 56), and the field `J` of `Consts` is $0$ (line 55). The $J$ of the claim is $\log\Lambda_0$, not this field.
- We have not unfolded `Ready`, `ShortFamily`, `BergLe`, `BirOn` or `CuspFrame`.
