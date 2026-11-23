---
title: Base models
decls:
  - GlobalTheory.BaseModelEx.exists_baseModel
  - GlobalTheory.T.exists_base_model_semiAbelian
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Base models

A model of full level $N = n^J$, as in [the section on full level models](/entry/top-amp-exists/), receives the moduli spaces $X_l$ with $A = N$. The local model systems of [the section on local model systems](/entry/exists-local-systems-ample/) need models of the moduli spaces with $A = 1$, over rings in which only $n$ and the level $M$ are inverted. This section builds such a model, the *base model*, for every level $l_0$ with $A = 1$. It is the quotient of a model at level $A = N$, which lies finitely over the full level model, by the group of level changes. The quotient is taken with [the theorem on tame quotients](/entry/exists-quotient-model/) of the previous section. The base models are the first piece of the systems of the next section.

Fix a CM field $E$ with a host, a PEL datum $D$ and moduli spaces $X_l$ for all levels $l$, as in [the section on full level models](/entry/top-amp-exists/). For integers $S \ge 1$ and $A \ge 1$ write $R_{S,A} = \mathbb{Z}[\tfrac{1+\rho_0}{2}, \tfrac1S, \zeta_A] \subseteq \mathbb{C}$, so that $R_{n,N}$ is the base ring of a model of full level $N$. We use the projective models and the relation "above" of [the previous section](/entry/exists-quotient-model/). A model of a moduli space in the sense of [the section on local model systems](/entry/exists-local-systems-ample/) is in particular a projective model of $(X_{l,F}, G^{\mathrm{univ}})$.

For levels $l$ and $l'$ and a map $r : S' \to S$ with a map $\nu$ of PEL objects over $r$, we say that $(r, \nu)$ is *compatible with the level* if $\eta'(a)^{M'/M}$ maps to $\eta(a)$ and $\eta'_A(a)^{A'/A}$ maps to $\eta_A(a)$ for all $a \in \Lambda$.

Lean: `GlobalTheory.Models.LevComp`.

A projective model $C$ of $(U, t_0)$ *extends* an automorphism $r$ of $U$ with a map $\nu : t_0 \to t_0$ over $r$ if there are an automorphism $\rho$ of $X$ over $O$ and a map $\mu : t \to t$ over $\rho$ with $\rho \circ j = j \circ r$ and $\mu \circ m = m \circ \nu$.

Lean: `GlobalTheory.Models.Cpt.ExtendsAut`.

**Definition 5.9.1 (Base model).** Let $n$ be a prime, $N \ge 1$, $T$ a model of full level $N$ for $n$ with scheme $Z$ and semi-abelian scheme $G_T$, and $l_0$ a level with $A_0 = 1$ and modulus $M_0$. A *base model* of $T$ at $l_0$ consists of:

1. an inclusion $\beta : R_{nM_0, 1} \to K_{A_0}$ compatible with the inclusions into $\mathbb{C}$, and a projective model $C$ of $(X_{l_0}, G^{\mathrm{univ}})$ over $R_{nM_0,1}$ through $\beta$, with good semi-abelian scheme;
2. the extension property: every automorphism $r$ of $X_{l_0}$ over $K_{A_0}$, with a map $\nu$ of the universal object over $r$ that moves $\eta$ by an $\mathcal{O}_E$-linear map $g$ of $\Lambda$ (that is, $\nu \circ \eta(g(a)) = \eta(a)$ over $r$), is extended by $C$;
3. a level $l_1$ with the same $M$ and $\mathfrak{M}$ as $l_0$ and $A_1 = N$, an inclusion $\beta_1 : R_{nM_0, N} \to K_{A_1}$ compatible with the inclusions into $\mathbb{C}$, and a projective model $C_1$ of $(X_{l_1}, G^{\mathrm{univ}})$ over $R_{nM_0,N}$ through $\beta_1$;
4. the inclusion $b : R_{nM_0,1} \to R_{nM_0,N}$, a surjective map $r : X_{l_1} \to X_{l_0}$ with a map $\nu$ of universal objects over $r$, compatible with the level, such that $C_1$ is above $C$ over $(b, r, \nu)$;
5. the inclusion $b' : R_{n,N} \to R_{nM_0,N}$ and a map $q : X_1 \to Z$ over $\operatorname{Spec} b'$, such that the induced map $X_1 \to Z \times_{R_{n,N}} R_{nM_0,N}$ is finite, with a map of semi-abelian schemes $G_1 \to G_T$ over $q$, such that $q \circ j_1 = a_{l_1}$ and the composite of $m_1$ with $G_1 \to G_T$ is the map of the universal object of $X_{l_1}$ to $G_T$ given by $T$.

