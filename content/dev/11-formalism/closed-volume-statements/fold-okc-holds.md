---
id: fold-okc-holds
title: The folding conditions for the Poincaré series, given the Levi decomposition
kind: theorem
decl: Formalism.L2.SG.Closed.FoldOKC_holds
module: Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedVolumeStatements.UnipotentInLevelSubgroup
covers: 445
status: drafted
drafted_by: writer@claude
---
This theorem proves `FoldOKC`, the conditions `FoldOK` that let one fold an integral over $G(F) \backslash G(\mathbb A)$ against the Poincaré data of a word $u$. It has one hypothesis, `FinLeviC`, and sits under the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). The proof passes five inputs to [`foldOKC_holds_of`](/entry/fold-okc-holds-of/).

## Statement

Fix a setting $X$, a record `Y : Full X` and a word $u$. Let $S(u)$ be the subgroup attached to the frame of $u$, $H(u)$ the stabilizer of the frame and $N(u)$ a unipotent group. `FinLeviC` says: each $y \in S(u)(\mathbb A_f)$ is $h n$ with $h \in H(u)(\mathbb A_f)$ and $n \in N(u)(\mathbb A_f)$.

`FoldOKC` says: if the level subgroup is normalized and `WuDecay` holds, then `FoldOK` $X$ $u$ holds. Here:

- `WuDecay` asks that each archimedean function $W_u$ is fixed by right convolution with some bounded $\alpha$ of compact support, and that $\int \lvert W_u \rvert\, \nu_u^{N_1}\, d\nu_Q < \infty$. Here $\nu_u(x)$ is the infimum of $\lVert t x \rVert$ over $t \in S_\infty(u)$; the norm and $N_1$ are as in [`MultPoly_holds`](/entry/mult-poly-holds/).
- `FoldOK` asks that `Srat X u` has a fundamental domain in $G(\mathbb A)$, and that there are a compact $\Omega_0 \ni 1$ and $a \ge 0$ such that, for each $T$, `Ph X u hK T` is a fold datum on every compact $\Omega \supseteq \Omega_0$, and has a finite multiplicity integral against $G(F)$ for every compact $\Omega$ and every fundamental domain.

**Theorem.** `FinLeviC` implies `FoldOKC`.

## Proof

The five inputs of `foldOKC_holds_of` are:

1. `KsetSplit_holds`: if $n h \in K$ with $n \in N(u)(\mathbb A_f)$ and $h \in H(u)(\mathbb A_f)$, then $h \in K$.
2. `unipotent_in_level_subgroup`: for $n \in N(u)(\mathbb A_f) \cap K$, $m = x_u^{-1} n x_u \in K_2$ and $\chi_2(m) = \psi_{f,u}(n)$.
3. `RatLevi_holds`: each $\gamma \in G(F)$ with components in $S(u)$ is $\nu \eta$ with $\nu \in N(u)(F)$ and $\eta \in \Gamma_u$.
4. `psiProd_all`: $\psi_{\infty,u}(\nu_\infty)\, \psi_{f,u}(\nu_f) = 1$ for $\nu \in N(u)(F)$.
5. `IUnfold`, from `iUnfoldAll_of` applied to `FinLeviC`, `noCocompactC_holds` and `nilradical_strong_approximation` ($N(u)(F)$ is dense in $N(u)(\mathbb A_f)$).

## In the Lean code

The theorem is in [UnipotentInLevelSubgroup.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/UnipotentInLevelSubgroup.lean#L87). `FoldOKC` is in [PoincareConstantEq.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/PoincareConstantEq.lean#L75), `FoldOK` and `WuDecay` in [WuDecay.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/WuDecay.lean#L34).

The hypothesis `FinLeviC` is proved as `FinLeviPf.finLeviC_holds` in [FinLevi.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/FinLevi.lean#L615), and `FoldOKC_outright` in [FullExistsTiedHolds.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/FullExistsTiedHolds.lean#L25) applies this theorem to it. The callers in `MainEqWire.lean` and `FinXHolds.lean` still take `FinLeviC` as a hypothesis. Two other callers, in `MainEqWire.lean` and `FinXHolds.lean`, still take `FinLeviC` as a hypothesis.

We have not unfolded `SfinU`, `Hfin`, `NfinU`, `Srat`, `Ph` or `IsFoldDatum`; the descriptions of $H(u)$ and $N(u)$ follow the names.
