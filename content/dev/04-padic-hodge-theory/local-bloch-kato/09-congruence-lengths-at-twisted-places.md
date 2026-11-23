---
title: Congruence lengths at twisted places
decls:
  - GlobalTheory.T.congruenceLength_twistedPlaces_of_heckeIntegrality
  - GlobalTheory.etaJ_join_closed
  - GlobalTheory.etaJ_join
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Congruence lengths at twisted places

The data of the series carry, for each level $j$ and each place $w$, a number $\eta_j(w)$: the sum of the local congruence lengths at the localisations of level $j$ over $w$. This section proves that $\eta_j(w)$ is the congruence length of a definite family at $w$ when $w$ is twisted, and is 0 when $w$ is not twisted. The proof compares the local lengths with a rational length, the length of a quotient of two lattices in a space over the coefficient field $L$. The result is used in [the $\eta_j$ identity with local data](/entry/eta-j-with-local-data-eq-alt/).

Let $D$ be the data of the series, with coefficient field $L$, a number field with ring of integers $\mathcal{O}_L$, and $m_R \ge 1$ levels. Each place $w$ of the series has a tuple $\mu(w)$; the place is *twisted* if $\mu(w) \ne \mu_0$ for a fixed tuple $\mu_0$, and then $\mu(w)$ is the twisted tuple of $w$. For a tuple $\mu$ and a level $j$ the data give a finite-dimensional $L$-space $M_L(\mu, j)$, a complex space $M(\mu, j)$, an $L$-linear map $\iota : M_L(\mu, j) \to M(\mu, j)$ with the embedding of $L$ in $\mathbb{C}$, a set of generators of an integral structure in $M(\mu, j)$, a complex subspace $Z_0(\mu, j)$ of $M(\mu, j)$, and a hermitian form for which $Z_0^\perp$ is taken.

