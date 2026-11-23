---
title: The boundary ideal
decls:
  - GlobalTheory.T.unitaryCompactification_exists_boundary_ideal
  - GlobalTheory.UPoinc.uIdealSt_holds
  - GlobalTheory.T.exists_unitaryThetaSetup_ideal_over_component
  - GlobalTheory.UPoinc.exists_uSetup_ideal_over_component
  - GlobalTheory.T.exists_idealSheaf_descending_divisor_power
  - GlobalTheory.UPoinc.DescentPow.exists_idealSheaf_comap_uValThru
  - GlobalTheory.T.exists_unitaryApproxPoincareSeries
  - GlobalTheory.UPoinc.exists_uApproxAt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The boundary ideal

This section proves that each minimal compactification $C$ of $X_F$ carries a *boundary ideal*: an ideal sheaf $J$ on $Z_C$ whose support does not meet $i(X_F)$ and which has order $d\varphi$ along boundary traits through $i$, for some $d \ge 1$. [The theorem on the separating normalized blowup](/entry/u-poin-st-x-sep/) of Section 2 blows up this ideal. We work on one irreducible component at a time. Over a component we take a theta setup $X_1$ and a normal proper model over $Z_M$ with an effective Cartier divisor that has the right order along traits. A power of this divisor descends to an ideal on $Z_M$, and the germs that this descent needs are the approximations of Poincaré series, which we build first from the Fourier expansions of Section 3. Then we push the ideals down to $Z_C$ and multiply them. We use the notation of Sections 2 and 3.

**Definition 7.4.1 (Order through a map).** Let $i : X_F \to T$ and $\pi : S \to T$ be maps of schemes, $A \subset S$, $\varphi$ an invariant function, $J$ an ideal sheaf on $S$ and $d \in \mathbb{N}$. We say that $J$ has *order $d\varphi$ through $\pi$ over $A$* if the following holds. Let $W$ be a complete discrete valuation ring with uniformizer $\varpi$, $\chi : \operatorname{Spec} W \to S$ with $\chi$ of the closed point in $A$, and $y : \operatorname{Spec} \operatorname{Frac} W \to X_F$ with $i \circ y = \pi \circ \chi$ on $\operatorname{Spec} \operatorname{Frac} W$. Let $t$ be a semi-abelian datum on $W$ whose generic fibre is isomorphic to the universal datum at $y$, with a uniformization $P$ whose periods are monomial in $\varpi$ with exponent a level form $\beta$ of level $1$. Then there is $n \in \mathbb{N}$ with $n = d\varphi(\beta)$ and $\chi^* J = (\varpi^n)$.

Lean: `GlobalTheory.UPoinc.UValThru`.

For $\pi = \mathrm{id}$ and $A = S$ this is the order along boundary traits through $i$ of Section 2. We say *through $\pi$* when $A = S$.

**Definition 7.4.2 (Approximations).** Let $\varphi$ be an invariant function and $d \in \mathbb{N}$.

1. A theta setup $X_1$ has *approximations of order $d\varphi$* if for each prime $\ell$, each $z_1 \in Z_M$, each $\ell$-adic boundary trait $t_0$ through $z_1$ and each $e \in \mathbb{N}$ there is a germ $f \in \mathcal{O}_{Z_M, z_1}$ with $|\mathrm{val}_{t_0}(f)| = \exp(-\mathrm{sc}_{t_0}\, d\, \varphi(\beta_{T_0}))$, such that for each $\ell$-adic boundary trait $t$ through $z_1$, either $|\mathrm{val}_t(f)| \le \exp(-\mathrm{sc}_t\, d\, \varphi(\beta_T))$, or $|\mathrm{val}_t(f)| \le |\mathrm{val}_t(h)|^e$ for some $h$ in the maximal ideal.
2. A Fourier presystem $\Phi$ has *approximations of order $d\varphi$* if the same holds with $y_0, y \in Y$, $\mathrm{ev}_y$, $\mathrm{sc}_y$ and $\beta_y$ in place of $t_0$, $t$, $\mathrm{val}_t$, $\mathrm{sc}_t$ and $\beta_T$.
3. $\Phi$ is *dominated* if there is $C$ such that for each $y$ and $x \ne 0$ there is $h$ in the maximal ideal with $|\mathrm{ev}_y(h)| \ge \exp(-C\, \mathrm{sc}_y Q_y(x))$.

