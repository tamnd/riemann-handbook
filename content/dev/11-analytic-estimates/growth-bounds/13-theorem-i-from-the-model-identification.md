---
title: Theorem I from the model identification
decls:
  - Formalism.MainNotions.flipOneThree.Pf.oneTop_abs
  - Formalism.MainNotions.flipOneThree.Pf.single_weight_of_model_identification
  - Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_model_identification
  - Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_explicit_minor_map
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem I from the model identification

Section 12 reduced the closed form of Theorem I to the lattice functor comparison and the cloud maps statement, in [the Theorem (Theorem I from the lattice functor comparison)](/entry/theorem-i-of-lattice-functor-comparison/). This section reduces the lattice functor comparison to a model of the two-letter spaces by bihomogeneous polynomials in two sets of variables, and then to an explicit map built from minors. The step between them is a decomposition of bihomogeneous polynomials into harmonic parts with an explicit bound on the denominators, which we prove. Section 14 proves the explicit minor map statement and the cloud maps statement. We keep the notation of Section 12: the setting $R$, the lattices $H^0(\omega, \Lambda)$, $\lambda_a = \log_p(8a + m) + 1$ and the closed form of Theorem I.

### Harmonic parts with denominators

Let $K$ be a field of characteristic $0$ and $k \geq 1$. Let $\mathrm{Pol}_{A,B}$ be the space of polynomials in $x_1, \dots, x_k, y_1, \dots, y_k$ of degree $A$ in $x$ and $B$ in $y$, let $h = \sum_ix_iy_i$ and $\Delta = \sum_i\partial^2/\partial x_i\partial y_i$. On $\mathrm{Pol}_{A,B}$ one has $\Delta h - h\Delta = A + B + k$. The *harmonic* polynomials $\mathrm{Har}_{A,B}$ are the kernel of $\Delta$, and
$$\mathrm{Pol}_{A,B} = \bigoplus_{j \leq \min(A,B)}h^j\,\mathrm{Har}_{A-j,B-j}.$$
For a subring $\mathcal{O}_v$ of $K$, the *Gauss lattice* is the set of polynomials with coefficients in $\mathcal{O}_v$, and $\mathrm{GL}_k(K)$ acts on it by linear substitution in $x$ and the contragredient substitution in $y$.

**Lemma 5.13.1 (Harmonic decomposition with denominators).** Let $p$ be prime and $\mathcal{O}_v$ a valuation subring of $K$ in which every integer prime to $p$ is a unit. Let $V$ be a $K$-space with an isomorphism $\alpha : V \to \mathrm{Pol}_{P,Q}$, and for each $j$ let $\beta_j$ be a surjection of $\mathrm{Pol}_{P-j,Q-j}$ onto a space $W_j$ with kernel $h\,\mathrm{Pol}_{P-j-1,Q-j-1}$. Put $e = (k + 1)\lfloor\log_p(P + Q + k)\rfloor$. Then there are linear maps $\iota_j : W_j \to V$ and $\pi_j : V \to W_j$ with $\sum_{j \leq \min(P,Q)}\iota_j\pi_j = \mathrm{id}$, such that for every $g \in \mathrm{GL}_k(K)$ and $j \leq \min(P, Q)$:

1. if $\alpha(x)$ lies in $g$ times the Gauss lattice, then $p^e\pi_j(x) = \beta_j(f)$ for some $f \in \mathrm{Pol}_{P-j,Q-j}$ in $g$ times the Gauss lattice;
2. if $f$ lies in $g$ times the Gauss lattice, so does $\alpha(p^e\iota_j\beta_j(f))$.

Lean: `Formalism.MainNotions.flipOneThree.Pf.oneTop_abs`.

