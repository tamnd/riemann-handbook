---
title: Density of the lowest K-type and local index sums
decls:
  - Formalism.IndefR.Eqv.KerDiag.densLow_model
  - Formalism.IndefR.Eqv.KerDiag.densLow_of
  - Formalism.IndefR.Eqv.KerDiag.spanP_of_lowTNZ
  - Formalism.L2.Indef.Tree.on_core
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Density of the lowest K-type and local index sums

This section proves two more results that the chapter gives to other volumes. The first is a density statement for a discrete series representation of an indefinite unitary group: a functional that is bounded by finitely many derivatives and vanishes on the translates of the lowest $K$-type vanishes on every smooth vector. It gives the spanning property that [the spanning statement for the real data](/entry/span-p-of-given/) in the chapter on rows and frames of Volume 15 needs. The second assembles local index bounds at a finite set of places into the three inequalities of the condition on indices of an indefinite datum. It is used by [the core estimate at places](/entry/on-core-at-places/) in the chapter on Whittaker and Kirillov models of Volume 7.

### Discrete series models

Let $n \ge 1$, let $\varepsilon : \{1, \ldots, n\} \to \{0, 1\}$ be a signature and let $J_\varepsilon$ be the diagonal matrix with entries $\pm 1$ given by $\varepsilon$. Let $\lambda \in \mathbb{R}^n$ be a Harish-Chandra parameter. A *discrete series model* for a Hermitian matrix $G$ of signature $\varepsilon$ consists of:
- a nonzero complex Hilbert space $H$ and a map $\sigma$ from $n \times n$ complex matrices to bounded operators on $H$, which is a unitary, square integrable, [[irreducible representation|FX3NEFYFFN]] of the unitary group $U(J_\varepsilon)$; it has a $K$-type of weight $\lambda + \rho_n - \rho_c$, and this weight has the smallest norm among the weights of its $K$-types;
- an invertible matrix $f$ with $f^* J_\varepsilon f = G$.

The frame $f$ moves the representation to the unitary group $U(G)$ of $G$: put $\pi(g) = \sigma(f g f^{-1})$ for $g \in U(G)$. A vector $w \in H$ is *smooth* if for all $X_1, \ldots, X_k$ in the Lie algebra of $U(G)$ the map $(t_1, \ldots, t_k) \mapsto \pi(e^{t_1 X_1} \cdots e^{t_k X_k}) w$ is $C^\infty$. Let $H^\infty$ be the span of the smooth vectors, and for $X$ in the Lie algebra let $d\pi(X) w$ be the derivative at $t = 0$ of $\pi(e^{tX}) w$.

Here $K = U(J_\varepsilon) \cap U(n)$ is the maximal compact subgroup, a $K$-type is a finite-dimensional irreducible $K$-stable subspace, and $\rho_n$ and $\rho_c$ are the half sums of the noncompact and compact positive roots. The *lowest $K$-type* of the model is the sum $H_{\mathrm{low}}$ of the $K$-types that contain a weight vector of weight $\lambda + \rho_n - \rho_c$. Put $H_{\mathrm{low}}^\infty = H_{\mathrm{low}} \cap H^\infty$, and let $K_{\mathrm{low}}$ be the span of the vectors $\pi(g) w_0$ with $g \in U(G)$ and $w_0 \in H_{\mathrm{low}}^\infty$.

**Definition 7.10.1 (Sobolev bound).** A linear functional $\ell$ on $H$ is *Sobolev bounded* if there are finitely many words $X_{1} \cdots X_{k}$ in the Lie algebra and a constant $C$ such that for every smooth vector $w$,
$$|\ell(w)| \le C \sum_{\text{words}} \bigl\| d\pi(X_1) \cdots d\pi(X_k) w \bigr\| .$$

**Theorem 7.10.2 (Density of the lowest $K$-type).** Let $(H, \sigma, f)$ be a discrete series model and assume that $H_{\mathrm{low}}^\infty$ contains a nonzero vector. Let $\ell$ be a Sobolev bounded linear functional on $H$ that vanishes on $K_{\mathrm{low}}$. Then $\ell$ vanishes on $H^\infty$.

