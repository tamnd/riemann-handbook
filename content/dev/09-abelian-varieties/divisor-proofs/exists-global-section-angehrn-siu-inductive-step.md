---
id: exists-global-section-angehrn-siu-inductive-step
title: The inductive step of Angehrn-Siu, statement form
kind: theorem
decl: GlobalTheory.T.exists_global_section_angehrnSiu_inductive_step
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsGlobalSectionAngehrnSiuInductiveStepStatement
covers: 550
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`exists_global_step`](/entry/exists-global-step/). It has the same statement, and its proof applies that theorem. It has two users, `GlobalTheory.AmpleStep.exists_divisor` and `GlobalTheory.PairStep.exists_step_divisor`, in the files ExistsDivisorNonKltPointsNumericallyMultiple.lean and ExistsDivisorNonKltAtPointsNotContainingCentre.lean. In the dominator tree of the proof, its parent is [EveryCharacter from the literature](/step/every-character-of-literature/).

## Statement

Let $X$ be a normal projective variety over $\mathbb{C}$ with a klt pair $(X, \Delta)$, $A$ ample, $D$ effective $\mathbb{Q}$-Cartier, $Z = \overline{\{z\}}$ of dimension $k \geq 1$ equal to $X$ or a non-klt centre of $(X, \Delta + D)$, $P \subseteq Z$ finite and $h > 0$ with $|P| \, k^k < h^k (A^k \cdot Z)$. Assume `Published.Principalisation`.

**Theorem.** For each $l_0$ there are $l \geq l_0$ with $l > h$, a section $f_0$ of $\mathcal{O}(lA)$ that generates at $z$, and $\delta_0 \in (0, 1]$, such that for each section $u$ of $\mathcal{O}(lA)$ that vanishes at $z$, each $\delta \in [0, \delta_0]$ and each $x \in P$, the pair $\Delta + (1 - \delta) D + \tfrac{h}{l} \operatorname{div}(f_0 + u)$ is not klt at $x$.

## Proof

The proof is `GlobalTheory.PairStep.exists_global_step`, applied to all the arguments. The content, and the precise form of each hypothesis, are in [`exists_global_step`](/entry/exists-global-step/).

## In the Lean code

The theorem is at [ExistsGlobalSectionAngehrnSiuInductiveStepStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsGlobalSectionAngehrnSiuInductiveStepStatement.lean#L14). The proof is the tactic `first | exact @GlobalTheory.PairStep.exists_global_step | ...`. The two statements are written in the same words.

The klt hypothesis on $(X, \Delta)$ is part of the statement, but the proof of `exists_global_step` does not use it. Both callers pass it on.
