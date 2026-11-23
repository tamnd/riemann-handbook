---
id: pb-applied
title: The abstract pair bound, with its leaves supplied
kind: theorem
decl: Formalism.L2.SG.TheoremS.pbApplied
module: Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors.TheoremS
covers: 893
status: drafted
drafted_by: writer@claude
---
This theorem is the abstract form of Theorem S. For an abstract term series $X$ it bounds $\|K_0\|^2$ by $(1 + b^{-6})\, d$, with $d = d_u d_{u'} / D^*$. Its only user is [`theoremS_rec`](/entry/theorem-s-rec/), which puts the concrete series $t_O(u, u')$ in place of $X$. The proof is an assembly.

## Statement

A term series $X$ (`Terms`) splits its terms into identity, degenerate ($G = 0$), generic and non-generic terms, and $K_0 = K_{\mathrm{id}} + K_{\mathrm{gen}} + K_{\mathrm{ng}}$, with no degenerate part. The row conditions `RowBig`, `RowNotScalar`, `RowMain` and `RowNG` each bound a sum over pairs of terms, weighted by $\Gamma_1$, by a constant times $d$.

**Theorem.** For $C_4 \ge 1$ and $C_{\mathrm{thr}}$ there are $C_A \ge \max(C_{\mathrm{thr}}, 1)$ and $0 \le C \le C_A$. For $C_0 \ge 1$, $C_G \ge 0$, $C_\Delta > 4$ and $c_T, C_b > 0$ with $c_T C_b > 1$ there is $k_0$ with this property. Let $E$ be a CM field with datum $D$, size datum $G$ with $k_0 \le k$, mass data $B$ and term series $X$. Assume `SzHyp`, `Unram E`, `J.Inst`, `LocalModel D`, `RealInputs`, `DensInput`, `RowsInput`, `MassDataHyp`, `EnergyLink`, `Link X B`, `SplitInputs X` and `SizeNumbers`. Assume `RowBig` and `RowNotScalar` with $\varepsilon = e^{-c_5 k f \log k}$, and `RowNG` with $\varepsilon' = 2^{-(k-2r-5)} e^{C_n (2r+2)^5 f \log b}$. Then
$$\|K_0\|^2 \le (1 + b^{-6})\, d.$$

## Proof

The proof applies `t_PairBoundFromLocal` to 19 proved lemmas, in three groups:

- the main row: `t_MainRow`, `localCores`, `globalCores`, `t_LatticeLink`, `t_AxiomsOfLocalModel` and `lattice_average_induction`;
- the abstract bound: `t_PairBound`, `t_PairBoundAbstract`, `t_PriceOfIota`, `t_EqualIota`, `t_PairSplit` and `t_SubFamily`;
- the numerics: `t_NumPrice`, `t_NumExp`, `t_NumDens`, `t_NumLoops`, `t_NumNG`, `t_NGExponent` and `t_EtaZero`.

`MainRow` gives $\Gamma_1 \Sigma \le (1+\delta) e_1 d$ with $\delta \le b^{-7}$. By `Link`, this is `RowMain` with $A = (1+\delta) e_1$. `PairBoundAbstract` then gives
$$\|K_0\|^2 \le \Bigl(\sqrt{P_g (A + 2\varepsilon)} + \sqrt{P_g (\varepsilon + \varepsilon')}\Bigr)^2 d,$$
with $P_g = (1 + 3/g_1)^f (1 + 3/g_2)^f$. The numerics bound the bracket by $1 + b^{-6}$. We have not read the proofs of `MainRow` and `PairBoundAbstract`.

## In the Lean code

The theorem is at [TheoremS.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/TheoremS.lean#L19). The definitions are in [StatementPB.lean](lean:Formalism/HermitianCurvature/StatementPB.lean#L435), and `t_PairBoundFromLocal` is in [GrowthOfBasic.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/GrowthOfBasic.lean#L1236).

Three lemma names do not match their statements. `t_PriceOfIota` proves `NormSqBoundOfEqualIota`, `t_EqualIota` proves `GramSumLeOfPosSemidef`, and `t_EtaZero` proves `SqrtSumSqLeOneAddInvPowSix`. The last conjunct of `SplitInputs`, $G_{ii} = \Gamma_1$, is not used.
