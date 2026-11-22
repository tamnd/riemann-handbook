---
id: counting-theorem-of-volume-step
title: Counting automorphic forms of unitary groups, given the volume step
kind: theorem
decl: GlobalTheory.CountFinal.countingTheorem_of_volumeStep
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.UnitaryAutomorphicCountingOfCompactDualVolumeRat
covers: 1620
status: drafted
drafted_by: writer@claude
---
This theorem counts automorphic forms on a unitary group with fixed discrete series at the real places, given a volume recursion. Through [a renaming](/entry/unitary-automorphic-counting-of-compact-dual-volume-ratio/), [`count_typed_of_volumeStep`](/entry/count-typed-of-volume-step/) and [`count_constants_of_siegelWeil`](/entry/count-constants-of-siegel-weil/) it gives the counting row of [the unitary hypotheses node](/proof/unitary-hypotheses/).

## Statement

Let $E/F$ be a CM extension with $f = [F:\mathbb{Q}]$. Let $J$ be a nondegenerate [[hermitian form|48P4A1CX85]] of size $n$ over $E$ with a self-dual lattice, and let $G = U(J)$ be its [[unitary group|0R9R0Y1HDK]]. Let $\mu_f$ be a [[Haar measure|VY0HXD3GC4]] on $G_f$, and let $\Omega$ be a [[fundamental domain|KNJA2NEZ9F]] for $G(F)$ in $G_\infty \times G_f$. Let $r_d = |d_E|^{1/2f}$.

**Volume step.** For each such $J$ of signature $(P,Q)$ at all real places, with $n \ge 3$, and each sign $s$, there are a form $J'$ of size $n-1$ and signature $(P-1,Q)$ or $(P,Q-1)$, a vector $x$ with $x^* J x = \pm 1$, and a matrix $A$ with $x^* J A = 0$ and $A^* J A = J'$. Also
$$\frac{\mathrm{vol}(J)}{v_n^{f}} = \frac{\mathrm{vol}(J')}{v_{n-1}^{f}} \cdot M(E,n).$$
Here $\mathrm{vol}$ is the covolume of $G(F)$ over $\mu_f$ of the lattice stabilizer, times gauge constants, and $v_n$ has the form of a volume of the compact $U(n)$. $M(E,n)$ is $\bigl((n-1)!\,(r_d/2\pi)^n\bigr)^f r_d^{-f/2}$ times an Euler product over the primes of $E$.

**Theorem.** Assume the volume step. For each $C_g$ there is $n_0$ as follows. Let $\sigma_v$ be a discrete series of $U(p,q)$ at each real place $v$, with Harish-Chandra parameter $\lambda_v$, formal degree $d_v$ and a unit vector $w_v$ in its lowest $K$-type. Let $e$ be an admissible idempotent on $G_f$ of level $g$ with an auxiliary prime $g_0$. Suppose `CountHyp`: $n \ge n_0$, $q^2 \le n$, $\log f \le \sqrt n$, $|\lambda_v| \le b^2$ with $b \ge 2$, $1 \le g \le b^{C_g}$, $g_0 > 4n$ splits completely in $E$, two growth bounds on $r_d$ and $b$, and the gap between parameters of opposite sign is at least $8\cdot 10^{14}(C_g+4)\,n^{19} f^5 \log(b\,r_d)$. Let $D$ be the dimension of the space of maps $R(e) \circ T$, for $G_\infty$-maps $T \colon \bigotimes_v \sigma_v \to L^2(\Omega)$. Then $D$ is finite and
$$\Bigl|D - \prod_v d_v \cdot \mathrm{vol}(\Omega) \cdot e(1)\Bigr| \le e^{-\frac{1}{16} n f \log n} \prod_v d_v \cdot \mathrm{vol}(\Omega) \cdot e(1).$$

The main term has the shape of the DeGeorge-Wallach limit multiplicity formula (Ann. of Math. 107, 1978). We did not check normalizations.

## Proof

The proof is a trace formula argument on the kernel $K(x,y) = \sum_{\gamma \in G(F)} \varphi(x^{-1}\gamma y)$. Here $\varphi = \prod_v d_v \overline{\langle w_v, \sigma_v(g_v) w_v\rangle} \cdot e$.

1. The proved coefficient bound `FormulaGap` gives `DecGap` and a pointwise bound `PtBound` on $\varphi$.
2. The volume step gives `AbsoluteVolume` (a bound on the volume), `FlagMeasureBound` and `NonzeroFlagBound`.
3. `DecGap` and the volume bound give finite dimension.
4. Relative to the main term, the near terms on the moderate region are at most $e^{-nf\log n/4}$ and the far terms at most $e^{-n^2 f}$. The rare flag set has relative measure at most $e^{-nf\log n/4}$. The deep set gives at most $D e^{-n^2 f}$. We did not unfold the height `least` that defines these regions.
5. `countingTheorem_of_finite_of_bounds` adds the bounds.

## In the Lean code

The theorem is in [UnitaryAutomorphicCountingOfCompactDualVolumeRat.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/UnitaryAutomorphicCountingOfCompactDualVolumeRat.lean#L37). The statements are in [LatticeCountingTheorem.lean](lean:Development/AbelianVarietyTheory/BlockTheory/SiegelWeilLocal/LatticeCountingTheorem.lean#L10) and [SameKindIsometric.lean](lean:Development/AbelianVarietyTheory/Statements/CuspFrameWeights/SameKindIsometric.lean#L32). Most called lemmas are `first | exact` renamings. `lowestKType_compressionFormula_of_strictLowestKType` has no hypothesis, despite its name. $D$ is a `finrank`, which is $0$ in infinite dimension, so finite dimension is a separate conclusion. We did not unfold `IsDS`, `IsLowUnit` and `IsFdeg`.
