---
title: Local weight charts
decls:
  - scWlocExists
  - WlocSk.scWlocExists_of_chart
  - WlocSk.wlocExists_of_charts
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local weight charts

The mass formula is a statement at the finite places. At a real place the proof needs a local test vector: a Bessel function $W$ on the real unitary group that is equivariant for a Bessel subgroup, square integrable on the quotient, integrable against a power of a height function, and reproduced by convolution with a matrix coefficient of a discrete series. This section constructs such a $W$ from a coordinate chart on the nilradical of the Bessel subgroup. The construction feeds the [nonempty hypotheses](/step/nonempty-hyps/), where it gives the archimedean component of the test vectors of the global data. For representations and their matrix coefficients see [representations of a group](/learn/representations/#representations-of-a-group); for parabolic subgroups and their unipotent radicals see [parabolic subgroups](/learn/groups/#parabolic-subgroups).

### The setting at a real place

Fix integers $k \geq 2$ and $r \geq 0$, and put $n = 2r + k + 1$. Let $G$ be the unitary group of the Hermitian form $H_{p,k}$ on $\mathbb{C}^n$, a closed subgroup of $GL_n(\mathbb{C})$. Let $S = W_S N \subseteq G$ be the Bessel subgroup: $N$ is the unipotent radical of a parabolic subgroup and $W_S$ is a unitary group of a smaller form that normalizes $N$. A parameter $z \in \mathbb{C}^n$ and a vector $c \in (\mathbb{C}^\times)^r$ give a character $\psi = \psi_{z,c}$ of $S$, trivial on $W_S$. For $g \in GL_n(\mathbb{C})$ let $\|g\|_{\mathrm{op}}$ be a fixed norm, and put
$$\nu(x) = \inf_{t \in S} \|t x\|_{\mathrm{op}}, \qquad N_1 = 4 n^2 \sqrt{2(r+1)}.$$
The function $\nu$ is a height on $S \backslash G$, and the weight $\nu^{N_1}$ measures how far a point of the quotient is from the base point.

**Definition 7.10.1 (Bessel function of type $\pi$).** Let $\pi$ be a finite-dimensional unitary representation of $W_S$ on $V_\pi$. A function $W : G \to V_\pi$ is *$(S, \psi, \pi)$-equivariant* if
$$W(w u g) = \psi(u)\, \pi(w)\, W(g) \quad \text{for } w \in W_S,\ u \in N,\ g \in G.$$

Let $\sigma$ be a discrete series representation of $G$ on a Hilbert space $\mathcal{H}$ with Harish-Chandra parameter $\lambda$, and let $w \in \mathcal{H}$ be a unit vector in the lowest $K$-type. The *matrix coefficient* is $e(g) = \langle w, \sigma(g) w \rangle$, and for a function $\alpha$ on $G$ the *right convolution* is
$$(\alpha * W)(x) = \int_G \alpha(g)\, W(x g)\, d\mu_G(g).$$

**Definition 7.10.2 (Local weight function).** Given $\sigma$, $w$, $\pi$, Haar measures $\mu_G$ on $G$ and $\mu_S$ on $S$, and the quotient measure $\nu_{S \backslash G}$, a *local weight function* is a function $W : G \to V_\pi$ with the following properties.

1. $W$ is continuous and $(S, \psi, \pi)$-equivariant.
2. For each $x \in G$ the function $g \mapsto e(g) W(x g)$ is integrable, and $e * W = W$.
3. $\int_{S \backslash G} \|W\|\, d\nu < \infty$, and the $L^2$ norm of $W$ on $S \backslash G$ is $1$.
4. $\int_{S \backslash G} \|W(x)\|\, \nu(x)^{N_1}\, d\nu(x) < \infty$.
5. There are a compact set $\Omega \subseteq G$ with $1 \in \Omega$, a constant $a$ and a measurable function $\alpha$ supported in $\Omega$ with $|\alpha| \leq a$, such that $g \mapsto \alpha(g) W(x g)$ is integrable for each $x$ and $\alpha * W = W$.

The first two properties make $W$ a vector in the Bessel model of $\sigma$ of type $\pi$. The third and fourth control $W$ at infinity on the quotient, and the fifth lets the global argument replace the matrix coefficient by a compactly supported function.

### Inputs

**Theorem 7.10.3 (Nonvanishing of the Bessel period).** Assume the gap condition on the parameters. Then for each discrete series $\sigma$ of the given type, each $\pi$ of the given type, each lowest unit vector $w$ and all Haar measures $\mu_W$ on $W_S$ and $\mu_N$ on $N$, there are $x, x_0 \in G$ with
$$\int_{W_S \times N} \langle \sigma(x_0) w, \sigma(m u) \sigma(x) w \rangle\, \overline{\psi(u)}\, \pi(m)^{-1}\, d\mu_W(m)\, d\mu_N(u) \neq 0.$$

We also take as given the weighted local estimate on the coefficients, and the following reproducing property of discrete series.

**Theorem 7.10.4 (Reproducing formula).** Let $\sigma$ be a discrete series of $G$ of the given type and $w$ a vector of its lowest $K$-type. Then there is a bounded function $\alpha$ with compact support on $G$ such that
$$\int_G \alpha(g)\, \sigma(g) w\, d\mu_G(g) = w.$$

**Definition 7.10.5 (Nilpotent chart).** A *nilpotent chart* of the Bessel data gives, for each $k$ and $r$, an integer $m$, a dimension $d$, an exponent $q$ with $q(2m + d) < N_1$, a measurable embedding $\Phi$ of $\mathbb{R}^{2m+d}$ onto the nilradical set, and a constant $\kappa$, such that left multiplication by each element of the nilradical preserves the measure in the coordinates $\Phi$, and
$$1 + \|t\| \leq \kappa\, \|\Phi(t)\|_{\mathrm{op}}^{q} \quad \text{for all } t.$$

The chart turns the integral over $N$ into an integral over a Euclidean space, and the polynomial bound turns the decay of $W$ in the norm into the decay in $t$. The condition $q(2m + d) < N_1$ is what makes $\nu^{N_1}$ large enough to absorb the volume growth of the chart.

**Lemma 7.10.6 (Right invariance on the unipotent set).** The finite Haar measure on $W_S$ is invariant under right translation by the elements of $W_S$, and the group $N$ is unimodular.

### The construction

**Theorem 7.10.7 (Local weight functions from charts).** Assume that a nilpotent chart exists, that the right invariance holds, and that the reproducing formula holds. Then, under the nonvanishing of the Bessel period and the weighted local estimate, for all $k$, $r$, $z$, $c$ and parameters of the real place numerical setting, for each discrete series $\sigma$ of the given type, each $\pi$ of the given type, each lowest unit vector $w$, and all Haar measures $\mu_G$, $\mu_S$ with quotient measure $\nu$, there is a local weight function.

Lean: `WlocSk.wlocExists_of_charts` (also `WlocSk.scWlocExists_of_chart`, the same conclusion with the right invariance supplied, and `scWlocExists`, with the chart supplied).

*Proof.* The chart and the right invariance give Haar measures $\mu_W$ on $W_S$ and $\mu_N$ on $N$, with $\mu_W$ finite. The nonvanishing of the Bessel period, with the reproducing formula and the weighted estimate, gives $x_0 \in G$ and $\xi \in V_\pi$ such that the function
$$\begin{aligned} A(g) = \int_{W_S \times N} & \overline{\psi(u)}\, \langle \sigma(x_0) w, \sigma(m u)\, \sigma(g) w \rangle \\ & \cdot \pi(m)^{-1} \xi \; d\mu_W(m)\, d\mu_N(u) \end{aligned}$$
is not zero in $L^2(S \backslash G)$. Put $W = \|A\|_{2}^{-1} A$, so that the $L^2$ norm of $W$ is $1$. A change of variables $m \mapsto h m$ and $u \mapsto u u_0$ in the integral, with the invariance of $\mu_W$ and $\mu_N$, gives the equivariance. The continuity of $A$ and the two integrability properties come from the chart: in the coordinates $\Phi$ the integral over $N$ becomes an integral over $\mathbb{R}^{2m+d}$, the decay of the matrix coefficient and the bound $1 + \|t\| \leq \kappa \|\Phi(t)\|_{\mathrm{op}}^q$ give an integrable majorant, and $q(2m + d) < N_1$ leaves room for the weight $\nu^{N_1}$. The reproducing property $e * W = W$ comes from the fact that $w$ lies in the lowest $K$-type of $\sigma$, and the fifth property comes from the reproducing formula: with $\alpha$ as there, $\alpha * A = A$. All properties pass from $A$ to the scalar multiple $W$. $\square$

The chart itself is constructed explicitly from the root coordinates of the nilradical; we take its existence as the input of the last two names of the theorem.

**Remark 7.10.8 (Formalization).** The theorem is stated as an implication whose premises, the nonvanishing of the Bessel period and the weighted local estimate on coefficients, are not proved here ([SettingBlocks.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/SettingBlocks.lean#L429)). The proof passes through named facts on the decomposition of $\sigma$ into $K$-types, a decay estimate, the reproducing formula of matrix coefficients, the unitarity of $\sigma$, the compactness of the unipotent set and the uniqueness of the Haar measure on the nilradical; the analytic estimates in the proof above are our reading of these names, and we did not unfold the definition of the Bessel subgroup, the form $H_{p,k}$, the character $\psi_{z,c}$ or the numerical setting at the real place. The chart is stated in [OpnContinuous.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/LocalWeightCharts/OpnContinuous.lean#L23). The reproducing formula is supplied by the caller ([ScWlocExists.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/LocalWeightCharts/ScWlocExists.lean#L4)). The exponent $N_1$ here is $4n^2\sqrt{2(r+1)}$, a different constant from the exponent of the next section.
