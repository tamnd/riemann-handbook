---
id: unit-match-succ
title: The induction step for unit matching, by the action of SL(2)
kind: theorem
decl: GlobalTheory.JR.UnitStep.unitMatch_succ
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.JacquetRallisUnitMatchSucc
covers: 326
status: drafted
drafted_by: writer@claude
---
This theorem proves the Jacquet-Rallis fundamental lemma for unit functions in rank $r + 1$ from the same lemma in rank $r$. It uses actions of $\mathrm{SL}_2(F)$ on test functions on both sides. [Its statement file](/entry/jacquet-rallis-unit-match-succ/) renames it, and [unit matching from the quadratic Weil representation](/entry/unit-match-of-weil-field/) uses it in each step of its induction. That entry sketches this proof; here we give it with its lemmas.

## Statement

Assume $\mathrm{WeilEt}$ and $\mathrm{GammaOne}$, and let $r \ge 0$. If $\mathrm{FourierMatch}(r+1)$ and $\mathrm{UnitMatch}(r)$ hold, then $\mathrm{UnitMatch}(r+1)$ holds.

The notation is that of [unit matching](/entry/unit-match-of-weil-field/) and [Fourier matching](/entry/fourier-match-of-weil-field/). Write $\mathbf{1}'$ and $\mathbf{1}$ for the unit functions on $\mathfrak{g}_{r+1}$ and $\mathfrak{h}_{r+1}$, and $n(t)$, $w$ for the standard elements of $\mathrm{SL}_2(F)$.

## Proof

Fix $E/F$, the measures, and a character $\psi$ of conductor $\mathcal{O}_F$ (from `unramifiedStandardAddChar_conductor_properties`).

1. **Two actions.** `exists_weilRepSL2_glBorderedBlock` gives an action $W_1$ of $\mathrm{SL}_2(F)$ on test functions on $\mathfrak{g}_{r+1}$, with $W_1(n(t)) f' (Y) = \psi(t\,cb)\,f'(Y)$ and $W_1(w) f' = \widehat{f'}$. `exists_weilRepSL2_hermitianBlock` uses $\mathrm{WeilEt}$ and $\mathrm{GammaOne}$ to give $W_2$ on $\mathfrak{h}_{r+1}$, with $W_2(n(t)) f (X) = \psi(t\,v^* v)\,f(X)$ and $W_2(w) f = \widehat{f}$.
2. **The actions preserve matching.** The set of $g$ with "$f'$, $f$ match implies $W_1(g) f'$, $W_2(g) f$ match" is a monoid. It contains $w$ by $\mathrm{FourierMatch}(r+1)$. It contains each $n(t)$, since $cb$ and $v^* v$ are the same invariant of matching elements and so the factors agree. `submonoid_eq_top`, from `closure_weyl_and_integral_unipotents_eq_univ`, says that a monoid that contains $w$ and the $n(t)$ with $t \in \varpi^{-1}\mathcal{O}_F$ is all of $\mathrm{SL}_2(F)$.
3. **The differences match.** Let $S'$ be the set of $g$ for which $W_1(g)\mathbf{1}' - \mathbf{1}'$ and $W_2(g)\mathbf{1} - \mathbf{1}$ match. It is a monoid, by $W(gh)u - u = W(g)(W(h)u - u) + (W(g)u - u)$, step 2 and `jacquetRallis_matching_add`. It contains $w$, since the Fourier transforms fix the unit functions (`partialFourier_preserves_test_fixes_unit`). For $t \in \varpi^{-1}\mathcal{O}_F$, the differences for $n(t)$ are $(\psi(t\,cb) - 1)$ times the unit functions. At an invariant $a$ with $|cb| \ge 1$, `jacquetRallisUnitMatch_step_of_one_le_norm` uses $\mathrm{UnitMatch}(r)$ to give matching of the unit functions. At $a$ with $|cb| < 1$, both factors are $0$. So $S' = \mathrm{SL}_2(F)$.
4. **Conclusion.** Let $a$ be regular with $cb \ne 0$, and take $x$ with $\psi(x) \ne 1$. For $g = n(x / cb)$, the differences are the unit functions times a factor that is $\psi(x) - 1 \ne 0$ at $a$. Divide by it: the unit functions match at $a$. The second part of `jacquetRallis_match_of_dense_separable` extends matching from the $a$ with $cb \ne 0$ to all regular $a$.

## In the Lean code

The theorem is in [JacquetRallisUnitMatchSucc.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetRallisUnitMatchSucc.lean#L124). The same file proves `submonoid_eq_top` (line 103) and the rules `matchAt_mul`, `matchAt_mul_zero`, `matchAt_of_mul` for multiplying matching functions by a function of $cb$. The other lemmas are called by their names in `GlobalTheory.T`. We read their statements, not their proofs.

On the Hermitian side the invariant is written $\operatorname{Tr}_{E/F}(v^* v)/2$ (the function `qU`), which equals $v^* v$ since $v^* v \in F$. $\mathrm{UnitMatch}(r)$ is used only in step 3, through `jacquetRallisUnitMatch_step_of_one_le_norm`. $\mathrm{WeilEt}$ and $\mathrm{GammaOne}$ are used only to build $W_2$. In step 2 the Lean proof shows $n(t) \in S$ for every $t$, not only for $t \in \varpi^{-1}\mathcal{O}_F$.
