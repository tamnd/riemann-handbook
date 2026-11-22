---
id: etale-duality-trace-isomorphism
title: Power-sum classes of vector bundles in étale cohomology
kind: theorem
decl: UpperTheory.Et.etale_duality_trace_isomorphism
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.EtaleDualityTraceIsomorphism
covers: 1787
status: drafted
drafted_by: writer@claude
---
This theorem proves the axiom D2 of the étale chapter: vector bundles have power-sum classes in étale cohomology. It is one of the 27 axioms that [the finiteness theorem](/entry/etale-finiteness-of-duality/) passes to [e4](/entry/e4/), and it is also an input of the axiom D3 in the same file. Its proof only supplies 22 axiom theorems to a chapter theorem. The content is in [s57](/entry/s57/). Despite its name, the theorem says nothing about duality or a trace map.

## Statement

Let $q \neq 0$ and $k > 0$. For a simplicial presheaf $E$ on schemes, a map $V \colon E \to B\mathrm{GL}_N$ is a rank $N$ vector bundle on $E$. Say that $q$ is invertible on $E$ if $q$ is a unit in $\Gamma(U, \mathcal{O}_U)$ for each scheme $U$ with $E(U)_0 \neq \emptyset$.

**Theorem.** There are classes $s_k(V) \in H^{2k}(E, \mathbb{Z}/q(k))$, one for each vector bundle $V$, such that, when $q$ is invertible on the spaces involved:

1. $f^* s_k(V) = s_k(f^* V)$ for each map $f \colon E \to E'$;
2. $s_k(V \oplus W) = s_k(V) + s_k(W)$;
3. $s_k(L) = c_1(L)^k$ for a line bundle $L$.

These are power-sum (Newton) classes. For a sum $L_1 \oplus \dots \oplus L_N$ of line bundles, properties 2 and 3 force $s_k = \sum_j c_1(L_j)^k$.

## Proof

The proof is the chapter theorem `D2.intersectionNumber_baseChange`, a renaming of [s57](/entry/s57/), applied to the theorems that prove the axioms A1 to A5, A7 to A11, B1 to B5, B7, C1 to C5 and D1. Of these 22 inputs only D1, the [projective bundle formula](/entry/projective-bundle-formula-vector-bundle-any-space/), is used. The proof of s57 builds the Chern classes from D1 and sets $s_k$ to be the coefficient of $X^k$ in $-X c'(X)/c(X)$, where $c(X) = \sum_j c_j(V) X^j$.

## In the Lean code

The theorem is in [EtaleDualityTraceIsomorphism.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleDualityTraceIsomorphism.lean#L40). D2 is stated in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L124).

- The name is misleading. The duality axiom with a trace map is E8, at line 154 of the same file, and it is not used here.
- The lemma `D2.goal_of` in [InstCommRingR.lean](lean:Development/EtaleCohomology/EtaleSheaves/InstCommRingR.lean#L85) discards the first 21 of its 22 hypotheses with `intro _`. So 21 of the axiom theorems passed here are dead arguments.
- In Lean, $s_k(V)$ is defined as $0$ when $q$ is not invertible on $E$. The three properties are stated only for invertible $q$.
- C5 says that $H^1(\operatorname{Spec} A[t, t^{-1}], \mathbb{Z}/q(i)) \cong \mathbb{Z}/q$ and $H^n = 0$ for $n \geq 2$, for $A$ strictly henselian. Its input here is `etale_cohomology_locally_acyclic`, a name that does not describe this statement. We have not opened that theorem.
