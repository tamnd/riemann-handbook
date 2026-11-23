---
id: hodge-tate-comparison-smooth-projective
title: A Hodge-Tate pairing that is injective on smooth projective models
kind: theorem
decl: UpperTheory.Gal.Seam.HT.hodgeTate_comparison_smooth_projective
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.CrystallineTowers.ClosedHT
covers: 484
status: drafted
drafted_by: writer@claude
---
This theorem gives the first of the four inputs of [htBij](/entry/ht-bij/): a Hodge-Tate pairing $P$ on the $\ell$-adic cohomology of models over a finite extension of $\mathbb{Q}_\ell$, which is injective after extension of scalars to $\mathbb{C}_\ell$. `htBij` then adds surjectivity and the dimension count. The proof only applies [hodgeTate_of_etale_side](/entry/hodge-tate-of-etale-side/) to proved facts about étale cohomology.

## Statement

Let $\ell$ be a prime and $K \subset \overline{\mathbb{Q}}_\ell$ a finite extension of $\mathbb{Q}_\ell$. A *model* $M$ is a scheme $X$ over $\mathcal{O}_K$. It is *smooth* (`Model.Sm`) if $X$ is projective and strictly semistable over $\mathcal{O}_K$ and the structure map is smooth. Write $V^n = H^n_{\mathrm{et}}(X_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell)$ for the cohomology of the geometric generic fibre, and $\mathrm{Hdg}(a, n)$ for the Hodge pieces of the generic fibre over $K$ (we have not unfolded `Hdg`). Let $P$ be a pairing as in [htBij](/entry/ht-bij/) (the structure `HTPre`): linear, Galois-equivariant up to $\chi^a$, natural, and compatible with cup products, the unit class and first Chern classes.

**Theorem** (`HodgeTateMapExists`). For each $\ell$ and $K$ there is such a $P$ with the following property. For each smooth model $M$:

1. for each $n$, the map $V^n \otimes_{\mathbb{Q}_\ell} \mathbb{C}_\ell \to \prod_a \operatorname{Hom}(\mathrm{Hdg}(a,n)^\vee, \mathbb{C}_\ell)$ given by $P$ is injective (`HTPre.Inj`);
2. if the generic fibre is connected and smooth of relative dimension $d$ (`Model.Conn`), the part of this map in degree $2d$ with $a = d$ is already injective (`HTPre.Top`).

The full Hodge-Tate decomposition $V^n \otimes \mathbb{C}_\ell \cong \bigoplus_a H^{n-a}(X_K, \Omega^a) \otimes_K \mathbb{C}_\ell(-a)$ for smooth proper varieties is due to Faltings (J. Amer. Math. Soc. 1, 1988). This statement is only its injective half.

## Proof

The proof is `hodgeTate_of_etale_side etSideS`.

1. `etSideS` proves `EtSide` for smooth models. It is a field of `Top.core_holds`, which we have not unfolded. `EtSide` says: cup products exist; each $V^j$ has finite dimension; if the generic fibre is connected of dimension $d$, then $V^i = 0$ for $i > 2d$ and the functionals on $V^i$ given by cup product into $V^{2d}$ span the dual of $V^i$ (`Model.Dual`); and each smooth model has finitely many connected smooth models over it whose pullbacks detect each class (`comp`).
2. `hodgeTate_of_etale_side` is [ht_of](/entry/ht-of/) applied to `lvEx`, `kFin`, `dlog_class_exists_unique`, `kTop` and the étale facts. In `ht_of`, `pre_of` builds the pairing $P$, and `inj_of` proves clauses 1 and 2. `inj_of` uses the duality and the decomposition from `EtSide`, and `KTop`: the $d$-th power of the dlog first Chern class of a tautological line bundle is nonzero.

## In the Lean code

The theorem is in [ClosedHT.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/CrystallineTowers/ClosedHT.lean#L17). `HodgeTateMapExists` and `HTPre` are in [IsEtaleFirstChernUntwisted.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/IsEtaleFirstChernUntwisted.lean#L76), `ht_of` in [HtOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/HtOf.lean#L30), and `EtSide` in [EtSide.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/BocksteinBaseChange/EtSide.lean#L54).

Points to note:

- The name says "comparison", but the statement gives only a pairing and its injectivity. Surjectivity comes later, in `htBij_of`.
- A theorem with the same name, `CrystallineSemistableComparison.HT.hodgeTate_comparison_smooth_projective`, is in [HodgeTateComparisonSmoothProjective.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/HodgeTateComparisonSmoothProjective.lean#L19). It has two hypotheses, `E4` and `E8`, and is not used here.
