---
id: exists-key-rule-char-half
title: The key rule for half-integral characteristics
kind: theorem
decl: GlobalTheory.KeyTop.exists_keyRule_charHalf
module: Development.AbelianVarietyTheory.Proofs.ThetaLawProofs.ExistsKeyRuleCharHalf
covers: 891
status: drafted
drafted_by: writer@claude
---
This theorem gives a key rule: a unit attached to each abelian variety with a theta section and a tangent basis, of weight $8N(g)$, that is $1$ at the theta functions of half-integral characteristic. It passes its hypotheses to `T.thetaKeyRule_exists_of_algebraic_invariants`, together with the key invariant of [`kaSt`](/entry/ka-st/) under its [second name](/entry/exists-integral-key-invariant-rule-char-zero/). It is below the step [every character of the literature](/step/every-character-of-literature/), through `keyFormula_of_connFam`.

## Statement

A *key input* over a ring $R$ is a principally polarized abelian scheme $A$ over $R$ of dimension $g \ge 1$ with a rigidified line bundle $L$, a section $\theta$ of $L$ that is nonzero on each fibre, and a basis $v$ of the Lie algebra. A *key rule* $\mathrm{KeyRule}(N, 1, S)$ is a choice of a unit $\kappa(x) \in K^\times$ for each key input $x$ over a field $K$ of characteristic $0$, such that:

1. if $\theta' = a\theta$ and $v' = Mv$, then $a^{8N(g)}\kappa(x') = \det(M)^{4N(g)}\kappa(x)$;
2. $\kappa$ commutes with field maps;
3. over a discrete valuation ring $R$ whose fraction field has characteristic $0$, $\kappa$ is a unit of $R$, and it commutes with each surjection of $R$ onto a field of characteristic $0$;
4. over $\mathbb{C}$, if $A = \mathbb{C}^g/(\mathbb{Z}^g + \tau\mathbb{Z}^g)$ with $\tau$ symmetric and $\operatorname{Im}\tau$ positive definite, $\theta = \theta[a,b](\tau, z)$, $v$ is the standard basis divided by $2\pi i$, and $S(g, a, b)$ holds, then $\kappa(x) = 1$.

`charHalf` is the condition that each $a_i$ and $b_i$ is $0$ or $\tfrac12$.

**Theorem.** Assume the abelian scheme laws `Out.Laws`, the analytic uniformization `ThetaUnifAV`, the theta inversion `InversionStatement`, the holomorphy `PhHoloStatement` and `TorusAlgebraic`. Then there is $N$ with $N(g) \ge 1$ for all $g$ such that $\mathrm{KeyRule}(N, 1, \mathrm{charHalf})$ holds.

## Proof

1. `T.keyData_descend_countable_subrings` gives `KeyDesc`: each key input over a field of characteristic $0$ descends to a countable subfield.
2. `T.exists_integralKeyInvariantRule_charZero` gives `KaSt`: for each $g$ and prime $p$, a key invariant integral away from some $M$ prime to $p$.
3. `T.thetaKeyRule_exists_of_algebraic_invariants` (a second name of `KeyHouse.keyRule_of_kaSt`) builds the rule. It uses `KaSt` at $p = 2$ to choose $N$ and $\kappa$. For integrality at a ring where $M$ is not a unit, it takes the invariant for a prime $p \mid M$ and compares the two on $\mathbb{C}$, after descent to a countable field and an embedding into $\mathbb{C}$.

## In the Lean code

The theorem is in [ExistsKeyRuleCharHalf.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsKeyRuleCharHalf.lean#L28). `KeyRule` and `charHalf` are in [KeyRuleOneOfKeyFormula.lean](lean:Development/AbelianVarietyTheory/Definitions/KeyFormula/KeyRuleOneOfKeyFormula.lean#L41). We have not unfolded the five hypotheses. All five are discharged by the caller `keyFormula_of_connFam` in [KeyFormulaOfConnFam.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/KeyFormulaOfConnFam.lean#L36). Inside `keyRule_of_kaSt`, the invariant for dimension $g$ comes from `KaSt` at dimension $2g$, in [ThetaKeyRuleExistsOfAlgebraicInvariants.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ThetaKeyRuleExistsOfAlgebraicInvariants.lean#L101); we have not checked why.