**Definition 7.9.1 (Rational congruence length).** Fix $\mu$ and $j$, and write $M_L = M_L(\mu, j)$. Let $Z_L = \iota^{-1}(Z_0)$ and $Z_L' = \iota^{-1}(Z_0^\perp)$, two $L$-subspaces of $M_L$. Let $\Lambda$ be the $\mathcal{O}_L$-span of the $x \in M_L$ with $\iota(x)$ in the set of generators. Put
$$U = Z_L \cap (\Lambda + Z_L'), \qquad U_0 = \Lambda \cap Z_L.$$
For a finite place $w$ of $L$ with ramification index $e_w$ over $\mathbb{Z}$, the *rational congruence length* at $w$ is
$$\eta^{\mathrm{rat}}_j(\mu, w) = \frac{1}{e_w}\, \mathrm{length}_{\mathcal{O}_{L,w}} \big(U_w / (U_0)_w \cap U_w\big),$$
where the index $w$ means localisation at $w$. The space is *split* for $(\mu, j)$ if $Z_L + Z_L' = M_L$.

**Definition 7.9.2 (Local congruence lengths).** The data of the series have a set of *localisations*. A localisation $i$ has a prime $\ell_i$, a level $1 \le j_i \le m_R$, a place $w_i$ over $\ell_i$ that is twisted, the tuple $\mu_i = \mu(w_i)$, a complete discrete valuation ring $\mathcal{O}_i$ finite over $\mathbb{Z}_{\ell_i}$, an embedding of $L$ in the fraction field of $\mathcal{O}_i$ that is compatible with $w_i$, a lattice $M_i$ over $\mathcal{O}_i$ with a Hecke algebra acting on it, and a set $Z^{\mathrm{good}}_i$ of Hecke eigensystems. For a set $Y$ of eigensystems let $E_i(Y)$ be the sum of the eigenspaces for $Y$ in $M_i \otimes \mathrm{Frac}(\mathcal{O}_i)$. Put
$$U_i = E_i(Z^{\mathrm{good}}_i) \cap \big(M_i + E_i(Z^{\mathrm{good},c}_i)\big), \qquad U_{i,0} = M_i \cap E_i(Z^{\mathrm{good}}_i).$$
The *local congruence length* $\eta^{\mathrm{loc}}(i)$ is the length of $U_i / U_{i,0} \cap U_i$, normalized by $\ell_i$. We do not unfold the normalization. For a level $j$ and a place $w$, the data of the series satisfy
$$\eta_j(w) = \sum_{i : j_i = j,\ w_i = w} \eta^{\mathrm{loc}}(i).$$

A localisation also has a map $\mathrm{pr}_i$ from $M_L(\mu_i, j_i)$ to $M_i \otimes \mathrm{Frac}(\mathcal{O}_i)$. The *spectral condition* at $i$ says that $\mathrm{pr}_i$ maps $Z_L$ into $E_i(Z^{\mathrm{good}}_i)$ and $Z_L'$ into $E_i(Z^{\mathrm{good},c}_i)$. The *lattice condition* at level $j$ and a twisted place $w$ says that the local lattice at $(j, w)$ is stable under the Hecke operators at the generating places for $w$.

**Definition 7.9.3 (Definite family and its tie).** A *definite family* consists of a finite group $G$, a subgroup $P$ with a character $\psi : P \to L^\times$, a subspace $Z_s$, a number $m \le m_R$ of levels, a set $\mathcal{T}$ of indices, and for each $t \in \mathcal{T}$ and level $i < m$ spaces of forms with a lattice, a hermitian form and a subspace. It has a congruence length $\eta^{A}_i(t, w)$ at each finite place $w$. An *indefinite side* of the family is a set $\mathcal{Y}$ of points with a map $\mu_S$ to $\mathcal{T}$ and a set $\mathcal{Y}_{\mathrm{tw}}$ of twisted points. A *tie* of the family to $D$ is a map $\mathrm{tup}$ from $\mathcal{T}$ to the tuples of $D$ and identifications $e_{i,t}$ of the form space of $(i, t)$ with $M_L(\mathrm{tup}(t), i + 1)$, such that $\mathrm{tup}$ is injective and sends a fixed index $\mu_0^A$ to $\mu_0$, and $\mu(w) = \mathrm{tup}(\mu_S(w))$ for each place $w$ of $D$. Here the points of $\mathcal{Y}$ are finite places of $L$, and each place $w$ of $D$ gives a finite place of $L$, also written $w$. We do not unfold the forms, the lattice and the congruence length of the family.

**Theorem 7.9.4 ($\eta_j$ at twisted places, from the local conditions).** Let $D$ be the data of the series and let a definite family $A$ with $m \le m_R$ levels, an indefinite side and a tie be given. Assume that the family is good, that $y \in \mathcal{Y}$ is twisted if and only if $\mu_S(y) \ne \mu_0^A$, and that for every level $i < m$ and every twisted $y$ the identification $e_{i, \mu_S(y)}$ carries the hermitian form, the lattice and the subspace of the family to those of $D$. Assume that the Hecke operators are standard at twisted places, that the lattice condition holds at every level $j \le m_R$ and every twisted place, and that the spectral condition holds at every localisation. Then for every level $i < m$ and every place $w$,
$$\eta_{i+1}(w) = \begin{cases} \eta^{A}_i(\mu_S(w), w) & \text{if } w \text{ is twisted}, \\ 0 & \text{if not}. \end{cases}$$

Lean: `GlobalTheory.etaJ_join`.

*Proof.* Put $j = i + 1$, so $1 \le j \le m_R$. Suppose first that $w$ is twisted. Then $\mu(w) \ne \mu_0$ by the tie, and $\mu(w) = \mathrm{tup}(\mu_S(w))$ is the twisted tuple of $w$. Since $e_{i, \mu_S(w)}$ carries the form, the lattice and the subspace, a theorem on rational form lengths shows that the space is split for $(\mu(w), j)$ and that $\eta^{\mathrm{rat}}_j(\mu(w), w') = \eta^{A}_i(\mu_S(w), w')$ for every place $w'$. A second theorem compares local and rational lengths: when $w$ is twisted, the Hecke operators are standard, the lattice condition holds at $(j, w)$, the space is split and the spectral condition holds at every localisation over $(j, w)$, the sum $\eta_j(w)$ of the local lengths equals $\eta^{\mathrm{rat}}_j(\mu(w), w)$. Together these give $\eta_j(w) = \eta^{A}_i(\mu_S(w), w)$.

Suppose now that $w$ is not twisted, so $\mu(w) = \mu_0$. By the data, $\eta_j(w)$ is the sum of $\eta^{\mathrm{loc}}(i')$ over the localisations $i'$ with $j_{i'} = j$ and $w_{i'} = w$. Every localisation has a twisted place, so there is no such $i'$, and the sum is 0. $\square$

**Theorem 7.9.5 ($\eta_j$ at twisted places).** Let $D$, $A$, the indefinite side and the tie be as in the previous theorem, with the same conditions on the family, on the twisted points and on the identifications. Assume:

1. the Hecke operators are standard at twisted places;
2. the Hecke operators at the generating places of each twisted place are integral on the rational lattice, at every level;
3. the Hecke operators of $D$ are tied and rational, and the abelian varieties of $D$ are tied;
4. each localisation satisfies the class sum condition;
5. the theta maps of $D$ at the twisted points are given, through the identifications, by the theta matrices and the projections of the indefinite side;
6. the eigenspaces of the localisations span, the rows are isotypic and internal, two statements on sums of representations hold, and a goodness condition holds at all places.

Then for every level $i < m$ and every place $w$, $\eta_{i+1}(w) = \eta^{A}_i(\mu_S(w), w)$ if $w$ is twisted and $\eta_{i+1}(w) = 0$ if not.

Lean: `GlobalTheory.T.congruenceLength_twistedPlaces_of_heckeIntegrality` (also `GlobalTheory.etaJ_join_closed`).

*Proof.* We check the lattice condition and the spectral condition, and apply [the previous theorem](/entry/eta-j-join/). For each level $j \le m_R$ and twisted place $w$, integrality of the Hecke operators on the rational lattice shows that the local lattice at $(j, w)$ is stable under them, which is the lattice condition. For a localisation $i$, its place $w_i$ is twisted, so it is a twisted point of the indefinite side, and $\mu_i = \mathrm{tup}(\mu_S(w_i))$. The tie and hypothesis 5 then give a cut condition for the theta map at $(\mu_i, j_i)$. From hypotheses 1, 3, 4 and 6 and these cut conditions, a theorem on spectral projectors shows that the good part projector is spectral at every localisation, which is the spectral condition. $\square$

**Remark 7.9.6 (Formalization).** The second theorem has the hypothesis $m = m_R$ in addition to $m \le m_R$; the proof does not use it ([CongruenceLengthTwistedPlacesOfHeckeIntegrality.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CongruenceLengthTwistedPlacesOfHeckeIntegrality.lean#L13)), so the theorem holds for $m \le m_R$. The proof itself sets `maxHeartbeats` to 1000000, and its first Lean name is a wrapper that sets it again. The untwisted case uses only the tie, the description of the twisted points and the fact that every localisation sits over a twisted place.
