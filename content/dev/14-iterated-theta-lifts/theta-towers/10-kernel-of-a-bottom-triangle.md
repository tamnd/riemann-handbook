---
title: The theta kernel of a bottom triangle
decls:
  - GlobalTheory.KerFin.bottomTheta_kernel_finite
  - GlobalTheory.T.theta_parameters_match
  - GlobalTheory.ReadMatch.bottom_layer_parameters_match
  - GlobalTheory.T.standard_module_bottom_datum_exists
  - GlobalTheory.StdRead.standard_module_bottom_datum
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The theta kernel of a bottom triangle

This section proves the kernel identity that [Section 3.8.5](/entry/bottom-theta-kernel-finite-dimensional/) uses for the bottom formula: on finite points, a minor of the theta kernel of a bottom triangle is a fixed constant times a unit times the conjugate term of the bottom pair. The proof has two steps. First, a transform of the Schwartz function of the triangle into the Fock model reads the bottom pair: it is a constant times a unit times the vector of the pair. Second, this reading moves along the action of finite points, so that the theta parameters of the triangle match those of the pair.

We keep the notation of Section 8. We fix the local inputs of [ThetaLocalInputs](/step/theta-local-inputs-def/), the agreement of theta integrals [ThetaIntegralsAgree](/step/theta-integrals-agree-def/) and the [local matching](/step/local-matching-def/). We also fix the record $\mathrm{Inp}(D)$ for every datum $D$ and the small bottom condition. "At large scale" has the meaning of Section 8. A bottom triangle $X$ has a Schwartz function $f_s$ at each index $s$ and a Weil action $\omega_s(y, g)$ of pairs of points. A bottom pair $P$ has a vector $F$ in a space of functions on its lattice, and an action $\mathrm{Om}(x, h)$ of pairs of points on that space.

We say that a complex number $u$ has the unit property at $s$ if $u \neq 0$, $u$ is algebraic, and $|\lambda(u)| = 1$ for every prime $p \nmid Q_n(s)$ and every embedding $\lambda$ of the algebraic numbers into $\mathbb C_p$. If $u$ has the unit property, then so do $\bar u$ and $u^{-1}$, and the product of two numbers with the unit property has it.

**Definition 3.10.1 (Fock transform).** Let $r \neq 0$ be a complex number and $r_c$ a real number. For a function $f$ on the space of the triangle, the Fock transform $\xi_{r, r_c}(f)$ is the function

$$z \mapsto \exp\bigl(\tfrac{\pi}{2} H(z, z)\bigr)\, f\bigl(\mathrm{re}(-\delta^{-1} z)\bigr),$$

where $H$ is the Hermitian form of the triangle, scaled by $r$ and $r_c$, and $\mathrm{re}$ takes the real point. This is a Bargmann transform from the Schrödinger model to the Fock model.

**Theorem 3.10.2 (Reading of the standard module).** At large scale the following holds. Let $W$ be a Weil datum with a standard character, $i$, $j$ indices, and $X$ a bottom triangle at $(i, j)$ with $\beta = 1$. Let $\delta$ and $t_0$ be complex numbers. Let $r \neq 0$ and $r_c$ satisfy $r = -\delta$ when the curve condition at $\delta$ holds, and

$$r_c\, |r|^2 = 2\, |\tau_E(\xi_0)| \quad \text{for every embedding } \tau.$$

