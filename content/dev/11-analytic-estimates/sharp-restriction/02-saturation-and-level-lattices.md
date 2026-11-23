---
title: Restricted saturation and level lattices
decls:
  - Formalism.InvariantFactorPaths.L4.restricted_saturation_holds
  - Formalism.InvariantFactorPaths.L4.sat_main
  - Formalism.InvariantFactorPaths.KP.Top.levelLattice
  - Formalism.InvariantFactorPaths.MC.Top.theoremMV7
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Restricted saturation and level lattices

This section proves two lattice statements about the spaces of polynomials in many letters that carry the tie operators of the chapter on character sums. The first is a saturation theorem: an integral polynomial that is free of the last variable and satisfies the restricted threshold conditions is, after multiplication by an explicit power of $p$, the restriction of an integral polynomial of the full constrained space $Y$. It feeds [the Gram hypothesis from a log bound](/entry/gram-hypothesis-of-log-bound/). The second compares two lattices built from tie levels, one spanned by plain products and one spanned by harmonic projections, up to an explicit power of $p$. It feeds [the restriction theorem for level lattices](/entry/rest-ll-of/). Last, the section records the averaged bad count bound under the name that its user calls. The tools are [[discrete valuation ring|MGM3CNJW9V]] lattices ([lattices over discrete valuation rings](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices)) and [divided powers](/learn/combinatorics/#binomial-coefficients-factorials-and-divided-powers).

We use the notation of Definitions 6.7.1 and 6.7.2 of the chapter on character sums (see [the mean bad count](/entry/mc-theorem-mv7/)). Letters $L$ of length $N$ give each row $j < N$ a sign $v_j \in \{+, -\}$ and a degree $d_j$, with $|L| = \sum_j d_j$. The variables are $x_{j,c}$ with $j < N$ and colours $c < r$. $\mathrm{Pol}(L) \subseteq \mathbb{Q}_p[x]$ is spanned by the monomials of row degrees $d_j$, $\mathrm{Pol}_{\mathbb{Z}}(L)$ is its intersection with $\mathbb{Z}_p[x]$, the operators $e^{(j)}_{cd}$ act through the first $j$ rows, and $\mathrm{YCond}(j, M)$ is the largest subspace stable under all $e^{(j)}_{cd}$ that is spanned by monomials with $\mathrm{wt}_j(0, m) \leq M$. Thresholds $(J_k, M_k)_{k < q}$ with $M_k \in \mathbb{Z} \cup \{\infty\}$ define $Y(L) = \mathrm{Pol}(L) \cap \bigcap_k \mathrm{YCond}(J_k, M_k)$.

### Restricted saturation

Let $N = K + 1$, so that row $K$ is the last row, and let $\rho = r - 1$ be the last colour.

**Definition 8.2.1 (Restricted space).** For a set $S$ of colours, $j \leq N$ and $M \in \mathbb{Z} \cup \{\infty\}$, let $\mathrm{Types}_{\leq M}(j, S)$ be the sum of the isotypic components, for the operators $e^{(j)}_{cd}$ with $c, d \in S$, whose highest weight $\lambda$ has $\lambda_0 \leq M$. The *restricted space* $X(L)$ is the set of $x \in \mathrm{Pol}(L)$ that do not involve the variable $x_{K, \rho}$ and lie, for each $k$, in
$$\begin{cases} \mathrm{YCond}(K, M_k) \cap \mathrm{Types}_{\leq M_k}(K + 1, \{0, \dots, r - 2\}) & \text{if } K + 1 \leq J_k, \\ \mathrm{YCond}(J_k, M_k) & \text{otherwise.} \end{cases}$$
For $h \in \mathbb{Q}_p[x]$, the *initial part* $h|_{x_{K,\rho} = 0}$ is the sum of the terms of $h$ that do not involve $x_{K, \rho}$.

Lean: `Formalism.InvariantFactorPaths.L4.XSp` (also `Formalism.InvariantFactorPaths.L4.TypesLE`, `Formalism.InvariantFactorPaths.L4.FreeOf`).

Saturation asks which integral points of $X(L)$ are, up to a bounded power of $p$, initial parts of integral points of $Y(L)$.

**Theorem 8.2.2 (Restricted saturation).** Let $p$ be a prime, $r \geq 2$, $\rho = r - 1$, and let $L$ be letters of length $K + 1$ with $v_K = +$. Put
$$c_0 = 2 \binom{r}{2} \lfloor \log_p (4|L| + r - 1) \rfloor.$$
For every $x \in X(L) \cap \mathbb{Z}_p[x]$ there is $h \in Y(L) \cap \mathbb{Z}_p[x]$ with $h|_{x_{K,\rho} = 0} = p^{c_0} x$.

Lean: `Formalism.InvariantFactorPaths.L4.restricted_saturation_holds`.

The main case is the following.

**Proposition 8.2.3 (Saturation at a minimal threshold).** Let $r = s + 1$ with $s \geq 1$ and $v_K = +$. Let $k_0$ be an index with $K + 1 \leq J_{k_0}$ and $M_{k_0} = c \in \mathbb{Z}$, such that $M_{k_0} \leq M_k$ for every $k$ with $K + 1 \leq J_k$, and assume $c < |L|$. Then for every $x \in X(L) \cap \mathbb{Z}_p[x]$ there is $h \in Y(L) \cap \mathbb{Z}_p[x]$ with $h|_{x_{K,\rho} = 0} = p^{c_0} x$, with $c_0$ as in the theorem.

Lean: `Formalism.InvariantFactorPaths.L4.sat_main`.

*Proof (outline).* Put $D = \binom{s+1}{2} \lfloor \log_p(4|L| + s) \rfloor$, so that $c_0 = 2D$. There is an action of $\mathfrak{gl}_{s+1}$ on the polynomials in which the indices $1, \dots, s$ are the colours $0, \dots, s - 1$ through all $K + 1$ rows, and the index $0$ is carried by the last row: its weight on a monomial $m$ is $c - \sum_a m(K, a)$, its raising and lowering operators are built from derivatives in the last row. The polynomial $x$ is a sum of isotypic pieces $f_\lambda$ for this action, and each piece has highest weight with first entry at most $c$. For each $\lambda$, an integrality bound for isotypic projections and an integrality bound for the Weyl lattice of type $\lambda$ each cost a factor $p^D$, so $p^{2D} f_\lambda$ lies in an integral lattice $M_2$ of polynomials that extend to $Y(L)$. Summing over $\lambda$ gives $p^{2D} x \in M_2$, and the lifting property of $M_2$ gives $h$. $\square$

The exponent $D$ is the sandwich exponent $e(p, s + 1, 4|L|)$ of the first section.

*Proof of the theorem.* Write $r = s + 1$; then $s \geq 1$ and $\rho$ is the last colour. Suppose first that some $k$ has $K + 1 \leq J_k$ and $M_k < |L|$. Among the $k$ with $K + 1 \leq J_k$ choose $k_0$ with $M_{k_0}$ least. Then $M_{k_0} < |L|$, so $M_{k_0} = c$ is an integer with $c < |L|$, and the proposition applies. Otherwise every $k$ with $K + 1 \leq J_k$ has $M_k \geq |L|$. Every monomial $m$ of $\mathrm{Pol}(L)$ has $\mathrm{wt}_j(0, m) \leq |L|$, so $\mathrm{Pol}(L) \subseteq \mathrm{YCond}(J_k, M_k)$ for these $k$. For the other $k$ the condition on $x$ is the condition of $Y(L)$. Hence $x \in Y(L)$, and $h = p^{c_0} x$ works, since $x$ does not involve $x_{K,\rho}$. $\square$

### Level lattices

*Block data* consist of letters $L$ of length $N$, tie data $T$ (positions $\mathrm{pos}_i$ and shifts $z_i$ for $i < t$, and thresholds $(J_k, M_k)$), a row $u < N$, a bound $B$ and a shift $z_+$. They are *admissible* if $T$ is admissible for $L$ (Definition 6.7.2 of the chapter on character sums), $\mathrm{pos}_i + 1 < u$ for all $i$, $v_u = +$ and $u + 1 = N$. A *level* is a pair $(j, j_+)$ with $j \in \mathbb{N}^t$, $j_i \leq d_{\mathrm{pos}_i}$, $j_i \leq d_{\mathrm{pos}_i + 1}$ and $j_+ \leq \min(d_u, B)$. The letters $L(j, j_+)$ have the same signs as $L$, and the degree of row $a$ is lowered by $j_i$ for each $i$ with $a \in \{\mathrm{pos}_i, \mathrm{pos}_i + 1\}$ and by $j_+$ if $a = u$.

The polynomials now live in more variables: the variables $x_{a,c}$ of the rows $a < N$, an extra row $\xi_c$ ($c < r$), and two scalar variables $\zeta_i, \sigma_i$ for each $i \leq t$, where the index $i = t$ belongs to the pair $(u, \xi)$. For two rows $w, e$ the *tie operator* is $\tau_{we} = \sum_{c < r} \partial_{x_{w,c}} \partial_{x_{e,c}}$, and for scalar variables $\zeta, \sigma$ put $\hat{E}_{we} = \zeta \sigma + \sum_{c < r} x_{w,c}\, x_{e,c}$. For degrees $o, n$ and a shift $z$, the *projection* of a polynomial $y$ is
$$P^{o,n,z}_{we}(y) = \sum_{l = 0}^{o} \frac{(-1)^l}{(l!)^2 \binom{o + n + r + z - 1}{l}}\, \hat{E}_{we}^{\,l}\, \tau_{we}^{\,l} (\zeta^z y).$$
The alternating sum removes, term by term, the part of $\zeta^z y$ that the tie operator detects, in the manner of the classical projection onto harmonic polynomials.

**Definition 8.2.4 (Level lattices).** Put $\hat{E}_i = \zeta_i \sigma_i + \sum_c x_{\mathrm{pos}_i, c}\, x_{\mathrm{pos}_i + 1, c}$ for $i < t$ and $E_+ = \zeta_t \sigma_t + \sum_c x_{u,c}\, \xi_c$. For a level $(j, j_+)$, let $P_{j, j_+}$ be the composite of the projections $P^{o_i, n_i, z_i}$ at the tie pairs $(\mathrm{pos}_i, \mathrm{pos}_i + 1)$, with $o_i, n_i$ the degrees of these rows in $L(j, j_+)$, followed by the projection $P^{d_u - j_+,\, B - j_+,\, z_+}$ at the pair $(u, \xi)$. For $y \in Y(L(j, j_+)) \cap \mathbb{Z}_p[x]$ and an integral polynomial $g$ in the $\xi_c$ alone, homogeneous of degree $B - j_+$, the *plain product* and the *projected product* are
$$\begin{aligned} &\prod_i \hat{E}_i^{\,j_i} \cdot E_+^{\,j_+} \cdot \prod_i \zeta_i^{z_i} \cdot \zeta_t^{z_+} \cdot y\, g, \\ &\prod_i \hat{E}_i^{\,j_i} \cdot E_+^{\,j_+} \cdot P_{j, j_+}(y\, g). \end{aligned}$$
The lattice $S_{\mathbb{Z}}$ is the $\mathbb{Z}_p$-span of all plain products over all levels, and $P_{\mathbb{Z}}$ is the $\mathbb{Z}_p$-span of all projected products.

Lean: `Formalism.GM.M.BlockData.SSZ` (also `Formalism.GM.M.BlockData.PSZ`, `Formalism.GM.M.BlockData.Pall`, `Formalism.GM.M.tieP`).

**Theorem 8.2.5 (Level lattices).** Let $p$ be a prime, $r \geq 1$, $a \geq 1$, and let the block data be admissible with $d_x \leq 2a$ for all rows, $B \leq 2a$, $z_i \leq 2a$ and $z_+ \leq 2a$. Assume that for all $j \in \mathbb{N}^t$ and $j_+ \in \mathbb{N}$:

1. the tie operator of the pair $(\mathrm{pos}_i, \mathrm{pos}_i + 1)$ maps $Y(L(j, j_+))$ into $Y(L(j + e_i, j_+))$, for each $i < t$;
2. each derivative $\partial_{x_{u,c}}$ maps $Y(L(j, j_+))$ into $Y(L(j, j_+ + 1))$.

Put $\kappa = \lceil (r + 1)(\log_p(8a + r) + 1) \rceil$. Then $S_{\mathbb{Z}}$ and $P_{\mathbb{Z}}$ span the same $\mathbb{Q}_p$-space, and
$$p^{(t+1)\kappa} S_{\mathbb{Z}} \subseteq P_{\mathbb{Z}}, \qquad p^{(t+1)\kappa} P_{\mathbb{Z}} \subseteq S_{\mathbb{Z}}.$$

Lean: `Formalism.InvariantFactorPaths.KP.Top.levelLattice` (also `Formalism.GM.M.LevelLattice`).

*Proof (outline).* There is a chain of $\mathbb{Z}_p$-lattices $M_0, M_1, \dots, M_t$, where $M_k$ is spanned over all levels by the products $\prod_i \hat{E}_i^{\,j_i} \cdot E_+^{\,j_+} \cdot \prod_{i < k} \zeta_i^{z_i} \cdot \zeta_t^{z_+} \cdot Q$, with $Q$ the image of $y g$ under the projections at the tie pairs $i \geq k$. The lattice $M_+$ is spanned in the same way with all projections applied, including the one at $(u, \xi)$. The ends are $M_t = S_{\mathbb{Z}}$ and $M_+ = P_{\mathbb{Z}}$. Let $u$ be an integer with $r \lfloor \log_p(2a) \rfloor + \lfloor \log_p(6a + r) \rfloor \leq u$. The tie step says that $p^{u} M_{k+1} \subseteq M_k$ and $p^{u} M_k \subseteq M_{k+1}$ for each $k < t$; it uses hypothesis 1 and the bounds $d_x, z_i \leq 2a$. The plus step says that $p^{u} M_0 \subseteq M_+$ and $p^{u} M_+ \subseteq M_0$; it uses hypothesis 2 and the bounds $d_x, B, z_+ \leq 2a$. The number $u = \kappa$ satisfies the inequality, since $(r + 1)(\log_p(8a + r) + 1)$ is at least $r(\lfloor \log_p(2a) \rfloor + 1) + \lfloor \log_p(6a + r) \rfloor + 1$. Composing the $t$ tie steps with the plus step gives $p^{(t+1)\kappa} S_{\mathbb{Z}} \subseteq P_{\mathbb{Z}}$ and $p^{(t+1)\kappa} P_{\mathbb{Z}} \subseteq S_{\mathbb{Z}}$. Since $p$ is a unit in $\mathbb{Q}_p$, each inclusion gives an inclusion of the rational spans, so the two spans are equal. $\square$

### The averaged bad count

**Theorem 8.2.6 (Mean bad count on a progression grid).** The statement of [Theorem 6.7.12](/entry/mc-theorem-mv7/) holds.

Lean: `Formalism.InvariantFactorPaths.MC.Top.theoremMV7` (also `Formalism.InvariantFactorPaths.MC.theoremMV7`).

*Proof.* This is [Theorem 6.7.12](/entry/mc-theorem-mv7/) under a second name. $\square$

Its user is [the alternative mean value theorem](/entry/alternative-mean-value-theorem/).

**Remark 8.2.7 (Formalization).** The saturation theorem is `ResSatLThm` in [StatementG.lean](lean:Formalism/ThetaLogCoordinates/FockResolutionOnto/StatementG.lean#L1), with the restricted space in [ShiftLastLetterThresholds.lean](lean:Formalism/ThetaLogCoordinates/FockResolutionOnto/ShiftLastLetterThresholds.lean#L24). Both proofs are in [RestrictedSaturationHolds.lean](lean:Formalism/ThetaLogCoordinates/FockResolutionOnto/FockMonomialProofs/RestrictedSaturationHolds.lean#L49). The proposition uses `gl_action_exists`, `wtot_le_iso`, `typeInt`, `weylInt` and `restrictedLattice_exists_lift`; we have not opened their proofs, and the outline names only their roles. The isotypic components `IsoC` were not unfolded. In the second case of the theorem any power of $p$ works, since $x$ itself lies in $Y(L)$. The level lattice theorem is `LevelLattice` in [LevelLattice.lean](lean:Formalism/MahlerMeasure/LevelLattice.lean#L34); the brief places it in a file `FinalL.lean`, but the term is in [FinalLL.lean](lean:Formalism/ThetaLogCoordinates/BihomogeneousPairs/FinalLL.lean#L22), where it is `LevelLattice_of midTop midPEq stepTie stepPlus`. The proof is `LevelLattice_of` in [LevelLatticeOf.lean](lean:Formalism/ThetaLogCoordinates/BihomogeneousPairs/LetterChainEmbeddings/LevelLatticeOf.lean#L60); we opened only this assembly, not the proofs of the tie step and the plus step, so the outline states their conclusions only. Here $\log_p$ is the real logarithm, not its integer part. The mean bad count under the second name is in [LatticeTheoremEps28Valid.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/LatticeTheoremEps28Valid.lean#L7), a file of nine lines whose name mentions $\varepsilon$ and $28$, neither of which occurs in it.
