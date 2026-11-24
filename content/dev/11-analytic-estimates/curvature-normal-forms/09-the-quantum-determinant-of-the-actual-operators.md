---
title: The quantum determinant of the actual operators
decls:
  - Formalism.FourierDecayAlt.P.MAx1.D7.det8
  - Formalism.FourierDecayAlt.P.determinant_hat
  - Formalism.FourierDecayAlt.P.JacquetIntegral.detCore
  - Formalism.FourierDecayAlt.P.actual_start
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The quantum determinant of the actual operators

This section proves property (A) of the [normal form of the actual operators](/entry/normal-form-from-module-statement/): the matrix of the actual operators at the top level, with the scalar $q$ of the parameter, is a start. Of the four conditions of a [start](/entry/start-is-start/), the hard one is the quantum determinant. In the model it was a computation in the model algebra; we first record the eight relations that this computation gives. For the actual operators the quantum determinant comes from a classical fact: the quantum determinant of a matrix of Capelli type is a product of a left and a right Capelli determinant. The result is used in the step [HypsAlt is nonempty](/step/nonempty-hyps/).

### The eight relations in the model

Let $M(Y)$ be a family of $2 \times 2$ matrices over a ring, and write $M(Y) = (m_{ab}(Y))$. Put
$$J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad \varepsilon_{cd} = J_{cd}.$$
The two matrix equations
$$M(Y+1)^T J M(Y) = q(Y) J, \qquad M(Y) J M(Y+1)^T = q(Y) J$$
say that $M$ has quantum determinant $q$ from both sides. Written in entries, each equation is four scalar relations, so eight in all.

**Lemma 1.9.1 (The eight relations).** Let $P$ be an admissible parameter and let $D$ be a model algebra that satisfies the laws, and assume the twelve algebraic rules (Sc), (Sh), (U), (F), (D), (D$^*$), (St), (S), (N), (M), (K) and (G) of the [quantum determinant from the relations](/entry/q-qdet-of/). Then for every $Y \in \mathbb C$ the matrix $Q(Y)$ of the model satisfies the eight relations, with the scalar $q$ of $P$.

Lean: `Formalism.FourierDecayAlt.P.MAx1.D7.det8`

*Proof.* This is the argument of the [quantum determinant from the relations](/entry/q-qdet-of/). Outside the finite set of $Y$ where some $Y + \rho_j(\pi) + n$ with $n \in \{0, 1, 2\}$ vanishes, each relation is an identity between products of the model operators, and it follows from the twelve rules. Both sides of each relation are polynomials in $Y$ with coefficients in the algebra. Two polynomials that agree outside a finite set are equal, so the relations hold for all $Y$. $\square$

### The determinant of the hat matrix

Fix a parameter with $k \ge 1$ and $n = 2r + k + 1$, and points $z, z'$ in the middle block with $T(z) > 0$ and $T(z') > 0$. Let $t_{ab}(Y)$ be the actual operators at the top level. They act on smooth functions $f$ on an open set $D$ of matrices, with values in a normed space. The *hat determinant* is the operator
$$\hat q(Y) f = t_{11}(Y+1)\, t_{22}(Y) f - t_{21}(Y+1)\, t_{12}(Y) f.$$

A *frame* of $z$ is a family $B = (b_1, \dots, b_k)$ of vectors in $\mathbb C^n$ adapted to $z$ in the middle block. For such $B$ and $w \in \mathbb C$ let $\operatorname{Cap}^L(B, w)$ be the left Capelli determinant along $B$ at the shift $w$, and let $\operatorname{Cap}^R(B, w)$ be the right Capelli determinant. They are quantum minors of size $k$ of the left and right invariant derivatives, taken in the directions of $B$.

**Theorem 1.9.2 (Hat determinant).** Let $z, z'$ lie in the middle block with $T(z) > 0$ and $T(z') > 0$. Let $D$ be open, and let $f$ be smooth on $D$ at the top level. Let $B$ be a frame of $z$ and $B'$ a frame of $z'$. Then for every $g$ in $D$ at the top level and every $Y \in \mathbb C$,
$$\hat q(Y) f(g) = -T(z)\,T(z')\; \operatorname{Cap}^L\bigl(B, Y + \tfrac k2\bigr)\, \operatorname{Cap}^R\bigl(B', Y + \tfrac k2\bigr) f(g).$$

Lean: `Formalism.FourierDecayAlt.P.determinant_hat`

