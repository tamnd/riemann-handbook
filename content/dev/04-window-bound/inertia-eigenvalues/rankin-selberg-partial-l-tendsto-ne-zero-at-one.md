---
id: rankin-selberg-partial-l-tendsto-ne-zero-at-one
title: The partial Rankin-Selberg L-function of two distinct representations has a nonzero limit at 1, a second name
kind: theorem
decl: GlobalTheory.T.rankinSelberg_partialL_tendsto_ne_zero_at_one
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.RankinSelbergPartialLTendstoNeZeroAtOneStatement
covers: 768
status: drafted
drafted_by: writer@claude
---
This theorem states that $L^T(x, \sigma \times \tilde\sigma')$ has a finite nonzero limit as $x \to 1^{+}$ when $\sigma$ and $\sigma'$ are distinct unitary cuspidal representations. [The bound on the real part of the logarithm](/entry/abs-re-log-rs-bdd/) uses it. It is a second name for [`tendsto_partialL_ne_zero`](/entry/tendsto-partial-l-ne-zero/), which has the proof.

## Statement

Let $E$ be a totally complex number field and $T$ a finite set of primes of $E$. Let $\sigma$ be a unitary [[cuspidal representation|9AZ164C298]] of $\mathrm{GL}_a$ over $E$ and $\sigma'$ one of $\mathrm{GL}_b$, with $a, b \geq 1$ and $(a, \sigma) \neq (b, \sigma')$. Suppose both have Satake parameters at each $w \notin T$. For real $x > 1$ let
$$L^T(x) = \prod_{w \notin T} \prod_{\alpha \in \mathrm{sat}(\sigma, w)} \prod_{\beta \in \mathrm{sat}(\sigma', w)} \bigl(1 - \alpha \bar\beta\, Nw^{-x}\bigr)^{-1}.$$

**Theorem.** There is $z \in \mathbb{C}$ with $z \neq 0$ and $L^T(x) \to z$ as $x \to 1^{+}$.

For unitary $\sigma'$ the parameters $\bar\beta$ are those of the contragredient, so $L^T(x)$ is the partial L-function $L^T(x, \sigma \times \tilde\sigma')$. The result is the nonvanishing at $s = 1$ of Jacquet and Shalika and of Shahidi, cited in [the vanishing lemma](/entry/vanish/).

## Proof

The proof is one line, `first | exact @GlobalTheory.RSNonvan.tendsto_partialL_ne_zero | ...`. The statement is the same as that of [`tendsto_partialL_ne_zero`](/entry/tendsto-partial-l-ne-zero/).

## In the Lean code

- The theorem is in [RankinSelbergPartialLTendstoNeZeroAtOneStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RankinSelbergPartialLTendstoNeZeroAtOneStatement.lean#L6). Its file imports the file of the proof.
- The infinite product in Lean is `tprod` of `locL (Nw) (sat σ w) (conj (sat σ' w)) x`. `sat` and `locL` are in [UnrOutside.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/UnrOutside.lean#L16).
- The proof is by `first | ... | ... | ...`, with three ways to apply the same lemma. This pattern is the same in the other `...Statement` files of this folder.
