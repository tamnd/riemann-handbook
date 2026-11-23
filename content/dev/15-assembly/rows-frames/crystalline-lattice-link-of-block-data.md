---
id: crystalline-lattice-link-of-block-data
title: A crystalline lattice link from block data (restatement)
kind: theorem
decl: GlobalTheory.T.crystallineLatticeLink_of_blockData
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CrystallineLatticeLinkOfBlockDataStatement
covers: 987
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [the lattice link of a block](/entry/lattice-link-of-block-for/), under a second name. The real content is in that entry. Step 1 of [the model statement for a small frame](/entry/model-st-of-small-frame-gal/) takes from it the maps $fr$, $cj$ and the lattice link. `ExpModel.modelSt_of_frames` uses it too.

## Statement

Let $E$ be a CM field and $\ell \neq 2$ a prime that does not divide the discriminant of $E$. Let $\iota$ be a set of embeddings $E \to \overline{\mathbb{Q}}_\ell$ that holds exactly one of each pair $\{\tau, \bar\tau\}$ (`IsHalf`). The terms `Linked`, `BlockFor` and `LatticeLink` are defined in [the lattice link of a block](/entry/lattice-link-of-block-for/).

**Theorem.** Assume `BhattScholzeCrystallineLattices`. Then there are maps $fr \colon \mathbb{N} \to \iota \to \iota$ and $cj \colon \mathbb{N} \to \iota \to \mathrm{Bool}$ with this property. Let $(P, W)$ be parameters and weights with `P.Hyp` and `W.Ok P`, with all $U_W(\tau, a)$ in $[0, h_0(P)]$. Let $\mu$ be linked to $W$ at $\ell$ and let `BlockFor` hold for $\mu$. Then for each $\tau \in \iota$, `LatticeLink` holds for $W$ with Frobenius data replaced by $fr$, $cj$, at $\ell$ and $\tau$, with the first $N_r$ values of $\mu(\tau)$.

## Proof

The statement is the statement of `GlobalTheory.ExpLink.latticeLink_of_blockFor`, word for word. The proof applies that theorem.

## In the Lean code

The theorem is in [CrystallineLatticeLinkOfBlockDataStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CrystallineLatticeLinkOfBlockDataStatement.lean#L8). The proof is the tactic

```
first | exact @GlobalTheory.ExpLink.latticeLink_of_blockFor | exact GlobalTheory.ExpLink.latticeLink_of_blockFor | (intros; apply GlobalTheory.ExpLink.latticeLink_of_blockFor <;> assumption)
```

It tries three ways to apply the same theorem. The two statements have the same text, so the first way should be enough. We did not run Lean to see which way succeeds. The file also sets `maxHeartbeats` to 1000000 for this one line.
