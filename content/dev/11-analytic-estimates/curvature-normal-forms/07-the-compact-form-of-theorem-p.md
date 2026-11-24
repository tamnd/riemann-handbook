---
title: The compact form of Theorem P
decls:
  - Formalism.FourierDecayAlt.P5.HerC.thmPActualCpt_of_parts
  - Formalism.FourierDecayAlt.P5.HerC.thmPActualCpt_of_jf
  - Formalism.FourierDecayAlt.P5.HerC.thmPActualCpt_of_stepForm
  - Formalism.FourierDecayAlt.P5.HerC.thmPActualCpt_of_outer
  - Formalism.FourierDecayAlt.P5.HerD.theorem_P_compact_of_step_density
  - Formalism.FourierDecayAlt.P5.HerD.thmPActualCpt_of_stepExp0
  - Formalism.FourierDecayAlt.P.CutSE.stepExp0_of_leaves
  - Formalism.FourierDecayAlt.P.CutSE.thmPActualCpt_of_leaves
  - Formalism.FourierDecayAlt.P.CutSE.thmPActualCpt_of_spec
  - Formalism.FourierDecayAlt.P.CutSE.rDIdentSpec_of_R
  - Formalism.FourierDecayAlt.P.CutSE.thmPActualCpt_of_R
  - Formalism.FourierDecayAlt.P.CutSE.actual_compact_theorem
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The compact form of Theorem P

This section proves the compact form of Theorem P with no hypothesis. The theorem gives, for each normal form datum, a chain of subspaces $K_0, \dots, K_r$ of the radial space on which the level forms are positive and have Fourier decay, and it puts the restriction of every compactly supported nice coefficient into $K_0$. The proof is a chain of reductions. Each step replaces the remaining hypothesis by a hypothesis that is closer to an explicit computation, until the last hypotheses are two facts about radial operators, and these are proved. The compact form is used by the carrier inputs and by the built bounds, and so it sits below the trunk node [HypsAlt is nonempty](/step/nonempty-hyps/). The old entries [the compact form of Theorem P](/entry/actual-compact-theorem/), [the compact form from the radial operators](/entry/thm-pactual-cpt-of-r/), [the compact form from the spectral identity](/entry/thm-pactual-cpt-of-spec/) and [the compact form from three leaf facts](/entry/thm-pactual-cpt-of-leaves/) record the upper part of the chain.

### The setting

