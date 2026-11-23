---
title: Block lattices and the Fock block decomposition
decls:
  - Formalism.GM.FockB.fock_blocks_of_weights
  - Formalism.GM.fock_block_decomposition
  - Formalism.MainNotions.G.SymmetricFormBlocks.blkZ_gen
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Block lattices and the Fock block decomposition

A block is a word of letters with several ties and one extra tie to a new letter $\xi$. Its polynomials split into levels, one for each choice of the exponents of the tie elements. This section proves that the levels are orthogonal for the Fock pairing, and that inside one level the Fock pairing of the lifted vectors is an explicit product of binomial coefficients times the pairing of the tie operators of Section 2. From this decomposition we build, out of good pairs at each level, a family of dual pairs in the block lattice with one common exponent. The result is the input of the block valuation bound of Section 4.

**Definition 7.3.1 (Highest weight conditions).** Let $L$ be a word of $N$ letters and $j \leq N$. For $M \in \mathbb{Z} \cup \{\infty\}$ let $Y(j, M)$ be the largest subspace of $\mathbb{Q}_p[x]$ that is stable under the operators $E^{(j)}_{cd}$ of Section 2 and is contained in the span of the monomials $x^m$ with
$$\sum_{i < j,\ i \text{ vector}} m(i, 0) - \sum_{i < j,\ i \text{ covector}} m(i, 0) \leq M.$$
For a list of positions $J_1, \dots, J_q$ and thresholds $M_1, \dots, M_q$, put $Y(L) = \operatorname{Pol}(L) \cap \bigcap_k Y(J_k, M_k)$, and let $Y_{\mathbb{Z}}(L)$ be the set of $y \in Y(L)$ with coefficients in $\mathbb{Z}_p$.

So $Y(j, M)$ is the sum of the $\mathfrak{gl}_r$-subrepresentations for the first $j$ letters whose weights have first coordinate at most $M$. The thresholds cut out the part of $\operatorname{Pol}(L)$ of bounded first weight along the word.

**Definition 7.3.2 (Tie data).** *Tie data* on a word $L$ of $N$ letters consist of $t$ positions $\mathrm{pos}_0 < \dots < \mathrm{pos}_{t-1}$, shifts $z_i \in \mathbb{N}$, and the positions and thresholds $(J_k, M_k)_{k < q}$. They are *admissible* if each letter $\mathrm{pos}_i$ is a vector letter, each letter $\mathrm{pos}_i + 1$ is a covector letter, $\mathrm{pos}_i + 1 < N$, and each $\mathrm{pos}_i + 1$ equals some $J_k$. The $i$-th *tie* joins letters $\mathrm{pos}_i$ and $\mathrm{pos}_i + 1$.

**Definition 7.3.3 (Block data).** A *block* consists of a word $L$ of $N$ letters, admissible tie data, a natural number $B$ and a shift $z_+$, such that the last letter $u = N - 1$ is a vector letter and $\mathrm{pos}_i + 1 < u$ for every $i$. Its variables are $x_{a,c}$ for the $N$ letters, the variables $\xi_c$ ($c < r$) of an extra letter, and scalar variables $z_i, s_i$ for $i < t$ and $z_+, s_+$. Put
$$\hat E_i = z_i s_i + \sum_c x_{\mathrm{pos}_i, c}\, x_{\mathrm{pos}_i + 1, c}, \qquad E_+ = z_+ s_+ + \sum_c x_{u, c}\, \xi_c.$$

**Definition 7.3.4 (Levels).** A *level* of a block is a pair $(j, j_+)$ with $j \in \mathbb{N}^t$ and $j_+ \in \mathbb{N}$, such that $j_i$ is at most the degrees of letters $\mathrm{pos}_i$ and $\mathrm{pos}_i + 1$, and $j_+$ is at most $d_u$ and at most $B$. The word $L_{j,j_+}$ is $L$ with degrees lowered by $j_i$ at $\mathrm{pos}_i$ and $\mathrm{pos}_i + 1$, and by $j_+$ at $u$. Let $\Xi_{\mathbb{Z}}(b)$ be the polynomials of degree $b$ in the $\xi_c$ with coefficients in $\mathbb{Z}_p$. The *level lattice* is
$$\Lambda_{j,j_+} = \operatorname{span}_{\mathbb{Z}_p} \{\, y\, g : y \in Y_{\mathbb{Z}}(L_{j,j_+}),\ g \in \Xi_{\mathbb{Z}}(B - j_+) \,\}.$$

