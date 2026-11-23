---
id: descent-semi-abelian
title: A semi-abelian extension from complete regular charts
kind: theorem
decl: GlobalTheory.Desc.descent_semiAbelian
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SemiAbelianDescentFromCompleteRegularCharts
covers: 658
status: drafted
drafted_by: writer@claude
---
This theorem extends an abelian scheme over a dense open subset of a normal base to a semi-abelian scheme over the whole base. The input is local: at each point, an extension over a complete regular local ring. It is the proof of [its statement form](/entry/semi-abelian-descent-from-complete-regular-charts/), which lies below the [literature step](/step/every-character-of-literature/).

## Statement

Let $S$ be a noetherian scheme whose local rings are integrally closed domains. Let $j \colon X \to S$ be a dense open immersion. Let $A$ be an abelian scheme over $X$: a group scheme that is commutative, smooth, proper, with geometrically connected fibres. Let $L$ be a line bundle on $A$, given by a cocycle, that is relatively ample: over each affine open $U \subseteq S$, a power $L^N$ has sections $s_0, \dots, s_M$ over $A_U$ whose nonvanishing loci are affine, cover $A_U$, and have coordinate rings generated over $\mathcal{O}(U)$ by the ratios $s_k/s_i$.

A *chart* of $(j, A)$ at $x \in S$ consists of:

1. a complete regular local domain $R$ of characteristic $0$, with $\xi \colon \operatorname{Spec} R \to S$ that sends the closed point to $x$;
2. the map $\mathcal{O}_{S,x} \to R$ is flat, sends $\mathfrak{m}_x$ to a set that generates $\mathfrak{m}_R$, gives a finite residue extension, and the map to the residue field of $R$ is formally unramified;
3. a semi-abelian scheme $G_R$ over $R$: smooth, separated, quasi-compact, commutative, with geometrically connected fibres, each geometric fibre an extension of an abelian variety by a split torus;
4. a lift $y \colon \operatorname{Spec} \operatorname{Frac}(R) \to X$ of $\xi$ at the generic point, and an isomorphism of group schemes $\alpha$ from the generic fibre of $G_R$ to $y^* A$.

**Theorem.** If each $x \in S$ has a chart, then there are a semi-abelian scheme $G$ over $S$ and a map $e \colon A \to G$ that identifies $A$ with $j^* G$ as group schemes. For each chart $C$ at each $x$, there is a map $\pi \colon G_R \to G$ that identifies $G_R$ with $\xi^* G$ as group schemes, and $e \circ \alpha$ equals $\pi$ on the generic fibre.

## Proof

The proof has three steps.

1. **Near each point.** [`exists_semiAbelianExtension_near_point`](/entry/exists-semi-abelian-extension-near-point/) gives, for each $s \in S$, an open $U \ni s$ such that $A|_{X \cap U}$ extends to a semi-abelian scheme over $U$. This step uses $L$ and the charts.
2. **Glue.** `extendsToSemiAbelian_of_locally_normal_noetherian` glues the local extensions to $G$ over $S$. It uses only that $S$ is noetherian and normal and that $j$ is a dense open immersion.
3. **Compare with the charts.** `exists_grpPullback_completionChart_to_extension` gives the maps $\pi$ for each chart, from $G$ and $e$.

## In the Lean code

The theorem is at [SemiAbelianDescentFromCompleteRegularCharts.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianDescentFromCompleteRegularCharts.lean#L14).

- A chart is the structure `Chart` in [SubsetSpanBy.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SubsetSpanBy.lean#L94). Condition 2 is `IsEtaleCompletion` at [IsProperToroidalModelStructureMap.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsProperToroidalModelStructureMap.lean#L347) plus the field `unr`.
- `IsSemiAbelian` and `IsAbelianScheme` are at [IsAbelianScheme.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SemiabelianSchemes/AbelianSchemeQuotients/IsAbelianScheme.lean#L41). `IsGrpPullback` (a pullback square that respects the group law) is at [IsGrpPullback.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/IsGrpPullback.lean#L25). `RelAmple` is at [NonzeroLocus.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/NonzeroLocus.lean#L33).
- Steps 2 and 3 are second names for `ExtGlue.hasExt_of_locally` and `Desc.exists_grpPullback_chart_to_ext`. We have not unfolded them.
- The charts are not used in step 2. They enter step 1, and step 3 only as the objects that it compares.
