---
title: Reference geometries, Hodge ties and flag degrees
decls:
  - AnalyticReference.reference_geometry_holomorphic_inverse
  - PositivityTheory.UnitarySelfGeneration.pair_iso
  - GlobalTheory.CompanionTheory.Ar.PairIsoK.pair_iso
  - GlobalTheory.CompanionTheory.Ar.IndefiniteRowSideFullHecke.degFlPoly_eval'
  - GlobalTheory.CompanionTheory.Ar.IndefiniteRowSideFullHecke.FlDegC.tower
  - FlatDegreeResidue.flatDegreeSt_of_resK
  - ChowFormHeightComparison₂.CF.stVert
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reference geometries, Hodge ties and flag degrees

This section proves five results that other chapters use as black boxes. The first gives a holomorphic inverse for the projection of a reference geometry. The second compares two Hodge ties that differ by an automorphism of the host. The third computes the degree polynomial of a flag variety, with an induction over chains of blocks. The fourth gives the degree of the flat lines on a moduli space. The fifth computes the top self intersection of a line on a vertical fibre as a Chow degree; it feeds [the covolume bound on the boundary](/entry/top-covol-slim2-use-alt-alt/).

### A holomorphic inverse for reference geometries

A reference geometry on a model $Y$ of a moduli space is a Hodge compactification $\mathfrak{M}$ over an arithmetic variety $y$, with a flag of Hodge lines $h(\tau, i)$ for $\tau$ in the CM type and $i < p + q$, a degree map and an exponent. Its projection $\pi$ sends a point of the compactification to the point of $y$ given by the coordinates of the flag. An analytic structure on a reference geometry is a complex manifold structure on the interior with charts in which the Hodge lines have tame log norms.

**Theorem 10.19.1 (Holomorphic inverse for reference geometries).** Assume the given facts of the chapter, the existence of a generator of the flat line and of its components, that the model is global and that its components split, and let $p, q \geq 1$. Then every reference geometry $G$ has an analytic structure $A$ and a holomorphic map $\operatorname{inv}$ with $\operatorname{inv}(\pi(x)) = x$ for every interior point $x$.

Lean: `AnalyticReference.reference_geometry_holomorphic_inverse`.

*Proof.* Step 1: the flag. The Hodge flag of the compactification gives, for each $\tau$ and $i$, a singular part, a degree, a Hodge identity and a conjugation identity.

Step 2: the central chart. Let $\chi$ be a chart with simple normal crossings at the boundary, with $a = 0$, so that the chart has no punctured coordinates. By the flat line generator and its components, there are an analytic function $F$ with $F(0) \neq 0$ and a constant $d$ with
$$
\sum_i \log h(\tau, i) = \log \lvert F\rvert + d
$$
on the chart. So the full sum is plurisubharmonic near $0$.

Step 3: the partial sums. On every chart with simple normal crossings the partial sums
$$
-\sum_{k \leq i} \log h(\tau, k)
$$
are tame. If $a = 0$ they are plurisubharmonic near $0$. This follows from Step 2 by telescoping: the partial sums of the Hodge lines differ by the logs of the lines of the flag quotients.

Step 4: the structure. The construction of an analytic structure from local bounds takes the bounds of Step 3 on every chart and gives $A$ and the inverse map. $\square$

### Comparing two Hodge ties

A Hodge tie for a model $Y$ is a Hodge compactification together with singular lines $\operatorname{sing}(r)$, indexed by $r = (\tau, i)$, that carry the Hodge metrics. Let $g$ be an automorphism of the host field and let $\Phi$ be an automorphism of the moduli space that is compatible with the twist by $g$. Then $g$ induces a permutation $\pi$ of the CM type.

**Theorem 10.19.2 (Two Hodge ties are isometric).** Assume the compatibility of Hodge comparisons and the uniform theta bound for abelian varieties. Let $T$ and $T'$ be Hodge ties whose images are compact and which have the same set of rules on a set $S$, with $T'$ the image of $T$ under $(g, \Phi)$. Then there is an arithmetic variety $y$ of dimension $\dim \mathrm{Fl} + 1$, block maps $v$ and $v'$ from the bases of $T$ and $T'$ to $y$, and a form $b$ that does not vanish on $y$, such that the following hold.

