---
title: The normalizing constant
decls:
  - Formalism.L2.SG.Pf.NcLeaves.ncTieC_of_leaves
  - Formalism.L2.SG.Pf.NcAllS.ncTieAllS_of
  - Formalism.L2.SG.Pf.NcAllS.ncTie0All_of
  - Formalism.L2.SG.Pf.NcAllC.ncTieC_of_closed
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The normalizing constant

The theta lift of the proof carries a normalizing constant $c$. It is defined by the measures of the groups involved: the volume of the level subgroup, the volumes of the unipotent quotients at infinity, and the constant of the disintegration of the measure of $G$ along the stabilizer of a frame. On the other side there is an explicit number $c_{\mathrm{expl}}$, built from a mass, a power of the discriminant and special values of $L$-functions. This section proves that the two agree: the Theorem (Normalizing constant) gives $c = c_{\mathrm{expl}}$. It is used in the step [HypsAlt is nonempty](/step/nonempty-hyps/).

Fix a Hida setting for the CM extension $E/F$, with weight $k$, rank $r$, space dimension $R$ and the parameter $m$ as in the [section on covolumes](/entry/nofib-holds/), where $r = k + m - 1$ and $m + 3 \leq k$. Let $[F : \mathbb{Q}] = f$, let $g_S$ be the level, and let $u, u'$ be words with $T_u \equiv T_{u'} \pmod{g_S^2}$. Let $F_0$ be a base flag and $\mathcal{W}$ a set of row representatives. Let $\eta$ be the quadratic character of $E/F$ and $L(s, \eta)$ its $L$-function.

**Definition 8.9.1 (Explicit constant).** Put
$$\begin{aligned} c_{\mathrm{expl}} = {} & c_{\mathrm{mass}}(E, F, k - 1) \, |d_F|^{-2 r (r+1)(k-1)} \\ & \times \frac{\prod_{i = k}^{R} L(i, \eta)}{\mathrm{mass}(F_0, \mathcal{W})}, \end{aligned}$$
where $c_{\mathrm{mass}}(E, F, k - 1)$ is the mass constant in rank $k - 1$ of the [section on gluing](/entry/gluing-mass-holds/) and $\mathrm{mass}(F_0, \mathcal{W})$ is the mass of the rows.

**Definition 8.9.2 (Normalizing constant).** The measure data of the setting give real numbers $n_0$ (the unnormalized constant) and $\alpha$ (the archimedean factor). Put
$$\kappa_N = \mathrm{rd}_E^{\,2 r (r+1)(k-1) f} \, g_S^{-2 f r (r+1)}, \qquad \nu = \sqrt{|N(g_S^m)|}^{\,k - 1}.$$
We say that a number $c$ *ties the normalizing constant* if $c = n_0 \nu / (\alpha \kappa_N)$.

The constant $n_0$ is a product of measures. Let $D_C$ be the disintegration constant, $\mathrm{vol}(H)$ the volume of the stabilizer at infinity, $\mathrm{vol}(N)$ and $\mathrm{vol}(N')$ the volumes of the unipotent quotients, $\mathrm{vol}_1 / \mathrm{vol}_{\mathbb{Z}}$ the ratio of the unit level volume to the integral one, and $\mu(K)$ and $\mu(H')$ the measures of the level subgroups of $G$ and of the stabilizer. Under the volume conditions below, $c$ ties the normalizing constant if and only if
$$\begin{aligned} c \, \alpha = {} & D_C \, \mathrm{vol}(H) \, \mathrm{vol}(N) \, \mathrm{vol}(N') \\ & \times \frac{\mathrm{vol}_1}{\mathrm{vol}_{\mathbb{Z}}} \cdot \frac{\mu(K)}{\mu(H')} \, \nu. \end{aligned}$$

**Theorem 8.9.3 (Normalizing constant from the leaves).** Let $a' > 0$. Assume the positivity and the mass, level, ordinary, typed and volume conditions of the measure data, that the two Haar volumes of $G$ agree, that $\psi$ is a standard character of $\mathbb{A}_F / F$, the congruence $T_u \equiv T_{u'} \pmod{g_S^2}$, and that $\mathcal{W}$ is a set of row representatives for $F_0$. Assume also the finite splitting $\mu(K) \, a' = \mu(K \cap H) \prod_v \omega_v$ with the local orbital volumes $\omega_v$, and the real bracket identity for $a'$. Then $c_{\mathrm{expl}}$ ties the normalizing constant.

Lean: `Formalism.L2.SG.Pf.NcLeaves.ncTieC_of_leaves`.

