---
title: The nef case and the main theorem
decls:
  - GlobalTheory.NefUpper.main
  - GlobalTheory.T.arith_nef_volume_upper_bound
  - GlobalTheory.HSNef.arithHilbertSamuel_of_ampleHS
  - GlobalTheory.T.arithHilbertSamuel_nef_of_ample
  - GlobalTheory.arithHilbertSamuel_of_principalisation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The nef case and the main theorem

This section proves the main theorem of the chapter: principalisation of ideals implies the arithmetic Hilbert-Samuel formula for nef hermitian line bundles. The proof has three inputs: [the arithmetic intersection calculus](/entry/ar-calc-of-principalisation/), [the ample formula](/entry/ample-hs-of-principalisation/), and the fact that semipositive metrics pull back to semipositive metrics. We prove an upper bound for the number of small sections, quote a lower bound, and combine them. The main theorem is used in [the published results](/step/published-results-arithmetic/) of the proof, through [the Hilbert-Samuel formula from the literature](/entry/arith-hilbert-samuel-of-literature/).

### Nef bundles

Let $X$ be an arithmetic variety of relative dimension $D$ over $k$. A small section of a hermitian line bundle $\bar M$ is a global section $s$ with $\|s\|_\sigma(y) \le 1$ for every $\sigma$ and every $y \in X_\sigma(\mathbb{C})$.

**Definition 6.7.1 (Nef hermitian line bundle).** A hermitian line bundle $\bar L$ on $X$ is nef if three conditions hold.
1. Semipositivity: the weight of $\bar L$ is semipositive at every embedding.
2. Vertical curves: for every integral closed curve $Z \subseteq X$ that is an algebra over a finite field $\kappa$, the degree of $L|_Z$ over $\kappa$ is at least $0$.
3. Horizontal curves: for every integral closed curve $Z \subseteq X$ with $\Gamma(Z, \mathcal{O}_Z)$ of characteristic zero, there is a rational section $r$ of $L|_Z$ such that the arithmetic degree $\sum_z \operatorname{mult}_z(\operatorname{div} r) \log\#\kappa(z) - \sum_\sigma \sum_{y} \log\|r\|_\sigma(y)$ is at least $0$.

A bundle that satisfies condition 2 is nef on the fibres. This is Zhang's notion of a nef hermitian line bundle; see the [arithmetic volume and bigness](/learn/arakelov/#arithmetic-volume-and-bigness) of Volume 1.

**Definition 6.7.2 (Arithmetic Hilbert-Samuel formula).** The arithmetic Hilbert-Samuel formula is the statement: for every arithmetic variety $X$ of relative dimension $D$, all hermitian line bundles $\bar L$ and $\bar N$ on $X$ with $\bar L$ nef, and every self intersection $a$ of $\bar L$, the set of small sections of $\bar L^m \otimes \bar N$ is finite for all large $m$, and
$$\log \# \{\text{small sections of } \bar L^m \otimes \bar N\} = \frac{a}{(D+1)!} \, m^{D+1} + o(m^{D+1}) \qquad (m \to \infty).$$

Pull back of semipositivity is the statement: for arithmetic varieties $X$ and $Y$ over $k$ of relative dimensions $D$ and $E$ and every morphism $\pi : Y \to X$ over $k$, the pull back of a semipositive bundle on $X$ is semipositive on $Y$.

### The upper bound

**Theorem 6.7.3 (Upper bound for nef bundles).** Assume the arithmetic intersection calculus, the ample Hilbert-Samuel formula and the pull back of semipositivity. Let $\bar L$ be nef with self intersection $a$, and let $\bar N$ be any hermitian line bundle. Then for every $\varepsilon > 0$, for all large $m$,
$$\log \# \{\text{small sections of } \bar L^m \otimes \bar N\} \le \left( \frac{a}{(D+1)!} + \varepsilon \right) m^{D+1}.$$

Lean: `GlobalTheory.NefUpper.main` (also `GlobalTheory.T.arith_nef_volume_upper_bound`, a second name).

The main tool is a bound for the count of small sections by intersection numbers, which we take from the development. For $q \ge 3$ put $\Delta = \log(q/2)$ and, for real $b$ and $g$,
$$\alpha = \frac{b + (D+1)\big(\Delta + \tfrac{D}{2}\log 2\big) g}{(D+1)! \, \Delta}, \qquad \beta = \frac{(D+1) g}{2 (D+1)! \, \Delta},$$
$$\operatorname{bd}_q(b, g) = \log q \cdot \Big( \alpha + \beta \log\big((\alpha + 2\beta + 1)^2\big) \Big).$$
The bound says: let $x_1, \dots, x_D$ be algebraically independent rational functions, let $\bar W$ and $\bar H$ be hermitian line bundles such that every squarefree monomial $\prod_{i \in S} x_i$ is a small section of $\bar H$, and assume $\bar W \otimes \bar H$ nef with self intersection $b$ and degree $g = \deg (W \otimes H)_{\mathbb{C}}$. Then for every $q \ge 3$ the logarithm of the number of small sections of $\bar W$ is at most $\operatorname{bd}_q(b, g)$. This is where the ample formula and the pull back of semipositivity are used.