**Definition 7.3.5 (The two block lattices).** The *standard lattice* $\mathcal{S}$ is the $\mathbb{Z}_p$-span of the vectors
$$\prod_i \hat E_i^{j_i} \cdot E_+^{j_+} \cdot \prod_i z_i^{z_i} \cdot z_+^{z_+} \cdot y\, g$$
over all levels and all $y g$ as in $\Lambda_{j,j_+}$. Let $P_{j,j_+}$ be the composite of the projections $P_i$ at the ties (in the order of the ties) and the projection $P_+$ at the pair $(u, \xi)$, where each $P$ is
$$P(y) = \sum_{l=0}^{o} \frac{(-1)^l}{(l!)^2 \binom{o + n + r + z - 1}{l}} \hat E^{\,l} F^{\,l} (z^{z} y)$$
for the letter degrees $(o, n)$ of $L_{j,j_+}$ (for $P_+$: $o = d_u - j_+$, $n = B - j_+$, $z = z_+$). The *projected lattice* $\mathcal{P}$ is the $\mathbb{Z}_p$-span of the vectors $\prod_i \hat E_i^{j_i} E_+^{j_+} P_{j,j_+}(y g)$.

Let $\Phi_{j,j_+}$ be the composite of the tie operators $\Phi$ of Section 2 at the ties of $L_{j,j_+}$ and at $(u, \xi)$, with the same degrees and shifts. On $\Lambda_{j,j_+}$ we use the pairing
$$\beta_{j,j_+}(v, w) = \frac{\langle \Phi_{j,j_+} v,\ w \rangle}{\prod_a d_a(L_{j,j_+})!\,(B - j_+)!}.$$

**Theorem 7.3.6 (Fock block decomposition).** Let a block satisfy the conditions above and let $r \geq 1$. Write $T_{j,j_+}(v) = \prod_i \hat E_i^{j_i} E_+^{j_+} P_{j,j_+}(v)$.

