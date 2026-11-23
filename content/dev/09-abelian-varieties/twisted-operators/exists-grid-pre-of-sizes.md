---
id: exists-grid-pre-of-sizes
title: A grid of test data matches a given Weil family, under the size bounds
kind: theorem
decl: GlobalTheory.GridJoin.exists_gridPre_of_sizes
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.AuxiliaryPrimeLtFirstTypePrimeOfSizes
covers: 314
status: drafted
drafted_by: writer@claude
---
This theorem is [`exists_gridPre`](/entry/exists-grid-pre/) with two hypotheses given directly: `Sizes D` and $q_0 < g_0$, in place of the size rows. It builds a grid of test data and checks that it matches the given Weil family. Most of the work is in `exists_gridPre_agree`, in the same file, and in the lemmas that it calls.

## Statement

Assume `DiscreteSeriesUpqExists`, `DiscreteSeriesCover`, `HarishChandraModules`, `HostHyp D`, `Sizes D`, and $q_0 < g_0$, where $q_0$ = `q0 D` is the auxiliary prime and $g_0$ = `D.host.g 0`. Let $R$ satisfy `Core R F`, let `sc.cGap = 1`, and let $W$ be a Weil family of a grid $G'$ with `W.Over R`. Then there is $G$ : `GridPre R` with `G.Is` and `Match G W`.

A `GridPre R` holds the Hermitian spaces at the grid nodes, the core nodes $P_i$ and the top nodes $X_j$, with Weil representations, vacua, intertwiners and measures. `Match G W` is a match of the spaces and characters (node by node) and an agreement of the arrows (`ArrAgree`).

## Proof

1. `exists_sameWeil` replaces $W$ by a Weil family $W_1$ on a grid $G_1$ with the same data, whose lattices off row $0$ are `L0c`.
2. `exists_weil_ordered` replaces $W_1$ by $W_2$. At each node and each archimedean place it permutes the columns of the orthonormal basis, so that $b^* \,\mathrm{Gram}\, b = J_\varepsilon$ for sign data $\varepsilon$ that satisfy `IsEnum` with the local parameters. We did not unfold `IsEnum`. At row $0$ the basis does not change.
3. `exists_gridPre_agree` (line 123) gives $G$ with `G.Is` and `Agree G W₂`. It calls `T.exists_testGrid_from_levelChoiceGrid` for the spaces and characters, `T.exists_testGrid_arrows_vacua_intertwiners` for the arrows, and `exists_isMeas` for the measures.
4. `Agree G W₂` gives `Match G W`. At each node off row $0$, `nodeMatch_of` uses that the bases of $W_2$ and $W$ differ by a column permutation. At row $0$, `nodeAgree_grid0_of_weil_over` applies. The arrow part moves by `of_sameWeil`.

## In the Lean code

The theorem is at [AuxiliaryPrimeLtFirstTypePrimeOfSizes.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/AuxiliaryPrimeLtFirstTypePrimeOfSizes.lean#L153). The hypothesis $q_0 < g_0$ is used only through `auxiliaryPrime_ne_levelPrimes_of_lt`, which says that $q_0$ is not one of the level primes. In `exists_gridPre_agree` (lines 145 to 147) the arrow lemma is called by `first` in two forms, with and without `Sizes D`. We did not unfold `GridPre`, `Agree`, `Sizes` or `HostHyp`.