*Proof.* The function field of $X$ has transcendence degree $D$ over the field of fractions of $k$. Choose a transcendence basis $x_1, \dots, x_D$. By a result of the development there is a hermitian line bundle $\bar H$ such that $\bar N \otimes \bar H$ is nef and every squarefree monomial in the $x_i$ is a small section of $\bar H$. Put $\bar G = \bar N \otimes \bar H$.

Apply the bound to $\bar W = \bar L^m \otimes \bar N$ and $\bar H$, so that $\bar W \otimes \bar H = \bar L^m \otimes \bar G$. This bundle is nef, since powers and tensor products of nef bundles are nef. By the calculus it has a self intersection $b_m$, and $b_m / m^{D+1} \to a$, since the self intersection is a polynomial of degree $D + 1$ in $m$ with leading coefficient $a$. Also $b_m \ge 0$ by the arithmetic Kleiman inequality for nef bundles, which the development proves from the calculus. The degrees $g_m = \deg(L^m \otimes G)_{\mathbb{C}}$ are at least $0$ and $g_m / m^D \to \deg L_{\mathbb{C}}$. So for every $m$ and every $q \ge 3$,
$$\log \#\{\text{small sections of } \bar L^m \otimes \bar N\} \le \operatorname{bd}_q(b_m, g_m).$$

Now let $m \to \infty$ with $q$ fixed. Then $\alpha_m = a m^{D+1}/((D+1)!\,\Delta) + O(m^D)$ and $\beta_m = O(m^D)$, so $\beta_m \log((\alpha_m + 2\beta_m + 1)^2) = O(m^D \log m)$ and
$$\limsup_{m \to \infty} \frac{\operatorname{bd}_q(b_m, g_m)}{m^{D+1}} = \frac{a}{(D+1)!} \cdot \frac{\log q}{\log(q/2)}.$$
As $q \to \infty$ the factor $\log q / \log(q/2)$ tends to $1$, and $a \ge 0$. Given $\varepsilon > 0$, choose $q$ with $\frac{a}{(D+1)!}\big(\frac{\log q}{\log (q/2)} - 1\big) < \varepsilon/2$; then the bound is at most $(a/(D+1)! + \varepsilon) m^{D+1}$ for large $m$. $\square$

### The main theorem

We quote the matching lower bound, which the development proves from the calculus and the ample formula: if $\bar L$ is semipositive and nef on the fibres with self intersection $a$, then for every $\varepsilon > 0$ and all large $m$,
$$\left(\frac{a}{(D+1)!} - \varepsilon\right) m^{D+1} \le \log \#\{\text{small sections of } \bar L^m \otimes \bar N\}.$$

**Theorem 6.7.4 (Hilbert-Samuel formula from the ample case).** Assume the arithmetic intersection calculus, the ample Hilbert-Samuel formula and the pull back of semipositivity. Then the arithmetic Hilbert-Samuel formula holds.

Lean: `GlobalTheory.HSNef.arithHilbertSamuel_of_ampleHS` (also `GlobalTheory.T.arithHilbertSamuel_nef_of_ample`, a second name).

*Proof.* The set of small sections of any hermitian line bundle on an arithmetic variety is finite, since it is a discrete and bounded subset of a lattice; we take this from the development. A nef bundle is semipositive and nef on the fibres. So for every $\varepsilon > 0$ the lower bound and [the upper bound](/entry/nef-upper-main/) hold for all large $m$, and together they say that the difference between the logarithm of the count and $a m^{D+1}/(D+1)!$ is at most $\varepsilon m^{D+1}$ in absolute value. $\square$

**Theorem 6.7.5 (Arithmetic Hilbert-Samuel formula).** Principalisation of ideals implies the arithmetic Hilbert-Samuel formula. That is, assume principalisation. Let $X$ be an arithmetic variety of relative dimension $D$, let $\bar L$ be a nef hermitian line bundle with self intersection $a$, and let $\bar N$ be a hermitian line bundle. Then for all large $m$ the small sections of $\bar L^m \otimes \bar N$ form a finite set, and
$$\log \# \{\text{small sections of } \bar L^m \otimes \bar N\} = \frac{a}{(D+1)!} \, m^{D+1} + o(m^{D+1}).$$

Lean: `GlobalTheory.arithHilbertSamuel_of_principalisation`.

*Proof.* Principalisation gives the calculus by [the calculus from principalisation](/entry/ar-calc-of-principalisation/), the ample formula by [the ample case](/entry/ample-hs-of-principalisation/), and the pull back of semipositivity by a result of the development. Apply [the previous theorem](/entry/arith-hilbert-samuel-of-ample-hs/). $\square$

This is the theorem of Gillet and Soulé (1992), Abbes and Bouche (1995) and Zhang (1995) for nef bundles, in the form of Moriwaki; see the Notes and references.

**Remark 6.7.6 (Formalization).** The finiteness part is proved for every $m$, not only for large $m$. The lower bound needs only semipositivity and nefness on the fibres, not the condition on horizontal curves, and it does not use the pull back of semipositivity. The count is the cardinality of a set, which is $0$ for an infinite set. The bound $\operatorname{bd}_q$, the twist $\bar H$, the limit of $b_m / m^{D+1}$, the Kleiman inequality and the lower bound are cited results whose proofs we did not open.
