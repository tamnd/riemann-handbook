---
title: The Gelfand-Kazhdan criterion for GL(n)
decls:
  - GroundTheory.Automorphic.Whittaker.exists_good_nhds
  - GroundTheory.Automorphic.Whittaker.sub_sigma_mem_rel
  - GroundTheory.Automorphic.Whittaker.distribution_sigma_invariant
  - GroundTheory.Automorphic.Whittaker.biEquivariantSigmaInvariant_GL
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Gelfand-Kazhdan criterion for GL(n)

This section proves that every distribution on $\mathrm{GL}_n(F)$ that transforms on both sides by a generic character of the unipotent group is invariant under a fixed anti-involution $\sigma$. This is the geometric half of the theorem of Gelfand and Kazhdan. The next section turns it into the uniqueness of Whittaker functionals, which is used in the step [EveryCharacter from the Galois row](/step/every-character/). For the background, see [smooth representations of $p$-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups), [generic characters](/learn/periods/#generic-characters) and [local multiplicity one](/learn/periods/#local-multiplicity-one).

### The setting

Let $F$ be a non-archimedean [[local field|J85FZEQG38]] and $G = \mathrm{GL}_n(F)$. Let $N \subset G$ be the group of upper unitriangular matrices. Let $C_c^\infty(G)$ be the space of locally constant functions $G \to \mathbb{C}$ with compact support. A *distribution* on $G$ is a linear form on $C_c^\infty(G)$; no continuity is asked.

**Definition 4.1.1 (Generic character of $N$).** Let $\psi_0 \colon F \to \mathbb{C}^\times$ be a continuous nontrivial additive character. For $u \in N$ put
$$\psi_N(u) = \psi_0\Big(\sum_{i=1}^{n-1} u_{i,i+1}\Big).$$

The map $u \mapsto \sum_i u_{i,i+1}$ is a homomorphism from $N$ to $F$, since the superdiagonal of a product of unitriangular matrices is the sum of the superdiagonals. So $\psi_N$ is a character of $N$. It is nontrivial on each simple root group, which is the meaning of "generic".

**Definition 4.1.2 (The anti-involution $\sigma$).** For $g \in G$ let $\sigma(g)$ be the matrix with entries $\sigma(g)_{ij} = g_{n+1-j,\,n+1-i}$, the transpose of $g$ in the antidiagonal. Put $\theta(g) = \sigma(g)^{-1}$.

Then $\sigma(xy) = \sigma(y)\sigma(x)$ and $\sigma^2 = 1$. Also $\sigma(g) = w_0\, {}^t g\, w_0$, where $w_0$ is the antidiagonal permutation matrix. The map $\sigma$ sends $N$ to $N$, and it sends the entry in place $(i, i+1)$ to the place $(n-i, n+1-i)$, so $\psi_N(\sigma(u)) = \psi_N(u)$. Hence $\theta$ is an automorphism of $G$ that preserves $N$, with $\psi_N(\theta(u)) = \psi_N(u)^{-1}$.

**Definition 4.1.3 (Relations).** Let $N \times N$ act on $G$ by $(h_1, h_2) \cdot g = h_1 g h_2^{-1}$, and on functions by $(h \cdot f)(x) = f(h^{-1} \cdot x)$. Put $\chi(h_1, h_2) = \psi_N(h_1)\psi_N(h_2)^{-1}$. Let $\mathcal{R}$ be the span of the functions $h \cdot f - \chi(h) f$, with $h \in N \times N$ and $f \in C_c^\infty(G)$. A function $f \in C_c^\infty(G)$ is *good* if $f - f \circ \sigma \in \mathcal{R}$.

A distribution $D$ with $D(h \cdot f) = \chi(h) D(f)$ for all $h$ and $f$ is exactly a linear form that vanishes on $\mathcal{R}$. So the aim is to prove that every $f$ is good.

### Bruhat cells and ranks

For $1 \leq i, j \leq n$ and $g \in G$, let $r_{ij}(g)$ be the rank of the lower left block of $g$ formed by the rows $i, \dots, n$ and the columns $1, \dots, j$. Left multiplication by an upper triangular matrix and right multiplication by an upper triangular matrix do not change these ranks. By the Bruhat decomposition $G = \bigsqcup_w B w B$, and the ranks $r_{ij}$ determine the cell $BwB$ of $g$. For $g \in G$ put
$$C_{\geq}(g) = \{ y : r_{ij}(y) \geq r_{ij}(g) \text{ for all } i, j \}, \qquad C_{\leq}(g) = \{ y : r_{ij}(y) \leq r_{ij}(g) \text{ for all } i, j \}.$$
The rank of a matrix is lower semicontinuous, so $C_{\geq}(g)$ is open and $C_{\leq}(g)$ is closed. Their intersection is the Bruhat cell of $g$. Put $\Phi(g) = \sum_{i,j} r_{ij}(g)$. A point of $C_{\geq}(g) \setminus C_{\leq}(g)$ has $\Phi > \Phi(g)$.

Each cell $BwB$ is a union of $N \times N$-orbits of the points $t w$, with $t$ diagonal. A pair $(w, t)$ is *irrelevant* if there are $i < j$ with $w(i) < w(j)$ and $a \in F$ such that the root element $1 + (t_{w(i)}/t_{w(j)})\, a\, E_{w(i) w(j)}$ and the root element $1 + a E_{ij}$ have different values of $\psi_N$. Otherwise it is *relevant*. For an irrelevant pair, the character $\chi$ is nontrivial on the stabilizer of $tw$ in $N \times N$, and every function supported near the orbit lies in $\mathcal{R}$ modulo functions that vanish on the orbit. For a relevant pair, $\sigma(tw) = tw$.

**Lemma 4.1.4 (Good neighbourhoods).** Every $x \in G$ has an open neighbourhood $V$ such that each $f \in C_c^\infty(G)$ supported in $V$ is good.

Lean: `GroundTheory.Automorphic.Whittaker.exists_good_nhds`.

*Proof.* Suppose not. The function $\Phi$ is bounded by $n^3$, so among the bad points we can choose $g$ with $\Phi(g)$ maximal. Every point $y \in C_{\geq}(g) \setminus C_{\leq}(g)$ has $\Phi(y) > \Phi(g)$, so it is not bad: it has a good neighbourhood. By a partition of unity, every function supported in an open subset of $C_{\geq}(g)$ and vanishing on $C_{\leq}(g)$ is good.

Case 1: $\sigma$ maps the cell of $g$ to itself. Put $U = C_{\geq}(g) \cap \sigma^{-1} C_{\geq}(g)$. It is open, stable under $N \times N$ and $\sigma$, and contains the cell. Let $f$ be supported in $U$. On each orbit of the cell the pair is relevant, so $\sigma$ fixes the base point, and the lemma for relevant cells gives $f - f \circ \sigma = r + k$, with $r \in \mathcal{R}$ and $k$ supported in $U$ and zero on the cell. By maximality, $k - k \circ \sigma \in \mathcal{R}$. Apply $\sigma$ to the identity: $f \circ \sigma - f = r \circ \sigma + k \circ \sigma$. Adding the two identities gives $k + k \circ \sigma = -(r + r \circ \sigma)$. The space $\mathcal{R}$ is stable under $f \mapsto f \circ \sigma$, because $\sigma(h_1 g h_2^{-1}) = \theta(h_2)\, \sigma(g)\, \theta(h_1)^{-1}$ and $\chi(\theta h_2, \theta h_1) = \psi_N(h_2)^{-1}\psi_N(h_1) = \chi(h_1, h_2)$. So $k + k\circ\sigma \in \mathcal{R}$. Then
$$2k = (k + k \circ \sigma) + (k - k \circ \sigma) \in \mathcal{R},$$
so $k \in \mathcal{R}$ and $f - f \circ \sigma \in \mathcal{R}$.

Case 2: some $h$ in the cell of $g$ has $\sigma(h)$ in another cell. The cell of $\sigma(tw)$ is that of $w_0 w^{-1} w_0$, for every $t$. If some pair $(w, t)$ were relevant, then $\sigma(tw) = tw$, so $\sigma$ would preserve the cell. Hence every pair $(w, t)$ is irrelevant. Then every $f$ supported in $C_{\geq}(g)$ is $r + k$ with $r \in \mathcal{R}$ and $k$ zero on $C_{\leq}(g)$. The function $k$ is good by maximality, and $r - r\circ\sigma \in \mathcal{R}$. So $f$ is good.

In both cases $g$ has a good neighbourhood, a contradiction. $\square$

**Proposition 4.1.5 (Every test function is good).** For every $f \in C_c^\infty(G)$, $f - f \circ \sigma \in \mathcal{R}$.

Lean: `GroundTheory.Automorphic.Whittaker.sub_sigma_mem_rel`.

*Proof.* The support of $f$ is compact, so it is covered by finitely many good neighbourhoods from [Lemma 4.1.4](/entry/exists-good-nhds/). As $G$ is totally disconnected, we may take them open, compact and disjoint. Then $f$ is a finite sum of functions supported in good neighbourhoods, and the set of good functions is a linear subspace. $\square$

### Invariant distributions

**Theorem 4.1.6 (Gelfand-Kazhdan for Whittaker distributions).** Let $D$ be a distribution on $G$ such that
$$D\big(x \mapsto f(u_1^{-1} x u_2)\big) = \psi_N(u_1)\, \psi_N(u_2)^{-1}\, D(f)$$
for all $f \in C_c^\infty(G)$ and $u_1, u_2 \in N$. Then $D(f \circ \sigma) = D(f)$ for all $f$.

Lean: `GroundTheory.Automorphic.Whittaker.distribution_sigma_invariant`.

*Proof.* The hypothesis says that $D$ vanishes on the generators of $\mathcal{R}$, so $D$ vanishes on $\mathcal{R}$. By [Proposition 4.1.5](/entry/sub-sigma-mem-rel/), $f - f \circ \sigma \in \mathcal{R}$. $\square$

**Definition 4.1.7 (Gelfand-Kazhdan property).** Let $G$ be a topological group, $H$ a subgroup, $\chi \colon H \to \mathbb{C}$ a function and $\sigma \colon G \to G$ a homeomorphism. The triple has the *Gelfand-Kazhdan property* if every distribution $D$ with $D(f(h_1^{-1} \cdot h_2)) = \chi(h_1)\chi(h_2)^{-1} D(f)$ for all $h_1, h_2 \in H$ also satisfies $D(f \circ \sigma) = D(f)$.

**Corollary 4.1.8 (The criterion for $\mathrm{GL}_n$).** The triple $(N, \psi_N, \sigma)$ in $\mathrm{GL}_n(F)$ has the Gelfand-Kazhdan property.

Lean: `GroundTheory.Automorphic.Whittaker.biEquivariantSigmaInvariant_GL`.

*Proof.* This is [Theorem 4.1.6](/entry/distribution-sigma-invariant/) applied to $D$, with the two-sided translate $x \mapsto f(h_1^{-1} x h_2)$ written as the bi-translate of $f$. $\square$

**Remark 4.1.9 (Formalization).** The four results are in [WhittakerDistribution.lean](lean:GroundTheory/AutomorphicForms/WhittakerDistribution.lean#L573) and [WhittakerLocal.lean](lean:GroundTheory/AutomorphicForms/WhittakerLocal.lean#L15). The ranks $r_{ij}$ are `llRank`, the cells are `bruhatCell`, and the two cell lemmas are `cell_relevant` (line 438) and `cell_irrelevant` (line 404). The proof of the lemma by maximal $\Phi$ is a proof by contradiction, not an induction on the closure order of cells. The file turns off the linter for unused section variables at line 14. No hypothesis is unused.