*Proof.* By the volume conditions it is enough to prove the identity of the last display for $c = c_{\mathrm{expl}}$. The real bracket gives $D_C \, \mathrm{vol}(H) \, \mathrm{vol}(N) \, \mathrm{vol}(N')$ as $a'$ times $2^{k h_\infty} (\pi^k / (k-1)!)^{h_\infty} T_u^{-k h_\infty} |d_F|^{e(k, r)}$. The finite splitting replaces $a' \mu(K)$ by $\mu(K \cap H) \prod_v \omega_v$. What remains is an identity between explicit numbers. It is proved with two inputs: the product of the local differents, $\prod_v |\mathfrak{d}_v| = |d_F|^{-1}$, and the value of the mass of the row lattices, which accounts for the denominator $\mathrm{mass}(F_0, \mathcal{W})$ of $c_{\mathrm{expl}}$. $\square$

**Theorem 8.9.4 (Normalizing constant from the splitting).** Assume the splitting of the measure in the form of the [Theorem (Splitting the measure)](/entry/omega-splitting-of-witt/), the real bracket identity, and the conditions of the Theorem (Normalizing constant from the leaves) on the measure data, with the standing hypotheses of the setting (a lattice in $V$, a frame of $u'$ with Gram matrix of nonzero determinant, and the two Siegel-Weil compatibility conditions). Then $c_{\mathrm{expl}}$ ties the normalizing constant.

Lean: `Formalism.L2.SG.Pf.NcAllS.ncTieAllS_of`.

*Proof.* The measure of the level subgroup is positive and finite. We have $n = R$, and $2(2r + 1) < n$ follows from $m + 3 \leq k$ and $r = k + m - 1$. So the splitting of the measure applies at the frame of $u'$ and gives $a' > 0$ with the finite splitting. The real bracket holds for this $a'$, with the exponent $e(k, r)$. Then apply the [Theorem (Normalizing constant from the leaves)](/entry/nc-tie-c-of-leaves/). $\square$

**Theorem 8.9.5 (Normalizing constant from the real bracket).** Assume the real bracket, the Siegel-Weil mass data, and the standing hypotheses of the setting: the hypotheses on the fundamental domains, the measure compatibility for $\psi$, the standard hypotheses, a lattice in $V$, two Gram matrices of nonzero determinant, the convergence of the products, the local ties at $u$ and $u'$, the typed facts, the positivity of the quotient volumes, $s_d \geq 0$, $C \geq 0$, $\Theta > 0$, the congruence and the row representatives. Then $c_{\mathrm{expl}}$ ties the normalizing constant.

Lean: `Formalism.L2.SG.Pf.NcAllS.ncTie0All_of`.

*Proof.* This is the [Theorem (Normalizing constant from the splitting)](/entry/nc-tie-all-s-of/) applied to the [Corollary (Splitting the measure from the integral Witt condition)](/entry/split-om-of-int-witt/), with the integral Witt condition at almost all places. The two Siegel-Weil compatibility conditions are the two parts of the mass data. The conditions on the measure data follow from the standing hypotheses: the volume identity for $G$, the ordinary and typed volumes, the typed index, the local volumes $\omega_v$ ([Theorem 5.4](/entry/om-v-holds-x/)) and the field dictionary. $\square$

**Theorem 8.9.6 (Normalizing constant).** Assume the covolume reference, the Siegel-Weil mass data and the standing hypotheses of the Theorem (Normalizing constant from the real bracket). Then
$$c_{\mathrm{expl}} = \frac{n_0 \, \nu}{\alpha \, \kappa_N}.$$

Lean: `Formalism.L2.SG.Pf.NcAllC.ncTieC_of_closed`.

*Proof.* The real bracket holds under the covolume reference ([Theorem 5.6](/entry/real-bracket-holds/)). Apply the [Theorem (Normalizing constant from the real bracket)](/entry/nc-tie0-all-of/). $\square$

**Remark 8.9.7 (Formalization).** The four theorems are a chain of conditional statements. The last one still assumes the covolume reference and the mass data; they enter as hypotheses ([NcAllC.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcAllC.lean#L37)). The theorem from the leaves reduces the tie to the identity displayed in its proof, and that identity is proved from the product of the local differents and the mass of the row lattices. We read the statements of these two inputs but not every step of the arithmetic, so the proof above gives its structure. The theorem from the splitting takes, among its hypotheses, `SWa1` from a namespace named `UnusedSlot34` and `StabilizerFirstChernCompatibility`, a measure condition with a name about Chern classes ([NcAllS.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcAllS.lean#L36)). The positivity conditions $s_d \geq 0$, $C \geq 0$ and $\Theta > 0$ concern auxiliary parameters of the term system that do not appear in the conclusion.

## Notes and references

The chapter feeds two steps of the proof. The gluing mass formula, the fibred description of the integral unipotent group, the block covolumes and the normalizing constant are used in the step [HypsAlt is nonempty](/step/nonempty-hyps/), where the closed bound is turned into explicit constants. The identity part of the concentrated sum is used in [theta local matching](/step/theta-local-matching/). The local cokernel counts, the partner counts and the global frame bijection feed the [cut of the coefficient into leaves](/entry/theorem-s-leaves-of-carrier-g/) and the [deep cut](/entry/cut-leaves-deep-outright/). The real bracket is completed in the [Theorem 5.6](/entry/real-bracket-holds/), and the row frames are used in the [row form](/entry/row-form-c-of-leaves3/).

The gluing of a unimodular lattice from a sublattice and its orthogonal complement along their discriminant modules is due to Nikulin for $\mathbb{Z}$-lattices. The version here is local: the count at each prime is the number of form-preserving endomorphisms of the discriminant module, and the global count is the product of the local counts. The density formula of the first section is the Hermitian form of the classical reduction of a local density to the density of the unimodular part of a Jordan splitting. Here it is stated only for Jordan bases with diagonal Gram matrix, which exist because $K/F$ is unramified. The mass formula enters only as a hypothesis, through a mass constant; the Siegel mass formula is in [Volume 1](/learn/groups/#hermitian-lattices-and-the-mass-formula).

The count of lattices by the isomorphisms of marked cokernels of their Gram matrices is specific to this proof. Its classical analogue is the fact that the isomorphism class of a lattice relative to a fixed sublattice is determined by its gluing data.

- V. V. Nikulin, "Integral symmetric bilinear forms and some of their applications", *Math. USSR Izv.* 14 (1980), 103 to 167, §1.5.
- O. T. O'Meara, *Introduction to Quadratic Forms*, Chapter IX, §91 (Jordan splittings).
- O. T. O'Meara, *Introduction to Quadratic Forms*, Chapter IV, §42 (Witt's theorem).
- J. Neukirch, *Algebraic Number Theory*, Chapter III, §2 (the different and the discriminant).
