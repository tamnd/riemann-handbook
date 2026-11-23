---
title: Row families and packages at inert primes
decls:
  - UpperTheory.OrbitFamilyRestriction.exists_rowFamS
  - UpperTheory.exists_pkgCs_of_degree_bound_at_inert_primes
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Row families and packages at inert primes

At a prime $l$ that is inert in the CM field and has odd order, this section builds a *package*: a family of row data over the Frobenius orbits, with the weights, the degree data and the valuation block bound that the degree argument needs. The first theorem labels the orbits and applies [the theorem on row data](/entry/label-set-geo-of-even-of-rank-ok-of-not-dvd-discr/) of Section 6. The second theorem adds the degree data and gives the two kinds of packages, with the main term and with the zero term. [The theorem on packages at good primes](/entry/good-prime-packages/) uses both.

### Points

Let $E$ be a CM field with host $H$, let $D_w$ be a datum with multiplicities $\mathrm{mult}(\tau)$ for the embeddings $\tau : E \to \mathbb{C}$, and fix a level and a coefficient field $F_c$. A *point* is the following list of data and conditions:
- the involution of $O_E$ is complex conjugation;
- a numerical datum $N$ with ranks $k$, $m$, $r$ and $f$, and an index $j$ with $1 \le j \le m$;
- an injective map $\mathrm{pl}$ from the places of $N$ to the embeddings, whose image is the CM type, with $d(H) = d(N)$;
- the signature of $D_w$ is the signature of $N$ at $j$;
- an assignment $a(\tau, i)$ that decreases in $i$;
- a height-one prime $\mathfrak{l}$ of $O_{F_c}$ with residue characteristic $l$, where $l$ is not small, $l \ne q(N)$, $l \ne d(N)$, $l$ does not divide the level, and $l \ge 5$ if $l$ is inert;
- a complete discrete valuation ring $T$ over $\mathfrak{l}$ with ramification index $e$, and an algebraic integral frame $y$ over $T$ with an integral chart;
- integers $n_W$ and a real $\nu$ with $e_{\mathfrak{l}}\,\nu \le \nu_{\mathrm{loc}}(a, n_W)$, where $e_{\mathfrak{l}}$ is the ramification of $\mathfrak{l}$ over $\mathbb{Z}$.

A statement *holds at all points* if it holds for every such list.

The datum $N$ at $j$ and $l$ gives *parameters* $P = P(N, j, l)$: the places $\mathrm{Pl}$, a set of $f$ elements; the period $d = \mathrm{ord}(l)$; the ranks $k$, $m$ and $r$; weights $w(z)$ for the places; and a position map $\mathrm{pos}$. A set $Z$ of places is a set of *representatives* if each place is $\mathrm{pos}(z, s)$ for exactly one $z \in Z$ and $s \in \mathbb{Z}/d$. A *row family* over $Z$ is a field $C$ with a valuation $V$ at $l$ and row data $X_o$ with flags $F_o$ for every $o \in Z$, with $n(X_o) = k - 1$, $m(X_o) = m$, and $X_o$ alternating.

For an embedding $\tau$, write $g_a(\tau, i)$ for the gaps of the sequence $a(\tau, 0) \ge a(\tau, 1) \ge \cdots$, so that $a(\tau, i) = \sum_{i' > i} g_a(\tau, i')$ for $i < \mathrm{mult}(\tau)$.

**Theorem 6.7.1 (Row family at an inert prime of odd order).** Assume the upper bound law at every prime. At all points with $l$ inert and $\mathrm{ord}(l)$ odd, there are a set $Z$ of representatives, a labelling $\tau_{o,s}$ for $o \in Z$ and $s \in \mathbb{Z}/2d$, and a row family $R$ over $Z$ such that:
- the map $(o, s) \mapsto \tau_{o,s}$ is a bijection onto all embeddings of $E$;
- $\tau_{o,s}$ is in the CM type if and only if $s$ is even;
- for even $s$, $\tau_{o,s} = \mathrm{pl}(\mathrm{pos}(o, s \bmod d))$;
- the rank of $X_o$ at $(0, s)$ is $\mathrm{mult}(\tau_{o,s})$;
- the valuation block bound holds with shift $d$, the flags of $R$, $n_W$, the gaps $g_a(\tau_{o,s}, \cdot)$ and $\nu$.

