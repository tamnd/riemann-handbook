---
title: Unramified and level computations
decls:
  - GlobalTheory.T.satakeTransform_eq_at_thetaLift_of_vacuum_eq
  - GlobalTheory.SphTheta.satU_eq_satU_liftPar_of_heckeVec_eq
  - GlobalTheory.InertZeta.unramDoublingInert
  - GlobalTheory.FinZeta.zeta_sum
  - GlobalTheory.T.finiteZetaIntegral_thetaLift_eq_partialLValue
  - GlobalTheory.FinZeta.finiteZetaL
  - GlobalTheory.T.thetaLevelIndex_mul_schwartzNorm_formula
  - GlobalTheory.LevelIndex.levelIndexNormC
  - GlobalTheory.AdIsom.adelicIsometries
  - GlobalTheory.FramesExistLev.selfDual_frames_normal_at_level_places_of_charFrame
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Unramified and level computations

The ascent compares theta lifts by their Hecke eigenvalues at almost all places and by explicit constants at the finitely many level places. This section collects the local and semilocal computations behind these comparisons: the Satake parameters of an unramified theta lift, the unramified doubling integral at an inert place, the finite doubling zeta sum of a level vector, the norm of a level vector, and the existence of self-dual lattices and frames in normal form. All of them feed the step [the nonempty hypotheses](/step/nonempty-hyps/), and the frames feed the [realisation of frames](/entry/frames-ex-of-realisation-alt/).

### The unramified theta correspondence

