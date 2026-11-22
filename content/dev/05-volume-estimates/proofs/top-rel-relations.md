---
id: top-rel-relations
title: The Chern number relations for lattice bundles over a discrete valuation ring
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.TopRel.relations
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.ArithmeticRelationsStatementHolds
covers: 2226
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `RelationsStatement`: relations between Chern numbers of pairs of lattice bundles on a model over a discrete valuation ring, twisted by a permutation $\varphi$ of labels. [Its statement form](/entry/arithmetic-relations-statement-holds/) passes it to [the Hodge lattice flag bound from lattice families](/entry/model-on-hodge-of-family-pos/). The proof is short. It combines two lemmas, and both of them are relays to deeper proofs.

## Statement

Let $O$ be a discrete valuation ring of characteristic $0$ with a uniformizer $\varpi$, and let $\Omega$ be a field over $O$. Let $x$ be coordinates $x_{k,i} \in \Omega$, one block for each $k \in K$, such that the coordinate ideal of $x$ is a model over $O$ of dimension $d$ and the function field of $x$ is all of $\Omega$. Let $\Sigma$ be a finite set of labels with ranks $r, s \colon \Sigma \to \mathbb{N}$, let $p$ be a prime, $w \in O$, and $\varphi$ a permutation of $\Sigma$. Let $D$ be a lattice family: on each chart, lattices $\mathrm{lie} \leq W \leq w^{-1}\mathrm{lie}$ and $\omega_{\mathrm{HT}} \leq \omega \leq w^{-1}\omega_{\mathrm{HT}}$, with $p \neq 0$, $p$ not a unit, and $w^{p-1} = u p$ for a unit $u$. Let $\mathrm{Lie}, W$ (rank $r$) and $\Omega_1, \Omega_{\mathrm{HT}}$ (rank $s$) be chart bundles whose lattices are those of $D$. Let $\mathrm{lie}_\tau$ and $\mathrm{om}_\tau$ be local pairs that are flag pairs for these bundles.

**Theorem.** For each $k \geq 1$ and each list $Q$ of degrees with $|Q| + k = d + 1$, there is $h \colon \Sigma \to \mathbb{R}$ with

$$c_k(\mathrm{lie}_\tau) + c_k(\mathrm{om}_\tau) = h(\tau) - \frac{\lambda_k(\mathrm{lie}_\tau)}{p - 1}, \qquad p^k h(\tau) = h(\varphi\tau) + \lambda_k(\mathrm{lie}_{\varphi\tau})$$

for all $\tau$. Here $c_k$ is an intersection number of the pair with a power sum class, and $\lambda_k$ is $k$ times a class number on the divisor of $p$. When $\varphi$ is the identity, the second equation gives $h = \lambda_k/(p^k - 1)$.

## Proof

1. `lattice_family_ckRelations` gives the same relations for the bundles themselves, `CkRelations`.
2. $w \neq 0$: otherwise $u p = 0$, so $p = 0$ in $O$.
3. The bundles $\mathrm{Lie}$ and $W$ have the same generic fibre (`SameGeneric`): on each open chart, each lattice goes into the other after a multiplication by $1$ or by $w$. This uses the inclusions of $D$. The same holds for $\Omega_1$ and $\Omega_{\mathrm{HT}}$.
4. `uniformizer_model_perm_module_lattice` moves `CkRelations` from the bundles to the flag pairs and gives `Relations`.

## In the Lean code

The theorem is in [ArithmeticRelationsStatementHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/ArithmeticRelationsStatementHolds.lean#L12). `Relations` is in [BundleChernComparison.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/BundleChernComparison.lean#L66) and `CkRelations` is in [IsLatticeFamily.lean](lean:Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/IsLatticeFamily.lean#L42). The two lemmas are relays: `lattice_family_ckRelations` calls `CkTop.ckRelations_of_model`, and `uniformizer_model_perm_module_lattice` calls `CkRelations.main`. We have not opened those two proofs, and we have not unfolded the intersection numbers. The bundle number `ck` is defined with a choice of a flag model, and it is $0$ when no flag model exists.