Lean: `UpperTheory.OrbitFamilyRestriction.exists_rowFamS`

*Proof.* There is an algebraically closed complete field $C$ over the place, with valuation $V$ at $l$, an embedding $\iota$ that respects the valuations, and $\nu \le \nu_{\mathrm{loc}}$ for the integral chart. Since $l$ is not small, $l \ne 2$, and $v(M) = 0$ for the level $M$. The integral chart has a base change $Y$ to $C$; the trace of the idempotent of the CM host is $1$. Choose representatives $Z$ for the inert labelling. The existence theorem for orbit labellings at inert primes of odd order gives a label set with $2d$ positions, shift $h_d = d$, rank numbers $n = k - 1$, $j$ and $j' = m - j$, the big rule "$(g, s)$ is big if and only if $g + s$ is even", and $\tau_{o,s} = \mathrm{pl}(\mathrm{pos}(o, s))$ for even $s$ and its conjugate for odd $s$. The label set is arithmetic, every embedding is a label, and $l$ does not divide the discriminant.

Then $\tau_{o,s}$ is in the CM type exactly when $s$ is even, so $\mathrm{mult}(\tau_{o,s})$ is $p$ or $q$ by the parity of $s$. Since $d$ is odd, $s - d$ and $s$ have different parity. With $p$ and $q$ from the signature, this gives the rank condition. Also $j' < n$, because $m + 3 \le k$. The gaps satisfy the weight tie with $a$ and vanish outside $1 \le i \le \mathrm{mult}$, by the gap sum identity. [The theorem on row data](/entry/label-set-geo-of-even-of-rank-ok-of-not-dvd-discr/) now gives $X_o$ and $F_o$ with the valuation block bound.

The labelling is injective: if $\tau_{o,s} = \tau_{o',s'}$, then $s$ and $s'$ have the same parity, and $\mathrm{pos}(o, s) = \mathrm{pos}(o', s')$ by the injectivity of $\mathrm{pl}$ and of conjugation. The uniqueness of representatives gives $o = o'$ and $s \equiv s'$ modulo $d$. Two numbers below $2d$ with the same parity and the same residue modulo the odd number $d$ are equal. Surjectivity comes from the label set. $\square$

### Packages

*Degree data* $(T, \theta_0, \mathrm{rest}, C_1)$ for parameters $P$ and a weight $W$ on the places satisfy: $T \ge 1$; $w(z) > 0$; $(1 - \theta_0)\,w(z) \le T\,W(z) \le w(z) + C_1 S_E$; $0 \le \theta_0 \le 1$; $(k - 1)\theta_0 \le 5m$; and $0 \le T\cdot\mathrm{rest} \le C_1 f k S_E$, where $S_E$ is a constant of the parameters. For a point, put $W(z) = a(\mathrm{pl}(z), k - 2) - a(\mathrm{pl}(z), k - 1)$ and
$$\mathrm{rest} = \sum_{\tau}\sum_{i} a(\tau, i) - (k - 1)\sum_z W(z).$$

A *package with main term* for $P$, $l$ and $C_1$ consists of: $d$ odd; a set $Z$ of representatives; a row family $R$ over $Z$; weights $g(o, s, i)$ with $g(o, s, i) \ne 0$ only for $1 \le i \le \mathrm{rk}_0(X_o, s)$; $g(o, s, k - 1) = W(\mathrm{pos}(o, s \bmod d))$ for even $s$; the identity
$$\mathrm{rest} = \sum_{o}\sum_{s}\sum_{i = 1}^{r}\begin{cases}0 & \text{if } s \text{ is even and } i = k - 1,\\ i\,g(o, s, i) & \text{otherwise};\end{cases}$$
the bound $f\bigl((i_0 + 1)(k - 1) + 4r\bigr) \le n_W$; degree data; and the valuation block bound with $g$ and $\nu$. A *package with zero term* consists of $Z$, $R$, weights $g$, integers $K$ and $s$ and reals $T \ge 1$ and $\nu$ with: $w(z) \ge 0$; $g(o, \sigma, i) \ne 0$ only for $1 \le i \le \mathrm{rk}_0$ and $i \le K$; $\sum_{i = 1}^{K} g(o, \sigma, i) \le s(l - 1)$; $4Ks\,|Z|\,d \le n_W$; and the valuation block bound.

