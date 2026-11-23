---
id: admissible-at-each-site
title: The pending system is admitted at each joint site
kind: theorem
decl: GlobalTheory.TwV.admissible_at_each_site
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.JointSiteChainComparedCarriesAdmittedSystem
covers: 1483
status: drafted
drafted_by: writer@claude
---
This theorem shows that the local system at the prime below a place $w$ is `admitted` at every joint site. It is the step in [`site_cmpLite_siteAdm`](/entry/site-cmp-lite-site-adm/) that gives the admissibility part of `SiteAdm`. Its one hypothesis is `AdmAtEnt2`, which [`inert_theta_admissibility_of_complex_multiplication`](/entry/inert-theta-admissibility-of-complex-multiplication/) proves from the good model condition `CM2`. The work of this theorem is to check that a joint site supplies every input that `AdmAtEnt2` asks for.

## Statement

Fix a datum $D$ with its size data, ties, instances and extra data, a site $(u, \mu, w)$ with residue characteristic $p$ prime, a level structure $L_v$, a comparison input $I$ with hypothesis $H$ and label $X$, a standard choice `std` at $w$, a tied kernel entry $t$ and a joint $J$ (`Joint`). A *joint site* $S$ over these data (`Joint.At`) is a record with an embedding $\lambda \colon \overline{\mathbb Q} \to \mathbb C_p$, a complex embedding $E$ compatible with it, a datum $g$ of type `GL3Theta.G1 p` with `LTIso g`, a proof of `CurveIn`, an adelic datum $\Xi$ and a law `AdLawAt`. From $S$ one builds a pending element $S.Y$ of the local system `sysS H X std` at $p$.

**Theorem.** Assume `AdmAtEnt2`. Let $S$ be a joint site as above. If the twist $\mu$ is used (`DV.Used D μ`) and the stabilisers at level 0 are trivial (`Stab0 D`), then `admitted D (sysS H X std) S.Y`.

The predicate `admitted` is a conjunction of 13 conditions (`adm1` to `adm11`, `ArchimedeanSignatureMatching`, `MinkowskiCounting`). We have not unfolded them.

## Proof

`AdmAtEnt2` says: if `CurveIn`, the below-maximal-level hypotheses `ThetaSeriesDataHypothesesBelowMaximalLevel`, `XiIn`, `LawInLt` and ties `TiesAt` at each level $j < m$ hold, then the system is admitted. The proof supplies each input from $S$.

1. `latticeTuple_joint_dictionary` gives a dictionary from $J$. With it, the `kernelSite_*` lemmas give the pair, position, frame, independence and scalar facts. `allSites_k1_of_dict_pair_pos_scal` combines them into the below-maximal-level hypotheses.
2. `kernelSite_law_and_fixedCoordinateStabiliserLaw` gives `XiIn` and `LawInLt`. `S.curve` gives `CurveIn`.
3. `ThLoc.place_extends_to_iso` extends $\lambda$ to a ring isomorphism $\iota \colon \mathbb C \to \mathbb C_p$.
4. For each level $j < m$ the four ties are: the stabiliser tie from `tieStab_kaAtAny`, which is the only place where `DV.Used` and `Stab0` are used; the reading tie from `series_reading_entries`, with the compatibility of $\iota$ and $E$ on the field; the series tie from `series_compatibility_of`; and the kernel difference. For the last, `kernelSite_frameValues_step_zero` ($j = 0$) or `kernelSite_frameValues_positive_steps` ($j > 0$) gives $c_K$ with $\lVert c_K \rVert = 1$. So $c_K$ and $c_K^{-1}$ are integral and $c_K \neq 0$.

The rest is bookkeeping.

## In the Lean code

The theorem is at [JointSiteChainComparedCarriesAdmittedSystem.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JointSiteChainComparedCarriesAdmittedSystem.lean#L29). It is `private`, and it runs under `set_option maxHeartbeats 4000000`. The statement is written with `AllSites` from [JointCmpEmbeddingY.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/JointCmpEmbeddingY.lean#L179), which quantifies over all data and all joint sites. `admitted` is in [FormalGroupSystem.lean](lean:Formalism/SharpRestriction/GrowthBounds/FormalGroupSystem.lean#L771) and `TiesAt` in [SecondKernelEntrywiseLastLevel.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/SecondKernelEntrywiseLastLevel.lean#L55). The theorem uses `GlobalTheory.TwV.Lt.AdmAtEnt2`. A second definition with the same body is `Formalism.L2.KerInert.AdmLoc2.AdmAtEnt2`.
