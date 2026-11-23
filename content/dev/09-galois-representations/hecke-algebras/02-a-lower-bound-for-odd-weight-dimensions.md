---
title: A lower bound for odd weight dimensions
decls:
  - GlobalTheory.OddFrame.exists_frame
  - GlobalTheory.OddFrame.dim_lower_bound
  - GlobalTheory.T.oddWeight_modular_cusp_dimension_lower_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A lower bound for odd weight dimensions

The Eichler and Shimura isomorphism of the next section is proved by a count of dimensions. The space of cocycles is bounded above by a group theoretic count, and the space of modular forms plus cusp forms must be bounded below by the same number. This section proves the lower bound for a group $\Gamma$ between $\Gamma(M)$ and $\Gamma_1(N)$, $N \geq 5$, in odd weight $k \geq 3$:
$$
(k - 1)\,[\mathrm{SL}_2(\mathbb{Z}) : \Gamma] \leq 12 \bigl(\dim M_k(\Gamma) + \dim S_k(\Gamma)\bigr).
$$
The bound is used in the proof of [the Eichler and Shimura decomposition](/entry/exists-per-add-cj-per/). The proof does not use the Riemann and Roch theorem. It builds $r$ modular forms of odd weight for $\Gamma$ whose values at the $r$ cosets form an invertible matrix at every point, and then multiplies them by forms of level one.

