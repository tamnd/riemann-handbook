---
id: good-tower-antisymmetry
title: The swap relation on a good tower, with the singular metric statement filled in
kind: theorem
decl: SquareStatements.good_tower_antisymmetry
module: Development.WeilBound.CoreStatements.MultihomogeneousSquares.GoodTowerAntisymmetry
covers: 1618
status: drafted
drafted_by: writer@claude
---
This theorem only passes a proved lemma along. It is [the swap relation with one open hypothesis](/entry/antisymmetry-of-singular-statement/), with that hypothesis filled by a proved lemma. The theorem [full intersection tower relation](/entry/full-intersection-tower-i8-relation/) uses it, and that theorem is itself only a second name for this one. The real content is in [the swap relation from seven statements](/entry/good-tower-antisymmetry-of/).

## Statement

Assume the comparison statement `CmpSt`, the inputs `Given` and the Weil pairing statement `Out.WeilSt`. Let $E$ be a CM field with a host $H$, a datum $D$ with signature $(p_D, q_D)$, moduli spaces, a level $l$, a coefficient field and a model $Y$. Let $T$ be a root tower for $\Psi = \mathrm{CMType}(H)$ and $N = p_D + q_D$, with a good origin $o$ over $Y$ that satisfies `o.Extra`. Let $I$ be a full intersection system. If $p_D \geq 1$ and $q_D \geq 1$, then $T$ satisfies the relation $\mathrm{I8}$ for $I$ and the flag functional $h_{\mathrm{Fl}}$. In words: the defect $\mathrm{PP}_c(\lambda) - \mathrm{vol}(c)\, h_{\mathrm{Fl}}(\lambda)$ changes sign when two adjacent entries of the weight $\lambda$ are swapped. The [entry on the seven statements](/entry/good-tower-antisymmetry-of/) gives the relation in full.

## Proof

The statement is the proposition `GoodTowerAntisymmetry`. The proof is `antisymmetry_of_singular_statement` applied to `HeightCancellation.stSing`, a proof of the singular metric statement `StSing`. That proof is `Sing.stSing_of` applied to seven lemmas (`c0`, `c1`, `c2`, `c3w`, `c3o`, `c4`, `c5`), whose statements we have not unfolded.

## In the Lean code

The theorem is in [GoodTowerAntisymmetry.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/GoodTowerAntisymmetry.lean#L20). It writes out the body of `GoodTowerAntisymmetry` from [GoodTowerAntisymmetryOf.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/GoodTowerAntisymmetryOf.lean#L13). The proof of `StSing` is in [StSing.lean](lean:Development/WeilBound/CoreStatements/JacobiBlockDeterminants/StSing.lean#L8).
