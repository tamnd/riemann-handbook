---
title: Generation at the finite places
decls:
  - GlobalTheory.DownLift.GenFinite.genFin
  - GlobalTheory.T.thetaFunction_levelType_mem_span_translates
  - GlobalTheory.DownLift.GenFinite.gen_of_type_clean
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Generation at the finite places

Sections 28 to 33 prove the generation statements of the downward theta lift. They are inputs of [the nonemptiness of the hypotheses from unramified exponents](/entry/hypotheses-nonempty-of-unramified-exponents-alt/), in the first branch of [the unitary hypotheses](/proof/unitary-hypotheses/). The question is the following. A form $y$ on the larger unitary group gives a linear functional on theta functions, the downward theta integral. If it vanishes on a small explicit set of theta functions, does it vanish on all of them? This section answers the question at the finite places, Section 29 gives the local steps at two kinds of places, and Sections 30 to 32 treat the real places.

### The setting

Fix a real datum $R$ over $D$ with a face $F$, a step $i$ of the chain and an index $t$. Write $V$ and $W$ for the two hermitian spaces of step $i$, with $\operatorname{rank} W \leq \operatorname{rank} V$, and $\mathbb{A}$ for the adeles of $F$. The data give:

1. the Weil representation $\omega$ of $U(V)(\mathbb{A}) \times U(W)(\mathbb{A})$ on functions on the space of $\operatorname{rank} W \times \operatorname{rank} V$ matrices over $\mathbb{A}_E$;
2. the theta vector $v$, a theta function, and the Heisenberg action $\rho$ on functions;
3. the coefficient space $\mathcal{E}$, a finite-dimensional space with a representation of $U(V)(\mathbb{A})$;
4. for each form $y$ in the space $H_V$, an $\mathcal{E}$-valued function $\tilde{y}$ on $U(V)(\mathbb{A})$.

For a theta function $f$, a functional $l \in \mathcal{E}^*$ and $g \in U(W)(\mathbb{A})$, the *downward integral* is
$$d(y, f, l, g) = \int_{\mathcal{F}_V} \bigl(\omega(h, g) f\bigr)(0)\; l\bigl(\tilde{y}(h)\bigr)\, d\nu_V(h),$$
over a fundamental domain $\mathcal{F}_V$ for the rational points. It is linear in $f$ and in $l$.

A theta function $f$ is *of finite type* if each relation $\sum_u c_u\, \rho(u) v = 0$, where each $u$ has zero archimedean part, also holds with $f$ in place of $v$. The form $y$ has *no level character* if the averages of $l \circ \tilde{y}$ over the finite level group, weighted by the level character, vanish.

A theta function $f$ is *of level type* if the level group of $V$ acts on $f$ by the inverse of the level character. It is *clean* if each of its level averages is zero. For a finite set $S$ of finite places of $F$ there are three relative forms of these conditions:

1. $\mathrm{Off}(S)$: each relation $\sum_u c_u\, \rho(u) v = 0$, with each $u$ zero at the real places and at the places of $S$, also holds for $f$;
2. $\mathrm{Type}(S)$: the level elements $\kappa$ with $\kappa - 1$ supported in $S$ act on $f$ by the inverse of the level character;
3. $\mathrm{Clean}(S)$: the level averages of $f$ vanish for the primes over places of $S$ and for lifts supported in $S$.

For $S = \emptyset$, $\mathrm{Off}(S)$ is the condition of finite type. A function of level type that is clean satisfies $\mathrm{Type}(S)$ and $\mathrm{Clean}(S)$ for every $S$.

The hypotheses on $R$ are the *given conditions* on $(R, F)$: the core of the data, the parameters, irreducibility, the types, a guard and a gap condition on the real parameters. They come with the condition that $\omega$ is a full Weil representation, and in this section with the *unramified Howe condition* at the inert places.

### The local reduction

**Theorem 7.28.1 (Clean vectors of level type are generated).** Assume the unramified Howe condition, the given conditions on $(R, F)$, and that $\omega$ is a full Weil representation. Let $f$ be a theta function of level type that is clean. Then $f$ lies in the span of the translates $\omega(1, g) f'$, with $g \in U(W)(\mathbb{A})$ and $f'$ of finite type.

Lean: `GlobalTheory.T.thetaFunction_levelType_mem_span_translates` (also `GlobalTheory.DownLift.GenFinite.gen_of_type_clean`).

*Proof.* Let $\mathrm{Gen}(S)$ be the span of the translates $\omega(1, g) f'$ where $f'$ satisfies $\mathrm{Off}(S)$, $\mathrm{Type}(S)$ and $\mathrm{Clean}(S)$.

