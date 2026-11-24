---
title: The covolume of the stabilizer of a relevant term
decls:
  - GlobalTheory.LoopC.CovTerm.cov_lead
  - GlobalTheory.T.covolume_integralUnipotentStabilizer_of_term
  - GlobalTheory.LoopC.CovTerm.covolume_term
  - GlobalTheory.T.stabiliserCovolume_relevantTerm_le_heightPow
  - GlobalTheory.LoopVol.volRC_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The covolume of the stabilizer of a relevant term

A relevant term of the double coset sum carries a covolume: the volume of a fundamental set for the integral unipotent isometries that fix both of its flags, measured at the infinite places. The bounds on the terms in [the step](/step/nonempty-hyps/) need this covolume to be at most a power of the height of the Gram matrix of the term. This section proves that bound. The method is the reduction theory of unipotent groups over a number field: an upper unitriangular matrix can be moved by an integral one until its entries are bounded by a covering radius of the ring of integers, and the volume of the set of such reduced matrices is then bounded by counting.

**Definition 2.23.1 (Root set and root coordinates).** Let $N \ge 1$ and let $w$ be an $N \times N$ matrix. Its *root set* is
$$R(w) = \{\, (i, j) : i < j,\ w_{i' i} \ne 0 \text{ and } w_{j' j} \ne 0 \text{ for some } j' < i' \,\}.$$
For a family $c = (c_q)_{q \in R(w)}$ of complex numbers let $u(c)$ be the matrix with entry $c_q$ at each $q \in R(w)$, entry $1$ on the diagonal, and $0$ elsewhere.

When $w$ is a permutation matrix, $R(w)$ is the set of positive roots that $w$ sends to negative roots, and the matrices $u(c)$ form the unipotent group $U \cap w^{-1} U^- w$. This is the group that acts freely on the Bruhat cell of $w$.

**Definition 2.23.2 (Unitriangular stabilizer).** Let $K$ be a field and $Z \in GL_N(K)$. The *unitriangular stabilizer* of $Z$ is
$$\operatorname{St}(Z) = \{\, a \text{ upper unitriangular} : Z a Z^{-1} \text{ lower unitriangular} \,\}.$$

**Definition 2.23.3 (Leading minor height).** Let $K$ be a number field with a family of complex embeddings $(\tau_v)_{v \in \iota}$. For an $N \times N$ matrix $Z$ over $K$ with leading minors $D_1(Z), \dots, D_N(Z)$ put
$$\Pi(Z) = \prod_{v \in \iota} \prod_{l=1}^{N} \max\bigl(1, |\tau_v(D_l(Z))|\bigr).$$

**Theorem 2.23.4 (Reduced stabilizer elements).** Let $K$ be a CM field of degree $2|\iota|$ and $(\tau_v)_{v \in \iota}$ a family of embeddings, one for each infinite place, compatible with complex conjugation. Let $\rho \ge 1$ be a covering radius of $\mathcal{O}_K$: for every $x \in K$ there is $o \in \mathcal{O}_K$ with $|\tau_v(x + o)| \le \rho$ for all $v$. Assume $\prod_v |\tau_v(o)| \ge 1$ for every nonzero $o \in \mathcal{O}_K$. Let $L$ be lower unitriangular, $U$ upper unitriangular, $w$ a matrix, and assume $Z = L w U$ has entries in $\mathcal{O}_K$. Let $I \ne 0$ be an ideal of $\mathcal{O}_K$. Then there is a measurable set $\Omega \subseteq (\mathbb{C}^{R(w)})^{\iota}$ with
$$\operatorname{vol}(\Omega) \le \Bigl( |d_K|^{1/2}\, (4N^2)^{|\iota|}\, M^4\, \mathrm{N}(I)\, (N!)^{2|\iota|} \Bigr)^{N^2},$$
where $M = (4^N (N!)^2 \rho^{2N})^{|\iota|}\, \Pi(Z)^2$, such that for every $c \in (\mathbb{C}^{R(w)})^{\iota}$ there is $a \in \operatorname{St}(Z)$ with $a - 1$ entrywise in $I$ and
$$\Bigl( \bigl(\tau_v(U a U^{-1})\, u(c_v)\bigr)_{q} \Bigr)_{v,\, q \in R(w)} \in \Omega.$$

Lean: `GlobalTheory.LoopC.CovTerm.cov_lead`.

