---
id: m-in
title: The bundle of facts on integral moduli models
kind: theorem
decl: UpperTheory.Gal.Int.Geo.CovMain.mIn
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.GeometricFlagBases.CovLink
covers: 888
status: drafted
drafted_by: writer@claude
---
This theorem proves the structure `MIn`, the bundle of facts about integral models that [the Kodaira-Spencer theorem of weight one](/entry/kodaira-spencer-of-weight-one/) uses for `ksCong_holds` and `stdEx_holds`. The proof only fills seven fields with lemmas proved elsewhere. Of the 888 declarations below it, most sit below the field `cong`, which is the entry [congKS_link](/entry/cong-ks-link/).

## Statement

`MIn` is in [FinModel.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/FinModel.lean#L38). Its fields, each a `Prop`:

- `ex` (`ModelExists`): over every noetherian ring $R$ and for every level $N \ge 3$ prime to $p$, an integral `Model b N` exists.
- `proj` (`ModelProj`): if $R$ is a domain of characteristic $0$ and $D$ satisfies `CompactB`, the structure map of the model is projective.
- `cmp` (`GenCmp`): the moduli scheme over a $\mathbb{Q}$-algebra embeds in the generic fibre by an open and closed immersion.
- `finModel` (`FinModel`): for an étale ideal $\mathfrak{a}$, there is a model `EtModel` with level structure at $\mathfrak{a}^r$, a map to the model, and a Galois cover by `LevGrp D 𝔞 r`.
- `placeOf` (`PlaceOf`): over a discrete valuation ring of characteristic $0$ with $p$ in the maximal ideal, an ideal $\mathfrak{a}$ prime to $w$ is étale if and only if a power of $(p, \omega - r)$ lies in $\mathfrak{a}$.
- `cong` (`CongKS`): Hecke correspondences $T_j$ on the special fibre satisfy a pointwise congruence relation. See [congKS_link](/entry/cong-ks-link/).
- `corr` (`CorrBC`): every base change of $T_j$ is finite, étale after $p$ is inverted, with fibres of the size of the Grassmannian of $j$-planes in $(\mathcal{O}_F/w)^n$.

The first three fields are in [EtLevForget.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/EtLevForget.lean#L22).

## Proof

The proof is in [CovLink.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/CovLink.lean#L21). Each field is one term:

- `ex`, `proj` and `cmp` are `harrisTaylorIntegralModel_nonempty`, `Model.isProjOver_of_compactB` and `exists_open_closed_immersion_genModel_to_fibre`.
- `finModel` is `finModel_holds` applied to a covering lemma built from `repAll`, `repMul`, `ptAll`, `idealInd`, `crtMul`, `crtProj` and `grpFin`.
- `placeOf` is `placeOf_holds`.
- `cong` is `congKS_link`.
- `corr` is `corrBC_holds quotObj_link`.

## In the Lean code

Three theorems follow on lines 31 to 33: `ksCong_holds`, `stdEx_holds` and `ksCover_holds`, each one projection lemma applied to `mIn`. [KsGoodHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/FiniteEtaleModels/KsGoodHolds.lean#L31) uses `mIn` again in five theorems. The fields `ex` and `cmp` have the same text as the inputs `ModelEx` and `GenCmp` of [gUnif_of](/entry/g-unif-of/), in [LevelChange.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/LevelChange.lean#L219). They are copies in another namespace, and the same lemmas prove them.
