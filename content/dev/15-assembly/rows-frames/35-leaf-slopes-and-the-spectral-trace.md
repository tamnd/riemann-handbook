---
title: Leaf slopes and the spectral trace
decls:
  - GlobalTheory.BigTop.Fun.LeafMMTie.leafMM_of_test
  - GlobalTheory.PsCo.SpecX.specTrace
  - GlobalTheory.PsCo.SpecX.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Leaf slopes and the spectral trace

This section proves two inputs of different kinds. The first is a bound for the largest slope of a test lattice at a leaf of the tree of indefinite forms; it is an input of [the tie of the multiplicity bounds](/entry/mm-tie-alt/). The second is the spectral side of the trace formula on the cuspidal spectrum for test functions whose archimedean components are pseudo-coefficients of discrete series; it is an input of [the unitary theory of Harish-Chandra and Langlands](/entry/unitary-theory-of-harish-chandra-langlands-alt/).

### Normalized slopes

Let $K$ be a number field, $M \subseteq K^n$ a finitely generated $\mathcal{O}_K$-submodule, and $X' = (X'_v)$ a family of positive definite hermitian matrices, one for each infinite place $v$. They make $M$ a hermitian $\mathcal{O}_K$-lattice, with a largest slope $\mu_{\max}(M)$. Its *normalized* form is
$$\mu^{\mathrm{n}}_{\max}(M) = 2\, \mu_{\max}(M) - \log 2 + \frac{\log |d_K|}{[K : \mathbb{Q}]}.$$

A *function datum* $O$ carries such $M$ and $X'$, the number $f$ of archimedean indices, integers $m$ and $r$, a family of integers $\mathrm{cl}_\tau(i)$, and a gap $\mathrm{ga}(C) \in \mathbb{N}$ for each $C$. Put
$$\begin{aligned} n_p &= (r + 1) + m (r + 5), \\ L_c &= \max_\tau\, \max\bigl(\mathrm{cl}_\tau(2) - \mathrm{cl}_\tau(k),\, 0\bigr), \\ R_p(C) &= (m + 1)\bigl(\mathrm{ga}(C) + 1\bigr) + L_c + n_p, \\ E(C) &= 4 f\, n_p\, R_p(C)\, \log\bigl(n_p\, R_p(C)\bigr). \end{aligned}$$

**Definition 7.35.1 (Leaf slope bound).** The datum $O$ satisfies the *leaf slope bound* at $C$ if $M$ is finitely generated and nonzero, $\det X'_v$ is a unit for every $v$, and $\mu^{\mathrm{n}}_{\max}(M) \leq E(C)$.

### The bound at a leaf

At a point $p$ of the tree, a *function input* $d$ gives a function datum $d.O$, a grid $G$ and a test lattice for $G$. The *highest weights* of the grid at $\tau$ are integers $w_0 \geq w_1 \geq \dots$, built from the descending enumeration of a set of half-integral weights and a shift by the index. The slope test has remaining choices $a$, and the *tie test* is a condition on $d$ and $a$.

**Theorem 7.35.2 (Leaf slope bound from the tie test).** Let $d$ be a function input at $p$, $a$ remaining choices of the slope test, and assume the tie test for $d$ and $a$. Then $d.O$ satisfies the leaf slope bound at every $C \geq 1$.

Lean: `GlobalTheory.BigTop.Fun.LeafMMTie.leafMM_of_test`.

*Proof.* Fix $C \geq 1$, and write $k$, $m$ for the ranks of the datum.

