---
id: enstable-and-jumps
title: The monodromy of a Breuil-Kisin module converges at the uniformizer, and its jumps are Hodge-Tate jumps
kind: theorem
decl: GlobalTheory.NgalFil.ENStable_and_jumps
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.BreuilKisinLatticeStableAndHodgeTateJumps
covers: 345
status: drafted
drafted_by: writer@claude
---
This theorem joins two lemmas into one statement: the operator $E N$ maps the lattice $M$ into series that converge on a closed disc, and the jumps of the Breuil-Kisin filtration lie among the Hodge-Tate jumps of the Galois side. It is the proof behind the second name [`breuilKisin_lattice_stable_and_hodgeTate_jumps`](/entry/breuil-kisin-lattice-stable-and-hodge-tate-jumps/), which step 5 of [`exists_pack_isOfType`](/entry/exists-pack-is-of-type/) uses. The content is in the two lemmas, which have no entries.

## Statement

The notation is that of [the entry on the connection](/entry/int-conn-taylor-main/): a $\varphi$-module $P$ with matrices $Y_\tau$, its lattice $M$, $\varphi^*M$, $E = X^e + \ell$, and the canonical connection $\nabla$. Put $N = X\nabla$ (`conn`). Let $R$ be the ring of series in $L[[X]]$ that converge on the closed disc $|X| \le |\ell|^{1/e}$, and $M_R$ (`Man`) the extension of $M$ to $R$. The filtration of $P$ (`filL`) is $\mathrm{Fil}^i = (\varphi^*M \cap E^i M) + E\,\varphi^*M$ after $\ell$ is inverted, and $i$ is a *jump* of $P$ if $\mathrm{Fil}^{i+1} \ne \mathrm{Fil}^i$.

**Theorem.** Assume `FontaineBcris`. Let $\ell \ne 2$, let $T$ be a lattice of $G_{\mathbb{Q}_\ell}$ with representation $V$, and let $I$ identify $P$ with $T$ over Witt vectors. Let $j_B$ identify $B^n$ with $B \otimes T$, for the crystalline period ring $B$ of standard period data. Assume that $j_B$ agrees with $I$ on the lattice (`IsCrisCmp`), and that $G_{K_\varpi}$ fixes the image under $j_B$ of each horizontal vector $\xi(d)$ (`IsHoriz`). Then:

1. $E N (M) \subset M_R$;
2. for each set $U \subset \mathbb{Z}$: if the Hodge-Tate jumps of $V$ at each embedding lie in $U$ (`JumpsInV`), then the jumps of $P$ lie in $U$.

## Proof

Part 1 is `monodromyOperator_maps_into_completion`. Part 2 is `filtration_jumps_breuilKisin_subset_galoisJumps`, which takes part 1 as a hypothesis. Both take `FontaineBcris` and all the other hypotheses as arguments. The proof only applies the two lemmas.

## In the Lean code

The theorem is in [BreuilKisinLatticeStableAndHodgeTateJumps.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BreuilKisinLatticeStableAndHodgeTateJumps.lean#L13). `Man`, `EN`, `filL` and `jumps` are in [ExistsEqAlgebraMapAddPowMul.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ExistsEqAlgebraMapAddPowMul.lean#L201), and `IsCrisCmp` and `IsHoriz` in [IsPotential.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/IsPotential.lean#L32). We did not open the proofs of the two lemmas, and we did not unfold `IsStd` or the Hodge filtration `FildR` behind `JumpsInV`.

The name "lattice stable" refers to part 1. Part 1 does not say that $M$ is stable: $E N$ maps $M$ into the larger module $M_R$.
