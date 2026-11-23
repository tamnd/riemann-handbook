---
title: The Fock model and the oscillator representation
decls:
  - GlobalTheory.OscGauss.exists_isOsc
  - GlobalTheory.T.exists_oscillatorRepresentation_unitaryCover
  - GlobalTheory.nonempty_fockData_pair
  - GlobalTheory.CoefMapRecord.exists_io_record
  - GlobalTheory.TrueTheta.exists_family_of_curve
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Fock model and the oscillator representation

The theta series of this chapter use, at the archimedean places, the Weil representation of a unitary group $\mathrm{U}(p, q)$ in its Fock model, and they use, at the finite places, vectors of lattice models that are tied together by intertwining operators. This section constructs these objects. First, for every $p$ and $q$, we build the oscillator representation of the double cover of $\mathrm{U}(p, q)$ on the Fock space, from Gaussian vectors, and we get the Fock data of a seesaw pair. Then we build the harmonic coefficient map at the weights of the datum, which sends a highest weight vector to the letter polynomial. Last, from a curve datum we build a family of theta vectors at all even ranks, equivariant under the change of lattices. See [the Weil representation](/learn/theta/#the-weil-representation), [the Fock model](/learn/theta/#the-fock-model) and [highest weights](/learn/representations/#highest-weights-and-branching) in Volume 1.

### The Fock space and the cover

Let $p, q \ge 0$, and let $I = I_{p,q}$ be the disjoint union of $\{1, \dots, p\}$ and $\{1, \dots, q\}$. A *Fock space* on $I$ is a complex Hilbert space $H$ with an injective linear map $\iota$ from the polynomial ring $\mathbb{C}[x_a : a \in I]$ to $H$, with dense image, such that the monomials are orthogonal and $\langle \iota(x^\alpha), \iota(x^\alpha) \rangle = \alpha!$. This is the Bargmann-Fock space: the completion of the polynomials for the inner product with $\langle x^\alpha, x^\beta \rangle = \delta_{\alpha\beta}\,\alpha!$.

Let $J_{p,q}$ be the diagonal matrix with $p$ entries $1$ and $q$ entries $-1$, let $\mathrm{U}(p, q)$ be the group of $g$ with $g^{*} J_{p,q}\, g = J_{p,q}$, and let $\mathfrak{u}(p, q)$ be its Lie algebra. A *cover datum* for $(p, q)$ is a topological group $G$ with a Haar measure and two homomorphisms $c : G \to \mathrm{U}(p, q)$ and $s : G \to \mathbb{C}^\times$ with $s(g)^2 = \det c(g)$, such that $g \mapsto (c(g), s(g))$ is an embedding onto the pairs $(g, w)$ with $w^2 = \det g$, together with an exponential map from $\mathfrak{u}(p, q)$ to $G$ that lifts the matrix exponential on one-parameter subgroups. So $G$ is the square root cover of $\mathrm{U}(p, q)$ by the determinant.

Each $Z \in \mathfrak{u}(p, q)$ acts on polynomials by a second order operator $\omega_0(Z)$: a sum over the entries of $Z$ of the oscillator matrix units, which are the products $x_a x_b$, $x_a \partial_b$ and $\partial_a \partial_b$ according to the blocks of $Z$.

**Definition 3.8.1 (Oscillator representation).** Let $G$ be a cover datum and $H$ a Fock space on $I_{p,q}$. A homomorphism $\Omega : G \to \mathrm{End}(H)$ is an *oscillator representation* if each $\Omega(g)$ is an isometry, $g \mapsto \Omega(g)\,x$ is continuous for each $x$, and for each $Z \in \mathfrak{u}(p, q)$ and each polynomial $f$, the curve $t \mapsto \Omega(\exp(tZ))\,\iota(f)$ has derivative $\iota(\omega_0(Z) f)$ at $t = 0$.

### Gaussian vectors

Let $A$ be a complex $p \times q$ matrix with $1 - A^{*}A$ positive definite, and let $x \in \mathbb{C}^{I}$. Put
$$P_{A,x} = \sum_{i, j} A_{ij}\, x_i\, y_j + \sum_{a \in I} x_a\, X_a ,$$
where $x_i$ and $y_j$ are the variables of the two blocks and $X_a$ is the variable at $a$. The development proves that there is a unique vector $\gamma_{A,x} \in H$ whose coefficients against the monomials are those of the power series $\exp(P_{A,x})$: $\langle \iota(x^\alpha), \gamma_{A,x} \rangle = \alpha!\,[x^\alpha]\exp(P_{A,x})$. The condition on $A$ makes the series square summable.

A *Gaussian parameter* is a tuple $(c, Y, v, \varphi)$ of a scalar, a matrix $Y$ with $I$ rows and $q$ columns that is negative for the form $J_{p,q}$, and two vectors in $\mathbb{C}^{I}$. It defines a vector $\mathrm{vec}(c, Y, v, \varphi)$, a scalar multiple of a Gaussian vector. The group $G$ acts on parameters by $g \cdot (c, Y, v, \varphi) = (s(g)\,c,\ c(g)\,Y,\ c(g)\,v,\ \varphi\,c(g)^{-1})$.

**Lemma 3.8.2 (Gaussian vectors).** The inner product of two Gaussian vectors is $\overline{c}\,c'$ times a kernel $k(Y, v, \varphi; Y', v', \varphi')$ that is invariant under the action of $\mathrm{U}(p, q)$, up to the factor $|s(g)|^2 = 1$. The span of the Gaussian vectors is dense in $H$.

