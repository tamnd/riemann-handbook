---
title: Arcs and series of theta values
decls:
  - GlobalTheory.T.exists_arcSeries_integral_algebraic_over_powerSeries
  - GlobalTheory.ArcSeries.exists_series
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Arcs and series of theta values

An arc is a set of degeneration data with an action of $\mathcal{O}_E$ over a ring $O'$ that is a field or a complete discrete valuation ring. Mumford's construction turns such data, with a parameter $u$ of absolute value less than $1$, into an abelian variety over a complete field. Its theta null values are theta series in $u$. In this section we take $u$ to be the variable $X$ of the power series ring $O'[[X]]$. We prove that there are elements of an algebraic closure of $\operatorname{Frac} O'[[X]]$ that are algebraic over $O'[[X]]$, are integral at every valuation over $O'[[X]]$, and at every point with $|X| < 1$ become the theta values of the uniformised abelian variety. These series data are the raw material for the moduli point of [the section on moduli points over power series rings](/entry/exists-point/). For degeneration data see [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction) in Volume 1, and for theta series see [theta functions on complex tori](/learn/theta-functions-cm/#theta-functions-on-complex-tori).

### The moduli data

Throughout the chapter, $E$ is a CM field with ring of integers $\mathcal{O}_E$ and complex conjugation $a \mapsto \bar a$. A host for $E$ gives a prime $d$, a complex number $\rho_{\mathbb{C}}$ with $\rho_{\mathbb{C}}^2 = -d$, and an element $w_0 \in \mathcal{O}_E$. A PEL datum $D$ gives a hermitian $\mathcal{O}_E$-lattice $\Lambda$ and a signature $(p, q)$. A level $l$ gives integers $A, M, M' \geq 1$ and an ideal $\mathfrak{m}$ of $\mathcal{O}_E$. Let $X_o$ be the moduli space of these data with level $l$, let $F$ be its coefficient field, and let $V \subset F$ be the valuation ring cut out by a valuation ring $W_0 \subset \mathbb{C}$. We write $X_{o,F}$ for the moduli space over $F$ and $\zeta_A = e^{2\pi i/A}$.

**Definition 6.1.1 (Model).** A *model* $Y$ of $X_o$ over $V$ is a normal scheme $Y$, projective and flat over $\operatorname{Spec} V$, with an open dense immersion $j : X_{o,F} \to Y$ over $V$, a semi-abelian scheme $G$ over $Y$ with an action of $\mathcal{O}_E$ and a rigidified line bundle $L$, such that over $F$ the abelian locus of $G$ is the image of $j$.

The *abelian locus* of $G$ is the set of points of $Y$ where the fibre of $G$ is proper. For the semi-abelian schemes in this chapter, see [[abelian schemes|JDDXZ89N33]] and the Volume 1 section above.

**Definition 6.1.2 (Complete trait).** A local domain $W$ is a *complete trait* if it is a discrete valuation ring, it is complete for its maximal ideal, and it has characteristic $0$.

**Definition 6.1.3 (Arc base).** Let $O'$ be a domain and $\varpi \in O'$. The pair $(O', \varpi)$ is an *arc base* if either $O'$ is a field and $\varpi = 1$, or $O'$ is a discrete valuation ring, $\varpi$ is irreducible and $O'$ is $\varpi$-adically complete.

In both cases $O'$ is local and principal. We always assume that $O'$ has characteristic $0$, and we fix a map $b : V \to O'$.

### Numerical degeneration data

**Definition 6.1.4 (Numerical degeneration datum).** Let $O$ be a ring. A *numerical degeneration datum* $N$ over $O$ consists of a commutative group $\mathcal{A}$, a cubical cocycle $\theta : \mathcal{A}^3 \to O^\times$ with a compatible symmetric function $\sigma : \mathcal{A} \to O^\times$, a function $\vartheta : \mathcal{A} \to O$, a free abelian group $\mathsf{X}$ of finite rank, a homomorphism $c : \mathsf{X} \to \mathcal{A}$ and a function $\psi : \mathsf{X} \to O^\times$. We require $\psi(-\chi)\,\sigma(c(\chi)) = \psi(\chi)$, and that $\tau(a, b) = \psi(a+b)\psi(a)^{-1}\psi(b)^{-1}$ is bimultiplicative up to the factor $\theta(c(a), c(a'), c(b))$.

The group $\mathcal{A}$ stands for the points of the abelian part, $\theta$ and $\sigma$ for its cubical and symmetric structures, and $\vartheta$ for the values of a theta section. The pair $(c, \psi)$ is the period datum. For $k \geq 1$ the *torsion classes* of level $k$ form a group $Q_k(N)$ of pairs $(y, g)$, with $y \in \mathsf{X}$ and $g$ a point of the torus extension such that $g^k = \iota(y)$, where $\iota$ is the period map. Two classes are equivalent if they differ by $(kz, \iota(z))$.

For $m$ odd and $p \in Q_{m^2}(N)$, the theta series of $N$ at $p$ is
$$\vartheta_m(p) = \sum_{\chi \in \mathsf{X}} t_m(p, \chi),$$
where the term $t_m(p, \chi)$ is a unit times $\psi(\chi)\, g^m(\chi)\, \vartheta(c(\chi) \cdot b(g^m))$, with $(y, g) = p$ and $b(g^m)$ the abelian part of $g^m$. The series of coordinates $\vartheta_m(p, h)$ at a second torsion point $h$ is built in the same way.

**Definition 6.1.5 (Twist).** Let $\beta$ be a symmetric positive bilinear form on $\mathsf{X}$ with values in $2k\mathbb{Z}$, and let $u \in O^\times$. The *twist* $N^{\beta, u}$ is $N$ with $\psi$ replaced by $\chi \mapsto \psi(\chi)\, u^{\beta(\chi, \chi)/2}$.

So $\tau$ becomes $\tau(a, b)\, u^{\beta(a, b)}$. The twist is Mumford's period $u^\beta$ put on top of the given data. Let $r \in O^\times$ with $r^j$ related to $u$. A class $p' \in Q_j(N^{\beta, u})$ is *twist-related* to $p \in Q_j(N)$ by $r$ if they have the same $y$ and the same abelian part and $p'(z) = p(z)\, r^{\beta(y, z)}$ for all $z$.

### Arcs and their lifts

**Definition 6.1.6 (Arc).** An *arc* $a$ over $(O', b)$ consists of degeneration data $D_0$ over $O'$ with an action of $\mathcal{O}_E$ on its character lattice, such that $\psi$ is even, $\tau$ is bimultiplicative and $\psi$ is a unit on all of $\mathsf{X}$. It also has a positive definite form $\beta_a$ on $\mathsf{X}$ with $\beta_a(ay, z) = \beta_a(y, \bar a z)$ and $2M' \mid \beta_a$, level points of level $M$ and $A$, and the Lie signature of $D$.

**Definition 6.1.7 (Lift of an arc).** Let $C$ be a field over $\operatorname{Frac} O'$. A *lift* of $a$ to $C$ consists of $\rho \in C$ with $\rho^2 = -d$ and the signature condition of $D$ for the Lie algebra; a Tate isomorphism $I$, with roots of unity $\zeta_n$ and maps $\operatorname{ev}_n$ from $\Lambda$ to the $n$-torsion; a numerical degeneration datum $N$ over $C$ with a comparison $\nu$ to $D_0$; labels $q_n : \Lambda \to Q_n(N)$ that match $\operatorname{ev}_n$; a form $\beta$ on $\mathsf{X}(N)$ that is $\beta_a$ under $\nu$; and the conditions that $\rho$ and $\zeta_A$ are the images of the elements of $V$ that go to $\rho_{\mathbb{C}}$ and $\zeta_A$, and that the level points of $a$ agree with $\operatorname{ev}_A$ and $\operatorname{ev}_M$. We ask $C$ to be algebraically closed.

A lift is *integral* if, for the valuation ring $\{|x| \leq 1\}$ of a normed field $C$, all torsion points of the abelian part extend to integral points.

**Definition 6.1.8 (Roots).** Let $u \in C^\times$. A *system of roots* of $u$ is a map $r : \mathbb{N} \to C^\times$ with $r(1) = u$ and $r(nm)^m = r(n)$ for all $n, m \geq 1$.

**Definition 6.1.9 (Integral family).** Let $R$ be a ring, $i : R \to K$ a map to a field, $u \in R$, $s \in \mathbb{N}$ and $v : \Lambda \to K$. The family $v$ is *integral* for $(u, i, s)$ if for each valuation ring $S$ of $K$ with $i(R) \subset S$: every $v(x)$ lies in $S$; some $v(x)$ is a unit of $S$; and if $i(u)$ is a unit of $S$, then for every $x$ there is $h$ with $v(x + s h)$ a unit of $S$.

The last condition says that a unit occurs in each coset of $s\Lambda$. It is the integral form of the fact that theta null values of a good abelian variety do not all vanish on a coset.

**Definition 6.1.10 (Test points).** Let $K$ be a field over $\operatorname{Frac} O'$ and $i : O'[[X]] \to K$. A *test point* of $i$ is a complete, algebraically closed, ultrametric normed field $C$ over $\operatorname{Frac} O'$ with a map $\gamma : K \to C$ over $\operatorname{Frac} O'$ such that $|\gamma(i(f))| \leq 1$ for all $f$ and $u = \gamma(i(X))$ has $|u| < 1$.

**Definition 6.1.11 (Series datum).** Let $K$ be an algebraically closed field over $\operatorname{Frac} O'$ and $i : O'[[X]] \to K$ an injective map over $O'$ such that $K$ is algebraic over $O'[[X]]$. A *series datum* for $a$ in $K$ consists of a lift $A$ of $a$ to $K$, a system of roots $r$ of $i(X)$, values $v_m : \Lambda \to K$ and coordinates $w_{m,j,z} : \Lambda \to K$, with two properties.

1. For $n$ an odd prime that is a unit in $O'$ and $j \geq 1$, the family $v_{n^j}$ is integral for $(X, i, n^{j-1})$.
2. At each test point $(C, \gamma)$ with $u = \gamma(i(X))$, there is an integral lift $A'$ of $a$ to $C$ over $A$, with roots $r' = \gamma \circ r$, such that for each odd $m$ and each $p : \Lambda \to Q_{m^2}(N'^{\beta', u})$ twist-related to $q'_{m^2}$ by $r'(m^2)$, there is $s \in C^\times$ with $\gamma(v_m(x)) = s\, \vartheta_m(p(x))$ for all $x$, and the same holds for the coordinates $w_{m,j,z}$ at each torsion class twist-related to $q'_j(z)$.

So a series datum is a family of elements of $K$ that becomes, up to a scalar, the theta null point of Mumford's abelian variety at each value $u$ of $X$ with $|u| < 1$.

### The inputs

**Definition 6.1.12 (The inputs).** The *inputs* of Sections 1 to 6 are seven statements that the Lean development takes as hypotheses.

1. The laws: basic facts on abelian schemes, line bundles and their sections, with four statements on twisted base change over discrete valuation rings.
2. Uniqueness of uniformisations.
3. Uniformisation over complete traits: a semi-abelian scheme with $\mathcal{O}_E$ action over a complete trait $W$, polarized on the generic fibre and split over the closed point, has a uniformisation with a torsion isomorphism.
4. Extension of homomorphisms of semi-abelian schemes over a discrete valuation ring.
5. Theta points determine the variety: let $n$ be an odd prime, $k \geq 2$, $N = n^{2k}$ and $N' = n^j N$ with $N^g g! < N'$. Over an algebraically closed field in which $n$ is a unit, two polarized abelian varieties of dimension $g$ with level structures of level $N'^2$ and the same theta point of level $N'$ are isomorphic, by an isomorphism of polarized varieties that matches the level bases.
6. An endomorphism is determined on torsion: if $4^g g! \cdot 2c < M^2$, then an isomorphism of polarized varieties that commutes with the action of an element $a$ of norm at most $c$ on the $M$-torsion commutes with it everywhere.
7. Complex uniformisation: every polarized abelian variety over $\mathbb{C}$ is a complex torus $\mathbb{C}^g / \Lambda$ with a hermitian form, its sections of $L^n$ are theta functions, and the Weil pairing is given by the imaginary part of the form ([the complex uniformization](/learn/abelian-varieties/#the-complex-uniformization)).

Lean: `GlobalTheory.Ex.HV`, `ReciprocityTheory.ChartRestriction.G.Out.Laws6`, `GlobalTheory.LN.UDvrSt`, `GlobalTheory.LN.HomExtSt`, `GlobalTheory.ThetaPtDeterminesSt`, `GlobalTheory.EndDeterminedOnTorsionSt`, `ReciprocityTheory.ChartRestriction.G.Geo.Tor.ThetaUnifAV`.

Input 3 is the existence of degeneration data of Faltings and Chai, and input 5 is a form of Mumford's theorem that theta null values of high level give coordinates on the moduli space.

**Theorem 6.1.13 (Series of theta values).** Assume the seven inputs. Let $Y$ be a model of $X_o$ over $V$, let $(O', \varpi)$ be an arc base with $O'$ of characteristic $0$, let $b : V \to O'$ and let $a$ be an arc over $(O', b)$. Let $K$ be an algebraically closed field over $\operatorname{Frac} O'$ and over $O'[[X]]$, faithful and algebraic over $O'[[X]]$, such that the two maps agree on $O'$. Then $a$ has a series datum in $K$.

Lean: `GlobalTheory.T.exists_arcSeries_integral_algebraic_over_powerSeries` (also `GlobalTheory.ArcSeries.exists_series`, a second name).

*Proof.* Let $F$ be an algebraic closure of $\operatorname{Frac} O'$. The integral closure of $O'$ in $F$ is a valuation ring $S_0$ of $F$, since $O'$ is a field or a complete discrete valuation ring. Over $(F, S_0)$ the arc has a lift $A_0$ whose numerical datum is integral: the values of $\theta$, $\sigma$, $\vartheta$ and $\psi$ are units of $S_0$. Fix an embedding $F \to K$ over $\operatorname{Frac} O'$. The lift $A_0$ extends to a lift $A$ over $K$, and since $K$ is algebraically closed, $i(X)$ has a system of roots $r$.

Fix $m$ odd, $j \geq 1$ and $z \in \Lambda$. Choose representatives of $\Lambda / m^2 \Lambda$. The finitely many torsion classes $q_{m^2}(x)$ and $q_j(z)$ that occur descend to a finite free $O'$-algebra $O_1$ in $F$. Over $O_1$ the theta terms $t_m$ are power series in the root $r(m^2 j)$, with coefficients in $O_1$, and their sums define elements $v, w$ of $K$ that lie in a finite $O'[[X]]$-subalgebra $R_{m,j,z}$ of $K$. At each test point these elements become the twisted theta values and coordinates of the corresponding lift. We put $v_m = v$ for $(m, 1, 0)$ and $w_{m,j,z} = w$.

The second property of a series datum holds with $s = 1$. At a test point $(C, \gamma)$, the lift $A$ extends to an integral lift $A'$ over $C$, with a homomorphism of numerical data that has $\lambda = 1$, keeps the form and carries the labels. The values above then become the theta series of $A'$ twisted by $u = \gamma(i(X))$.

For the first property, let $n$ be an odd prime that is a unit in $O'$, let $j \geq 1$ and let $S$ be a valuation ring of $K$ that contains $i(O'[[X]])$. Each $v_{n^j}(x)$ lies in a finite $O'[[X]]$-algebra, so it is integral over $O'[[X]]$ and lies in $S$. For each $e$ there is a normed field $C$ and a map $\gamma : K \to C$ centred on $S$ with $|\gamma(X)| < 1$. Under $\gamma$, an element of valuation less than $1$ goes to an element of norm less than $1$, and if $X$ is a unit of $S$, to an element of norm at most $|\gamma(X)|^e$. On the other side, the twisted theta values have a value of norm at least $1$. In each coset $x + n^{j-1}\Lambda$ they have a value of norm at least $|\gamma(X)|^{\beta(y, y)}$, where $y$ is the class of $x$. This lower bound uses the separation of the torsion pairing values on the abelian part. Taking $e = 0$ gives a unit among the $v_{n^j}(x)$. If $X$ is a unit of $S$, taking $e$ larger than $\beta(y, y)$ gives a unit in each coset. $\square$

**Remark 6.1.14 (Formalization).** The proof uses only the first input, and of it only the first two bundles of laws; the other six inputs are introduced as `_` in [ExistsArcSeriesIntegralAlgebraicOverPowerSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsArcSeriesIntegralAlgebraicOverPowerSeries.lean#L94). The statement form is proved in [ExistsArcSeriesIntegralAlgebraicOverPowerSeriesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsArcSeriesIntegralAlgebraicOverPowerSeriesStatement.lean#L11) by a `first | exact ...` block under `maxHeartbeats 1000000`, as are all the statement forms of this chapter. We have not unfolded `ArcIn`, `TateIsoQ` or the laws. The description of the theta term $t_m$ follows `NumD.txT` and the description of the inputs follows their statements.
