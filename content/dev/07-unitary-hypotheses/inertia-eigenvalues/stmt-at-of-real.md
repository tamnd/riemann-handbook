---
id: stmt-at-of-real
title: Free cohomology and finite admissible classes at one prime
kind: theorem
decl: GlobalTheory.TopBridge.stmtAt_of_real
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TwistedLatticeCohomologyTheoremTOP
covers: 412
status: drafted
drafted_by: writer@claude
---
This theorem is the first of the three local statements in [admissible cocycles of twisted lattices](/entry/twisted-lattice-cohomology-theorem-top/). At one prime $\ell$ it shows that the cohomology of a twisted crystalline lattice is free, that $H^1_f$ is a direct summand, and that the admissible classes with coefficients in a finite module $X$ are $H^1_f \otimes X$. The parent turns this into the first of its three equivalences.

## Statement

We use the notation of [the parent entry](/entry/twisted-lattice-cohomology-theorem-top/): $\ell \ge 5$, $K$ unramified over $\mathbb{Q}_\ell$ of degree $n$, a coefficient field $L$ with ring of integers $\mathcal{O}$ and an irreducible $\lambda$, a crystalline lattice $T_0$ of rank $r$, crystalline characters $\chi_1$ and $\varepsilon$ (cyclotomic), and numeric data $D$ (`TopData`) that meet the conditions `T1`, `T2`, `T3`. Call such a tuple a *local situation* (`TopSit`). A situation is *real* (`TopSit.Real`) if for each residue field $k$ of $\mathcal{O}$ there is a functor to modules over $k((X))$ with a cyclotomic action, with a model of $T_0 \otimes k$ (twisted by $\chi_1^{-1}$) and a model of each admissible representation over $k$.

**Theorem.** Assume local Tate duality, the local Euler characteristic formula, a tied structure at $\ell$ (`LocTied`), that each local situation at $\ell$ is real, and the Bloch-Kato dimension formula for $H^1_f$ in case A (`BlochKatoJumpDimension`). Write $H = H^1(G_K, T_0(\chi_1^{-1}))$ and $H_f \subset H$ for the finite part. Then for each local situation:

1. $T_0(\chi_1^{-1}) \otimes \mathcal{O}/\lambda$ has no nonzero invariants, and its $H^2$ is zero;
2. $H$ is a free $\mathcal{O}$-module of rank $rn$;
3. $H_f$ has a complement in $H$, and its rank is $\sum_i d_i$, where $d_i$ is the number of Hodge-Tate weights of $T_0$ at the letter $i$ (with multiplicity) that are less than the weight $w_i$ of $\chi_1$;
4. for each finite $\mathcal{O}$-module $X$, the map $H \otimes X \to H^1(G_K, T_0(\chi_1^{-1}) \otimes X)$ is an isomorphism, and the admissible classes are the image of $H_f \otimes X$.

The dimension formula has the form of the formula $\dim H^1_f = \dim H^0 + \dim D_{\mathrm{dR}}/\mathrm{Fil}^0$ of Bloch and Kato (*L-functions and Tamagawa numbers of motives*, 1990, Section 3). The Lean form counts the negative jumps of the filtration, with multiplicity.

## Proof

1. `CrysRules.crysCalc` gives the crystalline calculus of the situation from the tied structure.
2. `TopVanish.vanish_of_real` uses Tate duality and reality to prove part 1.
3. `freeH_of_vanish_euler` (same file) proves part 2 and the isomorphism of part 4. It applies `FreeCoh.free_and_tensIso_gal` with the vanishing and the cardinality formula `T.card_H1_local_euler_formula` from the Euler characteristic.
4. `AdmClosure.admissible_closed` shows that admissible modules are closed under submodules, quotients and products. With step 1, `StdAdm.stdAdm` and `admissibleLocalSituation_admissible_classes` give the basic facts on admissible classes.
5. `FinSummandJumps.fSummand` uses the dimension formula to prove part 3.
6. `FiniteAdm.finAdm` (with `extCrys_of_tied`) and `ResidueBound.resBound_dsum` (with `PsiShiftProof.lemmaPsi`) give two facts, `FinAdm` and `ResBound`, which we did not unfold. With parts 2 and 3 they go to `AdmFinite.cls_eq_H1fX`, which proves the rest of part 4.

## In the Lean code

The theorem is in [TwistedLatticeCohomologyTheoremTOP.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistedLatticeCohomologyTheoremTOP.lean#L44). The conclusion is `ErrorExponentStatement P` and its body `Concl` in [InvariantsVanishing.lean](lean:Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/InvariantsVanishing.lean#L33). `TopSit` and `Real` are in [ResBound.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ResBound.lean#L36). We read the statements of the lemmas in the proof, not their proofs.

- The name `ErrorExponentStatement` does not describe the statement: there is no error exponent in it.
- Reality is a hypothesis here. The parent proves it with `BasePairs.real_of_presented`.
