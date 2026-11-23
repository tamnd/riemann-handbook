---
title: Operator words, jets, square integrability and random polynomials
decls:
  - operator_words_bound
  - jet_bound_ramified_prime
  - Formalism.REAL.square_integrable_of_lipschitz
  - Formalism.IrreducibleCountingLemmas.GaloisIrreducibility.property_W_of_estimates
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Operator words, jets, square integrability and random polynomials

This section collects four estimates that the rest of the proof uses at single places. The first writes operators on homogeneous polynomials as short words in the $\mathfrak{gl}_k$ operators $x_a\partial_b$; it feeds [the operator weight bound](/entry/operator-weight-bound-holds/) for real groups. The second bounds the coefficients of a jet at a ramified prime; it feeds [the entry divisor bound](/entry/entry-divisor-bound-holds/). The third shows that derivatives of square integrable eigenfunctions on $\mathrm{U}(p, q)$ stay square integrable with a weight; it feeds [the discrete series input](/entry/r0b-g/). The fourth bounds the share of tuples of random polynomials over a finite field whose roots fail a list of conditions; it is used in the step [EveryCharacter from the literature](/step/every-character-of-literature/).

**Definition 6.8.1 (Words in the operators $E_{ab}$).** Let $K$ be a field of characteristic $0$ and $V_d$ the space of homogeneous polynomials of degree $d$ in $x_1, \dots, x_k$ over $K$. Put $E_{ab} = x_a\partial_b$ on $V_d$. A *word of length $l$* is a product $E_{a_1b_1}\cdots E_{a_lb_l}$. An operator $A$ on $V_d$ has *weight* $\omega \in \mathbb{Z}^k$ if $[E_{aa}, A] = \omega_a A$ for each $a$.

Lean: `Formalism.MainNotions.TestSideCounting.EdWord` (also `Formalism.MainNotions.TestSideCounting.Ed`).

**Theorem 6.8.2 (Operator words).** Let $c \in \mathbb{N}$. Let $W$ be a subspace of $\mathrm{End}(V_d)$ with $[E_{ab}, W] \subseteq W$ for all $a, b$, spanned by a set $S$ of weight vectors whose weights $\omega$ satisfy $\omega_a \leq c$ for all $a$. Then each $A \in W$ is a linear combination of words of length at most $c$.

Lean: `operator_words_bound` (also `Formalism.MainNotions.TestSideCounting.OpBound`).

For $c \geq d$ this is the classical fact that $V_d$ is an irreducible $\mathfrak{gl}_k$-module, so the image of the enveloping algebra is all of $\mathrm{End}(V_d)$. For $c < d$ it is a filtered form of the same fact. *Proof (outline).* The *symbol* of an operator on $V_d$ is a polynomial in $x$ and dual variables $\xi$ of bidegree $(d, d)$, and the symbol map is injective. It turns composition with $E_{ab}$ on the left and right into explicit operators on symbols, and it carries the bracket with $E_{ab}$ to a derivation. Weights of operators become weights of bihomogeneous polynomials. The key step shows that if $c < d$, every polynomial in the image of $W$ vanishes on the quadric $\sum_i x_i\xi_i = 0$. A polarization and divisibility argument then shows that the image of $W$ lies in $t^{d-c}$ times the polynomials of bidegree $(c, c)$, where $t = \sum_i x_i\xi_i$. These are exactly the symbols of combinations of words of length at most $c$. $\square$

