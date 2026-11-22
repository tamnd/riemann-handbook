---
id: tower-alt-bis
title: The ratio of square constants along a tower of theta lifts
kind: theorem
decl: GlobalTheory.SqTower.tower_alt_bis
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.TowerOfThetaMatching
covers: 1960
status: drafted
drafted_by: writer@claude
---
This theorem proves `Tower`. It compares the square constant of a theta integral at a point $t$ with the constant at a base point $\mu_0$. The ratio is a unit away from a level, times step ratios, times values of [[Hecke L-functions|24GAZHVTGB]], times the ratio of the constants of a bottom triangle. It is used below [the last node of the trunk](/step/nonempty-hyps/), through [the joined estimates of the square top term](/entry/square-top-term-joined-estimates/). The proof is algebra on five lemmas about stages of a tower.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/), [`LocalMatching`](/step/local-matching-def/) and `LNe`. Then `Tower` holds.

Both `LNe` and `Tower` have the form `GBig Q`. This says: there is $CF_0$ such that for all $\varepsilon$ and $CF \ge CF_0$ there are $C_0$ and $x_0$ such that, for $C \ge C_0$, for every large datum $D$ with $\varepsilon$ and $x \ge x_0$ and with the field conditions of `Rec`, and for every grid $G$ over a level character with base point $\mu_0$, the property $Q$ holds.

Write $\Lambda_t$ for an entire function with $\Lambda_t(s) = \prod_v (1 - \chi_t(v) Nv^{-s})^{-1}$ for $\operatorname{Re} s > 1$, the product over unramified $v$ (`IsHeckeL`), where $\chi_t$ is the character `nuH G t i j`.

- `LNe`: for all $i, j$, each $\chi_t$ has such a $\Lambda_t$ with $\Lambda_t(s) \ne 0$ for integers $1 - e_0 \le s \le h$, where $h$ is `halfRank`. A second family `fam` has the same with $\Lambda(s) \ne 0$ for $s \ge 1$.
- `Tower`: take a Weil datum $W$ with a standard character, a grid choice $S$, a real match $\rho$, indices $i, j$ and a point $t$. Let $c$ and $c_0$ be square constants at $t$ and at $\mu_0$ (`IsSquareConst`, with `SquareNonzero`). Let $X$ be a bottom triangle with constant $c^{X}$ (`Tri.IsConst`). Then there are $u_k$ for $k < p + q$, each a step ratio, and an away unit $\zeta$ for the level `Qn G t` (`IsAwayUnit`) with

$$\frac{c}{c_0} \prod_{k<q} \frac{\Lambda_t(e+k+1)}{\Lambda_{\mu_0}(e+k+1)} = \zeta \cdot \prod_k u_k \cdot \frac{c^{X}(t)}{c^{X}(\mu_0)} \prod_{k<p} \frac{\Lambda_t(e+q-k)}{\Lambda_{\mu_0}(e+q-k)}.$$

Here $p = \lfloor (m-j-1)/2 \rfloor$, $q = \lfloor (m-j)/2 \rfloor$ and $e$ is half the rank jump from stage $(i,j)$ to $(i+1,j+1)$. We have not unfolded `SquareNonzero`, `IsBottomTri`, `NumbersIn` or `Qn`.

## Proof

1. The three theta inputs go to five lemmas: the top stage norm formula, the factor of a stage, the norm steps in small and in large rank, and the bottom constant ratio. `gbig_and` joins them with `LNe`, and `gbig_mono` gives `Tower`.
2. By uniqueness, $\Lambda_t$ and $\Lambda_{\mu_0}$ are the functions of `LNe`.
3. The top stage gives a triangle with constant $c_T$ and $c = \kappa_T(t)\, c_T(t)$.
4. The lemma `descent`, an induction on $q$, takes the top triangle down to stage $(0,0)$. It gives $c_T(t) \prod_{k<q} \Lambda_t(e+k+1) = \kappa \prod_{k<p+q} u_k(t)\, c_Y(t) \prod_{k<p} \Lambda_t(e+q-k)$.
5. The bottom lemma relates $c_Y$ to the constant of $X$ by a factor $v$ with $v(t) = \zeta_v\, v(\mu_0)$.
6. `LNe` makes the products at $\mu_0$ nonzero. The answer is $u_k(t)/u_k(\mu_0)$ (by `stepRatio_div`) and $\zeta = \zeta_T \zeta_v^{-1}$ (by `isAwayUnit_inv`). The rest is `field_simp`.

## In the Lean code

The theorem is at [TowerOfThetaMatching.lean line 32](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TowerOfThetaMatching.lean#L32). `Tower` and `LNe` are in [NormSmall.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/NormSmall.lean#L128). The helpers `gbig_and`, `gbig_mono`, `descent`, `stepRatio_div` and `isAwayUnit_inv` are in [the statement file](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TowerOfThetaMatching.lean#L99).

Odd points:

- The five lemmas, such as [the top stage formula](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/WittTowerTopStageThetaNormFormula.lean#L50), are `first | exact` wrappers. We did not follow how they use the three inputs.
- `GlobalTheory.T.tower_of_theta_matching_lNe` at line 111 is a renaming of this theorem. It is the form that the joined estimates call.
- Lines 23 to 28 hold two empty sections with only `variable` lines.
- The name "alt_bis" says nothing about the statement. The lemma names speak of a Witt tower, and `Tower` names none.
