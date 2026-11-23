---
title: The Fourier-Jacobi coefficient of an Eisenstein series
decls:
  - GlobalTheory.CompanionTheory.ZUnf.unfold_on
  - GlobalTheory.CompanionTheory.ZUnf.zUnfold
  - GlobalTheory.T.fourier_jacobi_unfolding
  - GlobalTheory.CompanionTheory.FJE.fjEis
  - GlobalTheory.T.fourier_jacobi_eisenstein
  - PositivityTheory.Rg.Rsw.fjEis
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Fourier-Jacobi coefficient of an Eisenstein series

Let $\rho + p = n$. A Siegel Eisenstein series on $G_n$ has a Fourier-Jacobi coefficient along the Heisenberg group of the parabolic subgroup with Levi factor $GL_\rho \times U(p,p)$. This section proves that, in the range of absolute convergence, the Fourier-Jacobi coefficient against a theta function is again a Siegel Eisenstein series, now on the smaller group $G_p$, of a section built from the original one. This is the classical reduction of the Fourier-Jacobi coefficients of Eisenstein series to Eisenstein series of lower rank ([Fourier-Jacobi periods](/learn/periods/#bessel-and-fourier-jacobi-periods)). The identity is an input of the residue functional and of the polar part identity, which feed [Theorem 5.7.3](/entry/res-core/).

We keep the notation of the previous section. Matrices with blocks of sizes $\rho$ and $p$ are written $\begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix}$, and $\mathrm{diag}(\alpha, \delta)$ is the block diagonal matrix. Let $\mathrm{Herm}_\rho$ be the Hermitian $\rho \times \rho$ matrices and $M_{\rho \times p}$ the $\rho \times p$ matrices.

**Definition 5.2.1 (Jacobi data).** Fix $\rho + p = n$. The *Jacobi data* are four continuous maps into $G_n$ with the following matrices.

1. A homomorphism $\iota \colon G_p \to G_n$: if $h = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, then $\iota(h) = \begin{pmatrix} \mathrm{diag}(1, a) & \mathrm{diag}(0, b) \\ \mathrm{diag}(0, c) & \mathrm{diag}(1, d) \end{pmatrix}$.
2. Heisenberg elements, for $z \in \mathrm{Herm}_\rho(\mathbb{A}_E)$ and $x \in M_{\rho \times p}(\mathbb{A}_E)$: $\mathbf{n}(z, x) = \begin{pmatrix} 1 & \begin{pmatrix} z & x \\ x^* & 0 \end{pmatrix} \\ 0 & 1 \end{pmatrix}$.
3. Shears, for $y \in M_{\rho \times p}(\mathbb{A}_E)$: $\mathbf{s}(y) = \mathrm{diag}\Bigl(\begin{pmatrix} 1 & y \\ 0 & 1 \end{pmatrix}, \begin{pmatrix} 1 & 0 \\ -y^* & 1 \end{pmatrix}\Bigr)$.
4. A Weyl element $w = \begin{pmatrix} \mathrm{diag}(0, 1) & \mathrm{diag}(1, 0) \\ \mathrm{diag}(-1, 0) & \mathrm{diag}(0, 1) \end{pmatrix}$.

The elements $\mathbf{n}(z, 0)$ form the centre of the Heisenberg group, and $\iota(G_p)$ and the shears normalise it. We also fix measures: a [Haar measure](/learn/analysis/#haar-measure) $\lambda$ on $\mathrm{Herm}_\rho(\mathbb{A}_E)$ with a fundamental domain $\mathcal{G}$ for $\mathrm{Herm}_\rho(E)$ of volume one, and a Haar measure $\mu$ on $M_{\rho \times p}(\mathbb{A}_E)$ with a fundamental domain $\mathcal{F}$ for $M_{\rho \times p}(E)$ of volume one.

An *additive character* is a continuous character $\psi \colon \mathbb{A} \to \mathbb{C}^\times$ with $|\psi| = 1$, trivial on $F$ and not trivial. A *Hecke character* is a continuous character $\chi \colon \mathbb{A}_E^\times \to \mathbb{C}^\times$ of absolute value $1$ that is trivial on $E^\times$ ([Hecke characters](/learn/class-field-theory/#hecke-characters)). We also fix a family $\vartheta$ of embeddings of the archimedean part of $\mathbb{A}_E$ into $\mathbb{C}$, one for each archimedean place; it determines the space of Schwartz functions on $M_{\rho \times p}(\mathbb{A}_E)$.

Fix an additive character $\psi$ and a rational $b_0 \in \mathrm{Herm}_\rho(E)$. Put $\psi_{b_0}(z) = \psi(\tfrac12 \operatorname{tr}(b_0 z))$, where $\tfrac12\operatorname{tr}$ is half the trace from $\mathbb{A}_E$ to $\mathbb{A}$, and $\langle x, y \rangle = x^* b_0 y \in M_p(\mathbb{A}_E)$ for $x, y \in M_{\rho \times p}(\mathbb{A}_E)$.

**Definition 5.2.2 (Coefficients).** For $F \colon G_n \to \mathbb{C}$ and $g \in G_n$ put
$$F_Z(g) = \int_{\mathcal{G}} F(\mathbf{n}(z, 0) g)\, \overline{\psi_{b_0}(z)}\, d\lambda(z), \qquad F_P(g) = \int_{\mathcal{F}} F_Z(\mathbf{n}(0, x) g)\, d\mu(x).$$
For $\varphi \colon M_{\rho \times p}(\mathbb{A}_E) \to \mathbb{C}$ the *Fourier-Jacobi coefficient* of $F$ is
$$\mathrm{FJ}(F)(g, \varphi) = \int F_P(\mathbf{s}(y) g)\, \overline{\varphi(y)}\, d\mu(y).$$

The first integral is the $\psi_{b_0}$-coefficient along the centre, and the second averages it over the rest of the Heisenberg group. For a section $f$ on $G_n$ we also use the integral over the whole centre, and the section on $G_p$ built from it.

**Definition 5.2.3 (Centre integral and reduced section).** For $f \colon G_n \to \mathbb{C}$ put
$$W(f)(g) = \int_{\mathrm{Herm}_\rho(\mathbb{A}_E)} f(w\, \mathbf{n}(z, 0)\, g)\, \overline{\psi_{b_0}(z)}\, d\lambda(z).$$
For $g \in G_n$ and $\Omega \colon G_p \times M_{\rho \times p}(\mathbb{A}_E) \to \mathbb{C}$, the *reduced section* is the function on $G_p$
$$R(f, g, \Omega)(h) = \int W(f)(\mathbf{s}(y)\, \iota(h)\, g)\, \overline{\Omega(h, y)}\, d\mu(y).$$

**Definition 5.2.4 (Theta class).** Let $\chi'$ be a Hecke character. The *theta class* $\mathrm{Th}(\psi, \chi', b_0)$ (for the fixed family $\vartheta$) is the set of $\Omega \colon G_p \times M_{\rho \times p}(\mathbb{A}_E) \to \mathbb{C}$ such that:

1. each $\Omega(h, \cdot)$ is a Schwartz function, $\Omega$ is continuous, and on each compact set of $h$ the functions $\Omega(h, \cdot)$ have a common Schwartz majorant;
2. for $m = \mathrm{diag}(a, (a^*)^{-1})$, $\Omega(mh, y) = \chi'(\det a)\, |\det a|^{\rho/2}\, \Omega(h, ya)$;
3. for $u = \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}$, $\Omega(uh, y) = \psi(\tfrac12 \operatorname{tr}(b \langle y, y \rangle))\, \Omega(h, y)$;
4. for $w_p = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, $\Omega(w_p h, x) = \int \Omega(h, y)\, \psi(\operatorname{tr} \langle x, y \rangle)\, d\mu(y)$.

These are the formulas of the [Weil representation](/learn/theta/#the-weil-representation) in the Schrödinger model: $h \mapsto \Omega(h, \cdot)$ is the orbit of a Schwartz function. The *theta function* of $\varphi$ is
$$\theta(\varphi)(z, x, y) = \psi_{b_0}(z) \sum_{\xi \in M_{\rho \times p}(E)} \psi(\operatorname{tr} \langle x, \xi \rangle)\, \varphi(\xi + y).$$

Recall that $f$ is a *section of degree $s$* for a Hecke character $\chi$ if $f(qg) = \chi(\det a_q)\, |\det a_q|^{s + n/2} f(g)$ for all $q \in P_n$.

**Theorem 5.2.5 (Unfolding along the centre).** Let $\psi$ be an additive character, $\det b_0 \neq 0$, $\chi$ a Hecke character, and $f$ a continuous section of degree $s$ for $\chi$ with $\operatorname{Re} s > n/2$. Let $C \subset G_n$ be compact. Then there are a summable function $U$ on $P_n(F) \backslash G_n(F)$ and an injective map
$$e \colon \mathrm{Herm}_\rho(E) \times \bigl(P_p(F) \backslash G_p(F) \times M_{\rho \times p}(E)\bigr) \to P_n(F) \backslash G_n(F)$$
such that for all $g \in C$ and $u = (q, \xi)$:

1. $|W(f)(\mathbf{s}(\xi)\, \iota(q)\, g)| \le \sum_{l} U(e(l, u))$;
2. the family $u \mapsto W(f)(\mathbf{s}(\xi)\, \iota(q)\, g)$ is summable with sum $E(f)_Z(g)$.

Lean: `GlobalTheory.CompanionTheory.ZUnf.unfold_on`.

*Proof.* Since $\operatorname{Re} s > n/2$, the terms $f(\gamma g)$ of $E(f)$ do not depend on the choice of representatives, and they have a summable majorant uniformly for $g$ in a compact set. We apply this to the compact set $K_0 C$, where $K_0$ is a compact set whose translates by $\mathrm{Herm}_\rho(E)$ cover $\mathrm{Herm}_\rho(\mathbb{A}_E)$; this gives $U$.

The rational centre $\mathbf{n}(l, 0)$, $l \in \mathrm{Herm}_\rho(E)$, acts on $P_n(F) \backslash G_n(F)$ by right translation. To each coset we attach a subspace of $E^\rho$, and we sort the cosets by it. The cosets with zero subspace are parametrised by $e$: the term of $e(l, u)$ at $\mathbf{n}(b, 0) g$ is $f(w\, \mathbf{n}(l + b, 0)\, \mathbf{s}(\xi)\, \iota(q)\, g)$. On these cosets, the sum over $l$ and the integral over the fundamental domain $\mathcal{G}$ combine into one integral over $\mathrm{Herm}_\rho(\mathbb{A}_E)$, and the character $\overline{\psi_{b_0}}$ is trivial on rational $l$. This gives $W(f)(\mathbf{s}(\xi)\, \iota(q)\, g)$, and the majorant gives the bound 1. For a coset with a nonzero subspace, there is a rational $\nu$ in it with $\psi_{b_0}(\nu) \neq 1$ and $q\, \mathbf{n}(\nu, 0) = x q$ with $x \in P_n$ and $\det a_x = 1$. So the term of the coset is invariant under the translation by $\nu$, while the character is not. Hence its integral against $\overline{\psi_{b_0}}$ over the compact quotient is zero. Here $\det b_0 \neq 0$ is used. The integral of the summable majorant justifies all exchanges of sums and integrals. $\square$

**Theorem 5.2.6 (Unfolding the centre coefficient).** Let $\psi$, $b_0$, $\chi$, $f$, $s$ be as in the last theorem. Then for each $g \in G_n$ the family
$$(q, \xi) \mapsto W(f)(\mathbf{s}(\xi)\, \iota(q)\, g), \qquad (q, \xi) \in P_p(F) \backslash G_p(F) \times M_{\rho \times p}(E),$$
is summable with sum $E(f)_Z(g)$. For each compact $C \subset G_n$ there is a summable function $c$ of $(q, \xi)$ with $|W(f)(\mathbf{s}(\xi)\, \iota(q)\, g)| \le c(q, \xi)$ for all $g \in C$.

Lean: `GlobalTheory.CompanionTheory.ZUnf.zUnfold` (also `GlobalTheory.T.fourier_jacobi_unfolding`, a second name).

*Proof.* The sum is [Theorem 5.2.5](/entry/unfold-on/) for the compact set $\{g\}$. For a compact $C$, take $U$ and $e$ from [Theorem 5.2.5](/entry/unfold-on/) and put $c(u) = \sum_l U(e(l, u))$. The map $(u, l) \mapsto e(l, u)$ is injective and $U$ is summable, so $(u, l) \mapsto U(e(l, u))$ is summable, and its partial sums $c$ over $l$ form a summable family. $\square$

The second input is the behaviour of the theta function under rational points of $G_p$. We take it as given.

**Theorem 5.2.7 (Theta twist).** Let $\psi$ be an additive character, $b_0$ rational with $\det b_0 \neq 0$, $\chi$ a Hecke character and $\Omega \in \mathrm{Th}(\psi, \chi, b_0)$ be given. Let $\gamma \in G_p(F)$, and let $z, x, y, z', x', y'$ satisfy
$$\iota(\gamma)\, \mathbf{n}(z, x)\, \mathbf{s}(y) = \mathbf{n}(z', x')\, \mathbf{s}(y')\, \iota(\gamma).$$
Then $\theta(\Omega(1, \cdot))(z, x, y) = \theta(\Omega(\gamma, \cdot))(z', x', y')$.

Lean: `GlobalTheory.T.theta_twist_identity`.

*Proof.* We take this result as given; we do not prove it in this chapter. It is the automorphy of the theta function in the Weil representation. $\square$

**Theorem 5.2.8 (Fourier-Jacobi coefficient of an Eisenstein series).** Assume the conclusions of the unfolding of the centre coefficient and of the theta twist. Let $\psi$ be an additive character, $\det b_0 \neq 0$, $\chi$ and $\chi'$ Hecke characters, $\Omega \in \mathrm{Th}(\psi, \chi', b_0)$, and $f$ a continuous section of degree $s$ for $\chi$ with $\operatorname{Re} s > n/2$. Then for all $g \in G_n$
$$\mathrm{FJ}(E(f))(g, \Omega(1, \cdot)) = E\bigl(R(f, g, \Omega)\bigr)(1),$$
where on the right $E$ is the Siegel Eisenstein sum on $G_p$.

Lean: `GlobalTheory.CompanionTheory.FJE.fjEis` (also `GlobalTheory.T.fourier_jacobi_eisenstein`, a second name).

*Proof.* Write $F = E(f)$. It is left invariant under $G_n(F)$, so $F_Z$ is invariant under the rational Heisenberg elements up to the character. Splitting the integral over $y$ in $\mathrm{FJ}$ into translates of $\mathcal{F}$, and the sum over the lattice into the theta function, gives
$$\mathrm{FJ}(F)(g, \Omega(1, \cdot)) = \int_{\mathcal{F} \times \mathcal{F}} F_Z\bigl(\mathbf{n}(0, v_2)\, \mathbf{s}(v_1)\, g\bigr)\, \overline{\theta(\Omega(1, \cdot))(0, v_2, v_1)}\, d\mu(v_1)\, d\mu(v_2).$$
Now replace $F_Z$ by its unfolded series from [Theorem 5.2.6](/entry/z-unfold/): a sum over $q \in P_p(F) \backslash G_p(F)$ and $\eta \in M_{\rho \times p}(E)$ of $W(f)(\mathbf{s}(\eta)\, \iota(q)\, \mathbf{n}(0, v_2)\, \mathbf{s}(v_1)\, g)$. For a fixed $q$, move $\iota(q)$ to the left of the Heisenberg element. The theta twist turns $\theta(\Omega(1, \cdot))$ at the old point into $\theta(\Omega(q, \cdot))$ at the new point. The sum over $\eta$ and the sum inside the theta function then combine with the integral over $\mathcal{F} \times \mathcal{F}$ into one integral over all $y \in M_{\rho \times p}(\mathbb{A}_E)$. This is
$$\int W(f)(\mathbf{s}(y)\, \iota(q)\, g)\, \overline{\Omega(q, y)}\, d\mu(y) = R(f, g, \Omega)(q).$$
The measure of $\mathcal{F} \times \mathcal{F}$ is $1$, and the majorant of [Theorem 5.2.6](/entry/z-unfold/) bounds the terms. So the sum over $q$ and the integral can be exchanged, and the sum over $q$ of $R(f, g, \Omega)(q)$ is $E(R(f, g, \Omega))(1)$. $\square$

**Corollary 5.2.9 (Fourier-Jacobi coefficient of an Eisenstein series).** The identity $\mathrm{FJ}(E(f))(g, \Omega(1, \cdot)) = E(R(f, g, \Omega))(1)$ holds under the hypotheses on $\psi$, $b_0$, $\chi$, $\chi'$, $\Omega$, $f$ and $s$ of the last theorem, with no further assumption.

Lean: `PositivityTheory.Rg.Rsw.fjEis`.

*Proof.* This is [Theorem 5.2.8](/entry/fje-fj-eis/) applied to [Theorem 5.2.6](/entry/z-unfold/) and to the theta twist. $\square$

**Remark 5.2.10 (Formalization).** We have not unfolded the Schwartz space attached to $\vartheta$, nor the subspace that sorts the cosets in the proof of the unfolding. The maps $\iota$, $\mathbf{n}$, $\mathbf{s}$, $w$ and the measures are data with the stated matrices and properties, not fixed formulas for the group elements. The proof of the unfolding raises the heartbeat limit to 1,600,000 ([FourierJacobiUnfolding.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FourierJacobiUnfolding.lean#L49)). The second names of the unfolding and of the main theorem are wrappers that try three tactics, with the heartbeat limit at one million, for a one-line proof. The main theorem asks for a Hecke character $\chi'$ for $\Omega$, but nothing ties $\chi'$ to $\chi$; the relation appears only in the next section, where $R(f, g, \Omega)$ is a section for $\chi \chi'^{-1}$.
