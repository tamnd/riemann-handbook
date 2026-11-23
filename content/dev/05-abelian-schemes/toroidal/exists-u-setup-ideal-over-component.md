---
id: exists-u-setup-ideal-over-component
title: A boundary ideal on a theta model over one component
kind: theorem
decl: GlobalTheory.UPoinc.exists_uSetup_ideal_over_component
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUnitaryThetaSetupIdealOverComponent
covers: 439
status: drafted
drafted_by: writer@claude
---
Let $Z$ be the integral compactification of a unitary moduli scheme. This theorem takes one irreducible component $A$ of $Z$ that meets the interior. It finds a normal model $M$ built from theta constants, with a finite map $\pi \colon M \to Z$ onto $A$, and an ideal on $M$ that lives on the boundary and has the valuations of $\iota\varphi$. It proves [the statement form](/entry/exists-unitary-theta-setup-ideal-over-component/), which [`uIdealSt_holds`](/entry/u-ideal-st-holds/) uses for each component.

## Statement

Fix $E$, $H$, a datum of signature $(p, q)$ with $p + q \geq 1$, the moduli scheme $X^\circ_F$, and $\varphi$ with `IsPolFan` in rank $\min(p, q)$, as in [`uPoinStX_sep`](/entry/u-poin-st-x-sep/). Let $C$ be a `UCompact` (see [the theta compactification](/entry/umin-theta-compactification-exists/)): a normal projective $Z$ over a Dedekind ring $o$, with $i \colon X^\circ_F \to Z$.

A theta setup $X_1$ over $C$ (`USetup`) is: a theta system $S$ over a ring $o_1$ and a field $\Omega_1$ (theta constants $\vartheta_a$ in a finitely generated $o_1$-algebra $R \subset \Omega_1$ with fraction field $\Omega_1$); a realization of $S$ by a polarized abelian scheme over $\operatorname{Spec} R$; a largeness condition on the level; a map $u$ to $X^\circ_F$ with `UOver` (by its name, the abelian scheme is the pullback of the universal one) that hits a generic point; a normal model $M$ of $\Omega_1$ over $o_1$; and a finite map $\pi \colon M \to Z$ compatible with $u$ and $i$.

`UValThru` for an ideal $J_1$ on $M$ with exponent $\iota$ says: let $W$ be a ring with `CDvr` and uniformizer $\varpi$, and $\chi \colon \operatorname{Spec} W \to M$ whose generic point maps by $\pi$ into $i(X^\circ_F)$. Suppose the point carries a semi-abelian scheme over $W$ with a uniformization whose degeneration is monomial in $\varpi$ with form $\beta$. Then $\chi^* J_1 = (\varpi^{n})$ with $n = \iota\varphi(\beta)$.

**Theorem.** If $A \subset Z$ is clopen, irreducible and meets $i(X^\circ_F)$, then there are $X_1$, $\iota \geq 1$ and $J_1$ with $\pi(M) = A$, $\pi(\operatorname{supp} J_1) \cap i(X^\circ_F) = \emptyset$, and `UValThru` for $J_1$ through $\pi$.

## Proof

1. `exists_genericPoint_closure_eq_of_isClopen`: $A$ is the closure of $i(\eta)$ for a generic point $\eta$ of $X^\circ_F$.
2. `GSetup.exists_uSetup_proj` (with level bound $0$): a setup $X_1$ with $M$ projective over $o_1$ and $u$ landing at $\eta$.
3. `USetup.range_π_eq`: then $\pi(M) = A$.
4. `unitary_exists_normalModel_effCartier_along_traits`: a proper map $Y \to M$ from a normal model $Y$, and an effective Cartier divisor $D$ on $Y$ over the boundary whose valuations are $\iota\varphi$. It needs $M$ projective.
5. `exists_idealSheaf_descending_divisor_power`: an ideal $J_1$ on $M$ whose pullback to $Y$ has the same two properties, for some $\iota' \geq 1$.
6. `ideal_orders_of_proper_model`: $Y \to M$ is proper and hits the generic point, so it is surjective. Both properties descend from the pullback of $J_1$ to $J_1$.

## In the Lean code

The theorem is in [ExistsUnitaryThetaSetupIdealOverComponent.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryThetaSetupIdealOverComponent.lean#L17). `USetup` is in [ExistsRatPointOfFiniteType.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsRatPointOfFiniteType.lean#L437) and `UValThru` in [UValThruTopOfDisjoint.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UValThruTopOfDisjoint.lean#L21). Step 4 is the statement form of `exists_zhModel_effCartier_orders`, and step 5 of `DescentPow.exists_idealSheaf_comap_uValThru`; we have not opened their proofs. We have not unfolded `CDvr`, `UOver`, `PELUnif` or `IsMonomial`.