We use the [modular forms and cusp forms](/learn/automorphic-forms/#modular-forms) of Volume 1. For a function $f$ on $\mathcal{H}$, an integer $k$ and $x \in \mathrm{SL}_2(\mathbb{Z})$, write $(f|_k x)(\tau) = (c\tau + d)^{-k} f(x\tau)$. Then $f|_k(-x) = (-1)^k f|_k x$.

**Definition 6.2.1 (Modular and cusp forms for a subgroup).** Let $\Gamma \leq \mathrm{SL}_2(\mathbb{Z})$ and $k \in \mathbb{Z}$. A *modular form of weight $k$ for $\Gamma$* is a holomorphic $f : \mathcal{H} \to \mathbb{C}$ with $f|_k \gamma = f$ for $\gamma \in \Gamma$ such that $f|_k x$ is bounded as $\mathrm{Im}\,\tau \to \infty$ for every $x \in \mathrm{SL}_2(\mathbb{Z})$. It is a *cusp form* if each $f|_k x$ tends to $0$ there. We write $M_k(\Gamma)$ and $S_k(\Gamma)$ for these spaces.

**Definition 6.2.2 (Signed coset representatives).** Let $\Gamma$ be a subgroup with $-1 \notin \Gamma$. A family $s_1, \dots, s_r$ in $\mathrm{SL}_2(\mathbb{Z})$ is a *system of signed representatives* for $\Gamma$ if every $x \in \mathrm{SL}_2(\mathbb{Z})$ is $\gamma s_i$ or $-\gamma s_i$ for some $i$ and some $\gamma \in \Gamma$, and $s_i = \pm \gamma s_j$ with $\gamma \in \Gamma$ only if $i = j$.

So the $s_i$ represent the cosets of $\{\pm 1\}\Gamma$. When $\Gamma$ has finite index and $-1 \notin \Gamma$, such a system exists and $2r = [\mathrm{SL}_2(\mathbb{Z}) : \Gamma]$.

**Definition 6.2.3 (Evaluation matrix).** Let $s_1, \dots, s_r$ be signed representatives, $w_1, \dots, w_r$ integers and $F_1, \dots, F_r$ functions on $\mathcal{H}$. The *evaluation matrix* at $\tau \in \mathcal{H}$ is the $r \times r$ matrix
$$
E(s, w, F; \tau) = \bigl( (F_j|_{w_j} s_i)(\tau) \bigr)_{i, j}.
$$
An *odd frame* for $\Gamma$ is a family with every $w_j$ odd, every $F_j \in M_{w_j}(\Gamma)$, and $\det E(s, w, F; \tau) \neq 0$ for every $\tau$.

When the weights are odd and $-1 \notin \Gamma$, changing $s_i$ to $-\gamma s_i$ multiplies row $i$ by $-1$. So whether the determinant vanishes does not depend on the choice of representatives.

**Lemma 6.2.4 (Odd frames with dual cusp frames).** Let $M \geq 1$, let $\Gamma(M) \leq \Gamma \leq \mathrm{SL}_2(\mathbb{Z})$ with $-1 \notin \Gamma$, and let $s_1, \dots, s_r$ be signed representatives for $\Gamma$. Then there are odd integers $w_1, \dots, w_r$, forms $F_j \in M_{w_j}(\Gamma)$ and cusp forms $G_j \in S_{12 - w_j}(\Gamma)$ such that $\det E(s, w, F; \tau) \neq 0$ and $\det E(s, 12 - w, G; \tau) \neq 0$ for every $\tau \in \mathcal{H}$.

Lean: `GlobalTheory.OddFrame.exists_frame`.

*Proof.* First $M \geq 3$, because $-1$ lies in $\Gamma(1)$ and $\Gamma(2)$ but not in $\Gamma$. For $M \geq 3$ there is, for each $x \notin \Gamma(M)$, a form of level $\Gamma(M)$ with $f|_k x \neq f$, for example a suitable Eisenstein series. From this one finds a point $\tau_0$ at which the maps $f \mapsto (f|_k x_i)(\tau_0)$, for $x_i$ in distinct cosets of $\Gamma(M)$, are linearly independent on the forms of level $\Gamma(M)$. A further lemma then gives odd weights $w_j$ and forms $F_j \in M_{w_j}(\Gamma)$ with $\det E(s, w, F; \tau_0) \neq 0$.

Say that a family *reduces* if one of its members $F_{j_0}$ can be traded for a form $G$ of smaller odd weight: there are holomorphic $e_j$ with $e_{j_0} \neq 0$ and a function $E_0$ such that $E_0 \cdot (G|_{w'} x) = \sum_j e_j \cdot (F_j|_{w_j} x)$ for every $x \in \mathrm{SL}_2(\mathbb{Z})$. A descent on the weights gives a family with $\det E(s, w, F; \tau_0) \neq 0$ at some point that does not reduce.

For this family the determinant vanishes nowhere. The idea is this: if $\det E(s, w, F; \tau_1) = 0$, a vector in the kernel at $\tau_1$ lets one divide a combination of the columns by a function vanishing at $\tau_1$, which is a reduction. In the same way, the matrix of the sums of the first $M$ coefficients of the expansions of $F_j|_{w_j} s_i$ in $q^{1/M}$ is invertible. Otherwise the family again reduces.

The invertibility of this leading matrix controls $E(s, w, F; \tau)^{-1}$ as $\mathrm{Im}\,\tau \to \infty$. After a diagonal change of scale, $E(s, w, F; \tau)$ tends to an invertible matrix, so $\Delta(\tau) E(s, w, F; \tau)^{-1}$ tends to $0$, where $\Delta$ is the discriminant form of weight $12$. The entries of $\Delta \cdot E^{-1}$ are then the values $G_j|_{12 - w_j} s_i$ of cusp forms $G_j$ of weight $12 - w_j$ for $\Gamma$, and their evaluation matrix is $\Delta$ times the transposed inverse, so its determinant never vanishes. $\square$

**Theorem 6.2.5 (Odd weight dimension bound).** Let $N \geq 5$ and $M \geq 1$, let $\Gamma(M) \leq \Gamma \leq \Gamma_1(N)$, and let $k \geq 3$ be odd. Then $M_k(\Gamma)$ and $S_k(\Gamma)$ are finite dimensional, and
$$
(k - 1)\,[\mathrm{SL}_2(\mathbb{Z}) : \Gamma] \leq 12 \bigl(\dim M_k(\Gamma) + \dim S_k(\Gamma)\bigr).
$$

Lean: `GlobalTheory.OddFrame.dim_lower_bound` (also `GlobalTheory.T.oddWeight_modular_cusp_dimension_lower_bound`, a second name).

*Proof.* Finite dimensionality holds for every $\Gamma$ containing some $\Gamma(M)$. Since $N \geq 5$, the group $\Gamma_1(N)$ does not contain $-1$, so neither does $\Gamma$. Choose signed representatives $s_1, \dots, s_r$, so $2r = [\mathrm{SL}_2(\mathbb{Z}) : \Gamma]$, and take an odd frame $(w, F)$ and its dual $(12 - w, G)$ from the lemma.

*Step 1.* The map
$$
\bigoplus_{j=1}^r M_{k - w_j}(\mathrm{SL}_2(\mathbb{Z})) \to M_k(\Gamma), \qquad (g_j) \mapsto \sum_j g_j F_j
$$
is injective. Indeed, if $\sum_j g_j F_j = 0$, apply $|_k s_i$. Since $g_j$ has level one, $g_j|_{k - w_j} s_i = g_j$, so $\sum_j g_j(\tau) (F_j|_{w_j} s_i)(\tau) = 0$ for all $i$. The evaluation matrix is invertible, so every $g_j(\tau) = 0$. The same argument with $G$ gives an injective map from $\bigoplus_j M_{k - 12 + w_j}(\mathrm{SL}_2(\mathbb{Z}))$ into $S_k(\Gamma)$, since a product with a cusp form is a cusp form. So
$$
\begin{aligned}
\sum_j \dim M_{k - w_j}(1) &\leq \dim M_k(\Gamma), \\
\sum_j \dim M_{k - 12 + w_j}(1) &\leq \dim S_k(\Gamma).
\end{aligned}
$$

*Step 2.* Exactly $r/3$ of the weights $w_j$ are divisible by $3$. To see this, evaluate the frame at $\rho = e^{2\pi i/3}$. The group $\Gamma_1(N)$ with $N \geq 5$ has no element of order $3$, so the stabiliser of $\rho$ in $\mathrm{PSL}_2(\mathbb{Z})$ permutes the $r$ cosets freely. Each column $\bigl((F_j|_{w_j} s_i)(\rho)\bigr)_i$ is an eigenvector of the induced signed permutation, with an eigenvalue that depends only on $w_j$ modulo $3$, and each of the three eigenspaces has dimension $r/3$. As the $r$ columns are independent, each class of weights modulo $3$ holds exactly $r/3$ columns.

*Step 3.* For $n$ even, the dimension formula in level one gives
$$
n + 5 + 3\,a_4(n) + 4\,a_6(n) \leq 12 \dim M_n(1),
$$
where $a_4(n) = 1$ if $4 \mid n$ and $-1$ otherwise, and $a_6(n)$ is $1$, $-1$ or $0$ as $n \equiv 0$, $n \equiv 2$ or otherwise modulo $6$. Here $\dim M_n(1) = 0$ for $n < 0$, and the left side is then at most $0$. Apply this to $n = k - w_j$ and $n = k - 12 + w_j$ for odd $k$ and odd $w_j$. These two numbers differ by $2w_j - 12 \equiv 2$ modulo $4$, so the terms $a_4$ cancel, and the terms $a_6$ add up to $c(k)(3\,\delta_j - 1)$, where $\delta_j = 1$ if $3 \mid w_j$ and $0$ otherwise, and $c(k) \in \{1, -1, 0\}$ depends on $k$ modulo $3$. So
$$
2k - 2 + 4\,c(k)(3\delta_j - 1) \leq 12 \bigl( \dim M_{k - w_j}(1) + \dim M_{k - 12 + w_j}(1) \bigr).
$$

*Step 4.* Sum over $j$. By Step 2, $\sum_j (3\delta_j - 1) = 0$, so the left side sums to $r(2k - 2) = (k - 1)[\mathrm{SL}_2(\mathbb{Z}) : \Gamma]$. By Step 1, the right side is at most $12(\dim M_k(\Gamma) + \dim S_k(\Gamma))$. $\square$

For $\Gamma$ without elliptic elements and without irregular cusps, the Riemann and Roch theorem gives $\dim M_k(\Gamma) + \dim S_k(\Gamma)$ for $k \geq 3$, and the bound above is then an equality. The frame argument gives the bound for every $\Gamma$ between $\Gamma(M)$ and $\Gamma_1(N)$ without the genus formula.

**Remark 6.2.6 (Formalization).** The statement with the second name is a wrapper of the first under `maxHeartbeats 1000000` ([OddWeightModularCuspDimensionLowerBoundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/OddWeightModularCuspDimensionLowerBoundStatement.lean#L8)). In the frame lemma the family $G$ is only claimed to have a nonvanishing evaluation matrix and cusp forms of weight $12 - w_j$; the leading coefficient matrix is used inside the proof and not stated. The descent, the vanishing at $\rho$ and the level one bound were read as statements; the sketches in Steps 2 and 3 and in the proof of the lemma give their mathematical content, not their formal proofs.
