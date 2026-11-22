---
id: link-n-of-tw-good-galois-preconditions
title: The twisted place bound LinkN for one family, by a cut of each datum
kind: theorem
decl: UpperTheory.GalC.linkN_of_twGood_galoisPreconditions
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LinkNFam
covers: 14241
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `LinkN` for one family $F$. `LinkN` is inside the predicate `NL` of the field `nRest` of `HypsAlt` (see the [unitary hypotheses chapter](/proof/unitary-hypotheses/) and the [step on HypsAlt](/step/hyps-alt-def/)). Its caller is [LinkN along a slot](/entry/link-n-of-bound-at-two-three-slot/). Below this theorem are 14,241 declarations.

## Statement

Let $F$ be a family (`FamP eps`): a threshold $x_1 > 1$, index types $I_x$, and for $i \in I_x$ a datum $D(x,i)$, size data $L(x,i)$ and, for $x > x_1$, a norm choice $n(x,i)$. Assume:

1. `Hypotheses₂`: seven inputs named after published results (Fontaine's $B_{\mathrm{cris}}$, global Artin reciprocity, local Bloch-Kato, local Tate duality, local Euler characteristic, local finiteness, Bhatt-Scholze). We have not checked them against the literature.
2. `CutGivesAlt`: for each datum $D$ and norm choice $n$ with `GaloisPreconditions D n` and `Tie4 D`, there is a good cut $c$ of $D$ such that the cut datum satisfies `NormChoiceFacts` and `Tie4`.
3. `TwGood F`: eventually along $F$, a twist condition holds at each member.
4. For all $x > x_1$ and $i$: `GaloisPreconditions (D x i) (n x i)` and `Tie4 (D x i)`.

Then `LinkN F` holds: there are $C$ and $x_0$ such that for all $x \ge x_0$, all $i$ with `ShaFinOdd (D x i)`, and each lift index $j$, if $\sum_l v(l)$ converges then

$$\eta(L,j) \le d_0(j)\Big(C\big(f\,m\,b\,L^2 + (\log x)^2 N_c\big) + \sum_l v(l)\Big).$$

Here $\eta(L,j)$ is the weighted sum over the twisted places in the support of $L$, as in the chapter, and $v(l) = \log l \sum_{e=1}^{t-1} \mathrm{sha}(l,e)$ for $l$ prime.

`GaloisPreconditions` is a record of 18 named conditions on a datum, and `Tie4` is a conjunction of four. We have not unfolded these fields.

A *cut* $c$ of $D$ (`CutD`) keeps some local indices and, at each kept index, a nonempty set $X_i$ of points. It is *good* if $i$ is kept exactly when $Z^{\mathrm{good}}_i \ne \emptyset$, $Z^{\mathrm{good}}_i \subseteq X_i$, the points of $Z_i \cap X_i$ are good, and a Hecke-equivariant endomorphism acts on eigenvectors by a fixed nonzero integer at good points and by $0$ outside $X_i$.

## Proof

1. `exists_const_tieChi_bound_of_facts` gives $C \ge 0$ and $C_T \in \mathbb{N}$ such that `NormChoiceFacts` and `Tie4` imply the bound `ExtraAlt D C CT` at each datum.
2. For each $x > x_1$ and $i$, hypothesis 2 gives a good cut $c(x,i)$. For $x \le x_1$ the proof takes the trivial cut `CutD.all`.
3. Let $F'$ = `gd F c` be the family with each datum replaced by its cut. Steps 1 and 2 give `FactsFAlt F' C CT`, and `twGood_gd` gives `TwGood F'`.
4. [`conclF_of_family_facts_and_bound_at_two_three`](/entry/concl-f-of-family-facts-and-bound-at-two-three/) gives `ConclF F'`, with the bound at 2 and 3 from `at23_family_alt`. Then `linkN_along_family_of_localBounds` gives `LinkN F'`.
5. `linkN_of_gd` moves `LinkN` back from $F'$ to $F$. For $x > x_1$ it needs a good cut, the multiplicity bound `MultLe` (from `goodPointMultiplicityLeRank_proof`) and `adm3`, a field of `GaloisPreconditions`. The new constant is $C + C_1$, where $C_1$ from `admissible_parameters_family_const` bounds the logarithm of the integer of the cut.

## In the Lean code

The theorem is in [LinkNFam.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L37). `gd`, `twGood_gd` and `linkN_of_gd` are in [LinkNOfGd.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/HeckeGaloisCriteria/LinkNOfGd.lean#L17).

The theorem takes no bound at 2 and 3 as a hypothesis: it proves it with `at23_family_alt hP`. So in the caller `linkN_of_boundAtTwoThree_slot`, the hypothesis `h23` gives only the numbers $\varepsilon_1$ and $K$. Its bound `hK` and the largeness hypothesis are not used ([LinkNFam.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L59)). The cut for $x \le x_1$ is an unused placeholder.
