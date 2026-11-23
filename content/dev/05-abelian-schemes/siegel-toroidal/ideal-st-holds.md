---
id: ideal-st-holds
title: A boundary ideal with the valuations of a fan function, by components
kind: theorem
decl: GlobalTheory.Poinc.idealSt_holds
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFanOrderIdealThetaCompactification
covers: 442
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{IdealSt}$: on a theta compactification $Z$ of the Siegel moduli scheme there is an ideal off the interior whose valuations along traits are $d\varphi(\beta)$. It cuts $Z$ into its clopen irreducible pieces, finds an ideal on each piece, and glues. It goes to [`poinSt`](/entry/poin-st/) through [the statement form](/entry/exists-fan-order-ideal-theta-compactification/).

## Statement

The statement $\mathrm{IdealSt}$ is given in full in [the statement form](/entry/exists-fan-order-ideal-theta-compactification/). The objects (theta compactifications, traits, `ValOn`) are defined in [`poinSt`](/entry/poin-st/). In short: for $g \geq 1$, odd $n \geq 3$, a theta compactification $i \colon X \to Z$ and a polarization function $\varphi$ for $g$, there are $d \geq 1$ and an ideal $J$ on $Z$, with support off $i(X)$, such that $\xi^* J = (\varpi^{d\varphi(\beta)})$ for each trait and each $\xi \colon \operatorname{Spec} V \to Z$ that extends $i \circ y$.

## Proof

1. **Pieces.** $Z$ is projective over $\mathbb{Z}[\zeta_n, 1/n]$ and normal. By `exists_clopen_irreducible_partition_of_normal_proj`, $Z$ is the disjoint union of finitely many sets $W_c$, each clopen and irreducible.
2. **An ideal on a model of each piece.** Fix $c$. By [`exists_thetaSetup_ideal_over_clopen_component`](/entry/exists-theta-setup-ideal-over-clopen-component/), there are a theta setup with a normal model $M$ and a finite map $\pi \colon M \to Z$ with image $W_c$, an integer $\iota \geq 1$ and an ideal $J_1$ on $M$ off $\pi^{-1}(i(X))$ with valuations $\iota\varphi(\beta)$ along traits through $\pi$.
3. **Down to $Z$.** `idealDescent_thetaModel_to_component_traitOrders` turns $J_1$ into $d_c \geq 1$ and an ideal $J_c$ on $Z$ with support in $W_c \setminus i(X)$. Its valuations are $d_c\varphi(\beta)$ along each trait whose closed point maps into $W_c$.
4. **Gluing.** `exists_fanOrder_ideal_glued_clopen_pieces` takes the finite family $(W_c, J_c, d_c)$ and gives one $d' \geq 1$ and one ideal $J'$ on $Z$ with support off $i(X)$ and `ValOn` for $(i, J', d')$.

The rest is bookkeeping: `choose` turns step 3 into functions of $c$.

## In the Lean code

The theorem is in [ExistsFanOrderIdealThetaCompactification.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFanOrderIdealThetaCompactification.lean#L17). Steps 1, 3 and 4 cite statement forms:

- `GlobalTheory.T.exists_clopen_irreducible_partition_of_normal_proj`, a renaming of `GlobalTheory.irreducibleComponents_clopen_partition`;
- `GlobalTheory.T.idealDescent_thetaModel_to_component_traitOrders`, a renaming of `GlobalTheory.PoincDown.idealDescent`;
- `GlobalTheory.T.exists_fanOrder_ideal_glued_clopen_pieces`, a renaming of `GlobalTheory.Poinc.exists_valOn_of_pieces`.

We have not opened the proofs of these three. So we do not know how the gluing chooses $d'$ and $J'$ from the $d_c$ and $J_c$. The gluing lemma is stated for any Siegel family over any base ring, and needs only that the $W_c$ are clopen and cover $Z$ with no overlap.
