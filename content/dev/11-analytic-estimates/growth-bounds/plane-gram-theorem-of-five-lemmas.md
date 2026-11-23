---
id: plane-gram-theorem-of-five-lemmas
title: The uniform lift bound from five local lemmas
kind: theorem
decl: Formalism.MainNotions.PlaneGram.plane_gram_theorem_of_five_lemmas
module: Formalism.SharpRestriction.GrowthBounds.MonomialOrderSegments.PlaneGramTheoremOfLemmas
covers: 307
status: drafted
drafted_by: writer@claude
---
This theorem proves the lift bound `LiftBoundUniform` from five local statements on polynomials. Its only user is [the plane Gram statement](/entry/stmt/), which gets them from the conditions `AdmAt`.

## Statement

Let $K$ be a field of characteristic $0$ with a valuation $v$ to $\mathbb{Q} \cup \{\infty\}$, and $p \in \mathbb{N}$. `DVRHyp v p` says that $p \ge 5$ is a prime with $v(p) = 1$. The lemmas use the valuation `valS` of [Statement E](/entry/stmt-e/) on polynomials in variables $X_{\ell, a}$.

- `V2`: bounds for `valS` on variables, under divided derivatives, and under a change of substituted letters.
- `SPAN`: an integral basis of products of column polynomials that reads off lower bounds on `valS`.
- `PROJ`: projections onto $\{F : \mathrm{valS}(F) \ge \theta\}$, orthogonal for the Fock pairing $\langle F, G \rangle = \sum_\alpha F_\alpha G_\alpha \, \alpha!$, that commute and lose at most $r^2 \lg$ in $v_{BB}(F) = \min_\alpha (v(F_\alpha) + \tfrac12 v(\alpha!))$.
- `DIG`: $\prod_a (\rho_a + p^g \beta_a)!$ is a constant times $\prod_a \beta_a!$ times a unit.
- `DER`: a congruence modulo $p^c$ for divided derivatives of $X^{\rho + p^g \beta}$.

**Theorem.** If $C_0 \ge 1$ and the five lemmas hold, then `LiftBoundUniform K v p C0` holds.

`LiftBoundUniform` is `LiftBoundWith` with the constants $13, 12, 30, 2$: for each valid twist datum $D$ with `HypH` and $c > 4(D_m + D_l + 3\kappa)$, and each $F$ in `InXX` with $v_{BB}(F) = 0$, there are polynomials $G'$ and $R$ that lose at most $12c$ and $30c$ in their thresholds, with $v(\langle F, \gamma \cdot \varphi(G' + R) \rangle) \le n_0 + E + \kappa$. Here $\varphi$ is the map `ph` that raises some variables to the power $p^{g}$, and $\gamma$ multiplies coefficients by units.

## Proof

The step lemmas are `stepB_of` (`V2`, `PROJ`), `stepC_of` (`V2` and `segStep_of`, which uses `SPAN`), `stepG_of` (`V2`), `stepP_of` (`PROJ`) and `stepE_of` (`V2`, `DER`). `stepBC_of` joins B and C; `stepDEF_of` joins `DIG`, G, P and E. Then `plane_gram_theorem_of_combined_lemmas` takes $Z$ from StepBC and an operator $\Omega$ with an integer $N_2$ from StepDEF, and sets $G' = p^{N_2} \Omega(Z)$ and $R = 0$.

## In the Lean code

The theorem is in [PlaneGramTheoremOfLemmas.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialOrderSegments/PlaneGramTheoremOfLemmas.lean#L13), the inputs in [LiftBoundOfHypotheses.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialOrderSegments/LiftBoundOfHypotheses.lean#L113) and the steps in [CollapseExponent.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialOrderSegments/CollapseExponent.lean#L66).

- $C_0$ does no work. `PROJ` and `eC` take it as an unused argument `_C0`. The caller sets $C_0 = 1$.
- $R$ is always $0$ ([TestBoundOfRhoAndNormSets.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialOrderSegments/TestBoundOfRhoAndNormSets.lean#L111)), so the four conditions on $R$ are trivial.
- `V2` does not mention $v$ or $p$. We have not unfolded `InXX`, `InYY` or the step proofs.
