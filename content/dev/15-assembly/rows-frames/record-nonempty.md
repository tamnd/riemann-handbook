---
id: record-nonempty
title: The datum of the proof has an example
kind: theorem
decl: GlobalTheory.MemLoc.record_nonempty
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalGapNonemptyAndRecordNonempty
covers: 499
status: drafted
drafted_by: writer@claude
---
This theorem says that the type `D7` has an element. Many statements of this volume quantify over `D7`. Its only user is [`exists_positions_global`](/entry/exists-positions-global/), below [`wach_lattices`](/entry/wach-lattices/). That proof takes an element $D$ of `D7` and keeps only its local part: the period rings at each prime.

## Statement

**Theorem.** `Nonempty D7`.

`D7` is a structure with many fields. Among them are the ranks, a host with number fields $F \subset E$ and a complex conjugation on $E$, a family of hermitian spaces, the row data with a number field $L$, Harish-Chandra parameters, embeddings of $E$ into $L$, and three fields `loc`, `locA` and `locT`. These three give, at each prime $\ell$:

- `loc ℓ`, a `LocPrime ℓ`: rings $B$ and $B_{\mathrm{dR}}$ over $\mathbb Q_\ell$ with an action of $G_{\mathbb Q_\ell}$, a Frobenius on $B$, a map $B \to B_{\mathrm{dR}}$, an element $t$, a cyclotomic character and a filtration on $B_{\mathrm{dR}}$;
- `locA ℓ`, a `LocAinf ℓ`: data for $A_{\inf}$, which we have not unfolded;
- `locT ℓ`, a `LocTied`: ring isomorphisms of $B$ and $B_{\mathrm{dR}}$ with the concrete rings `Per.Bcris ℓ` and `Per.BdR ℓ` that respect the Galois action, the Frobenius, the filtration, the element $t$ and the map from $A_{\inf}$.

So `locT` ties the abstract period rings to the [[period rings of Fontaine|K6HW8YWCQJ]] built in the Lean code.

## Proof

1. `exists_locTheory_tied` gives a `LocPrime`, a `LocAinf` and a `LocTied` at every prime. It chooses them prime by prime from `exists_locPrime_tied`, which builds them from a core `nonempty_core ℓ`. This makes `localGap_nonempty`: the structure `LocalGap H` (exactly these three fields) has an element for every host $H$.
2. [`record_nonempty_of_localGap`](/entry/record-nonempty-of-local-gap/) turns a `LocalGap` over the fixed example host $H_0$ into an element `exampleRecord` of `D7`. The other fields are built from $H_0$ and an explicit prime $T_0$ of 116 digits. The host $H_0$ uses the primes $571$, $599$, $751$, $991$, $413718278401$ and $603339156001$, and the checks on them are done by `norm_num` and `decide`. The rows are `toyRowsOfNumberField` and the member data is `trivialMember`.

## In the Lean code

The theorem is in [LocalGapNonemptyAndRecordNonempty.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalGapNonemptyAndRecordNonempty.lean#L14). The proof is one line, `record_nonempty_of_localGap (localGap_nonempty _)`. `D7` is in [RhoDetPrimeEqMuTildeMulChiPow.lean](lean:Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean#L76), `LocalGap` in [ExampleClassGroupCardPos.lean](lean:Formalism/LocalRingCardinality/SpanPowerMembership/ExampleClassGroupCardPos.lean#L21), `LocTied` in [LocTied.lean](lean:Formalism/LocalRingCardinality/AdicCompletionLocal/LocTied.lean#L11), and the example record in [SpanPowerMembership.lean](lean:Formalism/LocalRingCardinality/SpanPowerMembership.lean#L46). The same file proves `record_nonempty_iff_localGap`: `D7` is nonempty if and only if `LocalGap H0` is.

So a statement "for all $D$ in `D7`" is not vacuous. The theorem says nothing about a particular $D$.

The use is roundabout. At [ExistsSlotsGlobal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSlotsGlobal.lean#L279), `exists_positions_global` builds a whole `D7` and then uses only `D.loc`, `D.locA` and `D.locT`. Step 1 alone gives these three. Of the 499 declarations below this theorem, 495 are below `record_nonempty_of_localGap`, that is, the example host and record; that user does not need them.
