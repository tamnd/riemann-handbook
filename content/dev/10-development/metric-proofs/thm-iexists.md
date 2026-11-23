---
id: thm-iexists
title: The arithmetic intersection numbers exist, from Poincaré-Lelong and resolution
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Pub.thmIExists
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.IntersectionExistsOfPoincareLelong
covers: 323
status: drafted
drafted_by: writer@claude
---
This theorem builds heights, or arithmetic intersection numbers, for all arithmetic varieties in products of projective spaces over $\mathbb{Z}$. It assumes an arithmetic Poincaré-Lelong formula and complex-analytic log resolutions. Its only user is its second name, [the arithmetic intersection numbers exist (second name)](/entry/intersection-exists-of-poincare-lelong/).

## Statement

We use the words of [the projection formula, in two forms](/entry/gen-deg-and-pf-coord/). A family $I$ (`AllFam`) gives a real number $I(X; L_1, \dots, L_n)$ for each choice of blocks, each ideal $X$ and metrized line bundles $L_j$. It is a *family of heights* (`IsFamily`) if three axioms hold for arithmetic varieties $X$ of dimension $n$ and smooth $L_j$:

1. symmetry: $I(X; L_{\sigma(1)}, \dots, L_{\sigma(n)}) = I(X; L_1, \dots, L_n)$ for each permutation $\sigma$;
2. additivity: $I(X; L, A \otimes B) = I(X; L, A) + I(X; L, B)$;
3. recursion (`recR`): if $A$ has multidegree $a \in \mathbb{N}^K$ and $s \notin X$ is a form of degree $a$, then
$$I(X; L, A) = \sum_{W} m_W c_W - \int_{X(\mathbb{C})} \log \frac{|s|}{h_A}\, \omega_{L_1} \cdots \omega_{L_{n-1}}.$$
The sum runs over the relevant minimal primes $W$ of $X + (s)$, with $m_W$ the length at $W$. If $W$ is horizontal, $c_W = I(W; L)$. If not, $c_W$ is the geometric degree of $W$ for the multidegrees of $L$ (`geoNum`) times $\log p$, where $p$ is the characteristic of $W$. The integral is `arInt`, built from `ptsIntegral` against the potentials $\log h_{L_j}$. We have not unfolded its density `maDensity`.

This recursion has the shape of the recursive formula for heights of Bost, Gillet and Soulé (J. Amer. Math. Soc. 7, 1994).

**Theorem.** If `PoincareLelong` and `ResExistsStatement` hold, then a family of heights exists.

## Proof

The family is `famI`, defined by recursion on $n$, with value $0$ for $n = 0$. Let $m = \sum_k |a_k|$ and let $S_m$ be the Fubini-Study metric to the power $m$ on each block (`segreLine m`). Then $A = (A \otimes S_m) - S_m$, and both terms have nonnegative degree. So `famI` applies `recR` to $A \otimes S_m$ and to $S_m$, with forms chosen by `secOf`, and subtracts.

The main step is that the value does not depend on the chosen forms. The proof builds this in order:

- `PtsIntegrable.of_resExists` and `PtsAbsMeasurable.proof` use the resolution to make the integrals finite.
- `StokesStatement`: for two metrics $B, B'$ of degree $0$, the integral of $\log h_B$ against $\log h_{B'}$ is symmetric.
- `DeLeSemiPos`: a defect `De` is at most $0$ for semipositive $L_j$. This is the only use of `PoincareLelong`.
- `SectionSpaceSymmetry`: for two forms $s, s'$ with no common horizontal component, the cross terms of the recursion agree. It has the form of the symmetry of the star product of two Green currents.
- `Swap`: if $s$ and $s'$ have no common component, the two orders of the recursion agree.
- `WellDefined`: `recR` takes the same value for any two forms of the same degree.

`ThmIExists.proof` then gets axioms 2 and 3 from `WellDefined`, `RMul` (the recursion is additive under the product $st$) and `Inter_R1Indep` (independence of the form in dimension $1$). Axiom 1 comes from `ThmISymm.proof`, by `Swap` and the symmetry of the intersection numbers over $\mathbb{Z}/p$.

## In the Lean code

The theorem is in [IntersectionExistsOfPoincareLelong.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/IntersectionExistsOfPoincareLelong.lean#L142). `famI` is in [ThmIExistsFamily.lean](lean:GroundTheory/HeightsAndTheta/Heights/Intersections/ThmIExistsFamily.lean#L133), the axioms in [IsIntersectionFamily.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/IsIntersectionFamily.lean#L188), and `ThmIExists.proof` in [PThmIExists.lean](lean:GroundTheory/HeightsAndTheta/Heights/Intersections/PThmIExists.lean#L10). We have not unfolded the proofs of the lemmas in the list.

The value $0$ for $n = 0$ does no harm: no arithmetic variety has dimension $0$, so the axioms never test it.
