---
id: twisted-lattice-cohomology-theorem-top
title: Admissible cocycles of twisted lattices from the local hypotheses
kind: theorem
decl: GlobalTheory.TopBridge.twistedLatticeCohomology_theoremTOP
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TwistedLatticeCohomologyTheoremTOP
covers: 1472
status: drafted
drafted_by: writer@claude
---
This theorem describes the admissible cocycles of a crystalline lattice and of its twisting characters at an unramified place. It takes 24 local hypotheses, packed as `admitted`. Its user is [the top local theorem](/entry/bloch-kato-top-of-local-tate-duality-euler-char-alt/), which proves the 24 hypotheses. The result is used in [the congruence bound along a family](/entry/nlink-e-main-alt-alt/).

## Statement

Fix a prime $\ell$, a finite unramified extension $K$ of $\mathbb{Q}_\ell$ with $\ell \neq 2$, a coefficient field $L$ that is good for $K$ at level 1, its ring of integers $\mathcal{O}$, and an irreducible $\lambda \in \mathcal{O}$. Let $G = G_K$, let $I \subset G$ be the inertia subgroup, and let $\varepsilon$ be the cyclotomic character.

Let $\rho \colon G \to \mathrm{GL}(V)$ be continuous and crystalline, with Hodge-Tate multiplicities given by multisets $U_i$, and let $T_0$ be a lattice. Let $\chi_1, \dots, \chi_t \colon G \to \mathcal{O}^\times$ be crystalline characters with $\chi_c = \chi_1 \varepsilon^{-(c-1)}$, where $\chi_c$ has the single Hodge-Tate weight $w_i + c - 1$ at the embeddings of type $i$. Assume also numeric conditions on the weights. Let $X$ be a finite $\mathcal{O}$-module. A cocycle $z$ with values in $T \otimes X$, for the action twisted by $\chi_1^{-1}$, gives an extension of $\mathcal{O}(\chi_1)$ by $T \otimes X$. Call $z$ *admissible* if for all large $a$ with $\lambda^a X = 0$, this extension, with $\mathcal{O}(\chi_1)$ cut down to $\mathcal{O}/\lambda^a$, is a subquotient of lattices in a finite product of crystalline representations with prescribed Hodge-Tate multiplicities and with characteristic polynomials prescribed modulo $\lambda$.

**Theorem.** Assume `admitted D HW F Cm`. If $\ell \ge 5$, then:

1. on $T_0$, seen in $\chi_1^{-1} \rho$, $z$ is admissible if and only if $z$ is a sum of Bloch-Kato finite cocycles tensored with elements of $X$, plus a coboundary;
2. on a lattice of $\chi_c$ with $2 \le c \le t$, $z$ is admissible if and only if $z$ is a coboundary;
3. on a lattice of $\chi_1$, $z$ is admissible if and only if $z$ restricted to $I$ is a coboundary.

## Proof

The proof takes part 18 of `admitted` (Tate duality and the Euler characteristic) and part 19 (the dimension formula for $H^1_f$). First it shows that each local situation $S$ at $\ell$ is *real*: the reduction of the lattice modulo $\lambda$ has a model over a Laurent series field $k((X))$, and so does each admissible representation over $k$. This is `BasePairs.real_of_presented`, fed with `RedFun.realD`, `CrysRules.crysCalc` and `T.wachLattice_usedProperties_of_admitted`, which uses all of `admitted`.

From reality the proof gets three local statements:

- `stmtAt_of_real` . From Tate duality, `TopVanish.vanish_of_real` gives $H^0 = 0$ and $H^2 = 0$ for the residual representation. The Euler characteristic makes the module `HH` free of rank $rn$ (`freeH_of_vanish_euler`, through `T.card_H1_local_euler_formula`). Part 19 gives that $H^1_f$ is a direct summand. Last, `AdmFinite.cls_eq_H1fX` shows that the admissible classes are $H^1_f \otimes X$.
- `TopSteps.CharVanish.stmt_of_real`, for the twists $\chi_c$ with $c \ge 2$.
- `TopSteps.admissibleUntwistedCharUnramified_of_residueRealisation`, for $\chi_1$.

Then `T.exactLocalConditions_topCore` puts the three together into the three equivalences.

## In the Lean code

The theorem is in [TwistedLatticeCohomologyTheoremTOP.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistedLatticeCohomologyTheoremTOP.lean#L67). The conclusion is `tableLineDegreeTwo.Stmt D HW F Cm`, that is `admitted D HW F Cm → aux₃ D HW F`, with `TopCore` in [TableLineDegreeTwo.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/TableLineDegreeTwo.lean#L193). We have not unfolded `ErrorExponentStatement`, the two character statements, or `TopCore` as `exactLocalConditions_topCore` proves it. We describe them from the steps of their proofs.

- The name "theoremTOP" does not describe the statement.
- The conclusion `aux₃ D HW F` does not mention $Cm$. $Cm$ enters only through `admitted`.
