---
id: hs-claim-s-component-geo
title: The Hilbert-Samuel claim on a component, from the geometric bound
kind: theorem
decl: GlobalTheory.HSShort.hsClaimS_component_geo
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HilbertSamuelComponentShortBasisBound
covers: 745
status: drafted
drafted_by: writer@claude
---
This theorem applies the general bound `GeoBound` to the hermitian data of one component of the moduli space. It then rewrites the numbers of the data into numbers of the component. It has a second name, [hilbertSamuel_component_short_basis_bound](/entry/hilbert-samuel-component-short-basis-bound/). Below this theorem are 745 declarations.

## Statement

The statement is the one in the [second-name entry](/entry/hilbert-samuel-component-short-basis-bound/). In short: if the hermitian data $X$ = `h.data f₁ f₂ th k` of the component $Z$ satisfies `GeoHyp` at $\Lambda_0$, then `HSClaimS` holds with the degree `compDeg`, the height `compHeight`, the dimension of `cuspOn` and the lattice degree `degOn` of $Z$ in place of the abstract numbers $\delta$, $h$, $d$ and $\deg$ of $X$.

## Proof

1. `CompHS.compPresents_data` gives `CompPresents` for $X$: the dimension of $X$ is the dimension of the flag variety, and the component presents the hermitian system of $X$ through a frame of $f_1$.
2. From the presentation and the birationality field of `GeoHyp`, `ImageDegree.imageDeg_eq_del` gives that the degree of the image is the self-intersection number `del` of $X$.
3. In the same way, `T.height_birationalImage_eq_tuple_height` gives `X.IsHeight` of the image height. This uses the field `totallyComplex` of `GeoHyp`.
4. [arithmeticHilbertSamuelBound](/entry/arithmetic-hilbert-samuel-bound/) at $X$, $\Lambda_0$ and this height gives `HSClaimS` with the numbers of $X$.
5. `T.degree_supLattice_component_eq` gives $\deg M_j = $ `degOn` at the weight $P.\mathrm{wt}(j)$, for $j \le T$. Here it is used at $j = T$.
6. `h.data_numbers` matches $T$, $n$, $\Lambda$, $\beta$, $D$ and the other constants of $X$ with those of $P$, $f_1$ and $k$. `h.d_eq` gives $X.d = \dim$ `cuspOn`. A `rw` with these equations turns the claim of step 4 into the goal.

## In the Lean code

The theorem is at [HilbertSamuelComponentShortBasisBound.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HilbertSamuelComponentShortBasisBound.lean#L26), with the proof at lines 27 to 37.

- The proof is a specialization and a change of names. All of the analysis is in [geoBound_of_quoted'](/entry/geo-bound-of-quoted-prime/) and below.
- `GeoHyp` is passed on unchanged to step 4. Only two of its fields, `bir` and `totallyComplex`, are used here.
- The rewrite `← hd` replaces `del` by `imageDeg`, and the result must match `compDeg`. We have not unfolded `compDeg`, `compHeight`, `CompPresents` or `data_numbers`, so we do not show why these agree.
- The argument $J$ of `HSClaimS` is $\log\Lambda_0$, and the argument $j_0$ is $1$.
