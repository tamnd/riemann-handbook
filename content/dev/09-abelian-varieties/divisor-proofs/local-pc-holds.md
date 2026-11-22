---
id: local-pc-holds
title: Pseudo-coefficients for discrete series of U(p, q) with large gaps
kind: theorem
decl: GlobalTheory.PsCo.Pc.localPC_holds
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LocalPseudoCoefficientExistenceUnitaryGroup
covers: 1294
status: drafted
drafted_by: writer@claude
---
This theorem proves, with no hypothesis, that each discrete series of $U(p,q)$ whose parameter has large gaps has a pseudo-coefficient. Its only caller is its restatement [`localPseudoCoefficientExistence_unitaryGroup`](/entry/local-pseudo-coefficient-existence-unitary-group/), an input of the [comparison of cuspidal multiplicities](/entry/unitary-theory-of-harish-chandra-langlands-alt/). Below this theorem are 1,294 declarations.

## Statement

Let $r$ be odd, $\varepsilon \in \{\pm 1\}^r$, $J_\varepsilon = \operatorname{diag}(\varepsilon_a)$, $G = \{g \in \mathrm{GL}_r(\mathbb{C}) : g^* J_\varepsilon g = J_\varepsilon\}$, the [[unitary group|0R9R0Y1HDK]] $U(p,q)$. Let $K = U(p) \times U(q)$ be the unitary elements of $G$, and $\mu$ a [[Haar measure|VY0HXD3GC4]] on $G$.

Let $\lambda \in \mathbb{Z}^r$ with $\lambda_a - \lambda_{a+1} \geq 100\, r^4$ for each $a$. Let $D$ be a [[discrete series|9AB7HYGPEK]] representation with parameter $\lambda$ (`IsDS`): unitary, irreducible, square-integrable, with lowest $K$-type of highest weight $\lambda + \rho_n - \rho_c$. For $t_\theta = \operatorname{diag}(e^{i\theta_a})$ let

$$\Theta_\lambda(t_\theta) = (-1)^{pq}\, \frac{\sum_{w \in W_K} \operatorname{sgn}(w)\, e^{i \langle w\lambda, \theta \rangle}}{\prod_{a<b} \bigl(e^{i(\theta_a - \theta_b)/2} - e^{-i(\theta_a - \theta_b)/2}\bigr)},$$

with $W_K$ the permutations that preserve $\varepsilon$: Harish-Chandra's character of $D$ on the compact torus.

**Theorem.** There is $f \colon G \to \mathbb{C}$ such that:

1. $f$ has compact support, is a smooth function of the matrix entries, and is bi-$K$-finite;
2. $D(f) = \int_G f(g)\, D(g)\, d\mu(g)$ is trace class with trace $1$;
3. $\pi(f)$ is trace class with trace $0$ for each irreducible unitary $\pi$ not unitarily equivalent to $D$;
4. at each regular semisimple $s$ with noncompact centralizer $G_s$, the orbital integral $\int_{G_s \backslash G} f(x^{-1} s x)\, d\dot{x}$ is $0$;
5. at each regular semisimple $s$ with compact centralizer and $y^{-1} s y = t_\theta$, the orbital integral is $\overline{\Theta_\lambda(t_\theta)} / \operatorname{vol}(G_s)$.

The usual pseudo-coefficient (items 1, 2, and 3 for tempered $\pi$) exists by a theorem of L. Clozel and P. Delorme, "Le théorème de Paley-Wiener invariant pour les groupes de Lie réductifs" (1984). Item 3 asks more: trace $0$ also on non-tempered unitary representations.

## Proof

The proof is `localPC_of_steps`, applied to twelve step lemmas. Functions $\varphi_t$ concentrate on $K$ as $t \to \infty$, with traces and orbital integrals constant in $t$.

1. **Data on $K$.** `T.maximalCompact_pseudoCoefficientData` gives a polynomial $P_M$, a class function on $K$ with $P_M(t_\theta) = \overline{\Theta_\lambda(t_\theta)}\, d(\theta)$, $d(\theta) = \prod_{\varepsilon_a = 1,\, \varepsilon_b = -1} \lvert e^{i\theta_a} - e^{i\theta_b} \rvert^2$. The operator $\int_K P_M(k)\, \pi(k)\, dk$ has trace $1$ on $D$ and $0$ on other irreducible unitary $\pi$. Only this step uses the gaps and $r$ odd.
2. **The family.** With $\rho(g) = \sum_{\varepsilon_a = 1,\, \varepsilon_b = -1} \lvert g_{ab} \rvert^2$, `A.stAlg`, `stProfile_holds` and `stFam` give $\varphi_t$, a sum of polynomials times derivatives of a cut-off at $t\rho$, with $\varphi_t = 0$ where $t\rho > 1$. By `ShapeSmoothFinite.stShape` it meets item 1.
3. **Constancy.** $\varphi_1 - \varphi_t$ is a sum of derivatives along conjugation (`Homot.stHomot`), with orbital integrals and traces $0$ (`orbInt_adSpan_eq_zero`, `Pc3.stTrAd`).
4. **The limit.** By `Pcd.stLim` and `Pc3.stTr` there is $c \neq 0$ such that $c^{-1}\operatorname{tr}\pi(\varphi_t)$ tends to the trace in step 1, and $c^{-1}$ times the orbital integral at $t_\theta$ tends to $P_M(t_\theta)/d(\theta)$, which `stOrbCpt` turns into item 5.
5. **Non-elliptic $s$.** $\rho \geq R > 0$ on the conjugacy class of $s$ (`NonEll.stNonEll`), so $\varphi_t$ vanishes there for $t > 1/R$. This gives item 4.

Put $f = c^{-1} \varphi_1$.

## In the Lean code

The theorem is in [LocalPseudoCoefficientExistenceUnitaryGroup.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalPseudoCoefficientExistenceUnitaryGroup.lean#L21). `LocalPC` is in [RangeShape.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RangeShape.lean#L22), `localPC4_of` in [EqOfConstOfTendsto.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EqOfConstOfTendsto.lean#L47), `IsDS` in [RelevantZeroGramTerms.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean#L72). We have not unfolded `HasQuotInt`, which defines the orbital integral `HasOrbInt`.

The representation theory is all in `StKData`, proved by `maximalCompact_pseudoCoefficientData'` from 23 lemmas that we have not opened. By their names, they recognize $D$ by its lowest $K$-type and Casimir eigenvalue.

Odd point: `GapG` and `Gap4` are the same definition, and `LocalPC4` is `LocalPC` with `Gap4`.
