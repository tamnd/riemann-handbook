---
id: exists-hilbert-modular-form-congr-one
title: Hilbert modular forms congruent to 1, by name
kind: theorem
decl: UpperTheory.V.Published.exists_hilbertModularForm_congr_one
module: Development.AutomorphicArithmetic.AutomorphicVarieties.GaussSumFiltrations.ExistsHilbertModularFormCongrOne
covers: 581
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`hilbertOne`](/entry/hilbert-one/). It states `HilbertOne`, the existence of level one Hilbert modular forms whose $q$-expansions are $p$-adically close to $1$, in all weights divisible by $(p-1)p^N$. [`oneUse`](/entry/one-use/) uses it to get such a form in a weight above a given bound. The real content is in [`hilbertOne`](/entry/hilbert-one/).

## Statement

Let $F$ be totally real, $p$ an odd prime and $\iota \colon \overline{\mathbb{Q}}_p \to \mathbb{C}$ an isomorphism.

**Theorem** (`HilbertOne`). There is $N$ such that for every $k > 0$ with $(p-1)p^N \mid k$ there is a form $\varphi$ that is holomorphic of parallel weight $k$, with level exponent $0$ at every place and trivial central character (`IsHol k (fun _ => 0) 1 φ`). Its $q$-expansion `HasExp φ k c₀ c` has $\|\iota^{-1}(c_0(y)) - 1\| < 1$ for all $y$ and $\|\iota^{-1}(c(\mathfrak{m}))\| < 1$ for all $\mathfrak{m} \neq 0$.

## Proof

The proof is the term `GlobalTheory.HilbertThetaSeries.hilbertOne`. The statement and the proof are the same as those of that theorem.

## In the Lean code

The theorem is in [ExistsHilbertModularFormCongrOne.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaussSumFiltrations/ExistsHilbertModularFormCongrOne.lean#L6), and `HilbertOne` is in [Hilbert.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PublishedTheorems/Hilbert.lean#L18). The name is in the namespace `Published`, but the proof is in this development, not a cited result.
