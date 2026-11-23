---
id: kernel-half-chain-numbers-any-level-prime
title: Numbers that bound the kernel chain, at any level prime (second name)
kind: theorem
decl: GlobalTheory.T.kernelHalf_chainNumbers_any_levelPrime
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KernelHalfChainNumbersAnyLevelPrimeStatement
covers: 877
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. Its statement is word for word that of [the kernel side of the chain](/entry/ker-side-chain-s/), and its proof only calls that theorem. It is step 1 of the proof of [the body of the column rows](/entry/rows-body-col-face/), where it bounds each step map of the kernel chain $Q$.

## Statement

For each real $C_Y$ there is $C \ge 0$ with the following property. Take a member with level prime $T$ and its kernel chain $Q$ (`KerChain.ofCol`). Assume the four ties, $\mu_0 = 1$, a sharp constant at $\mu_0$, `I.Ok`, `FieldOfDefinition`, `Sizes`, `SizeRowsS` $C_Y$ and `Reads`. Then `KerSide` $R$ $C$ holds for `FactorBounds` of $Q$: there are numbers with explicit bounds in $C$, $m$, $N$, $L$ and $\log T$ such that, at each infinite place $v$, each step map of $Q$ multiplies the square norm by at most $e^{t}$, for a sum $t$ of these numbers. [The kernel side of the chain](/entry/ker-side-chain-s/) lists the bounds.

## Proof

The proof is one tactic line:

```
first | exact @GlobalTheory.KernelHalfS.kerSide_chainS | ...
```

The first branch closes the goal.

## In the Lean code

The theorem is in [KernelHalfChainNumbersAnyLevelPrimeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KernelHalfChainNumbersAnyLevelPrimeStatement.lean#L10). The theorem that it renames is in [KernelHalfChainNumbersAnyLevelPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KernelHalfChainNumbersAnyLevelPrime.lean#L219).