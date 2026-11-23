---
id: hom-fix-finite-type
title: Polarized homomorphisms over a locally noetherian base, by gluing affine pieces
kind: theorem
decl: GlobalTheory.HomFixGlue.homFix_finiteType
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFiniteTypeRepresentingPolarizedHomsLocNoet
covers: 454
status: drafted
drafted_by: writer@claude
---
This theorem proves [its statement form](/entry/exists-finite-type-representing-polarized-homs-loc-noeth/). It passes from an affine noetherian base to a locally noetherian base $S$. It covers $S$ by affine opens, uses the affine case on each, and glues. The result goes to [the finiteness of polarized homomorphisms](/entry/exists-finite-unramified/).

## Statement

Let $S$, $A$, $B$, $L$, $M$ be as in [the statement of the finite case](/entry/exists-finite-unramified-representing-polarized-homs/): $S$ locally noetherian, $A$ and $B$ abelian schemes over $S$, $L$ and $M$ rigidified and relatively ample line bundles on them.

**Theorem.** There is a scheme $\pi \colon H \to S$ that represents the homomorphisms $\Phi \colon A_T \to B_T$ with $\Phi^*M_T \cong L_T$, with $\pi$ quasi-compact, separated and locally of finite type.

## Proof

1. **Gluing.** `GlobalTheory.T.homFixedPullback_representable_glue` takes a family of open immersions $V_i \to S$ that covers $S$, and over each $V_i$ a representing object for the restrictions $A_{V_i}$, $B_{V_i}$, $L|_{V_i}$, $M|_{V_i}$ that is quasi-compact, separated and locally of finite type. It returns a representing object over $S$ with the same three properties. It does not ask for ampleness.
2. **The local-to-global input.** The gluing lemma takes one more hypothesis, a statement: for a homomorphism $\Phi \colon A \to B$ of abelian schemes over a base $H$ and rigidified bundles $L$, $M$, if $L \cong \Phi^*M$ locally over $H$, then $L \cong \Phi^*M$ on all of $A$. The proof supplies it as `GlobalTheory.T.rigidifiedBundle_pullbackIso_of_localIso_abelianHom`.
3. **The cover.** Take all affine opens $U$ of $S$, with the open immersions $\operatorname{Spec} \Gamma(S, U) \to S$. Each point lies in one.
4. **The affine pieces.** On each $U$ the ring $\Gamma(S, U)$ is noetherian, since $S$ is locally noetherian. `GlobalTheory.T.exists_abelianScheme_restrict_openImmersion` restricts $A$, $L$ (and $B$, $M$) to $\operatorname{Spec}\Gamma(S, U)$ and keeps the four properties: abelian scheme, line bundle, rigidified, relatively ample. Then [the affine case](/entry/exists-finite-type-scheme-representing-polarized-homs/) gives the local representing objects.

## In the Lean code

The theorem is in [ExistsFiniteTypeRepresentingPolarizedHomsLocNoet.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteTypeRepresentingPolarizedHomsLocNoet.lean#L17). The lemmas it calls:

- `GlobalTheory.T.homFixedPullback_representable_glue`;
- `GlobalTheory.T.rigidifiedBundle_pullbackIso_of_localIso_abelianHom`;
- `GlobalTheory.T.exists_abelianScheme_restrict_openImmersion`;
- `GlobalTheory.T.exists_finiteType_scheme_representing_polarizedHoms`.

We read only the statements of these four lemmas. The local-to-global statement of step 2 is a hypothesis of the gluing lemma, not a lemma that it imports, so this proof must pass it in. The ampleness of $L$ and $M$ is used only in step 4.