*Proof.* The level projection onto $h^j\mathrm{Har}_{P-j,Q-j}$ is $F \mapsto h^jD_jF$ with
$$D_j = \Big(\binom{P + Q + k - j - 1}{j}\,(j!)^2\Big)^{-1}H_{P-j,Q-j}\,\Delta^j,$$
where $H$ is the harmonic projection; this is how the level projections are built from $H$ and $\Delta$, and they sum to the identity on $\mathrm{Pol}_{P,Q}$. Put $\pi_j = \beta_j D_j\alpha$ and $\iota_j(\beta_j f) = \alpha^{-1}(h^jH f)$; this is well defined because $H$ kills $h\,\mathrm{Pol}$, and $\sum_j\iota_j\pi_j = \mathrm{id}$ is the decomposition above. Three facts on the Gauss lattice, which we use as proved results on bihomogeneous polynomials, give the integrality. First, the Gauss projection bound: if $F \in \mathrm{Pol}_{A,B}$ lies in $g$ times the Gauss lattice, so do $p^{(k+1)\lfloor\log_p(A + B + k)\rfloor}H F$ and $p^{(k+1)\lfloor\log_p(A + B + k)\rfloor}$ times each level projection of $F$; here one uses that integers prime to $p$ are units in $\mathcal{O}_v$. Second, the Gauss lemma for $h$: if $h^jG$ lies in $g$ times the Gauss lattice, so does $G$. Third, the level lattice: the elements of $h^j\mathrm{Har}_{a,b}$ in $g$ times the Gauss lattice are $h^j$ times the harmonic polynomials in that lattice. For the first claim, the level projection of $\alpha(x)$ is $h^jD_j\alpha(x)$; scaled by $p^e$ it lies in the lattice, so $f = p^eD_j\alpha(x)$ lies in it by the Gauss lemma, and $\beta_j(f) = p^e\pi_j(x)$. For the second claim, $p^eHf$ lies in the lattice by the Gauss projection bound at $(P - j, Q - j)$, whose exponent is at most $e$, and multiplication by $h^j$ keeps it there. $\square$

### The model of the two-letter spaces

For $P, Q \geq 0$ the *two-letter space* $\mathrm{Two}(P, Q)$ is the tensor product of the dual Weyl modules of a vector letter of degree $P$ and a covector letter of degree $Q$, in two sets of $(m + 1) \times (m + 1)$ matrix variables; for a lattice $\Lambda$ its integral form $\mathrm{Two}_\Lambda(P, Q)$ is the tensor product of the lattices $H^0(\mathcal{O}, \cdot, \Lambda)$. Let $S_{a,b}$ be the dual Weyl module of the weight $\omega_{a,b} = (a, 0, \dots, 0, -b)$.

**Definition 5.13.2 (Two-letter model identification).** The *two-letter model identification* holds if for every setting and $m \geq 2$ there are isomorphisms $\alpha_{P,Q} : \mathrm{Two}(P, Q) \to \mathrm{Pol}_{P,Q}$ (with $k = m + 1$) and surjections $\beta_{a,b} : \mathrm{Pol}_{a,b} \to S_{a,b}$ with kernel $h\,\mathrm{Pol}_{a-1,b-1}$, such that every lattice $\Lambda$ has some $g' \in \mathrm{GL}_{m+1}(K)$ for which $\mathrm{Two}_\Lambda(P, Q)$ is the inverse image under $\alpha$ of $g'$ times the Gauss lattice over $\mathcal{O}$, and $H^0(\omega_{a,b}, \Lambda)$ is the image under $\beta$ of $\mathrm{Pol}_{a,b}$ intersected with $g'$ times the Gauss lattice.

**Proposition 5.13.3 (Single weight comparison).** Assume the two-letter model identification. Then for every setting, $m \geq 2$ and $P + Q + 1 \leq 8a$ there are maps $\iota_j : S_{P-j,Q-j} \to \mathrm{Two}(P, Q)$ and $\pi_j$ back with $\sum_{j \leq \min(P,Q)}\iota_j\pi_j = \mathrm{id}$, such that $p^{\lceil(m+2)\lambda_a\rceil}\pi_j$ and $p^{\lceil(m+2)\lambda_a\rceil}\iota_j$ carry $\mathrm{Two}_\Lambda(P, Q)$ and $H^0(\omega_{P-j,Q-j}, \Lambda)$ into each other for every lattice $\Lambda$.