*Proof.* First reduce the two triangular factors. By the covering radius, an upper unitriangular $U$ has an integral upper unitriangular $B$ such that every entry of $U B$ has all embeddings of size at most $\rho$. One finds $B$ column by column: the entry $(i, j)$ of $U B$ is the entry of $B$ plus a sum of known terms, and one picks the entry of $B$ in $\mathcal{O}_K$ to bring the sum within $\rho$. The same reduction applied to $L^T$ gives an integral lower unitriangular $A^T$ with $A^T L$ reduced. Since integral unitriangular matrices do not change integrality, the leading minors of $Z$ and of $A^T L w U B$ agree. So we may assume $L$ and $U$ have entries bounded by $\rho$ at every embedding.

Next we use a covering lemma for congruence stabilizers, proved earlier in the development: if $L' w U'$ is integral, $I \ne 0$, and every minor of $L' w U'$ has $|\tau_v(\text{minor})| \le \beta_v$ with $\prod_v \max(1, \beta_v) \le \beta$ and $\beta \ge 1$, then there is a measurable $\Omega$ with
$$\operatorname{vol}(\Omega) \le \Bigl( |d_K|^{1/2}\, (4N^2)^{|\iota|}\, \beta^4\, \mathrm{N}(I)\, (N!)^{2|\iota|} \Bigr)^{N^2}$$
such that each $c$ is reached by some $a \in \operatorname{St}(L' w U')$ with $a - 1$ in $I$, in the sense of the Theorem. We apply it to $L' = A^T L$ and $U' = U B$. To get $\beta_v$, expand a minor of $L' w U'$ by the Cauchy-Binet formula: it is a sum of at most $(N!)^2$ products of minors of $L'$, of $w$ and of $U'$. The minors of $L'$ and $U'$ are bounded by $N! \rho^N$ at each embedding. The minors of $w$ are, up to sign, ratios of leading minors of $Z$, since $w$ is the matrix of a point of the cell decomposition. For a nonzero integral $o$ the norm lower bound gives $\prod_v \max(1, |\tau_v o|) \max(1, |\tau_v o|^{-1}) \le \prod_v \max(1, |\tau_v o|)^2$, so the product over $v$ of the bounds for the minors of $w$ is at most $\Pi(Z)^2$. This gives $\beta = M$. Last, $a \mapsto B a B^{-1}$ maps the stabilizer of $L' w U'$ to that of $Z$ and keeps $a - 1$ in $I$, because $B$ is integral with determinant $1$; and $U' a (U')^{-1} = U (B a B^{-1}) U^{-1}$, so the root coordinates are unchanged. $\square$

Now we apply this to a term. We use the setting of the double coset sum: a CM field $E$ of degree $2f$ with embeddings $\tau$, the rank $r_S$, $N = r_S + 1$, the root discriminant $r_E = |d_E|^{1/(2f)}$, and the number $b$ of the size data. For a flag $F$ with frame $(f_a)$ and a flag $F'$ with frame $(f'_b)$, let $\hat Z(F, F')$ be the Gram matrix with entries $h(f'_b, f_a)$ and let $\hat Z^{\pm}$ be the same matrix with column $j$ multiplied by $(-1)^{r_S - j}$. For a lattice $\Lambda$ and a flag $F$ let $N_\Lambda(F)$ be the group of unipotent isometries of $F$ that preserve $\Lambda$. The height of a Gram matrix is
$$\mathrm{H}(b, C, Z) = \bigl(b^{C m^2 f}\bigr)^{C m}\, \operatorname{size}(Z)^4,$$
where $m = 2r_S + 2$ and $\operatorname{size}(Z)$ is a size of $Z$ built from its leading minors at the infinite places.

