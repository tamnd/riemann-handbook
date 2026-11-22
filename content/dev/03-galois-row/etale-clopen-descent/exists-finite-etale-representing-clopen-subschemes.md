---
id: exists-finite-etale-representing-clopen-subschemes
title: The finite étale scheme of clopen subsets of a finite étale cover
kind: theorem
decl: UpperTheory.Cb.exists_finite_etale_representing_clopen_subschemes
module: Development.AutomorphicArithmetic.Foundations.EtaleClopenDescent.ExistsFiniteEtaleRepresentingClopenSubschemes
covers: 353
status: drafted
drafted_by: writer@claude
---
For a finite étale cover $G \to S$, this theorem gives a finite étale $S$-scheme that parametrizes the clopen subsets of the base changes of $G$. It is the first step of [the subgroup lemma](/entry/sub-rep-core/): there $G$ is a finite étale group scheme, and the lemma cuts the locus of subgroups out of the scheme $Y$ that this theorem gives.

## Statement

Let $S$ be a locally noetherian scheme, and let $G \to S$ be finite and étale. For an $S$-scheme $T$, write $G_T = T \times_S G$. Then there are an $S$-scheme $Y$ and a subset $U \subseteq Y \times_S G$ such that:

1. $Y \to S$ is finite and étale;
2. $U$ is open and closed;
3. for each $S$-scheme $T$ and each open and closed $V \subseteq G_T$, there is exactly one $S$-morphism $y \colon T \to Y$ with $(y \times \mathrm{id}_G)^{-1}(U) = V$.

So $Y$ represents the functor $T \mapsto \{\text{clopen subsets of } G_T\}$, and $U$ is the universal clopen subset.

## Proof

1. **Fixed rank.** For each $r \ge 0$, `exists_clopRepOfRank_of_locallyNoetherian` represents the clopen $V$ with $V \to T$ of constant degree $r$. It takes the Hilbert scheme $H_r$ of closed subschemes of $G$ that are finite flat of degree $r$ over the base (`GlobalTheory.T.hilbertScheme_finite_locallyFree_representable_proper`). The universal subscheme is a flat and étale closed immersion, so it is also open. This step uses that $S$ is locally noetherian.
2. **All ranks.** `exists_clopRep_of_clopRepOfRank` takes the disjoint union $Y = \coprod_r H_r$. A clopen $V \subseteq G_T$ is finite étale over $T$, so its degree is locally constant. On the open pieces of $T$ where the degree is constant, the maps to the $H_r$ glue to one map $T \to Y$.
3. **$Y$ is finite étale.** The private lemma `finite_etale_of_rep` in the same file splits $S$ into the open pieces $W_n$ where $G$ has degree $n$. On $W_n$ it calls `clopRep_finite_etale_of_constant_rank`. That lemma takes a finite étale surjective $S' \to W_n$ over which $G$ becomes $n$ disjoint copies of the base (`exists_isSplitOfRank_pullback`). Over $S'$, `exists_clopRep_of_isSplitOfRank` builds a finite étale representing object by induction on $n$. By uniqueness of representing objects (`clopRep_unique`), it is the base change of $Y$. Finiteness and étaleness descend along $S' \to W_n$, and they are local on $S$.

## In the Lean code

The theorem is in [ExistsFiniteEtaleRepresentingClopenSubschemes.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/ExistsFiniteEtaleRepresentingClopenSubschemes.lean#L51). Its last two clauses are the predicate `RepresentationRank.Rep` of [RepOfRank.lean](lean:Development/AutomorphicArithmetic/RepresentationRank/RepOfRank.lean#L12), written out. The product $Y \otimes G$ is the fibre product over $S$. The name says "clopen subschemes"; the statement uses open subsets that are closed, which is the same data.

A clopen subset of $G_T$ is the same as a $T$-morphism $G_T \to T \sqcup T$, so $Y$ is the Weil restriction of $S \sqcup S$ along $G \to S$. The proof that we read does not use this: it goes through the Hilbert scheme and needs $S$ to be locally noetherian.
