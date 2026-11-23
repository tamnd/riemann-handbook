---
id: iwasawa-formula
title: The integration formula for an isotropic flag of U(p, q)
kind: theorem
decl: GlobalTheory.FlagMeas.iwasawaFormula
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.UnitaryIwasawaIntegrationFormulaRealPlace
covers: 328
status: drafted
drafted_by: writer@claude
---
This theorem proves `IwasawaFormula`: an integration formula on the real [[unitary group|0R9R0Y1HDK]] $\mathrm{U}(p,q)$, for the decomposition $G = NMK$ attached to an isotropic flag, with the exact constant. [`unitary_iwasawa_integration_formula_real_place`](/entry/unitary-iwasawa-integration-formula-real-place/) renames it. [`OneClass.bound`](/entry/bound/) applies it at each real place to bound the measure of one flag class. The proof joins two lemmas; the constant is computed in [`iwasawa_constant`](/entry/iwasawa-constant/).

## Statement

Let $n = p + q$ and $J = \mathrm{diag}(\pm 1)$ with $p$ signs $+1$. Let $G = \{g \in \mathrm{GL}_n(\mathbb{C}) : g^* J g = J\}$ and let $\mu_G$ be a [[Haar measure|VY0HXD3GC4]] on $G$. For $X \subseteq G$, $d \ge 0$ and a measure $\mu$ on $G$, call $\mu$ a *gauge measure of dimension $d$ on $X$* (`IsGaugeSub`) if $\mu(G \setminus X) = 0$, $\mu$ is invariant under left translation by $X$, and $\mu\{g : \|g - 1\|_{HS} \le r\} / r^d$ tends to the volume of the unit ball of $\mathbb{R}^d$ as $r \to 0^+$. Call $c \in \mathbb{R}$ a *gauge constant* (`IsGauge`) if $c\,\mu_G$ has this limit with $d = n^2$.

Let $0 = W_0 \subseteq W_1 \subseteq \dots \subseteq W_a$ be a flag in $\mathbb{C}^n$ with $\dim W_{i} - \dim W_{i-1} = j_i \ge 1$, and $W_a$ totally isotropic for $J$. Let $N$ be the set of $g$ that act trivially on each $W_i / W_{i-1}$ and map each $y \in W_a^\perp$ into $y + W_a$. Let $M$ be the set of $g$ such that $g$ and $g^*$ preserve each $W_i$. Let $K = G \cap \mathrm{U}(n)$. Put $s = \sum_i j_i$ and

$$\tau_i(m) = \Bigl(\frac{|\det(m|_{W_i})|}{|\det(m|_{W_{i-1}})|}\Bigr)^{-1/j_i}, \qquad \delta(m) = \prod_{i<k} (\tau_i/\tau_k)^{2j_ij_k} (\tau_i\tau_k)^{2j_ij_k} \prod_i \tau_i^{2j_i(n-2s)+2j_i^2}.$$

**Theorem.** Let $c$ be a gauge constant, $\mu_N$ a gauge measure on $N$ of dimension $\dim N = 4\sum_{i<k} j_ij_k + 2s(n-2s) + \sum_i j_i^2$, $\mu_M$ a gauge measure on $M$ of dimension $(n-2s)^2 + 2\sum_i j_i^2$, and $\mu_K$ a left $K$-invariant probability measure on $K$. Then for every measurable $\varphi \colon G \to [0,\infty]$,

$$c \int_G \varphi \, d\mu_G = c_{Iw}(p,q,j) \int_N \int_M \delta(m) \int_K \varphi(umk)\, d\mu_K(k)\, d\mu_M(m)\, d\mu_N(u).$$

The constant $c_{Iw}$, a quotient of volumes of unitary groups, is written out in [`iwasawa_constant`](/entry/iwasawa-constant/).

## Proof

`iwasawa_integration_formula_up_to_constant` (a renaming of `IwasawaShape.iwasawa_shape`) gives a number $\kappa \in (0, \infty)$ with $\int_G \varphi\, d\mu_G = \kappa \cdot (\text{the triple integral})$ for all $\varphi$. [`iwasawa_integration_formula_constant`](/entry/iwasawa-integration-formula-constant/) gives $c \kappa = c_{Iw}(p,q,j)$. Substitute.

## In the Lean code

The theorem is in [UnitaryIwasawaIntegrationFormulaRealPlace.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/UnitaryIwasawaIntegrationFormulaRealPlace.lean#L10). `IwasawaFormula` is in [SameKindIsometric.lean](lean:Development/AbelianVarietyTheory/Statements/CuspFrameWeights/SameKindIsometric.lean#L60). The sets $N$, $M$, $K$ are `flagN`, `flagM`, `maxK`, and $\tau$ is `locSize`, in [DefClassNum.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/DefClassNum.lean#L52). $\delta$ is `layerProd n 1 j τ id` in [LayerProd.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/LayerProd.lean#L32).

The integrals are lower Lebesgue integrals. The name "Iwasawa" is used for this $NMK$ form, but $M \cap K$ is not trivial in general, so $N \times M \times K \to G$ is not injective. We did not open the proof of `iwasawa_shape`. It is not in the 328 declarations below this theorem; 327 of them are below the constant.
