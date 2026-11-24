---
title: The slope bound and the top level inputs
decls:
  - GlobalTheory.CompanionTheory.Ar.Sl.TopSlope.slopeBound
  - GlobalTheory.T.slope_bound_of_large_degree_line
  - GlobalTheory.CompanionTheory.Ar.Sl.slopeBound_and_lemmaS_of_siegel
  - GlobalTheory.T.slope_bound_of_line_large_degree
  - GlobalTheory.CompanionTheory.Ar.Top.given_of_inputs
  - GlobalTheory.T.final_theorem_of_inputs_left
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The slope bound and the top level inputs

This section ends the proof of the slope bound for Lie algebras of principally polarized semi-abelian schemes, and then assembles the top level inputs that the whole chapter assumes. The slope bound follows from the line statement of the last section and an absolute Siegel lemma: a subbundle of large slope contains a vector of large degree, and the line statement says that no vector has a large degree. The top level inputs are then built from twelve named inputs, with the slope bound as one part and two parts proved. They are used by the [volume theorem for reduced towers](/entry/good-tower-volume-of-reduced/) and by [the deep statement from use](/entry/deep-st-r-of-use/).

### The slope bound

Let $\overline{B}$ be a hermitian vector bundle over $\mathcal{O}_L$. Its maximal slope is
$$
\mu_{\max}(\overline{B}) = \sup_{0 \ne F \subseteq B} \mu(\overline{F}) ,
$$
the sup over the nonzero saturated submodules, with the restricted metrics, of the normalized slope $\mu(\overline{F}) = \widehat{\deg}_n \overline{F} / \mathrm{rk} F$. See the [learning page on hermitian lattices and slopes](/learn/arakelov/#hermitian-lattices-and-slopes).

**Definition 8.19.1 (Absolute Siegel lemma).** The absolute Siegel lemma says: for every number field $K$, every hermitian bundle $\overline{F}$ over $\mathcal{O}_K$ of rank $i \ge 1$ and every $\varepsilon > 0$ there are a finite extension $K'/K$ and $v \ne 0$ in $F \otimes \mathcal{O}_{K'}$ with
$$
\mu(\overline{F}) - \frac{1}{2} \log i - \varepsilon \le \widehat{\deg}_n(v) ,
$$
where $\widehat{\deg}_n(v) = - \frac{1}{[K':\mathbb{Q}]} \sum_\sigma \log \| v \|_\sigma$ for the integral vector $v$.

It is the [large degree line input](/entry/line-of-large-degree-of-use/), and it is one of the twelve inputs below.

**Definition 8.19.2 (Slope bound statement).** The slope bound statement says: there is $C \ge 0$ such that for every principally polarized semi-abelian scheme over $\mathcal{O}_L$ with Lie bundle $\overline{B}$,
$$
\mu_{\max}(\overline{B}) \le C \log \bigl( 2 + \mathrm{rk} B + \max(-\widehat{\deg}_n \overline{B}, 0) \bigr) .
$$

**Theorem 8.19.3 (Slope bound from the line statement).** The absolute Siegel lemma and the key degree statement imply the slope bound statement.

Lean: `GlobalTheory.T.slope_bound_of_large_degree_line` (also `GlobalTheory.CompanionTheory.Ar.Sl.TopSlope.slopeBound`, a second name).

*Proof.* The key degree statement gives the line statement with a constant $C$, by the last section. We prove the slope bound with $C + 2$. Let a scheme with Lie bundle $\overline{B}$ be given, and put
$$
\ell = \log \bigl( 2 + \mathrm{rk} B + \max(-\widehat{\deg}_n \overline{B}, 0) \bigr) .
$$
Then $\ell \ge \log 2 > \frac{2}{3}$, and $\log \mathrm{rk} B \le \ell$; when $\mathrm{rk} B = 0$ the left side is $\log 0 = 0$ by convention.

Let $F \subseteq B$ be a nonzero submodule. The short vector lemma for submodules, which is the Siegel lemma applied to $\overline{F}$ with $\varepsilon = 1$, gives a finite extension $L'/L$ and a nonzero vector $x$ of the base change of $B$ to $\mathcal{O}_{L'}$ with
$$
\mu(\overline{F}) - \frac{1}{2} \log \mathrm{rk} B - 1 \le - \frac{1}{[L':\mathbb{Q}]} \sum_\sigma \log \mathrm{len}_\sigma(x) .
$$
We pull the principally polarized datum back to $L'$. Its Lie bundle is the base change of $\overline{B}$, with the same rank and the same normalized degree, and there is an isometric map $\Phi$ from the base change of $\overline{B}$ to it. So the lengths of $\Phi(x)$ are the lengths of $x$.

If $\Phi(x) \ne 0$, the line statement on $L'$ gives
$$
- \frac{1}{[L':\mathbb{Q}]} \sum_\sigma \log \mathrm{len}_\sigma(x) \le C \ell .
$$
If $\Phi(x) = 0$, all lengths are $0$, the left side is $0$ by the convention $\log 0 = 0$, and the bound holds since $C \ell \ge 0$. In both cases
$$
\begin{aligned}
\mu(\overline{F}) &\le C \ell + \frac{1}{2} \log \mathrm{rk} B + 1 \\
&\le C \ell + \frac{1}{2} \ell + \frac{3}{2} \ell \le (C + 2) \ell .
\end{aligned}
$$
The sup over $F$ gives the slope bound. The provisional statement S is the slope bound statement itself, so the proof gives it too. $\square$

**Corollary 8.19.4 (Slope bound from the Siegel lemma).** The absolute Siegel lemma implies the slope bound statement and statement S.

Lean: `GlobalTheory.CompanionTheory.Ar.Sl.slopeBound_and_lemmaS_of_siegel` (also `GlobalTheory.T.slope_bound_of_line_large_degree`, a second name).

*Proof.* The bad reduction statement is proved, so the last section gives the key degree statement from it. Apply the theorem. $\square$

So the slope bound has one open input, the absolute Siegel lemma. The key formula and the integrality at bad reduction are proved.

### The top level inputs

The top level inputs are a conjunction of fourteen parts. Twelve of them are named inputs, which we list in the order of the conjunction.

1. The model clause: the integral models of part I, the conditions N1ab and N1c, and the compatibility of the toroidal compactifications with the level and with the Hecke operators.
2. The key formula for theta sections.
3. The extension of homomorphisms of semi-abelian schemes.
4. The numerical Segre statement.
5. Resolution of singularities with coordinates (the $\mathrm{ResK}$ statement).
6. The strong approximation statement for the special unitary group of the hermitian form. This part is proved.
7. The Hodge-Tate decomposition of Fargues.
8. GAGA for sections of line bundles.
9. The slope bound statement.
10. The pullback inputs.
11. The provisional statement HS.
12. The provisional analytic statement.
13. The dimension, pushdown and Grassmannian height bounds of Zhang.
14. The antisymmetric perturbation statement. This part is proved.

**Theorem 8.19.5 (Top level inputs from the named inputs).** Assume the model clause, the key formula, the extension of homomorphisms, the numerical Segre statement, the resolution statement, the Hodge-Tate decomposition, GAGA for sections, the absolute Siegel lemma, the pullback inputs, statement HS, the analytic statement and the bounds of Zhang. Then the top level inputs hold.

Lean: `GlobalTheory.T.final_theorem_of_inputs_left` (also `GlobalTheory.CompanionTheory.Ar.Top.given_of_inputs`, a second name).

*Proof.* The parts $1$ to $5$, $7$, $8$ and $10$ to $13$ are hypotheses. Part $6$ is the proved strong approximation statement, and part $14$ is the proved antisymmetric perturbation statement. Part $9$ is the first half of the corollary, applied to the absolute Siegel lemma. $\square$

The proof is one term: it puts the hypotheses and the three results in the places of the conjunction. The content of this section is in the slope bound.

**Remark 8.19.6 (Formalization).** The two names `slope_bound_of_line_large_degree` and `slope_bound_of_large_degree_line` differ only in the order of two words, and they name different results: the first takes only the Siegel lemma, the second also takes `KeyDegSt`. The name `final_theorem_of_inputs_left` names a result whose conclusion is `Top.Given` (GoodOrigin.lean:67), the set of hypotheses of the chapter, not a final theorem. The key formula is the second hypothesis of `given_of_inputs` (FinalTheoremOfInputsLeft.lean:22 to 25), but it is proved as `T.exactKeyFormula_proof` (ExactKeyFormulaProofStatement.lean:22), and `keyDeg_of_keyBad` uses that proof (KeyDegreeOfBadReduction.lean:225). Part 13 has a conjunct `True` (ZhangDimensionPushDownGrassmannianHeightBounds.lean:33), and in the same file `LemmaS` is defined to be `SlopeBoundSt` (line 35), so `slopeBound` ends with `⟨hS, hS⟩` (SlopeBoundOfLargeDegreeLine.lean:143). In `slopeBound` the fact $x \ne 0$ from `short_vector_of_submodule` is discarded (line 117), the case $\Phi x = 0$ uses `Real.log_zero`, and the term $\frac{1}{2} \log$ is taken of the rank of $B$, not of $F$; this is weaker than the Siegel lemma for $F$ but it is enough. We do not unfold the twelve named inputs.