Let $L$ be a complete discretely valued field with uniformiser $\varpi$ and an involution $\sigma$, and let $q$ be the size of the residue field. For $n \ge 0$ let $U_n$ be the unitary group of the standard split Hermitian form of rank $n$ over $L$, $K_n$ its standard maximal compact subgroup and $\mathcal{H}(U_n, K_n)$ its spherical Hecke algebra. For $h \in \mathcal{H}(U_n, K_n)$ and $\alpha \in (\mathbb{C}^\times)^{\lfloor n/2 \rfloor}$ let $\mathcal{S}h(\alpha)$ be the [Satake transform](/learn/representations/#unramified-representations) of $h$ at $\alpha$.

**Definition 8.4.1 (Lifted Satake parameter).** Let $n \le n'$ and $\alpha \in (\mathbb{C}^\times)^{\lfloor n/2 \rfloor}$. The *lifted parameter* $\alpha' \in (\mathbb{C}^\times)^{\lfloor n'/2 \rfloor}$ has the entries
$$\alpha'_k = (-1)^n\, q^{n' - n - 1 - 2k} \quad \text{for } k < \lfloor n'/2 \rfloor - \lfloor n/2 \rfloor,$$
and $\alpha'_k = (-1)^{n + n'}\, \alpha_{\lfloor n'/2 \rfloor - 1 - k}^{-1}$ for the other $k$.

These are the Satake parameters of the unramified [local theta correspondence](/learn/theta/#the-local-theta-correspondence) from $U_n$ to $U_{n'}$: the parameter of the small group together with a string of powers of $q$.

**Theorem 8.4.2 (Satake transforms of an unramified theta lift).** Let $\omega$ be a representation of $U_n \times U_{n'}$ on a space $M$ with a vacuum vector $s$, given with a Schrödinger model $\rho$ on $M_{n' \times n}(L)$, and assume that these data are standard unramified and satisfy the Cayley rule for both groups. Let $n \le n'$, $h \in \mathcal{H}(U_n, K_n)$ and $h' \in \mathcal{H}(U_{n'}, K_{n'})$ with $\omega(h) s = \omega(h') s$. Then $\mathcal{S}h(\alpha) = \mathcal{S}h'(\alpha')$ for every $\alpha \in (\mathbb{C}^\times)^{\lfloor n/2 \rfloor}$.

Lean: `GlobalTheory.T.satakeTransform_eq_at_thetaLift_of_vacuum_eq` (also `GlobalTheory.SphTheta.satU_eq_satU_liftPar_of_heckeVec_eq`, the proof).

*Proof.* There is a linear form $\ell$ on $M$ with $\ell(s) = 1$, invariant under the lattice that is self-dual in the mixed model and fixed by $K_n \times K_{n'}$. For an upper triangular $b \in U_n$ the value $\ell(\omega(b, 1) s)$ is multiplicative in $b$ and is fixed by the torus generators:
$$\ell(\omega(b, 1) s) = \prod_k \bigl((-1)^{n'} q^{2\lfloor n'/2 \rfloor - n'}\bigr)^{\operatorname{ord} b_{kk}}.$$
In the same way $\ell(\omega(1, b) s) = \prod_k ((-1)^n q^{-n})^{\operatorname{ord} b_{kk}}$ for upper triangular $b \in U_{n'}$. Both Hecke vectors are sums of translates of $s$ over upper triangular representatives, and their Satake transforms are the same sums with these characters replaced by $\alpha$. An upper triangular element of $U_{n'}$ is lower block triangular in the half blocks, which lets one pair the representatives of the two sums. Apply $\ell$ to $\omega(h) s = \omega(h') s$ and compare the two sums term by term. Two product identities in $q$ and $\alpha$ turn the resulting equality into $\mathcal{S}h(\alpha) = \mathcal{S}h'(\alpha')$. $\square$

### The doubling integral at an inert place

**Theorem 8.4.3 (Unramified doubling integral at an inert place).** Let $L$ be an unramified quadratic extension with involution $\sigma$, $\varpi$ a uniformiser fixed by $\sigma$, and $\mu$ the Haar measure on $U_n$ with $\mu(K_n) = 1$. Let $\chi$ be an unramified character of $L^\times$, $s \in \mathbb{C}$, $\Phi$ the spherical section of the degenerate principal series of the doubled group $U_{2n}$ attached to $\chi$ and $s$, and $w$ the zonal spherical function on $U_n$ with Satake parameter $\alpha$. Let $\iota : U_n \to U_{2n}$ be the doubling embedding of the first factor. Then:

1. if $s$ is in the domain of convergence for $\alpha$, the doubling integral $Z = \int_{U_n} \Phi(\iota(g))\, w(g)\, d\mu(g)$ converges absolutely and equals an explicit Gaussian binomial expression in $\alpha$ and in two variables $X$, $Y$ determined by $q$, $\chi(\varpi)$ and $s$; when $\chi(\varpi) = (-1)^m$, $Z = L(s + \frac12, \alpha, \chi) / d_m(s)$, with the standard $L$-factor and an explicit normalising factor $d_m(s)$;
2. if $n \le 1$, the integral converges and equals $1$.

Lean: `GlobalTheory.InertZeta.unramDoublingInert`.

*Proof.* The doubled lattice has a primitive isotropic frame over the completion. By the elementary divisor theorem every $g$ has a matrix length, and the section is $\Phi(\iota(g)) = X^{\operatorname{len}(g)}$. So $Z$ is the sum of $X^{\operatorname{len}(g)} w(g)$ over $U_n / K_n$. The number of cosets of each length and the values of $w$ on them give a generating function in $X$ and $Y$, which sums to the closed form by the Gaussian binomial theorem. When $\chi(\varpi) = (-1)^m$ the closed form factors as the standard $L$-factor over $d_m(s)$. For $n \le 1$ the group $U_n$ equals $K_n$, so $Z = \Phi(1) w(1) = 1$. $\square$

This is the local unramified computation of the [doubling method](/learn/theta/#the-doubling-method) at an inert place.

### The finite zeta sum and the level norm

The global datum of the proof fixes for each index $i$ a pair of Hermitian spaces $(V_i, W_i)$, a finite set $S$ of level places, a level subgroup of $G_{W_i}$ and a theta vector $f$ whose components outside $S$ are vacua. We call such a choice, together with a Weil datum and a lowest $K$-type model, *lift data at a face*. For a fundamental domain $\mathcal{X}$ of covolume $1$ put $\langle u, u' \rangle_{\mathcal{X}} = \int_{\mathcal{X}} u\, \overline{u'}$ and $\|u\|^2 = \langle u, u \rangle_{\mathcal{X}}$.

**Lemma 8.4.4 (Unramified doubling sum).** Assume the unramified doubling identity for $GL$. Let $(\psi, \chi_V, \chi_W, \omega)$ be a Weil datum for $(V, W)$ with $n_V$ and $n_W = r$ the ranks of the global datum, with $\chi_V, \chi_W$ unramified outside a finite set $S$. Let $K \le J$ be open subgroups of the finite adelic points of $G_W$ with finite index, where $J$ is the product of its components on $S$ with the maximal compacts outside $S$. Let $f$ be a theta function that is a vacuum outside $S$ and satisfies $\omega(1, k) f = \chi(k) f$ for $k \in J$, with $|\chi| = 1$. Then the sum over $G_W / J$ of $\langle \omega(1, y) f, f \rangle_{\mathcal{X}}$ against the Hecke eigenvalues of a spherical vector converges to $\|f\|^2$ times a partial standard $L$-value.

Lean: `GlobalTheory.FinZeta.zeta_sum`.

*Proof.* Outside $S$ the function $y \mapsto \langle \omega(1, y) f, f \rangle_{\mathcal{X}}$ factors as a product of local doubling sections, by the vacuum property and the transformation law under $J$. The sum over $G_W / J$ is then a product over places of local unramified doubling sums, which the unramified identity evaluates as local $L$-factors. $\square$

**Theorem 8.4.5 (Finite zeta integral of a theta lift).** Assume that cusp forms decrease rapidly, the Bernstein-Zelevinsky finiteness theorem, and the unramified doubling identity for $GL$. Let lift data at a face be given, with a theta vector $f$, and let a family of Hecke eigenvalues have a nonzero part of the given type. Then there is a family $B$ of Satake parameters for these eigenvalues outside $S$ such that:

1. $|\beta| \le N(w)^{(r - 1)/2}$ for each $\beta \in B_w$ and each place $w$ outside $S$;
2. the partial $L$-function of $B$ twisted by the inverse of the central character converges at $\frac{1 + t}{2}$;
3. for all vectors $U_1 v_1$ in the full part of the given type and $U_2 v_2$ in the target, the sum over the level cosets $y$ of $\langle \omega(1, y) f, f \rangle_{\mathcal{X}}\, \overline{\langle r(y) U_1 v_1, U_2 v_2 \rangle}$ equals
$$\frac{|H_P|\, \|f\|^2\, L^S\bigl(\tfrac{1+t}{2}, B\bigr)}{d_S}\, \overline{\langle U_1 v_1, U_2 v_2 \rangle},$$
where $H_P$ is the finite group of the face and $d_S$ is a product of local factors over $S$.

Lean: `GlobalTheory.T.finiteZetaIntegral_thetaLift_eq_partialLValue` (also `GlobalTheory.FinZeta.finiteZetaL`, the proof).

*Proof.* The level vector is a vacuum outside $S$ and transforms by the level character. The self-dual frames of the datum give self-dual lattices for $V_i$ and $W_i$, and the level is hyperspecial off $S$ with the right index in the lift level. A translate $\omega(1, g) f$ with $g$ outside the saturation of the level is orthogonal to $f$, since its support is moved off the support of $f$. So only the level cosets contribute. Rapid decay of cusp forms gives the Satake parameters with the bound in part 1 and the convergence in part 2, and the [Lemma 8.4.4](/entry/zeta-sum/) evaluates the sum. $\square$

**Theorem 8.4.6 (Level index times the norm of a level vector).** Assume the local integral identity for a single block of $GL$, and assume local models at all places. For lift data at a face with ranks $n_V = r + t$, the level $\Gamma$ of $V_i$ lies in the stabiliser $\Gamma_0$ of the self-dual lattice, and
$$[\Gamma_0 : \Gamma] \cdot \|f\|^2 = \prod_{v \in S} d_v^{-1},$$
where, with $k_v$ the residue field at the place above $v$,
$$d_v^{-1} = \frac{|GL_{r+t}(k_v)|}{|GL_t(k_v)|\, |k_v|^{rt}\, |k_v|^{r^2 + rt}}.$$

Lean: `GlobalTheory.T.thetaLevelIndex_mul_schwartzNorm_formula` (also `GlobalTheory.LevelIndex.levelIndexNormC`, the proof).

*Proof.* The level lies in the stabiliser of the self-dual lattice of the frame. The relative index is a product of local indices over $S$, and the square norm of the level vector is a product of local volumes, by the local integral identity. At each place of $S$ the level and twist places are split and distinct, and the local index times the local volume is the ratio of orders of finite general linear groups in the display, by the order of the parabolic quotient of $GL_{r+t}(k_v)$. $\square$

### Lattices and frames

**Theorem 8.4.7 (Adelic isometries and self-dual frames).** For every global datum the following facts on adelic Hermitian lattices hold: lattices decompose along the idempotents of the places; isometries transport lattices, with a correction unique modulo the stabiliser; local lattices glue and unglue along idempotent components; adelic unitary elements send self-dual lattices to self-dual lattices; Hermitian spaces of the same rank and signature are isometric, with a standard isometry; norm lines decompose; hyperbolic extension lattices are self-dual and stable under conjugation; and every Hermitian space $V$ has a self-dual frame of level $N^c$ for every $N$.

Lean: `GlobalTheory.AdIsom.adelicIsometries`.

*Proof.* Each clause is proved separately. The Hasse principle for Hermitian forms gives the isometry from rank and signature, and the existence of a self-dual frame follows from a self-dual coordinate lattice for a frame of each space. $\square$

**Theorem 8.4.8 (Self-dual frames in normal form at level places).** Let a character frame of the global datum be given and let $P_g$ be the set of places that divide its level. Then there are self-dual lattices and frames for all spaces of the chain and the pair, and at the places of $P_g$ the frames of the chain spaces are diagonal in normal form.

Lean: `GlobalTheory.FramesExistLev.selfDual_frames_normal_at_level_places_of_charFrame`.

*Proof.* Build a level datum with trivial characters and no twist places from the character frame. Take a standard base frame for each space, and auxiliary hyperbolic vectors for the chain spaces, with the given hyperbolic vectors for the first one. The standard frames then exist with the standard shape, the normal form at the places of $P_g$ follows from the shape, and the vertex conditions follow from transport along the level. $\square$

**Remark 8.4.9 (Formalization).** The finite zeta theorem takes the Bernstein-Zelevinsky finiteness hypothesis but does not use it ([FiniteZetaIntegralThetaLiftEqPartialLValue.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/FiniteZetaIntegralThetaLiftEqPartialLValue.lean#L181)). We have not unfolded the standard unramified conditions, the Cayley rule, the domain of convergence and the Gaussian binomial closed form of the inert integral, the structure of lift data at a face, or the twelve clauses of the lattice statement, which is a conjunction of twelve Prop-valued definitions. The lemma on the doubling sum is stated in a summary form; its Lean statement lists the hypotheses on $K$, $J$ and $\chi$ in full.
