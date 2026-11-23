---
title: Finite volume and the theta transformation formula
decls:
  - GlobalTheory.CompanionTheory.SW.finVol_unitaryGroup
  - GlobalTheory.T.theta_function_automorphy
  - GlobalTheory.CompanionTheory.SW.ThW.thetaInvariance
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finite volume and the theta transformation formula

This section sets up the unitary groups of the rest of the chapter and proves two analytic facts about them. The first is that the automorphic quotient of a unitary group has finite volume. The second is the transformation formula of a theta series under $\tau \mapsto -1/\tau$, proved by Poisson summation. Both serve the step [EveryCharacter](/step/every-character/) of the proof, through the Siegel-Weil formula: the finite volume makes the average of a theta function over the quotient a finite number, and the transformation formula is the automorphy of the theta kernel.

### Unitary groups over a CM extension

**Definition 1.8.1 (CM extension).** A *CM extension* is a pair of number fields $F \subseteq E$ with an automorphism $\sigma$ of $E$ over $F$ such that $F$ is totally real, $E$ is totally complex, $[E : F] = 2$, and $\tau(\sigma x) = \overline{\tau(x)}$ for every embedding $\tau \colon E \to \mathbb{C}$ and every $x \in E$.

Lean: `HeckeCharacterZeroLocus.SiegelWeilU.IsCMExt`.

