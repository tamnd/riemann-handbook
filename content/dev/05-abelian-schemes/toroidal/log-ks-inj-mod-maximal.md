---
id: log-ks-inj-mod-maximal
title: Injectivity modulo a maximal ideal, split into interior and boundary points
kind: theorem
decl: GlobalTheory.logKS_inj_mod_maximal
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LogKodairaSpencerInjectiveModMaximalIdeal
covers: 378
status: drafted
drafted_by: writer@claude
---
This theorem proves [the statement form](/entry/log-kodaira-spencer-injective-mod-maximal-ideal/), input 7 of the [log Kodaira-Spencer isomorphism](/entry/has-log-ks/). It splits the claim by the position of a point: in the interior, or on the boundary. The boundary case is [`logKodairaSpencer_injective_mod_maximal_boundary`](/entry/log-kodaira-spencer-injective-mod-maximal-boundary/), which carries most of the content.

## Statement

The statement is that of [the statement form](/entry/log-kodaira-spencer-injective-mod-maximal-ideal/). With the names of [`hasLogKS`](/entry/has-log-ks/): if $\mathrm{IsKS}(D, \Theta)$ holds on an affine open $U$ with ring $R$, and all entries of $\Theta$ lie in a maximal ideal $\mathfrak m$ of $R$, then the log derivation $D$ lies in $\mathfrak m T_U$.

## Proof

1. `exists_point_vanishing_of_isMaximal`: there is a point $x \in U$ at which each $f \in \mathfrak m$ vanishes, namely the image of $\mathfrak m$ under $\operatorname{Spec} R \cong U$.
2. If $x$ is in the interior $X^\circ_F$, then `kodairaSpencer_injective_closed_interior_point` gives $D \in \mathfrak m T_U$.
3. If $x$ is on the boundary, then [`logKodairaSpencer_injective_mod_maximal_boundary`](/entry/log-kodaira-spencer-injective-mod-maximal-boundary/) gives $D \in \mathfrak m T_U$.

Both lemmas take the same hypotheses as this theorem, and in addition the point $x$ with its position. The rest is bookkeeping.

## In the Lean code

The theorem is in [LogKodairaSpencerInjectiveModMaximalIdeal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerInjectiveModMaximalIdeal.lean#L31), and `exists_point_vanishing_of_isMaximal` is at [L19](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LogKodairaSpencerInjectiveModMaximalIdeal.lean#L19).

The name of the interior lemma says "closed interior point", but its hypothesis only asks for a point of the interior in $U$ at which $\mathfrak m$ vanishes; closedness is not stated. The boundary case is called through `first | exact key hb hKS hΘ | exact key hKS hΘ`, a fallback that accepts two forms of the lemma; the first form matches the statement file. We have not opened the proofs of the two lemmas, so we cannot say where the rigid charts are used. The [entry above](/entry/has-log-ks/) notes that this input is one of the two places where they can enter.