Lean: `Formalism.IndefR.Eqv.KerDiag.densLow_model`

*Proof.* Let $K'$ be the span in $H$ of the vectors $\pi(g) w_0$ with $g \in U(G)$ and $w_0 \in H_{\mathrm{low}}^\infty$. Each such vector is smooth, because $\pi(g)$ preserves smooth vectors, so $K'$ is the image of $K_{\mathrm{low}}$ in $H$ and $\ell$ vanishes on $K'$.

Step 1: the closure of $K'$ is $H$. The closure is a closed subspace, stable under $\pi(g)$ for every $g \in U(G)$, since each $\pi(g)$ is continuous and $K'$ is stable. Every element of $U(J_\varepsilon)$ has the form $f g f^{-1}$ with $g \in U(G)$, so the closure is stable under $\sigma$. It contains the nonzero vector $w_0$. By irreducibility it is all of $H$.

Step 2: smoothing. Let $\Phi$ be a $C^\infty$ function with compact support on the $n \times n$ complex matrices, and let $\sigma(\Phi) x = \int \Phi(h)\, \sigma(h) x \, dh$ over $U(J_\varepsilon)$. The Sobolev bound and the smoothness of $\Phi$ show that $x \mapsto \ell(\sigma(\Phi) x)$ is a continuous linear functional on $H$. For $x$ smooth, $\ell(\sigma(\Phi) x) = \int \Phi(h)\, \ell(\sigma(h) x)\, dh$. If $x \in K'$, then $\sigma(h) x = \pi(f^{-1} h f) x \in K'$ for every $h$, so $\ell(\sigma(\Phi) x) = 0$. By continuity and Step 1, $\ell(\sigma(\Phi) x) = 0$ for every $x \in H$.

Step 3: approximation of the identity. Let $w$ be smooth. The map $h \mapsto \ell(\sigma(h) w)$ is continuous, by the Sobolev bound. For $\delta > 0$ there is $\Phi$ as in Step 2 with $|\int \Phi(h)\, \ell(\sigma(h) w)\, dh - \ell(w)| \le \delta$. The integral is $\ell(\sigma(\Phi) w) = 0$, so $|\ell(w)| \le \delta$ for every $\delta > 0$. Hence $\ell(w) = 0$, and by linearity $\ell$ vanishes on $H^\infty$. $\square$

### The density and spanning properties of real data

A *real datum* $R$ attaches to each index $i$ and each infinite place $\tau$ a discrete series model $M_{i, \tau}$, and to each $i$ a space $\mathcal{W}_i$ of multilinear functionals $S$ on tuples of smooth vectors, one vector for each $\tau$. Three properties of $R$ enter:
- the *nonvanishing* property: for all $i$ and $\tau$, the lowest $K$-type of $M_{i, \tau}$ contains a nonzero smooth vector;
- the *density* property: for all $i$ and $\tau$, every Sobolev bounded functional on $M_{i, \tau}$ that vanishes on $K_{\mathrm{low}}$ vanishes on all smooth vectors;
- the *spanning* property: for every $i$, every $S \in \mathcal{W}_i$ that vanishes on all tuples of lowest $K$-type vectors is $0$.

**Corollary 7.10.3 (Density from nonvanishing).** If a real datum has the nonvanishing property, it has the density property.

Lean: `Formalism.IndefR.Eqv.KerDiag.densLow_of`

*Proof.* For each $i$ and $\tau$, apply the theorem to $M_{i, \tau}$. $\square$

**Corollary 7.10.4 (Spanning from nonvanishing).** If a real datum has the nonvanishing property, it has the spanning property.

Lean: `Formalism.IndefR.Eqv.KerDiag.spanP_of_lowTNZ`

*Proof.* By the previous corollary the datum has the density property. Let $S \in \mathcal{W}_i$ vanish on all tuples of lowest $K$-type vectors. The functionals in $\mathcal{W}_i$ are equivariant, so $S$ vanishes on all tuples of vectors in $K_{\mathrm{low}}$. A uniqueness statement for such functionals, applied with the density property at each place $\tau$, then gives $S = 0$. $\square$

### Local index sums

