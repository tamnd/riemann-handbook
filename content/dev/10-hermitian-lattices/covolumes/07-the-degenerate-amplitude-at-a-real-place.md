---
title: The degenerate amplitude at a real place
decls:
  - GlobalTheory.Amp.DegSide.side_bound
  - GlobalTheory.T.amplification_degenerate_side_piece_bound
  - GlobalTheory.Amp.DegConv.deg_core
  - GlobalTheory.T.amplitude_degenerate_operatorNorm_le_realPlace
  - GlobalTheory.Amp.sqrt_hsNormSq_amplitude_le_degBd
  - GlobalTheory.T.amplitude_hsNorm_le_degreeBound_realPlace
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The degenerate amplitude at a real place

We keep the setting of the [previous section](/entry/fibre-normal-fibre-volume/): $G = U(H)$ at a real place, the flag unipotent group $N$ with Haar measure $dn$, two negative vectors $z, z' \in W_b$, an element $\gamma \in G$ with a normal-form stabilizer measure $\mu_R$ of scale $s$, and an index $j$ with $1 \le j$, $j + 2 \le k$ and $j \le r$. The amplitude of $\gamma$ is an operator between two spaces of Bessel vectors, given by an integral over $R \backslash G$. This section bounds its operator norm and its Hilbert-Schmidt norm by an explicit degree bound. The bound decays in the size of the leading minors of $\gamma$, and it is the archimedean input of the [amplitude bound at terms](/entry/amplitude-bound-of-local-data-of-tail-bound/).

**Definition 2.7.1 (Bessel data on one side).** Let $W_p$ be a nonzero finite-dimensional complex inner product space. Let $U_z \subseteq G$ be the subgroup that fixes $e_a$ and $e_a^*$ for all $a < r$ and fixes $z$. Let $\mu_G$ be a Haar measure on $G$, $\mu_W$ a Haar measure on $U_z$ with total mass $1$, and $\kappa\, dn$ a Haar measure on $N$ with $\kappa > 0$. Let $\nu_S$ be the quotient measure of $\mu_G$ by the product measure on $U_z N$, so that $\int f\, d\mu_G = \int \int f(u x)\, d(\mu_W \times \kappa\, dn)(u)\, d\nu_S(x)$ for measurable $f \ge 0$. Let $\psi$ be a function on $N$ with $|\psi(n)| = 1$, let $\pi$ be an irreducible unitary representation of $U_z$ on $W_p$, and let $c > 0$. A Bessel function for these data is a function $\Phi : G \to W_p$, continuous on $G$, with
$$\Phi(u n g) = \psi(n)\, \pi(u)\, \Phi(g) \qquad (u \in U_z,\ n \in N,\ g \in G),$$
and with
$$\int \|\Phi\|^2\, d\nu_S = c \dim W_p.$$

