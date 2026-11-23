---
id: splitting-package-holds
title: Seven statements on path polynomials
kind: theorem
decl: Formalism.MainNotions.G.ColumnFamilies.splitting_package_holds
module: Formalism.SharpRestriction.GrowthBounds.BinomialPolynomialIdentities.SplittingThirdPartHolds
covers: 427
status: drafted
drafted_by: writer@claude
---
This theorem proves `Conclusion2 D`, seven statements on polynomials built from paths of weights. It is the second part of [`tool_statements_hold`](/entry/tool-statements-hold/). The proof only puts seven lemmas side by side. Below it are 427 declarations.

## Statement

Fix $N$ letters, each a vector or a covector letter (`Letters`). For $B \in \mathbb{N}^N$, $\mathrm{Pol}_R(n, B)$ is the module of polynomials in $X_{i,m}$ ($i < N$, $m < n$) of degree $B_i$ in letter $i$. A *path* (`PPath`) is a list of dominant weights $0 = \mu_0, \mu_1, \dots, \mu_N \in \mathbb{Z}^n$ in which each step is a horizontal strip of $B_i$ boxes: added to $\mu_i$ for a vector letter, removed from $\mu_i$ for a covector letter (`HStrip`). For a path and a family $I$ of column sets with `IsSt` (a standard filling), $\Psi_R(\mu, I)$ is a product over columns $c$ of polynomials `Kcol`. `Ican` is one canonical filling.

Let $O$ be a complete discrete valuation ring with $p \ne 0$ in its maximal ideal (`UniformizedDVR`), with residue field $\mathbb{F}$. `Conclusion2 D` is the conjunction of:

1. `AutomorphicSideConclusion`: for each path with last weight $\mu$, $\Psi_O(\mu, \mathrm{Ican})$ is a highest weight vector of weight $\mu$ (`IsHWVPol`: killed by the divided powers $E_{ab}^{(k)}$, $a < b$). Over $\mathbb{F}$ these vectors, for all paths ending at $\mu$, are linearly independent.
2. `DefiniteRankOne`: over $O$ and over $\mathbb{F}$, the polynomials $G \in \mathrm{Pol}(n,B)$ with $\theta_i \le$ `valS` and `lam1S` $\le M_i$ on the first $i+1$ letters, for all $i$, are the span of the $\Psi(\mu, I)$ with $\theta_i \le \mu_{i+1}(n-1)$ and $\mu_{i+1}(0) \le M_i$. These are the lowest and highest exponents after the substitution `twistSub`, which we have not unfolded.
3. `RotatedSumBound`: if $N + r \le K$, a path in $\mathbb{Z}^{r+K}$ with weights $(\nu_i, \kappa_i)$ exists exactly when $B = b' + b''$, $\nu$ is a path for $b'$, $\kappa$ is a path for $b''$, and `CondC` holds.
4. `PathWeightComponents`, 5. `ConclusionB3`, 6. `CoefficientDependence`, 7. `CanonicalTranslateJetIdentity`: we have not unfolded these four.

## Proof

Each conjunct is one lemma.

1. `automorphicSideConclusion_of_pathBasis`, from the basis lemma `admissible_standardPath_basis`.
2. `splitting_third_part_holds`, in the same file: `lemma_A3_over_domain` and `lemma_A3_over_field`.
3. `prvB1_of_D7`.
4. `lemma_B2`.
5. `nested_sets_lemma_of_admitted`, with `adm_fourteen` and `admissible_externalProduct`.
6. `coefficientDependence`.
7. `canonical_translate_jet_identity`.

## In the Lean code

The theorem is in [SplittingThirdPartHolds.lean](lean:Formalism/SharpRestriction/GrowthBounds/BinomialPolynomialIdentities/SplittingThirdPartHolds.lean#L17). `Conclusion2` is in [StatementOfDegreeAndBound.lean](lean:Formalism/SharpRestriction/GrowthBounds/StatementOfDegreeAndBound.lean#L437), and the paths and $\Psi$ are in [ObjPol.lean](lean:Formalism/SharpRestriction/GrowthBounds/ObjPol.lean#L300).

Odd points:

- The datum $D$ is not used. Each of the seven statements takes it as `_D`.
- The names do not match the content. `splitting_third_part_holds` proves the second conjunct. `DefiniteRankOne` and `AutomorphicSideConclusion` are about polynomial spans.
- `ColumnFamilies.Top.Conclusion2` in [BinomialPolynomialIdentities.lean](lean:Formalism/SharpRestriction/GrowthBounds/BinomialPolynomialIdentities.lean#L40) is a second name for this theorem. A different theorem with the same short name, `WittFrameLocaliserOrders.splitting_package_holds`, is in [WittFrameLocaliserOrders.lean](lean:Formalism/SharpRestriction/GrowthBounds/WittFrameLocaliserOrders.lean#L5804).
