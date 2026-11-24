---
title: Toral components and good lifts
decls:
  - GlobalTheory.ParaToral.toral_of_lower
  - GlobalTheory.ParaToral.toral_of_levelPara
  - GlobalTheory.LiftRows.spanP_of_given
  - GlobalTheory.GoodLift.goodMem_of_given
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Toral components and good lifts

This section proves two more inputs of [the nonemptiness of the hypotheses from unramified exponents](/entry/hypotheses-nonempty-of-unramified-exponents-alt/). The first is local: an irreducible representation of $\mathrm{GL}_n$ over a $p$-adic field that has a vector of a parahoric type is a subquotient of a principal series, so its cuspidal support consists of characters. The second is global: the downward theta lift sends good vectors to vectors that the extension map sees correctly, and this follows from a spanning statement for lowest types.

### Toral representations

Let $k$ be a nonarchimedean local field with valuation $|\cdot|$, integers $\mathcal{O}_k$ and maximal compact subgroup $K_0 = \mathrm{GL}_n(\mathcal{O}_k)$. Every irreducible smooth representation $x$ of $\mathrm{GL}_n(k)$ has a cuspidal support, a multiset of irreducible cuspidal representations of groups $\mathrm{GL}_{n_j}(k)$ with $\sum_j n_j = n$. We call $x$ *toral* if every element of its cuspidal support is a representation of $\mathrm{GL}_1(k)$, that is a character. A character $\alpha$ of $k^\times$ is *unramified* if it is trivial on $\mathcal{O}_k^\times$.

For $0 \leq m \leq n$ and $h \in K_0$, write $h_{<m}$ for the upper left $m \times m$ block of $h$. Let $K_0(m)$ be the set of $h \in K_0$ whose entries $h_{a b}$ with $a < m \leq b$ have $|h_{a b}| < 1$.

**Theorem 7.33.1 (Toral from a lower parahoric vector).** Assume the finiteness theorem of Bernstein and Zelevinsky. Let $\sigma$ be an irreducible smooth representation of $\mathrm{GL}_n(k)$, let $0 \leq m \leq n$, and let $\alpha, \beta$ be characters of $k^\times$ such that $\beta$ is unramified if $\alpha$ is. Let $u \neq 0$ be a vector with
$$\sigma(h)\, u = \alpha\bigl(\det h_{<m}\bigr)\, \beta(\det h)\, u \qquad \text{for all } h \in K_0(m).$$
Then $\sigma$ is toral.

Lean: `GlobalTheory.ParaToral.toral_of_lower`.

*Proof.* For $h \in K_0(m)$ the determinants $\det h_{<m}$ and $\det h$ are units. Let $\theta$ be the character of the diagonal torus given by $\alpha\beta$ on the first $m$ entries and $\beta$ on the others. Then the eigenvalue of $h$ on $u$ is $\theta$ evaluated on $h$, and it is $1$ if $\alpha$ is unramified.

1. Suppose $\alpha$ is unramified. Then $\beta$ is unramified, so $u$ is fixed by $K_0(m)$. Reversing the order of the indices turns $K_0(m)$ into a group that contains the Iwahori subgroup, and turns $u$ into a nonzero vector $u'$ fixed by the Iwahori subgroup. The representation $\sigma$ is admissible, by the finiteness theorem. By the theorem of Borel and Casselman, an irreducible admissible representation with a nonzero Iwahori fixed vector is a subquotient of an unramified principal series. A subquotient of a principal series induced from smooth characters is toral.
2. Suppose $\alpha$ is ramified. Then $u$ is a vector of the type $\theta$: for each $h$ in the Iwahori subgroup, $\sigma(h) u = \theta(h) u$, and the quotient $\theta_a / \theta_b$ for $a < m \leq b$ is $\alpha$, which is ramified. For such a type, an irreducible smooth representation with a nonzero vector of type $\theta$ is a subquotient of the principal series of a smooth character $\omega$ of the torus that extends $\theta$. So $\sigma$ is toral.

In both cases $\sigma$ is toral. $\square$

