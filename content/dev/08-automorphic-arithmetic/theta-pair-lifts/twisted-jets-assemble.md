---
id: twisted-jets-assemble
title: The jet step of the row test, restated
kind: theorem
decl: GlobalTheory.T.twisted_jets_assemble
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.TwistedJetSuccEqAssembly
covers: 1005
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`twistedJet_succ_eq_assembly`](/entry/twisted-jet-succ-eq-assembly/), which has the content. Its one user is [the five properties of the twisted theta lifts](/entry/theta-lift-row-properties-conj/), which gives its result to the lift formula `Formula2K`.

## Statement

Assume `ThetaLocalInputs`, the [record of named literature statements](/step/theta-local-inputs-def/), and the statement `SumOKK` that the finite sums of the row test are meaningful. Then `StepJets` holds: for all large admissible choices, each finite combination of periods is a fixed multiple of a finite sum over classes. The [entry of the main theorem](/entry/twisted-jet-succ-eq-assembly/) gives the exact form.

## Proof

The statement is the same as that of `twistedJet_succ_eq_assembly`, and the proof applies it.

## In the Lean code

The theorem is in [TwistedJetSuccEqAssembly.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedJetSuccEqAssembly.lean#L31). The proof is

```
first | exact @_root_.GlobalTheory.RowClaim.JetsAssembly.twistedJet_succ_eq_assembly | ...
```

The two theorems have the same type, so the first branch closes the goal.
