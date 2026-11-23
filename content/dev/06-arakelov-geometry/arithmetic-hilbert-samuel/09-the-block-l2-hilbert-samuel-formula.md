---
title: The L2 Hilbert-Samuel formula in coordinates
decls:
  - GroundTheory.Heights₂.Heights.HilbertSamuel.ModulePieceHilbert.proof
  - GroundTheory.Heights₂.Heights.HilbertSamuel.ResChiBounds.proof
  - GroundTheory.Heights₂.Heights.HilbertSamuel.ResChiBounds.full
  - GroundTheory.Heights₂.Heights.HilbertSamuel.ProjectionBounds.full
  - GroundTheory.Heights₂.Heights.HilbertSamuel.TheoremHSMBlock.of_open
  - PositivityTheory.LocalParametersCuspidal.MB.HSM.theoremHSMBlock
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The L2 Hilbert-Samuel formula in coordinates

This section and the next give a second proof of the lower bound of Moriwaki for the arithmetic volume. It does not go through the schemes and the principalisation of the previous sections. An arithmetic variety is given by the coordinates of a generic point, sections are polynomials, and metrics are functions on the cone. In this setting we prove the $L^2$ form of the arithmetic Hilbert-Samuel formula of Gillet and Soulé: the logarithm of the covolume of the lattice of sections of degree $n$, for the $L^2$ norm, is $\bar A^{D+1} n^{D+1}/(D+1)! + o(n^{D+1})$. We also prove that the sup norm and the $L^2$ norm differ by at most a factor $C n^{D/2}$. The [Moriwaki bigness](/entry/hs-chain/) of the next section uses both.

### The data

Let $D \ge 1$, let $\Omega$ be a field of characteristic zero, and let $\kappa$ be a finite index set. Write $\mathbb{Z}[x_i]$ for the polynomial ring in variables $x_i$, $i \in \kappa$.

**Definition 6.9.1 (Datum).** A datum of dimension $D$ consists of the following.
1. A point $x = (x_i)$ with coordinates in $\Omega$, linearly independent over $\mathbb{Z}$. Its ideal $P$ is the kernel of evaluation at $x$, and $X = \operatorname{Proj} \mathbb{Z}[x_i]/P$ must be an arithmetic variety of dimension $D + 1$.
2. A smooth cone metric $h$ on $\mathbb{C}^\kappa \setminus 0$, with $h(cz) = |c| h(z)$, invariant under complex conjugation. For a form $f$ of degree $n$ we write $\|f\|(z) = |f(z)| / h(z)^n$.
3. A resolution $\rho : \tilde X \to X(\mathbb{C})$ of the complex points, and a smooth positive volume $dV$ on $\tilde X$.
4. An ideal $P_0 \subseteq P$ with respect to which the metric is semipositive.

The sections of degree $n$ are the lattice $H_n$ of values $f(x)$ of forms $f$ of degree $n$ with integer coefficients. The $L^2$ Gram matrix of a basis $b_1, \dots, b_r$ of $H_n$ is
$$G_n(k, l) = \tfrac12 \operatorname{Re}\left( \int_{\tilde X} \langle b_k, b_l \rangle(\rho y) \, dV + \int_{\tilde X} \langle b_k, b_l \rangle(\overline{\rho y}) \, dV \right),$$
and $\chi(n) = -\tfrac12 \log \det G_n$. This is the logarithm of the covolume of $H_n$ for the $L^2$ norm, and it does not depend on the basis.

For projective space $\mathbb{P}^D$ with the Fubini-Study metric and the Gauss measure, the monomials are orthogonal, and we write $\chi_{\mathbb{P}}(n) = -\tfrac12 \sum_{|a| = n} \log \|x^a\|^2_{L^2}$ for its value.

**Definition 6.9.2 (Projection frame).** A projection frame for $x$ is an injective map $e : \{0, \dots, D\} \to \kappa$ such that $x_{e(0)}, \dots, x_{e(D)}$ are algebraically independent and every $x_i$ is integral over $\mathbb{Z}[x_{e(0)}, \dots, x_{e(D)}]$. Its degree $\delta_e$ is the degree of the field extension $\mathbb{Q}(x) / \mathbb{Q}(x \circ e)$.

