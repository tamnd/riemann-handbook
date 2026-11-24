---
title: The second part of the selection
decls:
  - Formalism.MainNotions.SelectionLemmas.Pf.lemT_of_adm
  - Formalism.MainNotions.SelectionLemmas.Pf.good_path_weight_of_top_count
  - Formalism.MainNotions.SelectionLemmas.Pf.good_path_weight
  - Formalism.MainNotions.SelectionLemmas.Pf.secondPartClosed
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The second part of the selection

This section proves the second part of the selection: a large free submodule of a module spanned by generators of segment polynomials, together with a degree bound for that module. The proof counts paths of weights. Most paths are good, and good paths give independent generators, so the rank is close to the product of the dimensions of the weight spaces. The result is used by [the local model results](/entry/local-model-results/) in Volume 15. We use the frames, letters and torus valuations of Sections 1 and 4.

### The statement

We work in the unramified quadratic setting of Section 3 over $\mathcal{O}$ with $p \geq 13$, with $r \geq 2$ and $K \geq 1$. Put $k = r + K$.

**Definition 5.8.1 (Second selection statement).** Let $C_{La}$, $C_k$, $C_{rk}$ and $C_{\deg}$ be numbers. The *second selection statement* with these constants says the following. Let $\mathcal{F}$ be valid frames of rank $r$ with parameters $L_1$, $N_1$, let $\deg_t$ be degrees with $a \leq \deg_t \leq 2a$ on the set $T$ of the frames, and let $N_s$, $E_0$, $m_*$, $E'_t$, $Y$ and $Q$ satisfy:

1. each segment has at most $N_s$ letters, $N_s \leq N_1$, $N_s \leq 2|T|$ and $N_s + r \leq K$;
2. $p^{\mathrm{dist}(j, x)} \leq Q$ for each letter $x$ of segment $j$, and $Y \geq 1$;
3. $C_kN_s^2\log a \leq k$ and $128k^2N_sY^2 \leq p^{L_1 - 1}$;
4. $E'_t \leq E_0$ on $T$, and $32pYk^2N_sQ^2(E_0 + m_* + 1) \leq a$.