**Theorem 6.7.2 (Packages at inert primes).** Assume the upper bound law at every prime. Then at all points with $l$ inert and $\mathrm{ord}(l)$ odd:
- for all $T$, $\theta_0$ and $C_1$ such that $(T, \theta_0, \mathrm{rest}, C_1)$ are degree data for $P(N, j, l)$ and $W$, and $f\bigl((i_0(k, l) + 1)(k - 1) + 4r\bigr) \le n_W$, there is a package with main term with this $T$ and this $\nu$;
- if $w_j(z) \ge 0$ for all $z$, and $s$ satisfies $a(\tau, 0) \le s(l - 1)$ for every $\tau$ with $\mathrm{mult}(\tau) > 0$ and $4rsf \le n_W$, there is a package with zero term with this $\nu$.

Lean: `UpperTheory.exists_pkgCs_of_degree_bound_at_inert_primes`

*Proof.* Take $Z$, $\tau$ and $R$ from [the theorem on row families](/entry/exists-row-fam-s/), and take $g(o, s, \cdot)$ to be the gaps of $a(\tau_{o,s}, \cdot)$. Since $\mathrm{mult}(\tau)$ is $p$ or $q$, it is at most $r$.

For the main term: if $s$ is even, $\tau_{o,s} = \mathrm{pl}(\mathrm{pos}(o, s \bmod d))$ is in the CM type, its multiplicity is the first entry of the signature at $j$, and by the values of the signature the gap at $k - 1$ is $a(\tau, k - 2) - a(\tau, k - 1) = W$. By the gap sum identity, $\sum_{i=1}^{r} i\,g_a(\tau, i) = \sum_{i < \mathrm{mult}(\tau)} a(\tau, i)$. So each inner sum in the identity for $\mathrm{rest}$ is $\sum_i a(\tau_{o,s}, i)$ minus $(k - 1)W$ when $s$ is even. Sum over the bijection $(o, s) \mapsto \tau_{o,s}$: the first parts give $\sum_\tau\sum_i a(\tau, i)$, and the second parts give $(k - 1)\sum_z W(z)$, since the even labels run through the image of $\mathrm{pl}$ once. This is the identity for $\mathrm{rest}$. The other conditions of the package are the hypotheses.

For the zero term, take $K = r$, the given $s$, and $T = 1$. The support condition follows from the gap identity and $\mathrm{mult} \le r$. The sum of all gaps is $a(\tau, 0) \le s(l - 1)$ when $\mathrm{mult}(\tau) > 0$, and $0$ otherwise. Finally $|Z|\,d = f$, because $(z, s) \mapsto \mathrm{pos}(z, s)$ is a bijection from $Z \times \mathbb{Z}/d$ onto the $f$ places. $\square$

**Remark 6.7.3 (Formalization).** The theorem on row families is `private` and five of its hypotheses are bound and never used: `hj1`, `hjm`, `hqq`, `hdd` and `hin5` ([ExistsPkgCsOfDegreeBoundAtInertPrimes.lean](lean:Development/AutomorphicArithmetic/OrbitLabellings/ExistsPkgCsOfDegreeBoundAtInertPrimes.lean#L45), the intro at line 55). The theorem on packages instantiates the row family once (line 207) and then repeats the full intro pattern of 27 names in each part to pass them on (lines 209 and 284). The package with zero term fixes $T := 1$ (line 301), so its $T$ is not a parameter of the statement. The weights $g$ are a `private` definition `gaT` through `GlobalTheory.RowAt.gap`. The text does not unfold `parOf`, the constant `RF.i0`, the weights `P.w` and the constant `P.SE`, `RF.IsReps` beyond its meaning, the predicates `OverLa` and `DomW`, or `UpFSt`.
