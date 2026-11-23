---
title: Classes killed on an étale neighbourhood
decls:
  - UpperTheory.Cb.MorphismCompositionLaws.contOf
  - UpperTheory.Cb.MorphismCompositionLaws.sys_of
  - UpperTheory.Cb.affineGeometricCase_of_obstructionExact_natural
  - UpperTheory.Cb.etale_cohomology_class_killed_on_neighborhood
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Classes killed on an étale neighbourhood

A class in [[étale cohomology|7YX76G0838]] that is zero at each strictly henselian point is zero on an étale neighbourhood of each point. This is the usual way to pass from stalks to a covering. This section proves it for the relative cohomology of a proper scheme and a closed subscheme. The tools are the strict henselization as a filtered colimit of étale algebras, the continuity of étale cohomology under such colimits, and the four lemma. The result is one input to the finiteness of the cohomology of proper schemes over an algebraically closed field.

The étale cohomology in this section is the one of the code. A scheme $X$ gives a space $\mathrm{sch}(X)$, and $H^n(X, \mathbb{Z}/q(i))$ is the cohomology of this space with coefficients in the twisted sheaf $\mathbb{Z}/q(i)$. A morphism of schemes gives a pullback map. The code takes the expected properties of this theory as a list of hypotheses, which we call the *axioms*. Two of them are used in this section: Čech descent along smooth surjective maps, and continuity for affine schemes, which we state below.

