---
id: gen-deg-of-res-exists
title: The projection formula for heights under a generically finite projection
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Pub.genDeg_of_resExists
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.DegreeAndCoordinatesOfResolution
covers: 320
status: drafted
drafted_by: writer@claude
---
This theorem proves the projection formula `GenDegStatement` for heights, from the existence of complex-analytic log resolutions. [The projection formula, in two forms](/entry/gen-deg-and-pf-coord/) uses it for both of its halves. This theorem holds almost all of that entry's 327 declarations.

## Statement

**Hypothesis** (`ResExistsStatement`). Let $X$ be an arithmetic variety of dimension $e + 1$ in a product of projective spaces, given by an ideal $P$. Let $J$ be a multihomogeneous ideal with $J \not\subseteq P$, so that $Z = V(J) \cap X$ is a proper closed subset. Then there is a multihomogeneous ideal $J' \subseteq J$ with $J' \not\subseteq P$, and a resolution `AnLogRes P J' e`, that is:

- a compact Hausdorff space $\tilde X$ with a finite holomorphic atlas of dimension $e$;
- local holomorphic lifts from $\tilde X$ to the cone over $X(\mathbb{C})$, which agree up to scalars on overlaps;
- the induced map $\tilde X \to X(\mathbb{C})$ is onto and one to one outside $V(J')$, and it is an immersion there;
- each form that does not vanish on $X$, but vanishes on $X(\mathbb{C})$ only inside $V(J')$, pulls back to a divisor with simple normal crossings;
- the inverse image of $V(J')$ has measure zero in each chart.

This has the shape of an embedded resolution of singularities in the sense of Hironaka (Ann. of Math. 79, 1964), read on complex points.

**Conclusion** (`GenDegStatement`). Let $\pi \colon X' \to X$ forget some blocks of coordinates, with $\dim X' = \dim X = d$. Then for every family $I$ of heights with the axioms `IsFamily`, every field intersection family $J$ and smooth metrized line bundles $L_1, \dots, L_d$ on $X$,
$$I(X'; \pi^* L_1, \dots, \pi^* L_d) = \deg(X'_\eta) \cdot I(X; L_1, \dots, L_d),$$
where $\deg(X'_\eta)$ is the value of $J$ on the generic fibre of $\pi$. The [parent entry](/entry/gen-deg-and-pf-coord/) defines these words.

## Proof

The axioms `IsFamily` give $I$ by a recursion: the height on $X$ is a sum over the components of a divisor $\operatorname{div}(s)$ of a section, minus an integral of $\log \|s\|$ over $X(\mathbb{C})$. The proof shows that each term scales by $\deg(X'_\eta)$ under $\pi$. It is an induction on $d$ in `PushforwardArithIntersection.proof`. The base case is empty, because no arithmetic variety has dimension $0$ (`arithVarZero`). `GenDeg.of_pts` supplies the three inputs of the inductive step.

1. **The recursion for rational sections** (`RatR.proof`). It needs only integrability, which `PtsIntegrable.of_resExists` gets from the resolution.
2. **The archimedean term** (`IntersectionWithSection.proof`, then `ArithmeticIntersectionIntegral.proof`). The integral of $\log \|\pi^* s\|$ on $X'$ against the pulled-back forms is $\deg(X'_\eta)$ times the integral on $X$, first for sections and then for rational sections. The inputs are the resolution, integrability, `pullbackPushforward_holds`, `pullbackDensity_holds` and `PullbackDegreeCount`.
3. **The cycle term** (`ArithmeticIntersectionCycle.of_remaining`). Given the formula in dimension $d - 1$, the finite sum over the components of $\operatorname{div}(\pi^* s)$ is $\deg(X'_\eta)$ times the sum for $\operatorname{div}(s)$. The inputs are `FibreIncomp.full` (the components above one component of $\operatorname{div}(s)$ are incomparable), `projDeg_all`, two lemmas on semilocal rings, and `fibreDim`.

## In the Lean code

The theorem is in [DegreeAndCoordinatesOfResolution.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/DegreeAndCoordinatesOfResolution.lean#L25). `ResExistsStatement` and `AnLogRes` are in [InterRes.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/InterRes.lean#L18). `GenDeg.of_pts` is in [GenDeg.lean](lean:GroundTheory/HeightsAndTheta/Heights/OrbitLimits/GenDeg.lean#L17).

The hypothesis is used in two places only: `PtsIntegrable.of_resExists` and `IntersectionWithSection.proof`. The cycle term does not use it. We have not unfolded the proofs of the lemmas in steps 1 to 3.
