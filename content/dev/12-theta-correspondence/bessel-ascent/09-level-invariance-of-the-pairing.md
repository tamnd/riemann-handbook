---
title: Level invariance of the pairing of points
decls:
  - GlobalTheory.T.normalisedKernelExpansionSum_levelInvariant
  - GlobalTheory.ExpansionInvariance.levels_invariant
  - GlobalTheory.T.expansionPairing_invariant_inner_vertex_level
  - GlobalTheory.ExpansionInvariance.pairPts_update_top
  - GlobalTheory.T.expansion_product_invariant_inner_vertex_level
  - GlobalTheory.ExpansionInvariance.product_invariant
  - GlobalTheory.T.unfoldingExpansion_productFunction_localInvariant
  - GlobalTheory.TopLevelInv.local_invariant
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Level invariance of the pairing of points

This section proves that the pairing of points of an expansion does not change when one point of the grid moves by an element of its level group. The pairing is a finite sum of brackets of two chains of theta kernels, one along the top nodes and one along the last row. The result is used by [the twisted pairing identity](/entry/twisted-pairing-identity/), which folds a period into a finite sum over classes. The proof moves each translation into the [Weil representation](/learn/theta/#the-weil-representation) and then into the [Schrödinger model](/learn/theta/#the-schrdinger-model), where it becomes a scalar identity at each place.

### The pairing of points

Fix a grid with $m \ge 2$ rows, a grid choice $S$ for a set $U$ of types, a type $t \in U$ and a datum $\Phi$. Let $P$ be the finite set of local places of the grid for $t$. At each $w \in P$ the grid gives a local unfolded term $u_w$, with a level group $\mathrm{pr}_j(u_w)$ at each top node $j$. A *coset family* $\beta$ is a choice of a coset at each $w \in P$, and $\beta$ is in the *support* if each coset is in the support of the local unfolded term.

A *pure datum* $d$ is a pair of families: theta data $d_{1,j}$ on the column edges $j < m$, between the top nodes $X_j$ and $X_{j+1}$, and theta data $d_{2,i}$ on the row edges $i < m$ of the last row. Each theta datum has a finite function $f$ on its symplectic space. Let $\tau$ be a finitely supported function on pure data.

**Definition 8.9.1 (Expansion).** The function $\tau$ is an *expansion* at $\beta$ if there is an idempotent sum $e$ for $P$ such that:

1. each datum in the support of $\tau$ has the place set $P$, the idempotent $e$ and the scalar $1$ on each edge;
2. for all points $x$ of the column spaces and $y$ of the row spaces whose entries are fixed by $e$,

$$\begin{aligned}
&\sum_d \tau(d) \prod_{j} f_{d,1,j}(x_j) \prod_{i} f_{d,2,i}(y_i) \\
&\quad = \prod_{w \in P} u_w\bigl(x(w), y(w)\bigr).
\end{aligned}$$

Here $x(w)$ and $y(w)$ are the local arguments at $w$, read in the frames of the grid choice.

The *top level group* $K^{\mathrm{top}}_j$ is the group $K^{+}$ of the grid for $j = 0$. For $0 < j < m$ it is the product over $w \in P$ of the local groups $\mathrm{pr}_j(u_w)$, read in the frame of the grid choice at $X_j$. The *row level group* $K^{\mathrm{row}}_i$ is the product over $w \in P$ of the given local levels at the vertex $(i, m)$.

**Definition 8.9.2 (Pairing of points).** Let $x = (x_j)_{j \le m}$ be finite adelic points of the top nodes, and let $y = (y_i)_{i \le m}$ be finite adelic points of the vertices of the last row. For a pure datum $d$, the *column map* $C_d(x)$ is the composite of the theta kernels of the theta functions of $d_{1,j}$ at the points $x_j u_j$ and $x_{j+1} u_{j+1}$, where $u_j$ is a fixed element of the grid choice. The *row map* $R_d(y)$ is built in the same way. The *pairing of points* is the bilinear form

$$P_\tau(x, y) = \sum_d \tau(d)\, \bigl[C_d(x), R_d(y)\bigr],$$

where $[\cdot, \cdot]$ is the bracket that pairs the weights at $X_m$ with the weights at the vertex $(m, m)$.

### The four invariances

**Theorem 8.9.3 (Level invariance of the pairing).** Let $\mu_0$ be a type with the level condition, let $p_{de}$ and $p'_{de}$ be prime to $Q_S q$, and let the absolute norm of the ideal $\mathfrak{c}_K$ lie in no prime of the finite set $Q(t)$. Let $\beta$ be in the support and let $\tau$ be an expansion at $\beta$ whose data have theta vectors. Let $\Psi$ and $F$ be vector valued functions on the points of $X_0$ and of the vertex $(0, m)$. Then:

1. for $0 < j < m$ and $k$ with image in $K^{\mathrm{top}}_j$, moving $x_j$ to $x_j k$ does not change $P_\tau(x, y)(\Psi(x_0), F(y_0))$;
2. if $\Psi(x k) = \Psi(x)$ for all $k \in K^{+}$, then moving $x_0$ to $x_0 k$ with $k \in K^{\mathrm{top}}_0$, and $\Psi(x_0)$ to $\Psi(x_0 k)$, does not change the value;
3. for $0 < i < m$ and $k$ with image in $K^{\mathrm{row}}_i$, moving $y_i$ to $y_i k$ does not change the value;
4. if $x_m = \iota(y_m)$ for the embedding $\iota$ of the top decomposition, then moving $y_m$ to $y_m k$ with $k \in K^{\mathrm{row}}_m$ and $x_m$ to $\iota(y_m k)$ together does not change the value.

Lean: `GlobalTheory.T.normalisedKernelExpansionSum_levelInvariant` (also `GlobalTheory.ExpansionInvariance.levels_invariant`, the proof).

*Proof.* Each part is one theorem. Part 1 is the theorem on the inner top vertices below. Parts 2, 3 and 4 are the theorems on the base point, on the inner row vertices and on the last vertex. $\square$

### The inner top vertices

For a pure datum $d$, an index $j$ with $j + 1 < m$ and a point $g$ of $X_{j+1}$, the *moved column* of $d$ is the family of theta functions that is $\omega(1, g) v_{d,j}$ at the edge $j$, $\omega(g, 1) v_{d,j+1}$ at the edge $j + 1$, and $v_{d,j'}$ at the other edges. Here $v_{d,j'}$ is the theta function of $d_{1,j'}$ and $\omega$ is the Weil representation of the edge. The *moved function* $f^{g}_{d,j'}$ is $f_{d,1,j'}$ composed with the action of $g^{-1}$ on the argument at the two edges $j$ and $j + 1$.

**Theorem 8.9.4 (Invariance at an inner top vertex).** Assume the hypotheses of the previous theorem. Let $0 < j < m$ and let $k$ be a point of $X_j$ with image in $K^{\mathrm{top}}_j$. Then

$$\begin{aligned}
&P_\tau(x_j \mapsto x_j k,\ y)\bigl(\Psi(x_0), F(y_0)\bigr) \\
&\quad = P_\tau(x, y)\bigl(\Psi(x_0), F(y_0)\bigr).
\end{aligned}$$

Lean: `GlobalTheory.T.expansionPairing_invariant_inner_vertex_level` (also `GlobalTheory.ExpansionInvariance.pairPts_update_top`, the proof).

*Proof.* Write $j = j' + 1$, let $u = u_j$ and let $g = u^{-1} k u$, so that $x_j k u = x_j u g$. The point $x_j$ enters only the kernels of the edges $j'$ and $j$. A theta kernel satisfies $K(f)(a k_1, b k_2) = K(\omega(k_1, k_2) f)(a, b)$. So the column map at the moved point is the column map of the moved column of $d$ at $x$. The pairing depends only on the function

$$(w, z) \mapsto \sum_d \tau(d) \prod_{j''} c_{d,j''}(w_{j''}) \prod_i r_{d,i}(z_i)$$

of its column and row theta functions, since these are theta functions and the Weil action keeps theta functions. So the claim follows from the next theorem at the edge $j'$. $\square$

**Theorem 8.9.5 (The product function is invariant).** Assume the hypotheses of the level invariance theorem. Let $j + 1 < m$, let $k$ be a point of $X_{j+1}$ with image in $K^{\mathrm{top}}_{j+1}$, and let $g = u_{j+1}^{-1} k u_{j+1}$. Then for all $w$ and $z$,

$$\begin{aligned}
&\sum_d \tau(d) \prod_{j'} v^{g}_{d,j'}(w_{j'}) \prod_i r_{d,i}(z_i) \\
&\quad = \sum_d \tau(d) \prod_{j'} v_{d,j'}(w_{j'}) \prod_i r_{d,i}(z_i),
\end{aligned}$$

where $v^{g}_{d}$ is the moved column of $d$ and $r_{d,i}$ is the theta function of $d_{2,i}$.

Lean: `GlobalTheory.T.expansion_product_invariant_inner_vertex_level` (also `GlobalTheory.ExpansionInvariance.product_invariant`, the proof).

*Proof.* If $\tau = 0$, both sides are $0$. Otherwise the expansion gives one idempotent sum $e$ shared by the data. From one datum, the theta vectors give for each edge a linear map $T$ that is a place model of the vacuum of the edge for $e$, and each theta function of the expansion is $T$ of its finite function. The vacuum at the edge $j$ moves by a scalar: $\omega(1, g)$ of the vacuum is $c_1$ times $T_j$ of a translate of the half indicator function. In the same way $\omega(g, 1)$ of the vacuum at the edge $j + 1$ is $c_2$ times $T_{j+1}$ of a translate. So $\omega(1, g) v_{d,j} = c_1 T_j(f^{g}_{d,j})$ and $\omega(g, 1) v_{d,j+1} = c_2 T_{j+1}(f^{g}_{d,j+1})$. The next theorem gives a pointwise identity of finite sums of products of finite functions. Two such sums that agree at each point still agree after a fixed linear map is applied to each factor. Apply this with the maps $T$. $\square$

### The local identity

**Theorem 8.9.6 (Local invariance of the product function).** Assume the hypotheses of the level invariance theorem. Let $j + 1 < m$, let $k$ be a point of $X_{j+1}$ with image in $K^{\mathrm{top}}_{j+1}$, and let $g = u_{j+1}^{-1} k u_{j+1}$. Let $e$ be an idempotent sum for $P$ such that each datum in the support of $\tau$ has the idempotent $e$ on each column edge. Let $T_1$ and $T_2$ be place models for $e$ of the vacua at the edges $j$ and $j + 1$, and let $c_1, c_2$ be scalars with

$$\begin{aligned}
\omega(1, g)\, v_j &= c_1\, T_1\bigl(h_j(\,\cdot\, g)\bigr), \\
\omega(g, 1)\, v_{j+1} &= c_2\, T_2\bigl(h_{j+1}(g^{-1} \,\cdot\,)\bigr),
\end{aligned}$$

where $v_j$ is the vacuum and $h_j$ is the half indicator function of the standard lattice at the edge $j$. Then for all $x$ and $y$,

$$\begin{aligned}
&\sum_d \tau(d)\, c_1 c_2 \prod_{j'} f^{g}_{d,j'}(x_{j'}) \prod_i f_{d,2,i}(y_i) \\
&\quad = \sum_d \tau(d) \prod_{j'} f_{d,1,j'}(x_{j'}) \prod_i f_{d,2,i}(y_i).
\end{aligned}$$

Lean: `GlobalTheory.T.unfoldingExpansion_productFunction_localInvariant` (also `GlobalTheory.TopLevelInv.local_invariant`, the proof).

*Proof.* The vacua are nonzero, since their norms are positive. So the scalars $c_1$ and $c_2$ are unique. The Weil action of a conjugated level element moves the vacuum by a character, so $c_1$ and $c_2$ are the values of these characters. The left side is $c_1 c_2$ times the right side at the moved point $x^{g}$.

Let $e'$ be the idempotent of the expansion. A point is fixed by $e'$ if and only if its image under the action of $g$ is fixed by $e'$. If some entry of $x$ or $y$ is not fixed by $e'$, each term of the sum is $0$, since the finite functions are supported on points fixed by $e'$. Both sides are then $0$.

If all entries are fixed by $e'$, the expansion writes both sides as products over $w \in P$ of the local unfolded terms. The column arguments of $x^{g}$ at $w$ are the column arguments of $x$ moved by the local component $\kappa_w$ of $k$ at the column $j + 1$. At each place, the local grid datum is admissible for the flipped tensor, since the local grid is good and each flip keeps admissibility. For an admissible datum and $\kappa$ in the local level,

$$\begin{aligned}
&\mu_{j+1}(\det \kappa)\, \mu_{j+2}(\det \kappa)^{-1}\, u_w(\kappa \cdot x, y) \\
&\quad = u_w(x, y).
\end{aligned}$$

The product over $w$ of the factors $\mu_{j+1}(\det \kappa_w) \mu_{j+2}(\det \kappa_w)^{-1}$ is $c_1 c_2$. $\square$

**Remark 8.9.7 (Formalization).** The theorems are in [NormalisedKernelExpansionSumLevelInvariant.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/NormalisedKernelExpansionSumLevelInvariant.lean#L19), [ExpansionPairingInvariantInnerVertexLevel.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExpansionPairingInvariantInnerVertexLevel.lean#L33), [ExpansionProductInvariantInnerVertexLevel.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExpansionProductInvariantInnerVertexLevel.lean#L17) and [UnfoldingExpansionProductFunctionLocalInvariant.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/UnfoldingExpansionProductFunctionLocalInvariant.lean#L143). Each statement under a `T.` name is a copy of its proof, closed by a `first` tactic. The name of the first theorem speaks of a normalised kernel expansion sum, but the statement is about the pairing of points with no normalisation. The local theorem does not use its support hypothesis on $\beta$, and it does not use the hypothesis that the data carry the idempotent $e$. It works with the idempotent of the expansion instead. We have not unfolded the place models, the level condition, the local unfolded terms or the flipped tensors.
