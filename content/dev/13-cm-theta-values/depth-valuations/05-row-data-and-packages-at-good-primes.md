---
title: Row data and packages at good primes
decls:
  - GlobalTheory.RowAt.supplyC_selfConj
  - GlobalTheory.T.rowData_supplied_at_selfConjugate_places
  - GlobalTheory.RowAt.supply_pairs
  - GlobalTheory.T.rowData_supplied_at_pairs_of_places
  - GlobalTheory.PkgConj.exists_rowFam
  - GlobalTheory.PkgConj.packages_conj
  - GlobalTheory.T.packages_exist_frobeniusComplexConjugation
  - GlobalTheory.goodPrime_packages
  - GlobalTheory.T.allGoodPrimeDepthDataExist_proof
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Row data and packages at good primes

This section proves that the character statement for formal groups, at all primes, gives a package of local data at every integral point of a unitary moduli space above a good prime. A package records row data on the formal group of the point, weights, and a lower bound for a valuation $\nu$ by blocks of jets. We build row data at self-conjugate places and at pairs of places, then the packages where Frobenius acts as complex conjugation, then the packages at all good primes. The package statement is used in the [depth bound at good leaves](/entry/leaf-depth-good-of-chart-form/), which is the next section.

### The character statement and the package statement

We keep the unitary moduli spaces of the earlier chapters. So $E$ is a CM field with a host datum, $D_w$ is a Hermitian datum of signature $(p, q)$, $l$ is a level of odd modulus $M \geq 3$, $X$ is the moduli space and $F$ is the coefficient field. For an embedding $\tau : E \to \mathbb{C}$ let $\mathrm{mult}(\tau)$ be the rank of the $\tau$-eigenspace of $\mathcal{O}_E$ on the tangent space. Formal groups and characters are as in [formal group laws](/learn/formal-groups/#formal-group-laws).

**Definition 4.5.1.** Let $p$ be a prime. The *character statement at $p$* says the following. Let $G$ be a formal group law over a complete local domain of characteristic $0$, with a chart onto a group with degeneration data and an action of an order $\mathcal{O}$ with $p \nmid \operatorname{disc} \mathcal{O}$. Let $O$ be a $p$-adically complete valuation ring in an algebraically closed field of characteristic $0$. Let $w$ be a place of $\mathcal{O}$ over $p$ of degree $n$, with embeddings $\tau_0, \dots, \tau_{n-1}$ into $O$ such that $\tau_{j+1}(x) \equiv \tau_j(x)^p$ modulo the maximal ideal. Let $r(\tau)$ be the rank of the $\tau$-eigenspace on the tangent space. Then for each $j$ there are finitely many characters of $G$ whose linear terms, paired with a basis of the $\tau_j$-eigenspace, give a cokernel of size at least
$$|p|^{\sum_{n' \geq 0} p^{-(n'+1)}\, r(\bar\tau_{j+n'+1})}.$$
The indices are taken modulo $n$. The size of a module $\bigoplus_i O/(c_i)$ is $\prod_i |c_i|$.

A *row datum* over a valued field $C$ is a table of jets of characters, with $n$ columns and $m$ rows, indexed by a sign $g \in \{0, 1\}$ and a label $s$, with a rank $\operatorname{rk}(g, s)$ for each pair and a flag that orders the jets. The *block bound* for a family of row data, an integer $n_W$, weights $\gamma$ and a real number $\nu$ says the following. For every choice of blocks on the rows, where each block attains its value, each block lies on one sign, twice the total width is at most $n_W$, and the block weights at each label add up to $\gamma$, the number $\nu$ is at most the sum of the block values.

For a rank $r$ and a weight $b$ the *gap weight* is $\mathrm{gap}(r, b)(i) = b(i - 1) - b(i)$ for $1 \leq i \leq r$, with $b(r)$ read as $0$, and $\mathrm{gap}(r, b)(i) = 0$ for other $i$.

A *good point* consists of a numerical datum $N$, an index $j$, an embedding datum tied to $N$, a dominant weight $a$, a prime $\lambda$ of $F$ whose residue characteristic $\ell$ is not small and is prime to $M$, a complete discrete valuation ring $T$ over $\lambda$ with ramification index $e_\lambda$, an algebraic integral point $y$ of $X$ over $T$ with a chart, an integer $n_W$ and a real number $\nu$ with $e_\lambda \nu \leq \nu_{\mathrm{loc}}$. Here $\nu_{\mathrm{loc}}$ is the local depth of the chart, an infimum of normalized valuations.

**Definition 4.5.2.** The *package statement* for $X$ and $F$ is the conjunction of seven statements, each of the form "at every good point with $\ell$ in a given class and $n_W$ large enough, there is a package whose valuation is $\nu$". The seven statements are the inert statement, the split statement, the zero statement, and two pairs, each of a main statement and a zero statement: one pair for primes where Frobenius acts as complex conjugation, and one pair for the class of inert primes with a degree bound.

### Row data at self-conjugate places

A *self-conjugate labelling* is a finite set $\mathrm{Orb}$ and a map $\tau : \mathrm{Orb} \times \mathbb{Z}/2 \to \operatorname{Hom}(E, \mathbb{C})$ with ranks $n, j, j'$. It is *arithmetic* if $\tau$ is injective, $\tau(o, s + 1) = \overline{\tau(o, s)}$, $\tau(o, s + 1)(x) \equiv \tau(o, s)(x)^\ell$ modulo the maximal ideal after the embeddings into $C$, and $\ell \nmid \operatorname{disc} E$. It has *correct ranks* if $\mathrm{mult}\,\tau(o, 0) = n + j$ and $\mathrm{mult}\,\tau(o, 1) = j'$.

**Theorem 4.5.3 (row data at self-conjugate places).** Assume the character statement at every prime, and that the involution of $\mathcal{O}_E$ is the conjugation of the host. Let $y$ be an algebraic integral point of $X$ over $T$ with a chart $C_3$. Let $C$ be an algebraically closed complete field of characteristic $0$ with a valuation $V$ of residue characteristic $\ell$, with an embedding $\iota$ of the fraction field of $T$, and let $Y$ be a chart over $C$ that is the base change of $C_3$ at level $k$. Let $\tau$ be an arithmetic self-conjugate labelling onto $\operatorname{Hom}(E, \mathbb{C})$, with correct ranks and $j' < n$. Let $a$ be a dominant weight, $n_W \geq 0$, and $\nu \leq \nu_{\mathrm{loc}}$. Then for each $o$ there are an alternating row datum $X_o$ of size $(n, j + j')$ with $\operatorname{rk} X_o(0, s) = \mathrm{mult}\,\tau(o, s)$, and a flag, such that the block bound holds for $n_W$, the gap weights $\mathrm{gap}(\mathrm{mult}\,\tau(o, s), a(\tau(o, s), \cdot))$ and $\nu$.

Lean: `GlobalTheory.T.rowData_supplied_at_selfConjugate_places` (also `GlobalTheory.RowAt.supplyC_selfConj`, a second name).

*Proof.* Step 1. For each orbit $o$ the chart $Y$ gives self-conjugate place data $p_o$, tied to $\tau$ and separated. The correct ranks give the rank and the alternating conditions of $p_o$.

Step 2. The raw chart of each $p_o$ satisfies the row hypotheses. Five of them are formal laws of the chart. The biextension of $Y$ is nondegenerate modulo the maximal ideal, because $Y$ comes from an integral chart, and this gives the maximal rank condition. The last hypothesis is a character bound in degree two. It follows from the character statement at $\ell$.

Step 3. The rows $X_o$ are the row data of these raw charts. A numbering of the letters gives flags and ranks.

Step 4. The block bound has four inputs. First, $\nu \leq \nu_{\mathrm{loc}}$ for $C_3$ gives the same bound for $Y$, and chart products on planes give the block values. Second, the jet of a product is the product of the jets. Third, block products lie in the chart family at the self-conjugate places. Fourth, the blocks are admissible. Admissibility uses $j' < n$, the alternating rows, and $\mathrm{gap}(r, b)(i) = 0$ for $i > r$. $\square$

### Row data at pairs of places

A *paired labelling* is a finite set $\mathrm{Orb}$, an integer $d \geq 1$, ranks $n, j, j'$, a map $\tau : \mathrm{Orb} \times \{0, 1\} \times \mathbb{Z}/d \to \operatorname{Hom}(E, \mathbb{C})$ and a predicate $\mathrm{big}(o, g, s)$. It is *arithmetic* if $\tau$ is injective, $\tau(o, 1, s) = \overline{\tau(o, 0, s)}$, $\tau(o, g, s + 1)(x) \equiv \tau(o, g, s)(x)^\ell$ modulo the maximal ideal, distinct labels are separated by some $x \in \mathcal{O}_E$ modulo the maximal ideal, and each $(o, g)$ has an idempotent $\varepsilon$ modulo $\ell$ that cuts out its labels. It has *correct ranks* if, for each $o$, $\mathrm{big}(o, 1 - g, s)$ holds exactly when $\mathrm{big}(o, g, s)$ fails, $\mathrm{mult}\,\tau(o, g, s) = n + j$ when $\mathrm{big}(o, g, s)$ holds, and $\mathrm{mult}\,\tau(o, g, s) = j'$ otherwise.

**Theorem 4.5.4 (row data at pairs of places).** Assume the character statement at every prime, and that the involution of $\mathcal{O}_E$ is the conjugation of the host. Let $y$, $C_3$, $C$ and $Y$ be as before, with $\ell \nmid \operatorname{disc} E$. Let $\tau$ be an arithmetic paired labelling onto $\operatorname{Hom}(E, \mathbb{C})$, with correct ranks and $j' < n$. Assume that for each $o$ either $d$ is even and $\mathrm{big}(o, 0, s)$ holds exactly for even $s$, or $\mathrm{big}(o, 0, s)$ holds for all $s$. Let $a$, $n_W$ and $\nu$ be as before. Then for each $o$ there are a row datum $X_o$ of size $(n, j + j')$ whose predicate and ranks are $\mathrm{big}(o, g, s)$ and $\mathrm{mult}\,\tau(o, g, s)$, and a flag, such that the block bound holds for $n_W$, the gap weights $\mathrm{gap}(\mathrm{mult}\,\tau(o, g, s), a(\tau(o, g, s), \cdot))$ and $\nu$.

Lean: `GlobalTheory.T.rowData_supplied_at_pairs_of_places` (also `GlobalTheory.RowAt.supply_pairs`, a second name).

*Proof.* The proof follows the previous one. Step 1. The arithmetic of the labelling gives integral, saturated eigenvectors on $Y$ that span each eigenspace. The biextension of $Y$ is nondegenerate.

Step 2. For each orbit the pair data of $o$ satisfies the row hypotheses. The Cartesian, axis and kernel laws are formal. The correct ranks give the rank hypothesis and, with the nondegeneracy, the maximal rank. The character bound for pairs of places follows from the character statement. This is the only step that uses $\ell \nmid \operatorname{disc} E$ and the algebraicity of $y$.

Step 3. A numbering gives the flags, and the ranks of $X_o$ are $\mathrm{mult}\,\tau(o, g, s)$.

Step 4. The block bound follows as before, with the separation of the pairs and a product formula for row values as extra inputs. Admissibility uses the dichotomy for $\mathrm{big}$, the inequality $j' < n$, and the vanishing of gap weights beyond the multiplicity. $\square$

The paired version is the input for the inert, the split and the zero statements. Those packages are built outside this chapter.

### Frobenius as complex conjugation

Let a good point be given, with numerical datum $N$ of ranks $k, m$, an index $1 \leq j \leq m$ and an injective map $p_l$ from the places $z$ of the datum to $\operatorname{Hom}(E, \mathbb{C})$. Assume that $\ell$ is in the inert class of $N$ and that the shift of places at $\ell$ is trivial. Then the Frobenius condition of the embedding datum gives $\overline{\tau}(x) \equiv \tau(x)^\ell$ modulo $\lambda$ for each chosen $\tau$. So Frobenius acts as complex conjugation. Put $\tau(z, 0) = p_l(z)$ and $\tau(z, 1) = \overline{p_l(z)}$. The signature is $(k + j - 1, m - j)$, and $\mathrm{mult}(\tau)$ is $k + j - 1$ on the image of $p_l$ and $m - j$ outside it. Put $\gamma(z, s, i) = \mathrm{gap}(\mathrm{mult}\,\tau(z, s), a(\tau(z, s), \cdot))(i)$.

**Lemma 4.5.5 (row family).** Assume the character statement at every prime. At a good point where Frobenius acts as complex conjugation, the map $(z, s) \mapsto \tau(z, s)$ is a bijection onto $\operatorname{Hom}(E, \mathbb{C})$. There are a valued field $C$ of residue characteristic $\ell$ and alternating row data $R_z$ of size $(k - 1, m)$ with $\operatorname{rk} R_z(0, s) = \mathrm{mult}\,\tau(z, s)$, such that the block bound holds for $n_W$, the weights $\gamma$ and $\nu$.

Lean: `GlobalTheory.PkgConj.exists_rowFam`.

*Proof.* There is an algebraically closed field $C$ of characteristic $0$, complete for a valuation $V$ of residue characteristic $\ell$, with an embedding of the fraction field of $T$. In $C$ the bound $e_\lambda \nu \leq \nu_{\mathrm{loc}}$ becomes $\nu \leq \nu_{\mathrm{loc}}$ for $V$. The chart at $y$ has a base change $Y$ over $C$ at the level $M$. This needs $\ell \neq 2$, the trace identity $w_0 + \bar w_0 = 1$ of the host, and that $M$ is a unit at $\ell$. The labelling $\tau$ with ranks $(k - 1, j, m - j)$ is arithmetic and onto, by the Frobenius condition. Its ranks are correct: $\mathrm{mult}\,\tau(z, 0) = (k - 1) + j$, and $\mathrm{mult}\,\tau(z, 1) = m - j$ because the conjugate of an embedding in the image of $p_l$ is not in the image. Finally $m - j < k - 1$, since $m + 3 \leq k$. The theorem on self-conjugate places gives the rows, the flags and the block bound. $\square$

**Theorem 4.5.6 (packages when Frobenius is complex conjugation).** Assume the character statement at every prime. Then the two parts of the package statement for primes where Frobenius acts as complex conjugation hold for every $E$, host, $D_w$, $l$, $X$ and $F$. In detail, at every such good point:
1. for all real $T, \theta_0, C_1$ with the degree hypothesis for the main weight $W(z) = a(p_l z, k - 2) - a(p_l z, k - 1)$ and the rest, and with $8 r f \leq n_W$, there is a package with constant $C_1$, alternating rows, $\gamma(z, 0, k - 1) = W(z)$, and the given $T$ and $\nu$;
2. if the weights of $N$ are nonnegative, $a(\tau, 0) \leq s(\ell - 1)$ whenever $\mathrm{mult}(\tau) > 0$, and $4 r s f \leq n_W$, there is a zero package whose valuation is $\nu$.

Here $r = k + m - 1$ and $f$ is the number of places.

Lean: `GlobalTheory.T.packages_exist_frobeniusComplexConjugation` (also `GlobalTheory.PkgConj.packages_conj`, a second name).

*Proof.* Both parts start from the lemma.

Part 1. The gap weights $\gamma(z, s, \cdot)$ are supported in $[1, \mathrm{mult}\,\tau(z, s)]$. Since $\mathrm{mult}\, p_l(z) = k + j - 1 \geq k - 1$, the weight $\gamma(z, 0, k - 1)$ equals $W(z)$. A telescoping sum gives $\sum_i i\,\gamma(z, s, i) = \sum_{i < \mathrm{mult}} a(\tau(z, s), i)$. The bijection turns the sum over $(z, s)$ into the sum over all embeddings, so the rest of the package equals the prescribed rest after the main terms $(k - 1) \sum_z W(z)$ are removed. The other conditions are the hypotheses.

Part 2. Take $K = r$ and $T = 1$. The sum $\sum_{i \leq r} \gamma(z, \sigma, i)$ telescopes to $a(\tau(z, \sigma), 0)$, or to $0$ if the multiplicity is $0$. So it is at most $s(\ell - 1)$. $\square$

### All good primes

**Theorem 4.5.7 (packages at good primes).** Assume the character statement at every prime. Then for every CM field $E$ with a host datum, every Hermitian datum $D_w$, level $l$, moduli space $X$, coefficient field $F$ and involution of $\mathcal{O}_E$, the package statement holds for $X$ and $F$.

Lean: `GlobalTheory.T.allGoodPrimeDepthDataExist_proof` (also `GlobalTheory.goodPrime_packages`, a second name).

*Proof.* Each of the seven parts comes from one theorem applied to the character statement. The inert, the split and the zero statements come from three package theorems, and each of them uses the row data at pairs of places. The two parts where Frobenius is complex conjugation are the previous theorem. The pair for inert primes with a degree bound comes from the [packages at inert primes with a degree bound](/entry/exists-pkg-cs-of-degree-bound-at-inert-primes/). $\square$

**Remark 4.5.8 (Formalization).** The four theorems with the prefix `GlobalTheory.T.` are second names, proved by `first | exact @…` under `maxHeartbeats 1000000` ([RowDataSuppliedAtPairsOfPlacesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/RowDataSuppliedAtPairsOfPlacesStatement.lean#L8)). In the lemma on row families, the hypotheses $\ell \neq q_N$, $\ell \neq d_N$ and "$\ell$ inert implies $\ell \geq 5$" are introduced as `_` and not used ([PackagesExistFrobeniusComplexConjugation.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PackagesExistFrobeniusComplexConjugation.lean#L32)).