Lean: `Formalism.MainNotions.flipOneThree.Pf.single_weight_of_model_identification`.

*Proof.* Apply the Lemma (Harmonic decomposition with denominators) with $k = m + 1$, $\alpha = \alpha_{P,Q}$, $W_j = S_{P-j,Q-j}$ and $\beta_j = \beta_{P-j,Q-j}$, over the valuation ring of $K$, in which integers prime to $p$ are units. Since $P + Q + m + 1 \leq 8a + m$, the exponent $(m + 2)\lfloor\log_p(P + Q + m + 1)\rfloor$ is at most $\lceil(m + 2)\lambda_a\rceil$, and $p$ is integral. The lattice $g'$ of the model identification turns the two claims of the lemma into the integrality of $\pi_j$ and $\iota_j$. $\square$

**Theorem 5.13.4 (Theorem I from the model identification).** The two-letter model identification and the cloud maps statement imply the closed form of Theorem I.

Lean: `Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_model_identification`.

*Proof.* The single weight comparison, taken in each factor $s \in T$ of the tensor product, gives the lattice functor comparison, with the exponent multiplied by $|T|$. Apply the Theorem (Theorem I from the lattice functor comparison). $\square$

The model comes from an explicit map. Let $\Psi$ be the algebra map that sends $x_i$ to the variable $X^{(1)}_{i,0}$ of the first matrix and $y_i$ to the signed $m \times m$ minor $(-1)^i\det B^{(i)}$ of the second matrix, and let $\delta$ identify the two matrices.

**Definition 5.13.5 (Explicit minor map).** The *explicit minor map statement* holds if for every setting and $m \geq 2$: $\Psi$ is injective; $\Psi(\mathrm{Pol}_{P,Q}) = \mathrm{Two}(P, Q)$; $\delta\Psi(\mathrm{Pol}_{a,b}) = S_{a,b}$, with kernel $h\,\mathrm{Pol}_{a-1,b-1}$ on $\mathrm{Pol}_{a,b}$; and every lattice $\Lambda$ has $g'$ with $\Psi(f) \in \mathrm{Two}_\Lambda(P, Q)$ if and only if $f$ lies in $g'$ times the Gauss lattice, and $H^0(\omega_{a,b}, \Lambda) = \delta\Psi$ of the polynomials of $\mathrm{Pol}_{a,b}$ in that lattice.

**Theorem 5.13.6 (Theorem I from the explicit minor map).** The explicit minor map statement and the cloud maps statement imply the closed form of Theorem I.

Lean: `Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_explicit_minor_map`.

*Proof.* Take $\alpha_{P,Q}$ to be the inverse of $\Psi$ on $\mathrm{Pol}_{P,Q}$ and $\beta_{a,b} = \delta\Psi$; the four parts of the statement are the four parts of the two-letter model identification. Apply the Theorem (Theorem I from the model identification). $\square$

**Remark 5.13.7 (Formalization).** The three facts in the proof of the harmonic lemma are `Top.gaussProj`, `Top.gaussLemmaH` and `Top.levelLattice` for the statements at PolynomialDimension/StatementHar.lean:198, 218 and 226; their proofs were not unfolded. The lemma `oneTop_abs` (ColumnSpanDensity/HarProjEqZeroIff.lean:87) has a name that does not describe it. The passage from one weight to the tensor product, `functor_comparison_of_single_weight_facts`, was not unfolded; the proof above follows its statement. In `single_weight_of_model_identification` (ColumnSpanDensity/SingleWeightOfModelIdentification.lean:79) the maps of the lemma are extended from the subspaces to the whole polynomial rings by an arbitrary linear extension; only their values on the subspaces are used.