Lean: `GlobalTheory.UPoinc.UApproxAt` (also `GlobalTheory.Poinc.FPre.Approx`, `GlobalTheory.Poinc.FPre.abelian₂`).

Since $\exp(-\mathrm{sc}_t) = |\iota(\varpi)|$, the first condition says that $f$ has the size of $\varpi^{d \varphi(\beta_{T_0})}$ along $t_0$, as a local equation of the divisor of $d\varphi$ would.

**Theorem 7.4.3 (Approximating Poincaré series).** Let $p + q \ge 1$, $\varphi$ a polarized fan of rank $\min(p, q)$, $C$ a minimal compactification of $X_F$ and $X_1$ a theta setup for $C$. Then there is $d \ge 1$ such that $X_1$ has approximations of order $d\varphi$.

Lean: `GlobalTheory.UPoinc.exists_uApproxAt` (also `GlobalTheory.T.exists_unitaryApproxPoincareSeries`, a second name).

*Proof.* Since $\varphi$ is a polarized fan over a CM field, there is $d_0 \ge 1$ such that $\varphi$ has supporting tuples with constant $d_0$; we take $d = d_0$. The size condition on $S$ gives $L \ge 3$. Let $\ell$, $z_1$, $t_0$ and $e$ be given. The point $z_1$ is closed, as the image of a closed point. So there is a dominated Fourier presystem $\Phi$ over $\mathcal{O}_{Z_M, z_1}$ that covers $z_1$ and in which each $y$ matches a trait through $z_1$. By [the theorem on Fourier expansions at all levels](/entry/upoinc-four-of-classical/) of Section 3, $\Phi$ has Fourier expansions at level $L \ge 3$, so it has approximations of order $d_0 \varphi$.

If $y$ matches $t$, then $\mathrm{sc}_y \varphi(\beta_y) = \mathrm{sc}_t \varphi(\beta_T)$, because $\varphi$ is homogeneous and invariant. Let $y_0$ match $t_0$, and let $f$ be the germ for $y_0$ and $e$. Then $|\mathrm{val}_{t_0}(f)| = |\mathrm{ev}_{y_0}(f)| = \exp(-\mathrm{sc}_{t_0} d\, \varphi(\beta_{T_0}))$, and for each $t$ the alternative for a $y$ that matches $t$ is the alternative for $t$, since $\mathrm{val}_t = \mathrm{ev}_y$. $\square$

**Theorem 7.4.4 (Descent of a power of a divisor).** Let $p + q \ge 1$, $\varphi$ a polarized fan of rank $\min(p, q)$, $C$ a minimal compactification of $X_F$, $X_1$ a theta setup for $C$ and $\iota \ge 1$. Let $Y$ be a model over $(o_1, \Omega_1)$ with $Z_Y$ normal, and $\pi_Y : Z_Y \to Z_M$ a proper map of models over the identity. Let $D$ be an effective Cartier divisor on $Z_Y$ whose support maps outside $i(X_F)$ under $\pi \circ \pi_Y$, and whose ideal has order $\iota\varphi$ through $\pi \circ \pi_Y$. Then there are $\iota' \ge 1$ and an ideal sheaf $J_1$ on $Z_M$ such that $\pi_Y^{-1} J_1$ has these two properties with $\iota'$ in place of $\iota$.

Lean: `GlobalTheory.UPoinc.DescentPow.exists_idealSheaf_comap_uValThru` (also `GlobalTheory.T.exists_idealSheaf_descending_divisor_power`, a second name).