1. Since $f$ is a theta function, it is invariant under an open compact subgroup at almost all places. So there is a finite set $S$ of finite places with $\mathrm{Off}(S)$ for $f$. By the remark above, $f$ also has $\mathrm{Type}(S)$ and $\mathrm{Clean}(S)$.
2. Suppose the *local step* holds at each $v \in S$: each function with the three conditions for $S$ lies in $\mathrm{Gen}(S \setminus \{v\})$. Then by induction on $S$, every function with the three conditions for $S$ lies in $\mathrm{Gen}(\emptyset)$. The base case is $S = \emptyset$, with $g = 1$. In the inductive step, a translate $\omega(1, g)$ of an element of $\mathrm{Gen}(S')$ is again in $\mathrm{Gen}(S')$, since $\omega(1, g)\omega(1, g') = \omega(1, gg')$.
3. The local step at $v$ splits into four cases:
   - a prime of the type set of $R$ lies over $v$: the local generation at a type prime of Section 29;
   - otherwise, a prime of the twist set of $t$ lies over $v$: the local generation at a twist place of Section 29;
   - otherwise, if $v$ splits in $E$: the local generation at a split place away from the levels;
   - otherwise: the local generation at an inert place away from the levels, which uses the unramified Howe condition.

With the local step at each place of $S$, step 2 puts $f$ in $\mathrm{Gen}(\emptyset)$. Since $\mathrm{Off}(\emptyset)$ is the condition of finite type, this is the claim. $\square$

The induction removes one place at a time and keeps the conditions at the other places, so the local steps are independent of each other. The fourth case is the complement of the third, so it also covers the ramified places of $F$ that are not over the type set or the twist set.

### Generation at the finite places

**Theorem 7.28.2 (Generation at the finite places).** Assume the unramified Howe condition, the given conditions on $(R, F)$, and that $\omega$ is a full Weil representation. Let $y \in H_V$ have no level character, and suppose that $d(y, f, l, g) = 0$ for all $f$ of finite type, all $l \in \mathcal{E}^*$ and all $g \in U(W)(\mathbb{A})$. Then $d(y, f, l, g) = 0$ for every theta function $f$ and all $l$ and $g$.

Lean: `GlobalTheory.DownLift.GenFinite.genFin`.

*Proof.* Let $\mathcal{A}$ be the set of theta functions $f$ with $d(y, f, l, g) = 0$ for all $l$ and $g$. Since $d$ is linear in $f$, $\mathcal{A}$ is a subspace.

1. $\mathcal{A}$ contains each translate $\omega(1, g') f$ of an $f$ of finite type, since $d(y, \omega(1, g')f, l, g) = d(y, f, l, g g')$.
2. $\mathcal{A}$ contains the level averages of theta functions. This uses that $y$ has no level character: the integral of a level average against $\tilde{y}$ is an average of $l \circ \tilde{y}$ weighted by the level character, and this is zero.
3. Let $f$ be of level type. Then $f$ is in the span of the level averages and of the clean functions of level type. A clean function of level type is in the span of the translates of step 1, by the theorem above. So $f \in \mathcal{A}$.
4. $\mathcal{A}$ contains each difference $\omega(\kappa, 1) f - \chi(\kappa)^{-1} f$ with $\kappa$ in the level group. Here the integral is invariant under the level group, which acts on $\tilde{y}$ by $\chi$.
5. Each theta function is in the span of the functions of level type and these differences.

By steps 3 to 5, every theta function lies in $\mathcal{A}$. $\square$

The real half of the generation argument, for the vanishing on theta functions of finite type, is Section 30. Together they give the injectivity and type properties of the [lift of rows](/entry/lift-rows-injective-and-type-properties-of-nonvanishing/).

**Remark 7.28.3 (Formalization).** The theorem `genFin` is at line 60 of [ThetaLiftGenerationFinitePlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ThetaLiftGenerationFinitePlaces.lean#L60); its conclusion is stated as `¬ SomeLift R i t y`, that no theta function gives a nonzero downward integral. The predicates `GenFin`, `FinLike`, `NoChi` and `downInt` are in [ParamsEx.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ParamsEx.lean#L46), and `Gen`, `TypeVec`, `TypeDiff` and `AvgIm` in [HeisOAdd.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HeisOAdd.lean#L27). The relay `thetaFunction_levelType_mem_span_translates` is at line 12 of [ThetaFunctionLevelTypeMemSpanTranslatesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ThetaFunctionLevelTypeMemSpanTranslatesStatement.lean#L12), which sets `maxHeartbeats 1000000` for a proof of one line. The target `gen_of_type_clean` is at line 66 of [ThetaFunctionLevelTypeMemSpanTranslates.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ThetaFunctionLevelTypeMemSpanTranslates.lean#L66), with the induction `mem_span_gen_of_step` at line 42. The three relative conditions `LikeOff`, `TypeIn` and `CleanIn` are at line 30 of [DropPlInsert.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DropPlInsert.lean#L30). The test "$v$ splits in $E$" is that $e\, \varepsilon_v \neq 0$ for a split idempotent $e$ of the adeles of $E$; the fourth lemma is named for inert places, but it also covers the ramified places outside the type and twist sets. The unramified Howe condition is used only in that fourth case.
