---
id: down7-inclusion-w-seven-real-holds
title: The lattice inclusion at the coarse weight bound, from the short bound
kind: theorem
decl: Formalism.CohomologicalDescent.Down7.inclusion_w_seven_real_holds
module: Formalism.PieriBlockIdeals.PieriColumnMinors.CorollaryOfParamsSevenLinkage
covers: 888
status: drafted
drafted_by: writer@claude
---
This theorem moves the lattice inclusion of a Hida setting from the short weight bound $J_W(l)$ up to the coarse weight bound $c_W(l)$. The inclusion itself comes from [`Down.inclusion_w_real_holds`](/entry/down-inclusion-w-real-holds/); this proof only shows $J_W(l) \le c_W(l)$ and that a larger exponent still works. Its alias [`Top.inclusion_w_seven_real_holds`](/entry/top-inclusion-w-seven-real-holds/) gives it to [`lIncl_of_models`](/entry/l-incl-of-models/).

## Statement

Use $P$, $W$, $X$, `Incl l J` and $c_W(l) = \sum_\tau c_\tau(l)$ from [the entry for `lIncl_of_models`](/entry/l-incl-of-models/). For $\tau \in T_2$, $c_\tau(l) = \min(e_\tau(l), \lfloor c^{\mathrm{co}}_\tau(l) \rfloor)$, where $c^{\mathrm{co}}_\tau$ is the real number `cCoarse`. The short bound $J_W(l)$ is the same sum with `cCoarse` replaced by `cShort6`. The two differ by one term:

$$c^{\mathrm{co}}_\tau(l) = c^{\mathrm{sh}}_\tau(l) + 6(q_\tau + 2j_\tau), \qquad c^{\mathrm{sh}}_\tau(l) = (q_\tau + 2j_\tau)\frac{h + N'}{l - 1} + \cdots.$$

**Theorem** (`HidaLatticeInclusionAtCoarseWeightBound`). Suppose $P$ satisfies `Hyp` and `Large`, $W$ satisfies `Ok P`, $l$ is a prime that is not a unit in $O$, $l > l_J(P)$, and `WInputs` holds for $X$ at $l$. Then `Incl l` $c_W(l)$ holds, and $J_{\min}(l) \le c_W(l)$.

## Proof

1. `Down.inclusion_w_real_holds` gives, under the same hypotheses, `Incl l` $J_W(l)$ and $J_{\min}(l) \le J_W(l)$.
2. $c^{\mathrm{sh}}_\tau \le c^{\mathrm{co}}_\tau$, since $6(q_\tau + 2j_\tau) \ge 0$ (`cShort6_le_cCoarse`). Floor and $\min$ are monotone, so $J_W(l) \le c_W(l)$ term by term (`JW_le_coarseWeightBound`).
3. `Incl l J` says that $l^J$ moves each localized form with values in $\bigotimes_\tau \nabla(\lambda_\tau)$ into the forms with values in $\bigotimes_\tau \Delta(\lambda_\tau)$. If $J \le J'$, then $l^{J'} y = l^J (l^{J'-J} y)$, so `Incl l J` implies `Incl l J'` (`Incl_mono`).

## In the Lean code

The theorem is in [CorollaryOfParamsSevenLinkage.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/CorollaryOfParamsSevenLinkage.lean#L39). The three lemmas of steps 2 and 3 are private lemmas of the same file. `cShort6` is in [LatticeInclusionRealSettingAlt.lean](lean:Formalism/PieriBlockIdeals/LatticeInclusionRealSettingAlt.lean#L15) and `cCoarse` in [FactorialValuationSum.lean](lean:Formalism/PieriBlockIdeals/FactorialValuationSum.lean#L127).

Since $c_W(l) \ge J_W(l)$, the conclusion is weaker than that of `Down.inclusion_w_real_holds`. `Incl_mono` repeats the content of the proposition `TopInclMono` in [BlockIdealBound5Derived.lean](lean:Formalism/PieriBlockIdeals/BlockIdealBound5Derived.lean#L331), which this file does not use. The inclusion statement `InclWReal` used here is the one in `Down` ([StatementDown.lean](lean:Formalism/PieriBlockIdeals/StatementDown.lean#L204)), with no `LemmaDGraded` hypothesis: `Down.inclusion_w_real_holds` supplies that lemma itself, as `hG`.