The two cases are the two kinds of Iwahori types: the unramified one, where the Iwahori fixed vectors detect the unramified principal series, and the ramified one, where the type of a character of the Iwahori subgroup detects the principal series of a tamely ramified character. There is a companion theorem for upper parahoric vectors, with the block conditions reversed.

### Toral local components at a split place

Let $L$ be a CM field, $L^+$ its maximal totally real subfield, and $\mathbb{A}_{L,f}$ the finite adeles. Let $S$ be an irreducible automorphic representation of $\mathrm{GL}_n(\mathbb{A}_{L,f})$ with values in the representation of an algebraic weight $a$. A *split place* $s$ is a place $v$ of $L^+$ that splits in $L$, with a chosen place $s_w$ of $L$ above it; its conjugate $\bar{s}$ has the other place above $v$. Let $J$ be an open subgroup of $\mathrm{GL}_n(\mathbb{A}_{L,f})$ with a character $\chi$ that is trivial on a congruence subgroup. The pair $(J, \chi)$ has *parahoric level* at $s_0$, of type $r$ and with a character $\xi$ of $(L^+_v)^\times$, if:

1. an element $\kappa$ that is trivial outside $v$ lies in $J$ if and only if its component at $s_0$ lies in the parahoric subgroup of block type $r$;
2. for such $\kappa$, $\chi(\kappa)$ is $\xi$ of the determinant of the diagonal block.

**Theorem 7.33.2 (Toral components at a parahoric level).** Assume the finiteness theorem of Bernstein and Zelevinsky and Zelevinsky's polynomial ring theorem. Let $S$, $J$, $\chi$ be as above, with parahoric level at $s_0$ of type $r$ and character $\xi$. Let $f \neq 0$ lie in the isotypic part of $S$ and in the type space of $(J, \chi)$. Let $s$ be a split place with the same place $v$ as $s_0$, and let $\sigma$ be the local component of $S$ at $s$. Then $\sigma$ is toral.

Lean: `GlobalTheory.ParaToral.toral_of_levelPara`.

*Proof.* From $f$ we get a local vector. There are an identification $c$ of $L_{s_w}$ with $L^+_v$ that matches the valuations and a vector $u \neq 0$ in $\sigma$ on which the parahoric subgroup at $v$ acts by the character given by $\xi$ and $\chi$. There are two cases.

1. If $s = s_0$, then $u$ is an upper parahoric vector of the theorem above, in its companion form, and $\sigma$ is toral.
2. If $s = \bar{s}_0$, the identification of the two completions goes through the conjugation, and the group $\mathrm{GL}_n$ at $s$ is identified with the group at $s_0$ by the transpose inverse. Under this map the upper block conditions become lower block conditions, and $u$ is a lower parahoric vector. By the theorem above, $\sigma$ is toral.

Since $s$ and $s_0$ have the same place $v$, one of the two cases holds. $\square$

### Spanning by lowest types

We return to the real datum $R$ with face $F$ of Section 28. For each step $i$ there is a space $W_{\mathrm{all}}(i)$ of multilinear forms in one lowest-type vector for each archimedean index $\tau$, and the *lowest-type spaces* $\mathrm{low}_\tau$. The real data satisfy the *spanning property* if, for each $i$, each element of $W_{\mathrm{all}}(i)$ that vanishes on all tuples of lowest-type vectors is zero.

**Theorem 7.33.3 (Spanning from the given conditions).** If $(R, F)$ satisfies the given conditions, then $R$ has the spanning property.

Lean: `GlobalTheory.LiftRows.spanP_of_given`.

*Proof.* Each lowest-type space $\mathrm{low}_\tau$ is nonzero, since the lowest type of the real model at $\tau$ is a nonzero subspace. If every lowest-type space has a nonzero vector, the spanning property holds. $\square$

The proof does not use the given conditions. So the spanning property holds for every real datum.

### Good vectors

For a step $i$ and an index $t$ there are two lifts of a form $y \in H_V$ to $W_{\mathrm{all}}(i)$: the lift $\theta_G(y)$ through the highest weight model, followed by its extension map $e$, and the lift $\theta_F(y)$ by the downward theta integral on lowest types. The form $y$ is *good* if its level averages are compatible with the level characters of the finite group $G$ of the datum.

