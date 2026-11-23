---
id: ka-st
title: The key invariant of a principally polarized abelian variety
kind: theorem
decl: GlobalTheory.KaExists.kaSt
module: Development.AbelianVarietyTheory.Proofs.ThetaLawProofs.ExistsIntegralKeyInvariantRuleCharZero
covers: 837
status: drafted
drafted_by: writer@claude
---
This theorem builds the key invariant: a unit attached to an abelian variety with a theta section and a tangent basis. It has weight $4c$, commutes with base change, is integral away from $M$ and is holomorphic in the period matrix. Through its [second name](/entry/exists-integral-key-invariant-rule-char-zero/), [the key rule for half characteristics](/entry/exists-key-rule-char-half/) uses it.

## Statement

A *key input* $x$ over a ring $R$ (`KeyIn`) is an abelian scheme $A/R$ of relative dimension $g$ with a symmetric, rigidified, relatively ample $L$ with trivial $K(L)$, a section $\theta$ of $L$ nonzero on each fibre, and a basis $v_1, \dots, v_g$ of the tangent space at $0$. A *pullback* of $x$ along $f \colon R \to R'$ (`KeyPB`) is a key input over $R'$ isomorphic to the base change of $x$.

**Theorem.** Assume `Out.Laws`, `ThetaUnifAV`, `TorusAlgebraic` and `KeyDesc` (descent of key inputs to countable subfields). Let $g \geq 1$ and $p$ prime. Then there are integers $c, M \geq 1$ with $p \nmid M$ and a unit $\kappa(x) \in K^\times$ for each key input $x$ over an algebraically closed field $K$ of characteristic $0$, such that for $x$ of dimension $g$:

1. If $x'$ is $x$ with $a\theta$ and $v'_i = \sum_k m_{ik} v_k$ in place of $\theta$ and $v_i$, then $a^{8c}\kappa(x') = \det(m)^{4c}\kappa(x)$.
2. If $x'$ is a pullback of $x$ along $f \colon K \to K'$, then $\kappa(x') = f(\kappa(x))$.
3. For $x$ over a discrete valuation ring $R$ of characteristic $0$ with $M \in R^\times$, there are an injective local map $j \colon R \to R'$ of discrete valuation rings and $u \in R'^\times$ with $\kappa(x_K) = f(u)$ for each $f \colon R' \to K$ and each pullback $x_K$ of $x$ along $f \circ j$.
4. For $a, b \in \{0, \tfrac12\}^g$ there is a function $U$, holomorphic on the Siegel upper half space $\mathfrak{H}_g$, with $\kappa(x) = U(\tau)$ for each complex $x$ that is *normal at* $\tau$: $A(\mathbb{C}) \cong \mathbb{C}^g/(\mathbb{Z}^g + \tau\mathbb{Z}^g)$, $\theta$ is the theta function with characteristic $(a, b)$, and $v_i$ is $(2\pi i)^{-1} e_i$.

## Proof

1. **Numbers.** `exists_admissibleKeyNumericalData_prime_to` gives $n \geq 4$, $gn < l < l'$ and integer $4 \times 4$ matrices $\alpha_m$ with $\alpha_m^{T}\alpha_m = m$, and $p \nmid M$, where $M = \prod_{j=0}^{g}(l - jn)(l' - jn)$. Then $c = 2M^{3g+2}\, g!\, n^g (l' - l)$.
2. **The value.** A *key value* (`KaVal`) of $x$ is a product of powers of Koszul values at the levels $l, l'$, of comparison constants at the levels $l - jn, l' - jn$, and of the Jacobians of $g$ sections of $L^n$ at their $g!\,n^g$ common zeros. `T.keyInvariant_independent_of_sections` gives one $\kappa(x) \in K^\times$ equal to every key value over every extension of $K$. In other dimensions $\kappa(x) = 1$.
3. **Weight.** `KaScale.kaVal_scale` and three helper lemmas compare key values of $x$ and $x'$.
4. **Base change.** Uniqueness in step 2 and `keyPB_trans`.
5. **Integrality.** `exists_kaVal_dvr` extends $R$ to a complete discrete valuation ring with enough algebraically independent elements for generic sections (`T.generic_sections_meet_transversally`). `T.exists_keyInvariant_after_dvr_extension` then gives a unit key value $u$.
6. **Holomorphy.** `KeyOfPeriod.exists_keyIn_normalAt` gives a complex key input normal at each $\tau \in \mathfrak{H}_g$. `exists_kaVal_complex` descends it to a countable field $K_0$ by `KeyDesc`. A [[transcendence basis|E45PA267S4]] of $\mathbb{C}$ over $K_0$ is infinite, so generic sections exist. `T.koszulInvariant_locally_holomorphic_periodMatrix` makes $\kappa$ holomorphic near each $\tau$.

## In the Lean code

The theorem is at [ExistsIntegralKeyInvariantRuleCharZero.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsIntegralKeyInvariantRuleCharZero.lean#L160). The statement `KaSt` and the rule `KaRule` are in [KaRuleK.lean](lean:Development/AbelianVarietyTheory/Definitions/KeyFormula/KaRuleK.lean#L18).

`Out.Laws` is used in most steps. The other three hypotheses are used only in step 6. Holomorphy is `Key.IsHoloSiegel`, a condition on $X \mapsto U(\tfrac12(X + X^{T}))$. Off $\mathfrak{H}_g$ the proof sets $U = 0$. We have not unfolded `KosVal` or `IsSquareDeterminantComparison`.
