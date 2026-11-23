---
title: Good models from the j-invariant
decls:
  - ReciprocityTheory.ChartRestriction.L1.goodReduction_of_integral_unramified
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Good models from the j-invariant

This section proves that a lattice with complex multiplication has a good model over $\breve{\mathbb{Q}}_l$ for each prime $l \ge 5$ with $l \nmid d$. That is, there is $\lambda \ne 0$ such that the scaled invariants $\lambda^4 \iota(g_2)$ and $\lambda^6 \iota(g_3)$ form a good pair in the sense of [the section on torsion points](/entry/tor-kur/). It assumes two facts on the [[j-invariant|9538W1K1EX]]: it is integral at every prime, and it is unramified at the primes $l \nmid d$. These are the hypotheses that the theorems of [the previous section](/entry/cm4/) and of the next section need. The result gives [the good model](/entry/good-model/) of the chapter on CM periods.

We keep the notation of the previous section: $d$ is squarefree with $d \equiv 3 \pmod 4$, $\omega_K = (1 + i\sqrt d)/2$, $L$ is a lattice with $\omega_K L \subseteq L$, $l$ is a prime and $\iota : \mathbb{C} \to \mathbb{C}_l$ is a field isomorphism. The $j$-invariant of $L$ is
$$j(L) = \frac{1728\, g_2(L)^3}{g_2(L)^3 - 27 g_3(L)^2}$$
([the $j$-invariant](/learn/elliptic-curves/#elliptic-curves-and-the-j-invariant)).

**Definition 7.5.1 (Good model).** A *good model* of $L$ at $(l, \iota)$ is a pair $(g_2, g_3)$ of elements of $\breve{\mathbb{Q}}_l$ with $|g_2| \le 1$, $|g_3| \le 1$, $|g_2^3 - 27 g_3^2| = 1$, and $\lambda \in \mathbb{C}_l$, $\lambda \ne 0$, with $g_2 = \lambda^4 \iota(g_2(L))$ and $g_3 = \lambda^6 \iota(g_3(L))$.

The curve of a good model is isomorphic over $\mathbb{C}_l$ to the image under $\iota$ of the curve of $L$, by $(x, y) \mapsto (\lambda^2 x, \lambda^3 y)$, and it has good reduction.

### The main theorem

**Theorem 7.5.2 (Good models of CM lattices).** Assume:

1. (Integrality of $j$) for every $d, L$ as above, every prime $l$ and every field isomorphism $\iota : \mathbb{C} \to \mathbb{C}_l$, $|\iota(j(L))| \le 1$;
2. (Unramifiedness of $j$) for every $d, L$ as above, every prime $l \ge 5$ with $l \nmid d$ and every $\iota$, $\iota(j(L)) \in \breve{\mathbb{Q}}_l$.

Then for every $d, L$ as above, every prime $l \ge 5$ with $l \nmid d$ and every $\iota$, the lattice $L$ has a good model at $(l, \iota)$.

Lean: `ReciprocityTheory.ChartRestriction.L1.goodReduction_of_integral_unramified`

Both assumptions hold. The number $j(L)$ is an algebraic integer (Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Theorem II.6.1), so its image under any $\iota$ has absolute value at most $1$. The field $K(j(L))$ is the Hilbert class field of $K = \mathbb{Q}(\sqrt{-d})$ (same book, Theorem II.4.3), which is unramified over $K$; for $l \nmid d$ the prime $l$ is unramified in $K$, so $\mathbb{Q}(j(L))$ is unramified at $l$ and $\iota(j(L))$ lies in $\breve{\mathbb{Q}}_l$. Here the theorem takes them as hypotheses.

The proof has three steps. Write $J = \iota(j(L))$. A model exists as soon as $|J|$ is a cube power of $l$ and $|J - 1728|$ is an even power of $l$. Then two lemmas prove these two conditions with torsion points of complex multiplication.

### A model from the valuations of $J$

**Lemma 7.5.3 (Model from valuations).** Let $l \ge 5$ and $\iota$ be given, and let $L$ be any lattice. Suppose that $J = \iota(j(L)) \in \breve{\mathbb{Q}}_l$, $|J| \le 1$, and
- if $J \ne 0$, then $|J| = l^{3m}$ for some $m \in \mathbb{Z}$;
- if $J \ne 1728$, then $|J - 1728| = l^{2n}$ for some $n \in \mathbb{Z}$.

Then $L$ has a good model at $(l, \iota)$.

Lean: `ReciprocityTheory.ChartRestriction.L1.model_of_valDiv` (also `ReciprocityTheory.ChartRestriction.L1.model_generic`)

*Proof.* Put $a = \iota(g_2(L))$ and $b = \iota(g_3(L))$. Then $a^3 - 27 b^2 \ne 0$. Since $l \ge 5$, $|27| = |1728| = 1$. If $a = 0$, choose $\lambda$ with $\lambda^6 = b^{-1}$; the model is $(0, 1)$, with $|0 - 27| = 1$. If $b = 0$, choose $\lambda$ with $\lambda^4 = a^{-1}$; the model is $(1, 0)$. Now let $a, b \ne 0$. Then $J \ne 0$ and $J \ne 1728$, so $|J| = l^{3m}$ and $|J - 1728| = l^{2n}$. Put $X = l^m$ and $Y = l^n$, and
$$c = \frac{27 J}{J - 1728} = \frac{a^3}{b^2}, \qquad t = l^{m - n}, \qquad g_2 = t^2 c, \qquad g_3 = t^3 c .$$
Then $c, t \in \breve{\mathbb{Q}}_l$, and $|t| = Y/X$, $|c| = X^3/Y^2$ and $|c - 27| = |27 \cdot 1728/(J - 1728)| = Y^{-2}$. Hence
$$|g_2|^3 = \frac{Y^6}{X^6} \cdot \frac{X^9}{Y^6} = |J| \le 1, \qquad |g_3|^2 = \frac{Y^6}{X^6} \cdot \frac{X^6}{Y^4} = |J - 1728| \le 1,$$
and $|J - 1728| \le 1$ holds because $|J| \le 1$. The discriminant is $g_2^3 - 27 g_3^2 = t^6 c^2 (c - 27)$, of absolute value $\frac{Y^6}{X^6} \cdot \frac{X^6}{Y^4} \cdot \frac{1}{Y^2} = 1$. Finally choose $\lambda$ with $\lambda^2 = t a / b$. Then $\lambda^4 a = t^2 a^3/b^2 = g_2$ and $\lambda^6 b = t^3 a^3/b^2 = g_3$. $\square$

### Torsion of complex multiplication

The two conditions on $J$ come from units. For an elliptic curve with good reduction, the $x$-coordinate of a torsion point of suitable order is a unit, and a product of such coordinates lies in a field generated over $\mathbb{Q}$ by $g_2$, $g_3$ and $\omega_K$. Values in $\breve{\mathbb{Q}}_l$ have absolute values in $l^{\mathbb{Z}}$, since the field is unramified. This forces divisibility of the exponents.

**Lemma 7.5.4 (Kernel products).** Let $l \ge 5$ be a prime with $l \nmid d$, and let $e = 2$, or $e = 3$ and $d \ne 3$. Then there are $N \in \mathbb{N}$ and a finite set $T \subset \mathbb{C}$ with $l \nmid N$, $e \nmid N$ and $e \nmid |T|$, such that each $z \in T$ has $z \notin L$ and $Nz \in L$, and $\prod_{z \in T} \wp(z)$ lies in every subfield of $\mathbb{C}$ that contains $g_2(L)$, $g_3(L)$ and $\omega_K$.

Lean: `ReciprocityTheory.ChartRestriction.L1.kerProd` (also `ReciprocityTheory.ChartRestriction.L1.kerProd_prin`, `ReciprocityTheory.ChartRestriction.L1.kerProd_ideal`)

In the main case one takes $\alpha = r + \sqrt{-d} \in \mathcal{O}_K$ with odd norm $N = r^2 + d$, and $T$ a set of representatives, up to sign, of the nonzero points of $\mathbb{C}/L$ killed by $\alpha$, so $2|T| + 1 = N$. For $e = 2$ one takes $r = 0$; then $N = d$ and $|T| = (d - 1)/2$ is odd because $d \equiv 3 \pmod 4$. When $3 \mid d$ and $e = 3$, the proof uses a prime ideal of $\mathcal{O}_K$ in place of $\alpha$.

**Lemma 7.5.5 (Units at torsion points).** Let $l \ge 5$, $\mu \in \mathbb{C}_l$ with $\mu^{12} \iota(g_2(L)^3 - 27 g_3(L)^2) = 1$, $|\mu^4 \iota(g_2(L))| \le 1$ and $|\mu^6 \iota(g_3(L))| \le 1$. Let $e = 3$ and $|\mu^4 \iota(g_2(L))| < 1$, or $e = 2$ and $|\mu^6 \iota(g_3(L))| < 1$. Let $N$ with $l \nmid N$ and $e \nmid N$, and let $z \notin L$ with $Nz \in L$. Then $|\mu^2 \iota(\wp(z))| = 1$.

Lean: `ReciprocityTheory.ChartRestriction.L1.unit_point` (also `ReciprocityTheory.ChartRestriction.L1.unit_prod`)

*Proof.* The scaled invariants form an integral model with $|\Delta| = 1$, and $P = (\mu^2 \iota(\wp(z)), \mu^3 \iota(\wp'(z))/2)$ is a point on it with $NP = O$ ([the proposition on scaled torsion points](/entry/cm4/)). The point $P$ is integral by the lemma on torsion points in [the section on torsion](/entry/tor-kur/). Suppose $e = 3$ and $|x(P)| < 1$. Then $|g_2| < 1$ forces $|g_3| = 1$ and $|y(P)| = 1$, and the doubling formulas give $|x(2P)| < 1$ and $|y(2P) + y(P)| < 1$, so $2P$ and $-P$ have the same reduction. Thus $3P$ lies in the kernel of reduction. It is torsion of order prime to $l$, so $3P = O$, which contradicts $3 \nmid N$. For $e = 2$ the reduced curve is $y^2 = x^3 - \frac{g_2}{4}x$, whose points with $x = 0$ have order $2$, and the same argument applies with $2 \nmid N$. $\square$

Multiplying over $T$ gives $|\mu|^{2|T|}\, \bigl|\iota\bigl(\prod_{z \in T} \wp(z)\bigr)\bigr| = 1$.

### The two valuation lemmas

**Lemma 7.5.6 ($|J|$ is a cube).** Under the hypotheses of the main theorem for $(d, L, l, \iota)$, if $J \ne 0$ then $|J| = l^{3m}$ for some $m \in \mathbb{Z}$.

Lean: `ReciprocityTheory.ChartRestriction.L1.valDiv3`

*Proof.* If $|J| = 1$, take $m = 0$. Let $|J| < 1$. Then $|J - 1728| = 1$, so $g_2(L) \ne 0$ and $g_3(L) \ne 0$, and $d \ne 3$, since $g_2 = 0$ for $d = 3$. Rescale $L$ to a lattice $L_0$ with complex multiplication by $\mathcal{O}_K$ and $g_2(L_0) = g_3(L_0) = 27 j/(j - 1728)$. Put $c = \iota(g_2(L_0)) = 27J/(J - 1728)$; then $|c| = |J|$ and $|c^3 - 27c^2| = |J|^2$. Choose $\mu$ with $\mu^{12}(c^3 - 27c^2) = 1$, so $|\mu|^{12} |J|^2 = 1$. Then $|\mu^4 c|^3 = |J| < 1$ and $|\mu^6 c| = 1$. Apply the kernel products lemma with $e = 3$ to $L_0$, and the units lemma: $|\mu|^{2|T|} |\iota(\Pi)| = 1$ with $\Pi = \prod_{z \in T}\wp_{L_0}(z)$. The field $\iota^{-1}(\breve{\mathbb{Q}}_l)$ contains $g_2(L_0)$, $g_3(L_0)$ (because $J \in \breve{\mathbb{Q}}_l$) and $\omega_K$ (because $\iota(\omega_K)$ is a root of $X^2 - X + (d+1)/4$, unramified at $l$). So $\iota(\Pi) \in \breve{\mathbb{Q}}_l$, and $|\iota(\Pi)| = l^a$, $|J| = l^n$ for integers $a, n$. From $|\mu|^{12} = l^{-2n}$ and $|\mu|^{2|T|} = l^{-a}$ we get $n|T| = 3a$. As $3 \nmid |T|$, $3 \mid n$. $\square$

**Lemma 7.5.7 ($|J - 1728|$ is a square).** Under the hypotheses of the main theorem for $(d, L, l, \iota)$, if $J \ne 1728$ then $|J - 1728| = l^{2m}$ for some $m \in \mathbb{Z}$.

Lean: `ReciprocityTheory.ChartRestriction.L1.valDiv2`

*Proof.* Write $|J - 1728| = l^b$, which holds as $J - 1728 \in \breve{\mathbb{Q}}_l$ is nonzero. If $b = 0$, take $m = 0$. Otherwise $|J - 1728| < 1$, so $|J| = 1$, and $g_2(L), g_3(L) \ne 0$. With $L_0$ and $c$ as before, $|c| = |J - 1728|^{-1}$ and $\mu^{12} = \iota(\Delta(L_0))^{-1}$ gives $|\mu|^4 = |J - 1728|$. Then $|\mu^4 c| = 1$ and $|\mu^6 c| < 1$. The kernel products lemma with $e = 2$ and the units lemma give $|\mu|^{2|T|} l^a = 1$ with $|T|$ odd. With $|\mu|^4 = l^b$ this gives $b|T| = -2a$, so $b$ is even. $\square$

*Proof of the main theorem.* By the hypotheses, $J \in \breve{\mathbb{Q}}_l$ and $|J| \le 1$. The two valuation lemmas give the conditions of the lemma on models from valuations, which gives the good model. $\square$

**Remark 7.5.8 (Formalization).** The integrality hypothesis is stated for every prime $l$, with no condition $l \ge 5$ or $l \nmid d$: [Interface.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/Interface.lean#L9). This is the true classical statement. The fact $|1728| = 1$ for $l \ge 5$ is proved three times, at [RedModel.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/RedModel.lean#L24), [Norm1728EqOneOfFiveLe.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/Norm1728EqOneOfFiveLe.lean#L27) and [NormWeierstrassCoeffSmallJ.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/NormWeierstrassCoeffSmallJ.lean#L59), and $|27| = 1$ also three times. The kernel product condition quantifies over all subfields of $\mathbb{C}$: [RedDefs.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/RedDefs.lean#L42).
