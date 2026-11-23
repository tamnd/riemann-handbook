---
id: crystalline-block-lattices-over-power-series-ring
title: Lattices over a power series ring for a crystalline block (restatement)
kind: theorem
decl: GlobalTheory.T.crystalline_block_lattices_over_power_series_ring
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CrystallineBlockLatticesOverPowerSeriesRingStatement
covers: 970
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [the Wach inputs of a block](/entry/wach-inputs/), under a second name. The real content is in that entry, and below it in [the Wach lattices](/entry/wach-lattices/). Its only user is step 4 of [the lattice link of a block](/entry/lattice-link-of-block-for/).

## Statement

Let $E$ be a CM field and $\ell \neq 2$ a prime with $\ell \nmid \operatorname{disc} E$. Let $\Phi$ be the set of embeddings $E \to \overline{\mathbb{Q}}_\ell$ and $\sigma$ a permutation of $\Phi$ with $|\sigma\tau(x) - \tau(x)^\ell| < 1$ for $x \in \mathcal{O}_E$ (`IsFrobPerm`). Let $n, t, h \ge 0$, $J(\tau, a) \in [0, h]$ and $\mathrm{bot}(\tau) + s \in [0, h]$ for $s < t$.

**Theorem.** Assume `BhattScholzeCrystallineLattices` and `BlockPair E Ω l n t J bot`. Then there are a domain $\mathcal{O}'$ over $\mathbb{Z}_\ell$, complete for an ideal $I$, a field $F$ of characteristic $\ell$, a field $L'$, data `WLat` of rank $n$ with $t$ rank one parts, a unit $u$ and $c$ of $\mathbb{Z}_\ell$, integers $\kappa$, an element $\zeta$, a map $\mathcal{O}' \to L'$ and maps $j_b$ such that `NInputs` holds at height $h$ with weights $J$ and $\mathrm{bot} + s$.

`BlockPair` and `NInputs` are explained in [the Wach inputs of a block](/entry/wach-inputs/).

## Proof

The statement is the statement of `GlobalTheory.WachBlock.wach_inputs`, word for word. The proof applies that theorem.

## In the Lean code

The theorem is in [CrystallineBlockLatticesOverPowerSeriesRingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CrystallineBlockLatticesOverPowerSeriesRingStatement.lean#L8). The proof is the tactic

```
first | exact @GlobalTheory.WachBlock.wach_inputs | exact GlobalTheory.WachBlock.wach_inputs | (intros; apply GlobalTheory.WachBlock.wach_inputs <;> assumption)
```

It tries three ways to apply the same theorem. The two statements have the same text, so the first way should be enough. We did not run Lean to see which way succeeds. The file also sets `maxHeartbeats` to 1000000 for this one line.
