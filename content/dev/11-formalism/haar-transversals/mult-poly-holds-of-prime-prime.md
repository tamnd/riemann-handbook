---
id: mult-poly-holds-of-prime-prime
title: The polynomial multiplicity bound from a covering of compact sets
kind: theorem
decl: Formalism.L2.SG.Pf.multPoly_holds_of''
module: Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.UnitaryHaarProducts.IUnfold
covers: 370
status: drafted
drafted_by: writer@claude
---
This theorem proves `MultPoly`: the multiplicity of a compact set at a point $c\,(g, 1)$ grows at most polynomially in $g$. It assumes one covering fact, `OmCover`. Its only user is [a polynomial bound on the folding multiplicity](/entry/mult-poly-holds/), which proves `OmCover`. The bound is used by [the folding statement from five local steps](/entry/fold-okc-holds-of/).

## Statement

Fix a Hida setting $X$ with group $G$ over a field $F$ with $f = [F : \mathbb{Q}]$, and $n \ge 1$. For $g$ at the infinite places, let $\|g\| = \prod_v \|g_v\|_{op}$ (`normI`), and let $N_1 = 4n^2 \sqrt{2 \max_v q_v}$. For a compact $\Omega$ and a point $x$, $\mathrm{mult}(\Omega, x)$ is the supremum over $y$ of the number of rational $\gamma$ with $x^{-1} \gamma y \in \Omega$ (`FoldBound.mult`).

`OmCover` says: each compact $\Omega$ lies in a finite union of right translates $\mathrm{Om}(r, K')\, a^{-1}$, $a \in A$, with $K' \subseteq$ `Kset`. Here $\mathrm{Om}(r, K')$ is the set of $\omega$ with Cartan distance at most $r_v$ at each infinite place $v$ and finite part in $K'$.

**Theorem.** If `OmCover` holds, then for compact $\Omega$ and $C_C$ there is $C$ with $\mathrm{mult}(\Omega, c\,(g, 1)) \le C \|g\|^{N_1}$ for all $c \in C_C$ and all $g$.

## Proof

The theorem fills two inputs of `multPoly_of`: `TauTrans` (`tauTrans_holds`) and `NormPow` (`normPow_holds`). The other inputs are `LatCount_holds`, `DistTri_holds` and `reduction_theory`. Put $k = 4n^2 f$ and $x = c\,(g, 1)$.

1. `OmCover` covers $\Omega$ by the sets $\mathrm{Om}(r, K')\, a^{-1}$. By monotony, a bound for unions and right translation, $\mathrm{mult}(\Omega, x) \le |A| \cdot \mathrm{COm}(r) / \tau_1(x)^k$. The last bound is `multBound_of_latCount`.
2. `reduction_theory` says $\tau_1$ is continuous and positive. So $\tau_1$ has a minimum $m > 0$ on $C_C$.
3. `TauTrans` says $\tau_1(c) \le \tau_1(x)\, \|g\|^{1/f}$. So $1/\tau_1(x)^k \le \|g\|^{4n^2} / m^k$.
4. `NormPow` says $\|g\|^{4n^2} \le \|g\|^{N_1}$. If some $q_v \ge 1$, this holds because $\|g\| \ge 1$. If not, every $\|g_v\|_{op}$ is 1.

So $C = |A| \cdot \mathrm{COm}(r) / m^k$.

## In the Lean code

The theorem is at [IUnfold.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/IUnfold.lean#L795). It calls `multPoly_holds_of'` (line 676), then `multPoly_holds_of` (line 575), then `multPoly_of` (line 123). `TauTrans`, `NormPow` and `OmCover` are at lines 93, 97 and 102. `MultPoly` is in [InHHCut.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHCut.lean#L317). We have not unfolded `LatCount`, `DistTri` or $\tau_1$ beyond its definition as $\min(1/2, \cdot)$ of a size function.
