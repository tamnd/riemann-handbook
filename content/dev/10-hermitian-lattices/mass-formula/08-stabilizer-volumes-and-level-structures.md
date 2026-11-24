---
title: Stabilizer volumes and level structures
decls:
  - PI.OmFibreUniq.W.gram_map_fibre_existence
  - PI.VolStabS.MassDataS.volStabXS_of
  - PI.VolStabS.Assembly.volStabFromSW_holds
  - PI.VolStabS.Assembly.volStabFromSW_of_cntAA
  - PI.VolStabS.Assembly.volStabFromSW_of_open_ic
  - PI.VolStabS.Assembly.volStabFromSW_of_open_vic
  - PI.VolStabS.Assembly.volStabFromSW_of_open_aa
  - MassDataLevelSSteps.inLevelSAt_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Stabilizer volumes and level structures

The volume formula of the last section is for the whole group $U_J$. The proof also needs it for the stabilizer of a tuple of vectors: if $X$ is an $a$-tuple in $E^M$ with nondegenerate Gram matrix, then the stabilizer of $X$ in $U_J$ is a smaller unitary group, and its fundamental domain must have the same volume as the fundamental domain of $U_J$ when the measures are compatible. This section proves that equality from a Siegel-Weil type identity, and the input it needs on local densities: a fibre measure on each level set of the Gram map, the count of points of the level set at almost all places, and the bound on the local densities. The results feed the [nonempty hypotheses](/step/nonempty-hyps/), where the mass data of a Hida setting are built, and the [character analysis](/step/every-character-of-literature/), where the fibre measures give the orbit integrals. At the end we record the level structure of the same mass data. For local densities see [local densities](/learn/hermitian-lattices/#local-densities).

### The Gram map and its fibres

Let $v$ be a place of $F$, and put $E_v = F_v \otimes_F E$. Let $J$ be a nondegenerate Hermitian $M \times M$ matrix and $1 \leq a$. The *Gram map* sends an $a$-tuple $X = (x_1, \dots, x_a)$ of vectors of $E_v^M$ to the $a \times a$ Hermitian matrix
$$\operatorname{Gr}(X) = \bigl(h(x_i, x_j)\bigr)_{i, j}.$$
Let $\mathcal{U} \subseteq (E_v^M)^a$ be the open set of linearly independent tuples.

**Definition 7.8.1 (Fibre family).** Let $\mu$ be a Haar measure on $(E_v^M)^a$ and $\nu$ a Haar measure on the space $\operatorname{Herm}_a(E_v)$ of Hermitian $a \times a$ matrices. A *fibre family* is a family of measures $(\mu_T)_{T \in \operatorname{Herm}_a(E_v)}$ with three properties.

1. Each $\mu_T$ is concentrated on $\mathcal{U} \cap \operatorname{Gr}^{-1}(T)$.
2. The restriction of $\mu$ to $\mathcal{U}$ disintegrates along $\nu$: for measurable $A$,
$$\mu(A \cap \mathcal{U}) = \int \mu_T(A)\, d\nu(T).$$
3. For each continuous function $\varphi$ with compact support in $\mathcal{U}$, the map $T \mapsto \int \varphi\, d\mu_T$ is integrable and continuous.

The fibre measure $\mu_T$ is the measure $\mu / \operatorname{Gr}^* \nu$ on the level set. Its total mass on a lattice is the local density of the lattice at $T$, and the continuity in $T$ makes the local densities into continuous functions of the Gram matrix.

**Theorem 7.8.2 (Existence of fibre families).** Let $E/F$ be a CM extension, $J$ a nondegenerate Hermitian matrix, $v$ a place and $a \geq 1$. For all Haar measures $\mu$ on $(E_v^M)^a$ and $\nu$ on $\operatorname{Herm}_a(E_v)$ there is a fibre family.

Lean: `PI.OmFibreUniq.W.gram_map_fibre_existence`.

*Proof.* We define $\mu_T$ as a limit of densities. For a small neighbourhood $T + \Lambda$ of $T$, with $\Lambda$ a lattice in $\operatorname{Herm}_a(E_v)$, the ratio $\mu(\varphi \cdot 1_{\operatorname{Gr}^{-1}(T + \Lambda)}) / \nu(\Lambda)$ is defined. On the set $\mathcal{U}$ the Gram map is a submersion. So in local coordinates the preimages of lattice cosets are filtered by cosets, and a Hensel count shows that the ratio is constant once $\Lambda$ is small enough. The limit is a positive linear functional in $\varphi$, so a measure $\mu_T$ on $\operatorname{Gr}^{-1}(T)$. The disintegration follows from the density approximation: the integral over $T$ of the ratios is $\mu(\varphi)$ for every $\Lambda$. The tensor facts on Haar measures of the factors give the continuity in $T$. $\square$

The fibre family is unique up to $\nu$-null sets; the uniqueness is proved from this theorem and is used for the orbit integrals.

### The stabilizer volume

Let $G = U_J$ and let $X_0$ be an $a$-tuple of vectors in $E^M$ with $\det \operatorname{Gr}(X_0) \neq 0$. Let $H \subseteq G$ be the stabilizer of $X_0$.

**Definition 7.8.3 (Stabilizer volume).** The *stabilizer volume* holds at $X_0$ if the following holds for each additive character $\psi$, each Haar measure $\mu$ on $G(\mathbb{A}_F)$, each orbit measure $\nu_{X_0}$ on $G(\mathbb{A}_F) \cdot X_0$, each Haar measure $\mu'$ on $H(\mathbb{A}_F)$ compatible with $\mu$ and $\nu_{X_0}$, each fundamental domain $\mathcal{F}$ of $G(F)$ in $G(\mathbb{A}_F)$ and each fundamental domain $\mathcal{F}'$ of $H(F)$ in $H(\mathbb{A}_F)$:
$$\mu'(\mathcal{F}') = \mu(\mathcal{F}).$$

