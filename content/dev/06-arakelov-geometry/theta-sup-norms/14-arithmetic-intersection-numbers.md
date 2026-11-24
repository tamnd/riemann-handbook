---
title: Arithmetic intersection numbers and the projection formula
decls:
  - GlobalTheory.CompanionTheory.Ar.Pub.arithIntersectionSystem_of_poincareLelong_resK
  - GlobalTheory.T.intersection_exists_of_poincare_lelong
  - GlobalTheory.CompanionTheory.Ar.Pub.thmIExists
  - GlobalTheory.T.degree_and_coordinates_of_resolution
  - GlobalTheory.CompanionTheory.Ar.Pub.genDeg_and_pfCoord
  - GlobalTheory.CompanionTheory.Ar.Pub.genDeg_of_resExists
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Arithmetic intersection numbers and the projection formula

The volume bounds of this chapter are stated with arithmetic intersection numbers of hermitian lines on arithmetic varieties in products of projective spaces. This section builds these numbers from two inputs: the arithmetic Poincaré-Lelong formula of Section 13 and resolution of singularities in characteristic $0$. The numbers are defined by the recursion of Bost, Gillet and Soulé over the divisor of a section. We then prove the projection formula for a map that forgets some blocks of coordinates, and we collect everything into a system of intersection numbers. This system is the input of [the arithmetic intersection calculus](/entry/ar-calc-direct/).

### Families of heights

We keep the words of Section 13: blocks $K$, the ring $R$, arithmetic varieties $P$ of dimension $d$, hermitian lines with multidegrees, sections and horizontal primes. A family $I$ gives a real number $I(P; L_1, \dots, L_n)$ for each choice of blocks, each ideal $P$ and lines $L_1, \dots, L_n$.

**Definition 10.14.1.** A family $I$ is a family of heights if the following hold for every arithmetic variety $P$ of dimension $n$ and all smooth lines.

1. Symmetry: $I(P; L_{\sigma(1)}, \dots, L_{\sigma(n)}) = I(P; L_1, \dots, L_n)$ for every permutation $\sigma$.
2. Additivity in the last line: $I(P; L, A \otimes B) = I(P; L, A) + I(P; L, B)$, where $L$ has $n - 1$ entries.
3. Recursion: if $A$ has multidegree $a \geq 0$ and $s$ is a section of $A$ on $P$, then
$$
I(P; L, A) = \sum_W m_W c_W - \int_{X(\mathbb{C})} \log\lVert s\rVert_A \, \omega_L ,
$$
where $W$ runs over the minimal primes of $P + (s)$, $m_W$ is the length at $W$, $c_W = I(W; L)$ if $W$ is horizontal, and $c_W = \deg_L(W) \log p$ if $W$ lies over the prime $p$.

Here $\deg_L(W)$ is the geometric degree of the variety $W$ over $\mathbb{F}_p$ for the multidegrees of $L$. The recursion is the recursive formula for heights in the style of Bost, Gillet and Soulé.

