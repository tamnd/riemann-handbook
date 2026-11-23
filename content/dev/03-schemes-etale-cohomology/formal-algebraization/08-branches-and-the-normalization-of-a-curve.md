---
title: Branches and the normalization of a curve
decls:
  - GlobalTheory.CompanionTheory.BranchNorm.placeHasBranch
  - GlobalTheory.CompanionTheory.BranchNorm.branchNormalisation
  - GlobalTheory.T.branch_normalisation_holds
  - GlobalTheory.CompanionTheory.Heights.CurveBranch.curveBranchLength
  - GlobalTheory.T.curve_branch_length_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Branches and the normalization of a curve

This section treats the case of curves. Let $I$ be an ideal of $\mathbb{C}[x_1, \dots, x_n]$ whose zero set is a curve near a point $q$, covered near $q$ by finitely many holomorphic discs through $q$. We prove that the discs are in bijection with the maximal ideals of the normalization of the local ring at $q$, and that the order of vanishing of a polynomial along a disc is its valuation at the corresponding maximal ideal. As a consequence, the multiplicity of the intersection of the curve with a hyperplane at $q$ is the sum of the orders of vanishing of the linear form along the discs. Section 9 reduces the general case to this one by generic linear slices.

We keep the notation of Section 7, and we use [local rings and dimension](/learn/commutative-algebra/#local-rings-and-dimension). Let $\mathfrak{m}_q \subseteq \mathbb{C}[x]$ be the maximal ideal of the polynomials that vanish at $q$.

**Definition 7.8.1 (Local ring, normalization and orders).** Let $I \subseteq \mathbb{C}[x_1, \dots, x_n]$ be an ideal and $q \in \mathbb{C}^n$.

1. $I$ is *radical at* $q$ if for each $f$ in the radical of $I$ there is a polynomial $s$ with $s(q) \neq 0$ and $s f \in I$.
2. The *local ring* of $I$ at $q$ is $\mathcal{O}_q = \mathbb{C}[x]_{\mathfrak{m}_q} / I \mathbb{C}[x]_{\mathfrak{m}_q}$. Its *normalization* $\bar{\mathcal{O}}_q$ is the integral closure of $\mathcal{O}_q$ in its total ring of fractions.
3. For a maximal ideal $P$ of $\bar{\mathcal{O}}_q$ and a polynomial $f$, $\operatorname{ord}_P(f) \in \mathbb{N} \cup \{\infty\}$ is the order of the image of $f$ in the localization of $\bar{\mathcal{O}}_q$ at $P$.
4. For a curve branch $c$ of $I$ at $q$ (a branch of dimension $1$), the *branch order* $\operatorname{ord}_c(f) \in \mathbb{N} \cup \{\infty\}$ is the order of vanishing at $\tau = 0$ of the holomorphic function $\tau \mapsto f(c(\tau))$.
5. For ideals $K$ and $W$ of a ring $B$, with $W$ prime, the *local multiplicity* $\operatorname{mult}_W(K)$ is the length of $B_W / K B_W$ as a $B_W$-module, if this length is finite, and $0$ if it is infinite. If $W$ is not prime, $\operatorname{mult}_W(K) = 0$.

If $I$ is radical at $q$, then $\mathcal{O}_q$ is reduced. In the theorems below the curve branches $c_1, \dots, c_m$ are branches of $I$ at $q$ of dimension $1$, and we use two hypotheses on them:

- (Cover) there is a neighbourhood $N$ of $q$ such that $Z(I) \cap N$ is contained in the union of the images of the $c_b$;
- (Meet at $q$) for $b \neq b'$, the images of $c_b$ and $c_{b'}$ meet only in $\{q\}$.

**Lemma 7.8.2 (Each place has a branch).** Let $I$ be radical at $q$, with $\dim \mathcal{O}_q = 1$. Let $c_1, \dots, c_m$ be curve branches of $I$ at $q$ that satisfy (Cover) and (Meet at $q$). Then for each maximal ideal $P$ of $\bar{\mathcal{O}}_q$ there is an index $b$ with $\operatorname{ord}_P(f) = \operatorname{ord}_{c_b}(f)$ for each polynomial $f$.

