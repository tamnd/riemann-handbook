---
id: conjugates-of-rational-theta-lift-from-characterisation
title: Galois conjugates of a rational theta lift, restated
kind: theorem
decl: GlobalTheory.T.conjugatesOfRationalThetaLift_from_characterisation
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ConjugatesOfRationalThetaLiftFromCharacterisatioStatement
covers: 620
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`conjRatLift5`](/entry/conj-rat-lift5/), and that entry has the real content. It proves the statement $\mathrm{ConjRatLift5}$, which is used below the step [the hypotheses are nonempty](/step/nonempty-hyps/). Below this theorem are 620 declarations; all but one are below `conjRatLift5`.

## Statement

**Theorem.** $\mathrm{ConjRatLift5}$ holds.

In short, $\mathrm{ConjRatLift5}$ says the following. Take a real datum $R$ with its finite group action, its [[theta|6WB6TKE70H]] lifts and its rational structures, and suppose the conditions that tie them together. Fix an index $i$ and a phase $ph$. Then three things hold. Each rational vector $x$ has exactly one rational form $y$ whose base embedding is $ph$ times the theta lift of $x$. For each complex embedding $\sigma$ that agrees with the base one on the field $K$, the conjugate of this lift by $\sigma$ is again a theta lift, up to a phase and a central shift. For each other $\sigma$, the inner products at $\sigma$ are the complex conjugates of those at $\bar\sigma$. The [entry for `conjRatLift5`](/entry/conj-rat-lift5/) states each part in full.

## Proof

The proof is the term `conjRatLift5`. The rest is bookkeeping.

## In the Lean code

The theorem is in [ConjugatesOfRationalThetaLiftFromCharacterisatioStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ConjugatesOfRationalThetaLiftFromCharacterisatioStatement.lean#L10). The statement is in [FormalDegreeUpperC.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FormalDegreeUpperC.lean#L101).

The proof is the tactic `first | exact @conjRatLift5 | ...`. The types are the same, so the first branch suffices. Two lemmas use this name: `liftEigenvalueLowerBound_of_weakCharacterisation` in FinitenessInputsRealDataThree.lean and `liftScalarIdentity_offFixedPlace_baseLevel` in ConjugateBaseLevelOfHoweUnramifiedCorrespondence.lean. The file name is cut short: "Characterisatio" for "Characterisation".
