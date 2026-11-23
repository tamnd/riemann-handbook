---
title: Torsion values of the Weierstrass function
decls:
  - ReciprocityTheory.ChartRestriction.L1.cmTorsion_of_point
  - ReciprocityTheory.ChartRestriction.L1.cm4
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Torsion values of the Weierstrass function

This section transports the [Weierstrass function](/learn/elliptic-curves/#lattices-and-the-weierstrass-function) of a complex lattice to $\mathbb{C}_l$ by a field isomorphism, and proves that its values at torsion points of order prime to $l$, suitably scaled, are integral and lie in $\breve{\mathbb{Q}}_l$. The scaling is the one that gives the curve good reduction. It is one of the statements on complex multiplication that [the service row from Artin reciprocity](/entry/serv-h-row-of-artin/) depends on, and through it the [unitary hypotheses](/proof/unitary-hypotheses/) of the proof.

### Lattices and their curves

Let $L = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2 \subset \mathbb{C}$ be a lattice. Its invariants are
$$g_2(L) = 60 \sum_{\omega \in L \setminus 0} \omega^{-4}, \qquad g_3(L) = 140 \sum_{\omega \in L \setminus 0} \omega^{-6},$$
and $g_2(L)^3 - 27 g_3(L)^2 \ne 0$. The Weierstrass function $\wp = \wp_L$ satisfies $\wp'^2 = 4\wp^3 - g_2 \wp - g_3$. So for $z \notin L$ the pair $(\wp(z), \wp'(z)/2)$ lies on the curve
$$y^2 = x^3 - \tfrac{g_2(L)}{4} x - \tfrac{g_3(L)}{4},$$
and the map $z \mapsto (\wp(z), \wp'(z)/2)$, $L \mapsto O$, is an isomorphism of groups from $\mathbb{C}/L$ to the complex points of this curve (Silverman, *The Arithmetic of Elliptic Curves*, Proposition VI.3.6).

For a squarefree integer $d > 0$ with $d \equiv 3 \pmod 4$, put $\omega_K = (1 + i\sqrt{d})/2$. It generates the ring of integers of $K = \mathbb{Q}(\sqrt{-d})$ ([complex multiplication](/learn/elliptic-curves/#complex-multiplication)). The lattice $L$ has *complex multiplication by* $\mathcal{O}_K$ if $\omega_K L \subseteq L$.

Let $l$ be a prime and let $\iota : \mathbb{C} \to \mathbb{C}_l$ be an isomorphism of fields. Such isomorphisms exist, since both fields are algebraically closed of characteristic $0$ and of the same cardinality, but no such $\iota$ is continuous. So $\iota$ carries algebraic identities, not limits. We keep the field $\breve{\mathbb{Q}}_l$ and the good pairs of [the previous section](/entry/tor-kur/).

### The scaled torsion point

**Proposition 7.4.1 (Scaled torsion points).** Let $l$ be a prime, $L$ a lattice, $\iota : \mathbb{C} \to \mathbb{C}_l$ a field isomorphism and $\lambda \in \mathbb{C}_l$ with $\lambda \ne 0$. Let $E_\lambda$ be the curve
$$y^2 = x^3 - \tfrac{\lambda^4 \iota(g_2(L))}{4} x - \tfrac{\lambda^6 \iota(g_3(L))}{4}.$$
Let $z \in \mathbb{C}$ and $N \in \mathbb{N}$ with $Nz \in L$ and $z \notin L$. Then
$$P = \bigl(\lambda^2 \iota(\wp(z)),\ \lambda^3 \iota(\wp'(z))/2\bigr)$$
is a nonsingular point of $E_\lambda$, and $NP = O$.

Lean: `ReciprocityTheory.ChartRestriction.L1.torPt` (also `Formalism.L2.Th1.E.scaled_torsion_point_of_add`, `Formalism.L2.Th1.E.PtOfAdd_of`)

*Proof.* Let $\mu = \iota^{-1}(\lambda)$ and $L' = \mu^{-1} L$. Homogeneity of the Weierstrass function gives
$$g_2(L') = \mu^4 g_2(L), \quad g_3(L') = \mu^6 g_3(L), \quad \wp_{L'}(\mu^{-1} z) = \mu^2 \wp_L(z), \quad \wp'_{L'}(\mu^{-1} z) = \mu^3 \wp'_L(z).$$
So $P$ is the image under $\iota$ of the point $(\wp_{L'}(z'), \wp'_{L'}(z')/2)$ with $z' = \mu^{-1} z$, and $E_\lambda$ is the image under $\iota$ of the curve of $L'$. The map $t \mapsto \iota(\wp_{L'}(t), \wp'_{L'}(t)/2)$ from $\mathbb{C}/L'$ to the image curve is a homomorphism, because the addition formulas of $\wp$ are algebraic identities and $\iota$ is a field isomorphism. It sends $t \in L'$ to $O$. Since $N z' \in L'$, we get $NP = O$. Nonsingularity is preserved by $\iota$. $\square$

### Integrality of the torsion values

**Theorem 7.4.2 (Torsion values of the Weierstrass function).** Let $d$ be a squarefree integer with $d \equiv 3 \pmod 4$, and let $L$ be a lattice with complex multiplication by $\mathcal{O}_K$, $K = \mathbb{Q}(\sqrt{-d})$. Let $l \ge 5$ be a prime with $l \nmid d$, let $\iota : \mathbb{C} \to \mathbb{C}_l$ be a field isomorphism, and let $\lambda \in \mathbb{C}_l$, $\lambda \ne 0$, with
$$\lambda^4 \iota(g_2(L)),\ \lambda^6 \iota(g_3(L)) \in \breve{\mathbb{Q}}_l, \qquad |\lambda^4 \iota(g_2(L))| \le 1, \quad |\lambda^6 \iota(g_3(L))| \le 1,$$
$$\bigl|(\lambda^4 \iota(g_2(L)))^3 - 27 (\lambda^6 \iota(g_3(L)))^2\bigr| = 1 .$$
Let $z \in \mathbb{C}$ and $N > 0$ with $l \nmid N$, $Nz \in L$ and $z \notin L$. Then
$$\lambda^2 \iota(\wp(z)) \in \breve{\mathbb{Q}}_l, \quad \lambda^3 \iota(\wp'(z)) \in \breve{\mathbb{Q}}_l, \quad |\lambda^2 \iota(\wp(z))| \le 1, \quad |\lambda^3 \iota(\wp'(z))| \le 1 .$$

Lean: `ReciprocityTheory.ChartRestriction.L1.cm4` (also `ReciprocityTheory.ChartRestriction.L1.cmTorsion_of_point`, which derives it from the proposition on scaled torsion points)

*Proof.* Put $g_2' = \lambda^4 \iota(g_2(L))$ and $g_3' = \lambda^6 \iota(g_3(L))$. The hypotheses say that $(g_2', g_3')$ is a good pair. By the proposition, $P = (\lambda^2 \iota(\wp(z)), \lambda^3 \iota(\wp'(z))/2)$ is a point of its curve, $P \ne O$ and $NP = O$. By [the theorem on torsion points](/entry/tor-kur/), both coordinates of $P$ lie in $\breve{\mathbb{Q}}_l$. By the lemma that torsion points are integral, in the same section, both have absolute value at most $1$. Multiply the second coordinate by $2$: then $\lambda^3 \iota(\wp'(z)) \in \breve{\mathbb{Q}}_l$, and $|2| \le 1$ keeps the bound. $\square$

**Example 7.4.3.** Take $d = 3$, so $\omega_K = (1 + i\sqrt 3)/2$ is a primitive sixth root of unity, and let $L = \mathbb{Z} + \mathbb{Z}\omega_K$. Then $\omega_K L = L$ and $g_2(L) = 0$, since the sum defining $g_2$ is invariant under $\omega \mapsto \omega_K \omega$ and $\omega_K^{-4} \ne 1$. For $l \ge 5$, choose $\lambda$ with $\lambda^6 \iota(g_3(L)) = 1$. Then $g_2' = 0$, $g_3' = 1$, and $|0 - 27| = 1$. The theorem says that $\lambda^2 \iota(\wp(z))$ is integral and lies in $\breve{\mathbb{Q}}_l$ for every $z$ of order $N$ prime to $l$ in $\mathbb{C}/L$.

**Remark 7.4.4.** Classically, the theorem follows from the theory of complex multiplication: the values $\wp(z)$ at torsion points generate abelian extensions of $K(j(L))$ (Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Chapter II), and good reduction at $l$ makes the torsion prime to $l$ unramified at $l$ (Silverman, *The Arithmetic of Elliptic Curves*, Proposition VII.3.1 and Theorem VII.7.1). The proof here uses neither. It needs only good reduction over $\breve{\mathbb{Q}}_l$, and it holds for any lattice.

**Remark 7.4.5 (Formalization).** The hypotheses that $d$ is squarefree, that $d \equiv 3 \pmod 4$, that $l \nmid d$ and that $L$ has complex multiplication are not used in the proof: they are introduced and discarded at [TorStatus.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorStatus.lean#L16). They are part of the statement because the statements on complex multiplication that the development uses share one list of hypotheses. In the proposition on scaled torsion points, $N = 0$ is allowed; then the conclusion $NP = O$ is trivial.
