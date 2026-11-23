---
title: Semistable majorants of self-dual Hermitian lattices
decls:
  - ReciprocityTheory.MultiplicativeHeights.Closed.semiPoint
  - ReciprocityTheory.MultiplicativeHeights.semiDeg_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Semistable majorants of self-dual Hermitian lattices

This section and the next two collect three results which the proof uses through [the step on characters from the literature](/step/every-character-of-literature/). They concern Hermitian lattices and formal groups rather than good reduction, and they sit in this chapter because they enter the proof at the same place as the theorems of Serre and Tate. The result of this section is that a self-dual lattice for a Hermitian form over a number field has a majorant for which it is semistable of degree zero, in the sense of Arakelov degrees. Background is in [lattices in quadratic and Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces) and [Hermitian lattices and slopes](/learn/arakelov/#hermitian-lattices-and-slopes) of Volume 1.

### Hermitian forms, lattices and degrees

Throughout, $K$ is a number field with ring of integers $\mathcal{O}_K$, and $\sigma$ runs over the field embeddings $K \to \mathbb{C}$. For a vector or matrix $x$ over $K$, $x^\sigma$ is the result of applying $\sigma$ to the entries.

**Definition 3.5.1 (Hermitian form).** A *[[Hermitian form|48P4A1CX85]]* of rank $r$ over $K$ is a pair $(c, G)$, where $c$ is a ring automorphism of $K$ with $c^2 = 1$ and $\sigma(c x) = \overline{\sigma(x)}$ for all $\sigma$ and $x$, and $G \in M_r(K)$ satisfies $c(G_{ab}) = G_{ba}$. The form is
$$
h(x, y) = \sum_{a, b} c(x_a)\, G_{ab}\, y_b , \qquad x, y \in K^r .
$$

The condition on $c$ says that $c$ is complex conjugation in every embedding. Such a $c$ exists only when $K$ is totally real, and then $c = 1$, or $K$ is a CM field, and then $c$ is its complex conjugation.

**Definition 3.5.2 (Lattice, self-dual lattice).** A *lattice* is a finitely generated $\mathcal{O}_K$-submodule $L \subseteq K^r$ which spans $K^r$ over $K$. It is *integral* if $h(x, y) \in \mathcal{O}_K$ for all $x, y \in L$, and *self-dual* if it is integral and every $x \in K^r$ with $h(x, y) \in \mathcal{O}_K$ for all $y \in L$ lies in $L$.

**Definition 3.5.3 (Majorant).** A *majorant* of $(c, G)$ is a family of matrices $H_\sigma \in M_r(\mathbb{C})$, one for each $\sigma$, such that each $H_\sigma$ is positive definite, $H_\sigma (G^\sigma)^{-1} H_\sigma = G^\sigma$, and $H_{\bar\sigma} = \overline{H_\sigma}$, where $\bar\sigma$ is $\sigma$ followed by complex conjugation.

**Definition 3.5.4 (Degree).** Let $H = (H_\sigma)$ be a family of positive definite matrices, $B \subseteq K^r$ an $\mathcal{O}_K$-submodule, and $b_1, \ldots, b_k \in B$ a *$K$-basis in $B$*: the $b_i$ lie in $B$, are linearly independent over $K$, and $B$ lies in their $K$-span. The *degree* of $B$ with respect to $b$ is
$$
\deg_H(B, b) = \log\,[B : \textstyle\sum_i \mathcal{O}_K b_i] - \frac{1}{2} \sum_\sigma \log \operatorname{Re} \det\bigl( (b_i^\sigma)^* H_\sigma\, b_j^\sigma \bigr)_{i, j} .
$$

**Definition 3.5.5 (Semistable of degree zero).** A lattice $L$ is *semistable of degree zero* for $H$ if $\deg_H(L, b) = 0$ for every $K$-basis $b$ in $L$, and $\deg_H(B, b) \leq 0$ for every submodule $B \subseteq L$ and every $K$-basis $b$ in $B$.

**Definition 3.5.6 (Additivity of the degree).** For a lattice $L$ and $K$-linearly independent $b_1, \ldots, b_k, c_1, \ldots, c_m$ in $L$ whose span contains $L$, the *quotient degree* is
$$
\begin{aligned}
\deg_H(L, b, c) = {}& \log\,[L : (L \cap K b) + \textstyle\sum_j \mathcal{O}_K c_j] \\
&- \frac{1}{2} \sum_\sigma \log \operatorname{Re} \det Q_\sigma ,
\end{aligned}
$$
where $Q_\sigma$ is the Schur complement of the Gram matrix of $b$ in the Gram matrix of $(b, c)$, for $H_\sigma$. The *additivity of the degree* is the statement that $\deg_H(L, (b, c)) = \deg_H(L \cap Kb, b) + \deg_H(L, b, c)$ whenever each $H_\sigma$ is positive definite.

### Six inputs

The proof uses six statements about these notions, which are proved elsewhere and which we do not unfold, except the last.

**Lemma 3.5.7 (Witt basis).** If $\det G \neq 0$, there are $P \in GL_r(K)$, an integer $m$ with $2m \leq r$, and $g_1, \ldots, g_r \in K$ such that $(P^c)^T G P$ has entries $1$ at the positions $(i, r-1-i)$ for $i < m$ or $i \geq r - m$, entries $g_i$ on the diagonal for $m \leq i < r - m$, and $0$ elsewhere, and such that the diagonal form $\sum_i c(t_i) g_i t_i$ on the middle coordinates is anisotropic.

Lean: `ReciprocityTheory.MultiplicativeHeights.wittBasis_holds`.

**Lemma 3.5.8 (Independence of the basis).** If each $H_\sigma$ is positive definite and $B$ is finitely generated, $\deg_H(B, b)$ does not depend on the $K$-basis $b$ in $B$.

Lean: `ReciprocityTheory.MultiplicativeHeights.latDegBasis_holds`.

**Lemma 3.5.9 (Integral index).** If $B$ is finitely generated and integral, $b$ is a $K$-basis in $B$ and the matrix $h(b) = (h(b_i, b_j))$ has nonzero determinant, then $[B : \sum_i \mathcal{O}_K b_i]^2 \leq |N_{K/\mathbb{Q}} \det h(b)|$.

Lean: `ReciprocityTheory.MultiplicativeHeights.integralIndex_holds`.

**Lemma 3.5.10 (Self-dual index).** If $L$ is a self-dual lattice and $b$ a $K$-basis in $L$, then $|N_{K/\mathbb{Q}} \det h(b)| \leq [L : \sum_i \mathcal{O}_K b_i]^2$.

Lean: `ReciprocityTheory.MultiplicativeHeights.selfDualIndex_holds`.

**Lemma 3.5.11 (Graded extension).** Let $F_e \subseteq K^r$ be the vectors whose coordinates $i \geq e$ vanish, and $\pi_e$ the projection which keeps the coordinates $i \geq e$. For a diagonal metric $H$ with positive entries and a finitely generated $B$,
$$
\deg_H(B) \leq \deg_H(B \cap F_e) + \deg_H(\pi_e B),
$$
with any $K$-bases in the three modules.

Lean: `ReciprocityTheory.MultiplicativeHeights.gradedExt_holds`.

This lemma is deduced from the additivity of the degree and the independence of the basis, and it is the only place where the additivity enters.

**Lemma 3.5.12 (A determinant inequality).** Let $A, C \in M_n(\mathbb{C})$ with $A$ positive definite and $C$ Hermitian, and assume $|v^* C v| \leq \operatorname{Re}(v^* A v)$ for all $v$. Then $|\det C| \leq \det A$.

Lean: `ReciprocityTheory.MultiplicativeHeights.absDet_holds`.

*Proof.* Replace $C$ by $A^{-1/2} C A^{-1/2}$, which is Hermitian and satisfies $|w^* C w| \leq w^* w$. Its eigenvalues are real of absolute value at most $1$, so its determinant has absolute value at most $1$, and $\det A$ factors out. $\square$

### The theorem

**Theorem 3.5.13 (Semistable majorant, conditional form).** Assume the additivity of the degree. Let $(c, G)$ be a Hermitian form of rank $r$ over $K$ and $L$ a self-dual lattice. Then $(c, G)$ has a majorant $H$ for which $L$ is semistable of degree zero.

Lean: `ReciprocityTheory.MultiplicativeHeights.semiDeg_holds`.

*Proof.* First, $\det G \neq 0$. Otherwise there is $x \neq 0$ with $h(x, y) = 0$ for all $y$, and by self-duality every multiple $a x$ with $a \in K$ lies in $L$, which is impossible for a finitely generated $\mathcal{O}_K$-module.

By the Witt basis lemma, take $P$, $m$ and $g$, put $Q = P^{-1}$ and $L' = QL$. In the new coordinates the form has the matrix $J = (P^c)^T G P$ of that lemma, and $L'$ is integral for it. Since $c(g_i) = g_i$ for the middle indices, each $\sigma(g_i)$ is real.

For positive reals $d_0, \ldots, d_{r-1}$, let $D_\sigma$ be the diagonal matrix with entries $d_i$ for $i < m$, $d_{r-1-i}^{-1}$ for $i \geq r - m$, and $|\sigma(g_i)|$ in the middle. The main step is that the $d_i$ can be chosen so that every submodule $B \subseteq L'$ has $\deg_D(B) \leq 0$. For $j < m$, $d_j$ is defined from the $j$-th graded piece of $L'$ along the flag $(F_e)$, so that this piece has degree $0$. The degree of $B$ is then bounded, by the graded extension lemma along the flag, by the sum of the degrees of the graded pieces of $B$, each of rank at most one. The middle pieces have degree at most $0$ by the integral index lemma for the anisotropic part, and the last $m$ pieces by the pairing of coordinate $j$ with coordinate $r - 1 - j$, which uses the determinant inequality.

Now put $H_\sigma = (Q^\sigma)^* D_\sigma Q^\sigma$. It is positive definite, and $H_{\bar\sigma} = \overline{H_\sigma}$. Since $G^\sigma = (Q^\sigma)^* J^\sigma Q^\sigma$,
$$
\begin{aligned}
H_\sigma (G^\sigma)^{-1} H_\sigma &= (Q^\sigma)^* D_\sigma (J^\sigma)^{-1} D_\sigma Q^\sigma \\
&= (Q^\sigma)^* J^\sigma Q^\sigma = G^\sigma ,
\end{aligned}
$$
because $D_\sigma (J^\sigma)^{-1} D_\sigma = J^\sigma$: on a hyperbolic pair the entries are $d \cdot d^{-1} = 1$, and on the middle $|\sigma g_i|^2 / \sigma(g_i) = \sigma(g_i)$ as $\sigma(g_i)$ is real. So $H$ is a majorant.

The degree is invariant under the change of coordinates: $\deg_H(B, b) = \deg_D(QB, Qb)$. So $\deg_H(B) \leq 0$ for every $B \subseteq L$.

It remains to show $\deg_H(L, b) \geq 0$ for a $K$-basis $b$ in $L$, which has $r$ elements. From $H_\sigma (G^\sigma)^{-1} H_\sigma = G^\sigma$ we get $\det H_\sigma = |\det G^\sigma|$, so the Gram determinant of $b^\sigma$ for $H_\sigma$ is $|\sigma(\det h(b))|$. Summing over $\sigma$,
$$
\deg_H(L, b) = \log\,[L : \textstyle\sum_i \mathcal{O}_K b_i] - \frac{1}{2} \log |N_{K/\mathbb{Q}} \det h(b)| \geq 0
$$
by the self-dual index lemma. Hence $\deg_H(L, b) = 0$. $\square$

**Theorem 3.5.14 (Semistable majorant).** Let $K$ be a number field, $(c, G)$ a Hermitian form of rank $r$ over $K$, and $L$ a self-dual lattice. Then $(c, G)$ has a majorant for which $L$ is semistable of degree zero.

Lean: `ReciprocityTheory.MultiplicativeHeights.Closed.semiPoint`.

*Proof.* The additivity of the degree holds (Lean: `ReciprocityTheory.MultiplicativeHeights.Closed.degAdd`), and the conditional form applies. $\square$

**Remark 3.5.15 (Formalization).** The conditional form is one line: `SemiPt.semiPoint_of` applied to the six inputs ([SemiDeg.lean](lean:ReciprocityTheory/SemistableReduction/SemiDeg.lean#L9)), and the theorem applies it to `degAdd` ([SemiAll.lean](lean:ReciprocityTheory/SemistableReduction/SemiAll.lean#L9)). The proof above follows `SemiPt.semiPoint_of` ([SemiDegZA.lean](lean:ReciprocityTheory/SemistableReduction/SemiDegZA.lean#L104)), with the choice of the $d_i$ in `adapted_semistable` ([SemiDegW.lean](lean:ReciprocityTheory/SemistableReduction/SemiDegW.lean#L51)) and the majorant in `exists_adapted_majorant` ([SemiDegG.lean](lean:ReciprocityTheory/SemistableReduction/SemiDegG.lean#L26)); our account of the choice of the $d_i$ is an outline. In the Lean metric the $d_i$ do not depend on $\sigma$. The index in the degree is a relative index of additive groups, which is $0$ for an infinite index; for a $K$-basis in a finitely generated module the index is finite. The degree has no discriminant term, so $\mathcal{O}_K$ with the standard metric has degree $0$. The theorem `semistable` of the same file, which adds a statement on contracting endomorphisms, is not part of this chapter.