1. The rank of the grid is $n_p$. Indeed with $r = k + m - 1$,
$$\begin{aligned} (k + m) + m (k + m + 4) &= (r + 1) + m (r + 5) = n_p. \end{aligned}$$
2. The gap is monotone in $C$, so $\mathrm{ga}(C) \geq \mathrm{gap}(1)$. Then $R_p(C) \geq (m + 1)(\mathrm{ga}(C) + 1) \geq 1$.
3. The weights of the grid at $\tau$ in level $0$ lie between $v_k - \tfrac12$ and $a_0 = v_2 + \tfrac12 + (m + 1)\, \mathrm{gap}$, where $v_i$ are the parameters of the Harish-Chandra datum at $\tau$. Each weight comes from a top, from the half cloud, or from a block between two levels, and each case is checked from the monotonicity of $v$ and of the levels $a_i$.
4. So for all $i$ and $j$,
$$\begin{aligned} w_i - w_j &\leq (v_2 - v_k) + 1 + (m + 1)\, \mathrm{gap}(1) + n_p \\ &\leq L_c + (m + 1)\bigl(\mathrm{ga}(C) + 1\bigr) + n_p = R_p(C), \end{aligned}$$
since $v_2 - v_k \leq L_c$ and $\mathrm{gap}(1) + 1 \leq \mathrm{ga}(C) + 1$. So the highest weights have spread at most $R_p(C)$.
5. The bound for the largest slope of a grid test lattice applies. It holds whenever the slope bound for test lattices holds, which it does, for a conjugate infinite place $v_0$ of the field of the datum, for $R \geq 1$, and for highest weights of spread at most $R$. It gives that the test lattice is finitely generated, nonzero, with unit determinants, and with normalized largest slope at most the bound $B(f, n_p, R)$.
6. With $R = R_p(C)$, the rank $n_p$ and $f$ the number of archimedean indices, $B(f, n_p, R_p(C))$ is $E(C)$.

This proves the theorem. $\square$

The constant $E(C)$ has the shape of the classical bound for the largest slope of a lattice spanned by vectors of controlled height: a rank factor $n_p$, a weight spread $R_p(C)$ and a logarithm of their product. The tie test is what makes the test lattice a grid test lattice of the right kind.

### The spectral side of the trace formula

Let $D$ be a datum, $V$ a hermitian space and $G = U(V)$. Let $f = f_\infty \otimes f_f$ be a test function: at each archimedean place $f_\infty$ is a pseudo-coefficient of the discrete series of a model $M$, and $f_f$ is a finite pure tensor, with the conditions of a test datum. For an irreducible admissible representation $\sigma$ of $G(\mathbb{A}_f)$, let $m(\sigma)$ be the multiplicity in the cuspidal spectrum of the representations whose finite part is $\sigma$ and whose archimedean components are the discrete series of $M$.

**Definition 7.35.3 (Spectral trace statement).** The *spectral trace statement* says: for every test function $f$ as above, every Haar measure $\nu$ on $G(\mathbb{A}_f)$ of the finite measures, and every finite family $\sigma_1, \dots, \sigma_n$ of pairwise inequivalent irreducible admissible representations such that every irreducible admissible $\sigma$ with $m(\sigma) \neq 0$ and $\sigma(f_f) \neq 0$ is equivalent to some $\sigma_i$, if $c_i$ is the trace of $\sigma_i(f_f)$, then the operator $R(f)$ on the cuspidal spectrum is trace class with
$$\operatorname{tr} R(f) = \sum_{i = 1}^{n} m(\sigma_i)\, c_i.$$

**Theorem 7.35.4 (The spectral trace).** Assume the structural statements on irreducible subrepresentations, on components, on compactness of cuspidal operators and on admissibility, the classification of discrete series, the trace class property of cusp forms, the vanishing of radical integrals of cuspidal operators, and the vanishing of parabolic constant terms. Then the spectral trace statement holds.

Lean: `GlobalTheory.PsCo.SpecX.specTrace` (also `GlobalTheory.PsCo.SpecX.main`).

The theorem `main` supplies the structural statements, the vanishing of radical integrals and of constant terms, and keeps the classification of discrete series and the trace class property of cusp forms as hypotheses.

*Proof.* We follow the Lean proof.