A block datum is the same structure for coordinates $y_{k,i}$ in blocks $k \in K$, with multihomogeneous forms, a distinguished block $k_0$ and a hermitian line $\bar A$ of degree one in the block $k_0$; the point must be birational to its projection to $k_0$. Its characteristic $\chi(n)$ and its $L^2$ norm are defined in the same way, from forms of multidegree $n$ in the block $k_0$.

A projection frame is a finite projection $X \to \mathbb{P}^D_{\mathbb{Z}}$, in the sense of Noether normalisation. The degree $\delta_e$ is the degree of the projection. A frame is compatible with the metric if the pull back of the Fubini-Study metric along it is controlled by $h$; this is a condition of the development.

### The finite part

The first piece is a count of finite modules. For multihomogeneous ideals $J_2 \subseteq J_1$ of a multigraded polynomial ring and a multidegree $a$, let $[J_1 : J_2]_a$ be the number of elements of $(J_1/J_2)_a$.

**Proposition 6.9.3 (Hilbert function of a finite piece).** Let $J_2 \subseteq J_1$ be multihomogeneous ideals of the multigraded ring $\mathbb{Z}[x_{k,i}]$, with blocks indexed by a finite set $K$. Assume $N J_1 \subseteq J_2$ for an integer $N > 0$, and that every relevant prime $W \supseteq J_2$ has $\dim \mathbb{Z}[x_{k,i}]/W \le d + |K|$. Let $s$ be a multidegree. Then there are $a_0$ and $C$ such that for all $a$ with $a_k \ge a_0$ for all $k$,
$$\left| \log [J_1 : J_2]_{a + s} - \frac{1}{d!} \sum_{W} \big(\operatorname{mult}_W J_2 - \operatorname{mult}_W J_1\big) \log p_W \, \deg_a(W) \right| \le C (|a| + 1)^{d - 1},$$
where $W$ runs over the primes of dimension $d + |K|$ that contain $J_2$, $p_W$ is the characteristic of $\mathbb{Z}[x_{k,i}]/W$, and $\deg_a(W)$ is the degree of $V(W)$ for $d$ copies of the line bundle $\mathcal{O}(a)$.

Lean: `GroundTheory.Heights₂.Heights.HilbertSamuel.ModulePieceHilbert.proof`.

*Proof.* If $W$ is horizontal, the integer $N$ is a unit at $W$, and $N J_1 \subseteq J_2$ gives equal multiplicities of $J_1$ and $J_2$ at $W$, so $W$ adds nothing to the sum. So only vertical $W$ count, and for them $p_W \ne 0$. Choose a filtration of $J_1 / J_2$ by multihomogeneous submodules whose quotients are shifted copies of $\mathbb{Z}[x_{k,i}]/q$ for primes $q$. The count of $J_1/J_2$ in degree $a + s$ is the product of the counts of the quotients, so its logarithm is the sum of their logarithms.

For one quotient $\mathbb{Z}[x_{k,i}]/q$ shifted by $b$, the prime $q$ contains $p = p_q$, so the quotient is a vector space over $\mathbb{F}_p$, and its count in degree $a + s - b$ is $p$ raised to the Hilbert function of $V(q)$ in that degree. If $q$ has dimension $d + |K|$, the multigraded Hilbert-Samuel formula gives $\deg_a(q)/d!$ up to $O(|a|^{d-1})$; the shift by $s - b$ changes $\deg_a$ by $O(|a|^{d-1})$, since $\deg$ is a form of degree $d$ in $a$. If $q$ has smaller dimension, the count is $O(|a|^{d-1})$. This is the factor estimate of the development. Each prime $W$ of dimension $d + |K|$ occurs in the filtration $\operatorname{mult}_W J_2 - \operatorname{mult}_W J_1$ times, by additivity of length at $W$. Summing gives the formula. $\square$

The proposition controls the change of $\chi$ when the lattice $H_n$ is replaced by a sublattice of finite index, which happens when we change the model.

### The sandwich

**Theorem 6.9.4 (Sandwich for the $L^2$ characteristic).** Assume that sup norms on the resolution are bounded by $L^2$ norms: for every datum there is $C$ with $\|f\|(z) \le C n^{D/2} \|f\|_{L^2}$ for all forms $f$ of degree $n \ge 1$ and all complex points $z$ of $X$. Let $e$ be a projection frame compatible with the metric. Then there are $k$ and $C$ such that for $n \ge k + 1$
$$\delta_e \chi_{\mathbb{P}}(n - k) - C n^D \log(n+1) \le \chi(n) \le \delta_e \chi_{\mathbb{P}}(n + k) + C n^D \log(n+1).$$

