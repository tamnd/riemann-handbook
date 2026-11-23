---
id: nc-tie-all-s-of
title: The normalizing constant from the split and the archimedean bracket
kind: theorem
decl: Formalism.L2.SG.Pf.NcAllS.ncTieAllS_of
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.DualFamilyCounting.NcAllS
covers: 311
status: drafted
drafted_by: writer@claude
---
This lemma proves the closed form $c_{\mathrm{expl}} = n_0 g / (\alpha \kappa)$ for the record `bCF`, from two global identities taken as hypotheses: the finite split `SplitOm` and the archimedean identity `RealBracket`. Its only caller is [`ncTie0All_of`](/entry/nc-tie0-all-of/), which supplies all hypotheses. The lemma makes the two identities concrete and passes them to [`ncTieC_of_leaves`](/entry/nc-tie-c-of-leaves/), where the arithmetic is done.

## Statement

The data, the record $B = $ `bCF` and the conclusion `NcTieC` are as in [`ncTieC_of_closed`](/entry/nc-tie-c-of-closed/). The hypotheses are those of [`ncTie0All_of`](/entry/nc-tie0-all-of/), with these changes:

1. `SplitOm` and `RealBracket` are hypotheses. They are quantified over all settings.
2. The facts about $B$ (`Pos`, `InMass`, `InMasses`, `InLevelS`, `InOrdinary`, `InTyped`, `InVolumes`, $\mathrm{vol}_{H a'} = \mathrm{vol}_G$) are hypotheses, not derived from `MassDataX`.
3. The local inputs `VolOrdV`, `VolTypV`, `IndexTypC`, `OmV`, `FieldDict` and `ProdConv` are hypotheses.
4. `SWa1` and `StabilizerFirstChernCompatibility` appear as two separate hypotheses.

**Lemma.** Under these hypotheses, `NcTieC` holds for $c_{\mathrm{expl}}$.

## Proof

1. `Pos` says that the quotient $\mu_{G_f}(K_f) / \prod_{v \text{ typed}} \mu_{G_v}(K_v)$ is positive, and that each factor $\mu_{G_v}(K_v)$ at a typed place is positive. So $0 < \mu_{G_f}(K_f) < \infty$, and $\mu_K = \mu_{G_f}(K_f)$.
2. `SplitOm`, applied to the frame of $u'$, gives $a' > 0$, the clause `AinfClause` at infinity, and $\mu_K\, a' = \mu_{H'} \prod_v \omega_v(K_v \cdot Y)$. The bound $2(2r+1) < n$ that it needs comes from $n = R$, a field of `FieldDict`, and from relations between the ranks.
3. `RealBracket`, applied to $a'$, gives the real identity of [`RealBracket_holds`](/entry/real-bracket-holds/). The exponent `eDF` is unfolded to $-(8r^3 + 6r^2 + 6kr^2 + r)/3$.
4. The lemma calls `ncTieC_of_leaves` with $a'$, the two identities and the other hypotheses.

The rest is bookkeeping.

## In the Lean code

The lemma is in [NcAllS.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcAllS.lean#L36). `SplitOm` is the version in [NcSplitS.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcSplitS.lean#L13). The file [RealBracketHolds.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/RealBracketHolds.lean#L24) proves a near duplicate, `NcSplit.SplitOm`, as `SplitOm_holds`; this lemma does not use it.

The lemma calls only `Formalism.L2.SG.Pf.NcLeaves.ncTieC_of_leaves`. It does no estimate of its own. The proof states three facts about the ranks (`hk5`, `hm`, `hr`) for the `omega` call that proves the bound on $n$.
