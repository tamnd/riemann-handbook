---
title: The field of the bottom class sums
decls:
  - GlobalTheory.RowEx.bottomField_isNumberField
  - GlobalTheory.RowEx.BotField.sums_mem_bottomField
  - GlobalTheory.T.bottom_classSums_algebraic
  - GlobalTheory.BotAlgI.classSums_isAlgebraic
  - GlobalTheory.BotAlgI.classSum_kernel_isAlgebraic
  - GlobalTheory.T.bottom_twistedClassSums_algebraic
  - GlobalTheory.BotAlgI'.twistedClassSums_isAlgebraic
  - GlobalTheory.T.bottomClassSum_eq_formula
  - GlobalTheory.BotFormulaI'.bottomClassSum_formula
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The field of the bottom class sums

The rationality of the sums in the row properties of [Section 3.6.6](/entry/theta-lift-row-properties-conj/) needs one number field that contains, up to two periods, every value of the two theta integrals of every bottom triangle. This section constructs that field. We prove that the values of the theta integrals of a bottom triangle at monomials are algebraic after division by one period, that they lie in a finite extension of $\mathbb Q$, and that the compositum over all squares of the grid is again a finite extension. The last statement is one of the hypotheses checked in the step [the hypotheses are not empty](/step/nonempty-hyps/).

