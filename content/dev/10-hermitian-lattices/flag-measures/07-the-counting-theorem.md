---
title: The counting theorem
decls:
  - GlobalTheory.NearMod.nearModerate
  - GlobalTheory.CountFinal.countingTheorem_of_volumeStep
  - GlobalTheory.T.unitaryAutomorphicCounting_of_compactDualVolumeRatio
  - GlobalTheory.CountBridge.count_typed_of_volumeStep
  - GlobalTheory.CountConstants.count_constants_of_siegelWeil
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The counting theorem

This section proves the counting theorem: the dimension $D$ of a space of automorphic forms on $U(p,q)$ with a discrete series type at each infinite place is $D^\ast (1 + O(e^{-nf \log n/16}))$, where $D^\ast$ is the main term. The proof is a trace formula argument (see [the trace formula for a compact quotient](/learn/trace-formula/#the-trace-formula-for-a-compact-quotient)). The identity term gives $D^\ast$, and the other terms are split into near terms, far terms, rare flags and a deep region. The flag measure bound of the fourth section controls the near terms in the moderate region. The section ends with the form of the counting theorem that the later chapters use, with explicit constants, under the Siegel-Weil formula.

### Counting data

A *counting datum* consists of the global setting of the fourth section with signature $(p,q)$ at every infinite place, and at each infinite place $v$ a [discrete series](/learn/representations/#discrete-series) representation $\sigma_v$ with Harish-Chandra parameter $\lambda_v$, a unit lowest $K$-type vector $w_v$ and formal degree $d_v$. It also contains a level $g \ge 1$, an auxiliary prime $g_0$ and a finite test function. Let $D$ be the dimension of the space of forms of this type, and let $D^\ast$ be the main term, built from $\prod_v d_v$ and the volume of the quotient. The test function at the infinite places is
$$\phi(g) = \prod_v d_v \cdot \overline{\prod_v \langle w_v, \sigma_v(g_v) w_v \rangle}.$$

Let $r_E = |d_E|^{1/(2f)}$ be the root discriminant of $E$ and $n = p + q$.

**Definition 3.7.1 (Counting hypotheses).** Let $C_g \ge 0$, $n_0 \ge 1$ and $b > 0$. A counting datum satisfies the *counting hypotheses* for $(C_g, n_0, b)$ if:

1. each $\sigma_v$ is a discrete series with the parameter $\lambda_v$, lowest $K$-type vector $w_v$ and formal degree $d_v$;
2. $n_0 \le n$, $q^2 \le n$, $\log r_E \le e^n$ and $\log f \le \sqrt n$;
3. $b \ge 2$, $\log b \le e^{nf \log n/16}$ and $|\lambda_{v,a}| \le b^2$ for all $v$ and $a$;
4. $1 \le g \le b^{C_g}$;
5. $g_0$ is a prime with $g_0 > 4n$ that splits completely in $E$;
6. the gap of each $\lambda_v$ is at least $8 \cdot 10^{14} (C_g + 4) n^{19} f^5 \log(b\, r_E)$.

**Definition 3.7.2 (Counting theorem).** The *counting theorem* is the statement: for every $C_g$ there is $n_0$ such that every counting datum with the counting hypotheses for $(C_g, n_0, b)$ has a finite dimensional space of forms and
$$|D - D^\ast| \le e^{-nf \log n / 16}\, D^\ast.$$

### Near terms in the moderate region

For $x \in G_{\mathbb{A}}$ let $\ell(x)$ be the least size of a nonzero sublattice of $\Lambda_x$. Put $X = n f r_E\, g\, b$ and $\tau^\ast = X^{-11q}$. The *moderate region* is the set of $x$ in the fundamental domain with $\ell(x) \ge \tau^\ast$. An element $\gamma \in \Gamma$ is *near* $x$ if $x^{-1}\gamma x$ has finite part in $K_f$ and its infinite part is within Hilbert-Schmidt distance $\varepsilon_N = 10^{-6} n^{-8} f^{-2}$ of $1$ at each place. Let $\nu(x)$ be the sum of $|\phi(x^{-1} \gamma x)|$ over the near $\gamma \ne 1$.

**Theorem 3.7.3 (Near terms in the moderate region).** Assume the flag measure bound and the constant bound: for $j_i \ge 1$ with $\sum_i j_i \le q$, $15 \le \log n$, $q^2 \le n$, $\log(2v_E) \le e^n$ and $\log f \le \sqrt n$,
$$\kappa(E, p, q, j) \le e^{-\frac12 s n f \log n}, \qquad s = \sum_i j_i.$$
Assume also the bounds for near unipotent elements and the pointwise bound of the deep region. Then for every $C_g \ge 0$ there is $n_0$ such that for every counting datum with $q \ge 1$ and the counting hypotheses for $(C_g, n_0, b)$
$$\int_{\text{moderate}} \nu\, d\mu_{\mathbb{A}} \le e^{-nf \log n/4}\, D^\ast.$$

Lean: `GlobalTheory.NearMod.nearModerate`.

*Proof.* Put $L = nf \log n$. Take $n_0$ at least $3^{15}$ and large enough that $(2fq \cdot 11q \log X) \le e^{L/8}$ under the counting hypotheses. The proof has four steps.

1. If $\ell(x) \ge 1/2$, there is no near $\gamma \ne 1$, so $\nu(x) = 0$. Every other point of the moderate region has a type $(j, \tau)$ in the sense of the fourth section, with $s = \sum_i j_i \le q$.
2. For one type $j$ with $s = J$, the flag measure bound, the near unipotent bound and the pointwise bound give
$$\int_{T_j \cap \text{moderate}} \nu \le D^\ast \cdot 2 \kappa(E,p,q,j)\, Y^a, \qquad Y = 2fq \cdot 11 q \log X.$$
3. With $\kappa \le e^{-JL/2}$, $Y \le e^{L/8}$ and $a \le J$, an arithmetic lemma gives $2\kappa Y^a \le 2 e^{-3L/8}$.
4. The types are compositions $j$ of numbers $J \le q$, and there are fewer than $2^q$ of them. So the integral is at most $2^q \cdot 2 e^{-3L/8} D^\ast$. Since $q^2 \le n$ and $\log n \ge 15$, this is at most $e^{-L/4} D^\ast$. $\square$

### The counting theorem from the volume step

**Theorem 3.7.4 (Counting theorem from the volume step).** The volume step implies the counting theorem.

Lean: `GlobalTheory.CountFinal.countingTheorem_of_volumeStep` (also `GlobalTheory.T.unitaryAutomorphicCounting_of_compactDualVolumeRatio`, a second name).

*Proof.* Assume the volume step. The proof collects nine inputs.

1. The compression formula for the strict lowest $K$-type holds, and it gives the decay of the matrix coefficients of $\sigma_v$ away from $K_v$ in terms of the gap. This gives the pointwise bound of the deep region.
2. The volume ratio of the fourth section, from the volume step, gives an absolute bound for the volume of the quotient.
3. The volume ratio gives the flag measure bound of the fourth section.
4. The space of forms is finite dimensional.
5. The near terms in the moderate region are bounded by the theorem above. Its constant bound is proved with the explicit constant $\kappa$, and the near unipotent bound is proved separately.
6. The far terms in the moderate region are bounded from the flag measure bound and the pointwise bound.
7. The points with a nonzero flag are rare: their probability is at most $e^{-nf \log n/3}$, from the volume ratio.
8. The kernel on the diagonal in the deep region is bounded from the pointwise bound.
9. The counting theorem for discrete series follows from the finiteness and these bounds. The identity term is $D^\ast$, and the error terms add up to at most $e^{-nf\log n/16} D^\ast$. $\square$

### The constants for the later chapters

The later chapters use the counting theorem in a form with fixed exponents $c = c_b = 1/16$.

**Theorem 3.7.5 (Typed counting from the volume step).** Assume the volume step. Then for every $A$ there are $n_0$ and $C_0 \ge 0$ such that for all $n_1 \ge n_0$ and $C \ge C_0$ the following holds. For every counting datum at level $n_1$ with parameter $A$, gap $h \ge C n^{19} f^5 \log(b\, r_E)$, $\log f \le \sqrt n$ and $\log \log b \le \frac{1}{16} nf \log n$,
$$|D - D^\ast| \le e^{-nf \log n/16}\, D^\ast.$$

Lean: `GlobalTheory.CountBridge.count_typed_of_volumeStep`.

*Proof.* Apply the counting theorem from the volume step and its unbundled form, with $C_0 = \max(0, 8 \cdot 10^{14}(A + 4))$. The hypotheses of the statement are the counting hypotheses with $C_g = A$. $\square$

**Theorem 3.7.6 (Counting constants from the Siegel-Weil formula).** Assume the Siegel-Weil formula in its convergent range. Then there are counting constants depending on the list of output constants of a family, and $c_I = 1/16 > 0$, with these properties: for every family, the exponent $A$ is $2(\ell_6 + 1)$ where $\ell_6$ is the seventh output constant, $C \ge 0$, $A \ge 2(C_{YL} + 1)$, $c_I \le c$, and the counting statement holds for every class predicate with these constants.

Lean: `GlobalTheory.CountConstants.count_constants_of_siegelWeil`.

*Proof.* The Siegel-Weil formula gives the volume step by the fifth section. The typed counting gives $n_0(A)$ and $C_0(A)$ for each $A$. Take $A = 2(\ell_6 + 1)$, $n_0 = n_0(A)$, $C = C_0(A)$, $c = c_b = 1/16$, and the residual constants $0$. The inequality $A \ge 2(C_{YL} + 1)$ holds with equality. The counting statement for a class predicate follows from the typed counting at $n_1 = n_0$ and $C = C_0$. $\square$

**Remark 3.7.7 (Formalization).** The counting data are `RowsAut`, the counting hypotheses are `CountHyp` (LayerProd.lean, line 108), the main term is `mainTerm`, defined through `Dstar` and not unfolded here, and $D$ is `B.D`. The counting theorem is `CountingTheorem` (LatticeCountingTheorem.lean, line 10). The theorem on near terms takes the flag measure bound and the constant bound as hypotheses (OneTypeArith.lean, line 57); in the proof of the counting theorem the constant bound is `flag_explicit_constant_le_exp_neg_half`. Its per type bound is `nearTerms_moderate_points_one_type_bound` and the arithmetic lemma is `one_type_arith` (OneTypeArith.lean, line 36). The compression formula of step 1 is `lowestKType_compressionFormula_of_strictLowestKType`, which takes no hypothesis. The other inputs of the counting theorem are `hermAbsoluteVolumeBound_of_volume_ratio_induction`, `isotropicFlagProbabilityBound_of_volumeRatio`, `finiteDimensional_rowsSpace_discreteSeriesCount`, `near_unipotent`, `farTermsModerateRegion_of_flagBound`, `nonzeroFlagProbabilityBound_of_volumeRatioInduction`, `deepRegion_kernelDiagonal_bound` and `discreteSeries_counting_of_finite_and_bounds`, none of which is unfolded here. The statement file of the second name imports the proof module (UnitaryAutomorphicCountingOfCompactDualVolumeRatStatement.lean, line 2). The typed counting goes through `unitaryAutomorphicCounting_unbundled` (UnitaryAutomorphicCountingUnbundled.lean, line 40). The predicate `PointsLemma` ignores its first argument `_D` (PlaceDegreeData.lean, line 364), so the typed counting holds for every `D` with the same constants. In the counting constants, `count_class_of_count` drops the class predicate `P` (BridgeCountE.lean, line 45), and the inequality on $A$ is closed by `le_refl`.
