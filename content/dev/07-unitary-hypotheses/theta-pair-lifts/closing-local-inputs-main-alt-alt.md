---
id: closing-local-inputs-main-alt-alt
title: The congruence length bound at one datum, from p-adic Hodge theory and Artin reciprocity
kind: theorem
decl: GlobalTheory.ClosingLocalInputs.main_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.AdmG14OfAux
covers: 3255
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `PairedCharacterConditionAlt D C CT` at one datum $D$: at each local index, the length of a congruence module is at most a weighted sum of local terms. It has the content of a chain of copies. Its copy [`conclusion41_of_pAdicHodge_alt`](/entry/conclusion41-of-p-adic-hodge-alt/) is called by [`NormFromFacts.main_alt_alt`](/entry/norm-from-facts-main-alt-alt/), and the bound goes up to [the bound LinkN for one family](/entry/link-n-of-tw-good-galois-preconditions/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 3,255 declarations.

## Statement

A datum $D$ (a `D7`) has a CM field $E$, two primes $g_0, g_1$, ranks $r$, $n_V$, $t$, $f$, and local indices $i$. At $i$ there are a prime $\ell_i$, a ring $O_i$, a finite set $X_i$ of Hecke eigensystems with subsets $Z_i$ and $Z^{\mathrm{good}}_i$, and a Hecke algebra that acts on a free $O_i$-module $M_i$. Let $\eta_i$ (`etaLoc`) be the $\ell_i$-adic length of $M^{\mathrm{up}}_i / M^{\mathrm{low}}_i$, where $M^{\mathrm{low}}_i$ is the lattice part of the good eigenspaces and $M^{\mathrm{up}}_i$ is the part of the good eigenspaces in the lattice plus the other eigenspaces. So $\eta_i$ measures congruences between good and other eigensystems. Let $m(\pi)$ be the Hecke multiplicity of $\pi$.

`PairedCharacterConditionAlt D C CT` says: let $\ell_i = g_k$ with $k \neq k'$. Let $r_x \colon G_E \to \mathrm{GL}_{n_V}(O_i)$ and $\rho_x \colon G_E \to \mathrm{GL}_r(O_i)$, for $x \in X_i$, be good families with a semisimple decomposition at each $\pi \in Z_i$. Let $\eta, s, S \in \mathbb N$, signs $\mathrm{sg}$ and finite sets $U(w) \subset \mathbb Z$ satisfy:

- $\eta + t + 1 < s$, $\log g_{k'} \le 2 \log g_k$ and $C_T\bigl((s+S)(n_V+1)^2 + (n_V+1)^3\bigr) < g_k$;
- the signs are opposite at distinct conjugate places above $\ell_i$;
- at each place $w$ above $\ell_i$, $|U(w)| \le n_V$, $U(w)$ holds the jumps (`IsJumpV`) of the local twisted $r_x$, and each $a \in U(w)$ is in $[0,t)$, near the centre $(t-1)/2$, or in a window fixed by $\mathrm{sg}(w)$, with $a \neq -1, t$;
- a finiteness condition `Br.sFin` at each good $\pi$, and $\mathrm{sha}(\ell_i, e) < \infty$ for $0 < e < t$.

Then $\eta_i \le \sum_{\pi \in Z^{\mathrm{good}}_i} m(\pi)\, R(\pi)$, where $R(\pi)$ is $4 f C n_V^3 (n_V + \eta + t) + 2 f r^2$ plus five local terms (`rhs`).

**Theorem.** Assume `GlobalArtinReciprocity`, `BhattScholzeIntegral`, `FontaineBcris`, `BlochKatoLocal`, `LocalTateDualityK` and `LocalEulerCharK`. Let $D$ be a datum with local data $HW$, $F$, $Cm$ (`HWOf`, `FonOf`, `CmpOf`). Let $C_T \ge 40$ and $8 C_T \le C$. Assume a pending datum $P$ with `admDZ P` and `EigSpan P`, and twelve named conditions on $D$: `tie0`, `adm1`, `adm2_alt`, `adm5`, `provisionFortyOne`, `ConclusionG5`, `ConclusionG6`, `ResidualIrreducibleRankR`, `SerLoc`, `TypePrimeWildIdempotentChoice`, `TieInePoly`, `tieChi`. Then `PairedCharacterConditionAlt D C CT`. We have not unfolded most of them.

## Proof

1. `crystallinePeriodBound_all_constant_ge_forty` (3,069 declarations) gives `admT CT` from the five p-adic inputs, as $C_T \ge 40$. This is a statement `thmT` at each prime $\ell$: for potentially crystalline lattices and a surjection between them, with jumps in $U \subset [-\eta, H]$ and inertia through a set of size at most $N$, if $C_T(HN^2 + N^3) < \ell$ then a lifting property `LiftF` holds with an explicit bound. We have not unfolded `LiftF`.
2. Three lemmas give local statements from Bloch-Kato, Tate duality and the Euler characteristic: `local_absorption_length_bound_of_blochKato`, `theorem_tb_of_local_blochKato_duality_euler`, `blochKatoLocal_all_of_tateDuality_eulerChar`.
3. `residualRep_spans_matrixAlgebra_of_goodPoint` gives residual absolute irreducibility. `typePrimeCongruences_forall` gives `TypePrimeChoiceLemmas`. `galoisFamilyConditions_of_sumRepresentations_alt` reads `GaloisFamilyConditions'` off `provisionFortyOne`.
4. `admT_of_artin_reciprocity_and_local_conditions` takes Artin reciprocity and all of the above and gives the bound.

## In the Lean code

The theorem is at [AdmG14OfAux.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AdmG14OfAux.lean#L15), the bound at [LocalGlobalCompatibility.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocalGlobalCompatibility.lean#L15), and $\eta_i$ at [DataN.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean#L219). Each hypothesis is used.

Odd points:

- `PairedCharacterConditionAlt` is `aux₃` of [PairedCharacterCondition.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/PairedCharacterCondition.lean#L159) without the hypothesis `SetSQ i r`, so it is stronger. Its name speaks of characters; its statement is a length bound.
- The file name `AdmG14OfAux` does not match the statement.
