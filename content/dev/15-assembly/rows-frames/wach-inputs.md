---
id: wach-inputs
title: The Wach inputs of a crystalline block
kind: theorem
decl: GlobalTheory.WachBlock.wach_inputs
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CrystallineBlockLatticesOverPowerSeriesRing
covers: 969
status: drafted
drafted_by: writer@claude
---
This theorem makes the lattice data `NInputs` for a crystalline block: matrices of Wach type over a power series ring, in bases where the reduced Frobenius and $\gamma$ are block triangular. It is the proof of [the lattices over a power series ring for a crystalline block](/entry/crystalline-block-lattices-over-power-series-ring/), a second name for it. The proof joins three results. The lattices themselves come from [the Wach lattices](/entry/wach-lattices/).

## Statement

Let $E$ be a CM field, $\ell \neq 2$ a prime with $\ell \nmid \operatorname{disc} E$, and $\Phi$ the set of embeddings $E \to \overline{\mathbb{Q}}_\ell$. Let $\sigma$ be a permutation of $\Phi$ with $|\sigma\tau(x) - \tau(x)^\ell| < 1$ for $x \in \mathcal{O}_E$ (`IsFrobPerm`). Let $n, t, h \ge 0$, $J(\tau, a) \in [0, h]$ for $a < n$, and $\mathrm{bot}(\tau) + s \in [0, h]$ for $s < t$.

`BlockPair E Ω l n t J bot` says: there are a representation $r \colon G_E \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$, crystalline with Hodge-Tate weights $J$ (`CrysWith`), a continuous $\rho \colon G_E \to \mathrm{GL}_a$ with $a + t = n$, and characters $\chi_s$, crystalline of weight $\mathrm{bot} + s$, such that every coefficient of $\operatorname{charpoly} r(g) - \operatorname{charpoly} \rho(g) \prod_s (X - \chi_s(g))$ has norm less than $1$.

**Theorem.** Assume `BhattScholzeCrystallineLattices` and `BlockPair E Ω l n t J bot`. Then there are $\mathcal{O}'$, $F$, $L'$, $I$, a `WLat` $W_l$, $u$, $c$, $\kappa$, $\zeta$, $\mathrm{em}$ and $j_b$ with `NInputs` at height $h$, weights $J$ for the rank $n$ part and $\mathrm{bot} + s$ for the rank one parts.

A `WLat` holds a reduction map $\mathcal{O}' \to F$, a power series $u_n$, the lattice data $N$ and $N_{\psi,s}$ of [the Wach lattices](/entry/wach-lattices/), base changes $g_\tau$ over $F[[X]]$, a block index $b$, positions $\mathrm{pos}(s)$ and units $w_{\tau,s}$. `NInputs` asks that:

1. $u = 1 + \ell c$ with $c$ a unit, `IsUn`, and the weights in $[0, h]$;
2. after the base change $g$, the reduced Frobenius and $\gamma$ matrices of $N$ are block triangular for $b$, and their diagonal entries at $\mathrm{pos}(s)$ match $N_{\psi,s}$ up to $w$ and powers $X^{\kappa}$;
3. $\zeta$ is a primitive $\ell$-th root of unity with $\zeta - 1 \in I$, and `IsLocExp` holds for $j_b$;
4. `LatN` holds for $N$ and for each $N_{\psi,s}$.

## Proof

1. `integralCrystallineBlockData_of_reductionPair` turns the `BlockPair` into an `IntegralBlock`: a crystalline representation with weights $J$ over the integers of a finite extension, with a stable lattice chain whose steps add lines on which it acts by characters $\psi_s$ of weight $\mathrm{bot} + s$.
2. [`wachLattices_rankOne_models_reducedFiltration`](/entry/wach-lattices-rank-one-models-reduced-filtration/) gives $N$, $N_{\psi}$, $u$, $c$, $u_n$, $\zeta$, $j_b$ and the flag `RedFilt` of the reductions.
3. `adaptedBases_blockTriangular_of_reducedEtaleFiltration` turns the flag into $g$, $b$, $\mathrm{pos}$, $w$ and $\kappa$ with the conditions of clause 2.

The proof packs these into a `WLat` and `NInputs`. It adds no mathematics.

## In the Lean code

The theorem is in [CrystallineBlockLatticesOverPowerSeriesRing.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CrystallineBlockLatticesOverPowerSeriesRing.lean#L18). `WLat`, `WFrame` and `NInputs` are in [LemmaWFromLattice.lean](lean:Formalism/PieriBlockIdeals/LemmaWFromLattice.lean#L216), in the namespace `Formalism.CohomologicalDescent.FrobeniusPeriodChange`. `BlockPair` is in [HasBlockOfOccurs.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasBlockOfOccurs.lean#L196).

- Step 1 does not use the Bhatt-Scholze input, $\ell \neq 2$ or the discriminant. They only pass to step 2.
- We have not unfolded `CrysWith`, `IsUn`, `IsLocExp` or `LatN` here. [The Wach lattices](/entry/wach-lattices/) describes `LatN`.