These are the matrix coefficients of a Bessel model in the sense of the [Gan-Gross-Prasad](/learn/groups/#unitary-groups) setting: $\Phi$ transforms on the left by a character of $N$ and a representation of the stabilizer of $z$.

**Definition 2.7.2 (Tail bound).** Let $q \in \mathbb{N}$ and $H_1 > 0$. A function $\Phi$ has a tail bound of order $q$ with scale $H_1$ for $(z, \nu_S)$ if for every $\lambda > 0$
$$\int_{T_\lambda} \|\Phi\|^2\, d\nu_S \le 2(2r+2)\, \lambda^{-2q} \int \|\Phi\|^2\, d\nu_S,$$
where $T_\lambda$ is the set of $x$ with $\lambda H_1 \le \max(\lambda_a(z,x), \lambda_a(z,x)^{-1})$ for some $a \le r$.

The tail bound says that $\Phi$ decays like $S_z(x)^{-q}$ in mean square: most of its mass sits where the size of $x$ is at most a constant times $H_1$.

**Definition 2.7.3 (Amplitude operator).** Let $\Phi : G \to W_p$ and $\Phi' : G \to W_q$ be Bessel functions for $z$ and for $z'$, and let $\nu_R$ be a measure. The amplitude of $\gamma$ is the operator $J : W_q \to W_p$,
$$J(w) = c^{-1} \int \langle \Phi'(x), w \rangle\, \Phi(\gamma x)\, d\nu_R(x).$$

In the application, $\nu_R$ is the quotient measure of $\mu_G$ by $\mu_R$: $\int f\, d\mu_G = \int \int f(\rho x)\, d\mu_R(\rho)\, d\nu_R(x)$. So $J$ is an orbital integral of the pair $(\Phi, \Phi')$ over the stabilizer of $\gamma$.

**Definition 2.7.4 (Degree bound).** For $\gamma \in G$ and $H_1 \ge 1$ put
$$\sigma(\gamma, H_1) = \max\Bigl(1, \max_{0 \le l \le r} \frac{|D_l(\gamma)|}{(2H_1)^{2r}}\Bigr).$$
For $D > 0$ and $\sigma \ge 1$ the degree bound is
$$\begin{aligned} \mathrm{Deg}(H_1, D_e, D, \sigma) = {} & 16(4r+4)(4r)^{4r^2} (2H_1)^{16r^3+4r} D_e^{8r^2+2} \\ & \cdot \Bigl(\frac{8\pi e}{k-1-j}\Bigr)^{j(k-1-j)} D^{-(k-1-j)} \\ & \cdot \sigma^{-(q - 16r^3 - 4r - 1)/r}. \end{aligned}$$

We use it with $D = |D_j(\gamma)|$ and $\sigma = \sigma(\gamma, H_1)$. The last factor gives the decay in the minors of $\gamma$. It is a decay only when $q > 16r^3 + 4r + 1$.

**Theorem 2.7.5 (Side pieces of the degenerate amplitude).** Let $1 \le j$, $j + 2 \le k$, $j \le r$, $\kappa > 0$, $s > 0$, $H_1 \ge 1$ and $c > 0$. Let $\Phi'$ be a Bessel function for $z'$ with Haar measure $\kappa\, dn$ on $N$ and constant $c$, with quotient measure $\nu_S'$, and with a tail bound of order $q$ and scale $H_1$. Let $D_e$ be a minor bound for $\gamma$, let $\mu_R$ be a normal-form stabilizer measure for $\gamma$ with scale $s$, and let $\nu_R$ be the quotient measure of $\mu_G$ by $\mu_R$. Then:

1. the set of $x$ that are not in $G$ or have $Y_j(\gamma, x) = 0$ is $\nu_R$-null;
2. for every unit vector $w \in W_q$, every $i \in \mathbb{N}$, and all $R_0 \ge 1$, $y > 0$,
$$\int_{Q_i} |\langle w, \Phi'(x) \rangle|^2\, d\nu_R(x) \le \frac{\kappa}{s}\, V(R_0, D_e, y)\, \frac{4r+4}{2^{2iq}}\, c,$$
where $Q_i$ is the set of $x \in E(\gamma; R_0, y)$ such that $i = 0$ or $2^i H_1 < S_{z'}(x)$.

Lean: `GlobalTheory.Amp.DegSide.side_bound` (also `GlobalTheory.T.amplification_degenerate_side_piece_bound`, a second name).

*Proof.* The stabilizer $R$ of $\gamma$ is closed, and the measure $\mu_R$ is a left and right Haar measure on it. There is a cutoff $\varphi$ for $(G, \mu_R)$ that computes $\nu_R$-integrals: for $f \ge 0$ that are left $R$-invariant, $\int f\, d\nu_R = \int \varphi f\, d\mu_G$. We apply this to $f(x) = |\langle w, \Phi'(x)\rangle|^2 \mathbf{1}_{Q_i}(x)$. This $f$ is left $R$-invariant: $Y_j(\gamma, \rho x) = Y_j(\gamma, x)$ for $\rho \in R$, and the sizes are invariant as well.

Next we unfold over $U_{z'} N$. Let $Q$ be a measurable set that is invariant under left multiplication by $U_{z'} N$, let $f \ge 0$ be measurable, and assume $\int_N f(n g)\, \kappa\, dn \le \mathrm{Vol}$ for every $g \in G$. Then for every unit vector $w$
$$\int_Q f\, |\langle w, \Phi' \rangle|^2\, d\mu_G \le \frac{\mathrm{Vol}}{\dim W_q} \int_Q \|\Phi'\|^2\, d\nu_S'.$$
Here the factor $1/\dim W_q$ comes from the average of $|\langle w, \pi'(u) v\rangle|^2$ over $u \in U_{z'}$ for the irreducible representation $\pi'$, and $|\psi'| = 1$. We use $f = \varphi \mathbf{1}_{E(\gamma)}$ and $Q$ the set where $i = 0$ or $2^i H_1 < S_{z'}$; the set $Q$ has the needed invariance because $S_{z'}$ does. The [fibre volume theorem](/entry/fibre-volume-fibre-volume/) gives $\mathrm{Vol} = \kappa V(R_0, D_e, y) / s$, and gives part 1 by the same splitting. It remains to bound $\int \|\Phi'\|^2$ over the set where $i = 0$ or $2^i H_1 < S_{z'}(g)$. For $i = 0$ this is at most $c \dim W_q \le (4r+4) c \dim W_q$. For $i \ge 1$, the condition $2^i H_1 < S_{z'}(g)$ forces $2^i H_1 \le \max(\lambda_a, \lambda_a^{-1})$ for some $a$, since $S_{z'} = 1$ is excluded by $2^i H_1 > 1$. The tail bound with $\lambda = 2^i$ gives at most $(4r+4)\, 2^{-2iq} c \dim W_q$. The factor $\dim W_q$ cancels. $\square$

**Theorem 2.7.6 (Operator norm of the degenerate amplitude).** Let $1 \le j$, $j + 2 \le k$, $j \le r$, $16 r^3 + 4r + 2 \le q$, $\kappa > 0$, $s > 0$, $H_1 \ge 1$ and $c > 0$. Let $\Phi$ and $\Phi'$ be Bessel functions for $z$ and for $z'$, both with Haar measure $\kappa\, dn$ on $N$ and constant $c$, with quotient measures $\nu_S$ and $\nu_S'$, and both with a tail bound of order $q$ and scale $H_1$. Let $D_e$ be a minor bound for $\gamma$, let $\mu_R$ be a normal-form stabilizer measure for $\gamma$ with scale $s$, and let $\nu_R$ be the quotient measure of $\mu_G$ by $\mu_R$. Then the integrand of $J$ is $\nu_R$-integrable, and
$$\|J\| \le \frac{\kappa}{s}\, \mathrm{Deg}\bigl(H_1, D_e, |D_j(\gamma)|, \sigma(\gamma, H_1)\bigr).$$

Lean: `GlobalTheory.Amp.DegConv.deg_core` (also `GlobalTheory.T.amplitude_degenerate_operatorNorm_le_realPlace`, a second name).

*Proof.* The element $\gamma^{-1}$, with the roles of $z$ and $z'$ exchanged, also has a normal-form stabilizer measure of scale $s$, and $D_e$ is a minor bound for it. Its quotient measure is the image of $\nu_R$ under $x \mapsto \gamma x$. So the [side bound](/entry/side-bound/) applies on both sides: to $(\gamma, \Phi')$ in the variable $x$, and to $(\gamma^{-1}, \Phi)$ in the variable $\gamma x$. By part 1 on both sides, almost every $x$ lies in $G$ and has $Y_j(\gamma, x) \ne 0$ and $Y_j(\gamma^{-1}, \gamma x) \ne 0$.

