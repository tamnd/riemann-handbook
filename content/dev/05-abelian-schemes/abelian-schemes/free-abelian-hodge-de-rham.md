---
id: free-abelian-hodge-de-rham
title: The Hodge-de Rham sequence of an abelian scheme
kind: theorem
decl: MainStatements.Hodge.Free.abelianHodgeDeRham
module: Development.WeilBound.CoreStatements.AutomorphicKernels.AbelianDeRham.AbelianHodgeDeRham.AbelianHodgeDeRham
covers: 1044
status: drafted
drafted_by: writer@claude
---
This theorem proves the Hodge-de Rham facts in degree 1 for an abelian scheme over any commutative ring, in Čech-de Rham form. It is the main input of [the first de Rham cohomology of an abelian scheme](/entry/abelian-de-rham/), which uses it for the rank, the Hodge filtration, the base change and the duality. Below it are 1,044 declarations; 1,003 of them are below [the list of chapters](/entry/abelian-hodge-de-rham-prime/) that it calls.

## Statement

Let $R$ be a commutative ring and $A$ an abelian scheme over $\operatorname{Spec} R$ of relative dimension $g$. The code computes cohomology on the category of affine opens $U$ of $A$, with the functor $U \mapsto \mathcal{O}(U)$ (`OAff`). On it:

- $H^1_{\mathrm{dR}}(A/R)$ and $H^2_{\mathrm{dR}}(A/R)$ are the hypercohomology of the Čech-de Rham double complex (`HH1`, `HH2`), with cup product `cupHH`;
- $H^1(A, \mathcal{O}_A)$ is Čech cohomology (`HO1`), and `toHO1` is the map $H^1_{\mathrm{dR}} \to H^1(A, \mathcal{O}_A)$;
- $H^0(A, \Omega^1)$ is the module of compatible families of Kähler 1-forms on the affine opens (`GlobForm`), and `clForm` sends a closed form to its class.

**Theorem.** For all such $R$, $A$, $g$:

1. $H^1_{\mathrm{dR}}$ is finite projective, of rank $2g$ at each prime.
2. Cup product gives an isomorphism $\bigwedge^2_R H^1_{\mathrm{dR}} \cong H^2_{\mathrm{dR}}$.
3. $H^0(A, \Omega^1)$ and $H^1(A, \mathcal{O}_A)$ are finite projective, of rank $g$ at each prime.
4. Each global 1-form is closed, the class map $H^0(A, \Omega^1) \to H^1_{\mathrm{dR}}$ is injective, and $H^1_{\mathrm{dR}} \to H^1(A, \mathcal{O}_A)$ is surjective.
5. For each $R$-algebra $R'$ and each pullback square $X' = A \times_R R'$, there are isomorphisms $R' \otimes_R H^1_{\mathrm{dR}}(A) \cong H^1_{\mathrm{dR}}(X')$, $R' \otimes_R H^0(A, \Omega^1) \cong H^0(X', \Omega^1)$ and $R' \otimes_R H^1(A, \mathcal{O}_A) \cong H^1(X', \mathcal{O}_{X'})$, compatible with pullback.

The code also proves that the kernel of `toHO1` is the image of `clForm` (`cechHodgeFiltration_eq_range`). With part 4 this gives the exact sequence $0 \to H^0(A, \Omega^1) \to H^1_{\mathrm{dR}}(A/R) \to H^1(A, \mathcal{O}_A) \to 0$. These are the standard facts of Berthelot, Breen and Messing, *Théorie de Dieudonné cristalline II*, LNM 930 (1982), Section 2.5.

## Proof

The proof is one line. It applies `Chapters.print` to [`abelianHodgeDeRham'`](/entry/abelian-hodge-de-rham-prime/), a proof of the structure `Chapters`, and to five more theorems: `schemeModels`, `smooth_spreads`, `properSpreads`, `trivLocus` and `kFinite`. They give `SchemeModels`, `Spreads` for smooth and for proper maps, `TrivLocus` and `KFinite`. We have not unfolded these five statements.

`Chapters.print` chains the fields of `Chapters`. In order:

1. The Čech complexes: a dictionary of cochains, $d \circ d = 0$, homotopy invariance, descent (`DescentSt`: the restriction maps `resSys` are quasi-isomorphisms) and base change.
2. Finiteness: a smooth proper scheme has a finite system of opens whose Čech complex has the property `Perf`, which we have not unfolded (`PerfSt`).
3. The rank of $H^1(A, \mathcal{O}_A)$: at most $g$ (`h1le`) and at least $g$ (`h1ge`) over a field, then rank $g$ over any base (`h1all`).
4. Base change of $H^1(A, \mathcal{O}_A)$ and the wedge statement (`oside`).
5. One-forms: $H^0(A, \Omega^1)$ has rank $g$ (`ParSt`), and all global forms are closed and $H^1_{\mathrm{dR}} \to H^1(\mathcal{O})$ is onto (`DegenSt`).
6. `final` (`abelianHodgeDeRham_of_statements`) assembles these into the theorem.

## In the Lean code

The theorem is in [AbelianHodgeDeRham.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/AbelianDeRham/AbelianHodgeDeRham/AbelianHodgeDeRham.lean#L107). The statement `GlobalTheory.Published.AbelianHodgeDeRham` is in [AbelianHodgeDeRham.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/AbelianHodgeDeRham.lean#L15), and `Chapters` and `Chapters.print` are in [Development.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/AbelianDeRham/AbelianHodgeDeRham/Development.lean#L67).

The theorem has no hypothesis. The work is in the 47 theorems that fill `Chapters` and in the five extra theorems. `Chapters.print` only passes the fields to each other. The namespace name `Free` covers only part 1.
