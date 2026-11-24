---
title: Families and the absolute constant
decls:
  - Formalism.MainNotions.AuxBlock8.Pf.stmtEF
  - Formalism.MainNotions.AuxBlock8.Pf.stmtF
  - Formalism.MainNotions.G.second_theorem_closed_everywhere
  - Formalism.MainNotions.G.second_theorem_absolute_constant
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Families and the absolute constant

This section proves two uniformity statements. The first part takes a family of data that depends on a real parameter $x$ and shows that the local estimates of the logarithmic sums hold along the family with one constant $C$ and with an error exponent that goes to $0$ as $x \to \infty$. This gives the [family statement](/entry/stmt-f/), which the [link without kernels](/entry/link-g-without-kernels/) uses. The second part shows that Statement E of Section 3 holds at every datum, and then that one constant $C_0$ serves all data at the same time. This gives the [absolute constant](/entry/second-theorem-absolute-constant/), which the [closed local link](/entry/link-of-local-closed/) uses.

### Families of data

**Definition 5.9.1 (Family of data).** Let $\varepsilon > 0$. A *family with exponent $\varepsilon$* gives, for each real number $x$, an index set $I_x$, and for each $i \in I_x$ a datum $\mathcal{D}_{x,i}$ with size data $L_{x,i}$. The size data contain positive numbers $a_{x,i}$ and $b_{x,i}$ and the exponent $\varepsilon$. The set $I_0$ is not empty. There is $x_1$ such that for $x > x_1$ the data carry parameter choices, and the list of constants of these parameter choices is the same for all $x > x_1$ and all $i \in I_x$.

The last condition is the reason why one constant can serve the whole family. It does not fix the data. It fixes only the constants that the local estimates use.

**Definition 5.9.2 (Local conclusion).** Let $\mathcal{D}$ be a datum with size data $L$, let $X$ be an instance for $(\mathcal{D}, L)$, let $K \geq 0$ be a set of constants, and let $C, \beta \geq 0$. The *local conclusion with $(C, \beta)$* is the conjunction of six statements.

1. The gain bound: at each prime $p \leq X''$ in the residue class zero or in the special set, the gains at $p$ are between $0$ and $4|T|a/p$, and the sum of the asks above the lower term $\mathrm{lo}(C, \beta, p)$ exceeds the total gain minus $\tau_p$ by at most $m\,\mathrm{fl}(C, p)$.
2. The mean bound for the numbers $\kappa$.
3. The points lemma: for each pair $(a, b)$ in the windows that satisfies the weighted requirement, two weighted prime sums are bounded by $5m|T|a/x$ and by $m|T|a\,x^{-9}$.
4. The weight vector: some pair $(a, b)$ in the windows satisfies the weighted requirement.
5. The ask comparison: for each pair $(a, b)$ with $a_s \leq 2a$ and $b_s \geq 0$, the global ask is at least the local ask and at most the local ask plus $N_m \log_p(2a)$.
6. The weighted prime sum bound: the sums over primes $p > X''$ are at most $m|T|a\,x^{-16}$, and two sums over primes $p \leq X''$ are at most $b\,x^{-100}$.

Here $T$ is the set of host indices of $\mathcal{D}$, and $m$, $N_m$, $X''$ are numbers attached to $\mathcal{D}$ and $L$.

**Definition 5.9.3 (Admissible along a family).** Let a family with exponent $\varepsilon$ be given. Let $K \geq 0$, let $X$ and $Y$ give an instance and a lattice instance at each $(x, i)$, and let $C_{31} > 0$, $C_e \geq 0$ and $C_m \geq 0$. We say that $(X, Y)$ is *admissible along the family with $(C_{31}, C_e, C_m)$* if for every $\delta > 0$ there is $x_0 > 1$ such that the twelve local admissibility conditions hold at $(\mathcal{D}_{x,i}, L_{x,i}, X_{x,i}, Y_{x,i})$ with constants $(C_{31}, C_e, C_m, \delta)$ for all $x \geq x_0$ and all $i \in I_x$.

**Theorem 5.9.4 (Closed form along a family).** Let a family with exponent $\varepsilon$ be given. Let $K \geq 0$, $C_{31} > 0$, $C_e \geq 0$ and $C_m \geq 0$. Then there is $C \geq 0$ with the following property. If $(X, Y)$ is admissible along the family with $(C_{31}, C_e, C_m)$, then there are a function $\delta$ with $\delta(x) \to 0$ as $x \to \infty$ and a number $x_0$ such that, for all $x \geq x_0$ and all $i \in I_x$, the local conclusion holds at $(\mathcal{D}_{x,i}, L_{x,i}, X_{x,i})$ with constants
$$
(C, \beta), \qquad \beta = b_{x,i}^{\delta(x)}.
$$
We can take $\delta(x) = x^{-\varepsilon/2}$.

Lean: `Formalism.MainNotions.AuxBlock8.Pf.stmtEF`

