---
title: Clopen subsets of a finite étale scheme
decls:
  - UpperTheory.Cb.exists_finite_etale_representing_clopen_subschemes
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Clopen subsets of a finite étale scheme

Let $G \to S$ be finite étale. An open and closed subset of $G$ is a finite étale scheme over $S$ again, and such subsets move well under base change. This section shows that they are the points of one finite étale $S$-scheme $Y$. The next two sections apply this to subgroups of the torsion of an abelian scheme and to kernels of isogenies.

Recall that a morphism is [finite étale](/learn/geometry/#schemes-and-varieties) if it is finite and étale, and that a subset of a topological space is *clopen* if it is open and closed ([[clopen set|DQ4E55T3BW]]). For schemes $T$ and $G$ over $S$ we write $G_T = T \times_S G$, and for a morphism $y : T \to Y$ of $S$-schemes we write $y \times 1 : G_T \to G_Y$.

**Definition (Clopen functor).** Let $S$ be a scheme and $G \to S$ a scheme over $S$. For an $S$-scheme $T$ let $\mathrm{Clop}_G(T)$ be the set of clopen subsets of $G_T$. A morphism $T' \to T$ of $S$-schemes gives the map $\mathrm{Clop}_G(T) \to \mathrm{Clop}_G(T')$ that takes $V$ to its inverse image in $G_{T'}$. A pair $(Y, U)$ of an $S$-scheme $Y$ and $U \in \mathrm{Clop}_G(Y)$ *represents* $\mathrm{Clop}_G$ if for each $S$-scheme $T$ and each $V \in \mathrm{Clop}_G(T)$ there is exactly one $S$-morphism $y : T \to Y$ with $(y \times 1)^{-1}(U) = V$.

So $Y$ is the scheme of clopen subsets of $G$, and $U$ is the universal clopen subset. The pair is unique up to a unique isomorphism, as for each representable functor.

**Example.** Let $G = S \sqcup S$ be two copies of $S$. A clopen subset of $T$ is the same as an $S$-morphism $T \to S \sqcup S$: the subset is the inverse image of the first copy. A clopen subset of $G_T = T \sqcup T$ is a pair of clopen subsets of $T$. So $\mathrm{Clop}_G$ is represented by $(S \sqcup S) \times_S (S \sqcup S)$, which is four copies of $S$. In the same way, if $G$ is $n$ copies of $S$, then $Y$ is $2^n$ copies of $S$. It is finite étale over $S$ of degree $2^n$.

The example is the general case after an étale base change, because each finite étale scheme is split after a surjective étale base change. The theorem below is proved in this way, with one more input: for a fixed degree, a Hilbert scheme gives the representing scheme directly.

**Definition (Rank).** Let $V \to T$ be finite and flat, with $T$ locally noetherian. Then $V$ is locally free over $T$, and for $t \in T$ the *rank* of $V$ at $t$ is the rank of the free module of $V$ at $t$. It is a locally constant function of $t$. We say that $(Y, U)$ represents $\mathrm{Clop}_G$ *in rank* $r$ if $U$ has rank $r$ at each point of $Y$, and the condition of the last definition holds for all $V$ of rank $r$ at each point of $T$.

**Theorem (Scheme of clopen subsets).** Let $S$ be a locally noetherian scheme and $G \to S$ finite étale. Then there is a pair $(Y, U)$ that represents $\mathrm{Clop}_G$, with $Y \to S$ finite étale.

Lean: `UpperTheory.Cb.exists_finite_etale_representing_clopen_subschemes`.

*Proof.* We give the proof in three steps.

First, fix $r \geq 0$. The Hilbert scheme of finite flat closed subschemes of rank $r$ of $G$ gives a proper $S$-scheme $H_r$ and a closed subscheme $U_r \subseteq G_{H_r}$, finite and flat of rank $r$ over $H_r$, with this property: each closed subscheme $V \subseteq G_T$ that is finite and flat of rank $r$ over $T$ is the inverse image of $U_r$ along exactly one $S$-morphism $T \to H_r$. The code takes this as a theorem about Hilbert schemes. Now $G_{H_r} \to H_r$ is étale and $U_r \to H_r$ is flat, so the closed immersion $U_r \to G_{H_r}$ is flat. A closed immersion that is flat and locally of finite presentation is also an open immersion, so $U_r$ is clopen. Conversely, a clopen subset $V$ of $G_T$, with its open subscheme structure, is a closed subscheme that is finite étale over $T$. So $(H_r, U_r)$ represents $\mathrm{Clop}_G$ in rank $r$.

Second, let $Y'$ be the disjoint union of the $H_r$ over all $r \geq 0$, and $U'$ the union of the $U_r$. Let $V \in \mathrm{Clop}_G(T)$. The rank of $V$ is locally constant on $T$, so $T$ is the disjoint union of the clopen sets $T_r$ where $V$ has rank $r$. On $T_r$ the first step gives a unique morphism to $H_r$, and these glue to a unique morphism $T \to Y'$. So $(Y', U')$ represents $\mathrm{Clop}_G$.

Third, $Y' \to S$ is finite étale. Both properties are local on $S$. The rank of $G$ is locally constant on $S$, so $S$ is the union of the open sets $S_n$ where $G$ has rank $n$, and it suffices to work over one $S_n$. The base change of $(Y', U')$ to $S_n$ represents $\mathrm{Clop}$ of $G_{S_n}$, because representability is stable under base change. There is a surjective étale $S' \to S_n$ over which $G$ becomes $n$ copies of $S'$. By the example, $\mathrm{Clop}$ is represented over $S'$ by $2^n$ copies of $S'$. Two representing pairs are isomorphic, so $Y' \times_S S'$ is $2^n$ copies of $S'$, and it is finite étale over $S'$. Finiteness and étaleness descend along the surjective étale map $S' \to S_n$. So $Y' \to S$ is finite étale. $\square$

**Remark.** In the classical construction, $Y$ is the Weil restriction along $G \to S$ of the $G$-scheme $G \sqcup G$: an $S$-morphism $T \to Y$ is a $G$-morphism $G_T \to G \sqcup G$, and that is a clopen subset of $G_T$. Weil restriction along a finite locally free morphism exists for quasi-projective schemes (S. Bosch, W. Lütkebohmert and M. Raynaud, *Néron Models*, §7.6). The Lean proof uses a Hilbert scheme instead, and it needs $S$ locally noetherian for that step.

**Remark.** The Hilbert scheme enters as the statement [HilbertSchemeFiniteLocallyFreeRepresentablePropeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HilbertSchemeFiniteLocallyFreeRepresentablePropeStatement.lean#L6), which is proved by another lemma of the code that we have not opened. The descent in the third step is a lemma for finite maps along fpqc covers and a lemma for properties that descend along étale covers. We have read the statements of these lemmas as they are used, not their proofs. The predicate "represents" is written out in the statement of the theorem; its name in the code is `Rep`, in [RepOfRank.lean](lean:Development/AutomorphicArithmetic/RepresentationRank/RepOfRank.lean#L12).
