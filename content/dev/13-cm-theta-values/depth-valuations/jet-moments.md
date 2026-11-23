---
id: jet-moments
title: The integral jet moments
kind: theorem
decl: GlobalTheory.MomTop.jetMoments
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.KernelJetsLevelPlaceIntegralMoments
covers: 1599
status: drafted
drafted_by: writer@claude
---
This theorem proves `JetMoments`: the jet sums of the theta kernels, mapped into $\mathbb{C}_p$, are limits of integral combinations of explicit point tables. Through its [second name](/entry/kernel-jets-level-place-integral-moments/) it goes to [the five kernel laws on the true chains](/entry/laws-true-fam/), where it gives the two lattice bounds `KerBar` and `KerP`. The proof only closes the hypotheses of a reduction lemma. The analytic content is in [the moments of the unit period translates](/entry/moments-fin/).

## Statement

Let $p$ be a prime, $\mathcal{H}$ a set and $M$ a set of indices. For a table $t \colon \mathcal{H} \times M \to \mathbb{C}_p$, a support $S \subseteq \mathcal{H}$ and $J \colon M \to \mathbb{C}_p$, say that $J$ is in the *integral closure* of $t$ over $S$ if for each finite $F \subseteq M$ and $\varepsilon > 0$ there is a finitely supported $c \colon S \to \mathbb{C}_p$ with $|c(x)| \le 1$ and $|J(m) - \sum_x c(x)\, t(x, m)| < \varepsilon$ for $m \in F$. An embedding $\iota \colon K \to \mathbb{C}_p$ *induces* a prime $w$ of $K$ if $y \in w \iff |\iota(y)| < 1$ for integers $y$.

The point table of $\iota$ and weights $u_\tau$ is $\mathrm{pt}(x, m) = \prod_{k} \bigl(u_{\tau_k}\, \iota(\tau_k(x^*_k))\bigr)^{m_k}$, where $x^*$ is the adjoint matrix and $m$ is a multi-index. The jet sum $J(m)$ is a lattice sum of $\Xi(x)$ times the $m$-th jet of the theta kernel at $x$.

**Theorem** (`JetMoments`). Let $D$ be a datum with `D.Ok`, and let $(s, c, \delta, B, \chi, c_D)$ be analytic data with `AnaOk`: the seam is good, $c$ is a curve ideal, $\delta^{12}$ is the discriminant of the lattice of $c$, $\chi$ is admissible and $c_D$ is nondegenerate. Let $u$ be a word with $T(u)$ prime and prime to $N(c)$. Let $w$ be a prime of $K$ and $\iota \colon K \to \mathbb{C}_{T(u)}$ an embedding that induces $w$. Then there are $u_\tau$ with $|u_\tau| = 1$ such that, for all selection data, decorations $d, d'$ at steps $i, i+1$ that are standard at $T$, and an off datum $\Xi_0$:

- if $\tau(\bar\pi_T(u)) \in w$ for each $\tau$ (`seenBarC`), the jet sums are in the integral closure of $\mathrm{pt}$ over the support `suppBar`;
- if $\tau(\pi_T(u)) \in w$ for each $\tau$ (`seenC`), the jet sums are in the integral closure of $T(u)^{-f N_i}\,\mathrm{pt}$ over the support `suppP`.

In both cases $m$ runs over the rational indices `RatIdx`.

## Proof

The proof is one line:

```
jetMoments_of_unitPeriod (unitPeriodTranslates_moments_finite eq_and_alg.1 eq_and_alg.2) eq_and_alg.1 latticeFactsAll
```

1. `jetMoments_of_unitPeriod` reduces `JetMoments` to three facts: the moment bound of [`unitPeriodTranslates_moments_finite`](/entry/unit-period-translates-moments-finite/), the equivariance laws `MovesAll`, and `LatticeFactsAll`. It takes $u_\tau = \lambda(c_D(\tau))/\Omega$, which has norm 1 by `EigenGenerator.norm_generator_eq_one`. It checks $T(u) \ne 2$ and that $-d$ is a square mod $T(u)$ (`SplitK.splitk`), so the moment bound applies. Then it treats the two cases with `PtMoments.ptMom`, `MomentCompanion.companion`, `ChiMove.chi_move` and `Move.move`.
2. `eq_and_alg` gives both hypotheses of the moment bound: the equivariance laws `EqP` and the algebraicity of the Taylor coefficients of the translates.
3. `latticeFactsAll` gives the lattice facts.

## In the Lean code

The theorem is in [KernelJetsLevelPlaceIntegralMoments.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/KernelJetsLevelPlaceIntegralMoments.lean#L13). `JetMoments` is in [JetSumTable.lean](lean:Development/AbelianVarietyTheory/BlockTheory/GlobalSignature/JetSumTable.lean#L123). The reduction is in [JetMomentsOfUnitPeriod.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/JetMomentsOfUnitPeriod.lean#L19), and `eq_and_alg` is in [EqAndAlg.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/EqAndAlg.lean#L10). We did not unfold the theta kernel `jetK`, `RatIdx` past its statement, or the lemmas of the case analysis.

The equivariance law `EqP` is proved twice. Here it comes from `eulerProduct_eq_of_curve_ideal` in [FinalEq.lean](lean:Formalism/LocalToGlobal/PairingIndexBounds/SplitPairEquations/FinalEq.lean#L6). In [the five kernel laws](/entry/laws-true-fam/) it comes from `normalisedFamily_satisfies_equivarianceLaws`. The name "Euler product" does not match `EqP`, which is three transformation laws of the theta family under unitary matrices and changes of lattice.
