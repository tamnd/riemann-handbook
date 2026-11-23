---
id: kodaira-spencer-of-weight-one
title: Six facts about towers of fibre powers, given the Lefschetz formula
kind: theorem
decl: UpperTheory.Gal.Int.Geo.kodaira_spencer_of_weight_one
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.GeometricFlagBases.GeometricRealizationOfWeightOne
covers: 11907
status: drafted
drafted_by: writer@claude
---
This theorem proves `KSAll`, six facts about the towers of Shimura-type varieties that carry the Galois representations of the Galois row. It is the second part of [the Galois row from geometry](/entry/geometric-realization-of-weight-one/), where `KSAll` turns each plan into a pack. Its proof only collects six proved facts. The holomorphic Lefschetz formula $\mathrm{HLF}$ enters in one of them, through [ksHodge_of_geo](/entry/ks-hodge-of-geo/).

## Statement

Fix a prime $p$, a PEL-type datum $D$ (`Datum`) with CM field $F$, a group datum $G$ (`HTGroup`, a central simple algebra over a CM field with an involution), and a link $L$ between them. The *scope* condition `Sc` asks $D.a = 1$, $D.m = 1$, $G.a = 1$, $n = G.n$ odd and `CompactB`. A *level* is an integer $N \geq 3$ prime to $p$, with compact open group $K_N$.

For a field $R \supseteq \mathbb{Q}$, a base point `gb` over $R$ and $k \geq 0$, a *tower* `KS L gb k` is a tower $X$ over $\operatorname{Spec} R$ with group $G(\mathbb{A}_f)$, indexed by levels, with group $K_N$ at level $N$ and Hecke elements the integral $h$. Its level $N$ is identified with the $k$-th fibre power of the universal abelian scheme over a fine moduli model `M N`, and its transition maps come from isogenies. For $N$ and Hecke data $g$, the tower gives a Hecke tower `T.tower N g`.

**Theorem.** If $\mathrm{HLF}$ holds, then `KSAll` holds, that is:

1. `StdEx`: if $D.a = 1$, each number field $E \cong F$ has a standard base point;
2. `KSEx`: under `Sc`, a tower `KS L gb k` exists for each $R$, `gb` and $k$;
3. `KSNice`: each Hecke tower `T.tower N g` is `Nice`;
4. `KSGood`: at a place $w$ that matches a prime of $F$ where the Hecke data are good (`GoodGrp`), the Hecke tower is good at $w$ (`GoodAtW`);
5. `KSCong`: the same with congruences (`CongGrp` gives `CongAtW`);
6. `KSHodge`: for each dominant weight $\lambda$ there is $k$ such that, on any tower `KS L gb k`, every Hecke eigensystem $\theta$ that occurs in weight $\lambda$ occurs in Dolbeault cohomology $H^{a,b}$ of the tower, after base change to $\mathbb{C}$ and a twist by $\sigma \in \operatorname{Aut}(\mathbb{C})$, for each exponent $a$ in the list given by `IsHExp`.

We have not unfolded `Nice`, `GoodAtW`, `CongAtW`, `GoodGrp` or `CongGrp`. Clause 6 is stated in full in [ksHodge_of_geo](/entry/ks-hodge-of-geo/).

## Proof

The proof is the tuple of six proved facts:

- `CovMain.stdEx_holds` and `CovMain.ksCong_holds`, from `mIn`, a bundle of facts about integral models (existence, projectivity, finite models, congruences);
- `G3.kSEx_holds`, from `kNBasic_holds` and seven facts about the witnesses of Hecke translations;
- `G3.kSNice_holds`, from `kNBasic_holds`, the smoothness of fibre powers (`powSm_holds`), `twFEt_holds` and `sigmaFEt_holds` (not unfolded);
- `FiniteEtaleModels.ksGood_holds`;
- `LocalSmoothExtension.ksHodge_of_geo hW FixZ.FixK_holds`, see [ksHodge_of_geo](/entry/ks-hodge-of-geo/) and [FixK_holds](/entry/fix-k-holds/).

Only the last one uses $\mathrm{HLF}$. The written proof lists the largest children: [model_nonempty](/entry/model-nonempty/) (2,597), [ksHodge_of_geo](/entry/ks-hodge-of-geo/) (1,902) and [FixK_holds](/entry/fix-k-holds/) (1,789).

## In the Lean code

The theorem is in [GeometricRealizationOfWeightOne.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/GeometricRealizationOfWeightOne.lean#L22). `KSAll` and `KSHodge` are in [PackExOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PackExOf.lean#L93). The structure `KS` and the other five facts are in [IntegOfMem.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/IntegOfMem.lean#L48).

The names say Kodaira-Spencer. The structure `KS` holds a tower of fibre powers of a universal abelian scheme, and no Kodaira-Spencer map appears in the six statements as far as we unfolded them.