*Proof.* There are four steps. First, an algebraic quantum determinant: for a matrix of generators of $\mathfrak{gl}$ that satisfies the commutation relations of the Lie algebra, the quantum determinant of a Capelli matrix built from it, with the shifts $u, u+1, \dots$, is a quantum minor. Second, the hat matrix of the top level is such a matrix in the frame given by $B$ on the left and $B'$ on the right: the entries $t_{ab}$ are bordered minors in which the border rows and columns are the coordinates of $z$ and $z'$, and the frames complete these to a basis. Third, the right Capelli determinant along $B'$ is good: it acts on functions on the top level in the same way as the right Capelli element of the frame. Fourth, a swap rule moves left Capelli elements past right ones, since left and right invariant derivatives commute. The factor $-T(z)T(z')$ is the product of the values of the hermitian form at the two border vectors, and the sign comes from the order of the rows. The shift $Y + k/2$ is the shift $u = Y + (m - 1)/2$ with $m = k + 1$ at the top level. $\square$

### The quantum determinant at the top level

The hat determinant is one of the eight relations. The others follow from it by symmetry of the actual operators. We state the result for functions in the space $\mathcal F$ of smooth functions on a domain $D$ at the top level that are left and right equivariant for the unipotent characters $\psi$ and for $\pi$, $\pi'$.

**Theorem 1.9.3 (Quantum determinant of the actual operators).** Let $P$ be a parameter, take a place of $P$ with points $z, z'$ and representations $\pi, \pi'$, and let $D$ be a domain at the top level. Then for every $J \in \mathcal F$, every $g \in D$ at the top level, every $Y$, and all $c, d \in \{1, 2\}$,
$$\begin{aligned} t_{1c}(Y+1)\, t_{2d}(Y) J - t_{2c}(Y+1)\, t_{1d}(Y) J &= q(Y)\, \varepsilon_{cd}\, J,\\ t_{c1}(Y)\, t_{d2}(Y+1) J - t_{c2}(Y)\, t_{d1}(Y+1) J &= q(Y)\, \varepsilon_{cd}\, J, \end{aligned}$$
evaluated at $g$. Here $q$ is the scalar of the parameter.

Lean: `Formalism.FourierDecayAlt.P.JacquetIntegral.detCore`

*Proof.* We use seven inputs: the RTT relation for the actual operators at each level; the fact that for any matrix $M$ over a ring that satisfies the RTT relation, the quantum determinant $M(Y+1)^T J M(Y)$ is a scalar multiple $\hat q J$ of $J$ for some element $\hat q$ of the ring; the [hat determinant](/entry/determinant-hat/); the right and the left action of the types on $\mathcal F$; the fact that the actual operators preserve $\mathcal F$; and the locality of the actual operators. By the second input, both equations reduce to one element $\hat q(Y)$ of the operator algebra. The hat determinant computes $\hat q(Y)$ as $-T(z)T(z')$ times a product of a left and a right Capelli determinant. On a function in $\mathcal F$ the right Capelli determinant along $B'$ acts through the representation $\pi'$ and the left one along $B$ through $\pi$. The type actions identify these with scalars, whose product with $-T(z)T(z')$ is $q(Y)$ by the definition of the scalar $q$ of the parameter. Locality reduces the identity on $D$ to an identity at each point. $\square$

### The start

**Theorem 1.9.4 (The actual operators form a start).** For every parameter $P$, every place of $P$, and every family $X$ of actual operators on the radial space at the top level, the pair $(X.Q, q)$ is a start, and the entries $t_{21}(Y)$ and $t_{21}(Y')$ commute for all $Y, Y'$.

Lean: `Formalism.FourierDecayAlt.P.actual_start`

*Proof.* The RTT relation at the top level gives condition 2 of a start and the commutation of the entries $t_{21}$: the RTT relation for the pair of indices $(2, 1), (2, 1)$ says $[t_{21}(Y), t_{21}(Y')] = 0$. The [quantum determinant of the actual operators](/entry/det-core/) gives condition 3. Both relations are first proved on the slices of a radial function at each point, and the locality of the actual operators lifts them to the radial space. The operators of the radial space live in the pair algebra $\mathrm{Pr} = \mathrm{Op} \times \mathrm{Op}^{op}$, and the remaining conditions, the hermitian property for real $Y$ and the reality of $q$ on the real line, are proved in this algebra from $q(\bar Y) = \overline{q(Y)}$. $\square$

This theorem is property (A) of the [normal form of the actual operators](/entry/normal-form-from-module-statement/).

**Remark 1.9.5 (Formalization).** The lemma on the eight relations exists twice: once for a model algebra with laws, and once in another namespace without the algebra argument ([WeightedSumDifferenceIdentity.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/WeightedSumDifferenceIdentity.lean#L1493)). The hat determinant is first proved for smooth functions; the statement that the regular case implies the smooth case is then proved by ignoring its hypothesis and returning the smooth result ([DeterminantGeneric.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/DeterminantGeneric.lean#L26)). We did not unfold the definitions of the frames of $z$ and of the Capelli determinants; the description above follows their names and the shape of the statements.
