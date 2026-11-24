---
title: Two lemmas of the selection
decls:
  - Formalism.MainNotions.SelectionLemmas.Pf.atypical_path_small_weight
  - Formalism.MainNotions.SelectionLemmas.Pf.generator_modulo_uniformiser_of_adm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Two lemmas of the selection

Section 8 proved the second part of the selection from a count of good paths and from two facts modulo the uniformizer. This section states and proves two of the lemmas that the proof there used without a statement. The first bounds the number of tableaux over an atypical path; it is the input of [Lemma T](/entry/lem-t-of-adm/). The second says that the discriminant times a coarse generator is, modulo the uniformizer, a generator of the module $N$ of the second selection statement; it is the step "the generators are independent modulo the uniformizer" in the proof of [the second part of the selection](/entry/second-part-closed/). We keep the notation of Section 8: the path hypotheses, $k = r + K$, $\Xi_i = L_ab_i/(pk)$, $\mathrm{rk}$ and $\ell_0 = \log(1 + 2aN)$.

### Atypical paths

**Lemma 5.10.1 (Atypical paths have small weight).** Let the datum be admissible of the second kind. Let $(N, n_0, r, K, B, \mathrm{od}, b, a, L_a, p)$ satisfy the path hypotheses, and let $\mu$ be an admissible path that is not typical. Then the number of semistandard tableaux of shape the tangent part of $\mu_N$, with entries in $\{1, \dots, K\}$, is at most
$$\exp\Big(9N^2\ell_0 - \min\Big(\frac{L_a(K - 2N)}{16k}, \frac{K - 2N}{12}\Big)\Big)\,\mathrm{rk}.$$

Lean: `Formalism.MainNotions.SelectionLemmas.Pf.atypical_path_small_weight`.

