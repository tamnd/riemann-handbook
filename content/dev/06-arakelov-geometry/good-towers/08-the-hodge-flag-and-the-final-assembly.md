---
title: The Hodge flag and the final assembly
decls:
  - GlobalTheory.CompanionTheory.Ar.Num.HodgeModel.model_on_hodge_of_family_pos
  - GlobalTheory.T.model_on_hodge_from_family
  - GlobalTheory.CompanionTheory.Ar.Top.goodTower_volume_of_reduced
  - GlobalTheory.T.final_theorem_of_inputs_right
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The Hodge flag and the final assembly

This section has two results. The first computes the local Chern numbers of the Hodge flag at a place above a prime $\ell$. The answer is a combination of intersection numbers on the fibre at $\ell$, with coefficients that come from the Frobenius action on the labels. The second result is the main theorem of the chapter: from a list of inputs, every global integral model has a good tower, and good towers satisfy the volume theorem. The [base setting](/entry/base-setting-of-good-origin/) of the previous section and the Hodge flag numbers both enter the [volume theorem](/entry/volume-theorem-x-of-inputs/). For the background see [heights](/learn/arakelov/#heights) and [semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction).

Fix a CM field $E$ with host $H$, a datum $D$ of signature $(p, q)$ with $N = p + q$, and a Hodge component $\mathfrak{M}$ with coordinates $y$ in a field $\Omega$ and a set of primes $S$. Assume that the coordinates define an arithmetic variety of dimension $d + 1$. The labels are the elements of two copies of the set of CM types. Each label $s$ has a de Rham lattice $V_{\mathrm{dR}}(s)$ and, at each prime $\ell \in S$, a Hodge Tate lattice $V_\ell(s)$.

A permutation $\varphi$ of the labels is a Frobenius at $\ell$ if $\varphi(s)(a) \equiv s(a)^\ell$ modulo every prime above $\ell$ of the coefficient field, for every label $s$ and every $a \in \mathcal{O}_E$. For $k \ge 1$ and labels $\tau, \sigma$, the Frobenius coefficient is

$$
\operatorname{co}_k(\tau, \sigma) = \sum_{n \ge 0} [\varphi^{n+1} \tau = \sigma]\, \ell^{-k(n+1)} - \frac{[\sigma = \tau]}{\ell - 1}.
$$

A local pair $T$ indexed by a set $\Sigma$ consists of integer weights $x_i$ and $x'_i$ and polynomials $f_i$ and $g_i$ in the coordinates, for each $i \in \Sigma$. Over a discrete valuation ring $O$ with a model $P$ of the coordinates, the local Chern number $\operatorname{ck}_k(T, Q)$ of a local pair with a list $Q$ of classes is the intersection number on the special fibre of the $k$-th power sum of the divisors of the $f_i / g_i$, weighted by $x_i - x'_i$, with the classes $Q$. We do not unfold it. For $m \ge 0$ and a CM type $\tau$, put

$$
\begin{aligned}
\lambda_m(\tau, 1) &= \textstyle\sum_{i < p} x_{(\tau, i)}^{\,m}, \\
\lambda_m(\tau, 2) &= \textstyle\sum_{i \ge p} (-x_{(\tau, i)})^{m},
\end{aligned}
$$

where $(\tau, 1)$ and $(\tau, 2)$ are the two labels of $\tau$.

**Definition 8.8.1 (Flag Chern comparison).** Let $T$ be a local pair indexed by pairs $(\tau, i)$ with $\tau$ a CM type and $0 \le i < N$, and let $T_\tau$ be its restriction to the indices $(\tau, i)$. Then $T$ satisfies the flag Chern comparison at $\ell$ over $O$ if, for every CM type $\tau$, every $k \ge 1$ and every list $Q$ with $|Q| + k = d + 1$,

$$
\operatorname{ck}_k(T_\tau, Q) = \operatorname{cyc}\Big(\operatorname{div}(\ell), x, \; k \sum_{\tau'} \operatorname{co}_k\big((\tau, 1), \tau'\big)\, \lambda_{k-1}(\tau') , \; Q\Big).
$$

Here $\operatorname{cyc}(Z, x, F, Q)$ is the intersection number of the cycle $Z$ with the polynomial $F$ evaluated at the classes $x$ and with $Q$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.FlagChernComparison`

A flag $\mathrm{Fl}$ of $\mathfrak{M}$ gives a basis $b_s$ of the Lie algebra for each label. It has two levels for a set $S_0 \subset S$ and a local pair $T$ if the following hold. The lattice that is the de Rham lattice outside $S_0$ and the Hodge Tate lattice at the primes of $S_0$ is a vector bundle and a flag bundle along $b$. Its root lines have degrees $x$ with generators $e_0$, and the root lines of the flag have degrees $x'$ with generators $e$. Each $f_i / g_i$ takes the value $e_i / e_{0, i}$ at the coordinates, and each pair $(f_i, g_i)$ is vertical off the primes of $S \setminus S_0$.

The input on Hodge Tate lattice families says the following. Let $p + q > 0$, let $b$ be bases of the label spaces, and let $\ell \in S$ be a prime at which $\mathfrak{M}$ is free, with $\ell \ne 2$ and $\ell \nmid d_E$. Let $\varphi$ be a Frobenius at $\ell$. Then at every place $O$ above $\ell$ of the integral closure of $\mathbb{Z}$ in $\Omega$, every label $t_0$ lies in an orbit $e : \Sigma \to$ labels with $e \circ \varphi' = \varphi \circ e$. On this orbit there are a finite field $F$ of characteristic $\ell$, embeddings of $F$ into the residue field of $O$, and Lie lattice data on the charts that form a family at $\ell$. The de Rham and Hodge Tate lattices of the family are those of $\mathfrak{M}$ at the labels $e(\tau)$ and at their partners.

**Theorem 8.8.2 (Chern numbers of the Hodge flag).** Assume the input on Hodge Tate lattice families. Let $\mathrm{Fl}$ be a flag of $\mathfrak{M}$ with two levels for $S_0 \subset S$ and a local pair $T$ with integer coefficients. Let $\ell \in S \setminus S_0$ be a prime at which $\mathfrak{M}$ is free, with $\ell \ne 2$ and $\ell \nmid d_E$, and let $\varphi$ be a Frobenius at $\ell$. Then at every place $O$ above $\ell$ of the integral closure of $\mathbb{Z}$ in $\Omega$, the pair $T$ satisfies the flag Chern comparison at $\ell$ over $O$, with the cut at $p$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.HodgeModel.model_on_hodge_of_family_pos` (also `GlobalTheory.T.model_on_hodge_from_family`, a second name)

*Proof.* If $p + q = 0$, there are no indices, so both sides are $0$. Assume $p + q > 0$. The localization of the integral closure at the place is a discrete valuation ring $O$ with a uniformizer $\varpi$, and the coordinates have a model over $O$ in which $T$ is vertical. The flag gives bases $b$ that are independent and span the label spaces, so the input gives, for each label $t$, an orbit with a finite field $F_t$ and a family $D_t$.

Let $M = \prod_t (|F_t| - 1)$, which is positive. Take an extension $O'$ of $O$ that is a discrete valuation ring and contains a primitive $M$-th root of unity $\zeta$. Then $\zeta^{M / (|F_t| - 1)}$ is a primitive root of order $|F_t| - 1$ for each $t$. The model and the function field move to $O'$.

The Hodge Tate and de Rham lattices agree at the points that lie on no fibre over a prime. With the two levels this gives the degrees of the Hodge flag for each CM type. The Dedekind constants of the arithmetic variety then give lattices with frames for each label, and a compatibility of chart bundles gives the dual lattices. Both descend along the valuations of $O'$.

For each label $t$, the descent of the generic fibre puts the family $D_t$ over $O'$. The arithmetic relations then give numbers $h(\tau)$ on the orbit of $t$ with, for every $k \ge 1$ and $Q$ with $|Q| + k = d + 1$,

$$
\begin{aligned}
\operatorname{ck}_k(\mathrm{lie}_\tau) + \operatorname{ck}_k(\omega_\tau) &= h(\tau) - \frac{\Lambda_k(\tau)}{\ell - 1}, \\
\ell^{\,k}\, h(\tau) &= h(\varphi \tau) + \Lambda_k(\varphi \tau),
\end{aligned}
$$

where $\mathrm{lie}_\tau$ and $\omega_\tau$ are the local pairs of the label and of its dual, and $\Lambda_k(\tau)$ is $k$ times the number of the $(k-1)$-th power sum of the weights of $\mathrm{lie}_\tau$ against the divisor of $\ell$. The local comparison of orbits solves this Frobenius recursion: $\operatorname{ck}_k(\mathrm{lie}_\tau) + \operatorname{ck}_k(\omega_\tau) = \sum_{\tau'} \operatorname{co}_k(\tau, \tau')\, \Lambda_k(\tau')$. The second half of the flag uses the reversed dual, and the local numbers are invariant under the reversal of indices. This gives the flag Chern comparison over $O'$, and the descent along the integral closure brings it down to $O$. $\square$

**Theorem 8.8.3 (Good towers and the volume theorem).** Assume the following inputs.

1. The first part of the integral model theory, the moduli schemes for $1 \le p + q$ and their compactifications, and the toroidal compatibility with the level and with Hecke operators.
2. The key formula, the extension theorem for homomorphisms of semi-abelian schemes, the numerical Segre input, resolution of singularities in characteristic $0$, the Fargues comparison for Hodge Tate lattices and the GAGA input for flat sections.
3. The Siegel lemma for lines of large degree.
4. The inputs of the proof theory, the Hilbert Samuel input, the analytic input and the height bounds for push downs to Grassmannians.
5. The integrability of point integrals and the avoidance input.
6. The quotient by finite flat group schemes, the Zarhin trick and the uniform theta bound for abelian varieties.

Then two statements hold. First, every global integral model with split components, with $p, q \ge 1$, has a root tower of type $(\Phi, p + q)$ with a good origin with the extra conditions. Second, there is $C \ge 0$ with this property. Let $E$ be abelian Galois over $\mathbb{Q}$, let $Y$ be global, let $T$ have a good origin with the extra conditions, and let $\mathrm{II}$ be full. Assume $q \ge 1$, $3q + 1 \le p + q$ and that $T$ has at most $4 f (p + q)^2$ bad primes. Then $T$ is proportional, all its volumes are equal, and it satisfies the bounds T1, B, T2 and the mean slope bound with $C$, $\mathrm{rd}_E$ and $L_H$.

Lean: `GlobalTheory.CompanionTheory.Ar.Top.goodTower_volume_of_reduced` (also `GlobalTheory.T.final_theorem_of_inputs_right`, a second name)

Here T1 says that, for admissible weights $u$ and large $B$, the twisted root lines are nef on the fibres and semipositive, and their top intersections, degrees and slopes converge, with positive limiting degree $\operatorname{vol}(c) \deg u$. The bound B is an asymptotic formula for the intersection numbers of monomials with error $C \log B / B$. T2 is a lower bound of the form $-C (d + 1) \operatorname{vol}\, \deg u\, \beta_B(u)$ for the total intersection number at $u$, and the mean slope bound is the lower bound $-C \beta_B(u)$ for the mean of the slopes over the components, where $\beta_B(u)$ depends on $\mathrm{rd}_E$, $L_H$, $B$ and $u$. We do not unfold these.

*Proof.* The inputs of the first four groups give the top level inputs. The Weil pairing statement holds without hypotheses. The Hodge Tate datum statement and the statement on ordinary curves are proved, and with the Fargues comparison, the quotient by finite flat group schemes and the Zarhin trick they give the input on Hodge Tate lattice families. The inputs of the proof theory, the avoidance input and resolution give the comparison input. The comparison is tied with the Hodge structure, and with the uniform theta bound this gives the comparison pair. The [good tower and volume theorem](/entry/good-tower-volume-theorem/) takes the top level inputs, the integrability of point integrals, the avoidance input, the Weil pairing statement, the family input and the comparison pair, and gives both statements. $\square$

**Remark 8.8.4 (Formalization).** The family input is `Num.FamilyExistsPos`, and the conclusion of the first theorem is `HodgeLatticeFlagBound`. The proof of the first theorem calls `T.arith_variety_coord_ideal`, `T.localization_model_over_place`, `T.exists_dvr_extension_field`, `T.hodge_flag_outside_prime_fibres`, `T.hodge_flag_cm_type_degree`, `T.arith_variety_dedekind_constants`, `T.flag_pair_chart_bundle_compat`, `T.model_descent_valuation_fibre`, `T.model_descent_generic_fibre`, `T.arithmetic_relations_statement_holds`, `T.local_comparison_of_orbits_holds`, `T.flag_m3_from_local` and `T.model_descent_integral_closure`. The second theorem gets `Top.Given` from `T.final_theorem_of_inputs_left`, `Out.WeilSt` from `Link.weilSt`, the family input from `T.family_pos_of_hodge_tate_inputs` with `GR.Top.main` and `T.ordinary_curve_statement_holds`, `Cmp.CmpSt` from `T.comparison_of_inputs_avoidance`, and `Cmp.CmpPair` from `T.cmpPair_of_inputs` with `T.CmpHodgeTied_holds`, and then applies `T.good_tower_volume_theorem`. Its conclusion is `Top.GoodTowerExistsX ∧ Top.VolumeTheoremX`; the bounds are `RootTower.T1`, `ThmB`, `T2` and `MeanSlope`. The hypothesis `Prov.ZhangDimensionPushDownGrassmannianHeightBounds` is bound to the name `hNine` in the proof, although it is not the statement `NineGeoU`.