We take two statements as given. The first says that the quotient has finite volume: for each Haar measure $\mu$ and each fundamental domain $\mathcal{F}$ of $G(F)$, $\mu(\mathcal{F}) < \infty$. This is the theorem of Borel and Harish-Chandra. The second is a Siegel-Weil type identity.

**Theorem 7.8.4 (Compatibility of the first Chern data).** Let $n$ be an integer with $2n < M$, let $T$ be a nondegenerate Hermitian $n \times n$ matrix, and let $\Phi = \Phi_\infty \otimes \Phi_f$ be a Schwartz function on $(\mathbb{A}_E^M)^n$ with $\Phi_\infty$ smooth with compact support and $\Phi_f$ a pure tensor. Then the mean over $\mathcal{F}$ of the part of the theta series with Gram matrix $T$ is
$$\frac{1}{\mu(\mathcal{F})} \int_{\mathcal{F}} \sum_{\operatorname{Gr}(X) = T} \Phi(g^{-1} X)\, d\mu(g) = g_\infty(T) \prod_v g_v(T),$$
where $g_v(T) = \int \Phi_v\, d\mu_{v, T}$ is the integral of $\Phi_v$ against the fibre measure at $T$.

**Theorem 7.8.5 (Stabilizer volume from Siegel-Weil).** Let $E/F$ be a CM extension and $J$ a nondegenerate Hermitian matrix. Assume that the quotients of $G$ have finite volume and that the compatibility of the first Chern data holds. Then the stabilizer volume holds at each $X_0$ with $1 \leq a$, $2a < M$ and $\det \operatorname{Gr}(X_0) \neq 0$.

Lean: `PI.VolStabS.Assembly.volStabFromSW_holds` (also `PI.VolStabS.Assembly.volStabFromSW_of_cntAA`, `PI.VolStabS.Assembly.volStabFromSW_of_open_ic`, `PI.VolStabS.Assembly.volStabFromSW_of_open_vic` and `PI.VolStabS.Assembly.volStabFromSW_of_open_aa`, the same conclusion from fewer of the local inputs below).

The proof needs five local inputs at almost all places $v$, that is at all $v$ outside a finite set. Let $q_v = \#(\mathcal{O}_F / \mathfrak{p}_v)$, let $\Lambda_v = (\mathcal{O}_{E_v}^M)^a$ and let $\operatorname{Herm}_a(\mathcal{O}_v)$ be the integral Hermitian matrices.

**Lemma 7.8.6 (Count at almost all places).** For almost all $v$ and each integral $T$,
$$\mu\bigl(\Lambda_v \cap \operatorname{Gr}^{-1}(T + \mathfrak{p}_v \operatorname{Herm}_a)\bigr) = N_{k_v}(\bar{T}) \cdot \mu(\mathfrak{p}_v \Lambda_v),$$
where $k_v$ is a finite field with $q_v$ elements, $\bar{T}$ is the reduction of $T$, and $N_{k_v}(\bar{T})$ is the number of $a$-tuples $\bar{X}$ over $k_v$ with $\operatorname{Gr}(\bar{X}) = \bar{T}$.

