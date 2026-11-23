---
title: Least values of theta generators at a level prime
decls:
  - GlobalTheory.DepthFromChars.depth_bound_of_chars
  - GlobalTheory.T.depth_bound_from_characters_pointDatum
  - GlobalTheory.PowGerm.lemmaBT_of_characters
  - GlobalTheory.PowGerm.lemmaBT_of_hodgeTate_chart
  - GlobalTheory.T.depthBelowOne_of_hodgeTate_chart_form
  - GlobalTheory.LevelPrimePoint.least_value_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Least values of theta generators at a level prime

The pointwise bounds of the earlier sections hold at a real place. This section proves a bound of the same kind at a finite place: at an integral point over a complete discrete valuation ring of residue characteristic dividing the level, some theta generator of weight $a$ has a small valuation. The bound is $\mathrm{DF}(a)\, v(g)/(g-1)$ plus two small error terms. The main input is a statement on $p$-adic formal groups: a fixed multiple of every tangent vector is a combination of differentials of characters. The section builds the bound in three layers: a bound from characters at a point, a bound for products of minors on power data, and the bound for theta generators. The last one is used by the step [every character from the literature](/step/every-character-of-literature/).

### Characters of formal groups

Let $O$ be a commutative ring and $F$ a [formal group law](/learn/formal-groups/#formal-group-laws) of dimension $d$ over $O$. A *character* of $F$ is a power series $u(X_1, \dots, X_d)$ over $O$ with constant term $1$ and $u(F(X, Y)) = u(X)\, u(Y)$; it is a homomorphism from $F$ to the multiplicative formal group. Its *differential* $\mathrm{dl}(u) \in O^d$ is the vector of the coefficients of $X_1, \dots, X_d$ in $u$.

**Definition 5.7.1 (Hodge-Tate chart statement).** Let $p$ be a prime. The *Hodge-Tate chart statement at $p$* says the following. Let $T$ be a complete noetherian local domain of characteristic $0$ in which $p$ is not a unit. Let $G$ be a commutative group over $T$ with degeneration data, a polarized abelian variety over the fraction field, a uniformization and a chart by a formal group law $F$ of dimension $d$. Let $C$ be an algebraically closed field of characteristic $0$ with a valuation $v : C \to \mathbb{R}_{\ge 0}$ and ring of integers $O$, $p$-adically complete with $p$ not a unit, and let $T \to O$ be a local map. Then there are characters $u_1, \dots, u_N$ of the image of $F$ over $O$ such that for every $c \in O$ with $v(c)^{p-1} \le v(p)$,
$$c\, O^d \subseteq \mathrm{span}_O\bigl(\mathrm{dl}(u_1), \dots, \mathrm{dl}(u_N)\bigr).$$

The bound $v(c)^{p-1} \le v(p)$ is the bound $|c| \le |p|^{1/(p-1)}$. It has the shape of the classical result that the cokernel of the Hodge-Tate map of a [$p$-divisible group](/learn/formal-groups/#p-divisible-groups) is killed by $p^{1/(p-1)}$; see [Hodge-Tate representations](/learn/padic-hodge/#admissible-representations-and-hodge-tate-representations). We have not checked that the statement is that result.

### The bound from characters

Fix a CM field $E$ with a host and an integral point $y$ over an algebraically closed field $F$ of characteristic $0$ with additive valuation $v$ and ring of integers $O_v$. The point carries a tangent action $c \mapsto \mathrm{dAct}(c)$ of $\mathcal{O}_E$ on $F^d$. For a prime $p$ and $a \in \mathcal{O}_E$ with $a\bar a = p$, an *eigenframe at $a$* is a finite set $\mathcal{T}$ of characters $\tau : \mathcal{O}_E \to O_v$ with ranks, vectors $e_{t,i} \in O_v^d$ with $\mathrm{dAct}(c) e_{t,i} = \tau_t(c) e_{t,i}$, dual vectors $\lambda$ with $\lambda_{l} \cdot e_{l'} = \delta_{l l'}$, and elements $\varepsilon_t \in \mathcal{O}_E$ with $\tau_{t'}(\varepsilon_t) \equiv \delta_{t t'} \pmod p$.

**Definition 5.7.2 (Character hypothesis).** The *character hypothesis* says: for every prime $p$, every such point with $O_v$ $p$-adically complete and $p$ not a unit, every $a$ with $a \bar a = p$ and $ua + u'\bar a = 1$ for some $u, u'$, every eigenframe at $a$ with $\tau_t(a) \in pO_v$ for all $t$, every $c \in O_v$ with $(p-1)v(c) = v(p)$, and injective column maps $\mathrm{col}_t$ into $\{1, \dots, n\}$, there are $y_{l,b} \in O_v$ such that each column is the tangent value of a character on the $a$-torsion, and each leading minor of size $s+1$ of each block has valuation at most $(s+1)v(c)$.

**Theorem 5.7.3 (Depth bound from characters).** Assume the four groups of laws used by the point data, namely `Laws`, `Laws2`, `Laws4` and the twisted base change statement, and the character hypothesis. Let $p$ be a prime and $y$ a point as above, reduced with constants $(r, b, C_c, M_0)$, with a Tate isomorphism. Let $a \in \mathcal{O}_E$ with $a\bar a = p$ and a Bezout relation, and $k$ coprime to $p$. Let $\mathcal{T}$ be an eigenframe at $a$ and $V \subseteq \mathcal{T}$ with $\tau_t(a) \in pO_v$ for $t \in V$ and $\tau_t(a)$ a unit for $t \notin V$. Let $S \subseteq \{1, \dots, n\}$, injective column maps with $\mathrm{col}_t(i) \in S$ exactly when $t \in V$, and multiplicities $m_{t,s}$ with
$$D = \sum_t \sum_s m_{t,s}(s+1), \qquad D < p - 1, \quad 4D + 4 \le k, \quad D M_0 < k .$$
Let $h$ be a canonical gauge and $v(p) = e_p$. Then there are families $s, s', t$, power series $f$ and $\gamma \in \mathbb{Q}$ with the four germ properties at each column, such that the value of the minor product of $f$ at $kp$ has valuation $\gamma$ and
$$\gamma \le \frac{D\, e_p}{p - 1} + \frac{|S|\, r\, C_c}{4k} + \frac{D^2 C_c}{k} .$$

Lean: `GlobalTheory.DepthFromChars.depth_bound_of_chars` (also `GlobalTheory.T.depth_bound_from_characters_pointDatum`, a second name).

*Proof.* Put $\theta = e_p/(p-1)$ and choose $c \in O_v$ with $v(c) = \theta$, so $(p-1)v(c) = v(p)$. Split the multiplicities into $m_1$, supported on $V$, and $m_2$, supported off $V$. Apply the character hypothesis to the part of the frame in $V$. It gives column values whose leading minors of size $s+1$ have valuation at most $(s+1)\theta$; weighted by the multiplicities, these give the term $D e_p/(p-1)$ at most. A chain of lemmas on germs, jets and pullbacks then builds $s, s', t$ and $f$ with the four germ properties, and bounds the valuation of the minor product by the sum of this term and two error terms that come from the reduction constants and from $k$. $\square$

### Products of minors on power data

**Definition 5.7.4 (Minor bound).** The *minor bound* is the statement that, for an integral point $y$ of a PEL moduli space over a complete discrete valuation ring $T$ with a chart, a truncation and a uniformization with a torsion isomorphism, a uniformizer $\varpi$ and a quadratic form $Q$, two distinct odd primes $g, g'$ with $g = \pi\bar\pi$, $g' = \pi'\bar\pi'$ and Bezout relations for both, $g$ totally split in $E$ and not a unit in $T$, a basis $b_1, \dots, b_r$ with $Q(b_j) \le \Phi$ and $|Q(b_j + z) - Q(b_j) - Q(z)| \le M_0 Q(z)$, power data of rank $n_1 + n_2 \ge 1$, and multiplicities $m$ of degree $D$ with
$$D < g - 1, \qquad 4D + 4 \le g', \qquad D M_0 < g',$$
there are nine objects with their properties and a rational $\rho$ that is the valuation of a product of minors, split by the sign of $v(\tau(\bar\pi))$, with
$$\rho \le \frac{v(g)\, D}{g-1} + \frac{n_1 r \Phi}{4g'} + \frac{2D^2\Phi}{g'} .$$

**Theorem 5.7.5 (Minor bound from characters).** Assume `Laws`, `Laws2`, `Laws4`, the twisted base change statement and the character hypothesis. Then the minor bound holds.

Lean: `GlobalTheory.PowGerm.lemmaBT_of_characters`.

*Proof.* Step 1. The star on $\mathcal{O}_E$ is the conjugation of the host. A lemma gives the embeddings $\tau$, the eigenvectors, dual vectors and idempotents at $g$, and the fact that $v(\tau(x)) > 0$ exactly when $\tau(x) \in gO$.

Step 2. A lemma gives a chart point and a transfer to the power data, and matches the two tangent actions.

Step 3. The product of the two minor factors is a product of leading minors in injective columns, with multiplicities of total degree $D$. Choose a canonical gauge.

Step 4. Apply the depth bound from characters with $p = g$, $a = \bar\pi$, $k = g'$, $S$ the first $n_1$ columns and degree $D$. This gives $\gamma$ with $\gamma \le D v(g)/(g-1) + |S| r\Phi/(4g') + D^2\Phi/g'$.

Step 5. The transfer carries the result to the power data and gives the nine properties.

Step 6. The minor product has valuation $\gamma$. This uses a lemma on local rings: if $xy$ is not a unit and $ux + u'y = 1$, then $x$ is a unit exactly when $y$ is not. So exactly one of $\tau(\pi)$ and $\tau(\bar\pi)$ has positive valuation, and the split of the columns matches.

Step 7. $|S| = n_1$ and $D^2\Phi/g' \le 2D^2\Phi/g'$. $\square$

**Theorem 5.7.6 (Minor bound from the Hodge-Tate chart).** If the Hodge-Tate chart statement holds at every prime $p$, then the minor bound holds.

Lean: `GlobalTheory.PowGerm.lemmaBT_of_hodgeTate_chart` (also `GlobalTheory.T.depthBelowOne_of_hodgeTate_chart_form`, a second name).

*Proof.* This is Theorem (Minor bound from characters) applied to `Laws`, `Laws2` and `Laws4` from the first laws, the twisted base change statement, and the character hypothesis, which a lemma derives from the Hodge-Tate chart statement. $\square$

### Theta generators

Fix the datum $D_w$ of signature $(p, q)$, a level $l$ and coefficients. For a weight $a = (a(\tau, i))$ put $\mathrm{DF}(a) = \sum_\tau \sum_{i < m_\tau} a(\tau, i)$, with $m_\tau$ the multiplicity of $\tau$. A *theta generator* of weight $a$ and size $n$ is a rule $f$ for which there are a vector $x$ of $n$ lattice points and a harmonic polynomial $P$ of weight $a$ such that the value of $f$ at each point is the theta value of $(x, P)$. We have not unfolded the theta value. For a complete discrete valuation ring $T$ with valuation $v_T$ and $e > 0$, put $\mathrm{nval}_e(x) = v_T(x)/e$.

**Theorem 5.7.7 (Least value of theta generators).** Assume the Hodge-Tate chart statement at every prime. Let $\nabla$ be a theta value map with the two theta value conditions. Let $y$ be an integral point over $T$, with a chart, a truncation and a uniformization with a torsion isomorphism. Let $\varpi$ be a uniformizer, $Q$ a quadratic form and $b_1, \dots, b_r$ a basis with $Q(b_j) \le \Phi$ and $|Q(b_j + z) - Q(b_j) - Q(z)| \le M_0 Q(z)$. Let $g \ne g'$ be primes with $l.M = g'g$, $\pi\bar\pi = g$, $\pi'\bar\pi' = g'$ and $l.M_b = (\pi\pi')$, with $g$ totally split in $E$ and not a unit in $T$. Let $a$ be antitone in $i$ for each $\tau$, and let $n \ge 2(p+q)$, $n \ge 1$, $e > 0$, $\mathrm{DF}(a) < g - 1$, $4\mathrm{DF}(a) + 4 \le g'$ and $\mathrm{DF}(a) M_0 < g'$. Then
$$\begin{aligned}&\inf_{f} \mathrm{nval}_e(f(y)) + \mathrm{nval}_e\Bigl(\prod_\tau \iota\bigl(\tau(\bar\pi\bar\pi')\bigr)^{\sum_i a(\tau, i)}\Bigr) \\ &\quad \le \frac1e \Bigl(\frac{v_T(g)\,\mathrm{DF}(a)}{g-1} + \frac{(p+q) r \Phi}{4g'} + \frac{2\,\mathrm{DF}(a)^2 \Phi}{g'}\Bigr),\end{aligned}$$
where $f$ runs over the theta generators of weight $a$ and size $n$.

Lean: `GlobalTheory.LevelPrimePoint.least_value_le`.

*Proof.* Step 1. The level relation gives Bezout relations for $\pi\pi'$ and $\bar\pi\bar\pi'$, and for $\pi$ and $\bar\pi$.

Step 2. Extend $T$ to an algebraically closed valued field $F$ with ring $O$. Take a Tate isomorphism for the chart and power data on $(p+q) + n_2$ copies.

Step 3. For each $\tau$ exactly one of $v(\tau(\bar\pi)) > 0$ and $v(\bar\tau(\bar\pi)) > 0$ holds. This chooses a type for each $\tau$.

Step 4. A lemma gives a harmonic polynomial of weight $a$ that is a product of leading minors of total degree $\mathrm{DF}(a)$.

Step 5. The minor bound from the Hodge-Tate chart bounds the valuation $\rho$ of this minor product by the right side, before division by $e$.

Step 6. A lemma on copies writes the value of valuation $\rho$ as $\sum_i \alpha_i z_i$ with $v(\alpha_i) \ge 0$, so some $z_i$ has $v(z_i) \le \rho$.

Step 7. A translation lemma gives $z_i = \varepsilon A\, f(y)$ for a theta generator $f$, with $A$ the product over $\tau$. Dividing by $e$ gives the bound for the infimum. $\square$

**Remark 5.7.8 (Formalization).** The least value bound is in [ThetaGeneratorsLeastValueOverLevelPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/ThetaGeneratorsLeastValueOverLevelPrime.lean#L196); the Hodge-Tate chart statement `HTFSt` is used only at line 270, and it is proved by `hodgeTate_inclusion_chart` in [HodgeTateInclusionChartCharacters.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/HodgeTateInclusionChartCharacters.lean#L49). The minor bound is `LemmaBT` in [JetsOnCopiesCompatibleFrames.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/JetsOnCopiesCompatibleFrames.lean#L551). The proof of the minor bound from characters in [IsUnitIffNotIsUnitOfCoprime.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/IsUnitIffNotIsUnitOfCoprime.lean#L50) does not use that $g$ and $g'$ are odd, the relation $\pi'\bar\pi' = g'$ with its Bezout relation, the bound $1 \le n_1 + n_2$, or the algebraicity of $y$, and the factor $2$ in its last term is slack. In [DepthBoundFromCharactersPointDatum.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthBoundFromCharactersPointDatum.lean#L28), `Laws2` is bound to `_` at line 29 and not used. The second name `depthBelowOne_of_hodgeTate_chart_form` speaks of depth, but no notion of depth appears in its statement. We did not open the germ lemmas, so the proofs above follow their statements. We have not unfolded `CharAt`, `nabValN`, `minorProd`, `IsNab`, `IsQ`, `FrTrunc`, `TorsionIso` or the four germ properties.
