---
id: finite-adelic-double-cosets-of-rational-sl-subgroup
title: Finitely many double cosets for a rational subgroup of SL, second name
kind: theorem
decl: GlobalTheory.T.finiteAdelicDoubleCosets_of_rational_SL_subgroup
module: Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.FiniteAdelicDoubleCosetsOfRationalSLSubgroupStatement
covers: 388
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [cf_of_isQGroup](/entry/cf-of-is-qgroup/). Its proof only calls that theorem. Its one user is [classFinite_integralLevel](/entry/class-finite-integral-level/), which applies it to a matrix group made from a subgroup of $\mathrm{GL}_n$ over a number field. Below it are 388 declarations.

## Statement

Let $\Gamma \subseteq M_\iota(\mathbb{C})$ be a set of matrices with `IsQGroup Γ`: $\Gamma$ is a subgroup of $\mathrm{SL}_\iota(\mathbb{C})$, it is stable under each field automorphism of $\mathbb{C}$, and it is closed for the Zariski topology defined by polynomials with rational coefficients. Let $R$ be a $\mathbb{Q}$-algebra and $R_0 \subseteq R$ a subring with `AdelicPair R R₀`: a rational number in $R_0$ is an integer, and $R = \mathbb{Q} + M R_0$ for each integer $M \geq 1$.

**Theorem.** `CF Γ R R₀` holds: let $\Gamma(A)$ be the set of matrices over $A$ that satisfy each rational polynomial equation of $\Gamma$, and $\Gamma(R_0)$ the elements of $\Gamma(R)$ with entries in $R_0$. Then there is a finite set $T \subseteq \Gamma(R)$ with

$$\Gamma(R) = \bigcup_{s \in T} \Gamma(\mathbb{Q}) \, s \, \Gamma(R_0).$$

## Proof

The proof is `cf_of_isQGroup`, applied with `exact`.

## In the Lean code

The theorem is in [FiniteAdelicDoubleCosetsOfRationalSLSubgroupStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/FiniteAdelicDoubleCosetsOfRationalSLSubgroupStatement.lean#L7). Its type is that of `cf_of_isQGroup` word for word, and the proof is a `first` combinator. The definitions are in [AdelicPair.lean](lean:Development/AbelianVarietyTheory/Definitions/AdelicHermitianForms/AdelicPair.lean#L15). The name says "adelic", but $R$ is any ring with `AdelicPair`.
