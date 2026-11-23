---
id: positivity-theory-rg-bc-b-f-match-all-match-lmb2-2
title: Local matching at the places of a frame, with the three matching lemmas filled in
kind: theorem
decl: PositivityTheory.Rg.BcB.F.MatchAll.matchLMB2₀
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.SatakeExponents.UniformizerValuations.AdelicHeckeBlocks.HM2
covers: 421
status: drafted
drafted_by: writer@claude
---
This theorem proves `MatchLMB2`, the local matching that [the frame bound](/entry/frame-word-identity-frame-bound/) uses through `locMatch`. It is a pass-through. It applies the theorem `matchLMB2` of the same namespace to three matching lemmas `hM2`, `hM3` and [`hM4`](/entry/h-m4/), and `matchLMB2` passes them on to `matchLMB3Of_pf`. The real content is in `matchLMB3Of_pf` and in the three lemmas.

## Statement

Let $E$ be a CM field in which each finite place is unramified over the maximal real subfield (`Unr`). A datum `LocData` for $E$ and $n$ gives finite sets $T$, $S_0$ and $\mathrm{Bad}$ of places, with $B = T \cup S_0 \cup \mathrm{Bad}$. At each place $w$ it also gives a character $\mu_w$, a uniformizer, test functions and subgroups. From these it builds a function $g_0$ on the unitary group at $w$ and its powers $g_U(m)$ under convolution. On the side of $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$ it builds two matrices of local functions, `fixL a` and `betaL a`. `MOk` asks: places of $T$ are not split, with a matrix $b$ as in `IsWitt` and a uniformizer as in `IsUnifAt`; places of $S_0$ split; at places of $\mathrm{Bad}$ the function `fix` is a constant term (split places) or a congruence indicator (other places).

**Theorem** (`MatchLMB2`). If the datum satisfies `Ok` and `MOk`, then for each $a \le n$, $m \in \mathbb{N}$ and $w \in B$, the function $g_U(m+1)$ at $w$ and the $w$ entry of the trace of `fixL a` times the $m$-th power of `betaL a` match for $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$ with the character $\mu_w$ (`Match`).

## Proof

`matchLMB3Of_pf` proves `MatchLMB3Of`: six facts imply `MatchLMB2`. `matchLMB2` supplies them.

1. `MatchT`, for places of $T$: `matchT_of` from `hM4`, the Iwahori matching [`M4`](/entry/m4/).
2. `MatchSplitPlace`, for places of $S_0$: from `hM3` and `locOp3`.
3. `MatchBadS`, for split bad places: from `hM3`.
4. `MatchBadI`, for other bad places: from `hM2`.
5. `fixIdem` and `idemAlg`, two algebra facts.

`hM2` is proved by `match_principal_congruence_inert`, and `hM3` by `match_ctMu_of_isSplitAt`.

## In the Lean code

The theorem is in [HM2.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/AdelicHeckeBlocks/HM2.lean#L13). `matchLMB2` is in [MatchAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/AdelicHeckeBlocks/MatchAll.lean#L52), and `MatchLMB2` and `MOk` are in [MatchLM.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/LeviMatchingWords/MatchLM.lean#L67). We have not unfolded `matchLMB3Of_pf` or the proofs of `hM2` and `hM3`.

The file `MatchLM.lean` also states `MatchLMB2Of`, with a seventh hypothesis `MatchLin`. The proof does not use it: `MatchLMB3Of` in [SplitPlaceGeneratorPowers.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/LeviMatchingWords/SplitPlaceGeneratorPowers.lean#L54) drops it. In [SymIdx.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/SymIdx.lean#L20), `M2` and `M3` are defined by `type_of%` as the statements of `congruence_subgroup_indicator_weight` and `splitPlace_twistedConstantTerm_matches`. So each has no written form there, and `hM2` and `hM3` prove them by theorems with other names.
