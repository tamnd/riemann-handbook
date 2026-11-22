---
id: isog-rep-exists-rep
title: Construction of the scheme of isogenies of type T_j
kind: theorem
decl: GlobalTheory.UPel.HT.ES.IsogRep.exists_rep
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HarrisTaylorTypeTjIsogeniesRepresentable
covers: 478
status: drafted
drafted_by: writer@claude
---
This lemma builds a finite étale scheme $Y$ over $S$ that classifies the $c$-isogenies of type $T_j$ out of a Harris-Taylor object $o$ over $S$. Its statement is the statement of [isogenies of type T_j are represented by a finite étale scheme](/entry/harris-taylor-type-tj-isogenies-representable/), which is a second name for it. The idea: first classify all quasi-isogenies of degree $c$ of the abelian scheme, then cut out the open and closed part where the target is again an object and the isogeny has type $T_j$.

## Statement

As in [the statement entry](/entry/harris-taylor-type-tj-isogenies-representable/), with the same notation and hypotheses.

## Proof

Let $A$ be the abelian scheme of $o$. Since $c = p^e$ and $p$ is a unit in $R$, $c$ is a unit on $S$ (`isUnit_pow`).

1. **All quasi-isogenies.** [The finite étale scheme of quasi-isogenies](/entry/isogeny-representable-finite-etale/) gives a finite étale $Z \to S$ and, over $Z$, an abelian scheme $B$ with $\psi \colon A_Z \to B$ and $\psi' \colon B \to A_Z$, $\psi'\psi = c$ and $\psi\psi' = c$. The pair is universal for such pairs out of pullbacks of $A$. Pull $o$ back to $o_Z$ over $Z$ (`exists_pull`).
2. **Three clopen loci.** Three lemmas give open and closed subsets of $Z$: $W_1$, where $\ker\psi$ is stable under $O$ (`T.exists_clopen_kernelStable_harrisTaylor`); $W_2$, where the polarization descends along $\psi$ (`T.harrisTaylor_pullback_kernel_locus_isClopen`); and $W_3$, where $\psi$ has type $T_j$ (`T.exists_clopen_locus_of_annihilator`). Each locus is characterized by the maps $T \to Z$ whose image lies in it.
3. **The subscheme.** `LevCover.exists_sub` gives the open and closed subscheme $Y$ of $Z$ on $W_1 \cap W_2 \cap W_3$. It is finite étale over $S$, and a map $T \to Z$ factors through $Y$ if and only if its image lies in the three loci.
4. **The object $o'$.** Over $Y$, let $o_0$ be the pullback of $o$ and $B_0$ the pullback of $B$ (`T.quasiInverseIsogenyPair_baseChange_grpPullback`). `exists_obj` makes $B_0$ an object $o'$: it descends the $O$-action, the polarization bundle and the Lie condition along $\psi$, and sets $\eta' = \psi \circ \eta$. The result is a $c$-isogeny $\chi \colon A_0 \to A'$. It has type $T_j$ since $Y$ lies in $W_3$ (`T.harrisTaylorType_iff_pulledBack_identity`).
5. **Universality.** Given $x \colon T \to S$, $o_1$ and a $c$-isogeny $\psi_1$ of type $T_j$, the universal property of $Z$ gives a unique $z \colon T \to Z$. The three conditions on $\psi_1$ put the image of $z$ in $W_1 \cap W_2 \cap W_3$, so $z$ factors through $Y$. `T.exists_objMap_of_p_isogeny_pullback` gives the map $o_1' \to o'$. Uniqueness comes from the uniqueness of $z$, since $Y \to Z$ is a monomorphism.

The rest is bookkeeping with the maps of objects (`exists_comp`, `exists_factor`).

## In the Lean code

The lemma is in [HarrisTaylorTypeTjIsogeniesRepresentable.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorTypeTjIsogeniesRepresentable.lean#L108). The helper `exists_obj` is at [L82](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorTypeTjIsogeniesRepresentable.lean#L82); it calls eight lemmas, among them `T.exists_orderAction_descent_along_isogeny`, `T.exists_polarization_descent_of_quasi_isogeny` and `T.harrisTaylor_lie_of_quasiInverseIsogeny`, which we have not opened. `exists_factor` uses $N \geq 3$ through `T.harrisTaylor_pullback_abelian_map_unique_of_base_eq`.

The proof introduces four hypotheses as `_` and never refers to them: $w$ maximal, $u_r \subseteq w$, $j \leq n$ and $m = 1$. It also drops the clause "$e > 0$ if $j > 0$" at once. So the same proof works without these hypotheses. The clopen lemmas take any $r$, $w$ and $j$.