Lean: `GlobalTheory.CompanionTheory.BranchNorm.placeHasBranch`.

*Proof.* We take three facts as given. First, each maximal ideal $P$ gives a holomorphic disc $\nu$ in $Z(I)$ centred at $q$ with $\operatorname{ord}_P(f) = \operatorname{ord}_\nu(f)$ for all $f$. This uses a normal model of the component of $Z(I)$ on which $P$ lies, a disc at the point of the normal model over $P$, and the local injectivity of the projection to $Z(I)$. Second, if the punctured disc $\nu$ minus its centre lies in the union of the images of the $c_b$, then it lies in the image of one $c_b$. This is where (Meet at $q$) is used: the images minus $q$ are disjoint and open in $Z(I)$ minus $q$ near $q$, since the curve is regular off its centre, and the punctured disc is connected. Third, if the punctured disc $\nu$ lies in the image of $c_b$, then $\nu = c_b \circ h$ for a holomorphic $h$ with $h(0) = 0$ that is invertible near $0$, so the orders along $\nu$ and $c_b$ agree.

Let $P$ be given and take $\nu$ from the first fact. By (Cover), the disc $\nu$ near its centre lies in the union of the images. By the second fact it lies in the image of one $c_b$, and by the third fact $\operatorname{ord}_P(f) = \operatorname{ord}_\nu(f) = \operatorname{ord}_{c_b}(f)$ for each $f$. $\square$

**Theorem 7.8.3 (Branches and the normalization).** Let $I$ be radical at $q$, and let $c_1, \dots, c_m$ be curve branches of $I$ at $q$ with $m > 0$ that satisfy (Cover) and (Meet at $q$). Then:

1. $\dim \mathcal{O}_q = 1$;
2. if $f$ is a polynomial with $\operatorname{ord}_{c_b}(f) < \infty$ for each $b$, then the image of $f$ in $\mathcal{O}_q$ is a nonzerodivisor;
3. there is a bijection $b \mapsto P_b$ from $\{1, \dots, m\}$ to the maximal ideals of $\bar{\mathcal{O}}_q$ such that, for each $b$, the quotient $\bar{\mathcal{O}}_q / P_b$ has length $1$ over $\mathcal{O}_q$, and $\operatorname{ord}_{P_b}(f) = \operatorname{ord}_{c_b}(f)$ for each $f$.

Lean: `GlobalTheory.CompanionTheory.BranchNorm.branchNormalisation` (also `GlobalTheory.T.branch_normalisation_holds`, a second name).

*Proof.* We take as given the following facts. A germ of an analytic set at $q$ that is a finite union of discs through $q$ has dimension $1$, which gives the first claim since $m > 0$. Each branch $c_b$ lies in one irreducible component of $Z(I)$ and gives a maximal ideal $P_b$ of $\bar{\mathcal{O}}_q$, through the minimal prime of that component, with $\operatorname{ord}_{P_b} = \operatorname{ord}_{c_b}$. Two curve branches with the same order function for all polynomials have images that meet at points other than $q$. Two maximal ideals of $\bar{\mathcal{O}}_q$ with the same order function are equal. The residue field of $\bar{\mathcal{O}}_q$ at each maximal ideal is $\mathbb{C}$, so the quotient has length $1$.

For the second claim, let $f$ have finite order along each branch. If the image of $f$ were a zerodivisor, then $f$ would lie in a minimal prime of $\mathcal{O}_q$, since $\mathcal{O}_q$ is reduced, and so $\operatorname{ord}_P(f) = \infty$ for a maximal ideal $P$ over that prime. By the lemma, $\operatorname{ord}_{c_b}(f) = \infty$ for some $b$, against the assumption.