1. Both covers have positive degree, and $\deg(v) \deg \mathrm{Fl} = \deg(v') \deg \mathrm{Fl}'$.
2. For each $r = (\tau, i)$ the pullbacks of $\operatorname{sing}_T(r)$ and of $\operatorname{sing}_{T'}(\pi\tau, i)$ are isometric off the zeros of $b$.

Lean: `GlobalTheory.CompanionTheory.Ar.PairIsoK.pair_iso` (also `PositivityTheory.UnitarySelfGeneration.pair_iso`, a second name).

*Proof.* Step 1: the permutation. The automorphism $g$ acts on the CM type of the host. This action is $\pi$, since both send $\tau$ to the embedding $\tau \circ g$.

Step 2: the twist. The comparison of twisted Hodge compactifications gives a map $\theta$ between the index groups of the two flags, a field isomorphism $\psi$ between the two base fields, and the identity of the flag spaces after $\theta$ and $\pi$.

Step 3: a common field. Both flags are generic. The flag of $T'$, moved by $\theta$ and $\pi$, is generic on the same space as the flag of $T$. The lemma on generic flags gives a field $\Omega_3$ with embeddings of the two base fields and positive degrees $n_1, n_2$ with $n_1 \deg \mathrm{Fl} = n_2 \deg \mathrm{Fl}'$. The field $\Omega_3$ is finite over both images.

Step 4: the variety. The flag of $\Omega_3$ gives the arithmetic variety $y$ and the block maps $v$ and $v'$. An interior point of the compactification shows that $y$ has the right dimension, and a multihomogeneous form of the compactification gives $b$.

Step 5: the isometry. The comparison of Hodge compactifications with an isomorphism of flags gives the isometry of the singular lines at every point off the zeros of $b$. The compatibility hypothesis is used here. $\square$

### The degree of a flag variety

Let $\Psi$ be a CM type and $N \geq 2$. The flag variety $\mathrm{Fl}$ has a block for each pair $(\tau, i)$ with $i < N$, and its dimension is $\delta = \lvert\Psi\rvert\binom N2$. For a word $w$ of length $\delta$ in the pairs, let $a(w)$ be the archimedean integral of the product of the potentials of the coordinate lines $x_{w(1)}, \dots, x_{w(\delta)}$ over the complex points of $\mathrm{Fl}$. The degree polynomial $D_{\mathrm{Fl}}$ is the polynomial in the variables $x_{\tau,i}$ whose coefficients are built from the values $a(w)$. For a weight $\lambda$ the flag degree is
$$
\deg_{\mathrm{Fl}}(\lambda) = \delta! \prod_{\tau \in \Psi} \prod_{i < k} \frac{\lambda_{\tau,i} - \lambda_{\tau,k}}{k - i} .
$$

A chain of blocks is an injective map $j$ from a finite set $K$ to the blocks such that the blocks below a block of the chain are also in the chain. Each chain $j$ gives a partial flag variety $P_j$ and unit lines on it.

**Lemma 10.19.3 (Tower of a chain).** Assume the inputs and let $I$ be a full system of intersection numbers. Let $j : K \to \mathrm{Fl}$ be a chain with $\lvert K\rvert = n + 1$. Then there is a word $w$ in $K$ in which each $k$ occurs $N - 1 - j(k)_2$ times, such that the archimedean integral over $P_j$ of the potentials of the unit lines along $w$ is $1$.

Lean: `GlobalTheory.CompanionTheory.Ar.IndefiniteRowSideFullHecke.FlDegC.tower`.

*Proof.* Induction on $n$. If $n = 0$, then $K$ has one element $k_0$, and the chain condition forces $j(k_0)_2 = 0$. Take the word of length $N - 1$ with all letters $k_0$. The base lemma gives the value $1$.

For the step, choose $k_0$ with $j(k_0)_2$ maximal. Removing $k_0$ gives a chain on $K \setminus \{k_0\}$ with $n + 1$ elements. The induction hypothesis gives a word $w_0$ for it. Append $N - 1 - j(k_0)_2$ copies of $k_0$. The count is right for $k_0$, since $w_0$ does not contain $k_0$, and for every other $k$, since the appended letters are all $k_0$. The step lemma says that appending these letters does not change the integral, so it stays $1$. $\square$

**Theorem 10.19.4 (Evaluation of the degree polynomial).** Assume the inputs and let $I$ be a full system of intersection numbers. Let $\Psi$ be nonempty and $N \geq 2$. Then for every weight $\lambda$,
$$
D_{\mathrm{Fl}}(\lambda) = \deg_{\mathrm{Fl}}(\lambda) .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.IndefiniteRowSideFullHecke.degFlPoly_eval'`.

*Proof.* Step 1: the shape. By the Vandermonde lemma there is a constant $c$ with $D_{\mathrm{Fl}} = c \, \Delta$, where $\Delta$ is the product of the differences $x_{\tau,i} - x_{\tau,k}$ for $i < k$. The lemma uses the antisymmetry of the degree polynomial of a uniformized flag variety.

Step 2: one coefficient. Apply the tower lemma to the chain of all blocks. It gives a word $w$ in which the pair $(\tau, i)$ occurs $N - 1 - i$ times, with value $a(w) = 1$. The length of $w$ is the sum of these counts, which is $\delta$, by the dimension of the flag variety. The coefficient of $\Delta$ at the monomial of $w$ is the product of the gaps $k - i$. So
$$
c \prod_{\tau} \prod_{i < k} (k - i) = \delta! .
$$

Step 3: evaluate. Put $\lambda$ into $c \Delta$ and split the product. The Weyl formula for the flag degree gives the claim. $\square$

### The flat degree

Let $E$ be a CM field with a host $H$ of level $d$ and a Kronecker character $\chi$. Let $X$ be a moduli space with a uniformization that satisfies the laws: the level is $1$, the levels are good at all primes, the uniformizations are unramified, the function field is algebraically closed in the right sense, the characters and determinants are trivial on the groups, and the cusp sections span.

**Theorem 10.19.5 (Flat degree).** Assume resolution of singularities in the Hironaka form. Then for every component $Z$ and every $\tau$ in the CM type, flat sections of the flat line exist, and every flat section has degree
$$
\deg s = \frac{p - q}{2} \log \Omega_\chi + q (\log d - \log \operatorname{rd}_E) ,
$$
where $\Omega_\chi$ is the period of $\chi$ and $\operatorname{rd}_E$ is the root discriminant of $E$.

Lean: `FlatDegreeResidue.flatDegreeSt_of_resK`.

*Proof.* The GAGA statement for sections is proved. With resolution it gives a section $s$ of the flat line that is constant at every finite place, with a known degree. Shift $s$ by the defect at each place, which is $q$ times the order of the conjugate different minus the valuation of $d$. The defect is finite, and its sum gives the second term. All flat sections have the same degree, by the laws, so the degree of the shifted section is the degree of every flat section. $\square$

### Top self intersections on vertical fibres

Let $K$ be a number field and $Z$ an integral scheme, projective over $\mathcal{O}_K$, with a line bundle $B$ and sections $s_1, \dots, s_m$ that embed $Z$ in $\mathbb{P}^{m-1}$. For a point $z$ of $Z$ let $P(z)$ be its ideal in $\mathcal{O}_K[x_1, \dots, x_m]$.

**Theorem 10.19.6 (Top self intersection of a vertical fibre).** Assume the statements on the points of an embedding, on pullbacks along closed immersions, and on divisors of sections. Let $v$ be a finite place of $K$, assume that the ideal of the generic point of $Z$ meets $\mathcal{O}_K$ in $v$, and let $Z$ have dimension $d$. Then $Z$ is a scheme over the residue field $\kappa(v)$, and
$$
(B^d)_{\kappa(v)} = \deg_{\mathrm{Ch}}\bigl(P(\eta) \bmod v, \, d + 1\bigr) ,
$$
where $\eta$ is the generic point and $\deg_{\mathrm{Ch}}$ is the Chow degree.

Lean: `ChowFormHeightComparison₂.CF.stVert`.

*Proof.* Step 1: the residue field. An element $r$ of $\mathcal{O}_K$ is $0$ on $Z$ if and only if $r \in v$, since the ideal of $\eta$ meets $\mathcal{O}_K$ in $v$. So the structure map factors through $\kappa(v)$, and $Z$ is projective over $\kappa(v)$ with the same embedding.

Step 2: the reduction. The ideal of $\eta$ over $\kappa(v)$ is the reduction mod $v$ of $P(\eta)$, since $\mathcal{O}_K \to \kappa(v)$ is onto.

Step 3: the dimension. The Krull dimension of the quotient of $\kappa(v)[x_1, \dots, x_m]$ by this ideal is at most $m$ and at least $d + 1$. So it is a finite number $n$ with $d + 1 \leq n$.

Step 4: the field case. The theorem over a field, together with the Chow degree of a section, gives that $Z$ has dimension $n - 1$ and that its top self intersection is the Chow degree in dimension $n$. So $n - 1 = d$, and the claim follows. $\square$

**Remark 10.19.7 (Formalization).** The holomorphic inverse is at `Development/WeilBound/CoreStatements/CentralCharts/ReferenceGeometryHolomorphicInverse.lean:155`; the central chart is at line 37, the local bounds at line 72 and the telescoping lemmas at lines 14 and 24. It extracts the inputs from the given facts by position, `hG.2.2.2.2.2.2.2.2.2.1` (line 161). The comparison of ties is at `Development/WeilBound/CoreStatements/HomogeneousNonvanishing/PairIso.lean:232`, and the second name at line 411 is a bare relay to it. The tower lemma and the evaluation are at `Development/WeilBound/CoreStatements/IntegralPointHeights/NegativeIntegralPoints/FlDegFree.lean:328` and `:441`; the Vandermonde lemma is `degFl_vand` (line 400), and the base and step lemmas are at lines 58 and 240. The degree polynomial is `PB.degFlPoly` (`AgreementIffGuarded.lean:21`), the flag degree is `flagDeg` (`CompactGapsGE.lean:28`), and the Weyl formula is `flagDeg_eq_weyl` (`FlagDegreeWeightFormula.lean:9`). The flat degree is a relay at `Development/WeilBound/CoreStatements/ComplexPeriods/FlatDegreeResidues/FlatSlim.lean:5` to `flatDegreeSt_of_resK_gaga` (`FlatDegreeStOfResKGaga.lean:18`) with the proved `gagaSections`; the degree value is `flatDegVal` (`ExistsFlatSecRankZero.lean:751`). The vertical theorem is at `Development/WeilBound/CoreStatements/MinimalPrimeDimensions/ChowDegreeSection.lean:146`, and its statement `StVert` is at `GenIdeal.lean:77`. Its Step 3 is a case split on the values $\bot$, $\top$ and finite in `WithBot ℕ∞` (lines 184 to 197).
