---
id: local-factor
title: The doubling integrand splits off a local factor at a twist place
kind: theorem
decl: GlobalTheory.ChainTw.OnePlace.local_factor
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.FlatIntegrandLocalFactorSplitsTwistPlace
covers: 383
status: drafted
drafted_by: writer@claude
---
This theorem is the local computation at one twist place of the doubling integral of a theta step. Translation at that place multiplies the integrand by a local function $\zeta$,, and the integral of $\zeta$ is a product of local $L$-factors. Its restatement [`flatIntegrand_localFactor_splits_twistPlace`](/entry/flat-integrand-local-factor-splits-twist-place/) is used by [`qPeel_holds`](/entry/q-peel-holds/).

## Statement

The setting and the integrand $\mathcal I_z(g) = \langle \omega(g,1)\Phi, \Phi\rangle \, H_a(g)^{z - t/2} \, \langle R(g)\overline{F_1}, \overline{F_2}\rangle$ are those of [`qPeel_holds`](/entry/q-peel-holds/). Let $\mathfrak P \in Q$ be a twist place over the place $v$ of $F$, and $G_v$ the local group of $s.V$ at $v$.

**Theorem.** Assume `UnramifiedDoublingGL` and `CuspRapidDecay`. There are an open subgroup $J \subseteq G_v$, a [[Haar measure|VY0HXD3GC4]] $\mu$ on $G_v$ with $\mu(J) = 1$, and an integrable $\zeta \colon G_v \to \mathbb C$ with $\zeta = 1$ on $J$, such that:

1. $g_v$ lies in the level group if and only if the projection of $g$ to $G_v$ lies in $J$;
2. if $z = t/2$, then $\int \zeta \, d\mu = \ell_{\mathfrak P}$, the product `blockL * zinv` written out in [`qPeel_holds`](/entry/q-peel-holds/);
3. if $x$ is integral off $S$ and $x_v = 1$, then $\mathcal I_z(x y) = \zeta(y)\, \mathcal I_z(x)$ for all $y \in G_v$.

## Proof

1. **Charts.** `exists_charts_at_twist_places_chain` shows that $v$ splits in $E$ and gives a uniformiser $\varpi$, a character $\mu_T$ of $F_v^\times$ matching $\chi_{T,k+1}$, and a chart $\iota \colon \mathrm{GL}_{r + kt}(F_v) \to U(s.V)(\mathbb A)$. `splitPlaceChart_parahoric_level_stabiliser_height` gives an isomorphism $e$ of topological groups from $\mathrm{GL}_{r+kt}(F_v)$ to $G_v$. Under $e$ the level group is the parahoric with blocks $r$ and $kt$, the level character comes from $\mu_T$, which lifts $\xi_{\mathfrak P}$, and the height becomes a height $H$ (`IsHgt`). The character $\mu_T$ is tame and ramified.
2. **The Weil factor.** `weilCoefficient_splits_localFactor_twistPlace`: for $x_v = 1$, the Weil coefficient at $x\,\iota(y)$ times $\overline{c(1)}$ equals the coefficient at $x$ times $\overline{c(y)}$. Here $c$ is a coefficient of the local Weil representation (`SplitWeil.om`).
3. **The automorphic factor.** `rcoef_eq_coef`, in the same file, writes $y \mapsto \langle R(x\iota(y))\overline{F_1}, \overline{F_2}\rangle$ as $\ell(\pi(y)u)$. Here $\pi$ is right translation on $L^2$, $u = \overline{F_1}$ has the type given by `IsQ`, and $\ell$ has the dual type (`IsCoType`, by `val_type`). `CuspRapidDecay` gives $L^2$ (`memL2_of_cusp_form`).
4. **The local integral.** [`unramifiedDoublingIntegral_twisted_place_eigenvector`](/entry/unramified-doubling-integral-twisted-place-eigenvector/), from `UnramifiedDoublingGL`, gives $c(1) \neq 0$ and a function $\zeta_0$, equal to $1$ on the parahoric, with $\overline{c(g)}\,\ell(\pi(g)u) = \overline{c(1)}\,\zeta_0(g)\,\ell(u)$ for every such pair $(\pi, u, \ell)$. It also gives $\int \zeta_0 H^{s - t/2} = L(s + \tfrac12, \alpha)\, L(s + \tfrac12, \alpha^{-1})$ times a normalising factor, where $\alpha$ lists the parameters `qPar` shifted by $\mu_T(\varpi)^{-1}$. At $s = t/2$, `lower_block_parameter_twist_L_factor` turns this into $\ell_{\mathfrak P}$.
5. **Assembly.** `hgt_split` splits the height: $H_a(x\,e(y)) = H_a(x)\, H(y)$, and `hgt_one` gives $H = 1$ on the parahoric. Put $\zeta = (\zeta_0 \cdot H^{z - t/2}) \circ e^{-1}$, and move the Haar measure of volume one on the parahoric (`exists_haar`) to $G_v$. Claim 3 follows from steps 2 to 4 after cancelling $\overline{c(1)}$.

## In the Lean code

The theorem is in [FlatIntegrandLocalFactorSplitsTwistPlace.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/FlatIntegrandLocalFactorSplitsTwistPlace.lean#L164), with its helpers above it. `UnramifiedDoublingGL` is in [PairwiseDisjointCell.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/PairwiseDisjointCell.lean#L314). We have not opened the proofs of the lemmas in steps 1, 2 and 4.

The integral is computed only at $z = t/2$; for other $z > t/2 - 1$ the theorem gives only that $\zeta$ is integrable. The node gap hypothesis of `ForStepQ` is used only by `weilCoefficient_splits_localFactor_twistPlace`. `UnramifiedDoublingGL` has the shape of the unramified computation in the doubling method of Piatetski-Shapiro and Rallis (Lecture Notes in Math. 1254, 1987), but here it is used at a place where $\mu_T$ is ramified.
