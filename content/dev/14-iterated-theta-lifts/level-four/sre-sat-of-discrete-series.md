---
id: sre-sat-of-discrete-series
title: S-objects over the replaced stage
kind: theorem
decl: GlobalTheory.Mem.SRe.satOfDiscreteSeries
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsSpectralObjectsOverReplacedStages
covers: 358
status: drafted
drafted_by: writer@claude
---
This theorem chooses a new S-datum from an S-pack and builds S-objects over each stage restaged with it. Through its second name [`exists_spectralObjects_over_replacedStages`](/entry/exists-spectral-objects-over-replaced-stages/) it gives `SatNew` in [`UpS.satOfDiscreteSeries`](/entry/up-s-sat-of-discrete-series/), fact 1 of [the step from level three to level four](/entry/has4-of-has3-of-s-ext-none/). The spectral work is in [`exists_sRest_top`](/entry/exists-s-rest-top/); this theorem moves its output to the restaged datum. Below it are 358 declarations.

## Statement

Let $a$ be a late stage with datum $D = a.D$. Let $R$ be real data, $F$ a face, $F_0$ a family of degree zero forms, $e_E \colon EE \to H_E$ a linear map, and $P$ an S-pack over $F_0$.

**Theorem.** Assume `DSInfChar`, `HarishChandraFinite`, `CuspRapidDecay`, `DiscreteSeriesUpqUnique` and `RowsFinDim`. Assume:

1. on $D$: `GapHyp`, `LocTied`, `RealTied`, $D^* = D^*_{\mathrm{std}}$, and `IdempotentRealFixed` (the coefficients of the idempotent $e_0$ are fixed by complex conjugation);
2. on $P$: the function $P.X.\mathrm{ph}$ is integrable for $\mu_\infty$;
3. on $R$, $F$, $e_E$: the level character condition, `grp_levels`, `GrpPin`, `IsModels`, $\operatorname{range} e_E = $ the preimage of $EE$ at the level of $F$, $\|e_E x\|^2 = n_P \|x\|^2$, and `DallTie` ($D_{\mathrm{all}} = \dim \mathrm{Mult}(R, F)$).

Then there is $Z_s$ in `SNew D` such that for all divisor data $(N, h)$ and all forms $F_1$ on the restaged datum `reL a ⟨Z_s, N, h⟩` with the same levels and values as $F_0$, the type `SAtL` is nonempty.

An element of `SAtL` is an `SAt` record on the restaged datum: an S-pack, a restriction `SRest` of it, an adelic element $t$, a constant $c > 0$, and three conditions. `SeeAt` says that $t$ is finite adelic, that $t^{-1}$ relates the level and character of $R$ to those of the pack (`ConjLevel`, not unfolded), and that a row level match holds. `EvalTieT` says that a unit vector $v_0$ and an isomorphism carry the multiplicity space onto the space $EEC$ of $L^2$ functions, with $\Phi \mapsto (x \mapsto \mathrm{ev}_{v_0}\Phi(\iota^{-1}(x)\,t))$ and $\|\cdot\|^2 = c \cdot \langle \Phi, \Phi\rangle$. `RowJ` says that the isometry $j$ of the restriction is evaluation of $e_E$ at translates by $t$, up to a positive scalar.

## Proof

1. [`exists_spectralLevel_objects_replacedStages`](/entry/exists-spectral-level-objects-replaced-stages/) gives $\dim HH(P.X) = D_{\mathrm{all}}$, an isometry $j \colon EE \to EEC$, $t$ and $c$ with the three conditions, and for each $(N, h, F_1)$ a restriction $S$ of the repacked $P$ that matches $j$.
2. Take $Z_s = $ `P.toNew hD j`, the S-data of $P$ with this dimension and $j$.
3. For given $(N, h, F_1)$, `nonempty_sAtL` builds the record. `packL` and `restL` carry $P$ and $S$ to the restaged datum, `tL` carries $t$, and `mvSee`, `mvEv_holds` and `mvRowJ` carry the three conditions.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsSpectralObjectsOverReplacedStages.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsSpectralObjectsOverReplacedStages.lean#L63). The lemmas:

- `nonempty_sAtL`, `packL` and `restL`, in the same file, lines 29 to 57.
- `SPack.toNew` in [SameDegreeZeroFormsSelf.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/SameDegreeZeroFormsSelf.lean#L64); `SAt` in [See.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/See.lean#L16).
- `mvSee` (MultREqReL.lean), `mvEv_holds` (MvEvHolds.lean) and `mvRowJ` (MvRowJ.lean). We have not unfolded them.

Most transports are `with_unfolding_all exact`. The five hypotheses are only passed on. The same name `satOfDiscreteSeries` is used for [the `SatNew` theorem](/entry/up-s-sat-of-discrete-series/) in the namespace `UpS`.
