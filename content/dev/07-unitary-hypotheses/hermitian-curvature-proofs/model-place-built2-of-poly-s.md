---
id: model-place-built2-of-poly-s
title: Model places from the radial polynomial relation
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_polyS
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutJASSnRepDone
covers: 1283
status: drafted
drafted_by: writer@claude
---
This theorem is a relay. It proves `ModelPlaceBuilt2` from two hypotheses, `JfSmoothDS` and `PolyRadialS`. Its only user is [model places from the smoothness of the transfer](/entry/model-place-built2-of-jf/), which supplies `PolyRadialS` with `polynomial_radial_holds`. The statement `ModelPlaceBuilt2` is given in words in [each place of a built setting is a model place](/entry/model-place-built-holds/), and `JfSmoothDS` in the entry for `modelPlaceBuilt2_of_jf`.

## Statement

Let $P$ be a parameter record: integers $k$ and $r$, reals $T, T'$ and two sequences $u, u'$. The statement assumes $k \ge 2$. Put $T_P = T T'$ and let $\mathrm{Ann}_P = \{\zeta \in \mathbb{C} : |\zeta|^2 > T_P\}$. Let $B$ be the data at one real place, with representations $\sigma$, $\sigma'$ on the inner product spaces $W_p$, $W_q$. For $\zeta \in \mathrm{Ann}_P$, the fibre $\mathrm{Fib}(\zeta)$ is the set of linear maps $X \colon W_q \to W_p$ with $\sigma(h_1) X \sigma'(h_2) = X$ for each pair $(h_1, h_2)$ in a stabilizer that depends on $\zeta$. Let $\nu_0(\zeta)$ be the vector built from $\zeta$ and the base points of $B$, normalized for a Hermitian form.

`PolyRadialS` says the following. Fix the data above, operators and level data that satisfy `ActHyp`, an index $1 \le l \le k - 1$, an operator family $S_\zeta$ that represents the $l$-th operator of the level data pointwise (`IsSSPt`), a family of projections $\mathrm{Pr}_\rho(a)$ that meets `PRhoSpec` (smooth, equivariant, self-adjoint, orthogonal, and cut out by a capacity eigenvalue condition), and frames $B_w$, $B_w'$. Let $\pi, \rho$ be two types with $\rho = \pi + e_l$ (`M.Up`). Then there are $n \in \mathbb{N}$ and $q \in \mathbb{C}[X]$ such that, for each $\zeta \in \mathrm{Ann}_P$ and each $X \in \mathrm{Fib}(\zeta)$ with $\mathrm{Pr}_\pi(\nu_0(\zeta)) X = X$,

$$(|\zeta|^2 - T_P)^n \, \mathrm{Pr}_\rho(\nu_0) \, S_\zeta X = q\bigl(\sqrt{|\zeta|^2 - T_P}\bigr) \, \mathrm{Pr}_\rho(\nu_0) \, \theta_\zeta X,$$

where $\theta_\zeta$ is the explicit operator `tht`, a double sum of sandwiched elementary operators over the frames.

**Theorem.** If `JfSmoothDS` and `PolyRadialS` hold, then `ModelPlaceBuilt2` holds.

## Proof

1. `ssnRep_of_polyS` proves `SSnRep` from `PolyRadialS`. `SSnRep` says: there is $K \ge 0$ such that for $C_c \ge K$, at each place of a built setting and for each frame $e$ that satisfies `IsFrame`, `IsGauge` and `IsGaugeQQ`, and each $1 \le l \le k - 1$, a fibre map exists (`IsFibreMap`). The proof calls `ssnRep_of_open2` with three proved facts: `rho_projection_existence` (projections as in `PRhoSpec` exist), `modular_constancy_holds` (`ModConst`: in the norm of `B.hsVec`, the squared norms of $\mathrm{Pr}_\rho S_\zeta X$ and $\mathrm{Pr}_\rho \theta_\zeta X$ are $c_1 \|X\|^2$ and $c_2 \|X\|^2$) and `line_nonvanishing_holds` (`LineNonzero`: a nonzero $X$ with $\mathrm{Pr}_\pi X = X$ exists in each fibre). Inside, `thConst_of_open` uses `theta_constancy_assembly_scalar` and `polynomial_finish_holds` to get `ThConst`: the ratio of the two sides is a constant $\theta(\pi)$, independent of $\zeta$. We have not read the proof of `theta_constancy_assembly_scalar`.
2. `modelPlaceBuilt2_of_SSnRep` turns `JfSmoothDS` and `SSnRep` into `ModelPlaceBuilt2`. It adds the gauge input `rotation_K_invariance_holds` and goes through `modelPlaceBuilt2_of_rotK`, `modelPlaceBuilt2_of_ssnRep` and `modelPlaceBuilt2_of_bdd`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [CutJASSnRepDone.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJASSnRepDone.lean#L27). The same file proves `modular_constancy_holds` (line 12) and `ssnRep_of_polyS` (line 20). `PolyRadialS` is in [CutJASSnRepThConstS.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJASSnRepThConstS.lean#L10), `SSnRep` in [CutJABddSSn.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJABddSSn.lean#L249) and `modelPlaceBuilt2_of_SSnRep` in [GaugeConstructionHolds.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/GaugeConstructionHolds.lean#L12).

`ssnRep_of_open2` accepts `PolyRadial ∨ PolyRadialS`. `PolyRadial` ([CutJASSnRepThConst.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJASSnRepThConst.lean#L10)) evaluates $q$ at $|\zeta|^2$ in place of $\sqrt{|\zeta|^2 - T_P}$. This theorem uses only the second branch. The theorem `polynomial_radial_holds` proves `PolyRadialS`, not `PolyRadial`, so its name fits the other branch.
