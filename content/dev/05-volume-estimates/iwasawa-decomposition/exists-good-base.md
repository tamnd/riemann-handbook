---
id: exists-good-base
title: A base with a good Hodge metric and its Chern integrals
kind: theorem
decl: GlobalTheory.LieBase.exists_goodBase
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsGoodBase
covers: 1300
status: drafted
drafted_by: writer@claude
---
This theorem supplies the geometry and the analysis for [Mumford proportionality](/entry/mumford-proportionality-of-good-chern-weil/). For a component $Y_k$ of a toroidal flag space it gives a base variety $X$, a vector bundle on $X$ whose full flag bundle is $Y_k$, and a metric on the open part of $X$ that is good in the sense of Mumford. It also computes the Chern integrals of this metric: each one is a covolume times a flag degree. The proof only collects four lemmas.

## Statement

Use the setting and notation of [Mumford proportionality](/entry/mumford-proportionality-of-good-chern-weil/): the data with `GoodEmb` and `IsUnf`, a toroidal flag space $\Phi$, a component $k$, the variety $Y_k$ with divisors $D_{\tau,i}$, the ranks $m_\tau$ ($p$ for $\tau \in \Psi$, $q$ otherwise), the polynomial $Q_\lambda$ and the flag degree $\deg_{\mathrm{Fl}}$.

**Theorem.** There are a smooth projective variety $X$ over $F$, a family $\mathcal{E}$ of vector bundles of ranks $m_\tau$ on $X$, a full flag $\mathcal{E}'$ of $\mathcal{E}$ on $Y_k$, a morphism $f \colon Y_k \to X$ with its map $\varphi$ on function fields, an open $O \subseteq X$ and a metric $h$ on $\mathcal{E}$ over $O$, such that:

1. $\mathcal{E}'$ refines $\mathcal{E}$ along $f$ (`Refines`): each point of $X$ with a frame of $\mathcal{E}$ and a flag has one lift to $Y_k$;
2. $\mathcal{E}'$ is graded by the divisors $D_{\tau,i}$ (`IsGraded`);
3. $h$ is positive definite, smooth, and compatible with changes of frame on $O$ (`IsMetricOn`);
4. $h$ is good at the boundary $X \setminus O$ (`IsGood`);
5. for each weight $\lambda$ and each $R$ with $\operatorname{antisym}(Q_\lambda) = R(e)\,\Delta$, $\int_O R = \operatorname{covol}(U_k)\cdot\deg_{\mathrm{Fl}}(\lambda)$.

## Proof

1. `exists_base_of_flagCpt` gives $X$, an open immersion $j$ of $X$ into the generic fibre of the toroidal model with $j \circ f = \pi$, a frame $f_0$ at the generic point, the bundle $\mathcal{E}$ with a base frame $A_0$, and $\mathcal{E}'$, $\varphi$ with properties 1 and 2. These data form a "Lie base" (`IsLieBase`: $j$ is an open immersion, $j \circ f = \pi$, and the frames of $\mathcal{E}$ are tied to eigenframes of the tangent space).
2. Take $O = j^{-1}(\text{complement of the boundary})$ (`openPart`). Take $h$ = `lieGram`: at a point $y$, the transpose of the Gram matrix of the Hodge metric `hodgeMet` in the eigenframe that matches the frame at $y$, and $0$ when there is no such frame.
3. `isMetricOn_lieGram` gives property 3.
4. `hodgeMetric_lieGram_isGood_mumford` gives property 4.
5. `hodgeMetric_chernIntegral_eq_covolume_mul_flagDegree` gives property 5.

## In the Lean code

The theorem is in [ExistsGoodBase.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsGoodBase.lean#L15). The lemmas:

- `GlobalTheory.LieBase.exists_base_of_flagCpt`, in [ExistsBaseOfFlagCpt.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsBaseOfFlagCpt.lean#L15). It calls `exists_variety_connectedComponent_genericFibre`, `TieBase.exists_tied`, `flagSpace_component_unique_point_each_flag` and `flagSpaceComponent_refines_lie_frames_graded`, which we have not unfolded.
- `GlobalTheory.LieBase.isMetricOn_lieGram`, in [HodgeMetricLieFramesSmoothHermitianOffBoundary.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HodgeMetricLieFramesSmoothHermitianOffBoundary.lean#L111).
- `GlobalTheory.T.hodgeMetric_lieGram_isGood_mumford`, a restatement of `GlobalTheory.LieBaseGood.lieGram_isGood`.
- `GlobalTheory.T.hodgeMetric_chernIntegral_eq_covolume_mul_flagDegree`, a restatement of `GlobalTheory.LieBase.hasChernIntegral_covol_flagDeg`.

The real content is in the last two. `hasChernIntegral_covol_flagDeg` is the mechanism of proportionality. `pointwise_hodge` says that at each point of $O$ the Chern form of $R$ is $\deg_{\mathrm{Fl}}(\lambda)$ times the Chern form of a fixed polynomial `pointPoly` $= \prod_{\tau \in \Psi} \bigl((-1)^p c_p(\mathcal{E}_\tau)\bigr)^{q}$. `hasChernIntegral_pointPoly_covol` says that $\int_O$ `pointPoly` $= \operatorname{covol}(U_k)$. `hasChernIntegral_of_eq_mul` multiplies the two. We have not unfolded the proofs of `pointwise_hodge` and `hasChernIntegral_pointPoly_covol`.

The definitions `IsLieBase`, `openPart` and `lieGram` are in [ExistsIsLieBase.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsIsLieBase.lean#L22). The value $0$ of `lieGram` when no eigenframe matches is a default value. The last step uses `convert … using 3`; we have not checked which terms differ.
