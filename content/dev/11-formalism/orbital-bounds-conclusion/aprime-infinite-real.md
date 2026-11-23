---
id: aprime-infinite-real
title: The archimedean orbit constant, second name
kind: theorem
decl: PI.AprimeInfAsm.aprime_infinite_real
module: Formalism.PeriodIntegrals.OrbitalBoundsConclusion.AprimeInf
covers: 987
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`aprimeInf_of_hinfCompact`](/entry/aprime-inf-of-hinf-compact/). It has the same hypotheses and the same conclusion, and its proof only calls that theorem. Its only caller is [`AprimeInf_holds`](/entry/aprime-inf-holds/), which supplies both hypotheses.

## Statement

**Theorem.** Assume `HinfCompact` (for every setting and every word $u$, the stabilizer at infinity of the frame of $u$ is compact) and `GaugeVolUD` (the gauge density exists for each $U(k)$, and $U(k)$ has gauge volume $V_k$). Then `AprimeInf` holds: the constant $a'$ of the disintegration at infinity is
$$a' = \frac{g_U\, V_k^{\,d}\, T_{u'}^{-kd}}{\mu_H(u')(\mathrm{all})}.$$
The notation is that of [`AprimeInf_holds`](/entry/aprime-inf-holds/).

## Proof

`aprime_infinite_real hC hV` is `aprimeInf_of_hinfCompact hC hV`. That theorem applies [`aprimeInf_of_grp`](/entry/aprime-inf-of-grp/) to `hC`, to `grpStd_full expProdU_holds hV`, to `nuBridge` and to `placeJacAll_holds`.

## In the Lean code

Both theorems are in [AprimeInf.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/AprimeInf.lean#L13), at lines 10 and 13. The file has no other declarations. The second name adds no content. `AprimeInf_holds` calls it by this name, not the first.
