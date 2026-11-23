---
id: ansq-exists
title: The analytic square of an adjacent swap
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.PB.WSq.ansq_exists
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.FlagAdjacentSwapSquareSystem
covers: 577
status: drafted
drafted_by: writer@claude
---
This theorem builds the analytic square for one adjacent swap on a flag model $M$. The square lives on a log resolution of the swap variety, with two maps to the analytic flag system and a norm formula for its section. The [statement form](/entry/flag-adjacent-swap-square-system/) passes it to [square systems on a flag cover](/entry/t-c-sqsys/).

## Statement

Assume `Inputs`. Let $M$ be a flag model of type $(N, j)$ over the coordinates $y$, let $\mathrm{BM}$ be a base metric on $M$ and let $\mathrm{FA}$ be analytic flag data of dimension $d$ over $\mathrm{BM}$. Let $\tau \in \Psi$ and let $a, b$ be rows with $b = a + 1$ and $b < j$ or $j \leq a$. Let $k_0$ be the block of $(\tau, a)$, let $c_a$ be the last column of row $a$ (`lastCol`: $N - j + a$ if $a + 1 \leq j$, else $a - j$) and let $c_b = c_a + 1$. Assume that the coordinate ideal of $y$ is an arithmetic variety of dimension $d + 2$.

**Theorem.** There are an analytic square $Q$ at $(\tau, a)$ with coefficients $\xi_{\tau,a}$, a log resolution $R_W$ of dimension $d + 2$ of the coordinate ideal of `M.wCo`, and a map $e \colon R_W \to W$ to the space of $Q$, with these properties.

1. $e$ is holomorphic and of degree one off the empty set.
2. Over $q_0(e(x))$, the points of the flag resolution are in the orbit of the old coordinates of $R_W$.
3. Over $q_1(e(x))$, they are in the orbit of a point $z_1$ that agrees with $R_W$ off $k_0$ and takes the new block on $k_0$.
4. $w \mapsto (q_0(w), q_1(w))$ is injective.
5. For frames $F$ of $M$ that are good at $z_0$, a block diagonal $h$ with $\det h \neq 0$, and $t \neq 0$: if $z_0$ is exact for $h$ and $z_1$ is exact for $h(1 + t E_{c_b c_a})$, then
$$\log\lVert v \rVert(e(x)) + \mathrm{cst} = \log\Bigl\lvert t \prod_i \mu_i^{\xi_{\tau,a}(\tau,i)} \Bigr\rvert + \tfrac12 \sum_p \xi_{\tau,a}(p)\bigl(\log h_p(z_0) + \log h_p(z_1)\bigr).$$
Here $\mu_i = 1$ at a proper step, and otherwise $\mu_i$ is the value of the frame section $\upsilon_{\tau,i}$ at $z_0$ times a principal minor of $h$. The weight $h_p$ is the Fubini-Study metric `fsHerm` of $dy_p$.

## Proof

1. `flag_analytic_dimension_count` gives $d + 1 = n + \lvert\Psi\rvert\bigl(\binom{j}{2} + \binom{N-j}{2}\bigr)$.
2. `flag_adjacent_rows_resolution` gives $R_W$ and a projection to the base.
3. `flag_adjacent_rows_analytic` gives $q_0$ and $q_1$, the two orbit conditions and the injectivity.
4. `snc_adapted_atlas_projection` and `log_resolution_fubini_study_positive` give the simple normal crossings and the positivity on $R_W$.
5. `two_map_pullback_energy` gives the constants, $t_0$ and the singular and regular weights.
6. `flag_adjacent_rows_base_metric` gives $L'$, $v$, $\mathrm{cst}$ and the norm formula.
7. `flag_adjacent_rows_dimension` and `flag_adjacent_rows_log_resolution` give the cover charts and the potentials.

The analytic system of $Q$ is then built on $R_W$ itself. The new index `none` takes $\theta_{\tau,a}$ pulled back by $q_1$, and an old index $p$ takes $\theta_p$ pulled back by $q_0$. Thus $e$ is the identity.

## In the Lean code

The theorem is in [FlagAdjacentSwapSquareSystem.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/FlagAdjacentSwapSquareSystem.lean#L24). We did not unfold the nine lemmas of the proof; they are statement forms. Of `Inputs`, only the part `pullback` is used, at line 54. The map $e$ is `id` at line 155, so the degree condition is `isDegreeOff_id`. The norm formula needs points over $q_0(x)$ and $q_1(x)$; the proof gets them from the fact that $\pi$ of `FA` has degree one with empty branch locus (`FA.deg_one`, `FA.br_empty`, line 152).
