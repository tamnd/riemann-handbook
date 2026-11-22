---
id: good-tower-and-volume
title: A good tower exists and the volume theorem holds
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Top.goodTower_and_volume
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.GoodTowerVolumeTheorem
covers: 17796
status: drafted
drafted_by: writer@claude
---
This theorem gives the two statements that the volume branch of [the Weil bound](/proof/weil-bound/) needs (its Step 4). The first says that a tower of integral models with a good origin exists. The second, the volume theorem, bounds the arithmetic self-intersection numbers of each such tower from below. The proof builds seven inputs from six hypotheses and sends them to [the volume theorem from its inputs](/entry/volume-theorem-of-inputs/). Its statement form is [`good_tower_volume_theorem`](/entry/good-tower-volume-theorem/), whose user is [`goodTower_volume_of_reduced`](/entry/good-tower-volume-of-reduced/).

## Statement

The hypotheses are these.

1. $\mathrm{Given}$: a conjunction of fourteen statements, among them a resolution statement `ResKStatement`, `FarguesHodgeTate`, `GagaSections`, the bundle `PB.Inputs` of facts on intersection systems, and `Prov.HS`, which contains [Zhang's successive minima bounds](/learn/arakelov/#heights). This proof uses four of them by position.
2. $\mathrm{PtsInt}$: for an arithmetic variety in multiprojective coordinates with a good linear projection, smooth hermitian lines $\overline L_1, \dots, \overline L_e$ and a section $s$ of a smooth hermitian line $\overline A$, the sum over the fibres of the projection of the densities built from $\log\|s\|$ and the metrics of the $\overline L_j$ is integrable. We have not unfolded `sheetDensity`.
3. $\mathrm{Avoid}$: for a commutative ring $R$ and a finite set of multihomogeneous primes of a multigraded polynomial ring over $R$, there is a multidegree $d_0$ such that in each multidegree $d \geq d_0$ some multihomogeneous element lies in none of the primes.
4. $\mathrm{Weil}$: for a polarized abelian scheme $A$ over a locally noetherian $S$ and $k \geq 1$, each pair $x, y$ of $k$-torsion points has a unique Weil pairing value $e_k(x, y) \in \Gamma(S, \mathcal{O}^\times)$; it is multiplicative in $x$, $e_k(x, x) = 1$, and $e_{kl}(x, y) = e_k(x^l, y)$ when $kl$ is invertible.
5. $\mathrm{Fam}$ (`FamilyExistsPos`): at each good prime $p$ of a Hodge component, there are local lattice families with Frobenius labels. We have not unfolded `IsPreFamily` and `IsFamilyOf`.
6. $\mathrm{CmpPair}$: let $M, M'$ be two root models tied to the same integral model, related by an automorphism $g$ of the host, an automorphism $\Phi$ of the moduli space over its base, and the permutation $\pi$ of CM types that $g$ induces, with some compatibility conditions. Then the normalized intersection numbers of the metrized lines $x_t(w_j)$ on $M$ and of the lines $x_t(\pi w_j)$ on $M'$ differ by a term that tends to $0$ as $t \to 0^+$.

**Theorem.** If 1 to 6 hold, then:

- (`GoodTowerExistsX`) for each CM field $E$, host $H$, datum $D$ with $p, q \geq 1$, level $l$, coefficients $c$ and integral model $Y$ that is global and has split components, there are a root tower $T$ for the CM types of $H$ and $N = p + q$, and a good origin $o$ of $Y$ for $T$ that satisfies `Extra`;
- (`VolumeTheoremX`) there is $C \geq 0$ such that each good root tower over an abelian CM field with $q \geq 1$, $3q + 1 \leq p + q$ and at most $4\,\#\mathrm{CMType}(H)\,(p+q)^2$ bad primes satisfies six properties, the last a lower bound for the mean slope.

The [entry of the volume theorem](/entry/volume-theorem-x-of-inputs/) defines root towers and states the six properties. `Extra` says two things: on each component the map to projective space has local holomorphic lifts and an injective differential, and a number `R p` of the origin equals $4$ at each prime of `S B`.

## Proof

The proof has two independent parts.

**The tower.** From $\mathrm{Given}$ it takes `ResKStatement` and `GagaSections`. With them, `flat_zero_from_resolution_and_gaga` and `flat_first_from_resolution_and_gaga` give the existence of flat generators of a line, on the whole model and on each component. Then `exists_good_root_tower`, with $\mathrm{Given}$ and $\mathrm{Weil}$, gives the tower and its good origin.

**The volume theorem.** The proof applies `volume_theorem_of_inputs` to $\mathrm{Given}$, $\mathrm{PtsInt}$, $\mathrm{Weil}$, $\mathrm{CmpPair}$ and six statements that it builds:

- constants $C_h, C_u$ with `NineGeoU`, from `exists_geometric_height_constants` ($\mathrm{Given}$, $\mathrm{Weil}$, `FlatDegree`);
- `HodgeLatticeFlagBound`, from [`model_on_hodge_from_family`](/entry/model-on-hodge-from-family/) and $\mathrm{Fam}$;
- `TrivFlagOnHodge`, from `triv_flag_on_hodge_of_fargues` and `FarguesHodgeTate`;
- `FlatDegree` and `TwistAut`, from `FlatDegree_holds` and `TwistAut_holds`, which have no hypotheses;
- `CmpSt`, from `comparison_of_inputs_avoidance` with `PB.Inputs`, $\mathrm{Avoid}$ and `ResKStatement`.

## In the Lean code

The theorem is in [GoodTowerVolumeTheorem.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerVolumeTheorem.lean#L36). The two conclusions are defined in [GoodTowerExistsX.lean](lean:Development/AutomorphicSpectrum/Statements/TowerExistence/GoodTowerExistsX.lean#L22), and $\mathrm{Given}$ in [GoodOrigin.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/GoodOrigin.lean#L67).

The proof takes the parts of $\mathrm{Given}$ by position: `hG.2.2.2.2.1` is `ResKStatement`, `hG.2.2.2.2.2.2.1` is `FarguesHodgeTate`, `hG.2.2.2.2.2.2.2.1` is `GagaSections` and `hG.2.2.2.2.2.2.2.2.2.1` is `PB.Inputs`.

The conjunction is only a pair. The proof of `VolumeTheoremX` does not use the tower of the first part: the volume theorem is a statement about every good tower. The first part uses only $\mathrm{Given}$ and $\mathrm{Weil}$.

The caller `goodTower_volume_of_reduced` builds `CmpSt` with the same call `comparison_of_inputs_avoidance hPB hAvoid hResK`, to get `CmpPair`. So `CmpSt` is built twice. This is harmless.
