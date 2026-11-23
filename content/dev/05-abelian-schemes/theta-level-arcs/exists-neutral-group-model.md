---
id: exists-neutral-group-model
title: A smooth connected group model of an abelian variety
kind: theorem
decl: GlobalTheory.SS.exists_neutral_group_model
module: Development.AbelianVarietyTheory.Proofs.DegenerationProofs.ExistsNeutralGroupModel
covers: 490
status: drafted
drafted_by: writer@claude
---
This theorem builds a smooth group scheme over a strictly Henselian discrete valuation ring whose generic fibre is a given abelian variety. Each rational point, after multiplication by a fixed integer $c$, extends to an integral point of this group. The argument of [the step on every character](/step/every-character/) uses it through semi-abelian reduction and good reduction. The construction follows the steps of the Néron model: a weak Néron model, a birational group law, a strict model, and then a group scheme.

## Statement

Let $R$ be a local domain with fraction field $K$. Assume `SH R K`: $R$ is a discrete valuation ring, Henselian, with algebraically closed residue field, and $K = \operatorname{Frac} R$. Let $A$ be a commutative group object over $\operatorname{Spec} K$ that is an abelian scheme (smooth, proper, geometrically connected, commutative) and is projective (it has a very ample line bundle).

Then there are a model $G$ of $A$ over $R$ and a group structure on $G$ such that:

- $G$ is commutative, smooth, separated, quasi-compact and geometrically connected (`SmConn`);
- the isomorphism of the generic fibre of $G$ with $A$ is a homomorphism of monoids;
- there is $c \ge 1$ such that for each $K$-point $a$ of $A$, the point $a^c$ extends to an $R$-point of $G$.

A model is a smooth, separated, quasi-compact scheme over $\operatorname{Spec} R$ with an isomorphism of its generic fibre with $A$.

## Proof

1. `exists_weak_neron_model` gives finitely many irreducible models $M_1, \dots, M_n$ that together have the extension property of a weak Néron model. The residue field is perfect because it is algebraically closed.
2. `exists_weakNeronModel_birational_groupLaw` gives one model $N$ with a birational group law, and $c \ge 1$ such that translation by $a^c$ is an isomorphism at some point of the special fibre of $N$, for each $K$-point $a$.
3. `exists_strict_model_of_birational` gives a strict model $N'$ with an open immersion $N' \to N$.
4. `exists_grpObj_of_strictBirationalLaw` gives the group scheme $G$. Each $a$ whose translation on $N'$ is an isomorphism at a point of the special fibre extends to an $R$-point of $G$.
5. The calculus `modelMapGenericallyOpenImmersion_calculus` (open immersions, composition and inverses) moves the property of step 2 from $N$ to $N'$. Step 4 then applies to $a^c$.

For the classical construction, see Bosch, Lütkebohmert and Raynaud, *Néron Models* (Springer, 1990), Chapters 3 to 5. I do not claim that the Lean statement is a theorem of that book word for word.

## In the Lean code

The theorem is in [ExistsNeutralGroupModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsNeutralGroupModel.lean#L18). The definitions `Model`, `GenIso`, `BirLaw`, `Strict`, `SH` and `SmConn` are in [OfDerivationFnOn.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/OfDerivationFnOn.lean#L11). The four construction lemmas are second names in `*Statement.lean` files of the same folder. I have not unfolded their proofs.

The three parts of `SH` enter the proof as local instances, so no hypothesis is unused. The name says "neutral", but the statement does not mention a neutral component: $G$ is geometrically connected. The second name `exists_neutral_group_model'` only calls this theorem.
