---
title: Lie algebras of semi-abelian schemes
decls:
  - GlobalTheory.Nef.semiAbelianLieSeminegative
  - GlobalTheory.T.lieSheaf_semiAbelian_semiNeg_of_isAlgClosed
  - GlobalTheory.Nef.semiNeg_lie_of_isAlgClosed
  - GlobalTheory.T.lie_subsheaf_lines_degree_nonpos
  - GlobalTheory.Nef.linesLE_zero_of_sub_lie
  - GlobalTheory.T.adelicMatrixFamilyDegree_le_rank_mul_line_bound
  - GlobalTheory.Nef.deg_le_rank_mul_of_linesLE
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lie algebras of semi-abelian schemes

Let $G$ be a semi-abelian scheme over a projective curve $C$ in characteristic $0$. This section proves that each sub-bundle of the Lie algebra of $G$ has a determinant of degree at most $0$. This is the input `SemiAbelianLieSeminegative` of the step [every character from the literature](/step/every-character-of-literature/), where it replaces [the statement from the literature](/entry/semi-abelian-lie-seminegative-of-literature/). By duality it says that the Hodge bundle of $G$ is nef in a weak sense; see the [Hodge bundle of Volume 1](/learn/arakelov/#the-hodge-bundle-and-zarhins-trick) and the remark on seminegativity in the [toroidal compactifications of Volume 1](/learn/abelian-varieties/#toroidal-and-minimal-compactifications).

The proof has three steps. We first pass to an algebraically closed base field. Over such a field we describe a sub-bundle by a family of matrices, one for each place of the function field of $C$. A rigidity property of formal paths in $G$ shows that each line in the generic fibre has degree at most $0$, also after any finite extension of the function field. An induction on the rank, with an Iwasawa decomposition at all places, then bounds the degree of the whole family.

### Curves, Lie algebras and seminegativity

**Definition 5.4.1 (Curve).** Let $k$ be a field. A curve over $k$ is a scheme $C$ with a structure of $k$-algebra on $\Gamma(C, \mathcal{O}_C)$, such that $C$ is smooth of relative dimension $1$, projective and geometrically connected over $k$.

Lean: `GlobalTheory.Nef.IsCurve`.

**Definition 5.4.2 (Lie algebra).** Let $G$ be a group scheme over $C$ with unit section $e$. The Lie algebra $\operatorname{Lie}(G)$ is the dual of the conormal sheaf $\omega_G$ of $e$.

Lean: `GlobalTheory.Nef.Lie`.

A semi-abelian scheme over $C$ is a commutative group scheme that is smooth, separated, quasi-compact and geometrically connected over $C$, and whose geometric fibres are extensions of abelian varieties by tori.

**Definition 5.4.3 (Seminegative).** A sheaf $\mathcal{F}$ on a curve $C$ over $k$ is seminegative if for each vector bundle $W$ of rank $r$ on $C$ and each monomorphism $W \to \mathcal{F}$,
$$\deg_C(\det W) \le 0.$$

Lean: `GlobalTheory.Nef.SemiNeg`.

The degree here is the intersection number of [the first section](/entry/chern-int-eq-top-self-of-generated/) on the curve $C$.

### Families of matrices over a function field

Let $k$ be a field and $F$ a function field of one variable over $k$: there is an element $t \in F$, transcendental over $k$, with $F$ finite over $k(t)$. A place of $F$ is a surjective valuation $v : F \to \mathbb{Z} \cup \{\infty\}$ that is trivial on $k^\times$. For $x \in F^r$ put $\operatorname{ord}_v(x) = \min_i \operatorname{ord}_v(x_i)$.

**Definition 5.4.4 (Degree of a matrix family).** A family $g = (g_v)$ of $r \times r$ matrices over $F$, one for each place $v$, is admitted if each $\det g_v$ is nonzero and $g_v$ fails to be unimodular for only finitely many $v$. Its degree and the degree of a vector $x \in F^r$ are
$$\deg g = \sum_v \operatorname{ord}_v \det g_v, \qquad \deg_g(x) = \sum_v \operatorname{ord}_v(g_v x).$$

Lean: `GlobalTheory.Nef.deg` (also `GlobalTheory.Nef.admitted`, the condition, and `GlobalTheory.Nef.degLine`, the degree of a vector).

Both sums are finite sums in the sense of `finsum`, so they are $0$ when the support is infinite. Let $E$ be a finite extension of $F$ and $\rho$ a map from places of $E$ to places of $F$ that sends each place to its restriction. The pull back of $g$ is the family $g_{\rho(p)}$ at the place $p$ of $E$, with entries in $E$.

**Definition 5.4.5 (Lines of bounded degree).** A family $g$ has lines of degree at most $b \in \mathbb{R}$ if for each finite extension $E$ of $F$, each restriction map $\rho$ and each nonzero $x \in E^r$, the degree of $x$ for the pull back of $g$ is at most $b \cdot [E : F]$.

Lean: `GlobalTheory.Nef.LinesLE`.

If $W$ is a vector bundle on $C$ with a frame $s$ on an open set $V_0$, the development attaches to each place $v$ of $K(C)$ a matrix $g_v$: the matrix of $s$ in a frame of $W$ at a point of a valuation ring that extends the generic point. We do not unfold this condition. The degree of $g$ is then the degree of $\det W$.

### The degree bound

**Theorem 5.4.6 (Degree from lines).** Let $k$ be an algebraically closed field of characteristic $0$, and let $F$ be a function field of one variable over $k$. Let $g$ be an admitted family of $r \times r$ matrices over $F$, and let $b \in \mathbb{R}$. If $g$ has lines of degree at most $b$, then $\deg g \le r b$.

Lean: `GlobalTheory.Nef.deg_le_rank_mul_of_linesLE` (also `GlobalTheory.T.adelicMatrixFamilyDegree_le_rank_mul_line_bound`, a second name).

*Proof.* We use induction on $r$. For $r = 0$ each determinant is $1$, so $\deg g = 0$. Assume the claim for $r$, and let $g$ have rank $r + 1$. Let $S$ be the set of $c$ such that $g$ has lines of degree at most $c$. The set $S$ contains $b$. It is bounded below by the degree of the first basis vector for $g$ itself, with $E = F$. Let $a = \inf S$. For each $E$, $\rho$ and $x$, the degree divided by $[E : F]$ is a lower bound of $S$, so $g$ has lines of degree at most $a$.

Let $\varepsilon > 0$. Since $a - \varepsilon \notin S$, there are $E$, $\rho$ and $x \neq 0$ with degree of $x$ greater than $(a - \varepsilon) n$, where $n = [E : F]$. The pull back $g'$ of $g$ to $E$ is admitted, $\deg g' = n \deg g$, and $g'$ has lines of degree at most $a n$. An Iwasawa decomposition at all places of $E$ gives an invertible matrix $h$ and unimodular matrices $u_v$ such that the first column of $u_v g'_v h$ is $0$ below the first entry. Let $q$ be the family of lower right $r \times r$ blocks. Then $q$ is admitted, and
$$\deg g' = \delta + \deg q, \qquad \delta = \deg_{g'}(x) > (a - \varepsilon) n.$$
A lemma on triangular families gives that $q$ has lines of degree at most $2 a n - \delta$. By induction, $\deg q \le r (2 a n - \delta)$. Since $\delta \le a n$,
$$\begin{aligned} n \deg g &\le \delta + r (2 a n - \delta) \\ &\le (r + 1) a n + r \varepsilon n. \end{aligned}$$
So $\deg g \le (r + 1) a + r \varepsilon$ for each $\varepsilon > 0$. Hence $\deg g \le (r + 1) a \le (r + 1) b$. $\square$

