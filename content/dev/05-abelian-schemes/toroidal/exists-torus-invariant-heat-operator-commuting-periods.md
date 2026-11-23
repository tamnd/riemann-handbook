---
id: exists-torus-invariant-heat-operator-commuting-periods
title: A torus-invariant heat operator that commutes with the periods (statement form)
kind: theorem
decl: GlobalTheory.T.exists_torusInvariant_heatOperator_commuting_periods
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTorusInvariantHeatOperatorCommutingPeriodsStatement
covers: 538
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`heat_commuting_periods_exists`](/entry/heat-commuting-periods-exists/), which has the proof. It has two users, both on power series charts: `exists_isKS_of_logDer` and [`isConstAlong_of_ks_zero`](/entry/is-const-along-of-ks-zero/). They lie below different inputs of [`hasLogKS`](/entry/has-log-ks/), so that theorem is its parent in the proof tree.

## Statement

Let $R$ be a Noetherian local domain that contains $\mathbb{Q}$ and is complete for its maximal ideal. Let $Q$ be a degeneration datum over $R$ (`DegData`) with abelian part $B$, line bundle $L$ on $B$ and character group $X$, and let a ring $O$ with involution act on it. Let $q \colon \tilde G \to B$ be the group scheme of the Lean structure `Ray`. We read $\tilde G$ as the Raynaud extension of $B$ by the torus with character group $X$; we have not unfolded `splitExt`. Let $v_1, \dots, v_n$ be a basis of the tangent vectors of $\tilde G$ along the unit section, and $\partial_a$ the invariant vector field of $v_a$ (`IsInv`). Let $t_1, \dots, t_m$ be nonzero elements of $R$ in which $Q$ is monomial for some forms $\gamma_i$, and $D$ a derivation of $R$ with $D(t_i) \in (t_i)$ for all $i$.

A *heat operator* (`Heat`) is a symmetric matrix $\Theta \in M_n(R)$, a vector $u \in R^n$, an open cover $(W_i)$ of $\tilde G$ with each $W_i$ over a trivializing open of $L$, vector fields $d_i$ on $W_i$ that lift $D$, and functions $p_i, p_i'$ on $W_i$. For each $k$ they define

$$\mathcal{H}_{i,k} f = 2k\, d_i f - \sum_{a,b} \Theta_{ab}\, \partial_a \partial_b f + 2 \sum_a u_a\, \partial_a f + (2k^2 p_i + 2k p_i')\, f,$$

and these must glue to an operator on sections of $q^* L^{k}$: $\mathcal{H}_{i,k}(g^k f) = g^k \mathcal{H}_{i',k} f$ for the transition functions $g$. It is *basic* (`IsBasic`) if each $W_i$ is $q^{-1}$ of an open of $B$, $p_i$ and $p_i'$ have weight $0$ for the torus, and $d_i$ keeps each weight $\alpha \in X$.

**Theorem.** There is a basic heat operator with defect $0$ (`HasDefect` with $c = 0$): for $k \geq 1$ and $\mu, \alpha \in X$, if $\sigma_1$ is the shift of $\sigma$ by the period of $\mu$, then the image of $\sigma_1$ is the shift of the image of $\sigma$. We have not unfolded the shift relation `ShiftEq`.

## Proof

The statement is that of `GlobalTheory.heat_commuting_periods_exists`, and the proof applies it. That proof starts from an operator with polynomial defect $2k\,w(\mu, \alpha) + 2k^2 \pi(\mu) + 2k\,\pi'(\mu)$ ([`exists_torusInvariant_heatOperator_polynomial_defect`](/entry/exists-torus-invariant-heat-operator-polynomial-defect/)), shows that the defect is a cocycle, and removes it.

## In the Lean code

The theorem is in [ExistsTorusInvariantHeatOperatorCommutingPeriodsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTorusInvariantHeatOperatorCommutingPeriodsStatement.lean#L16). The proof is `first | exact @GlobalTheory.heat_commuting_periods_exists | ...`. `Heat`, `IsBasic` and `HasDefect` are in [HasDefect.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasDefect.lean#L58). The monomial hypothesis and the condition on $D$ go only to the first lemma of that proof.
