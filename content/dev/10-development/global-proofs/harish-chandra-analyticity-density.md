---
id: harish-chandra-analyticity-density
title: Analytic matrix coefficients and dense Levi submodules, the proof
kind: theorem
decl: GlobalTheory.CompanionTheory.Hypotheses₂.harishChandra_analyticity_density
module: Development.AutomorphicSpectrum.Proofs.GlobalProofs.AdmissibleOfIwasawaDecomposition
covers: 313
status: drafted
drafted_by: writer@claude
---
This theorem proves the two statements that [the literature form](/entry/harish-chandra-analyticity-of-literature/) gives for $G = U(p,q)$ and $K = U(p) \times U(q)$. Part 1 says that $K$-finite matrix coefficients of an admissible representation are real analytic. Part 2 says that a nonzero subspace of a unitary irreducible representation of a Levi group $M$ is dense if it is stable under the derivatives along one-parameter subgroups. We use the names of that entry.

## Statement

The statement is the pair of parts 1 and 2 of [the literature form](/entry/harish-chandra-analyticity-of-literature/). The proof is the pair of two lemmas, `admissibleCoefficientsAnalytic` for part 1 and `leviSubmoduleDense` for part 2.

## Proof

Both parts go through a word bound. A smooth vector $v$ satisfies the word bound if there is $C$ with

$$\lVert X_1 \cdots X_k v \rVert \le C^{k+1}\, k!\, \lVert X_1 \rVert \cdots \lVert X_k \rVert$$

for all $k$ and all $X_i$ in the Lie algebra. Here $X v$ is the derivative of $t \mapsto \pi(\exp tX) v$ at $0$.

**From $K$-finite to the word bound.** Let $v$ be $K$-finite in an admissible $\pi$ on a closed linear reductive group.

1. $v$ lies in a finite-dimensional $K$-stable subspace $Y$ that every operator commuting with $K$ keeps (`isotypic`).
2. Every vector of $Y$ is smooth (`garding`).
3. Pick a basis $b_1, \dots, b_d$ of the Lie algebra on which $K$ acts by orthogonal matrices (`inv_basis`). Then $\Delta = \sum_i b_i^2$ commutes with $K$ (`delta_comm`), so $\Delta$ keeps $Y$.
4. A finite-dimensional space of smooth vectors that $\Delta$ keeps satisfies the word bound (`word_of_delta`). This step needs $\pi$ to be almost isometric: an inner product $Q$ comparable to the norm, with $Q(\pi(\exp tX)x)$ at most $e^{a\lvert t \rvert}$ times $Q(x)$.

This route has the form of Nelson's theorem on analytic vectors (Ann. of Math. 70, 1959). We have not compared the constants.

**Part 1.** $G$ is linear reductive and closed, and $\pi$ is admissible on it. The almost isometric condition comes from polynomial growth of $\lVert \pi(g) \rVert$ and an integrability bound on $G$ (`growth`, `volume`, `almost_of_growth`). The word bound then gives that $g \mapsto \langle w, \pi(g)v \rangle$ is analytic on $G$ (`analytic_uj`).

**Part 2.** The Levi group $M$ is linear reductive and closed. Its unitary irreducible $\sigma$ is admissible by the Iwasawa decomposition of $M$ (`admissible_of_iwasawa_decomposition`). A unitary representation is almost isometric with $a = 0$.

1. Fix $X$ with $\exp tX \in M$ for all $t$. For $v \in S$ the function $t \mapsto \langle w, \sigma(\exp tX)v \rangle$ is analytic (`one_param`). With the derivative hypothesis, this keeps $\sigma(\exp X)v$ in the closure $\bar S$.
2. Each $g \in M$ is $\exp X \exp Y$ with such $X, Y$. So $\bar S$ is stable under $M$.
3. By irreducibility $\bar S$ is $0$ or everything. It is not $0$, since $S \ne 0$. So $S$ is dense.

## In the Lean code

The theorem is in [AdmissibleOfIwasawaDecomposition.lean](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/AdmissibleOfIwasawaDecomposition.lean#L172). The two lemmas are at [L136](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/AdmissibleOfIwasawaDecomposition.lean#L136) and [L148](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/AdmissibleOfIwasawaDecomposition.lean#L148). The common step is `smooth_word_of_adm`. `WordBound`, `AlmostIsom` and `IsSmoothVec` are in [IsSmoothVec.lean](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/IsSmoothVec.lean#L18). The lemmas `isotypic`, `garding`, `growth`, `volume`, `inv_basis`, `delta_comm`, `word_of_delta`, `analytic_uj`, `one_param` and `admissible_of_iwasawa_decomposition` are second names, proved by `@` of lemmas in other files. We have not opened those proofs.
