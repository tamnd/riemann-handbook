---
id: nc-tie0-all-of
title: The normalizing constant from the archimedean bracket
kind: theorem
decl: Formalism.L2.SG.Pf.NcAllS.ncTie0All_of
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.DualFamilyCounting.NcAllS
covers: 1622
status: drafted
drafted_by: writer@claude
---
This theorem has the same conclusion as [`ncTieC_of_closed`](/entry/nc-tie-c-of-closed/): the normalizing constant `cExpl` equals $n_0 g / (\alpha \kappa)$ for the record `bCF`. It takes the archimedean identity `RealBracket` as a hypothesis, where `ncTieC_of_closed` takes `CovolRef`. The proof supplies about fifteen inputs from other files to the lemma `ncTieAllS_of` in the same file. It does no computation of its own.

## Statement

The data and the conclusion are as in [`ncTieC_of_closed`](/entry/nc-tie-c-of-closed/). The hypotheses are also the same, with two changes. The hypothesis `CovolRef` is replaced by `RealBracket`, the identity that [`RealBracket_holds`](/entry/real-bracket-holds/) proves. Of the three `Fact` instances, only `HermRepUnram` is assumed. That instance says that in an unramified CM field, each totally positive self-adjoint element $n$ has the form $a s \bar s + b t \bar t$ for given totally positive $a$, $b$.

## Proof

The proof is one call to `ncTieAllS_of` ([NcAllS.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcAllS.lean#L36)). That lemma has many more hypotheses. They are supplied as follows.

1. `SplitOm` comes from `splitOm_of_intWitt` and `integral_witt_almost_everywhere`. It gives $a' > 0$, the archimedean clause `AinfClause`, and the relation $\mu_K\, a' = \mu_{H'} \prod_v \omega_v(K_v \cdot Y)$ over the finite places. Here $Y$ is the frame of $u'$ and $\omega_v$ is the fibre measure over its Gram matrix.
2. The two parts of `SWXS` give `SWa1` (Haar measures and a fundamental domain of finite volume exist) and `StabilizerFirstChernCompatibility`.
3. Seven facts about the record `bCF` come from `MassDataX` and `MassDataConc`: `Pos`, `InMass`, `InMasses`, `InLevelS`, `InOrdinary`, `InTyped`, `InVolumes`, and $\mathrm{vol}_{H a'} = \mathrm{vol}_G$. These use `HypX`, `ProdConv`, `LocTieX`, `TypFacts`, `QuotVolPosC` and the signs of $s_d$, $C$, $\Theta$.
4. The local volumes at ordinary and typed places come from `volOrdV_holds` and `volTypV_holds`, and the index at typed places from `indexTypC_holds`.
5. The local fibre volumes `OmV` come from [`omV_holdsX`](/entry/om-v-holds-x/).
6. `FieldDict` comes from `fieldDict_holds`.

Inside `ncTieAllS_of`, the proof gets $\mu_K(K_f) > 0$ and finite from `Pos`. Then it applies `SplitOm` to get $a'$, and `RealBracket` to get the real identity. It rewrites the exponent `eDF`. Last, it calls `NcLeaves.ncTieC_of_leaves`, which does the arithmetic. We have not unfolded `ncTieC_of_leaves`.

## In the Lean code

The theorem is in [NcAllS.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcAllS.lean#L110).

`StabilizerFirstChernCompatibility` ([SiegelWeilNarrowOfWide.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/SiegelWeilNarrowOfWide.lean#L22)) does not mention a Chern class. It says that the mean of a theta series over the vectors with Gram matrix $T$ equals a product of local factors, for $2n < M$. That is the shape of a Siegel-Weil formula. The name is misleading.

`SWa1` is in a namespace called `UnusedSlot34`, but this proof uses it.

This proof uses `NcS.SplitPf.splitOm_of_intWitt`. The file `RealBracketHolds.lean` uses the copy in `NcX` for `SplitOm_holds`. The two `IntWitt` files are near duplicates.
