---
id: record-nonempty-of-local-gap
title: A datum of the proof from local period ring data
kind: theorem
decl: Formalism.BasicNotions.Examples₂.record_nonempty_of_localGap
module: Formalism.LocalRingCardinality.SpanPowerMembership
covers: 495
status: drafted
drafted_by: writer@claude
---
This theorem turns local period ring data over the example host $H_0$ into an element of the type `D7`. It is a pass-through: it applies the construction `exampleRecord`, and the 495 declarations below it are that construction. Its one user is [`record_nonempty`](/entry/record-nonempty/), which describes `D7`, `LocalGap` and the example record.

## Statement

**Theorem.** If `LocalGap H0` is nonempty, then `D7` is nonempty.

`LocalGap H` has three fields: a `LocTheory`, that is, period rings $B$ and $B_{\mathrm{dR}}$ at each prime $\ell$; data for $A_{\inf}$ at each $\ell$; and at each $\ell$ a `LocTied` that ties these rings to the concrete rings of the Lean code. The host $H$ does not occur in the fields.

## Proof

Given $G$ in `LocalGap H0`, `nonempty_D7_of_localGap` gives the element `exampleRecord G` of `D7`. This is `exampleRecordOfData` applied to $H_0$, the prime $T_0$ and the checks on them: the type primes split in $E$, the type hypothesis `THyp`, $T_0$ is a level prime, $T_0 \ne 751, 991$, and an element $\pi_0$ of norm $T_0$ with a congruence. The checks in this file are `norm_num` on explicit numbers. The fields `loc`, `locA` and `locT` of the record are the three fields of $G$; the other uses of $G$ (`G.tame`, `G.cd`) do not depend on $G$.

## In the Lean code

The theorem is in [SpanPowerMembership.lean](lean:Formalism/LocalRingCardinality/SpanPowerMembership.lean#L51). The proof is `fun ⟨G⟩ => nonempty_D7_of_localGap G`, and `nonempty_D7_of_localGap` (line 49) is `⟨exampleRecord G⟩`. `exampleRecordOfData` is in [ExampleClassGroupCardPos.lean](lean:Formalism/LocalRingCardinality/SpanPowerMembership/ExampleClassGroupCardPos.lean#L82), which also defines `LocalGap` at line 21.

The namespace `Formalism.BasicNotions.Examples₂` and the module name `SpanPowerMembership` say nothing about this content. The same file proves the equivalence, `record_nonempty_iff_localGap`.
