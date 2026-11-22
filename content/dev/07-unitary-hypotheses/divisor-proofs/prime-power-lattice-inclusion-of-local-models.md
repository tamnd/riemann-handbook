---
id: prime-power-lattice-inclusion-of-local-models
title: A prime power lattice inclusion from local models (restatement)
kind: theorem
decl: GlobalTheory.T.primePowerLatticeInclusion_of_localModels
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.PrimePowerLatticeInclusionOfLocalModelsStatement
covers: 1051
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [the inclusion from local models](/entry/l-incl-of-models/), under a second name. The real content is in that entry. Its only user is [the bound on the lattice exponent](/entry/jexp-u-le-jrec7/), in its case inside the range.

## Statement

Let $w$ be a finite place of a number field $K$, and $p$ its residue characteristic. Let $\Lambda_\nabla$ and $\Lambda_\Delta$ be the two lattices of a block datum $B$, and $\mathrm{LIncl}(J)$ the inclusion $p^J \Lambda_\nabla \subseteq (\Lambda_\Delta)_{(w)}$. Let $(P, W)$ be parameters and a weight datum with `NumOk`, and $c_W(p)$ the coarse weight bound of $W$ at $p$. All of these are defined in [the inclusion from local models](/entry/l-incl-of-models/).

**Theorem.** Suppose that $p$ is prime and in the range of $W$. Let $\mathrm{fr}, \mathrm{cj}$ be Frobenius data and $(X_i)$ Hida settings that cover $B$ at $w$ (`Covers`). Suppose that for each $i$, $p$ is not a unit in $O_i$ and `WInputsLink` holds for $X_i$, $p$ and $W$ with its Frobenius data replaced by $\mathrm{fr}, \mathrm{cj}$. Then $\mathrm{LIncl}(c_W(p))$ holds.

## Proof

The statement is the statement of `GlobalTheory.ExpTie.lIncl_of_models`, word for word. The proof applies that theorem.

## In the Lean code

The theorem is in [PrimePowerLatticeInclusionOfLocalModelsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PrimePowerLatticeInclusionOfLocalModelsStatement.lean#L6). The proof is the tactic

```
first | exact @GlobalTheory.ExpTie.lIncl_of_models | exact GlobalTheory.ExpTie.lIncl_of_models | (intros; apply GlobalTheory.ExpTie.lIncl_of_models <;> assumption)
```

It tries three ways to apply the same theorem. The two statements have the same text, so the first way should be enough. We did not run Lean to see which way succeeds. The file also sets `maxHeartbeats` to 1000000 for this one line. As in `lIncl_of_models`, the hypothesis that $p$ is prime always holds, by `plc_prime`.
