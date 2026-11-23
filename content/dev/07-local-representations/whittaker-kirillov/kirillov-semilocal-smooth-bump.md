---
id: kirillov-semilocal-smooth-bump
title: A vector of a cuspidal representation with a prescribed Whittaker function on the semi-local mirabolic subgroup
kind: theorem
decl: GlobalTheory.T.kirillov_semilocal_smooth_bump
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KirillovSemilocalSmoothBumpStatement
covers: 384
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the semi-local Kirillov bump](/entry/kirillov-semilocal-bump/), which states it in full and gives the reduction. It sits below [the linear independence of Satake power sums](/entry/vanish/). Three lemmas use it, among them the construction of matched Whittaker vectors for the Rankin-Selberg integral.

## Statement

The statement of [the semi-local Kirillov bump](/entry/kirillov-semilocal-bump/), word for word. In short: let $\pi$ be a [[cuspidal representation|9AZ164C298]] of $\mathrm{GL}_{m+1}$ over a totally complex field $E$, let $S$ be a finite set of finite places, and let $\varphi \in \pi$ have a Whittaker function that is not zero at some point that is trivial at the finite places outside $S$. Then each smooth function $b$ that transforms on the left by $\psi_N$, is compactly supported modulo $N$ on the semi-local mirabolic subgroup $P_S$, and is right invariant under an open subgroup at the finite places, is the Whittaker function on $P_S$ of a function $F$ in the span of $\pi$. Also $F$ keeps the invariances of $\varphi$ outside $S$ and infinity.

## Proof

The proof is `exact KirSemi.kirillov_semilocal_bump`. See [the semi-local Kirillov bump](/entry/kirillov-semilocal-bump/).

## In the Lean code

The theorem is in [KirillovSemilocalSmoothBumpStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KirillovSemilocalSmoothBumpStatement.lean#L9). The proof is a `first` combinator around `exact`. The users are in [ExistsMatchedWhittakerVectorsShintaniRelations.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsMatchedWhittakerVectorsShintaniRelations.lean#L167), [ExistsShiftedVectorShintaniFormulaRamified.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsShiftedVectorShintaniFormulaRamified.lean#L88) and [ExistsBumpShintani.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsBumpShintani.lean#L49). The words "smooth bump" in the name describe the function $b$, not the conclusion.
