---
title: The product formula in dimension one
decls:
  - GroundTheory.Heights₂.Heights.AutoClose.Inter_R1Indep
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The product formula in dimension one

This section proves that on an arithmetic variety of dimension one, the arithmetic degree of a hermitian line bundle computed from a section $s$ does not depend on $s$. The degree is the sum of the logarithms of the residue field sizes along the divisor of $s$, minus the sum of $\log\|s\|$ over the complex points. Independence of the section is the product formula for the number field of the variety. The result is the first step of the recursion that defines arithmetic intersection numbers, and it is used in [the existence of the intersection family](/entry/thm-iexists/) of the chapter on sup norms of theta functions.

We use the notation of the previous section: the multigraded ring $\mathbb{Z}[x]$, arithmetic varieties $P$, hermitian line bundles $\bar A = (a, h_A)$, sections $s$, the divisor of $s$ with multiplicities $m_W$, and horizontal and vertical components.

### The degree in dimension one

Let $P$ be an arithmetic variety of dimension $1$. A closed point is a relevant multihomogeneous prime $W$ with $\dim \mathbb{Z}[x]/W = |K|$. A vertical component $W$ of a divisor lies over a prime number $p_W$, the characteristic of $\mathbb{Z}[x]/W$. Its degree $\deg W$ is the length over $\mathbb{Z}$ of the ring $\mathbb{Z}[x]/(W + (x_{k,i_k} - 1)_k)$, for a choice of one variable $x_{k,i_k}$ outside $W$ in each block. So $\deg W \cdot \log p_W$ is the logarithm of the size of the residue field of $W$.

**Definition 4.13.1 (Recursive term).** Let $I$ be any function that assigns a real number to an arithmetic variety and a family of hermitian line bundles. For a hermitian line bundle $\bar A$ and a section $s$ of $\bar A$ on $P$, put
$$\begin{aligned}
R_I(\bar A, s) &= \sum_{W \text{ horizontal}} m_W\, I(W) + \sum_{W \text{ vertical}} m_W \deg W \log p_W \\
&\quad - \int_{P(\mathbb{C})} \log\|s\|,
\end{aligned}$$
where the sums run over the components of the divisor of $s$ on $P$, and the integral with no forms is the integral over the zero-dimensional variety $P(\mathbb{C})$.

In higher dimension, $R_I$ is the right side of the recursion that defines the arithmetic intersection numbers $I$; the horizontal term then carries the lower-dimensional intersection numbers. In dimension one, $R_I(\bar A, s)$ is the classical arithmetic degree $\log \#(A/sA) - \sum_\sigma \log\|s\|_\sigma$ of the hermitian line bundle on an order of a number field.

### The theorem

**Theorem 4.13.2 (Independence of the section in dimension one).** Let $P$ be an arithmetic variety of dimension $1$, let $I$ be any function as above, let $\bar A$ be a hermitian line bundle, and let $s$ and $t$ be sections of $\bar A$ on $P$. Then
$$R_I(\bar A, s) = R_I(\bar A, t).$$

Lean: `GroundTheory.Heights₂.Heights.AutoClose.Inter_R1Indep` (also `GroundTheory.Heights₂.Heights.Inter.RegularityIndependence.proof`)

The function field $F$ of $P$ is the field of fractions $u/v$ of multihomogeneous elements of the same multidegree with $v \notin P$. Its regular ring $\mathcal{O}_P$ is the set of $x \in F$ that lie in the local ring of $P$ at every closed point. The proof uses the following three facts, which are proved in the development.

**Lemma 4.13.3 (Points).** The set $P(\mathbb{C})$ is finite up to scaling. There are a finite set $R$ of representatives and a bijection $t \mapsto \sigma_t$ from $R$ to the ring maps $F \to \mathbb{C}$ such that $\sigma_t(u/v) = u(t)/v(t)$. The integral over $P(\mathbb{C})$ of a scaling invariant function $g$ is $\sum_{t \in R} g(t)$.

Lean: `GroundTheory.Heights₂.Heights.Inter.regularityPointsSum_holds.full` (also `GroundTheory.Heights₂.Heights.Inter.regularityEmbedding_holds.full`)

**Lemma 4.13.4 (Maximal ideals of the regular ring).** The regular ring $\mathcal{O}_P$ is a free $\mathbb{Z}$-module of finite rank, equal to $[F : \mathbb{Q}]$ when $F$ is a number field. Every maximal ideal of $\mathcal{O}_P$ is contained in the maximal ideal of the local ring at some closed point.

Lean: `GroundTheory.Heights₂.Heights.Inter.RegularityOrder.full` (also `GroundTheory.Heights₂.Heights.AutoClose.Inter_R1RegMaxSurj`)

**Lemma 4.13.5 (Vertical part and norms).** Let $f$ and $g$ be multihomogeneous of the same multidegree, not in $P$, and let $x = f/g \in F$. Then
$$\sum_{W} m_W(f) \deg W \log p_W - \sum_{W} m_W(g) \deg W \log p_W = \sum_{\sigma : F \to \mathbb{C}} \log|\sigma(x)|,$$
where the sums run over the vertical components of the divisors of $f$ and of $g$.

Lean: `GroundTheory.Heights₂.Heights.Inter.VerticalEmbedding.of_remaining`