A system of intersection numbers is a family of heights that is also multilinear, satisfies the projection formula below, and vanishes on mixed contractions: if $\pi$ forgets some blocks, $\dim P' = d + r$ and $\dim \pi(P') < d$, then $I(P'; \pi^* L_1, \dots, \pi^* L_d, N_1, \dots, N_r) = 0$.

### Resolution

The Hironaka form of resolution says: for a field $k$ of characteristic $0$ and a reduced closed subscheme $X \subseteq \mathbb{P}^M_k$ with a dense open smooth part $U$ of dimension $D$, there is a smooth closed $X' \subseteq \mathbb{P}^M_k \times \mathbb{P}^r_k$ of dimension $D$ whose projection to $X$ is an isomorphism over $U$, such that the complement of the inverse image of $U$ is a divisor with simple normal crossings.

The analytic form says: for an arithmetic variety $P$ of dimension $e + 1$ and a multihomogeneous ideal $J \not\subseteq P$, there are $J' \subseteq J$ with $J' \not\subseteq P$ and a compact complex manifold $\tilde X$ of dimension $e$ with a finite atlas and a holomorphic map onto $X(\mathbb{C})$. The map is injective and immersive off $V(J')$, every form that vanishes on $X(\mathbb{C})$ only inside $V(J')$ pulls back to a divisor with simple normal crossings, and the inverse image of $V(J')$ is null in each chart. The Hironaka form gives the analytic form by passing to complex points, see Section 15 for the normal crossing charts.

### Existence

**Theorem 10.14.2 (Existence of arithmetic intersection numbers).** Assume the arithmetic Poincaré-Lelong formula and the analytic form of resolution. Then a family of heights exists.

Lean: `GlobalTheory.CompanionTheory.Ar.Pub.thmIExists` (also `GlobalTheory.T.intersection_exists_of_poincare_lelong`, a second name).

*Proof.* Step 1: the definition. Define $I$ by recursion on $n$, with $I = 0$ for $n = 0$. Let $A$ have multidegree $a$ and let $m = \sum_k \lvert a_k\rvert$. Let $S_m$ be the Fubini-Study line of degree $m$ on every block. Then $A = (A \otimes S_m) - S_m$, and both lines have nonnegative degree. Choose sections of both on $P$ and define $I(P; L, A)$ as the difference of the two right sides of the recursion. The value $0$ at $n = 0$ is never tested, since no arithmetic variety has dimension $0$.

Step 2: the integrals are finite. The analytic form of resolution pulls the integrals over $X(\mathbb{C})$ back to a compact manifold where $\log\lVert s\rVert$ has normal crossings. So the integrands are integrable and absolutely integrable, and the integrals are bilinear in the potentials.

Step 3: Stokes. For two lines $B, B'$ of degree $0$, the integral of $\log h_B$ against $dd^c \log h_{B'}$ and $\omega_L$ is symmetric in $B$ and $B'$. This follows from bilinearity and a Stokes theorem on the variety, computed in Segre charts.

Step 4: a defect inequality. For semipositive lines, a defect term built from the recursion is at most $0$. This is the only place where the Poincaré-Lelong formula is used. With the twisted lines of semipositive twists, this gives the symmetry of the cross terms: for two sections $s$, $s'$ with no common horizontal component, the cross terms of the two recursions agree. This is the symmetry of the star product of two Green currents.

Step 5: independence. If $s$ and $s'$ have no common component, the recursion in the order $(s, s')$ and in the order $(s', s)$ gives the same value. The cycle terms agree by a count of the components over each prime, and the archimedean terms by Step 4. With the additivity of the recursion under products $s s'$, any two sections of the same degree give the same value. So $I$ is well defined, and additivity follows.

Step 6: symmetry. The swap of Step 5 and the symmetry of intersection numbers over the finite fields $\mathbb{Z}/p$ give axiom 1. Independence of the section in dimension $1$ is checked directly. $\square$

### The projection formula

Let $K \subseteq K'$ be blocks with the same coordinates on $K$, and let $\pi$ forget the blocks outside $K$. Let $P'$ and $P = \pi(P')$ be arithmetic varieties of the same dimension $d$. The generic fibre $P'_\eta$ of $\pi$ is a variety of dimension $0$ over the function field of $P$, and its degree is $\deg(P'_\eta)$, computed by an intersection family over fields.

**Theorem 10.14.3 (Projection formula).** Assume the analytic form of resolution. Then for every family of heights $I$ and smooth lines $L_1, \dots, L_d$ on $P$,
$$
I(P'; \pi^* L_1, \dots, \pi^* L_d) = \deg(P'_\eta) \, I(P; L_1, \dots, L_d).
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Pub.genDeg_of_resExists`.

*Proof.* Induction on $d$. The case $d = 0$ is empty. For the step, write $L_d$ as a difference of lines with sections and apply the recursion on both sides with a section $s$ on $P$ and its pullback $\pi^* s$ on $P'$. The recursion for rational sections only needs integrability, which comes from resolution.

The archimedean term. The integral of $\log\lVert \pi^* s\rVert$ against the pulled back forms on $X'(\mathbb{C})$ is $\deg(P'_\eta)$ times the integral on $X(\mathbb{C})$. Off a null set the map $X'(\mathbb{C}) \to X(\mathbb{C})$ is a covering of degree $\deg(P'_\eta)$, and the pushforward of the pulled back density is that multiple of the density. This is first shown for sections and then for rational sections.

The cycle term. The components of $P' + (\pi^* s)$ above one component $W$ of $P + (s)$ are incomparable. A computation in the semilocal ring of $P'$ along $W$ shows that the sum of their lengths times their fibre degrees is $m_W \deg(P'_\eta)$. By the induction hypothesis in dimension $d - 1$, and by the degree of the special fibres over $\mathbb{F}_p$ for vertical components, the cycle sum on $P'$ is $\deg(P'_\eta)$ times the cycle sum on $P$. $\square$

**Corollary 10.14.4 (Projection formula in coordinates).** Assume the analytic form of resolution. Then the projection formula holds, and if $P'$ is the closure of a point $y$ with coordinates in a field of characteristic $0$, the factor is
$$
\deg(P'_\eta) = [\mathbb{Q}(y) : \mathbb{Q}(\pi(y))],
$$
where $\mathbb{Q}(y)$ is the field generated by the ratios of coordinates of $y$ in the same block.

Lean: `GlobalTheory.CompanionTheory.Ar.Pub.genDeg_and_pfCoord` (also `GlobalTheory.T.degree_and_coordinates_of_resolution`, a second name).

*Proof.* The first part is the theorem. For the second, choose a generic fibre and an intersection family over the function field. The fibre has dimension $0$. Its degree is the number of its points in one affine chart, and this number is the field degree $[\mathbb{Q}(y) : \mathbb{Q}(\pi(y))]$. Put this into the theorem. $\square$

### The system of intersection numbers

**Theorem 10.14.5 (Arithmetic intersection system).** Assume the arithmetic Poincaré-Lelong formula and resolution of singularities in the Hironaka form. Then a system of arithmetic intersection numbers exists.

Lean: `GlobalTheory.CompanionTheory.Ar.Pub.arithIntersectionSystem_of_poincareLelong_resK`.

*Proof.* The Hironaka form gives the analytic form. The existence theorem gives a family of heights $I$. The corollary gives the projection formula in coordinates. The vanishing on mixed contractions holds with no hypotheses: if $\dim \pi(P') < d$, the pullbacks of $d$ lines from a variety of dimension less than $d$ give a zero top form on the complex points, and the cycle terms vanish for the same reason over each finite field. Multilinearity follows from additivity in the last line and symmetry, which moves any line to the last place. $\square$

**Remark 10.14.6 (Formalization).** The system theorem is at `Development/AutomorphicSpectrum/Proofs/MetricProofs/ArithIntersectionSystemOfPoincareLelong.lean:42` and the vanishing on mixed contractions is `contractMixed_closed` at line 30 of the same file. The system uses only the second half of the corollary (`.2`). The existence theorem is at `IntersectionExistsOfPoincareLelong.lean:142`; the Segre chart lemmas of Step 3 are the theorems `Seg.*` at lines 76 to 139 of that file, and the defect inequality `Inter.DeLeSemiPos.proof` is the only use of the Poincaré-Lelong hypothesis. The projection formula is at `DegreeAndCoordinatesOfResolution.lean:25`, the coordinate form `pfCoord_of_genDeg` at line 43, and the corollary at line 50; the corollary proves the first half twice, once inside the coordinate form. The coordinate factor is `IntermediateField.relfinrank`, which is $0$ for an infinite extension; the statement does not assume finiteness. The second names are at `IntersectionExistsOfPoincareLelongStatement.lean:11` and `DegreeAndCoordinatesOfResolutionStatement.lean:11`. The analytic form of resolution is `ResExistsStatement` (`ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/InterRes.lean:18`).
