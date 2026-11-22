---
id: member-e-closing-alt-alt
title: The membership statement from the construction steps
kind: theorem
decl: GlobalTheory.Mem.Top.Closing.memberE_closing_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MemberEClosing
covers: 5216
status: drafted
drafted_by: writer@claude
---
This theorem proves the membership statement `MemberE` for the parameter of a norm choice extension $N$, from named literature hypotheses and from step conditions for $N$ and a refinement $N_g$. It is step 2 of the [pair theorem](/entry/exists-base-lattice-of-pair-alt/). It does no work of its own: it supplies the inputs of [`exists_member_of_construction_steps_secondPass`](/entry/exists-member-of-construction-steps-second-pass/), which has the content.

## Statement

The words *parameter*, $p(N)$, *slot* and `MemberE` are as in the [entry of the membership theorem](/entry/member-bundles-large-unramified-exponents-alt/). Write $s = p(N).s$ and $s_g = p(N_g).s$.

**Theorem.** Assume nineteen propositions. Sixteen are named after published results or objects: ray class fields, principal ideals, CM curves with good reduction outside a prime, `DSInfChar`, Harish-Chandra finiteness, rapid decay of cusp forms (twice), uniqueness of discrete series of $U(p,q)$, `RowsFinDim`, Siegel-Weil convergence, existence of discrete series, a formal degree formula, the Siegel mass ratio for CM fields, the Weil representation of a unitary pair, Casselman-Wallach, Harish-Chandra modules. The other three are statements on discrete series, written out in full:

- for each $n$, signature $\varepsilon$ and Harish-Chandra parameter $\lambda$ (strictly decreasing, with $\lambda_a - \frac{n-1}{2} \in \mathbb Z$), there is a Hilbert space $H$ and a map $\sigma$ on $n \times n$ complex matrices with `IsDS ε λ σ`: on the set $U_\varepsilon$ = `UJset ε`, $\sigma$ is an irreducible, square integrable, unitary representation, with a $K$-type at `lowK ε λ` that is minimal for the norm `vNormSq`;
- two such representations with the same $\varepsilon$ and $\lambda$ are unitarily equivalent on $U_\varepsilon$ (we have not unfolded `inUJ`, the predicate that defines $U_\varepsilon$);
- for each group datum `GrpData p q` and each parameter with `IsParam`, there is a discrete series datum `DSRep` with that parameter.

Let `hL : RecTExists` and let $N, N_g$ be norm choice extensions. Assume `StepW Start (Has3 s)`, `LevelThreeCondition` for $s$ and for $s_g$, `ExportF KPx (IsBuiltE s)`, the pass condition into bases with a level three object for $s_g$ (as in the [pair theorem](/entry/exists-base-lattice-of-pair-alt/)), and that each datum of $N_g$ gives a datum of $N$ at which `GoodO` holds. Then `MemberE` $s$.

## Proof

The proof is one call of [`exists_member_of_construction_steps_secondPass`](/entry/exists-member-of-construction-steps-second-pass/) with the two slots $s$ and $s_g$. Its inputs are made as follows, for $s$ and again for $s_g$:

- the step from level three to level four, `StepW (pinAnd (Has3 ·)) (Has4 ·)`, by [`has4_of_has3_of_lv3Mv`](/entry/has4-of-has3-of-lv3-mv/) from nine of the hypotheses and the level three condition;
- `AmbEx`, by `ambEx_of_rx`, because the position of both slots is `RX`;
- `DivEx`, by `divEx_geoCl` from the first three hypotheses;
- `ThEx`, by `exists_thetaData_trueRowsColumns_allCompatible` from seven hypotheses (the Weil representation, rapid decay, Casselman-Wallach, Harish-Chandra modules and the three discrete series statements), with `io_zero` for its side condition.

The hypotheses `Has3`, `ExportF` and the pass condition are passed on unchanged. The last input says that built points of $s_g$ are good points of $s$ with the twist condition `TwAllAt`. It comes from `goodE_of_builtE_alt` and the map from $N_g$ to $N$. The rest is bookkeeping.

## In the Lean code

The theorem is in [MemberEClosing.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberEClosing.lean#L17). The lemmas it calls are `exists_member_of_construction_steps_secondPass`, `has4_of_has3_of_lv3Mv` (twice), `ambEx_of_rx`, `divEx_geoCl`, `exists_thetaData_trueRowsColumns_allCompatible` (twice), `io_zero` and `goodE_of_builtE_alt`.

Odd points:

- `CuspRapidDecay` is a hypothesis twice (the sixth and the fourteenth). The caller passes the same field `a6` of `HypAAlt` to both.
- The local names of the hypotheses skip `s7`. This has no effect.
- We have not checked that the three discrete series statements are correct forms of Harish-Chandra's results. They are hypotheses here.
