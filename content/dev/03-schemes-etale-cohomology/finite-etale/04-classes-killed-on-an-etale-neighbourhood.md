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

A class in [[étale cohomology|7YX76G0838]] that is zero at each strictly henselian point is zero on an étale neighbourhood of each point. This is the usual way to pass from stalks to a covering. This section proves it for the relative cohomology of a proper scheme and a closed subscheme. The tools are the strict henselization as a filtered colimit of étale algebras, the continuity of étale cohomology under such colimits, and the four lemma. The main result is Theorem 5.4.7. It is used to show that a relative class that vanishes at all strictly henselian points vanishes on an étale covering, in the proof of [the finiteness of étale cohomology](/entry/etale-topology-top/).

We work with an axiomatic model of étale cohomology. A scheme $X$ gives a space $\mathrm{sch}(X)$, and $H^n(X, \mathbb{Z}/q(i))$ is the cohomology of this space with coefficients in the twisted sheaf $\mathbb{Z}/q(i)$, for an integer $q \geq 1$. A morphism of schemes gives a pullback map. We assume a list of the expected properties of this theory, which we call the *axioms*. Two of them are used in this section: Čech descent along smooth surjective maps, and continuity for affine schemes, which we state below.

**Definition 5.4.1 (Relative cohomology).** Let $f : X' \to X$ be a morphism of schemes. The *relative cohomology* $H^n(X, X'; \mathbb{Z}/q(i))$ is the cohomology of the mapping cone of $\mathrm{sch}(f)$. It sits in a long exact sequence
$$
\begin{aligned}
H^{n-1}(X) \to H^{n-1}(X') &\to H^n(X, X') \\
&\to H^n(X) \to H^n(X'),
\end{aligned}
$$
where all groups have coefficients $\mathbb{Z}/q(i)$. The sequence is natural in the pair.

We fix the setting of the section. Let $k$ be a field and $q \geq 1$ an integer that is a unit in $k$. Let $B$ be a scheme over $k$, let $\iota : W \to B$ be a closed immersion, and let $p : Y \to B$ be proper. For an étale $B$-scheme $U$ write $Y_U = Y \times_B U$ and $W_U = Y_U \times_B W$, a closed subscheme of $Y_U$. A class $z \in H^m(Y_U, W_U; \mathbb{Z}/q(i))$ restricts along each étale map $U' \to U$ over $B$, and along each morphism $t : \mathrm{Spec}\, A \to U$, where we replace $U$ by $\mathrm{Spec}\, A$ in the definition of $Y_U$ and $W_U$.

**Definition 5.4.2 (Continuity).** Let $(D_j)$ be a filtered system of rings with colimit $D$, and let $(E_j)$ be the spaces of a compatible system of schemes over $\mathrm{Spec}\, D_j$, with limit $E$. We say that the cohomology in degree $n$ is *continuous* for the system if each class in $H^n(E)$ comes from some $H^n(E_j)$, and each class in $H^n(E_j)$ that is zero in $H^n(E)$ is zero in some $H^n(E_k)$ with $j \to k$. The axiom of *continuity for affine schemes* asks this for $E_j = \mathrm{Spec}\, D_j$, when $q$ is a unit in the rings.

So continuity says that $H^n(E)$ is the colimit of the $H^n(E_j)$. For a classical statement see J. S. Milne, *Étale Cohomology*, Chapter III, §1.

**Lemma 5.4.3 (Continuity after base change).** Let $R$ be a ring in which $q$ is a unit, let $(D_j)$ be a filtered system of $R$-algebras with colimit $D$, and let $X \to \mathrm{Spec}\, R$ be quasi-compact and separated. Assume the axioms of Čech descent and of continuity for affine schemes. Then for all $i$ and $n$, the cohomology with coefficients $\mathbb{Z}/q(i)$ of the system $X \times_R \mathrm{Spec}\, D_j$, with limit $X \times_R \mathrm{Spec}\, D$, is continuous in degree $n$.

Lean: `UpperTheory.Cb.MorphismCompositionLaws.contOf`.

*Proof.* This is the theorem of continuity after base change, applied to $X$, $R$ and the system $(D_j)$. The classical proof covers $X$ by finitely many affine open sets, uses that their intersections are again affine because $X$ is separated, and passes from the affine case to $X$ by Čech descent. $\square$

**Definition 5.4.4 (Neighbourhood system).** Let $U$ be étale over $B$ and $u \in U$. A *neighbourhood system* for $(U, u)$ in degree $m$ is the following data. A filtered category $J$, étale $B$-schemes $V_j$ with maps $a_j : V_j \to U$ whose images contain $u$, and transition maps $V_k \to V_j$ for $j \to k$ over $U$. A strictly henselian ring $A$ and a map $t : \mathrm{Spec}\, A \to U$, with compatible maps $Y_A \to Y_{V_j}$ and $W_A \to W_{V_j}$ over $U$. The three conditions are that the cohomology of $(Y_{V_j})$ is continuous at $Y_A$ for injectivity in degree $m$ and for surjectivity in degree $m - 1$, and that the cohomology of $(W_{V_j})$ is continuous at $W_A$ for injectivity in degree $m - 1$.

**Lemma 5.4.5 (Affine neighbourhood system).** Assume the two axioms. Let $B$ be a scheme, $\iota : W \to B$ a closed immersion and $p : Y \to B$ proper. Let $U$ be étale over $B$ with $U \cong \mathrm{Spec}\, R$ and $q$ a unit in $R$, and let $u \in U$. Then for each $m$ there is a neighbourhood system for $(U, u)$ in degree $m$.

Lean: `UpperTheory.Cb.MorphismCompositionLaws.sys_of`.

*Proof.* Let $\mathfrak{p}$ be the prime of $R$ at $u$. The strict henselization $A$ of $R$ at $\mathfrak{p}$ is a filtered colimit of étale $R$-algebras $D_j$, each with a prime over $\mathfrak{p}$ (Milne, *Étale Cohomology*, Chapter I, §4). Let $V_j = \mathrm{Spec}\, D_j$. It is étale over $U$, so it is étale over $B$, and its image contains $u$. Let $t : \mathrm{Spec}\, A \to U$ be the natural map. Now $Y_U \to U$ is proper, so it is quasi-compact and separated, and $W_U \to U$ is a closed subscheme of it, so it has the same properties. The continuity lemma for $X = Y_U$ in degrees $m$ and $m - 1$, and for $X = W_U$ in degree $m - 1$, gives the three conditions. $\square$

**Theorem 5.4.6 (Affine geometric case).** Suppose that for every map of spaces $X' \to X$, every $q \geq 1$ and every $n$, the sequence of Definition 5.4.1 is exact at $H^{n+1}(X, X')$, and that its connecting map $H^n(X') \to H^{n+1}(X, X')$ is natural for maps of pairs. Assume the axioms. Let $k$, $q$, $B$, $W$, $Y$ be as in the setting, let $U$ be étale over $B$ with $U \cong \mathrm{Spec}\, R$, and let $u \in U$. Then for each $m$ there is a neighbourhood system for $(U, u)$ in degree $m$.

