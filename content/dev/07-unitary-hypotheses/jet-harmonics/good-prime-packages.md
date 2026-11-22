---
id: good-prime-packages
title: The seven package statements at all integral points
kind: theorem
decl: GlobalTheory.goodPrime_packages
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.AllGoodPrimeDepthDataExistProof
covers: 3594
status: drafted
drafted_by: writer@claude
---
This theorem proves `PkgSt`: at each algebraic integral point of a moduli scheme $X$, over a complete discrete valuation ring above a good prime, there is a package (a record of local data) with a prescribed valuation $\nu$. Its one hypothesis is the chart statement `UpFSt p` for all primes $p$. The proof joins five lemmas. Through its alias [`allGoodPrimeDepthDataExist_proof`](/entry/all-good-prime-depth-data-exist-proof/), the result goes to [`leafDepthGood_of_chartForm`](/entry/leaf-depth-good-of-chart-form/).

## Statement

**The objects.** $E$ is a CM field with a host datum `H`: a prime $d \equiv 7 \pmod{16}$ with $\sqrt{-d} \in \mathcal{O}_E$, and $E$ unramified over its maximal real subfield. `Dw` is a projective $\mathcal{O}_E$-module with a unimodular alternating form, compatible with conjugation, of signature $(p,q)$. `lv` is a level: an odd $M \ge 3$ and an ideal $\mathfrak{M}$ with $\mathfrak{M}\bar{\mathfrak{M}} = (M)$. $X$ (`Moduli`) is a smooth quasi-projective scheme over a field $K_A$ that represents the functor `Obj Dw lv` (not unfolded here) on reduced schemes. $F$ (`Coeff`) is a number field in $\mathbb{C}$ that contains all embeddings of $E$, a root of unity of order $\operatorname{lcm}(M, A)$, and $K_A$.

**The chart statement.** `UpFSt p` says the following. Let $p \ne 2$. Let $G$ be a commutative group scheme with degeneration data over a complete Noetherian local domain $R$ of characteristic $0$, and $F_G$ a formal group law of dimension $d$ with a chart onto $G$ (`IsChartJ`). Let an order $\mathcal{O}$ with $p \nmid \operatorname{disc} \mathcal{O}$ act on $G$ and on $F_G$, compatibly. Let $O$ be a $p$-adically complete valuation ring in an algebraically closed field of characteristic $0$, with a local map $R \to O$. Let $w$ be a place of $\mathcal{O}$ over $p$ of degree $n$ with embeddings $\tau_0, \dots, \tau_{n-1}$ into $O$ such that $\tau_{j+1}(a) \equiv \tau_j(a)^p$ modulo the maximal ideal and an étale basis condition. Let $r(\tau)$ be the rank of the $\tau$-eigenspace of the action on the tangent space. Then for each $j$ there are finitely many characters of $F_G$ (series $u$ with $u(0) = 1$ and $u(F_G(X,Y)) = u(X)u(Y)$) such that the cokernel of the map that pairs their linear terms with an eigenbasis of the $\tau_j$-eigenspace has size $x_j$ with

$$|p|^{\sum_{n' \ge 0} p^{-(n'+1)}\, r(\bar\tau_{j+n'+1})} \le x_j.$$

The indices are taken mod $n$, and $\bar\tau$ is $\tau$ composed with the involution of $\mathcal{O}$. Size means $\prod_i |c_i|$ for a module $\bigoplus_i O/(c_i)$ (`HasLen`).

**Theorem.** If `UpFSt p` holds for all primes $p$, then for all $E$, `H`, `Dw`, `lv`, $X$, $F$ and each involution on $\mathcal{O}_E$, `PkgSt X F` holds.

`PkgSt X F` is the conjunction of seven statements `PkgInertSt`, `PkgPhiCSt`, `PkgSplitSt`, `PkgZeroSt`, `PkgZeroCSt`, `PkgCsSt` and `PkgZeroCsSt`. Each has the form `AllPts X F Φ`: for each numerical datum $N$, index $j \in [1, m]$, embedding datum tied to $N$ (`PlaceTie`), dominant weight $a$ with signature $(p, q)$ given by $N$, prime $\lambda$ of $F$ whose residue characteristic $\ell$ is not small, not $q$, not $d$ and prime to $M$, complete discrete valuation ring over $\lambda$ with ramification $e$, algebraic integral point $y$ of $X$, chart at $y$, integer $n_W$ and real $\nu$ with $e_\lambda \nu \le \nu_{\mathrm{loc}}$ at the chart, $\Phi$ holds. Each $\Phi$ asks, for one class of $\ell$ (inert, split, and so on) and $n_W$ large, for a package `Pk` with `Pk.ν = ν`, and often `Pk.T = T`.

## Proof

The proof applies five lemmas to `UpFSt`:

1. `PkgInertSt` from `GlobalTheory.T.inertPrimeDepthDataExistsAtPoints_proof`;
2. `PkgPhiCSt` and `PkgZeroCSt` from `GlobalTheory.T.packages_exist_frobeniusComplexConjugation`;
3. `PkgSplitSt` from `GlobalTheory.T.splitPrimeDepthDataExistsAtPoints_proof`;
4. `PkgZeroSt` from `GlobalTheory.T.largePrimeDepthDataExistsAtPoints_proof`;
5. `PkgCsSt` and `PkgZeroCsSt` from [`exists_pkgCs_of_degree_bound_at_inert_primes`](/entry/exists-pkg-cs-of-degree-bound-at-inert-primes/) (2,002 declarations).

The rest is bookkeeping.

## In the Lean code

The theorem is in [AllGoodPrimeDepthDataExistProof.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/AllGoodPrimeDepthDataExistProof.lean#L16). `PkgSt` and its parts are in [DepthNumbersThresholdEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/DepthNumbersThresholdEq.lean#L143), `UpFSt` in [StChartF.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/PlaceDivisors/StChartF.lean#L169), and `Host`, `Datum` and `Level` in [TwoWeightEqOneAddRoot.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/TwoWeightEqOneAddRoot.lean#L14).

The first four lemmas are aliases too, each a one-line `first | exact ...`: of `InertPackage.pkgInert`, `PkgConj.packages_conj`, `SplitPackage.pkgSplit` and `LargePkg.pkgZero`. We have not opened those. The lemma for `PkgZeroSt` has "large prime" in its name, but `PkgZeroSt` does not ask that $\ell$ be large. We have not unfolded the operator in $\nu_{\mathrm{loc}}$ (`nuLocC`, an infimum of normalized valuations) or the package records.
