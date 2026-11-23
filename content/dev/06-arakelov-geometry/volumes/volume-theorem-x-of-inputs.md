---
id: volume-theorem-x-of-inputs
title: The volume theorem for good root towers
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Cusp.volumeTheoremX_of_inputs
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.VolumeTheoremOfInputs
covers: 8966
status: drafted
drafted_by: writer@claude
---
This theorem proves the volume theorem `VolumeTheoremX` from ten inputs. For one good tower it checks the seventeen hypotheses of [the chain of tower estimates](/entry/chain-tower/) and returns its four conclusions with two more properties. Its statement form is [`volume_theorem_of_inputs`](/entry/volume-theorem-of-inputs/). The result is the volume part of Step 4 of [the Weil bound](/proof/weil-bound/).

## Statement

Let $\Psi$ be a finite set (here the CM types of the host) and $N \geq 1$. A weight is $\lambda \in \mathbb{R}^{\Psi \times \{0, \dots, N-1\}}$, and $L_\lambda = -\sum_r \lambda_r x_r$ is a linear form in variables $x_r$. Let $d = |\Psi|\,N(N-1)/2$, the dimension of a product of $|\Psi|$ flag varieties of $\mathrm{GL}_N$.

A *root model* ([Birational.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Birational.lean#L11)) is an [arithmetic variety](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers) $X$ of dimension $d + 1$ in multiprojective coordinates, with smooth hermitian lines $\overline x_r(t)$ that depend on $t > 0$ and one more hermitian line $\overline A$. For a polynomial $F$ in the $x_r$, $\mathrm{PP}(F)$ is the limit as $t \to 0^+$ of the arithmetic intersection numbers of the monomials of $F$, divided by a positive integer $\delta$ and by a power of the degree $k_A$ of $\overline A$. So $\mathrm{PP}(L_u^{d+1})$ is the arithmetic self-intersection of the line of weight $u$.

A *root tower* $T$ ([Proportional.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Proportional.lean#L10)) is an integer $1 \leq j < N$, a finite nonempty set of components $c$, a finite set of bad primes that contains $2$, a rational weight $\nu$ and a root model $M_{B,c}$ for each $B \in \mathbb{N}$ and each $c$. Write $\mathrm{PP}_{B,c}$ for $\mathrm{PP}$ on $M_{B,c}$ and $\mathrm{PP}_B = \sum_c \mathrm{PP}_{B,c}$. The volume $\mathrm{vol}(c)$ is the geometric degree of $L_\rho^d$ on $M_{2,c}$ divided by $\deg_{\mathrm{Fl}}(L_\rho^d)$, for $\rho = (N-1, \dots, 0)$. Here $\deg_{\mathrm{Fl}} F$ is the signed sum of the coefficients of $F$ at the permuted exponents $\sigma(\rho)$; by its name it is the degree on the flag variety. The slope of $u$ on $c$ is $\mathrm{PP}_{B,c}(L_u^{d+1}) / ((d+1)\,\mathrm{vol}(c)\deg_{\mathrm{Fl}}(L_u^d))$.

Let $\Lambda_B = \log(B\,\mathrm{rd}_E) + |L'/L(1, \chi)|$, where $\mathrm{rd}_E = |d_E|^{1/[E:\mathbb{Q}]}$ and $\chi$ is the quadratic character modulo the prime $d$ of the host.

**Theorem.** Assume the ten inputs listed in [the statement form](/entry/volume-theorem-of-inputs/). Then there is $C \geq 0$ with this property. Let $E$ be a CM field, abelian over $\mathbb{Q}$, with host $H$ and datum $D$ with $q \geq 1$ and $3q + 1 \leq p + q$. Let $Y$ be a global integral model, $T$ a root tower for $N = p + q$ with at most $4\,|\Psi|\,N^2$ bad primes, $o$ a good origin of $Y$ for $T$ with `Extra`, and $II$ a full intersection system. Then:

1. (`Proportional`) $\mathrm{vol}(c) > 0$, and the geometric degree of each $F$ on $M_{B,c}$ is $\mathrm{vol}(c)\deg_{\mathrm{Fl}}(F)$, for all $B$;
2. (`VolEq`) all $\mathrm{vol}(c)$ are equal;
3. (`T1`) for each regular dominant weight $u$ with gaps at least $g > 0$, and $B + 1 > 4|\Psi|N^2(1 + \|u\|/g)$, the perturbed intersection numbers tend to $\mathrm{PP}_{B,c}(L_u^{d+1})$ and their ratio tends to the slope;
4. (`ThmB`) $\mathrm{PP}_B$ on monomials of degree $d+1$ is $\sum_c \mathrm{vol}(c)$ times the flag height $h_{\mathrm{Fl}}$ minus a correction linear in two vectors $\alpha, \beta$ (that depend on $B$), up to $O(\log B / B)$;
5. (`T2`) $\mathrm{PP}_B(L_u^{d+1}) \geq -C(d+1)\,\sum_c \mathrm{vol}(c)\,\deg_{\mathrm{Fl}}(L_u^d)\,[u]_B$ for $u, g, B$ as in `T1` with $B \geq 128$ and $B$ at least the number of bad primes;
6. (`MeanSlope`) under the same conditions, the mean of the slopes over the components is at least $-C\,[u]_B$.

Here $[u]_B = \Lambda_B \|u\|_1 + \min(j, N-j)\,\mathrm{spread}(u)$.

## Proof

Let $C_h, C_u$ be the constants of `NineGeoU` and $C_0 = \max(C_h + C_u/2, 0)$. Take $C = 2C_0 + 17$. From $3q + 1 \leq p + q$ we get $1 \leq p$ and $q \leq p$. The proof builds the hypotheses of `tower_weil_inputs_combined`, mostly from $\mathrm{Given}$:

- proportionality: `good_tower_real_agreement` and `real_tower_proportional`;
- the limits and the bounds `I1`, `I2`, `A1`: `real_tower_conv_I2`, `real_tower_I1` with `good_tower_real_I6`, `real_tower_A1`;
- nefness at small and bad primes, at large primes, of $\overline A$ and in general: `good_tower_M1_nef`, `good_tower_M2`, `root_model_nef_fibres`, `real_tower_nef_general` with `good_tower_real_conditions`;
- the height bounds `I5`, `I6` for points: `good_tower_I5`;
- the antisymmetry `I8`: [`full_intersection_tower_I8_identity`](/entry/full-intersection-tower-i8-identity/), with `CmpSt` and `Out.WeilSt`;
- Frobenius permutations and the Hecke relation `Prop6`: `good_tower_global_conditions` (with `CmpSt`, `HodgeLatticeFlagBound`, `TrivFlagOnHodge`) and `linked_tower_power_sum`;
- the symmetry `PropA`: `good_tower_propA_of_global_extra` (with `TwistAut`, `CmpPair`);
- the bound `PropF` with constant $4$: `PropFTop_holds` (with `PtsIntegrableStatement`) and `good_tower_real_extra` (with `FlatDegree`);
- `VolEq`: `good_tower_intersection_extra` (with `CmpSt`);
- the lower bound `SlopeLower` with constant $C_h + C_u/2$: `slope_lower_base_settings`, fed by `base_setting_of_good_tower` (with `NineGeoU`, `Out.WeilSt`); then `slopeLower_mono_top` raises the constant to $C_0$.

Then [`tower_weil_inputs_combined`](/entry/tower-weil-inputs-combined/) with $C_0$ and $C' = 4$ gives `T1`, `ThmB`, `T2` and `MeanSlope` with the constant $2C_0 + 3 \cdot 4 + 5 = C$.

## In the Lean code

The theorem is in [VolumeTheoremOfInputs.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/VolumeTheoremOfInputs.lean#L72). `VolumeTheoremX` is in [GoodTowerExistsX.lean](lean:Development/AutomorphicSpectrum/Statements/TowerExistence/GoodTowerExistsX.lean#L28), and the six properties in Proportional.lean and [HeckeSectionsIsotropicCommutatorPairingPower.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/HeckeSectionsIsotropicCommutatorPairingPower.lean#L76).

The helper `slopeLower_mono_top` (line 55) raises the constant of `SlopeLower`. All ten inputs are used. From $\mathrm{Given}$ the proof takes `PB.Inputs`, `Prov.HS` (the two successive minima bounds), `Prov.ZhangDimensionPushDownGrassmannianHeightBounds` and `AntisymPerturbation.Statement` by position.

The lemma `real_tower_conv_I2` takes a real tower $R$ but no property of $R$. We have not unfolded `NineGeoU`, `RealTower` or the lemmas of the list.
