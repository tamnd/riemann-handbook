---
id: exists-act-rep-finite
title: The scheme of adjoint actions is a closed subscheme of a finite scheme of polarized maps
kind: theorem
decl: GlobalTheory.ActFin.exists_actRep_finite
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFiniteSchemeAdjointActionsAbelian
covers: 598
status: drafted
drafted_by: writer@claude
---
This theorem builds the scheme of adjoint actions of [the finite unramified result](/entry/act-rep-finite-unramified/) and proves that it is finite over the base. [Its statement form](/entry/exists-finite-scheme-adjoint-actions-abelian/) repeats it. The idea: an adjoint action is fixed by the images of the generators $e_1, \dots, e_r$, so it gives a map $A \to A^r$. The relation $\sum W_{ij} e_j \bar e_i = d$ makes this map respect two line bundles, and such maps form a finite scheme.

## Statement

Use $S$, $A$, $Q$, $O$, $\bar{\ }$, $e$, $W$, $d$ and the notion of an adjoint action as in [the finite unramified result](/entry/act-rep-finite-unramified/), with the same hypotheses. Then there is a scheme $\pi \colon H \to S$ with a universal adjoint action on $A_H$, and $\pi$ is [[finite|N9C4X7XKE4]].

## Proof

Put $L = (\Delta^*Q)^{\otimes d}$ on $A$ and $M = \bigotimes_{u,v} (p_u, p_v)^*Q^{\otimes W_{uv}}$ on $A^r$, where $p_u \colon A^r \to A$ are the projections.

1. `matrixWeightedPairBundle_rigidified_ample` uses $W + W^{\mathsf T} > 0$: $A^r$ is an abelian scheme and $M$ is rigidified and relatively ample. `diagonalPullbackPower_isRigidified_relAmple` uses $d > 0$: the same holds for $L$ on $A$.
2. [The finite scheme of polarized maps](/entry/exists-finite-unramified-representing-polarized-homs/) gives a finite $H_0 \to S$ and a universal homomorphism $\Phi \colon A_{H_0} \to A^r_{H_0}$ with $\Phi^*M \cong L$. Put $f_k = p_k \circ \Phi$. Since $S$ is locally noetherian and $H_0 \to S$ is finite, $H_0$ is locally noetherian.
3. `groupScheme_ringAction_iff_endomorphism_relations`: since the $e_k$ span $O$, there are integers $N$, $c^1$, $c^{ijk}$ such that, on any commutative group scheme, endomorphisms $g_1, \dots, g_r$ are the images of the $e_k$ under an action exactly when $\sum_k N_{jk} g_k = 0$ for all $j$, $\sum_k c^1_k g_k = 1$, and $g_j \circ g_i = \sum_k c^{ijk} g_k$.
4. Write $\bar e_i = \sum_k b_{ik} e_k$. Each condition of step 3 on the $f_k$ holds on a closed subscheme of $H_0$ (`abelianScheme_homAgreeLocus_closedSubscheme`). The condition $(f_i \times 1)^*Q \cong (1 \times \sum_k b_{ik} f_k)^*Q$ also holds on a closed subscheme (`exists_closedSubscheme_pullback_adjoint_endomorphism_pair`). Let $Z \subseteq H_0$ be the intersection of these finitely many closed subschemes.
5. On $A_Z$, step 3 gives an action $\alpha_Z$ with $\alpha_Z(e_k) = f_k$. It is adjoint on each $e_i$. `ringAction_adjoint_of_adjoint_on_spanning_family` extends adjointness to all of $O$, by additivity of $\bar{\ }$.
6. Universality. Let $\alpha$ be an adjoint action on $A_T$. Let $\Phi' = (\alpha(e_1), \dots, \alpha(e_r)) \colon A_T \to A^r_T$. By `formBundle_pullback_adjointAction_eq_diagonalPower`, $\Phi'^*M_T \cong L_T$; this is the only use of $\sum W_{ij} e_j \bar e_i = d$. So $\Phi'$ comes from a unique $h_0 \colon T \to H_0$. The $\alpha(e_k)$ satisfy the relations of step 3 and adjointness, so $h_0$ factors through $Z$. The factorization is unique because $Z \to H_0$ is a monomorphism.
7. $Z \to H_0$ is a [[closed immersion|WWRWYSJDET]], so $Z \to S$ is finite. Take $H = Z$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsFiniteSchemeAdjointActionsAbelian.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteSchemeAdjointActionsAbelian.lean#L83). The bundles are `diagPow` and `formLB` in [IsMonHomProdPow.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsMonHomProdPow.lean#L25), and the hypotheses on $Q$ are bundled as `QHyp`. The file first gives short names to fourteen lemmas of `GlobalTheory.T` (`formLB_props`, `homFix_iso_of_act` and others); we read only their statements. The intersection in step 4 uses `GlobalTheory.T.exists_closedSubscheme_finite_intersection` and `GlobalTheory.T.exists_closedSubscheme_intersection`.

Step 2 discards the "formally unramified" part of the polarized maps result. The lemma `qHyp_pull` (`symmetricBiextensionHyp_pullback_of_groupPullback`) carries the hypotheses on $Q$ to $H_0$ and $Z$; the name says "biextension", but `QHyp` asks for no biextension structure: only that $A$ is abelian and the conditions on $Q$ listed in the parent.
