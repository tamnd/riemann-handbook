---
id: lattice-link-of-block-for
title: A lattice link from a crystalline block
kind: theorem
decl: GlobalTheory.ExpLink.latticeLink_of_blockFor
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CrystallineLatticeLinkOfBlockData
covers: 986
status: drafted
drafted_by: writer@claude
---
This theorem turns a crystalline block at a prime $\ell$ into a lattice link: labels on the embeddings of $E$, with Wach-type lattices that carry them. It is the proof of [the crystalline lattice link of block data](/entry/crystalline-lattice-link-of-block-data/), a second name for it. The lattices come from [the Wach inputs of a block](/entry/crystalline-block-lattices-over-power-series-ring/). This theorem only chooses the Frobenius permutation and does the bookkeeping of labels.

## Statement

Let $E$ be a CM field, $\ell \neq 2$ a prime with $\ell \nmid \operatorname{disc} E$, and $\Phi$ the set of embeddings $E \to \overline{\mathbb{Q}}_\ell$. Write $\bar\tau = \tau \circ c$ for complex conjugation $c$. Let $\mathrm{inc} \colon \iota \to \Phi$ be `IsHalf`: injective, $\overline{\mathrm{inc}\,\tau} \neq \mathrm{inc}\,\tau'$, and each embedding is $\mathrm{inc}\,\tau$ or $\overline{\mathrm{inc}\,\tau}$.

Let $(P, W)$ be parameters and weights, with $N = N_r$, height $h_0 = \lfloor h \rfloor$ and labels $U_W(\tau, a) = \lambda_\tau(a) + N - 1 - a$. $\mu$ is `Linked` to $\lambda = W.\mathrm{lam}$ at $\ell$ if each $\mu_\tau$ is decreasing on $[0, N)$, lies between $\lambda_\tau(N-1)$ and $\lambda_\tau(0)$, has the sum of $\lambda_\tau$, and $\prod_a (X + \lambda_\tau(a) - a) = \prod_a (X + \mu_\tau(a) - a)$ in $\mathbb{F}_\ell[X]$.

`BlockFor` $\mu$ says that a crystalline block `BlockPair` (see [the Wach inputs](/entry/wach-inputs/)) exists with weights $J = U_\mu$ on $\mathrm{inc}\,\tau$ and $h_0 - U_\mu$ reversed on $\overline{\mathrm{inc}\,\tau}$, and with $\mathrm{bot}$ given by $W$, up to a global swap by $c$.

**Theorem.** Assume `BhattScholzeCrystallineLattices`. There are $fr \colon \mathbb{N} \to \iota \to \iota$ and $cj \colon \mathbb{N} \to \iota \to \mathrm{Bool}$ such that: if `P.Hyp`, `W.Ok P`, all $U_W(\tau, a) \in [0, h_0]$, $\mu$ is `Linked` to $\lambda$ and `BlockFor` $\mu$ holds, then for each $\tau$, `LatticeLink` holds for $W$ with Frobenius data $fr, cj$, at $\ell$, $\tau$ and $\mu_\tau$.

`LatticeLink` asks for a permutation $\sigma$ of a finite set, labels $D$ on it and data `WLat` with `NInputs` at height $h_0$. The labels are symmetric under $c$ (`Refl`), have congruent characteristic polynomials (`Linked`), are carried by $J$ (`Carried`) and agree with $W$ on $\iota$. $\sigma$ sends $\mathrm{inc}\,\tau$ to $\mathrm{inc}(fr\,\tau)$ or its conjugate, as $cj\,\tau$ says.

## Proof

1. `exists_arithFrobenius_embedding_perm_cmConj` uses $\ell \nmid \operatorname{disc} E$ to give a permutation $\sigma$ of $\Phi$ with $|\sigma\tau(x) - \tau(x)^\ell| < 1$ on $\mathcal{O}_E$ that commutes with $c$.
2. Write $\sigma(\mathrm{inc}\,\tau)$ as $\mathrm{inc}\,\tau'$ or $\overline{\mathrm{inc}\,\tau'}$. Set $fr\,\tau = \tau'$, and let $cj\,\tau$ say which case holds.
3. From `BlockFor` take $J$, $\mathrm{bot}$ and the `BlockPair`. The bounds on $U_W$ and `Linked` give $0 \le J \le h_0$ and $0 \le \mathrm{bot} + s \le h_0$.
4. [The Wach inputs of a block](/entry/crystalline-block-lattices-over-power-series-ring/) give `WLat` and `NInputs`.
5. Take $\Phi$, $\sigma$ and the labels `labels inc P W mu`: $U_W$ and $U_\mu$ on $\mathrm{inc}\,\iota$, and $h_0$ minus the reversed labels on the conjugates. The rest is bookkeeping from `W.Ok`, `Linked` and `BlockFor`.

## In the Lean code

The theorem is in [CrystallineLatticeLinkOfBlockData.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CrystallineLatticeLinkOfBlockData.lean#L58). `LatticeLink` is in [LatticeInclusionRealSettingAlt.lean](lean:Formalism/PieriBlockIdeals/LatticeInclusionRealSettingAlt.lean#L372). `Linked`, `BlockPair`, `IsHalf` and `BlockFor` are in [HasBlockOfOccurs.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasBlockOfOccurs.lean#L36).

- $fr$ and $cj$ ignore their argument in $\mathbb{N}$. They depend only on $\iota$ and $\sigma$, not on $P$, $W$ or $\mu$.
- We have not unfolded `CrysWith`, `IsCrysAt` or `IsJumpsAt`. The words "crystalline with weights" above are their names, not checked content.
