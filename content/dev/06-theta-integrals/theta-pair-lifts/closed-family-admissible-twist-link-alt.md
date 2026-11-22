---
id: closed-family-admissible-twist-link-alt
title: The valuation bound on period columns, closed on the design class
kind: theorem
decl: GlobalTheory.Top.closed_family_admissible_twist_link_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ClosedFamilyAdmissibleTwistLink
covers: 1823
status: drafted
drafted_by: writer@claude
---
This theorem proves that the valuation bound `adm2` holds, eventually in $x$, on the families of the class $\mathcal{D}(\mathcal{A})$ (the Lean `D3 3 𝒜`), in the sense of [`Closed`](/step/closed-def/). The theorem [`shape_closed_link_n_of_green`](/entry/shape-closed-link-n-of-green/) uses the result as one input of the division kernel bound that gives `LinkDIVt`. Below this theorem are 1,823 declarations of the proof. Almost all of them (1,751) are below [`closed_servF_of_servT_of_dGamSize`](/entry/closed-serv-f-of-serv-t-of-d-gam-size/).

## Statement

Let $\mathcal{A}$ be a family class with a twist selection. Assume seven bounds, each closed on $\mathcal{D}(\mathcal{A})$ and each eventual in $x$, for $x > x_1$ and each $i \in I_x$:

- `Conclusion6` and `PeriodClassSumWeyl` for the datum $D(x,i)$, and `TwistedPointIntegral` and `TwistedPeriodAdmissible` for its twist;
- `Conclusion5Sharp` and `TwistedColumnBoundAtT` at each word $u$;
- a constant $C_1$ with `UsedTuplesBoundByConstant` and `familySizeBoundAtTypePrime`;

and the statement `SelectionServed` for the selection. Then, closed on $\mathcal{D}(\mathcal{A})$, there is $x_0$ such that `adm2` holds for $(D(x,i), L(x,i))$ for all $x \ge x_0$ with $x > x_1$ and all $i$.

The bound `adm2 D L` says this. Let $u$ be a word, $w$ a place, $\varphi$ a vector in the lattice $L.\mathrm{NuLat}(u)$, and $F$ a vector of the space `Mtilde` at $w$ that lies in `V0`. Then the period column value `perCol` of $(u, \varphi, F)$ is the image of an element $y$ of the number field `LL`, and either $y = 0$ or the valuation of $y$ at $w$ is at least $\lfloor \mathrm{ur}(D, w, L.\mathrm{sg}(u,w)) \rfloor$.

## Proof

The proof fills the eight fields of the structure `Adm2InU` for the class $\mathcal{D}(\mathcal{A})$ and applies `admissible_family_of_inclusion`. That lemma gives `adm2` and a second bound `adm12`; the proof keeps `adm2`. Six fields are the hypotheses. The other two are proved here.

1. `serv`, the closed bound `ServF`: from [`closed_servF_of_servT_of_dGamSize`](/entry/closed-serv-f-of-serv-t-of-d-gam-size/), applied to `SelectionServed` and to `DGamSize`. `DGamSize` holds on $\mathcal{D}(\mathcal{A})$ by the definition of the class.
2. `dgt`, the bound `LevelPrimeCoprimeStabiliser`: from `closed_eventually_levelPrimeCoprimeStabiliser` with $C_0 = 3$.

## In the Lean code

The theorem is in [ClosedFamilyAdmissibleTwistLink.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ClosedFamilyAdmissibleTwistLink.lean#L12). The lemmas it calls:

- `Adm2InU` and `admissible_family_of_inclusion` in [AdmissibleAtGeneratorPlaces.lean](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleAtGeneratorPlaces.lean#L302);
- `closed_servF_of_servT_of_dGamSize` in [GServT.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GServT.lean#L31);
- `closed_eventually_levelPrimeCoprimeStabiliser` in `Formalism/SharpRestriction/GlobalSchurBounds/PlugDgt.lean`.

`adm2` is in [LocalQuadraticParts.lean](lean:Formalism/SharpRestriction/Divisibility/LocalQuadraticParts.lean#L206). Other files define different predicates named `adm2`; for example the `Adm2F` of [`linkG_concrete5`](/entry/link-g-concrete5/) uses `AuxBlock8.adm2`. We have not unfolded the seven hypotheses or `adm12`. The second conclusion `adm12` is proved and then dropped.