### Lines in the Lie algebra

**Lemma 5.4.7 (Lines in the Lie algebra).** Let $k$ be an algebraically closed field of characteristic $0$, let $C$ be a curve over $k$ with function field $K$, and let $x$ be the generic point. Let $G$ be a semi-abelian scheme over $C$, let $W$ be a vector bundle of rank $r$ and $i : W \to \operatorname{Lie}(G)$ a monomorphism. Let $s$ be a frame of $W$ on a nonempty open set $V_0$, and let $g$ be an admitted family of matrices that are local frames for $s$ at all places of $K$. Then $g$ has lines of degree at most $0$.

Lean: `GlobalTheory.Nef.linesLE_zero_of_sub_lie` (also `GlobalTheory.T.lie_subsheaf_lines_degree_nonpos`, a second name).

*Proof.* Assume that $E$ is a finite extension of $K$, $\rho$ is a restriction map and $w \in E^r$ is nonzero with positive degree for the pull back of $g$. The field $E$ has characteristic $0$. The point $\operatorname{Spec} E \to \operatorname{Spec} K \to C$ lies in $V_0$. The vector $\sum_j w_j \, i(s_j)$ is a tangent vector of $G$ at the unit over $E$, and there is a formal path $\xi$ in $G$ over $E$ with this tangent vector, of squaring type.

