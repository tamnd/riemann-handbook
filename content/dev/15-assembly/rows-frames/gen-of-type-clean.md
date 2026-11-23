---
id: gen-of-type-clean
title: Clean theta functions of level type are spans of translates of finite type
kind: theorem
decl: GlobalTheory.DownLift.GenFinite.gen_of_type_clean
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ThetaFunctionLevelTypeMemSpanTranslates
covers: 407
status: drafted
drafted_by: writer@claude
---
This theorem reduces a global generation statement for theta functions to one local step at each finite place in a finite set. It is the proof behind the second name [`thetaFunction_levelType_mem_span_translates`](/entry/theta-function-level-type-mem-span-translates/), which [`genFin`](/entry/gen-fin/) uses in step 3. The real work is in the four local lemmas that it calls.

## Statement

Use the notation of [`genFin`](/entry/gen-fin/): the Weil representation $\omega$, the theta vector $v$, the Heisenberg action $\rho$ and the theta functions of finite type.

**Theorem.** Assume `HoweUnram`, `Given R F` and `R.FullP`. Let $f$ be a theta function of level type (`TypeVec`) that is clean (`Clean`). Then $f$ lies in the span of the translates $\omega(1, g)f'$, with $g \in U(W)(\mathbb A)$ and $f'$ of finite type.

## Proof

For a finite set $S$ of finite places of $F$, the proof uses three conditions on a theta function $f$, from [DropPlInsert.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DropPlInsert.lean#L30):

- `LikeOff S`: each relation $\sum_u c_u \rho(u) v = 0$, with each $u$ zero at the real places and at the places of $S$, also holds for $f$;
- `TypeIn S`: the level elements $\kappa$ with $\kappa - 1$ supported in $S$ act on $f$ by the inverse of the level character;
- `CleanIn S`: the level averages of $f$ vanish for the primes over places in $S$ and lifts supported in $S$.

For $S = \emptyset$, `LikeOff` is the condition of finite type. `TypeVec` and `Clean` give `TypeIn S` and `CleanIn S` for each $S$.

1. `exists_places_thetaFunction_fixedVectorShape` gives a finite $S$ with `LikeOff S` for $f$.
2. `mem_span_gen_of_step` is an induction on $S$. Suppose that for each $v \in S$, each $f$ with the three conditions for $S$ lies in the span of translates $\omega(1,g)f'$ with the three conditions for $S \setminus \{v\}$. Then $f$ is in the span of translates of finite type. The base case takes $g = 1$. The inductive step uses that a translate of the span stays in the span (`transl_mem_span_gen`).
3. The local step splits into four cases by the place $v$:
   - a prime of `R.Pg` lies over $v$: `local_generation_thetaFun_at_type_prime`;
   - else a prime of `R.Q t` lies over $v$: `localGeneration_thetaFunctions_twistPlace`;
   - else $v$ splits in $E$: `thetaFunction_localGeneration_splitPlaceOffLevels`;
   - else: `thetaFunction_local_generation_inertPlace_offLevel`, which uses `HoweUnram`.

We have not opened the proofs of the four local lemmas.

## In the Lean code

The theorem is at [ThetaFunctionLevelTypeMemSpanTranslates.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ThetaFunctionLevelTypeMemSpanTranslates.lean#L66), with `mem_span_gen_of_step` at line 42.

- "$v$ splits in $E$" is the Lean test that $e \cdot \varepsilon_v \neq 0$ for some `IsSplitIdem` $e$, where $\varepsilon_v$ is the adelic idempotent of $v$. An `IsSplitIdem` is an idempotent $e$ with $e \bar e = 0$ and $e + \bar e$ the idempotent of some place.
- The fourth case is the complement of the third. Its lemma name says "inert", but ramified places of $F$ that are not over `R.Pg` or `R.Q t` also fall in it.
- `HoweUnram` is used only in the fourth case.
