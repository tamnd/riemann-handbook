---
title: Growth of cusp sections and the flag degree
decls:
  - GlobalTheory.T.uniform_norm_degree_bound
  - GlobalTheory.CompanionTheory.Ar.Plug.topGrowth
  - GlobalTheory.T.growthOn_le_vol_mul_flagDeg
  - GlobalTheory.CompanionTheory.Ar.Plug.growth_le_vol_deg
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Growth of cusp sections and the flag degree

The volume slope of the last section is normalized by the top degree $\delta_Z(u)$ of a weight on a component. This section computes the top degree. It proves that the number of cusp sections of weight $\tau u$ on a component $Z$ grows like $\tau^D / D!$ times the volume of the component in the tower times the degree of the flag variety for the weight $u$. So the top degree is positive, and it is a product of a volume and a Weyl dimension factor. The result is used in the [comparison of slopes](/entry/slope-sub-cost-le-comp-vol-slope/), where $\delta_Z(u) > 0$ is a hypothesis.

We keep the setting of the last section, and we assume the arithmetic Riemann-Roch statement for nef lines and the top level inputs. We have the component laws, a real $x$ with $|\tau(\xi_0)| = x$, a model $Y$ over $\mathcal{O}_F$, a root tower $T$ with a good origin, the bijection $\kappa$ between components of $X_o$ and of the tower, and an intersection system $\mathrm{II}$ that is full, proportional and has property T1. We write $D$ for the dimension of the flag variety.

### Growth and the flag degree

**Definition 8.17.1 (Growth).** For a function $r: \mathbb{N} \to \mathbb{N}$ put
$$
\mathrm{growth}_D(r) = \limsup_{\tau \to \infty} \frac{D! \, r(\tau)}{\tau^D} \in [0, \infty] .
$$
For a component $Z$ and a weight $G$ let $\mathrm{Cusp}_Z(\tau G)$ be the space of cusp sections of weight $\tau G$ that vanish at every other component $Z' \ne Z$, and put
$$
\mathrm{growth}_Z(G) = \mathrm{growth}_D \bigl( \tau \mapsto \mathrm{rk}_F \, \mathrm{Cusp}_Z(\tau G) \bigr) .
$$

For a weight $u = (u_{\tau,i})$ put
$$
\mathrm{vdm}(u) = \prod_{\tau} \prod_{i < k} (u_{\tau,i} - u_{\tau,k}) ,
$$
the Vandermonde product over the embeddings. Let $u_0$ be the standard weight. Put
$$
\begin{aligned}
v_0(Z) &= \frac{\mathrm{growth}_Z(u_0)}{\mathrm{vdm}(u_0)} , \\
\mathrm{top}_Z(u) &= v_0(Z) \, \mathrm{vdm}(u) .
\end{aligned}
$$
So $\mathrm{top}_Z(u)$ is the top degree $\delta_Z(u)$ of the last section.

**Definition 8.17.2 (Flag degree).** For a weight $\lambda$ the flag degree is the degree of the line bundle of $\lambda$ on the flag variety:
$$
\mathrm{flagDeg}(\lambda) = D! \prod_{\tau} \prod_{i < k} \frac{\lambda_{\tau,i} - \lambda_{\tau,k}}{k - i} .
$$

This is the Weyl dimension formula, read at the top degree. The weight $\mathrm{re}(u)$ is the weight of $u$ in the coordinates of the flag variety; the formula gives
$$
\mathrm{flagDeg}(\mathrm{re}(u)) = C \, \mathrm{vdm}(u), \qquad C = D! \prod_\tau \prod_{i<k} \frac{1}{k - i} .
$$
So the flag degree and the Vandermonde product differ by a constant that depends only on the shape.

### The upper bound

**Lemma 8.17.3 (Growth is at most volume times flag degree).** For each component $Z$ and each weight $u$ with strictly decreasing rows,
$$
\mathrm{growth}_Z(\mathrm{wt}(u)) \le \mathrm{vol}_T(\kappa Z) \cdot \mathrm{flagDeg}(\mathrm{re}(u)) .
$$

Lean: `GlobalTheory.T.growthOn_le_vol_mul_flagDeg` (also `GlobalTheory.CompanionTheory.Ar.Plug.growth_le_vol_deg`, a second name).

*Proof.* There are two steps. First we compare the cusp sections on $Z$ with the sections of a line bundle on the tower; then we count the latter by the arithmetic Riemann-Roch statement for nef lines.

For the first step we need a rule on lattices. Let $V$ be a vector space over a number field $K$, and let $f_1, \dots, f_d$ be traces from $V$ to $\mathbb{Q}$ with a nondegenerate joint pairing. Then every lattice that contains the images has rank at least
$$
\mathrm{rk}_K V \cdot [K : \mathbb{Q}] \cdot d .
$$
The generic frame bound on components gives these traces on the cusp sections, so the rank of $\mathrm{Cusp}_Z(\tau G)$ times a fixed $\delta > 0$ is at most the number $R(\tau + k_0)$ of sections of the combined line bundle on the tower component $\kappa Z$, for a fixed shift $k_0$. The components of the tower have compatible laws, and the tower weight of $0$ is $0$, so the shift only adds a fixed weight.

