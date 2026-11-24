---
title: The covolume of the reference lattice stabilizer
decls:
  - GlobalTheory.DegVol.RefCov.covol_ref
  - GlobalTheory.T.covolume_referenceLattice_stabiliser_bounds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The covolume of the reference lattice stabilizer

The weight of a term is a ratio of covolumes of arithmetic subgroups of the group $R$ of [the first section](/entry/om-le/). To compare the weight with the archimedean measure $\mu^0_\beta$ of [the fibre volume section](/entry/fibre-normal-fibre-volume/), we need the covolume of one subgroup in absolute terms. This section proves two-sided bounds for the covolume of the stabilizer of the reference lattice, measured with $\mu^0_\beta$ at every infinite place. The bound is used in the [amplitude bound at terms](/entry/amplitude-bound-of-local-data-of-tail-bound/), where it turns the normal-form stabilizer measure of a term into an explicit multiple of $\mu^0_\beta$.

We keep the notation of the first section: an unramified CM field $K$ with $f$ infinite places, a Hermitian space $V$ over $K$ of dimension $2r + k + 1$, a normal form $N$ with index $j$ and ideal $\mathfrak{d}$, the reference lattice $P_0$, the lattice $\operatorname{Ref}(L) = P_0 + (L \cap W_n)$, and the stabilizer $\Gamma(\Lambda)$ in $R$ of a lattice $\Lambda$. Put $v = |d_K|^{1/(2f)}/2$, so that $2v$ is the root discriminant of $K$.

**Definition 2.8.1 (Realization of a normal form at the infinite places).** Let $\iota$ be a finite set and $(\sigma_w)_{w \in \iota}$ a family of embeddings $K \to \mathbb{C}$. The family is a set of places if each $\sigma_w$ commutes with the involution and complex conjugation, and each infinite place of $K$ is induced by exactly one $\sigma_w$. A realization of $N$ at the places is a family of $\sigma_w$-linear maps $\Phi_w : V \to \mathbb{C}^{2r+k+1}$ (real points of $V$ at $w$), vectors $z_w, z'_w$ in the middle block with $T(z_w) > 0$, and elements $g_w$ that are normal with data $(j, \beta, c_w)$ for $(z_w, z'_w)$, such that, with $\rho = 2v$:

1. $\Phi_w(e_a) = \rho^{r-a} e_a$ and $g_w \Phi_w(e'_a) = \rho^{r-a} e_a$ for $a < r$, where $e_a$ and $e'_a$ are the flag vectors of $F$ and $F'$;
2. $\Phi_w(\iota_b) = \rho^{-(r-b)} e_b^*$ for $j \le b < r$;
3. $\Phi_w(z_F) = z'_w$ and $g_w \Phi_w(z_{F'}) = z_w$.

So $\Phi_w$ carries the flag $F$ to the standard flag, $g_w \Phi_w$ carries $F'$ to the standard flag, and both are scaled by powers of $2v$. Then $\Phi_w R \Phi_w^{-1}$ lies in the common stabilizer $R(g_w)$ of [the fibre volume section](/entry/fibre-normal-fibre-volume/). The real points of a subgroup $\Gamma \subseteq R$ are the families $(\Phi_w s \Phi_w^{-1})_w$ for $s \in \Gamma$.

**Definition 2.8.2 (Fundamental set).** Let $\Gamma$ act on a set $X$ of families $x = (x_w)_w$ by $(\gamma x)_w = \gamma_w x_w$. A measurable set $\Omega$ is a fundamental set for $\Gamma$ on $X$ if for every $x \in X$ there is exactly one $\gamma \in \Gamma$ with $\gamma x \in \Omega$.

