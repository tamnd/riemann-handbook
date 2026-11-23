---
title: Haar measures on unipotent groups and an energy bound
decls:
  - Formalism.L2.S.Pv.HaarSubS.measN_holds
  - Formalism.L2.S.Pv.HaarSubS.stepSubG_holds
  - Formalism.L2.S.Pv.EnergyAbs.energyAbs_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Haar measures on unipotent groups and an energy bound

This section moves to the archimedean places. We study the real points of the flag subgroups of the last section and their Haar measures, and we prove an abstract bound on the energy of a family of vector valued functions on a group. The first two results show that the subgroup $S_\infty$ with its measure satisfies the hypotheses of the bound; they serve the [real object at infinity](/entry/real-obj-in-infinity-x-jsz/). The bound serves the [estimate at infinity](/entry/in-infinity-xat/). For Haar measures see [Haar measure](/learn/analysis/#haar-measure) and [[Haar measure|CE0V9686M8]]; for the representations see [discrete series](/learn/representations/#discrete-series).

### The groups at infinity

Let $F$ be a totally real field and $n \geq 1$. For each real place $v$ of $F$ fix a sign vector $\varepsilon_v \in \{\pm 1\}^n$, let $J_v$ be the diagonal matrix with entries $\varepsilon_v$, and let $h_v(x, y) = x^* J_v y$ on $\mathbb{C}^n$. Let $U_v \subseteq GL_n(\mathbb{C})$ be the unitary group of $h_v$ and
$$G_\infty = \prod_{v} U_v,$$
with the product $\mu_\infty$ of fixed Haar measures on the factors.

We fix the data of a *Hermitian setting*: a Hermitian space over the CM field $K$ with a basis, vectors $e_1, \dots, e_r$, $f_1, \dots, f_r$ and, for each index $u$ of a finite family, a vector $z_u$. Their images under the real place $v$ are vectors $e_a^v, f_a^v, z_u^v \in \mathbb{C}^n$. The data satisfy the frame relations of the last section: $h(e_a, e_b) = h(f_a, f_b) = 0$, $h(e_a, f_b) = \delta_{ab}$, $h(e_a, z_u) = h(f_a, z_u) = 0$, and $h(z_u, z_u) = -T_u$ for a prime number $T_u$.

**Definition 6.9.1 (Flag subgroups at infinity).** Fix $u$.

1. $S_\infty(u)$ is the set of $g \in G_\infty$ such that at each real place $v$, $(g_v - 1) e_a^v \in \operatorname{span}(e_b^v : b < a)$ for each $a$ and $(g_v - 1) z_u^v \in \operatorname{span}(e_b^v)$.
2. $N_\infty(u)$ is the set of $g \in S_\infty(u)$ such that at each $v$, $(g_v - 1) y \in \operatorname{span}(e_b^v)$ for every $y \in \mathbb{C}^n$ with $h_v(e_a^v, y) = 0$ for all $a$.
3. $H_u$ is the set of $g \in G_\infty$ that fix $e_a^v$, $f_a^v$ and $z_u^v$ at every $v$.

These are the real points of the groups $S$, $N$, $H$ of the [semidirect decomposition](/entry/semi-gen/). In the setting, $n = 2r + 1 + k$, and the complement $W_v$ of the span of $e_a^v, f_a^v, z_u^v$ has a basis of $k$ vectors that is orthonormal for $h_v$. So $h_v$ is positive definite on $W_v$, and $H_u$, a product of copies of the compact group $U(k)$, is compact.

A measure $\mu$ on $G_\infty$ is *Haar on a set* $A \subseteq G_\infty$ if it is $\sigma$-finite, nonzero, $\mu(G_\infty \setminus A) = 0$, and $\mu$ is invariant under left translation by each element of $A$. The setting gives measures $\mu_N(u)$ and $\mu_H(u)$ that are Haar on $N_\infty(u)$ and on $H_u$. Let $\mu_S(u)$ be the image of $\mu_N(u) \times \mu_H(u)$ under $(n, h) \mapsto n h$. The setting also gives a measure $\nu_Q(u)$ on $G_\infty$ with
$$\int_{G_\infty} f\, d\mu_\infty = \int_{G_\infty} \int_{G_\infty} f(s x)\, d\mu_S(u)(s)\, d\nu_Q(u)(x)$$
for each measurable $f \geq 0$. So $\nu_Q(u)$ is a quotient measure on $S_\infty(u) \backslash G_\infty$, lifted to $G_\infty$ ([Folland, §2.6](/learn/analysis/#haar-measure)).

### Invariance of the Haar measures

**Theorem 6.9.2 (Haar measure on the unipotent group).** For every Hermitian setting and every index $u$, the measure $\mu_N(u)$ is finite on compact sets, invariant under right translation by each element of $N_\infty(u)$, invariant under $x \mapsto x^{-1}$, and invariant under conjugation $x \mapsto h x h^{-1}$ by each $h \in H_u$.

Lean: `Formalism.L2.S.Pv.HaarSubS.measN_holds`.

*Proof.* The vectors $e_a$, $f_a$, $z_u$ satisfy the frame relations, with $h(z_u, z_u) = -T_u \neq 0$ since $T_u$ is prime. For any such frame, the four properties hold for every measure that is Haar on $N_\infty$. The reasons are these. The group $N_\infty$ is a connected unipotent real group, so it is nilpotent and unimodular; a left Haar measure on a unimodular group is right invariant and invariant under inversion ([Folland, Chapter 2, §2.4](/learn/analysis/#haar-measure)). Conjugation by $h \in H_u$ is an automorphism of $N_\infty$, so it multiplies the Haar measure by a positive number $\Delta(h)$. The map $h \mapsto \Delta(h)$ is a continuous homomorphism from the compact group $H_u$ to $\mathbb{R}_{>0}$, so $\Delta = 1$. Finiteness on compact sets is part of the Haar property on the locally compact group $N_\infty$. $\square$

**Theorem 6.9.3 (Properties of the flag subgroup at infinity).** For every Hermitian setting and every index $u$:

1. $S = S_\infty(u)$ is a closed subgroup of $G_\infty$, and $\mu_S = \mu_S(u)$ is $\sigma$-finite, nonzero, zero outside $S$, finite on compact sets, invariant under left and under right translation by elements of $S$, and invariant under inversion;
2. $S$ has the *Følner property* for $\mu_S$: for each compact $C \subseteq S$ and each $\epsilon > 0$ there is a measurable $\Omega \subseteq S$ with $0 < \mu_S(\Omega) < \infty$ and
$$\mu_S(\Omega) \leq (1 + \epsilon)\, \mu_S(\{ t \in \Omega : c t \in \Omega \text{ for all } c \in C \});$$
3. the operator $\tau_u(s) = \psi_\infty(s) \pi_u(s)$ satisfies $\tau_u(1) = 1$ and $\tau_u(s t) = \tau_u(s) \tau_u(t)$ for $s, t \in S$, where $\pi_u$ is the representation of $S$ and $\psi_\infty$ the character of the setting;
4. $\nu_Q(u)$ is $s$-finite.

Lean: `Formalism.L2.S.Pv.HaarSubS.stepSubG_holds`.

*Proof.* At each real place, the semidirect decomposition of the last section gives $S = N_\infty \cdot H_u$, where $H_u$ is a compact subgroup that normalizes $N_\infty$ and $N_\infty \cap H_u = 1$. For (1), $\mu_S$ is the image of $\mu_N \times \mu_H$. Left translation by $n' h' \in S$ sends $n h$ to $(n' \cdot h' n h'^{-1}) \cdot h' h$. By the [Haar measure on the unipotent group](/entry/meas-n-holds/), $\mu_N$ is invariant under conjugation by $h'$ and under translations by $N_\infty$, and $\mu_H$ is invariant under $H_u$. So $\mu_S$ is left invariant. Since $H_u$ is compact, $\mu_H$ is finite and bi-invariant. Right invariance and inversion invariance follow in the same way from the right and inversion invariance of $\mu_N$. So $S$ is unimodular and $\mu_S$ is its Haar measure. For (2), one takes for $\Omega$ a product $B \cdot H_u$, where $B$ is a large box in the coordinates of the nilpotent group $N_\infty$; a fixed compact set moves such a box only near its boundary, whose relative measure tends to $0$. For (3), $\pi_u$ is a representation of $S$ and $\psi_\infty$ is a character of $S$, so their product is multiplicative. For (4), $\nu_Q$ is $\sigma$-finite, as a quotient of the $\sigma$-finite measure $\mu_\infty$ by $\mu_S$, and so it is $s$-finite. $\square$

### An energy bound

Now let $G$ be a locally compact Hausdorff second countable group with its Borel sets, and $\mu$ a Haar measure on $G$ that is also right invariant. Let $\mathcal{H}$ be a complex Hilbert space and $V$, $V'$ finite-dimensional complex inner product spaces. Inner products are linear in the second variable. For $v \in V$ and $w \in V'$, $v \otimes w^*$ is the operator $x \mapsto \langle w, x \rangle v$ from $V'$ to $V$. For an operator $A \colon V' \to V$, $\|A\|_{\mathrm{HS}}^2 = \sum_i \|A \beta_i\|^2$ over an orthonormal basis $(\beta_i)$ of $V'$.

**Definition 6.9.4 (Square-integrable representation with formal degree $d$).** A map $\sigma \colon G \to B(\mathcal{H})$ is a *unitary representation* if $\sigma(1) = 1$, $\sigma(x y) = \sigma(x) \sigma(y)$, each $\sigma(x)$ is unitary and $x \mapsto \sigma(x) a$ is continuous for each $a$. It satisfies the *Schur relations with constant $d > 0$* if for all $a, b, a', b' \in \mathcal{H}$ the function $x \mapsto \langle b, \sigma(x) a \rangle \overline{\langle b', \sigma(x) a' \rangle}$ is integrable and
$$\int_G \langle b, \sigma(x) a \rangle\, \overline{\langle b', \sigma(x) a' \rangle}\, d\mu(x) = \frac{\langle a', a \rangle \langle b, b' \rangle}{d}.$$

These are the Schur orthogonality relations of a discrete series representation with formal degree $d$ ([Knapp, Chapter IX](/learn/representations/#discrete-series)).

**Definition 6.9.5 (Data for the bound).** A pair $(S, \mu_S)$ is a *Haar subgroup* if it has the properties of part (1) of the last theorem; the *Følner property* is part (2). A measure $\nu$ is a *quotient* for $\mu$ and $\mu_S$ if $\int_G f\, d\mu = \int_G \int_G f(s x)\, d\mu_S(s)\, d\nu(x)$ for measurable $f \geq 0$. Let $w \in \mathcal{H}$ be a unit vector. A continuous map $W \colon G \to V$ is an *$S$-equivariant vector for $w$*, with an operator valued map $\tau \colon G \to B(V)$, if $\tau(1) = 1$, $\tau$ is multiplicative and unitary on $S$, $W(s x) = \tau(s) W(x)$ for $s \in S$, the reproducing identity
$$\int_G d\, \overline{\langle w, \sigma(y) w \rangle}\, W(x y)\, d\mu(y) = W(x)$$
holds with an integrable integrand for every $x$, $\int \|W\|\, d\nu < \infty$ and $\int \|W\|^2\, d\nu = 1$. For two Haar subgroups $(S, \mu_S)$, $(S', \mu_{S'})$, a measure space $(C, m)$ with a map $\eta \colon C \to G$ is a *double coset disintegration* if
$$\int_G \varphi\, d\mu = \int_C \int_G \int_G \varphi(s\, \eta(c)\, s'^{-1})\, d\mu_{S'}(s')\, d\mu_S(s)\, dm(c)$$
for every measurable $\varphi \geq 0$.

**Theorem 6.9.6 (Energy bound).** Let $\sigma$ be a unitary representation with the Schur relations for $d > 0$, and $w$ a unit vector. Let $(S, \mu_S)$ and $(S', \mu_{S'})$ be Haar subgroups with the Følner property, $\nu$ and $\nu'$ $s$-finite quotient measures, $W \colon G \to V$ and $W' \colon G \to V'$ equivariant vectors for $w$ with respect to $S$ and $S'$, and $(C, m, \eta)$ a double coset disintegration with $\eta$ measurable. Assume:

1. for each $c$, $x \mapsto W(x) \otimes W'(\eta(c)^{-1} x)^*$ is integrable for $\mu$;
2. for each $c$, $\iiiint |\langle \sigma(z) w, \sigma(s \eta(c) s'^{-1}) \sigma(z') w \rangle|\, \|W(z)\|\, \|W'(z')\|\, d\mu_{S'}(s')\, d\mu_S(s)\, d\nu'(z')\, d\nu(z) < \infty$;
3. $\iiint |\langle \sigma(z) w, \sigma(s) \sigma(z') w \rangle|\, \|W(z)\|\, \|W(z')\|\, d\mu_S(s)\, d\nu(z')\, d\nu(z) < \infty$, and the same for $W'$, $S'$, $\nu'$.

Then
$$\int_C \Bigl\| \int_G W(x) \otimes W'(\eta(c)^{-1} x)^*\, d\mu(x) \Bigr\|_{\mathrm{HS}}^2\, dm(c) \leq \frac{1}{d}.$$

Lean: `Formalism.L2.S.Pv.EnergyAbs.energyAbs_holds`.

*Proof.* By the Følner property and second countability, there are measurable sets $\Omega_k \subseteq S$ of finite positive measure such that for each compact $C_0 \subseteq S$, $\mu_S(\{ t \in \Omega_k : C_0 t \subseteq \Omega_k \}) / \mu_S(\Omega_k) \to 1$. Choose $\Omega'_k \subseteq S'$ in the same way. Truncate $W$ along $\Omega_k$: define $Y_k \colon V \to \mathcal{H}$ by
$$Y_k(\beta) = \int_G \int_{\Omega_k} \langle W(s^{-1} z), \beta \rangle\, \sigma(s^{-1} z) w\, d\mu_S(s)\, d\nu(z),$$
and define $Y'_k$ in the same way. For $\gamma \in G$ let $X_k(\gamma) = d\, Y_k^* \sigma(\gamma) Y'_k$, an operator $V' \to V$.

First, for each $c$,
$$\Bigl\| \int_G W(x) \otimes W'(\eta(c)^{-1} x)^*\, d\mu \Bigr\|_{\mathrm{HS}}^2 \leq \liminf_k \frac{1}{\mu_S(\Omega_k) \mu_{S'}(\Omega'_k)} \iint \|X_k(s \eta(c) s'^{-1})\|_{\mathrm{HS}}^2\, d\mu_{S'}(s')\, d\mu_S(s).$$
This uses the reproducing identity, the equivariance of $W$ and $W'$ and the quotient formulas, which express the operator on the left as a limit of averages of $X_k$ over the double translates, and the convexity of $\|\cdot\|_{\mathrm{HS}}^2$; the hypotheses (1) and (2) justify the use of Fubini's theorem. Second, integrate over $c$. By the disintegration, the integral of the right side without the limit is
$$\frac{1}{\mu_S(\Omega_k) \mu_{S'}(\Omega'_k)} \int_G \|X_k(g)\|_{\mathrm{HS}}^2\, d\mu(g) = \frac{d\, \|Y_k\|_{\mathrm{HS}}^2\, \|Y'_k\|_{\mathrm{HS}}^2}{\mu_S(\Omega_k)\, \mu_{S'}(\Omega'_k)},$$
because by the Schur relations $\int_G |\langle Y_k \beta_i, \sigma(g) Y'_k \beta'_j \rangle|^2\, d\mu = \|Y_k \beta_i\|^2 \|Y'_k \beta'_j\|^2 / d$. Third, $\|Y_k\|_{\mathrm{HS}}^2 / \mu_S(\Omega_k) \to 1/d$, and the same for $Y'_k$; this uses the Følner property, the normalization $\int \|W\|^2 d\nu = 1$ and hypothesis (3). So the integrals tend to $d \cdot d^{-1} \cdot d^{-1} = 1/d$. Fatou's lemma, applied to the pointwise bound of the first step, gives the result. $\square$

**Remark 6.9.7 (Formalization).** The first theorem is the general invariance result `PI.n_measure_invariant` applied to the frame of the setting; that result is proved through `measure_contraction_formula`, which we did not open, so the argument given above is the standard one, not a transcript. The frame relation $h(z_u, z_u) \neq 0$ comes from the primality of $T_u$ ([HaarSubSWire.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/TraceIntegralEstimates/HaarSubSWire.lean#L48)), which is more than needed. In the second theorem, the Følner property is `folner_of_haar` through `isFolner_Sinf_gen`, and part (3) is `tauU_one` and `tauU_mul`; we read their statements, not their proofs. The proof of (4) gets $\sigma$-finiteness from `quotient_sigma_finite`, while the statement asks only for $s$-finiteness. The compactness of $H_u$ is part of the decomposition `sDecomp_holds`. The energy bound ([EnergyAbs.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/EnergyAbs.lean#L58)) is abstract: it is a statement about any group with these data, and its many hypotheses are checked where it is used. Of its proof (EnergyAbsMain.lean) we read the main steps, `folner_seq`, `point_lower`, `lintegral_hsA_Xop`, `folner_limit` and `tendsto_energy`, by their statements; the description of the first step is ours.