Put $L_a = C_{La}N_s^2\log a$. For a letter $x$ of segment $j$ let $B(j, x)$ be the degree of the oldest letter divided by $p$ to its distance. The segment modules of Section 4 with $w$-levels $m_* + \lfloor B/(k^2Y)\rfloor$, thresholds $B/2$ and order bounds
$$o(j, x) = \frac{L_a\,a}{p\,k\,p^{\mathrm{dist}(j,x)}} + c_x\,a\,p^{-L_1 - \mathrm{dist}(j,x)}$$
with $c_x = 10$ for even $x$ and $c_x = 1$ for odd $x$, give generators in degree $d_t = \deg_t - E'_t$ on $T$ (and $0$ off $T$). Let $N$ be their span and put
$$\beta = \Big(1 - \frac{C_{rk}|T|r^2k}{Y}\Big)\prod_{t \in T}\binom{\deg_t + k - 1}{k - 1}.$$
Then there is a submodule $S \subseteq N$ with a complement and a basis of generators, with
$$\mathrm{rank}\,S \geq p^{-n'rK}\beta, \qquad \mathrm{rank}\,S \geq \beta/\#\mathrm{Gr}_r(\mathbb{F}^k)$$
for every finite field $\mathbb{F}$ with $p^{n'}$ elements, where $\mathrm{Gr}_r(\mathbb{F}^k)$ is the set of $r$-planes; and every monomial of every element of $N$ has degree at most $C_{\deg}|T|\big(L_aa/(pk) + ap^{-L_1} + kQ\big)$.

The product of binomial coefficients is the dimension of the space of polynomials of degree $\deg_t$ in $k$ variables for each $t \in T$, so $\beta$ is this full dimension up to a factor near $1$.

**Definition 5.8.2 (Admissibility of the second kind).** A datum is *admissible of the second kind* if thirteen conditions hold. Among them are the correspondence between paths and pairs of frames, the additivity of the torus valuations, and three classical facts on [semistandard tableaux](/learn/combinatorics/#partitions-and-young-tableaux): the number of tableaux of a dominant weight is the Weyl dimension formula; the branching rule from $\mathrm{GL}_{m+1}$ to $\mathrm{GL}_m$; and the [Pieri rule](/learn/combinatorics/#the-pieri-and-littlewood-richardson-rules), in the form that a tableau count times $\binom{b+m}{m}$ is the sum of the counts over horizontal strips of size $b$.

### Paths

A *letter list* of length $N$ is a sequence of letters, each a vector or a covector. A *Pieri path* with steps $B_1, \dots, B_N$ in $k$ coordinates is a sequence of dominant weights $\mu_0 = 0, \mu_1, \dots, \mu_N$ such that $\mu_i$ is obtained from $\mu_{i-1}$ by adding a horizontal strip of size $B_i$ if letter $i$ is a vector, and by removing one if it is a covector. Split each weight into a plane part (the first $r$ coordinates) and a tangent part.

**Definition 5.8.3 (Path hypotheses).** Data $(N, n_0, r, K, B, \mathrm{od}, b, a, L_a, p)$ satisfy the *path hypotheses* if $N = n_0 + r$, $r \geq 1$, $a \geq 3$, $p \geq 13$, $k \leq B_i \leq 2a$ for $i < n_0$, the $B_i$ of letters of the same kind grow by at least $p^2/5$, the first $r$ and the last letters are vectors, $2r \leq n_0$, $N + r \leq K$, $k/2 \leq K - 2N$, $N \leq a$, $L_a > 0$, and the index map $\mathrm{od}$ and the weights $b_i > 0$ satisfy order conditions (for $i \geq r$, $\mathrm{od}(i) < i$ is a vector with exactly $r$ vectors in $[\mathrm{od}(i), i)$, and $B_l \leq 4b_i/p$ for $l < i$).

A path is *admissible* if its first $n_0$ steps have the given degrees and its head after $n_0$ is fixed. For a path $\mu$ let $\Xi_i = L_ab_i/(pk)$.

**Definition 5.8.4 (Typical and good paths).** A path is *typical* if, at each step, the positive part of the weight drops by at most $\Xi_i$ at a covector, the negative part drops by at most $\Xi_i$ at a vector with $i \geq r$, and for $i \geq r$ the last plane coordinate is at least $\frac{2}{3}B_{\mathrm{od}(i)}$. It is *good* if, for $i \geq r$, the last plane coordinate is at least $\frac{2}{3}B_{\mathrm{od}(i)}$, the tangent part grows by at most $\Xi_i + 2B_{\mathrm{od}(i)}$ at a vector, and the plane part drops by at most $\Xi_i$ at a covector.

A *weighted path* is a path $\mu$ together with a semistandard tableau of shape the tangent part of $\mu_N$. Let $\mathrm{rk} = \prod_{i < n_0}\binom{B_i + k - 1}{k - 1}$ and $\ell_0 = \log(1 + 2aN)$.

**Definition 5.8.5 (Lemma T).** *Lemma T* says: under the path hypotheses the set of good weighted paths is finite and has at least
$$\Big(1 - e^{11N^2\ell_0 - \min(L_a, k)/32}\Big)\,\mathrm{rk}$$
elements.

**Lemma 5.8.6 (Lemma T).** For every datum that is admissible of the second kind, Lemma T holds.

Lean: `Formalism.MainNotions.SelectionLemmas.Pf.lemT_of_adm`.

*Proof.* The tableau count, the branching rule and the Pieri rule give that the number of weighted paths is exactly $\mathrm{rk}$. The number of admissible paths is at most $e^{2N^2\ell_0}$. For an atypical path, the tableau count is at most
$$e^{9N^2\ell_0 - \min\left(\frac{L_a(K - 2N)}{16k}, \frac{K - 2N}{12}\right)}\,\mathrm{rk},$$
by the tableau count again. A typical path is good. So the weighted paths that are not good are those over atypical paths, and their number is at most $e^{2N^2\ell_0}$ times the bound above. With $k/2 \leq K - 2N$ this gives the claim. $\square$

### Good path weight

For segment data in the sense of Section 4, a segment $j$ and a letter degree $b$ admissible for $j$, let $\mathcal{T}(j, b)$ be the set of good indices: weighted paths through the segment that are good for the data. Let $B_w$ and $m_0$ be the degree bounds of the twisted letters.

**Definition 5.8.7 (Good path weight).** The *good path weight* with constant $C_0$ says: for segment data with their hypotheses and $C_{La}, C_k \geq C_0$, for every segment $j$ and every admissible $b$, the set $\mathcal{T}(j, b)$ is finite and
$$|\mathcal{T}(j,b)| \geq (1 - a^{-N_s^2})\prod_x\binom{b_x + k - 1}{k - 1}\prod_{i < r}\binom{B_{w,i} - m_0 + k - 1}{k - 1},$$
where $x$ runs over the base letters of segment $j$ and $i$ over the twisted letters of segment $j - 1$.

The *top count bounds* with constant $C_0$ say: for segment data with $C_{La}, C_k \geq C_0$, the top degree of each $t \in T$ is at least $\frac{9}{10}\deg_t$, and the exponents are at most the degrees.

**Proposition 5.8.8 (Good path weight from top counts).** Let the datum be admissible of the second kind, and assume the top count bounds with $C_0 = 1088$. Then the good path weight holds with $C_0 = 1088$.

Lean: `Formalism.MainNotions.SelectionLemmas.Pf.good_path_weight_of_top_count`.

*Proof.* The top count bounds give a letter dictionary: each segment, with its degrees, satisfies the path hypotheses for suitable $n_0$ and $\mathrm{od}$, with $b_i = a/p^{\mathrm{dist} + R_j}$; the paths of the segment are the admissible paths; good paths in the sense of Lemma T are good for the segment; the number $\mathrm{rk}$ is the product of binomials in the definition; and $e^{11N^2\ell_0 - \min(L_a, k)/32} \leq a^{-N_s^2}$. Now apply [Lemma T](/entry/lem-t-of-adm/). $\square$

**Theorem 5.8.9 (Good path weight).** For every datum that is admissible of the second kind, the good path weight holds with $C_0 = 1088$.

Lean: `Formalism.MainNotions.SelectionLemmas.Pf.good_path_weight`.

*Proof.* The top count bounds hold for every $C_0 \geq 32$, since each leading letter occurs in at most two segments. Apply [the Proposition](/entry/good-path-weight-of-top-count/). $\square$

**Theorem 5.8.10 (Second part of the selection).** For every datum $\mathcal{D}$ that is admissible of the second kind, there is $C_0 > 0$ such that for all $C_{La}, C_k \geq C_0$ there are $C_{rk}, C_{\deg} > 0$ for which the second selection statement holds.

Lean: `Formalism.MainNotions.SelectionLemmas.Pf.secondPartClosed`.

*Proof.* Take $C_0 = 1088$ and $C_{rk} = 1$. A rank bound gives the statement, with a degree bound and a selection lemma that hold for every datum. The rank bound follows from a count and two facts modulo the uniformizer: the discriminant is nonzero modulo the uniformizer, and the generators are independent modulo the uniformizer (this uses admissibility). The count follows from a weight bound, a padding fact, a sum fact and a segment statement. The segment statement follows from five parts: membership of the family elements in the segment modules, their linear independence, finiteness of the segment modules, the [good path weight](/entry/good-path-weight/), and a monotonicity bound that compares the good indices with the indices over residue classes of exponents. Membership, independence and the weight bound use admissibility. $\square$

**Remark 5.8.11 (Formalization).** The statement is `SelectionLemmas.Conclusion2` (ValuationLowestDegreeRename.lean:18), which ignores `_D`; `SecondPartClosed` (line 274) keeps the hypothesis `AdmB D` (line 268), so the theorem is conditional on the thirteen parts of `AdmB`. Three of these parts are classical theorems taken as hypotheses: `admB3` is the count of semistandard tableaux by the Weyl dimension formula, `ColumnFamilyLowerSet` is the branching rule, and `GenericProjectionCriterion` is the Pieri rule (lines 84, 90, 97); the names do not describe the content. `ColumnFamilyClosure` (line 106) is the count $q^{r(k-r)} \leq \#\mathrm{Gr}_r$, also a true fact taken as a hypothesis. `lemT_of_adm` and `good_path_weight_of_top_count` use only the parts 3, 4 and 5 of `AdmB`, through `path_weight_eq_rank` (SegmentDegree/ProdFromSelfEqOne.lean:110); `good_path_weight_of_top_count` calls `path_weight_eq_rank` a second time. The constant 1088 is fixed in `second_estimate_of_restrictions` (SegmentDegree.lean:21), while `top_count_lower_bounds` needs only $C_0 \geq 32$. There are two more definitions named `SecondPartClosed` and two more named `AdmB` (ProjectionLemmaBaseLevel.lean:239, 260; StatementOfDegreeAndBound.lean:499, 512). The tableau predicate `IsSt`, the segment data `Dat` and its fields, `Gen`, `XX'`, `nPl`, `vsDeg`, and the proofs of `path_count_finite`, `atypical_path_small_weight`, `typical_path_orders_small`, `TE.letter_dictionary_bounds`, `top_occurs_in_at_most_two_segments`, `second_estimate_of_rank_bound`, `restRank_of`, `restCount_of`, `restSeg_of`, `restMon_of`, `restMem_of`, `restInd_of`, `restLam_of`, `restPad`, `restSum`, `discriminant_nonzero_mod_uniformiser` and `generator_modulo_uniformiser_of_adm` were not unfolded; the description of their roles follows their statements and names.
