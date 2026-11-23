---
title: Densities and the global cores
decls:
  - Formalism.FourierDecayAlt.P.HilbertSchmidtNorm.globalCores
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Densities and the global cores

The bound on the energy uses [Theorem A](/entry/theorem-a-after/) in a special case. All the numbers $e_i$ vanish below the top level, and the top number is $e_{r+1} = \max(d, 1) - 1$, where $d$ is the supremum of a local density. This section proves that $d \leq 2$ under a size condition on the weight, shows how the density moves into the top kernel, and collects these facts with Theorem A into one statement. That statement and [the local cores](/entry/local-cores/) are the two kernel inputs of [the applied Theorem PB](/entry/pb-applied/).

**Lemma 3.4.1 (Density bounds).**

1. Let $S$ be a finite set, let $n \geq 2$, and for $p \in S$ let $l_p$ be a prime and $q_p \geq l_p$ a real number. Assume that for each $m$ at most $f$ elements $p \in S$ have $l_p = m$. Then $\sum_{p \in S} q_p^{-n} \leq 3f\, 2^{-n}$.
2. If $18 f \leq 2^n$, then $\exp(12 f\, 2^{-n}) \leq 2$.
3. If $2r + 2 + f + 5 \leq k$, then $18 f \leq 2^{k - 2r - 2}$.
4. Let $k$ and $m$ be kernels on a finite set $Y$, and $d \in \mathbb{R}$. If $k$ and $d\, k - m$ are positive semidefinite on $Y$, then so is $\max(d, 1)\, k - m$.

*Proof.* For part 1, group $S$ by the value of $l$. Then $\sum_{p \in S} q_p^{-n} \leq \sum_p l_p^{-n} \leq f \sum_{m \geq 2} m^{-n}$. Compare the tail with an integral: $\sum_{m \geq 3} m^{-n} \leq \int_2^\infty x^{-n}\, dx = 2^{1-n}/(n-1) \leq 2 \cdot 2^{-n}$. So the sum is at most $3f\, 2^{-n}$. For part 2, $12 f\, 2^{-n} \leq 12/18 = 2/3$, and $e^{2/3} < 1.95$. For part 3, $k - 2r - 2 \geq f + 5$, so $2^{k - 2r - 2} \geq 32 \cdot 2^f \geq 18 f$. For part 4, write $\max(d, 1)\, k - m = (d\, k - m) + (\max(d, 1) - d)\, k$. The coefficient $\max(d, 1) - d$ is nonnegative, so both terms are positive semidefinite, and so is their sum. $\square$

**Proposition 3.4.2 (The density is at most 2).** Let $k, r, f \in \mathbb{N}$ with $2r + 2 + f + 5 \leq k$, and put $n = k - 2r - 2$. Let $P$ be a set, and for $p \in P$ let $l_p$ be a prime and $q_p \geq l_p$. Assume that each finite subset of $P$ on which $l$ is constant has at most $f$ elements. Let $d \in \mathbb{R}$, and assume that for each $x < d$ there is a finite $S \subseteq P$ with
$$x \leq \prod_{p \in S} \exp\big(4\, q_p^{-n}\big).$$
Then $d \leq \exp(12 f\, 2^{-n})$ and $d \leq 2$.

*Proof.* Part 3 of the Lemma gives $18 f \leq 2^n$, and $n \geq f + 5 \geq 2$. Let $x < d$ and take $S$ as in the hypothesis. The product is $\exp(4 \sum_{p \in S} q_p^{-n})$, and part 1 of the Lemma bounds the sum by $3f\, 2^{-n}$. So $x \leq \exp(12 f\, 2^{-n})$. Since $x < d$ is arbitrary, $d \leq \exp(12 f\, 2^{-n})$, and part 2 gives $d \leq 2$. $\square$

The hypothesis on $d$ says that $d$ is at most the supremum of the finite products. In the application, $p$ runs over places of a number field above the primes $l_p$, $q_p$ is the size of the residue field, and $f$ is the degree; at most $f$ places lie over each prime.

**Definition 3.4.3 (Scaling the top).** For kernel data $D$ and $\lambda \in \mathbb{R}$, the data $D_\lambda$ agree with $D$ except at the top level: the top kernel is $\lambda K_{r+1}$, and $e_{r+1}$ is replaced by $\lambda - 1$.

**Lemma 3.4.4 (Scaling the top).** Let $T$ be a tower, let $\lambda \geq 0$, and assume $e_{r+1} = 0$. If the family $\Theta$ dominates $T$ for $D$, then the family equal to $\lambda \Theta_{r+1, s, t}$ at level $r + 1$ and to $\Theta_{i, s, t}$ below it dominates $T$ for $D_\lambda$.

