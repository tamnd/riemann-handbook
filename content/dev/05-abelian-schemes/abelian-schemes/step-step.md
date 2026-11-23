---
id: step-step
title: The inductive step for the dual abelian scheme over a ring of finite type
kind: theorem
decl: GlobalTheory.DualCon.Step.step
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasProperSmoothDualRepresentativeNoetherianInducBis
covers: 661
status: drafted
drafted_by: writer@claude
---
This theorem is the inductive step of the noetherian induction that builds the dual of an abelian scheme over a ring of finite type over $\mathbb{Z}$. It assumes the dual over each proper closed subscheme $\operatorname{Spec} R/J$ and builds it over $\operatorname{Spec} R$. Its result goes to [`hasProperSmoothDualRepresentative_noetherian_induction`](/entry/global-theory-t-has-proper-smooth-dual-representative-noetherian-induction-2/), a second name, and from there to the induction in [`hasRep_of_finiteType`](/entry/has-rep-of-finite-type/).

## Statement

**Theorem.** Let $R$ be a commutative ring of finite type over $\mathbb{Z}$, and let $A \to \operatorname{Spec} R$ be an abelian scheme, smooth of relative dimension $g$. Suppose that for each ideal $J \neq 0$ of $R$, $A$ has a dual of dimension $g$ over $\operatorname{Spec} R/J$. Then $A$ has a dual of dimension $g$ over $\operatorname{Spec} R$.

"Has a dual of dimension $g$ over $S'$" is `HasRep A g S'`, defined in [`hasRep_affineOpen`](/entry/has-rep-affine-open/).

## Proof

**$R$ not reduced.** `exists_sq_zero` gives an ideal $J \neq 0$ with $J^2 = 0$: the nilradical $N$ is nonzero, and nilpotent since $R$ is noetherian; let $n$ be least with $N^n = 0$; then $n \ge 2$, and $J = N^{n-1}$ works, since $2n - 2 \ge n$. The hypothesis gives a dual over $\operatorname{Spec} R/J$. `T.hasProperSmoothDualRepresentative_of_sqZero` lifts a dual over $\operatorname{Spec} R/J$ to a dual over $\operatorname{Spec} R$ when $J^2 = 0$.

**$R$ reduced.** `T.hasProperSmoothDualRepresentative_of_local` says that a dual exists over $\operatorname{Spec} R$ if each point has an open neighbourhood with a dual. Fix a point $s$ (`local_rep`).

1. `T.exists_basicOpen_affineOpen_meeting_fibres_grpScheme` gives $f \in R$ with $s \in D(f)$ and an affine open $W \subseteq A$ that meets each fibre over $D(f)$.
2. Let $A' = A \times_R R_f$. It is abelian of relative dimension $g$, and `T.affineOpen_meeting_fibres_pullback_specRingHom` gives an affine open of $A'$ that meets each fibre over $\operatorname{Spec} R_f$. The ring $R_f$ is reduced and of finite type over $\mathbb{Z}$.
3. The hypothesis passes to $R_f$ (`hasRep_quot`). Let $J' \neq 0$ be an ideal of $R_f$ and $J$ its preimage in $R$. Then $J \neq 0$ (`comap_ne_bot_away`). The dual over $\operatorname{Spec} R/J$ base changes to $\operatorname{Spec} R_f/J'$ (`T.baseChangeBis`), and becomes a dual of $A'$ there (`T.hasProperSmoothDualRepresentative_grpPullback_iff`).
4. `T.hasProperSmoothDualRepresentative_noetherianInduction` now gives a dual of $A'$ over $\operatorname{Spec} R_f$.
5. `T.hasProperSmoothDualRepresentative_grpPullback_iff` turns it into a dual of $A$ over $D(f)$, and `hasRep_opens` restricts it to the open $D(f)$ of $\operatorname{Spec} R$.

## In the Lean code

The theorem is at [HasProperSmoothDualRepresentativeNoetherianInducBis.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasProperSmoothDualRepresentativeNoetherianInducBis.lean#L126). The helper lemmas `exists_sq_zero`, `hasRep_opens`, `comap_ne_bot_away`, `hasRep_quot` and `local_rep` are in the same file, at lines 22 to 124.

The lemmas that do the work, all second names given by a one-line proof:

- `T.hasProperSmoothDualRepresentative_of_sqZero`, for `LBLift.hasRep_of_sqZero`. We have not read its proof.
- `T.hasProperSmoothDualRepresentative_of_local`, for `DualCon.hasRep_of_local`, which glues duals over an open cover. We have not read its proof.
- `T.hasProperSmoothDualRepresentative_noetherianInduction`, for `GlobalTheory.DualConStep.step` in [HasProperSmoothDualRepresentativeNoetherianInduc.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasProperSmoothDualRepresentativeNoetherianInduc.lean#L64). We read its proof, not its lemmas. It writes $R$ as a subring of a finite product of normal noetherian domains $D_i$ with nonzero conductor. Over each $D_i$ the affine open gives a relatively ample line bundle, and from it a dual. It then descends the dual from $\prod D_i$ to $R$ with the dual over the closed subscheme cut out by the conductor, which the hypothesis supplies.

Two names are close and easy to confuse: `GlobalTheory.DualCon.Step.step` (this theorem) and `GlobalTheory.DualConStep.step` (the reduced case above). So are their second names, `hasProperSmoothDualRepresentative_noetherian_induction` and `hasProperSmoothDualRepresentative_noetherianInduction`.