**Lemma 7.8.7 (Index and volume at almost all places).** For almost all $v$ the index of $\operatorname{Herm}_a(\mathcal{O}_v)$ in its first level is $q_v^{a^2}$, and the self-dual measures give $\Lambda_v$ the volume $1$.

**Lemma 7.8.8 (Hensel lift).** For almost all $v$ each tuple over $k_v$ with Gram matrix $\bar{T}$ and independent reduction lifts to $\Lambda_v \cap \operatorname{Gr}^{-1}(T)$, and the lifts of one tuple fill one coset of $\mathfrak{p}_v \Lambda_v$ in the level set.

**Proposition 7.8.9 (Densities at almost all places).** From the four lemmas: there is a constant $C$ such that for almost all $v$,
$$\Bigl| \int 1_{\Lambda_v}\, d\mu_{v, T} - 1 \Bigr| \leq C\, q_v^{-2}.$$

*Proof.* The Hensel lift makes the density at $T$ equal to its value on the first level, so $\int 1_{\Lambda_v}\, d\mu_{v,T}$ is the measure of the count lemma divided by the $\nu$-measure of the first level of $\operatorname{Herm}_a(\mathcal{O}_v)$. The index lemma and the volume lemma give these measures as powers of $q_v$, and the count lemma reduces the claim to a bound for the number $N_{k_v}(\bar{T})$ of points over a finite field, which is close to the expected power of $q_v$ with an error of relative size $O(q_v^{-2})$. $\square$

*Proof of the theorem.* Since $\sum_v q_v^{-2}$ converges, the product $\prod_v g_v(T)$ of the local densities converges and is nonzero, because each factor is positive at the finite places and the archimedean factor is positive. So the orbit measure $\nu_{X_0}$ is nonzero, and the stabilizer measure $\mu'$ that is compatible with $\mu$ and $\nu_{X_0}$ exists, is invariant and is finite on $\mathcal{F}'$. Now unfold the left side of the identity of Siegel-Weil type: the theta sum over $\operatorname{Gr}(X) = T$ is a sum over $G(F)$-orbits, and with $T = \operatorname{Gr}(X_0)$ the orbit of $X_0$ unfolds the integral over $\mathcal{F}$ to $\mu'(\mathcal{F}')$ times the orbit integral of $\Phi$. The orbit integral is $g_\infty(T) \prod_v g_v(T)$. A positive test function makes this nonzero, and the comparison gives $\mu'(\mathcal{F}') / \mu(\mathcal{F}) = 1$. $\square$

**Corollary 7.8.10 (Stabilizer volume for a Hida setting).** Assume that for each Hida setting $X$ the finite volume and the compatibility of the first Chern data hold for the data $(F, E, J, n)$ of $X$. Then for each Hida setting the stabilizer volume holds.

Lean: `PI.VolStabS.MassDataS.volStabXS_of`.

*Proof.* This is the stabilizer volume from Siegel-Weil, applied to the CM data and the Hermitian matrix of $X$. $\square$

### Level structures

**Theorem 7.8.11 (Level structure of the mass data).** For each Hida setting $X$, the mass data built from $X$ have the level structure at each place: the compact subgroups at the split places are compact and open, the standard frame and the adapted lattice exist, the local products of the level subgroups are the global level subgroups, and the Haar measures of the local and global level subgroups have the expected indices on the Levi parts.

Lean: `MassDataLevelSSteps.inLevelSAt_holds`.

*Proof.* Each of the listed properties is a separate statement: the splitting at all places, the compactness and the openness of the subgroups at split places, the CM instance, the standard frame, the adapted lattice, the product of the non-split parts, the global subgroup as a product of parts, the local and global Haar indices, the local Levi parts and the global product. The theorem collects them. $\square$

**Remark 7.8.12 (Formalization).** The theorem on stabilizer volumes is assembled through a chain in which each step proves one more local input; two more steps of the chain, `volStabFromSW_of_open_orb` and `volStabFromSW_of_finVol`, ignore their hypotheses ([Assembly.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/Assembly.lean#L59)). We did not unfold the compatibility of the first Chern data beyond its statement ([SiegelWeilNarrowOfWide.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/SiegelWeilNarrowOfWide.lean#L22)); its name does not describe it, since it is a Siegel-Weil identity for the theta series. The counting and density proof above is our reading of the inputs (count, Hensel lift, index, volume, density bound, convergence of $\sum q_v^{-2}$); we did not unfold their proofs. We did not unfold the level structure field of the mass data ([MassDataInst.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/MassDataInst.lean#L242)); the list in the theorem is the list of its inputs. One user tries three names in turn with `first | apply` ([MassDataXVolAll.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/MassDataXVolAll.lean#L18)).