1. *Discrete series components.* Let $\pi$ be an irreducible unitary representation of $G(\mathbb{A})$ with $\operatorname{tr} \pi(f) = c \neq 0$. At each archimedean $\tau$ the operator $\pi(f)$ is $\pi_\tau(f_\tau) \circ Q$ for an operator $Q$ commuting with $G_\tau$. Since $c \neq 0$, $\pi_\tau(f_\tau) \neq 0$, and $\pi$ restricted to $G_\tau$ has an irreducible subrepresentation $\delta$ in the isotypic part where $f_\tau$ acts. If $\operatorname{tr} \delta(f_\tau) = 0$, the trace of $\pi(f)$ would vanish, by the vanishing of traces on an isotypic part. So $\operatorname{tr} \delta(f_\tau) \neq 0$, and the pseudo-coefficient property of $f_\tau$ forces $\delta$ to be the discrete series of $M$ at $\tau$.
2. *Finite parts.* If in addition $\pi(g)$ is compact for all $g$, then the finite part $\sigma$ of $\pi$ is irreducible and admissible, $\pi$ is the completion of $\sigma$ tensored with the discrete series of $M$, and $\operatorname{tr} \sigma(f_f) = c$.
3. *The sum over the dual.* The cuspidal operator $R(f)$ is trace class, and its trace is the sum over the unitary dual of $m_{\mathrm{cusp}}(x) \operatorname{tr} x(f)$.
4. *Matching.* Match $x$ in the dual with the index $i$ if $x$ is a copy of $\sigma_i$ tensored with the discrete series of $M$. A term with $m_{\mathrm{cusp}}(x) \neq 0$ and $\operatorname{tr} x(f) \neq 0$ matches some $i$, by steps 1 and 2 and the covering hypothesis. Each $i$ with $m(\sigma_i) \neq 0$ matches some $x$, the completion of $\sigma_i$. Matched pairs have the same multiplicity and $\operatorname{tr} x(f) = c_i$. Two indices matched with the same $x$ are equal, since the $\sigma_i$ are pairwise inequivalent and two copies are unitarily equivalent if and only if their finite parts are equivalent. Two elements $x, y$ matched with the same $i$ are equal for the same reason.
5. A sum indexed by a set with such a bijective matching on the nonzero terms equals the sum over the matched indices. This gives $\operatorname{tr} R(f) = \sum_i m(\sigma_i) c_i$.

This proves the theorem. $\square$

**Remark 7.35.5 (Formalization).** The theorem `leafMM_of_test` is at line 94 of [MultiplicityAtFittedPoints.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MultiplicityAtFittedPoints.lean#L94); step 1 is `np_eq` (line 82), steps 3 and 4 are `weightX_zero_bounds` and `La_sub_le` (line 61), and its user `mm_tie` is at line 142. `LeafMM` is at line 158 of [FunctionalLowerBoundOfConditionsNumeric.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/FunctionalLowerBoundOfConditionsNumeric.lean#L158), with `Rp` at line 114 and `EMM` at line 116, and `muMaxDef` is at line 67 of [StatementPl.lean](lean:Formalism/HarderNarasimhan/StatementPl.lean#L67). Step 5 is `IsTestLat.gridTestLattice_largestSlope_bound` at line 217 of [GridTestLatticeLargestSlopeBound.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/GridTestLatticeLargestSlopeBound.lean#L217), applied with `TestLat.slope_holds`. The theorems `specTrace` and `main` are at lines 68 and 114 of [HasDSComp.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasDSComp.lean#L68), with `hasDSComp` (step 1) at line 26 and `copyFinDS` (step 2) at line 53. In this file `hasDSComp` and `copyFinDS` take two hypotheses of type `True`, and `specTrace` takes two more; `main` passes `trivial` for them. The file [HasDSComp.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FlatHermitianReps/HasDSComp.lean#L23) under `WeilBound` has the same three theorems, at lines 23, 50 and 65, where these places hold `HarishChandraCharacters` and `PseudoCoeffSeparation`. So the version used here has dropped the two hypotheses that the archimedean trace step of step 1 needed in the other version. `SpecTraceX` is at line 244 of [TestFnConstTermVanishX.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/TestFnConstTermVanishX.lean#L244), `HasDSComp` and `IsCopyFinDS` at lines 271 and 289 of [ForallEventuallyFinLocIff.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ForallEventuallyFinLocIff.lean#L271), and `mCuspDS` at line 103 of [MemL2OfAutomorphicEmbedding.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/MemL2OfAutomorphicEmbedding.lean#L103). The facts used in steps 1 to 4, such as the vanishing of traces on an isotypic part and the criterion for unitary equivalence, are cited lemmas; we did not open them.
