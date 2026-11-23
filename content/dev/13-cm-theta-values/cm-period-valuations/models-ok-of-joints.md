---
id: models-ok-of-joints
title: Good local models from joints at each site
kind: theorem
decl: GlobalTheory.TwV.modelsOK_of_joints
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.ThetaLocalModelsOfSplitUnramifiedJoints
covers: 2340
status: drafted
drafted_by: writer@claude
---
This theorem proves the local model condition `ModelsOK` from a joint at each site. It chooses, at each site, the level structure of a joint and the chain that the joint gives, and it proves the two conditions of `ModelsOK` at that site with [`jointSite_chain_compared_carries_admittedSystem`](/entry/joint-site-chain-compared-carries-admitted-system/). [`modelsAt_of_part`](/entry/models-at-of-part/) uses it in the restated form [`thetaLocalModels_of_splitUnramified_joints`](/entry/theta-local-models-of-split-unramified-joints/). Of the 2,340 declarations below this theorem, 2,335 are below the site lemma.

## Statement

Let $D$ be a datum of type `D7` with size data $L$ (of scale $\varepsilon$), ties $h_T$, instances $G_i$ and $G_l$, division data $D_x$, constants and extra data `ex`, which holds a lattice comparison `ex.cmp` and twisted forms `ex.tw`. A *site* is a word $u$, a tuple $\mu$, a place $w$ with residue characteristic $p$, and an index $h_g$ (the predicate `GIdx` at $u$ and $p$; its first part says that $p$ is prime). A tuple $\mu$ is *used* (`DV.Used`) if it is $\mu_0$, $\mu^*$, $\mu^{*\prime}$ or $\mu_{w'}$ for some place $w'$. The site is *good* if $\mu$ is used and $p \notin D_x.Q_p(\mu)$.

`ModelsOK D Gl ex.cmp Dx ex.tw` is the conjunction of:

1. $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ for each word $u$;
2. there is a choice `LC` of a level structure $L_v$ on the fills $G_l.\mathrm{Fl}(u, w, h_g)$ and a chain on $L_v$ at each site, such that at each good site the chain satisfies `CmpLite` and the triple (fills, $L_v$, chain) satisfies `SiteAdm`. Both are described in [`site_cmpLite_siteAdm`](/entry/site-cmp-lite-site-adm/).

`JointsAt t μ` says: at each $u$, $w$, $h_g$ with $p \notin D_x.Q_p(\mu)$, there are a level structure $L_v$, a comparison input $I$, a hypothesis $H$ on $I$, a label $X$ of $I$, and a joint (`Joint t H X`). A joint is a structure of 35 fields. It holds group compatibility data, chart choices at each step, adelic data, an element $a$ of $\mathcal{O}_E$, and conditions that tie the step zero data of $D$ to those of the twist. It also holds the tie `LatTied hT Gi Gl`, the fact $p \notin D_x.Q_p(\mu)$, and the fact that $p$ is prime to the norm of the ideal $t.c_c$ of $t$.

**Theorem.** Assume `AdmAtEnt2` and `CurveEx`. Let $t$ be a tied kernel entry of `ex`. Assume `JointsAt t μ` for each used $\mu$, the equality in (1), `Stab0 D`, and $2\, r_G(\varepsilon) \le k$. Then `ModelsOK D Gl ex.cmp Dx ex.tw` holds.

Here `Stab0 D` says that at step zero each class of $D$, and of each used twist of $D$, has a stabiliser of one element. The number $r_G(\varepsilon)$ is defined in [`modelsAt_of_part`](/entry/models-at-of-part/).

## Proof

The first condition is the hypothesis (1).

For the choice `LC`: at a good site, `JointsAt` gives $L_v$, $I$, $H$, $X$ and a joint $J$. Choose them, and take the pair $(L_v, \mathrm{chainAt}(H, h_T))$. At the other sites, take the level structure and chain of $G_l$.

At a good site the choice reduces to the first case. Then [`jointSite_chain_compared_carries_admittedSystem`](/entry/joint-site-chain-compared-carries-admitted-system/), applied to $J$, the fact that $\mu$ is used, `Stab0 D` and the bound on $k$, gives `CmpLite` and `SiteAdm` for this pair. The rest is bookkeeping.

## In the Lean code

The theorem is at [ThetaLocalModelsOfSplitUnramifiedJoints.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ThetaLocalModelsOfSplitUnramifiedJoints.lean#L11). The definitions are in [ModelsOK.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ModelsOK.lean#L56) (`ModelsOK`), [JointCmpEmbeddingY.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/JointCmpEmbeddingY.lean#L190) (`JointsAt`, and `Joint` at line 35), [OrbitPlaces.lean](lean:Formalism/SharpRestriction/Divisibility/OrbitPlaces.lean#L111) (`Stab0`) and [DataAmbForm.lean](lean:Formalism/LocalRingCardinality/DataAmbForm.lean#L9) (`DV.Used`). The only lemma it calls is `GlobalTheory.T.jointSite_chain_compared_carries_admittedSystem`.

The choice is made with `Classical.choose` on the nested existential of `JointsAt`, and the joint with `Nonempty.some`. The hypotheses `AdmAtEnt2`, `CurveEx`, `Stab0 D` and the bound on $k$ are only passed on to the site lemma.
