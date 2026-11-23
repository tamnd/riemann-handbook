---
id: s-weil-ex
title: Existence of the Weil representation for a unitary dual pair, as WeilEx
kind: theorem
decl: PositivityTheory.ThKW.S.weilEx
module: Development.WeilBound.ThetaLifts.Reductions.WeilPairs.WeilPairExistence.WeilEx
covers: 300
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It packages `exists_isWeil`, proved in the same file, as the statement `WeilEx`. It sits below [the step EveryCharacter of literature](/step/every-character-of-literature/). The `_k` copy is [WeilEx_k](/entry/weil-ex-k/), and [its proof entry](/entry/exists-is-weil-k/) describes the argument in detail.

## Statement

**Theorem.** Let $E/F$ be number fields with an involution $\sigma$ and base data $B$ with `B.IsGood σ`. Let $X$ be a hermitian space of signature $(r, s)$ and $W$ a skew-hermitian space of signature $(r', s')$, of dimensions $n$ and $d$. Let $M$ be a tensor model with `M.IsGood B.ψ`, and let $\chi_X, \chi_W$ be Hecke characters with `ResEtaPow` for $n$ and $d$. Then there is $\omega$ with `M.IsWeil B.ψ χX χW ω`.

This is the statement of [WeilEx_k](/entry/weil-ex-k/) with `IsGood` in place of `GoodK`.

## Proof

The proof term is `exists_isWeil`. Its type is the text of `WeilEx`, so no step is needed. The proof of `exists_isWeil` follows the eight steps in [the `_k` entry](/entry/exists-is-weil-k/). It differs only in its first step, which takes $\xi_0 \neq 0$ with $\sigma(\xi_0) = -\xi_0$ from `exists_ne_zero_conj_neg_of_cmExtension`. It passes `B.IsGood` whole to several lemmas. Of `M.IsGood` it uses only the field `rat`.

## In the Lean code

The theorem is in [WeilEx.lean](lean:Development/WeilBound/ThetaLifts/Reductions/WeilPairs/WeilPairExistence/WeilEx.lean#L49), and `exists_isWeil` is at line 21. `WeilEx` is in `TowerModels/PlaneHerm.lean` (line 31). It has the same text as `Published.WeilRepresentationExists` in `Divisors₂/WeilRepresentationExists.lean` (line 12).

A third name, `PositivityTheory.ThKW.weilEx` in `Reductions/WeilPairs/WeilEx.lean` (line 3), is this theorem again. It is used in `TheoremKSphOf.lean` (line 16), in `TheoremKOfMod.lean` (line 20) and by `UpperTheory.Lit.weilRepresentationExists_pair`.
