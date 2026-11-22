---
id: twisted-place-selmer-length-bound-of-local-duality
title: The congruence bound at the twisted places from local duality, a second name
kind: theorem
decl: GlobalTheory.T.twistedPlace_selmerLengthBound_of_localDuality
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TwistedPlaceSelmerLengthBoundOfLocalDualityStatement
covers: 1270
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the congruence bound at the twisted places](/entry/twisted-place-bound-closing/). That entry has the content. Its user is [the bound at the primes q and d from the setup](/entry/theorem-bqd-main-alt-alt/), which uses only the third conclusion.

## Statement

**Theorem.** Assume global Artin reciprocity, `BlochKatoLocal`, local Tate duality and the local Euler characteristic formula. Let $D$ be a datum with local data $HW$, $F$, $Cm$, let $r$ and $\rho$ be families of Galois representations at the places of $D$, and let $C \ge 2080$ and a polynomial $Q$ with $260 f^2 t^2 (r + t) \le Q(f, r, t)$ be given. Assume thirteen further conditions on $r$, $\rho$ and the size data. Then:

1. at the places over the primes $q$ and $d$, the local fields have the form $K_0(\sqrt{-\ell})$;
2. $q$ and $d$ are $3$ modulo $4$, and their places in the CM field have ramification index 2 and conditions on the CM type;
3. at the twisted places over $q$ and $d$, the length of the congruence module is at most an explicit bound plus Sha lengths and a Selmer length.

All three are stated in [the congruence bound at the twisted places](/entry/twisted-place-bound-closing/).

## Proof

The proof applies `GlobalTheory.TwistedPlaceBound.closing`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [TwistedPlaceSelmerLengthBoundOfLocalDualityStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistedPlaceSelmerLengthBoundOfLocalDualityStatement.lean#L12). The proof is a `first | exact ... | ...` combinator with three tries. Each try applies the same lemma. The file has `set_option maxHeartbeats 1000000` (line 11). The statement file imports the proof module (line 2) and only renames it.
