---
title: The flat degree at CM points
decls:
  - GlobalTheory.T.FlatDegree_holds
  - GlobalTheory.CompanionTheory.Ar.Fl.flatDegree
  - GlobalTheory.T.exists_cm_period_embedding
  - GlobalTheory.CompanionTheory.Ar.Fl.exists_cmPoint_locBasis_frames
  - GlobalTheory.T.frame_function_cm_height
  - GlobalTheory.CompanionTheory.Ar.Fl.flatGen_finNorm
  - GlobalTheory.T.cm_pack_pure_norm
  - GlobalTheory.CompanionTheory.Ar.Fl.GFin.intFrames_fin
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The flat degree at CM points

The flat degree $\deg_{\mathrm{fl}}(u)$ of the earlier sections is the degree of a line bundle that is flat: its generator is a frame function, and its norms are constant on each component, at each place. This section computes this degree at a CM point. It is a sum of a Chowla-Selberg period term and a term in the discriminants. The proof reads the norms of the frame function at a point whose abelian part is a product of CM elliptic curves, where both the archimedean and the finite norms can be computed. The result is used in the [covolume statement](/entry/top-covol-slim2-use-alt-alt/), where the flat degree is the constant part of the slope.

Let $E$ be a CM field, with host $H$, a datum $D$ with $N = p + q$, a level, a moduli space $X_o$ and a coefficient datum with number field $F$. Let $-d$ be the discriminant of the imaginary quadratic field that the host fixes, with a square root $r_0$ of $-d$ in $\mathbb{C}$. Let a family uniformization of type $\mathrm{ty}$ be given, with an index $i$ and an unfolding $U$. Let $\tau$ be an embedding of $F$ with $\tau(\sqrt{-d}) = r_0$.

### Frame functions and their norms

A frame function $\varphi$ attaches a number $\varphi(y, v, w)$ to a point $y$ of the family and to frames $v$ and $w$ of the $\tau$ and $\bar\tau$ eigenspaces of the Lie algebra.

**Definition 8.20.1 (Flat generator).** $\varphi$ is a flat generator for $U$ and $\tau$ if it is a line function, that is, a generator of the line bundle of top wedges of the two eigenspaces, and if it is flat: for some linearly independent periods $e$ there is a constant $\rho$ with
$$
\varphi(y, v, w) \cdot \det \begin{pmatrix} C \\ F_m \end{pmatrix} = \rho
$$
for all period data, where $C$ and $F_m$ are the period rows of the frames.

**Definition 8.20.2 (Log norms).** A family of log norms $N$ on $F$ is a number $N_{\infty}(s)$ for each archimedean place $s$ and a number $N_{\mathrm{fin}}(p)$ for each prime $p$, the sum over the places above $p$. It is adelic if $N_{\mathrm{fin}}(p) \ne 0$ for only finitely many $p$. Its degree is
$$
\deg N = - \frac{1}{[F:\mathbb{Q}]} \Bigl( \sum_s N_\infty(s) + \sum_p N_{\mathrm{fin}}(p) \Bigr) .
$$

**Definition 8.20.3 (Norms of a frame function).** $\varphi$ has the norms $N$ if:

1. At each archimedean place, for Hodge frames with Gram matrices $\Gamma$ and $\Delta$,
$$
\log |\varphi| + \frac{1}{2} \bigl( \log |\det \Gamma| - \log |\det \Delta| \bigr) = N_\infty(s) .
$$
2. At each prime $p$ and each embedding $j$ into $\mathbb{C}_p$, at integral frames over discrete valuation rings,
$$
\log |j \varphi(K, y, v, w)| = t_j ,
$$
and the sum of the $t_j$ over the places above $p$ is $N_{\mathrm{fin}}(p)$ minus the shift $q \bigl( \log \mathfrak{d}_E - \log |d|_p \bigr)$, where $\log \mathfrak{d}_E$ is the log norm of the different.

