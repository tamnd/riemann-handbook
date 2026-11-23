---
id: ht-u-of-given
title: A lower bound for the heights of points for the twisted cusp lines
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Cusp.TopHt.htU_of_given
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.CuspHeightUpper
covers: 394
status: drafted
drafted_by: writer@claude
---
This theorem proves the second of the three parts of `NineGeoU`, the height bound `HtU`, with one constant $C_h$ for all data. Its statement form is [`T.cusp_height_upper`](/entry/cusp-height-upper/), and [`nineGeoU_of_given`](/entry/nine-geo-u-of-given/) takes $C_h$ from it. The proof computes the [height](/learn/arakelov/#heights) of a point as a finite part plus an archimedean part, writes the finite part as minus a degree of a lattice, and bounds that degree.

## Statement

We use the notation of [the constants entry](/entry/nine-geo-u-of-given/): the component datum $D_c$ with $f$, $N$, $j' = N - j$, the constant $K_A$ and the line $\overline A'$; the cusp weight $U$; the bounded regularisation $S'$ with potential $\log h_\mu + U/2$; the twisted line $\overline M_{B,p,q,t'}$ (`MUc`); and $\Lambda_B = \log(B\,\mathrm{rd}_E) + |L_H|$.

**Theorem.** Assume `Top.Given` and `FlatDegree`. Then there is $C_h$ such that for all data over an abelian CM field $E$, if $II$ is a full intersection system, the component origin is admitted at some $B_1$, $U$ is a cusp weight and $S'$ is tied, then `HtU` holds: for $B \geq 4fN^2$ and $1 \leq p \leq q$ there is $t_0 > 0$ such that for $0 < t' \leq t_0$ and each point $P$ of the component,
$$\frac{II(P;\, \overline M_{B,p,q,t'})}{q\,\deg P} \geq -C_h\, f\, j'\, \Lambda_B - \frac{p}{q} K_A.$$

## Proof

1. `T.phiDeg_fibLat_le_of_isOFamily_of_isAdapted` (from `Top.Given` and `FlatDegree`) gives $C \geq 0$: for each admitted origin and each algebraic point with adapted families, a degree `phiDeg` of the fibre lattices is at most $C f j' \Lambda_B$. We take $C_h = C$. We have not unfolded `phiDeg`.
2. `T.regularized_weight_dominates_eventually` uses that $S'$ is tied. For small $t'$, the regularised weight $\psi_{t'}$ dominates the potential of $S'$, and $\overline M_{B,p,q,t'}$ is smooth with $\log \|\cdot\| = q(\log h_{\mathrm{ref}} + \psi_{t'} + \sum_{r \in S_B} \log v_r) + p \log h_{A'}$ on the points of the component. We take $t_0$ as half of that range.
3. `T.height_of_zero_dim_variety` writes $P$ as the coordinate ideal of a point $w$ over a number field $L_0$, with $II(P; \overline L)/\deg P$ equal to the height of $w$ for each smooth $\overline L$. The field `heights` of $D_c$ gives $h_{\overline A'}(w) \geq -K_A$.
4. `T.small_points_over_number_field` extends $w$ to an integral point $z$ of the Hodge component over a larger field $L$, with an abelian part and a linear point $A$. `T.cusp_correspondence_bound` gives $2\,\#\mathrm{CMType}(H) = [E:\mathbb{Q}]$. Then `T.adapted_family_exists_on_eigenspace` gives a family $v$ and, for each CM type $\tau$, an adapted family $q_\tau$ in the eigenspace of $\tau$, with $r + k = j'$.
5. `T.cusp_intersection_height` gives archimedean numbers $x_e$, one for each $e \colon L \to \mathbb{C}$, such that the finite part of the height plus $\frac{1}{[L:\mathbb{Q}]}\sum_e x_e$ equals $-\mathrm{phiDeg}$. `T.cusp_intersection_finite` uses that $U$ is a cusp weight: $x_e \leq \psi_{t'} + \log h_{\mathrm{ref}}$ at $e(w)$.
6. `lineHt_decomp` splits the height: $h_{\overline M}(w) = q\,(\text{finite part} + \text{archimedean part}) + p\, h_{\overline A'}(w)$. `T.line_height_invariant_scaling` shows that the heights do not change from $L_0$ to $L$. Steps 1, 3 and 5 give the bound.

## In the Lean code

The theorem is in [CuspHeightUpper.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/CuspHeightUpper.lean#L120), with its helpers, among them `lineHt_decomp`. `HtU` and `admitted` are in [NineGeoU.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/NineGeoU.lean#L32).

Each hypothesis is used. Of `IsFullIntersectionSystem` only the first part is used, and of `admitted` the proof takes `Or.Good` separately and passes the whole condition to step 1. The name `cusp_height_upper` says "upper", but the statement is a lower bound for heights. It is an upper bound only for $-h$, or for `phiDeg`.
