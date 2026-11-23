---
id: orbit-entry-bounds-of-family
title: The orbit entry bounds of a datum
kind: theorem
decl: Formalism.MainNotions.DIV.Lemmas.OrbitEntryBounds.orbit_entry_bounds_of_family
module: Formalism.SharpRestriction.Divisibility.ChainOperators.OrbitEntryBounds
covers: 437
status: drafted
drafted_by: writer@claude
---
This theorem proves the eight orbit bounds `Core D L X K Dx E ce C` from one valuation bound and three shape conditions. Its only user is [the orbit entry bounds from the letter bounds](/entry/orbit-entry-bounds-hold/), which proves the valuation bound.

## Statement

Let $D$ be a datum of type `D7`. A datum `E : Ent D` gives, for each word $u$, level $i$ and place $z$, a Young diagram $\nu_{u,i,z}$ with row lengths fixed by $D$. It also gives, for each place $w$ with residue characteristic $\ell$, power series `Th` over $\mathbb{C}_\ell$. The basic bound is `KvalGe l nu Th B`:
$$\big\| \mathrm{coeff}_m \big( \mathrm{applyAt0}(\mathrm{Th}, G_{\nu, I}) \big) \big\| \le \ell^{-B} \quad \text{for all column choices } I \text{ and all } m.$$

`Core` is the conjunction of eight statements.

- `OrbitsAddLowerBound`: if each orbit representative $r$ has a bound $\beta_r$ on its orbit, then a theta series with an expansion at all places has the bound $\sum_r \beta_r$.
- `OrbitsAddAtConjugate`: the same when `nP D p = 1`, for the expansion `ThetaExpansionRealPlaces`.
- `OrbitRestriction` and `OrbitRestrictionAtConjugate`: the restriction of such a series to one orbit or place satisfies the local condition there.
- `OrbitValuationBound`: an orbit bound with the threshold `g0Pl + FOrb - errF`.
- `EntriesAtDiscriminant`: at places of class `ramD`, `Th` has the bound $-\tfrac12 \sum_t c_t$.
- `ValuationSumBound`: an inequality between `FInert - EatC` and a size term.
- `ScaledGeneratorsInSup`: at `IsCs` primes, a bound `lowCs` for series of theta product form and, if `ce.Large`, the inequality `FInert - EatI ≤ lowCs`.

**Theorem.** If `OrbitValuationBound E X K ce`, `ThetaKernelShapeAtD E Dx`, `Shape D L X E` and `CLarge C6 C K ce` hold, then `Core D L X K Dx E ce C` holds.

`Shape` has ten conditions on sizes, rows and caps. `CLarge` says $0 \le C$, $C_6 \le$ `ce.c6`, $3C \le 1 +$ `K.dl1` and $3C \le$ `ce.dig`, with two sign conditions.

## Proof

The term is a tuple. The four orbit parts are `PI.OrbAddUp`, `PI.OrbAddOne`, `PI.OrbRestr` and `PI.OrbRestrOne`, applied to `toEnt E`. `OrbitValuationBound` is the hypothesis. `EntriesAtDiscriminant` is `jet_bound_ramified_prime` with `ThetaKernelShapeAtD`. `ValuationSumBound` is `PI.SumOrbC` with `Shape` and `CLarge`. `ScaledGeneratorsInSup` uses `kvalGe_theta_of_shape` and `fInert_sub_eatI_le_orbit_average_sub_errors`.

## In the Lean code

The theorem is in [OrbitEntryBounds.lean](lean:Formalism/SharpRestriction/Divisibility/ChainOperators/OrbitEntryBounds.lean#L43) and `Core` is in [OrbitPlaces.lean](lean:Formalism/SharpRestriction/Divisibility/OrbitPlaces.lean#L1323).

- The name says "of family", but the statement is about one datum $D$ and one `E`.
- The four orbit parts need no hypothesis, and `C6` does not appear in `Core`.
- We have not unfolded `applyAt0`, `Gxz`, `FOrb`, `errF`, `FInert` or the lemma proofs.
