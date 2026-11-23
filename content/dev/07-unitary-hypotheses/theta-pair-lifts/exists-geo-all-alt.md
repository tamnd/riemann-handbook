---
id: exists-geo-all-alt
title: A true framed geometric family for each word
kind: theorem
decl: GlobalTheory.GeoExists.exists_geoAll_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.CoreDataOfPoint
covers: 728
status: drafted
drafted_by: writer@claude
---
This theorem builds, for each word $u$, one geometric family that is true, has the identity as top matrix and carries a framed Bessel datum. Its second name [`all_true_family_datum_alt`](/entry/all-true-family-datum-alt/) gives this family to [`famAllQ_of_allTrue_alt`](/entry/fam-all-q-of-all-true-alt/) in step 2 of its proof. The theorem chooses a geometric datum and checks the hypotheses of [`core_data_of_point`](/entry/core-data-of-point/), which does the construction.

## Statement

Assume the published inputs `DiscreteSeriesCover`, `HarishChandraModules` and `StrongApproxSU`, which we have not unfolded. Let $D$ = `I.rec7 l Z` and let $W$ be a real package over $D$ with `AllFamilyConditions W`. Geometric families (`GeometricFamily W u`) are described in [`famAllQ_of_allTrue_alt`](/entry/fam-all-q-of-all-true-alt/). `a.Is` has twelve fields and `a.True` has four: `pinX`, `std`, `emb`, `z0`.

**Theorem.** For each word $u$ there is $a$ with `a.Is`, `a.True`, $i_A = 1$ for the top orthogonal decomposition of $g$ at level $m$, and `Framed a.d.B`.

## Proof

1. `all_true_family_geometry_alt` (from `StrongApproxSU` and `AllFamilyConditions W`) gives a geometric datum $a$ (`XGeo`) and constants $c_0$. They satisfy the pin condition `PinX`, $b_T = 1$, $i_A = 1$, $L_T = \Lambda_X$, the conditions `emb` and `z0`, and the following. The vector $\zeta_0$ spans the line $L_z$ and $\langle \zeta_0, \zeta_0 \rangle = T_u$, where $T_u$ = `(D.mem u).A.T`. For each place there is a self-dual lattice $L_Z$ in $L_z$ with the orthogonality condition `OrthAt`. Each place of $P_g$ or of $Q$ has local data `LocX` with standard frames.
2. The field `top1` of the family conditions gives $j$ with `LeadingReadAt W u j 1`.
3. `base_fields_primes_ok` says that $T_u$ is prime, so $T_u \neq 0$. With the level condition `hW.lev`, `T_notMem_vGs` shows that $T_u$ is not in any place of $P_g$, and `Q_notMem_of_ok` shows that no place of $Q$ is in $P_g$.
4. `core_data_of_point`, with the predicate $R$ = `StdT` on type data, gives a family $A$ with `A.Is`, $A.c_0 = c_0$, the geometric datum of $A$ equal to $a$, `Framed A.d.B` and `StdT` for the type data of $A$. Its hypothesis on type data is `all_true_family_geometry_column_alt`.
5. Steps 1 and 4 give the four fields of `A.True` and $i_A = 1$.

## In the Lean code

The theorem is at [CoreDataOfPoint.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoreDataOfPoint.lean#L133). `GeometricFamily`, `Is` and `True` are in [GeoAll.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GeoAll.lean#L28). The lemmas it calls:

- `all_true_family_geometry_alt`, the only use of `StrongApproxSU`;
- `all_true_family_geometry_column_alt`;
- `base_fields_primes_ok`, `T_notMem_vGs`, `TC.Q_notMem_of_ok`;
- `core_data_of_point`, the only use of `DiscreteSeriesCover` and `HarishChandraModules`.

The orthogonality hypothesis of `core_data_of_point` is asked only at places that do not divide $T_u$; step 1 gives it at all places. A parallel copy for `RealPack`, `exists_geoAll`, is in [AllTrueFamilyDatum.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/AllTrueFamilyDatum.lean#L161).
