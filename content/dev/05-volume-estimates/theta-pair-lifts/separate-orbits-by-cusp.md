---
id: separate-orbits-by-cusp
title: Cusp forms separate the level orbit of a general point
kind: theorem
decl: GlobalTheory.OrbitSep.separate_orbits_by_cusp
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.ExistsCuspRegularLevelDeterminant
covers: 741
status: drafted
drafted_by: writer@claude
---
This theorem is the geometric step of [the regular level determinant](/entry/exists-cusp-regular-level-determinant/). On each connected component, it finds a complex point $y$ whose orbit under a group of level automorphisms is separated by cusp forms of large Hodge weight. Below this theorem are 741 declarations.

## Statement

We use the notation of [the parent entry](/entry/exists-cusp-regular-level-determinant/). Let $Y$ be a good cover at level $j$ with signature $(p, q)$, $p, q \ge 1$, and $[E:\mathbb{Q}]/2 > 2$. Let $d$ be the dimension. Let $S$ be a group of level automorphisms. Let $I$ be an ideal of $\mathcal{O}_E$ that contains the level, such that $g = N(I)$ is a prime, $g \notin I^2$, $p + q + 1 < g$ (`NeatPrime`), and each $\gamma \in S$ is unipotent modulo $I$ (`UnipAt`: $(\gamma - 1)^m \Lambda \subseteq I \Lambda$ for some $m$). Let $s \ge p + q + \binom{d+1}{2} + 1$ and let $Z$ be a connected component.

**Theorem.** Under the six published inputs of the parent, there is a complex framed point $y$ on $Z$ with this property. Let $S_Z$ be the set of $h \in S$ with $h^{-1} y$ on $Z$. If $a \colon S_Z \to \mathbb{C}$ and

$$\sum_{h \in S_Z} a_h\, u(h^{-1} y) = 0$$

for every cusp form $u$ of weight $s \lambda_H$ supported on $Z$, then $a = 0$.

## Proof

1. **The compactification.** A toroidal flag space exists, and its part $\bar Z$ over $Z$ is integral, smooth, projective and geometrically connected. The point $y$ is a complex point over the generic point of $\bar Z$.
2. **The quotient.** The stabiliser $\Gamma$ of the component acts by level automorphisms. `equivariant_normal_projective_compactification` gives a normal projective $\Gamma$-model $X'$ with a finite quotient $q \colon X' \to W$. The Hodge bundle $\delta$ descends to $W$, since it is $\Gamma$-linearised up to rational equivalence. The points $h^{-1} y$ lie in one fibre of $q$.
3. **The bundles.** Write $s = m + t$ with $m = \binom{d+1}{2} + 1$. `exists_toroidalCanonicalBundle_weight_line` gives a line bundle $\kappa$ whose pullback is the automorphic bundle of the weight `kapBase`, and a section $\theta$ of $\kappa \otimes K^{-1}$ that is nonzero exactly on the interior. Put $N' = t\delta - \kappa$ and $B = m\delta + N'$. Then $N'$ is nef (`base_weight_line_bundle_is_nef`), $\delta$ is nef and big (`hodgeLineBundle_bigness_on_shimuraVariety`), and $K \otimes B$ has weight $s \lambda_H$.
4. **Separation.** For $\delta$ nef and big, $N'$ nef and $m > \binom{d+1}{2}$, sections of $K \otimes B$ separate distinct points of one fibre of $q$ when one is generic (`sections_separate_quotient_generic_fibre_descends`). The points $h^{-1} y$ are distinct, since a level automorphism that is unipotent modulo $I$ and fixes a complex point is $1$.
5. **Back to cusp forms.** `exists_cuspRule_of_boundaryVanishing_componentSection` turns each section into a cusp form of weight $s\lambda_H$ on $Z$, with the same values up to units $\lambda_h$. It applies to $\theta g$ for $g$ a section of $K \otimes B$, since $\theta g$ vanishes on the boundary. As $\lambda_h$ and $\theta(h^{-1}y)$ are nonzero, the relation passes to the sections, so $a = 0$.

## In the Lean code

The theorem is at [ExistsCuspRegularLevelDeterminant.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ExistsCuspRegularLevelDeterminant.lean#L27). `NeatPrime` and `UnipAt` are in [GapGeSubKapBase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GapGeSubKapBase.lean#L87).

- Step 4 uses three fields of the published bundle: `q15` (`NadelVanishingAndNonKltDivisor`), `q16` (`Principalisation`) and `Quoted.nef` (`NefNumerics`). We have not opened `QuotSep.sections_separate_quotient_fibre`, which it restates, or the lemmas of steps 1 to 3.
- The statement quantifies over a `Fintype` instance on $S_Z$ (line 36).
- The bound $m > \binom{d+1}{2}$ looks like the Angehrn-Siu bound. The Lean code names no source, and we do not claim that step 4 is that theorem.