**Theorem 2.23.5 (Covolume of the stabilizer of a term).** For all constants of the setting there is $C \ge 1$ with the following property. Assume the standing hypotheses of the setting with $C' \ge 1$ and $C_l \ge 1$. Let $F_0$ be a base flag, $\Lambda$ a row lattice for $F_0$, and $F'$ a terminal flag for $\Lambda$ and $F_0$. Let $p$ be a point of the cell decomposition with matrix $w_p$, and let $L$ be lower and $U$ upper unitriangular with $\hat Z^{\pm}(F_0, F') = L w_p U$. Then there is a measurable set $\Omega \subseteq (\mathbb{C}^{R(w_p)})^{\tau}$ with
$$\operatorname{vol}(\Omega)\, r_E^{2f (r_S + 1)^3} \le \mathrm{H}\bigl(b, C, \hat Z(F_0, F')\bigr)^{C r_S^2},$$
such that for every $c$ there are $n \in N_\Lambda(F_0) \cap N_\Lambda(F')$ and a matrix $a$ with
$$n(f'_j) = \sum_i (-1)^{i+j} a_{ij}\, f'_i \quad \text{for all } j,$$
and the root coordinates of $\tau(U a U^{-1})\, u(c_\tau)$ lie in $\Omega$.

Lean: `GlobalTheory.T.covolume_integralUnipotentStabilizer_of_term` (also `GlobalTheory.LoopC.CovTerm.covolume_term`, its proof).

*Proof.* Take $C = \lceil C_T \rceil + 20$. Each embedding of $E$ is complex, since $E$ is a CM field. The set $\mathcal{O}_E$ has a covering radius $\rho = \sqrt{2f}\, r_E$ for the embeddings, and the norm of a nonzero integer is at least $1$. The Gram matrix $\hat Z^{\pm}(F_0, F')$ is integral, because the frames of a row lattice and of a terminal flag lie in $\Lambda$ and its dual. The setting gives a nonzero ideal $I$ whose norm is bounded by a power of $b$, such that every $a \in \operatorname{St}(\hat Z^{\pm})$ with $a - 1$ in $I$ comes from some $n \in N_\Lambda(F_0) \cap N_\Lambda(F')$ by the formula of the Theorem; the signs $(-1)^{i+j}$ come from the passage between $\hat Z$ and $\hat Z^{\pm}$. Apply [Theorem 2.23.4](/entry/cov-lead/) with this $\rho$ and $I$. It gives $\Omega$ and the elements $a$. It remains to bound its volume. The standing hypotheses give $r_E \le b$, $f \le b^{r_S}$ and $\rho \le b^{2(r_S + 1)}$. The leading minors of $\hat Z^{\pm}$ have the same absolute values as those of $\hat Z$, so $\Pi(\hat Z^{\pm})$ is bounded by a power of the size of $\hat Z$. Multiplying the bound of [Theorem 2.23.4](/entry/cov-lead/) by $r_E^{2f (r_S+1)^3}$ and collecting powers of $b$ gives the stated power of $\mathrm{H}$. $\square$

**Theorem 2.23.6 (Covolume of a relevant term).** For all constants of the setting there is $C$ with the following property. Assume the standing hypotheses with $C_l \ge 1$. Let $t$ be a relevant term of the double coset sum for $(u, u')$ with nonzero Gram value, with flags $F_t$ and $F'_t$. Then its covolume $\operatorname{vol}(t)$ satisfies
$$\operatorname{vol}(t) \le \mathrm{H}\bigl(b, C, \hat Z(F_t, F'_t)\bigr)^{C r_S^2}.$$

Lean: `GlobalTheory.T.stabiliserCovolume_relevantTerm_le_heightPow` (also `GlobalTheory.LoopVol.volRC_le`, its proof).

*Proof.* Take the constant $C$ of [Theorem 2.23.5](/entry/covolume-integral-unipotent-stabilizer-of-term/). The height is at least $1$, and the exponent $C r_S^2$ is nonnegative, so the right side is at least $1$. If the term has no pinned fundamental set, its covolume is $1$ by definition and the bound holds. Otherwise the term is pinned at a point $p$ of the cell decomposition, with a fundamental set at the infinite places. The covolume of a fundamental set for $N_\Lambda(F_0) \cap N_\Lambda(F')$ is at most $\operatorname{vol}(\Omega)\, r_E^{2f(r_S+1)^3}$ for every set $\Omega$ of root coordinates that meets each orbit, since the root coordinates form a chart of the real group with Jacobian bounded by this power of $r_E$. The set $\Omega$ of [Theorem 2.23.5](/entry/covolume-integral-unipotent-stabilizer-of-term/) meets each orbit. The Gram matrix of the term has the same leading minors as the Gram matrix of the pinned frames, because leading minors are constant on a double coset of unipotent groups. So the two heights agree. $\square$

**Remark 2.23.7 (Formalization).** The covolume `volRC` is $1$ when the term is not pinned ([LoopTerm.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/LoopTerm.lean#L107)), and `covR` is $1$ when there is no pin (line 104); the bound is trivial in these cases. The constant of `covolume_term` is $\lceil C_T \rceil + 20$ ([CovolumeIntegralUnipotentStabilizerOfTerm.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CovolumeIntegralUnipotentStabilizerOfTerm.lean#L563)). The reduction step is `reduce_up` (line 237) and $\Pi$ is `PiZ` (line 253). The ideal $I$ comes from `congruence_stabU_from_integral_unipotent_isometry`, and the comparison of the covolume with $\operatorname{vol}(\Omega)$ is `stabiliserCovolume_le_rootCoordinateCover`; neither is unfolded here. The size `sizeZ` in the height `HHZ` is not unfolded here. The covering lemma is `covolume_congruence_stabiliser` ([CovolumeCongruenceStabiliser.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CovolumeCongruenceStabiliser.lean#L296)), and the minor expansion is `minorBound`; the arithmetic of the exponents is the lemma `num` (line 345).
