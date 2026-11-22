---
id: ks-hodge-of-geo
title: Hecke eigensystems occur in Dolbeault cohomology, given the Lefschetz formula and the fixed-point count
kind: theorem
decl: UpperTheory.Gal.LocalSmoothExtension.ksHodge_of_geo
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.LefschetzSigmaSums.KsHodgeOfGeo
covers: 1902
status: drafted
drafted_by: writer@claude
---
This theorem proves `KSHodge`, the sixth field of `KSAll` in [kodaira_spencer_of_weight_one](/entry/kodaira-spencer-of-weight-one/). It is the only place where the holomorphic Lefschetz formula $\mathrm{HLF}$ of [the Galois row from geometry](/entry/geometric-realization-of-weight-one/) is used. The proof passes its two hypotheses to `ksHodge_of_inputs` and adds two proved group-side identities. The fixed-point count that it needs is [FixK_holds](/entry/fix-k-holds/).

## Statement

Let $p$, $D$, $G$, $L$ satisfy the scope condition `Sc`, and let towers `KS L gb k` be as in [kodaira_spencer_of_weight_one](/entry/kodaira-spencer-of-weight-one/).

**Theorem.** Assume $\mathrm{HLF}$ and `FixK`. Let $\lambda$ be a weight with $\lambda_\tau$ nonincreasing for each embedding $\tau \colon F \to \mathbb{C}$. Then there is $k$ with this property. Let $R \supseteq \mathbb{Q}$ be a field, `gb` a base point over $R$, $T$ a tower `KS L gb k`, $N$ a level, $(g_j)_{j \in J}$ Hecke data at level $N$ with functions $\psi_j$, $\theta \colon J \to \mathbb{C}$, and $f$ a test function such that `Spec` holds: $\theta$ is a system of Hecke eigenvalues of the $\psi_j$ in weight $\lambda$, seen through $f$. Let $\tau \colon R \to \mathbb{C}$ send `gb` to the standard complex point, $\sigma \in \operatorname{Aut}(\mathbb{C})$, and let $m_1, \dots, m_n$ be the exponents that `IsHExp` gives for the weight $\lambda \circ \sigma^{-1}$. Then for each $i$ there are $b$ and a nonzero $x \in H^b(T_N \otimes_\tau \mathbb{C}, \Omega^{m_i})$ such that, for each $j$, the Hecke correspondence of $g_j$ (pull back along one leg, trace along the other) sends $x$ to $\sigma(\theta_j)\, x$.

We have not unfolded `Spec` beyond this reading.

## Proof

`ksHodge_of_inputs hW hF h₁ h₂` takes the third part of `hodgeTrace_of_lefschetz_and_groupSide`, where $h_1$ is `weighted_count_definite_unitary` (it rewrites the weighted fixed-point count `cxTotalM` as a sum over pairs) and $h_2$ is `trace_definite_forms_identity` (a sum over definite forms equals an automorphic trace). That theorem works in three steps:

1. `hodgeTr_of`: from $\mathrm{HLF}$, `FixK`, $h_1$, $h_2$ and `KSProj_holds` (the levels are projective and smooth), the alternating trace over $b$ of a Hecke operator composed with an operator `cutD c` on $H^b(\Omega^a)$ equals $\operatorname{dTrace} \cdot \sum_i y^{m_i}$ (`HodgeTr`);
2. `hodgeEig_of`: this trace formula gives a nonzero eigenvector in some $H^{m_i, b}$ over $\mathbb{C}$ (`HodgeEig`);
3. `kSHodge_of`: base change of towers along $\tau$ (`KSBc_holds`) and four other facts move the result to any $R$.

## In the Lean code

The theorem is in [KsHodgeOfGeo.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/KsHodgeOfGeo.lean#L7). The three steps are in [HodgeTraceOfLefschetzAndGroupSide.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/HodgeTraceOfLefschetzAndGroupSide.lean#L44). `FixK`, `HodgeTr` and `HodgeEig` are in [HodgeTraceFromLefschetzAndGroupSide.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/HodgeTraceFromLefschetzAndGroupSide.lean#L125), and `KSHodge` in [PackExOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PackExOf.lean#L25).
