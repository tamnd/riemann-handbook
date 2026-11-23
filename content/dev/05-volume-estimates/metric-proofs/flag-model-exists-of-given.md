---
id: flag-model-exists-of-given
title: Flag models over a Hodge component, the statement form
kind: theorem
decl: GlobalTheory.T.flag_model_exists_of_given
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.FlagModelExistsOfGivenStatement
covers: 413
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states that each Hodge component of a unitary Shimura variety has a flag model, and its proof applies [flag models over a Hodge component](/entry/flag-model-exists/), where the real content is. Its one user is [the tie lemma](/entry/tie-of/), which turns the flag model into the square systems that feed [the swap relation from seven statements](/entry/good-tower-antisymmetry-of/).

## Statement

$\mathrm{Given} \Rightarrow \mathrm{FlagModelExists}$. Here $\mathrm{Given}$ is the bundle `Top.Given` of the volume branch, which we do not unfold. $\mathrm{FlagModelExists}$ is stated in full in [flag models over a Hodge component](/entry/flag-model-exists/). In short: from a Hodge component $\mathfrak{M}$ over a point $x_0$ with arithmetic dimension $n + 1$ and degree $d$, it builds a flag model with a flag of degree $d$ over a point $y$ with arithmetic dimension $n + |\Psi|\bigl(\binom{p}{2} + \binom{q}{2}\bigr) + 1$.

## Proof

The proof is `first | exact @GlobalTheory.CompanionTheory.Ar.PB.FMX.flagModelExists | ...`. It applies the theorem with the same statement.

## In the Lean code

The theorem is in [FlagModelExistsOfGivenStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/FlagModelExistsOfGivenStatement.lean#L9). Its user is `tie_of` in [ChooseTwoAdd.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/ChooseTwoAdd.lean#L65).

The hypothesis $\mathrm{Given}$ is not used. The proof of `flagModelExists` introduces it with no name and never refers to it. So the statement is true with no hypothesis, and $\mathrm{Given}$ only matches the form of the other statements of `tie_of`.
