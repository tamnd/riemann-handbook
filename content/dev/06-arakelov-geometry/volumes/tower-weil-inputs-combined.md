---
id: tower-weil-inputs-combined
title: The chain of tower estimates (statement form)
kind: theorem
decl: GlobalTheory.T.tower_weil_inputs_combined
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.TowerWeilInputsCombinedStatement
covers: 1194
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [`chain_tower`](/entry/chain-tower/), which has the real content, and its proof applies that theorem. Its user is [the volume theorem for good root towers](/entry/volume-theorem-x-of-inputs/), which checks the seventeen properties of one good tower and passes them in.

## Statement

Assume six published inputs: the flag height statement `PB.FlagHeight`, the inputs `PB.Inputs`, the two successive minima bounds of Zhang (see [heights](/learn/arakelov/#heights)), `AntisymPerturbation.Statement` and `GrassmannianHeightZTwo.Statement`. Let $II$ be a full intersection system, $T$ a root tower, $\mathrm{frob}$ a Frobenius map, and $C, C' \geq 0$, $\mathrm{rd} \geq 1$, $L$ real numbers.

**Theorem.** If $\mathrm{frob}$ has `FrobShape` and $T$ has `Proportional`, `I1`, `I2`, `A1`, `ModelNefStatement`, `M2`, `ANef`, `I5`, `I6`, `I7`, `I8`, `Prop6`, `PropA`, `PropF` with constant $C'$, `VolEq` and `SlopeLower` with constant $C$, then $T$ has `T1`, `ThmB` and, with constant $2C + 3C' + 5$, `T2` and `MeanSlope`.

The properties are explained in [the chain of tower estimates](/entry/chain-tower/) and [the volume theorem for good root towers](/entry/volume-theorem-x-of-inputs/).

## Proof

Apply `chain_tower`.

## In the Lean code

The theorem is in [TowerWeilInputsCombinedStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/TowerWeilInputsCombinedStatement.lean#L7). The proof is the `first | exact @… | exact … | (intros; apply … <;> assumption)` pattern of the other statement files of this chapter. The name speaks of Weil, but the "Weil theorem" in this chain is `ThmW`, a bound $O(\log B / B)$ on walls of weights, and not a classical theorem of Weil.
