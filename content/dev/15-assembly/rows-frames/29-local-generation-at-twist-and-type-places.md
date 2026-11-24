---
title: Local generation at twist and type places
decls:
  - GlobalTheory.T.localGeneration_thetaFunctions_twistPlace
  - GlobalTheory.DownLift.GenTwist.step_twist
  - GlobalTheory.T.local_generation_thetaFun_at_type_prime
  - GlobalTheory.DownLift.GenSplit.gen_at_type_prime
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local generation at twist and type places

This section proves two of the four local steps of [the reduction of Section 28](/entry/gen-of-type-clean/): the step at a place below a twist prime and the step at a place below a type prime. In both cases the place $v$ of $F$ splits in $E$. So at $v$ the unitary groups become general linear groups, and the Weil representation has a Schrödinger model on functions of matrices over $F_v$. The proofs reduce the global statement to a statement about such functions.

### The local step

We keep the notation of Section 28: the real datum $R$ with face $F$, the step $i$, the index $t$, the hermitian spaces $V$ and $W$, the Weil representation $\omega$, the theta vector $v$ and the Heisenberg action $\rho$. Let $S$ be a finite set of finite places of $F$ and $v \in S$. Let $\mathrm{Gen}(S \setminus \{v\})$ be the span of the translates $\omega(1, g) f'$ with $g \in U(W)(\mathbb{A})$ and $f'$ satisfying $\mathrm{Off}$, $\mathrm{Type}$ and $\mathrm{Clean}$ for $S \setminus \{v\}$.

The *type set* of $R$ is a finite set of primes of $E$ over the type primes, and for each index $t$ the *twist set* of $t$ is a finite set of primes of $E$ where the theta vector carries a twist character $\xi_t$. All these primes lie over places of $F$ that split in $E$. A prime $\mathfrak{P}$ of $E$ lies *over* $v$ if it lies over the prime of $F$ at $v$.

**Theorem 7.29.1 (Local generation at a twist place).** Assume the given conditions on $(R, F)$ and that $\omega$ is a full Weil representation. Let $v \in S$, assume that no prime of the type set lies over $v$, and that some prime $\mathfrak{P}$ of the twist set of $t$ lies over $v$. Let $f$ satisfy $\mathrm{Type}(S)$, $\mathrm{Clean}(S)$ and $\mathrm{Off}(S)$. Then $f \in \mathrm{Gen}(S \setminus \{v\})$.

Lean: `GlobalTheory.T.localGeneration_thetaFunctions_twistPlace` (also `GlobalTheory.DownLift.GenTwist.step_twist`).

**Theorem 7.29.2 (Local generation at a type prime).** Assume the given conditions on $(R, F)$ and that $\omega$ is a full Weil representation. Let $v \in S$, and assume that some prime $\mathfrak{P}$ of the type set lies over $v$. Let $f$ satisfy $\mathrm{Type}(S)$, $\mathrm{Clean}(S)$ and $\mathrm{Off}(S)$. Then $f \in \mathrm{Gen}(S \setminus \{v\})$.

Lean: `GlobalTheory.T.local_generation_thetaFun_at_type_prime` (also `GlobalTheory.DownLift.GenSplit.gen_at_type_prime`).

The order of the two cases in Section 28 explains the hypotheses: the type case is tried first, so the twist case may assume that no type prime lies over $v$.

### The shape at a split place

Let $v$ split in $E$, with the primes $\mathfrak{P}$ and $\bar{\mathfrak{P}}$ of $E$ over it. Then there is a *split idempotent* $e$ of the adeles of $E$, with $e\, \bar{e} = 0$ and $e + \bar{e}$ the idempotent $\varepsilon_v$ of the place $v$, such that $e$ projects to the component at $\mathfrak{P}$. The points $x$ of the matrix space with $x = \bar{e}\, x$ form the *half* at $v$. In the Lean code the split idempotents and the places are matched by a dictionary.

The Heisenberg group acts on theta functions, and the *invariant forms* $\ell$ at $e$ are the linear forms on functions that are invariant under the Heisenberg elements away from the half. Two theta functions $f_1, f_2$ are equal if $\ell(\rho(x) f_1) = \ell(\rho(x) f_2)$ for every invariant form $\ell$ and every $x$ in the half. So a theta function $f$ is determined by the functions
$$\Phi_\ell(X) = \ell\bigl(\rho(\sigma(X)) f\bigr), \qquad X \in M_{(r+t) \times r}(F_v),$$
where $\sigma$ is a section from matrices over $F_v$ to the half. These are the *Schrödinger functions* of $f$ at $v$. The groups $U(V)(F_v)$ and $U(W)(F_v)$ act on them through general linear groups over $F_v$.

### Proof at a type prime

*Proof.* Let $\mathfrak{P}$ be a prime of the type set over $v$, $e$ its split idempotent, and $\varpi$ a uniformizer of $\mathcal{O}_v$.

