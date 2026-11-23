---
id: word-bound-cpt-coef
title: The word bound for compactly supported coefficients
kind: theorem
decl: GlobalTheory.HatNF.wordBound_cptCoef
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.WordBoundCompactSupportCoefficients
covers: 340
status: drafted
drafted_by: writer@claude
---
This theorem moves a pointwise bound for word operators from the radial picture to the group picture. The radial bound is [`T.wordOperator_radial_pointwise_bound`](/entry/word-operator-radial-pointwise-bound/). Here it becomes a bound at the big-cell points of a place datum $p$, for coefficients $f$ with compact support. The restatement [`T.wordBound_compactSupportCoefficients`](/entry/word-bound-compact-support-coefficients/) gives it a second name, and [`HatNF.wordBound_decay`](/entry/word-bound-decay/) uses it.

## Statement

Let $a \colon \mathbb{N} \to \mathbb{N}$ satisfy `BasicLiftAll a`: for all real place data and normal form data $d$, each basic element of $d$ lies in the span $\mathrm{nfSpan}(d, T, 0, a(r), 1)$. Here $T$ is the set of radial operators that are radial parts of polynomial differential operators of order at most $2r+k+1$ with coefficients of degree at most $8(r+1)(2r+k+1)$.

Let $p$ be a place datum (`KB.Pl`) for the parameter $P = (k, r, \dots)$, and $w$ a word whose letters lie on the cut and differ pairwise by more than $2$ (`KB.CutWord`). Write $N = |w|$, $G_p$ for the function `TBB.Gp p` and $\gamma_c$ for the big-cell point of $c \in (\mathbb{C}^\times)^{r+1}$. Let $\vartheta = x\frac{d}{dx}$.

**Theorem.** There are $C \ge 0$, $J \in \mathbb{N}$ and a list $\Theta_1, \dots, \Theta_m$ of polynomial differential operators, of order at most $N(2r+k+1)$ and coefficient degree at most $8N(r+1)(2r+k+1)$, with this property. Let $\varphi$ be smooth on $\mathbb{R}$ and let $f$ have compact coefficients (`KB.CptCoef`: smooth on $G$, bounded support, and $G_f \ge \varepsilon > 0$ on the support). Put $(\varphi f)(g) = \varphi(G_f(g)) f(g)$. Then for each index $e$ and each $c$ with $G_p(\gamma_c) > 0$,

$$\|V(\Theta_{w,e}(\varphi f))(\gamma_c)\| \le C\, \Bigl|\prod_l c_l\Bigr|^{-N} G_p(\gamma_c)^{-a(r)N} \sum_{j=0}^{J} |\vartheta^j\varphi(G_p(\gamma_c))| \sum_{i=1}^{m} \|V(\Theta_i f)(\gamma_c)\|.$$

Here $\Theta_{w,e}$ is the top lift of $p$ and $V$ is the vector map `p.V`.

## Proof

1. The field `p.hΘ` gives data $X, \mu, L, \mathrm{st}$ and the fact that the top lift of $p$ is the radial word operator in the group picture (`IsTopLift2`). `normal_form_actual` gives normal form data $d$. `JCTx5.wordOK_of` shows that the positioned word is admitted.
2. `T.wordOperator_radial_pointwise_bound` gives $C$, $J$ and lists $H$ of $N$ elements of $T$.
3. Each product $\prod H$ has a polynomial lift of order $N(2r+k+1)$ (`polyLift_listProd`, by induction from `T.polyLift_one_mono_mul`). These lifts are the $\Theta_i$.
4. For given $\varphi, f$: `T.radial_picture_smul_cutoff_G_multiplier`, `mulG_exists`, `compact_support_facts` and `P5.radJFExists` give the radial pictures of $f$ and of $\varphi f$. `T.bigCellVector_norm_eq_radialValue_norm` gives a radial point $x$ with $g_R(x) = G_p(\gamma_c)$, $d_R(x) = |\prod c_l|$ and a factor $\lambda > 0$ that turns radial norms into norms at $\gamma_c$.

Multiply the radial bound by $\lambda$. The rest is bookkeeping.

## In the Lean code

The theorem is in [WordBoundCompactSupportCoefficients.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/WordBoundCompactSupportCoefficients.lean#L29). `WordBound` and `BasicLiftAll` are in [BasicLiftAll.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/BasicLiftAll.lean#L21). The helper `polyLift_listProd` is at line 17.

The constant $C$ depends on $p$ and $w$, not on $\varphi$, $f$, $e$ or $c$. For lists $H$ outside the chosen family, the proof picks an arbitrary lift; these are never used. We have not unfolded `KB.Pl`, the top lift `Top.TopLift` or `p.V`.