1. If $(j, j_+) \neq (j', j'_+)$ are levels, $y \in Y(L_{j,j_+})$, $y' \in Y(L_{j',j'_+})$, $g \in \Xi_{\mathbb{Z}}(B - j_+)$ and $g' \in \Xi_{\mathbb{Z}}(B - j'_+)$, then $\langle T_{j,j_+}(y g), T_{j',j'_+}(y' g') \rangle = 0$.
2. If $(j, j_+)$ is a level, $y, y' \in Y(L_{j,j_+})$ and $g, g' \in \Xi_{\mathbb{Z}}(B - j_+)$, put $c = (\prod_i j_i! \cdot j_+!)^{-1}$. Then
$$\begin{aligned}
\langle c\, T_{j,j_+}(y g),\ c\, T_{j,j_+}(y' g') \rangle
&= \prod_i \binom{o_i + n_i + r + z_i + j_i}{j_i} z_i! \\
&\quad \cdot \binom{o_+ + n_+ + r + z_+ + j_+}{j_+} z_+! \cdot \langle y g,\ \Phi_{j,j_+}(y' g') \rangle,
\end{aligned}$$
where $(o_i, n_i)$ are the degrees of letters $\mathrm{pos}_i$, $\mathrm{pos}_i + 1$ in $L_{j,j_+}$, and $o_+ = d_u - j_+$, $n_+ = B - j_+$.

Lean: `Formalism.GM.FockB.fock_blocks_of_weights` (also `Formalism.GM.fock_block_decomposition`, a second name).

*Proof.* The ties of a block use disjoint sets of variables, because the positions are distinct and the tie to $\xi$ uses the last letter, which no tie touches. So the Fock pairing factors over the ties, and it suffices to treat one tie with its pair of scalar variables $z, s$ and then argue by induction along the chain of ties. For one tie, $\hat E = zs + E$ is the tie element for $r + 1$ columns, and its Fock adjoint is $\hat F = \partial_z \partial_s + F$. Add $z$ to the vector letter and $s$ to the covector letter. Then $z^{z} y$ has bidegree $(o + z, n)$, and $P$ is the harmonic projection of Section 2 for $r + 1$ columns and bidegree $(o + z, n)$ applied to $z^{z} y$: its binomials are $\binom{(o + z) + n + (r + 1) - 2}{l}$, and $\hat F$ and $F$ agree on polynomials free of $s$. So $\hat F P(y) = 0$. By adjointness and the commutation rule of the proof of the Lemma (Action on levels) of Section 2, with $r + 1$ in place of $r$,
$$\langle \hat E^{j} P y,\ \hat E^{j'} P y' \rangle = 0 \ \ (j \neq j'), \qquad \langle \hat E^{j} P y,\ \hat E^{j} P y' \rangle = (j!)^2 \binom{o + n + r + z + j}{j} \langle P y, P y' \rangle.$$
Finally $\langle P y, P y' \rangle = \langle z^{z} y, P y' \rangle$, as $P$ is a self-adjoint idempotent on these polynomials. In $\langle z^{z} y, \hat E^{l} F^{l} z^{z} y' \rangle$ only the part of $\hat E^{l}$ free of $s$ survives, which is $E^{l}$, so the pairing is $z!\, \langle y, E^{l} F^{l} y' \rangle$. Summing over $l$ gives $\langle P y, P y' \rangle = z!\, \langle y, \Phi_{o,n,z}\, y' \rangle$. The two parts of the theorem follow by multiplying these identities over the ties. $\square$

The level lattices are the building blocks of the block bound. The next theorem moves good pairs of each $\Lambda_{j,j_+}$ into $\mathcal{S}$.

**Theorem 7.3.7 (Good pairs in the standard lattice).** Let a block satisfy the conditions above and let $r \geq 1$. Let $U, M \in \mathbb{N}$ with $p^{U} \mathcal{P} \subseteq \mathcal{S}$, and assume that for every level
$$v_p\bigl(\lambda_{j,j_+} \cdot \textstyle\prod_a d_a(L_{j,j_+})!\,(B - j_+)!\bigr) \leq M,$$
where $\lambda_{j,j_+} = (\prod_i j_i!\, j_+!)^2 \prod_i \binom{o_i + n_i + r + z_i + j_i}{j_i} z_i! \cdot \binom{o_+ + n_+ + r + z_+ + j_+}{j_+} z_+!$. Let $D \in \mathbb{Z}$. Then there are $n \geq 0$ and $x_1, \dots, x_n, y_1, \dots, y_n \in \mathcal{S}$ with
$$\langle x_k, y_l \rangle = p^{D + 2U + M} \delta_{kl}, \qquad \sum_{(j,j_+)} \operatorname{rk} \Lambda_{j,j_+} \leq n + \sum_{(j,j_+)} \operatorname{bad}(\beta_{j,j_+}, \Lambda_{j,j_+}, D),$$
the sums running over all levels.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.blkZ_gen`.

*Proof.* At each level choose good pairs $u_1, \dots, u_{n_{j,j_+}}$, $v_1, \dots, v_{n_{j,j_+}}$ in $\Lambda_{j,j_+}$ with $\beta_{j,j_+}(u_k, v_l) = p^{D} \delta_{kl}$, where $n_{j,j_+}$ is the good count of Section 1; the supremum is attained because it is bounded by the rank. The number $\lambda_{j,j_+} \prod_a d_a! (B - j_+)!$ is a nonzero integer with valuation at most $M$, so there is $s \in \mathbb{Z}_p$ with $s \lambda_{j,j_+} \prod_a d_a! (B - j_+)! = p^{M}$. Put $x = p^{U} T_{j,j_+}(v_k)$ and $y = s\, p^{U} T_{j,j_+}(u_k)$. They lie in $\mathcal{S}$, since $T_{j,j_+}(\Lambda_{j,j_+}) \subseteq \mathcal{P}$. By part 2 of the [Theorem (Fock block decomposition)](/entry/fock-block-decomposition/) and symmetry of the Fock pairing, $\langle x, y \rangle$ for two pairs of one level is $p^{2U} s \lambda_{j,j_+} \prod_a d_a! (B - j_+)!\, \beta_{j,j_+}(u_l, v_k) = p^{D + 2U + M} \delta_{kl}$. By part 1, pairs from different levels are orthogonal. Take $n = \sum n_{j,j_+}$; then $\operatorname{rk} \Lambda_{j,j_+} = n_{j,j_+} + \operatorname{bad}$ at each level, and summing gives the bound. $\square$

**Remark 7.3.8 (Formalization).** The proof of the decomposition is in [FockBlocks.lean](lean:Formalism/MahlerMeasure/MahlerMeasureProofs/FockBlocks.lean#L689), through the one-tie identities `step_same` and `step_orth` and their chain versions `chain_main` and `chain_orth`; we read the statements of these lemmas, and the proof above follows them. `fock_block_decomposition` (line 740) is the same statement under a second name. The binomials of the statement are written $\binom{o + n + r + z + 1 + j - 1}{j}$. The level lattices `Ljj` do not contain the powers of $\hat E_i$ or $z_i$; these appear only in the standard lattice `SSZ`. The levels of the second theorem are those with all $j_i \leq \sum_a d_a$ and $j_+ \leq B$, a finite set.
