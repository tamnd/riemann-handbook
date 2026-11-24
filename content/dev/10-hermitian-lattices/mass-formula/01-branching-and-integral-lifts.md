---
title: Branching maps between Weyl modules
decls:
  - PI.WGL.gTLower_of
  - PI.WGL.liftMod_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Branching maps between Weyl modules

The local factors of the mass formula and the bounds for orbital integrals need explicit vectors in the representations of $\mathrm{GL}_N$ and $U(N)$, with integral coordinates and with a bound on their norms. This section constructs, for a weight $\lambda$ of $\mathrm{GL}_N$ and a weight $\sigma$ of $\mathrm{GL}_{N-1}$ that interlaces it, an equivariant map from the module of $\sigma$ into the module of $\lambda$ and a map back. Both maps are integral, both are adjoint for the Fock pairing, and both have an explicit norm bound. The result is the theorem on [Gelfand-Tsetlin lowering](/entry/g-tlower-of/) of the chapter on orbital bounds, which feeds the bounds for branching coefficients.

### Weyl modules in the polynomial ring

Let $N \geq 1$ and let $R$ be a commutative ring. Let $R[X]$ be the polynomial ring in the $N^2$ variables $x_{ij}$, $0 \leq i, j < N$ (see [polynomials](/learn/algebra/#polynomials-and-power-series)). A *dominant weight* of length $N$ is a sequence $\lambda = (\lambda_0 \geq \lambda_1 \geq \dots \geq \lambda_{N-1})$ of integers. Put $d(\lambda) = \lambda_{N-1}$, $\nu = \lambda - d(\lambda) \in \mathbb{Z}_{\geq 0}^N$, and $s(\lambda) = \lambda_0 - \lambda_{N-1} + N$, the *spread* of $\lambda$.

**Definition 7.1.1 (The modules $\nabla$ and $\Delta$).** The *dual Weyl module* $\nabla_R(\lambda) \subseteq R[X]$ is the set of polynomials $f$ that are homogeneous of degree $\nu_j$ in the entries of column $j$ for each $j$, and that are invariant under each substitution that adds $t$ times column $l$ to column $j$, for $l < j$ and $t \in R$. The *extremal vector* is
$$e_\lambda = \prod_{s=0}^{N-1} \Delta_{s+1}^{\nu_s - \nu_{s+1}}, \qquad \nu_N = 0,$$
where $\Delta_k$ is the leading principal $k \times k$ minor of $X$. The *Weyl module* $\Delta_R(\lambda)$ is the $R$-span of the vectors obtained from $e_\lambda$ by the divided powers of the row operators $x_{bj}\,\partial / \partial x_{aj}$ (summed over $j$).

The group $\mathrm{GL}_N(R)$ acts on $R[X]$ by
$$(g \cdot f)(X) = \det(g)^{d(\lambda)} f(g^{\mathsf T} X).$$
Over $\mathbb{C}$ the module $\nabla_{\mathbb{C}}(\lambda)$ is the irreducible representation of highest weight $\lambda$, realized in the coordinate ring of matrices (see [highest weights and branching](/learn/representations/#highest-weights-and-branching)). The modules over $\mathbb{Z}$ are the two natural lattices in it, and the theorem below is about these lattices.

**Definition 7.1.2 (Fock pairing).** For $f = \sum_m f_m x^m$ and $g = \sum_m g_m x^m$ in $\mathbb{C}[X]$ put
$$F(f, g) = \sum_m f_m \overline{g_m} \prod_{k} m_k!, \qquad \langle f, g \rangle_\lambda = \frac{F(f, g)}{F(e_\lambda, e_\lambda)}.$$

The monomials are orthogonal, and $\langle e_\lambda, e_\lambda \rangle_\lambda = 1$. The pairing $F$ is the inner product of the Fock space, for which the operators $\partial / \partial x$ and multiplication by $x$ are adjoint. The analogous pairing over $\mathbb{Q}$ is written the same way.

### Interlacing and the branching data

Let $n + 1 = N$. A dominant weight $\sigma$ of length $n$ *interlaces* $\lambda$ if $\lambda_{i+1} \leq \sigma_i \leq \lambda_i$ for all $i < n$. Embed $\mathrm{GL}_n$ in $\mathrm{GL}_N$ by $g \mapsto \mathrm{diag}(g, 1)$, and let $t(a) = \mathrm{diag}(1, \dots, 1, a)$ be the last diagonal torus. For interlacing $\lambda$ and $\sigma$ define:

- $D_0 = \sum_{i<n} (\sigma_i - \lambda_{i+1})$ and $D_1 = \sum_{i<n} \min(\lambda_i - \lambda_{i+1}, D_0)$;
- the integer interval $R_i = [\lambda_{i+1}, \min(\lambda_i, \lambda_{i+1} + D_0)]$;
- the integer $c(\lambda, \sigma) = \prod_{i<n} \prod_{v \in R_i \setminus \{\sigma_i\}} \prod_{j<n} \big((v - i) - (\sigma_j - j)\big)$;
- the polynomial $\xi = \prod_{i<n} \Delta_{i+1}^{\sigma_i - \lambda_{i+1}} M_i^{\lambda_i - \sigma_i}$, where $M_i$ is the minor of $X$ on the rows $0, \dots, i-1, N-1$ and the first $i + 1$ columns;
- the bounds $C = (2 s(\lambda))^{N D_1}$ and $B = C \sqrt{\dim_{\mathbb{C}} \Delta_{\mathbb{C}}(\lambda)}$;
- the degree $\deg = \sum_i \lambda_i - \sum_i \sigma_i$.

The vector $\xi$ is the classical highest weight vector of the copy of $\sigma$ inside $\lambda$: the minors $\Delta_{i+1}$ carry the weight $\lambda_{i+1}$ and the minors $M_i$, which use the last row, carry the rest. The integer $c$ is the scalar by which a Capelli type operator acts on that copy; it is nonzero because $v \neq \sigma_i$ in each factor.

### The theorem

We take four facts on Weyl modules as given. Each is proved elsewhere in the development, and the [theorem](/entry/g-tlower-of/) of the chapter on orbital bounds that uses the result below supplies them.

**Theorem 7.1.3 (Integral duality).** Let $f \in \nabla_{\mathbb{Q}}(\lambda)$. Then $\langle f, g \rangle_\lambda \in \mathbb{Z}$ for all $g \in \nabla_{\mathbb{Z}}(\lambda)$ if and only if $f$ is the image of an element of $\Delta_{\mathbb{Z}}(\lambda)$.

**Theorem 7.1.4 (Highest weight).** For every dominant $\lambda$: $\nabla_{\mathbb{C}}(\lambda) = \Delta_{\mathbb{C}}(\lambda)$; the only $\mathrm{GL}_N(\mathbb{C})$-stable subspaces of $\nabla_{\mathbb{C}}(\lambda)$ are $0$ and $\nabla_{\mathbb{C}}(\lambda)$; and every $f \in \nabla_{\mathbb{C}}(\lambda)$ fixed by the upper unitriangular matrices is a multiple of $e_\lambda$.

**Theorem 7.1.5 (Gelfand-Tsetlin branching).** Let $n + 1 = N$ and $\lambda$ dominant of length $N$. (a) Let $\mu$ be dominant of length $n$ and let $\varphi, \varphi'$ be linear maps that send $\nabla_{\mathbb{C}}(\mu)$ into $\nabla_{\mathbb{C}}(\lambda)$ and commute with the action of $\mathrm{GL}_n(\mathbb{C})$. If $\varphi' \neq 0$ on $\nabla_{\mathbb{C}}(\mu)$, then $\mu$ interlaces $\lambda$ and $\varphi = c \varphi'$ on $\nabla_{\mathbb{C}}(\mu)$ for some $c \in \mathbb{C}$. (b) $\nabla_{\mathbb{C}}(\lambda)$ is the sum of the images $\varphi(\nabla_{\mathbb{C}}(\mu))$ over all interlacing $\mu$ and all such $\varphi$.

**Theorem 7.1.6 (Schur bound).** If $s \in \nabla_{\mathbb{C}}(\lambda)$ and $|s(x)| \leq 1$ for all $x \in U(N)$, then $\langle s, s \rangle_\lambda \leq \dim \Delta_{\mathbb{C}}(\lambda)$.

Part (a) and (b) are the branching law of Weyl and of Gelfand and Tsetlin: the restriction of the representation $\lambda$ of $\mathrm{GL}_N$ to $\mathrm{GL}_{N-1}$ is the direct sum of the representations $\mu$ that interlace $\lambda$, each once.

**Theorem 7.1.7 (Gelfand-Tsetlin lowering).** Let $n + 1 = N$, let $\lambda$ be dominant of length $N$ and $\sigma$ dominant of length $n$, and let $\sigma$ interlace $\lambda$. Assume the four theorems above. Then $c(\lambda, \sigma) \neq 0$, $|c(\lambda, \sigma)| \leq C$, $\xi \neq 0$ and $\deg = \lambda_0 - D_0$. There are $\mathbb{C}$-linear maps $\iota : \mathbb{C}[X_n] \to \mathbb{C}[X_N]$ and $\beta : \mathbb{C}[X_N] \to \mathbb{C}[X_n]$ with the following properties.

1. $\iota$ maps $\nabla_{\mathbb{C}}(\sigma)$ into $\nabla_{\mathbb{C}}(\lambda)$ and $\nabla_{\mathbb{Z}}(\sigma)$ into $\nabla_{\mathbb{Z}}(\lambda)$; it satisfies $\iota(g \cdot s) = \mathrm{diag}(g, 1) \cdot \iota(s)$ and $t(a) \cdot \iota(s) = a^{\deg} \iota(s)$ for $s \in \nabla_{\mathbb{C}}(\sigma)$; it sends $e_\sigma$ to $c(\lambda, \sigma) \xi$; and $\operatorname{Re} \langle \iota s, \iota s \rangle_\lambda \leq B^2 \operatorname{Re} \langle s, s \rangle_\sigma$.
2. $\beta$ maps $\Delta_{\mathbb{C}}(\lambda)$ into $\Delta_{\mathbb{C}}(\sigma)$ and $\Delta_{\mathbb{Z}}(\lambda)$ into $\Delta_{\mathbb{Z}}(\sigma)$; it is not zero on $\Delta_{\mathbb{C}}(\lambda)$; it satisfies $\beta(\mathrm{diag}(g, 1) \cdot f) = g \cdot \beta(f)$ and $\beta(t(a) \cdot f) = a^{\deg} \beta(f)$; and $\operatorname{Re} \langle \beta f, \beta f \rangle_\sigma \leq B^2 \operatorname{Re} \langle f, f \rangle_\lambda$.
3. $\langle \iota s, f \rangle_\lambda = \langle s, \beta f \rangle_\sigma$ for $s \in \nabla_{\mathbb{C}}(\sigma)$ and $f \in \Delta_{\mathbb{C}}(\lambda)$.

Lean: `PI.WGL.gTLower_of`.

The key step is the integrality of $\iota$. It rests on a lemma that lifts integral vectors modulo the other branching components. For $\lambda$ and $\sigma$ as above let $O(\lambda, \sigma) \subseteq \mathbb{C}[X_N]$ be the sum of the images $\varphi(\nabla_{\mathbb{C}}(\mu))$ over the dominant $\mu \neq \sigma$ that interlace $\lambda$ with $\sum \mu = \sum \sigma$, and over the equivariant maps $\varphi$ from $\nabla_{\mathbb{C}}(\mu)$ into $\nabla_{\mathbb{C}}(\lambda)$.

**Lemma 7.1.8 (Integral lift modulo the other components).** Assume the highest weight theorem and the branching theorem. Let $\sigma$ interlace $\lambda$, and let $\iota_0$ be a linear map that sends $\nabla_{\mathbb{C}}(\sigma)$ equivariantly into $\nabla_{\mathbb{C}}(\lambda)$, with $\iota_0(e_\sigma) = \xi$, and on which the last torus acts by $a^{\deg}$. Then for every $s \in \nabla_{\mathbb{Z}}(\sigma)$ there is $m \in \nabla_{\mathbb{Z}}(\lambda)$ with $m - \iota_0(s) \in O(\lambda, \sigma)$.

Lean: `PI.WGL.liftMod_of`.

*Proof.* We use two facts on the operator of Capelli type. There is an operator $Z$ on $\mathbb{C}[X_N]$ that maps $\nabla_{\mathbb{Z}}(\lambda)$ into itself and acts on each image $\varphi(\nabla_{\mathbb{C}}(\mu))$ by the integer $z(\mu)$, the product that defines $c(\lambda, \sigma)$ with $\mu_j$ in place of $\sigma_j$. So $z(\sigma) = c(\lambda, \sigma)$, and $z(\mu) = 0$ when $\mu \neq \sigma$ and $\sum \mu = \sum \sigma$. Hence $Z$ kills $O(\lambda, \sigma)$ and acts on $\iota_0(\nabla(\sigma))$ by $c = c(\lambda, \sigma) \neq 0$. By part (b) of the branching theorem, each $f \in \nabla_{\mathbb{C}}(\lambda)$ of the right weight for the last torus is $\iota_0(u) + o$ with $u \in \nabla_{\mathbb{C}}(\sigma)$ and $o \in O(\lambda, \sigma)$ (part (a) makes the $\sigma$ component a multiple of $\iota_0$). Then $Z f = c\, \iota_0(u)$. So an element $f$ of this weight with $Z f = c\, \iota_0(s)$ satisfies $f - \iota_0(s) \in O(\lambda, \sigma)$. Next, the equivariant map $\iota_0$ commutes with the divided powers of the row operators of $\mathrm{GL}_n$, read as row operators of $\mathrm{GL}_N$, and so does $Z$. The lattice $\nabla_{\mathbb{Z}}(\sigma)$ is spanned by divided powers of row operators applied to products of minors. For a product of minors the lift $m$ is written down from minors of $X_N$, and the Fock pairing detects that it lies in the right component (this uses the highest weight theorem). Applying the same row operators to $m$ gives the lift of a general generator, and sums of lifts are lifts. $\square$

*Proof of the theorem.* The facts on $c(\lambda, \sigma)$, $C$, $\deg$ and $\xi$ are direct estimates on the integers and minors that define them. By the highest weight theorem and part (a) of the branching theorem, there is an equivariant $\iota_0$ from $\nabla_{\mathbb{C}}(\sigma)$ into $\nabla_{\mathbb{C}}(\lambda)$ with $\iota_0(e_\sigma) = \xi$: the vector $\xi$ is fixed by the upper unitriangular group of $\mathrm{GL}_n$ and has weight $\sigma$, so it generates a copy of $\nabla(\sigma)$. Put $\iota = c\, \iota_0$. For $s \in \nabla_{\mathbb{Z}}(\sigma)$ the lemma gives $m \in \nabla_{\mathbb{Z}}(\lambda)$ with $m - \iota_0(s) \in O(\lambda, \sigma)$. Apply $Z$: since $Z$ kills $O(\lambda, \sigma)$, $Z m = c\, \iota_0(s) = \iota(s)$, and $Z m$ is integral. So $\iota$ is integral. Let $\beta$ be the adjoint of $\iota$ for the Fock pairings; it is equivariant and nonzero, and by irreducibility $\beta \circ \iota$ is a scalar on $\nabla(\sigma)$. The scalar is computed on $e_\sigma$, and the Schur bound applied to $\xi$, which is bounded by $1$ on $U(N)$ as a product of minors of a unitary matrix, gives the bounds with $B^2$. Integral duality and the highest weight theorem give the integrality of $\beta$: for $f \in \Delta_{\mathbb{Z}}(\lambda)$ and $s \in \nabla_{\mathbb{Z}}(\sigma)$, $\langle \beta f, s \rangle = \overline{\langle \iota s, f \rangle}$ is an integer, because $\iota s$ is integral. $\square$

**Remark 7.1.9 (Formalization).** The theorem has the same short name as its caller in the chapter on orbital bounds, which fills in the four hypotheses. The arithmetic facts, the existence of $\iota_0$, the operator $Z$ and the vanishing of $z(\mu)$ are proved lemmas that the proof cites; we did not unfold the integrality of $\beta$ and the adjoint construction beyond the statements. In the lift lemma the hypothesis on the weight of the last torus is not used: it is bound as `_hW` in [LiftAsm.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/GelfandTsetlinLowering/LiftAsm.lean#L131). The two theorems are in [GTLowerOf.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/GelfandTsetlinLowering/GTLowerOf.lean#L14) and [ConstructionLift.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/GelfandTsetlinLowering/ConstructionLift.lean#L15).
