---
id: eventually-cong-bound-of-facts
title: The congruence bound for large parameters, restated
kind: theorem
decl: GlobalTheory.T.eventually_congBound_of_facts
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.AdmissibleParameterEventuallyStatement
covers: 2069
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [the congruence bound along a family](/entry/nlink-e-main-alt-alt/), and its proof only cites that theorem. Its user is [the closing of the family bound](/entry/nlink-close-main-alt-alt/), which feeds it to the lemma that the local bound is zero at large primes. The content is in [the congruence bound along a family](/entry/nlink-e-main-alt-alt/).

## Statement

**Theorem.** Assume the seven hypotheses $\mathrm{Hyp}_2$. Let $\varepsilon$ be real and let $F$ be a family of data with parameter $\varepsilon$. Then there is $x_0$ such that for each $x \ge x_0$ with $x > x_1(F)$ and each index $i$ of the family at $x$, if the norm choice facts hold for the datum $D_{x,i}$, then the congruence bound holds for $D_{x,i}$ and its size data $L_{x,i}$.

The congruence bound says that, at each prime $\ell > \ell^*$ off the exceptional set, the normalized length of the congruence module at $\pi$ is at most the sum of a Selmer length, the lengths of the Tate-Shafarevich groups, $v_\ell(h_E)$ and a term from the auxiliary primes. See the [entry above](/entry/nlink-e-main-alt-alt/) for the full statement.

## Proof

The proof is the term `NLinkE.main_alt_alt`. There is nothing else.

## In the Lean code

The theorem is in [AdmissibleParameterEventuallyStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AdmissibleParameterEventuallyStatement.lean#L11). The proof is `first | exact @NLinkE.main_alt_alt | ...`, a tactic that tries three ways to apply the other theorem. The two statements are the same, word for word. The name says "of facts" and "eventually", which matches the statement.
