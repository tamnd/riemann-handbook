---
title: Base potentials from theta sums
decls:
  - GlobalTheory.ExtraWeight.extra_weight_exists
  - GlobalTheory.ThetaWeight.exists_weight
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Base potentials from theta sums

This section constructs the base potential that [the archimedean datum at a run](/entry/arch-at-of-run/) uses at the indices $j < m$. The base potential is an invariant smooth function on the domain of each component. Its Levi form is bounded below by a multiple of the Levi form of the signature weight, and it decays along the isotropic directions. It gives the extra curvature that the archimedean datum needs at an indefinite index, in the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). The function is the logarithm of a theta sum over a torus attached to each point of the domain.

### The setting

We keep the notation of section 19 for a component $X$ of rank $r$ over the CM field $E$, with signature $p_0$, domain $\Omega$, the weight functions $\varphi_G$ and the Levi forms in the charts. Let $f = [E : \mathbb{Q}]/2$, which is the number $|\Psi|$ of embeddings in the CM type, and let $\mathrm{rd}(E)$ be the root discriminant of $E$. The component holds a lattice $\Lambda \subseteq E^r$, a hermitian matrix $G_m$ and a scalar $\xi_0$, which define the hermitian form $h(u, v)$ and the trace pairing $\operatorname{tr}_{E/\mathbb{Q}}(\xi_0\, h(u, v))$.

The *signature weight* $\varepsilon$ of $X$ has the entry $+1$ at the positions $i \geq p_0$ and $-1$ at the positions $i < p_0$, at each embedding. A vector $\xi \in E^r$ is *isotropic* if it lies in $\Lambda$, is nonzero and has $h(\xi, \xi) = 0$. For an isotropic $\xi$ and a point $x \in \Omega$ there are numbers $t_\tau(\xi, x)$, one for each embedding $\tau$, which measure the height of $x$ in the direction of $\xi$. Let $\lambda_1(x)$ be the first minimum at $x$.

For a constant $a > 0$ a function $\psi$ on $\Omega$ has *cusp decay* $a$ if there are $C, A'$ with

$$\psi(x) \leq C + A' \log\bigl(1 + 1/\lambda_1(x)\bigr) \quad (x \in \Omega),$$

and for each $0 < \eta < 1/2$ there are $C, A'$ such that, for each isotropic $\xi$ and each $x \in \Omega$ with $t_\tau(\xi, x) \geq 1$ at all $\tau$,

$$\psi(x) \leq C + A' \log\bigl(1 + 1/\lambda_1(x)\bigr) - 8 \pi (1 - 2 \eta)\, a\, \min_\tau t_\tau(\xi, x).$$

A *base potential* for $X$ with constant $a$ is a function $\psi_0$ on $\Omega$ with four properties:

1. $\psi_0$ is invariant under the group of $X$;
2. $\psi_0$ is smooth in each chart;
3. in each chart, for each tangent vector $\xi$,

$$- \tfrac{r}{2}\, \mathrm{Levi}(\varphi_\varepsilon)(\xi) \leq \mathrm{Levi}(\psi_0)(\xi);$$

4. $\psi_0$ has cusp decay $a$.

Put

$$a_1(E) = \frac{1}{2 \cdot 5^4\, |\operatorname{disc} E|^{1/f}}.$$

The *torus hypotheses* for $X$ are the following:

1. there is $w_0 \in \mathcal{O}_E$ such that, for all $u, v \in \Lambda$, the difference $\operatorname{tr}(\xi_0\, h(u, (w_0 - \bar{w}_0) v)) - \operatorname{tr}(\xi_0\, h(u, v))$ is an even integer;
2. $f \leq \mathrm{rd}(E)$, $f^2 \leq \mathrm{rd}(E)$ and $16 \leq \mathrm{rd}(E)$;
3. there is $m \geq 1$ with $m^4 \leq f$ and $p_0 \leq m$ or $r - p_0 \leq m$.

### The potential on one component

**Theorem 7.20.1 (Base potential on a component).** Assume the theta bound for the tori. Let $X$ be a component with an isotropic vector, which satisfies the torus hypotheses. Then $X$ has a base potential with constant $a_1(E)$.

Lean: `GlobalTheory.ThetaWeight.exists_weight`.

*Proof.* We take the steps in order.

1. The trace pairing on $\Lambda$ is perfect. With the element $w_0$ of hypothesis 1, this gives at each point $x \in \Omega$ a torus $A_x$: a complex torus with a lattice $L_x$, a basis $b$ and a polarization, on which $\mathcal{O}_E$ acts.
2. For $x \in \Omega$ let $\mathcal{A}_x$ be the set of tuples $a = (a_1, \ldots, a_r)$ of points in the fundamental domain of $b$ such that $25\, a_i \in L_x$ for each $i$ and every point of $L_x$ is $\sum_i c_i \cdot 25\, a_i + 5 y$ for some $c_i \in \mathcal{O}_E$ and $y \in L_x$. Put

$$\psi_0(x) = \log \sum_{a \in \mathcal{A}_x} \prod_{i} \frac{N_2(a_i)}{\ell_2},$$

