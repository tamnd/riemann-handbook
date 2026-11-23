---
id: div-ex-prov
title: Divisor data exist when the object slot asks only for the eigenvalue tie
kind: theorem
decl: GlobalTheory.Mem.Top.DivRec.divEx_prov
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.TupPinsOfMuIsW
covers: 338
status: drafted
drafted_by: writer@claude
---
This theorem proves the divisor step `DivEx` for every system of slots whose object component is `OX anyGeometry`. Its only caller is [`divEx_of_ox`](/entry/div-ex-of-ox/), which adds three hypotheses that it does not use. From there the result goes through `divEx_geoCl` into the [membership theorem](/entry/member-e-closing-alt-alt/). The construction is in [`exists_divT`](/entry/exists-div-t/); this theorem only adds the object condition.

## Statement

A system of slots $\mathcal S$ has four components: a position $R_x$, a norm condition $N_x$, a side position $S_x$ and an object component $O_x$. For a pinned column datum $w$, a later stage $Z$ of $w$ and a level-four record $l$ (`Lv4`), `DivEx` $\mathcal S$ asks, eventually in the context, for a divisor datum $Y$ over the datum $D = w.D(Z)$ such that:

1. $Y$ is tied to the character choice of $l$ (`DivT`);
2. the hermitian lattices of $Y$ are tied to the reading of $l$ (`MjAre`);
3. $\kappa_R(\sigma) = \kappa^\sharp$ for all $\sigma$;
4. for each object $O$ with $O.X = Y$, base row side $l.p_0$ and rows record equal to that of $l$, the type $O_x(\ldots, O, t)$ is inhabited.

**Theorem.** If $O_x = $ `OX anyGeometry`, then `DivEx` $\mathcal S$ holds.

`OX Γ` asks for a record `OAt Γ t X` with two fields: the geometric predicate $\Gamma$ at $X$, and `LamAre`, the eigenvalue tie of $X$ to the reading. Here $\Gamma = $ `anyGeometry` is the constant predicate `True`. So condition 4 only asks that $Y$ satisfies `LamAre`.

## Proof

`StepW.of_all` reduces the claim to one column datum. A pin of $w$ is taken from `Pinned` by `Nonempty.some`. Then [`exists_divT`](/entry/exists-div-t/) gives $Y$ with conditions 1 to 3 and `LamAre` for the reading of $l$. For condition 4, the geometric field is `trivial`. `lamAre_heq` moves `LamAre` from the rows record of $l$ to the given record $t$, by the equalities $O.p_0 = l.p_0$ and $t \simeq l$. The rest is bookkeeping.

## In the Lean code

The theorem is in [TupPinsOfMuIsW.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TupPinsOfMuIsW.lean#L204). It calls `StepW.of_all`, `exists_divT` and `lamAre_heq`. `DivEx` is defined in [NonzeroPlacesOverPrimes.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NonzeroPlacesOverPrimes.lean#L183), and `OX` and `anyGeometry` in [OverIx.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L49).

The hypotheses of `StepW.of_all` (the context is over the base, and `Forced`) are not used. The components $R_x$, $N_x$, $S_x$ of $\mathcal S$ are arbitrary. The parent `divEx_of_ox` takes `RayField`, `PrincipalIdealSt` and `CMCurveGoodOutsidePrimeSt` and discards them.
