---
id: ker-ent-c-true
title: Rescaled adapted bases give a kernel entry that is tied and adapted
kind: theorem
decl: GlobalTheory.Pdv.kerEntC_true
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.TrueColumnChoicesKernelDatumAdaptedBases
covers: 515
status: drafted
drafted_by: writer@claude
---
This theorem chooses, at each local place, bases of the local lattices of the theta objects, and shows that the kernel entry made from them has the two properties that `EntOk` asks for. It is used under the second name [`trueColumnChoices_kernelDatum_adaptedBases`](/entry/true-column-choices-kernel-datum-adapted-bases/). The new work here is a rescaling of the bases by units.

## Statement

Take a true column choice $I$ with its law $l$ and later datum $Z$, a divisor datum $Y$, standard lifts $O_{u,\mu}$ of the twisted theta objects, and places $P$ (`EntPl`). At a place $w$ with residue characteristic $p_w$, a *basis family* gives for each $u, \mu$, level $i$, class $c$ and embedding $\tau$ a square matrix $B$ over $\mathbb{C}_{p_w}$. It is *good* (`BasOk`) if for $i \le m$ each $B$ is a basis of the lattice of $O_{u,\mu}$ at $(i, c)$: $\det B \ne 0$, $B^{-1}$ maps the lattice to integral vectors, and the columns are integral combinations of lattice vectors (`BasR`).

`KerEntHyp` asks, at the places $w$ that are free of the level (`LevFree`: $p_w$ is not one of a finite list of primes of the data), for four things: the target projections have the norms of global elements, the local lattices are cut out by norm $\le 1$ conditions on the source and on the target projections, and a kernel formula relates the target projection to the source projection.

**Theorem.** Assume `I.Ok`, the pin conditions, that the places of $Y$ are those that $I$ fixes, that $O$ is standard, the unfolding conditions below level $m$, and integral jets (`ColIn.JetsIn`). Then there are a basis family $B$ and a proof $h$ of `KerEntHyp` for $B$ such that the kernel entry $K_h$ (`kerEntC`) satisfies `EntOk`: at each level-free place $K_h$ is tied to $O$ (`KFTie`, with its unit condition), and $K_h$ is adapted (`AdaptedTh`).

## Proof

1. `AdaptedBases.exists_sys` gives at each place a system of matrices $P_w$ over the number field $E$ of the data that map to bases of the lattices, are invariant under embeddings with the same prime, and are unitary duals for conjugate embeddings. Let $B_0 = \tau(P_w)$. Then $B_0$ is good.
2. [`kernelEntryHyp_of_trueColumnChoices`](/entry/kernel-entry-hyp-of-true-column-choices/), a second name of [`kerEntHyp_true`](/entry/ker-ent-hyp-true/), gives `KerEntHyp` for $B_0$, since the entries of $B_0$ lie in the image of $E$ (`tauEmb_mem`).
3. Let $a_w = \lambda_w(g_w)^{-1}$ (`lamC`) at the inert, signal and ramified places (`AdPl`), where $g_w$ is the generator `dgen`, and $a_w = 1$ elsewhere (`adUnit`). By `dgenUnitAd`, $|a_w| = 1$ (`norm_adUnit`). Put $B = a_w^{\,i} B_0$ at level $i$ (`scB`).
4. Scaling by a unit keeps a basis (`basOk_scB`). It multiplies the projections by factors of norm 1, so `KerEntHyp` stays true (`kerEntHyp_scB`). This step needs `CanOnto`, from `toy_entPl_canOnto`, and `RhoAlg`, from `rhoAlg_std`.
5. $B$ has the form that `AdaptedEnt` asks for, by the definition of $a_w$. Then `adaptedTh_kerEntC` gives `AdaptedTh`, and `kfTieOf`, `kfTieOf_un` give the ties.

## In the Lean code

The theorem is at [TrueColumnChoicesKernelDatumAdaptedBases.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/TrueColumnChoicesKernelDatumAdaptedBases.lean#L219). The scaling lemmas are in the same file, from line 20; `kerEntHyp_scB` is at line 160. `exists_sys` is in [NormNatCastEqOne.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/NormNatCastEqOne.lean#L158), `adaptedTh_kerEntC` in [AdaptedThKerEntC.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/AdaptedThKerEntC.lean#L129), `KerEntHyp` in [KerEntHyp.lean](lean:Formalism/LocalToGlobal/KernelLattices/ColumnData/KerEntHyp.lean#L140) and `AdaptedEnt` in [AdaptedEnt.lean](lean:Formalism/LocalToGlobal/KernelLattices/AdaptedEnt.lean#L30). We did not unfold the projections `prSC`, `prTC` or the theta map `thAtW`.

Odd points:

- `toy_entPl_canOnto` has "toy" in its name, but it proves `CanOnto` for every datum and every $P$ ([DominantWeightPolynomialFunctionalMinorsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/DominantWeightPolynomialFunctionalMinorsStatement.lean#L11)).
- `kerEnt_true` at the end of `AdaptedThKerEntC.lean` proves a similar result with `kerEntR` in place of `kerEntC`.