*Proof.* By the previous theorem, $X_1$ has approximations of order $d\varphi$ for some $d \ge 1$. Let $\iota' = \operatorname{lcm}(\iota, d) = k\iota = md$. Raising the germs to the power $m$ gives approximations of order $\iota'\varphi$. The divisor $kD$ has order $\iota'\varphi$ through $\pi \circ \pi_Y$, because its ideal along each trait is the $k$-th power, and its support lies in the support of $D$.

There is an open $W \subset Z_C$ that contains $i(X_F)$, such that each $\ell$-adic point of $Z_C$ with generic point in $W$ has generic point in $i(X_F)$. Let $U$ be the preimage of $W$ in $Z_Y$ minus the support of $kD$. It is not empty, because it contains the image of the point $\mathrm{pt}_Y$, which maps into $i(X_F)$.

A criterion for descent now gives an ideal sheaf $J_1$ on $Z_M$ with $\pi_Y^{-1} J_1$ equal to the ideal of $kD$, if the following holds for each closed point $z_0$ of $Z_M$ and each closed point $x$ of $Z_Y$ over $z_0$. There must be a prime $\ell$ and a point $y_0 : \operatorname{Spec} \mathcal{O}_\ell \to Z_Y$ centred at $x$ with generic point in $U$, and for each $e$ an integral germ $f$ at $z_0$, such that $|f| = |g|$ at $y_0$ for each local equation $g$ of $kD$ at $x$, and such that at each $\ell'$-adic point $y$ centred over $z_0$ with generic point in $U$ and each local equation $g$ of $kD$ at the centre of $y$, either $|f| \le |g|$ or $|f| \le |h|^e$ for some $h$ in the maximal ideal of $\mathcal{O}_{Z_M, z_0}$.

