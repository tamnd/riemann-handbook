---
id: site-cmp-lite-site-adm
title: The chain of a joint is compared and admitted
kind: theorem
decl: GlobalTheory.TwV.site_cmpLite_siteAdm
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.JointSiteChainComparedCarriesAdmittedSystem
covers: 2334
status: drafted
drafted_by: writer@claude
---
This theorem proves the two conditions of `ModelsOK` at one site. `CmpLite` is read off a kernel datum. `SiteAdm` comes from the hypothesis `AdmAtEnt2`, after [`admissible_at_each_site`](/entry/admissible-at-each-site/) checks its premises. [`modelsOK_of_joints`](/entry/models-ok-of-joints/) uses it in the restated form [`jointSite_chain_compared_carries_admittedSystem`](/entry/joint-site-chain-compared-carries-admitted-system/). Of the 2,334 declarations below this theorem, 1,483 are below `admissible_at_each_site`.

## Statement

Take the setting of [`modelsOK_of_joints`](/entry/models-ok-of-joints/): a datum $D$ with its data, a tied kernel entry $t$, and a site $(u, \mu, w, h_g)$ with residue characteristic $p$. Let $L_v$ be a level structure on the fills $F = G_l.\mathrm{Fl}(u, w, h_g)$, $I$ a comparison input, $H$ a hypothesis on $I$, $X$ a label of $I$, and $\mathrm{Ch} = \mathrm{chainAt}(H, h_T)$.

`AdmAtEnt2` says: at each site, for each chain with a kernel datum and all local data, if `CurveIn`, a theta series condition, `XiIn`, `LawInLt` and the ties `TiesAt` at each step $j < m$ hold, then the pending system of these data is `admitted`. `CurveEx` says: for each prime $p \ge 5$ with some conditions and each $\lambda \colon \overline{\mathbb{Q}} \to \mathbb{C}_p$, there is $g$ with `LTIso g` and `CurveIn D p cc δ g B χ λ`.

Then:

- `CmpLite`: there are maps $c_j$, semilinear over `ex.cmp.embW u w hg`, from the lattice space of the twisted form at step $j$ to `Lv.Fm j`, with $c_0 \circ e_0$ equal to the comparison of `ex`, with $c_{j+1}(y) = \mathrm{Ch}.K_z(j)(c_j(x))$ when the step map $K_j$ relates $x$ to $y$, with `KRat j` for $j < m$, and with a valuation bound `VGe` at step $m$.
- `SiteAdm D u w hg F Lv Ch`: $p$ is prime, and there are local data, a function $d_G \colon \mathbb{N} \to \mathbb{N}$ and a pending system $Y$ over the system of $(F, L_v, \mathrm{Ch})$, such that $Y$ is `admitted`, $d_G(0) = 0$, and $d_G(j) \le v_p(\Delta_\Gamma)$ for all $j$, where $\Delta_\Gamma$ is `(D.mem u).C.DGam`.

**Theorem.** Assume `AdmAtEnt2` and `CurveEx`. If there is a joint `Joint t H X`, $\mu$ is used, `Stab0 D` holds and $2\, r_G(\varepsilon) \le k$, then `CmpLite` holds for $\mathrm{Ch}$ and `SiteAdm D u w hg F Lv Ch` holds.

We have not unfolded `admitted`, `CurveIn`, `LTIso`, `KRat`, `VGe` or the premises of `AdmAtEnt2`.

## Proof

1. **Comparison.** `kaAt X H hT` is a kernel datum `KerAtMu` for $\mathrm{Ch}$. Its fields `cmp`, `cmp_zero`, `cmp_K`, `rat` and `val` are the five parts of `CmpLite`.
2. **Standard data.** $p$ is prime by $h_g$. `std_at_served` gives `StdAtW` from the tie `J.tied` of the joint and $2\, r_G \le k$.
3. **Site data.** `jointData_at_p_and_adelicDatum_nonempty` uses `CurveEx` to give a site datum $S$ of type `J.At std`, which holds $\lambda$, $g$ and the curve condition.
4. **Admissibility.** [`admissible_at_each_site`](/entry/admissible-at-each-site/) applies `AdmAtEnt2` to $S$, with the facts that $\mu$ is used and `Stab0 D`, and gives `admitted D (sysS H X std) S.Y`.
5. **Witnesses.** Take $Y = S.Y$ and $d_G = $ `Lt.dGT D u p`, which is $0$ at $j = 0$ and $v_p(\Delta_\Gamma)$ for $j > 0$. Both conditions on $d_G$ hold by this definition (`split_ifs <;> simp`).

## In the Lean code

The theorem is at [JointSiteChainComparedCarriesAdmittedSystem.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JointSiteChainComparedCarriesAdmittedSystem.lean#L77). `CmpLite` is in [ModelsOK.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ModelsOK.lean#L46), `SiteAdm` in [IsPlaceCofactorValuationLowerBound.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/IsPlaceCofactorValuationLowerBound.lean#L10), and `AdmAtEnt2`, `CurveEx` and `dGT` in [ThetaSeriesDataHypothesesBelowMaximalLevel.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ThetaSeriesDataHypothesesBelowMaximalLevel.lean#L106). The private theorem `admissible_at_each_site` is at [line 29](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JointSiteChainComparedCarriesAdmittedSystem.lean#L29).

The admissibility in `SiteAdm` is the conclusion of the hypothesis `AdmAtEnt2`; the proof only checks its premises. Higher up, [`servH_row_of_artin`](/entry/serv-h-row-of-artin/) proves both hypotheses from the statement `CM2`, with [`inert_theta_admissibility_of_complex_multiplication`](/entry/inert-theta-admissibility-of-complex-multiplication/) and `exists_genusOne_formal_iso_of_unramified_good_reduction`.

`CmpLite` is [`KerAtMu`](lean:Formalism/SharpRestriction/GrowthBounds/LatticeMultiplicityLemmas/LatticeMultiplicityCheck/Retype.lean#L9) without its fields on fills, classes, stabilisers, injectivity and integrality. The first conclusion uses no hypothesis.
