---
id: exists-lower
title: The abelian part of a degeneration lies on a lower Shimura variety
kind: theorem
decl: GlobalTheory.LowDat.exists_lower
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ImportsTailExtra
covers: 307
status: drafted
drafted_by: writer@claude
---
Let $C$ be a degenerating family over an admissible base $R$, whose character group has rank $r \geq 1$ over $\mathcal{O}_E$. This theorem finds an isotropic submodule $Z$ of rank $r$ of the lattice, a datum $D'$ for $Z^\perp / Z$, and an object of the moduli problem of $D'$ whose abelian scheme is the abelian part of $C$. It is step 2 of [`exists_divFrom`](/entry/exists-div-from/). The proof only joins three lemmas.

## Statement

Use the moduli scheme $X^\circ_F$ for a datum $D$ with lattice $\Lambda$, form `EF` and signature $(p, q)$, and admissible bases, as in [`exists_taut_through`](/entry/exists-taut-through/). A family `UChart.Fam` over $R$ is a semi-abelian scheme $G$ with uniformization, with abelian part $B$ and character group $X$, and a generic point $y \colon \operatorname{Spec}\operatorname{Frac} R \to X^\circ_F$ that it classifies.

**Theorem.** Let $R$ be an admissible base and $C$ such a family with $r = \operatorname{rank}_{\mathcal{O}_E} X \geq 1$. Then there are:

1. an $\mathcal{O}_E$-submodule $Z \subset \Lambda$ of rank $r$ that is isotropic ($Z \subset Z^\perp$) and saturated ($n x \in Z$ with $n \neq 0$ implies $x \in Z$);
2. a datum $D'$ with signature $(p - r, q - r)$ and a surjection $f \colon Z^\perp \to \Lambda'$ with kernel $Z$ that preserves the forms;
3. an object $o'$ of the moduli problem of $D'$ over $R$ at the level `lowLevel l`, and a map $\varphi_B$ from its abelian scheme to $B$: a pullback of group schemes over the identity, $\mathcal{O}_E$-linear, matching the line bundles;
4. a semi-abelian scheme over $\operatorname{Frac} R$ that maps to $G$ and to the universal family at $y$, and, for each algebraically closed $F' \supset \operatorname{Frac} R$, Tate isomorphisms for $C$ and $o'$ with `XFLevel` (the level structures match), `FiltGraded` (for $n > 0$, the level-$n$ point of $a \in \Lambda$ has a representative with zero component `y` exactly when $a \in Z^\perp + n\Lambda$) and `LowGraded` (on $Z^\perp$, the Tate data of $C$ go through $f$ and $\varphi_B$ to those of $o'$).

We have not unfolded `TateIsoQ` or `QkPt`; the glosses in (4) follow the definitions in [FiltGraded.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FiltGraded.lean#L59). The result has the form of the description of a boundary stratum of a PEL Shimura variety by the smaller datum on $Z^\perp / Z$ (Lan, *Arithmetic Compactifications of PEL-Type Shimura Varieties*, 2013). We have not checked that the definitions match.

## Proof

`exists_isotropic_saturated_weight_filtration` gives $Z$ and the data of (4) for $C$. `exists_lower_datum_of_isotropic_saturated` gives $D'$ and $f$. `exists_lowerObject_abelianPart_tateIsometry` gives $o'$, $\varphi_B$ and the Tate isomorphisms for $o'$. The rest is bookkeeping.

## In the Lean code

The theorem is in [ImportsTailExtra.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ImportsTailExtra.lean#L15). The three lemmas are statement forms; we have not opened their proofs. The file name says nothing about its content. It takes a `UChart.Fam`: no parameters, forms or fan function.
