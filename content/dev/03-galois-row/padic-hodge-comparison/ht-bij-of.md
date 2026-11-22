---
id: ht-bij-of
title: The Hodge-Tate comparison for good reduction, from a diagonal argument
kind: theorem
decl: CrystallineSemistableComparison.Onto.htBij_of
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.HodgeSurjectivity.HtBijOf
covers: 1058
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem proves that a Hodge-Tate comparison map for a smooth projective scheme over the integers of an $\ell$-adic field is bijective, and that the étale Betti numbers are sums of Hodge numbers. [htBij](/entry/ht-bij/) supplies its four hypotheses, and the result goes on to the [jump step](/entry/jump-step-holds/). Below this theorem are 1,058 declarations.

## Statement

Let $K \subset \overline{\mathbb{Q}}_\ell$ be finite over $\mathbb{Q}_\ell$, with integers $\mathcal{O}_K$. A *model* is a scheme $X$ over $\mathcal{O}_K$. It is *smooth* if it is projective, strictly semistable and smooth over $\mathcal{O}_K$. Put $V_n = H^n_{\mathrm{et}}(X_{\overline{\mathbb{Q}}_\ell}, \mathbb{Q}_\ell)$, with its action of $G_K$. For $a, n \geq 0$, $\mathrm{Hdg}(a, n)$ is the degree $n$ cohomology of a graded piece $\mathrm{gr}^a$ of a complex on $X_K$, a $K$-space. We have not unfolded `grT`.

A *Hodge-Tate premap* $P$ (`HTPre`) gives, for each model and each $a, n$, a pairing $h_{a,n} \colon V_n \times \mathrm{Hdg}(a,n)^\vee \to \mathbb{C}_\ell$ that is $\mathbb{Q}_\ell$-linear in $V_n$ and $K$-linear in the dual, through $K \subset \mathbb{C}_\ell$. It requires $\mathrm{Hdg}(a,n)$ to have finite dimension, and to be $0$ for $n < a$, as for $H^{n-a}(X_K, \Omega^a)$. It is $G_K$-equivariant up to the $a$-th power of the cyclotomic character, natural, and compatible with cup products, the unit class and $c_1$. Let $h_n \colon V_n \otimes \mathbb{C}_\ell \to \bigoplus_{a \leq n} \mathrm{Hdg}(a,n) \otimes_K \mathbb{C}_\ell$ be the map that $h$ gives.

- `Inj`: $h_n$ is injective;
- `Top`: for $X_K$ connected of dimension $d$, the part $V_{2d} \otimes \mathbb{C}_\ell \to \mathrm{Hdg}(d, 2d) \otimes_K \mathbb{C}_\ell$ is injective;
- `Surj`: $h_n$ is surjective.

**Theorem.** Assume:

1. (`HodgeTateMapExists`) for each $\ell$ and $K$ there is a premap $P$ with `Inj` for all smooth models and all $n$, and `Top` for the connected ones;
2. (`SqEx3`) a smooth model of relative dimension $d+1 \geq 2$ has a square datum: $X \times_{\mathcal{O}_K} X$ with its diagonal, and a smooth model $Y$ over it with étale line data;
3. (`DiagEt3`) for such a datum, the class of $Y$ in degree $2 + 2d$ is a sum of cup products of pullbacks along the two projections;
4. (`EtFin`) each $V_n$ has finite dimension.

Then for each $\ell$ and $K$ some premap $P$ has `Inj` and `Top`, and for each smooth model and each $n$, $h_n$ is surjective and
$$\dim_{\mathbb{Q}_\ell} V_n = \sum_{a=0}^{n} \dim_K \mathrm{Hdg}(a, n).$$

With $\mathrm{Hdg}(a,n) = H^{n-a}(X_K, \Omega^a)$ this is the Hodge-Tate decomposition of Faltings (p-adic Hodge theory, J. Amer. Math. Soc. 1, 1988) in the case of good reduction. This identification is our reading of the names; we did not check it.

## Proof

The proof is `htBij_of_parts parts rank_equality hH hS hD hF`.

1. `parts` proves `Parts`, 31 facts on sites, Kähler forms, Künneth maps, cup products and charts, each from a named lemma.
2. `htBij_of_parts` takes $P$ from hypothesis 1, which gives `Inj` and `Top`.
3. Surjectivity is `ontoAll_of`. In relative dimension $d+1 \geq 2$, `OntoOf3` gets it in all degrees from `Inj` in degree $2 + 2d$ and hypotheses 2 and 3. In lower dimension, `Retract` makes the model a retract of one of relative dimension $d+2$, and `OntoLow` carries surjectivity back.
4. `rank_equality` is linear algebra: a bijective $h_n$ gives the equality of dimensions.

## In the Lean code

The theorem is in [HtBijOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/HtBijOf.lean#L79), with `parts` at line 43. The other lemmas:

- `htBij_of_parts` and `HTBij` in [HtBijOfParts.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/HtBijOfParts.lean#L17).
- `ontoAll_of` and `Parts` in [OntoAllOf.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/OntoAllOf.lean#L47).
- `rank_equality` in [HodgeTateDimensionEquality.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/HodgeSurjectivity/CupSurjectivity/HodgeTateDimensionEquality.lean#L14).

`HTPre` and `HodgeTateMapExists` are in [IsEtaleFirstChernUntwisted.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/HodgeTateResidues/IsEtaleFirstChernUntwisted.lean#L39). The theorem adds surjectivity and the dimension count to the $P$ of hypothesis 1, which is assumed to exist and be injective. `DiagEt3` is a long existential statement with most of the geometry. A smooth model must be strictly semistable and smooth at once, so "semistable" in the names adds no case beyond good reduction.