Lean: `GlobalTheory.Models.BaseModel`.

So a base model is a model at level $l_0$, a model at level $l_1$ above it, and a finite map from the second to the full level model. The model $C_1$ is the bridge: it is close to $T$ (finite over it), and it is a cover of $C$ (it lies above $C$).

**Theorem 5.9.2 (Base models exist).** Assume the homomorphism extension theorem (every homomorphism between the generic fibres of two semi-abelian schemes over a [[discrete valuation ring|MGM3CNJW9V]] extends uniquely), the laws, the second laws and the third laws. Let $E$ be a CM field with a host, $D$ a PEL datum with $p_D + q_D \ge 1$ and $X_l$ moduli spaces for all levels, and assume the level compatibility for $D$. Let $n$ be an auxiliary inert prime, $J \ge 1$, and $T$ a model of full level $n^J$ for $n$. Then for every level $l_0$ with $A_0 = 1$ there is a base model of $T$ at $l_0$.

Lean: `GlobalTheory.BaseModelEx.exists_baseModel` (also `GlobalTheory.T.exists_base_model_semiAbelian`, a second name).

*Proof.* Write $N = n^J$, $M_0$ for the modulus of $l_0$ and $l_1$ for the level $l_0$ with $A$ replaced by $N$. The rings $R_{nM_0,1}$ and $R_{nM_0,N}$ are [[Dedekind domains|7NPY2CN5KB]] of characteristic $0$, of finite type over $\mathbb{Z}$, with fraction fields $K_{A_0}$ and $K_{A_1}$ through inclusions $\beta$ and $\beta_1$. The inclusion $b : R_{nM_0,1} \to R_{nM_0,N}$ is [[finite|N9C4X7XKE4]], and $b' : R_{n,N} \to R_{nM_0,N}$ is [[étale|H84VHC8PX2]] and gives an open immersion on spectra, since it only inverts $M_0$.

*The model at level $l_1$.* A lemma on compact models gives a projective model $C_1$ of $(X_{l_1}, G^{\mathrm{univ}})$ over $R_{nM_0,N}$ and a map $q : X_1 \to Z$ over $\operatorname{Spec} b'$, finite onto the base change of $Z$, with a map $G_1 \to G_T$, compatible with $a_{l_1}$ and with the maps from the universal object. It also shows that $G_1$ is quasi-projective over $R_{nM_0,N}$. Since $T$ is good and $G_1$ is the pullback of $G_T$ along $q$, the third laws (base change of split extensions) show that $G_1$ is good.

*The group.* The level compatibility for $l_0 \mid l_1$ gives a surjective map $r : X_{l_1} \to X_{l_0}$ over $K_{A_0} \subseteq K_{A_1}$, finite and étale after base change, compatible with the level. A lemma on level quotients shows that $X_{l_0}$ is the quotient of $X_{l_1}$ by a finite group $\Gamma$ through $r$, with an injective action $\rho_0$ on $X_{l_1}$ and $\tau_0$ on the universal semi-abelian scheme. Each element acts through a symplectic similitude $g$ of $\Lambda$ and a field automorphism $\sigma$ of $K_{A_1}$ that fixes $K_{A_0}$, and $\nu$ is invariant.

