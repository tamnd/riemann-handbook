---
id: geometric-realization-of-weight-one
title: The Galois row from geometry, given the Lefschetz formula
kind: theorem
decl: UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.GeometricFlagBases.GeometricRealizationOfWeightOne
covers: 41363
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem makes the Galois representations of the [Galois row](/step/geo-one-def/) from the cohomology of a tower of Shimura varieties. It has one hypothesis: a holomorphic Lefschetz fixed point formula for finite étale correspondences. The step [GeoOne holds](/step/geo-one-holds/) supplies that formula and gets the row with no hypothesis. Below this theorem are 41,363 declarations of the proof.

## Statement

Let $\mathrm{HLF}$ be the following statement. Let $Z$ be a smooth projective variety over $\mathbb{C}$ of dimension $d$. Let $c_1, c_2 \colon Y \to Z$ be two finite étale maps from a variety $Y$. Let $F$ be the set of points $y$ of $Y$ with $c_1(y) = c_2(y)$, and suppose that at each $y \in F$ the map on tangent spaces is given by a matrix $A_y$ with $\det(1 - A_y) \neq 0$. Then for each $a$ the groups $H^b(Z, \Omega^a)$ have finite dimension, and

$$\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^a)\bigr) = \sum_{y \in F} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.$$

This is the holomorphic Lefschetz formula of Atiyah and Bott (Ann. of Math. 88, 1968), in the form for correspondences.

**Theorem.** If $\mathrm{HLF}$ holds, then the Galois row $\mathrm{GeoOne}$ holds.

$\mathrm{GeoOne}$ is stated in full in the [step that defines it](/step/geo-one-def/). In short: let $E$ be a CM field, $\ell$ a prime with an isomorphism $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$, $a$ an odd weight, and $U$ a space of automorphic forms of weight $a$ that meets the conditions at the places $w_0$ and $v'$ above $\ell$. Call a representation $\rho \colon G_E \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$ *attached to* $U$ if it is continuous and semisimple, if at almost all good places $w$ the Frobenius eigenvalues of $\rho$ are the Satake parameters of $U$ at $w$ (normalized by $a$), and if its Hodge-Tate weights satisfy a richness condition. Then:

1. there is a $\rho$ attached to $U$;
2. for each good place $w$ not above $\ell$ where $U$ has Satake parameters, there is such a $\rho$ that matches them at $w$ itself;
3. for each place $w$ above $\ell$ that meets the conditions, there is such a $\rho$ that is crystalline at $w$, with the Hodge-Tate weights $\tfrac{a-1}{2} - z$ for $z$ in the infinitesimal character of the weight of $U$;
4. for the same $w$, there is such a $\rho$ that is crystalline at $w$ and for which the characteristic polynomial of a Frobenius on the Weil-Deligne representation of $\rho$ at $w$ divides a power of the characteristic polynomial of the Satake parameters.

## Proof

The proof has three parts and one assembly.

1. **The local steps.** `steps_holds` proves `Steps`, a list of 17 facts about a representation $\rho$ cut out of the cohomology of a tower. The main ones: such a $\rho$ exists and is semisimple (`repEx_holds`); it satisfies the Eichler-Shimura relation at good places (`Mod.esStep_holds`); it is crystalline above $\ell$ (`Seam.crysStep_holds`); its Hodge-Tate weights are the jumps of the Hodge filtration (`jumpStep_holds`); and its crystalline Frobenius is controlled by the Satake parameters (`phiStep`). Four further facts say that each property survives a twist of $\rho$ by a character.
2. **The Kuga-Sato tower.** `kodaira_spencer_of_weight_one` proves `KSAll`, six facts about the tower of $k$-fold fibre powers of the universal abelian scheme over the Shimura varieties (the Lean structure `KS`). Five are proved outright. The sixth, `KSHodge`, says that each Hecke eigensystem of a given weight occurs in the Hodge cohomology of this tower in the expected degrees. It comes from [`ksHodge_of_geo`](/entry/ks-hodge-of-geo/), and this is the one place where $\mathrm{HLF}$ is used.
3. **The plans.** `Pl.planEx_holds` proves `PlanEx`: for each space $U$ as above, there is a plan, that is, a group datum at an auxiliary prime $p$, a level, a family of Hecke eigenvectors with their eigenvalues, an algebraic Hecke character, a weight and a test function, with the right behaviour at $v'$ and at the place $w$ in question.

The assembly is `geoOne_of_parts`. First `packEx_of` turns each plan into a pack, which is the same data with the tower of Shimura varieties built from it. `KSAll` proves the conditions on the tower that the plan only states for the group. Then `geoOne_of` proves each clause of $\mathrm{GeoOne}$ from a pack. It takes the representation $\rho$ of the tower and twists it by the algebraic Hecke character $\chi$ of the pack. The twist lemmas carry the four properties from $\rho$ to $\rho \otimes \chi$, and the twist moves the Satake parameters and Hodge-Tate weights to the normalization of $U$. The rest is bookkeeping.

## In the Lean code

The theorem is in [GeometricRealizationOfWeightOne.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/GeometricRealizationOfWeightOne.lean#L25). The proof is one line:

```
geoOne_of_parts steps_holds (kodaira_spencer_of_weight_one hW) Pl.planEx_holds
```

The lemmas it calls:

- `steps_holds` and `jumpStep_holds`, in the same file.
- `kodaira_spencer_of_weight_one`, in the same file. It uses `hW` only through `ksHodge_of_geo`.
- `Pl.planEx_holds`.
- `geoOne_of_parts`, `packEx_of` and `Plan.pack` in [PackExOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/PackExOf.lean#L127), and `geoOne_of` and `Pack.rep` in [MapInvMul.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/MapInvMul.lean#L89).

In the Lean code, $\mathrm{HLF}$ is `LocalSmoothExtension.HolomorphicLefschetzFormula`. It is stated with Dolbeault cohomology `hodgeH s a b` and the trace of `hodgeTrace h1 a b ∘ₗ hodgePull h2 a b`, and with the tangent condition `IsTan`. It is proved as `weight_one_geometric_realization`. Its name and the name of this theorem are swapped: the name "geometric realization of weight one" goes to the Lefschetz formula, and the theorem that does the geometric realization has the other name. The written proof notes the same swap.

The name `kodaira_spencer_of_weight_one` is also misleading. No Kodaira-Spencer map appears in `KSAll`; the letters KS stand for the fibre powers (Kuga-Sato varieties) in the structure `KS` in [IntegOfMem.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/IntegOfMem.lean#L48).
