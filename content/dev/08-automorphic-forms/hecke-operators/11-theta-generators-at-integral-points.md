---
title: Theta generators at integral points
decls:
  - GlobalTheory.HkIntegral.theta_unit
  - GlobalTheory.T.sum_symmetricTranslates_thetaPullback_extends
  - GlobalTheory.HkIntegral.RegSum.reg_of_isTranslSum
  - GlobalTheory.HkIntegral.RegSum.reg_of_isTransl
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta generators at integral points

This section and the next show that the Hecke operators of the two sections before keep integrality at the places of the coefficient field that do not lie over the Hecke prime. The method is to work with points, not with sections. This section treats the theta generator. If a Hecke point $z$ of an integral point $y$ is written as an integral point $y'$ changed by a diagonal $t$, the theta entry $t_0$ of $t$ is a unit. The tool is the theta group: the pullback of a theta generator along a Hecke isogeny is a sum of symmetric translates of a theta generator, and such sums extend over integral models ([the Heisenberg group](/learn/groups/#the-heisenberg-and-metaplectic-groups)). The classical model is the theory of theta groups and symmetric theta structures of Mumford.

### Integral framed points

We keep the notation of [the section on Hecke operators on sections](/entry/hecke-transform-of-point-laws/): $X$ is the moduli space of abelian schemes with $\mathcal{O}_E$-action, polarization and level prime to $M$, $F_c$ is the coefficient field, and a framed point carries tangent bases $u_{\tau,j}$ and a theta generator $s$. Let $T$ be a complete discrete valuation ring with fraction field $K$ and normalized valuation $v_T$, and let $\iota : F_c \to K$ be a field map.

**Definition 6.11.1 (Integral framed point).** An *integral framed point* over $(T, \iota)$ is a framed point $y$ over $K$ that comes from a test ring and that has an *integral datum*: a semi-abelian scheme $\mathcal{G}$ over $T$ with $\mathcal{O}_E$-action whose generic fibre is $A_y$ with its structures, such that each tangent basis $u_\tau$ is a $T$-basis of the $\tau$-part of $\mathrm{Lie}(\mathcal{G})$, and $s$ is the restriction of a generator $\theta$ of the theta line of $\mathcal{G}$ over $T$. The point is *good* if it has an integral datum with $\mathcal{G}$ proper, that is, an abelian scheme. The point is *algebraic* if the residue field of $T$ is finite.

A *class* of integral points is a condition on integral framed points over all pairs $(T, \iota)$. We use two classes: the *good class*, and the *full class*, which holds for every integral point. For a map $k : K \to \Omega$ to a field, the base change of a framed point $y$ along $k$ is written $y_\Omega$. If $t = (t_0, (t_{\tau,j}))$ is a tuple of units, we write $z = t \cdot y$ when $z$ comes from $y$ by the triangular change with diagonal $t$, as in the weight law.

### Translates of the theta generator

