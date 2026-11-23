---
id: line-of-key
title: Short Lie vectors have bounded degree, by theta functions and jets
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Sl.LineProof.line_of_key
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.LineOfKeyDegree
covers: 809
status: drafted
drafted_by: writer@claude
---
This theorem bounds the degree of each line in the Lie bundle of a principally polarized semi-abelian scheme by $C \log(2 + g + h)$. It assumes the key degree bound on theta sections. Through the renaming [`T.line_of_key_degree`](/entry/line-of-key-degree/) it gives the constant $C$ of [`TopSlope.slopeBound`](/entry/top-slope-slope-bound/).

## Statement

**Theorem.** `KeyDegSt` implies `LineSt`: there is $C \ge 0$ such that for each principally polarized semi-abelian datum $D$ over a number field $L$ and each $x \ne 0$ in its Lie bundle $B$,
$$-\operatorname{mean}_\sigma \log |x|_\sigma \le C \log(2 + g + h), \qquad g = \operatorname{rk} B, \quad h = \max(-\widehat{\deg}_n \overline{B}, 0).$$
Both statements are given in words in [the renaming](/entry/line-of-key-degree/).

At an embedding $\sigma$, an archimedean frame is a uniformization $\mathbb{C}^g \to A_\sigma$ with a lattice $\Lambda$, a hermitian form $H$ and a multiplier $\chi$. A section of the $n$-th power of the polarization is a theta function $\theta$ of level $n$, with norm $\|\theta(w)\| e^{-\pi n H(w,w)/2}$. The vector $x$ gives a tangent vector $c_x \in \mathbb{C}^g$ with $|x|_\sigma^2 = \pi H(c_x, c_x)$ (`theta_function_archimedean_frame`).

## Proof

The proof is an auxiliary-section argument with jets along the direction $c_x$.

1. **Setup.** `g_pos` gives $g \ge 1$, since $x \ne 0$. `KeyDegSt` gives an extension $L_1$ and a theta section $\theta$ with $\operatorname{mean} \log b_\sigma \le \Phi = \frac h2 + C_1 g$.
2. **Sup norms.** [`exists_theta_sup_bound_log_mean`](/entry/exists-theta-sup-bound-log-mean/) turns the mean-square bound into sup bounds $M_\sigma$ with $\operatorname{mean} \log M_\sigma \le \Phi + C_3 g \log(2 + g + \Phi)$.
3. **Many sections.** Let $m = 3K$ with $K = \lceil 2 + g^2 + h \rceil$. `exists_theta_sections_bounded` gives, over $L_2$, $r = m^{2g}$ sections $s_j$ of level $m^2$ with sup norms at most $M_\sigma$, which span all theta functions of level $m^2$ at each frame.
4. **The jet inequality** (`core_applied`, with $n' = 3K^2$ and $m^2 = 3n'$). `exists_integral_jet_basis` gives vectors $J_i \in L^r$ whose combinations with $\mathcal{O}_L$ coefficients are the $i$-th derivatives of $\sum_j c_j s_j(\tau c_x)$ at $\tau = 0$, integral once the lower jets vanish. `integral_flag_embedding_criterion` then gives
$$0 \le \sum_{i=0}^{n'} \sum_\sigma \log A_i(\sigma),$$
once two facts hold for each $i \le n'$. First, some combination has vanishing order exactly $i$. This comes from `theta_derivative_bound`, a theta function of level $3n'$ with that order, and the spanning property. Second, $|\text{jet}_i| \le A_i(\sigma)\,\|c\|$, with $A_i(\sigma) = (e\, m^2 n')^{i/2} |x|_\sigma^i \sqrt r\, M_\sigma$. This comes from `sum_bound` (a Gaussian growth bound of the combination) and `iterated_deriv_bound_gaussian_growth` (a Cauchy estimate).
5. **Solving.** `slope_sum` turns the inequality into
$$-\operatorname{mean} \log |x|_\sigma \le \tfrac12 \log(e\, m^2 n') + \tfrac{2}{n'}\bigl(g \log m + \operatorname{mean} \log M_\sigma\bigr).$$
Lengths and means do not change under the extensions (`polarized_data_field_extension`, `mean_comp`).
6. **The constant.** `SlopeParameterChoice.full` is a lemma about real numbers. With the bound of step 2, it gives $C_4$ with the right side at most $C_4 \log(2 + g + h)$. Take $C = \max(C_4, 0)$.

## In the Lean code

The theorem is in [LineOfKeyDegree.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/LineOfKeyDegree.lean#L269). The helpers `slope_sum`, `mean_comp`, `sum_bound`, `g_pos`, `len_pos`, `theta_on_ext` and `core_applied` are in the same file. The lemmas from other files:

- `exists_theta_sup_bound_log_mean`, `exists_theta_sections_bounded`, `exists_integral_jet_basis`, `integral_flag_embedding_criterion`, `theta_derivative_bound`, `theta_multiplier_quadratic_character`, `iterated_deriv_bound_gaussian_growth`, `theta_function_archimedean_frame`, `section_sup_norm_field_extension` and `polarized_data_field_extension`, all `GlobalTheory.T` restatements;
- `SlopeParameterChoice.full`, in [Assembly.lean](lean:GroundTheory/HeightsAndTheta/Heights/FactorialBounds/Assembly.lean#L27).

We have read their statements, not their proofs. `HasTheta` and `SupLe` quantify over all archimedean frames. Their content depends on `theta_function_archimedean_frame`, which says that frames exist.
