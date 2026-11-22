---
id: ht-bij
title: The Hodge-Tate map is bijective for smooth projective models
kind: theorem
decl: UpperTheory.Gal.Seam.HT.htBij
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.CrystallineTowers.ClosedHT
covers: 1802
status: drafted
drafted_by: writer@claude
---
This theorem says that a Hodge-Tate comparison map exists and is bijective on the cohomology of a smooth projective model over a $p$-adic field. Its only use is in [htSpecGood](/entry/ht-spec-good/), which turns it into period matrices. The proof only applies [htBij_of](/entry/ht-bij-of/) to four proved facts. The real content is in that entry.

## Statement

Let $\ell$, $K$, a good model $M$ and $V^n$ be as in [htSpecGood](/entry/ht-spec-good/). Let $\mathrm{Hdg}(a, n)$ be the Hodge pieces of the generic fibre.

**Theorem.** There is a pairing $P$ (a structure `HTPre`) which sends $v \in V^n$ to a $\mathbb{C}_\ell$-valued function on $\mathrm{Hdg}(a,n)^\vee$ for each $a$, and which is linear, $G_K$-equivariant up to the twist $\chi^a$, natural in $M$, and compatible with cup products, the unit class and first Chern classes. For each good model $M$:

1. for each $n$, the induced map $V^n \otimes \mathbb{C}_\ell \to \bigoplus_a \mathrm{Hdg}(a,n) \otimes_K \mathbb{C}_\ell$ is injective;
2. if $X_K$ is connected and smooth of dimension $d$, the part in degree $2d$ and $a = d$ is injective;
3. if $p$ is smooth of relative dimension $d$, then for each $n$ the map is onto, and $\dim_{\mathbb{Q}_\ell} V^n = \sum_{a=0}^{n} \dim_K \mathrm{Hdg}(a, n)$.

## Proof

It is `Onto.htBij_of` applied to:

- `hodgeTate_comparison_smooth_projective`: $P$ exists with clauses 1 and 2 (`HodgeTateMapExists`);
- `G.sqEx3`: for a model of relative dimension at least 2, there is an object `Sq` over it whose map `S.D.f` is étale;
- `Top.diagEt3_holds`, a decomposition of classes on that object;
- `Top.etFin_holds`: each $V^n$ has finite dimension.

## In the Lean code

The theorem is in [ClosedHT.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/ClosedHT.lean#L19). `HTBij` is in [HtBijOfParts.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/HtBijOfParts.lean#L11), and `HTPre` in [IsEtaleFirstChernUntwisted.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/IsEtaleFirstChernUntwisted.lean#L39). We have not unfolded `Sq` or the conclusion of `DiagEt3`. The local theorem `hodgeTate_comparison_smooth_projective` at line 17 has the same name as a theorem in `CrystallineSemistableComparison.HT` with other hypotheses.
