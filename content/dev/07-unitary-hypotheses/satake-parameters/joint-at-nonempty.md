---
id: joint-at-nonempty
title: Each joint has a site
kind: theorem
decl: GlobalTheory.TwV.joint_at_nonempty
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.JointDataAtPAndAdelicDatumNonempty
covers: 749
status: drafted
drafted_by: writer@claude
---
This theorem builds a joint site over each joint. A joint site is the record that [`admissible_at_each_site`](/entry/admissible-at-each-site/) needs to prove that the pending system is admitted. The theorem is used in the restated form [`jointData_at_p_and_adelicDatum_nonempty`](/entry/joint-data-at-p-and-adelic-datum-nonempty/), in step 3 of [`site_cmpLite_siteAdm`](/entry/site-cmp-lite-site-adm/). It only assembles a record: the curve comes from the hypothesis `CurveEx`, and the adelic datum comes from [`adLawAt_xiAd`](/entry/ad-law-at-xi-ad/), which dominates 710 of the 749 declarations below this theorem.

## Statement

`CurveEx` says: let $D$ be a datum, $c_c$ an ideal, $\delta \in \mathbb{C}$, $B$ a base and $\chi$ a character, with the curve ideal, discriminant and character conditions. Let $p \ge 5$ be a prime prime to the norm of $c_c$, with the inertness condition `InertK D p`. Then for each embedding $\lambda \colon \overline{\mathbb{Q}} \to \mathbb{C}_p$ there is $g$ of type `GL3Theta.G1 p` with `LTIso g` and `CurveIn D p cc δ g B χ λ`. Here `CurveIn` says that $p \ge 5$, that $g$ fits $c_c$ and $\delta$, that $g$ has a model over the Witt vectors, the three conditions above, $\lambda = g.\lambda$, and that the abelian variety of $g$ is that of $B$.

**Theorem.** Assume `CurveEx`. Let $t$ be a tied kernel entry, $(u, \mu, w, h_g)$ a site with residue characteristic $p$ prime, `std` a standard choice at $w$ and $J$ a joint, as in [`jointData_at_p_and_adelicDatum_nonempty`](/entry/joint-data-at-p-and-adelic-datum-nonempty/). Then there is a joint site $S$ of type `J.At std`.

## Proof

The proof fills the eleven fields of $S$.

1. **Embeddings.** `exists_cEmbC_lam` gives a complex embedding datum $E$ of the local group (`nonempty_cEmbC`) and an embedding $\lambda \colon \overline{\mathbb{Q}} \to \mathbb{C}_p$ that extends $E$ on the field of the site (`padic_emb_extends_algebraicClosure`). This is the field `hK`.
2. **Curve.** `gidx_facts` reads $p \ge 5$ and `InertK D p` off $h_g$. The joint gives that $p$ is prime to the norm of $t.c_c$ (`J.cop`), and $t$ gives the three conditions on $c_c$, $\delta$ and $\chi$. `CurveEx` at $\lambda$ gives $g$, `LTIso g` and `CurveIn`.
3. **Finiteness.** `finClasses_sysS` gives that each level of the system has finitely many classes of lattice tuples. `finStab_site` gives that each lattice tuple has a finite stabiliser.
4. **Adelic datum.** [`exists_adelicDatum_with_laws_at_joint`](/entry/exists-adelic-datum-with-laws-at-joint/) gives $\Xi$, $\mu_T$ and `AdLawAt J.A J.dtU J.a Ξ μ_T`.

## In the Lean code

The theorem is at [JointDataAtPAndAdelicDatumNonempty.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/JointDataAtPAndAdelicDatumNonempty.lean#L16). `Joint.At` is in [JointCmpEmbeddingY.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/JointCmpEmbeddingY.lean#L134), `CurveEx` in [ThetaSeriesDataHypothesesBelowMaximalLevel.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ThetaSeriesDataHypothesesBelowMaximalLevel.lean#L131) and `CurveIn` in [StatementAdmAt.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/StatementAdmAt.lean#L29). We have not unfolded `CEmbC`, `LTIso` or `GL3Theta.At`.

`CurveEx` is a hypothesis here. Higher up, [`servH_row_of_artin`](/entry/serv-h-row-of-artin/) proves it with `exists_genusOne_formal_iso_of_unramified_good_reduction`. Of the four parts, only the curve depends on another: it is chosen for the $\lambda$ of part 1.
