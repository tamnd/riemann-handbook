---
id: nu-good
title: The local depth at a good place is bounded by the content
kind: theorem
decl: GlobalTheory.GoodDepth.nuGood
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.GoodPlaceDepthBoundProof
covers: 808
status: drafted
drafted_by: writer@claude
---
This theorem bounds the depth $\nu_W(\lambda)$ of a moduli space at a place $\lambda$ of good residue characteristic $\ell$. It selects, by the class of $\ell$, one of four package bounds or the vanishing for zero packages. Its alias [`goodPlaceDepthBound_proof`](/entry/good-place-depth-bound-proof/) gives it to [`leafGood`](/entry/leaf-good/).

## Statement

Let $X$ be a moduli space over a CM field $E$, with level $M$ and coefficient field $F$. For a place $\lambda$ of $F$ over a prime $\ell$, let $e_\lambda$ be its ramification index. For a weight $a$ and an integer $n_W$, the depth is

$$\nu_W(\lambda) = \max\Bigl(0, \sup_{V, y} \inf_{C} \nu_C\Bigr),$$

where $V$ runs over complete discrete valuation rings over $\lambda$, $y$ over algebraic integral points of $X$ over $V$, $C$ over integral charts at $y$, and $\nu_C$ (`nuLocC`) is an infimum of valuations of differential operators (from a set `FFV`) applied to integral power series. Let $\theta(k,\ell) = \sup \ell^{-i}$ over odd $i \ge 3$ with $\ell^i > k^{3/2}$ (`thl`).

**Theorem** (`NuGoodSt`). For each $C_1 \ge 0$ there is $C_c > 0$ with the following property. Assume the star on $\mathcal{O}_E$ is complex conjugation, every algebraic integral point of $X$ has an integral chart, and `PkgSt` holds for $X$. Let $N$ be a numerical datum with ranks $k, m, f$, sizes $S_c, \eta$, weights $w_j$ and content $F_j$; let $1 \le j \le m$, and let $a, n_W, T, b, L, w$ satisfy `PlaceTie`, `DomW`, the signature condition, `GoodPage` for $C_1$, $\sum_z w_j(z) \le w$ and $b \le w$. Let $\ell \notin s_m \cup \{q, d, g_0, g_1\}$ and $\ell \nmid M$. Then $\nu_W(\lambda) < \infty$,

$$\frac{T\nu_W(\lambda)}{e_\lambda} \le F_j(\ell) + C_c\Bigl(\frac{m w\log k}{\ell} + \frac{fk(S_c+\eta)}{\ell} + k\theta(k,\ell)w + [\ell > X'']\frac{kw}{\ell^2}\Bigr),$$

and $\nu_W(\lambda) = 0$ if $D_F < \ell$.

## Proof

By `nuW_bound_of_charts` it is enough to show $\nu \le B/T$ for each local chart and each $\nu$ with $e_\lambda \nu \le \nu_C$, where $B$ is the right side. `PkgSt` gives a package with this $T$ and $\nu$, of a kind fixed by the class of $\ell$ in $N$.

1. **Zero packages.** If $\ell \ge m b/(T f (k-1)^3 L)$ with $b \ge 0$, then `RowBudgets.main` and `GoodPage` give $s$ with $a(\tau,0) \le s(\ell-1)$ for each $\tau$ of positive multiplicity. If $b < 0$, `GoodPage` gives $T a(\tau,0) \le 3b < 0$, so no such $\tau$ exists and $s = 0$ works. A zero package (`PkgZero`, or `PkgZeroCs` when $\ell$ is in the conjugate class) exists, and `largePrime_packages_depth_nonpos` or `pkgZeroCs_nu_nonpos_of_monSupply` gives $\nu \le 0$.
2. **Small $\ell$.** `ContentValue.main` shows that $\ell$ is inert or split, and bounds the main term of each inert case by $F_j(\ell)$ plus $2[\ell > X'']kw/\ell^2$. Then:
   - $\ell$ in class `PhiC`: `complexConjFrobeniusDepthContentBound_proof`;
   - $\ell$ in class `ConjIn` only: `rowBound_le_Fnum_sum_add_error`;
   - other inert $\ell$: `inertPrimeDepthContentBound_proof`;
   - split $\ell$: `splitPrimeDepthContentBound_proof`.

   Each bounds $T\nu$ by a main term plus a constant times `errB`. `RowBudgets.main` gives $Tf(k-1)^3\log^2 k \le m w \log k/\ell$, so `errB` is at most twice the error above. The proof takes $C_c = 2C_I + 2C_P + 2C_C + C_S + 2$.
3. **Vanishing.** If $D_F < \ell$ then $a(\tau,0) \le D_F \le \ell - 1$, the zero case with $s = 1$ gives $\nu \le 0$, and `nuW_bound_of_charts` with $B = 0$ gives $\nu_W(\lambda) = 0$.

## In the Lean code

The theorem is in [GoodPlaceDepthBoundProof.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/GoodPlaceDepthBoundProof.lean#L56). $\nu_W$ is `nuW` in [PlaceBelow.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/PlaceBelow.lean#L67). We have not unfolded the package structures or `FFV`. The proof does not use `PkgZeroCSt`, one of the seven statements in `PkgSt`.
