---
id: siegel-kernel-bounded-representable-of-coprime
title: Siegel moduli with bounded polarization kernel are representable (statement form)
kind: theorem
decl: GlobalTheory.T.siegelKernelBoundedRepresentable_of_coprime
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SiegelKernelBoundedRepresentableOfCoprimeStatement
covers: 1049
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the representability of Siegel moduli with kernel killed by $d$](/entry/sd-rep-of-coprime/), which has the real content. Its one user is [the quasi-projective representing family](/entry/exists-rep-fam-qproj/), which applies it with $h = \lfloor \operatorname{rank}\Lambda/2 \rfloor$, an odd prime $M$ and the integer $e$ of the datum.

## Statement

Use the Siegel objects of genus $h$ and level $M$ over $B_M = \mathbb{Z}[\zeta_M, 1/M]$, and the condition "of kernel $d$", from [the entry with the proof](/entry/sd-rep-of-coprime/).

**Theorem.** Let $h \geq 1$, $M \geq 3$ odd, $d \geq 1$ and $\gcd(M, d) = 1$. Then there is a scheme $X$, quasi-projective over $B_M$ with $d$ a unit on $X$, and a Siegel object $u$ of kernel $d$ over $X$, such that each Siegel object of kernel $d$ over a scheme $S$ on which $d$ is a unit is the pullback of $u$ along a unique map $S \to X$.

## Proof

The statement is the same as that of `GlobalTheory.UPel.HT.sdRep_of_coprime`, and the proof applies it.

## In the Lean code

The theorem is in [SiegelKernelBoundedRepresentableOfCoprimeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelKernelBoundedRepresentableOfCoprimeStatement.lean#L7). The conclusion is `SDRep h M d`, defined in [TwoLeFinrankLa.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwoLeFinrankLa.lean#L32). The proof is `first | exact @GlobalTheory.UPel.HT.sdRep_of_coprime | ...`, a tactic that tries the alias in three forms.
