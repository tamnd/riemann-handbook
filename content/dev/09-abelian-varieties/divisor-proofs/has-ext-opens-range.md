---
id: has-ext-opens-range
title: The semi-abelian extension over one affine open
kind: theorem
decl: GlobalTheory.Desc.hasExt_opensRange
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsSemiAbelianExtensionNearPoint
covers: 644
status: drafted
drafted_by: writer@claude
---
This theorem extends an abelian scheme to a semi-abelian scheme over one affine open of the base, given a chart at each point. Its only user is [`exists_hasExt_near`](/entry/exists-has-ext-near/), which applies it to an affine open neighbourhood of a given point. The theorem reduces to the case $X = \operatorname{Spec} R_f$, $S = \operatorname{Spec} R$, which is [`extendsToSemiAbelian_away_of_charts`](/entry/extends-to-semi-abelian-away-of-charts/). That case has the real content.

## Statement

Let $S$ be a noetherian normal scheme and $j \colon X \to S$ a dense open immersion. Let $A$ be an abelian scheme over $X$ (in Lean, `IsAbelianScheme`: a commutative group scheme that is smooth, proper and geometrically connected). Let $L$ be a line bundle on $A$, given by a cocycle, that is relatively ample over $X$.

A *semi-abelian scheme* (`IsSemiAbelian`) is a commutative group scheme that is smooth, separated, quasi-compact and geometrically connected, and whose geometric fibres are extensions of abelian varieties by split tori.

A *chart of $A$ at $x \in S$* (`Chart j A x`) consists of:

- a complete regular local domain $R_x$ of characteristic 0 and a map $\xi \colon \operatorname{Spec} R_x \to S$ that sends the closed point to $x$, such that $\mathcal{O}_{S,x} \to R_x$ is flat, $\mathfrak{m}_x R_x = \mathfrak{m}_{R_x}$, and the residue field of $R_x$ is finite and formally unramified over $\kappa(x)$;
- a semi-abelian scheme $G_x$ over $\operatorname{Spec} R_x$;
- a lift $y \colon \operatorname{Spec} \operatorname{Frac}(R_x) \to X$ of $\xi$ at the generic point, and an identification of the generic fibre of $G_x$ with $y^* A$ as group schemes.

We say that *$A$ extends over $S$* (`HasExt j A`) if there are a semi-abelian scheme $G$ over $S$ and a map $e \colon A \to G$ that identifies $A$ with $G \times_S X$ as group schemes.

**Theorem.** Suppose that $A$ has a chart at each point of $S$. Let $R$ be a noetherian integrally closed domain and $i \colon \operatorname{Spec} R \to S$ an open immersion with image $U$. Then $A|_{j^{-1}(U)}$ extends over $U$.

## Proof

1. Since $X$ is dense, $j(X)$ meets $U$. So there is $f \in R$, $f \neq 0$, with $\emptyset \neq D(f) \subseteq i^{-1}(j(X))$. On $\operatorname{Spec} R_f$, the map $i$ factors through an open immersion $k \colon \operatorname{Spec} R_f \to X$.
2. The pullback $k^* A$ is an abelian scheme, and the pullback of $L$ is relatively ample (`relAmple_pull`).
3. `Chart.nonempty_restrict`: a chart of $A$ at $i(x)$ gives a chart of $k^* A$ at $x$, relative to $\operatorname{Spec} R_f \to \operatorname{Spec} R$. The proof lifts $\xi$ through $i$. Since $\xi$ is flat, the generic point of $\operatorname{Spec} R_x$ goes into $\operatorname{Spec} R_f$.
4. [`extendsToSemiAbelian_away_of_charts`](/entry/extends-to-semi-abelian-away-of-charts/): $k^* A$ extends over $\operatorname{Spec} R$.
5. `HasExt.of_comp` moves this extension along the isomorphism $\operatorname{Spec} R \cong U$.
6. `HasExt.of_dense`: $\operatorname{Spec} R_f$ is dense in $j^{-1}(U)$. So $G|_{j^{-1}(U)}$ and $A|_{j^{-1}(U)}$ are two semi-abelian models of $k^*A$ over the noetherian normal scheme $j^{-1}(U)$. They are isomorphic by `semiAbelianHomExtension_holds.existsUnique_iso_of_extensions`. So $G$ extends $A|_{j^{-1}(U)}$.

The rest is bookkeeping.

## In the Lean code

The theorem is at [ExistsSemiAbelianExtensionNearPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSemiAbelianExtensionNearPoint.lean#L111). `Chart`, `HasExt` and `awayMap` are in [SubsetSpanBy.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SubsetSpanBy.lean#L94). The lemmas it calls:

- `HasExt.of_comp`, `HasExt.of_dense` and `Chart.nonempty_restrict`, in the same file;
- `GlobalTheory.T.extendsToSemiAbelian_away_of_charts`;
- `relAmple_pull` and `isAbelianScheme_pullback_obj` for the pullbacks.

The hypothesis asks for a chart at each point of $S$. The proof uses only the charts at points of $U$. The name `IsEtaleCompletion` of the condition on $\mathcal{O}_{S,x} \to R_x$ says only: flat, $\mathfrak{m}_x R_x = \mathfrak{m}_{R_x}$, finite residue extension. Completeness is a separate field of `Chart`.