**Theorem 7.33.4 (Good vectors lift correctly).** Assume the given conditions on $(R, F)$ and that $\omega$ is a full Weil representation. Then for each step $i$, each index $t$ and each good $y \in H_V$,
$$e\bigl(\theta_G(y)\bigr) = \theta_F(y).$$

Lean: `GlobalTheory.GoodLift.goodMem_of_given`.

*Proof.* Let $e_G(g)$ for $g \in G$ be the level elements of the datum, and $c(g)$ the coefficients of the central idempotent of the trivial character.

1. Each $e_G(g)$ lifts to $U(V)(\mathbb{A})$, and $y$ has a translate $y_g$ by this lift, with the same extension to the adelic group up to the action of $e_G(g)$.
2. Since $y$ is good, the extensions satisfy
$$\tilde{y} = \sum_{g \in G} c(g)\, \tilde{y}_g.$$
3. The element $e(\theta_G(y)) - \theta_F(y)$ lies in $W_{\mathrm{all}}(i)$, since both terms lie there.
4. On a tuple $v$ of lowest-type vectors, the left term is
$$\begin{aligned} e\bigl(\theta_G(y)\bigr)(v) &= \sum_{g} c(g)\, \bigl(e_G(g) \cdot \theta_F(y)\bigr)(v) \\ &= \sum_g c(g)\, \theta_F(y_g)(v) \\ &= \theta_F\Bigl(\sum_g c(g)\, y_g\Bigr)(v) = \theta_F(y)(v). \end{aligned}$$
The first equality is the formula for the extension map as an average, the second is the behaviour of $\theta_F$ under translates on lowest types, the third is linearity, and the last uses step 2, since $\theta_F$ on lowest types only depends on the extension.
5. So the difference of step 3 vanishes on all tuples of lowest-type vectors. By the spanning property it is zero.

This proves the theorem. $\square$

**Remark 7.33.5 (Formalization).** The theorems `toral_of_lower` and `toral_of_levelPara` are at lines 234 and 408 of [ToralOfIsSubquotient.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ToralOfIsSubquotient.lean#L234). The case $\alpha$ unramified uses `rv` (line 204), `exists_rv`, `GlobalTheory.SatakeExists.exists_isSubquotient_prinSeries` and `toral_of_isSubquotient` (line 193); the other case uses `HasVec (fam n m α β)` and `GlobalTheory.PsType.subquotient_prinSeries_of_hasVec`. The companion `toral_of_upper` is at line 283 and `exists_vec` at line 356. The hypothesis `ZelevinskyPolynomialRing` of `toral_of_levelPara` is not used (`intro hBZ _ ...`, line 409). `Toral` and `Good` are at line 25 of [RecTExists.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/RecTExists.lean#L25), and `LevelPara` at line 35 of [DefsLevel.lean](lean:Formalism/LocalToGlobal/GaloisLevelStructure/DefsLevel.lean#L35). The theorem `spanP_of_given` is at line 26 of [SpanPOfGiven.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SpanPOfGiven.lean#L26); it is `fun R _ _ => spanP_of_lowTNZ R (lowTNZ_holds R)` and ignores the face and the given conditions. `SpanP` is at line 36 of [ThFEquivOf.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/LevelTypeEquivalence/ThFEquivOf.lean#L36) and `LowTNZ` at line 194 of [DensLow.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/LevelTypeEquivalence/DensLow.lean#L194). The theorem `goodMem_of_given` is at line 131 of [DownwardThetaLiftPreservesGood.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DownwardThetaLiftPreservesGood.lean#L131), under `maxHeartbeats 8000000`; the hypothesis `R.FullP` is not used (`intro ... hG _ i t y hy`, line 134), and its helpers at lines 55 to 119 each use `maxHeartbeats 4000000`. `GoodMem` is at line 87 of [ParamsEx.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ParamsEx.lean#L87), and `Given` at line 28 of [RealLowestKTypeCoeffSquareIntegrable.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/RealLowestKTypeCoeffSquareIntegrable.lean#L28). The ramified case of `toral_of_lower` and the statements of Borel and Casselman are classical results that the Lean proof cites as lemmas; we did not open those lemmas.
