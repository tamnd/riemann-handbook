---
id: nc-tie-c-of-closed
title: The normalizing constant in closed form
kind: theorem
decl: Formalism.L2.SG.Pf.NcAllC.ncTieC_of_closed
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.DualFamilyCounting.NcAllC
covers: 3278
status: drafted
drafted_by: writer@claude
---
This theorem computes one normalizing constant of a mass computation for a unitary group in closed form. It sits in the dominator tree under the [unitary hypotheses node](/step/nonempty-hyps/). Two callers use it: `NormalizingConstantPositiveAll.lean` and the Development file `MeanCountConstantEqUnscaledMainConstant.lean`, which supplies the hypothesis $h_{\mathrm{Cov}}$ by `CovolRef_outright`. The theorem only passes its hypotheses along. The content is in [`ncTie0All_of`](/entry/nc-tie0-all-of/) and [`RealBracket_holds`](/entry/real-bracket-holds/).

## Statement

Fix a datum $D$ and a setting $X$ over it (`HidaSetting D`). It has a totally real field $F$ with $d$ infinite places, a CM extension $E/F$, a nondegenerate Hermitian matrix $J$ of size $n$ and a lattice $L \subset E^n$. Fix two words $u, u'$ with positive integers $T_u, T_{u'}$, and let $r$, $k$, $R$ be the ranks `D.R.rS`, `D.R.k`, `D.R.r`. Let $B$ be the record of real numbers `bCF` built from these data: global and local volumes, masses and constants.

**Theorem.** Under the hypotheses below,
$$c_{\mathrm{expl}} = \frac{n_0(B)\, g(D)}{\alpha(B)\, \kappa(D)}.$$

The terms are these ([MassDataConc.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/MassDataConc.lean#L331), [StepsR.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/StepsR.lean#L57)):

- $n_0(B) = A(B)/\rho_0(B)$. Here $A$ is a covolume times a constant times a ratio of products of local volumes, divided by the volume $\mu_K$ of the level. $\rho_0$ is the mass $\sum_c 1/\lvert \Gamma \cap cKc^{-1} \rvert$ of the stabilizer of the frame of $u$.
- $\alpha(B) = \prod_v \alpha_v$ over the finite places of $F$, with $\alpha_v = a_v(T_u)$ or $a_v(T_u)\, a_v(T_{u'})$, and $a_v(T) = \prod_{i=i_0}^{n} (1 - \eta_v^i q_v^{-i})$. Here $\eta_v = 1$ if $E \otimes F_v$ splits and $-1$ if not, and $i_0$ is $k$ if $v \mid T$ and $k+1$ if not.
- $\kappa(D)$ and $g(D)$ are explicit powers of an integer $g_S$ and of a real `rdE` attached to $E$.
- $c_{\mathrm{expl}} = c_{\mathrm{mass}} \cdot \lvert d_F \rvert^{-2r(r+1)(k-1)} \cdot \prod_{i=k}^{R} L(i, \eta) \,/\, \sum_{\Lambda \in S} \lvert \mathrm{Aut}\, \Lambda \rvert^{-1}$, with $L(i,\eta) = \prod_{\mathfrak p} (1 - \eta(\mathfrak p)^i N\mathfrak p^{-i})^{-1}$. The constant $c_{\mathrm{mass}}$ is picked by choice from a predicate `MassConst`, which we have not unfolded.

The hypotheses, grouped:

1. Analytic inputs: `CovolRef` (two reference volumes at infinity multiply to $\lvert d_F \rvert^{e}$, with $e = -(8r^3 + 6r^2 + 6kr^2 + r)/3$), `SWXS`, and the `Fact` instances `GaugeVolUD`, `RhsWLim`, `HermRepUnram`.
2. The setting: `HypX`, `MeasCompatψ`, `StdHyp`, $L$ is a lattice, and two Gram determinants are nonzero.
3. Local conditions: `ProdConv`, `LocTieX` at $u$ and $u'$, `TypFacts`.
4. Positivity: `QuotVolPosC`, $s_d \ge 0$, $C \ge 0$, $\Theta > 0$.
5. Arithmetic: $T_u \equiv T_{u'} \pmod{g_S^2}$, and $S$ is a set of representatives of the row lattices modulo the stabilizer of the flag (`IsRowReps`).

## Proof

The proof is one term: `ncTie0All_of` applied to all hypotheses, with `RealBracket_holds hCov` in the place of its hypothesis `RealBracket`.

## In the Lean code

The theorem is in [NcAllC.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcAllC.lean#L37). It calls `Formalism.L2.SG.Pf.NcAllS.ncTie0All_of` and `Formalism.L2.SG.Closed.RealBracket_holds`.

The three `Fact` instances are hypotheses of the theorem, not facts proved in this file. Instances of all three are declared elsewhere, for example `factGaugeVol` in [FactsGV.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/WeightedGaugeFactors/FactsGV.lean#L6).

The word "closed" in the name does not refer to the predicate `Closed` of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). No hypothesis uses it. It seems to mean "closed form" of the constant.
