---
id: wach-lattices-rank-one-models-reduced-filtration
title: Wach lattices with rank one models and a reduced filtration (restatement)
kind: theorem
decl: GlobalTheory.T.wachLattices_rankOne_models_reducedFiltration
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.WachLatticesRankOneModelsReducedFiltrationStatement
covers: 890
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [the Wach lattices for an integral block](/entry/wach-lattices/), under a second name. The real content is in that entry, and below it in [the global positions lemma](/entry/exists-positions-global/). Its only user is step 2 of [the Wach inputs of a block](/entry/wach-inputs/).

## Statement

Let $E$ be a CM field, $\ell \neq 2$ a prime with $\ell \nmid \operatorname{disc} E$, and $\sigma$ a permutation of the embeddings $E \to \overline{\mathbb{Q}}_\ell$ that lifts Frobenius (`IsFrobPerm`). Let $n, t, h \ge 0$, $J(\tau, a) \in [0, h]$ and $\mathrm{bot}(\tau) + s \in [0, h]$ for $s < t$.

**Theorem.** Assume `BhattScholzeCrystallineLattices` and `IntegralBlock E Ω l n t J bot`. Then there are a domain $\mathcal{O}'$ over $\mathbb{Z}_\ell$, complete for an ideal $I$, with a reduction map to a field $F$ of characteristic $\ell$, a power series $u_n$, lattice data $N$ of rank $n$ and $N_{\psi,s}$ of rank one, $u = 1 + \ell c$ with $c$ a unit, $\zeta$ and maps $j_b$ such that:

1. `IsUn` holds for $u_n$, $\zeta$ is a primitive $\ell$-th root of unity with $\zeta - 1 \in I$, and `IsLocExp` holds for each $j_b$, $0 < b < \ell$;
2. `LatN` holds for $N$ with weights $J$ and for $N_{\psi,s}$ with weight $\mathrm{bot} + s$;
3. the reductions satisfy `RedFilt`.

All terms are defined in [the Wach lattices for an integral block](/entry/wach-lattices/).

## Proof

The statement is the statement of `GlobalTheory.WachPlace.wach_lattices`, word for word. The proof applies that theorem.

## In the Lean code

The theorem is in [WachLatticesRankOneModelsReducedFiltrationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/WachLatticesRankOneModelsReducedFiltrationStatement.lean#L7). The proof is the tactic

```
first | exact @GlobalTheory.WachPlace.wach_lattices | exact GlobalTheory.WachPlace.wach_lattices | (intros; apply GlobalTheory.WachPlace.wach_lattices <;> assumption)
```

It tries three ways to apply the same theorem. The two statements have the same text, so the first way should be enough. We did not run Lean to see which way succeeds. The file also sets `maxHeartbeats` to 1000000 for this one line, and it imports `Mathlib` twice.