Lean: `GroundTheory.Heights₂.Heights.HilbertSamuel.ResChiBounds.proof`.

*Proof.* By results of the development, the entries of the Gram matrix are integrable and the Gram matrix of a basis is positive definite. The development also proves an upper and a lower sandwich. In outline, the projection identifies $H_n$ with a module of rank $\delta_e$ over the sections of degree about $n$ on $\mathbb{P}^D$, up to a shift of the degree by a fixed $k$. The upper sandwich compares the $L^2$ norm on $X$ with the sup norm and then with the Fubini-Study norm on $\mathbb{P}^D$, and it uses the hypothesis. The lower sandwich uses that the complement of the complex points has measure zero. Each gives a constant $k_i$ and $C_i$.

The function $\chi_{\mathbb{P}}$ is monotone, since $\chi_{\mathbb{P}}(n+1) - \chi_{\mathbb{P}}(n) \ge 0$. So replacing $k_1$ and $k_2$ by $k = \max(k_1, k_2)$ makes the lower bound smaller and the upper bound larger, since $\delta_e \ge 0$. Replacing $C_i$ by $\max(C_1, C_2)$ does the same, since $n^D \log(n+1) \ge 0$. $\square$

**Corollary 6.9.5 (Sandwich for the $L^2$ characteristic, unconditional).** The bounds of the theorem hold for every datum and every compatible projection frame.

Lean: `GroundTheory.Heights₂.Heights.HilbertSamuel.ResChiBounds.full`.

*Proof.* The bound of sup norms by $L^2$ norms on a resolution holds, by a result of the development; it is the inequality of Gromov for a smooth volume. Apply [the theorem](/entry/res-chi-bounds-proof/). $\square$

**Theorem 6.9.6 (Projection bounds).** Let $e$ be a projection frame for a datum, compatible with the metric. Then there are $k$, forms $E_1, \dots, E_{\delta_e}$ of degree $k$ with integer coefficients and a constant $C$ with these properties.
1. The values $E_l(x)$ are linearly independent over $\mathbb{Q}(x \circ e)$.
2. For $s \in H_n$, the trace of $s E_l(x)$ from $\mathbb{Q}(x)$ to $\mathbb{Q}(x \circ e)$ is a section of degree $n + k$ on $\mathbb{P}^D$, and these traces vanish for all $l$ only if $s = 0$.
3. $\big|\operatorname{rank} H_n - \delta_e n^D / D!\big| \le C (n+1)^{D-1}$.
4. Sup norms on $X$ and Fubini-Study sup norms of traces on $\mathbb{P}^D$ agree up to the factor $C$, in both directions.
5. The sandwich of the corollary holds with this $k$ and $C$.

Lean: `GroundTheory.Heights₂.Heights.HilbertSamuel.ProjectionBounds.full`.

*Proof.* Take $k_\chi$ and $C_\chi$ from [the unconditional sandwich](/entry/res-chi-bounds-full/). Since $x$ is integral over $\mathbb{Z}[x \circ e]$ and the extension of function fields has degree $\delta_e$, there are $\delta_e$ sections $\varepsilon_l$ of a common degree $k_0$ that form a basis of $\mathbb{Q}(x)$ over $\mathbb{Q}(x \circ e)$; lift them to forms $H_l$ of degree $k_0$. Put $E_l = x_{e(0)}^{k_\chi} H_l$, of degree $k = k_\chi + k_0$. Since $x_{e(0)} \ne 0$, multiplication by its power is injective, so the $E_l(x)$ stay linearly independent.

In outline, the trace of an element integral over the integrally closed ring $\mathbb{Z}[x \circ e]$ lies in that ring, which gives the first half of 2, and the trace form of the separable extension is nondegenerate, which gives the second half. The rank bound 3 is the Hilbert polynomial of $X_{\mathbb{Q}}$, of degree $\delta_e$. The norm comparisons 4 follow from the bound $|E_l(z)| \le S \, p(z)^k$ by the projected norm $p(z)$ and from the compatibility of the frame. We take the details of 2, 3 and 4 from the development. Property 5 holds with the larger $k$ and $C$, by the monotonicity used before. $\square$

### The formula

