---
id: closed-serv-f-of-serv-t-of-d-gam-size
title: The served bound from a served selection
kind: theorem
decl: Formalism.L2.G.ServT.closed_servF_of_servT_of_dGamSize
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.GServT
covers: 1751
status: drafted
drafted_by: writer@claude
---
This theorem is a wrapper. It restates its hypothesis in the form that [`sum_over_primes_service`](/entry/sum-over-primes-service/) asks for, and applies that theorem. The real content is in `sum_over_primes_service`, which dominates 1,747 of the 1,751 declarations below this one. The user is [`closed_family_admissible_twist_link_alt`](/entry/closed-family-admissible-twist-link-alt/), which needs the bound `ServF` as the field `serv` of the structure `Adm2InU`.

## Statement

Let $\mathcal{C}$ be a family class with a twist selection `sel`. Assume that `DGamSize` is [closed](/step/closed-def/) on $\mathcal{C}$, and that `SelectionServed 𝒞 sel` holds. Then `ServF` is closed on $\mathcal{C}$.

`SelectionServed` has two fields. `twU` is a closed bound on the twisted local systems `SysTw` of each family, eventually in $x$. `pdv` asks, for each family of $\mathcal{C}$, each $x$ above the threshold of the selection and each $i$, that the kernel entry chosen by `sel` satisfies a list of orbit conditions (`UnUnit`, `KmapRat`, `EvenConditionsInert`, `OrbitBoundWithoutOperator`, `JetIntegralityBis`, `Shape` and others).

`ServF` says: there are $C \ge 0$ and $x_0$ such that for all $x \ge x_0$ with $x > x_1$ and all $i$, the statement `Serv` holds for the data of the family at $(x,i)$ with constant $C$. `Serv` is a conjunction of three parts: size conditions at the type primes, the bound `Conclusion1`, and a valuation bound on columns away from the type primes.

## Proof

`sumOverPrimesService_of_servT` turns `SelectionServed 𝒞 sel` into `SumOverPrimesHypotheses 𝒞`. The field `twU` is copied. The field `pdv` of `SumOverPrimesHypotheses` asks only for some kernel entry $E$ with the same orbit conditions; the proof takes the entry chosen by `sel`, with the threshold of the selection as $x_0$. Then `sum_over_primes_service 𝒞 hD` gives `ServF`. The rest is bookkeeping.

## In the Lean code

The theorem is in [GServT.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GServT.lean#L31), with `SelectionServed` at line 13 and `sumOverPrimesService_of_servT` at line 28 of the same file. `sum_over_primes_service` and `SumOverPrimesHypotheses` are in [SumOverPrimesHypotheses.lean](lean:Formalism/SharpRestriction/SmoothDesignExistence/SumOverPrimesHypotheses.lean#L187). `ServF` and `Serv` are in [WeilJacquetShalikaLaw.lean](lean:Formalism/SharpRestriction/GrowthBounds/WeilJacquetShalikaLaw.lean#L252). We have not unfolded the orbit conditions or the three parts of `Serv`. The file is named after Weil, Jacquet and Shalika, but we have not checked that `Serv` states a result of theirs.
