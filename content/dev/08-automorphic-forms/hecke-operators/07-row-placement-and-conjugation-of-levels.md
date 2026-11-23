---
title: Row placement and the conjugation of levels
decls:
  - GlobalTheory.SeeConj.exists_frame_symLevel
  - GlobalTheory.T.exists_frame_conjugate_level_symmetricLevel
  - GlobalTheory.SeeConj.exists_conj_level
  - GlobalTheory.T.exists_finite_element_conj_rowLevel_character
  - GlobalTheory.SeeEval.evalTieT_of_levelMatch
  - GlobalTheory.T.goodRows_compare_by_levelMatching_evaluation
  - GlobalTheory.rowPlacement_exists
  - GlobalTheory.T.exists_rowPlacement_finiteElement_matches_levels
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Row placement and the conjugation of levels

A space of automorphic forms on a unitary group is defined by a level: an open compact subgroup $K$ of the finite adelic points and a character $\chi$ of $K$. The same group can carry a second level, written in other coordinates. This section shows that the level of the first row space of a theta datum is conjugate, by a finite adelic element $t$, to the level of a Hida setting. It then shows that after the translation by $t$, evaluation at a fixed vector identifies the row of forms with the good part of the Hida space, with a fixed scaling of norms. The result is used in [the placement of a normalized realization](/entry/placement-of-realisation-alt/).

### Frames and level groups