For the third claim, the map $b \mapsto P_b$ is defined above. It is injective: if $P_b = P_{b'}$ with $b \neq b'$, then $c_b$ and $c_{b'}$ have the same order function, so their images meet away from $q$, which (Meet at $q$) excludes. It is surjective: for a maximal ideal $P$, the lemma gives $b$ with $\operatorname{ord}_P = \operatorname{ord}_{c_b} = \operatorname{ord}_{P_b}$, so $P = P_b$. The length claim is the fact on residue fields. $\square$

**Theorem 7.8.4 (Multiplicity on a curve).** Let $I \subseteq \mathbb{C}[x_1, \dots, x_n]$ be radical at $q$, let $u \in \mathbb{C}^n$, and let $c_1, \dots, c_m$ be curve branches of $I$ at $q$ with orders $o_1, \dots, o_m \geq 0$. Assume (Cover), that for $b \neq b'$ the images of $c_b$ and $c_{b'}$ meet only in $\{\ell_u = 0\}$, and that $\ell_u \circ c_b$ vanishes to order $o_b$ on the disc of $c_b$ for each $b$. Then
$$\operatorname{mult}_{\mathfrak{m}_q}\big(I + (\ell_u)\big) = \sum_{b=1}^m o_b.$$

Lean: `GlobalTheory.CompanionTheory.Heights.CurveBranch.curveBranchLength` (also `GlobalTheory.T.curve_branch_length_holds`, a second name).

*Proof.* We take as given the classical formula for the length on a curve: if $I$ is radical at $q$, $\dim \mathcal{O}_q = 1$, and the image of $f$ in $\mathcal{O}_q$ is a nonzerodivisor, then, in $\mathbb{N} \cup \{\infty\}$,
$$\operatorname{mult}_{\mathfrak{m}_q}\big(I + (f)\big) = \sum_{P} \operatorname{ord}_P(f) \cdot \operatorname{length}\big(\bar{\mathcal{O}}_q / P\big),$$
where $P$ runs over the maximal ideals of $\bar{\mathcal{O}}_q$.

First let $\ell_u(q) \neq 0$ or $m = 0$. If $\ell_u(q) \neq 0$, then $\ell_u$ is a unit in $\mathbb{C}[x]_{\mathfrak{m}_q}$, so the left side is $0$. Also $\ell_u(c_b(0)) = \ell_u(q) \neq 0$, so each $o_b = 0$. If $m = 0$, the right side is $0$, and (Cover) shows that $q \notin Z(I)$, so $I \not\subseteq \mathfrak{m}_q$ and the left side is $0$.

Now let $\ell_u(q) = 0$ and $m > 0$. On the disc of $c_b$ we have $\ell_u(c_b(\tau)) = \tau^{o_b} H_b(\tau)$ with $H_b$ nowhere zero, so $\ell_u \circ c_b$ vanishes only at $\tau = 0$. Since $c_b$ is injective, $c_b(0) = q$ is the only point of the image of $c_b$ where $\ell_u = 0$. So the images of two different branches meet only in $\{q\}$, which is (Meet at $q$). Also $\operatorname{ord}_{c_b}(\ell_u) = o_b$ is finite for each $b$. The theorem on branches and the normalization now gives $\dim \mathcal{O}_q = 1$, that $\ell_u$ is a nonzerodivisor in $\mathcal{O}_q$, and the bijection $b \mapsto P_b$ with lengths $1$ and $\operatorname{ord}_{P_b}(\ell_u) = o_b$. The formula for the length gives
$$\operatorname{mult}_{\mathfrak{m}_q}\big(I + (\ell_u)\big) = \sum_{b=1}^m \operatorname{ord}_{P_b}(\ell_u) \cdot 1 = \sum_{b=1}^m o_b.$$
The right side is finite, so the convention for infinite lengths does not enter. $\square$

**Remark 7.8.5 (Formalization).** The lemma and the second theorem are in [BranchNormalisationHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/BranchNormalisationHolds.lean#L380), as applications of the proofs of named statements. The third theorem is in [CurveBranchLengthHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/CurveBranchLengthHolds.lean#L14), and its proof, with the two degenerate cases, is in [PCurveBranchLength.lean](lean:GroundTheory/HeightsAndTheta/Heights/ComplexAnalyticSets/PCurveBranchLength.lean#L21). The multiplicity is `localMult` in [Statements.lean](lean:GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/Statements.lean#L50); it converts the length with `toNat`, so an infinite length gives $0$. The third theorem has no hypothesis $m > 0$, and its hypothesis on the intersections of the images differs from that of the second theorem; the proof derives the second from the first. The formula for the length is `AutoClose.CurveNormalisationLength`. The two second names are wrappers that close with `first | exact ...`.
