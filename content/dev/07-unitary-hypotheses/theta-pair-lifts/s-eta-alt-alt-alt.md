---
id: s-eta-alt-alt-alt
title: The eta statement from the point statement
kind: theorem
decl: GlobalTheory.StEta.sEta_alt_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SLarge
covers: 375
status: drafted
drafted_by: writer@claude
---
This theorem proves `EtaStatement'` from `PointStatement` and the published inputs. In [the stage statements](/entry/all-stages-of-specializations-alt/) it is the first step of item 6. Its result goes to [`sFin_and_sFinl_of_archCmp_sEta_thetaData`](/entry/s-fin-and-s-finl-of-arch-cmp-s-eta-theta-data/), and from there, at each stage, to hypothesis $h_E$ of [the level 3 record](/entry/lv3-of-third-alt-alt/).

## Statement

Fix a stage $x$ of a datum $P$ with a `StrictHenselianAcyclicLevel` datum $l$, and its data $A$, $M$, $\chi$ and `tup`. For a property $Q$ of data of type `D7`, `ForcedByAutomorphicSemisimpleData A M χ tup Q` says: there is a finite set `big` of complex numbers at each place such that $Q(D')$ holds for $D' = $ `withLoc L` for all $L$ built for `big`. A datum built for a larger `big` is also built for a smaller one, so this is about all large enough coefficient rings. We write "$Q$ holds eventually".

- `PointStatement hL`: at every such $(x, l)$, eventually $D'$ satisfies `EigSpan` and `IsotInternal`, and, if `hypO` holds, also `provisionFortyOne`, `ResidualIrreducibleGood`, `Conclusion42` and `ConclusionZ`.
- `EtaStatement' hL`: at every such $(x, l)$, if the automorphic side exists, then eventually $D'$ is `Large` and $\eta_j(v)$ for $D'$ equals $\eta_j(v)$ for $P$, for $1 \le j \le m$.

`Large D'` is `hypO ∧ OSplit ∧ TakenAll`.

**Theorem.** If `PublishedInputsThirdLayerAlt` holds, then `PointStatement hL` implies `EtaStatement' hL`.

## Proof

1. Six lemmas give, at every stage: eventually, under `hypO`, the $\eta_j$ agree (`eventually_etaJ_eq_eta_of_levelC`); $\mathrm{LL}_0$ is stable under `star`; each `eExp` is an integer; the places over `pde` and `pde'` split; `ChebSplit` holds; eventually `GaloisRepsCusp` holds.
2. The laws of "eventually" (`evO_laws_alt`: conjunction and monotonicity) turn the point statement and the last fact into one eventual property.
3. `large_of_large_rings_alt`, in the same file, gives that $D'$ is eventually `Large`. It gets `hypO` from `side_eigen_rationality_alt`, `OSplit` from `side_multiplicity_cusp_alt`, and `TakenAll` from `side_eigen_hecke_match_alt`, with the input `Cheb`.
4. A last conjunction with step 1 gives the $\eta_j$, since `Large` contains `hypO`.

## In the Lean code

The theorem is in [SLarge.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SLarge.lean#L56). The two statements are in [ThetaDataExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ThetaDataExists.lean#L42) and [SameGaloisLevelExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SameGaloisLevelExists.lean#L50).

- The proof uses only the field `cheb` directly; the six lemmas take the whole record.
- Step 2 keeps only `provisionFortyOne` and `ResidualIrreducibleGood` from the point statement and drops `EigSpan`, `IsotInternal`, `Conclusion42` and `ConclusionZ`. The $\eta$ lemma of step 1 also takes the whole point statement; we have not read its proof.
- Under the published inputs, the premise "the automorphic side exists" always holds at these stages: [`builtEx_of_published_inputs'`](/entry/built-ex-of-published-inputs-prime/) proves it.
- No `sEta_alt` or `sEta_alt_alt` exists in the source. The older `sEta` in [SEta.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SEta.lean#L21) has the same shape, with `BuiltEx` and `EvO`.