For a Kronecker character $\chi$ of conductor $d$ put
$$
\log \Omega_E(\chi) = \gamma + \log \frac{2\pi}{\mathrm{rd}_E} - \frac{L'(1, \chi)}{L(1, \chi)} ,
$$
with Euler's constant $\gamma$ and the root discriminant $\mathrm{rd}_E$ of $E$. This is the Chowla-Selberg period of the [learning page](/learn/elliptic-curves/#the-chowla-selberg-formula), normalized by $E$.

**Theorem 8.20.4 (Flat degree).** Let $\chi$ be a Kronecker character modulo $d$, and let $\varphi$ be a flat generator for $U$ and $\tau$ with norms $N$, where the family has the CM type function. Then $N$ is adelic, and
$$
\deg N = \frac{p - q}{2} \, \mathrm{Re} \log \Omega_E(\chi) + q \bigl( 2 \log \sqrt{d} - \log \mathrm{rd}_E \bigr) .
$$

Lean: `GlobalTheory.T.FlatDegree_holds` (also `GlobalTheory.CompanionTheory.Ar.Fl.flatDegree`, a second name).

The proof is at the end of the section. It needs three lemmas: a CM point with local bases, the finite norm at it, and integral frames at it.

### A CM point

A pure family of the period lattice is a basis whose first $p$ vectors lie in the part of sign $+$ and whose last $q$ vectors lie in the part of sign $-$. A family $x$ is a local basis at $\ell$ for $\mathcal{O}_E$ if it is linearly independent and for every $y$ there is $n$ prime to $\ell$ with $n y$ in the span of $x$.

A CM pack is a number field $K \supseteq F$ with CM elliptic curves $C_b$ over number fields $M_b$, one for each sign $b$, a polarized abelian scheme $B$ over $\mathcal{O}_K$ of dimension $g$, a $K$ point $y$ that is the value of the family uniformization at a period, and maps from the pure lattices to the lattices of the $C_b$. A CM frame at the pack is a frame whose vectors are the images of the vectors of the $C_b$, combined with the dual basis.

**Lemma 8.20.5 (A CM point with local bases).** For each prime $\ell$ and each finite dimensional subfield $k \subseteq \mathbb{C}$ there are a period $P$, a pure family $x$, a CM pack $X$ with $k \le X.K$, such that $x$ is a local basis at $\ell$, and CM frames $v$ and $w$ at $X$.

Lean: `GlobalTheory.T.exists_cm_period_embedding` (also `GlobalTheory.CompanionTheory.Ar.Fl.exists_cmPoint_locBasis_frames`, a second name).

*Proof.* The set of periods is not empty. A pure period has a local basis at $\ell$, and it decomposes as a pure family. A period gives a CM pack with a field as large as we want, so we can take $k \le X.K$. The pure frame result at the pack gives $v$ and $w$. $\square$

### The finite norm

Let $\mathrm{Gram}_E(e)$ be the matrix of the hermitian form on a family $e$.

**Lemma 8.20.6 (Finite norm of a flat generator).** Let $\varphi$ be a flat generator with periods $e$. There is $t \in E$ with:

1. for all $j: E \to \mathbb{C}_\ell$,
$$
\log |j t| + \log |j \bar t| + \log |j \det \mathrm{Gram}_E(e)| = -(p + q) \log \mathfrak{d}_E ;
$$
2. if $e$ is a local basis at $\ell$, then $\log |j t| = 0$;
3. for every $j: k \to \mathbb{C}_\ell$ and every $t_0$ with the finite norm property at $j$,
$$
t_0 = \log |j \rho| - \log |j \tau(t)| - q \log \mathfrak{d}_E - \log |j \tau(\sqrt{-d})| .
$$

Lean: `GlobalTheory.T.frame_function_cm_height` (also `GlobalTheory.CompanionTheory.Ar.Fl.flatGen_finNorm`, a second name).

*Proof.* Take the CM point of the last lemma, with a pure local basis $x$ at $\ell$. There is a transition matrix from $e$ to $x$, with determinant $t$. The Gram determinant of a pure family is the different up to a unit, which gives part 1. If $e$ is itself a local basis at $\ell$, the transition matrix is invertible over the localization, and its determinant has $\ell$-adic norm $1$; this is part 2. For part 3 we extend $j$ to an algebraically closed field. At the CM pack the pure norm result says that the frame function at integral CM frames is $\rho$ divided by the transition determinant and by the generator of the different and $\tau(\sqrt{-d})$. The pure lattices of the two signs are orthogonal, and the local basis has a Gram determinant whose log norm is the different. Since $z \ne 0$ for the CM curves, all terms are finite, and part 3 follows. $\square$

### Integral frames

**Lemma 8.20.7 (Integral frames at a CM pack).** Let $X$ be a CM pack and $j$ an embedding of $X.K$ into $\mathbb{C}_\ell$. There are a discrete valuation ring $V \subseteq X.K$ that is the unit ball of $j$, a semi-abelian scheme over $V$, and $\delta, \delta' \ne 0$ with
$$
\begin{aligned}
\log |j \delta| &= \log \mathfrak{d}_E - \log |j \beta \tau(\sqrt{-d})| , \\
\log |j \delta'| &= \log |j \delta| ,
\end{aligned}
$$
such that the frames $\delta v$ and $\delta' w$ are framed and are integral frames over $V$.

Lean: `GlobalTheory.T.cm_pack_pure_norm` (also `GlobalTheory.CompanionTheory.Ar.Fl.GFin.intFrames_fin`, a second name).

*Proof.* The $\ell$-adic embedding gives a discrete valuation ring. The CM order has a local basis, and its Lie model has an action of $\mathcal{O}_E$. A twisted generator of the different exists, and we take $\delta$ and $\delta'$ from it. The product frame of the pack extends over the valuation ring, since the Lie model extends. The scaled frames span the Lie lattice in each eigen part, so they are integral frames. $\square$

### Proof of the flat degree theorem

Let $\varphi$ be a flat generator with norms $N$ and periods $e$.

At the archimedean places we use the Chowla-Selberg formula for both signs $b$, with the square root $\pm r_0$ of $-d$. At the CM point the frame function has the value $\rho$ divided by the periods of the CM curves, and the Hodge Gram matrices are the Gram matrices of the periods. So $N_\infty(s)$ is the log norm of $\rho$ plus $\frac{p - q}{2}$ times the log of the Chowla-Selberg period at the place, by the formula for the log norm of a hermitian metric.

At a prime $\ell$, the finite norm lemma, with the integral frames of the last lemma, gives $t_j$. If the periods $e$ are a local basis at $\ell$, then $\log |j t| = 0$; this holds for all but finitely many $\ell$, since the Gram determinant of $e$ is nonzero. Outside the primes that divide the different, $d$ and $\rho$, the shifted sum is then $0$. So $N$ is adelic.

For the degree, the terms in $\rho$ and in $t$ cancel by the product formula in the number field $F$, and the mean over the extensions does not change the degree. The sum over the two conjugate embeddings of $E$ is real, and we get the real part. Let
$$
x = \gamma + \log \frac{2\pi}{\sqrt{d}} - \frac{L'(1,\chi)}{L(1,\chi)} ;
$$
the Chowla-Selberg formula gives the archimedean sum in terms of $x$, and
$$
\mathrm{Re} \log \Omega_E(\chi) = x - \log \mathrm{rd}_E + \log \sqrt{d} .
$$
The finite shifts give $q$ times the log norm of the different minus $q \log d$, and the different of $E$ has normalized log norm $\log \mathrm{rd}_E$. Collecting the terms gives
$$
\deg N = \frac{p - q}{2} \, \mathrm{Re} \log \Omega_E(\chi) + q \bigl( 2 \log \sqrt{d} - \log \mathrm{rd}_E \bigr) .
$$
$\square$

So the flat degree is a sum of a period term with the factor $\frac{p - q}{2}$ and a term in the discriminants with the factor $q$.

**Remark 8.20.8 (Formalization).** The degree of log norms uses `finsum` over the primes (FactPrimes.lean:14), which is $0$ when the support is infinite; this is why the theorem proves that the norms are adelic. The statement writes $2 \log \sqrt{d}$ for $\log d$, and it takes `Re` of the complex number `logOm` (ExistsIsThetaDegOfIsLocalModel.lean:23); a Kronecker character is real, so $L'(1,\chi)/L(1,\chi)$ is real and the real part changes nothing. The hypothesis `IsKroneckerChar` is used only to call `chowla_selberg_period`, which has no entry in the outline. The four `T.*` names are renamings proved by `first | exact @...`, under `maxHeartbeats 1000000` (FlatDegreeHoldsStatement.lean:4). The integral frames lemma `intFrames_fin` is at CmPackPureNorm.lean:160 with helpers `exists_frame` (line 40), `span_fam` (68), `scaled` (104) and `half` (129). We do not unfold the family uniformization, the CM pack or the Chowla-Selberg formula.