The vertical lemma is the classical identity $\log\#(\mathcal{O}/x\mathcal{O}) = \log|N_{F/\mathbb{Q}}(x)|$, written divisor by divisor. At a closed point $W$, divide $f$ by a monomial $t_W$ of the same multidegree that does not vanish at $W$. Then $m_W(f)$ is the length of the local ring $\mathcal{O}_W$ modulo $f/t_W$, and the length times $\deg W \log p_W$ is $\log\#(\mathcal{O}_W/(f/t_W))$. The local terms multiply to the norm, and the lemma on maximal ideals makes sure that every prime of $\mathcal{O}_P$ is seen by some closed point.

*Proof of the theorem.* First, the divisors of $s$ and $t$ have no horizontal components. A horizontal component $W$ would be an arithmetic variety of dimension $0$, which does not exist: a relevant multihomogeneous prime with $W \cap \mathbb{Z} = 0$ has $\dim \mathbb{Z}[x]/W \ge |K| + 1$. So the function $I$ does not enter, and
$$R_I(\bar A, s) = V(s) - \int_{P(\mathbb{C})} \log\|s\|,$$
where $V(s)$ is the vertical sum. For the same reason, $s$ and $t$ do not vanish at any complex point of $P$: such a point would lie on a horizontal component of the divisor.

Second, at each point $z$ of $P(\mathbb{C})$,
$$\log\|s\|(z) = \log\frac{|s(z)|}{|t(z)|} + \log\|t\|(z),$$
since both norms use the same $h_A$. The integral over the finite set $P(\mathbb{C})$ is a finite sum, so
$$\int_{P(\mathbb{C})} \log\|s\| = \int_{P(\mathbb{C})} \log\frac{|s|}{|t|} + \int_{P(\mathbb{C})} \log\|t\|.$$
The function $|s|/|t|$ is invariant under scaling, because $s$ and $t$ have the same multidegree.

Third, the product formula. Let $x = s/t \in F$. By the points lemma, the integral of $\log(|s|/|t|)$ is $\sum_{t' \in R} \log|s(t')/t(t')| = \sum_\sigma \log|\sigma(x)|$. By the vertical lemma this is $V(s) - V(t)$. Hence
$$\begin{aligned}
R_I(\bar A, s) &= V(s) - \Bigl(V(s) - V(t)\Bigr) - \int_{P(\mathbb{C})} \log\|t\| \\
&= R_I(\bar A, t). \qquad \square
\end{aligned}$$

**Example 4.13.6.** Let $K$ have one element and $P = (x_1 - 2x_0) \subseteq \mathbb{Z}[x_0, x_1]$, the point $[1 : 2]$ of $\mathbb{P}^1_{\mathbb{Z}}$. Then $\mathbb{Z}[x]/P \cong \mathbb{Z}[x_0]$ has dimension $2 = 1 + |K|$, so $P$ has dimension $1$, and $P(\mathbb{C})$ is the single point $z = (1, 2)$. Take $\bar A$ of degree $1$ with $h_A(z) = (|z_0|^2 + |z_1|^2)^{1/2}$.

For $s = x_0$, the ideal $P + (x_0) = (x_0, x_1)$ is not relevant, so the divisor is empty, and
$$R_I(\bar A, x_0) = -\log\frac{1}{\sqrt 5} = \tfrac{1}{2}\log 5.$$
For $t = x_1$, the divisor is the closed point $W = (2, x_1)$ over $p = 2$ with $m_W = 1$ and $\deg W = 1$, and
$$R_I(\bar A, x_1) = \log 2 - \log\frac{2}{\sqrt 5} = \tfrac{1}{2}\log 5.$$
The common value $\frac{1}{2}\log 5$ is the Fubini-Study height of the point $[1 : 2]$.

**Remark 4.13.7.** The theorem needs no smoothness of $h_A$, since only finitely many values of $h_A$ enter, and it holds for every function $I$, since $I$ only enters through horizontal components. The vertical lemma is where the arithmetic is. For $P$ equal to a point of $\mathbb{P}^N_{\mathbb{Z}}$ with residue field $\mathbb{Q}$, it says that $\sum_p v_p(x)\log p = \log|x|$ for a nonzero rational number $x$, which is the product formula for $\mathbb{Q}$.

**Remark 4.13.8 (Formalization).** The theorem is one line ([NumbersDVRC3ResidualContractionComponent.lean](lean:GroundTheory/HeightsAndTheta/Heights/LocalFiniteness/NumbersDVRC3ResidualContractionComponent.lean#L88)): it applies `RegularityIndependence.of_remaining` to the closed statement on maximal ideals, through an explicit `@` application. The statement is `DimensionOneRationalSectionIndependence` ([ThmISt.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArithmeticIntersection/RationalSections/ThmISt.lean#L59)). The main argument is in [NotIsHorizontalOfDimOne.lean](lean:GroundTheory/HeightsAndTheta/Heights/Intersections/NotIsHorizontalOfDimOne.lean#L204). The statement asks for no smoothness of the metric and quantifies over all functions $I$, not only over intersection families. The fact that no arithmetic variety of dimension $0$ exists and the finiteness of the fibres of a good projection enter as separate closed statements.
