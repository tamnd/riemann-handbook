---
title: K-finite vectors and the Fock space
decls:
  - PositivityTheory.SiegelWeilFormula.KFP.kFinPoly_of_k
status: drafted
drafted_by: writer@claude-opus-5-5
---
## K-finite vectors and the Fock space

The Siegel-Weil formula is an identity for each $K$-finite vector of the Weil representation. Its proof works with a smaller and more concrete space, the *Fock space*: at each real place the function is a polynomial times a Gaussian, and at the finite places it is a Schwartz-Bruhat function. This section proves that each $K$-finite vector is in the Fock space. The argument is a classical one, in the spirit of the [Fock model](/learn/theta/#the-fock-model) and of the [[Bargmann transform|QPH28QH036]]: a rotation in $K$ acts on a line of the Fock space with an eigenvalue that is not a root of unity, a finite relation among the rotated vectors forces an entire function to be a polynomial, and a function whose Gaussian Laplace transforms are polynomials on every line is a polynomial times the Gaussian. The result is an input of [the Siegel-Weil formula before the main step](/entry/siegel-weil-std-pre-k/).

We keep the Siegel-Weil datum $d$ of [the constant term split](/entry/ct-split-of-k/): the spaces $A$ of dimension $m$ and $Y$ of dimension $n$, the doubled group $G$, the maximal compact subgroup $K$ of $G(\mathbb{A})$, and the Weil representation $\omega$ of $G(\mathbb{A})$ on the [[Schwartz space|GE020MY43M]] $\mathcal{S}$ of a Lagrangian. The *matrix model* is a linear map $\Phi \mapsto T\Phi$ from $\mathcal{S}$ to functions on the space $M = M_{m \times n}(\mathbb{A}_E)$ of matrices. It is the Schrödinger model of [the Weil representation](/learn/theta/#the-weil-representation) written in the coordinates $X$ of $M$.

**Definition 6.3.1 (K-finite vector).** A vector $\Phi \in \mathcal{S}$ is *$K$-finite* if the span of the vectors $\omega(k)\Phi$ for $k \in K$ is a finite-dimensional complex vector space.

**Definition 6.3.2 (Real datum and Fock space).** A *real datum* $R$ for $d$ consists of a frame $\mathrm{fr}_w \in GL_m(\mathbb{C})$ and a sign $\mathrm{sg}_w = \pm 1$ for each infinite place $w$ of $F$, with $\zeta\, {}^t\mathrm{fr}_w\, J_A\, \overline{\mathrm{fr}_w} = \mathrm{sg}_w$ for a fixed $\zeta \in \{1, i\}$, and continuous homomorphisms $\iota_w$ from the real unitary group of rank $n$ into $G(\mathbb{A})$ that act at the place $w$ only. For $X \in M$ let $\mathrm{loc}_w(X) \in M_{m \times n}(\mathbb{C})$ be the complex conjugate of $\mathrm{fr}_w^{-1} X_w$. For a polynomial $P$ in the entries $u_{ai}$ and $\bar u_{ai}$ of an $m \times n$ complex matrix $u$ put
$$f_P(u) = P(u, \bar u)\, \exp\Bigl(-2\pi \sum_{a, i} \lvert u_{ai} \rvert^2\Bigr).$$
The *Fock space* $\mathcal{F}_R$ is the complex span of the functions
$$X \longmapsto \Bigl(\prod_{w \mid \infty} f_{P_w}\bigl(\mathrm{loc}_w(X)\bigr)\Bigr)\, g(X_f),$$
where $P_w$ is a polynomial for each infinite place $w$, $X_f$ is the finite part of $X$ in a fixed basis of $E$ over $F$, and $g$ is a Schwartz-Bruhat function of the finite coordinates. The *vacuum vectors* are the functions of this form with $P_w = 1$ for all $w$.

The proof takes seven properties of the matrix model and of the real datum as given. They are the standard formulas of the Schrödinger model of [the Weil representation](/learn/theta/#the-weil-representation) (Kudla 1994 for the unitary case), and the main theorem takes them as assumptions.

1. *Transform laws.* The map $\Phi \mapsto T\Phi$ is a bijection from $\mathcal{S}$ onto the Schwartz space of $M$; it has the usual formulas for the Siegel parabolic, $\omega(n(\beta))$ acting by the character $\psi(-\tfrac12 \operatorname{tr}(\beta\, {}^tX J_A \bar X))$ and $\omega(m(t))$ acting by $\chi(\det t) \lvert \det t \rvert^{m/2}$ and a change of variables; the Weyl element acts by a Fourier transform; the theta sum of $\Phi$ is the sum of $T\Phi$ over the rational points; and the theta integral is automorphic.
2. *Unitarity.* $\omega$ preserves the $L^2$ pairing $B(\Phi, \Phi') = \int_M T\Phi\, \overline{T\Phi'}\, d\nu$ for each Haar measure $\nu$.
3. *Heisenberg translates.* The operators of the Heisenberg group act on $T\Phi$ by translation and multiplication by a character.
4. *Datum properties.* There is a measure for the Fourier transform, a rational Weyl element, and $G(\mathbb{A})$ is a locally compact, second countable, Hausdorff topological group.
5. *Fock membership.* $\mathcal{F}_R$ is inside the Schwartz space of $M$, and at each real place $w$ each element of $\mathcal{F}_R$ is a finite sum of products of a function $f_P(\mathrm{loc}_w(X))$ with a function of the other coordinates.
6. *Local operators.* At each real place there are operators $L(y)$ for $y$ in the real unitary group with $T(\omega(\iota_w(y))\Phi) = L(y) f \cdot \Psi$ whenever $T\Phi = f \cdot \Psi$.
7. *Local instances.* These local operators come from a representation of the real unitary group on polynomials, with the signature conditions of a holomorphic discrete series model, and the maximal compact subgroup maps polynomials of the form $f_P$ to polynomials of the same form.

**Theorem 6.3.3 (K-finite vectors are in the Fock space).** Assume the seven properties above for all Siegel-Weil data and all real data. Let $d$ be a Siegel-Weil datum and $R$ a real datum for $d$. If $\Phi \in \mathcal{S}$ is $K$-finite, then $T\Phi \in \mathcal{F}_R$.

Lean: `PositivityTheory.SiegelWeilFormula.KFP.kFinPoly_of_k`.

The proof uses three lemmas. The first two are statements about one complex variable and about Gaussian integrals on a Euclidean space.

**Lemma 6.3.4 (A finite relation under a rotation).** Let $q$ be a nonzero complex polynomial, $\mu \ne 0$, and $\omega \ne 0$ such that $\omega^j \ne 1$ for all integers $j \ge 1$. There is $N$ with this property: if $E$ is an entire function with
$$\sum_{i = 0}^{\deg q} q_i\, \mu^i\, E(\omega^i z) = 0 \quad \text{for all } z \in \mathbb{C},$$
then $E$ is a polynomial of degree at most $N$.

Lean: `PositivityTheory.SiegelWeilFormula.KFP.poly_of_rot`.

*Proof.* Expand $E(z) = \sum_j a_j z^j$. The relation gives $a_j\, q(\mu \omega^j) = 0$ for each $j$. The numbers $\mu \omega^j$ are pairwise distinct, since $\omega^a = \omega^b$ with $a < b$ gives $\omega^{b - a} = 1$. So at most $\deg q$ of them are roots of $q$, and $a_j = 0$ for all $j$ larger than the largest such index. Take $N$ to be that index. $\square$

**Lemma 6.3.5 (Polynomials on all lines).** Let $V$ be a real Euclidean space, $c > 0$, $N \ge 0$ and $h$ a Schwartz function on $V$. Assume that for each $\xi \in V$ there is a polynomial $p_\xi$ of degree at most $N$ with
$$\int_V h(u)\, e^{-c \lVert u \rVert^2}\, e^{z \langle \xi, u \rangle}\, du = \exp\Bigl(\frac{z^2 \lVert \xi \rVert^2}{8c}\Bigr)\, p_\xi(z) \quad \text{for all } z \in \mathbb{C}.$$
Then there is a polynomial $P$ on $V$ of total degree at most $N$ with $h(u) = P(u)\, e^{-c \lVert u \rVert^2}$ for all $u$.

Lean: `PositivityTheory.SiegelWeilFormula.KFP.poly_gauss_of_lines`.

*Proof.* At $z = i t$ the left side is the Fourier transform of $h\, e^{-c\lVert u \rVert^2}$ in the direction $\xi$. The hypothesis says that this Fourier transform is the Gaussian $\exp(-t^2 \lVert \xi \rVert^2 / 8c)$ times a polynomial of degree at most $N$ on each line through $0$. A function on $V$ that is a polynomial of degree at most $N$ on every line through $0$, and is smooth, is a polynomial of total degree at most $N$. So the Fourier transform is a polynomial times a Gaussian. The inverse Fourier transform of a polynomial times a Gaussian is a polynomial times a Gaussian, with the same bound on the degree. Comparing with $h\, e^{-c\lVert u \rVert^2}$ and dividing by the Gaussian gives $P$. $\square$

**Lemma 6.3.6 (Line data).** Under the assumptions of the theorem, for each real datum $R$ there are an element $k \in K$, a complex number $\omega$ with $\lvert \omega \rvert = 1$ that is not a root of unity, an eigenvalue $\chi \ne 0$, constants $C \ne 0$ and $c$, and a family of vectors $v(\xi, z)$ of the symplectic space, for $\xi$ in the real Euclidean space $V$ of the real coordinates of $\mathrm{loc}_w$ at all real places and $z \in \mathbb{C}$, such that:

1. $\omega(k)\Omega = \chi\, \Omega$ for each vacuum vector $T\Omega$;
2. $k$ acts on the family by $k \cdot v(\xi, z) = v(\xi, \omega z)$;
3. for each vacuum vector $T\Omega$ with finite part $g$ and each $\Phi \in \mathcal{S}$,
$$\begin{aligned} B\bigl(\Phi, \rho(v(\xi, z))\Omega\bigr) &= C\, e^{-c \lvert z \rvert^2 \lVert \xi \rVert^2}\, e^{-z^2 \lVert \xi \rVert^2 / 16\pi} \\ &\quad \cdot \int_V h_g(u)\, e^{-2\pi \lVert u \rVert^2}\, e^{z \langle \xi, u \rangle}\, du, \end{aligned}$$
where $\rho$ is the Heisenberg action and $h_g(u) = \int T\Phi(u, y)\, \overline{g(y)}\, dy$ is the integral of $T\Phi$ against $\bar g$ over the finite coordinates.

Lean: `PositivityTheory.SiegelWeilFormula.KFP.line_data_k`.

*Proof.* Take $k$ to be the element of $K$ that rotates each real coordinate by $e^{-i}$; it is in $K$, and $\omega = e^{-i}$ has absolute value $1$ and is not a root of unity because $\pi$ is irrational. The vacuum vectors are eigenvectors of $k$ by the local instances. The family $v(\xi, z)$ is the line of the Heisenberg group in the direction $\xi$ with parameter $z$, and $k$ rotates it. The formula for the pairing comes from the Heisenberg translates and the unitarity: the Heisenberg operator moves the Gaussian of $\Omega$, and the pairing with a moved Gaussian is a Gaussian Laplace transform. $\square$

*Proof of the Theorem.* Let $\Phi$ be $K$-finite, and let $V_\Phi$ be the finite-dimensional span of its $K$-translates. Take $k$, $\omega$ and $\chi$ from the lemma on line data. The operator $\omega(k)$ maps $V_\Phi$ to itself, so its characteristic polynomial $q \ne 0$ gives
$$\sum_{i = 0}^{\deg q} q_i\, \omega(k)^i \Phi = 0.$$
By a criterion for the Fock space, which follows from the Fock membership property, it is enough to show that for each Schwartz-Bruhat function $g$ of the finite coordinates the function $h_g$ is a polynomial times $e^{-2\pi \lVert u \rVert^2}$. Fix $g$, and let $\Omega$ be the vector with $T\Omega$ the vacuum vector of finite part $g$; it exists since $T$ is onto. Fix $\xi$ and put
$$E_\xi(z) = e^{-z^2 \lVert \xi \rVert^2 / 16\pi} \int_V h_g(u)\, e^{-2\pi \lVert u \rVert^2}\, e^{z \langle \xi, u \rangle}\, du.$$
This is an entire function. Pair the relation with $\rho(v(\xi, z))\Omega$. Unitarity moves $\omega(k)^i$ to the other side as $\omega(k)^{-i}$. There it acts on $\Omega$ by $\bar\chi^{-i}$ and on $v(\xi, z)$ by $z \mapsto \omega^{-i} z$. The line data formula then gives
$$C\, e^{-c \lvert z \rvert^2 \lVert \xi \rVert^2} \sum_{i = 0}^{\deg q} q_i\, \bar\chi^{-i}\, E_\xi(\omega^{-i} z) = 0,$$
because $\lvert \omega^{-i} z \rvert = \lvert z \rvert$. The factor in front is not $0$. The lemma on a finite relation under a rotation, with $\mu = \bar\chi^{-1}$ and the rotation $\omega^{-1}$, gives a bound $N$ that does not depend on $\xi$ and shows that $E_\xi$ is a polynomial of degree at most $N$. So the Gaussian Laplace transform of $h_g$ on the line of $\xi$ is $e^{z^2 \lVert \xi \rVert^2 / 16\pi}$ times a polynomial of degree at most $N$. With $c = 2\pi$ we have $8c = 16\pi$, and the lemma on polynomials on all lines gives $h_g = P\, e^{-2\pi \lVert u \rVert^2}$. $\square$

The converse, that a vector whose matrix model is in the Fock space is $K$-finite, is a separate input of the [Siegel-Weil formula, middle step](/entry/siegel-weil-std-mid-k/).

**Remark 6.3.7 (Formalization).** The two one-variable lemmas exist twice: the versions in [PolyGaussOfLines.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/RealAdelicFockSpace/PolyGaussOfLines.lean#L12) are wrappers, with the same statements, of the lemmas in [IteratedDerivScale.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/PolynomialGaussianIntegrals/IteratedDerivScale.lean#L27) and [PolynomialGaussianIntegrals/PolyGaussOfLines.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/PolynomialGaussianIntegrals/PolyGaussOfLines.lean#L92). Two small lemmas of the theorem, that the action on the symplectic space is a group action, are public helpers in [SiegelWeilKfpMain.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilKfpMain.lean#L20). The seven properties are hypotheses of the theorem; the datum properties are the copy for all base data, not the copy for the good base data of this chapter. We have not opened the proof of the line data or of the criterion for the Fock space, and the proof of the line data above is a summary of the shape of the statement.