We check this. A point $y_0$ as above exists. Since its generic point lies in $U$, the composite $\pi_Y \circ y_0$ is the map of an $\ell$-adic boundary trait $t_0$ of $X_1$ through $z_0$, and each local equation $g$ of $kD$ has $|g| = \exp(-\mathrm{sc}_{t_0}\, \iota' \varphi(\beta_{T_0}))$ at $y_0$. The approximations of order $\iota'\varphi$ for $t_0$ and $e$ give the germ $f$. For $y$ centred over $z_0$, the prime $\ell'$ equals $\ell$, since both are the residue characteristic at $z_0$. Then $y$ also gives a trait $t$ with the same equality for $|g|$, and the alternative for $t$ gives the alternative for $y$. So $J_1$ exists, and $\pi_Y^{-1} J_1$ has the properties of $kD$. $\square$

**Theorem 7.4.5 (Boundary ideal over a component).** Let $p + q \ge 1$, $\varphi$ a polarized fan of rank $\min(p, q)$ and $C$ a minimal compactification of $X_F$. Let $A \subset Z_C$ be open, closed and irreducible, and let $A$ meet $i(X_F)$. Then there are a theta setup $X_1$ for $C$ with $\pi(Z_M) = A$, an integer $\iota \ge 1$ and an ideal sheaf $J_1$ on $Z_M$ whose support maps outside $i(X_F)$ under $\pi$, and which has order $\iota\varphi$ through $\pi$.

Lean: `GlobalTheory.UPoinc.exists_uSetup_ideal_over_component` (also `GlobalTheory.T.exists_unitaryThetaSetup_ideal_over_component`, a second name).

*Proof.* There is a generic point $\eta$ of $X_F$ whose image has closure $A$. There is a theta setup $X_1$ with $Z_M$ projective over $o_1$ and with $u$ sending $\operatorname{Spec} \Omega_1$ to $\eta$, and then $\pi(Z_M) = A$. By [the theorem on normal models with Cartier divisors along traits](/entry/unitary-exists-normal-model-eff-cartier-along-traits/), there are $\iota \ge 1$, a normal model $Y$ with a proper map of models $\pi_Y : Z_Y \to Z_M$, and an effective Cartier divisor $D$ on $Z_Y$ as in the previous theorem. That theorem gives $\iota'$ and $J_1$ on $Z_M$ such that $\pi_Y^{-1} J_1$ has the two properties. Since $\pi_Y$ is proper, $J_1$ has them too. $\square$

**Theorem 7.4.6 (Boundary ideal).** Let $p + q \ge 1$, $\varphi$ a polarized fan of rank $\min(p, q)$ and $C$ a minimal compactification of $X_F$. Then there are $d \ge 1$ and an ideal sheaf $J$ on $Z_C$ whose support does not meet $i(X_F)$ and which has order $d\varphi$ along boundary traits through $i$.

Lean: `GlobalTheory.UPoinc.uIdealSt_holds` (also `GlobalTheory.T.unitaryCompactification_exists_boundary_ideal`, a second name; `GlobalTheory.UPoinc.UIdealSt`, the statement).

*Proof.* The ring $o$ is noetherian and $Z_C$ is projective over $o$, so $Z_C$ is noetherian and has finitely many irreducible components. Its local rings are domains, so no point lies on two components, and each component $A$ is open and closed. For each component $A$ we find $d_A \ge 1$ and an ideal sheaf $J_A$ on $Z_C$ whose support lies in $A$ and does not meet $i(X_F)$, and which has order $d_A \varphi$ through the identity over $A$.

If $A$ meets $i(X_F)$, the previous theorem gives $X_1$, $\iota$ and $J_1$ over $A$, and pushing $J_1$ down along the finite map $\pi$ gives $d_A$ and $J_A$. If $A$ does not meet $i(X_F)$, we take $d_A = 1$ and $J_A = \mathcal{O}_{Z_C}$. No trait has its closed point in $A$: its generic point would lie in the open set $A$ and also in $i(X_F)$.

Let $d = \prod_A d_A$ and $J = \prod_A J_A^{d / d_A}$. The support of $J$ does not meet $i(X_F)$. Each point lies in exactly one component $A$, and near it the factors $J_{A'}$ with $A' \ne A$ are the unit ideal. So along a trait with closed point in $A$ the ideal $J$ pulls back to $(\varpi^{n d / d_A})$ with $n = d_A \varphi(\beta)$, which is $(\varpi^{d\varphi(\beta)})$. $\square$

**Remark 7.4.7 (Formalization).** The proofs are in [UnitaryCompactificationExistsBoundaryIdeal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryCompactificationExistsBoundaryIdeal.lean#L19), [ExistsUnitaryThetaSetupIdealOverComponent.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryThetaSetupIdealOverComponent.lean#L17), [ExistsIdealSheafDescendingDivisorPower.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsIdealSheafDescendingDivisorPower.lean#L73) and [ExistsUnitaryApproxPoincareSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryApproxPoincareSeries.lean#L96). The definition `UValThru` is in [UValThruTopOfDisjoint.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UValThruTopOfDisjoint.lean#L21). The `T.*` names are wrappers that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. In `exists_uApproxAt` the constant is `(!![1] 0 0).toNat * d₀` (lines 105 to 116), which is $d_0$. In `uIdealSt_holds`, the case of a component that does not meet $i(X_F)$ uses `uValThru_top_of_disjoint`. That case does not occur, since $i$ has dense image and each component is open and not empty, but the proof does not use this. The proofs apply lemmas with no entries in this chapter, among them `exists_hasSupports_cm`, `T.exists_unitaryThetaSystem_classicalTraits_closedPoint`, `Poinc.approx_of_fpre`, `sc_evalZ_eq`, `T.unitaryApproxPoincareSeriesAt_mul`, `T.exists_open_compactification_generic_subset_moduli`, `T.exists_idealSheaf_pullback_eq_divisor_of_approx`, `exists_uCTrait_norm_eqAt`, `T.prime_eq_of_classicalPoint_same_centre`, `exists_genericPoint_closure_eq_of_isClopen`, `GSetup.exists_uSetup_proj`, `ideal_orders_of_proper_model`, `T.ideal_descent_to_component_compactification` and `exists_uValOn_of_pieces`. We use only their statements as the proofs apply them. We have not unfolded `EffCartierData`, `RatModel.IsHom`, `EqAt`, `idlAlong` or `HasSupports`.
