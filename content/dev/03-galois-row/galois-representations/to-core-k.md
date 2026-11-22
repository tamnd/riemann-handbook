---
id: to-core-k
title: The core statement from the theta lift and the odd limit
kind: theorem
decl: UpperTheory.Gal.Int.Core.toCoreK
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.CrystallineDescent.ToCoreK
covers: 499
status: drafted
drafted_by: writer@claude
---
This theorem proves `Core` from the theta lift statement [TLiftK](/step/tlift-k-def/) and three more statements. Its user is [coreAll_of](/entry/core-all-of/), which states `Core` in words. The theorem itself is a wrapper of one line. It turns `TLiftK` into `TwoUpOK` and gives the result to the theorem `toCore`. The real work is in `toCore` and in the chain of lemmas below it, which have no entry of their own. Below it are 499 declarations.

## Statement

**Theorem.** Assume `TLiftK`. If `ClosedPhi`, `DescOffT` and `LimFinOdd` hold, then `Core` holds.

`TwoUpOK` says this. Let $E$ be a CM field such that $E/E^+$ is unramified at each finite place, $-d$ is a square in $E$ for some $d > 0$, $[E^+ : \mathbb{Q}]$ is even, and the condition `InertOK` holds. Then for each even $n \geq 1$, `TwoUp E n` holds. `InertOK` says that at each non-split place, the place below is not above $2$, has norm greater than $3$, and does not contain the different. `TwoUp E n` says that an automorphic $U$ on $U_n$ has two lifts $U_1, U_2$ to $U_{n+t}$ with $n + t$ odd, whose Satake parameters at split places are those of $U$ twisted by a character $\kappa$, plus the values of distinct algebraic characters $\psi_1, \psi_2$.

## Proof

The proof is `toCore (twoUpOK_of_k hT)`. The lemma `twoUpOK_of_k` applies `twoUpOK_of_steps` to `TLiftK` and three proved facts. In that proof the odd length is $n + t$ with $t = 2(d_0 + n) + 1$, and $d_0$ comes from `TLiftK`.

The theorem `toCore` composes these steps:

1. `limOdd_of_limFinOdd` only rewrites `Odd a` as `1 ≤ a ∧ Odd a`. This gives `LimOdd`.
2. `limU_of_limOdd` uses `ClosedPhi` to change the joint approximation clause above $\ell$ into a `PhiAt` clause. This gives `LimU`.
3. `joinU_holds` gives `CoreUd`: the result for odd $m$ at the places `UsPl d`.
4. `joinAll_holds` uses `TwoUpOK` to pass to all $n \geq 1$. This gives `AllUd`.
5. `joinGL_holds` uses `DescOffT` to pass to $\pi$ in scope `csd` with $\chi$ a power of `quadChar E`. This gives `CoreGLu`.
6. `joinUp_holds` uses `jacquetShalikaRigidity`, `gk_holds` and `quadLift` to reach all places. This gives `RowCsd`.
7. `joinEnd_holds` and `core_of_rowStarCore` end at `Core`.

We have not unfolded `JoinGL`, `JoinUp` or `JoinEnd` beyond their types.

## In the Lean code

The theorem is in [ToCoreK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineDescent/ToCoreK.lean#L7). `toCore` and the chain are in [LimOddOfLimFinOdd.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineDescent/LimOddOfLimFinOdd.lean#L61). The types of the join steps are in [PatchOneAlt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CrystallineDescent/PatchOneAlt.lean#L107). `twoUpOK_of_k` is in [TwoUpOKOfSteps.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/TwoUpOKOfSteps.lean#L33), and `TwoUpOK` in [AllCoreOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/AllCoreOf.lean#L18). The letter K in the name refers to `TLiftK`.
