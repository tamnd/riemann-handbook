---
title: Normal models with Cartier divisors along traits
decls:
  - GlobalTheory.T.unitary_exists_normalModel_effCartier_along_traits
  - GlobalTheory.UPoinc.exists_zhModel_effCartier_orders
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Normal models with Cartier divisors along traits

This section gives the input of [the theorem on the boundary ideal over a component](/entry/exists-unitary-theta-setup-ideal-over-component/) of Section 4. Over a theta setup $X_1$ we find a normal model $Y$ with a proper map to $Z_M$ and an effective Cartier divisor $D$ on $Z_Y$. The divisor lies over the boundary of $Z_C$, and along each boundary trait its ideal has order $\iota\varphi$ for one integer $\iota \ge 1$. The divisor is glued from local ratios of theta functions. At each point of the model one ratio of a finite tuple is integral, and its order along each trait is the least order in the tuple. We use the notation of Sections 2 to 4. $C$ is a minimal compactification of $X_F$, $X_1$ is a theta setup for $C$ with the model $M$ over $(o_1, \Omega_1)$, the scheme $Z_M$, the point $\mathrm{pt}_M$ and the finite map $\pi : Z_M \to Z_C$.

**Definition 7.7.1 (Model over a base).** Let $o$ be a ring and $\Omega$ a field that is an $o$-algebra.

