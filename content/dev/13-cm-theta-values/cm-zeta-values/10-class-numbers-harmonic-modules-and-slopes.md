---
title: Class numbers, harmonic modules and slopes
decls:
  - GlobalTheory.ColClassNumber.classNumber_all
  - GlobalTheory.HarmModule.harmonicModule_of
  - GlobalTheory.TestLat.slope_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Class numbers, harmonic modules and slopes

This section proves three facts that the [nonempty hypotheses](/step/nonempty-hyps/) and the [leaf bound for test lattices](/entry/leaf-mm-of-test/) need. The first is a class number formula: the class number of a column group of a datum is the mass of the standard hermitian lattice times a local index. The second builds, from the Fock model of the dual pair $(\mathrm{U}(p, q), \mathrm{U}(n))$, a discrete series representation with a lowest $K$-type and harmonic maps. The third bounds the maximal slope of the test lattices built from self-dual lattices. The background is in [class numbers](/learn/hermitian-lattices/#class-numbers), [the mass formula for unitary groups](/learn/hermitian-lattices/#the-mass-formula-for-unitary-groups), [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees) and [hermitian lattices and slopes](/learn/arakelov/#hermitian-lattices-and-slopes).

### Class numbers of column groups

**Lemma 1.10.1 (counting double cosets).** Let $G$ be a group, let $\Gamma$, $U$ and $K$ be subgroups with $U \subset K$ and $[K : U]$ finite and nonzero. Let the set $\Gamma \backslash G / K$ be finite, let each group $\Gamma \cap x K x^{-1}$ be finite, and put
$$m = \sum_{x \in \Gamma \backslash G / K} \frac{1}{\#(\Gamma \cap x K x^{-1})}.$$
Assume that $x^{-1} \gamma x \in U$ with $\gamma \in \Gamma$ implies $\gamma = 1$. Then $\#(\Gamma \backslash G / U) = [K : U] \cdot m$.

*Proof.* Fix a double coset $\Gamma x K$. The group $\Gamma_x = \Gamma \cap x K x^{-1}$ acts on $x K / U$, which has $[K : U]$ points. The orbits are the double cosets $\Gamma y U$ inside $\Gamma x K$, and the stabiliser of $y U$ is $\Gamma \cap y U y^{-1}$, which is trivial by assumption. So $\Gamma x K$ contains $[K : U] / \#\Gamma_x$ double cosets of $U$. Sum over $x$. $\square$

Now fix a datum. It gives a CM extension $E/F$, ranks $f$ and $k$, two primes $g_0, g_1$, and for each word $u$ a prime $T_u$ and a column group whose class set is $\mathrm{cls}_0(u)$. A level datum fixes a compact open level group at each word.

**Definition 1.10.2 (big prime, split prime, local index, mass).** The datum has a *big prime* if $2 f k < g_i - 1$ for some $i$. A prime $p$ *splits in $F$* if there are exactly $f$ primes of $\mathcal{O}_F$ over $p$ and each has residue field of size $p$. For a prime $g$, the *local column index* is
$$\iota(g, k) = \frac{\#\mathrm{GL}_k(\mathbb{F}_g)}{\#\{A \in \mathrm{GL}_k(\mathbb{F}_g) : A \text{ upper unitriangular}\}} = \frac{\#\mathrm{GL}_k(\mathbb{F}_g)}{g^{k(k-1)/2}}.$$
Let $\mu_k$ be the mass of the standard hermitian lattice $\mathcal{O}_E^k$ with the form $\sum x_i\, \bar y_i$.

For $k = 2$ the index is $(g^2 - 1)(g - 1)$.

**Theorem 1.10.3 (class number of column groups).** Let the datum have a big prime, and let $g_0$ and $g_1$ split in $F$. Let $u$ be a word such that $T_u$ splits in $F$. Then
$$\#\mathrm{cls}_0(u) = \mu_k \cdot \iota(g_0, k)^f\, \iota(g_1, k)^f \cdot (T_u^k - 1)^f.$$

Lean: `GlobalTheory.ColClassNumber.classNumber_all`.

*Proof.* The level datum identifies $\mathrm{cls}_0(u)$ with a double coset space $\Gamma \backslash G / U$, where $U$ is the level group. Four inputs are proved elsewhere.

1. There is a self-dual lattice $N$ over the base column lattice whose stabiliser $K$ contains $U$. A self-dual coordinate lattice comes from a unimodular lattice $M$ of the first space, so $N = M$ in coordinates.
2. The index formula: $[K : U] = \iota(g_0, k)^f\, \iota(g_1, k)^f\, (T_u^k - 1)^f$.
3. The classes of the genus of $M$ are the double cosets $\Gamma \backslash G / K$, and the mass of $M$ is the coset mass $m$ of the lemma. The mass of a unimodular lattice of the first space is $\mu_k$, by the mass of the standard genus.
4. The column stabilisers are trivial when the datum has a big prime. So $x^{-1} \gamma x \in U$ forces $\gamma = 1$.

The index in item 2 is positive, so $[K : U] \neq 0$. The lemma gives $\#\mathrm{cls}_0(u) = [K : U] \cdot \mu_k$, which is the claim. $\square$

### Harmonic modules

Let $1 \le p + q < n$. Let $\mathrm{U}(p, q)$ act with $\mathrm{U}(n)$ on the Fock space of polynomials on $\mathrm{M}_{(p+q) \times n}(\mathbb{C})$. For a block matrix $X$ in the noncompact part $\mathfrak{p}$ of the Lie algebra of $\mathrm{U}(p, q)$, let $s_i(X)$, for $i < \min(p, q)$, be the singular values of its upper right block, and put
$$\Delta_n(X) = \prod_{i < \min(p, q)} \cosh\big(s_i(X)\big)^{-n}.$$

**Definition 1.10.4 (harmonic decay, cosh integrals).** *Harmonic decay* holds if, for all Fock data, all $X \in \mathfrak{p}$ and all polynomials $\Phi_1, \Phi_2$ killed by the lowering operators,
$$\big|\langle \pi(\exp X)\, \Phi_1, \Phi_2 \rangle\big| \le \Delta_n(X)\, \|\Phi_1\|\, \|\Phi_2\|.$$
The *cosh integral* property holds if, for the Haar measure of $\mathrm{U}(p, q)$ with the standard density, the function $g \mapsto \prod_i \cosh(s_i(g))^{-c}$ of the Cartan part is integrable for $c > 2(p + q - 1)$, locally uniformly in $c$, and if its integral for $c = 2n$ with $n \ge p + q$ is at most $\exp\big(3 (p+q)^2 \log(p + q + 2)\big)$.

**Theorem 1.10.5 (harmonic module).** Assume harmonic decay and the cosh integral property. Let $1 \le p + q < n$, let $a^+ \in \mathbb{Z}^p$ and $a^- \in \mathbb{Z}^q$ be antitone with all entries at least $1$, and fix Fock data for $\mathrm{U}(p, q) \times \mathrm{U}(n)$. Then there are a discrete series representation $D$ of $\mathrm{U}(p, q)$ and a $K$-submodule $W$ of its Harish-Chandra module such that:

1. $W$ is the lowest $K$-type of $D$, of weight $\lambda_K(a^+, a^-)$;
2. the Blattner parameter of the Harish-Chandra parameter $\lambda_{HC}(a^+, a^-)$ is $\lambda_K$, and $D$ has Harish-Chandra parameter $\lambda_{HC}$;
3. for $k_1, k_2 \in K$, $X \in \mathfrak{p}$ and $e, e' \in W$, $|\langle e', D(k_1 \exp X\, k_2)\, e\rangle| \le \Delta_n(X)\, \|e\|\, \|e'\|$;
4. $W$ has a unit vector of the extreme weight;
5. $\mathrm{U}(n)$ has a module of compact type with the highest weight $\lambda_H(a^+, a^-)$, and for each such module and each extreme unit vector $e_0 \in W$ there are harmonic maps from $W \otimes M$ and from the Harish-Chandra module tensored with $M$ to the Fock space.

Lean: `GlobalTheory.HarmModule.harmonicModule_of`.

*Proof.*

*The lowest type.* Inside the Fock space there is a $(\mathfrak{g}, K)$-module $M_1$ with a $K$-submodule $W$ of weight $\lambda_K$ that is its lowest type, a highest weight vector $v \in W$, and a line of extreme weight vectors in $W$.

*Globalisation.* The vectors of $M_1$ are analytic in the Fock space: the action of each $Y$ is the derivative of the group action, and $\|Y^k y\| \le C \rho^k k!$. So the closure of $M_1$ is an irreducible unitary subrepresentation $\sigma$ of the Fock space, and $M_1$ is its Harish-Chandra module through an injective map $j$.

*Decay.* The vectors of $W$ are killed by the lowering operators, since $W$ is the lowest type. Harmonic decay then gives item 3 for $\sigma$.

*Square integrability.* By item 3, $|\langle \sigma(g) j v, j v\rangle|^2 \le \|j v\|^4 \prod_i \cosh(s_i(g))^{-2n}$. Since $2 n > 2(p + q - 1)$, the cosh integral property shows that this matrix coefficient is square integrable. Schur orthogonality gives a formal degree $d > 0$. So $\sigma$ is a discrete series representation $D$.

*Parameters.* The centred Harish-Chandra parameter $\lambda_{HC}$ is a parameter, and its Blattner parameter is $\lambda_K$. This gives items 1 and 2.

*Unit vector.* The vector $v / \|j v\|$ is a unit vector of extreme weight in $W$.

*Compact side.* A module $M_2$ of compact type with highest weight $\lambda_H$ exists in the Fock space of $\mathrm{U}(n)$. A module $M$ of compact type is finite dimensional and irreducible, and it has an intertwiner to $M_2$ that maps highest weight vector to highest weight vector. An extreme unit vector $e_0$ is a nonzero multiple of $v$, by the line property. An equivariant tensor map out of the cyclic module, and the fact that invariant inner forms on a weight line are proportional, give the harmonic maps. $\square$

### Slopes of test lattices

Let $K$ be a totally complex number field with an involution $*$ that is complex conjugation at a place $v_0$. Let $\iota$ be a finite set with $f = \#\iota$ elements. A *dominant weight* of rank $n$ is an antitone map $\lambda : \{1, \dots, n\} \to \mathbb{Z}$. A family $(\lambda_\tau)_{\tau \in \iota}$ has *spread at most $R$* if $\lambda_\tau(i) - \lambda_\tau(j) \le R$ for all $\tau, i, j$.

**Definition 1.10.6 (definite Gram matrix, self-dual lattice, test lattice condition).** A matrix $G \in \mathrm{M}_n(K)$ is a *definite Gram matrix* if $G^* = G$, its entries lie in the CM maximal order, and $\varphi(G)$ is positive definite for every embedding $\varphi : K \to \mathbb{C}$. A lattice $M \subset K^n$ is *self-dual* for $G$ if its hermitian dual for $G$ is $M$. Given $X_v \in \mathrm{GL}_N(\mathbb{C})$ at each infinite place $v$, a lattice $M \subset K^N$ satisfies the *test lattice condition* with bound $B$ if $M$ is finitely generated and nonzero, each $X_v$ is invertible, and the maximal slope of $M$ for the metric $X$ is at most $B$.

Put $B(f, n, R) = 4 f n R \log(n R)$. A self-dual family $(M_{c, \tau})$, indexed by $c$ in a nonempty set $C$, gives two lattices in the sum of the weight spaces of the $\lambda_\tau$: the sum of the lattices $\nabla_\lambda(M_c)$ and the sum of the lattices $\Delta_\lambda(M_c)$. A bijection $\{1, \dots, N\} \cong C \times I_\lambda$ with the index set of a basis puts them in $K^N$. The sum Gram matrix $H$ is the block diagonal matrix of the induced forms. We say $X$ is a metric for $H$ if $(X_v^{-1})^* X_v^{-1} = v(H)$ at each $v$.

**Theorem 1.10.7 (slope bound).** Let $R \ge 1$, let $(\lambda_\tau)$ have spread at most $R$, let $G_\tau$ be definite Gram matrices, and let each $M_{c, \tau}$ be self-dual for $G_\tau$. If $X$ is a metric for $H$, then the sum of the $\nabla_\lambda(M_c)$ and the sum of the $\Delta_\lambda(M_c)$ satisfy the test lattice condition with bound $B(f, n, R)$. If $X$ is a metric for $(H^{-1})^{T}$, then the dual of the sum of the $\Delta_\lambda(M_c)$ satisfies it.

The same holds over a CM field $E$ with complex conjugation $c_E$, with embeddings $\varepsilon_\tau : E \to K$ that satisfy $\varepsilon_\tau(x)^* = \varepsilon_\tau(c_E x)$, with a matrix $J \in \mathrm{M}_n(E)$ that is positive definite at every complex embedding, and with lattices $L_c \subset E^n$ self-dual for $J$. The four conclusions are for the Gram family $\varepsilon_\tau(J)$ with the lattices $\varepsilon_\tau(L_c)$, and for the Gram family $(\varepsilon_\tau(J)^{-1})^T$ with the dual lattices of $\varepsilon_\tau(L_c)$.

Lean: `GlobalTheory.TestLat.slope_holds`.

*Proof.* Over $K$, the two cases are two theorems proved elsewhere in the development: the slope bound for the sums of Weyl lattices and of dual Weyl lattices, and the slope bound for the dual of the sum. Over $E$, the field embedding lemma says that $\varepsilon_\tau(J)$ and $(\varepsilon_\tau(J)^{-1})^T$ are definite Gram matrices, that $\varepsilon_\tau(L)$ is self-dual for $\varepsilon_\tau(J)$ when $L$ is self-dual for $J$, and that its dual lattice is self-dual for $(\varepsilon_\tau(J)^{-1})^T$. Apply the case over $K$ to each family. $\square$

**Remark 1.10.8 (Formalization).** The class number theorem is in [ClassNumberAll.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/ClassNumberAll.lean#L11). It applies `classNumber_of_index` to `T.selfDualLattice_over_columnBaseLattice` and `T.stabiliser_self_dual_lattice_level_index_formula`. The proof `classNumber` and the lemma `card_eq_index_mul_mass` are in [MassSelfDualLatticeFirstSpaceEq.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/MassSelfDualLatticeFirstSpaceEq.lean#L102); they use `doubleCosetCount`, `exists_lattice`, `mass_selfDualLattice_firstSpace_eq` (through `genusMassStd`), `massAsCosetSum` and `columnStabilisersTrivial`, whose proofs we did not open. The statement `ClassNumberFormula₂` at [StandardLattice.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/StandardLattice.lean#L453) takes the level datum as `_Lv` and does not mention it; the level enters only through the bijection `y_bij` in the proof. The harmonic module theorem is `harmonicModule_of` in [ExistsKTranslate.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/ExistsKTranslate.lean#L487). It takes `HarmonicDecay` and `CoshIntegral` as hypotheses; its users pass `FockDecay.harmonicDecay` and `CartanInt.coshIntegral`. Its steps are local lemmas such as `exists_lowest`, `globalize` and `exists_fdeg`, and `T.*` theorems such as `T.memLp_two_of_cosh_decay_unitaryPQCover`. The slope theorem is in [SlopeEHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/SlopeEHolds.lean#L27), the conjunction of `slopeK_holds` and `slopeE_holds`. The first is two `T.maxSlope_*` theorems; the second uses `T.defGram_selfDual_after_field_embedding`. Over $E$ the proof drops the $\Delta$ part of the first conclusion of each call. The dual lattice `dualFr` uses the bilinear dot product.

## Notes and references

The results of this chapter feed the [nonempty hypotheses](/step/nonempty-hyps/), the [key rules for every character](/step/every-character-of-literature/), the [literature join](/entry/join-out-of-literature/), [Gross's curves](/entry/cm-curve-good-outside-prime-st-of-literature/), [the family of curves](/entry/exists-family-of-curve/), [the record of published inputs](/step/published-results-eigen/) and [the leaf bound for test lattices](/entry/leaf-mm-of-test/).

The classical theory of complex multiplication and lattice sums is in Silverman, Cox, and Whittaker and Watson; see [complex multiplication](/learn/elliptic-curves/#complex-multiplication) and [Eisenstein sums of lattices](/learn/elliptic-curves/#eisenstein-sums-of-lattices). Hilbert Eisenstein series and their values go back to Hecke, and Deligne and Ribet treat them over totally real fields. Gross's curves are in Gross's notes. The $p$-adic sigma function is due to Mazur and Tate, and the cube structure of theta functions to Breen. The Weil representation is due to Weil, and the Fock model with its harmonic polynomials to Kashiwara and Vergne and to Howe. Lattice neighbours are due to Kneser. Discrete series are due to Harish-Chandra; here they are built inside the Fock model. The exact mass formula for unitary groups is due to Gan, Hanke and Yu; here only the count of double cosets is proved. Slopes of lattices follow Stuhler and Grayson.

- L. Breen, *Fonctions thêta et théorème du cube*, Lecture Notes in Math. 980, Springer, 1983.
- D. A. Cox, *Primes of the Form $x^2 + ny^2$*, Wiley, 1989, §10 and §11.
- P. Deligne and K. A. Ribet, Values of abelian L-functions at negative integers over totally real fields, Invent. Math. 59 (1980), 227-286.
- W. T. Gan, J. P. Hanke and J.-K. Yu, On an exact mass formula of Shimura, Duke Math. J. 107 (2001), 103-133.
- D. R. Grayson, Reduction theory using semistability, Comment. Math. Helv. 59 (1984), 600-634.
- B. H. Gross, *Arithmetic on Elliptic Curves with Complex Multiplication*, Lecture Notes in Math. 776, Springer, 1980.
- Harish-Chandra, Discrete series for semisimple Lie groups II, Acta Math. 116 (1966), 1-111.
- R. Howe, Transcending classical invariant theory, J. Amer. Math. Soc. 2 (1989), 535-552.
- M. Kashiwara and M. Vergne, On the Segal-Shale-Weil representations and harmonic polynomials, Invent. Math. 44 (1978), 1-47.
- M. Kneser, Klassenzahlen definiter quadratischer Formen, Arch. Math. 8 (1957), 241-250.
- B. Mazur and J. Tate, The $p$-adic sigma function, Duke Math. J. 62 (1991), 663-688.
- D. Mumford, *Tata Lectures on Theta I*, Progress in Math. 28, Birkhäuser, 1983, Chapter I and Chapter II.
- J.-P. Serre, *Local Fields*, Graduate Texts in Math. 67, Springer, 1979, Chapter X, §1.
- J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Graduate Texts in Math. 106, Springer, 2009, Chapter VI and Chapter VII.
- J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Graduate Texts in Math. 151, Springer, 1994, Chapter II.
- U. Stuhler, Eine Bemerkung zur Reduktionstheorie quadratischer Formen, Arch. Math. 27 (1976), 604-610.
- A. Weil, Sur certains groupes d'opérateurs unitaires, Acta Math. 111 (1964), 143-211.
- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis*, 4th ed., Cambridge University Press, 1927, Chapter XX.
