---
title: Branches of an affine variety proper at a point
decls:
  - GlobalTheory.CompanionTheory.Ar.Branch.branchProperAtPoint
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Branches of an affine variety proper at a point

Sections 7 to 9 study the zero set of a prime ideal of $\mathbb{C}[x_1, \dots, x_n]$ near a point, through local holomorphic parametrizations that we call branches. They prepare the Poincaré and Lelong formula, which compares the current of integration on a hyperplane section with the $dd^c$ of $\log |\ell|$. That formula needs two local facts. First, a branch does not come back near one of its points from the rim of its domain; this section proves it. Second, the multiplicity of a component of a hyperplane section is the sum of the orders of vanishing along the branches; Sections 8 and 9 prove it. The results are inputs of the [literature step](/step/every-character-of-literature/).

Fix $n \geq 0$ and an ideal $J \subseteq \mathbb{C}[x_1, \dots, x_n]$. Let $Z(J) \subseteq \mathbb{C}^n$ be its zero set. On $\mathbb{C}^k$ we use the norm $|t| = \max_i |t_i|$, so the ball $B(0, r)$ is the polydisc of radius $r$ ([holomorphic functions](/learn/complex-analysis/#holomorphic-functions)). For $u \in \mathbb{C}^n$ let $\ell_u(x) = \sum_j u_j x_j$, both as a function on $\mathbb{C}^n$ and as a linear form in $\mathbb{C}[x]$.

**Definition 7.7.1 (Branch).** Let $k \geq 0$ and $p \in \mathbb{C}^n$. A *branch of $J$ of dimension $k$ at $p$* is a pair of a radius $r > 0$ and a map $\gamma : \mathbb{C}^k \to \mathbb{C}^n$ such that $\gamma$ is holomorphic and injective on $B(0, r)$, $\gamma(0) = p$, and $\gamma(B(0, r)) \subseteq Z(J)$. The *image* of the branch is $\gamma(B(0, r))$. For $k = d + 1$, the *slice* of the branch is $\gamma(B(0, r) \cap \{t_0 = 0\})$.

**Definition 7.7.2 (Order of vanishing).** Let $F$ be a function on $\mathbb{C}^{d+1}$, $r > 0$ and $m \geq 0$. Then $F$ *vanishes to order $m$* on $B(0, r)$ if $F(t) = t_0^m H(t)$ for $t \in B(0, r)$, with $H$ holomorphic and nowhere zero on $B(0, r)$.

So $F$ vanishes exactly on the hyperplane $t_0 = 0$, to order $m$. For a curve branch, $d = 0$ and this says that $F$ has a zero of order $m$ at $0$ and no other zero on the disc.

**Theorem 7.7.3 (Branches are proper at a point).** Let $J \subseteq \mathbb{C}[x_1, \dots, x_n]$ be a prime ideal with $\dim \mathbb{C}[x]/J = k$, and let $u \in \mathbb{C}^n$ with $\ell_u \notin J$. Let $p, x \in \mathbb{C}^n$, and let $\gamma_1, \dots, \gamma_m$ be branches of $J$ of dimension $k$ at $p$, with radii $r_1, \dots, r_m$. Assume:

1. there is a neighbourhood $N$ of $x$ such that $Z(J) \cap N$ is contained in the union of the images of the $\gamma_b$;
2. for $b \neq b'$, the images of $\gamma_b$ and $\gamma_{b'}$ meet only in the hyperplane $\{\ell_u = 0\}$.

Let $b$ be an index, let $s \in B(0, r_b)$ with $\gamma_b(s) = x$, and let $P$ be a neighbourhood of $s$. Then there is $\varepsilon > 0$ such that each $\tau \in B(0, r_b)$ with $|\gamma_b(\tau) - x| < \varepsilon$ is in $P$.

Lean: `GlobalTheory.CompanionTheory.Ar.Branch.branchProperAtPoint`.

So the inverse image under $\gamma_b$ of a small ball around $x$ lies in a given neighbourhood of $s$. In other words, the inverse of $\gamma_b$ on its image is continuous at $x$. The danger is a part of the image near the rim of $B(0, r_b)$ that comes back close to $x$. Injectivity alone does not exclude this.

*Proof.* We take as given the following fact.

*Away from the rim.* Under the hypotheses of the theorem, there are $\varepsilon_0 > 0$ and $\rho < r_b$ such that each $\tau \in B(0, r_b)$ with $|\gamma_b(\tau) - x| < \varepsilon_0$ has $|\tau| \leq \rho$.

Its proof uses the normalization of the affine variety $Z(J)$: the normal model exists and is proper over $Z(J)$, branches lift to it, it is locally irreducible at its points, and a branch contains a normal point. We do not give this proof here.

Now let $P' \subseteq P$ be an open neighbourhood of $s$. Let $K = \bar B(0, \rho) \setminus P'$, the closed polydisc of radius $\rho$ minus $P'$. It is closed and bounded, so compact. It lies in $B(0, r_b)$, where $\gamma_b$ is continuous, so $\gamma_b(K)$ is compact. Since $\gamma_b$ is injective on $B(0, r_b)$ and $s \notin K$, we have $x = \gamma_b(s) \notin \gamma_b(K)$. A compact set that does not contain $x$ has positive distance from $x$, so there is $\delta > 0$ with $B(x, \delta) \cap \gamma_b(K) = \emptyset$. Put $\varepsilon = \min(\varepsilon_0, \delta)$.

Let $\tau \in B(0, r_b)$ with $|\gamma_b(\tau) - x| < \varepsilon$. Then $|\tau| \leq \rho$ by the fact above, since $\varepsilon \leq \varepsilon_0$. Also $\gamma_b(\tau) \notin \gamma_b(K)$, since $\varepsilon \leq \delta$, so $\tau \notin K$. Hence $\tau \in \bar B(0, \rho) \setminus K \subseteq P' \subseteq P$. $\square$

The theorem is an input of a limit statement for the Lelong numbers at the branches, which leads to the Poincaré and Lelong theorems. In such a limit one integrates over the inverse image under $\gamma_b$ of a small ball around $x$. The theorem shows that this inverse image is a small neighbourhood of $s$, so the integral becomes a local integral on the parameter space of one branch.

**Remark 7.7.4 (Formalization).** The theorem is in [BranchProperAtPointHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/BranchProperAtPointHolds.lean#L166), with the statement in [StBranchProperAtPoint.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/StBranchProperAtPoint.lean#L11). Its proof is about 160 `have` lines that apply the proofs of named statements to each other. The last two are `BranchAwayFromRim.proof` and `BranchProperAtPoint.proof`. The branches are `VarBranch` in [StatementsCurrent.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/StatementsCurrent.lean#L61). The ball is `Metric.ball` on `Fin k → ℂ`, which carries the sup norm, so it is a polydisc and not a Euclidean ball. The point $x$ is not assumed to lie in an image; the conclusion is about a given preimage $s$. The theorem reaches the literature step through `Ar.Lelong.lelongLimitAtBranches` and the Poincaré and Lelong theorems `poincareLelong` and `poincareLelongInv`.