*The action on the model.* Every element of $\Gamma$ extends to $Z$, by the condition on automorphisms in the model of full level $T$. Since $b'$ is an open immersion and $n M_0$ is a unit in $R_{nM_0,N}$, this automorphism of $Z$ restricts to the base change of $Z$, and a lemma on actions, which uses the homomorphism extension theorem, extends it to actions $\rho$ on $X_1$ and $\tau$ on $G_1$, compatible with $j_1$ and $m_1$.

*Tameness.* Let $x$ be a point of $X_1$ with values in a field. If an element $\gamma$ of $\Gamma$ fixes $x$, then its field part $\sigma$ is the identity, since $\gamma$ fixes the image of $x$ in $\operatorname{Spec} R_{nM_0,N}$. Then $\gamma$ is a level change $g$ of finite order, and a lemma on fixed fibres shows that $\tau(\gamma)$ is the identity on the fibre of $G_1$ at $x$, when the field is algebraically closed. Another lemma shows that such a $\gamma$ satisfies $\gamma^{n^k} = 1$ for some $k$, since it is trivial on the $n$-power torsion of the fibre. So the stabilizer of $x$ is an $n$-group. Its order is nonzero in the residue field, since $n$ is a unit in $R_{nM_0,N}$.

*The quotient.* The pushforward of the polarization bundle of $G_1$ is invertible by a lemma on models, which uses the coefficient ring and the local sections of goodness. Now all the hypotheses of [the theorem on tame quotients](/entry/exists-quotient-model/) hold, with $U = X_{l_1}$, $U' = X_{l_0}$, the maps $b$ and $r$, and the field inclusion $k : K_{A_0} \to K_{A_1}$, which satisfies $\beta_1 \circ b = k \circ \beta$. It gives a projective model $C$ of $(X_{l_0}, G^{\mathrm{univ}})$ over $R_{nM_0,1}$ with good semi-abelian scheme, such that $C_1$ is above $C$ over $(b, r, \nu)$.

*The extension property.* A lemma on auxiliary primes shows that an auxiliary inert prime is prime to the modulus of every level, so $n^J$ is prime to $M_0$. A lemma on level changes then extends every automorphism of $X_{l_0}$ of the form in the definition to $C$: it lifts the automorphism to $X_{l_1}$, extends it to $C_1$ through $T$, and descends it along the quotient map. The data $l_1$, $C_1$, $b$, $r$, $\nu$, $b'$ and $q$ complete the base model. $\square$

**Remark 5.9.3.** The tameness argument is the reason for the choice of an inert prime $n$. The group $\Gamma$ changes the level only at $n$, its stabilizers are $n$-groups, and $n$ is a unit on the base. If $N$ had a second prime factor $p$, a stabilizer could have order divisible by $p$, and the action would be wild in characteristic $p$. Since $N$ is a power of $n$, the quotient model exists over $R_{nM_0,1}$, that is, over every prime that does not divide $n M_0$.

**Remark 5.9.4 (Formalization).** The hypothesis $1 \le J$ is named `hJ` in the `intro` of [ExistsBaseModelSemiAbelian.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsBaseModelSemiAbelian.lean#L103) and is never used, so the theorem also holds for $J = 0$ as stated. The lemmas are `BaseRing.isDedFrac_RZ`, `T.cmModelCoefficient_inclusions_etale_openImmersion`, `T.exists_compactModel_above_fullLevel`, `T.exists_finite_etale_surjective_levelMap`, `T.moduli_level_quotient_by_finite_group`, `exists_action_model`, `galoisPart_eq_refl_of_fixes_point`, `T.finiteOrderAutomorphism_fixing_level_trivial_on_fixedFibre`, `T.iterate_eq_id_of_trivial_on_fixed_fibre`, `card_stab_ne_zero`, `good_pullback`, `T.pushforward_polarisationBundle_invertible_on_model`, `T.exists_quotient_model_by_tame_finite_group` and `T.levelChange_extends_base_model`; we followed their statements and did not open their proofs. The coprimality of $n$ and $M_0$ is the second part of `T.exists_two_inert_odd_primes_coprime_level`. The second name is a wrapper proved by `first | exact @...` under `maxHeartbeats 1000000`.
