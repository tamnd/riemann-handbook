---
title: Multipliers of formal endomorphisms
decls:
  - GlobalTheory.T.mumfordSections_multiplier_thickenings
  - GlobalTheory.MumMult.main
  - GlobalTheory.T.mumfordMultiplier_thickening_chart_sections
  - GlobalTheory.MumMult.chart_main
  - GlobalTheory.T.exists_mumfordMultiplier_of_section
  - GlobalTheory.MumMult.exists_mult_of_posN
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Multipliers of formal endomorphisms

This section and the next prove that a formal endomorphism of a uniformised semi-abelian scheme is algebraic. Here a formal endomorphism is a compatible family of endomorphisms of the thickenings of the closed fibre that lifts endomorphisms of degeneration data. This section proves the main step. A formal endomorphism $b$ moves sections of powers of the line bundle, up to a multiplier: for every section $s$ of $L_G^k$ there is a section of $L_G^{Nk}$ that is, on every thickening, the product of a fixed multiplier with $b^*s$. The multiplier is a unit at one point of the closed fibre. The next section uses these sections to compare $b$ with a homomorphism of the generic fibre. The method is Mumford's: sections are read through their theta expansions. See [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction) in Volume 1.

### The setting

Throughout this section and the next, $R$ is a base with maximal ideal $\mathfrak{m}$ and fraction field $K$, and $D = (B, L, \mathsf{X}, c, \psi)$ is degeneration data over $R$ with $\tau$ as in [the first section](/entry/has-of-base/). Let $A$ be a polarised abelian variety over $K$, $G$ a commutative semi-abelian group scheme over $R$, and $U$ a uniformisation of $(A, G)$ by $D$, with line bundle $L_G$ on $G$. For $e \geq 0$ let $G_e = G \otimes_R R/\mathfrak{m}^{e+1}$, with $\pi_e : G_e \to G$, projection $q_e : G_e \to B_e$, map $p_e : G_e \to B$ and torus $T_e \to G_e$ given by $U$. Integral theta families and the bundles $M_{k,\chi}$ on $B$ are as in [the section on theta expansions](/entry/exists-map-exp-all-traits/).

The bundle $L_G$ is given by a cover of $G$ by opens $G^i$ with trivialisations. A section $s$ of $L_G^k$ is a family of functions $s_i$ on $G^i$. For a family $(b_e)$ of endomorphisms of the $G_e$ and indices $i, i'$ we put

$$
W_e(i, i') = (\pi_e b_e)^{-1}(G^i) \cap \pi_e^{-1}(G^{i'}) \subseteq G_e.
$$

On $B \times B$ let $\Lambda(L)$ be the bundle with fibre $L_{x+y} \otimes L_x^{-1} \otimes L_y^{-1}$ at $(x, y)$.

**Definition 4.20.1 (Endomorphism data).** Let $a, a'$ be endomorphisms of the scheme $B$ and $h, h'$ endomorphisms of $\mathsf{X}$. They are *endomorphism data* for $D$ if:

1. $a$ and $a'$ are homomorphisms of group schemes;
2. the bundle $(a \times 1)^*\Lambda(L) \otimes (1 \times a')^*\Lambda(L)^{-1}$ on $B \times B$ is trivial locally on $\operatorname{Spec} R$, so $a$ and $a'$ are adjoint for the polarisation of $L$;
3. $c(h(y)) = a(c(y))$ and $c(h'(y)) = a'(c(y))$ for all $y \in \mathsf{X}$;
4. for every trivialisation $u$ of the bundle in 2 with $u(0, 0) = 1$ we have $\tau(h(y), y') \, u(c(y), c(y')) = \tau(y, h'(y'))$ for all $y, y' \in \mathsf{X}$.

Lean: `GlobalTheory.Mum.EndData`.

**Definition 4.20.2 (Formal endomorphism).** Let $a$ be an endomorphism of $B$ and $h'$ an endomorphism of $\mathsf{X}$. A *formal endomorphism* over $(a, h')$ is a family $b = (b_e)_{e \geq 0}$ of homomorphisms $b_e : G_e \to G_e$ with these properties:

1. $b_{e+1}$ restricts to $b_e$ on $G_e \subseteq G_{e+1}$;
2. $q_e \circ b_e = a \circ q_e$;
3. on the torus, $b_e$ is the endomorphism $t$ of $T_e$ with $t^*\chi = h'(\chi)$ for every character $\chi$.

