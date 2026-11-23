---
title: The orbit constant at the archimedean places
decls:
  - PI.AprimeInfAsm.aprimeInf_of_good
  - PI.AprimeInfAsm.aprimeInf_of_std
  - PI.AprimeInfAsm.aprimeInf_of_grp
  - Formalism.L2.SG.Closed.AprimeInf_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The orbit constant at the archimedean places

Let $G_\infty$ act on frames of $2r + 1$ vectors in a Hermitian space. The Haar measure of $G_\infty$ disintegrates over the orbit of a frame: it is a constant $a'$ times the product of a measure on the orbit, read off from the Gram matrix, and the Haar measure of the stabilizer. This section computes $a'$. The answer is
$$a' = \frac{\gamma \, V_k^{d} \, T_{u'}^{-kd}}{\mu_{H}(H_\infty)},$$
with the gauge constant $\gamma$ and the volume $V_k$ of [the previous section](/entry/grp-std-full/). We first reduce the computation to three statements about charts, then discharge them. The result feeds the [orbit constant on the compact real stabilizer](/entry/aprime-inf-of-hinf-compact/) and, through the [real bracket](/entry/real-bracket-holds/), the [theta local matching](/step/theta-local-matching/).

### The setting at infinity

Let $E$ be a CM field with totally real subfield $F$, and let $d$ be the number of infinite places of $F$. Let $V$ be a Hermitian space over $E$ of dimension $n = 2r + k + 1$ with $k \geq 1$, and at each infinite place $v$ let $\varepsilon_v$ be its sign vector, so that $G_\infty = \prod_v \mathrm{U}(J_{\varepsilon_v})$ with a fixed Haar measure $\mu_G$. To a word $u'$ the setting attaches a frame $Y_0 = Y_0(u')$ of $2r + 1$ vectors, with a vector $z_{u'}$ of norm $h(z_{u'}, z_{u'}) = -T_{u'}$, $T_{u'} > 0$. Let $T = (h(y_i, y_j))_{i,j}$ be the Gram matrix of the frame; it is a Hermitian matrix. Let $H_\infty$ be the stabilizer of $Y_0$ in $G_\infty$, with a Haar measure $\mu_H$.

Let $\psi$ be an [additive character](/learn/class-field-theory/#additive-characters) of $\mathbb{A}_F / F$. On the space of tuples of $2r + 1$ vectors of $V \otimes F_\infty$ and on the space of Hermitian matrices of size $2r + 1$ we use measures $\mu_{\mathrm{tup}}$ and $\nu$ that are self-dual for the character $\psi_\infty$. A *fibre family* is a family $(\mathrm{fib}_S)_S$ of measures on tuples, indexed by Hermitian matrices $S$, such that $\mathrm{fib}_S$ lives on the tuples of Gram matrix $S$, and
$$\int \varphi \, d\mu_{\mathrm{tup}} = \int \int \varphi \, d\mathrm{fib}_S \, d\nu(S)$$
for all measurable $\varphi \geq 0$ on the linearly independent tuples, with a continuity condition in $S$ for compactly supported continuous $\varphi$.

**Definition 5.2.1 (Orbit constant).** A real number $a' > 0$ is an *orbit constant* for $u'$ if, for every choice of self-dual measures $\mu_{\mathrm{tup}}, \nu$ and fibre family, for every measurable $f \geq 0$ on $G_\infty$, and for every section $s$ of the orbit map (a map with $s(y) Y_0 = y$ for every $y$ in the orbit $G_\infty Y_0$),
$$\int_{G_\infty} f \, d\mu_G = a' \int \int_{H_\infty} f(s(y) h) \, d\mu_H(h) \, d\mathrm{fib}_T(y).$$

Lean: `Formalism.L2.SG.Pf.NcReal.AinfClause`.

The orbit constant compares two normalizations of the same measure on $G_\infty / H_\infty$, which the orbit map identifies with the orbit of $Y_0$ ([homogeneous spaces](/learn/analysis/#haar-measure)). It does not depend on the section $s$, since $\mu_H$ is invariant.

**Theorem 5.2.2 (Orbit constant at infinity).** Let the setting be as above, with the standing hypotheses of the setting on the fundamental domains and measures, a measure compatible with $\psi$, and $\psi$ standard. Assume that the gauge density exists at every infinite place. If $a' > 0$ is an orbit constant for $u'$, then
$$a' = \frac{\gamma \, V_k^{d} \, T_{u'}^{-kd}}{\mu_H(H_\infty)}.$$

Lean: `Formalism.L2.SG.Pf.NcReal.AprimeInf`.

Here $\gamma = \prod_v \gamma_{\varepsilon_v}$. The numerator is the limit of the [tube volume](/entry/grp-std-full/) theorem, and the factor $T_{u'}^{-kd}$ is the Jacobian of the frame chart below, at $d$ places.

### The reduction to charts

The proof of the theorem goes through a chart of the orbit near $Y_0$: a neighbourhood $\Omega$ of $T$ in the Hermitian matrices and a continuous map $a$ from $\Omega$ to the invertible matrices of size $2r + 1$, with $a(T) = 1$, such that the frame $Y_0 a(S)$ has Gram matrix $S$ for every $S \in \Omega$. A *good chart* is a chart for which the Jacobian of the map $(g, S) \mapsto g Y_0 a(S)$ has the value that matches the tube volume.

We take three inputs. The first is compactness: for every word $u$, the stabilizer $H_\infty$ of the frame of $u$ is compact. This holds since the orthogonal complement of the frame is positive definite at each place.

**Proposition 5.2.3 (Orbit constant from good charts).** Assume that the stabilizers $H_\infty$ are compact, and that a good chart exists for every $u'$ under the standing hypotheses on the measures. Then the orbit constant theorem holds.

Lean: `PI.AprimeInfAsm.aprimeInf_of_good`.

*Proof.* Since $H_\infty$ is compact, the orbit $G_\infty Y_0$ is closed, the orbit map is proper, and the pushforward of $\mu_G$ to the orbit is a Radon measure. The orbit is unique in its fibre: two frames with the same Gram matrix $T$ in the same orbit differ by an element of $G_\infty$ (Witt's theorem for the archimedean Hermitian spaces). So the integral of $f$ over $G_\infty$ is $a''$ times the integral over the orbit of the fibre integrals over $H_\infty$, for a constant $a''$; this is the polar decomposition of $\mu_G$ along the orbit. The good chart gives the Jacobian of $(g, S) \mapsto g Y_0 a(S)$ at $(1, T)$ as $1$ for the self-dual normalizations, so the constant $a''$ is computed from the tube volume and the Weil formula for the total mass: $a'' \mu_H(H_\infty)$ is the limit of $\mu_G$ of a small tube divided by the fibre measure of the matching set of frames. Comparing with the defining identity of the orbit constant gives $a' = a''$, and the value follows. $\square$

A good chart is built from two limits. The first is the tube volume of the previous section, for the standard conjugate $c^{-1} H_\infty c$ of the stabilizer.

**Proposition 5.2.4 (Orbit constant from standard tubes).** Assume that the stabilizers $H_\infty$ are compact, that the [tube volume](/entry/grp-std-full/) theorem holds in the form of the previous section, and that for every $u'$ there is a chart $(\Omega, a)$ for which the measure of the frames $Y_0 a(S)$, $S$ near $T$, has the limit $c_{\mathrm{tup}} |\det \Psi'| / c_\nu = T_{u'}^{kd}$ (the tuple limit). Then the orbit constant theorem holds.

Lean: `PI.AprimeInfAsm.aprimeInf_of_std`.

*Proof.* A good chart is built from the two limits. The frames of the orbit near $Y_0$ are linearly independent, and their orthogonal complement is positive definite, so Witt's theorem applies near $Y_0$ uniformly. The tube volume gives the measure of $\kappa(B_\rho) H_\infty$, the tuple limit gives the measure of the corresponding set of frames, and their quotient is the Jacobian of the chart. So a good chart exists, and the result is the [proposition on good charts](/entry/aprime-inf-of-good/). $\square$

The tuple limit itself reduces to linear algebra at each place. A measure bridge identifies the space of Hermitian matrices of size $2r + 1$ at the infinite places with a Euclidean space, by an isometry for the Frobenius norm that is additive and onto. A Jacobian identity at each place computes the determinant of a linear map built from a matrix $w$ of size $n \times m$ with $w^* J_\varepsilon w$ invertible and with zero rows on a set $S$ of $n - m$ indices, an isometry $c$ of $J_\varepsilon$, and isometric parametrizations of the Lie algebra and of the Hermitian matrices of size $m$.

**Proposition 5.2.5 (Orbit constant from the group limit).** Assume that the stabilizers $H_\infty$ are compact, that the tube volume theorem holds, that the measure bridge for Hermitian matrices exists, and that the Jacobian identity holds at every place. Then the orbit constant theorem holds.

Lean: `PI.AprimeInfAsm.aprimeInf_of_grp`.

*Proof.* The measure bridge and the Jacobian identity give the determinant of the differential of the frame chart in self-dual coordinates, and with the smoothness of the chart this gives the tuple limit. Then the result is the [proposition on standard tubes](/entry/aprime-inf-of-std/). $\square$

### The unconditional form

**Theorem 5.2.6 (Orbit constant, closed form).** Assume the volume formula $\mu^{\mathrm{g}}(\mathrm{U}(k)) = V_k$ for all $k$. Then the orbit constant theorem holds.

Lean: `Formalism.L2.SG.Closed.AprimeInf_holds`.

*Proof.* The stabilizers are compact, and the volume formula with the [product chart](/entry/exp-prod-u-holds/) gives the [tube volume](/entry/grp-std-full/). The measure bridge holds, and the Jacobian identity holds at every place. So this is the [proposition on the group limit](/entry/aprime-inf-of-grp/) applied to these inputs, in the form of the [orbit constant for a compact stabilizer](/entry/aprime-infinite-real/). $\square$

**Remark 5.2.7 (Formalization).** The reductions are in [Assembly.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/Assembly.lean#L31). The proof of the closed form is `aprime_infinite_real hinfCompact_holds hG.out`, and the volume formula enters as an instance argument `[Fact GaugeVolUD]`. That instance is `factGaugeVol`, proved as `GV.gaugeVolU`, so the volume of $\mathrm{U}(k)$ is proved, not assumed, at the top of the proof. The variant `aprimeInf_of_open` ([Assembly.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ArchimedeanOrbitMeasures/Assembly.lean#L55)) takes the value of the Cayley density at $0$ as a hypothesis, although `cayValId_holds` proves it. The statement asks that the gauge density exists at each place; this is proved as `gauge_density_exists`. The definitions of a good chart (`GoodP`), the tuple limit (`TupStd`), the measure bridge (`NuBridge`) and the Jacobian identity (`PlaceJacAll`) are only sketched above; we did not unfold `GoodP` or the standing hypotheses `HypX` and `MeasCompatψ`.