**Theorem 6.9.7 (Block Hilbert-Samuel formula from nineteen statements).** Assume nineteen statements of the development on finite pieces, change of model, projection frames, resolutions and Veronese embeddings, among them [the Hilbert function of a finite piece](/entry/module-piece-hilbert-proof/). Let $\bar A$ be a semipositive cone metric on a block datum of dimension $D$, and let $\bar A^{D+1}$ be its self intersection for an intersection system $I$. Then
$$\chi(n) = \frac{\bar A^{D+1}}{(D+1)!} \, n^{D+1} + o(n^{D+1}),$$
and there is $C$ with $\|f\|(z) \le C n^{D/2} \|f\|_{L^2}$ for every form $f$ of degree $n \ge 1$ and every complex point $z$.

Lean: `GroundTheory.Heights₂.Heights.HilbertSamuel.TheoremHSMBlock.of_open`.

*Proof.* There are three steps.

Reduction to projective space. Let $g$ be the generic degree of $X$. The development shows that
$$\Big(\chi(n) - \frac{\bar A^{D+1}}{(D+1)!} n^{D+1}\Big) - g \Big(\chi_{\mathbb{P}}(n) - \frac{h_{\mathbb{P}}}{(D+1)!} n^{D+1}\Big) = o(n^{D+1}),$$
where $h_{\mathbb{P}}$ is the height of $\mathbb{P}^D$ for the Fubini-Study metric. Choose a compatible projection frame. By [the projection bounds](/entry/projection-bounds-full/) the defect of $\chi$ is $\delta_e$ times the defect of $\chi_{\mathbb{P}}$, up to $O(n^D \log n)$. Then change the model and the metric, which changes $\chi$ by a finite index, controlled by the Hilbert function of finite pieces, and by an integral that the calculus of the intersection system computes. The degree $\delta_e$ equals the generic degree $g$.

Projective space. The defect $\chi_{\mathbb{P}}(n) - h_{\mathbb{P}} n^{D+1}/(D+1)!$ is $o(n^{D+1})$. The development proves this by the same reduction applied to the second Veronese embedding of $\mathbb{P}^D$, for which both sides can be computed from the monomials.

Conclusion. Multiply the projective estimate by $g$ and add it to the reduction. This gives the formula. The sup bound is a separate result of the development for block data. $\square$

**Theorem 6.9.8 (Block Hilbert-Samuel formula).** Assume that arithmetic intersection systems exist and that complex points have resolutions. Then the conclusion of the previous theorem holds for every block datum and every intersection system.

Lean: `PositivityTheory.LocalParametersCuspidal.MB.HSM.theoremHSMBlock`.

*Proof.* We prove the nineteen statements and apply [the previous theorem](/entry/theorem-hsmblock-of-open/). The statements on finite pieces, [the Hilbert function](/entry/module-piece-hilbert-proof/) among them, have proofs in the development. The existence of intersection systems gives the pushforward formula, the degree of a system and the generic degree. The resolution statement gives the existence of resolutions of complex points and the integrability of their sections. From these, results of the development give the change of model, the transport along matrices, the graph degrees for projection frames, blocks and Veronese embeddings, and the remaining resolution statements. $\square$

**Remark 6.9.9 (Formalization).** The finite piece proposition uses multiplicities in $\mathbb{N} \cup \{\infty\}$ cast to the reals, so an infinite multiplicity counts as $0$, and its error term is written as $C(|a|+1)^d/(|a|+1)$ ([StatementsModulePieceHilbert.lean](lean:GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/StatementsModulePieceHilbert.lean#L13)). The value $\chi(n)$ is defined with a chosen basis, and it is set to $0$ when there is no basis. The proof term of the nineteen statement theorem writes out the reduction to projective space, with the projection bounds, twice: once for the block datum and once inside the proof for projective space ([AssemblyConditional.lean](lean:GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/AssemblyConditional.lean#L147) and line 174); the hypothesis on change of model for graphs is used twice, for the block image and for the Veronese embedding. The sup bound for block data enters with no hypothesis. The field of a datum that says $P_0 \subseteq P$ has a name about normal forms and dual spans. The final theorem sits in a namespace about cuspidal local parameters, which is not related to its content ([HSMBlock.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelBlock/HSMBlock.lean#L37)). The sandwich lemmas, the sup bound, the reduction and most of the nineteen statements are cited results whose proofs we did not open.
