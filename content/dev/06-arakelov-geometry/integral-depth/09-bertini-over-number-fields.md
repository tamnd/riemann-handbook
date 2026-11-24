---
title: Bertini over number fields
decls:
  - GlobalTheory.BertiniTop.bertini
  - GlobalTheory.T.bertini_simple_zeros_generic_sections
  - GlobalTheory.HSShort.bertiniNumberField_of_hilbertSamuel
  - GlobalTheory.T.bertiniNumberField_of_hilbertSamuel₂
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bertini over number fields

The determinant method of the next three sections cuts the image of a projective variety by $D$ general hyperplanes, where $D$ is the dimension of the image. It needs the cut to be a set of exactly $\delta$ distinct points, where $\delta$ is the degree, and it needs the Chow form of the image to factor at the cut into the linear forms of these points. This section proves that both hold off a hypersurface in the space of linear sections. The result is a form of the Bertini theorem. The explicit Hilbert-Samuel bound of [the last of these sections](/entry/geo-bound-of-abstract/) uses it in the form over number fields, and [the Hilbert-Samuel bound on a component](/entry/arithmetic-hilbert-samuel-bound/) of the previous section quotes that form.

We use the notation of the previous section. In particular $\mathsf{Q}$ is the conjunction of the quoted theorems.

**Definition 3.9.1 (Tuple and its image).** Let $F$ be a number field. A *tuple* $T$ over $F$ is a projective scheme over $F$ with a line bundle and $N$ global sections $r_1, \dots, r_N$ of it. The sections define a rational map to $\mathbb{P}^{N-1}_F$. The *image ideal* $I_T \subset F[x_1, \dots, x_N]$ is the ideal of forms that vanish on the image, and $D$ is the dimension of the image. The integer $\mathrm{del}(T)$ is the self-intersection number of the line bundle. The tuple is *birational* if the map onto its image is birational, and *geometric* if the scheme is a variety and the sections have no common zero, with further conditions that we do not unfold.