*Proof.* The inner product of two Gaussian vectors is a Gaussian integral; the development computes it as an explicit kernel and proves the invariance of the kernel. The kernel has a determinant factor $\det(Y^{*}J_{p,q}Y')$, which is a unit because $Y$ and $Y'$ are negative. The coherent vectors $\gamma_{0,x}$ already span a dense subspace. $\square$

**Theorem 3.8.3 (Oscillator representation).** For every cover datum $G$ for $(p, q)$ and every Fock space $H$ on $I_{p,q}$, there is an oscillator representation $\Omega$ of $G$ on $H$.

Lean: `GlobalTheory.OscGauss.exists_isOsc` (also `GlobalTheory.T.exists_oscillatorRepresentation_unitaryCover`, a second name).

*Proof.* Define $\Omega$ on Gaussian vectors by $\Omega(g)\,\mathrm{vec}(\mathfrak{p}) = \mathrm{vec}(g \cdot \mathfrak{p})$. The action on parameters is an action of $G$. By the lemma, $\Omega(g)$ preserves the inner products of Gaussian vectors, and the inner products are continuous in $g$. A map that is defined on a family with dense span and preserves its inner products extends to a unitary representation: this gives $\Omega$, isometric and strongly continuous.

For the derivative condition, fix $Z$ and a polynomial $f$. It is enough to compute the derivative weakly on the dense set of Gaussian vectors, since the operators $\Omega(\exp(tZ))$ are isometries that form a one-parameter group and preserve the set of Gaussian vectors. For a Gaussian vector $\mathrm{vec}(\mathfrak{p})$, the function $t \mapsto \langle \iota(f), \Omega(\exp(-tZ))\,\mathrm{vec}(\mathfrak{p}) \rangle$ is the inner product of $\iota(f)$ with a Gaussian vector whose parameters move smoothly in $t$. Its derivative at $0$ is $\langle \iota(\omega_0(Z) f), \mathrm{vec}(\mathfrak{p}) \rangle$, by the annihilator equations of the Gaussian vectors and the formula for the adjoint of $\omega_0(Z)$, which is $\omega_0(-Z)$ for $Z \in \mathfrak{u}(p, q)$. $\square$

### The seesaw pair

Let $p, q, r, s \ge 0$. The tensor product of a Hermitian space of signature $(p, q)$ and one of signature $(r, s)$ has signature $(pr + qs, ps + qr)$, and this gives the seesaw embedding of $\mathrm{U}(p, q) \times \mathrm{U}(r, s)$ into $\mathrm{U}(pr + qs, ps + qr)$ by Kronecker products (see [reductive dual pairs](/learn/theta/#reductive-dual-pairs)).

**Definition 3.8.4 (Fock data of a pair).** Let $G_0$, $G_1$, $G_2$ be cover data for $(pr + qs, ps + qr)$, $(p, q)$ and $(r, s)$. *Fock data* for $(G_0, G_1, G_2)$ are a Fock space $H$ on the polynomials in $pr + qs + ps + qr$ variables, an oscillator representation $\Omega$ of $G_0$ on $H$ in the indexing of the tensor product, and a homomorphism $G_1 \times G_2 \to G_0$ that covers the Kronecker product, with $s_0(g_1, g_2) = s_1(g_1)^{r+s}\,s_2(g_2)^{p+q}$.

**Corollary 3.8.5 (Fock data exist).** For all $p, q, r, s$ and all cover data $G_0$, $G_1$, $G_2$ as above, Fock data exist.

Lean: `GlobalTheory.nonempty_fockData_pair`

*Proof.* Take the Fock space of square summable sequences on the monomials, which exists for every index set. [The oscillator theorem](/entry/exists-is-osc/) gives an oscillator representation of $G_0$ on it. The development proves that Fock data exist if and only if an oscillator representation of $G_0$ exists: the seesaw map $G_1 \times G_2 \to G_0$ comes from the uniqueness of lifts in the cover datum $G_0$, since $(c_1 \otimes c_2,\ s_1^{r+s} s_2^{p+q})$ is a pair with the right square. $\square$

### The harmonic coefficient map

Let $D$ be a datum, and fix the weights $\kappa_i$ of the datum at each index $i$, with the condition that ties them to the signature of $W_i$. Let $c$ be a coefficient field of the datum and let $\lambda_i$ be the highest weights of the representation $V_{\lambda_i}$ of $\mathrm{GL}_{n}$ at each embedding, $n = \dim V_i$.

**Definition 3.8.6 (Harmonic coefficient record).** A *harmonic coefficient record* at $i$ is a $c$-linear map $\iota$ from $V_{\lambda_i}$ (over $c$) to polynomials in the letters of the archimedean datum, and a vector $h \in V_{\lambda_i}$, with these properties. The vector $h$ is the tensor product of the extremal vectors. The map $\iota$ is injective, and its image is the span of the harmonic polynomials with the multiplicities $a$ of the weights. For every unitary matrix $\gamma$ over $E$, $\iota(\rho(\gamma) v)$ is a scalar $c_\gamma$ times the conjugate action of $\gamma$ on $\iota(v)$. The vector $h$ lies in the standard lattice and is primitive there. The map sends $h$ to the letter polynomial, and the image of the standard lattice contains the integral harmonic polynomials.

**Theorem 3.8.7 (Harmonic coefficient record).** Let the parameters of $D$ be pinned, and let the weights $\kappa$ satisfy the tie to the signatures. Then for every index $i$ and every coefficient field $c$ there is a harmonic coefficient record at $i$, with the multiplicities of $\kappa_i$ and the highest weight $\lambda_i$.

Lean: `GlobalTheory.CoefMapRecord.exists_io_record`

*Proof.* The weight exponents of the datum give, at each embedding $\tau$, the exponents of the weight at the positive and at the negative places of $W_i$, injectivity of the embedding map, and the values of the multiplicities. The highest weight $\lambda_i$ at $\tau$ has the form $s + a^{+}(n) - a^{-}(n^{\vee})$ for an integer $s$, where $a^{+}$ is read on the first $k + i$ coordinates and $a^{-}$ on the last $m - i - 1$ coordinates in reverse order. This uses the half shift of the parameters, the oddness of $t$, and the gap condition of the parameters. A general result of the development builds the record from such a weight when the signature $(p, q)$ satisfies $p + q \le n$; here $p = k + i$, $q = m - i - 1$, and $p + q \le n$ holds. The multiplicity of each weight equals the multiplicity in the record by the tie of $\kappa$ to the signatures, at the embeddings with and without the CM type. $\square$

### Theta vectors from a curve

**Theorem 3.8.8 (Family of theta vectors).** Let $D$ be a datum, $\mathfrak{c}$ an ideal of the ring of integers of $K$ and $\delta \in \mathbb{C}$, and assume that $(\mathfrak{c}, \delta)$ is a curve datum for $D$. Then there are a character $\chi$ of the ideles of $E$ in the admissible class and, for all even $N$ and $N'$ and all self-dual lattices $L \subset E^{N}$ and $L' \subset E^{N'}$, vectors $e(N, N', L, L')$ with these properties.

1. Each $e(N, N', L, L')$ lies in the theta space of the lattice pair $(L, L')$, is nonzero, and has coefficients in a number field.
2. The family is equivariant under rational scaling of the lattices, and under change of lattices: if $L'$ is replaced by $L''$ (or $L$ by $L_1$), then $e$ changes by the intertwining operator between the lattice models, times a power of $\chi$ of the determinant of the change.

Lean: `GlobalTheory.TrueTheta.exists_family_of_curve`

*Proof.* The curve datum has a torsion point $t_0$ of order $2$, and it gives a scalar function $\kappa$ and a character $\chi$ whose value on determinants matches $\kappa$. For even $N N'$, the development gives a nonzero vacuum vector $e_0(N, N')$ in the standard lattice model. Put
$$e(N, N', L, L') = \chi(\det L)^{N'/2}\,\chi(\det L')^{-N/2}\, I(L_0 \to L, L')\, e_0(N, N'),$$
where $I$ is the intertwining operator from the standard lattice model to the model of $(L, L')$. For a self-dual lattice there is a group element $g$ that moves the standard lattice to it. With these moves, $e(N, N', L, L')$ is the scalar $\kappa(g, g')$ times the intertwined vacuum. The Weil representation of the pair carries the vacuum to $e$ under the moves, and the scalars $\kappa(g, g')$ are algebraic. Part 1 follows: the intertwiner is unitary between theta spaces, the scalar is a unit, and the coefficients lie in a number field because the vacuum and the scalars do. Part 2 is a computation: compose two moves, use the multiplicativity of the Weil representation on the theta spaces and the compatibility of the Weil representation with the intertwiners, and the determinant formula for $\chi$. For rational scaling, the even rank gives the oddness equation of the Weil data, so the scaled vector is the same vector. $\square$

**Remark 3.8.9 (Formalization).** The oscillator theorem is `OscGauss.exists_isOsc` in [ExistsOscillatorRepresentationUnitaryCover.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsOscillatorRepresentationUnitaryCover.lean#L156), with `gauss` (line 27), `vec` (line 41), the action `act` (line 44), `inner_vec` (line 56), `dense_vec` (line 75) and the unitary extension `exists_rep` (line 82). The Gaussian inputs, from `T.fock_existsUnique_gaussian_vector` to `T.hasDerivAt_of_weak_deriv_on_invariant_total_set`, were not opened. `Fock` and `IsOsc` are in [OscActMonomialOfUnique.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OscActMonomialOfUnique.lean#L468), and `GrpData` and `FockData` in [DataTheta.lean](lean:Formalism/LocalRingCardinality/DataTheta.lean#L93). A different predicate `IsOsc`, and a different `exists_isOsc` in the namespace `RealWeil.Osc`, are in `Proofs/DivisorProofs`. The pair corollary is [NonemptyFockModelUnitaryDualPair.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/NonemptyFockModelUnitaryDualPair.lean#L10); its proof uses only $G_0$, and the seesaw map is built inside `Osc.nonempty_fockData_iff`. The coefficient record is [ExistsHarmonicCoefficientMapAtWeights.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsHarmonicCoefficientMapAtWeights.lean#L131), with `IoLFRec` in [ThClassPinsRec.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ThClassPinsRec.lean#L45) and `IoLF` in [ThClass.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ThClass.lean#L123). The family of theta vectors is [ExistsThetaVectorFamilyOfCurveDatum.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsThetaVectorFamilyOfCurveDatum.lean#L15); when $N N'$ is odd, its proof sets the vacuum to $0$ (line 25), a value that the conclusion never uses, since it is stated only for even $N$ and $N'$. We have not unfolded `Crv`, `vec22`, `eq22`, `IsChi` or `Iop`. These files are in the folder `IwasawaDecomposition`; no Iwasawa decomposition occurs in them.
