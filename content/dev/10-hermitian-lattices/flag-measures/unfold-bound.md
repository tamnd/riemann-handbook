---
id: unfold-bound
title: Unfolding the points of a flag type over the classes of flags
kind: theorem
decl: GlobalTheory.FlagUnfold.unfoldBound
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.IsotropicFlagUnfoldingBound
covers: 854
status: drafted
drafted_by: writer@claude
---
This theorem bounds the covolume of the points of a given flag type. It cuts the set into slices, one for each class of model flag, and bounds each by [the bound for one flag class](/entry/flag-class-measure-bound-lattice-stabiliser/). Under the name [`isotropicFlag_unfolding_bound`](/entry/isotropic-flag-unfolding-bound/) it goes to [the flag measure bound](/entry/flag-measure-bound/).

## Statement

Take $T(j,B)$ and $\mathrm{dens}$ from [the flag measure bound](/entry/flag-measure-bound/). The covolume $\mathrm{covol}_\Gamma(A)$ is the infimum of $\mu(D)$ over measurable $D$ that contain a $\Gamma$-translate of each point of $A$. A gauge at a real place $v$ is a constant $c_v$ with $c_v \mu_v(\{g : \|g - 1\|_{\mathrm{HS}} \le r\}) \sim \mathrm{vol}(B^{n^2})\, r^{n^2}$ as $r \to 0$, for the Haar measure $\mu_v$ of $U(p,q)$ and the unit ball $B^{n^2}$. The gauge volume is

$$\mathrm{vol}(G) = \Bigl(\prod_v c_v\Bigr) \frac{\mathrm{covol}_{G(F)}(G(\mathbb{A}))}{\mu_f(K_f)},$$

which does not depend on $\mu_f$.

**Theorem.** Let $G$ and $G_0$ be unitary groups of hermitian spaces over the same CM field $E$, of signatures $(p,q)$ and $(p-s,q-s)$ at every real place. Let $a \ge 1$, $j_i \ge 1$, $s = \sum_i j_i \le \min(p,q)$. Let $c, c_0$ be gauges and $B$ a measurable set of increasing $\tau$ in $(0,1/2)^a$. Then

$$\Bigl(\prod_v c_v\Bigr) \frac{\mathrm{covol}_{G(F)}(T(j,B))}{\mu_f(K_f)} \le C \prod_i 2^{f j_i^2} \mathrm{vol}(\mathrm{GL}_{j_i}/E) \cdot \mathrm{vol}(G_0) \int_B \mathrm{dens}(\tau)\, d\tau,$$

with $C = c_{\mathrm{Iw}}(p,q,j)^f\, r_d^{f d_N/2}$. Here $c_{\mathrm{Iw}}$ is the constant of [the Iwasawa formula](/entry/iwasawa-constant/), and $\mathrm{vol}(\mathrm{GL}_j/E)$ (`glVol`) is the sum over the $\mathrm{GL}_j(E)$-classes of lattices $\Lambda \subset E^j$ of the covolume of the units of $\Lambda$ in the slab $1 \le \prod_w |\det g_w|^2 < e$.

## Proof

1. **Index set.** A class is a pair: a class of lattice $\Lambda_i \subset E^{j_i}$ for each $i$, and a double coset $x_0 \in G_0(F)\backslash G_{0,f}/K_{0,f}$. Both sets are countable (`countable_lattices`, `countable_dc`). Choose an adapted model for each class that has one. A model (`IsAdapted`) is a splitting of the lattice of $x_f$ as $\bigoplus_i T_i \Lambda_i \oplus \bigoplus_i T'_i \Lambda_i^\vee \oplus T_0 \Lambda_{x_0}$, with $T_i, T'_i$ dual isotropic blocks orthogonal to $T_0$, and $T_0^* J T_0 = J_0$. The flag is $S_k = \bigoplus_{i<k} T_i \Lambda_i$.
2. **Covering.** Each $y \in T(j,B)$ has a saturated isotropic flag with sizes in $B$ (`exists_isSatFlag`) and an adapted basis (`exists_adaptedBasis_saturatedIsotropicFlag`). After a change to the chosen representatives (`exists_adapted_basis_change_models`), some $\gamma \in G(F)$ and $k \in K_f$ move $y$ onto the chosen model with the same sizes (`flags_conjugate_of_same_adapted_models`).
3. **Slices.** `covol_prod_le_tsum_slices` gives $\mathrm{covol}(T(j,B)) \le \mu_f(K_f) \sum_t \mathrm{covol}_{\Gamma_t}(\{g : \mathrm{sizes}(g) \in B\})$, with $\Gamma_t$ the arithmetic subgroup that preserves the model flag.
4. **Each slice.** [The bound for one flag class](/entry/flag-class-measure-bound-lattice-stabiliser/) bounds slice $t$ by the same constants times the slab volumes of the $\Lambda_i$ and the gauge covolume of the arithmetic group of $G_0$ at $x_0$.
5. **Sum.** Summed over lattice classes, the slab volumes give $\mathrm{vol}(\mathrm{GL}_{j_i}/E)$ by definition (`tsum_pi_prod_le` handles the tuples). `sum_latGroup_le` bounds the sum over double cosets by $\mathrm{vol}(G_0)$: its core `sum_covol_le` unfolds $G_0(F)\backslash G_0(\mathbb{A})$ into the arithmetic quotients.

## In the Lean code

The theorem is in [IsotropicFlagUnfoldingBound.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/IsotropicFlagUnfoldingBound.lean#L213). The models are `IsAdapted` in [IsLatMeasurableConst.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/IsLatMeasurableConst.lean#L12).

- The hypothesis $1 \le a$ is introduced as `_` on line 214 and not used.
- Only classes with a model are summed, and that sum is bounded by the sum over all classes. So the result is an inequality.
- `UnfoldBound` does not ask that $G_0$ has rank $n - 2s$; `IsAdapted` contains $n = n_0 + 2s$.
- We did not open the proofs of the four lemmas in step 2.