A norm bound for $J$ follows from a bound for its matrix coefficients: if $\int |\langle v, \Phi(\gamma x)\rangle|\, |\langle w, \Phi'(x)\rangle|\, d\nu_R \le K$ for all unit vectors $v, w$, then the integrand of $J$ is integrable and $\|J\| \le K / c$. We bound this integral by a dyadic decomposition. Cut the domain by the sizes $S_z(\gamma x) \in (2^i H_1, 2^{i+1} H_1]$ and $S_{z'}(x) \in (2^{i'} H_1, 2^{i'+1} H_1]$ and by the dyadic ranges of $Y_j(\gamma, x)$ and $Y_j(\gamma^{-1}, \gamma x)$. On each piece, apply Cauchy-Schwarz and the side bound with $R_0 = 2^{i+i'+1} H_1$ on both sides.

Three pointwise facts control the pieces. First, $Y_j(\gamma, x) \cdot Y_j(\gamma^{-1}, \gamma x) \cdot |D_j(\gamma)| \le 2^j$, so the two Gram volumes cannot both be large. Second, each leading minor $|D_l(\gamma)|$ is at most a power of $S_z(\gamma x) S_{z'}(x)$, so on the pieces with small sizes the minors force $\sigma(\gamma, H_1)$ to be small. Third, each Gram volume is bounded above by the same majorant. A summation lemma for dyadic sums with decay then adds up the pieces: the factors $2^{-2iq}$ and $2^{-2i'q}$ beat the growth $(2^{i+i'+1}H_1)^{16r^3}$ of the box volumes, and the restriction from the minors gives the factor $\sigma^{-(q-16r^3-4r-1)/r}$. The result is $K = \kappa s^{-1} c$ times a constant, and an elementary inequality, valid for $j \ge 1$, $H_1 \ge 1$, $D_e \ge 1$, $D > 0$ and $\sigma \ge 1$, bounds that constant by $\mathrm{Deg}$. $\square$

**Lemma 2.7.7 (Hilbert-Schmidt norm).** Let $J : W_q \to W_p$ be a linear map of finite-dimensional inner product spaces. Then
$$\|J\|_{\mathrm{HS}}^2 \le \dim W_p\, \|J\|^2.$$

*Proof.* Let $(e_i)$ and $(f_l)$ be orthonormal bases of $W_q$ and $W_p$. Then $\|J\|_{\mathrm{HS}}^2 = \sum_i \|J e_i\|^2 = \sum_l \|J^* f_l\|^2$, and each $\|J^* f_l\|$ is at most $\|J^*\| = \|J\|$. There are $\dim W_p$ terms. $\square$

At the real place of the proof, the Bessel functions come from good local data. Let $v > 0$ be the constant of the host field, let $\theta > 0$, let $\tau$ be a type and $u, u'$ words with positive traces, and suppose the local data at the real place are good for $(\tau, u, u', \theta)$. Then $\Phi$ and $\Phi'$ are Bessel functions for $z$ and $z'$ with the constant $c$ of the data and with the Haar measure $\kappa_\theta\, dn$ on $N$, where
$$\kappa_\theta = (2v)^{-rk}\, \theta\, 2^{r(k+1) + r(r-1)}.$$

**Theorem 2.7.8 (Hilbert-Schmidt norm of the degenerate amplitude).** Assume the local data at the real place are good for $(\tau, u, u', \theta)$ as above, with $v > 0$, $\theta > 0$ and positive traces of $u$ and $u'$. Let $1 \le j$, $j + 2 \le k$, $j \le r$, $16 r^3 + 4r + 2 \le q$, $s > 0$ and $H_1 \ge 1$. Assume that $\Phi$ and $\Phi'$ have tail bounds of order $q$ and scale $H_1$, that $D_e$ is a minor bound for $\gamma$, that $\mu_R$ is a normal-form stabilizer measure for $\gamma$ with scale $s$, and that $\nu_R$ is the quotient measure of $\mu_G$ by $\mu_R$. Then
$$\|J\|_{\mathrm{HS}} \le \sqrt{\dim W_p}\, \frac{\kappa_\theta}{s}\, \mathrm{Deg}\bigl(H_1, D_e, |D_j(\gamma)|, \sigma(\gamma, H_1)\bigr).$$

Lean: `GlobalTheory.Amp.sqrt_hsNormSq_amplitude_le_degBd` (also `GlobalTheory.T.amplitude_hsNorm_le_degreeBound_realPlace`, a second name).

*Proof.* Good local data give the two Bessel functions with $\kappa = \kappa_\theta > 0$. The [operator norm bound](/entry/deg-core/) gives $\|J\| \le (\kappa_\theta / s)\, \mathrm{Deg}$. The Lemma gives $\|J\|_{\mathrm{HS}} \le \sqrt{\dim W_p}\, \|J\|$. $\square$

**Remark 2.7.9.** The hypothesis $q \ge 16 r^3 + 4r + 2$ makes the exponent of $\sigma$ negative. Then the Hilbert-Schmidt norm of the amplitude decays like a negative power of the largest leading minor of $\gamma$. The factor $D^{-(k-1-j)}$ grows when $|D_j(\gamma)|$ is small, and the minor bound $D_e$ controls it.

**Remark 2.7.10 (Formalization).** The local data at the real place are records `D7`, `LocW`, `LocS` with conditions `GoodW` and `GoodS`; the text uses them only through the result that they give the two one-side conditions `OneSide` with the constant $\kappa_\theta$. We have not unfolded these records. The Hilbert-Schmidt norm is `hsNormSq`, and the identity $\|J\|_{\mathrm{HS}}^2 = \sum_i \|J e_i\|^2$ is the private lemma `hsNormSq_eq_sum_norm_sq`. The side bound has a local helper `tail` ([AmplificationDegenerateSidePieceBound.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplificationDegenerateSidePieceBound.lean#L82)) for the tail step, and the operator norm bound has local helpers `side` and `arith` (lines 78 and 133 of AmplitudeDegenerateOperatorNormLeRealPlace.lean). The second names are wrappers of the form `first | exact @X | exact X | ...`.
