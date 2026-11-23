---
id: top-density-dominated
title: An integrable majorant for the cut-off top densities
kind: theorem
decl: GlobalTheory.HatNF.top_density_dominated
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.TopDensityDominated
covers: 373
status: drafted
drafted_by: writer@claude
---
This theorem gives one integrable function that bounds the top density of $\chi(G/\varepsilon)\,G^{p_0} f$ for all $\varepsilon > 0$. It combines a pointwise word bound with an integrability theorem for the empty word. [`topDensity_cut_dominated_all`](/entry/top-density-cut-dominated-all/) uses it with $a = 0$ to prove `NFTopDomAll`.

## Statement

We use the notation of [`topDensity_cut_dominated_all`](/entry/top-density-cut-dominated-all/): $n$, $p$, $G$, $G_p$, $\mathrm{big}(c)$, $E^w_H$, and the conditions 1 to 4 on $\chi$, $p$, $f$, $A_0$, $p_0$, $N$.

**Theorem.** Assume `BesselXiIntegrable`. Let $a \colon \mathbb{N} \to \mathbb{N}$ satisfy `BasicLiftAll a`, and let $C_b \in \mathbb{R}$. There is $C_c$ with this property. Suppose conditions 1 to 4 hold, $N(1 + 2a(r)) \le 2p_0$, $w$ is a cut word (`CutWord`) and $|w| \le N$. Put $F_\varepsilon(g) = \chi(G(g)/\varepsilon)\, G(g)^{p_0} f(g)$. Then:

1. for each $\varepsilon > 0$, $c \mapsto E^w_{F_\varepsilon}(\mathrm{big}(c))$ is almost everywhere strongly measurable on $\mathbb{C}^{r+1}$;
2. there is an integrable $h$ on $\mathbb{C}^{r+1}$ with $|E^w_{F_\varepsilon}(\mathrm{big}(c))| \le h(c)$ for all $\varepsilon > 0$ and all $c$.

`BasicLiftAll a` says that the basic elements of each normal form lie in a span of polynomial lifts, with the exponent $a(r)$; we have not unfolded it further. A cut word has letters on the cut of the types $u, u'$, pairwise more than $2$ apart.

## Proof

Write $v_H(c)$ for the vector `B.hsVec (p.V H (big c))`, and $D = |\prod_l c_l|$.

1. **Word bound.** [`T.wordBound_smooth_decaying_coefficients`](/entry/word-bound-smooth-decaying-coefficients/) gives $C_1$, and then $C$, $J$ and a list of differential operators $\Theta_1, \dots, \Theta_s$, with: for each index $e$ and each $c$ with all $c_l \neq 0$ and $G_p > 0$,
$$|v_{\Theta_{w,e}((\varphi \circ G) f)}(c)| \le C\, D^{-|w|} G_p^{-a(r)|w|} \sum_{j \le J} |\varphi^{(j)}(G_p)| \sum_t |v_{\Theta_t f}(c)|,$$
with $\varphi^{(j)}$ the $j$-th derivative in $\log x$ (`LE.ld`).
2. **The cut power.** `ld_cut_pow` shows that $\varphi_\varepsilon(y) = \chi(y/\varepsilon) y^{p_0}$ is admissible in step 1 and $|\varphi_\varepsilon^{(j)}(x)| \le C' x^{p_0}$ for $j \le J$, uniformly in $\varepsilon$.
3. **Top density.** `TopDensityBound.top_density_le` shows that $E^w_H(\mathrm{big}(c)) = 0$ unless all $c_l \neq 0$ and $G_p > 0$. In that case $E_H = n(c) |v_H|^2$ with a weight $n(c) \ge 0$, and $|E^w_H| \le C_t\, n(c) (D^2/G_p)^{|w|} \sum_e |v_{\Theta_{w,e} H}|^2$.
4. **Combine** (`dom_real_bound`). The powers of $G_p$ give $G_p^m$ with $m = 2p_0 - |w|(1 + 2a(r)) \ge 0$, and $G_p^m \le 1 + G_p^{2p_0}$. With Cauchy-Schwarz over $t$:
$$|E^w_{F_\varepsilon}(\mathrm{big}(c))| \le K \sum_t \bigl(E_{\Theta_t f} + E_{G^{p_0}\Theta_t f}\bigr)(\mathrm{big}(c)),$$
with $K$ independent of $\varepsilon$ and $c$. This right side is $h$.
5. **Integrability.** Put $d = 8|w|(r+1)n$. Each $\Theta_t f$ is smooth with decay $A_0 - d$ (`class_lower_decay_holds`), and $G^{p_0}\Theta_t f$ has decay $A_0 - d - (2r+2)p_0$ (`inCC_Gpow_smul`). `dom_thr` and the margin give $C_2 (r+1)^4 n^3 \le A_0 - d - (2r+2)p_0$. So `T.integrable_emptyWordDensity_decayingCoefficients` (constant $C_2$) makes each term of $h$ integrable.

Take $C_c = \max(C_1, C_2, 8)$. Measurability comes from `TopVec.aestronglyMeasurable_tv`. The rest is bookkeeping.

## In the Lean code

The theorem is at [TopDensityDominated.lean line 82](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/TopDensityDominated.lean#L82). The real inequalities are `dom_pow_le` (line 20), `dom_real_bound` (line 28) and `dom_thr` (line 73) in the same file. `BasicLiftAll` and `mulG` are in [BasicLiftAll.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/BasicLiftAll.lean#L21).

`BesselXiIntegrable` is used only by the integrability theorem in step 5. The majorant $h$ depends on $\chi$ through $C'$, but not on $\varepsilon$. We have not opened `top_density_le` beyond its statement, nor the weight $n(c)$ (`TBB.nPt`).
