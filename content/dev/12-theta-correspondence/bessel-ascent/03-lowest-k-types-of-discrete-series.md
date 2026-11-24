---
title: Lowest K-types of discrete series
decls:
  - GlobalTheory.InducedPBW.pbw_induced
  - GlobalTheory.T.exists_injective_intertwiner_of_lowest_type
  - GlobalTheory.LowestType.embeds_of_lowest_type
  - GlobalTheory.SphJet.compress_eq
  - GlobalTheory.SphJet.core
  - GlobalTheory.SphJet.of_trivial
  - GlobalTheory.SphJet.of_any
  - GlobalTheory.SphJet.lowest_type_positive_and_decays
  - GlobalTheory.ArchRec.archOnRecord_of_cover
  - GlobalTheory.ArchRec.archOnRecord
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lowest K-types of discrete series

At a real place the ascent works with [discrete series](/learn/representations/#discrete-series) representations of $U(p, q)$ and of its determinant square root cover. This section proves three facts about them. First, an induced $(\mathfrak{g}, K)$-module has a Poincaré-Birkhoff-Witt filtration. Second, a unitary module that contains the lowest $K$-type of a discrete series with the right infinitesimal character contains a copy of every irreducible module with these data. Third, when the Harish-Chandra parameter has large gaps, the matrix coefficients of the lowest $K$-type are nonnegative on the noncompact directions and decay like a Gaussian. The step [the nonempty hypotheses](/step/nonempty-hyps/) uses these facts for the real theta correspondence, and the section ends with the package of archimedean facts that the [seesaw chapter](/entry/arch-on-record-closed/) records.

**Definition 8.3.1 (Real unitary groups and their Lie algebras).** Fix $p, q \ge 0$ and let $I = I_+ \sqcup I_-$ with $|I_+| = p$ and $|I_-| = q$. Two indices are in the *same block* if both are in $I_+$ or both in $I_-$. Let $J$ be the diagonal matrix with entries $1$ on $I_+$ and $-1$ on $I_-$, and let $U(p, q)$ be the group of $g \in GL_I(\mathbb{C})$ with $g^* J g = J$. Its complexified Lie algebra is $\mathfrak{g} = M_I(\mathbb{C})$, with $\mathfrak{k}$ the block diagonal matrices and $\mathfrak{p}$ the matrices with zero diagonal blocks. Let $\mathfrak{p}_\mathbb{R}$ be the real points of $\mathfrak{p}$ in the Lie algebra of $U(p, q)$. Let $E_{ab}$ be the matrix units.

**Definition 8.3.2 (The cover).** A *cover* of $U(p, q)$ is a locally compact group $G$ with a Haar measure, continuous homomorphisms $\mathrm{cov} : G \to U(p, q)$ and $\mathrm{sq} : G \to \mathbb{C}^\times$ with $\mathrm{sq}(x)^2 = \det \mathrm{cov}(x)$, such that $x \mapsto (\mathrm{cov}(x), \mathrm{sq}(x))$ is a topological embedding onto the pairs $(g, w)$ with $w^2 = \det g$, together with an exponential map $\exp$ from the Lie algebra that lifts the matrix exponential and is additive on lines. Its maximal compact subgroup $K$ is the set of $x$ with $\mathrm{cov}(x)$ block diagonal.

A [representation of the real group](/learn/representations/#representations-of-real-groups) is then a unitary representation $\pi$ of $G$ on a Hilbert space. A *discrete series representation* is an irreducible one whose matrix coefficients are square integrable, with $\int_G |\langle y, \pi(g) x \rangle|^2\, dg = \|x\|^2 \|y\|^2 / d_\pi$ for a formal degree $d_\pi > 0$. It comes with its $(\mathfrak{g}, K)$-module: the space of $K$-finite vectors, with the derived action of $\mathfrak{g}$.

**Definition 8.3.3 (Parameters).** A *Harish-Chandra parameter* is a map $\lambda : I \to \mathbb{Q}$ that is injective, strictly decreasing on each block in the fixed order, with $2\lambda(a) \in \mathbb{Z}$ and $\lambda(a) - \lambda(b) \in \mathbb{Z}$ for all $a, b$. For $a \in I$ put
$$\rho_n(a) = \tfrac12\bigl(\#\{b \notin \text{block}(a) : \lambda_b < \lambda_a\} - \#\{b \notin \text{block}(a) : \lambda_b > \lambda_a\}\bigr),$$
and $\rho_c(a)$ in the same way with $b$ in the block of $a$. The *Blattner parameter* is $\Lambda = \lambda + \rho_n - \rho_c$. The parameter has *gap* at least $h$ if $|\lambda_a - \lambda_b| \ge h$ whenever $a$ and $b$ lie in different blocks. The *Casimir* of a $(\mathfrak{g}, K)$-module is $\Omega = \sum_{a, b} E_{ab} E_{ba}$.

A vector $v$ is a *highest weight vector* of weight $\mu$ if $v \neq 0$, $E_{aa} v = \mu_a v$ for all $a$, and $E_{ab} v = 0$ for $a < b$ in the same block. The [highest weight theory](/learn/representations/#highest-weights-and-branching) of $K = U(p) \times U(q)$ describes the $K$-types by such weights. Harish-Chandra's theorem and the Blattner formula say that the discrete series with parameter $\lambda$ contains the $K$-type $\Lambda$ once, its Casimir acts by $\|\lambda\|^2 - \|\rho\|^2$ with $\|\rho\|^2 = \sum_{i < p+q} (\frac{p+q-1}{2} - i)^2$, and every highest weight of a $K$-type is $\Lambda$ plus a sum of positive noncompact roots $e_a - e_b$ with $\lambda_a > \lambda_b$.

### The PBW filtration of an induced module

Let $V$ be a vector space with a Lie action of $\mathfrak{k}$. The *induced module* is $\operatorname{Ind} V = U(\mathfrak{g}) \otimes_{U(\mathfrak{k})} V$. Let $F_k$ be the span of the images of $u \otimes v$ with $u$ a product of at most $k$ elements of $\mathfrak{g}$, and $F_{<k} = \sum_{j < k} F_j$. The *symmetrisation* sends a monomial in the coordinates $E_{ab}$ of $\mathfrak{p}$, $a$ and $b$ in different blocks, to the average of the products of the $E_{ab}$ over all orders.

**Theorem 8.3.4 (PBW for induced modules).** Let $V$ carry a Lie action of $\mathfrak{k}$. Then $\bigcup_k F_k = \operatorname{Ind} V$, and for each $k$, with $\sigma$ the symmetrisation applied to the homogeneous polynomials of degree $k$ on $\mathfrak{p}$ tensored with $V$:

1. $F_k = F_{<k} + \sigma(S^k(\mathfrak{p}) \otimes V)$;
2. if $\sigma(z) \in F_{<k}$ for $z \in S^k(\mathfrak{p}) \otimes V$, then $z = 0$;
3. for $Y \in \mathfrak{k}$, $\sigma(Y \cdot z) - Y \sigma(z) \in F_{<k}$, where $Y$ acts on $S^k(\mathfrak{p}) \otimes V$ by the adjoint action on the first factor and by the given action on the second.

Lean: `GlobalTheory.InducedPBW.pbw_induced`.

*Proof.* The filtration exhausts $\operatorname{Ind} V$ because $U(\mathfrak{g})$ is spanned by products. For part 1, write a product of $k$ elements as a product of elements of $\mathfrak{p}$ and $\mathfrak{k}$; the elements of $\mathfrak{k}$ move to the right past $\mathfrak{p}$ at the cost of commutators, which lower the degree, and then act on $V$. Reordering the remaining product of $\mathfrak{p}$ elements also costs only lower terms, so it equals its symmetrisation modulo $F_{<k}$. For part 2, the Lie action of $\mathfrak{k}$ on $V$ extends to a representation of $\mathfrak{gl}$-type on a model, which gives a symbol map from $\operatorname{Ind} V$ to the polynomials on $\mathfrak{p}$ tensored with $V$. It kills $F_{<k}$ in degree $k$ and is the identity on $\sigma(S^k(\mathfrak{p}) \otimes V)$. For part 3, the commutator of $Y$ with a symmetrised product is the symmetrised product with $[Y, E_{ab}]$ inserted, and the two differ by lower terms. $\square$

### Embeddings from the lowest K-type

**Theorem 8.3.5 (Embedding from a lowest K-type).** Assume the PBW statement of the Theorem above, and assume that for finite-dimensional $\mathfrak{k}$-modules $V_1$, $V_2$ with $V_1$ irreducible of highest weight $\mu$ and $V_2$ a sum of weight spaces, every highest weight of $V_1 \otimes V_2$ is $\mu + w$ for a weight $w$ of $V_2$. Let $\lambda$ be a Harish-Chandra parameter with gap greater than $(p + q)^3$. Let $A$ and $B$ be unitary $(\mathfrak{g}, K)$-modules with highest weight vectors $u \in A$ and $v \in B$ of weight $\Lambda$, with
$$\Omega u = (\|\lambda\|^2 - \|\rho\|^2) u, \qquad \Omega v = (\|\lambda\|^2 - \|\rho\|^2) v,$$
and with $B$ irreducible. Then there is an injective $\mathfrak{g}$-map $e : B \to A$ with $e(v) = u$.

Lean: `GlobalTheory.T.exists_injective_intertwiner_of_lowest_type` (also `GlobalTheory.LowestType.embeds_of_lowest_type`, the proof).

*Proof.* A gap greater than $(p + q)^3$ gives a gap greater than $(p + q)^3 / 24 + 1$ and a gap greater than $p + q - 1$. With these two gaps, two highest weight vectors of weight $\Lambda$ with the same Casimir eigenvalue in unitary modules generate isomorphic submodules, and when $B$ is irreducible the isomorphism is an injective map from $B$ that sends $v$ to $u$. The proof of that statement maps the induced module $\operatorname{Ind}(\text{the } K\text{-type } \Lambda)$ onto both submodules. The PBW filtration and the tensor product rule bound the $K$-types of the kernel, and the gap together with the Casimir eigenvalue shows that the two kernels agree. $\square$

### Positivity and decay of lowest K-type coefficients

Let $\pi$ be a discrete series representation of the cover with parameter $\lambda$, and let $H_\Lambda$ be the set of images of the vectors of the $(\mathfrak{g}, K)$-module that lie in a finite-dimensional $K$-stable subspace all of whose highest weights equal $\Lambda$. These are the vectors of the lowest $K$-type. For $Y \in M_I(\mathbb{C})$ let $\|Y\|$ be the Hilbert-Schmidt norm.

**Lemma 8.3.6 (Compression to the K-type).** Let $\tau$ be a holomorphic model of the lowest $K$-type on a finite-dimensional space $W$, extended to the complexified group, with a unit vector $w$ of weight $-\Lambda$ fixed by the lower unipotent matrices. Let $\Psi(z)$ be the operator on $W$ given by
$$\Psi(z) = \dim W \int_K \Phi_\lambda(k^{-1} z k)\, \langle \cdot, \tau(k) w \rangle\, \tau(k) w\, dk,$$
where $\Phi_\lambda$ is the product of powers of leading minors attached to $\lambda$. Let $j : W \to H$ be the isometry onto the lowest $K$-type. If the gap is at least $2(p+q) + 1$ and no $K$-type $\Lambda - (e_a - e_b)$ with $a < b$ in different blocks occurs, then for $X \in \mathfrak{p}_\mathbb{R}$ and $x, y \in W$,
$$\langle j y, \pi(\exp X)\, j x \rangle = \langle y, \Psi(\exp X^{\mathsf T})\, x \rangle.$$

Lean: `GlobalTheory.SphJet.compress_eq`.

*Proof.* The function $\Psi$ is analytic near the positive matrices. Its jets at $1$ satisfy the Schmid system of first-order equations that the lowest $K$-type of $\pi$ satisfies, and the compressed words in the Lie algebra satisfy the same relations because no lower $K$-type occurs. The difference of the two systems is nilpotent under the gap condition, so the two jets agree at $1$. A unitary flow $t \mapsto \pi(\exp tX)$ is determined by its Taylor series on analytic vectors, so the two analytic functions of $t$ agree for all $t$. On $\mathfrak{p}$ the involution of the Lie algebra is the transpose. $\square$

**Proposition 8.3.7 (Positivity and decay of the compressed coefficient).** Under the hypotheses of the Lemma and a gap at least $h$, for $X \in \mathfrak{p}_\mathbb{R}$ and $x, y$ in the lowest $K$-type,
$$\langle x, \pi(\exp X) x \rangle \ge 0, \qquad |\langle y, \pi(\exp X) x \rangle| \le d_h(\|X\|)\, \|x\|\, \|y\|,$$
where $d_h(t) = \exp\bigl(-\frac h8 \min(t^2, t / \sqrt{2r})\bigr)$ and $r = \min(p, q)$.

Lean: `GlobalTheory.SphJet.core`.

*Proof.* A holomorphic model $\tau$ of the $K$-type exists by the analytic continuation of the $K$-action. By the [Lemma 8.3.6](/entry/compress-eq/) the coefficient is $\langle y, \Psi(\exp X^{\mathsf T}) x \rangle$. The averaged minor operator $\Psi(z)$ is positive at positive matrices $z$ and has operator norm at most $d_h(\|X\|)$ at $z = \exp X^{\mathsf T}$, since $\Phi_\lambda$ is a product of minors whose exponents grow with the gap. $\square$

**Theorem 8.3.8 (Lowest K-type coefficients of a discrete series).** Let $\pi$ be a discrete series representation of the cover with parameter $\lambda$, and assume that its $K$-type $\Lambda$ has multiplicity one and that every highest weight of its $(\mathfrak{g}, K)$-module is $\Lambda + \sum m_{ab} (e_a - e_b)$ with $m_{ab} \in \mathbb{N}$ nonzero only when $\lambda_b < \lambda_a$. Let the gap be at least $h$ and at least $2(p + q) + 1$. Then for $Y \in \mathfrak{p}_\mathbb{R}$, $x, y \in H_\Lambda$ and $k \in K$,
$$\langle x, \pi(\exp Y) x \rangle \ge 0, \qquad |\langle y, \pi(k \exp Y) x \rangle| \le d_h(\|Y\|)\, \|x\|\, \|y\|.$$

Lean: `GlobalTheory.SphJet.of_any` (also `GlobalTheory.SphJet.of_trivial`, the case where the kernel of the cover acts trivially).

*Proof.* Either the kernel of $\mathrm{cov}$ acts trivially, or $\pi$ is a twist by $\mathrm{sq}^{-1}$ of a representation where it does. In the first case $\pi$ is a representation of $U(p, q)$. The lowest $K$-type spans a finite-dimensional space with a highest weight vector, the hypothesis on highest weights excludes the $K$-types $\Lambda - (e_a - e_b)$, and the [Proposition 8.3.7](/entry/sph-jet-core/) gives the bounds; the factor $k$ is unitary on the $K$-type. In the second case replace $\lambda$ by $\lambda - \frac12$. This is again a parameter with the same gaps, its Blattner parameter is $\Lambda - \frac12$, and the twist moves the $K$-types by $-\frac12$. The first case applies to the twist. Since $\mathrm{sq}(\exp Y) = 1$ for $Y \in \mathfrak{p}_\mathbb{R}$ and $|\mathrm{sq}| = 1$, the twist does not change the two bounds. $\square$

**Theorem 8.3.9 (Positivity of discrete series).** Let a family of covers, Fock models and discrete series $\pi_\lambda$ be given, and assume the Blattner properties: the $K$-type $\Lambda$ has multiplicity one in $\pi_\lambda$, the Casimir acts by $\|\lambda\|^2 - \|\rho\|^2$, and every highest weight is $\Lambda$ plus a positive combination of the roots $e_a - e_b$ with $\lambda_a > \lambda_b$. Then for every parameter $\lambda$ with gap at least $h$ and
$$h \ge 120\,(p + q) \min(p, q)^{3/2},$$
every $Y \in \mathfrak{p}_\mathbb{R}$, every $k \in K$ and all $x, y$ in the $K$-type $\Lambda$ of $\pi_\lambda$: the number $\langle x, \pi_\lambda(\exp Y) x \rangle$ is real and nonnegative, and $|\langle y, \pi_\lambda(k \exp Y) x \rangle| \le d_h(\|Y\|)\, \|x\|\, \|y\|$.

Lean: `GlobalTheory.SphJet.lowest_type_positive_and_decays`.

*Proof.* If two indices lie in different blocks then $p, q \ge 1$, so $\min(p, q)^{3/2} \ge 1$ and $p + q \ge 1$, and the bound on $h$ gives a gap at least $2(p+q) + 1$. Now apply the [Theorem 8.3.8](/entry/of-any/). $\square$

### The archimedean facts on record

**Theorem 8.3.10 (Archimedean facts for the chain).** Assume the classification of discrete series of the covers by Harish-Chandra parameters with the Blattner properties, and the theory of Harish-Chandra modules: two unitary representations whose $(\mathfrak{g}, K)$-modules are isomorphic are unitarily equivalent, and a unitary representation with an admissible irreducible $(\mathfrak{g}, K)$-module is irreducible. Then the archimedean facts used by the chain hold for every global datum: the real theta lifts along the chain and the pair have no lower occurrence, and when the parameters have the required gaps they reach the expected discrete series, their zeta integrals do not vanish, the real theta maps of the chain compose as expected, and the lowest $K$-type maps to the Fock model exist, are unique and are harmonic.

Lean: `GlobalTheory.ArchRec.archOnRecord` (also `GlobalTheory.ArchRec.archOnRecord_of_cover`, the form with a chosen family).

*Proof.* The two hypotheses give a family of covers and discrete series with the Blattner properties, admissible Harish-Chandra modules, and two archimedean Rallis statements: the first occurrence and the up and down law along a line. They also show that the theta models are discrete series of the cover. For this family the statements without a gap follow from the absence of lower $K$-types in the joint harmonics. The statements under the gap follow from the up and down law, from the uniform real theta intertwiners of the chain step and their proportionality, and from the existence, uniqueness and harmonicity of the lowest $K$-type maps to the Fock model. $\square$

**Remark 8.3.11 (Formalization).** The Blattner properties, positivity, and the two auxiliary module statements are Prop-valued definitions in [SchurIrreducible.lean](lean:Formalism/SharpRestriction/Divisibility/SchurIrreducible.lean#L74). The positivity theorem takes two further hypotheses on admissibility and the two module statements, and does not use them ([LowestTypePositiveAndDecays.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/LowestTypePositiveAndDecays.lean#L579)). The form with a chosen family takes a family $X$ and two Rallis hypotheses for it, but its proof discards them and uses a new family from the literature hypotheses ([DiscreteSeriesHarishChandraModuleAdmissible.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/DiscreteSeriesHarishChandraModuleAdmissible.lean#L499)). The archimedean facts for the chain are a conjunction of seven definitions, which we describe but do not unfold. The operator $\Psi$, the minor function $\Phi_\lambda$ and the decay of $\Psi$ are used through their statements.