**Definition 6.8.3 (Jet of a column product).** Let $\ell$ be a prime, $H$ a finite set and $Z = \{0, 1\} \times H$. Let $y_{z,a,b}$ ($z \in Z$, $a < N_0$, $b < N_1$) and $x_{z,i,a}$ be variables. For Young diagrams $\nu_z$ and a *column choice* $I$, which gives each column $c$ of $\nu_z$ an increasing map $I_{z,c}$ from $\{0, \dots, \nu'_{z,c} - 1\}$ to $\{0, \dots, N_1 - 1\}$ ($\nu'$ the column lengths), put
$$G_I = \prod_{z \in Z}\prod_c \det\Bigl(\sum_{a < N_0} x_{z,i,a}\,y_{z,a,I_{z,c}(k)}\Bigr)_{i, k < \nu'_{z,c}}.$$
For a power series $\Theta$ in the $y$ over $\mathbb{C}_\ell$, the *jet* $G_I(x, \partial_y)\Theta|_{y=0}$ replaces each monomial $y^\mu$ of $G_I$ by $\mu!$ times the coefficient of $y^\mu$ in $\Theta$. $\Theta$ has *ramified shape* if
$$\Theta = \exp\Bigl(-S\sum_{t \in H}u_t\sum_{a,b}y_{(0,t),a,b}\,y_{(1,t),a,b}\Bigr)\cdot\sigma$$
with $|S| \leq \ell^{1/2}$, $|u_t| \leq 1$, and $|m!\,\sigma_m| \leq 1$ for every coefficient $\sigma_m$ of $\sigma$.

Lean: `PI.EntAtD.applyAt0` (also `PI.EntAtD.Gxz`, `PI.EntAtD.KvalGe`, `PI.EntAtD.ShapeD`).

**Theorem 6.8.4 (Jet bound at a ramified prime).** Fix the global data $D$ of the proof and a divisor datum. Let $\nu$ give a Young diagram $\nu_{u,i,z}$ for each word $u$, level $i$ and $z \in Z$, whose row $r$ has length equal to the row datum $\nu_{\mathrm{row}}(u, i + 1, \tau(z), r)$ for $r < N_i$ and $0$ otherwise, and whose first column has length at most $N_i$. Let $\Theta_{u,\mu,w,i,L,L'}$ be power series in the variables with $N_0 = N_i$ and $N_1 = N_{i+1}$ over $\mathbb{C}_\ell$, $\ell$ the residue characteristic of the place $w$. Suppose $\Theta$ has ramified shape whenever $w$ is level free and $\ell$ is in the ramified class. Then for such $u, \mu, w$, each $i < m$ and classes $L, L'$, each column choice $I$ and each monomial $x^m$,
$$\bigl|\text{coefficient of } x^m \text{ in } G_I(x, \partial_y)\Theta|_{y=0}\bigr| \leq \ell^{\frac12\sum_{t \in H}\mathrm{ct}(u, i + 1, t)}.$$

Lean: `jet_bound_ramified_prime` (also `PI.EntAtD.EntAtD`).

Here $\mathrm{ct}(u, j, t)$ is a combination of the size of $\nu$ at the place $(0, t)$ and of its first two row lengths at $(0, t)$ and $(1, t)$; we do not unfold its parts.

*Proof (outline).* The derivatives of $\sigma$ at $0$ are integral. In the exponential, $(\sum_j y_jy'_j)^k/k!$ has $\mu!\cdot$coefficient integral, so each term with $k$ pairs costs at most $|S|^k \leq \ell^{k/2}$. Expanding, the jet is a sum over $k$ of $S^k$ times integral terms, each obtained by applying $k$ powers of the Laplacian $\sum_{a,b}\partial_{(0,t),a,b}\partial_{(1,t),a,b}$ to the column product. Laplace expansion of the minors, a degree count and the commutation of the Laplacians show that these terms vanish once $k$ exceeds $\sum_t\mathrm{ct}(u, i + 1, t)$. $\square$

**Theorem 6.8.5 (Weighted square integrability).** Let $\varepsilon \in \{\pm 1\}^n$, $J = \mathrm{diag}(\varepsilon)$, $G = \{g \in \mathrm{GL}_n(\mathbb{C}) : g^*Jg = J\}$ with [[Haar measure|VY0HXD3GC4]] $\mu$, and $h(g) = \log\sum_{a,b}|g_{ab}|^2$. For $X$ in the Lie algebra of $G$ let $R_X$ be the right derivative, and let $E_{ab} = R_{X_1} + iR_{X_2}$ where the matrix unit is $X_1 + iX_2$. Put $\Omega = \sum_{a,b}E_{ab}E_{ba}$. Assume:

1. $h$ is smooth and $|R_Xh(g)| \leq 2(\sum_{a,b}|X_{ab}|^2)^{1/2}$;
2. $\int_G R_X\varphi\,d\mu = 0$ for every smooth $\varphi$ that vanishes where $\sum_{a,b}|g_{ab}|^2 > R$, for some $R$.

Let $W$ be a finite-dimensional space of smooth functions on $G$, $c \in \mathbb{C}$ and $a \geq 0$. Suppose $E_{ij}W \subseteq W$ when $\varepsilon_i = \varepsilon_j$, $\Omega f = cf$ and $e^{2ah}|f|^2 \in L^1(G)$ for $f \in W$. Then for all words $E_{w_1}$, $E_{w_2}$ in the $E_{ab}$ and all $f, f' \in W$: $E_{w_1}f$ is smooth, $e^{2ah}|E_{w_1}f|^2 \in L^1(G)$, and for all $i, j$
$$\int_G E_{ij}(E_{w_1}f)\,\overline{E_{w_2}f'}\,d\mu = \mathrm{sgn}(i, j)\int_G E_{w_1}f\,\overline{E_{ji}E_{w_2}f'}\,d\mu,$$
with $\mathrm{sgn}(i, j) = 1$ if $\varepsilon_i = \varepsilon_j$ and $-1$ otherwise.

Lean: `Formalism.REAL.square_integrable_of_lipschitz` (also `Formalism.REAL.SmoothVectorGrowthBound`, `Formalism.REAL.HhLip`, `Formalism.REAL.IntRdZero`).

The two assumptions are proved elsewhere in the formalization, so the theorem holds outright. It is a weighted form of the fact that a $K$-finite, $\mathcal{Z}$-finite square integrable function generates a $(\mathfrak{g}, K)$-module of square integrable functions; see [discrete series](/learn/real-groups/#discrete-series-and-formal-degrees). *Proof (outline).* Induct on the length of $w_1$. The operators $E_{ij}$ with $\varepsilon_i = \varepsilon_j$ keep $W$. For the other $E_{ij}$, write $\Omega$ as its compact part plus $\sum_{\varepsilon_i \neq \varepsilon_j}E_{ij}E_{ji}$. Multiply by a cutoff, integrate by parts with assumption 2, and bound the derivative of the weight $e^{2ah}$ with assumption 1. This gives $e^{2ah}|E_{ij}f|^2 \in L^1$ from the same bound for $f$ and $\Omega f = cf$. The adjoint formula is integration by parts once more, with the sign from $J$. $\square$

**Definition 6.8.6 (Weighted squarefree polynomials).** Let $\mathbb{F}$ be a finite field with $q$ elements and $N \geq 1$. For $c \in \mathbb{F}^N$ let $f_c = X^N + \sum_{i<N}c_iX^i$. $\mathrm{Sq}_N$ is the set of $c$ with $f_c$ squarefree and $f_c(0) \neq 0$, and
$$\mathrm{wt}(f) = \prod_{P \mid f,\ P\text{ monic irreducible}}\frac{1}{q^{\deg P} - 1}.$$
For a prime $l$ and $x$ of finite order, $x_{(l')}$ is the power of $x$ whose order is the prime-to-$l$ part of the order of $x$. $B(q, N)$ is the set of $q$ and the primes $l \leq q^N$ with $q^\delta < l^{4v_l(q^\delta - 1)}$ for some $1 \leq \delta \leq N$.

Lean: `Formalism.IrreducibleCountingLemmas.GaloisIrreducibility.sqWeight` (also `sqSet`, `monicOf`, `primeToPart`, `BB`).

For squarefree $f$ with $f(0) \neq 0$, $\mathrm{wt}(f)$ is the probability that a random element of $\mathrm{GL}_N(\mathbb{F})$ has characteristic polynomial $f$, since its centralizer is $\prod_P \mathbb{F}_{q^{\deg P}}^\times$.

**Definition 6.8.7 (Good tuple).** Let $\bar{\mathbb{F}}$ be an algebraic closure, $\iota, J$ finite sets and $\chi_{v,j} \in \mathbb{F}^\times$. A tuple $(f_v)_{v \in \iota}$ is *good* if: each $f_v$ is monic of degree $N$, squarefree, with $f_v(0) \neq 0$; for primes $l \notin B(q, N)$, $x \mapsto x_{(l')}$ is injective on the roots of each $f_v$; for primes $l \neq q$, no root $x$ of $f_v$ has $x_{(l')}$ equal to $(\chi_{v,j})_{(l')}$ or $(\chi_{v,j}^{-1})_{(l')}$; for each $1 \leq a \leq N/2$ some $f_v$ has no factor of degree $a$; and some $f_v$ has an irreducible factor of prime degree $\delta$ with $N/2 < \delta \leq N - 3$.

Lean: `Formalism.IrreducibleCountingLemmas.GaloisIrreducibility.GoodAt`.

**Theorem 6.8.8 (Property W).** Let $N \geq 100$, $q \geq 2^{12}$, and $q_1 \neq d$ odd primes with $\max(q_1, d) \geq 16$ and $16q_1d \mid q - 1$. Let $P$ be a probability on $\mathbb{F}^N$ with $P(c) = \mathrm{wt}(f_c)$ for $c \in \mathrm{Sq}_N$. Draw $c_v$ ($v \in \iota$) independently from $P$. Then the probability that $(f_{c_v})_v$ is not good is at most
$$\begin{aligned} &\frac{2|\iota|}{q} + \frac{23|\iota|\log q}{\sqrt q} + 2|\iota||J|\Bigl(\frac{1}{4\min(q_1, d)} + \frac{1 + \log N}{q - 1}\Bigr) \\ &\quad + \frac{N}{2}\Bigl(\frac78\Bigr)^{|\iota|} + \exp\Bigl(-\frac{|\iota|}{5\log N}\Bigr). \end{aligned}$$

Lean: `Formalism.IrreducibleCountingLemmas.GaloisIrreducibility.property_W_of_estimates` (also `Formalism.IrreducibleCountingLemmas.GaloisIrreducibility.PropW`).

The last two conditions are a criterion of Jordan type: a transitive permutation group of degree $N$ that contains a cycle of prime length $\delta$ with $N/2 < \delta \leq N - 3$ contains the alternating group. Gallagher used the same idea in his large sieve for Galois groups. *Proof (outline).* Use a union bound over the five conditions. The weights on $\mathrm{Sq}_N$ have total mass at least $1 - 2/q$, so each $f_v$ falls outside $\mathrm{Sq}_N$ with probability at most $2/q$. Local estimate II bounds the mass of the $f$ with a non-injective $x \mapsto x_{(l')}$ for some $l \notin B(q, N)$ by $23\log q/\sqrt q$. Local estimate III bounds the mass with a root meeting a fixed $\chi$ by $1/(4\min(q_1, d)) + (1 + \log N)/(q - 1)$; apply it to $\chi_{v,j}$ and its inverse. Local estimate IV bounds the mass of the $f$ with a factor of degree $a$ by $7/8$. By independence, all $f_v$ have such a factor with probability at most $(7/8)^{|\iota|}$; sum over $a \leq N/2$. Local estimate V bounds the mass without a prime degree factor in the range by $1 - 1/(5\log N)$, and $(1 - u)^{|\iota|} \leq e^{-u|\iota|}$. $\square$

**Remark 6.8.9 (Formalization).** `operator_words_bound` is in [OpWords.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/OpWords.lean#L6); its proof applies `opBound_of_vanish` to `vanishingOnQuadric`, and the statement `OpBound` is in [OpBound.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/OpBound.lean#L36). `jet_bound_ramified_prime` is in [EntAtD.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/EntAtD.lean#L11) and applies `entAtD_of` to six named inputs; the statement is in [PeriodIntegrals/EntAtD.lean](lean:Formalism/PeriodIntegrals/EntAtD.lean#L62). The constants $\mathrm{ct}$, the row data and the class of a place come from the data structure `D7` and are not unfolded. Its shape hypothesis is assumed for all $u, \mu, w$ at once. `square_integrable_of_lipschitz` is in [IntegrableComplexContinuousBoundedSupport.lean](lean:Formalism/RealPlaceAnalysis/RealPlaceTaylor/IntegrableComplexContinuousBoundedSupport.lean#L1497); the two assumptions are `log_frobenius_lipschitz_holds` and `integral_right_derivative_zero` in RightDerivativeZeroOutsideSupport.lean. The hypothesis that $W$ is finite-dimensional is introduced as `_` at line 1498 and never used. `property_W_of_estimates` is in [PropertyWOfEstimates.lean](lean:Formalism/PadicSubsetSums/StableGradedCounts/PropertyWOfEstimates.lean#L7) and applies `propW_of_localEstimates` to local estimates II and III; estimates IV and V are proved inside that lemma. We opened the statements of these inputs, not their proofs, so the four outlines follow statements only.

## Notes and references

The zero density and Deuring-Heilbronn estimates of [Section 6.1.3](/entry/log-density-bound/) and the prime number theorem for progressions of [Section 6.2.3](/entry/pnt-progressions-relative-weak-holds/) follow the classical theory of [[Dirichlet L-functions|24GAZHVTGB]]; the Background sections on [zeros of Dirichlet L-functions](/learn/analytic-number-theory/#zeros-of-dirichlet-l-functions), [the explicit formula](/learn/analytic-number-theory/#the-explicit-formula) and [mean values and the large sieve](/learn/analytic-number-theory/#mean-values-and-the-large-sieve) give the setting. The [[explicit formula|72WNRWJQC1]] of [Section 6.3.8](/entry/explicit-formula-closed/) is the standard one for a [[Dirichlet character|JR4QSEFXWF]]. The mean squares and good pairs of Sections 5 and 6 use Jacobi sums, as in [Gauss and Jacobi sums](/learn/analytic-number-theory/#gauss-and-jacobi-sums). The $p$-adic counts of [Section 6.7.12](/entry/mc-theorem-mv7/) use the Bombieri inner product and Smith forms over $\mathbb{Z}_p$. Property W is a form of the probabilistic Galois theory of random polynomials.

- H. Davenport, *Multiplicative Number Theory*, 3rd ed., Graduate Texts in Mathematics 74, Springer, 2000, Chapters 14, 16, 19 and 20.
- H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I. Classical Theory*, Cambridge University Press, 2007, Chapter 12.
- H. Iwaniec and E. Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, 2004, Chapters 10 and 18.
- H. L. Montgomery, *Ten Lectures on the Interface between Analytic Number Theory and Harmonic Analysis*, CBMS Regional Conference Series 84, AMS, 1994.
- P. X. Gallagher, A large sieve density estimate near $\sigma = 1$, Invent. Math. 11 (1970), 329 to 339.
- C. L. Siegel, Über die Classenzahl quadratischer Zahlkörper, Acta Arith. 1 (1935), 83 to 86.
- B. Beauzamy, E. Bombieri, P. Enflo and H. L. Montgomery, Products of polynomials in many variables, J. Number Theory 36 (1990), 219 to 245.
- N. Jacobson, *Basic Algebra I*, 2nd ed., W. H. Freeman, 1985, Section 3.7.
- A. W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986.
- P. X. Gallagher, The large sieve and probabilistic Galois theory, Proc. Sympos. Pure Math. 24, AMS, 1973.
- R. Arratia, A. D. Barbour and S. Tavaré, *Logarithmic Combinatorial Structures: a Probabilistic Approach*, EMS Monographs in Mathematics, 2003.