Let $n = 2r + k + 1$ with $k \ge 1$, and let $H$ be the hermitian form that pairs $e_a$ with $e_{n-1-a}$ for $a < r$ and is $\operatorname{diag}(1, \dots, 1, -1)$ on the middle $k + 1$ coordinates. Let $G = U(H)$, a [unitary group](/learn/groups/#unitary-groups) of signature $(r + k, r + 1)$. Fix $z, z'$ in the middle block with $H(z, z) < 0$ and $H(z', z') < 0$, and multiplicative maps $\pi, \pi'$ on the stabilizers $H_z, H_{z'}$. For $F$ on $G$ with values in $\operatorname{Hom}(W_q, W_p)$, the function $J_F$ integrates $F$ over the two unipotent sides, twisted by $\pi$, $\pi'$ and a character $\psi$.

The radial space $\mathcal{R}$ holds the smooth functions $\Phi(c, g)$, with $c \in (\mathbb{C}^\times)^r$ and $g \in G$, that vanish off a domain $\Omega_R$ and satisfy $\Phi(c, h g h') = \pi(h) \Phi(c, g) \pi'(h')$. The restriction $\operatorname{res}$ sends $J$ to the function $(c, g) \mapsto \prod_a |c_a|^{m_a - 1} J(w(c) g)$ for a cell element $w(c)$.

A normal form datum is a tuple $(X, \mu, L, \mathrm{st}, l_0)$ of operators, a measure, level data, a start and an integer, with the conditions of Section 03. Throughout, $1 \le l_0 \le k$, and $D$ is real place data with the same $z, z', \pi, \pi'$.

**Theorem 1.7.1 (compact form of Theorem P).** Let $(X, \mu, L, \mathrm{st}, l_0)$ be a normal form datum, let $S$ be a finite set of letters, and let $A \ge A_{\mathrm{user}}$ and $m \ge m_{\mathrm{user}}$. Then there are subspaces $K_0, \dots, K_r$ of $\mathcal{R}$ such that:

1. for each admissible word the level form at each level $i$ is sesquilinear and positive semidefinite on $K_i$; at the top level the twisted form is the integral of $e^{s\zeta - \bar s \bar\zeta}$ times the top density; at each level $l < r$ it is the [Fourier transform](/learn/analysis/#the-fourier-transform) of a continuous function $\varphi$ with $|\varphi(t)| \le C(1 + |t|)^{-4}$;
2. the slice operator at level $l$ maps $K_l$ into $K_{l+1}$;
3. the level zero form is the integral over $(c, g)$, with weight $\prod_l |c_l|^{-2}$, of the top density of the images under all slice operators;
4. if $F$ has compact support, lies in every nice class, and satisfies $G_f \ge \varepsilon > 0$ where $F \neq 0$, then some $\Phi \in K_0$ equals $\operatorname{res}(J_F)$ on $\Omega_R$.

The proof below builds $K_i$ as the span $K^c_i$ of the generated class at level $i$: the restrictions of compact nice coefficients, closed under the slice, wave and multiplication operators.

### From the classes to the theorem

We name the intermediate statements. All of them are for every normal form datum and every $D$ as above.

- (Top) The top class $K^c_r$ lies in the subspace of compactly supported radial functions.
- (SF) The step densities exist on the classes $K^c$, and the level forms are integrals of the pairing over the glued points.
- (SD) The first half of (SF).
- (FO) For each admissible word, each level $i$, each $c \in \Omega_X$ and $x, y \in K^c_i$, the function $c' \mapsto \prod_l |c'_l|^{-2} \sum_a \langle R_i(w) x_a, y_a \rangle(c \cdot c')$ is integrable.
- (JF) If $F$ is a compact coefficient and $\Phi$ is a radial form of $J_F$, then $\Phi$ is locally compact.

**Theorem 1.7.2.** (Top) and (SF) imply the compact form of Theorem P.

Lean: `Formalism.FourierDecayAlt.P5.HerC.thmPActualCpt_of_parts`

*Proof.* Take $K = K^c$. From (Top) we get the top adjoint identity on $K_r$, and with the frame of an admissible word this gives the top identity. The normal form of the actual datum and the positivity of the fibre constant $\kappa$ give the nonnegativity of the top density. The slice operators keep the classes, by construction. With (SD) and the measurability of the top density, the integral formula of the steps gives item 3. The smoothness of $\zeta$ gives the top twist, and the wave operators keep the classes. The integral half of (SF) gives sesquilinearity. For item 4, the radial form of $J_F$ exists for compactly supported $F$ with $G_f \ge \varepsilon$, and it lies in $K^c_0$ by the definition of the class. This gives all parts of the class statement. The commutation of the wave operator with the matrix $Q$ and the plane wave identity then give the step twist. With the top identity this gives item 1, and items 2, 3 and 4 are already proved. $\square$

**Theorem 1.7.3.** (JF) and (SF) imply the compact form of Theorem P.

Lean: `Formalism.FourierDecayAlt.P5.HerC.thmPActualCpt_of_jf`

*Proof.* By (JF) every generator of the top class is locally compact, so $K^c_r$ lies in the locally compact subspace, and this subspace lies in the compactly supported subspace. This is (Top), and the previous theorem applies. $\square$

**Theorem 1.7.4.** (SF) implies the compact form of Theorem P.

Lean: `Formalism.FourierDecayAlt.P5.HerC.thmPActualCpt_of_stepForm`

*Proof.* (JF) is proved separately, for every compact coefficient and every radial form of its function $J_F$. Apply the previous theorem. $\square$

**Theorem 1.7.5.** (SD) and (FO) imply the compact form of Theorem P.

Lean: `Formalism.FourierDecayAlt.P5.HerC.thmPActualCpt_of_outer`

*Proof.* We prove (SF). Its first half is (SD). For the second half, fix a word, a level, a point $c$ and $x, y$ in the class. The pairing at each glued point $c \cdot c'$ is the integral of the pairing over the fibre, by the integral lemma for the classes. Integrability is (FO). Apply the previous theorem. $\square$

### The step expansion and level transport

- (E0) At the level $l = 0$, for each admissible word $w$, each $c \in \Omega_X$ and $x, y \in K^c_0$, the step density $\phi_w(x, y, c)(t)$ is a finite sum $\sum_i a_i \, \partial^{j_i} D_i(t)$ for $t \neq 0$. Here each $D_i$ decays with $j_i \le n$, and the terms of order $0$ have total integral equal to the level form $R_0(w; x, y)(c)$.
- (LT) For each level $i$ and each $c$ with $c_l \neq 0$ for $l < i$, there are a normal form datum at rank $r - i$ and a linear map $T$ from $\mathcal{R}$ to the radial space of that rank. The map satisfies the transport clauses: it carries the pairing to a multiple $\kappa$ of the pairing, and the words and slices to the words and slices of the new datum. It also carries $K^c_i$ into the class at level $0$ of the new datum.

**Theorem 1.7.6.** (LT) and (E0) imply the compact form of Theorem P.

Lean: `Formalism.FourierDecayAlt.P5.HerD.theorem_P_compact_of_step_density`

*Proof.* We prove (SD) and (FO). Fix a level $l$ and data. By (LT) at the level $l$ we get a datum of rank $r - l$ and a map $T$. Under $T$ the level $l$ becomes the level $0$ of the new datum, and the level $l + 1$ becomes its level $1$. So (E0) for the new datum, applied to $Tx$ and $Ty$, gives the step expansion at level $l$, after we divide by $\kappa$ and rewrite the words. This gives (SD). The same transport reduces (FO) to the square integrability of the residues at positive rank, which is proved for every datum. $\square$

**Theorem 1.7.7.** (E0) implies the compact form of Theorem P.

Lean: `Formalism.FourierDecayAlt.P5.HerD.thmPActualCpt_of_stepExp0`

*Proof.* (LT) is proved: it is the hermitian level transport, built from a good slice family. Apply the previous theorem. $\square$

### The three density facts

Let $D(t) = \operatorname{Dens}(\mu, l, u, v, c)(t)$ be the density of a pair $u, v$ in the level class at a point $c \in \Omega_X$, with $l = 0$.

- (Sm) $D$ is of class $C^n$ on $t \neq 0$ for every $n$, and $u, v$ are square integrable at level $l + 1$.
- (O) For each letter with a real point there are a scalar $e$ and a Wirtinger derivative $\partial$ such that the action of the letter changes $D$ to $D + e \, \partial D'$, where $D'$ is the density of $u$ and a modified $v$.
- (RD) For radial vectors $\Phi, \Psi$ that agree on $\Omega_R$ with restrictions of nice coefficients, and multiplication by $f_s(c_l)$, the local pairing is at most $C(1 + |s|)^{-(n+3)}$, for each $n$.

**Theorem 1.7.8.** (O), (Sm) and (RD) imply (E0).

Lean: `Formalism.FourierDecayAlt.P.CutSE.stepExp0_of_leaves`

*Proof.* From (Sm) the density is continuous on $t \neq 0$. From (RD) and the outgoing wave identity for the orbital integral we get

$$\Bigl| \int f_s(t) D(t) \, dt \Bigr| \le C (1 + |s|)^{-(n + 3)}.$$

With the site multiplication identity we get the same bound for the density times $(1 + |t|^2)^2$. These bounds say that $D$ and its weighted form have decaying Fourier transforms. With (O) we write the step density of a word letter by letter as a sum of derivatives of such densities. The terms of order $0$ integrate to the level form. This is (E0). $\square$

**Theorem 1.7.9.** (O), (Sm) and (RD) imply the compact form of Theorem P.

Lean: `Formalism.FourierDecayAlt.P.CutSE.thmPActualCpt_of_leaves`

*Proof.* Combine the previous theorem with the reduction from (E0). $\square$

### The spectral identity and the radial operators

- (Sp) There are a real $Y$ with $Y$ and $Y + 1$ in the invertible set of the start, and four differential operators $\Theta_0, \dots, \Theta_3$ on $G$ with smooth coefficients that commute with the action and have polynomial bounds, such that $\Theta_j$ and its formal adjoint act on restrictions as the $j$-th entry of the list below and its adjoint:

$$\bigl(\hat A_v(Y + 1),\ G_i \xi(Y) R_h(Y),\ G_i \xi(Y + 1) R_{hv}(Y + 1),\ \hat A(Y)\bigr).$$

- (R) For each real $Y$ with $Y - 1$, $Y$ and $Y + 1$ invertible, there is a differential operator $\Theta$ with these properties such that, on $\Omega_R$ and for each $J$ in the class,

$$\operatorname{res}(\Theta J) = G_i\, \xi(Y)\, R_h(Y) \operatorname{res}(J).$$

- (Rv) The same as (R) for $G_i\, \xi(Y + 1)\, R_{hv}(Y + 1)$.

**Theorem 1.7.10.** (Sp) implies the compact form of Theorem P.

Lean: `Formalism.FourierDecayAlt.P.CutSE.thmPActualCpt_of_spec`

*Proof.* We prove (O), (Sm) and (RD). The radial locality of the slice functions is proved. From it we get the Leibniz class and (Sm). From the Leibniz class and (Sm) the one letter estimate gives (O). For (RD), the four operators of (Sp) lift to the group identity

$$s \cdot w_s J = \Theta_0^*(w_s \Theta_1 J) - \Theta_2^*(w_s \Theta_3 J)$$

for the wave operator $w_s$. The radial identity of the spectral data follows, and from it the decay bound (RD). Apply the previous theorem. $\square$

**Theorem 1.7.11.** (R) and (Rv) imply (Sp).

Lean: `Formalism.FourierDecayAlt.P.CutSE.rDIdentSpec_of_R`

*Proof.* Choose a real $Y$ with $Y - 1$, $Y$ and $Y + 1$ invertible; the lemma on real points of the start gives such a $Y$. The operators for $\hat A(Y)$ and $\hat A_v(Y + 1)$ are proved. (R) and (Rv) give the two middle operators. The pairing identities and the quadratic adjoint relation show that each radial operator in the list is adjoint to its partner for the inner product of $\mathcal{R}$. So the formal adjoint of each $\Theta_j$ acts on restrictions as the partner. The test of $\xi$ gives the scalar factor. This is (Sp). $\square$

**Theorem 1.7.12.** (R) and (Rv) imply the compact form of Theorem P.

Lean: `Formalism.FourierDecayAlt.P.CutSE.thmPActualCpt_of_R`

*Proof.* Combine the previous two theorems. $\square$

**Theorem 1.7.13.** The compact form of Theorem P holds.

Lean: `Formalism.FourierDecayAlt.P.CutSE.actual_compact_theorem`

*Proof.* We prove (R) and (Rv). For (R), take the composite $T_0 \circ \Theta$ of a group operator $\Theta$ with the zero order term $T_0$ of the operator for $X$. Four proved facts show that it acts on restrictions as $G_i \xi(Y) R_h(Y)$: the right action of the group, the operator for $X$, the right action of $\rho$ and the composition at order zero. For (Rv), use the adjoint forms of the same four facts. Apply the previous theorem. $\square$

**Remark 1.7.14 (Formalization).** The chain from `CutSE.actual_compact_theorem` at `HermitianCurvatureProofs/CutSETopFinal.lean:14` to `P5.HerC.thmPActualCpt_of_parts` at `HermitianCurvatureProofs/StepFormCptAllOfStepFormAll.lean:118` is eleven one-line relays. The other relays are at `CutSETopR.lean:11` and `:14`, `CutSE_TopSpec.lean:13`, `CutSETopHer.lean:9` and `:13`, `TheoremPCompactOfStepSquare.lean:6`, `TheoremPCompactOfStepDensity.lean:245`, `ThmPActualCptOfOuter.lean:116`, `ThmPActualCptOfStepForm.lean:170` and `OpLEqZeroOfEventually.lean:232`. All are in `HermitianCurvatureProofs`. The statement `P5.ThmPActualCpt` at `HermitianCurvature/HerGenC.lean:63` takes $A \ge A_{\mathrm{user}}$ and $m \ge m_{\mathrm{user}}$ (line 71). The conclusion never uses them, because the nice classes in item 4 range over new variables, and `herClassesCpt_of_parts` discards both hypotheses (`StepFormCptAllOfStepFormAll.lean:97`). The bound $A_{\mathrm{user}} = 127 (r + 1)^3 (N n_V^2 + n_V^3)$ is at `HermitianCurvature/CompositeFormulaLevelZero.lean:340`. The radial operator statements (R) and (Rv) ask for $Y - 1$ invertible, but (Sp) does not keep this condition. (E0) is stated only for $l = 0$ with $l$ of type `Fin P.r` (`TheoremPCompactOfStepDensity.lean:120`), so for $r = 0$ it is empty. `theorem_P_compact_of_step_density` passes the same level transport to both of its parts. The hypothesis (JF) of `thmPActualCpt_of_jf` is the proved `jfCptLocAll` (`ThmPActualCptOfStepForm.lean:54`). The chain moves between three namespaces, `P.CutSE`, `P5.HerD` and `P5.HerC`.