At each place $p$ of $E$ the vector $g_{\rho(p)} w$ is nonzero, since the determinant is nonzero. So there is a coordinate $u_p \neq 0$ that attains the norm, with $\operatorname{ord}_p(u_p) = \operatorname{ord}_p(g_{\rho(p)} w)$. The sum of these orders is the degree of $w$, which is positive; in particular the support is finite. At each place the generic path $\xi$ is a scaling of a path over the valuation ring. So $\xi$ is integral at all places, and it is rational. Rational paths of squaring type in a semi-abelian scheme are rigid, so $\xi$ is the trivial path. The tangent vector of the trivial path is $0$, so $w = 0$. This is a contradiction. $\square$

### Seminegativity

**Theorem 5.4.8 (Seminegativity over an algebraically closed field).** Let $k$ be an algebraically closed field of characteristic $0$, let $C$ be a curve over $k$ and let $G$ be a semi-abelian scheme over $C$. Then $\operatorname{Lie}(G)$ is seminegative.

Lean: `GlobalTheory.Nef.semiNeg_lie_of_isAlgClosed` (also `GlobalTheory.T.lieSheaf_semiAbelian_semiNeg_of_isAlgClosed`, a second name).

*Proof.* Let $W$ be a vector bundle of rank $r$ with a monomorphism $i : W \to \operatorname{Lie}(G)$. The generic point of $C$ gives the function field $K$, which is a function field of one variable over $k$. There is a nonempty open set $V_0$ with a frame $s$ of $W$, and an admitted family $g$ that consists of local frames for $s$ at all places of $K$. By the lemma on lines in the Lie algebra, $g$ has lines of degree at most $0$. By the theorem on the degree from lines with $b = 0$, $\deg g \le 0$. The degree of $\det W$ on $C$ is at most $0$ when the degree of such a family is at most $0$. $\square$

**Theorem 5.4.9 (Seminegativity of Lie algebras).** Let $k$ be a field of characteristic $0$, let $C$ be a curve over $k$ and let $G$ be a semi-abelian scheme over $C$. Let $W$ be a vector bundle of rank $r$ on $C$ and $i : W \to \operatorname{Lie}(G)$ a monomorphism. Then
$$\deg_C(\det W) \le 0.$$

Lean: `GlobalTheory.Nef.semiAbelianLieSeminegative`.

*Proof.* Let $\bar{k}$ be an algebraic closure of $k$. There is a curve $C'$ over $\bar{k}$ with a map $\pi : C' \to C$, such that a sheaf on $C$ is seminegative when its pull back to $C'$ is seminegative. The pull back of $G$ along $\pi$ is a semi-abelian scheme over $C'$, and its Lie algebra is isomorphic to the pull back of $\operatorname{Lie}(G)$. By the theorem over an algebraically closed field, this Lie algebra is seminegative, so the pull back of $\operatorname{Lie}(G)$ is seminegative. Hence $\operatorname{Lie}(G)$ is seminegative, and the bound holds for $W$. $\square$

**Remark 5.4.10 (Formalization).** The published statement `SemiAbelianLieSeminegative` takes the semi-abelian structure of $G$ as an instance argument, while `semiNeg_lie_of_isAlgClosed` takes it as an explicit hypothesis. The degree of a family and of a vector are `finsum`s, which are $0$ for an infinite support; the admitted condition makes the support of $\deg g$ finite, and the proof of the lemma on lines proves the finiteness of its support separately. The theorem on the degree from lines asks for an algebraically closed field $k$ of characteristic $0$. The descent to $\bar{k}$, the frames at all places, the formal paths and their rigidity, the Iwasawa decomposition and the lemma on triangular families are results of the development that the proofs cite. We did not unfold the condition that a matrix is a local frame at a place.