Assume that for every index $s$ and bottom pair $(P, P')$ at $s$ the Fock transform of $\bar f_s$ lies in the function space of $P$, and that it moves with the actions: for finite points $g$ over $h$ and $y$ over $x$,

$$\xi_{r, r_c}\bigl(\overline{\omega_s(y, g) f_s}\bigr) = \mathrm{Om}(x, h)\, \xi_{r, r_c}(\bar f_s).$$

Then there is $\kappa \neq 0$ such that for every $s$ and bottom pair $(P, P')$ at $s$ there is $u$ with the unit property at $s$ and

$$\xi_{r, r_c}(\bar f_s) = \kappa\, \bar u\, F.$$

Lean: `GlobalTheory.StdRead.standard_module_bottom_datum` (also `GlobalTheory.T.standard_module_bottom_datum_exists`, a second name).

*Proof.* The thresholds can be $0$. If the curve condition at $\delta$ fails, there is no bottom pair, since every pair satisfies it, and $\kappa = 1$ works. Assume it holds; then $r = -\delta$. The size record gives that the class field of $D$ is the whole field, so the lattice of $D$ at $\delta$ has scale $1$. Compare the relation for $r_c$ at one embedding with the norm of the scale: since the area of the lattice is positive, this gives $r_c = \mathrm{area}^{-1}$. Since $X$ is standard, its lattices are the standard lattices and its characters are trivial at the real places. The conjugate vacuum of $X$ is then a vacuum for the conjugate space. The adelic vacuum on the standard lattices gives a function $G_0 \neq 0$ in the theta space that reads the conjugate vacuum. The record $\mathrm{Inp}(D)$ gives $\kappa \neq 0$ such that each nonzero odd vector $e_0$ at a point of order two that is not killed satisfies $(\kappa u)\, e_0 = G_0$ for a phase $u$. For a bottom pair at $s$ the ranks agree with those of $X$, and its vector $e_0$ is of this kind. The Schrödinger model of the conjugate space gives a function that reads $f_s$. The reading lemma at the standard modulus of the grid gives a second phase $u'$ with the reading of $P$. The transform of the reading is the vector $F$ of $P$, so $\xi(\bar f_s) = \kappa\, \overline{u u'}\, F$, after a change of $u$. The product $\overline{u u'}$ has the unit property. $\square$

**Theorem 3.10.3 (Theta parameters match).** At large scale, for every Weil datum $W$ with a standard character, every bottom triangle $X$ at $(i, j)$ with $\beta = 1$ and all $\delta$, $t_0$, there are $r \neq 0$, a real $r_c$ with the relation of the theorem above, and $\kappa \neq 0$ with this property. For every $s$ and bottom pair $(P, P')$ at $s$ there is $u$ with the unit property at $s$ such that for finite points $g$ over $h$ and $y$ over $x$,

$$\xi_{r, r_c}\bigl(\overline{\omega_s(y, g) f_s}\bigr) = \kappa\, \bar u\, \mathrm{Om}(x, h)\, F.$$

Lean: `GlobalTheory.ReadMatch.bottom_layer_parameters_match` (also `GlobalTheory.T.theta_parameters_match`, a second name).

*Proof.* Take the larger thresholds of two results. The first is an intertwiner on the bottom stratum: it gives $r \neq 0$ and $r_c$ with $r = -\delta$ under the curve condition, the relation for $r_c$, and the two assumptions of [Theorem 3.10.2](/entry/standard-module-bottom-datum/). That theorem then gives $\kappa$ and, for each bottom pair, the number $u$ with $\xi(\bar f_s) = \kappa \bar u F$. By the equivariance,

$$\xi\bigl(\overline{\omega_s(y, g) f_s}\bigr) = \mathrm{Om}(x, h)\bigl(\kappa\, \bar u\, F\bigr).$$

The action $\mathrm{Om}(x, h)$ is linear on the test vectors of $P$, and $F$ is one of them. So it commutes with the scalar $\kappa \bar u$. $\square$

**Theorem 3.10.4 (Kernel of a bottom triangle).** At large scale, for every Weil datum $W$ with a standard character, every bottom triangle $X$ at $(i, j)$ with $\beta = 1$ and all $\delta$, $t_0$, there is $\Omega_0 \neq 0$ with this property. For every $s$, every $Q$, every bottom pair $(P, P')$ at $s$ and every tuple $T$ there is $u$ with the unit property at $s$ such that for finite points $g$ over $h$ and $y$ over $x$,

$$k_s(\varphi_T)(g, y) = \Omega_0\, u\, \overline{P(x, h, T)}.$$

Lean: `GlobalTheory.KerFin.bottomTheta_kernel_finite`.

*Proof.* Take the larger thresholds of [Theorem 3.10.3](/entry/bottom-layer-parameters-match/) and of the constancy of the weights of bottom pairs. Fix $W$, $X$, $\delta$ and $t_0$. The first result gives $r$, $r_c$ and $\kappa \neq 0$. The second gives that the weights of the pairs at $(\delta, t_0)$ are constant. A lemma on the minors of the theta kernel of a bottom triple then gives $\Omega \neq 0$ such that, whenever the transform of $\overline{\omega_s(y, g) f_s}$ is a scalar $c$ times $\mathrm{Om}(x, h) F$, the minor $k_s(\varphi_T)(g, y)$ is $\Omega\, \bar c$ times the conjugate jet of $P$ at $(x, h, T)$. The conjugate jet is $\overline{P(x, h, T)}$. Put $\Omega_0 = \Omega \bar\kappa$, which is not $0$. For a bottom pair at $s$ take the number $u$ of the first result. Then $c = \kappa \bar u$, so

$$k_s(\varphi_T)(g, y) = \Omega\, \bar\kappa\, u\, \overline{P(x, h, T)} = \Omega_0\, u\, \overline{P(x, h, T)}.$$

The scalar passes through the evaluation of the vector at the tuple. $\square$

The theorem is the source of the lemma on the kernel at the bottom in Section 8, which restates it.

**Remark 3.10.5 (Formalization).** The kernel theorem is named for finite dimensionality, but it states a kernel identity and no dimension appears ([BottomThetaKernelFiniteDimensional.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BottomThetaKernelFiniteDimensional.lean#L18)). The reading theorem ([StandardModuleBottomDatumExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/StandardModuleBottomDatumExists.lean#L35)) takes the local inputs, the agreement of theta integrals, the local matching and the small bottom condition, and uses none of them: only $\mathrm{Inp}(D)$ and the size record enter. Its thresholds are $0$. The hypothesis $r \neq 0$ and the equivariance part of the reading hypothesis are not used; only the membership in the theta space is used. When the curve condition fails, the claim is empty. The intertwiner of the bottom stratum and the constancy of weights are inputs we have not opened, and nor are the reading lemma, the adelic vacuum and the minor lemma for bottom triples. The parameter theorem ([BottomLayerParametersMatch.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BottomLayerParametersMatch.lean#L19)) has a second name at line 54.