**Definition (Relative cohomology).** Let $f : X' \to X$ be a morphism of schemes. The *relative cohomology* $H^n(X, X'; \mathbb{Z}/q(i))$ is the cohomology of the mapping cone of $\mathrm{sch}(f)$. It sits in a long exact sequence
$$
\begin{aligned}
H^{n-1}(X) \to H^{n-1}(X') &\to H^n(X, X') \\
&\to H^n(X) \to H^n(X'),
\end{aligned}
$$
where all groups have coefficients $\mathbb{Z}/q(i)$. The sequence is natural in the pair.

We fix the setting of the section. Let $k$ be a field and $q \geq 1$ an integer that is a unit in $k$. Let $B$ be a scheme over $k$, let $\iota : W \to B$ be a closed immersion, and let $p : Y \to B$ be proper. For an étale $B$-scheme $U$ write $Y_U = Y \times_B U$ and $W_U = Y_U \times_B W$, a closed subscheme of $Y_U$. A class $z \in H^m(Y_U, W_U; \mathbb{Z}/q(i))$ restricts along each étale map $U' \to U$ over $B$, and along each morphism $t : \mathrm{Spec}\, A \to U$, where we replace $U$ by $\mathrm{Spec}\, A$ in the definition of $Y_U$ and $W_U$.

**Definition (Continuity).** Let $(D_j)$ be a filtered system of rings with colimit $D$, and let $(E_j)$ be the spaces of a compatible system of schemes over $\mathrm{Spec}\, D_j$, with limit $E$. We say that the cohomology in degree $n$ is *continuous* for the system if each class in $H^n(E)$ comes from some $H^n(E_j)$, and each class in $H^n(E_j)$ that is zero in $H^n(E)$ is zero in some $H^n(E_k)$ with $j \to k$. The axiom of *continuity for affine schemes* asks this for $E_j = \mathrm{Spec}\, D_j$, when $q$ is a unit in the rings.

So continuity says that $H^n(E)$ is the colimit of the $H^n(E_j)$. For a classical statement see J. S. Milne, *Étale Cohomology*, Chapter III, §1.

**Lemma (Continuity after base change).** Let $R$ be a ring in which $q$ is a unit, let $(D_j)$ be a filtered system of $R$-algebras with colimit $D$, and let $X \to \mathrm{Spec}\, R$ be quasi-compact and separated. Assume the axioms of Čech descent and of continuity for affine schemes. Then the cohomology of the system $X \times_R \mathrm{Spec}\, D_j$, with limit $X \times_R \mathrm{Spec}\, D$, is continuous in each degree.

Lean: `UpperTheory.Cb.MorphismCompositionLaws.contOf`.

*Proof.* This is a theorem of the code on continuity after base change, applied to $X$, $R$ and the system $(D_j)$. We read that theorem only as a statement. The classical proof covers $X$ by finitely many affine open sets, uses that their intersections are again affine because $X$ is separated, and passes from the affine case to $X$ by Čech descent. $\square$

**Definition (Neighbourhood system).** Let $U$ be étale over $B$ and $u \in U$. A *neighbourhood system* for $(U, u)$ in degree $m$ is the following data. A filtered category $J$, étale $B$-schemes $V_j$ with maps $a_j : V_j \to U$ whose images contain $u$, and transition maps $V_k \to V_j$ for $j \to k$ over $U$. A strictly henselian ring $A$ and a map $t : \mathrm{Spec}\, A \to U$, with compatible maps $Y_A \to Y_{V_j}$ and $W_A \to W_{V_j}$ over $U$. The three conditions are that the cohomology of $(Y_{V_j})$ is continuous at $Y_A$ for injectivity in degree $m$ and for surjectivity in degree $m - 1$, and that the cohomology of $(W_{V_j})$ is continuous at $W_A$ for injectivity in degree $m - 1$.

**Lemma (Affine neighbourhood system).** Assume the two axioms. Let $U$ be étale over $B$ with $U \cong \mathrm{Spec}\, R$ and $q$ a unit in $R$, and let $u \in U$. Then for each $m$ there is a neighbourhood system for $(U, u)$ in degree $m$.

Lean: `UpperTheory.Cb.MorphismCompositionLaws.sys_of`.

*Proof.* Let $\mathfrak{p}$ be the prime of $R$ at $u$. The strict henselization $A$ of $R$ at $\mathfrak{p}$ is a filtered colimit of étale $R$-algebras $D_j$, each with a prime over $\mathfrak{p}$ (Milne, *Étale Cohomology*, Chapter I, §4). Let $V_j = \mathrm{Spec}\, D_j$. It is étale over $U$, so it is étale over $B$, and its image contains $u$. Let $t : \mathrm{Spec}\, A \to U$ be the natural map. Now $Y_U \to U$ is proper, so it is quasi-compact and separated, and $W_U \to U$ is a closed subscheme of it, so it has the same properties. The continuity lemma for $X = Y_U$ in degrees $m$ and $m - 1$, and for $X = W_U$ in degree $m - 1$, gives the three conditions. $\square$

**Theorem (Affine geometric case).** Assume the axioms. Let $k$, $q$, $B$, $W$, $Y$ be as in the setting, let $U$ be étale over $B$ with $U \cong \mathrm{Spec}\, R$, and let $u \in U$. Then for each $m$ there is a neighbourhood system for $(U, u)$ in degree $m$.

Lean: `UpperTheory.Cb.affineGeometricCase_of_obstructionExact_natural`.

*Proof.* The ring $R$ is a $k$-algebra through $U \to B \to \mathrm{Spec}\, k$, and $q$ is a unit in $k$, so $q$ is a unit in $R$. This is the last lemma applied to $U \cong \mathrm{Spec}\, R$. $\square$

**Theorem (Killing on a neighbourhood).** Assume the axioms. Let $k$ be a field, $q$ a unit in $k$, and $B$, $\iota : W \to B$, $p : Y \to B$ as in the setting. Let $U$ be étale over $B$ and $z \in H^m(Y_U, W_U; \mathbb{Z}/q(i))$. Suppose that the restriction of $z$ along each $\mathrm{Spec}\, A \to U$ with $A$ strictly henselian is zero. Then each $u \in U$ lies in the image of an étale map $U' \to U$ over $B$ such that the restriction of $z$ to $(Y_{U'}, W_{U'})$ is zero.

Lean: `UpperTheory.Cb.etale_cohomology_class_killed_on_neighborhood`.

*Proof.* We give the proof in three steps.

First, there is a neighbourhood system for $(U, u)$ in degree $m$. Take an affine open neighbourhood $U_0 \subseteq U$ of $u$. The last theorem gives a system for $(U_0, u)$. Compose its maps $a_j$ with the inclusion $U_0 \to U$. This gives a system for $(U, u)$.

Second, let $(V_j)$, $A$ and $t$ be the system. The long exact sequences of the pairs $(Y_{V_j}, W_{V_j})$ form a filtered system of exact sequences, and filtered colimits of abelian groups are exact. So the colimit of the sequences is exact, and it maps to the long exact sequence of $(Y_A, W_A)$. In the diagram
$$
\begin{aligned}
\varinjlim H^{m-1}(Y_{V_j}) \to \varinjlim H^{m-1}(W_{V_j}) &\to \varinjlim H^m(Y_{V_j}, W_{V_j}) \to \varinjlim H^m(Y_{V_j}) \\
H^{m-1}(Y_A) \to H^{m-1}(W_A) &\to H^m(Y_A, W_A) \to H^m(Y_A)
\end{aligned}
$$
the first vertical map is surjective, and the second and fourth vertical maps are injective, by the three conditions. By the four lemma, the third vertical map is injective.

Third, the image of $z$ in $H^m(Y_A, W_A)$ is zero by hypothesis, since $A$ is strictly henselian. By the second step the image of $z$ in the colimit is zero. So there is a $j$ such that the restriction of $z$ to $(Y_{V_j}, W_{V_j})$ is zero, and $U' = V_j$ works. $\square$

**Remark.** The affine geometric case is stated in the code with two hypotheses: the exactness of an obstruction sequence and its naturality. The proof introduces both and does not use them. The theorem of killing on a neighbourhood is built from a lemma that also takes these two hypotheses and ignores them. Both hypotheses are supplied by other theorems of the code, so the result is unconditional apart from the axioms. The names of the two lemmas `contOf` and `sys_of` are in a namespace called `MorphismCompositionLaws`, and the continuity theorem that `contOf` applies is called `intersectionNumber_baseChange` in [FinCont.lean](lean:Development/EtaleCohomology/KummerTheory/FinCont.lean#L51). The strict henselization lemma has the same misleading name in [FinSHen.lean](lean:Development/EtaleCohomology/KummerTheory/FinSHen.lean#L6). None of these names describes the statement.

**Remark.** The four lemma and the exactness of filtered colimits are in the step that the code calls `Pack`, which we read as a statement. The theorem is used to show that a class of the relative cohomology that vanishes at all strictly henselian points vanishes on an étale covering, in the proof of the finiteness theorem of [the étale cohomology chapter](/entry/etale-topology-top/).
