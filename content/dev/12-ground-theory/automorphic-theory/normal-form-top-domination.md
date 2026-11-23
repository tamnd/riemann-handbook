---
id: normal-form-top-domination
title: Domination of the cut-off top-degree integrand
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutBP.CompactFormNormalFormDomination.normal_form_top_domination
module: CompanionTheory.AutomorphicTheory.CompactTopologicalForms.NormalFormTopDomination
covers: 575
status: drafted
drafted_by: writer@claude
---
This theorem gives the domination hypothesis for a limit of integrals of cut-off functions. The endpoint bounds that feed [the weighted one-place Bessel bound](/entry/wave-bessel-period-threshold/) use it. Its proof is one line. The real content is in the lemma `nfTopDomAll_of_ptwC`, which this theorem reaches through two wrappers.

## Statement

For a function $F$ on the group, let $\mathrm{cut}(\chi, F, \varepsilon)(g) = \chi(G(g)/\varepsilon) F(g)$. Here $\chi$ is a smooth cutoff that vanishes near $0$ and equals $1$ on $[1, \infty)$. For a word $w$, let $\mathrm{top}_w(F)$ be the function of $c \in \mathbb{C}^{r+1}$ given by the local term $E_w$ of $F$ at the big-cell point with coordinates $c$.

**Theorem.** For each $C_b$ there is $C_c$ with this property. Let $f$, $A_0$, $p_0$, $\chi$ and $N$ satisfy `NFHyp` $C_b$ $C_c$: $\chi$ is a cutoff as above, the place satisfies `InDDplus2` at $C_b$, $f$ is smooth, $f$ lies in `InCC` $A_0$ $m$ for all $m$, $C_c (r+1)^4 (N n^2 + n^3) \leq A_0 - (2r+2)p_0$, and $N \leq 2p_0$. Let $F$ be the modified function `fpm p f id p₀`. Then for each admissible word $w$ of length at most $N$:

1. for small $\varepsilon > 0$, $\mathrm{top}_w(\mathrm{cut}(\chi, F, \varepsilon))$ is a.e. strongly measurable;
2. there is one integrable $h$ with $|\mathrm{top}_w(\mathrm{cut}(\chi, F, \varepsilon))| \leq h$ a.e., for small $\varepsilon > 0$.

These are the hypotheses of the dominated convergence theorem as $\varepsilon \to 0^+$.

## Proof

The proof is `nfTopDomAll_of_tieC` applied to `normal_form_hat_compact`, a pointwise bound of the type `NFTieHatC`. That lemma calls `nfTopDomAll_of_C` with two more proved inputs, `normal_form_hat_product_bessel` and `normal_form_jacobi_cutoff`. It calls `nfTopDomAll_of_ptwC`. There, the integrand is bounded at each point by finitely many differential operators of $f$, with one constant $M$. Each operator gives an integrable function $h_t$ by `dominated_L2_truncation_bound_holds`. The dominating function is $h = M \sum_t |h_t|$.

## In the Lean code

The theorem is in [NormalFormTopDomination.lean](lean:CompanionTheory/AutomorphicTheory/CompactTopologicalForms/NormalFormTopDomination.lean#L10). `NFTopDom` and `NFTopDomAll` are in [CutLimENF.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutLimENF.lean#L23); `limEvT_of_NF` there applies dominated convergence. `nfTopDomAll_of_ptwC` is in [NFDomC.lean](lean:CompanionTheory/AutomorphicTheory/DiscreteGroupWaves/NFDomC.lean#L12). The file of the theorem also proves `thmBpAt_top` and `thmBpAt_eqR_top`, which pass this theorem to `thmBpAt_dom` in [FinalC.lean](lean:CompanionTheory/AutomorphicTheory/CompactTopologicalForms/FinalC.lean#L21). There it is used twice: as the domination input and, through `nfTopIdAll_of_dom`, to prove the identity `NFTopId`. We have not unfolded `Ew`, `fpm` or `InCC`.