Let $y$ be an integral framed point with integral datum $\mathcal{G}$ and let $N \ge 1$ be an integer. Let $L$ be the theta line bundle on the fibre $A_y$, with its rigidification. There is a normalized isomorphism $[N]^* L \cong L^{N^2}$. A *symmetric translate* of $s$ at level $N$ is a section $F$ of $L^{N^2}$ of the form $F = U \cdot [N]^* s$, where $U$ is a symmetric lift to the theta group of $L^{N^2}$ of a point $t'$ of $A_y$ with $N^2 t' = 0$. The section $F$ *extends* if it is the restriction of a section of $\mathcal{L}^{N^2}$ over the integral datum, where $\mathcal{L}$ is the theta line of $\mathcal{G}$ ([the Weil representation](/learn/theta/#the-weil-representation), [the Heisenberg group](/learn/groups/#the-heisenberg-and-metaplectic-groups)).

**Lemma 6.11.2 (One translate extends).** Let $y$ be an integral framed point over $(T, \iota)$ with integral datum $\mathcal{G}$, and suppose that $\mathcal{G}$ has a uniformization with a torsion isomorphism. Let $N$ be an integer that is a unit in $T$. Then every symmetric translate of $s$ at level $N$ extends over $\mathcal{G}$.

Lean: `GlobalTheory.HkIntegral.RegSum.reg_of_isTransl`.

*Proof.* Let $F = U \cdot [N]^* s$. The generator $s$ is the restriction of a generator $\theta$ of $\mathcal{L}$, so $F$ is the restriction to the generic fibre of the translate $U \cdot [N]^* \theta$, formed with the same point $t'$ on the generic fibre. Since $N$ is a unit in $T$, the $N^2$-torsion of $\mathcal{G}$ is étale over $T$, and the torsion isomorphism identifies it with the $N^2$-torsion of the uniformization. The input on uniformized models says that $U \cdot [N]^* \theta$ is then regular on the model. In the uniformization, $\theta$ is a theta series, and this input is the statement that a symmetric translate of a theta series, with its normalizing factor, is again a theta series with integral coefficients. So $F$ extends. $\square$

**Lemma 6.11.3 (Sums of translates extend).** Under the hypotheses of the last lemma, every finite sum of symmetric translates of $s$ at level $N$ extends over $\mathcal{G}$.

Lean: `GlobalTheory.HkIntegral.RegSum.reg_of_isTranslSum` (also `GlobalTheory.T.sum_symmetricTranslates_thetaPullback_extends`, a second name).

*Proof.* Let $F = \sum_{i} F_i$ with each $F_i$ a symmetric translate. By the last lemma each $F_i$ is the restriction of a section $\sigma_i$ of $\mathcal{L}^{N^2}$ over $\mathcal{G}$. Restriction is additive, so $F$ is the restriction of $\sum_i \sigma_i$. $\square$

### The theta entry of a Hecke change

Let $(\mathfrak{P}, p_0)$ be split off, as in the section on Hecke operators on sections. For framed points $y$ and $z$ over $K$, say that $z$ is a *Hecke point of $y$ over $K$* if there is a Hecke isogeny $\psi : A_y \to A_z$ of type $(\mathfrak{P}, p_0, i)$ for some $i$, defined over $K$, with the laws of a Hecke point: the Weil pairing law, the level law, the tangent law and the trace law for theta generators.

**Lemma 6.11.4 (Theta entry is a unit).** Let $p_0$ be prime and a unit in $T$, and let the residue field of $T$ be finite. Let $y$ and $y'$ be integral framed points over $(T, \iota)$, let $z$ be a Hecke point of $y$ over $K$, and let $z = t \cdot y'$ for a tuple $t$ of units of $K$. Then $v_T(t_0) = 0$.

Lean: `GlobalTheory.HkIntegral.theta_unit`.

*Proof.* There is a finite extension $T_1$ of $T$, with valuations scaled by some $r > 0$, over which every model of the abelian varieties in play has a uniformization with a torsion isomorphism, and over which $y$, $y'$ and $z$ have base changes $y_1$, $y'_1$ and $z_1$ with the same relations. Since $v_{T_1}(t_0) = r\, v_T(t_0)$, it is enough to prove $v_{T_1}(t_0) = 0$. We prove two bounds.

Lower bound. The Hecke isogeny $\psi$ and the isogeny of the integral data extend to a map of models. The trace law says that the theta generator of $z$ is the trace of the theta generator of $y$ along $\psi$. So the pullback of $t_0 s_{y'}$ along $\psi$ is a sum of symmetric translates of $s_y$ at level $p_0$. By the lemma on sums of translates, with $N = p_0$, this sum extends over the integral datum of $y$. Since $s_{y'}$ is the restriction of a generator of the theta line of the integral datum of $y'$, and $p_0^2$ is a unit, the scalar $t_0$ is integral: $v_{T_1}(t_0) \ge 0$.

Upper bound. The orthogonality relation of the theta trace gives an isogeny $\psi_2 : A_{z} \to A_y$ in the other direction and a scalar $b \in K$, such that the pullback of $b\, s_y$ along $\psi_2$ is a sum of symmetric translates of $s_{y'}$ at level $p_0^2$, and
$$t_0\, b = p_0^{\,m}\, \zeta$$
for an integer $m$ and a root of unity $\zeta$ of order dividing $p_0$. By the lemma on sums of translates, applied to $y'$ with $N = p_0^2$, the sum extends over the integral datum of $y'$, and so $b$ is integral. Then $b \ne 0$, $v_{T_1}(p_0) = 0$ since $p_0$ is a unit, and $v_{T_1}(\zeta) = 0$ since $\zeta^{p_0} = 1$. So
$$v_{T_1}(t_0) = -v_{T_1}(b) \le 0.$$
The two bounds give $v_{T_1}(t_0) = 0$. $\square$

**Remark 6.11.5 (Formalization).** The lemma on the theta entry is at line 242 of [IsUnitNatCastUp.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/IsUnitNatCastUp.lean#L242), with the two bounds `theta_low` (line 166) and `theta_high` (line 183). The module is named after the helper `isUnit_natCast_up` at line 217, which says that a unit stays a unit after a finite extension. An algebraic point is a point over a ring with finite residue field; `IntFr.IsAlg` does not depend on the point ([VAtVNeBot.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/VAtVNeBot.lean#L83)). The two lemmas on translates are in [SumSymmetricTranslatesThetaPullbackExtends.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/SumSymmetricTranslatesThetaPullbackExtends.lean#L60), lines 60 and 81. The second name of the lemma on sums is in [SumSymmetricTranslatesThetaPullbackExtendsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/SumSymmetricTranslatesThetaPullbackExtendsStatement.lean#L12); that file imports Mathlib twice (lines 1 and 3), and its proof tries three forms of `reg_of_isTranslSum` with `first`. The regularity of a single translate on a uniformized model, the extension of isogenies to models, the pullback along the isogeny in the other direction with its root of unity, and the existence of uniformized models after a finite extension are inputs from other modules; we did not unfold them here.
