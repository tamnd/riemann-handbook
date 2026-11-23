---
id: e2-main
title: Proper base change from fifteen axioms
kind: theorem
decl: UpperTheory.Et.E2.main
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.SpecAbsolutelyIntegrallyClosedCohomology
covers: 1246
status: drafted
drafted_by: writer@claude
---
This theorem proves proper base change over a strictly henselian local ring from 15 axioms of the étale chapter. [Proper base change](/entry/proper-base-change/) supplies the axioms. The method is to pass to integral schemes whose rings of sections are absolutely integrally closed. Their cohomology vanishes in positive degrees, so only $H^0$ and the closed fibre need work.

## Statement

A ring $B$ is *absolutely integrally closed* if each monic polynomial of positive degree over $B$ has a root in $B$. Call a scheme $Z$ an *AIC scheme* if it is integral and $\Gamma(U, \mathcal{O})$ is absolutely integrally closed for each nonempty affine open $U$. For $p \colon X \to \operatorname{Spec} A$ with $A$ local, write $\mathrm{PB}(p)$ when restriction to the closed fibre is bijective on $H^n(\,\cdot\,, \mathbb{Z}/q(i))$ for all $n$.

**Theorem.** Assume the axioms A1 to A5, A7 to A10, B1 to B5 and E1. Let $A$ be a strictly henselian local ring, $q$ a unit in $A$, and $p \colon X \to \operatorname{Spec} A$ proper. Then $\mathrm{PB}(p)$ holds for each $i$.

## Proof

1. **Reduction to AIC schemes** (`reduce`). By descent along integral surjections (`n1`) and a covering lemma (`n9`), it is enough to prove $\mathrm{PB}(h \circ p)$ for each integral map $h \colon Z \to X$ from an AIC scheme $Z$.
2. **Chow's lemma** (`e2Cut_chow`). For such $h$ there is a dominant map $c \colon Z' \to Z$ from an AIC scheme with $c$ and $p \circ h \circ c$ in the class $\mathrm{IT}$. A map is in $\mathrm{IT}$ if it is a tower of steps, each an integral map followed by a proper base change of $\mathbb{P}^1_{\mathbb{Z}}$.
3. **Towers** (`towers`, from `tower` in LineHigh.lean). $\mathrm{PB}$ holds for each map in $\mathrm{IT}$ to a strictly henselian base, and for its composites with integral maps. The proof is an induction on the tower. An integral map is handled by `proper_base_change_integral_pullback`. For a step $c$ followed by $k$, step 1 gives an AIC source, Stein factorization (`proper_base_change_stein_factorization`) splits the map, and the fibre criterion `proper_base_change_fibre` reduces to two cases: the shorter tower, by induction, and a single step over a strictly henselian base. In the second case the source is an AIC scheme, so it has no positive-degree cohomology (`n49`). The closed fibre is connected (`n52`), so $H^0$ matches (`n45`). The closed fibre has $H^1 = 0$ (`n74`) and $H^n = 0$ for $n \geq 2$ (`proper_base_change_affine_space`).
4. **Descent along $c$.** `proper_base_change_fibre` says: if $\mathrm{PB}$ holds for the base change of $c$ to every strictly henselian point, then $\mathrm{PB}(p \circ h \circ c)$ is equivalent to $\mathrm{PB}(p \circ h)$. Step 3 gives both inputs.

The rest is bookkeeping.

## In the Lean code

The theorem is in [SpecAbsolutelyIntegrallyClosedCohomology.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/SpecAbsolutelyIntegrallyClosedCohomology.lean#L499). The definitions of $\mathrm{PB}$, AIC scheme, $\mathrm{IT}$ and the leaf statements, and the lemmas `reduce` and `tower`, are in [LineHigh.lean](lean:Development/EtaleCohomology/EtaleSheaves/LineHigh.lean#L189). The leaves are proved in the same file as the theorem, from line 148 to line 488, by about 100 lemmas `n1` to `n98` and named lemmas. We have not unfolded them.

- The hypotheses are a record `Hyp` of 15 axioms. LineHigh.lean also has `goal_of`, which states the result with the 25 axioms of `EtaleChapterETwo` and discards 10 of them: A11, B7, C1 to C5 and D1 to D3.
- The name of the file says "Spec of an absolutely integrally closed ring". It names the method, not the result.
- The coefficients are only $\mathbb{Z}/q(i)$ with $q$ a unit in $A$.
