---
id: relay-cusp-weight-regularisations-tied
title: A cusp weight and two tied regularisations of the Hodge line
kind: theorem
decl: GlobalTheory.CompanionTheory.Relay.cusp_weight_regularisations_tied
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.CuspWeightRegularisationsTied
covers: 685
status: drafted
drafted_by: writer@claude
---
On one component of the Shimura variety, this theorem gives a cusp weight $U$ and two regularisations: one of the metric of the Hodge line $\overline\mu$, one of the potential $\log h_\mu + U/2$. It joins seven lemmas. Its statement form is [`T.cusp_weight_regularisations_tied`](/entry/t-cusp-weight-regularisations-tied/). Its result goes to [the base degree setting](/entry/base-setting-of-good-origin/), which feeds the slope bound of [the volume theorem](/entry/volume-theorem-x-of-inputs/).

## Statement

Let $X \subset \prod_{k \in K} \mathbb{P}^{J_k}$ be the arithmetic variety of a component datum $D_c$ (`ComponentData`), of dimension $n + 1$ with $n = f\,j\,(N-j)$ and $f = \#\mathrm{CMType}(H)$. It has a closed boundary $\partial$, stable under the torus $(\mathbb{C}^\times)^K$ and under conjugation; $X^o = X(\mathbb{C}) \setminus \partial$. A Hodge datum $H_d$ gives a hermitian line $\overline\mu$ of multidegree $a_\mu$, with metric built from adapted frames of the Hodge bundles; write $\varphi_\mu = \log h_\mu$. A component origin $O$ (`CptOrigin`) ties $D_c$ to a Hodge component $\mathfrak M$ of the model $Y$, with a side $s$.

A *cusp weight* (`IsCuspWeight`) is a function $U$ such that at each interior complex point of $\mathfrak M$ with coordinates $w$, the fibre is a Riemann lattice $R$ with embeddings $\sigma$ on the side $s$, and $U(w) = \max\bigl(0, \sup_I (-\log \mathrm{nz}_\sigma(I))\bigr)$ over the cusps $I$ of $R$. We have not unfolded `RiemLat.nz`.

**Theorem.** Assume `Top.Given` (see [the good tower theorem](/entry/good-tower-and-volume/)). Let $E$ be an abelian CM field and $D_c, H_d, O$ as above. Then there are a function $U$, a complex model $M$ of $X$ (`XModel`), a log-log regularisation $S$ of $\overline\mu$ and a bounded regularisation $S'$ of degree $a_\mu$ with potential $w_U = \varphi_\mu + U/2$ (`corrW`), such that:

1. $U$ is a cusp weight for $O$;
2. $U \geq 0$;
3. $U(c \cdot z) = U(z)$ for $z \in X^o$ and $c \in (\mathbb{C}^\times)^K$;
4. $S$ and $S'$ are tied: an error $e_1(t) \to 0$ as $t \to 0^+$ bounds the difference of the regularised potentials of overlapping charts (for $S$ also $K(t) \to \infty$, $K(t) \geq C \log\log t^{-1}$);
5. `ConjU`: for $B \geq 4f + 2$ and $1 \leq p \leq q$, the twisted line $\overline M_{B,p,q,t'}$ of $S'$ is conjugation invariant for small $t' > 0$.

## Proof

1. `T.intersection_system_weight_left` gives a cusp weight $U \geq 0$, invariant under the torus and under conjugation.
2. `T.cusp_intersection_positive`: $\varphi_\mu$ and $w_U$ are plurisubharmonic and continuous on the charts off $\partial$.
3. `T.cusp_chart_log_growth_bounds`: $w_U$ is locally bounded on the charts.
4. `Relay.hodge_metric_frame_properties`: $\varphi_\mu(c \cdot z) = \varphi_\mu(z) + \sum_k a_{\mu,k} \log|c_k|$ on $X^o$, and $\varphi_\mu$ is conjugation invariant there.
5. `Relay.exists_compactified_model` gives $M$, and `T.exists_regularization_of_hodge_metric` gives a tied $S$ from step 2.
6. `T.exists_regularization_setting`, applied to $w_U$, gives a tied $S'$ with `ConjU`. Its hypotheses come from steps 1 to 4.

## In the Lean code

The theorem is in [CuspWeightRegularisationsTied.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/CuspWeightRegularisationsTied.lean#L27). The proof is 17 lines. Only the first three lemmas take `Top.Given`.

Some parts of the lemmas are discarded: the uniqueness of $U$ on $X^o$ from step 1, and the bound of $U$ and $|\varphi_\mu|$ by $C \log$ of the chart function `logR` from step 3. Step 1 gives torus invariance at all points; conclusion 3 keeps it only on $X^o$. We have read the statements of the seven lemmas, not their proofs.
