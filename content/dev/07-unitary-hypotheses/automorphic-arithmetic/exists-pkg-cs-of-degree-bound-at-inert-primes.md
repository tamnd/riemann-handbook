---
id: exists-pkg-cs-of-degree-bound-at-inert-primes
title: Row packages at inert primes of odd order
kind: theorem
decl: UpperTheory.exists_pkgCs_of_degree_bound_at_inert_primes
module: Development.AutomorphicArithmetic.OrbitLabellings.ExistsPkgCsOfDegreeBoundAtInertPrimes
covers: 2002
status: drafted
drafted_by: writer@claude
---
This theorem builds two kinds of row packages at an inert prime $l$ whose Frobenius order is odd. Its one user, [`goodPrime_packages`](/entry/good-prime-packages/), takes its two halves as the parts `PkgCsSt` and `PkgZeroCsSt` of `PkgSt`. The work is in the private lemma [`exists_rowFamS`](/entry/exists-row-fam-s/). This theorem adds bookkeeping only. The chain above it ends in branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The written proof does not name it.

## Statement

Let $E$ be a CM number field with a host $H$, a datum $D$, a level $M$, a moduli scheme $X$ and a coefficient field $c$. The predicate `AllPts` $\Phi$ says this. Assume that `star` is the conjugation of $H$ on $O_E$. Let $N$ be a numerical datum and $1 \le j \le m$, such that the signature $(p,q)$ of $D$ is $\sigma_j$. Let $p_l$ be a map from the places $\mathrm{Bool} \times A$ of $N$ to the embeddings $E \to \mathbb{C}$ that is tied to $c$ (`PlaceTie`), and let $a$ be a dominant weight. Let $\lambda$ be a finite prime of $c$ whose residue characteristic $l$ is not small, is not one of the primes $q_N$ and $d_N$ of $N$, and does not divide $M$, with $5 \le l$ when $l$ is `Inert`. Let $y$ be an algebraic integral point over a complete discrete valuation ring above $\lambda$, with an integral chart. Let $\nu$ be a real with $e_\lambda \nu$ at most the local value `nuLocC` of the chart, where $e_\lambda$ = `ramOverZ`. Then $\Phi(N, j, l, p_l, a, n_W, \nu)$ holds.

**Theorem.** Assume `UpFSt p` for all primes $p$. Let $l$ be inert with odd order `ordP l`, and let $P$ = `parOf N j l`.

1. For all reals $T, \theta_0, C_1$ with `DegHyp2` $P$ `gapW` $T\ \theta_0$ `restOf` $C_1$, and with $f((i_0(k,l)+1)(k-1)+4r) \le n_W$, there is a package `PkgCs` with $T$ and $\nu$ as its fields.
2. If $w_j \ge 0$, $a(\tau,0) \le s(l-1)$ when $D$ has positive multiplicity at $\tau$, and $4rsf \le n_W$, then there is a package `PkgZeroCs` with $\nu$ as its field.

Here `gapW` is $a(p_l z, k-2) - a(p_l z, k-1)$ and `restOf` is $\mathrm{DF}(D,a) - (k-1)\sum_z$ `gapW` $z$.

## Proof

Both halves call [`exists_rowFamS`](/entry/exists-row-fam-s/) with the same hypotheses. It gives orbit representatives $Z$, a bijection $\tau$ from $Z \times \mathbb{Z}/2d$ onto the embeddings, a row family and the bound `ValBlocksS` on $\nu$. In part 1 the proof shows that the multiplicities are at most $r$ and that the gap weight at $k-1$ is `gapW` at even $s$. It then reindexes $\mathrm{DF}$ and $\sum$ `gapW` through $\tau$ to get the field `rest_eq`. The two numeric hypotheses go unchanged into the fields `deg` and `what₂`. In part 2 it takes $K = r$ and $T = 1$. The field `first` comes from `gap_sums`, and the size bound comes from $|Z| \cdot d = f$.

## In the Lean code

The theorem is in [ExistsPkgCsOfDegreeBoundAtInertPrimes.lean](lean:Development/AutomorphicArithmetic/OrbitLabellings/ExistsPkgCsOfDegreeBoundAtInertPrimes.lean#L195). `AllPts`, `parOf`, `gapW`, `restOf`, `PkgCsSt` and `PkgZeroCsSt` are in [DepthNumbersThresholdEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/DepthNumbersThresholdEq.lean#L95). `PkgCs` and `PkgZeroCs` are in [RowDefs.lean](lean:Development/AutomorphicArithmetic/OrbitLabellings/RowDefs.lean#L55), and `gap_sums` is in [GapParts.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/GapParts.lean#L45). We have not unfolded `nuLocC`, `Moduli`, `IntFr` or `IntChart`. The packages go on to `rowBound_le_Fnum_sum_add_error` and `pkgZeroCs_nu_nonpos_of_monSupply` in the same folder.

The statement copies `PkgCsSt ∧ PkgZeroCsSt` in full instead of using the two names. `UpFSt` is used only to call `exists_rowFamS`.
