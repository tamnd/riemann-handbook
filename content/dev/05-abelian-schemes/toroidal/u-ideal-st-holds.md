---
id: u-ideal-st-holds
title: A boundary ideal with the valuations of a fan function
kind: theorem
decl: GlobalTheory.UPoinc.uIdealSt_holds
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnitaryCompactificationExistsBoundaryIdeal
covers: 458
status: drafted
drafted_by: writer@claude
---
This theorem builds, on an integral compactification $Z_o$, an ideal sheaf supported on the boundary whose valuations along traits are $d\varphi$. It works one irreducible component at a time and then multiplies the pieces. It is the proof of [the boundary ideal statement](/entry/unitary-compactification-exists-boundary-ideal/), which [the normalized blowup with separation](/entry/u-poin-st-x-sep/) uses. Below it are 458 declarations.

## Statement

The statement is `UIdealSt`, as in [the statement entry](/entry/unitary-compactification-exists-boundary-ideal/). The condition `UValOn` for $J$ and $d$ reads as follows. Let $W$ be a complete discrete valuation ring of characteristic $0$ with uniformizer $\varpi$. Let $\chi \colon \operatorname{Spec} W \to Z_o$ and $y \colon \operatorname{Spec} \operatorname{Frac} W \to X_F$ with $i \circ y = \chi$ on the generic point. Let $t$ be a semi-abelian scheme over $W$ that extends the abelian scheme of $y$, with degeneration data $P$, and let $\beta$ be a form of level $1$ such that $P$ is monomial in $\varpi$ with form $\beta$. Then $\chi^* J = (\varpi^n)$ with $n = d\,\varphi(\beta)$.

A local version, `UValThru`, asks the same only for $\chi$ whose closed point lies in a set $A$.

## Proof

1. $Z_o$ is projective over the Dedekind domain $o$, so it is noetherian. It is normal, so its stalks are domains. Hence $Z_o$ has finitely many irreducible components, and each one is open and closed (`CompPart.isOpen_of_mem`). Each point lies in exactly one of them.
2. Let $A$ be a component that meets $i(X_F)$. [The theta setup over a component](/entry/exists-unitary-theta-setup-ideal-over-component/) gives a theta setup $X_1$ with $\pi \colon M \to Z_o$ onto $A$, $\iota \geq 1$ and an ideal $J_1$ on $M$, supported off $\pi^{-1} i(X_F)$, with `UValThru` for $\iota$ along $\pi$. Then `T.ideal_descent_to_component_compactification` gives $d_A \geq 1$ and an ideal $J_A$ on $Z_o$, supported in $A$ and off $i(X_F)$, with `UValThru` on $A$ for $d_A$.
3. Let $A$ be a component that misses $i(X_F)$. Take $d_A = 1$ and $J_A = \mathcal{O}$. The support is empty. `UValThru` holds by `uValThru_top_of_disjoint`: the generic point of $\chi$ lies in $i(X_F)$ and specializes to a point of the open set $A$, so it lies in $A \cap i(X_F) = \emptyset$. Thus no such $\chi$ exists.
4. `exists_uValOn_of_pieces` takes $d = \prod_A d_A$ and $J = \prod_A J_A^{d/d_A}$. Near a point of $A$ every other factor is the unit ideal, so $\chi^* J = (\chi^* J_A)^{d/d_A} = (\varpi^{n_A d/d_A})$ and $n_A d/d_A = d\,\varphi(\beta)$.

## In the Lean code

The theorem is in [UnitaryCompactificationExistsBoundaryIdeal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryCompactificationExistsBoundaryIdeal.lean#L19). `UValThru`, `uValThru_top_of_disjoint` and `exists_uValOn_of_pieces` are in [UValThruTopOfDisjoint.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UValThruTopOfDisjoint.lean#L21). `UValOn` is in [ExistsOverIff.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsOverIff.lean#L20).

Step 3 never applies. `UCompact` asks that $i(X_F)$ is dense in $Z_o$, and each component is a nonempty open set, so each component meets $i(X_F)$. The proof does not use this and splits into cases. We have not opened the proof of the descent lemma `T.ideal_descent_to_component_compactification`; only its statement, which has no entry in the outline.
