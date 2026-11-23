---
id: hodge-trace-of-lefschetz-and-group-side
title: A trace formula on Dolbeault cohomology, from the Lefschetz formula and the group side
kind: theorem
decl: UpperTheory.Gal.LocalSmoothExtension.hodgeTrace_of_lefschetz_and_groupSide
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.LefschetzSigmaSums.HodgeTraceOfLefschetzAndGroupSide
covers: 334
status: drafted
drafted_by: writer@claude
---
This theorem joins the geometric side and the group side of a trace formula on the towers of fibre powers. From five hypotheses it proves a trace formula on Dolbeault cohomology (`HodgeTr`), then the existence of eigenvectors (`HodgeEig`), then `KSHodge`. Its only use is in [ksHodge_of_inputs](/entry/ks-hodge-of-inputs/), which keeps `KSHodge`. The three steps are listed in [ksHodge_of_geo](/entry/ks-hodge-of-geo/); this entry says how the first step joins the two sides.

## Statement

Let the towers `KS L gb k`, the levels $N$ and the Hecke operators $T_f$ on $H^b(T_N, \Omega^a)$ be as in [ksHodge_of_geo](/entry/ks-hodge-of-geo/). For a smooth projective $s \colon Z \to \operatorname{Spec}\mathbb{C}$ of dimension $d$ and operators $u_{a,b}$ on $H^b(Z, \Omega^a)$, put

$$\operatorname{altTr}(u)(y) = \sum_{a=0}^{d} (-y)^a \sum_{b=0}^{d} (-1)^b \operatorname{tr}(u_{a,b}).$$

**Theorem.** Assume $\mathrm{HLF}$, `KSProj` (each level is projective and smooth), `FixK`, and the two group-side identities [weighted_count_definite_unitary](/entry/weighted-count-definite-unitary/) and [trace_definite_forms_identity](/entry/cnt-trace-definite-forms-identity/). Then:

1. `HodgeTr`: let $h_1, \dots, h_n$ be the exponents that `IsHExp` gives for a weight $\lambda$. There are $k_0$ and, for each $k \geq k_0$, a finite combination $c = \sum_\alpha c_\alpha [\alpha]$ of diagonal endomorphisms $\alpha$ of the fibre power, such that for each level $N$, each representation $\xi$ of weight $\lambda$, each good Hecke function $f$ and each $y \in \mathbb{C}$,
$$\operatorname{altTr}\Bigl(T_f \circ \sum_\alpha c_\alpha\, \alpha^*\Bigr)(y) = \operatorname{dTrace}(\xi, f) \cdot \sum_{i=1}^{n} y^{h_i};$$
2. `HodgeEig`: each eigensystem of weight $\lambda$ has a nonzero eigenvector in some $H^b(T_N, \Omega^{h_i})$ over $\mathbb{C}$;
3. `KSHodge`, as in [ksHodge_of_geo](/entry/ks-hodge-of-geo/).

Here $\operatorname{dTrace}(\xi, f)$ is the trace of the Hecke operator of $f$ on automorphic forms of weight $\xi$ on the definite groups, summed over their classes (`dTrace`).

## Proof

Step 1 is `hodgeTr_of`. Write $f = \sum_i a_i\, \mathrm{ind}(g_i^{-1})$ as a combination of the indicator functions `ind` of Hecke elements (`FnDecomp`), so that $T_f = \sum_i a_i T_i$ with $T_i$ the operator of $\mathrm{ind}(g_i^{-1})$ (`HopWord`). Expand the alternating trace in $i$ and $\alpha$ (`AltLin`). For each $i$ and $\alpha$, `GeoStep` says that $\operatorname{altTr}(T_i \circ \alpha^*)(y)$ is the weighted fixed-point count $\mathrm{cxTotalM}$ with the weight `cW α y`. `geoStep_of` proves this from $\mathrm{HLF}$, `KSProj` and `FixK`: `FixK` gives the fixed points and their tangent matrices, and $\mathrm{HLF}$ turns their Lefschetz terms into traces. `CxLin` collects the counts back into one count with the combined weight. `GroupTop`, proved by `GroupTop_of` from the two group-side identities, says that this count equals $\operatorname{dTrace}(\xi, f) \sum_i y^{h_i}$.

Step 2 is `hodgeEig_of`. It uses `HodgeTr`, `KSProj`, and `HodgeFin` (finite dimension of $H^b(\Omega^a)$, from $\mathrm{HLF}$ by `hodgeFin_of`). Step 3 is `kSHodge_of`, which moves the result from $\mathbb{C}$ to any base field. We have not unfolded the proofs of steps 2 and 3.

## In the Lean code

The theorem is in [HodgeTraceOfLefschetzAndGroupSide.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/HodgeTraceOfLefschetzAndGroupSide.lean#L44). The statement `HodgeTraceFromLefschetzAndGroupSide`, with `HodgeTr`, `HodgeEig` and `GeoStep`, is in [HodgeTraceFromLefschetzAndGroupSide.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/HodgeTraceFromLefschetzAndGroupSide.lean#L167). The lemmas: `hodgeTr_of` in [PHodgeTr.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/PHodgeTr.lean#L14), `geoStep_of` in [PGeoStep.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/PGeoStep.lean#L16), `groupTop_of` in [PGroupTop.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/PGroupTop.lean#L12), `hodgeEig_of` in `PHodgeEig.lean` and `kSHodge_of` in `PKSHodge.lean`.

Points to note:

- `geoStep_of` also takes `G3.HodgeTr` (supplied by `Tw.hodgeTr`). This is another declaration with the same short name as `HodgeTr` above. We have not unfolded it.
- `HodgeTr` and `HodgeEig` are proved but not used outside this theorem.