**Definition 3.9.2 (Chow form).** A *Chow form* of degree $\delta$ of $I_T$ is a polynomial $f$ in $D + 1$ groups of $N$ variables $u_{i j}$ ($0 \le i \le D$, $1 \le j \le N$) with coefficients in $F$. It is homogeneous of degree $\delta$ in each group, and it vanishes at $(u_{i j})$ exactly when the $D + 1$ hyperplanes $\sum_j u_{i j} x_j = 0$ have a common zero on the image ([heights](/learn/arakelov/#heights)). We do not unfold the precise definition.

For a field $E \supset F$ and a matrix $s = (s_{i j}) \in E^{D \times N}$, the *linear section* at $s$ is the set of the $D$ hyperplanes $\sum_j s_{i j} x_j = 0$, $1 \le i \le D$. For a point $y \in \bar E^N$ let $\ell_y$ be the linear form $\sum_j y_j u_j$ in one group of variables. The specialization of $f$ at $s$ is the polynomial in the last group $u_0$ that we get when we put $u_i = s_i$ for $1 \le i \le D$; write $f(s)$ for it.

**Definition 3.9.3 (Simple section).** Let $T$ be a tuple over $F$, $\delta \in \mathbb{N}$, $f$ a polynomial as above and $s \in E^{D \times N}$ for a field $E \supset F$. The section $s$ is *simple* for $(T, \delta, f)$ if:

1. $s$ is a good section of $T$ (a condition on the cut that we do not unfold);
2. the set $P_s$ of geometric points of the image cut out by the linear section at $s$ has exactly $\delta$ elements;
3. the base change of the linear system to $E$ is injective on $P_s$;
4. there is a $c \in \bar E$ with $c \ne 0$ and
$$f(s) = c \prod_{x \in P_s} \ell_{y(x)},$$
where $y(x) \in \bar E^N$ are the coordinates of $x$.

The last condition says that the Chow form at $s$ splits into the linear forms of the $\delta$ points. It is the classical description of the Chow form of a zero-dimensional cycle as the product of the linear forms of its points.

**Definition 3.9.4 (Bertini statement).** The *Bertini statement* says: for every number field $F$, every geometric birational tuple $T$ over $F$, every $\delta \in \mathbb{N}$ and every Chow form $f$ of degree $\delta$ of $I_T$, we have $\delta = \mathrm{del}(T)$, and there is a polynomial $Q \ne 0$ in $D N$ variables over $F$ such that, for every field $E \supset F$ and every $s \in E^{D \times N}$ with $Q(s) \ne 0$, the section $s$ is simple for $(T, \delta, f)$. The *Bertini statement over number fields* is the same statement with $E$ restricted to number fields that contain $F$.

**Theorem 3.9.5 (Bertini theorem for good linear sections).** If the quoted theorems hold, then the Bertini statement holds.

Lean: `GlobalTheory.BertiniTop.bertini` (also `GlobalTheory.T.bertini_simple_zeros_generic_sections`, a second name).

*Proof.* Fix $F$, $T$, $\delta$ and $f$.

*The degree.* An input lemma, proved from $\mathsf{Q}$, says that for a birational tuple of a variety whose sections have no common zero, $\mathrm{del}(T)$ equals the degree of the image in the sense of Hilbert polynomials. The image of a variety is irreducible, so $I_T$ is a prime ideal. It is homogeneous, since the image is a projective variety. The degree of a Chow form of a prime homogeneous ideal is the Hilbert degree. So $\delta = \mathrm{del}(T)$.

*The bad locus.* We construct $Q$ as a product $Q_1 Q_2$.

1. There is a form $g_1 \notin I_T$ that vanishes on the part of the image where the map is not an isomorphism (the boundary of the open set over which the tuple is birational onto its image).
2. There is a form $g_2 \notin I_T$ off whose zero set the fibres of the linear system are finite.
3. An elimination lemma for general linear forms on the cone over the image gives a polynomial $Q_1 \ne 0$ in the entries of $s$ such that $Q_1(s) \ne 0$ implies that the linear section at $s$ meets the image in a finite set that avoids the zeros of $g_1 g_2$. This is the classical fact that $D$ general hyperplanes cut a $D$-dimensional variety in finitely many points and miss a given proper closed subset.
4. A lemma on pencils gives a polynomial $Q_2 \ne 0$ such that $Q_2(s) \ne 0$ implies that $f(s)$ has no square factor over $\bar E$.

Each of the four steps is an input lemma proved in the development. They are the classical Bertini arguments; we do not reproduce them.

*The simple sections.* Let $E \supset F$ be a field and $s \in E^{D \times N}$ with $Q(s) \ne 0$. Then $Q(s) \ne 0$ also in $\bar E$. By step 3 the cut is finite and lies in the open set where the map is an isomorphism. By step 4 the specialization $f(s)$ is squarefree. A lemma on Chow forms then shows that the cut is étale over $E$. Its geometric points are therefore distinct and $\delta$ in number, the linear system separates them, and $f(s)$ is a nonzero constant times the product of their linear forms. These are the four conditions of a simple section. $\square$

**Corollary 3.9.6 (Bertini theorem over number fields).** If the quoted theorems hold, then the Bertini statement over number fields holds.

Lean: `GlobalTheory.HSShort.bertiniNumberField_of_hilbertSamuel` (also `GlobalTheory.T.bertiniNumberField_of_hilbertSamuel₂`, a second name).

*Proof.* The Bertini statement for all fields $E \supset F$ contains the statement for number fields $E \supset F$, with the same $Q$. Apply the previous theorem. $\square$

**Example 3.9.7.** Let $T$ be the tuple of a smooth plane conic $C \subset \mathbb{P}^2_F$ with the sections $x_1, x_2, x_3$ of $\mathcal{O}(1)$. Then $D = 1$, $\mathrm{del}(T) = 2$, and a Chow form of degree $2$ is the resultant form: $f(u_0, u_1)$ vanishes when the lines $u_0 \cdot x = 0$ and $u_1 \cdot x = 0$ meet on $C$. A line $s$ meets $C$ in two distinct points exactly when it is not tangent to $C$. Tangency is the vanishing of a quadratic form in $s$ (the dual conic), and we can take $Q$ to be this form. For a line $s$ off the dual conic, $f(s)$ is a constant times the product of the two linear forms of the two points.

**Remark 3.9.8 (Formalization).** The theorem over number fields only restricts the quantifier over $E$ ([BertiniNumberFieldOfHilbertSamuel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/BertiniNumberFieldOfHilbertSamuel.lean#L9)). In the Bertini theorem the quoted theorems enter only through the degree lemma; the four steps that build $Q$ use none of them ([BertiniSimpleZerosGenericSections.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/BertiniSimpleZerosGenericSections.lean#L26)). The second names are wrappers. We have not unfolded the predicates for a geometric tuple, a good section and a Chow form; the text describes them by their role.
