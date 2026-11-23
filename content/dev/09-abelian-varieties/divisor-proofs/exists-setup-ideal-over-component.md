---
id: exists-setup-ideal-over-component
title: A boundary ideal on a theta model over one Siegel component
kind: theorem
decl: GlobalTheory.Poinc.exists_setup_ideal_over_component
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsThetaSetupIdealOverClopenComponent
covers: 420
status: drafted
drafted_by: writer@claude
---
Let $Z$ be a theta compactification of the Siegel moduli scheme $X$, and $W$ a clopen irreducible piece of $Z$. This theorem finds a normal model $M$ built from theta constants, with a finite map $\pi \colon M \to Z$ onto $W$, and an ideal on $M$ that lives on the boundary and has the valuations of $\iota\varphi$. It proves [the statement form](/entry/exists-theta-setup-ideal-over-clopen-component/), which [`idealSt_holds`](/entry/ideal-st-holds/) uses for each piece. The unitary analogue is [`exists_uSetup_ideal_over_component`](/entry/exists-u-setup-ideal-over-component/).

## Statement

Fix $g \geq 1$, odd $n \geq 3$, a theta compactification $i \colon X \to Z$ over $\Lambda_n = \mathbb{Z}[\zeta_n, 1/n]$, and a polarization function $\varphi$ for $g$. Traits are as in [`poinSt`](/entry/poin-st/).

A *theta setup* $X_1$ for an $8 \times 8$ matrix $W_8$ (`Setup F W8 i`) is:

- a base ring $o_1$ and a field $\Omega_1$ (`ArithBase`), and a map $\kappa \colon \Lambda_n \to o_1$;
- a theta system $S$ over $(o_1, \Omega_1)$: theta constants $\vartheta_a$ in a finitely generated $o_1$-algebra $R \subset \Omega_1$ with fraction field $\Omega_1$, realized by a polarized abelian scheme $P$ over $\operatorname{Spec} R$, with a largeness condition `S.Big`;
- a map $u \colon \operatorname{Spec} R \to X$ that hits only generic points of $X$, with `SharpOver`: $P$ is the 8-fold product of the pullback by $u$ of the universal abelian scheme, with the polarization given by $W_8$;
- a normal model $M$ of $\Omega_1$ over $o_1$, and a finite map $\pi \colon M \to Z$ that agrees with $i \circ u$ on the generic point;
- copies of the hypotheses on $g$, $n$ and $(Z, i)$, and compatibility of $\kappa$ with the structure maps.

**Theorem.** Let $W \subset Z$ be clopen and irreducible. Then there are $W_8$, a theta setup $X_1$ for $W_8$, $\iota \geq 1$ and an ideal $J_1$ on $M$ with $\pi(M) = W$, $\pi(\operatorname{supp} J_1) \cap i(X) = \emptyset$, and $\xi_1^* J_1 = (\varpi^{\iota\varphi(\beta)})$ for each trait and each $\xi_1 \colon \operatorname{Spec} V \to M$ with $\pi \circ \xi_1$ extending $i \circ y$.

## Proof

1. `exists_mem_genericPoints_closure_eq_of_isClopen`: $W$ is the closure of $i(\eta)$ for a generic point $\eta$ of $X$.
2. `GSetup.exists_setup` (with level bound $0$): a theta setup $X_1$, for the matrix $W_8$ of `IsThetaCompact`, with $u$ landing at $\eta$.
3. `Setup.range_π_eq`: then $\pi(M) = W$.
4. `exists_normal_model_cartierDivisor_thetaSetup`: $\iota \geq 1$, a normal model $Y$ of $\Omega_1$ with a proper map $\pi_Y \colon Y \to M$ of models, and an effective Cartier divisor $D$ on $Y$ over the boundary with valuations $\iota\varphi(\beta)$.
5. `exists_idealSheaf_descending_divisor_power_thetaSetup`: an ideal $J_1$ on $M$ whose pullback to $Y$ has the same two properties, for some $\iota' \geq 1$. It needs $M$ projective over $o_1$ (`Setup.projM`).
6. *Homogeneity.* For each trait, $\varphi(k\beta) = k\varphi(\beta)$ for $k \geq 1$. By `Trait.dim_add_rank`, $\beta$ is a form on a lattice of rank at most $g$. It is positive semidefinite by `IsMonomial`, and `IsPolFan` gives homogeneity on such forms.
7. `ideal_orders_of_proper_model`: $\pi_Y$ is proper, and with step 6 both properties descend from the pullback of $J_1$ to $J_1$ itself.

## In the Lean code

The theorem is in [ExistsThetaSetupIdealOverClopenComponent.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsThetaSetupIdealOverClopenComponent.lean#L18). `Setup` is in [ThetaSetupStructureMapComp.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ThetaSetupStructureMapComp.lean#L16), and `projM` at line 122 of that file. Step 2 is in [E8ThetaSetupGenericPointExists.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/E8ThetaSetupGenericPointExists.lean#L87). Steps 4 and 5 are statement forms of `Poinc.exists_model_divisor_of_orders` and `Poinc.DescentPow.exists_idealSheaf_comap_orders`; we have not opened their proofs. The level bound that step 2 also returns is dropped. We have not unfolded `ArithBase`, `S.Big`, `IsMonomial`, `Unif` or `IsPolFan` past its homogeneity field.
