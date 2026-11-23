---
id: th-p-vec-eq-translate
title: A theta level vector is a translate of a sum of Heisenberg translates of a base vector
kind: theorem
decl: GlobalTheory.LiftLevel.thP_vec_eq_translate
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ThetaLiftFiniteVectorEqTranslateLevelDatum
covers: 308
status: drafted
drafted_by: writer@claude
---
This theorem rewrites a theta level vector $f$ in the form that the theta-series lemma of [`span_std`](/entry/span-std/) needs: a finite adelic translate of the vector `uVec` of a level datum. It is used under the second name [`thetaLiftFiniteVector_eq_translate_levelDatum`](/entry/theta-lift-finite-vector-eq-translate-level-datum/).

## Statement

The hypotheses are those listed in the second-name entry. The vector $f$ satisfies `IsThPVecOf`: there is a vacuum $f_0$ and an idempotent sum $e$ for the places of $P_g \cup Q$, and $f = T_m(\Phi)$ for each theta map $T_m$, where $\Phi$ = `thPDatum` is built from the characters $\xi$ on the places of $P_g$ and $Q$. We did not unfold `IsThetaAt`, `omegaK` or `omegaQ`.

**Theorem.** There are a level datum $L_v$ (`SW.Level C.X`, with an ideal $\mathfrak m$, an element $w$, a group $J$ and coefficients `dat`), a vector $f'$, $k_0 \in G_S(\mathbb A_f)$ and $M \in \mathbb N$ such that:

1. $w \bar w = 2b$ for an integral $b$ (`IdemTwo`), and $0 < M \in \mathfrak m$;
2. $f'$ is a base vector: theta, nonzero, Fock for $B$, and a lattice vacuum for the lattice of $L_v$ (`IsBase`);
3. $f = \omega(k_0,1)\,u$, where $u = \sum_c \mathrm{dat}(-c)\, \rho(c) f'$ is the sum over the classes $c$ of `LvCls` (`uVec`), and $u$ is theta, Fock and nonzero;
4. each $k$ in the level group `LevK` of $L_v$ stabilizes $\beta_T$ and reduces to $1$ at the places of $P_g$.

## Proof

1. `T.theta_kernel_finite_vector_ne_zero` gives $f \ne 0$.
2. `T.thetaLift_level_datum_sum_of_translates` (a second name of `LiftLevel.lift_level_datum`) gives $L_v$, $k_0$ and a lattice $L$ with $\Phi(x) = \sum_c \mathrm{dat}(-c)\, \mathbf 1_L(x + t_c)$, where $t_c$ is the $e$-part of $k_0 \cdot c$.
3. `T.placeModel_indicator_theta_fock_latticeVacuum` says that $f'' = T_m(\mathbf 1_L)$ is theta, Fock and a lattice vacuum. So $f = \sum_c \mathrm{dat}(-c)\, \mathrm{heis}(t_c) f''$.
4. Put $f' = \omega(k_0^{-1},1) f''$. By `om_heis`, $\omega(k_0,1)\rho(c) f' = \mathrm{heis}(k_0 c) f''$. The difference $k_0 c - t_c = 2v$ lies in the lattice, and $\mathrm{heis}(2v)$ fixes the lattice vacuum $f''$ with trivial phase. This gives $f = \omega(k_0,1)u$.
5. `WeakMove.om_move` carries the Fock property to $f'$ and to $u$, and `TensLatMove.hatA_move` carries the lattice-vacuum property. $u \ne 0$ since $f \ne 0$.
6. $M$ is the absolute norm of $\mathfrak m$, which is positive since $\mathfrak m \ne 0$. Clause 4 is `T.hermitianThetaLevelGroup_stabilizes_selfDualLatticeFrame`.

## In the Lean code

The theorem is at [ThetaLiftFiniteVectorEqTranslateLevelDatum.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ThetaLiftFiniteVectorEqTranslateLevelDatum.lean#L26). The decomposition of $\Phi$ is in step 2; this theorem moves it through $T_m$ and $\omega(k_0,1)$. The number $M$ is `Ideal.absNorm Lv.𝔪`, so clause 1 on $M$ holds for any nonzero ideal and carries no information. We did not unfold `SW.Level`.
