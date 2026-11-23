---
id: is-ks-of-heat
title: The symbol of a commuting heat operator is the Kodaira-Spencer matrix
kind: theorem
decl: GlobalTheory.KBracket.isKS_of_heat
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KodairaSpencerOfCommutingHeatOperatorsRaynaud
covers: 514
status: drafted
drafted_by: writer@claude
---
This theorem says that a heat operator with zero defect, built on the Raynaud extension, has as its symbol the Kodaira-Spencer matrix of its derivation on the abelian locus. It proves [the statement form](/entry/kodaira-spencer-of-commuting-heat-operators-raynaud/). The heat operator comes from [`heat_commuting_periods_exists`](/entry/heat-commuting-periods-exists/), and the result feeds the boundary charts of the [log Kodaira-Spencer isomorphism](/entry/has-log-ks/).

## Statement

Let $E$ be a CM field and $R$ a complete Noetherian local domain that contains $\mathbb{Q}$. Let $G$ be a semi-abelian scheme over $R$ with an $\mathcal{O}_E$-action and a symmetric rigidified line bundle with a cubical structure (`SAB`). Let $P$ be a PEL uniformisation of $G$ over $(R, \mathfrak m)$ (`PELUnif`): degeneration data in the sense of Mumford with an $\mathcal{O}_E$-action, and an identification of $G$ with the object built from it. Assume:

1. the periods are monomial in nonzero $t_1, \dots, t_m \in R$ (`IsMonomial`), as in [`heat_commuting_periods_exists`](/entry/heat-commuting-periods-exists/);
2. a prime $\mathfrak p$ of $R$ is in the abelian locus of $G$ if and only if $t_1 \cdots t_m \notin \mathfrak p$.

Let $\tilde G$ be a Raynaud extension for $P$, with a tangent basis $v_1, \dots, v_n$ and invariant vector fields $\partial_a$. Let $v'_a$ be tangent vectors of $G$ that correspond to $v_a$ under the uniformisation (`IsPointOf`). Let $D$ be a derivation of $R$ and $h$ a basic heat operator for $D$ on $\tilde G$ with defect 0, with symbol $\Theta$.

**Theorem.** On $\operatorname{Spec} R$, with interior $V = \{t_1 \cdots t_m \neq 0\}$, $\mathrm{IsKS}(D, \Theta)$ holds in the frame $v'$: $\Theta$ satisfies the Čech Kodaira-Spencer relation of [`hasLogKS`](/entry/has-log-ks/) over the abelian locus.

## Proof

The idea: two heat operators with the same derivation term that act on the values of theta functions at a formal point have the same symbol.

1. $\tilde G$ is smooth (`RayTan.smooth_H`) and integral (`isIntegral_raynaudExtension_noetherian_local`). Some $W_{i_0}$ of the cover of $h$ contains the origin.
2. `exists_formalPoint_origin_smoothCommGroupScheme`: a complete local domain $\Omega$ over $R$ and a point $x \colon \operatorname{Spec} \Omega \to W_{i_0}$, with derivations of $\Omega$ that match $\partial_a$ and $d_{i_0}$, and with $f \mapsto f(x)$ injective. Then $R \to \Omega$ is injective.
3. `exists_uniformisedGroup_point_sameDerivations` moves $x$ to a point $x'$ of $G$ with the same derivations. Fix a local generator of the line bundle at $x'$.
4. `commuting_heatOperators_act_on_values`: $h$ induces an operator on the values at $x'$ of sections of $L^k$.
5. `exists_symmetric_kodairaSpencer_abelianLocus`: after $D$ is extended to $R[1/(t_1 \cdots t_m)]$, there is a symmetric $\Theta_1$ with $\mathrm{IsKS}(D, \Theta_1)$ on the abelian locus. `heatOperators_kodairaSpencer_formal_point_values` gives a second operator on values with symbol $\Theta_1$.
6. `heatOperator_symbol_unique_principalPolarisation`: the two symbols are equal in $\operatorname{Frac}\Omega$. The map $R[1/(t_1 \cdots t_m)] \to \operatorname{Frac}\Omega$ is injective, so $\Theta_1$ is the image of $\Theta$.
7. `isKodairaSpencer_affineChart_of_basicOpen` moves $\mathrm{IsKS}$ from the basic open to $\operatorname{Spec} R$ with interior $V$.

## In the Lean code

The theorem is in [KodairaSpencerOfCommutingHeatOperatorsRaynaud.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KodairaSpencerOfCommutingHeatOperatorsRaynaud.lean#L89). The same file proves `exists_der_ext` and `exists_der_frac`: a derivation extends to a localization.

The defect-zero hypothesis and the basic property of $h$ are used only by step 4. The monomial hypothesis is passed to the lemmas of steps 3 to 6, whose proofs we have not opened. The name of the lemma in step 6 says "principal polarisation", but its statement has no hypothesis about the degree of the polarisation.

Welters relates heat operators on theta functions to the Kodaira-Spencer class in *Polarized abelian varieties and the heat equations* (Compositio Math. 49, 1983). We have not compared the Lean form with his.
