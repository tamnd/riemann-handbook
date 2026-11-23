---
title: Weights of branching paths
decls:
  - Formalism.InvariantFactorPaths.BranchingDimensions.Top.lemma_t_one
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Weights of branching paths

This section bounds the dimension attached to a branching path of highest weights. A path records how a highest weight of $\mathrm{GL}_k$ changes when we tensor in turn with symmetric powers of the standard representation and of its dual. The weight of the path is the Weyl dimension of its last stage, restricted to a block of $K$ rows. We prove that this weight is at most a fixed multiple of a product of binomial coefficients, and that it is exponentially smaller when the path is atypical, that is, when it moves too much mass at some step. The bound feeds [the small weight of atypical paths](/entry/atypical-path-small-weight/), which sums it over all atypical paths. The tools are the [Pieri rule](/learn/combinatorics/#the-pieri-and-littlewood-richardson-rules), the [Weyl dimension formula](/learn/representations/#highest-weights-and-branching) and elementary bounds for [binomial coefficients](/learn/combinatorics/#binomial-coefficients-factorials-and-divided-powers).

### Paths

**Definition 8.3.1 (Path data).** Path data consist of integers $r, K, N_s \geq 0$, a sign $v_i \in \{+, -\}$ for each step $i \geq 1$, and a size $B_i \in \mathbb{N}$ for each step. Put $k = r + K$, $n_0 = N_s - r$ and $k' = K - 2N_s$ (truncated subtraction). The data are *well formed* if $r \geq 1$, $K \geq 1$, $3r \leq N_s$, and $v_i = +$ for $1 \leq i \leq r$ and for $n_0 < i \leq N_s$. Put $\beta = \sum_{i=1}^{n_0} B_i$.

For $\lambda, \mu \in \mathbb{Z}^k$, say that $\mu / \lambda$ is a *horizontal strip* if $\lambda_m \leq \mu_m$ for all $m < k$ and $\mu_{m+1} \leq \lambda_m$ for $m + 1 < k$. A weight $\lambda$ is *dominant* if $\lambda_0 \geq \lambda_1 \geq \dots \geq \lambda_{k-1}$, and its size is $|\lambda| = \sum_m \lambda_m$.

**Definition 8.3.2 (Path).** A *path* is a sequence $\mu^{(0)}, \dots, \mu^{(N_s)}$ in $\mathbb{Z}^k$ with:

1. $\mu^{(0)} = 0$, and every $\mu^{(i)}$ is dominant;
2. for $1 \leq i \leq N_s$, $\mu^{(i)} / \mu^{(i-1)}$ is a horizontal strip if $v_i = +$, and $\mu^{(i-1)} / \mu^{(i)}$ is a horizontal strip if $v_i = -$;
3. for $1 \leq i \leq n_0$, $|\mu^{(i)}| - |\mu^{(i-1)}| = B_i$ if $v_i = +$, and $|\mu^{(i-1)}| - |\mu^{(i)}| = B_i$ if $v_i = -$;
4. for $1 \leq i' \leq r$ and $m < i'$, $\mu^{(n_0 + i')}_m = \beta$.

By the Pieri rule, conditions 1 to 3 say that $\mu^{(i)}$ runs through the highest weights that occur when the representation of highest weight $\mu^{(i-1)}$ is tensored with $\mathrm{Sym}^{B_i}$ of the standard representation ($v_i = +$) or of its dual ($v_i = -$). Condition 4 fixes the first $i'$ rows at the last $r$ steps to the total size $\beta$.

**Definition 8.3.3 (Weight and rank).** For $n \geq 1$ and $\lambda \in \mathbb{Z}^n$ put
$$\dim_n(\lambda) = \prod_{0 \leq i < j < n} \frac{\lambda_i - \lambda_j + j - i}{j - i}.$$
The *weight* of a path is $\mathrm{wt}(\mu) = \dim_K(\mu^{(N_s)}_r, \mu^{(N_s)}_{r+1}, \dots, \mu^{(N_s)}_{r+K-1})$, the value at the last $K$ rows of the last stage. The *rank* of the data is
$$A = \prod_{i=1}^{n_0} \binom{B_i + k - 1}{k - 1}.$$

For dominant $\lambda$, $\dim_n(\lambda)$ is the dimension of the irreducible representation of $\mathrm{GL}_n$ of highest weight $\lambda$, by Weyl's dimension formula. The number $\binom{B + k - 1}{k - 1}$ is the dimension of $\mathrm{Sym}^B$ of a space of dimension $k$, so $A$ is the dimension of the tensor product of the symmetric powers at the first $n_0$ steps.

### Typical paths

The last $r$ steps are vector steps whose first rows are fixed, and the bound below asks that the mass moved at each later step stays below a threshold. For a stage $\mu^{(i)}$ put $\delta_i = \max(i - n_0, 0)$ and write $s^{(i)}$ for its entries in the rows $m \geq \delta_i$, a vector of length $k - \delta_i$. For a vector $\lambda$ of length $n$ put
$$\mathrm{tail}^{+}(\lambda) = \sum_{m < n} \max(\lambda_m, 0), \qquad \mathrm{tail}^{-}(\lambda) = \sum_{m < n} \max(-\lambda_m, 0).$$
For $r < i \leq N_s$ let $\mathrm{Bo}_i$ be the size $B_l$ of the vector step $l < i$, $l \leq n_0$, that comes $r - (i - n_0)$ places before the last such step (and $0$ if there is none).

**Definition 8.3.4 (Typical path).** Let $X = (X_i)$ be real thresholds. A path is *typical for $X$* if:

1. $\mathrm{tail}^{+}(s^{(i-1)}) - \mathrm{tail}^{+}(s^{(i)}) \leq X_i$ for $1 \leq i \leq N_s$ with $v_i = -$;
2. $\mathrm{tail}^{-}(s^{(i-1)}) - \mathrm{tail}^{-}(s^{(i)}) \leq X_i$ for $r < i \leq N_s$ with $v_i = +$;
3. $\frac{2}{3}\mathrm{Bo}_i \leq \mu^{(i-1)}_{r-1}$ for $r < i \leq N_s$.

**Definition 8.3.5 (Size hypotheses).** Let $a \in \mathbb{R}$ and let $p$ be a prime. The data satisfy the *size hypotheses* for $(a, p)$ if:

1. $a \geq 3$ and $p \geq 13$;
2. $k \leq B_i \leq 2a$ for $1 \leq i \leq n_0$;
3. if $b_0, b_1, \dots$ are the sizes $B_l$ of the vector steps $l \leq n_0$, listed from the last to the first, then $p^2 b_{l+1} \leq 5 b_l$; the same holds for the covector steps;
4. $v_i = +$ for $n_0 - r < i \leq n_0$;
5. $N_s + r \leq K$, $2r \leq N_s$, $k \leq 2k'$ and $N_s \leq a$.

Condition 3 says that the sizes of the steps of each sign grow by a factor of at least $p^2/5$ toward the end. *Threshold data* are a real $\Lambda > 0$ and reals $b_i > 0$ for $r < i \leq N_s$ with $B_l \leq 4 b_i / p$ for $1 \leq l < i$, $l \leq n_0$. They give the thresholds $X_i = \Lambda b_i / (p k)$.

**Theorem 8.3.6 (Weight of a path).** Let the path data be well formed and satisfy the size hypotheses for $(a, p)$, and let $(\Lambda, b)$ be threshold data. Put $E = 9 N_s^2 \log(1 + 2aN_s)$. For every path $\mu$,
$$\mathrm{wt}(\mu) \leq e^{E} A.$$
If $\mu$ is not typical for the thresholds $X_i = \Lambda b_i/(pk)$, then
$$\mathrm{wt}(\mu) \leq \exp\Bigl(E - \min\Bigl(\frac{\Lambda k'}{16 k}, \frac{k'}{12}\Bigr)\Bigr) A.$$

Lean: `Formalism.InvariantFactorPaths.BranchingDimensions.Top.lemma_t_one` (also `Formalism.InvariantFactorPaths.BranchingDimensions.PathWeightBound`).

The proof compares both sides with sums of the function
$$f(y) = \sum_{j=1}^{k'} \log\frac{y + j}{j}, \qquad f(y) = \log \binom{y + k'}{k'} \text{ for } y \in \mathbb{N}.$$
We use the following facts, for $y \geq 0$ and $k' \geq 1$. The function $f$ is increasing and concave, with $f(0) = 0$ and derivative $f'(y) = \sum_{j=1}^{k'} 1/(y + j)$, and
$$\frac{k'}{y + k'} \leq f'(y) \leq \frac{k'}{y + 1}, \qquad f'(y) \geq \frac{k'}{2y} \text{ if } y \geq k'.$$
If $k' \leq y$ and $4y \leq y'$, then $f'(y') \leq f'(y)/2$.

*Proof (outline).* Let $\lambda = (\mu^{(N_s)}_{r+m})_{m < K}$ be the last $K$ rows of the last stage, so that $\mathrm{wt}(\mu) = \dim_K(\lambda)$.

Step 1 (entry bounds). By the Pieri conditions, a stage $\mu^{(i)}$ has at most as many positive entries as there are vector steps up to $i$, and at most as many negative entries as there are covector steps. So $\lambda$ has at most $N_s$ positive and at most $N_s$ negative entries. The interlacing at the last $r$ steps shows that every entry of $\lambda$ lies between $-\beta^-$ and $\beta^+$, the total sizes of the covector and vector steps. Hence $\max(\lambda_0, 0) + \max(-\lambda_{K-1}, 0) \leq \beta \leq 2aN_s$, by the size hypotheses.

Step 2 (Weyl dimension). For a dominant $\lambda \in \mathbb{Z}^K$ with at most $N_s$ positive and at most $N_s$ negative entries, $2N_s \leq K$, and $\max(\lambda_0, 0) + \max(-\lambda_{K-1}, 0) \leq A_0$, we have $\dim_K(\lambda) > 0$ and
$$\log \dim_K(\lambda) \leq \sum_m f(\max(\lambda_m, 0)) + \sum_m f(\max(-\lambda_m, 0)) + (2N_s r + 8N_s^2) \log(1 + A_0).$$
There is also a lower bound with error $-2N_s^2 \log(1 + A_0)$, which we do not need. We apply this with $A_0 = 2aN_s$. Since $2r \leq N_s$, the error is at most $E$.

Step 3 (rank). For $0 \leq A_0$ with $B_i \leq A_0$,
$$0 \leq \log A - \sum_{i=1}^{n_0} f(B_i) \leq N_s(r + 2N_s)\log(1 + A_0).$$
The lower bound is the one we need: $\sum_i f(B_i) \leq \log A$.

Step 4 (comparison of the sums). Split the steps $i \leq n_0$ by sign. List the positive entries of $\lambda$ in decreasing order as $\alpha_0 \geq \alpha_1 \geq \dots$, and the vector step sizes from the last to the first as $b_0, b_1, \dots$. By the Pieri conditions, the tails satisfy $\sum_{l \geq u} \alpha_l \leq \sum_{l \geq u} b_l$ for every $u$. By condition 3 of the size hypotheses $4b_{l+1} \leq b_l$, and $b_l \geq k \geq k'$. Write $f(\alpha_l) - f(b_l) \leq f'(b_l)(\alpha_l - b_l)$ by concavity, and sum by parts: the coefficients $f'(b_u) - f'(b_{u-1})$ are nonnegative, so
$$\sum_l f(\alpha_l) - \sum_l f(b_l) \leq \sum_u \bigl(f'(b_u) - f'(b_{u-1})\bigr)\Bigl(\sum_{l \geq u} \alpha_l - \sum_{l \geq u} b_l\Bigr) \leq 0.$$
The same holds for the negative entries and the covector steps. With Steps 2 and 3 this gives $\log \mathrm{wt}(\mu) \leq E + \log A$, the first bound.

Step 5 (atypical paths). Suppose that condition 1 fails at a covector step $i$. Since the data are well formed, a covector step has $r < i \leq n_0$. A covector step does not change the list of vector step sizes, so the positive tail at stage $i$ is at most the bound of Step 4 minus $X_i$. The tail bounds carry this deficit along the path: at the last stage some tail $\sum_{l \geq u_0} \alpha_l$ is at most $\sum_{l \geq u_0} b_l - X_i$, where $b_{u_0} = B_l$ for a vector step $l < i$. Since $f'(b_{u_0}) - f'(b_{u_0 - 1}) \geq f'(b_{u_0})/2$ by the halving property, the sum by parts gains
$$-\frac{X_i\, f'(b_{u_0})}{2} \leq -\frac{X_i\, k'}{4 b_{u_0}},$$
by $f'(y) \geq k'/(2y)$. With $X_i = \Lambda b_i/(pk)$ and $b_{u_0} \leq 4 b_i/p$ from the threshold data, the gain is at least $\Lambda k'/(16 k)$. Condition 2 is handled in the same way, with the negative entries and the covector steps. If condition 3 fails at $i$, then $0 \leq \mu^{(i-1)}_{r-1} < \frac{2}{3}\mathrm{Bo}_i$, so $\mathrm{Bo}_i > 0$, and the positive tail of stage $i - 1$ from the row of $\mathrm{Bo}_i$ on is at most its bound minus $\mathrm{Bo}_i/3$. The same argument with $X = \mathrm{Bo}_i/3$ and $b_{u_0} = \mathrm{Bo}_i$ gives the gain $(\mathrm{Bo}_i/3)\, k'/(4\mathrm{Bo}_i) = k'/12$. In each case $\log \mathrm{wt}(\mu) \leq E - \min(\Lambda k'/(16k), k'/12) + \log A$. $\square$

**Remark 8.3.7 (Formalization).** The theorem is assembled in [FinalT.lean](lean:Formalism/ThetaLogCoordinates/ResidueClassEstimates/FinalT.lean#L11) from seven statements of [StatementT.lean](lean:Formalism/ThetaLogCoordinates/ResidueClassEstimates/StatementT.lean#L16): the entry bounds, the interlacing criterion, the properties of $f$, the Weyl dimension estimate, the rank estimate, the tail bounds and the binomial deficit bound. Steps 1 to 4 and the inequalities in the preamble of the proof are these statements, which we read but whose proofs we did not open. The assembly is in [AtypicalWeightBoundOf.lean](lean:Formalism/ThetaLogCoordinates/ResidueClassEstimates/VandermondeRankEstimates/AtypicalWeightBoundOf.lean#L313); we read its three cases for Step 5, where the constants $16$ and $12$ come from. The path data, paths and typical paths are defined in [Letters.lean](lean:Formalism/ThetaLogCoordinates/ResidueClassEstimates/Letters.lean#L36). The number $\mathrm{Bo}_i$ is defined by an index into the list of vector step sizes, with the value $0$ when the index is out of range. The prime $p$ enters only through $p \geq 13$, the growth condition and the thresholds.
