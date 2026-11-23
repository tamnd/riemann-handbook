---
id: core-data-of-point
title: A geometric family on a given geometric datum
kind: theorem
decl: GlobalTheory.GeoExists.core_data_of_point
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.CoreDataOfPoint
covers: 543
status: drafted
drafted_by: writer@claude
---
This theorem extends a geometric datum $a$ to a full geometric family: rational data, measures, level data, type data, local groups and a bottom datum, with all twelve conditions of `Is`. Its only user is [`exists_geoAll_alt`](/entry/exists-geo-all-alt/), which supplies $a$ and the hypotheses in step 4 of its proof. The lattices, base points and frames come from [`local_component_vector_relation_alt`](/entry/local-component-vector-relation-alt/).

## Statement

Let $W$ be a real package over $D$, $u$ a word, and $T_u$ = `(D.mem u).A.T`. A geometric datum $a$ (`XGeo D`) is a chain of spaces $x_j$ on $X_j$ with lattices $L_j$, vacuum functions, a line $L_z$ with a vector $\zeta_0$, orthogonal decompositions at the top level $m$, and an element $b_T$ and a lattice $L_T$ of the top space $X'$. Assume:

- the published inputs `DiscreteSeriesCover` and `HarishChandraModules`, and `PackageHypotheses W`;
- $P_g$ is a set of type places (`IsTypePlaces`); $T_u \neq 0$; $T_u$ lies in no place of $P_g$; no place of $Q$ is in $P_g$;
- a linear map $j$ with `LeadingReadAt W u j 1`;
- each $x_j$ satisfies `Is` for $j \le m$; $b_T = 1$; $L_T = \Lambda_X$; $\zeta_0$ spans $L_z$ and $\langle \zeta_0, \zeta_0 \rangle = T_u$;
- at each place prime to $T_u$, a self-dual lattice of $L_z$ with the orthogonality condition `OrthAt`;
- at each place of $P_g$ or $Q$, local data `LocX` with standard frames;
- a predicate $R$ on local type data, and the condition `hpre`: for all rational data $y$, measures, base points and level data $v$ with $v.N_T = L_T$, twist places the places dividing $T_u$, $v.\tau = y.\tau$ and `y.Tau`, there are type data $o$ with `PreT v o`, $o.\zeta_0 = \zeta_0$ and $R(o)$.

**Theorem.** For each $c_0$ there is a geometric family $A$ with `A.Is`, $A.c_0 = c_0$, geometric datum equal to $a$, `Framed A.d.B`, and $R$ for the type data of $A$.

## Proof

1. `line_vector_bessel_existence_alt` gives rational data $y$ and a Bessel datum $\mathcal B$ on $X_0$: adapted, framed, of norm $-T_u$, with level equal to the Bessel datum of $y$ at $(0, r_S)$.
2. `exists_yMeas_geoMeas_volLast` gives measures $m$; `commOf_is_of_geoMeas_of_coords_is` (the two published inputs) gives the conditions on the common datum.
3. Let $P_T$ be the places dividing $T_u$ (`exists_places`) and $P_G$ the places under $P_g$. They are disjoint.
4. A first level datum $v_0$ with $P_G$, $P_T$, base points 1 and zero test data. `hpre` gives type data $o$.
5. `exists_symData_symRead_at_type_places` gives symmetric data at $P_g$. Their bases define a basis family, equal to 1 off $P_g$.
6. `local_component_vector_relation_alt` gives lattices $N_j$, base points $b_j$, a twist $d_T$, lattices and frames for $o$, the shape condition and `LocY` at each place.
7. The measure condition does not depend on base points (`meas_upd_alt`), so $m$ still works with $b$.
8. `local_component_places_characterized_alt` gives the test functions $\Psi, \Psi_T$ and the ties. `exists_levelData_alt` gives level groups and the local groups $G_i$. `local_component_at_split_place_alt` gives the data at $Q$.
9. The bottom datum is $(\mathcal B, b_0, 1, 1, 1)$. The rest is bookkeeping.

## In the Lean code

The theorem is at [CoreDataOfPoint.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoreDataOfPoint.lean#L52); `XGeo`, `YRat`, `LocX` and `LocY` are in [FrameTopAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/FrameTopAlt.lean#L25). The type data $o$ are built for base points 1 and reused for $b$. The constants $c_0$ are free: the proof stores them. The proof shows twice that $P_G$ and $P_T$ are disjoint (here and in `lattices_frames_basePoints_exist_alt`). We have not unfolded `PreT`, `IsTypePlaces` or the published inputs. A parallel copy for `RealPack`, `core`, is in [AllTrueFamilyDatum.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/AllTrueFamilyDatum.lean#L77).