*Proof.* The proof uses six estimates along the family. Each of them has the same form: for the given $K$ and constants, and for $(X, Y)$ admissible along the family, there is a threshold beyond which a statement holds at every $(x, i)$.

1. The ask estimate gives, for $x$ large, the ask comparison for all primes $p$ and all pairs $(a, b)$ with $a_s \leq 2a$ and $b_s \geq 0$.
2. The remaining counting statement gives a constant $C \geq 0$ that depends only on $K$, $C_{31}$, $C_e$ and $C_m$. For $x$ large it gives the gain bound with constants $(C, b_{x,i}^{\delta(x)})$, with $\delta(x) = x^{-\varepsilon/2}$, at every pair $(a, b)$ in the window of $L_{x,i}$. This statement comes from the star estimate along the family.
3. The fourth estimate gives the mean bound for $\kappa$.
4. The weight vector estimate gives a pair $(a, b)$ that satisfies the weighted requirement.
5. The fifth estimate gives the points lemma at every $(x, i)$ where the gain bound of step 2 holds.
6. The third estimate along the family gives the weighted prime sum bound with the constant $C$ of step 2.

Fix $C$ from step 2. Then let $(X, Y)$ be admissible along the family. Each step gives a threshold, and we let $x_0$ be the largest of the six thresholds. Let $x \geq x_0$ and $i \in I_x$.

The size data $L_{x,i}$ define a pair $(a_L, b_L)$, with $a_L(s) = a_s$ and $b_L(s) = b_s$ for $s \in T$ and value $0$ outside $T$. This pair is in the window of $L_{x,i}$, because $a_s$ lies in the window and $b_s$ is at least the lower bound. So step 2 at $(a_L, b_L)$ gives part 1 of the local conclusion. Steps 3, 4 and 6 give parts 2, 4 and 6. Step 5 with the result of step 2 gives part 3. Step 1 holds at all primes, so it holds at the primes of part 5 in particular.

The function $\delta(x) = x^{-\varepsilon/2}$ goes to $0$ as $x \to \infty$, because $\varepsilon > 0$. The exponent $\varepsilon$ is positive because the size data at $(0, i)$ have exponent $\varepsilon$, and size data always have a positive exponent; here we use that $I_0$ is not empty. $\square$

**Corollary 5.9.5 (Family statement).** Let a family with exponent $\varepsilon$ be given and let $K \geq 0$. Let $(X, Y)$ be admissible along the family with some constants $C_{31} > 0$, $C_e \geq 0$, $C_m \geq 0$. Then there are $C$, a function $\delta$ with $\delta(x) \to 0$, and $x_0$ such that for all $x \geq x_0$ and all $i \in I_x$ the local conclusion holds at $(\mathcal{D}_{x,i}, L_{x,i}, X_{x,i})$ with constants $(C, b_{x,i}^{\delta(x)})$.

Lean: `Formalism.MainNotions.AuxBlock8.Pf.stmtF`

*Proof.* Take the constants $C_{31}$, $C_e$, $C_m$ from the hypothesis. The theorem gives $C$ for these constants, and then gives $\delta$ and $x_0$ for $(X, Y)$. $\square$

The corollary differs from the theorem in the order of the quantifiers. In the theorem, $C$ comes before $(X, Y)$, so $C$ is uniform in all admissible pairs with the given constants. In the corollary, the constants of admissibility are part of the hypothesis, and $C$ is chosen after them.

### The second theorem at every datum

Recall from Section 3 that *Statement E for a datum $\mathcal{D}$* means: there is $C_0 > 0$ such that Statement E holds with every constant $C \geq C_0$. Statement E with constant $C$ is a statement about the unramified quadratic setting. Its hypotheses are conditions on $p$, the orbit data and the weights, and none of them refers to $\mathcal{D}$.

The next theorem takes two groups of inputs.

1. The *projector condition* at every datum. With the positivity, weight, exponent and key positivity conditions, which are known at every datum, it gives the local conditions of the weight theory, and so it gives the first and second conclusions of covariant degrees and the hyperplane rank.
2. The *list of inputs for the second theorem*. It contains the reduced second theorem at every datum, the second part of the selection at every datum (Section 8), the three combinatorial facts of Section 8 (the tableau count, the branching rule and the Pieri rule), and twelve other conditions: a dual height inclusion, a perfectness condition, an LP1 condition, a flat top condition, a dual height basis, a spanning condition, the test side condition, a Witt identity, the filtered projection criterion, a condition from clause 22, the few bad orbits condition and the level primes proviso.

The *reduced second theorem* at $\mathcal{D}$ says: if $\mathcal{D}$ is admissible with constants $C_{La}$, $C_k$, $C_{rk}$, $C_{\deg}$, if source cleaning holds with some positive constants, and if plane Gram holds with some positive constants $(C_H, C_E, C_6, C_{18})$ for all $C_H$ above a bound, then Statement E holds for $\mathcal{D}$.

