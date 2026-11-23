---
id: see-saw-iterated-integral-law-at-twist-of-factorisation
title: The iterated integral law for a pinned tuple, second name
kind: theorem
decl: GlobalTheory.T.seeSawIteratedIntegralLaw_at_twist_of_factorisation
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.SeeSawIteratedIntegralLawAtTwistOfFactorisationStatement
covers: 636
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the iterated integral law of a pinned tuple](/entry/q-law-of-pin/). The statement is the same, and the proof only applies that theorem. The real content is there and in [the law for one character](/entry/one-chart/). The theorem is used in [the laws for a rescaled pinned tuple](/entry/laws-of-pin-resc/), which gives `QLaw` for a pinned tuple $w_0$ and then moves it to a rescaled tuple.

## Statement

Fix a datum $D$, a common datum $c$, level data $v$, a tuple $t$ and a decorated tuple $w$ over $t$, with the names of [the parent entry](/entry/laws-of-pin-resc/).

**Theorem.** If $c$, $t$ and $v$ satisfy `Is`, $v$ satisfies `WeilOK` for $t$, and $w$ is pinned (`QPin v w`), then `QLaw v w` holds.

The identity `QLaw v w` is written out in [the source entry](/entry/q-law-of-pin/).

## Proof

The proof is one line. It applies `GlobalTheory.QLawPf.qLaw_of_pin` with the same arguments.

## In the Lean code

The theorem is in [SeeSawIteratedIntegralLawAtTwistOfFactorisationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawIteratedIntegralLawAtTwistOfFactorisationStatement.lean#L12). Its proof is

```
first | exact @GlobalTheory.QLawPf.qLaw_of_pin | ...
```

The hypothesis `t.Is` is in the statement, but the source theorem never uses it. The name speaks of a "factorisation" at the "twist". In the statement, the factorisation is the pin `QPin`: the coefficients of $w$ are convolution products of local data at finitely many split places.
