---
id: row-form-all-p-of
title: The row form for all ties, from four global facts
kind: theorem
decl: Formalism.L2.SG.PoincareAmplitudeLowerBounds.rowFormAllP_of
module: Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors.TheoremSClosedP
covers: 330
status: drafted
drafted_by: writer@claude
---
This theorem proves `RowFormAllP`, one of the [nineteen hypotheses of Theorem S](/entry/theorem-s-leaves-of-carrier-g/). `RowFormAllP` says that the row form `RowFormC` holds at every admissible pair of words, uniformly in the constants. The proof collects the inputs of [`rowFormC_of_leaves3`](/entry/row-form-c-of-leaves3/) and applies it. That lemma holds the real content. [`theoremS_closedP`](/entry/theorem-s-closed-p/) uses `RowFormAllP` as its hypothesis `hRF`.

## Statement

**Theorem.** Assume `FormulaC`, `VolumeOddGeneric`, `VIndepAtAllP` and `NormalizingConstantPositiveAll`. Then `RowFormAllP` holds.

`RowFormAllP` says this. For all constants $C_g, c_b, C_w, c_{Tf}, C_T, C_{0f}$ with $c_b > 0$ and $c_{Tf} > 0$, there are thresholds $C'_0, C_{l,0}$ such that for $C' \ge C'_0$ and $C_l \ge C_{l,0}$ the following holds. Take a datum $D$ with ties, size data and the size hypothesis `Hyp0`, words $u \ne u'$ with `Stand` and $T_u \equiv T_{u'} \pmod{g_S^2}$, and a tie $T$ with `ConcTie`. Assume $g_i \ge 3$, the Gram determinant of $X_0$ is nonzero, $2r + 2 + f + 5 \le k$, $i_0 = i_0'$, `PtRepExists`, `NuQPin`, `RowLabel κ`, and each $\varpi_p$ is irreducible. Then `RowFormC` holds, with the local density divided by $\prod_q \alpha_D(q)$ and with $n_c$ the explicit constant `cExpl`.

## Proof

1. `VIndepAtAllP` gives the thresholds and then `VIndepAtC` at the pair.
2. `ConcTie` gives `WuDecay` and `LocTied`. With `FoldOKC_outright`, `fundExistsC_holds` and `ooIntAll_of`, `absConvC_outright` gives absolute convergence `AbsConvT`.
3. `NormalizingConstantPositiveAll` gives `NcTieC` and $c_0 c_0' > 0$.
4. `FormulaC` gives $n_c > 0$, and `tprod_alpD_pos` gives $\prod_q \alpha_D(q) > 0$.
5. Other inputs come from lemmas with no hypothesis: `primeHyp_of_stand`, `gUnramAll`, `phaseTieC_holds`, `normRepExists_of`, and `level_subgroup_properties` for $\mathrm{vol}(K_2) > 0$.
6. Apply `rowFormC_of_leaves3`.

## In the Lean code

The theorem is at [TheoremSClosedP.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/TheoremSClosedP.lean#L229), and `RowFormAllP` at line 212 of the same file. `NormalizingConstantPositiveAll` is in [RowFormAllOf.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/RowFormAllOf.lean#L214), and `FormulaC` in [TheoremSRecursion.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/TheoremSRecursion.lean#L34).

In the parent, the four hypotheses come from `formulaCT_holds`, [`volume_determined`](/entry/volume-determined/), `vIndepAtAllP_ofG` (from `UniqGap`) and `normalizing_constants_all` (from `SWXS`). The proof uses only the first part of `FormulaC`, the positivity $0 < c_{\mathrm{expl}}$. The counting identity in `Formula` is not used here.
