---
id: bound
title: The measure bound for one class of flags
kind: theorem
decl: GlobalTheory.FlagBase.OneClass.bound
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.FlagClassMeasureBoundLatticeStabiliser
covers: 781
status: drafted
drafted_by: writer@claude
---
This theorem bounds the covolume of one slice of the set of points of a given flag type: the slice that belongs to one model flag. It splits $G_\infty$ along the parabolic subgroup of the flag as $NMK$ and bounds the $N$ part and the $M$ part separately. Under the name [`flagClass_measure_bound_lattice_stabiliser`](/entry/flag-class-measure-bound-lattice-stabiliser/) it goes to [`unfoldBound`](/entry/unfold-bound/), which sums it over all classes.

## Statement

Use the notation of [`unfoldBound`](/entry/unfold-bound/) and [the flag measure bound](/entry/flag-measure-bound/). Fix $x_f \in G_f$ and an adapted model (`IsAdapted`) with flag $S_0 \subset \dots \subset S_a$, lattices $\Lambda_i \subset E^{j_i}$, a point $x_0 \in G_{0,f}$ and blocks $T, T', T_0$. For $g \in G_\infty$ let $\mathrm{sizes}(g)_i = \mathrm{size}(S_i/S_{i-1})$ in the metric of $(g, x_f)$. Let $\Gamma_{x_f} = \{\gamma_\infty : \gamma \in G(F),\ x_f^{-1}\gamma x_f \in K_f\}$, and let $\Gamma_S \subseteq \Gamma_{x_f}$ be the elements that preserve the complexified flag at every real place. Let $\Gamma_{0,x_0}$ be the same group for $G_0$ at $x_0$.

**Theorem.** Let $G$ have signature $(p,q)$, let $j_i \ge 1$, let $c, c_0$ be gauges, and let $B$ be a measurable set of increasing $\tau \in (0,1/2)^a$. Then

$$\begin{aligned}&{\Bigl(\prod_v c_v\Bigr) \mathrm{covol}_{\Gamma_S}\{g : \mathrm{sizes}(g) \in B\} \le c_{\mathrm{Iw}}^f\, r_d^{f d_N/2} \prod_i 2^{f j_i^2}\, \mathrm{vol}(\Lambda_i)}\\ &{\quad \cdot \Bigl(\prod_v c_{0,v}\Bigr) \mathrm{covol}_{\Gamma_{0,x_0}}(G_{0,\infty}) \int_B \mathrm{dens}(\tau)\, d\tau.}\end{aligned}$$

Here the covolumes are for the product of the Haar measures of the groups $U(p,q)$ at the real places, and $\mathrm{vol}(\Lambda_i)$ (`slabVol`) is the covolume of the units of $\Lambda_i$ in the slab $1 \le \prod_w |\det g_w|^2 < e$ of $\prod_w \mathrm{GL}_{j_i}(\mathbb{C})$.

## Proof

If the set $\{g : \mathrm{sizes}(g) \in B\}$ is empty, its covolume is $0$. Otherwise:

1. **The flag.** `isSaturatedIsotropicFlag_of_adaptedBasis` makes $S$ a saturated isotropic flag. `isTotallyIsotropicFlag_complexified_saturatedFlag` makes each complexified flag $W_v$ isotropic.
2. **The decomposition.** At each real place, `isotropicFlagUnipotentRadical_closed_subgroup_keeps` and `isotropicFlagLevi_maxCompact_closed_subgroups` give closed subgroups $N_v$ (the unipotent radical), $M_v$ (the Levi part) and $K_v$ (the maximal compact). `iwasawa_decomposition_unitary_isotropicFlag` gives $G_v = N_v M_v K_v$, and $um \in K_v$ with $u \in N_v$, $m \in M_v$ forces $u = 1$. `exists_gauge_measures_isotropicFlag_parabolic` gives gauge measures on $N_v$, $M_v$ and a probability measure on $K_v$.
3. **Sizes depend on $M$ only.** `gradedPieceSizes_unipotent_levi_compact_move` gives $\mathrm{sizes}(umk)_i^f = \mathrm{sizes}(1)_i^f \prod_v |\det(m_v \text{ on } W_{v,i}/W_{v,i-1})|^{-1/j_i}$.
4. **Integration.** [The Iwasawa formula](/entry/unitary-iwasawa-integration-formula-real-place/) at each place and `iwasawaNMKIntegration_pi_product` give $\prod_v c_v \int_{G_\infty} \varphi = c_{\mathrm{Iw}}^f \int_N \int_M \delta(m) \int_K \varphi(umk)$.
5. **The $N$ part.** `unipotentRadical_integral_points_covolume` bounds the covolume of $\Gamma_S \cap N$ in $N$ by $r_d^{f d_N/2}\, \ell(\mathrm{sizes}(1))$.
6. **The $M$ part.** `levi_factor_integral_mod_integral_points_le` bounds the covolume of the Levi quotient, with density $F(\mathrm{sizes}(m))$ for $F = 1_B \ell$, by the slab volumes, the covolume for $G_0$, and $\int_{\tau > 0} F(\tau) \prod_i 2 f j_i/\tau_i\, d\tau$. This integral is $\int_B \mathrm{dens}$.
7. **Assembly.** The abstract lemma `covol_le` in the same file puts steps 2 to 6 together. It uses a measurable section of $K \cap M$ (`exists_measurable_coset_section'`) and the invariance of the sizes under $\Gamma_S$ (`flagGradedPieceSizes_stabiliser_mul`).

## In the Lean code

The theorem is in [FlagClassMeasureBoundLatticeStabiliser.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/FlagClassMeasureBoundLatticeStabiliser.lean#L174), and `covol_le` is on [line 29](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/FlagClassMeasureBoundLatticeStabiliser.lean#L29). The groups `flagGroup`, `latGroup`, `leviGroup` and the function `sizesAt` are in [IsLatMeasurableConst.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/IsLatMeasurableConst.lean#L25).

- The signature $(p,q)$ enters only through the Iwasawa formula and the constant $c_{\mathrm{Iw}}$.
- The result is a bound, not an equality: step 7 covers the slice by one Iwasawa slice built from a fundamental set for $N$ and one for $M$.
- We did not open the proofs of the lemmas in steps 1 to 6.
