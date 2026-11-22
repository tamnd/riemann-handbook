---
id: hecke-int-transform-read-tie
title: Integrality, transforms and readings of Hecke operators
kind: theorem
decl: GlobalTheory.HeckeMember.heckeInt_transform_readTie
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.HeckeIntegralityStatements
covers: 1105
status: drafted
drafted_by: writer@claude
---
This theorem puts three facts about Hecke operators at split primes into one conjunction. It has no hypotheses. Its user is [the local inputs of a member](/entry/exists-hyp-n-of-geometric-galois-compat/), which takes from it three of the six parts of the series facts `SerN`. Below it are 1,105 declarations. The theorem only pairs three proofs. The content is in the lemmas that it names, which have no entries.

## Statement

Let $E$ be a CM field with a host $H$, a datum, a level $\ell$ and a coefficient system. A prime ideal $\mathfrak{P}$ of $\mathcal{O}_E$ is *split off* over $p$ if $\mathfrak{P}$ is maximal, $\mathfrak{P} + \bar{\mathfrak{P}} = \mathcal{O}_E$, $p$ is a prime in $\mathfrak{P}$, and $p$ does not divide the level number $M'$.

**Theorem.** The following three statements hold.

1. `HeckeInt`. For all such data, two integrality statements hold, for the class of good points and for all points. At each split-off prime and each place $\lambda$ not over $p$, a point $z$ that is Hecke related to the image of an integral algebraic point is integral up to units, after a finite extension of the complete discrete valuation ring. Each section with nonnegative valuations has a value at $z$ that is integral.
2. `HeckeTransform`. This is `SecTransform` and `CuspTransform`. If $1 \le p + q$, $\mathfrak{P}$ is split off, $i \le p + q$ and $n$ is even, then `HasTransform` holds at $\mathfrak{P}$, $p$, $i$ and $n$. We have not unfolded `HasTransform`. For each core with the laws `LawsM`, the Hecke operator at a split-off prime keeps the cuspidal subspace.
3. `HeckeReadTie`. For a datum $D$, a finite group, a family, a core, real data and a face, if the level character, group, family, model, theta and tie conditions hold, then a frame pin at stage $i$ gives a reading of the core at $i$ by $\kappa(i)$. We have not unfolded `FramePin` and `ReadsAt`.

## Proof

1. `HkIntegral.heckeInt` proves `HeckeInt` from the frame and value integrality for the two classes of points.
2. `ThetaTransport.thetaTransportLaw` proves a transport law for theta generators at split-off primes. `heckePointLaws_of_transport` turns it into the point laws `HeckePointLaws`: finiteness, totality, single values and detection by points. `heckeTransform_of_pointLaws` gives `SecTransform` from these laws, and `CuspTransform` by `cuspTransform`, which needs no input.
3. `HeckeReadProof.heckeReadTie` proves `HeckeReadTie` from two facts for all $D$: `splitLinearModel`, a formula for the operators of a Weil datum in a split place model, and `vacFixed`, which says that at unramified places the lattice stabilizers fix the vacuum theta function.

## In the Lean code

The theorem is in [HeckeIntegralityStatements.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HeckeIntegralityStatements.lean#L15). The lemmas:

- `heckeInt` in [IsUnitNatCastUp.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/IsUnitNatCastUp.lean#L403).
- `heckeTransform_of_pointLaws` in [HeckeTransformOfPointLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeTransformOfPointLaws.lean#L419).
- `heckePointLaws_of_transport` in [HeckePointLawsOfTransport.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckePointLawsOfTransport.lean#L245).
- `thetaTransportLaw` in [HeckeIsogenyThetaGeneratorTransport.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeIsogenyThetaGeneratorTransport.lean#L735).
- `heckeReadTie` in [HeckeReadTie.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeReadTie.lean#L34).

`HeckeInt` is in the namespace `UnusedSlot39` ([HeckeValueIntegrality.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/HeckeValueIntegrality.lean#L79)), but the proof uses it. An `example` on line 82 of that file shows that value integrality for all points gives it for good points, so the good class adds nothing to the value half.

The split-off condition is defined at least four times: `IsHeckePrime` in HeckeValueIntegrality.lean line 27, the structure `IsSplitOff` in SplitOffDetection.lean line 20, the definition `IsSplitOff` in ExistenceTori/FibrePushforward.lean line 17, and `IsHeckePrime` in HeckePrimeDetection.lean line 17. The last one writes $M' \notin \mathfrak{P}$ in place of $p \nmid M'$.

There are two theorems `heckePointLaws`: one in HeckePointLaws.lean line 10, through `heckeIsogeny_thetaGenerator_transport`, and one in HeckeIsogenyThetaGeneratorTransport.lean line 741, through `thetaTransportLaw`. `heckeReadTie` uses the first one on its line 42. This theorem builds the second one again inline on its line 19.
