---
id: exists-wach
title: The local Wach construction assembled from its layers
kind: theorem
decl: GlobalTheory.HWL.Assembly.exists_wach
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsLocalWachFunctor
covers: 393
status: drafted
drafted_by: writer@claude
---
This theorem builds, at one prime $l$, Wach modules, étale $(\varphi, \Gamma)$-modules and a comparison between them, for every good triple of fields. It is the target of [the local statement](/entry/exists-local-wach-functor/). The proof builds seven layers, one lemma for each. One layer, the Wach lattice, is not built here: it comes from the hypothesis `WachEx`. The Wach lattices themselves come from the Bhatt-Scholze theorem in [the global assembly](/entry/exists-hw-fon-cmp-ties/).

## Statement

The statement is the same as in the local statement entry. Given `LocTied`, `FaithH` and `WachEx` at $l$, there are $H$ (`LocHW l P`), $F$ (`LocFon l P A H`) and a comparison in `LocCmpT l P A H F`.

## Proof

`tied_uniformiser` uses `LocTied` to show two facts in $B_{\mathrm{dR}}$: $\mu - t \in \mathrm{Fil}^2$, and $\pi_1$ has an inverse in $\mathrm{Fil}^0$. Then `exists_of_layers` reduces the theorem to one record `Layers` for each good triple $(K, s, L')$. The proof fills the record in this order.

1. $\Gamma$ (`nonempty_gamS`): the group $\Gamma$, its cyclotomic character, and a generator $\gamma$ with $v(\chi(\gamma) - 1) = s$.
2. $R$ (`nonempty_wSer`): the power series ring $O[[X]]$ with Frobenius $\varphi(X) = (1+X)^p - 1$, where $p$ is the prime of the period data, and an action of $\gamma$, and a ring $\mathcal E$ over it in which $\pi$ is a unit.
3. $I$ (`IoLayer.main`): maps of these rings into two rings `RA` and `RW` (not unfolded here). The first sends $\pi$ to $1 \otimes ([\varepsilon] - 1)$. The map on $\mathcal E$ commutes with $\varphi$ and $\Gamma$. The condition `IoW` fixes their values on Teichmüller lifts of roots of unity.
4. $E$ (`nonempty_wEt`): the étale module functor $T \mapsto D(T)$, free of rank $\mathrm{rank}\, T$, with an injective map $D(T) \to R_W \otimes T$ that respects $\varphi$ and the Galois action. Its input is a basis from `exists_etBasis`, which uses `FaithH`.
5. $M$: the Wach lattice $N(T) \subseteq D(T)$. This is `hW` applied to the layers above.
6. $C_l$ (`exists_classMaps`): class maps from Herr cocycles to lattice cohomology.
7. $C_m$ (`nonempty_cmpS`): the comparison of $N(T)$ with $V \otimes B$. It uses `LocTied` and $M$.

## In the Lean code

The theorem is at [ExistsLocalWachFunctor.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsLocalWachFunctor.lean#L16). The pass-through of `WachEx` is at line 25. The layer types and `exists_of_layers` are in [ExistsOfLayers.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ExistsOfLayers.lean#L311). We have not unfolded `WCl` and `WCmp` in detail.

The Wach layer `WN` has a field `N_junk` (line 176): if $T$ is not crystalline, then $N(T) = 0$. So $N$ is a total function with a junk value. The other conditions on $N$ are stated only for crystalline $T$, or are trivial for the zero module.