Lean: `UpperTheory.Cb.affineGeometricCase_of_obstructionExact_natural`.

*Proof.* The ring $R$ is a $k$-algebra through $U \to B \to \mathrm{Spec}\, k$, and $q$ is a unit in $k$, so $q$ is a unit in $R$. This is the last lemma applied to $U \cong \mathrm{Spec}\, R$. The proof does not use the first two hypotheses. $\square$

**Theorem 5.4.7 (Killing on a neighbourhood).** Assume the axioms. Let $k$ be a field, $q$ a unit in $k$, and $B$, $\iota : W \to B$, $p : Y \to B$ as in the setting. Let $U$ be étale over $B$ and $z \in H^m(Y_U, W_U; \mathbb{Z}/q(i))$. Suppose that the restriction of $z$ along each $\mathrm{Spec}\, A \to U$ with $A$ strictly henselian is zero. Then each $u \in U$ lies in the image of an étale map $U' \to U$ over $B$ such that the restriction of $z$ to $(Y_{U'}, W_{U'})$ is zero.

Lean: `UpperTheory.Cb.etale_cohomology_class_killed_on_neighborhood`.

*Proof.* We give the proof in three steps.

First, there is a neighbourhood system for $(U, u)$ in degree $m$. Take an affine open neighbourhood $U_0 \cong \mathrm{Spec}\, R$ of $u$ in $U$. It is étale over $B$, and $q$ is a unit in $R$ as in the proof of the last theorem. Lemma 5.4.5 gives a system for $(U_0, u)$. Compose its maps $a_j$ with the inclusion $U_0 \to U$. This gives a system for $(U, u)$.

Second, let $(V_j)$, $A$ and $t$ be the system. The long exact sequences of the pairs $(Y_{V_j}, W_{V_j})$ form a filtered system of exact sequences, and filtered colimits of abelian groups are exact. So the colimit of the sequences is exact, and it maps to the long exact sequence of $(Y_A, W_A)$. In the diagram
$$
\begin{aligned}
\varinjlim H^{m-1}(Y_{V_j}) \to \varinjlim H^{m-1}(W_{V_j}) &\to \varinjlim H^m(Y_{V_j}, W_{V_j}) \to \varinjlim H^m(Y_{V_j}) \\
H^{m-1}(Y_A) \to H^{m-1}(W_A) &\to H^m(Y_A, W_A) \to H^m(Y_A)
\end{aligned}
$$
the first vertical map is surjective, and the second and fourth vertical maps are injective, by the three conditions. By the four lemma, the third vertical map is injective.

Third, the image of $z$ in $H^m(Y_A, W_A)$ is zero by hypothesis, since $A$ is strictly henselian. By the second step the image of $z$ in the colimit is zero. So there is a $j$ such that the restriction of $z$ to $(Y_{V_j}, W_{V_j})$ is zero, and $U' = V_j$ works. $\square$

**Remark 5.4.8 (Formalization).** The axioms are a list of hypotheses on the model, and the proofs here use two of them. The two exactness and naturality hypotheses of Theorem 5.4.6 are not used in its proof. The proof of Theorem 5.4.7 goes through a lemma that also takes these two hypotheses and ignores them, and they are supplied there by other theorems, so the result depends only on the axioms. The continuity theorem behind Lemma 5.4.3 ([FinCont.lean](lean:Development/EtaleCohomology/KummerTheory/FinCont.lean#L51)), the presentation of the strict henselization ([FinSHen.lean](lean:Development/EtaleCohomology/KummerTheory/FinSHen.lean#L6)), and the step with the four lemma and filtered colimits were read as statements, not proofs. The names of these results (an intersection number, base change, composition laws of morphisms) do not describe their statements.
