---
id: exists-lab-cover-of-pel-ok
title: A labelled cover for degeneration data of unitary PEL type, from one complete trait
kind: theorem
decl: GlobalTheory.Mum.exists_labCover_of_pelOK
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsLabelledCoverUnitaryPELTypeFiniteExt
covers: 424
status: drafted
drafted_by: writer@claude
---
This theorem builds a labelled cover for degeneration data of unitary PEL type, after a finite extension of the base. It uniformises the data over one complete discrete valuation ring, uses that trait to choose torsion labels, and puts the labels on a uniformised cover. It is restated as [`exists_labelledCover_unitaryPELType_finiteExt`](/entry/exists-labelled-cover-unitary-peltype-finite-ext/), step 3 of [`has_of_base`](/entry/has-of-base/). The cover then goes to [`hasFin_of_labCover`](/entry/has-fin-of-lab-cover/).

## Statement

Let $R$ be a local domain with `Base R`, and $D$ degeneration data over $R$ for $\mathfrak{m}$ (see the [entry for `has_of_base`](/entry/has-of-base/)). Let $E$ be a CM field.

- A host datum $H$ (`Host E`) fixes a prime $d \equiv 7 \pmod{16}$, an element $r \in \mathcal{O}_E$ with $r^2 = -d$, an element $w_0$ with $2w_0 = 1 + r$, and complex conjugation on $\mathcal{O}_E$. It asks that $E$ be unramified over its maximal real subfield.
- A PEL datum `Dm : Datum H` is a finite projective $\mathcal{O}_E$-module $L$ with an alternating unimodular $\mathbb{Z}$-form $\langle\ ,\ \rangle$ such that $\langle ax, y\rangle = \langle x, \bar a y\rangle$, a signature $(p, q)$ with $p + q = \operatorname{rank} L$, and a complex structure on $L \otimes \mathbb{R}$ of that signature.
- `PelOK Dm D o` says: $p = q \geq 1$; a twisted trace form condition at $w_0$ (`TraceFormTwistIso`); over each algebraically closed field over $K$, each embedding of $\mathcal{O}_E$ acts on the Lie algebra of the abelian part with a multiplicity $n$ with $n + \operatorname{rank} X = p$ (`LieMult`); and Tate isomorphisms for each compatible system of roots of unity (`TateIsoQ`). We have not unfolded `TraceFormTwistIso`, `LieMult` or `TateIsoQ`.

**Theorem.** If $X \neq 0$ and `PelOK Dm D o`, then after a finite extension $R \to R'$ (`FinExt`) a pullback $D'$ of $D$ has a labelled cover.

## Proof

1. `exists_odd_prime_isUnit_in_localRing`: $3$ or $5$ is a unit in $R$, since $2 \cdot 3 - 5 = 1$ and $R$ is local. Call it $n$.
2. `PrimeUnif.exists_cdvr`: there is an injective local map $\varphi \colon R \to V$ to a complete discrete valuation ring. Pull $D$ back to $D_V$ (`MumPull.exists_pull`). `PelOK` and $X \neq 0$ pass to $D_V$ (`pelOK_of_isPullDeg`).
3. `exists_mumfordUniformisation_unitaryTypeTrait`: after a finite extension $V \to V'$, a pullback of $D_V$ uniformises a semi-abelian $G'$, with a polarised $A'$ that satisfies `HypS` (two inverse group automorphisms of $A'$ with isomorphisms of cube line bundles).
4. `exists_labelledSemiAbelianCover_finite_extension`: from this trait, after a finite extension $R \to R_1$, there are a pullback $D_1$, a polarised $A$ over the fraction field of $R_1$ with `HypS`, and labels on the torsion points of $D_1$ that match a uniformisation along one trait (`OneTrait`) and are Galois equivariant on $n^j$-torsion (`GalEqN n`).
5. `exists_uniformised_cover_finite_ext_of_symmetric`: after a finite extension $R_1 \to R_2$, there is a uniformised cover $C$ (`UCover`) whose generic fibre is the pullback of $A$.
6. `exists_torsionLabels_finiteExtension_galoisEquivariant` moves the labels to $C$ and the pullback $D_2$ of $D_1$.
7. `nonempty_labelled_cover_of_odd_prime`: $C$, the labels and $n$ give `LabCover D₂`.

The rest is bookkeeping: $R_1$ and $R_2$ satisfy `Base`, and the extensions and pullbacks compose.

## In the Lean code

The theorem is in [ExistsLabelledCoverUnitaryPELTypeFiniteExt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLabelledCoverUnitaryPELTypeFiniteExt.lean#L35). The helper `exists_odd_prime_isUnit_in_localRing` (line 26) is in the same file. `PelOK` and `LabCover` are in [ExistsToricRankOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsToricRankOne.lean#L90), `Host` and `Datum` in [TwoWeightEqOneAddRoot.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/TwoWeightEqOneAddRoot.lean#L14), and `UCover` and `GalEqN` in [IsProjOverWeierstrass.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsProjOverWeierstrass.lean#L44).

We read the statements of the lemmas in steps 2 to 7, not their proofs. `PelOK` is used only in steps 2 and 3.
