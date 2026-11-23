---
id: q-peel-holds
title: Peeling the twist places off the doubling integral of a theta step
kind: theorem
decl: GlobalTheory.ChainTw.Peel.qPeel_holds
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ChainTwistPlacesIntegralPeelOfDoubling
covers: 400
status: drafted
drafted_by: writer@claude
---
This theorem proves `QPeel D`: at a step of a twisted theta chain, the doubling integral over the elements that are integral off $S$ equals a product of local factors at the twist places times the integral over the level set. Its restatement [`chainTwistPlacesIntegralPeel_of_doubling`](/entry/chain-twist-places-integral-peel-of-doubling/) feeds `thetaLiftChainStep_exact_innerProduct` in [`scalars_of_given_all`](/entry/scalars-of-given-all/).

## Statement

`QPeel D` is quantified by `ForStepQ`. Assume the node gap for $D$. Let $c$ be a common datum (`Com D`) and $w$ a twist with `w.Is c`: the places `c.Pg` split as the disjoint union of `w.Pg` and the twist places $Q$ = `w.Q`, and at each $\mathfrak P \in Q$ the characters of $c$ are $\xi_{\mathfrak P}^{-1}$ for a nontrivial character $\xi_{\mathfrak P}$. Let $k < m$ and let $p$ be a step (`IsStep`) from stage $s$ to stage $s'$ of the chain, at $k$ and $k+1$. Take a majorant $a$ (`IsMajOf`), forms $u_1, u_2$ in `s.CC c`, a polynomial $\varphi$, and $K$-finite vectors $v_1, v_2$. Let $F_i$ be the automorphic function of $u_i$ at $v_i$. Assume `IsQ w k u₁`: at each twist place, $F_1$ has a fixed local type with parameters `qPar`.

For real $z$ let

$$\mathcal I_z(g) = \langle \omega(g,1)\Phi, \Phi\rangle \cdot H_a(g)^{z - t/2} \cdot \langle R(g)\overline{F_1}, \overline{F_2}\rangle,$$

the integrand `flatInt`. Here $\Phi$ is the Fock vector of $\varphi$, $H_a$ is the height of $g$ for the majorant $a$, the shift $t/2$ is `sZero`, half the difference of the ranks of the two stages, and the last factor is a Petersson product. Let $\mathrm{Lev}$ be the set of $g$ whose finite part lies in the level group (`levSet s`), and $\mathrm{Off}$ the set of $g$ with $g_v$ in the stabiliser of the lattice for every $v \notin S$ (`intOff c s`). For $\mathfrak P \in Q$ with norm $q$, put $\alpha_i = (\mu_i \mu_{k+1}^{-1})(\mathfrak P)$ and

$$\ell_{\mathfrak P} = \prod_{i=1}^{k} \prod_{n=1}^{t} \frac{1}{(1 - \alpha_i q^{-n})(1 - \alpha_i^{-1} q^{-n})} \cdot \prod_{n=t+1}^{(k+1)t} (1 - q^{-n}),$$

that is `blockL c k 𝔓 * zinv 𝔓 t ((k+1)t)`.

**Theorem.** Assume `UnramifiedDoublingGL` and `CuspRapidDecay`. Then `QPeel D` holds for every $D$: if $z > t/2 - 1$ and $\mathcal I_z$ is integrable on $\mathrm{Lev}$, then it is integrable on $\mathrm{Off}$, and for $z = t/2$

$$\int_{\mathrm{Off}} \mathcal I_z \, dg = \prod_{\mathfrak P \in Q} \ell_{\mathfrak P} \int_{\mathrm{Lev}} \mathcal I_z \, dg.$$

## Proof

1. [`flatIntegrand_localFactor_splits_twistPlace`](/entry/flat-integrand-local-factor-splits-twist-place/) gives, for each $\mathfrak P \in Q$, an open subgroup $J_{\mathfrak P}$ of the local group with volume one and a function $\zeta_{\mathfrak P}$ with $\int \zeta_{\mathfrak P} = \ell_{\mathfrak P}$ at $z = t/2$, such that right translation of $\mathcal I_z$ at the place of $\mathfrak P$ multiplies it by $\zeta_{\mathfrak P}$. See [`local_factor`](/entry/local-factor/).
2. For $T \subseteq Q$ let $E_T$ be the set of $g \in \mathrm{Off}$ whose component at each $\mathfrak P \in T$ lies in the level group. By induction on $T$, `integral_split_finite_place_fubini` peels one place at a time: $\int_{E_{Q \setminus T}} = \prod_{\mathfrak P \in T} \ell_{\mathfrak P} \int_{E_Q}$. The places of $Q$ lie over distinct places of $F$ (`LevelPlaces.injOn_under`).
3. $E_\emptyset = \mathrm{Off}$, and $\mathrm{Lev} \subseteq E_Q$ by `thetaChainStage_finiteLevel_eq_product_localLevels`. On $E_Q \setminus \mathrm{Lev}$ the integrand is zero: at a place of `w.Pg` the Weil coefficient vanishes off the level group (`twistedChain_coefficient_supported_principal_level`).

## In the Lean code

The theorem is in [ChainTwistPlacesIntegralPeelOfDoubling.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ChainTwistPlacesIntegralPeelOfDoubling.lean#L27). `QPeel`, `blockL`, `zinv`, `levSet` and `flatInt` are in [IsLevMeas.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsLevMeas.lean#L159), the integrand in [IntegrandSZero.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IntegrandSZero.lean#L44), and `intOff` in [ChainParSucc.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ChainParSucc.lean#L134).

The equality is claimed only at $z = t/2$; for other $z$ the theorem gives integrability only.
