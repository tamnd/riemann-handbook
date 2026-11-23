---
title: A line of large degree from the successive minima bounds
decls:
  - GroundTheory.Heights₂.Heights.LineOfLargeDegreeFromZ.ofOpen
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A line of large degree from the successive minima bounds

This section proves an absolute Siegel lemma: every hermitian lattice $F$ of rank $i$ over a number field contains, after a finite extension of the field, a line of normalized degree at least $\mu(F) - \frac12 \log i - \varepsilon$. The proof realizes the projective space of $F$ as an arithmetic variety in a projective space over $\mathbb{Z}$, with a hermitian line bundle built from the metric of $F$. Then it compares the lower and the upper successive minima bounds for this variety. The result is the core of [the Siegel lemma from the successive minima bounds](/entry/line-of-large-degree-of-use/), which gives the slope bound for Lie algebras in [the Weil bound chapter](/proof/weil-bound/).

### Hermitian lattices and their lines

Let $K$ be a number field and $i \ge 1$. A hermitian lattice of rank $i$ over $K$ is a finitely generated $\mathcal{O}_K$-submodule $L \subseteq K^i$ that spans $K^i$, together with a positive definite hermitian matrix $H_\sigma$ of size $i$ for each embedding $\sigma : K \to \mathbb{C}$, such that $H_{\bar\sigma} = \overline{H_\sigma}$. This is a [hermitian lattice](/learn/arakelov/#hermitian-lattices-and-slopes) in the sense of Volume 1, written in the coordinates of $K^i$. For two subgroups $A$ and $B$ of the same group we write $[A : B] = [A : A \cap B]/[B : A \cap B]$ for the generalized index.

**Definition 4.14.1 (Degree, slope, degree of a line).** The degree of $F = (L, H)$ is
$$\deg F = \log [L : \mathcal{O}_K^i] - \frac12 \sum_{\sigma} \log \det H_\sigma,$$
and its slope is $\mu(F) = \deg F / ([K : \mathbb{Q}]\, i)$. Let $K'$ be a finite extension of $K$, let $L' = \mathcal{O}_{K'} L$, and let $v \in K'^i$. The degree of the line of $v$ is
$$\begin{aligned}
\deg_{K'}(v) = \frac{1}{[K' : \mathbb{Q}]} \Bigl( &\log [L' \cap K'v : \mathcal{O}_{K'} v] \\
&- \frac12 \sum_{\sigma'} \log \bigl(\sigma'(v)^* H_{\sigma'|_K}\, \sigma'(v)\bigr) \Bigr),
\end{aligned}$$
where $\sigma'$ runs over the embeddings $K' \to \mathbb{C}$.

The first term is the arithmetic part of the degree of the line and the second term is its archimedean part. Division by $[K' : \mathbb{Q}]$ makes degrees over different fields comparable.

### The dual variety and its line bundle

The dual of $F$ is the $\mathbb{Z}$-module
$$F^\vee = \{\varphi \in K^i : \varphi \cdot x \in \mathcal{O}_K \text{ for all } x \in L\}.$$
Fix a $\mathbb{Z}$-basis $(b_t)_{t \in T}$ of $F^\vee$. Then $|T| = i\,[K : \mathbb{Q}]$.

**Definition 4.14.2 (Dual variety, dual line bundle).** The dual variety $P_b$ is the kernel of the map
$$\mathbb{Z}[x_t : t \in T] \to K(X_1, \dots, X_i), \qquad x_t \mapsto \sum_j b_t(j)\, X_j.$$
Let $M$ be the complex matrix with rows indexed by $T$ and columns indexed by pairs $(\sigma, j)$, with entries $M_{t, (\sigma, j)} = \sigma(b_t(j))$. The dual line bundle $\bar A_F$ has degree $1$ and the metric
$$h_F(z)^2 = \sum_\sigma w_\sigma^* H_\sigma\, w_\sigma, \qquad w = M^{-1} z,$$
where $w_\sigma = (w_{\sigma, j})_j$.

The matrix $M$ is invertible, so $h_F$ is well defined and positive away from $0$. On a point $z = M w$ with $w$ supported on one embedding $\sigma$, the value $h_F(z)$ is the norm of $w_\sigma$ for the metric $H_\sigma$. So $\bar A_F$ carries the metric of $F$ on each conjugate of the projective space of $K^i$.

The following facts are proved in the development, without open hypotheses. The variety $P_b$ is an arithmetic variety of dimension $i$. The bundle $\bar A_F$ is semipositive on $P_b$ and invariant under complex conjugation, and it is nef on the fibres since its degree is $1 \ge 0$.

### The theorem

The proof uses three inputs that the theorem takes as hypotheses. Let $I$ be an intersection system, and for an arithmetic variety $P$ of dimension $D + 1$ write $\deg_{\mathbb{C}}$ for the degree of a closed point and $\gamma(P, \bar A)$ for the geometric degree of $P$ with respect to $\bar A$, which is the integral of $c_1(\bar A)^D$ over $P(\mathbb{C})$.

- The lower successive minima bound. Let $\bar A$ be semipositive, nef on the fibres and conjugation invariant on $P$, and let $e \in \mathbb{R}$. If $e \deg_{\mathbb{C}} W \le I(W; \bar A)$ for every closed point $W$ of $P$, then $(D+1)\, e\, \gamma(P, \bar A) \le I(P; \bar A^{D+1})$.
- The upper successive minima bound. Under the same hypotheses on $\bar A$, if a Zariski dense set of closed points $W$ of $P$ has $I(W; \bar A) \le e' \deg_{\mathbb{C}} W$, then $I(P; \bar A^{D+1}) \le (D+1)\, e'\, \gamma(P, \bar A)$.
- An intersection system exists.

**Theorem 4.14.3 (Line of large degree).** Assume the lower and the upper successive minima bounds, and assume that an intersection system exists. Let $K$ be a number field, let $i \ge 1$, let $F$ be a hermitian lattice of rank $i$ over $K$ and let $\varepsilon > 0$. Then there are a finite extension $K'$ of $K$ and a nonzero $v \in K'^i$ with
$$\mu(F) - \tfrac12 \log i - \varepsilon \le \deg_{K'}(v).$$

Lean: `GroundTheory.Heights₂.Heights.LineOfLargeDegreeFromZ.ofOpen` (also `GroundTheory.Heights₂.Heights.LineOfLargeDegreeFromZ.proofDual`)

The proof reduces the theorem to three lemmas on the dual variety. Fix $K$, $i$, $F$, a basis $b$ of $F^\vee$ and an intersection system $I$.

**Lemma 4.14.4 (Closed points give lines).** For every closed point $W$ of $P_b$, the degree $\deg_{\mathbb{C}} W$ is positive, and there are a finite extension $K'$ of $K$ and a nonzero $v \in K'^i$ with
$$\deg_{K'}(v) = -\frac{I(W; \bar A_F)}{\deg_{\mathbb{C}} W}.$$

Lean: `GroundTheory.Heights₂.Heights.DualPointLineDegree.ofOpen`

**Lemma 4.14.5 (Top intersection bound).** Assume the upper successive minima bound. Then
$$I(P_b; \bar A_F^{\,i}) \le i \Bigl(-\mu(F) + \tfrac12 \log i\Bigr)\, \gamma(P_b, \bar A_F).$$

Lean: `GroundTheory.Heights₂.Heights.DualTopBound.ofOpen`

**Lemma 4.14.6 (Positive geometric degree).** The geometric degree $\gamma(P_b, \bar A_F)$ is positive.

Lean: `GroundTheory.Heights₂.Heights.DualGeomDegPos.ofOpen`

For the first lemma, a closed point $W$ is given by a point of $P_b$ with coordinates in a number field $K'$, and $v$ is the vector of $K'^i$ that it defines. The intersection number $I(W; \bar A_F)$ is the arithmetic degree of the previous section, and its vertical part is an index of lattices. The top bound is proved in three moves. First, a change of the metric $H$ to the identity changes $I(P_b; \bar A_F^{\,i})$ by $(\deg F_{\mathrm{std}} - \deg F)\, g$, where $F_{\mathrm{std}}$ is $L$ with the identity metric and $g$ is the geometric degree of $\mathbb{P}^{i-1}$ with the Fubini-Study metric. Second, a change of the lattice $L$ to $\mathcal{O}_K^i$ changes it by $-\deg F_{\mathrm{std}}\, g$. Third, for the standard lattice the intersection number is $[K : \mathbb{Q}]$ times the Fubini-Study height of $\mathbb{P}^{i-1}_{\mathbb{Z}}$, which is at most $i \cdot \frac12 \log i \cdot g$ by the upper bound applied to the points with coordinates in the roots of unity. With $\gamma(P_b, \bar A_F) = [K : \mathbb{Q}]\, g$ and $\deg F = [K : \mathbb{Q}]\, i\, \mu(F)$, the three moves give the bound.

*Proof of the theorem.* Suppose that the conclusion fails. Then every finite extension $K'$ and every nonzero $v \in K'^i$ have
$$\deg_{K'}(v) < \mu(F) - \tfrac12 \log i - \varepsilon.$$
Put $e = -\mu(F) + \frac12 \log i + \varepsilon$, so that $\deg_{K'}(v) < -e$ for all such $v$.

Let $W$ be a closed point of $P_b$. The first lemma gives $\deg_{\mathbb{C}} W > 0$ and a line $v$ with $\deg_{K'}(v) = -I(W; \bar A_F)/\deg_{\mathbb{C}} W$. So $-I(W; \bar A_F)/\deg_{\mathbb{C}} W < -e$, and
$$e \deg_{\mathbb{C}} W \le I(W; \bar A_F).$$

The variety $P_b$ has dimension $i = (i - 1) + 1$, and $\bar A_F$ is semipositive, nef on the fibres and conjugation invariant. The lower successive minima bound, with $D = i - 1$, gives
$$i\, e\, \gamma(P_b, \bar A_F) \le I(P_b; \bar A_F^{\,i}).$$
By the top intersection bound,
$$\begin{aligned}
i\, e\, \gamma(P_b, \bar A_F) &\le I(P_b; \bar A_F^{\,i}) \\
&\le i \Bigl(-\mu(F) + \tfrac12 \log i\Bigr)\, \gamma(P_b, \bar A_F).
\end{aligned}$$
The difference of the two outer terms is $i\, \varepsilon\, \gamma(P_b, \bar A_F) \le 0$. But $i \ge 1$, $\varepsilon > 0$ and $\gamma(P_b, \bar A_F) > 0$ by the third lemma, so this product is positive. This is a contradiction. $\square$

**Example 4.14.7.** Let $K = \mathbb{Q}$, $i = 1$, $L = 2\mathbb{Z}$ and $H = (c)$ with $c > 0$. Then $\deg F = \log[2\mathbb{Z} : \mathbb{Z}] - \frac12 \log c = -\log 2 - \frac12\log c$, and $\mu(F) = \deg F$. For $K' = \mathbb{Q}$ and $v = 1$, the lattice $L \cap \mathbb{Q}v$ is $2\mathbb{Z}$, so $\deg_{\mathbb{Q}}(1) = -\log 2 - \frac12 \log c = \mu(F)$. In rank one the only line is $F$ itself, and the theorem holds with $\frac12 \log 1 = 0$.

**Remark 4.14.8.** The constant $\frac12 \log i$ is the Fubini-Study constant: it comes from the bound for the height of $\mathbb{P}^{i-1}_{\mathbb{Z}}$ through the points with coordinates in the roots of unity, which have height $0$ for the $\ell^\infty$ norm and height at most $\frac12 \log i$ for the $\ell^2$ norm. The theorem allows the extension $K'$ to depend on $F$ and $\varepsilon$. Over $K$ itself, the classical Siegel lemma has an extra term that depends on the discriminant of $K$.

**Remark 4.14.9 (Formalization).** The theorem ([Assembly.lean](lean:GroundTheory/HeightsAndTheta/Heights/HeightKernels/Assembly.lean#L110)) applies `LineOfLargeDegreeFromZ.proofDual` ([PLineOfLargeDegreeDual.lean](lean:GroundTheory/HeightsAndTheta/Heights/HeightKernels/PLineOfLargeDegreeDual.lean#L9)) to the closed facts on the dual variety and to the three lemmas above. It is not closed: it takes 13 open statements as hypotheses. Two of them, `VertRIndex` and `SectionIndexNorm`, give the vertical part of a closed point as an index and compare that index with a norm; they enter the first lemma. Nine of them enter the top bound: the metric energy, the change of basis, the stacked bases and their degrees, the base change for the standard lattice, the identification of the Grassmannian of lines with projective space, the chart formulas for the geometric degree and the invariance of the chart mass. The last two, `DegreeStatement` and `PtsIndepStatement`, enter the positivity of the geometric degree. The three inputs of the theorem itself are the premises of the statement `LineOfLargeDegreeFromZ.Statement` ([StatementsLineDegree.lean](lean:GroundTheory/HeightsAndTheta/Heights/HeightKernels/StatementsLineDegree.lean#L117)), whose conclusion is `LineOfLargeDegree.Statement` ([KernelsLattice.lean](lean:GroundTheory/HeightsAndTheta/Heights/KernelsLattice.lean#L85)). The file of the statement also defines a direct model of projective space, with the lattice line bundle and three statements for it, and this proof does not use them. In `LineOfLargeDegree.proof` the lower successive minima bound is supplied from the arithmetic Hilbert-Samuel statement.
