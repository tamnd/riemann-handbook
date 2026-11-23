---
id: built-bounds-compact-of-head-top
title: The built bounds from the head formula
kind: theorem
decl: Formalism.FourierDecayAlt.P.built_bounds_compact_of_head_top
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.BuiltBoundsCompactOfHeadTop
covers: 1011
status: drafted
drafted_by: writer@claude
---
This theorem proves `BuiltBounds2Cpt` from one hypothesis, the head formula `HeadTop` at the top level. It is an assembly. It gives `HeadTop` and seven proved facts to `built_bounds_compact_of_leaves`. Almost all of the built-bounds chain is below this theorem: its size is 1,011, and the size of [the built bounds at the infinite places, restated](/entry/pb-built-bounds2-cpt/) is 1,014. Its only user is [the built bounds from the top truncation statement](/entry/pb-built-bounds2-cpt-of-mk-top/).

## Statement

`HeadTop` says the following. Fix the data $p$ at one real place, with parameters $k$ and $r$, a coefficient $F$ that satisfies `CptCoef`, a cut word $w$ (`CutWord`) and two local points $h$, $h'$ at level $r$. Let $X$, $\mu$, $L$ and `st` satisfy `P5.IsData` at level $r$, and let `InDDplus2` hold with a constant $C_b$. Let $\Phi$, $\Phi'$ be families of radial vectors, indexed by `Wd.Ix (Fin w.length)`, that are radial forms (`Top.IsRadOf`) of the slices `slv` at $h$ and $h'$. Then for each $x$ in the domain `DomR`,

$$\mathrm{topDens}(\Phi, \Phi')(x) = R_F^{(r+1)}\bigl(w;\ h \cdot (1, \zeta),\ h' \cdot (1, \zeta)\bigr),$$

where $R_F$ is `p.RR F`, $h \cdot (1, \zeta)$ is the list $h$ with the pair $(1, \zeta)$ added at the end, and $\zeta$ is the last coordinate `zetaL` of $x$. So the top density equals a value of the function `RR` one level up. We have not unfolded `topDens`, `RR` or `zetaL`.

`BuiltBounds2Cpt` is stated in [the built bounds at the infinite places, restated](/entry/pb-built-bounds2-cpt/).

**Theorem.** If `HeadTop` holds, then `BuiltBounds2Cpt` holds.

## Proof

The proof takes the premise `ThmPActualCpt` of `BuiltBounds2Cpt` as `hA`. Then it applies `built_bounds_compact_of_leaves`, which needs eight inputs:

1. `radial_head` (`RadHead`): the same head formula at the levels $j < r$, with a weight `levW`.
2. `HeadTop`, the hypothesis.
3. `degree_of_lift_pairing` (`DegLift`): an identity that writes a power of $t^{-1} - t'^{-1}$ times `RR` as a sum with the Lagrange coefficients `lagCo`.
4. `top_local_built_places` (`TopLocB`).
5. `degree_top` (`DegTop`): an identity of the same type for the top vectors `p.V`.
6. `top_ratio` (`TopRatio`): the top ratio `topR` is real and positive, and it bounds `S.P v y`.
7. `germ_parts_compact_support` with `kernel_continuity_built`, `germ_rate_bound` and `hA` (`GermPartsC`).
8. A uniform decay bound. `uniform_decay_of_heads` gives the bound at one place from `radial_head` and `HeadTop`. `uniform_decay_of_place` turns it into the bound for a whole setting.

Inside, `builtBounds2CptOfLeaves` gets the standard pairing decay `PStdC` and the integral bound `IntB`. Then it calls `builtBounds2CptOfParts` with these and other proved facts.

## In the Lean code

The theorem is in [BuiltBoundsCompactOfHeadTop.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompactOfHeadTop.lean#L14). `HeadTop` and `RadHead` are in [RealInputsClosedAdmissibleSettings.lean](lean:Formalism/HermitianCurvature/RealInputsClosedAdmissibleSettings.lean#L228). The list of leaves is `BuiltBounds2CptOfLeaves` in [BuiltBoundsCompactOfLeaves.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompactOfLeaves.lean#L41).

The hypothesis is not necessary. `head_top` in [RadialExhaustion.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/RadialExhaustion.lean#L6) proves `HeadTop`.

Two definitions have the name `DecayUnif`. `PBO.DecayUnif` in [WaveDiffForm.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/WaveDiffForm.lean#L18) is a bound at one place, with `ThmPActualCpt` as a premise. `PBASM.DecayUnif` in [BuiltBoundsCompactOfParts.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompactOfParts.lean#L84) is a bound for a whole leading-form setting. Step 8 converts the first into the second.
