---
id: top-inclusion-w-seven-real-holds
title: The lattice inclusion at the coarse weight bound (top form)
kind: theorem
decl: Formalism.CohomologicalDescent.Top.inclusion_w_seven_real_holds
module: Formalism.PieriBlockIdeals.PieriColumnMinors.CorollaryOfParamsSevenLinkageAlt
covers: 890
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It states `Top.HidaLatticeInclusionAtCoarseWeightBound` and proves it by [`Down7.inclusion_w_seven_real_holds`](/entry/down7-inclusion-w-seven-real-holds/), which has the content. Its one user is [`lIncl_of_models`](/entry/l-incl-of-models/), which applies it to each Hida setting $X_i$ at the residue characteristic $p$.

## Statement

Use the parameters $P$, the weight datum $W$ with index set $I$, the Hida setting $X$, the inclusion `Incl l J` and the coarse weight bound $c_W(l)$ from [the entry for `lIncl_of_models`](/entry/l-incl-of-models/).

**Theorem.** Suppose $P$ satisfies `Hyp` and `Large`, $W$ satisfies `Ok P`, $l$ is a prime that is not a unit in the ring $O$ of $X$, $l > l_J(P)$, and the weight inputs `WInputs` hold for $X$ at $l$. Then $X$ has an inclusion of exponent $c_W(l)$ at $l$, and the least such exponent $J_{\min}(l)$ is at most $c_W(l)$.

## Proof

The statement in the namespace `Top` is the same proposition as the one in `Down7`, and the proof is that theorem.

## In the Lean code

The theorem is in [CorollaryOfParamsSevenLinkageAlt.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/CorollaryOfParamsSevenLinkageAlt.lean#L9). The proof is the term `Formalism.CohomologicalDescent.Down7.inclusion_w_seven_real_holds`. The file checks by `rfl` that `Top.HidaLatticeInclusionAtCoarseWeightBound` and `Down7.HidaLatticeInclusionAtCoarseWeightBound` are equal, and the same for `RecIncl7`. It also defines `prime_count_bound_rs`, a second name for `prime_count_bound`.

There is a third definition with the same name, in [LatticeInclusionRealSettingAlt.lean](lean:Formalism/PieriBlockIdeals/LatticeInclusionRealSettingAlt.lean#L455). It has the extra hypothesis `LemmaDGraded`, and it is proved by another theorem `inclusion_w_seven_real_holds`, in the namespace `ShortWeightBounds` ([WeightBounds.lean](lean:Formalism/PieriBlockIdeals/PieriColumnMinors/WeightBounds.lean#L674)). The proof here does not use that one.
