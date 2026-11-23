---
id: towers
title: Proper base change for towers over a strictly henselian ring
kind: theorem
decl: UpperTheory.Et.E2.towers
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.SpecAbsolutelyIntegrallyClosedCohomology
covers: 558
status: drafted
drafted_by: writer@claude
---
This theorem is step 3 of [the proper base change theorem in E2](/entry/e2-main/). It says that $\mathrm{PB}$ holds for each map in the class $\mathrm{IT}$ to the spectrum of a strictly henselian local ring. It is a specialization of the lemma `tower`. The induction on the tower is in `tower`, and [the parent entry](/entry/e2-main/) describes it. This entry only fills in the inputs.

## Statement

**Theorem.** Assume the axioms `Hyp`. Let $B$ be a strictly henselian local ring, $q$ a unit in $B$, and $i \in \mathbb{Z}$. Let $r \colon Y \to \operatorname{Spec} B$ be in $\mathrm{IT}$. Then $\mathrm{PB}_{q,i}(r)$ holds: restriction to the closed fibre is bijective on $H^n(\,\cdot\,, \mathbb{Z}/q(i))$ for all $n$.

## Proof

1. Apply `tower` with the ten leaf lemmas. In order these are `n1 : Desc`, `n9 : Cover`, `n45 : HZero`, `n49 : AICAcyc`, `n52 : LineZero`, `n74 : LineOne`, `proper_base_change_affine_space : LineHigh`, `proper_base_change_integral_pullback : IntPB`, `proper_base_change_stein_factorization : Stein` and `proper_base_change_fibre : Fib`.
2. `tower` gives $\mathrm{PB}(v \circ r)$ for each integral map $v$ into $Y$. Take $v$ to be the identity of $Y$. It is integral by `inferInstance`.
3. `simpa` removes the composite with the identity.

## In the Lean code

- The theorem is in [SpecAbsolutelyIntegrallyClosedCohomology.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/SpecAbsolutelyIntegrallyClosedCohomology.lean#L492). `tower` is in [LineHigh.lean](lean:Development/EtaleCohomology/EtaleSheaves/LineHigh.lean#L213).
- `main` uses it two times: once for the composite $p \circ h \circ c$ over $A$, and once for the base change of $c$ to each strictly henselian point.
- `goal_of` in LineHigh.lean has its own internal copy of this specialization. So the same step is written two times.
- We have not unfolded the leaf lemmas.
