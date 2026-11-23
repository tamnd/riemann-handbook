---
id: exists-choice
title: Twist data at one index, by cases on the step
kind: theorem
decl: GlobalTheory.LevPrimeAll.exists_choice
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.SeesawLevelPrimeLawAllTuples
covers: 578
status: drafted
drafted_by: writer@claude
---
This lemma gives the twist data and the twist place law at one index $j$. [`lawLevelPrime_all`](/entry/law-level-prime-all/) applies it to every $j$ and makes the choices into functions of $j$. The lemma is a case split. The work is in two lemmas that it calls: one for a double step and one for the last step.

## Statement

Use the notation of [`lawLevelPrime_all`](/entry/law-level-prime-all/), with $m$ = `D.R.m`. Assume `c.Is`, `v.Is` and `ShapeOff v o`, and fix $j$.

**Lemma.** There are units $\varepsilon(i)$ of $\mathcal{O}_k$, an operator $\mathrm{op}$ on the kernels of the step $j$, reals $r(i) > 0$ and integers $e(i)$ such that $\mathrm{op}$ is supported at $P_T$ (`OpAt`), and:

1. if $j + 2(\sigma + 1) + 2 = m$, then for each tuple $t$ that satisfies `Is`, `WeilOK` and `UnrOn` at $P_T$, the double step part of the law holds at $j$, with the constant $\prod_i r(i)\, \chi(\varpi_i)^{e(i)}$ in place of $c_T(j)$ and $S_j$ built from $\varepsilon$;
2. if $j + 2 = m$, then for each such $t$ that also satisfies `UnrK` at $P_T$, the last step part holds at $j$ in the same form, for every automorphic $f$ on $T$.

## Proof

There are three cases.

1. There is $\sigma$ with $j + 2(\sigma + 1) + 2 = m$. Then `seeSawLevelPrimeLaw_doubleStep` gives the data and clause 1 for this $\sigma$. The equation fixes $\sigma$, so clause 1 holds for every $\sigma'$ that meets it. Clause 2 is empty, since $j + 2 = m$ contradicts the equation.
2. $j + 2 = m$. Then `levelPrime_law_last_two_steps_all_tuples` gives the data and clause 2. Clause 1 is empty by the case hypothesis.
3. Neither. Both clauses are empty. The proof takes $\varepsilon = 1$, the operator with no terms, $r = 1$ and $e = 0$.

## In the Lean code

The lemma is at [SeesawLevelPrimeLawAllTuples.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeesawLevelPrimeLawAllTuples.lean#L42). The two lemmas it calls are restatements in [SeeSawLevelPrimeLawDoubleStepStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawLevelPrimeLawDoubleStepStatement.lean#L6) (proved by `LevPrimeMid.lawLevelPrime_double`) and [LevelPrimeLawLastTwoStepsAllTuplesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/LevelPrimeLawLastTwoStepsAllTuplesStatement.lean#L6) (proved by `FinPl.TLastAll.main`). We have not opened those proofs. Each gives the data with the same conclusion as the matching clause here, so the lemma only sorts the cases.