**Theorem 5.9.6 (Second theorem at every datum).** Assume the projector condition and the list of inputs for the second theorem. Then Statement E holds for every datum $\mathcal{D}$.

Lean: `Formalism.MainNotions.G.second_theorem_closed_everywhere`

*Proof.* Fix $\mathcal{D}$. The projector condition gives the conclusions of covariant degrees and the hyperplane rank at $\mathcal{D}$. The plane count theorem with constants uses these conclusions, the three combinatorial facts and the second part of the selection. It gives constants $C_{La}$, $C_k$, $C_{rk}$, $C_{\deg}$ and the rank and degree bounds for them.

Then we build the $37$ admissibility conditions of $\mathcal{D}$ for these constants. Some come from the list of inputs directly. Some are known at every datum, for example the orbit position and orbit count conditions. The others follow from the conclusions of covariant degrees by short lemmas that turn each conclusion into an orbit count, a multiplicity bound or a support statement. One of them uses the rank and degree bounds.

The derived statements with constants give source cleaning at $\mathcal{D}$ with positive constants. The split theorem with constants gives plane Gram at $\mathcal{D}$ for all $C_H$ above a bound. Now the reduced second theorem at $\mathcal{D}$ gives Statement E for $\mathcal{D}$. $\square$

**Theorem 5.9.7 (Absolute constant).** Assume the projector condition and the list of inputs for the second theorem. Then there is $C_0 \geq 0$ such that Statement E with constant $C_0$ holds for every datum $\mathcal{D}$.

Lean: `Formalism.MainNotions.G.second_theorem_absolute_constant`

*Proof.* There are two cases.

If there is a datum $\mathcal{D}_0$, the previous theorem gives $C_0 > 0$ such that Statement E holds for $\mathcal{D}_0$ with every constant $C \geq C_0$, and in particular with $C_0$. Statement E with constant $C_0$ does not refer to the datum. So it holds for every datum $\mathcal{D}$.

If there is no datum, put $C_0 = 0$. The statement about every datum is then empty. $\square$

The proof does not need a uniform bound over the data. The constant comes from one datum, and it serves all data because Statement E does not depend on the datum.

**Remark 5.9.8 (Formalization).** The family is `FamP` (ParConsts.lean:31). The local conclusion is `AuxBlock8.Conclusion₂` and the twelve conditions are `AuxBlock8.admitted` (SmallOrderPrimes.lean:241, 246). The theorem states `FamilyClosedForm` and the corollary states `KudlaFamilyStatement` (SmallOrderPrimes.lean:270, 266). The proof of the theorem is `stmtEF_of` (LogarithmicSums/RemainingCountingStatement.lean:47) applied to `rest0`, `remainingCountingStatement_of_restStar`, `rest2`, `restW`, `rest3` and `restT` (LogarithmicSums.lean:36 to 98). These six lemmas, and `St.star_fam` and `G5.third_estimate_along_family` behind them, were not unfolded. The admissibility conditions and the six parts of the conclusion were read only at the level of their statements. The proof of `stmtEF_of` proves inline that $(a_L, b_L)$ is in the window (RemainingCountingStatement.lean:71), although the lemma `inWin_sizeData` (Conclusion1OfGainBoundAll.lean:151) states the same fact. The fifth estimate `FamilyFifthBound` takes the gain bound as a hypothesis at each point, so step 5 of the proof depends on step 2. The symbol $\delta$ has two roles: it is the constant of admissibility in `AConsts` and the error function in the conclusion. The names `KudlaFamilyStatement` and `FamilyClosedForm` are defined in five files with different meanings (SmallOrderPrimes.lean:266, TableLineDegreeFive.lean:253, Lemma5aAt.lean:336, ColumnSystems.lean:287, StatementOfDegreeAndBound.lean:524), and `CornerGLContinuity.lean:333` has a sixth. The theorems of the second part are in PlaneCountTheoremWithConstants.lean:1121 and 1137. The projector condition is `ExtremalProjectorTools` (line 1005), a structure with the one field `CovariantDegrees.adm5` at every datum. The list of inputs is the structure `Loc6` (line 1059). Its field `p14R` is the reduced second theorem `SecondTheoremReduced` (line 1020) at every datum, so the main step of the proof is a hypothesis. The lemma `criterion_restricted_of_closed` (line 1025) shows that `SecondTheoremReduced` follows from `tableLineDegreeFive.ClosedFormOfAdmitted` and drops the source cleaning and plane Gram inputs. In `SecondTheoremReduced` and in `split_theorem_with_constants` a bound real variable is named `FormalChartAtZero` (lines 1023, 1111). The lemmas of the namespace `Joints`, `plane_count_theorem_with_constants`, `derived_statements_with_constants` and `split_theorem_with_constants` were not unfolded in this section. Statement E with constant $C$ is `tableLineDegreeFive.aux₃ D C`, which ignores `D` (TableLineDegreeFive.lean:30); the proof of the absolute constant depends on this. If `D7` is empty, the absolute constant theorem is vacuous.