Lean: `GlobalTheory.Mum.FormalEnd`.

**Definition 4.20.3 (Expansion on an open).** Let $e \geq 0$, $k \geq 1$, $W$ an open of $G_e$ inside $\pi_e^{-1}(G^{i'})$, $g$ a function on $W$, and $f = (f_\chi)$ a family of sections $f_\chi$ of $M_{k,\chi}$ on $B$. We say that $g$ *has expansion $f$ on $W$* if there is a finite set $S \subseteq \mathsf{X}$ with the following properties. For $\chi \notin S$ the pullback $p_e^* f_\chi$ is zero. On $W$, in the trivialisation of $L_G^k$ on $G_e$ by $p_e^*L^k$ that $U$ gives, we have $g = \sum_{\chi \in S} p_e^* f_\chi \cdot t_\chi$, where $t_\chi$ is the torus coordinate of $\chi$. A section $s$ of $L_G^k$ *has expansion $f$ on $G_e$* if each $s_i$ has expansion $f$ on $\pi_e^{-1}(G^i)$.

Lean: `GlobalTheory.MumMult.ChartExpOn` (also `ReciprocityTheory.ChartRestriction.G.Out.UnifPre.ExpandsAt`, the second notion).

**Definition 4.20.4 (Multiplier).** Let $b$ be a formal endomorphism and $N \geq 1$. A *multiplier of exponent $N$* for $b$ is a family of functions $m_e(i, i')$ on $W_e(i, i')$ with these properties.

1. Let $k \geq 3$, $f$ an integral theta family of level $k$, and $s$ a section of $L_G^k$ that has expansion $f$ on every $G_e$. Then there is an integral theta family $F$ of level $Nk$ such that $m_e(i, i')^k \cdot (\pi_e b_e)^* s_i$ has expansion $F$ on $W_e(i, i')$ for all $e, i, i'$.
2. There is a point $x$ of $B$ over the closed point such that $m_0(i, i')$ is a unit at every $y \in W_0(i, i')$ with $p_0(y) = x$, for all $i, i'$.

Lean: `GlobalTheory.MumMult.MultAct` (also `GlobalTheory.MumMult.LeadPt`, condition 2).

**Definition 4.20.5 (Admissible exponent).** Let $a$ be an endomorphism of $B$, $h, h'$ endomorphisms of $\mathsf{X}$ and $N \geq 1$. We say that $N$ is *admissible* if:

1. the bundle $L^N \otimes a^*L^{-1}$ is relatively ample on $B$ over $R$;
2. let $\kappa : \mathsf{X} \to K^\times$ be even with $\kappa(0) = 1$, with values in $R$, and with $\kappa(x+y+z)\kappa(x)\kappa(y)\kappa(z) = \kappa(x+y)\kappa(x+z)\kappa(y+z)$; suppose that for all $y, z$ the ratio of $\kappa(h(y)+z)\kappa(y)\kappa(h'(z))$ and $\kappa(y+h'(z))\kappa(h(y))\kappa(z)$ is a unit of $R$; then $\kappa(y)^N \in R \cdot \kappa(y)\kappa(h(y))$ for every $y$.

A section $\sigma_0$ of $L^N \otimes a^*L^{-1}$ is *nonzero at* a point $x$ of $B$ if it does not vanish at $x$ in any trivialisation.

Lean: `GlobalTheory.MumMult.PosN` (also `GlobalTheory.MumMult.NonzeroAt`, the second notion).

The cubic identity says that $\kappa$ is a quadratic function. Condition 2 bounds the growth of $\kappa \circ h$ by a power of $\kappa$. It is what makes the theta series of the multiplier converge.

### The multiplier

**Theorem 4.20.6 (Multiplier from a section).** Let $a, a', h, h'$ be endomorphism data for $D$ and $b$ a formal endomorphism over $(a, h')$. Let $N \geq 1$ be admissible, $\sigma_0$ a section of $L^N \otimes a^*L^{-1}$ on $B$, and $x$ a point of $B$ over the closed point at which $\sigma_0$ is nonzero. Then $b$ has a multiplier of exponent $N$.

Lean: `GlobalTheory.MumMult.exists_mult_of_posN` (also `GlobalTheory.T.exists_mumfordMultiplier_of_section`, a second name).

*Proof.* *Step 1: a family of coefficients.* By an input that uses the admissibility of $N$ and the section $\sigma_0$, there is a family $(g_\beta)_{\beta \in \mathsf{X}}$ of sections of twists of $L^N \otimes a^*L^{-1}$ on $B$ with these properties: for each $e$, all but finitely many $g_\beta$ vanish modulo $\mathfrak{m}^{e+1}$; the family satisfies the functional equation of its level; $g_\beta$ vanishes on the closed fibre for $\beta \neq 0$; and $g_0 = \sigma_0$ on the closed fibre.

*Step 2: the multiplier.* Fix $e$. Since $q_e \circ b_e = a \circ q_e$, a gluing lemma gives a section $\tau_e$ of $L_G^N \otimes b_e^* L_G^{-1}$ on $G_e$ whose expansion is $(g_\beta)$. Let $m_e(i, i')$ be $\tau_e$ read in the trivialisations $i'$ of $L_G^N$ and $i$ of $b_e^*L_G^{-1}$ on $W_e(i, i')$.

*Step 3: the action on sections.* Let $k \geq 3$, $f$ and $s$ be as in condition 1. By an input, there is a small family $\rho$ that satisfies the functional equation and is the expansion of $b_e^* s$ on every $G_e$. By a second input, the product of $(g_\beta)$ to the power $k$ with $\rho$ is a small family $F'$ that satisfies the functional equation of level $Nk$ and is the expansion of $\tau_e^k \otimes b_e^* s$. By a third input, $F'$ comes from an integral theta family $F$ of level $Nk$. Locally at a point $z$ of $W_e(i, i')$, read in a trivialisation at $z$, the product $m_e(i,i')^k \cdot (\pi_e b_e)^* s_i$ equals the value of $\tau_e^k \otimes b_e^* s$. The reason is that the transition factor of $b_e^*L_G^{-1}$ appears with power $k$ in $m_e(i,i')^k$ and its inverse appears in $(\pi_e b_e)^* s_i$. A last input turns these local identities into the expansion $F$ on $W_e(i, i')$.

*Step 4: the unit.* Let $y \in W_0(i, i')$ with $p_0(y) = x$. By Step 1, only the term $\beta = 0$ of the expansion of $\tau_0$ is nonzero on the closed fibre. So the value of $\tau_0$ at $y$ is $\sigma_0(x)$ times a unit. Since $\sigma_0$ is nonzero at $x$, $\tau_0$ is a unit at $y$, and so is $m_0(i, i')$. $\square$

**Theorem 4.20.7 (Multiplier on the charts).** Let $a, a', h, h'$ be endomorphism data for $D$ and $b$ a formal endomorphism over $(a, h')$. Then there are $N \geq 1$ and functions $m_e(i, i')$ on $W_e(i, i')$ with these properties.

1. For every $k \geq 3$ and every section $s$ of $L_G^k$ there is an integral theta family $F$ of level $Nk$ such that $m_e(i, i')^k \cdot (\pi_e b_e)^* s_i$ has expansion $F$ on $W_e(i, i')$ for all $e, i, i'$.
2. There is a point $y \in \pi_0^{-1}(G^{i'})$ for some $i'$ such that $m_0(i, i')$ is a unit at $y$ for all $i, i'$ with $y \in W_0(i, i')$.

Lean: `GlobalTheory.MumMult.chart_main` (also `GlobalTheory.T.mumfordMultiplier_thickening_chart_sections`, a second name).

*Proof.* By an input, there are an admissible $N \geq 1$, a section $\sigma_0$ of $L^N \otimes a^*L^{-1}$ and a point $x$ of $B$ over the closed point at which $\sigma_0$ is nonzero. The theorem on the multiplier from a section gives a multiplier $m$ of exponent $N$. For condition 1, let $s$ be a section of $L_G^k$ with $k \geq 3$. By an input, $s$ has an integral theta family $f$ of level $k$ as its expansion on every $G_e$, and condition 1 of the multiplier applies. For condition 2, an input turns condition 2 of the multiplier into a point $y$ of the closed fibre in some $\pi_0^{-1}(G^{i'})$. $\square$

**Theorem 4.20.8 (Sections moved by a formal endomorphism).** Let $a, a', h, h'$ be endomorphism data for $D$ and $b$ a formal endomorphism over $(a, h')$. Then there is $N \geq 1$ with the following property. For every $k \geq 3$ there are a map $S$ from sections of $L_G^k$ to sections of $L_G^{Nk}$ and functions $c_e(i, i')$ on $W_e(i, i')$ such that:

1. $\pi_e^*(S(s))_{i'} = c_e(i, i') \cdot (\pi_e b_e)^* s_i$ on $W_e(i, i')$ for all $e$, $s$, $i$ and $i'$;
2. there is a point $y \in \pi_0^{-1}(G^{i'})$ for some $i'$ such that $c_0(i, i')$ is a unit at $y$ for all $i, i'$ with $y \in W_0(i, i')$.

Lean: `GlobalTheory.MumMult.main` (also `GlobalTheory.T.mumfordSections_multiplier_thickenings`, a second name).

*Proof.* Take $N$, $m$ and $y$ from the theorem on the multiplier on the charts, and fix $k \geq 3$. For each section $s$ of $L_G^k$ let $F_s$ be the family of level $Nk$ from condition 1. Since $Nk \geq 1$ and $U$ is a uniformisation, an input gives a section $S(s)$ of $L_G^{Nk}$ that has expansion $F_s$ on every $G_e$. Put $c_e(i, i') = m_e(i, i')^k$. On $W_e(i, i')$ the functions $\pi_e^*(S(s))_{i'}$ and $c_e(i,i') \cdot (\pi_e b_e)^* s_i$ have the same expansion $F_s$. By an input, two functions on an open of $G_e$ with the same expansion are equal. This gives 1. A power $m^k$ with $k \geq 1$ is a unit exactly where $m$ is a unit, which gives 2. $\square$

The map $S$ is chosen section by section. The theorem does not claim that it is linear. Only the identity 1 and the point $y$ are used later.

**Remark 4.20.9 (Formalization).** The second names are wrappers proved by a `first | exact` tactic. The theorem on the multiplier on the charts calls the wrapper of the first theorem, and the last theorem calls the wrapper of the second. In the first theorem ([ExistsMumfordMultiplierOfSection.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsMumfordMultiplierOfSection.lean#L74)), Steps 1 to 3 are `GlobalTheory.T.exists_mumford_formal_section_coefficient_family`, `GlobalTheory.TwFamGlue.glue`, `GlobalTheory.T.exists_pullback_integralExpansion_formalEndomorphism`, `GlobalTheory.T.multiplier_power_mul_pullback_small_family`, `GlobalTheory.TwBack.exists_intFam` and `GlobalTheory.MumMult.chartExpOn_of_tExp`. The cancellation of transition factors in Step 3 is the local lemma `gs_pow_mul_pull` at line 24, and Step 4 uses the private lemma `isUnit_gs_iff_mem`. The inputs of the second theorem ([MumfordMultiplierThickeningChartSections.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MumfordMultiplierThickeningChartSections.lean#L23)) are `GlobalTheory.T.exists_mumfordMultiplier_exponent_nonzero_section`, `GlobalTheory.T.exists_integralThetaExpansion_of_section_power_ge_three` and `GlobalTheory.T.exists_closedFibre_chart_point_mumfordMultiplier_nonzero`. The inputs of the last theorem ([MumfordSectionsMultiplierThickenings.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MumfordSectionsMultiplierThickenings.lean#L19)) are `GlobalTheory.T.exists_expandsAt_section_uniformised` and `GlobalTheory.T.eq_of_same_expansion_thickening_open`; its last step tries four forms of the lemma `Scheme.basicOpen_pow` in a `first` block, one for each possible argument pattern. The trivialising cover of $L_G$ is indexed by maps `Fin 1 → U.LG.L.ι`, the opens $W_e(i, i')$ are `GlobalTheory.MumMult.multW` and the bundle in condition 2 of endomorphism data is built in `RosatiAdj`, with condition 4 being `TauBal`. Condition 2 of endomorphism data, condition 3 for $h$ and condition 4 enter only through the inputs; the definition of a formal endomorphism uses only $a$ and $h'$. We did not open the proofs of the inputs. The reading of the admissibility condition as a growth bound is ours.