*Proof.* The third condition of admissibility of the second kind is the tableau count: the number of semistandard tableaux of a dominant shape $\nu \in \mathbb{Z}^K$ with entries in $\{1, \dots, K\}$ is
$$\dim_K(\nu) = \prod_{0 \leq i < j < K}\frac{\nu_i - \nu_j + j - i}{j - i},$$
the [Weyl dimension](/learn/representations/#highest-weights-and-branching) of the representation of $\mathrm{GL}_K$ of highest weight $\nu$. So the number to bound is the weight $\mathrm{wt}(\mu)$ of the path in the sense of [the Theorem (Weight of a path)](/entry/lemma-t-one/), the Weyl dimension of the last $K$ rows of $\mu_N$.

We put the data in the form of that theorem. The letter list gives the signs $v_i$, with vectors at the first $r$ and at the last steps, and the degrees $B_i$ give the sizes. Take $N_s = N$, so that $k' = K - 2N$ and $n_0 = N - r$. Take the real number $a$, the prime $13$ in place of $p$, $\Lambda = L_a$, and the weights $b'_i = 13b_i/p$. The size hypotheses for $(a, 13)$ follow from the path hypotheses: $a \geq 3$, $k \leq B_i \leq 2a$, the growth of the sizes by a factor $p^2/5 \geq 13^2/5$, $N + r \leq K$, $2r \leq n_0$, $k \leq 2(K - 2N)$ and $N \leq a$. The condition $B_l \leq 4b_i/p$ of the path hypotheses reads $B_l \leq 4b'_i/13$, so $(L_a, b')$ are threshold data. Their thresholds are
$$X_i = \frac{L_a b'_i}{13k} = \frac{L_ab_i}{pk} = \Xi_i.$$
With these thresholds, typical in the sense of the theorem is typical in the sense of Section 8: the three conditions on the drop of the positive part at a covector, the drop of the negative part at a vector, and the last plane coordinate, are the same. So $\mu$ is not typical for $X$, and the second bound of the theorem gives $\mathrm{wt}(\mu) \leq \exp(E - \min(\Lambda k'/(16k), k'/12))A$ with $E = 9N^2\ell_0$ and $A = \mathrm{rk}$. $\square$

The proof of Lemma T in Section 8 multiplies this bound by the number $e^{2N^2\ell_0}$ of admissible paths. The exponent $\min(L_a, k)/32$ of Lemma T comes from $k/2 \leq K - 2N$, which turns $\min(L_a(K - 2N)/(16k), (K - 2N)/12)$ into at least $\min(L_a, k)/32$.

### The discriminant modulo the uniformizer

We work with segment data in the sense of Section 4, with their hypotheses, over a discrete valuation ring $\mathcal{O}$ with uniformizer $w$, residue map $\mathcal{O} \to \mathbb{F}$, and $p \in w\mathcal{O}$, $p \neq 0$. For a segment $j$, a letter $x$ of segment $j$ is *late* if it is not a twisted letter. The *rows* of a late letter $x$ are the last $r$ even letters $\mathrm{row}(j, x, 0), \dots, \mathrm{row}(j, x, r - 1)$ of segment $j$ below $x$. Recall from Section 8 the $w$-level $s(j, x) = \lfloor B(j, x)/(k^2Y)\rfloor$, where $B(j, x)$ is the degree of the oldest letter divided by $p^{\mathrm{dist}(j, x)}$.

**Definition 5.10.2 (Discriminant).** For a late letter $x$ of segment $j$ let
$$\det\nolimits_{j,x} = \det\big(X_{\mathrm{row}(j,x,a),\,c}\big)_{0 \leq a, c < r},$$
the $r \times r$ minor of the plane variables in the rows of $x$. Put $\Delta_j = \prod_x \det_{j,x}^{s(j,x)}$, the product over the late letters of segment $j$. The *discriminant* is
$$\Delta = \prod_{j < J}\varphi_j(\Delta_j),$$
where $\varphi_j$ is the segment map of Section 4, which carries a polynomial in the plane variables of segment $j$ into the ring of all positions.

Each minor $\det_{j,x}$ has degree $r$ in the variables of its rows, so $\Delta$ is multihomogeneous. Let $E_t$ be its degree at the position $t$, and put $a'_t = d_t - E_t$, where $d_t$ is the degree of the generators of $N$.

**Definition 5.10.3 (Coarse generators).** For a segment $j$ let $R_j = \lfloor\log_p(a/(8Yk^2N_s\,p^{\mathrm{dist}}))\rfloor$, with $\mathrm{dist}$ the distance of the first twisted letter of segment $j - 1$, and let $\varphi'_j$ be the substitution that sends the variable $X_{v,c}$ of a letter $v$ to $X_{\mathrm{pos}(v),c}^{\,p^{\mathrm{dist}(j,v) + R_j}}$. A *coarse label* is an exponent vector $l$ with $l(\mathrm{pos}(x), c) < p^{\mathrm{dist}(j,x) + R_j}$ for every late letter $x$ of every segment $j$ and every column $c$. For degrees $b$ of the letters of segment $j$, let $M_j(b)$ be the segment module of Section 4 at segment $j$, with $w$-levels $(r + K)N_s + 1$, thresholds two thirds of the degree of the oldest letter and order bounds as in Section 8, cut down to the polynomials of letter degrees $b$ whose exponents at the plane variables of the twisted letters are below the bound $Q_c(j)$. A *coarse generator* is a polynomial
$$u = \Big(\prod_{j < J}\varphi'_j(y_j)\Big)\,X^l, \qquad y_j \in M_j(b_j),$$
with $l$ a coarse label and $u$ homogeneous of degree $a'$.

The coarse generators are the generators of $N$ seen at a coarser scale: the Frobenius substitution $\varphi'_j$ replaces each variable by a $p$-power, and the label $l$ records the low digits. The discriminant makes up the degree $E$ that the substitution loses.

**Lemma 5.10.4 (Generators modulo the uniformizer).** Let the datum be admissible of the second kind and let $C_0 \geq 32$. Assume the hypotheses of the segment data and $C_{La}, C_k \geq C_0$. Then for every coarse generator $u$ there is a generator $g$ of $N$ with
$$\Delta\,u \equiv g \pmod{w}.$$

Lean: `Formalism.MainNotions.SelectionLemmas.Pf.generator_modulo_uniformiser_of_adm`.

*Proof.* We use three of the thirteen conditions of admissibility: the additivity of the torus valuations (the first half of the eighth condition), the ninth condition, and the twelfth condition, which says that each segment module is the image under the renaming of letters of the integral segment module.

First, the top counts. Each leading letter occurs in at most two segments, so for $C_0 \geq 32$ the top degree of each $t \in T$ is at least $\frac{9}{10}\deg_t$, and the exponents are at most the degrees, as in the proof of [the good path weight](/entry/good-path-weight/).

Second, the column words. Write $\Delta_j y_j$ as a sum of products of columns. The rows of distinct late letters are distinct, so each late letter contributes its own minor. The top counts, the bound $\deg \leq p^{\mathrm{dist}}$ on the letter degrees and the bound of the multiplicities by a power of $p$ give the column conditions of the segment module: the torus valuations of a column word add, by additivity, and stay above the thresholds. The order bounds of the oldest letters give the order condition on words. The late rows give the letters that a column word may use. With these three facts and the twelfth condition, each column word of $\Delta_j y_j$ reduces, modulo $w$, to a column word of an element of the segment module at the levels of $N$. The reduction uses that in characteristic $p$ a $p^e$-th power of a sum is the sum of the $p^e$-th powers, applied to the substitution $\varphi'_j$.

Third, the assembly. The coarse label $l$ factors over the segments, because its exponents at a late letter are below $p^{\mathrm{dist} + R_j}$. The discriminant is multihomogeneous and nonzero modulo $w$, because the late vectors have distinct top letters; so the degrees of $\Delta u$ are determined, and equal $E + a' = d$. The image of a segment polynomial under $\varphi_j$ is multihomogeneous, and the degree of the product over the segments is determined by the degrees of the factors. The top degree of $\Delta u$ is compared with the top degree of the generators of $N$ using the top counts. Together these show that the reduction of $\Delta u$ is the reduction of a product over the segments of elements of the segment modules, times a monomial, in degree $d$: that is, of a generator $g$ of $N$. $\square$

In Section 8 the lemma is combined with the nonvanishing of $\Delta$ modulo $w$: multiplication by $\Delta$ is injective on the residue ring, so the residues of the coarse generators span a space of dimension at most the rank of the residues of the generators of $N$. The count of coarse generators then gives the rank bound $p^{-n'rK}\beta$.

**Remark 5.10.5 (Formalization).** The tableau count used in the first lemma is the third part `admB3` of `AdmB` (ValuationLowestDegreeRename.lean:84), which ignores its datum, so `atypical_path_small_weight` (SegmentDegree/TypOfTypical.lean:169) uses the datum only through a datum-free hypothesis. It applies `BranchingDimensions.Top.lemma_t_one` with the prime argument $13$; the comparison of typicality is `typ_of_Typical` (line 136). The coarse objects are in SegmentDegree/Coarse.lean (`Dl` line 31, `lamGen` line 78, `GeneratorModuloUniformiser` line 95). In DiscriminantNonzeroModUniformiser.lean the proof of `generator_modulo_uniformiser_of_adm` (line 13) computes `top_count_lower_bounds` inline (line 17), although the same fact is the theorem at line 25. The segment map `phSeg`, the ninth condition `DefiniteRankOne` and the steps `column_conditions_of_numeric_bounds`, `word_order_bound_of_numeric_bound`, `allowed_letters_of_late_rows`, `column_word_reduction_of_four`, `frobenius_reduction_product` and `generator_of_segment_reductions` were not unfolded; the proof above follows their statements and the order in which they are combined.
