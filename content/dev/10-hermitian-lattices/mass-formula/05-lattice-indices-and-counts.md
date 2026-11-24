---
title: Lattice indices and lattice counts
decls:
  - PI.UnitaryGroupMassFormula.LCG.latCountAll_of_idx
  - PI.UnitaryGroupMassFormula.LCG.latCountAll_of_index
  - PI.TermsAtPtFiniteW.termsAtFinite_of_frameOp_shortFin
  - PI.UnitaryDimensionFormula.indexGe
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lattice indices and lattice counts

Three finiteness statements of the chapter on orbital bounds rest on counting points of lattices. The [lattice count](/entry/lattice-count-all/) bounds the number of lattice vectors in a box in terms of the size of the lattice. The theorem on [finitely many terms at a point](/entry/terms-at-point-finite/) shows that an orbital sum has only finitely many terms near a point. The [dimension bound](/entry/kappa-off-diagonal-dim-form-c/) needs, over each lattice of a family, many points in distinct cosets of a level group. This section reduces each of the three to a short list of facts about lattices: an index inequality for duals and determinants, a reduction of cells by unipotent matrices, and a lifting of Levi elements over the residue fields. For the background see [lattices in Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces) and [rings, ideals and modules](/learn/algebra/#rings-ideals-and-modules).

### Duals and indices

Let $K$ be a number field with ring of integers $\mathcal{O}_K$, and let $k \geq 1$. On $K^k$ we use the dot product $s \cdot t = \sum_i s_i t_i$.

**Definition 7.5.1 (Dual module and index).** For an $\mathcal{O}_K$-submodule $X \subseteq K^k$, the *dual* of $X$ is
$$X^\vee = \{ t \in K^k : s \cdot t \in \mathcal{O}_K \text{ for all } s \in X \}.$$
For submodules $X \subseteq Y$, the *index* $[Y : X]$ is the number of cosets of $X$ in $Y$, and we put $[Y : X] = 0$ when there are infinitely many. For a subgroup $B$ of a module and vectors $b_1, \dots, b_k$, put $\operatorname{idx}(B, b) = \# \bigl( B / (B \cap \operatorname{span}_{\mathcal{O}} b) \bigr)$.

The dual reverses inclusions. For $X = \mathcal{O}_K^k$ the dual is $\mathcal{O}_K^k$ again. If $X = \varpi \mathcal{O}_K^k$ for a nonzero $\varpi \in \mathcal{O}_K$, then $X^\vee = \varpi^{-1} \mathcal{O}_K^k$, and both indices $[\mathcal{O}_K^k : X]$ and $[X^\vee : \mathcal{O}_K^k]$ equal $|N_{K/\mathbb{Q}}(\varpi)|^k$. The next two lemmas say that this is the general pattern, up to an inequality.

**Lemma 7.5.2 (Dual index).** Let $X \subseteq Y \subseteq K^k$ be submodules with $[Y : X]$ finite. Then $[X^\vee : Y^\vee] \neq 0$ and $[X^\vee : Y^\vee] \leq [Y : X]$.

**Lemma 7.5.3 (Determinant and index).** Let $Q$ and $D$ be submodules of $K^k$ with $\mathcal{O}_K^k \subseteq Q$, $D \subseteq \mathcal{O}_K^k$, and both indices $[Q : \mathcal{O}_K^k]$ and $[\mathcal{O}_K^k : D]$ finite. Let $N$ be a $k \times k$ matrix over $K$ such that every $r \in D$ is of the form $s N$ with $s \in Q$. Then
$$|N_{K/\mathbb{Q}}(\det N)| \leq [Q : \mathcal{O}_K^k] \cdot [\mathcal{O}_K^k : D].$$

Now let $E$ be the CM field of the setting, $h(x, y) = \bar{x}^T J y$ a Hermitian form on $E^m$, and $\Lambda \subseteq E^m$ a finitely generated $\mathcal{O}_E$-module that spans $E^m$, such that $u \in \Lambda$ whenever $h(w, u) \in \mathcal{O}_E$ for all $w \in \Lambda$.

**Proposition 7.5.4 (Index inequality).** Let $\delta$ be an $m \times m$ matrix over $E$. Let $u_1, \dots, u_k \in \Lambda$ be such that the vectors $\delta u_c$ are linearly independent and span the image of $\delta$. Let $b'_1, \dots, b'_k \in \Lambda$ be linearly independent, orthogonal to $\ker \delta$, and spanning the orthogonal complement $(\ker \delta)^\perp$. Assume that the two indices below are finite. Then
$$\bigl| N_{E/\mathbb{Q}} \det \bigl( h(b'_a, u_c) \bigr)_{a, c} \bigr| \leq \operatorname{idx}(\delta \Lambda, \delta u) \cdot \operatorname{idx}\bigl(\Lambda \cap (\ker \delta)^\perp, b'\bigr).$$

In the proof of the lattice count the proposition enters as one implication: the two lemmas give the proposition. The matrix $(h(b'_a, u_c))$ plays the part of $N$ in the second lemma.

**Theorem 7.5.5 (Lattice count from the index inequality).** Assume the lemma on determinants and indices. Assume that the two lemmas together imply the index inequality. Then the [lattice count](/entry/lattice-count-all/) holds: for every setting, every self-dual lattice and every box of the given radii, the number of lattice vectors in the box is at most the bound of that theorem.

Lean: `PI.UnitaryGroupMassFormula.LCG.latCountAll_of_idx` (also `PI.UnitaryGroupMassFormula.LCG.latCountAll_of_index`, the same conclusion from the index inequality itself).

*Proof.* The dual index lemma is proved, so the second assumption gives the index inequality. The lattice count then follows from the index inequality and seven further facts, all proved: a box bound for the archimedean sizes, a packing lemma, an inclusion of the dual, a choice of a basis adapted to $\ker \delta$, an inequality at the archimedean places and its form at one place, together with the separation of lattice points (which uses that a lattice is discrete, the product formula for the norm, the monotony of the determinant and a bound on the number of places). The index inequality enters at one step: it bounds the covolume of the image $\delta \Lambda$ by the norm of a determinant of values of $h$, and so bounds the number of possible images. $\square$

### Finitely many terms at a point

We use the setting of the theorem on [finitely many terms at a point](/entry/terms-at-point-finite/): a Hermitian space $V$ over $E$, a flag $F_0$ of rank $r$, row lattices $\Lambda$, lifted flags $F'$ with values $G(F_0, F')$ and cells. Each lifted flag gives a matrix $\hat{Z}(F_0, F')$ of coordinates; a point $p$ has a cell, the set of matrices $L \cdot \operatorname{pt}(p) \cdot U$ with $L$ lower and $U$ upper unitriangular. Let $N_\Lambda$ be the unipotent radical of the flag stabilizer intersected with the stabilizer of $\Lambda$.

**Definition 7.5.6 (Frame operators and short vectors).** We say that *frame operators exist* if there is an integer $b > 0$ such that for every row lattice $\Lambda$ and every upper unitriangular matrix $B$ whose entries above the diagonal are divisible by $b$, some $n \in N_\Lambda$ acts on the frame of the flag by $B$. We say that *short vectors are finite* if for every lattice $\Lambda$, every subspace $P$ on which $h$ is positive definite at every infinite place, and every $c$, only finitely many $x \in \Lambda \cap P$ have $h(x, x) = c$.

The second property is the classical finiteness of lattice vectors of bounded length in a positive definite space: at each infinite place the condition $h(x, x) = c$ bounds $x$, and a lattice meets a bounded set in finitely many points.

**Theorem 7.5.7 (Terms at a point from frames and short vectors).** Assume that frame operators exist and that short vectors are finite. Then for every flag $F_0$, every row lattice $\Lambda$ and every point $w$, only finitely many terms for $(u', F_0, \Lambda)$ sit at $w$.

Lean: `PI.TermsAtPtFiniteW.termsAtFinite_of_frameOp_shortFin`.

*Proof.* The set of terms at $w$ is the image of the set of lifted flags $F'$ with $G(F_0, F') \neq 0$ whose cell contains $w$. We bound this set in two steps.

First, the matrices $\hat{Z}(F_0, F')$ take finitely many values up to the action of $N_\Lambda$. A reduction of cells holds: for $b \neq 0$ there is a finite set $Z_s$ of matrices such that every integral matrix $Z$ in the cell of $w$ is moved into $Z_s$ by $Z \mapsto A Z B$, with $A$ lower unitriangular and congruent to $1$ modulo $b$, and $B$ upper unitriangular with entries above the diagonal divisible by $b$. The coordinate matrices are integral, and the carrier of a row is preserved. The frame operators realize the matrices $B$ by elements of $N_\Lambda$, so each class of terms meets a lifted flag with $\hat{Z} \in Z_s$.

Second, for each fixed $Z$ only finitely many terms have $G \neq 0$ and $\hat{Z}(F_0, F') = Z$. Fix $Z$. A lifted flag with this matrix is fixed up to a vector $x$ in a positive definite part of $\Lambda$ with a fixed value $h(x, x)$, and up to a skew matrix. The Heisenberg elements
$$v \mapsto v + \sum_c h(e_c, v) a_c - \sum_c h(a_c, v) e_c + \sum_{c, d} s_{cd}\, h(e_d, v)\, e_c,$$
with $s + s^* = -h(a, a)$, lie in $N_\Lambda$. They move the skew part, and the skew equation can be solved when the rows are dependent and a right inverse exists. The vector part has finitely many values because short vectors are finite, and the rest lives in $\Lambda / c \Lambda$ for a nonzero $c$, which is finite. So there are finitely many terms with this $Z$.

The terms at $w$ are a finite union over $Z \in Z_s$ of finite sets. $\square$

### Points in distinct cosets

We use the setting of the [dimension bound](/entry/kappa-off-diagonal-dim-form-c/): a full family $Y$ of lattices with the tie condition, a word $u$, the finite adelic group $H_f(u)$ of the word, its level subgroup $K_u$, and for $t \in H_f(u)$ the lattice $\operatorname{lat}(t)$. Let $k$ be the rank of the Levi block, and let $v$ run over the finite set of places of the level, with residue fields $\mathbb{F}_{q_v}$. Put
$$I = \prod_v GL_k(\mathbb{F}_{q_v}), \qquad U = \prod_v U_k(\mathbb{F}_{q_v}),$$
where $U_k$ is the group of upper unitriangular matrices, and put $\Gamma_1 = \#(I / U)$.

**Theorem 7.5.8 (Index lower bound).** For every setting, every full family $Y$ with the tie condition, every word $u$ and every lattice $\Lambda$ of $Y$ for $u$, there are $n \geq \Gamma_1$ and $t_1, \dots, t_n \in H_f(u)$ with $\operatorname{lat}(t_i) = \Lambda$ for all $i$, such that $t_i^{-1} t_j \in K_u$ only if $i = j$.

Lean: `PI.UnitaryDimensionFormula.indexGe`.

*Proof.* There is a reduction map $s \mapsto \operatorname{levi}(s) \in I$, defined on the elements $s \in H_f(u)$ whose conjugate lies in the level set. It has three properties. It is multiplicative and sends $1$ to $1$. It sends $K_u$ into $U$. And it is onto $I$: every $A \in I$ is $\operatorname{levi}(s)$ for some $s$. The surjectivity comes from split frames: at each place a pair of dual frames $b, b^*$ of the lattice identifies the Levi block with $GL_k$, and the integral points of the Levi lift the points over the residue field.

Fix $\Lambda$ and an element $h_\Lambda$ with $\operatorname{lat}(h_\Lambda) = \Lambda$. Choose representatives $A_1, \dots, A_n$ of the cosets $I / U$, so $n = \Gamma_1$, and lift each to $s_i$ with $\operatorname{levi}(s_i) = A_i$. Put $t_i = h_\Lambda s_i$. The elements $s_i$ preserve the lattice, so $\operatorname{lat}(t_i) = \Lambda$. If $t_i^{-1} t_j = s_i^{-1} s_j \in K_u$, then $A_i^{-1} A_j = \operatorname{levi}(s_i^{-1} s_j) \in U$, since unipotent upper triangular matrices form a subgroup. So $A_i U = A_j U$ and $i = j$. $\square$

**Remark 7.5.9 (Formalization).** The lattice count takes the index inequality as an implication from the two lemmas; its caller proves both. The data of the index inequality ask only one half of self-duality ([SepDefs.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LatticeCountingBound/SepDefs.lean#L79)). The seven further facts of the lattice count were not unfolded. In the theorem on terms the cell reduction, the integrality of $\hat{Z}$ and the Heisenberg, skew and residue facts are proved inputs; we describe them from their statements in [CarrierRow.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/TermsFiniteAtPoint/CarrierRow.lean#L18). In the index bound the constant is $\#(I/U)$ by [IndexGe.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/RankTwoDimensionFormula/IndexGe.lean#L78); the maps $\operatorname{levi}$ and the lattice map were not unfolded.