Let $E/F$ be a CM extension with complex conjugation $x \mapsto \bar{x}$, and let $V$ be a Hermitian space over $E$ of dimension $n$ with unitary group $G = \mathrm{U}(V)$. Let $\mathbb{A}_f$ be the finite adeles of $F$ and $E_f = E \otimes_F \mathbb{A}_f$. Let $G^c_f \le G(\mathbb{A})$ be the elements with trivial archimedean component. For a prime $\mathfrak{P}$ of $E$ let $k_{\mathfrak{P}}$ be its residue field ([unitary groups](/learn/groups/#unitary-groups)).

**Definition 6.7.1 (Frame).** A *frame* of an $\mathcal{O}_E$-lattice $L \subset E^n$ is an element $\beta \in \mathrm{GL}_n(E_f)$ whose columns are a basis of $L \otimes \hat{\mathcal{O}}_E$. For a frame $\beta$ and an element $x$ of $\mathrm{GL}_n(E_f)$ that preserves the lattice of $\beta$, the *reduction* of $x$ at $\mathfrak{P}$ is the matrix in $\mathrm{GL}_n(k_{\mathfrak{P}})$ of $x$ in the basis $\beta$, modulo $\mathfrak{P}$.

**Definition 6.7.2 (Level datum).** A *level datum* $\mathcal{L}$ consists of integers $r \le n$ and $t$, a finite set $P$ of primes of $E$ (the *level places*), a finite set $Q$ of primes, a subgroup $H \le \prod_{\mathfrak{P} \in P} \mathrm{GL}_r(k_{\mathfrak{P}})$ with a character $\psi_H$, and characters of the residue fields. For a frame $\beta$, the *level group* $K(\beta, \mathcal{L})$ is the set of $x \in G(\mathbb{A}_f)$ that preserve the lattice of $\beta$, whose reduction at each $\mathfrak{P} \in P$ is block upper triangular for the blocks given by $r$ and $t$, with upper left $r \times r$ block in $H$, and whose reduction at each $\mathfrak{P} \in Q$ is block upper triangular for the blocks given by $r$. The *level character* $\chi(\beta, \mathcal{L})$ on $K(\beta, \mathcal{L})$ is $\psi_H$ of the tuple of upper left blocks, times the residue field characters of the remaining diagonal entries.

Two frames that have the same reduction at every level place, and that have the same lattice, give the same level group and the same character. If $t \in G^c_f$, then conjugation by $t$ carries $K(\beta, \mathcal{L})$ onto $K(t\beta, \mathcal{L})$, and the characters correspond.

The level places in the applications use the following subgroup. Let $U_r \le \mathrm{GL}_r(k)$ be the upper triangular unipotent matrices. Fix integers $\rho$ and $k$. An *edge* is a pair $(i, i+1)$ with $i \ne \rho - 1$ and $i \ne \rho + k - 1$ (counting indices from $0$), or the single pair $(\rho - 1, \rho + k)$. Let $U_{\rho, k} \le U_r$ be the matrices whose column $\rho + k$ vanishes in the rows $\rho, \dots, \rho + k - 1$. On $U_{\rho, k}$ the map $u \mapsto \sum_{(i,j) \text{ edge}} u_{ij}$ is a homomorphism to $k$. For an additive character $\psi$ of $k$, put
$$\psi^{\sharp}(u) = \psi\Bigl(\sum_{(i,j) \text{ edge}} u_{ij}\Bigr).$$
The *symmetric level datum* $\mathcal{L}^{\sharp}(\psi)$, for characters $\psi_{\mathfrak{P}}$ of $k_{\mathfrak{P}}$ with $\mathfrak{P} \in P$, has $H = \prod_{\mathfrak{P}} U_{\rho, k}(k_{\mathfrak{P}})$ and $\psi_H = \prod_{\mathfrak{P}} \psi_{\mathfrak{P}}^{\sharp}$. The family $\psi$ is *generic* if each $\psi_{\mathfrak{P}}$ is nontrivial. This is the analogue, for the group $U_{\rho, k}$, of the generic characters of the unipotent radical that define Gelfand-Graev representations ([generic representations](/learn/representations/#generic-representations-and-local-factors)).

**Lemma 6.7.3 (Diagonal conjugation).** Let $k$ be a finite field, $\psi'$ and $\psi_0$ nontrivial additive characters of $k$, and $a_{ij} \in k^\times$ for each edge. Then there is a diagonal matrix $d = \mathrm{diag}(d_0, \dots, d_{r-1})$ with entries in $k^\times$ such that for all $u \in U_{\rho, k}$,
$$\psi'\Bigl(\sum_{(i,j) \text{ edge}} a_{ij} u_{ij}\Bigr) = \psi_0^{\sharp}(d^{-1} u d).$$

*Proof.* Since $\psi_0$ is nontrivial, $\psi'(x) = \psi_0(bx)$ for some $b \in k^\times$. The entries of $d^{-1}ud$ are $d_i^{-1} u_{ij} d_j$. So it is enough to have $d_i^{-1} d_j = b\, a_{ij}$ for every edge $(i,j)$. The edges form a forest on $\{0, \dots, r-1\}$: the path $0, \dots, \rho - 1$ is joined to the path $\rho + k, \dots, r - 1$ by the edge $(\rho - 1, \rho + k)$, and the path $\rho, \dots, \rho + k - 1$ is a separate component. On a forest we can choose $d$ at one vertex of each component and solve along the edges. $\square$

### Hida settings and rows

A *Hida setting* consists of a unitary group $G_X$, an open compact subgroup $K_2 \le G_X(\mathbb{A}_f)$ with a character $\chi_2$, a space $L^2_X$ of square integrable functions with a Haar measure, and an isomorphism $\iota : G(\mathbb{A}) \to G_X(\mathbb{A})$ that comes from a rational isomorphism of the groups. A *good operator* is an operator $R$ on $L^2_X$; the *good space* is the set of cusp forms $\varphi$ in the row space of the setting with $R(\bar\varphi) = \bar\varphi$.

The *first row* of a theta datum is a space $\mathcal{E}$ of linear maps $T$ from a discrete series model $\mathcal{H} = \bigotimes_\tau \mathcal{H}_\tau$ (finite-dimensional Hilbert spaces indexed by the archimedean places) into functions on $G(\mathbb{A})$ that are automorphic of level $(K, \chi)$, where $K = K(\beta_Y, \mathcal{L})$ is the level group of the self-dual frame $\beta_Y$ of the row and $\chi$ its character ([discrete series](/learn/representations/#discrete-series)). It carries a Petersson inner product $\langle T, T \rangle$. For $v_0 \in \mathcal{H}$ the *evaluation* of $T$ at $v_0$ is the function $g \mapsto T(v_0)(g)$.

**Definition 6.7.4 (Conjugate levels).** An element $t$ *conjugates* $(K, \chi)$ to $(K', \chi')$ if, for all $k$, $k \in K$ exactly when $t^{-1} k t \in K'$, and then $\chi'(t^{-1}kt) = \chi(k)$.

**Definition 6.7.5 (Evaluation tie).** For $t \in G(\mathbb{A})$ and $c \in \mathbb{R}$, the row $\mathcal{E}$ is *tied* to the good space at $t$ with constant $c$ if there are a vector $v_0 \in \mathcal{H}$ whose components have norm $1$ and a linear isomorphism $j$ from $\mathcal{E}$ onto the good space with
$$j(T)(x) = T(v_0)\bigl(\iota^{-1}(x)\, t\bigr) \text{ for almost all } x, \qquad \|j(T)\|^2 = c\, \langle T, T \rangle.$$

### The level of the row and the Hida level

Let $\Lambda_0$ be the base lattice of the first row space $V$, and let $K_2' = \iota^{-1}(1 \times K_2)$ be the Hida level viewed in $G(\mathbb{A})$, with character $\bar\chi_2 \circ \iota$.

**Lemma 6.7.6 (A frame for the Hida level).** Assume the level and group hypotheses on the theta datum, and let $\psi_0$ be a generic family of additive characters at the level places. Then there is a frame $\beta_3$ of $\Lambda_0$ such that $K_2' = K(\beta_3, \mathcal{L}^{\sharp}(\psi_0))$, and on this group $\bar\chi_2 \circ \iota = \chi(\beta_3, \mathcal{L}^{\sharp}(\psi_0))$.

Lean: `GlobalTheory.SeeConj.exists_frame_symLevel` (also `GlobalTheory.T.exists_frame_conjugate_level_symmetricLevel`, a second name).

*Proof.* The group hypotheses give a frame $\beta$ of $\Lambda_0$ whose reductions at the level places are a flag basis for the Hida level. In this frame, an element $\kappa$ with trivial archimedean part lies in $K_2'$ exactly when it preserves the lattice of $\beta$ and its upper left blocks at the level places lie in $U_{\rho,k}$. On $K_2'$ the character $\bar\chi_2$ is $\prod_{\mathfrak{P}} \psi'_{\mathfrak{P}}(\sum a_{\mathfrak{P}, ij} u_{ij})$ for some nontrivial $\psi'_{\mathfrak{P}}$ and some $a_{\mathfrak{P}, ij} \in k_{\mathfrak{P}}^\times$. Apply the lemma on diagonal conjugation at each level place to get $d_{\mathfrak{P}}$. Then rescale $\beta$ at the places in $P$ so that its reduction there is conjugated by $d_{\mathfrak{P}}$. This gives a frame $\beta_3$ of the same lattice. Since $d_{\mathfrak{P}}$ normalizes $U_{\rho,k}$, the level group of $\beta_3$ for $\mathcal{L}^{\sharp}(\psi_0)$ is $K_2'$, and its character is $\bar\chi_2$ by the choice of $d_{\mathfrak{P}}$. $\square$

**Theorem 6.7.7 (Conjugation of the row level).** Assume the level, group and model hypotheses on the theta datum. Then there is $t \in G^c_f$ that conjugates $(K_2', \bar\chi_2 \circ \iota)$ back to $(K, \chi)$: $k \in K$ exactly when $tkt^{-1} \in K_2'$, and then $\chi(k) = \bar\chi_2(\iota(tkt^{-1}))$. Also, $t\beta_Y$ is a frame of $\Lambda_0$.

Lean: `GlobalTheory.SeeConj.exists_conj_level` (also `GlobalTheory.T.exists_finite_element_conj_rowLevel_character`, a second name).

*Proof.* The group hypotheses give a generic family $\psi_0$ and a permutation $\pi$ that reorders the level datum $\mathcal{L}$ of the row into $\mathcal{L}^{\sharp}(\psi_0)$. Let $\beta_3$ be the frame of the previous lemma. Permuting $\beta_3$ by $\pi$ gives a frame $\beta_2$ of $\Lambda_0$ whose level group and character for $\mathcal{L}$ are those of $\beta_3$ for $\mathcal{L}^{\sharp}(\psi_0)$. The frame $\beta_Y$ is self-dual, so there is $t_0 \in G^c_f$ with $t_0\beta_Y$ a frame of $\Lambda_0$. The level places are pairwise not conjugate under $x \mapsto \bar{x}$. So the reductions at the different level places can be prescribed independently, and there is $u \in G^c_f$, preserving $\Lambda_0$, such that $u t_0 \beta_Y$ has the same reductions as $\beta_2$ at every level place. Put $t = u t_0$. Conjugation by $t$ carries $(K(\beta_Y, \mathcal{L}), \chi)$ to the level of $t\beta_Y$ for $\mathcal{L}$. This level is the level of $\beta_2$, since the two frames have the same reductions, and so it is $K_2'$ with $\bar\chi_2$. $\square$

**Theorem 6.7.8 (Evaluation tie from matching levels).** Assume the classification of discrete series of the archimedean unitary groups, the level, group, model and host hypotheses, and that the Hida setting uses the standard identifications. Let $R$ be a good operator and $t \in G^c_f$. Assume that $t^{-1}$ conjugates $(K, \chi)$ to $(K_2', \bar\chi_2 \circ \iota)$ and that the row level matches the Hida level at $t$: for $k \in K_2$, the element $t^{-1}\iota^{-1}(1,k)t$ lies in $K$ with $\chi$-value $\overline{\chi_2(k)}$, and right translation by these elements acts on the row through a reduction map to a finite group, compatibly with the coefficients. Then there is $c$ such that the row is tied to the good space at $t$ with constant $c$.

Lean: `GlobalTheory.SeeEval.evalTieT_of_levelMatch` (also `GlobalTheory.T.goodRows_compare_by_levelMatching_evaluation`, a second name).

*Proof.* By the classification of discrete series, there are isometries from the archimedean model spaces $\mathcal{H}_\tau$ onto the minimal $K$-types of the Hida setting. Let $v_0$ be the vector that corresponds to the fixed lowest weight vectors; its components have norm $1$. Translated evaluation $T \mapsto (x \mapsto T(v_0)(\iota^{-1}(x)t))$ is square integrable, with $\|\cdot\|^2 = c\langle T, T\rangle$ for a constant $c > 0$, by the unfolding of the Petersson product along $t$. There are three things to check. First, the image of $T$ lies in the good space. The translated evaluation lies in the row space by the level match, and the good operator fixes its conjugate, since on the image of the row the good operator is the good projector. Second, every element $\Phi$ of the good space is the image of some $T$. The conjugation of levels shows that $\Phi$ has the level of the row after translation by $t^{-1}$. The discrete series classification gives a $T$ in the multiplicity space with this evaluation. Then $T$ is in the row, since its post-projection vanishes when its evaluation agrees with its good projection. Third, the map is injective: if the evaluation vanishes almost everywhere, then $c\langle T,T\rangle = 0$, so $T = 0$. $\square$

**Theorem 6.7.9 (Row placement).** Under the hypotheses of the previous theorem, together with the pinning data, let $t_S \in G^c_f$. Assume that the conjugation of levels and the level match at any element of $G^c_f$ imply both at $t_S$. Then some $t \in G^c_f$ has the conjugation of levels and the level match, and there is $c$ such that the row is tied to the good space at $t_S$ with constant $c$.

Lean: `GlobalTheory.rowPlacement_exists` (also `GlobalTheory.T.exists_rowPlacement_finiteElement_matches_levels`, a second name).

*Proof.* The theorem on the conjugation of the row level gives $t$ with the conjugation of levels and with $t\beta_Y$ a frame of $\Lambda_0$. These two facts, with the pinning data, give the level match at $t$. By the assumption, both hold at $t_S$. The previous theorem at $t_S$ gives the evaluation tie. $\square$

**Remark 6.7.10 (Formalization).** The assumption that moves the two properties from any $t$ to $t_S$ is a hypothesis of the row placement theorem ([ExistsRowPlacementFiniteElementMatchesLevels.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsRowPlacementFiniteElementMatchesLevels.lean#L24)). The proof does not show that $t_S$ matches the levels; it assumes it. The first conclusion does not use $t_S$ or the discrete series classification. In the conjugation of the row level, the model hypothesis is never used ([ExistsFiniteElementConjRowLevelCharacter.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsFiniteElementConjRowLevelCharacter.lean#L18)). Each of the four theorems has a second name, whose proof applies the first name. The level match ([RowLevelMatch.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RowLevelMatch.lean#L42)) has three parts, and the evaluation tie uses only the first. The diagonal conjugation lemma, the existence of the flag frame, the surjectivity at non-conjugate places and the square integrability of translated evaluations are inputs we did not unfold. The edge sum in the lemma on diagonal conjugation is defined on all of $\mathrm{GL}_r(k)$, and it is a homomorphism only on $U_{\rho,k}$.