where $N_2$ is the squared norm of the theta function of the torus at a point and $\ell_2$ is its mean square. Put $\psi_0(x) = 0$ outside $\Omega$.
3. The sum is positive, so $\psi_0$ is defined. The theorem on the log theta sum gives that $\psi_0$ is invariant and smooth in each chart. The theorem on its Levi form gives property 3.
4. The theta bound for the tori, with hypotheses 2 and 3, gives the growth and the decay of the theta sum: there are $C, A'$ with the first bound of cusp decay, and with

$$\psi_0(x) \leq C + A' \log\bigl(1 + 1/\lambda_1(x)\bigr) - 8 \pi\, a_1(E) \min_\tau t_\tau(\xi, x)$$

in the isotropic region, for every $\eta$.
5. In the isotropic region $\min_\tau t_\tau(\xi, x) \geq 1 > 0$. Since $\pi$, $\eta$ and $a_1(E)$ are positive, $8 \pi (1 - 2\eta)\, a_1(E) \min_\tau t_\tau \leq 8 \pi\, a_1(E) \min_\tau t_\tau$. So the bound of step 4 gives the second bound of cusp decay.

This proves the theorem. $\square$

The proof does not choose the torus in a continuous way. The value $\psi_0(x)$ does not depend on the torus at $x$, and the theorem on the log theta sum uses this.

### The potential at a run

**Theorem 7.20.2 (Extra weight at a run).** Let $T$ be a record with the laws whose core has the theta values, and let $j$ be an index in range with $j < m$. Let $L$ be size data with $2 \leq L$ and $w$ a weight with the sup bound of the page rows and $r \leq n(w)$. Assume

$$f^2 \leq \mathrm{rd}(E), \qquad 16 \leq \mathrm{rd}(E), \qquad m^4 \leq f,$$

for the host field $E$ of $D$. Then each component of $X_j$ at the base embedding has a base potential with constant $a_1(E)$.

Lean: `GlobalTheory.ExtraWeight.extra_weight_exists`.

*Proof.* We take the steps in order.

1. The bounds for the cusp data at the base embedding give, for each component $k$, a component $X_k$ over $E$ with the lattice, form and scalar of the record. This uses the theta values of the core, the sup bound, $2 \leq L$ and $r \leq n(w)$.
2. The degree of $E$ is $2f$. The CM type of $X_k$ has half the embeddings, so $|\Psi| = f$.
3. The laws give the signature $p_0 = m - j$ of $X_k$. Since $j < m$, the number $\rho_j = m - j$ is positive.
4. The core gives a cusp datum of $X_k$ at $\rho_j$. Its first vector has a nonzero multiple $c \cdot e_1$ in $\Lambda$, with $c \in \mathcal{O}_E$. This multiple is isotropic, since $h(c e_1, c e_1) = c \bar{c}\, h(e_1, e_1) = 0$.
5. The host field holds the half integral generator $w_0$. Its conjugate is $\bar{w}_0 = 1 - w_0$. This gives hypothesis 1 of the torus hypotheses, by the evenness of the imaginary part of the hermitian form.
6. From $f \geq 1$ and $f^2 \leq \mathrm{rd}(E)$ we get $f \leq \mathrm{rd}(E)$. Take $m$ itself in hypothesis 3: $m \geq 1$, $m^4 \leq f$ and $p_0 = m - j \leq m$.
7. [The base potential on a component](/entry/exists-weight/), with the theta bound for the tori, gives the claim at $X_k$.

This proves the theorem. $\square$

The constant $a_1(E)$ depends only on the host field. The hypotheses on $L$ and $w$ are only used to name the components in step 1. At the definite index $j = m$ there is no isotropic vector, and the archimedean datum does not need a base potential there.

**Remark 7.20.3 (Formalization).** The theorem `extra_weight_exists` is at line 53 of [ConjCmHalfIntegralGeneratorEqOneSub.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/ConjCmHalfIntegralGeneratorEqOneSub.lean#L53). It keeps only the components `e` of `cusp_data_bounds` and drops the rest by the pattern `⟨e, -⟩`. The isotropic vector is `exists_isIso` at line 36, and the conjugate of the generator is `conj_cmHalfIntegralGenerator_eq_one_sub` at line 42, a renaming of `CMConjugationOfSquareRoot.main`. The theorem `exists_weight` is at line 32 of [NonemptyTorusAt.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/NonemptyTorusAt.lean#L32). It takes the theta bound as a hypothesis `TStatement`, and the caller supplies `theta_bound_tStatement`. It builds $\psi_0$ by `choose` with the value $0$ off the domain, and the set of tuples is written out twice in the proof; the same set is `TTset` at line 107 of [InterpolationModelInequalities.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovVolumes/UpperBounds/InterpolationModelInequalities.lean#L107). The goal `BasePotentialExistence` is at line 20 of that file, the signature weight `de2W` at line 91, and the torus hypotheses `TorusHyp` at line 93. The cusp decay `cfwM` is at line 20 of [BasePsiLeviLowerBound.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovVolumes/UpperBounds/BasePsiLeviLowerBound.lean#L20). The hypothesis $f \leq \mathrm{rd}(E)$ of `TorusHyp` follows from $f^2 \leq \mathrm{rd}(E)$, and the proof gets it by `nlinarith`. The theta bound gives the decay with the factor $1$, and the proof weakens it to $1 - 2\eta$ by `linarith`.