*Proof.* Below the top nothing changes. At level $i = r + 1$, conditions 1 and 2 of [domination](/entry/theorem-a-after/) are multiplied by $\lambda \geq 0$, which keeps positivity and equality. Condition 3 for $D$ reads: $K_{r+1-s} - \sum_{t \in S} \Theta_{r+1, s, t}$ is positive semidefinite, since $e_{r+1} = 0$. For $D_\lambda$ the factor is $1 + (\lambda - 1) = \lambda$, and the kernel $\lambda K_{r+1-s} - \sum_t \lambda \Theta_{r+1, s, t}$ is $\lambda$ times the former. $\square$

**Corollary 3.4.5 (Theorem A with a density).** For $C_1, C_4 \geq 1$ there are $C, C'$ with the following property. Let the data satisfy the hypotheses of Theorem A with $C' \leq \vartheta$ and $r(C/\vartheta)^f \leq 1$, let $e_i = 0$ for $1 \leq i \leq r$, and let $1 + e_{r+1} = \max(d, 1)$. Then for each finite $R \subseteq \mathbb{N}$
$$\sum_{\rho \in R} \Big\| \sum_p c_\rho(p)\, V_p \Big\|^2 \leq \Big(1 + C(r + 1)\Big(\frac{C}{\vartheta}\Big)^f\Big) \max(d, 1)\; j.$$

*Proof.* This is Theorem A, since $\prod_{i=1}^{r+1} (1 + e_i) = \max(d, 1)$. $\square$

In the application one starts from data with $e_{r+1} = 0$ and a leading domination with factor $d$: the kernel $d\, K_{r+1} - \sum_\rho c_\rho \otimes \overline{c_\rho}$ is positive semidefinite. Part 4 of the Lemma replaces $d$ by $\max(d, 1)$, and the scaling lemma with $\lambda = \max(d, 1)$ gives data that satisfy the hypotheses of the Corollary. With $d \leq 2$, the condition $e_{r+1} \leq 1$ of Theorem A holds.

**Theorem 3.4.6 (Global cores).** The following hold together.

1. [Theorem A](/entry/theorem-a-after/), and the Corollary above.
2. The scaling lemma, and the statement that the scaled data $D_{\max(d, 1)}$ satisfy the hypotheses of Theorem A, with the same $r$ and $f$, with $1 + e_{r+1} = \max(d, 1)$ and with the same $e_i$ for $i \leq r$, when $d \leq 2$ and $e_{r+1} = 0$ for $D$.
3. The four parts of the Lemma on density bounds and the Proposition above.
4. Eighteen further statements: a Poisson summation step and two joint forms of it, a bound for smoothed sums over boxes, facts on lattices, ideals, norms and degrees for a CM field, frame products, the identification of a lattice with its first member, joint lattice sums, sizes and lattice sums for the instance at hand, the main size statement and its passage to the recursion, positivity of a global quantity, and a main theorem together with the passage from the energy form to it.

Lean: `Formalism.FourierDecayAlt.P.HilbertSchmidtNorm.globalCores`.

*Proof.* The theorem is the conjunction of its items, each proved separately. Item 1 is Theorem A and the Corollary. Item 2 is the scaling lemma, and the transfer of the hypotheses uses part 4 of the Lemma for the leading domination. Item 3 is the Lemma and the Proposition. The statements of item 4 are proved by the results that the Remark below names. $\square$

**Remark 3.4.7 (Formalization).** `globalCores` ([SecondDerivativeHolds.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/SecondDerivativeHolds.lean#L47)) is a 27-tuple proving `PB.GlobalCores` ([StatementPB.lean](lean:Formalism/HermitianCurvature/StatementPB.lean#L346)). Its first nine entries are `TC.TheoremAAfter`, `TC.RecursionWithDens`, `TC.DomScaleTop`, `TC.SumBoundMax`, `TC.RecHypScaleTop`, `TC.DensSum`, `TC.DensLeTwo`, `TC.DensSize` and `TC.DensChain` ([StatementTC.lean](lean:Formalism/HermitianCurvature/StatementTC.lean#L239)); we read these statements, and we give our own proofs of the density bounds, since we did not open theirs. `RecursionWithDens` and `DensChain` take the other statements as hypotheses (for example `DensSum → DensLeTwo → DensSize → ...`), so they are implications, and the tuple supplies their inputs separately. The remaining eighteen entries, such as `F7.PoissonStepText`, `Formalism.SA.C.BoxSum`, `S6.LatticesGeneral`, `J.XIsLamOne` and `S3.MainTheorem`, are paraphrased from their names only; we did not open them. `TheoremS.lean` in the folder `LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors` uses `globalCores`. The namespace `HilbertSchmidtNorm` does not describe the content.
