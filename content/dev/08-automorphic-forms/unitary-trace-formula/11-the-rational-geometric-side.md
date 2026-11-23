---
title: The rational geometric side
decls:
  - GlobalTheory.PreStabU.fixedP
  - GlobalTheory.PreStabU.geomURat_eq_geomU
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The rational geometric side

This section stabilizes the class sum of [the Hecke traces](/entry/tr-on-forms-hop-eq-geom/) on a definite unitary group. The class sum is a sum over rational conjugacy classes. We rewrite it as a sum over pairs of coprime elliptic polynomials $(P_1, P_2)$, with a global constant and a product of local $\kappa$-orbital integrals for each pair. The pairs are the elliptic classes of the endoscopic groups $\mathrm{U}(a) \times \mathrm{U}(n - a)$, and the local factors are the ones that [the inert places](/entry/match-principal-congruence-inert/) and [the split places](/entry/match-ct-mu-of-is-split-at/) compare with the twisted orbital integrals of $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$. So the result puts the geometric side of the unitary trace formula in the form that the comparison with the twisted trace formula needs, on the way to the step [every character](/step/every-character/). For the background, see [the trace formula for a compact quotient](/learn/trace-formula/#the-trace-formula-for-a-compact-quotient) and [the mass formula for unitary groups](/learn/hermitian-lattices/#the-mass-formula-for-unitary-groups).

### Setting

We keep the notation of [the Hecke traces](/entry/tr-on-forms-hop-eq-kern-sum/) and of [the conjugacy classes](/entry/unitary-classes-main/): $E$ is a CM field in which every finite place is unramified over $E^+$, $\mathrm{U}(E)$ is the definite [[unitary group|0R9R0Y1HDK]] of rank $n \ge 1$, $S$ is a section, $\mathrm{U}_w$ and $K_w$ are the local groups for $w \in S$, $\lambda$ is a weight, $K'$ is a level and $f = (f_w)$ is a test function for $K'$. The set $\mathrm{Ell}(E, n)$ of elliptic polynomials and the local signs $\epsilon_w(Q, y)$ are as in [the conjugacy classes](/entry/unitary-classes-main/). For a polynomial $P$ let $r(P)$ be the number of its monic irreducible factors, counted with multiplicity, and for $P \in E[X]$ and $w \in S$ write $P$ also for its image in $E_w[X]$.

**Definition 2.11.1 (Local κ-orbital integrals).** Let $w \in S$, and let $P_1$, $P_2$ be monic with $P_1 P_2$ of degree $n$. For a function $\varphi$ on $\mathrm{U}_w$ put
$$O^\kappa_{P_1, P_2}(\varphi) = \sum_{y} \epsilon_w(P_1, y)\, O_y(\varphi),$$
the sum over the conjugacy classes of $y \in \mathrm{U}_w$ with characteristic polynomial $P_1 P_2$, where $O_y$ is the orbital integral with $K_w$ as the compact subgroup.

At an inert place this is the $\kappa$-orbital integral of [the inert places](/entry/kap-orb-congruence-eq-kap-sum/). At a split place the sign is $1$, and for separable $P_1 P_2$ there is one class, so $O^\kappa_{P_1, P_2}(\varphi)$ is a single orbital integral on $\mathrm{GL}_n(E_w)$.

**Definition 2.11.2 (Global constants).** Let $\theta(g) = \Phi\, {}^t c(g)^{-1}\, \Phi^{-1}$ be the twist of $\mathrm{GL}_n$ that defines the base change from $\mathrm{U}$, with $\Phi$ a fixed matrix. For $P \in \mathrm{Ell}(E, n)$ put
$$k(P) = \frac{m^\theta(\delta)}{2^{r(P)}}$$
if there is $\delta \in \mathrm{GL}_n(E)$ such that $\delta\,\theta(\delta)$ has characteristic polynomial $P$, where $m^\theta(\delta)$ is the mass of the twisted centralizer of $\delta$ in $\mathrm{GL}_n(\mathbb{A}_f)$, defined as the mass $m(\gamma)$ of [the class sum](/entry/tr-on-forms-hop-eq-geom/). Put $k(P) = 0$ if there is no such $\delta$. Put $\overline{\chi_\lambda}(P) = \overline{\chi_\lambda(\gamma)}$ for any $\gamma \in \mathrm{GL}_n(E)$ with characteristic polynomial $P$.

The constant $k(P)$ depends on $P$ only, and $\chi_\lambda$ is a class function. The same constants appear in the stable twisted trace formula, which is why the comparison works term by term.

### Counting classes with given local data

**Proposition 2.11.3 (Classes with a fixed characteristic polynomial).** Let $P \in \mathrm{Ell}(E, n)$. Then only finitely many conjugacy classes $\gamma$ of $\mathrm{U}(E)$ with characteristic polynomial $P$ have $\prod_{w \in S} O_{\gamma_w}(f_w) \ne 0$, and
$$2^{r(P)} \sum_{\gamma} \prod_{w \in S} O_{\gamma_w}(f_w) = \sum_{P_1 P_2 = P} \ \prod_{w \in S} O^\kappa_{P_1, P_2}(f_w),$$
where $\gamma$ runs over the conjugacy classes of $\mathrm{U}(E)$ with characteristic polynomial $P$, and $(P_1, P_2)$ over the pairs of monic polynomials with product $P$.

Lean: `GlobalTheory.PreStabU.fixedP`

*Proof.* For $w \in S$ let $\mathrm{Cl}_w$ be the set of conjugacy classes of $\mathrm{U}_w$ with characteristic polynomial $P$. It is finite. Let $\mathrm{Cl}$ be the set of classes of $\mathrm{U}(E)$ with characteristic polynomial $P$, and $\gamma \mapsto (\gamma_w)$ the map to the families of local classes. Call a local class *good* if it meets $K_w$.

*Step 1: almost all places.* For almost all $w$: $f_w = \mathbf{1}_{K_w}$; exactly one class in $\mathrm{Cl}_w$ is good; the orbital integral $O_y(\mathbf{1}_{K_w})$ is $1$ for the good class and $0$ for the others; and the signs $\epsilon_w(P_1, y)$ of the good class are $1$ for every divisor $P_1$ of $P$. Each global class is good at almost all places, since its entries and the entries of its inverse are integral at almost all places.

*Step 2: the sign sum.* Let $x = (x_w)$ be a family of local classes, good at almost all places. Put $\sigma(P_1) = \prod_{w \in S} \epsilon_w(P_1, x_w)$ for monic divisors $P_1$ of $P$. Each $\epsilon_w(\cdot, x_w)$ is multiplicative on coprime divisors, since the kernel of $P_1 P_1'(x_w)$ is the orthogonal sum of the kernels of $P_1(x_w)$ and $P_1'(x_w)$. So $\sigma$ is a character of the group of monic divisors of $P$ under the operation $(P_1, P_1') \mapsto P_1 P_1' / \gcd(P_1, P_1')^2$, which is $(\mathbb{Z}/2)^{r(P)}$, and the sum of its values is $2^{r(P)}$ if $\sigma = 1$ and $0$ otherwise. By the [Theorem on classes](/entry/unitary-classes-main/), items 2 and 3, $\sigma = 1$ if and only if $x$ is the family of local classes of a global class. So
$$\sum_{P_1 P_2 = P} \ \prod_{w \in S} \epsilon_w(P_1, x_w) = \begin{cases} 2^{r(P)} & \text{if } x \text{ comes from } \mathrm{Cl}, \\ 0 & \text{otherwise.} \end{cases}$$

*Step 3: exchange of sum and product.* By item 1 of the same Theorem, the map from $\mathrm{Cl}$ to the families of local classes is injective. Expand the right side of the claim:
$$\begin{aligned}
\sum_{P_1 P_2 = P} \ \prod_{w \in S} O^\kappa_{P_1, P_2}(f_w) &= \sum_{P_1 P_2 = P} \ \prod_{w \in S} \ \sum_{y \in \mathrm{Cl}_w} \epsilon_w(P_1, y)\, O_y(f_w) \\
&= \sum_{x} \Big( \sum_{P_1 P_2 = P} \ \prod_{w \in S} \epsilon_w(P_1, x_w) \Big) \prod_{w \in S} O_{x_w}(f_w),
\end{aligned}$$
where $x$ runs over the families of local classes that are good at almost all places. The products are finite products by Step 1, and the sum over $x$ has finite support, since at almost all places only the good class gives a nonzero term. By Step 2, only the families that come from $\mathrm{Cl}$ remain, each with the factor $2^{r(P)}$, and by injectivity each global class appears once. $\square$

### The stable form of the class sum

**Theorem 2.11.4 (Stabilization of the class sum).** Let $E$ be a CM field in which every finite place is unramified over $E^+$, $n \ge 1$, $S$ a section, $\lambda$ a weight, $K'$ a level and $f$ a test function for $K'$. Suppose that there is $w \in S$ such that every $y \in \mathrm{U}_w$ with $f_w(y) \ne 0$ has separable characteristic polynomial. Then
$$\sum_{\gamma} m(\gamma)\, \overline{\chi_\lambda(\gamma)}\, O_\gamma(f) = \sum_{a = 0}^{n} \ \sum_{(P_1, P_2)} k(P_1 P_2)\, \overline{\chi_\lambda}(P_1 P_2) \prod_{w \in S} O^\kappa_{P_1, P_2}(f_w),$$
where $\gamma$ runs over the conjugacy classes of $\mathrm{U}(E)$ with separable characteristic polynomial, and $(P_1, P_2)$ over the coprime pairs with $P_1 \in \mathrm{Ell}(E, a)$ and $P_2 \in \mathrm{Ell}(E, n - a)$.

Lean: `GlobalTheory.PreStabU.geomURat_eq_geomU`

*Proof.* *Step 1: finiteness.* If $O_\gamma(f) \ne 0$, then for every $w \in S$ there is $y \in \mathrm{U}_w$ with $f_w(y) \ne 0$ and the same characteristic polynomial as $\gamma$. Since $f_w = \mathbf{1}_{K_w}$ for almost all $w$ and each $f_w$ has compact support, the coefficients of the characteristic polynomial lie in a compact set at each place and are integral at almost all places. So only a finite set $F \subseteq \mathrm{Ell}(E, n)$ of characteristic polynomials occurs.

*Step 2: the mass.* A class $\gamma$ of $\mathrm{U}(E)$ with separable characteristic polynomial $P$ has $P \in \mathrm{Ell}(E, n)$, and by the mass formula for the torus $\mathrm{U}_\gamma$,
$$m(\gamma) = k(P)\, 2^{r(P)}.$$
So the left side is
$$\sum_{P \in F} k(P)\, \overline{\chi_\lambda}(P)\; 2^{r(P)} \sum_{\gamma \mapsto P} \ \prod_{w \in S} O_{\gamma_w}(f_w),$$
since $O_\gamma(f)$ is the product of the local orbital integrals.

*Step 3: the Proposition.* By the Proposition, the inner expression is $\sum_{P_1 P_2 = P} \prod_{w} O^\kappa_{P_1, P_2}(f_w)$.

*Step 4: reindexing.* A monic divisor of an elliptic polynomial is elliptic, and the two factors of a separable polynomial are coprime. Conversely, if $P_1 \in \mathrm{Ell}(E, a)$ and $P_2 \in \mathrm{Ell}(E, n - a)$ are coprime, then $P_1 P_2 \in \mathrm{Ell}(E, n)$. So the pairs $(P_1, P_2)$ of the right side, with $a = \deg P_1$, are exactly the monic factorizations of the polynomials $P \in \mathrm{Ell}(E, n)$. A pair whose product is not in $F$ gives $0$, since then some local factor $O^\kappa_{P_1, P_2}(f_w)$ is a sum of zeros. $\square$

The right side has the shape of the stable twisted trace formula of $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$: a sum over pairs of elliptic polynomials, with the global constant $k$ and a product of local factors. After matching at each place, the local factor $O^\kappa_{P_1, P_2}(f_w)$ becomes a stable twisted orbital integral of the matching function, multiplied by the transfer factor. This is how the stabilized class sum is compared with the twisted side.

**Remark 2.11.5 (Formalization).** The regularity hypothesis of the Theorem is not used in its proof: the class sum is already restricted to separable classes, and finiteness comes from the support of $f$ alone ([UnitaryGeometricSideSeparableTest.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/IsobaricBaseChange/IntegralCoefficientBaseChange/UnitaryBaseChangeCharacters/UnitaryBaseChangeLinks/UnitaryGeometricSideSeparableTest.lean#L458)). The orbital integrals, the class sums and the sums over pairs are all `finsum`, which is $0$ for infinite support; this is why the Proposition states the finiteness of the support as a first conclusion. The exchange of sum and product in Step 3 of the Proposition is an abstract named result about finite sets of local classes, a map from global classes, and sign functions, applied with $N = 2^{r(P)}$; the Hasse principle and the sign criterion of [the conjugacy classes](/entry/unitary-classes-main/) supply its hypotheses ([UnitaryGeometricSideSeparableTest.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/IsobaricBaseChange/IntegralCoefficientBaseChange/UnitaryBaseChangeCharacters/UnitaryBaseChangeLinks/UnitaryGeometricSideSeparableTest.lean#L357)). Step 2 of the Proposition is a separate lemma ([UnitaryGeometricSideSeparableTest.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/IsobaricBaseChange/IntegralCoefficientBaseChange/UnitaryBaseChangeCharacters/UnitaryBaseChangeLinks/UnitaryGeometricSideSeparableTest.lean#L263)), which uses the multiplicativity of the signs at line 238 and a named result on character sums over monic divisors. Step 1 is the lemma at line 139; it rests on named results on unit orbital integrals and integral conjugacy at almost all places. The mass formula of Step 2 of the Theorem, the finiteness of Step 1, and the ellipticity of products in Step 4 are also named results, and we did not unfold them. In the formal statement, $r(P)$ counts the normalized factors of $P$; for separable $P$ this is the number of irreducible factors. The constant $k(P)$ is defined with a representative $\delta$ picked by choice ([SimpleTwistedTraceFormulaStable.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SimpleTwistedTraceFormulaStable.lean#L114)).
