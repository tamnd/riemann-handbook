---
id: exists-spectral-objects-over-replaced-stages
title: Spectral objects over replaced stages, a second name
kind: theorem
decl: GlobalTheory.T.exists_spectralObjects_over_replacedStages
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsSpectralObjectsOverReplacedStagesStatement
covers: 359
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`GlobalTheory.Mem.SRe.satOfDiscreteSeries`](/entry/sre-sat-of-discrete-series/). Its statement is that theorem's statement, word for word, and its proof only applies it. Its one user is [`UpS.satOfDiscreteSeries`](/entry/up-s-sat-of-discrete-series/), which proves `SatNew` with it. Below it are 359 declarations.

## Statement

Assume the five spectral hypotheses `DSInfChar`, `HarishChandraFinite`, `CuspRapidDecay`, `DiscreteSeriesUpqUnique` and `RowsFinDim`. Let $a$ be a late stage over a base $B$ and columns $C$, with datum $a.D$. Let $R$, $F$ and $e_E$ be real data, a face and a map that satisfy the seven row conditions, and let $P$ be an S-pack over forms $F_0$ that satisfies the gap, integrability, local, real, $D^*$ and idempotent conditions. Then there is a new S-datum $Z_s$ such that for all divisor data $(N, h)$ and all forms $F_1$ that agree with $F_0$, the type of S-objects `SAtL` at the restaged datum is nonempty.

The hypotheses are listed in full in [the S-stage theorem](/entry/sre-sat-of-discrete-series/).

## Proof

The proof is one tactic line that applies `GlobalTheory.Mem.SRe.satOfDiscreteSeries`.

## In the Lean code

The theorem is in [ExistsSpectralObjectsOverReplacedStagesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsSpectralObjectsOverReplacedStagesStatement.lean#L11). The proof is `first | exact @satOfDiscreteSeries | exact satOfDiscreteSeries | (intros; apply satOfDiscreteSeries <;> assumption)`: three forms of the same call. "Replaced stages" refers to the restaged datum `reL a Z`, the late stage $a$ with its S-stage replaced by $Z_s$ and its divisor stage replaced by $(N, h)$ ([RelabelledWeight.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/RelabelledWeight.lean#L38)).
