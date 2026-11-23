---
title: Convolution integrals and amplitudes at the real place
decls:
  - Formalism.L2.SG.RealObj.EnergyConvJ.BM.stepConvG_holds
  - Formalism.L2.SG.RealObj.EnergyConvJ.BM.stepConvG_jsz
  - Formalism.L2.SG.RealObj.EnergyConvJ.BM.realObj_inInfinityX_jsz
  - Formalism.L2.S.Pv.AmpOrbCoef.BM.ampUnif_gap
  - CompanionTheory.Lime.BM.ampUnif
  - CompanionTheory.Lime.BM.ampUnif_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Convolution integrals and amplitudes at the real place

This section draws two consequences of the uniqueness of Bessel maps, [Theorem 6.2.7](/entry/bessel-map-uniq-gap/), for the global argument. The first is the convergence of the convolution integrals of matrix coefficients against local Bessel weights at the infinite places, and with it the bound at infinity of the off-diagonal energy integral. The second is a uniform bound of the amplitudes of the relative trace formula by orbital integrals of $K$-finite matrix coefficients. Both are inputs of [HypsAlt is nonempty](/step/nonempty-hyps/). The relative trace formula and its orbital integrals are described in [orbit integrals and the relative trace formula](/learn/periods/#orbit-integrals-and-the-relative-trace-formula).

The global objects of this section are large, and we describe them only as far as the statements need. A *global datum* $D$ fixes a CM extension $E/F$, the integers $k$ and $r$, a family of discrete series parameters at the real places, and a finite set of index data. A *setting* $X$ over $D$ fixes, at each real place $v$ of $F$, a sign vector $\varepsilon_v$, a discrete series $\sigma_v$ of $\mathrm{U}(J_{\varepsilon_v})$ with a unit vector $w_v$, a Haar measure $\mu_v$, and for each word $u$ a local Bessel weight $W_{u,v}$ on $\mathrm{U}(J_{\varepsilon_v})$. The tensor product over the real places gives a representation $\sigma_\infty$ of $G_\infty = \prod_v \mathrm{U}(J_{\varepsilon_v})$ with vector $w_\infty = \otimes_v w_v$, a weight $W_u$ on $G_\infty$, a subgroup $S_u \subset G_\infty$ with Haar measure $\mu_{S,u}$, and a quotient measure $\nu_u$. We write $d_v$ for the formal degree of $\sigma_v$ ([discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees)) and $\deg X = \prod_v d_v$.

**Definition 6.3.1 (Gap condition on a datum).** A global datum $D$ satisfies the *gap condition* if $r \geq 1801$ and, for each index $\tau$ and each $j$, the Harish-Chandra parameters $b_j$ of $D$ satisfy $b_{j+1} - b_j \geq 16 r^{19}$.

### Convolution integrals

**Definition 6.3.2 (Local kernel).** For a word $w$ and a real place $v$ put
$$K_v(a) = |W_{w,v}(a)| \int_{\mathrm{U}(J_{\varepsilon_v})} |\langle \sigma_v(a) w_v, \sigma_v(b) w_v \rangle| \, |W_{w,v}(b)| \, d\mu_v(b).$$

This is the absolute value of the convolution of a matrix coefficient with the Bessel weight, weighted once more by the Bessel weight. Its integral over a quotient is the local factor of the energy of a Bessel period.

**Theorem 6.3.3 (Convergence of the convolution integrals).** Assume the uniqueness of Bessel maps in the form of [Theorem 6.2.7](/entry/bessel-map-uniq-gap/), and assume three facts on discrete series that are proved elsewhere in the development: decay of matrix coefficients at the lower and at the upper end of the parameter, and smoothness of $K$-finite vectors. Let $D$ satisfy the gap condition, $X$ a setting over $D$, $u, u'$ words and $s > 0$. Then:

1. for each $c$ in the set of good coordinates and each $\gamma \in G_\infty$ that is diagonal for $(u, u', s, c)$,
$$\begin{aligned}
\int \!\! \int \!\! \int \!\! \int & |\langle \sigma_\infty(z) w_\infty, \sigma_\infty(s_1 \gamma s_2^{-1}) \sigma_\infty(z') w_\infty \rangle| \\
& \cdot |W_u(z)| \, |W_{u'}(z')| \, d\mu_{S,u'}(s_2) \, d\mu_{S,u}(s_1) \, d\nu_{u'}(z') \, d\nu_u(z) < \infty;
\end{aligned}$$
2. for each word $w$,
$$\int \!\! \int \!\! \int |\langle \sigma_\infty(z) w_\infty, \sigma_\infty(s) \sigma_\infty(z') w_\infty \rangle| \, |W_w(z)| \, |W_w(z')| \, d\mu_{S,w}(s) \, d\nu_w(z') \, d\nu_w(z) < \infty.$$

Lean: `Formalism.L2.SG.RealObj.EnergyConvJ.BM.stepConvG_holds` (also `Formalism.L2.SG.RealObj.EnergyConvJ.BM.stepConvG_jsz`, the form with only the uniqueness assumption).

*Proof.* The fourfold and threefold integrals factor over the real places. So it is enough to prove two local statements at each real place $v$: a double integral of $|\langle \sigma_v(x) w_v, \sigma_v(g) \sigma_v(y) w_v \rangle| \, |W_{u,v}(x)| \, |W_{u',v}(y)|$ is finite for the relevant $g$, and $\int K_v \, d\nu_{l,v} < \infty$ for each quotient measure $\nu_{l,v}$ that comes with a quotient witness. We prove the second; the first is similar.

There is a pair of measures $(\mu_S, \nu)$ at $v$, with $\mu_S$ an invariant measure on $S$ and $\nu$ a measure on $\mathrm{U}(J_{\varepsilon_v})$, such that $\int f \, d\mu_v = \int \int f(s x) \, d\mu_S(s) \, d\nu(x)$ for measurable $f \geq 0$ and such that the triple integral
$$\int \int \int |\langle \sigma_v(a) w_v, \sigma_v(s b) w_v \rangle| \, |W_{w,v}(a)| \, |W_{w,v}(b)| \, d\mu_S(s) \, d\nu(b) \, d\mu_v(a)$$
is finite. This pair is constructed from the reproducing formula for square-integrable representations, the $L^2$ theory of right translations, the gap condition and a computation of local factors, with the four assumed facts as inputs. This is the only place where the uniqueness of Bessel maps enters. The unfolding identity for the Haar measure $\mu_v$ over $S$ rewrites this triple integral as $\int K_v \, d\nu$. So $\int K_v \, d\nu < \infty$. The function $K_v$ is invariant under $S$. Quotient measures on $S \backslash \mathrm{U}(J_{\varepsilon_v})$ are unique up to a positive constant ([Haar measure](/learn/analysis/#haar-measure)), so $\nu_{l,v} = c\,\nu$ with $0 < c < \infty$, and $\int K_v \, d\nu_{l,v} = c \int K_v \, d\nu < \infty$. $\square$

**Definition 6.3.4 (Bound at infinity).** For words $u, u'$ and $s > 0$, let $I_{OO}(u, u', s)$ be the integral over the good coordinates $c$ of a weight times the squared Hilbert-Schmidt norm of the Gram operator at $c$. We say that $X$ satisfies the *bound at infinity* at $(u, u', s)$ if: the disintegration constant of the coordinate map is positive; each good $c$ has a diagonal $\gamma$, and the off-diagonal orbital integral at $c$ converges; and
$$I_{OO}(u, u', s) \leq \frac{1}{\deg X}.$$

**Theorem 6.3.5 (Bound at infinity).** Assume the uniqueness of Bessel maps in the form of [Theorem 6.2.7](/entry/bessel-map-uniq-gap/). Let $D$ satisfy the gap condition, $X$ a setting over $D$, $u, u'$ words and $s > 0$. Then $X$ satisfies the bound at infinity at $(u, u', s)$.

Lean: `Formalism.L2.SG.RealObj.EnergyConvJ.BM.realObj_inInfinityX_jsz`.

*Proof.* By the theorem above, and by a parallel statement for the energy integrals that is proved from the same four inputs, the convolution integrals and the energy integrals converge. The positivity of the disintegration constant comes from the disintegration of Haar measure at the real places, and the existence of diagonal points from a computation at the real places. The convergence of the off-diagonal orbital integrals is the energy statement. The inequality $I_{OO} \leq 1/\deg X$ is a general reduction, proved elsewhere in the development, from the two convergence statements, the Schur orthogonality relations for tensor products of discrete series, Haar measure on subgroups and the choice of sections. $\square$

### Amplitudes

The amplitude $A_J(\nu_R, \gamma)$ of a relevant point $\gamma$ is an operator between the spaces of two local Bessel data. It is defined by an integral over the stabilizer of $\gamma$ with the measure $\nu_R$. The next theorem bounds it by an orbital integral of one $K$-finite matrix coefficient.

**Definition 6.3.6 (Amplitude bound).** Let $D$ be a global datum with size data, and let $C', C_l, C_g, c_b, C_u, c_T, C_T, C_0, C_1, C$ be constants. The *amplitude bound* holds for $D$ with these constants if the following is true whenever the base hypothesis of the size data holds. Let $(\tau, w, w')$ be an admissible triple, $\theta$ a point of the window of size $C_1$, $W$ a good local datum and $A$ a good local Bessel datum at the parameter $\lambda_D(\tau)$ of $D$. Then there are a $K$-finite matrix coefficient $f$ of the local discrete series and $K > 0$ such that:

1. for each section $\mu$ of the coordinate map, the $J$-norm $j(f, \mu)$ is nonzero and $K \, j(f, \mu) \leq M(w, w', A, \mu)$;
2. for each relevant pair $(\gamma, p)$, each $\theta'$ in the window and each stabilizer measure $\nu_R$,
$$\| A_J(\nu_R, \gamma) \|_{HS}^2 \leq K \, b^{C m^2} \, O(f, p),$$
where $O(f, p)$ is the squared orbital integral of $f$ at $p$, $b$ is the size parameter and $m$ the number of blocks.

**Theorem 6.3.7 (Uniform amplitude bound).** Assume the uniqueness of Bessel maps in the form of [Theorem 6.2.7](/entry/bessel-map-uniq-gap/). Assume also that the $K$-finite vectors of a discrete series of $G$ are dense in its smooth vectors for each finite family of word seminorms. Then for all constants $C_g, c_b, C_u, c_T, C_T, C_0, C_1$ there are $C_a \geq 0$ and $C'_0, C_{l,0}$ such that for all $C' \geq C'_0$, all $C_l \geq C_{l,0}$ and every global datum $D$ with size data, the amplitude bound holds with the constant $C_a$.

Lean: `Formalism.L2.S.Pv.AmpOrbCoef.BM.ampUnif_gap`.

*Proof.* The bound is assembled from six parts. The main part is an orbital integral formula: for $C_l \geq 1000$, each amplitude $A_J(\nu_R, \gamma)$ equals the orbital integral of a $K$-finite matrix coefficient $f$. Here uniqueness and density enter. A Bessel functional at the real place is unique up to a scalar, so the amplitude, which is built from two Bessel functionals, is a scalar times the orbital integral of the coefficient $\langle \sigma(\cdot) x, x' \rangle$ for any vectors $x, x'$. Density lets us take $x, x'$ to be $K$-finite, with an error that is small in the seminorms that control the Bessel functionals. The other five parts are: the Jacobian of the root coordinates, the Haar measure of the root group, the existence of a quotient measure on the orbit, a relation between the amplitude and the orbital integral at one point, and the nonvanishing of the $J$-norm, which uses that an archimedean local coefficient is nonzero. Together they give items 1 and 2, with $C'_0 = 0$ and $C_{l,0} = 1000$ in the orbit step. $\square$

**Corollary 6.3.8 (Uniform amplitude bound, unconditional).** The conclusion of the theorem above holds without assumptions.

Lean: `CompanionTheory.Lime.BM.ampUnif_holds` (also `CompanionTheory.Lime.BM.ampUnif`, the form with the uniqueness assumption only).

*Proof.* The density of $K$-finite vectors in smooth vectors is proved elsewhere in the development; it is a form of Harish-Chandra's density theorem for $K$-finite vectors. The uniqueness is [Theorem 6.2.7](/entry/bessel-map-uniq-gap/). Apply the theorem above. $\square$

**Remark 6.3.9.** In the global argument, the bound at infinity is used with uniqueness supplied by [Theorem 6.2.7](/entry/bessel-map-uniq-gap/), so it holds for every setting over a datum with the gap condition.

**Remark 6.3.10 (Formalization).** The amplitude bound is used only with the parameter defect $C_n = 0$, so the condition $\ell^1(\lambda', \lambda_D) \leq C_n k m^3$ forces $\lambda' = \lambda_D$ ([AmplitudeOrbitalIntegral.lean](lean:CompanionTheory/AutomorphicTheory/LocalBesselUniqueness/BesselModels/AmplitudeOrbitalIntegral.lean#L417)). That file turns off the duplicate namespace linter at line 9. A second definition named `AmpUnif` exists in `BDataOf.lean`. The assumption of uniqueness is a copy of the uniqueness theorem under a new name, and the map between them is the identity ([UniqGapOfBmu.lean](lean:CompanionTheory/AutomorphicTheory/LocalBesselUniqueness/BesselModels/UniqGapOfBmu.lean#L10)). The file that discharges it, `MultiplicityOneUnitaryBranchingOfGapHyp.lean`, has a name about branching laws. The suffix `jsz` in three names presumably refers to Jiang, Sun and Zhu, but nothing in the code says so. `ConvGG.lean` turns off the unused variables linter at line 4, and `LocQuad1GHolds.lean` raises the heartbeat limit to 800000 at line 17. We have not unfolded the global datum, the setting, the good coordinates, the Gram operator, the stabilizer measures or the $J$-norm. The descriptions above stay at the level of their statements.
