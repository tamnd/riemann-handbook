---
id: end-ab-sph
title: Two theta integrals agree once one part of their constant terms agrees
kind: theorem
decl: PositivityTheory.Sph.Tr.endAB_sph
module: Development.WeilBound.ThetaLifts.SphericalLattices.SphericalClosure.EndCore
covers: 858
status: drafted
drafted_by: writer@claude
---
This theorem proves the two endgame statements `EndA` and `EndB` of the theta comparison. Each says that two matched [[theta integrals|6WB6TKE70H]] are proportional as soon as one of the two parts of their constant terms is proportional. Its user is [`closeSph`](/entry/close-sph/), which states the ten hypotheses in words. The proof assembles about 170 named facts and ends in two lemmas, `endA_of` and `endB_of`. Below it are 858 declarations.

## Statement

Fix a matched datum: number fields $E/F$ with an involution $\sigma$, a geometric datum $G$ with spaces $V$, $V'$, $W$, two Weil representations $\omega$, $\omega'$, and the local maps $R$, $R_f$, with `IsMatched`. Write $I(\Phi)$ and $I'(\Phi')$ for the two theta integrals, as functions on the [[unitary group|0R9R0Y1HDK]] $U(W)$ over the [[adeles|NYJFYZ0B4M]]. Let $H'$ be an adapted plane, with isotropic vector $x$. A *split* of a function $f$ (`Split2`) is $f_a + f_b$ such that the constant term of $f$ along the unipotent radical fixing $x$ is $f_a + f_b$, and $f_a$, $f_b$ transform under the Levi by the characters $\alpha\,|\cdot|^{a'/2}$ and $\beta\,|\cdot|^{a/2}$.

**Theorem.** Assume the ten hypotheses of [`closeSph`](/entry/close-sph/). Then:

- `EndB`: if $q \ge 1$, $c \in \mathbb{C}$, and $f_b(m) = c\,f'_b(m)$ for all matched pairs $(\Phi, \Phi')$, all splits of $I(\Phi)$ and $I'(\Phi')$ and all Levi elements $m$ with scale 1, then $I(\Phi) = c\,I'(\Phi')$ for all matched pairs;
- `EndA`: the same with $f_a$ in place of $f_b$, when $q = 0$ and $p \ge 1$.

Here $p$ and $q$ are two integers of the datum $G$ that we have not unfolded.

## Proof

Put $f = I(\Phi) - c\,I'(\Phi')$. By `diff_data`, $f$ lies in the space `Sig` and has the split $(f_a - c f'_a, f_b - c f'_b)$. The lemma `comp_zero` extends the vanishing of one part from the Levi elements to the whole group. It uses the leaves `iwa`, `ctBasic` and `matchStab`. The last says that matched pairs stay matched under the right translations that `comp_zero` needs. We have not unfolded `iwa` and `ctBasic`.

- **EndB** (`endB_of`). The $\beta$ part of $f$ is 0, so its constant term is pure $\alpha$. The lemma `sumB`, an induction on $p$ with the tower facts (`towerCodimensionTwo`, `alphaLow`, `twoStep`, base case `alphaZero`, base tower `TowerB`), shows that such an $f$ is 0.
- **EndA** (`endA_of`). The $\alpha$ part is 0, and `betaZero` kills the $\beta$ part. So the constant term of $f$ is 0, and `zero_of_line` (with `cuspOfLine`, `orthIso`, `orthAn`, `perpZero`) gives $f = 0$.

The 15 facts of the structure `Leaves` come from the hypotheses. The main routes: $\mathrm{LieSecond}$ gives `KReal`; the three finite inputs give `KFin`; `hKCo` gives `KCoinv` and then `MatchEx`; the Siegel set bound and `ArchLie` give `SigRapid`; `SiegelWeilStd` gives the anisotropic Siegel-Weil statements `SWAniso`; `EisBL` gives `EisContinues`; `WeilEx` gives the towers. The rest is bookkeeping.

## In the Lean code

The theorem is in [EndCore.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/SphericalClosure/EndCore.lean#L64). `EndA`, `EndB` and `Split2` are in [CTSmallCone.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/CTSmallCone.lean#L299). `Leaves`, `endB_of` and `endA_of` are in [TowerCodimensionTwo.lean](lean:Development/WeilBound/ThetaLifts/EigenvalueEndgame/TowerCodimensionTwo.lean#L91).

- Lines 147 to 149 only rename `hFinRam`, `hFinSplit` and `hFinInert`.
- `coneFac_of` is applied twice to the same arguments (lines 178 and 179), and `siegelWeilAniso_of` too (lines 205 and 220).
- The field `towerCodimensionTwo` of `Leaves` is filled by a fact named `TowerA2`.