**Theorem 2.8.3 (Covolume of the reference lattice stabilizer).** Let $K$ be an unramified CM field with $v \ge 1$, let $V$ have dimension $2r + k + 1$, and let $N$ be a normal form of length $r$ with index $j$ and ideal $\mathfrak{d}$. Let $(\sigma_w)_{w \in \iota}$ be a set of places and $(\Phi_w, z_w, z'_w, g_w)$ a realization of $N$ with $\rho = 2v$ and a common $\beta$. Assume $N(\mathfrak{d}) = (2v)^{2f}$, where $f = \#\iota$. Let $L$ be an $\mathcal{O}$-lattice that is unimodular on the part of $V$ orthogonal to both flags and that contains $z_F$. Then there is a fundamental set $\Omega$ for the real points of $\Gamma(\operatorname{Ref}(L))$ acting on $\prod_w R(g_w)$ with
$$\frac{v^{k(r-j)f}}{(8v)^{2(r+1)^2 f}} \le \Bigl(\prod_w \mu^0_\beta\Bigr)(\Omega) \le v^{k(r-j)f} (8v)^{2(r+1)^2 f}.$$

Lean: `GlobalTheory.DegVol.RefCov.covol_ref` (also `GlobalTheory.T.covolume_referenceLattice_stabiliser_bounds`, a second name).

*Proof.* The common stabilizer $R(g_w)$ has global coordinates. It is the image of an injective parametrization, and the parameters fall into four layers:

1. the top unitriangular coordinates $p_1$, one complex number for each pair $a < b$ of indices with $\beta$-block conditions;
2. the row coordinates $p_2$, one vector in $\mathbb{C}^{k+1}$ for each row $b$ with $j \le b < r$;
3. the top pair coordinates, one complex number for each pair $a < b$ with $j \le a$;
4. the skew coordinates, one skew-Hermitian matrix entry block for each $a \ge j$.

The measure $\mu^0_\beta$ is Lebesgue measure in these coordinates. The group law is triangular in the layers: if $p$ and $q$ are coordinates, then the product has coordinates $w$ with $w_1 = p_1 + q_1$ on the lowest unitriangular level not yet killed, $w_2 = p_2 + q_2$ when $p_1 = 0$, and $w_3, w_4$ additive when $p_1 = 0$ and $p_2 = 0$.

Next we describe $\Gamma(\operatorname{Ref}(L))$ in each layer. The real points of an element of $\Gamma(\operatorname{Ref}(L))$ have coordinates in the Minkowski image of fractional ideals: a top coordinate for the pair $a < b$ lies in $\rho^{b-a} \mathfrak{d}^{a-b}$; a row coordinate for $b$ lies in the image of $\mathfrak{d}^{-(r-b)} (L \cap W_n)$ scaled by $\rho^{r-b}$; a top pair coordinate lies in $\rho^{(r-a)+(r-b)} \mathfrak{d}^{-(r-a)-(r-b)}$; and the skew coordinates lie in a skew-Hermitian ideal lattice. Conversely, every coordinate vector of this form in one layer, with zero lower layers, comes from an element of $\Gamma(\operatorname{Ref}(L))$. Here the unimodularity of $L$ on the middle part gives the rows, and $z_F \in L$ keeps the negative vector fixed.

For each layer we take a fundamental set of the corresponding lattice in $\prod_w \mathbb{C}$. A fractional ideal $\mathfrak{a}$ has covolume $v^f\, N(\mathfrak{a})$ in $\prod_w \mathbb{C}$ (up to the normalization of Lebesgue measure fixed here), and the scaling by $\rho^n$ multiplies the volume by $\rho^{2nf}$. Since $N(\mathfrak{d}) = \rho^{2f}$, the scaling cancels the norm of the ideal. So each top coordinate gives a fundamental set $F_1$ of volume exactly $v^f$, each row gives a fundamental set $F_2$ of volume $(v^f)^{k+1}$, and each top pair coordinate gives a fundamental set $F_3$ of volume $v^f$. For the skew layer there is a fundamental set $F_4$ with explicit lower and upper bounds on its volume. Let $\Omega$ be the image of the product $\prod F_1 \times \prod F_2 \times \prod F_3 \times \prod F_4$ under the parametrization, at all places at once.

Then $\Omega$ is a fundamental set. Let $x \in \prod_w R(g_w)$. Because the group law is triangular, we find $\gamma$ layer by layer: first the top coordinates, then the rows, then the top pairs and the skew part. In each layer the translate is unique, since each $F_i$ is a fundamental set for an additive lattice, and the earlier layers are already fixed. The measure of $\Omega$ is the product of the volumes of the layers, since the parametrization carries the product of Lebesgue measures to $\prod_w \mu^0_\beta$.

Finally the volumes. There are $r - j$ rows, and the number of top coordinates and of top pair coordinates is at most $r^2$ each. So
$$\Bigl(\prod_w \mu^0_\beta\Bigr)(\Omega) = (v^f)^{n_1 + n_3} (v^f)^{(k+1)(r-j)} \prod_{a \ge j} \mathrm{vol}(F_4(a)),$$
with $n_1, n_3 \le r^2$. With the bounds for $F_4$ and $v \ge 1$, a direct estimate of the exponents gives both sides of the claim. $\square$

**Remark 2.8.4.** The bounds are crude: the factor $(8v)^{2(r+1)^2 f}$ absorbs all layers except the rows. Only the main factor $v^{k(r-j)f}$ matters in the application, because the amplitude bound compares it with the factor $D^{-(k-1-j)}$ of the [degree bound](/entry/deg-core/).

**Remark 2.8.5 (Formalization).** The unimodularity hypothesis on $L$ is `IsUnimodMod H L (uPerp N.F N.F') (II N.F N.F')`; we have not unfolded `uPerp` and `II`, and the text describes them only as "the part orthogonal to both flags". The count of coordinates uses `card_UT`, which bounds every subset of the index set of strictly upper pairs by $r^2$ ([CovolumeReferenceLatticeStabiliserBounds.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CovolumeReferenceLatticeStabiliserBounds.lean#L56)), not by $r(r-1)/2$. The fundamental sets $F_1, \dots, F_4$ come from separate results (`IdealFund.exists_fund_ipow`, `exists_fundamental_set_rows_middleSpace`, `SkewFund.exists_fund_skew`), and the final arithmetic is `layer_covolume_product_pow_two_sided_bounds`. The theorem is used at [IntegralUnipotentCovolumeFiniteBounded.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/IntegralUnipotentCovolumeFiniteBounded.lean#L73) and at [HermitianStabiliserCovolumeLe.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermitianStabiliserCovolumeLe.lean#L113). The second name is a wrapper of the form `first | exact @X | exact X | ...`.
