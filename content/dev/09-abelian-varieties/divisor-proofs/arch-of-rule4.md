---
id: arch-of-rule4
title: Theta jets of a degenerating family come from a complex abelian variety with the same key value
kind: theorem
decl: GlobalTheory.MBLow.ArchProof.arch_of_rule4
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KeyRuleComplexExistenceJetsKeyValue
covers: 465
status: drafted
drafted_by: writer@claude
---
This theorem proves that a key rule with the four properties `Rule4` has the archimedean property `Arch`. It is used through its second name [`T.keyRule_complex_existence_jets_key_value`](/entry/key-rule-complex-existence-jets-key-value/), which lies below [EveryCharacter from the literature and VWin](/step/every-character-of-literature/).

## Statement

A *key rule* $\kappa$ gives a unit $\kappa(x) \in K^\times$ for each polarized abelian variety $x$ over a field $K$ of characteristic 0, with a rigidification, a theta section $\theta$ and a Lie basis $v$. `Rule4` asks for four properties ([KeyRootOfKeyFormula.lean](lean:Development/AbelianVarietyTheory/Definitions/KeyFormula/KeyRootOfKeyFormula.lean#L13)):

- homogeneity: if $\theta' = a\theta$ and $v' = Mv$, then $a^8 \kappa(\theta', v') = (\det M)^4 \kappa(\theta, v)$;
- compatibility with base change;
- $\kappa(x) = 1$ when $x = \mathbb{C}^g / (\mathbb{Z}^g + \tau \mathbb{Z}^g)$ with the theta function with characteristic $(a, b) \in \{0, \tfrac12\}^{2g}$ and $v_i = (2\pi i)^{-1} \partial_i$;
- over a normal Noetherian domain, the value is a unit.

`Arch` is in [IsPolAVSectionInverseImage.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsPolAVSectionInverseImage.lean#L183). The data: degeneration data $D$ over a Noetherian local domain $R$ (with two conditions `PsiEven` and `TauBimult`), with an abelian part of dimension $g_0$ and a torus with character group $X$ of rank $r$; an embedding $\operatorname{Frac} R \to \mathbb{C}$; $g = g_0 + r \geq 1$; an odd $m$ with $m^2 \mid k$; a quadratic form $\beta$ on $X$; a level structure $q$ of level $m^2$ with root of unity $\zeta$; families $s_a$ of sections with Fourier coefficients on cosets $p_a + mX$; adapted tangent points $\gamma_j$; and $k_0$, the value of $\kappa$ on the abelian part (`BKey`). Let $c_{a,j}(\alpha)$ be the jet of $s_a$ at $\gamma_j$ in degree $\alpha \in X$, a dual number.

**Theorem.** If $\kappa$ satisfies `Rule4`, then $\kappa$ satisfies `Arch`: there is $\varepsilon > 0$ such that for $0 < |u| < \varepsilon$ the series $\sum_\alpha c_{a,j}(\alpha)\, u^{\lfloor \beta(\alpha,\alpha)/2m^2 \rfloor}$ converge absolutely, and there is a complex abelian variety $x_0$ of dimension $g$ with a level structure of level $m^2$ such that these sums (divided by a fixed power) are the values and first jets of the level-$m^2$ theta functions of $x_0$ at its level points, and $\kappa(x_0) = k_0$.

## Proof

1. `exists_cd`: classical data for $D$ with the key property `KeyOK`, from `MBLow.DimZero.main` if $g_0 = 0$ and from `T.exists_classicalThetaDescription_abelianPart` if $g_0 \geq 1$. `Cl.PsiFrame.exists_cd` puts the data in normal form.
2. `exists_vec` (with `Cl.jet_family_deriv` and `Cl.det_eq_det_block`): a matrix $M_x$ with $\det M_x \neq 0$ and $k_0 c^8 = (\det M_x)^4$, and each jet $c_{a,j}(\alpha)$ as the value and derivative of a holomorphic function.
3. `Cl.exists_integral_labels` gives integral labels for the level structure. `Cl.BlockPos.full_posDef` gives $T$ such that the period matrix built from $w\beta$ is admissible when $\operatorname{Im} w > T$. `Cl.term_smul_bmat` scales each term.
4. Take $\varepsilon = e^{-2\pi T}$ and $u = e^{2\pi i w}$ (`exists_log`). `coset_series`, `Cl.term_sum_and_fderiv` and `Cl.evT_eq_term` show that each series converges and equals $c$ times a theta series with characteristic at that period matrix.
5. `Cl.exists_keyIn_nf` gives the complex abelian variety $x_0$ in normal form. `LabelLevel.exists_level_of_labels` gives its level structure, and `Cl.thJet_of_normalForm` gives the theta jets.
6. `Cl.key_value_of_nf`, with homogeneity and the value $1$ on theta functions, gives $\kappa(x_0) c^8 = (\det M_x)^4$. Step 2 and $c \neq 0$ give $\kappa(x_0) = k_0$.

## In the Lean code

The theorem is at [KeyRuleComplexExistenceJetsKeyValue.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeyRuleComplexExistenceJetsKeyValue.lean#L122), We did not open the proofs of the `Cl.` and `T.` lemmas, and we have not unfolded `DegPre`, `PsiEven`, `TauBimult`, `KeyOK` or the jet `jc`.

Base change and the unit property are used only inside `T.exists_classicalThetaDescription_abelianPart`; the last step uses only homogeneity and the value $1$ ([line 198](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeyRuleComplexExistenceJetsKeyValue.lean#L198)).
