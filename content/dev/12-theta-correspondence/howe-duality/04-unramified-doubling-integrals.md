---
title: Unramified doubling integrals
decls:
  - GlobalTheory.ThK.Dbl.Inert.triv
  - GlobalTheory.ThK.Dbl.Inert.main
  - GlobalTheory.ThK.Dbl.locUnrSplit
  - PositivityTheory.ThKR.polynomial_vanishing_of_compactness
  - PositivityTheory.ThKEst.sigRapid
---
## Unramified doubling integrals

This section computes the local [doubling](/learn/theta/#the-doubling-method) zeta integral of a spherical section at an unramified finite place, first at an inert place and then at a split place, and proves two global facts on the difference of two matched theta integrals: a nonzero constant of proportionality in the base case, and rapid decay of its cuspidal part. All five results are inputs of the [spherical closure](/entry/close-sph/) and its [endgame](/entry/end-ab-sph/) in the chapter on theta series, which prove the [agreement of theta integrals](/step/theta-integrals-agree-def/) and [local matching](/step/local-matching-def/). The local computations are the unramified case of the doubling method of Piatetski-Shapiro and Rallis; the background is [unramified representations](/learn/representations/#unramified-representations) and [Haar measure](/learn/analysis/#haar-measure).

### The local integral at an inert place

Let $L$, $\mathcal{O}$ and an unramified involution $(\varpi, \sigma, q)$ be as in [the integral Witt theorem](/entry/witt-mod-pow/), so that $L$ is the unramified quadratic extension of $L^{\sigma}$ and its residue field has $q^2$ elements. Let $J_n$ be the antidiagonal matrix with entries $1$, let $G_n = U(J_n)$ with integral points $K_n$, and let $G_{2n}$ be the unitary group of the doubled form $J_n \oplus (-J_n)$, with Siegel parabolic $P$, Levi character $a : P \to L^{\times}$ and integral points $K_{2n}$. Let $\iota(g) = \iota(g, 1)$ be the embedding of the first factor of $G_n \times G_n$ into $G_{2n}$. For $s \in \mathbb{C}$ a function $\Phi$ on $G_{2n}$ is a *spherical section* (for the trivial character) if
$$\Phi(p k) = q^{-2 \operatorname{ord}(a(p)) (s + n/2)}$$
for all $p \in P$ and $k \in K_{2n}$.

**Theorem 2.4.1 (Doubling integral at an inert place).** Let $\mu$ be a Haar measure on $G_n$ with $\mu(K_n) = 1$, let $s \in \mathbb{C}$ with $\operatorname{Re} s > n/2$, and let $\Phi$ be a spherical section. Then $g \mapsto \Phi(\iota(g))$ is integrable and
$$\begin{aligned}
&\int_{G_n} \Phi(\iota(g)) \, d\mu(g) \cdot \prod_{i=0}^{n-1} \bigl(1 - (-1)^{n-i-1} q^{-(2s+i+1)}\bigr)^{-1} \\
&\qquad = \prod_{i=0}^{n-1} \bigl(1 - (q^2)^{-(s+n/2-i)}\bigr)^{-1}.
\end{aligned}$$

Lean: `GlobalTheory.ThK.Dbl.Inert.triv`

*Proof.* The constant function $1$ is the zonal spherical function of the trivial representation of $G_n$, and its Satake parameters are $\alpha_i = q^{n-1-2i}$ for $i < n/2$. The [unramified doubling integral](/entry/inert-zeta-top-unram-doubling-inert/) evaluates the integral of $\Phi(\iota(g)) w(g)$ for a zonal $w$ with parameters $\alpha$ in closed form, provided $y = q^{-(2s+1)}$ satisfies $|y| < 1$ and $|y \alpha_i^{\pm 1}| < 1$. With $X = q^{-(2s+n)}$ the closed form is
$$\begin{aligned}
&\prod_{j=0}^{n-1} \bigl(1 - (-q)^j X\bigr) \cdot \prod_{i < n/2} (1 - y \alpha_i)^{-1} (1 - y \alpha_i^{-1})^{-1} \\
&\qquad \cdot (1 - y)^{-\epsilon_n},
\end{aligned}$$
where $\epsilon_n = 1$ if $n$ is odd and $0$ otherwise. For $\alpha_i = q^{n-1-2i}$ the moduli are $q^{-(2 \operatorname{Re} s + 2 + 2i - n)}$ and $q^{-(2 \operatorname{Re} s + n - 2i)}$, which are less than $1$ because $\operatorname{Re} s > n/2$. Put $j = n - 1 - i$: then $(-q)^j X = (-1)^{n-i-1} q^{-(2s+i+1)}$, so the first product cancels the normalizing factor on the left; each of its factors is nonzero. The remaining factors are $(1 - q^{-m})^{-1}$ for $m = 2s + n - 2i$ with $i < n/2$, for $m = 2s + 2 + 2i - n$ with $i < n/2$, and for $m = 2s + 1$ when $n$ is odd. Together these are the $m = 2s + n - 2i$ for $0 \leq i < n$, which is the right side. $\square$

The normalizing product is $\prod_{i=1}^{n} L(2s + i, \eta^{n-i})$ for the unramified quadratic character $\eta$ of $L^{\sigma}$, and the right side is the standard $L$-function of the trivial representation; this is the shape of the unramified doubling computation in S. Gelbart, I. Piatetski-Shapiro and S. Rallis, *Explicit Constructions of Automorphic L-Functions*, Part A.

### The global statements at a finite place

Now let $F$ be a number field, $E/F$ a CM extension with involution $\sigma$, $Y$ a Hermitian space of rank $n$ over $E$, and $\chi$ a Hecke character of $E$ satisfying the restriction condition with exponent $0$. Let $G_2$ be the doubled unitary group with Siegel parabolic, let $e$ be an embedding of $U(Y) \times U(Y)$ into $G_2$, and let $K$ be a stabilizer of the standard kind. For a finite place $v$ of $F$ a function $f$ on $G_2$ is *spherical at $v$ with exponent $z$* if $f(p k) = \chi(\det t) |\det t|_E^{z}$ for $p$ in the Siegel parabolic with Levi part $t$ and $k \in K$, both trivial away from $v$. Put
$$d_v(z) = \prod_{i=0}^{n-1} \bigl(1 - \varepsilon_v^{\,n-i-1} N v^{-(2z+i+1)}\bigr)^{-1},$$
with $\varepsilon_v = 1$ if $v$ splits in $E$ and $-1$ otherwise, and let $L_v(\chi, z)$ be the product of the local factors $(1 - \chi_w(\varpi_w) N w^{-z})^{-1}$ over the places $w$ of $E$ above $v$ at which $\chi$ is unramified.

**Theorem 2.4.2 (Doubling integral at an inert place, global form).** Let $v$ be a finite place of $F$ inert in $E$ with $\chi$ unramified above $v$. Let $\mu$ be a Haar measure on $U(Y)(F_v)$ giving the integral points measure $1$, let $\operatorname{Re} z > n/2$, and let $f$ be spherical at $v$ with exponent $z + n/2$. Then $u \mapsto f(e(u, 1))$ is integrable and
$$\int f(e(u, 1)) \, d\mu(u) \cdot d_v(z) = \prod_{i=0}^{n-1} L_v(\chi, z + n/2 - i).$$

Lean: `GlobalTheory.ThK.Dbl.Inert.main`

*Proof.* At an inert place $E_w / F_v$ is the unramified quadratic extension, and a uniformizer of $F_v$ with the Galois involution gives an unramified involution with $q = N v$. A frame of $Y$ at $v$ identifies $U(Y)(F_v)$ with $G_n$, the doubled group with $G_{2n}$, and $f$ with a spherical section of the trivial character: $\chi_w$ is unramified and trivial on $F_v^{\times}$ by the restriction condition, hence trivial. There is one place $w$ above $v$, with $N w = q^2$, so the right side is the right side of the local theorem, and $d_v(z)$ is its normalizing factor. $\square$

**Lemma 2.4.3 (Zeta integral).** Let $k$ be a nonarchimedean local field with ring of integers $\mathcal{O}_k$, uniformizer $\varpi$ and residue field of order $q$. Let $A$ be an unramified character of $k^{\times}$ with $|A(\varpi)| q^i < 1$ for $i < n$, and let $\kappa$ be a left Haar measure on $GL_n(k)$ with $\kappa(GL_n(\mathcal{O}_k)) = 1$. Then
$$\int_{M_n(\mathcal{O}_k) \cap GL_n(k)} A(\det g) \, d\kappa(g) = \prod_{i=0}^{n-1} \bigl(1 - A(\varpi) q^i\bigr)^{-1}.$$

Lean: `GlobalTheory.ThK.Dbl.Split.zeta`

*Proof.* Decompose the integral over the double cosets $GL_n(\mathcal{O}_k) \operatorname{diag}(\varpi^{m_1}, \dots, \varpi^{m_n}) GL_n(\mathcal{O}_k)$ with $m_i \geq 0$, or equivalently sum over the sublattices of $\mathcal{O}_k^n$, counted by index; this is the zeta function of $M_n$ of Godement and Jacquet for the trivial representation. $\square$

**Lemma 2.4.4 (Doubling for $GL_n$).** In the setting of the lemma, let $A$ and $B$ be unramified characters with $|A(\varpi)| q^i$, $|B(\varpi)| q^i$ and $|(AB)(\varpi)| q^i$ less than $1$ for $i < n$, and let $\varphi(g) = B(\det g)^{-1} (AB)(\det t)$, where $t \mathcal{O}_k^n = \mathcal{O}_k^n \cap g \mathcal{O}_k^n$. Then $\varphi$ is integrable and
$$\int \varphi \, d\kappa \cdot \prod_{i<n} \bigl(1 - (AB)(\varpi) q^i\bigr)^{-1} = \prod_{i<n} \bigl(1 - A(\varpi) q^i\bigr)^{-1} \bigl(1 - B(\varpi) q^i\bigr)^{-1}.$$

Lean: `GlobalTheory.ThK.Dbl.Split.doubling`

*Proof.* A pair of integral matrices $(a, b)$ factors as a common divisor times a coprime pair, and coprime pairs correspond to the matrices $g = a b^{-1}$. Integrating $A(\det a) B(\det b)$ over pairs in these two ways gives the product of two zeta integrals on the right and the zeta integral of $AB$ times $\int \varphi$ on the left. $\square$

**Theorem 2.4.5 (Doubling integral at a split place).** The global form of the theorem holds also for every finite place $v$ of $F$ that splits in $E$ with $\chi$ unramified above $v$.

Lean: `GlobalTheory.ThK.Dbl.locUnrSplit`

*Proof.* At a split place $E \otimes_F F_v = F_v \times F_v$, and a frame identifies $U(Y)(F_v)$ with $GL_n(F_v)$ and the doubled group with $GL_{2n}(F_v)$. Under this identification $u \mapsto f(e(u, 1))$ becomes a function of the form $\varphi$ in the doubling lemma, for unramified characters $A$ and $B$ built from $\chi$ at the two places above $v$ and the exponent $z + n/2$; the bounds of the lemma hold because $\operatorname{Re} z > n/2$. Here $\varepsilon_v = 1$, and $L_v(\chi, \cdot)$ is the product of the two local factors, so the doubling lemma is the claimed identity. $\square$

### Two global facts on theta integrals

The next two results concern a matched configuration of the [theta series chapter](/entry/close-sph/): Hermitian spaces $V$, $V'$ and $W$ over $E$, [[Weil representations|H3Q2703KKV]] $\omega$ of $U(V) \times U(W)$ and $\omega'$ of $U(V') \times U(W)$, and the theta integrals $I(\Phi)$ and $I'(\Phi')$ on $U(W)(\mathbb{A})$ of polynomial test functions, with $\Phi'$ in a fixed subspace $\mathcal{S}'$. The configuration carries two integers $p$ and $q$, which we do not unfold.

**Theorem 2.4.6 (Base constant).** Assume fifteen statements: a standard Siegel-Weil formula, a statement on Siegel [[Eisenstein series|3NZBZXYWAJ]], that Hecke $L$-functions are entire and nonzero at $1$, and statements on nonvanishing, factorization, existence of matched pairs, theta kernels, convergence of Weil representations, decay, continuity, the topology of the adelic groups, characters, Siegel sets, finite volume and unimodularity. Then for every matched configuration with $p = q = 0$ there is $c \neq 0$ such that $I(\Phi)(h) = c \, I'(\Phi')(h)$ for all $h$ and all matched pairs $(\Phi, \Phi')$ with $\Phi' \in \mathcal{S}'$.

Lean: `PositivityTheory.ThKR.polynomial_vanishing_of_compactness`

*Proof.* In the base case the groups are compact modulo their rational points. The Siegel-Weil formula for anisotropic spaces, derived from the standard one, and the continuation of the Eisenstein series give a full Siegel-Weil identity on the box sections. Compactness, the line of Hermitian forms spanned by the theta integrals and the line of their coefficients then show that $I(\Phi)$ and $I'(\Phi')$ lie on one line, and the nonvanishing of the Hecke $L$-value gives that the constant is not zero. $\square$

**Theorem 2.4.7 (Rapid decay of cuspidal differences).** Assume reduction theory for the adelic unitary group by Siegel sets, the basic properties of theta kernels, and the two archimedean statements on the operators and the Lie algebra action of the Weil representation. Let $f = I(\Phi) - I'(\Phi')$ for a matched configuration and polynomial test functions. If $f$ is cuspidal, that is, its integral over $N(F) \backslash N(\mathbb{A})$ vanishes for the unipotent radical $N$ of the stabilizer of every nonzero isotropic subspace of $W$, then $f$ is rapidly decreasing: it is continuous, left invariant under $U(W)(F)$, and for every $N \geq 0$ the function $|f(h)| \operatorname{ht}(h)^N$ is bounded.

Lean: `PositivityTheory.ThKEst.sigRapid`

*Proof.* The theta integrals are of moderate growth on Siegel sets, uniformly in the test functions, by the decay of the theta kernels and the archimedean statements. A cuspidal function of uniform moderate growth whose derivatives under the Lie algebra are again of moderate growth is rapidly decreasing on Siegel sets, by the usual argument with constant terms, and the Siegel sets cover the group. $\square$

**Remark 2.4.8 (Formalization).** The local theorem is at [LocUnrInertN.lean](lean:Development/WeilBound/ThetaLifts/LatticeBasics/LocUnrInertN.lean#L20); it uses `unramDoublingInert`, whose statement is in [GaussianBinomialClosedForm.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/GaussianBinomialClosedForm.lean#L53). The inert global form is at [LocUnrInert.lean](lean:Development/WeilBound/ThetaLifts/LatticeBasics/LocUnrInert.lean#L206), with a second name `locUnrInert` at L244, and the split form at [LocUnrSplit.lean](lean:Development/WeilBound/ThetaLifts/LatticeBasics/LocUnrSplit.lean#L123); the two statements are `LocUnrSplit` and `LocUnrInert` in [LocUnr.lean](lean:Development/WeilBound/ThetaLifts/LatticeBasics/LocUnr.lean#L13), and $d_v$ is `locD` in [HodgeTateFromSandwich.lean](lean:Development/WeilBound/ThetaLifts/LatticeBasics/HodgeTateFromSandwich.lean#L51). The lemmas are in [LocUnrSplitL.lean](lean:Development/WeilBound/ThetaLifts/LatticeBasics/LocUnrSplitL.lean#L21). The local theorem is stated only for the trivial character, which is all the inert case needs. The base constant is at [PolZero.lean](lean:Development/WeilBound/ThetaLifts/Reductions/TopPolarZero/PolZero.lean#L35); its name speaks of polynomial vanishing and compactness, while the statement `PolZero` ([CTSmallCone.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/CTSmallCone.lean#L313)) is the existence of a nonzero constant of proportionality, and all fifteen hypotheses are used. Rapid decay is at [CuspRapid.lean](lean:Development/WeilBound/ThetaLifts/FrameEstimates/CuspRapid.lean#L35), with the statement `SigRapid` in SigThConst.lean; the height $\operatorname{ht}$ is `qht`.
