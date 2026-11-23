---
id: vs-fin
title: Bounded denominators of a section read off a tower section
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Plug.vs_fin
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.UniformAllTowerBound
covers: 310
status: drafted
drafted_by: writer@claude
---
This theorem bounds the denominators at the finite places of a section $f$ of the moduli space that is read off an integral section $s$ of a root tower. At a good prime of the tower, $f$ is integral. At a bad prime $p$, the denominator is at most $p^{\varepsilon_p \|u\|_1}$. It reaches [`descent_small`](/entry/descent-small/) through the restatement [`uniform_all_tower_bound`](/entry/uniform-all-tower-bound/).

## Statement

Let $E$ be a CM field, Galois over $\mathbb{Q}$, with a moduli space $X$ and a coefficient field $F$. Let $Z$ be an irreducible component of $X_F$, and $\Omega_Z$ the field of rational functions in the flag variables over the residue field of its generic point. Assume `Top.Given`, `CompLaws U h e` and `Ref.UnifAll`. Let $T$ be a root tower with a good origin, $B \in \mathbb{N}$, $b$ a component of $T$, and $\mathrm{Rd}$ a reading on $Z$: a map $\varphi \colon \Omega_Z \to \Omega$ to the field of the tower, of degree the flag degree, with torus elements $t_i$. Let $u$ be a weight and $a$ its multidegree on the tower. Suppose:

1. for each choice $c$ of a nonzero coordinate $y_{k, c_k}$ in each factor, $s \prod_k y_{k,c_k}^{-a_k}$ is integral over the chart ring (`chartLatNm`);
2. $f$ is a section of weight $\mathrm{ex}(u)$ on frames, and $f$ vanishes at each frame off $Z$;
3. the value of $f$ at the generic frame of $Z$ is $\operatorname{Tr}_{\Omega/\Omega_Z}(s/\gamma)$, with $\gamma$ the gauge of $\mathrm{Rd}$ (`trOf`).

Let $p$ be a prime, $\lambda$ a prime of $\mathcal{O}_F$ above $p$, and $v \in$ `recVals` at $\lambda$: $v(g) = v_R(g(y))/e$ for an integral algebraic point $y$ over a complete discrete valuation ring $R$ of ramification $e$ over $\lambda$. Then
$$v(f) \ge -v_\lambda(p)\,\varepsilon_p\,\|u\|_1, \qquad \varepsilon_p = \begin{cases} \tfrac{1}{p-1} + 40\,\tfrac{v_p(d_E)}{[E:\mathbb{Q}]} + [p = 2] & p \in S_B, \\ 0 & p \notin S_B, \end{cases}$$
with $S_B$ the bad primes of the origin at level $B$ and $\|u\|_1 = \sum_{\tau, i} |u_{\tau,i}|$.

## Proof

If $f(y) = 0$, then $v(f) = \infty$. Otherwise $y$ lies on $Z$. Put $x = s/\gamma$ and $v(f) = e_\lambda s_0$, with $e_\lambda$ the ramification index of $\lambda$ over $p$.

1. `good_origin_model_component_bound` shows that $\mathrm{Rd}$ is linked. The primes that divide $d_E$ are in $S_B$.
2. `uniform_all_root_origin_bound` gives an algebraic $p$-adic point $z$ of the tower and root parameters $\mathrm{rec}_r$ with $|\log \sup_r(z) - \log \mathrm{rec}_r| \le C_\theta \log p$. At $z$ the reading of $f$ has norm $p^{-s_0} \prod_r \mathrm{rec}_r^{n_r}$.
3. `trace_integral_subring_extension` writes the image of $\operatorname{Tr}(x)$ as a sum $\sum_j \mathrm{ev}'_j(x)$ of evaluations of $x$.
4. `weight_section_component_value` moves $y$ to a regular point. `integral_frame_component_value` shows that the image $W$ of $f$ is not $0$.
5. `chart_lattice_specialization_value`, with hypothesis 1, bounds the value of $s$ at $z$ by a sup norm, and `prod_zpow_le` bounds that by $\prod_r \mathrm{rec}_r^{n_r} \cdot p^{C_\theta \|u\|_1}$. So $|\mathrm{ev}'_j(x)| \le p^{s_0 + C_\theta \|u\|_1}\,|W|$ for each $j$.
6. The ultrametric inequality for $W = \sum_j \mathrm{ev}'_j(x)$ gives $s_0 \ge -C_\theta \|u\|_1$.

Last, $C_\theta \le \varepsilon_p$ and $v_\lambda(p) = e_\lambda$.

## In the Lean code

The theorem is in [UniformAllTowerBound.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/UniformAllTowerBound.lean#L28). The lemmas of steps 1 to 5 and `tower_weight_of_zero` are `GlobalTheory.T` restatements. We have read their statements, not their proofs.

The constant $\varepsilon_p$ is `exTwo E p` in [ModelSmall.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ModelSmall.lean#L50), built on `htEx` in [SemiposAtOfPositive.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SemiposAtOfPositive.lean#L76). The proof uses $C_\theta = \frac{1}{p-1} + [p=2] + \frac{v_p(d_E)}{[E:\mathbb{Q}]}$ for $p \in S_B$, with the factor $1$ where `htEx` has $40$. So the stated bound is weaker than the one proved.
