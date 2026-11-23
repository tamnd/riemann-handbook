---
id: isotropic-flag-probability-bound-of-volume-ratio
title: The flag measure bound from the volume step, a second name
kind: theorem
decl: GlobalTheory.T.isotropicFlagProbabilityBound_of_volumeRatio
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.IsotropicFlagProbabilityBoundOfVolumeRatioStatement
covers: 881
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the flag measure bound](/entry/flag-measure-bound/). That entry has the content. [The counting theorem from the volume step](/entry/counting-theorem-of-volume-step/) uses it to bound the measure of the rare flag set. The lemma `nonzeroFlagBound` uses it too: it sums the bound over all flag types to get `NonzeroFlagBound`.

## Statement

**Theorem.** `VolumeStep` implies `FlagMeasureBound`.

`VolumeStep` is the volume recursion stated in [the counting theorem from the volume step](/entry/counting-theorem-of-volume-step/). `FlagMeasureBound` says: in a fundamental domain for $G(F)$ in $G(\mathbb{A})$, the points whose lattice has a filtration of type $(j, \tau)$ with $\tau \in B$ have relative measure at most $\kappa(E,p,q,j) \int_B \mathrm{dens}(\tau)\, d\tau$. The set, the constant $\kappa$ and the density are defined in [the flag measure bound](/entry/flag-measure-bound/).

## Proof

The proof applies `GlobalTheory.FlagMeas.Bound.flagMeasureBound`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [IsotropicFlagProbabilityBoundOfVolumeRatioStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/IsotropicFlagProbabilityBoundOfVolumeRatioStatement.lean#L6). The proof is a `first | exact ... | ...` combinator with three tries, and each try applies the same lemma. The file sets `maxHeartbeats 1000000`, which a one-line proof does not need. The word "probability" in the name is the ratio $\mu(A \cap \Omega)/\mu(\Omega)$ for a fundamental domain $\Omega$. The word "isotropic" is not in the statement: the filtration of the lattice is isotropic (the lemma `exists_isSatFlag` proves this), but `FlagMeasureBound` does not say so.