So $\sigma$ is the nontrivial automorphism of $E/F$, and it is complex conjugation under every embedding ([kinds of number fields](/learn/number-fields/#kinds-of-number-fields)).

**Definition 1.8.2 (Hermitian matrix).** Let $M \geq 0$. A matrix $J \in M_M(E)$ is *nondegenerate Hermitian* if $\sigma(J_{ji}) = J_{ij}$ for all $i, j$ and $\det J \neq 0$. Its *Hermitian form* is $h(x, y) = \sigma(x)^{\mathsf T} J y$ for $x, y \in E^M$.

Lean: `HeckeCharacterZeroLocus.SiegelWeilU.IsHermND`.

The form $h$ is $\sigma$-linear in $x$, linear in $y$, and $h(y, x) = \sigma(h(x, y))$ ([Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms)). For a commutative $F$-algebra $R$, let $R_E = R \otimes_F E$ and extend $\sigma$, $J$ and $h$ to $R_E$.

**Definition 1.8.3 (Unitary group).** For a commutative $F$-algebra $R$, the *unitary group* of $J$ over $R$ is
$$U_J(R) = \{ g \in \mathrm{GL}_M(R_E) : \sigma(g)^{\mathsf T} J g = J \}.$$
The *rational subgroup* $U_J(F) \subseteq U_J(R)$ is the image of the group $U_J(F)$ of matrices over $E$.

Lean: `HeckeCharacterZeroLocus.SiegelWeilU.HR` (also `HeckeCharacterZeroLocus.SiegelWeilU.HFinIn`).

We use $R = \mathbb{A}_F$, the [[adele ring|NYJFYZ0B4M]] of $F$ ([adeles](/learn/number-fields/#adeles-and-ideles)), and write $\mathbb{A}_E = \mathbb{A}_F \otimes_F E$. The ring $\mathbb{A}_E$ has the topology of a finite free $\mathbb{A}_F$-module, $\mathrm{GL}_M(\mathbb{A}_E)$ the topology for which $g \mapsto (g, g^{-1})$ is an embedding into $M_M(\mathbb{A}_E)^2$, and $U_J(\mathbb{A}_F)$ the subspace topology. It is a locally compact group ([unitary groups](/learn/groups/#unitary-groups)), so it has a [Haar measure](/learn/analysis/#haar-measure).

**Definition 1.8.4 (Fundamental domain).** Let $\mu$ be a Haar measure on $U_J(\mathbb{A}_F)$. A *fundamental domain* for $U_J(F)$ is a measurable set $\mathcal{F} \subseteq U_J(\mathbb{A}_F)$ such that the translates $\gamma \mathcal{F}$, $\gamma \in U_J(F)$, cover $U_J(\mathbb{A}_F)$ up to a null set and meet pairwise in null sets.

Lean: `HeckeCharacterZeroLocus.SiegelWeilU.IsFDH`.

**Definition 1.8.5 (Finite volume).** We say that $U_J$ has *finite volume* if a Haar measure exists on $U_J(\mathbb{A}_F)$, if for each Haar measure $\mu$ a fundamental domain exists, and if $\mu(\mathcal{F}) < \infty$ for each Haar measure $\mu$ and each fundamental domain $\mathcal{F}$ for $\mu$.

Lean: `HeckeCharacterZeroLocus.SiegelWeilU.FinVol`.

Two fundamental domains for the same $\mu$ have the same measure, so the last condition is the finiteness of the volume of $U_J(F) \backslash U_J(\mathbb{A}_F)$ ([quotients of finite volume](/learn/groups/#quotients-of-finite-volume)).

**Theorem 1.8.6 (Finite volume of unitary groups).** Let $(F, E, \sigma)$ be a CM extension, $M \geq 0$, and $J \in M_M(E)$ nondegenerate Hermitian. Then $U_J$ has finite volume.

Lean: `GlobalTheory.CompanionTheory.SW.finVol_unitaryGroup`.

*Proof.* This is the [Theorem 6.9.5 of Volume 7](/entry/fin-vol/) of Volume 7 on the finite volume of unitary groups, applied to $(F, E, \sigma)$ and $J$. $\square$

**Remark 1.8.7.** The classical theorem is due to Borel and Harish-Chandra: for a reductive group $G$ over a number field $F$ with no nontrivial character defined over $F$, the quotient $G(F) \backslash G(\mathbb{A}_F)$ has finite volume. A unitary group $U_J$ is reductive, and its characters over $F$ factor through the determinant, whose image is the anisotropic torus of norm one elements of $E$; so it has no nontrivial character over $F$. Here the result is proved directly for $U_J$.

### Theta series of a quadratic form

Let $F$ be totally real, $\mathbb{A}_{F,f}$ its ring of finite adeles, and $\widehat{\mathcal{O}} = \prod_v \mathcal{O}_v \subseteq \mathbb{A}_{F,f}$. For each infinite place $w$ of $F$ let $\rho_w \colon F \to \mathbb{R}$ be the real embedding at $w$. Let $\iota$ be a finite set and $V = \mathbb{A}_{F,f}^\iota$.

**Definition 1.8.8 (Schwartz-Bruhat function).** A function $\varphi \colon V \to \mathbb{C}$ is *Schwartz-Bruhat* if it is locally constant and has compact support.

Lean: `GlobalTheory.CompanionTheory.SW.Core.SB`.

For $N \geq 1$ let $L_N = N \widehat{\mathcal{O}}^\iota$, an open compact subgroup of $V$. For $a \in F^\iota$ the indicator $\mathbf{1}_{a + L_N}$ is Schwartz-Bruhat, and every Schwartz-Bruhat function is a finite linear combination of such indicators for one $N$.

**Definition 1.8.9 (Quadratic datum).** A *quadratic datum* of size $2M$ is a symmetric matrix $B \in M_\iota(F)$ with $|\iota| = 2M$ and $\det B \neq 0$, together with, for each infinite place $w$, a positive definite matrix $P_w \in M_\iota(\mathbb{R})$ with
$$P_w\, (B^{\rho_w})^{-1}\, P_w = B^{\rho_w}.$$

Lean: `GlobalTheory.CompanionTheory.SW.Core.QSetup`.

The condition says that $P_w$ is a majorant of the real quadratic form $B^{\rho_w}$: in a basis where $B^{\rho_w} = \mathrm{diag}(1_p, -1_q)$ one can take $P_w = 1$.

Fix an additive Haar measure $\lambda$ on $\mathbb{A}_{F,f}$ with $\lambda(\widehat{\mathcal{O}}) = 1$ and a continuous additive character $\psi$ of $\mathbb{A}_{F,f}$ with $\psi(b) = \exp(-2\pi i \operatorname{Tr}_{F/\mathbb{Q}} b)$ for $b \in F$ ([additive characters](/learn/class-field-theory/#additive-characters)). Let $d_F$ be the discriminant of $F$. Put
$$\mu_B = |d_F|^{-|\iota|/2}\, |N_{F/\mathbb{Q}}(\det B)|^{-1/2}\, \lambda^\iota,$$
and define the Fourier transform of $\varphi$ by $\widehat{\varphi}(y) = \int_V \varphi(x)\, \psi(x^{\mathsf T} B y)\, d\mu_B(x)$.

For $\tau = (\tau_w)$ with $\operatorname{Im} \tau_w > 0$ and $x = (x_w) \in (\mathbb{R}^\iota)^{\{w\}}$, the *Gaussian* is
$$G_\tau(x) = \exp \sum_w \bigl( \pi i\, \operatorname{Re}(\tau_w)\, x_w^{\mathsf T} B^{\rho_w} x_w - \pi \operatorname{Im}(\tau_w)\, x_w^{\mathsf T} P_w x_w \bigr),$$
and $c(\tau) = |N_{F/\mathbb{Q}}(\det B)|^{1/2} \int G_\tau(x)\, dx$, with Lebesgue measure.

**Definition 1.8.10 (Theta series).** Let $g_f \in M_\iota(\mathbb{A}_{F,f})$ and $g_\infty = (g_w)_w$ with $g_w \in M_\iota(\mathbb{R})$. For $\varphi$ Schwartz-Bruhat the *theta series* is
$$\theta(g_f, g_\infty; \varphi)(\tau) = \sum_{x \in F^\iota} \varphi(g_f x)\, G_\tau\bigl( (g_w \rho_w(x))_w \bigr).$$

Lean: `GlobalTheory.CompanionTheory.SW.Core.theta`.

We say that $(g_f, g_\infty)$ is *orthogonal* if $g_f^{\mathsf T} B g_f = B$ and $g_w^{\mathsf T} B^{\rho_w} g_w = B^{\rho_w}$ for every $w$.

**Theorem 1.8.11 (Theta transformation formula).** Let $F$ be a totally real number field, $\lambda$ and $\psi$ as above, $(B, P)$ a quadratic datum of size $2M$, $(g_f, g_\infty)$ orthogonal, $\varphi$ Schwartz-Bruhat on $\mathbb{A}_{F,f}^\iota$, and $\tau = (\tau_w)$ with $\operatorname{Im} \tau_w > 0$ for every $w$. Then
$$c(\tau)\, \theta(g_f, g_\infty; \widehat{\varphi})(-1/\tau) = \theta(g_f, g_\infty; \varphi)(\tau),$$
where $-1/\tau = (-1/\tau_w)_w$.

Lean: `GlobalTheory.T.theta_function_automorphy` (also `GlobalTheory.CompanionTheory.SW.ThW.thetaInvariance`).

For one variable, $F = \mathbb{Q}$, $B = 1$ and $\varphi = \mathbf{1}_{\widehat{\mathbb{Z}}}$, the series is $\sum_n e^{\pi i \tau n^2}$, the Fourier transform is $\varphi$ again, and $c(\tau) = (-i\tau)^{-1/2}$; the formula is Jacobi's $\theta(-1/\tau) = (-i\tau)^{1/2}\theta(\tau)$. Here $|\iota|$ is even, so this case is only an illustration.

*Proof.* We use the following facts, proved in another part of the development. The measure $\mu_B$ is self-dual for the pairing $\psi(x^{\mathsf T} B y)$: for each open compact subgroup $L$ of $V$, the annihilator $L^\perp$ is open and compact and $\mu_B(L)\, \mu_B(L^\perp) = 1$. The Fourier transform maps Schwartz-Bruhat functions to Schwartz-Bruhat functions. The theta series converges absolutely.

First we reduce to $g_f = 1$ and $g_w = 1$. Taking determinants in $g_f^{\mathsf T} B g_f = B$ gives $(\det g_f)^2 = 1$, so $g_f$ is invertible. The Fourier transform commutes with an invertible $g_f$ that preserves $B$: $\widehat{\varphi \circ g_f} = \widehat{\varphi} \circ g_f$, since $\mu_B$ is invariant under $g_f$. At the infinite places, $(B, g_w^{\mathsf T} P_w g_w)$ is again a quadratic datum, $G_\tau(g_\infty x)$ is the Gaussian of the new datum, and $c(\tau)$ does not change, by the change of variables $x \mapsto g_\infty x$, whose determinant is $\pm 1$. So the formula for $(g_f, g_\infty; \varphi)$ is the formula for $(1, 1; \varphi \circ g_f)$ with the new datum.

Now let $g_f = 1$ and $g_w = 1$. Both sides are linear in $\varphi$, so it suffices to take $\varphi = \mathbf{1}_{a + L_N}$ with $a \in F^\iota$ and $N \geq 1$. Choose an integral basis of $F$. The set of $x \in F^\iota$ with $x \in a + L_N$ is $a + N\mathcal{O}_F^\iota$, and under $x \mapsto (\rho_w(x))_w$ it is the coset $\rho(a) + g\mathbb{Z}^{\iota \times \{w\}}$ of a lattice in $\mathbb{R}^{\iota \times \{w\}}$ with $|\det g| = (N^{[F:\mathbb{Q}]} |d_F|^{1/2})^{|\iota|}$. So the right side is a sum of the Gaussian over a lattice coset.

The Fourier transform of $\mathbf{1}_{a + L_N}$ is $\mu_B(L_N)\, \psi(a^{\mathsf T} B y)\, \mathbf{1}_{L_N^\perp}(y)$. A vector $y \in F^\iota$ lies in $L_N^\perp$ if and only if $\operatorname{Tr}_{F/\mathbb{Q}}(x^{\mathsf T} B y) \in \mathbb{Z}$ for all $x \in N\mathcal{O}_F^\iota$, and these $y$ form, under $\rho$, the dual lattice $B^{-1}(g^{-1})^{\mathsf T} \mathbb{Z}^{\iota \times \{w\}}$. For $y$ in it, $\psi(a^{\mathsf T} B y) = \exp(-2\pi i \operatorname{Tr}(a^{\mathsf T} B y))$. So the left side is $c(\tau)\, \mu_B(L_N)$ times a sum, over the dual lattice, of $G_{-1/\tau}$ twisted by these characters.

The Poisson summation formula for the Gaussian $G_\tau$ on the lattice $g\mathbb{Z}^{\iota \times \{w\}}$ (J. Tate, "Fourier analysis in number fields and Hecke's zeta-functions", in Cassels and Fröhlich, *Algebraic Number Theory*, Chapter XV) turns the sum over the coset $\rho(a) + g\mathbb{Z}$ into $|\det g|^{-1}$ times the sum of the Fourier transform of $G_\tau$ over the dual lattice, with the character of $\rho(a)$. For the pairing $(x, y) \mapsto e^{2\pi i\, x^{\mathsf T} D_B y}$, where $D_B$ is a real matrix built from the $B^{\rho_w}$ (we do not unfold its definition), the Fourier transform of $G_\tau$ is $|N_{F/\mathbb{Q}}(\det B)|^{-1/2}\, c(\tau)\, G_{-1/\tau}$; this formula holds for every quadratic datum. Last, $\mu_B(L_N) = |d_F|^{-|\iota|/2} |N(\det B)|^{-1/2} N^{-[F:\mathbb{Q}]|\iota|}$, since $\lambda(N\widehat{\mathcal{O}}) = N^{-[F:\mathbb{Q}]}$. Comparing constants gives the formula for $\mathbf{1}_{a + L_N}$. $\square$

**Remark 1.8.12 (Classical form).** The classical theorem is the transformation formula of the Siegel theta series of an indefinite quadratic form with a majorant (C. L. Siegel, "Indefinite quadratische Formen und Funktionentheorie I", *Math. Ann.* 124 (1951)), and its adelic form is the invariance of the theta distribution under the Weil representation of $\mathrm{SL}_2$ (A. Weil, "Sur certains groupes d'opérateurs unitaires", *Acta Math.* 111 (1964)). The form here differs in three points. The finite part is a Schwartz-Bruhat function on finite adeles, and the infinite part is the fixed Gaussian of the majorant $P$. The automorphy factor is the integral $c(\tau)$, not its closed form as a product of powers of $\tau_w$. The number of variables is even.

**Remark 1.8.13 (Formalization).** The theorem on finite volume in [UnitaryGroupFiniteVolume.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/UnitaryGroupFiniteVolume.lean#L8) is a one line call to `CompanionTheory.SWFin.finVol`; we have not opened its proof. In the transformation formula the sum over $F^\iota$ is a sum in the sense of `tsum`, which is $0$ for a series that does not converge; the absolute convergence is the input `GlobalTheory.T.theta_series_summable`. The self-duality is `GlobalTheory.T.weil_representation_quadratic_datum`, the invariance under $g_f$ is `GlobalTheory.T.weil_orthogonal_group_invariance`, and the Poisson formula is `GlobalTheory.T.poisson_summation_gaussian`; we have opened their uses in [ThetaFunctionAutomorphy.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/ThetaFunctionAutomorphy.lean#L285), not their proofs. The integer $M$ enters only through $|\iota| = 2M$. The wrapper `GlobalTheory.T.theta_function_automorphy` restates `GlobalTheory.CompanionTheory.SW.ThW.thetaInvariance` without change.
