---
title: The theta key scalar is a unit on integral models
decls:
  - GlobalTheory.KeyUnitModels.exists_chart_unit
  - GlobalTheory.KeyUnitModels.unitAt_local
  - GlobalTheory.KeyUnitModels.unitAt_valuation
  - GlobalTheory.KeyUnitModels.keyUnitOnModels
  - GlobalTheory.T.thetaKeyScalar_isUnit_on_integralModels
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The theta key scalar is a unit on integral models

A polarized abelian variety with a rigidified symmetric line bundle, a theta section and a basis of its Lie algebra has a scalar attached to it: the key scalar. It changes by explicit powers when the section or the basis changes, it is $1$ for the classical theta function with characteristic and the standard basis, and over $\mathbb{C}$ its absolute value is fixed by the $L^2$ norm of the theta function and the covolume of the period lattice. This section proves that on an integral model of a moduli space the key scalar is a unit at every point with values in a valuation ring. In other words, the key scalar has no zeros and no poles, also at the boundary. The result is used in [the covolume of the second top lattice](/entry/top-covol-slim2-use-alt-alt/) ([heights](/learn/arakelov/#heights)).

We keep the moduli data of the previous sections: a CM field $E$ with host data $H$, a datum $\mathcal{D}$ of signature $(p, q)$, a level $l$, a moduli space $X_o$ with coefficients $c$ in a number field $F$, and a model $Y$ of $X_o$ over a ring $O$ with a map $\beta : O \to F$. The model is a proper normal scheme $Y_X$ over $O$ with a universal semiabelian scheme $Y_t$, and the generic part $j : X_{o,F} \to Y_X$ is a dense open immersion.

**Definition 3.21.1 (Key inputs and key rules).** Let $K$ be a field of characteristic $0$. A *key input* $x$ over $K$ consists of a polarized abelian variety $P$ of dimension $g \ge 1$ over $K$ with its line bundle $L$, a generator of $L$ at the origin (the rigidification), a section $\theta$ of $L$ that is nonzero on fibres, and a basis $v_1, \dots, v_g$ of the Lie algebra. A *key rule* $\kappa$ assigns to every key input $x$ over every such $K$ a unit $\kappa(x) \in K^\times$. It is a *key rule in the strict sense* if:

1. if $x'$ differs from $x$ by $\theta' = a\theta$ and $v'_i = \sum_k M_{ik} v_k$, then
$$a^8 \kappa(x') = (\det M)^4 \kappa(x);$$
2. $\kappa$ commutes with base change along field maps $K \to K'$;
3. if $x$ is defined over a discrete valuation ring $R$ with fraction field $K$, then $\kappa$ of the generic fibre is a unit $u \in R^\times$, and $\kappa$ of the fibre over every surjection $R \to k$ onto a field of characteristic $0$ is the image of $u$;
4. over $\mathbb{C}$, if $P = \mathbb{C}^g/(\mathbb{Z}^g + \tau\mathbb{Z}^g)$, $\theta$ is the theta function with characteristic $(a, b) \in \{0, \tfrac12\}^{2g}$ and $v_i$ is the differential $(2\pi i)^{-1}\partial/\partial z_i$, then $\kappa(x) = 1$;
5. over $\mathbb{C}$, for a uniformization with hermitian form $H$, theta function $\vartheta$, differentials $W$ of the $v_i$ and fundamental domain $D$,
$$|\kappa(x)|\, n_\theta^4\, n_\eta^2 = (2\pi)^{2g},$$
where $n_\theta$ is the mean of $|\vartheta(z)|^2 e^{-\pi H(z, z)}$ over $D$ and $n_\eta = \mathrm{vol}(D) / (\pi^g |\det W|^2)$.

Part 5 says that the absolute value of the key scalar is fixed by the $L^2$ norm of the theta section and the norm of the Lie basis. Part 1 gives the change under the choices, and part 3 gives integrality at points of good reduction.

**Definition 3.21.2 (Units at valued points).** Let $V$ be a ring with a map $V \to K$. The key rule $\kappa$ is a *unit at* $(V, K)$ on $Y$ if the following holds for every $K$-point $y$ of $X_{o,F}$ and every $V$-point $\tilde y$ of $Y_X$ that extends $y$, every semiabelian scheme $t$ over $V$ with a map to $Y_t$ over $\tilde y$, every Lie basis $w$ of $t$, every section $\theta$ of its line bundle, and every key input $x$ over $K$ that is the generic fibre of $(t, \theta, w)$:

1. if $\theta$ generates the line bundle, then $\kappa(x)$ is the image of a unit of $V$, and for every $N$ divisible by $8$ the external power $\theta^{\boxtimes N}$ generates on the $N$-fold fibre power of $t$;
2. for every $N$ divisible by $8$, every generating section $\sigma$ of the external power line bundle and every $a \in V$ with $\theta^{\boxtimes N} = a\sigma$, the element $a\, \kappa(x)^{N/8}$ is the image of a unit of $V$.

The statement *the key scalar is a unit on models* says: for every key rule in the strict sense, every model $Y$ over a base ring with $p + q \ge 1$, a prime $p$, the level structure conditions at $p$, the uniformization condition, the arc condition and split fibres, $\kappa$ is a unit at $(V, K)$ when $V$ is a complete discrete valuation ring with fraction field $K$ of characteristic $0$, and when $V$ is the unit ball of a complete algebraically closed nonarchimedean field $K$ of characteristic $0$.

Here $\beta$ is a *base ring* if it is injective and its image contains every algebraic integer of $F$. The uniformization condition gives uniformizations of the semiabelian scheme over complete local rings, the arc condition gives formal arcs into the boundary, and split fibres says that the torus parts of the fibres split after a finite separable extension. We do not unfold them.

### The chart unit

A *chart* $M$ of $Y$ is an affine open $U_M \subset Y_X$ with theta data over it, such that every point $z$ of $U_M$ in the generic part has key inputs *read in the chart*. We do not unfold charts.

**Lemma 3.21.3 (Norms in normal form).** Let $\kappa$ be a key rule in the strict sense and $x$ a key input over $\mathbb{C}$ in normal form with period matrix $\tau$, a matrix $M_x$, a half characteristic $(a, b)$ and a constant $c_0 \ne 0$. If $C > 0$ and
$$C^{-1} \le |\det M_x| / |c_0|^2 \le C,$$
then $|\kappa(x)| \le C^4$ and $|\kappa(x)^{-1}| \le C^4$.

*Proof.* A rescaling lemma gives a key input $x_0$ in the normal form with constant $1$, and part 1 of the key rule relates $\kappa(x)$ to $\kappa(x_0)$ by $c_0$ and $\det M_x$. Part 4 gives $\kappa(x_0) = 1$. So
$$|\kappa(x)| = \bigl(|\det M_x| / |c_0|^2\bigr)^4,$$
and both bounds follow. $\square$

**Lemma 3.21.4 (Chart unit).** Let $W$ be a valuation subring of $F$ and $Y$ a model of $X_o$ over $W$ with $p + q \ge 1$, push invertible line bundle, the uniformization condition, the arc condition and split fibres. Let $\kappa$ be a key rule in the strict sense and $M$ a chart. Then there is a unit $u$ on $U_M$ such that for every field $K$ of characteristic $0$, every $K$-point $z$ of $U_M$ in the generic part and every key input $x$ of $z$ read in the chart,
$$\kappa(x) = u(z).$$

Lean: `GlobalTheory.KeyUnitModels.exists_chart_unit`.

*Proof.* *Generic unit.* An input lemma gives a nonempty open $W_0 \subset U_M$ in the generic part and a unit $f_0$ on $W_0$ with $\kappa(x) = f_0(z)$ for every point $z$ of $W_0$ and every key input $x$ of $z$ read in the chart.

*Extension.* The field $F$ is a number field, so $F$ and $W$ are countable. The scheme $Y_X$ is proper and of finite type over $W$, so it is locally noetherian, and it is normal. So the ring of functions on the affine $U_M$ is a countable normal noetherian domain, and $W_0$ is dense in $U_M$. An input extension lemma says that restriction from $U_M$ to $W_0$ is injective, and that a function on $W_0$ extends to $U_M$ if its value at every point with values in a discrete valuation ring $R$, whose generic point lies in $W_0$, lies in $R$. We apply it to $f_0$ and to $f_0^{-1}$.

*Integrality.* An input lemma reduces integrality to two kinds of points.

1. *Arcs into the boundary.* An arc normal form lemma, which uses the arc condition and $p + q \ge 1$, gives near such an arc a normal form of the theta data with $C^{-1} \le |\det M_x|/|c_0|^2 \le C$ for a constant $C$. The previous lemma bounds $|f_0|$ and $|f_0^{-1}|$ by $C^4$ on the arc. A function that is bounded near the arc has no pole there.
2. *Points of good reduction.* At a point over a discrete valuation ring where the abelian scheme has good reduction, part 3 of the key rule gives that $\kappa$ is a unit of the ring.

*Conclusion.* So $f_0$ and $f_0^{-1}$ extend to functions $f$ and $f'$ on $U_M$. The product $f f'$ restricts to $1$ on $W_0$, so $f f' = 1$ by injectivity, and $u = f$ is a unit. For a point $z$ of $U_M$ in the generic part, the value $u(z)$ is read on $W_0$ after a restriction, and equals $\kappa(x)$. $\square$

### Units at valued points

**Theorem 3.21.5 (Units over a valuation subring).** Let $W$, $Y$ and $\kappa$ be as in the previous lemma. Let $V$ be a valuation ring with fraction field $K$ of characteristic $0$. Then $\kappa$ is a unit at $(V, K)$ on $Y$.

Lean: `GlobalTheory.KeyUnitModels.unitAt_local`.

*Proof.* Fix the data $y$, $\tilde y$, $t$, $w$, $\theta$ and $x$. An input lemma gives a chart $M$ that contains the image of the closed point of $\operatorname{Spec} V$; then $\tilde y$ maps into $U_M$. Let $u$ be the chart unit.

*A section nonzero on the closed fibre.* An input lemma gives a section $\theta_0$ of the line bundle of $t$ that is nonzero on the closed fibre.

*Generating sections.* Let $\theta$ generate. An input lemma on frames gives a key input $x'$ read in the chart and units $a$ and $d$ of $V$ with
$$d^4 \kappa(x) = a^8 \kappa(x'),$$
by part 1 of the key rule. Since $\kappa(x') = u(\tilde y)$ is a unit,
$$\kappa(x) = d^{-4} a^8 u(\tilde y)$$
is the image of a unit of $V$. For $N$ divisible by $8$, the fibre power of $t$ is flat and $\theta^{\boxtimes N}$ is nonzero on its closed fibre; with a generic line argument this shows that $\theta^{\boxtimes N}$ generates. This proves part 1.

*Part 2.* Let $N = 8k$, $\sigma$ generating and $\theta^{\boxtimes N} = a\sigma$. The section $\theta_0$ generates, so $\theta = b\theta_0$ for some $b \in V$. An input lemma gives a key input $x_0$ for $\theta_0$ over $K$, and part 1 of the key rule with $M = 1$ gives
$$b^8 \kappa(x) = \kappa(x_0) = u_0,$$
where $u_0$ is a unit by the previous step. Since $\theta_0^{\boxtimes N}$ and $\sigma$ both generate, $\theta_0^{\boxtimes N} = c'\sigma$ with a unit $c'$, and $a = b^N c'$. So
$$a\, \kappa(x)^{k} = c'\, (b^8\kappa(x))^k = c'\, u_0^k,$$
which is a unit. $\square$

**Theorem 3.21.6 (Units over the base).** Let $Y$ be a model of $X_o$ over a ring $O$ with a base ring $\beta : O \to F$, with $p + q \ge 1$, push invertible line bundle, the uniformization condition, the arc condition and split fibres. Let $\kappa$ be a key rule in the strict sense, and $V$ a valuation ring with fraction field $K$ of characteristic $0$. Then $\kappa$ is a unit at $(V, K)$ on $Y$.

Lean: `GlobalTheory.KeyUnitModels.unitAt_valuation`.

*Proof.* Fix $y$ and $\tilde y$. The point $y$ gives a field map $\iota : F \to K$, and $\tilde y$ gives a ring map $b_0 : O \to V$ with $b_0$ followed by $V \subset K$ equal to $\iota \circ \beta$.

*A valuation subring.* Let $W = \iota^{-1}(V) \subset F$. It is a valuation subring of $F$, since $V$ is a valuation ring: for $a \in F^\times$ either $\iota(a)$ or $\iota(a)^{-1}$ lies in $V$. The map $\beta$ factors through $W$, and $b_0$ factors through a map $W \to V$.

*Base change.* Let $Y_W$ be the base change of $Y$ along $O \to W$. Since $\beta$ is a base ring, an input lemma shows that $W$ is flat over $O$ and that $Y_W$ is a model of $X_o$ over $W$. The point $\tilde y$ lifts to a $V$-point of $Y_W$, and the map from $t$ to the universal scheme lifts as well. Input lemmas show that push invertibility, the uniformization condition, the arc condition and split fibres pass to $Y_W$. The previous theorem, applied to $Y_W$, gives the claim. $\square$

**Theorem 3.21.7 (The key scalar is a unit on models).** The key scalar is a unit on models.

Lean: `GlobalTheory.KeyUnitModels.keyUnitOnModels` (also `GlobalTheory.T.thetaKeyScalar_isUnit_on_integralModels`, a second name).

*Proof.* The level structure conditions include push invertibility. A complete discrete valuation ring is a valuation ring, so the previous theorem gives the first case. The unit ball of a complete algebraically closed nonarchimedean field $K$ is a valuation ring with fraction field $K$, by an input lemma, and the previous theorem gives the second case. $\square$

The boundary is handled by the normal form at arcs, where part 4 fixes the value, and the interior by part 3 at points of good reduction.

**Remark 3.21.8 (Formalization).** In the final theorem the prime $p$ and its primality are not used, and of the level structure conditions only push invertibility is used ([ThetaKeyScalarIsUnitOnIntegralModels.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyScalarIsUnitOnIntegralModels.lean#L233)). The key rule axioms, the predicate for units at valued points and the statement are in [FibreFramesOnModels.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/FibreFramesOnModels.lean#L15). The countability of the ring of sections on an affine open, which the extension lemma needs, is proved in the same file from finite type over the countable ring $W$. We have not unfolded charts, key inputs read in a chart, the arc normal form, the extension lemma, the model conditions and the inputs on frames. The second name is a wrapper.
