---
id: ht-of
title: An injective Hodge-Tate pairing, built from lifts to crystalline families
kind: theorem
decl: CrystallineSemistableComparison.HT.ht_of
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.HodgeTateResidues.HtOf
covers: 428
status: drafted
drafted_by: writer@claude
---
This theorem builds the Hodge-Tate pairing $P$ and proves that it is injective on smooth models. Its only caller is [hodgeTate_of_etale_side](/entry/hodge-tate-of-etale-side/), which supplies four of its five hypotheses. The pairing is the structure `HTPre` of [the Hodge-Tate comparison for good reduction](/entry/ht-bij-of/). The proof puts together five lemmas. Below it are 428 declarations.

## Statement

The models, $V^n$, $\mathrm{Hdg}(a,n)$, `HTPre`, `Inj` and `Top` are as in [the injective Hodge-Tate pairing](/entry/hodge-tate-comparison-smooth-projective/).

**Theorem.** Assume:

1. (`LvEx`) for each $\ell$ and $K$, a level system for the crystalline base exists;
2. (`KFin`) for $X$ proper and smooth over a field $K$ of characteristic $0$, each $\mathrm{Hdg}(a,n)$ has finite dimension, and is $0$ for $n < a$;
3. (`DlogClassExistsUnique`) a line datum $D$ whose opens $\mathcal{V}_D$ have supremum $X$ has exactly one dlog first Chern class;
4. (`KTop`) for $X$ connected and smooth of relative dimension $d$ over $K$, with a tautological line datum, the $d$-th power of its dlog first Chern class is not $0$;
5. (`EtSideS`) the étale facts of [the previous entry](/entry/hodge-tate-of-etale-side/).

Then `HodgeTateMapExists`: for each $\ell$ and $K$ some $P$ satisfies `Inj` on every smooth model and `Top` on every connected one.

## Proof

Fix $\ell$ and $K$.

1. `etP` gives an étale family $e$: maps from the $\ell$-adic classes of each model to cohomology with coefficients in $A_{\mathrm{cris}}$ at each level, which respect the unit class and first Chern classes. It also gives a unit class in $V^0$.
2. `half1` turns $e$ into a lift relation (`Half1`). Each class $v$ in degree $j$ of a smooth model has a lift $x$ to a crystalline family, unique after a shift. The relation respects sums, scalars, shifts, Galois action, pullback, cup products, the unit and $c_1$.
3. `half2` gives functionals $\gamma$ from crystalline families to $\operatorname{Hom}(\mathrm{Hdg}(a,j)^\vee, \mathbb{C}_\ell)$ (`Half2`). They are linear over $A_{\mathrm{cris}}$ through $\theta$, linear over $K$, invariant under shifts, equivariant up to powers of $\chi$, natural, and compatible with cup products, the unit and $c_1$. This step uses hypothesis 1.
4. `pre_of` defines $P(v, \varphi) = \gamma(x)(\varphi)$ for a chosen lift $x$ of $v$ on a smooth model, and $0$ on other models. It checks the laws of `HTPre` with hypotheses 2 and 3.
5. `inj_of` proves `Inj` and `Top` from hypotheses 4 and 5, the laws `kForm` and the unit class of step 1.

We have not unfolded the proofs of these lemmas.

## In the Lean code

The theorem is in [HtOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/HtOf.lean#L30), with `half2` above it. The lemmas are in [FirstChernCocycleAllLevels.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/FirstChernCocycleAllLevels.lean#L117), [Half1.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/Half1.lean#L17), [HalfGaloisOfCompatible.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/HalfGaloisOfCompatible.lean#L56), [GTSmul.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/GTSmul.lean#L104) and [SumCoord.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/SumCoord.lean#L252). The hypotheses are in [KProps.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/KProps.lean#L13), and `Half1`, `Half2` in [IsFirstChernClassInFamily.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/IsFirstChernClassInFamily.lean#L167).

`half2` passes `KFin` to `half2Of`, but `half2Of` ignores its last argument, which is `KFin` (`fun ht hs hL h1 h2 h3 h4 h5 h6 h7 _`). So `KFin` is used only in step 4.
