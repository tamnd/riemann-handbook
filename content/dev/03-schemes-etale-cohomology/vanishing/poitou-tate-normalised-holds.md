---
id: poitou-tate-normalised-holds
title: Poitou-Tate duality with normalised local invariants
kind: theorem
decl: PositivityTheory.Lit1.PTN.poitouTateNormalised_holds
module: Development.WeilBound.CoreStatements.PublishedTheorems.PoitouTateDuality.PoitouTateNineTerm.PoitouTateNormalisedHolds
covers: 316
status: drafted
drafted_by: writer@claude
---
This theorem proves `PoitouTateNormalised`: the Poitou-Tate nine-term exact sequence, the duality of the Tate-Shafarevich groups and the vanishing of $H^n$ for $n \geq 3$, for finite $\ell$-primary modules. It sits below the step [EveryCharacter from Row0b](/step/every-character-of-row/). The code uses it through two wrappers that return it with no change: `poitou_tate_normalised_of_literature`, near the [literature structure](/step/every-character-of-literature/), and `poitou_tate_normalised_of_open`. Below this theorem are 316 declarations.

## Statement

Let $F$ be a number field with algebraic closure $\Omega$, $\ell$ a prime and $r > 0$, with $\ell \neq 2$ or $F$ totally complex. Let $\zeta \in \Omega$ be a primitive $\ell^r$-th root of unity.

**Theorem.** There is a family `inv` of local invariant maps $H^2(D_A, \mu_{\ell^r}) \to \mathbb{Z}/\ell^r$, one for each place $A$ of $\Omega$ over a finite place $v$, such that each is bijective and normalised (`IsNormalised ζ A v`). With this family the following holds. Let $S$ be a finite set of finite places that contains the places above $\ell$, with a chosen place over each $v \in S$, and let $\mu$ be the cyclotomic character of $G_S$ mod $\ell^r$. Let $M$ be a finite discrete $\mathbb{Z}/\ell^r$-module with a continuous action of $G_S$, and $M^* = \operatorname{Hom}(M, \mu_{\ell^r})$. Then:

1. `NineTermExact`: there are maps $\delta_1$ and $\delta_2$ such that
$$\begin{aligned}&{0 \to H^0(M) \to \bigoplus_{v \in S} H^0_v(M) \to H^2(M^*)^\vee \xrightarrow{\delta_1} {}}\\ &{\quad H^1(M) \to \bigoplus_v H^1_v(M) \to H^1(M^*)^\vee \xrightarrow{\delta_2} {}}\\ &{\quad H^2(M) \to \bigoplus_v H^2_v(M) \to H^0(M^*)^\vee \to 0}\end{aligned}$$
is exact. Here $H^i_v$ is the cohomology of the decomposition group at the chosen place, and the maps to the duals are sums of local cup products followed by `inv`.
2. `ShaDual`: $\mathrm{Sha}^1(M^*)$ and $\mathrm{Sha}^2(M)$ are finite, of the same order, and $\mathrm{Sha}^2(M)$ is isomorphic to the dual of $\mathrm{Sha}^1(M^*)$. The same holds with $M$ and $M^*$ swapped.
3. $H^n(G_S, M) = 0$ for $n \geq 3$.

This is the form of Milne, *Arithmetic Duality Theorems*, Theorem I.4.10. The archimedean terms are absent. This is correct because $\ell \neq 2$ or $F$ is totally complex.

## Proof

The proof is `poitouTateNormalised_of_nine (nineCmpFS_of_nineAddFS nineAddFS_V)`.

1. `nineAddFS_V` proves `NineAddFS`, the nine-term sequence over subfields $K \subset \overline{\mathbb{Q}}$, up to isomorphisms of the terms and signs of the maps. It takes data from `foundData_nonempty` and calls `nineAdd_core`. `nineCmpFS_of_nineAddFS` turns it into `NineCmpFS`, the same with $\mathbb{Z}/\ell^r$-linear isomorphisms.
2. `poitouTateNormalised_of_nine` adds the Sha duality `shaCmpFS'` and the vanishing `GFVanish.vanishAll`, and builds `PtfsHyp` with `ptfsHyp_of_cmp`.
3. `poitouTateNormalised_of` chooses `inv` by `exists_invFam_normalised`. Then `ptConclAt_all_of` moves the result from a subfield of $\overline{\mathbb{Q}}$ to $F$ and $\Omega$ (`exists_subfield_model`), with `locHyp_holds` for the decomposition groups and Frobenius elements.

## In the Lean code

The theorem is in [PoitouTateNormalisedHolds.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/PoitouTateDuality/PoitouTateNineTerm/PoitouTateNormalisedHolds.lean#L18). The statement is in [PoitouTateNormalised.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/PoitouTateNormalised.lean#L12), and `NineTermExact` and `ShaDual` are in [PoitouTateNineTermTransgressionZeroApply.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/PoitouTateNineTermTransgressionZeroApply.lean#L150). The bridge is in [Bridge.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/PoitouTateDuality/Bridge.lean#L21).

- The maps $\delta_1$ and $\delta_2$ are existential. The statement does not say that they are the connecting maps of the duality. The isomorphism in `ShaDual` is also existential and is not the cup product pairing. So the statement is weaker than Milne's.
- In `NineAdd` and `NineCmp` the ninth term has the variable name `BetaSesquilinearity`. The name has no relation to its role.
- We have not opened `nineAdd_core`, `shaCmpFS'` or `ptConcl_of_iso_of`.