1. A *model* $Y$ over $(o, \Omega)$ is an integral scheme $Z_Y$ with a map $s : Z_Y \to \operatorname{Spec} o$ that is separated, locally of finite type and quasi-compact, and a point $\mathrm{pt}_Y : \operatorname{Spec} \Omega \to Z_Y$ over $o$ whose image is the generic point. In addition, each $x \in \Omega$ is the value at $\mathrm{pt}_Y$ of a section $f$ of $\mathcal{O}_{Z_Y}$ over some nonempty open set $U$. So the function field of $Z_Y$ is $\Omega$, and for each $z \in Z_Y$ we view the local ring $\mathcal{O}_{Z_Y, z}$ as a subring of $\Omega$.
2. Let $Y'$ be a model over $(o, \Omega')$ and $\phi : \Omega \to \Omega'$ a map of $o$-algebras. A map $f : Z_{Y'} \to Z_Y$ is a *map of models over $\phi$* if $f \circ \mathrm{pt}_{Y'} = \mathrm{pt}_Y \circ \operatorname{Spec} \phi$.
3. Let $(t_j)_{j \in J}$ be a family in $\Omega$. The index $i$ is a *divisor index at $z$* if $t_i \ne 0$ and $t_j / t_i \in \mathcal{O}_{Z_Y, z}$ for each $j \in J$. The model $Y$ *has divisors for $t$* if each point $z$ has a divisor index.

Lean: `GlobalTheory.ZH.RatModel` (also `GlobalTheory.ZH.RatModel.IsHom`, `GlobalTheory.ZH.RatModel.Div`, `GlobalTheory.ZH.RatModel.HasDiv`).

Suppose that $Y$ has divisors for a finite family $t$. Near each point $z$, take a divisor index $i$ at $z$ and the element $t_i$ as a local equation. These local equations give one Cartier divisor on $Z_Y$. Two divisor indices $i, i'$ at $z$ give $t_i / t_{i'}$ and $t_{i'} / t_i$ both in $\mathcal{O}_{Z_Y, z}$, so this ratio is a unit and the local equations agree. This is the divisor of a linear system with no base points, as in [the algebraic theory of theta functions](/learn/theta-functions-cm/#the-algebraic-theory-of-theta-functions).

**Theorem 7.7.2 (Normal model with Cartier divisor along traits).** Let $E$, $H$ and $D$ be as in Section 1 with $p + q \ge 1$, let $\varphi$ be a polarized fan in rank at most $\min(p, q)$, let $C$ be a minimal compactification of $X_F$, and let $X_1$ be a theta setup for $C$ with $Z_M$ projective over $o_1$. Then there are an integer $\iota$, a model $Y$ over $(o_1, \Omega_1)$, a map $\pi_Y : Z_Y \to Z_M$ and an effective Cartier divisor $D$ on $Z_Y$ with:

1. $\iota \ge 1$;
2. $\pi_Y$ is a map of models over the identity of $\Omega_1$, and $\pi_Y$ is proper;
3. $Z_Y$ is normal;
4. for each $y$ in the support of $D$, the point $\pi(\pi_Y(y))$ is not in the image of $i$;
5. the ideal of $D$ has order $\iota\varphi$ through $\pi \circ \pi_Y$ over all of $Z_Y$.

Lean: `GlobalTheory.UPoinc.exists_zhModel_effCartier_orders` (also `GlobalTheory.T.unitary_exists_normalModel_effCartier_along_traits`, a second name).

Here "order $\iota\varphi$ through $\pi \circ \pi_Y$ over $Z_Y$" is the notion of Section 4, with the map $i : X_F \to Z_C$ and the set $A = Z_Y$.

*Proof.* There are five steps.

1. A lemma on theta tuples gives $\iota \ge 1$, a finite set $K$, and for each $k \in K$ a finite nonempty set $J_k$ and a tuple $(t_{k,j})_{j \in J_k}$ of nonzero elements of $\Omega_1$. It also gives a local property of least orders. Let $Y$ be a model with an admissible structure over a dense open $U_0$. For each point $x$ of $Z_Y$ there is $k \in K$ with this property. Take a boundary trait $T$ and a map $\xi$ from the spectrum of $V_T$ whose generic point lies in $U_0$ over $y_T$ and whose closed point specializes to $x$. Then each $t_{k,j}$ has order at least $\iota\varphi(\beta_T)$ along $\xi$, and some $t_{k,j}$ has order exactly $\iota\varphi(\beta_T)$.
2. A lemma on admissible theta models, applied to the theta system $S$ of $X_1$, its real point, the size condition and the projective model $M$, gives a model $Y$ over $(o_1, \Omega_1)$ with a map $\pi_Y$ of models over the identity. The map $\pi_Y$ is proper, $Y$ is admissible over an open $U_0$, and $Y$ has divisors for each tuple $t_k$. Admissibility includes that $Z_Y$ is normal.
3. A gluing lemma for local tuples, applied with the local property of step 1 at $Y$, gives an effective Cartier divisor $D$ on $Z_Y$. Along each trait $\xi$ as in step 1, the pullback of the ideal of $D$ is $(\varpi^a)$ with $a = \iota\varphi(\beta_T)$. Locally, $D$ is the divisor of the tuple $t_k$ that step 1 gives at the point.
4. A lemma on the support of trait divisors shows that the support of $D$ maps outside $i(X_F)$ under $\pi \circ \pi_Y$. A point of $Z_Y$ over $i(X_F)$ has a neighbourhood in which the tuples have no common zero.
5. A lemma on orders over the moduli scheme moves the orders of step 3 to all traits through $\pi \circ \pi_Y$ in the sense of Section 4. This gives property 5.

Property 3 comes from step 2. This gives $\iota$, $Y$, $\pi_Y$ and $D$. $\square$

The divisor $D$ lives on $Z_Y$, not on $Z_M$, and its ideal need not descend to $Z_M$ in general. [The theorem on the descent of a power of a divisor](/entry/exists-ideal-sheaf-descending-divisor-power/) of Section 4 replaces $D$ by a multiple whose ideal comes from $Z_M$.

**Remark 7.7.3 (Formalization).** The proof is in [UnitaryExistsNormalModelEffCartierAlongTraits.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryExistsNormalModelEffCartierAlongTraits.lean#L15). The `T.*` names are wrappers that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. `RatModel`, `Div`, `HasDiv` and `IsHom` are in [InducedModelMorphismCompStructureMap.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/InducedModelMorphismCompStructureMap.lean#L58), at lines 58, 377, 379 and 641. The local ring at $z$ in `Div` is `M.O z`, a subring of $\Omega$. The divisor $D$ is an `EffCartierData` on `Y.Z`. The five steps apply `T.exists_finite_theta_tuples_least_orders_unitary`, `Poinc.exists_admissible_projective_theta_model`, `T.exists_effectiveCartier_gluing_localTuples`, `T.unitaryTraitDivisor_support_not_mem_moduli_range` and `T.divisor_orders_all_traits_over_moduli`. These lemmas have no entries in this chapter, and we use only their statements. Normality is the field `normal` of the first part of the admissibility hypothesis. We have not unfolded `admitted`, `IsEE`, `ZHOut`, `Lies`, `UOrdGe`, `UOrdEq` or `EffCartierData`. In step 1 the structure of $Y$ over $U_0$ is a triple `U₀`, `EE`, `out`, and "lies over $y_T$" is the predicate `Lies` through `out.u₀`.
