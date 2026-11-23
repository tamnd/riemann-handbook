---
title: Uniqueness of Bessel maps for discrete series
decls:
  - CompanionTheory.Bmu.besselMapUniqGap
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Uniqueness of Bessel maps for discrete series

This section proves local multiplicity one for Bessel models at the real place, in the form that the proof uses: if $\sigma$ is a discrete series of $G = \mathrm{U}(r+k, r+1)$ whose Harish-Chandra parameter has a large gap between its two signs, and $\pi$ is an irreducible representation of $U_W \cong \mathrm{U}(k)$, then any two Bessel maps of type $(\psi_c, \pi)$ are proportional. The result is [Theorem 6.2.7](/entry/bessel-map-uniq-gap/) below. It is one of the inputs of [HypsAlt is nonempty](/step/nonempty-hyps/), and the next section turns it into convolution bounds and amplitude bounds. We use the notation of [the previous section](/entry/bounded/).

### Discrete series by their parameters

Let $\varepsilon : \{0, \dots, n-1\} \to \{+, -\}$ be a sign vector, $J_\varepsilon = \mathrm{diag}(\pm 1)$ with sign $\varepsilon_a$ at $a$, and $\mathrm{U}(J_\varepsilon) = \{ g : g^* J_\varepsilon g = J_\varepsilon \}$. Its maximal compact subgroup is $K_\varepsilon = \{ g \text{ unitary} : g J_\varepsilon = J_\varepsilon g \}$ ([discrete series](/learn/representations/#discrete-series), [real reductive groups](/learn/real-groups/#real-reductive-groups)).

**Definition 6.2.1 (Harish-Chandra parameter).** A vector $\lambda \in \mathbb{R}^n$ is a *Harish-Chandra parameter* if $\lambda_0 > \lambda_1 > \dots > \lambda_{n-1}$ and $\lambda_a - \frac{n-1}{2} \in \mathbb{Z}$ for all $a$.

**Definition 6.2.2 (Blattner parameter).** Let $\rho_c(a) = \frac12 ( \#\{ b > a : \varepsilon_b = \varepsilon_a \} - \#\{ b < a : \varepsilon_b = \varepsilon_a \})$ and $\rho_n(a) = \frac12 ( \#\{ b > a : \varepsilon_b \neq \varepsilon_a \} - \#\{ b < a : \varepsilon_b \neq \varepsilon_a \})$. The *Blattner parameter* of $(\varepsilon, \lambda)$ is $\Lambda = \lambda + \rho_n - \rho_c$.

**Definition 6.2.3 (Discrete series).** A representation $\sigma$ of $\mathrm{U}(J_\varepsilon)$ on a nonzero Hilbert space is a *discrete series with parameter $\lambda$* if it is unitary and irreducible, its matrix coefficients are square integrable, it contains a $K_\varepsilon$-type of highest weight $\Lambda$, and $\Lambda$ minimizes $\| \mu + 2 \rho_c \|^2$ over the highest weights $\mu$ of all $K_\varepsilon$-types of $\sigma$. A representation $\sigma$ of $G = \mathrm{U}(H)$ is a discrete series with parameter $(\varepsilon, \lambda)$ if there is a unitary $P$ with $P^* J_\varepsilon P = H$ such that $g \mapsto \sigma(P^{-1} g P)$ is a discrete series of $\mathrm{U}(J_\varepsilon)$ with parameter $\lambda$.

The last two conditions characterize the lowest $K$-type in the sense of Vogan's norm. A discrete series with Harish-Chandra parameter $\lambda$ contains the $K$-type $\Lambda$ with multiplicity one, and $\Lambda$ is its lowest $K$-type (Knapp, *Representation Theory of Semisimple Groups*, Chapter IX; see [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees)).

**Definition 6.2.4 (Gap).** Let $h \geq 0$. The parameter $(\varepsilon, \lambda)$ has *gap at least $h$* if $|\lambda_a - \lambda_b| \geq h$ whenever $\varepsilon_a \neq \varepsilon_b$.

So the entries of the two signs are far apart. Large gaps give fast decay of matrix coefficients ([asymptotics of matrix coefficients](/learn/real-groups/#asymptotics-of-matrix-coefficients)).

**Definition 6.2.5 (Type of $\pi$).** Let $u \in \mathbb{R}^k$. A *frame* for $z$ is an element $g \in G$ that fixes $e_a$ and $e_{2r+k-a}$ for $a < r$ and maps $\sqrt{T_z}\, e_{r+k}$ to $z$. Let $\iota : \mathrm{U}(k) \to G$ put a $k \times k$ unitary matrix in the rows and columns $r, \dots, r+k-1$. A representation $\pi$ of $U_W$ on $V$ has *Harish-Chandra type $u$* if for some frame $g$ the map $h \mapsto \pi(g \iota(h) g^{-1})$ is a unitary representation of $\mathrm{U}(k)$ on $V \neq 0$, $V$ is finite-dimensional, and $V$ is irreducible of highest weight $u - \rho_k$.

Here all signs are $+$, so $\rho_n = 0$ and the Blattner parameter is $u - \rho_k$: $u$ is the infinitesimal character of $\pi$, as in [highest weights and branching](/learn/representations/#highest-weights-and-branching).

### Uniqueness

The classical statement is the following.

**Theorem 6.2.6 (Jiang, Sun and Zhu).** Let $\sigma$ be an irreducible Casselman-Wallach representation of $\mathrm{U}(p, q)$ and $\pi$ an irreducible Casselman-Wallach representation of the subgroup $U_W$ of a Bessel pair, with a generic character $\psi$ of $N$. Then $\dim \mathrm{Hom}_R(\sigma \otimes \bar\pi \otimes \bar\psi, \mathbb{C}) \leq 1$.

The theorem used here is a special case, with a gap hypothesis and a proof by orbit integrals.

**Theorem 6.2.7 (Uniqueness of Bessel maps).** Let $k \geq 1$ and $n = 2r+k+1$. Let $(\varepsilon, \lambda)$ be a Harish-Chandra parameter with gap at least $h$, where $h \geq 120 n^3$. Let $\sigma$ be a discrete series of $G$ with parameter $(\varepsilon, \lambda)$. Let $z \in W_0$ with $T_z > 0$, and let $c \in \mathbb{C}^r$ with $c_a \neq 0$ for all $a$. Let $\pi$ be a representation of $U_W$ of Harish-Chandra type $u$. Let $B_1$ and $B_2$ be Bessel maps of type $(\psi_c, \pi)$. Then there are $a, b \in \mathbb{C}$, not both $0$, with
$$a B_1(v) + b B_2(v) = 0 \quad \text{for all smooth } v.$$

Lean: `CompanionTheory.Bmu.besselMapUniqGap`.

So the space of Bessel maps of type $(\psi_c, \pi)$ has dimension at most $1$.

*Proof.* We first move to the standard character. There is $\tau \in G$ that commutes with $U_W$, normalizes $N$, and satisfies $\psi_c(\tau m \tau^{-1}) = \psi_{\mathrm{std}}(m)$ for $m \in N$. We take this torus conjugacy as a proved lemma. If $B$ is a Bessel map of type $(\psi_c, \pi)$, then $B' = B \circ \sigma(\tau)$ satisfies
$$B'(\sigma(hm) v) = B(\sigma(h \, \tau m \tau^{-1} \, \tau) v) = \psi_{\mathrm{std}}(m) \, \pi(h) B'(v),$$
and $B'$ is again continuous for a Sobolev norm. So $B'$ is a Bessel map of type $(\psi_{\mathrm{std}}, \pi)$.

Next, decay. Since $\sigma$ is a discrete series, it is square integrable. The gap $h \geq 120 n^3$ exceeds a threshold of the form $t(\varepsilon) + 4 n^3$. For such gaps, each matrix coefficient between smooth vectors decays: $|\langle v, \sigma(x) w \rangle| \leq C \|x\|^{-a}$, with a fixed exponent $a$ that depends only on $k$ and $r$, for $x$ in the subset of $G$ over which the orbit integral below runs.

Fix a unit vector $w_0$ in the lowest $K$-type. It is smooth. By the multiplicity one theorem for the standard character, [Theorem 4.7](/entry/thm-m/), there is a Bessel map $l$ of type $(\psi_{\mathrm{std}}, \pi)$ with this property: every Bessel map of this type that is bounded on the orbit of $w_0$ is a multiple of $l$ on the vectors $\sigma(x) w_0$. That theorem is proved by an orbit integral. The reproducing formula for a square-integrable representation,
$$\int_G \overline{\langle v, \sigma(y) w_0 \rangle} \, \sigma(y) w_0 \, dy = d_\sigma^{-1} v,$$
with $d_\sigma$ the formal degree, expresses $B'(\sigma(x) w_0)$ as an integral of $B'$ over the orbit of $w_0$ against a matrix coefficient. The decay makes the integral converge, and the equivariance under $R$ reduces it to the values of $l$.

By [Theorem 6.1.5](/entry/bounded/), $B_i'$ is bounded on the orbit of $w_0$. So there are constants $c_1, c_2$ with
$$B_i(\sigma(\tau) \sigma(x) w_0) = c_i \, l(\sigma(x) w_0) \quad \text{for all } x \in G,\ i = 1, 2.$$
If $c_1 = 0$, take $(a,b) = (1, 0)$. Otherwise take $(a, b) = (c_2, -c_1)$. In both cases $a c_1 + b c_2 = 0$. Then $E = a B_1' + b B_2'$ is a Sobolev-continuous linear map that vanishes on all $\sigma(x) w_0$. The vector $w_0$ is cyclic for the smooth vectors: finite linear combinations of the $\sigma(x) w_0$ approximate each smooth vector in every finite family of word seminorms. So $E$ vanishes on smooth vectors. Applied to $\sigma(\tau^{-1}) v$, this gives $a B_1(v) + b B_2(v) = 0$. $\square$

**Remark 6.2.8.** The gap hypothesis is not in the theorem of Jiang, Sun and Zhu. Here it gives the decay of matrix coefficients that the orbit integral needs. The proof by an orbit integral and a reproducing formula is a form of the Gelfand-Kazhdan approach for square-integrable representations. It does not use invariant distributions.

**Remark 6.2.9 (Formalization).** The general statement without a gap, with the same objects, is defined in [BesselMapUniq.lean](lean:Formalism/PeriodIntegrals/BesselMapUniq.lean#L50) but not proved or used here. The threshold $120 n^3$ is used only through one inequality, [OrbitMult.lean](lean:CompanionTheory/AutomorphicTheory/BesselOrbitBounds/BesselMapUniqueness/OrbitMult.lean#L138). The proof is `uniq_of` applied to the orbit bound of the previous section and to wrappers for torus conjugacy, a derived series bound and a factorization. The character $\psi_c$ is defined in three places, and the group data $H$, $N$, $U_W$, $T_z$ are duplicated between [StatementG.lean](lean:Formalism/FormalDegreeBessel/StatementG.lean#L11) and [IsLowUnitH.lean](lean:Formalism/PeriodIntegrals/IsLowUnitH.lean#L87). We have not unfolded the decay estimate or the cyclicity lemma.