1. The level and Schrödinger bound: there is $N$ such that each $\Phi_\ell$ is supported on $\varpi^{-N} M(\mathcal{O}_v)$ and is invariant under translation by $\varpi^N M(\mathcal{O}_v)$. So each $\Phi_\ell$ is a Schwartz-Bruhat function.
2. By $\mathrm{Type}(S)$, each $\Phi_\ell$ is invariant under a congruence subgroup of $\mathrm{GL}_r(\mathcal{O}_v)$, acting through the level character at the type prime.
3. By $\mathrm{Clean}(S)$, the averages of each $\Phi_\ell$ over the hyperplanes of the level vanish.
4. For $g \in \mathrm{GL}_r(F_v)$, put
$$\mathrm{Tr}(g) = \Bigl\{\, X : X g \in \begin{pmatrix} 1_r \\ 0 \end{pmatrix} + \varpi\, M_{(r+t) \times r}(\mathcal{O}_v) \,\Bigr\}.$$
A Schwartz-Bruhat function on $M_{(r+t) \times r}(F_v)$ that is invariant as in step 2 and has vanishing hyperplane averages as in step 3 vanishes off a finite union of the sets $\mathrm{Tr}(g)$. Since the bound $N$ of step 1 does not depend on $\ell$, there is one finite set $\mathcal{G}$ of matrices $g$ that works for all $\ell$, and each point of the support lies in $\mathrm{Tr}(g)$ for exactly one $g \in \mathcal{G}$.
5. By step 2, each $\Phi_\ell$ is constant on each set $\mathrm{Tr}(g)$. For each $g$ the *piece* $P_g$ of $f$ is a theta function whose Schrödinger functions are $\Phi_\ell$ times the indicator of $\mathrm{Tr}(g)$. The piece lies in $\mathrm{Gen}(S \setminus \{v\})$: it is a translate by an element of $U(W)(F_v)$ of a function with the three conditions for $S \setminus \{v\}$.
6. The theta functions $f$ and $\sum_{g \in \mathcal{G}} P_g$ have the same Schrödinger functions at every invariant form, so they are equal.

So $f = \sum_g P_g$ lies in $\mathrm{Gen}(S \setminus \{v\})$. $\square$

### Proof at a twist place

*Proof.* Let $\mathfrak{P}$ be a prime of the twist set over $v$, and $e$ its split idempotent.

1. The lattices of $V$ and $W$ are self-dual, and $\operatorname{rank} W = r \leq \operatorname{rank} V$.
2. The theta vector $v$ is a product, over the primes of the type set and of the twist set, of local vectors. Since no prime of the type set lies over $v$, only the factor at $\mathfrak{P}$ is seen at $v$. So $v$ has the *adjoint shape* at $e$: it is the product of an adjoint datum, twisted by the character $\xi_t$ at the single prime $\mathfrak{P}$, with a function that does not depend on the coordinates at $v$.
3. The local data at the half are of Schwartz-Bruhat type, from the self-dual lattices.
4. A general step at a split place with a given shape reduces the claim to the following local statement: for each invariant form $\ell$, the function $\Phi_\ell$ lies in the span of the translates of the conjugate half by the level elements.
5. The local statement holds because the twist character $\xi_t$ is nontrivial at $\mathfrak{P}$. For each level element $\kappa$ that is $1$ at every prime other than $\mathfrak{P}$, the reduction of $\kappa$ is trivial at those primes, so $\kappa$ lies in the level group of $V$ with the conditions at $\mathfrak{P}$. With $\mathrm{Type}(S)$ and $\mathrm{Clean}(S)$, these level elements act on $\Phi_\ell$ by the twist, and the Fourier analysis on the level gives the span.

So $f$ lies in $\mathrm{Gen}(S \setminus \{v\})$. $\square$

Both proofs use the same principle: at a split place a theta function is a Schwartz-Bruhat function of matrices in the Schrödinger model, the level conditions make it invariant under a congruence subgroup, and the clean condition removes the part that is not spanned by translates. This is the local form of the statement that the theta correspondence for the pair $(\mathrm{GL}_n, \mathrm{GL}_m)$ over a local field is generated by translates of vectors fixed by a congruence subgroup.

**Remark 7.29.3 (Formalization).** The relay for the twist place is at line 12 of [LocalGenerationThetaFunctionsTwistPlaceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalGenerationThetaFunctionsTwistPlaceStatement.lean#L12), and the target `step_twist` is at line 196 of [LocalGenerationThetaFunctionsTwistPlace.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalGenerationThetaFunctionsTwistPlace.lean#L196). Its helpers are `om_form` (line 57), `cross_law` (69), `omegaQ_split` (95), `idem_over` (121), `step_of_shape` (136), `law_vP` (168) and `suppIn_of_suppAt` (186). The relay for the type prime is at line 12 of [LocalGenerationThetaFunAtTypePrimeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalGenerationThetaFunAtTypePrimeStatement.lean#L12), and the target `gen_at_type_prime` is at line 532 of [LocalGenerationThetaFunAtTypePrime.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalGenerationThetaFunAtTypePrime.lean#L532), with `trSet` at line 45 and `piece` at line 407. The vanishing off finitely many sets $\mathrm{Tr}(g)$ is `GlobalTheory.parahoric_schwartz_vanish_off_translates`, and the equality of step 6 is `eq_of_forms` at line 237. Both targets take `R.FullP` as a hypothesis and do not use it (`intro ... hG _ ...`). Step 5 of the twist proof is our summary of `mem_span_translates_conjugateHalf_twistPlace`, which we did not open; the Lean proof only checks its hypotheses on the level elements.
