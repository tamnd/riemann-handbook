---
id: exists-div-from
title: The periods of a degenerating family come from a lower base
kind: theorem
decl: GlobalTheory.VData.exists_divFrom
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.DegeneratingFamilyDataFromBaseAlgClosedResidue
covers: 443
status: drafted
drafted_by: writer@claude
---
This theorem shows that a degenerating monomial family over a complete local domain $V$ is obtained from a lower base $L$ (a base for a Shimura datum of smaller signature) by a local map $W \to V$ and monomial periods. It proves [the statement form](/entry/degenerating-family-data-from-base-alg-closed-residue/), which is step 1 of [`exists_canon_through`](/entry/exists-canon-through/).

## Statement

The statement is that of [the statement form](/entry/degenerating-family-data-from-base-alg-closed-residue/). Lower bases and `DivFrom` are as in [`exists_canon_through`](/entry/exists-canon-through/).

## Proof

Let $C$ have abelian part $B$, character group $X = X_C$ of rank $r \geq 1$, and the map $c \colon X \to B(V)$ of its degeneration datum. Let $M'$ be the integer of the level.

1. $X$ is finite projective over $\mathcal{O}_E$, so $r \geq 1$ as $X \neq 0$.
2. [`LowDat.exists_lower`](/entry/exists-lower/) gives a datum $D'$ with $p' = p - r$, $q' = q - r$, an object $o'$ of the moduli problem of $D'$ over $V$, and a map $\varphi_B$ from the abelian scheme $G'$ of $o'$ to $B$. It is a pullback of group schemes over the identity, it respects the $\mathcal{O}_E$-actions, and it matches the line bundles.
3. `grpPullback_iso` turns $\varphi_B$ into an isomorphism $i \colon B \to G'$, inverse to $\varphi_B$. It also respects the $\mathcal{O}_E$-actions.
4. The points $x(y) = i \circ c(y)$ of $G'(V)$ are additive and $\mathcal{O}_E$-linear in $y$. $M'$ is a unit in $V$, since $V$ is an algebra over $F$. `abelian_scheme_module_action_homomorphism` divides them: it gives additive, $\mathcal{O}_E$-linear points $x'(y)$ with $x'(M'y) = x(y)$. It uses that $V$ is Noetherian and complete with algebraically closed residue field.
5. `lowerDatumObject_comes_from_base_of_linearPoints` applied to $(o', x')$ gives the lower base $L$ with ring $W$, a local map $\theta_0 \colon W \to V$ compatible with $F$, an isomorphism $e \colon X \to X_L$, and a map from $o'$ to the object of $L$ over $\operatorname{Spec}\theta_0$ that sends $x'(y)$ to $c_L(e y)$.
6. The cone condition on the forms $\delta_i$ of $C$ says that they are part of a $\mathbb{Z}$-basis of the balanced forms on $X$. Move this basis to $X_L$ by $e$ to get $(\varepsilon_k)$.
7. `exists_periods_monomialFamily_coords_over_base` takes the composite map $B \to G' \to B_L$, which sends $c(y)$ to $c_L(M' e y)$, and gives the elements $t_k$ with the associate and unit conditions and `DivFrom`.

The rest is bookkeeping: three isomorphisms of line bundles are composed for step 7, and the signature equations come from step 2.

## In the Lean code

The theorem is in [DegeneratingFamilyDataFromBaseAlgClosedResidue.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegeneratingFamilyDataFromBaseAlgClosedResidue.lean#L16). It calls `LowDat.exists_lower`, `grpPullback_iso` and the statement forms of `AbDivLocal.exists_divided_linear`, `UCanon.lowBase_of_linearPoints` and `UCanon.Periods.exists_divFrom`. We have not opened the proofs of the last three.

The proof drops most of the output of `exists_lower`: the isotropic submodule $Z$, the map $f$, and all of its statements about Tate modules.
