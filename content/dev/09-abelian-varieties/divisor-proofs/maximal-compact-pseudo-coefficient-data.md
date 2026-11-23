---
id: maximal-compact-pseudo-coefficient-data
title: Pseudo-coefficient data on the maximal compact subgroup, restated
kind: theorem
decl: GlobalTheory.T.maximalCompact_pseudoCoefficientData
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MaximalCompactPseudoCoefficientDataStatement
covers: 784
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`maximalCompact_pseudoCoefficientData'`](/entry/maximal-compact-pseudo-coefficient-data-prime/), with the same statement `StKData`. That entry lists the lemmas, and [`stKData_of`](/entry/st-kdata-of/) has the argument. It is step 1 ("data on $K$") of [`localPC_holds`](/entry/local-pc-holds/).

## Statement

We use the notation of [`localPC_holds`](/entry/local-pc-holds/). Let $r$ be odd, $\lambda \in \mathbb{Z}^r$ with $\lambda_a - \lambda_{a+1} \geq 100\, r^4$, and $D$ a [[discrete series|9AB7HYGPEK]] with parameter $\lambda$. Then there are $M \in \mathbb{N}$ and a polynomial $P$ in the entries $x_{ab}$ with $\varepsilon_a = \varepsilon_b$ such that $P_M = \det(\bar{x})^M \cdot P \cdot \det(\Omega)$ satisfies:

1. $P_M({k'}^{-1} k k') = P_M(k)$ for $k, k' \in K$;
2. $P_M(t_\theta) = \overline{\Theta_\lambda(t_\theta)}\, d(\theta)$ when the $e^{i\theta_a}$ are distinct;
3. if $\int_K P_M(k)\, D(k)\, dk$ has trace $c$, then $c = 1$;
4. if $\pi$ is irreducible and unitary and not unitarily equivalent to $D$, and $\int_K P_M(k)\, \pi(k)\, dk$ has trace $c$, then $c = 0$.

Here $\Omega$ (`OmP`) is a matrix of derivations, indexed by the pairs $(a, b)$ with $\varepsilon_a = 1$, $\varepsilon_b = -1$. We have not unfolded `dM`, the derivation in it.

## Proof

The proof is the term `maximalCompact_pseudoCoefficientData'`. The rest is bookkeeping.

## In the Lean code

The statement is in [MaximalCompactPseudoCoefficientDataStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MaximalCompactPseudoCoefficientDataStatement.lean#L6). `StKData` is in [RangeShape.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RangeShape.lean#L121), and `topP` is in [TCoefMInMMul.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/TCoefMInMMul.lean#L48). Clauses 3 and 4 say "if the trace exists, it is 1 (or 0)". They do not state that the operator is trace class.
