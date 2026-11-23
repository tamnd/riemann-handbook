---
id: has-rep-of-finite-type
title: The dual abelian scheme over a ring of finite type over the integers, by noetherian induction
kind: theorem
decl: GlobalTheory.DualConFT.hasRep_of_finiteType
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasProperSmoothDualRepresentativeFiniteType
covers: 665
status: drafted
drafted_by: writer@claude
---
This theorem gives the dual of an abelian scheme over $\operatorname{Spec} R$ when $R$ is of finite type over $\mathbb{Z}$. It runs a noetherian induction on the closed subschemes $\operatorname{Spec} R/I$; the inductive step is [`hasProperSmoothDualRepresentative_noetherian_induction`](/entry/global-theory-t-has-proper-smooth-dual-representative-noetherian-induction-2/). The result goes to [`hasProperSmoothDualRepresentative_finiteType`](/entry/has-proper-smooth-dual-representative-finite-type/), a second name of this theorem.

## Statement

**Theorem.** Let $R$ be a commutative ring of finite type over $\mathbb{Z}$, let $A \to \operatorname{Spec} R$ be an abelian scheme, and let $g \ge 0$. If $A \to \operatorname{Spec} R$ is smooth of relative dimension $g$, then $A$ has a dual of dimension $g$ over $\operatorname{Spec} R$.

"Has a dual of dimension $g$ over $S'$" is `HasRep A g S'`, defined in [`hasRep_affineOpen`](/entry/has-rep-affine-open/).

## Proof

Write $\mathrm{D}(R)$ for the claim: each abelian scheme over $\operatorname{Spec} R$ that is smooth of relative dimension $g$ has a dual of dimension $g$ over $\operatorname{Spec} R$. The inductive step says: if $A$ has a dual over $\operatorname{Spec} R/J$ for each ideal $J \neq 0$, then $A$ has a dual over $\operatorname{Spec} R$.

**Transfer lemma** (`hasRep_quot_of_factor`). Let $J$ be an ideal of a ring $S_0$, and let $\varphi \colon S_0 \to T$ and $\psi \colon T \to S_0/J$ be ring maps with $\psi \circ \varphi$ the quotient map. If $\mathrm{D}(T)$ holds, then each abelian scheme $A$ over $\operatorname{Spec} S_0$ of relative dimension $g$ has a dual over $\operatorname{Spec} S_0/J$. Proof: base change $A$ along $\operatorname{Spec} T \to \operatorname{Spec} S_0$. The result is abelian of relative dimension $g$, so it has a dual over $\operatorname{Spec} T$. `T.hasProperSmoothDualRepresentative_grpPullback_iff` makes this a dual of $A$ over $\operatorname{Spec} T$, and `T.baseChangeBis` moves it along $\operatorname{Spec} \psi$.

**Induction** (`hasRep_quot`). We prove $\mathrm{D}(R/I)$ for each ideal $I$ of $R$. Since $R$ is noetherian, the ideals satisfy the ascending chain condition, so we may assume $\mathrm{D}(R/J)$ for each $J \supsetneq I$. Let $A$ be over $\operatorname{Spec} R/I$. The ring $R/I$ is of finite type over $\mathbb{Z}$, so the inductive step applies. Let $J' \neq 0$ be an ideal of $R/I$, and let $J \subseteq R$ be its preimage. Then $J \supsetneq I$, and the transfer lemma with $T = R/J$ and the induced map $R/J \to (R/I)/J'$ gives a dual of $A$ over $\operatorname{Spec} (R/I)/J'$. For $I = R$ the step has no hypothesis to check, since the zero ring has no ideal $J \neq 0$.

**Conclusion.** Apply the inductive step to $R$ itself. For each ideal $J$, the transfer lemma with $T = R/J$, $\psi = \mathrm{id}$ and $\mathrm{D}(R/J)$ gives the dual over $\operatorname{Spec} R/J$.

## In the Lean code

The theorem is at [HasProperSmoothDualRepresentativeFiniteType.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasProperSmoothDualRepresentativeFiniteType.lean#L72). The two lemmas `hasRep_quot_of_factor` ([line 17](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasProperSmoothDualRepresentativeFiniteType.lean#L17)) and `hasRep_quot` ([line 39](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasProperSmoothDualRepresentativeFiniteType.lean#L39)) are in the same file. The induction is `WellFoundedGT.induction` on the ideals of $R$.

- `GlobalTheory.T.hasProperSmoothDualRepresentative_noetherian_induction` is the inductive step, not the induction; the induction is here.
- In the conclusion, the proof does not use the hypothesis $J \neq 0$: the induction gives the dual over $\operatorname{Spec} R/J$ for every $J$.