Let $K$ be a number field with an involution, and let $w \mapsto \bar w$ be the conjugation of its finite places. For a finite place $w$, let $p_w$ be the residue characteristic, $e_w$ the valuation of $p_w$ at $w$ and $l_w = \log Nw / [K:\mathbb{Q}]$. An *indefinite datum* $S$ has a finite set $T$ of finite places, a rank $D$, a finite index set of $j$, a lattice $M_j$ and a matrix $\theta_{j, t}$ for each $j$ and each tuple $t$, and a tuple $\mu(w)$ for each place. Its *local index* $I_j(w)$ is the index at $w$ of the lattice spanned by the columns of $\theta_{j, \mu(w)}$ times a fixed matrix, relative to $M_j$. A *numerical datum* $N$ gives reals $F_0(w, j)$, $J_0(t, w, j)$ and $E_1(j)$.

**Definition 7.10.5 (Index condition).** For a function $\mathrm{err}$ on places and indices, the datum $S$ satisfies the *index condition* for $N$ with error $\mathrm{err}$ if:
1. for every $w \in T$, $\sum_j \bigl(I_j(w) + I_j(\bar w)\bigr) \le \Bigl(\sum_j \bigl(2 e_w F_0(w, j) + e_w\, \mathrm{err}(w, j)\bigr) + \dfrac{2 e_w}{p_w^2}\Bigr) D$;
2. $\mathrm{err}(w, j) \ge 0$ for $w \in T$ and all $j$;
3. for every $j$, $\sum_{w \in T} l_w \bigl(e_w\, \mathrm{err}(w, j) + e_w J_0(\mu(w), w, j)\bigr) \le E_1(j)$.

The result of this subsection works with an *object* $O$ on $S$. It carries a finite group $P$ with a subgroup $U$, reals $x \ge 1$ and $\varepsilon$, reals $C, k, m \ge 1$, $f \ge 8$ and $T, N_c \ge 0$, further constants, and four distinguished primes $g_1, g_2, q_1, d$ together with a finite set $\Sigma$ of further primes. Put
$$x_e = x^{\varepsilon}, \quad b = e^{x_e}, \quad B_0 = f m b\, x_e, \quad C_b = C_{b,1} + C_{b,2} + 4 .$$
The object defines an error $\mathrm{err}_O(w, j)$ as follows. Its main part depends only on $j$ and on the residue characteristic $p_w$: it is $4T + 4 f r_0^2$ if $p_w \in \{g_1, g_2\}$, it is $2 s_C(j) + 2T + 2$ if $p_w \in \Sigma$, it is $2(s_B(j) + T + 1) + 4\beta(p_w)$ if $p_w \in \{q_1, d\}$, and it is an explicit function of the depth data at all other primes. Here $r_0$, $s_B(j)$, $s_C(j)$ and $\beta$ are explicit in the constants of $O$, and $\beta$ vanishes except at $d$. To the main part is added the term $(r(w, j)/e_w + r(\bar w, j)/e_{\bar w}) / ([P : U]\, D)$, where $r(w, j)$ is a local correction term of the object.

**Theorem 7.10.6 (Local index sums).** Let $S$ be an indefinite datum whose index spaces all have dimension $D > 0$, let $N$ be a numerical datum and $O$ an object on $S$. Assume the leaf conditions on $O$: twelve local conditions on lattices at the places of $T$, four conditions on shares, indices, bad places and unipotent elements, four depth conditions, and six conditions on the constants, the bad places and the sums of $J_0$. Let $C_E \ge 4C^2 + 25C + C_b + 44$ and assume $E_1(j) = C_E\, x_e (B_0 + N_c)$ for every $j$. Then $S$ satisfies the index condition for $N$ with error $\mathrm{err}_O$.

Lean: `Formalism.L2.Indef.Tree.on_core`

*Proof.* Step 1: local bounds. At each $w \in T$ and each $j$, the first group of leaf conditions gives
$$I_j(w) \le e_w\Bigl(\bigl(e_0(w, j) + v_U(w)\bigr) D + \frac{r(w, j)/e_w + n_j v_U(w)}{[P : U]} + \varepsilon_0(w, j)\Bigr),$$
where $e_0$ is a normalized local exponent, $v_U(w)$ is the normalized valuation of the order of $U$, $n_j$ is a dimension and $\varepsilon_0$ a local error. The same bound holds at $\bar w$.

