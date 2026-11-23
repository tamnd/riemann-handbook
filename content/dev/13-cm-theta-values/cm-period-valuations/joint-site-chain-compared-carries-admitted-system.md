---
id: joint-site-chain-compared-carries-admitted-system
title: The chain of a joint is compared and admitted, restated
kind: theorem
decl: GlobalTheory.T.jointSite_chain_compared_carries_admittedSystem
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.JointSiteChainComparedCarriesAdmittedSystemStatement
covers: 2335
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`site_cmpLite_siteAdm`](/entry/site-cmp-lite-site-adm/). It has the same statement, and its proof applies that theorem. Its user is [`modelsOK_of_joints`](/entry/models-ok-of-joints/), which applies it at each good site. The content is in `site_cmpLite_siteAdm`, which dominates 2,334 of the 2,335 declarations below this theorem.

## Statement

Assume `AdmAtEnt2` and `CurveEx`. Let $D$ be a datum of type `D7` with its size data, ties $h_T$, instances, division data and extra data `ex`, and let $t$ be a tied kernel entry of `ex`. Let $(u, \mu, w, h_g)$ be a site, $L_v$ a level structure on the fills $G_l.\mathrm{Fl}(u, w, h_g)$, $I$ a comparison input, $H$ a hypothesis on $I$ and $X$ a label of $I$. Assume a joint `Joint t H X`, that $\mu$ is used, `Stab0 D`, and $2\, r_G(\varepsilon) \le k$. Then the chain $\mathrm{chainAt}(H, h_T)$ satisfies `CmpLite` at the site, and `SiteAdm` holds for the fills, $L_v$ and this chain. All these objects are described in [`site_cmpLite_siteAdm`](/entry/site-cmp-lite-site-adm/).

## Proof

Apply `site_cmpLite_siteAdm`. Nothing else is used.

## In the Lean code

The theorem is at [JointSiteChainComparedCarriesAdmittedSystemStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JointSiteChainComparedCarriesAdmittedSystemStatement.lean#L8). Its proof is the tactic

```
first | exact @site_cmpLite_siteAdm | exact site_cmpLite_siteAdm | (intros; apply site_cmpLite_siteAdm <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The first branch closes the goal, so the theorem is a renaming.
