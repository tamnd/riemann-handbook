---
id: intersection-exists-of-poincare-lelong
title: The arithmetic intersection numbers exist, from Poincaré-Lelong and resolution (second name)
kind: theorem
decl: GlobalTheory.T.intersection_exists_of_poincare_lelong
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.IntersectionExistsOfPoincareLelongStatement
covers: 324
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the arithmetic intersection numbers exist](/entry/thm-iexists/). Its only user is [the arithmetic intersection system from Poincaré-Lelong and resolution](/entry/arith-intersection-system-of-poincare-lelong-res-k/), which gets the family of heights from it. Below it are 324 declarations.

## Statement

Suppose that two statements hold:

- `PoincareLelong`: an integrated arithmetic Poincaré-Lelong formula on arithmetic varieties in products of projective spaces over $\mathbb{Z}$;
- `ResExistsStatement`: each such variety, with a proper closed subset of its complex points, has a complex-analytic log resolution.

Then `ExistsStatement` holds: there is a family $I$ of arithmetic intersection numbers with the axioms `IsFamily`. These axioms are symmetry, additivity in the last line bundle, and the recursion through the divisor of a section. The [parent entry](/entry/thm-iexists/) gives all three in full.

## Proof

The proof is `exact thmIExists`. The statement is the same, term for term.

## In the Lean code

The theorem is in [IntersectionExistsOfPoincareLelongStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/IntersectionExistsOfPoincareLelongStatement.lean#L11). Its proof is the tactic `first | exact @thmIExists | exact thmIExists | (intros; apply thmIExists <;> assumption)`. The first branch closes the goal, because the two types are equal. So this is a renaming. The file adds nothing else.