Step 2: comparison with the error. The leaf conditions give bounds on the auxiliary constants, on the shares $n_j / [P : U] \le 3D$, and on $v_U$: $0 \le v_U(w) = v_U(\bar w)$ and $4 v_U(w)$ is at most a term $g(w)$ that is nonzero only at $g_1$ and $g_2$. The depth conditions then give
$$e_0(w, j) + e_0(\bar w, j) - 2F_0(w, j) + 2 g(w) \le \mathrm{err}_O^{\mathrm{main}}(w, j)$$
for every $w \in T$ and every $j$, where $\mathrm{err}_O^{\mathrm{main}}$ is the main part of the error.

Step 3: sums over places. The leaf conditions bound $\sum_{w \in T} l_w e_w\, \mathrm{err}_O^{\mathrm{main}}(w, j)$, the sums of the correction terms $r$, and $\sum_{w \in T} l_w e_w J_0(\mu(w), w, j)$, each by an explicit expression in the constants of $O$.

Step 4: assembly. A general theorem on local conditions turns the local bounds of Steps 1 and 2 and the sums of Step 3 into the first two parts of the index condition, and into a bound for the sum in part 3. Elementary inequalities between the constants, with $C_E \ge 4C^2 + 25C + C_b + 44$, show that this bound is at most $C_E\, x_e (B_0 + N_c) = E_1(j)$. $\square$

**Remark 7.10.7 (Formalization).** The theorem on smoothing is at [DensLow.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/LevelTypeEquivalence/DensLow.lean#L145), and the two corollaries at lines 197 and 200 of the same file. The span $K'$ of the proof is defined in [DensLow.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/LevelTypeEquivalence/DensLow.lean#L45), as a second copy of the span $K_{\mathrm{low}}$ of [VanishTranslates.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/LevelTypeEquivalence/VanishTranslates.lean#L24) inside $H$ instead of inside $H^\infty$. The lowest $K$-type is defined three times with the same body: [DiscreteSeriesUnitary.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/FockTheta/DiscreteSeriesUnitary.lean#L75), [UpqRep.lean](lean:Formalism/PeriodIntegrals/UpqRep.lean#L313) and [RelevantZeroGramTerms.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean#L78). The theorem on index sums is in a file whose name does not describe it, [ExampleSatisfiesConditionsAtFive.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/ExampleSatisfiesConditionsAtFive.lean#L603), and it has 29 hypotheses. In that file, three accessors take an object that they do not use and read the constants instead (lines 152 to 156), $C_b$ is defined twice with the same formula (lines 33 and 226), and the index condition is restated at line 361 and shown equal to the original in [IndefSide.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefSide.lean#L318) by a proof that is reflexivity (line 369).

## Notes and references

The results of this chapter feed several other chapters. The integrality of torsion values and the good models feed [the service row from Artin reciprocity](/entry/serv-h-row-of-artin/) and [the good model](/entry/good-model/) of the chapter on CM periods. The Honda theory at inert primes, the jets at split primes and the admissible pending tuples feed the chapter on inert primes, through [the admissibility theorem for kernel laws](/entry/admissible-general-of-kernel-law/) and [the jet bound at a split prime](/entry/jet-at-split-amb-of/). The class map of a symmetric system feeds the chapter on depth valuations. The genus theorem goes to Volume 8, the quotient lengths to Volume 14, the density of the lowest $K$-type to Volume 15 and the local index sums to Volume 7.

For formal groups of elliptic curves, the kernel of reduction and the torsion of curves with good reduction, see Silverman, *The Arithmetic of Elliptic Curves*, Chapters IV and VII. For complex multiplication, see Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Chapter II. For Lubin-Tate formal groups, see Lubin and Tate, "Formal complex multiplication in local fields", Annals of Mathematics 81 (1965). For the classification of formal groups by their logarithms, see Honda, "On the theory of commutative formal groups", Journal of the Mathematical Society of Japan 22 (1970), and Hazewinkel, *Formal Groups and Applications* (1978).
