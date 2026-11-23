---
title: The local doubling integral at a twist place
decls:
  - GlobalTheory.T.unramifiedDoublingIntegral_twisted_place_eigenvector
  - GlobalTheory.TwistedZeta.local_zeta_twisted
  - GlobalTheory.TwistedZeta.lower_eigen
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local doubling integral at a twist place

A theta chain is a sequence of [[theta|6WB6TKE70H]] lifts between unitary groups. Its inner products are computed by [the doubling method](/learn/theta/#the-doubling-method). At most places the local data are unramified, and the local integral is the unramified doubling integral of Piatetski-Shapiro and Rallis. At a *twist place* the chain carries a character $\xi$ that is tamely ramified, and the local vector is not spherical but of a parahoric type. This section computes the local integral at such a place. The main result is the theorem on the doubling integral at a twist place at the end. It reduces the ramified integral to the unramified integral for $\mathrm{GL}_{lt}$, which we take as a hypothesis. The next section uses it, through [the local factor at a twist place](/entry/local-factor/).

Throughout, $k$ is a nonarchimedean local field with ring of integers $\mathcal{O}$, maximal ideal $\mathfrak{p}$, residue field of $q$ elements, and a uniformizer $\varpi$. A character $\mu \colon k^\times \to \mathbb{C}^\times$ is *unramified* if it is trivial on $\mathcal{O}^\times$ and *tame* if it is trivial on $1 + \mathfrak{p}$. We use [smooth representations](/learn/representations/#smooth-representations-of-p-adic-groups), [unramified representations](/learn/representations/#unramified-representations), [depth zero types](/learn/representations/#depth-zero-representations-and-types) and [[Haar measure|VY0HXD3GC4]] ([Haar measure](/learn/analysis/#haar-measure)).

**Definition 2.2.1 (Parahoric types).** Fix $r, N \geq 0$ and put $G = \mathrm{GL}_{r+N}(k)$, with blocks of sizes $r$ and $N$. Let $J \subset G$ be the parahoric subgroup of the elements of $\mathrm{GL}_{r+N}(\mathcal{O})$ whose lower left $N \times r$ block lies in $\mathfrak{p}$. For $j \in J$ write $j_{22}$ for its lower right block; then $\det j_{22} \in \mathcal{O}^\times$. Let $\xi$ be a tame character, $\pi$ a representation of $G$ on a complex vector space $V$, and $\ell$ a linear form on $V$.

- The *$\xi$-type space* $V^{J, \xi}$ is the space of $x \in V$ with $\pi(j)x = \xi(\det j_{22})\, x$ for all $j \in J$.
- The form $\ell$ has *dual type* $\xi$ if $\ell(\pi(j)v) = \xi(\det j_{22})\, \ell(v)$ for all $j \in J$ and $v \in V$.
- For $g \in G$, the *twisted Hecke operator* $T_g$ takes $x$ to $\sum_{j \in R} \xi(d_j)^{-1} \pi(jg)x$, where $R \subset J$ is a set of representatives for the cosets $Jg/J$ and $d_j$ is a unit attached to $j$. The vector $y$ is the value $T_g x$ if this sum equals $y$ for every choice of $(R, d)$.

For $e \in \mathbb{Z}^N$ put $t_e = \mathrm{diag}(1_r, \varpi^{e_1}, \dots, \varpi^{e_N})$, and for a subset $s \subseteq \{1, \dots, N\}$ let $1_s \in \mathbb{Z}^N$ be its indicator.

**Definition 2.2.2 (Generic vectors with parameters).** For a multiset $B$ of $N$ elements of $\mathbb{C}^\times$ and $0 \leq n \leq N$ put
$$\gamma^{r}_n(B) = q^{(rn + n(N-n))/2}\, e_n(B),$$
where $e_n$ is the $n$th elementary symmetric function. A vector $x \in V$ is *generic of type $\xi$ with parameters $B$* if $x \in V^{J,\xi}$, $B$ has $N$ elements, and $T_{t_{1_s}} x = \gamma^{r}_{|s|}(B)\, x$ for every subset $s$.

For $r = 0$ and $\xi = 1$ this is the classical description of an unramified vector by its Hecke eigenvalues. Then $J = \mathrm{GL}_N(\mathcal{O})$, $t_{1_s}$ is conjugate to $\mathrm{diag}(\varpi 1_n, 1_{N-n})$ with $n = |s|$, and $q^{n(N-n)/2} e_n(B)$ is the eigenvalue of the $n$th Hecke operator on the spherical vector with Satake parameters $B$.

**Definition 2.2.3 (Height function).** A function $H \colon \mathrm{GL}_n(k) \to \mathbb{R}$ is a *height* if it is invariant on both sides under $\mathrm{GL}_n(\mathcal{O})$ and $H(\mathrm{diag}(\varpi^{e_1}, \dots, \varpi^{e_n})) = q^{-|e|}$ for all $e \in \mathbb{Z}^n$, where $|e| = \sum_i |e_i|$.

For a multiset $\alpha$ of $n$ elements of $\mathbb{C}^\times$ let $L(s, \alpha) = \prod_i (1 - \alpha_i q^{-s})^{-1}$, and let $\alpha^{-1}$ be the multiset of the inverses.

**Theorem 2.2.4 (Unramified doubling identity).** Let $k$ have characteristic zero, let $\mu$ be a Haar measure on $\mathrm{GL}_n(k)$ with $\mu(\mathrm{GL}_n(\mathcal{O})) = 1$, let $\pi$ be a representation with Satake parameters $\alpha$, and let $\omega$ be a zonal spherical matrix coefficient of $\pi$. Let $f_s$ be the normalised spherical section of the degenerate principal series of $\mathrm{GL}_{2n}(k)$ used in the doubling method, and $\iota \colon \mathrm{GL}_n \times \mathrm{GL}_n \to \mathrm{GL}_{2n}$ the doubling embedding. Then there is $s_0$ such that for $\mathrm{Re}\, s > s_0$ the function $g \mapsto f_s(\iota(g, 1))\, \omega(g)$ is integrable and
$$\int_{\mathrm{GL}_n(k)} f_s(\iota(g,1))\, \omega(g)\, d\mu(g) = L(s + \tfrac12, \alpha)\, L(s + \tfrac12, \alpha^{-1}) \prod_{i=1}^{n} (1 - q^{-(2s+i)}).$$
(S. Gelbart, I. Piatetski-Shapiro and S. Rallis, *Explicit Constructions of Automorphic L-Functions*, Lecture Notes in Math. 1254, Springer, 1987.)

We take this identity as given. It is one of the third place hypotheses of the proof ([the definition of these hypotheses](/step/unitary-group-third-place-hypotheses-def/)).

**Lemma 2.2.5 (Lower block eigenvalues).** Let $\varpi$ be a uniformizer, let $r, l, t \geq 0$ and $N = lt$. Let $\xi$ be tame and not unramified, and $\mu_0$ unramified. Let $B$ be a multiset of $N$ elements and let $\alpha = B \cdot ((\mu_0\xi)(\varpi))^{-1}$. Let $H$ be a height on $\mathrm{GL}_{r+N}(k)$. Let $\mu_K$ be a measure on $\mathrm{GL}_N(k)$ and $Z \colon \mathrm{GL}_N(k) \to \mathbb{C}$ a function with this property: every function $f$ on $\mathrm{GL}_N(k)$ that is bi-invariant under $K = \mathrm{GL}_N(\mathcal{O})$ and satisfies $\sum_{g \in R} f(mg) = \gamma^0_{|s|}(\alpha) f(m)$ for each $s$, each $m$, and each set $R$ of representatives of $K t_{1_s} K/K$, is equal to $f(1) Z$. Let $x$ be generic of type $\xi$ with parameters $B$, and let $\ell$ have dual type $\xi$. Then for every $e \in \mathbb{Z}^N$
$$\ell(\pi(t_e)x) = (\mu_0\xi)(\varpi)^{\sum_i e_i}\, q^{-r|e|/2}\, Z(\varpi^e)\, \ell(x).$$

Lean: `GlobalTheory.TwistedZeta.lower_eigen`.

*Proof.* For $m \in \mathrm{GL}_N(k)$ put $f_1(m) = \xi(\det m)^{-1}\, \ell(\pi(\mathrm{diag}(1_r, m))x)$, divided by a fixed power of the height of $\mathrm{diag}(1_r, m)$. The type conditions on $x$ and $\ell$ make $f_1$ bi-invariant under $\mathrm{GL}_N(\mathcal{O})$. The eigenvalue conditions on $x$ make it an eigenfunction of the spherical Hecke operators with parameters $B \cdot \xi(\varpi)^{-1}$. Twisting by $\mu_0^{-1} \circ \det$ gives a spherical eigenfunction $f_2$ with parameters $\alpha$, since $\mu_0$ is unramified. The hypothesis on $Z$ gives $f_2 = f_2(1) Z$, and $f_2(1) = \ell(x)$. Evaluate at $\varpi^e$: the characters give the factor $(\mu_0\xi)(\varpi)^{\sum e_i}$, and the height gives $q^{-r|e|/2}$. $\square$

The hypothesis on $Z$ is the uniqueness of the zonal spherical function: a spherical Hecke eigenfunction is determined by its eigenvalues and its value at $1$.

We now fix the local theta datum of one step of the chain. Let $a = r + lt$ and $b = r + (l+1)t$. On functions on the space $M_{b \times a}(k)$ of $b \times a$ matrices, and for a character $\mu$, let
$$\omega_\mu(g, h)\Phi(x) = \mu(\det g)\, \mu(\det h)^{-1} |\det g|^{b/2} |\det h|^{-a/2}\, \Phi(h^{-1} x g)$$
for $g \in \mathrm{GL}_a(k)$ and $h \in \mathrm{GL}_b(k)$. This is the model of the [Weil representation](/learn/theta/#the-weil-representation) ([[Weil representation|CD20HVR9V8]]) of a split dual pair at a split place. Let $\Phi_\xi(x) = \xi(\det x_{11})^{-1}$ if $x$ is integral, its upper left $r \times r$ block $x_{11}$ has unit determinant, and its lower left block lies in $\mathfrak{p}$; let $\Phi_\xi(x) = 0$ otherwise. Let $\nu$ be the Haar measure on $k$ with $\nu(\mathcal{O}) = 1$, and $\langle \Phi_1, \Phi_2 \rangle = \int \Phi_1 \overline{\Phi_2}$ for the product measure on $M_{b \times a}(k)$.

**Theorem 2.2.6 (Doubling integral at a twist place).** Let $k$ have characteristic zero, and assume the unramified doubling identity. Let $\varpi$ be a uniformizer and $r, t, l \geq 0$. Let $\xi$ be unitary, tame and not unramified, and let $\mu_0$ be unitary and unramified. Let $B$ be a multiset of $lt$ elements, let $\alpha = B \cdot ((\mu_0\xi)(\varpi))^{-1}$, and let $\rho \in \mathbb{R}$ with $|\alpha_i| \leq q^\rho$ and $|\alpha_i|^{-1} \leq q^\rho$ for all $i$. Let $H$ be a height on $G = \mathrm{GL}_{r+lt}(k)$ and $m$ a Haar measure on $G$ with $m(J) = 1$. Put $c(g) = \langle \omega_{\mu_0\xi}(g, 1)\Phi_\xi, \Phi_\xi \rangle$. Then $c(1) \neq 0$, and there is $\zeta \colon G \to \mathbb{C}$ such that:

1. for every representation $\pi$ of $G$, every $x$ generic of type $\xi$ with parameters $B$, every $\ell$ of dual type $\xi$ and every $g \in G$, $\overline{c(g)}\, \ell(\pi(g)x) = \overline{c(1)}\, \zeta(g)\, \ell(x)$;
2. $\zeta = 1$ on $J$;
3. for $\mathrm{Re}\, s > \rho - \frac12$, the function $\zeta H^{s - t/2}$ is integrable and
$$\int_G \zeta(g)\, H(g)^{s - t/2}\, dm(g) = L(s + \tfrac12, \alpha)\, L(s + \tfrac12, \alpha^{-1}) \prod_{i=1}^{lt} (1 - q^{-(2s+i)}).$$

Lean: `GlobalTheory.TwistedZeta.local_zeta_twisted` (also `GlobalTheory.T.unramifiedDoublingIntegral_twisted_place_eigenvector`, a second name).

*Proof.* Let $N = lt$ and $K = \mathrm{GL}_N(\mathcal{O})$. For $e \in \mathbb{Z}^N$ write $C_e = J t_e J$.

1. Fix a Haar measure $\mu_K$ on $\mathrm{GL}_N(k)$ with $\mu_K(K) = 1$. There is a spherical function with parameters $\alpha$ whose zonal integral $Z$ has the uniqueness property of the lemma.
2. The volumes satisfy $m(C_e) = q^{r|e|} \mu_K(K t_e K)$, and the cells $C_e$ for decreasing $e$ are disjoint.
3. The coefficient $c$ transforms on both sides under $J$ by the characters $\xi(\det j_{22})$, and it vanishes off the union of the cells. Its value at $t_e$ is a unit times $C_0\, q^{-b|e|/2}$, with $C_0 > 0$. In particular $c(1) = C_0 \neq 0$.
4. Define $\zeta$ on $C_e$, for decreasing $e$, as $q^{-(2r + (l+1)t)|e|/2}\, Z(\varpi^e)$, and as $0$ off the cells. The cell $C_0$ is $J$, and $Z(1) = 1$, so claim 2 holds.
5. Claim 1 on a cell $C_e$: by the transformation laws of $c$ and $\ell$ under $J$ it suffices to take $g = t_e$, since the characters of $j$ and $j'$ in $g = j t_e j'$ cancel ($\xi$ is unitary). Step 3 gives $c(t_e) = u\, C_0\, q^{-b|e|/2}$ with $u = (\mu_0\xi)(\varpi)^{\sum e_i}$, and the lemma gives $\ell(\pi(t_e)x) = u\, q^{-r|e|/2} Z(\varpi^e) \ell(x)$. Since $|u| = 1$ and $b + r = 2r + (l+1)t$, both sides of claim 1 equal $C_0\, q^{-(2r+(l+1)t)|e|/2} Z(\varpi^e)\, \ell(x)$. Off the cells both sides vanish: $c$ is zero there, since $\xi$ is tame and ramified, and $\zeta$ is zero by definition.
6. Claim 3: $\zeta$ and $H$ are constant on each cell, $H(t_e) = q^{-|e|}$, and $\zeta$ vanishes off the cells. So the integral of $\zeta H^{s-t/2}$ is the sum over $e$ of $m(C_e)\, \zeta(t_e)\, q^{-|e|(s - t/2)}$. By step 2 and the definition of $\zeta$, the exponents of $q$ add up to those of the doubling series of $\mathrm{GL}_N$ for the spherical function $Z$. The unramified doubling identity sums this series to the right side, for $\mathrm{Re}\, s > \rho - \frac12$.

This proves the theorem. $\square$

The function $\zeta$ depends only on the local data $(\varpi, \xi, \mu_0, B)$. It does not depend on $\pi$, $x$ or $\ell$. This is what lets the next section use the same $\zeta$ for all automorphic forms of a given type.

**Remark 2.2.7 (Formalization).** The theorem is at [UnramifiedDoublingIntegralTwistedPlaceEigenvecto.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UnramifiedDoublingIntegralTwistedPlaceEigenvecto.lean#L213), the lemma at line 137. The module name is cut off, and its second name speaks of an eigenvector, while the conclusion is a functional equation and an integral. The unramified doubling identity is a hypothesis, stated in [PairwiseDisjointCell.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/PairwiseDisjointCell.lean#L314). It is applied here at a ramified place, after the reduction of steps 1 to 6 to $\mathrm{GL}_{lt}$. The characteristic zero assumption is used only to apply it. The lemma takes the uniqueness of the zonal spherical function as a hypothesis; the theorem supplies it in step 1. We have not opened the proofs of the lemmas behind steps 1, 2, 3 and 6, nor unfolded the spherical section, the doubling embedding, the zonal integral and the unit $d_j$ of the twisted Hecke operator.