For the second step, the combined line bundle is nef on the real tower, by the nef polarization and the general nef result for real towers. The section count result says that
$$
\frac{D! \, R(\tau)}{\tau^D} \to \mathrm{geomDeg}(L_{\mathrm{comb}}) .
$$
The geometric degree of the combined line is computed in two cases: in degree one it is the volume of the component, and at the top it is the flag degree times the volume. Proportionality is used here.

Now the growth rule ends the proof: if $r(\tau) \delta \le R(\tau + k_0)$ and $D! R(\tau)/\tau^D \to L$, then $\mathrm{growth}_D(r) \le L/\delta$. The shift $k_0$ does not change the limit. With $\delta$ chosen by the uniform section count, the bound is the one stated. $\square$

### The growth theorem

**Theorem 8.17.4 (Growth of cusp sections).** Assume the arithmetic Riemann-Roch statement for nef lines and the top level inputs, and keep the setting above.

1. For every weight $u$ with strictly decreasing rows and every component $Z$,
$$
\begin{aligned}
\mathrm{growth}_Z(\mathrm{wt}(u)) &= \mathrm{top}_Z(u) , \\
\mathrm{top}_Z(u) &= \mathrm{vol}_T(\kappa Z) \cdot \mathrm{flagDeg}(\mathrm{re}(u)) ,
\end{aligned}
$$
and $\mathrm{top}_Z(u) > 0$.
2. $v_0(Z) > 0$ for every component $Z$.
3. If the tower has equal volumes on all components, then $v_0(Z)$ does not depend on $Z$.
4. For a tower weight $a$ whose tower weight is regular dominant,
$$
\mathrm{vol}_L(a, Z) = \mathrm{vol}_T(\kappa Z) \cdot \mathrm{flagDeg}(\mathrm{tw}(a)) ,
$$
where $\mathrm{vol}_L(a, Z) = \limsup_n D! \dim \mathrm{Cusp}_Z(n a)/n^D$.

Lean: `GlobalTheory.T.uniform_norm_degree_bound` (also `GlobalTheory.CompanionTheory.Ar.Plug.topGrowth`, a second name).

*Proof.* For part 1, the lemma gives the upper bound. The uniform norm height count gives the lower bound: it produces, for each $\tau$, enough cusp sections of weight $\tau\,\mathrm{wt}(u)$ on $Z$ with small norm, and their number grows at least like the same product. So
$$
\mathrm{growth}_Z(\mathrm{wt}(u)) = \mathrm{vol}_T(\kappa Z) \cdot \mathrm{flagDeg}(\mathrm{re}(u)) .
$$
The volume of a component of a good tower is positive, and the flag degree of a weight with strictly decreasing rows is positive, since each factor $\lambda_{\tau,i} - \lambda_{\tau,k}$ with $i < k$ is positive. So the growth is positive.

The standard weight has strictly decreasing rows. Apply the equality to $u_0$ and divide by $\mathrm{vdm}(u_0) > 0$:
$$
v_0(Z) = \frac{\mathrm{vol}_T(\kappa Z) \cdot C \, \mathrm{vdm}(u_0)}{\mathrm{vdm}(u_0)} = C \, \mathrm{vol}_T(\kappa Z) .
$$
This gives part 2, and part 3, since $C$ depends only on the shape. Then
$$
\mathrm{top}_Z(u) = C \, \mathrm{vol}_T(\kappa Z) \, \mathrm{vdm}(u) = \mathrm{vol}_T(\kappa Z) \cdot \mathrm{flagDeg}(\mathrm{re}(u)) ,
$$
which is the rest of part 1.

For part 4, a regular dominant tower weight comes from an integral weight $u$ with strictly decreasing rows, with $\mathrm{tw}(a) = \mathrm{re}(u)$. The growth is a limit and not only an upper limit, by part 1 and the convergence of the section counts. So the real upper limit $\mathrm{vol}_L(a, Z)$ equals the growth, and part 1 gives the value. $\square$

So the top degree $\delta_Z(u)$ is positive for every regular weight, and on a tower with equal volumes it is the same on all components. This is the normalization that makes the mean volume slope of the last section well defined.

**Remark 8.17.5 (Formalization).** The name `uniform_norm_degree_bound` speaks of a norm bound, but the conclusion is an equality of growths; it is a renaming of `topGrowth` proved by `first | exact @...`, and so is `growthOn_le_vol_mul_flagDeg` of `growth_le_vol_deg` (UniformNormHeightEstimate.lean:284). Both statement files, UniformNormDegreeBoundStatement.lean and UniformNormHeightEstimateStatement.lean, import `Mathlib` twice (lines 1 and 3), and they remove the instance `GlobalTheory.CompHt.fintypePsi` by `attribute [-instance]`. In UniformNormDegreeBound.lean the lemmas `vdm_inst` (line 93) and `dimFlag_eq` (line 97) are proved by `first | rfl | convert rfl | congr 1`; they only match two instances of the same finite type, which looks like an instance diamond. The lower bound is the result `T.uniform_norm_height_count` (UniformNormDegreeBound.lean:139), which has no entry in the outline. The growth is an upper limit in $[0, \infty]$ (AevalEqZeroOfMemConeIdeal.lean:371), and `vZero` and `topDeg` are defined from it (IsHomogeneousCompIdeal.lean:221 to 230). We do not unfold the combined line bundle or the uniform section count.