We keep the notation of Sections 8, 10 and 11. Let $X$ be a bottom triangle at $(i, j)$ on the spaces $(A, A', W)$, with index set $\mathcal T$. For $t \in \mathcal T$, a polynomial $P$ and a finite point $h$ of the group of $W$, let $I_t(P)(h)$ and $I'_t(P)(h)$ be the two theta integrals of $X$, and let $k_t(P)(h, x)$ be the theta kernel of the first one at a finite point $x$ of the group of $A$. For a monomial $x^k$ in the variables of $W \otimes A$, the first coordinates of $k$ give a degree $\deg k$ in the variables of the embeddings. We call the values $I_t(x^k)(h)$ the class sums of $X$, and the values $I'_t(x^k)(h)$ its twisted class sums. We fix the local inputs, the record $\mathrm{Inp}(D)$ for every datum $D$, and a good level character at $\mu_0$.

**Definition 3.18.1 (Field of sums).** Let $M \subset \mathbb C$ be a subfield. The sums of $X$ lie in $M$ if there are $\Omega \neq 0$ and $\Omega' \neq 0$ such that for all $t$, all finite points $h$ and all monomials $x^k$,

$$\frac{I_t(x^k)(h)}{\Omega} \in M, \qquad \frac{I'_t(x^k)(h)}{\Omega'} \in M.$$

The bottom field condition says: at large scale, for every choice of the row there is a number field $M \subset \mathbb C$ such that for every square $(i, j)$ there is a bottom triangle at $(i, j)$ whose sums lie in $M$.

The periods $\Omega$ and $\Omega'$ are needed: the theta integrals are transcendental in general, and only their ratios are algebraic.

**Lemma 3.18.2 (Algebraic kernel values).** For every degree $d$ there is $\Omega \neq 0$ such that for all $t$, all finite points $x$ and $h$ and all monomials $x^k$ with $\deg k = d$, the number $k_t(x^k)(h, x)/\Omega$ is algebraic.

Lean: `GlobalTheory.BotAlgI.classSum_kernel_isAlgebraic`.

*Proof.* At a finite point the theta kernel is the theta sum of a translate of the vacuum vector. The vacuum is the sum of its Heisenberg expansion, and each translate by a finite point is an algebraic combination of Heisenberg translates of the vacuum. The jets of a Heisenberg translate of the vacuum at the monomials $x^k$ are algebraic multiples of one period that depends only on the degree, by the algebraicity of translated jets that the local inputs and $\mathrm{Inp}$ give. Section 19 studies the same jets in a sharper form. So every kernel value of degree $d$ is an algebraic number times the period $\Omega$ of the degree $d$. $\square$

**Theorem 3.18.3 (Algebraic class sums).** There is $\Omega \neq 0$ such that $I_t(x^k)(h)/\Omega$ is algebraic for all $t$, all finite points $h$ and all monomials $x^k$.

Lean: `GlobalTheory.BotAlgI.classSums_isAlgebraic` (also `GlobalTheory.T.bottom_classSums_algebraic`, a second name).

*Proof.* The class sum formula for a bottom triangle gives a real number $v > 0$, finitely many finite points $z_l$ of the group of $A$ and positive integers $w_l$ such that $I_t(P)(h) = v \sum_l w_l^{-1}\, I^{\mathrm{av}}_t(P)(h, z_l)$, where $I^{\mathrm{av}}$ is the real average of the kernel. The projection onto the real average is algebraic in a fixed degree $d$: there are algebraic numbers $r_{lp}$ and monomials $x^{k_p}$ with $\deg k_p = d$ such that

$$I_t(x^k)(h) = v \sum_l w_l^{-1} \sum_p r_{lp}\, k_t(x^{k_p})(h, z_l).$$

Take $\Omega$ from [Lemma 3.18.2](/entry/class-sum-kernel-is-algebraic/) for the degree $d$. Divide by $v\, \Omega$: each term is a rational number times an algebraic number times an algebraic kernel value, so the sum is algebraic. The period is $v\, \Omega \neq 0$. $\square$

For the twisted class sums we use the normal form of the second integral. A norm sum pair is a datum of the dictionary of norm sums in $\mathrm{Inp}(D)$: spaces of ranks $a$ and $d$, a Schwartz function and a level. A coordinate of such a pair is the value of its theta integral at a finite point $h'$ and a tuple $U$.

**Theorem 3.18.4 (Formula for the twisted class sums).** There is $\Omega \neq 0$ such that for all $t$, finite points $h$ and monomials $x^k$ there are $n$, algebraic numbers $c_1, \dots, c_n$ and coordinates $z_1, \dots, z_n$ of norm sum pairs with

$$I'_t(x^k)(h) = \Omega \sum_{l=1}^n c_l\, z_l.$$

Lean: `GlobalTheory.BotFormulaI'.bottomClassSum_formula` (also `GlobalTheory.T.bottomClassSum_eq_formula`, a second name).

*Proof.* The argument of [Theorem 3.18.3](/entry/class-sums-is-algebraic/) applies to the second integral, with the space $A'$ in place of $A$, and gives $I'_t(x^k)(h) = v\, \Omega\, S$ with $S$ algebraic and $v \neq 0$. A pair of rank zero is a norm sum pair whose coordinate at the trivial tuple is $1$. Take $n = 1$, the period $v\, \Omega$, the coefficient $c_1 = S$ and the coordinate $z_1 = 1$ of this pair. $\square$

**Theorem 3.18.5 (Algebraic twisted class sums).** There is $\Omega' \neq 0$ such that $I'_t(x^k)(h)/\Omega'$ is algebraic for all $t$, all finite points $h$ and all monomials $x^k$.

Lean: `GlobalTheory.BotAlgI'.twistedClassSums_isAlgebraic` (also `GlobalTheory.T.bottom_twistedClassSums_algebraic`, a second name).

*Proof.* By [Theorem 3.18.4](/entry/bottom-class-sum-formula/), $I'_t(x^k)(h)/\Omega$ is a finite sum $\sum_l c_l z_l$ with $c_l$ algebraic. The record $\mathrm{Inp}(D)$ gives that the coordinates of norm sum pairs are algebraic. Algebraic numbers form a field, so the sum is algebraic. Take $\Omega' = \Omega$. $\square$

To pass from algebraic values to a finite extension we need one more fact: the values are spanned by finitely many of them.

**Lemma 3.18.6 (Field of generators).** Let $v_t(h, k)$ be complex numbers indexed by a finite set of indices $t$, a set $H$ of good points $h$ and a set of labels $k$. Assume that there are finite sets $H_0 \subset H$ and $K_0$ and a number field $M_0$ such that every $v_t(h, k)$ is an $M_0$-linear combination of the $v_t(h', k')$ with $h' \in H_0$ and $k' \in K_0$, and that there is $\Omega \neq 0$ with every $v_t(h, k)/\Omega$ algebraic. Then there are a number field $M \subset \mathbb C$ and $\Omega \neq 0$ with $v_t(h, k)/\Omega \in M$ for all $t$, $h \in H$ and $k$.

*Proof.* Let $M$ be the field generated over $M_0$ by the finitely many algebraic numbers $v_t(h', k')/\Omega$ with $t$ in the finite index set, $h' \in H_0$ and $k' \in K_0$. It is a finite extension of $\mathbb Q$. Every other value divided by $\Omega$ is an $M_0$-linear combination of these generators, so it lies in $M$. $\square$

**Theorem 3.18.7 (The sums of a bottom triangle lie in a number field).** Let $X$ be a bottom triangle. Then there is a number field $M \subset \mathbb C$ such that the sums of $X$ lie in $M$.

Lean: `GlobalTheory.RowEx.BotField.sums_mem_bottomField`.

*Proof.* The class sums of $X$ are spanned, over a number field, by the class sums at finitely many finite points and monomials; this is the spanning lemma for bottom triangles that the local inputs and $\mathrm{Inp}$ give. With [Theorem 3.18.3](/entry/class-sums-is-algebraic/) the lemma on the field of generators gives a number field $M_1$ and $\Omega$. In the same way the twisted spanning lemma and [Theorem 3.18.5](/entry/twisted-class-sums-is-algebraic/) give $M_2$ and $\Omega'$. The compositum $M_1 M_2$ is a finite extension of $\mathbb Q$, and the sums of $X$ lie in it with the periods $\Omega$ and $\Omega'$. $\square$

**Theorem 3.18.8 (The bottom field is a number field).** Assume the local inputs and $\mathrm{Inp}(D)$ for every datum $D$. Then the bottom field condition holds.

Lean: `GlobalTheory.RowEx.bottomField_isNumberField`.

*Proof.* Fix a choice of the row. Its level character is good at $\mu_0$. For each square $(i, j)$ choose a bottom triangle $X_{ij}$ at $(i, j)$, and let $M_{ij}$ be the number field of [Theorem 3.18.7](/entry/sums-mem-bottom-field/). There are finitely many squares, so the compositum $M = \bigvee_{i,j} M_{ij}$ is a finite extension of $\mathbb Q$. If the sums of a triangle lie in a field, they lie in every larger field. So the sums of every $X_{ij}$ lie in $M$. $\square$

**Remark 3.18.9 (Formalization).** The theorem on the bottom field ([BottomFieldIsNumberField.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BottomFieldIsNumberField.lean#L30)) has all thresholds $0$, and it does not use the conditions of the choice beyond the finiteness of the index set and the good level character. The library has a second copy of both results that takes a different record of hypotheses ([NormalFormBottom.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/NormalFormBottom.lean#L49), lines 49 and 69). The formula for the twisted class sums ([BottomClassSumEqFormula.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BottomClassSumEqFormula.lean#L17)) is degenerate: it first proves that $I'_t(x^k)(h)/\Omega$ is algebraic and then writes this as one term with the coordinate $1$ of a pair of rank zero. The algebraicity of the twisted class sums ([BottomTwistedClassSumsAlgebraic.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BottomTwistedClassSumsAlgebraic.lean#L16)) then goes back through this formula and the algebraicity of norm sum coordinates, so the long route proves what the formula already contains. The lemma on the field of generators is in [NormalFormBottom.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/NormalFormBottom.lean#L26). We have not unfolded the class sum formula, the real average projection, the Heisenberg expansion of the vacuum, the spanning lemmas or the record $\mathrm{Inp}(D)$.
