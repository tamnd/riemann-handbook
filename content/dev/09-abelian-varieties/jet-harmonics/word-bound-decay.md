---
id: word-bound-decay
title: The word bound for smooth decaying functions, by approximation
kind: theorem
decl: GlobalTheory.HatNF.wordBound_decay
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.WordBoundSmoothDecayingCoefficients
covers: 347
status: drafted
drafted_by: writer@claude
---
This theorem extends a pointwise word bound from compactly supported functions to smooth functions with enough decay. It keeps the same constants and operators, and passes to the limit along smooth truncations. Its restatement [`T.wordBound_smooth_decaying_coefficients`](/entry/word-bound-smooth-decaying-coefficients/) feeds [`top_density_dominated`](/entry/top-density-dominated/).

## Statement

We use the notation of [`topDensity_cut_dominated_all`](/entry/top-density-cut-dominated-all/) for $n$, $p$, $G$, $G_p$ and $\mathrm{big}(c)$. Write $v_H(c)$ for the vector `B.hsVec (p.V H (big c))`, which we have not unfolded, and $\Theta_{w,e}$ for the word operators of $p$. A *cut power* of degree $e$ (`CutPow e φ`) is a smooth $\varphi \colon \mathbb{R} \to \mathbb{R}$ that vanishes on $(-\infty, \delta_0)$ for some $\delta_0 > 0$ and equals $\alpha x^e$ for $x \ge R$.

`WordBound p a w C J Θs K` means: $C \ge 0$; each $\Theta \in \Theta_s$ is a polynomial differential operator of orders $(|w| n,\ 8|w|(r+1)n)$ (`PolyOp`); and for each pair $(\varphi, f)$ with $K(\varphi, f)$, each index $e$ and each $c$ with all $c_l \neq 0$ and $G_p(\mathrm{big}(c)) > 0$,
$$|v_{\Theta_{w,e}((\varphi\circ G) f)}(c)| \le C\, |\textstyle\prod_l c_l|^{-|w|}\, G_p^{-a|w|} \sum_{j=0}^{J} |\varphi^{(j)}(G_p)| \sum_{\Theta \in \Theta_s} |v_{\Theta f}(c)|.$$
Here $G_p = G_p(\mathrm{big}(c))$ and $\varphi^{(j)}(x)$ is the $j$-th derivative of $u \mapsto \varphi(e^u)$ at $u = \log x$.

**Theorem.** The statement of [`T.wordBound_smooth_decaying_coefficients`](/entry/word-bound-smooth-decaying-coefficients/): under `BasicLiftAll a`, `InDDplus2` for $C_b$, a cut word $w$ and $|w| \le N$, `WordBound` holds for all cut powers $\varphi$ of degree $e$ and all smooth $f$ with decay $A \ge C_c(r+1)^4(Nn^2 + n^3) + (2r+2)e$.

## Proof

Take $C$, $J$ and $\Theta_s$ from [`T.wordBound_compactSupportCoefficients`](/entry/word-bound-compact-support-coefficients/), the same bound for smooth $\varphi$ and compactly supported $f$ (`CptCoef`: smooth, bounded support, and $G \ge \varepsilon > 0$ on the support). Fix $\varphi$, $f$, $e$ and $c$, and put $\gamma = \mathrm{big}(c)$.

1. Let $\delta = \min(\delta_0, G_p(\gamma)/2)$ and fix a cutoff $\chi$ (smooth, $0$ near $(-\infty, 0]$, $1$ on $[1, \infty)$). Let $f_n = \beta_n \cdot \chi(G/\delta) f$, with $\beta_n$ a smooth bump equal to $1$ on $\|g\| \le n+1$ and $0$ on $\|g\| \ge 2(n+1)$ (`cutN`). By `cptCoef_apx` each $f_n$ is compactly supported in this sense.
2. Since $\varphi = 0$ below $\delta_0$ and $\chi(G/\delta) = 1$ above $\delta_0$, $(\varphi\circ G) f_n = \beta_n (\varphi\circ G) f$. The compact case gives the bound for each $n$.
3. Let $n \to \infty$ on the left. By `InDDplus2`, $\Theta_{w,e}$ agrees near $\gamma$ with a differential operator. Then `PBE.vecV_cut_op` gives convergence of the truncated vectors; the decay margin covers its threshold (`thr_arith`).
4. Let $n \to \infty$ on the right. `vecV_cut_polyOp` gives convergence to $v_{\Theta(\chi(G/\delta) f)}(c)$. Since $\delta < G_p(\gamma)$, `vec_opApply_cutF_eq` shows that this equals $v_{\Theta f}(c)$.

The inequality passes to the limit (`le_of_tendsto_of_tendsto'`). The constant is $C_c = 5b + b^2 + 1 + |\max(c_1, c_2)|$ with $b = \max(C_b, 8)$ and $c_1, c_2$ the thresholds of the two convergence lemmas. The rest is bookkeeping.

## In the Lean code

The theorem is at [WordBoundSmoothDecayingCoefficients.lean line 18](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/WordBoundSmoothDecayingCoefficients.lean#L18). `WordBound` and `CutPow` are in [BasicLiftAll.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/BasicLiftAll.lean#L29), and `cutN` and `cptCoef_apx` in [CutDec.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutDec.lean#L12).

The hypothesis `BasicLiftAll a` is only passed to the compact case. `InDDplus2` and the decay are used only for the limit on the left side. The constants $C$, $J$ and $\Theta_s$ do not depend on $\varphi$ or $f$; they come from the compact case unchanged.
