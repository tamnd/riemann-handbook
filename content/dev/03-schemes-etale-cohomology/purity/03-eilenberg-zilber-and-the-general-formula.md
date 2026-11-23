---
title: The Eilenberg-Zilber theorem and the formula on every space
decls:
  - GlobalTheory.EZ.ez_nat
  - GlobalTheory.EZ.ez
  - GlobalTheory.PBFc.pbf_of_model
  - GlobalTheory.PBFg.pbf_of_disc
  - GlobalTheory.T.projectiveBundleFormula_of_discrete_spaces
  - GlobalTheory.EtC.projectiveBundleFormula_vectorBundle_any_space
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Eilenberg-Zilber theorem and the formula on every space

A space $E$ is built from the constant spaces $\mathrm{disc}(E_p)$ of its $p$-simplices. This section uses that fact to prove the projective bundle formula for every vector bundle on every space on which $q$ is invertible. The projective bundle $\mathbb{P}(V)$ is written as the diagonal of a bisimplicial space whose $p$-th column is a projective bundle over $\mathrm{disc}(E_p)$. The Eilenberg-Zilber theorem compares the chains of the diagonal with the total complex of the bisimplicial chains, and a filtration by columns reduces the formula to the columns, where [the theorem on constant spaces](/entry/projective-bundle-formula-discrete-space/) applies. The result is the form of the formula that [the theorem on the local steps](/entry/steps-holds/) of the Galois row needs.

**Definition 2.3.1 (Diagonal and total complex).** Let $\mathcal{C}$ be a preadditive category with finite coproducts and let $Y$ be a bisimplicial object of $\mathcal{C}$, with terms $Y_{p,k}$. The *diagonal complex* $\mathrm{diag}(Y)$ is the complex with $Y_{n,n}$ in degree $n$ and the alternating sum of the diagonal faces as differential. The *total complex* $\mathrm{Tot}(Y)$ has $\bigoplus_{p+k=n} Y_{p,k}$ in degree $n$, with the differential $d_h + (-1)^p d_v$ built from the alternating sums of the faces in the two directions. The *Alexander-Whitney map* $\mathrm{AW} : \mathrm{diag}(Y) \to \mathrm{Tot}(Y)$ sends $y \in Y_{n,n}$ to the sum over $p + k = n$ of the image of $y$ under the front face in the first direction and the back face in the second direction.

**Theorem 2.3.2 (Eilenberg-Zilber).** Let $\mathcal{C}$ be a preadditive category with finite coproducts.

1. For every bisimplicial object $Y$ of $\mathcal{C}$ there is a chain homotopy equivalence $\mathrm{diag}(Y) \to \mathrm{Tot}(Y)$ whose map in each degree $n$ is the Alexander-Whitney map.
2. Let $R$ be a commutative ring and let $X$ be a simplicial object in spaces, with diagonal space $\mathrm{diag}\, X$. There is a homotopy equivalence from $C_\bullet(\mathrm{diag}\, X)$ to the total complex of the bisimplicial complex of free sheaves $R[X_{p,k}]$ whose map in degree $-n$ is the Alexander-Whitney map, for every $n \geq 0$.

Lean: `GlobalTheory.EZ.ez_nat` (also `GlobalTheory.EZ.ez`).

For bisimplicial abelian groups this is the generalized Eilenberg-Zilber theorem, with homotopy inverse the shuffle map; see Goerss and Jardine, *Simplicial Homotopy Theory*, Chapter IV, §2. For a product of two simplicial abelian groups it is the original theorem of S. Eilenberg and J. A. Zilber, "On products of complexes", Amer. J. Math. 75 (1953).

*Proof.* For part 1 we take four facts as given: a family of shuffle operators on bisimplicial objects of $\mathcal{C}$ with their two defining identities; a homotopy from the composite of the shuffle map and the Alexander-Whitney map to the identity; a homotopy formula for the other composite; and the fact that these data assemble into a homotopy equivalence whose forward map in degree $n$ is the Alexander-Whitney map. For part 2, apply part 1 to the bisimplicial complex of free sheaves $R[X_{p,k}]$, an object of the preadditive category of sheaves of $R$-modules, and place degree $n$ at $-n$, as in the definition of $C_\bullet$. $\square$

**Remark 2.3.3.** Both sides are the unnormalized complexes, the full alternating face complexes. The statement names only the forward map; the homotopy inverse is not part of it.

A homotopy equivalence $\mathrm{AW} : C_\bullet(\mathrm{diag}\, X) \to \mathrm{Tot}(X)$ gives bijections $\mathrm{AW}^* : H^n(\mathrm{Tot}(X), I) \to H^n(C_\bullet(\mathrm{diag}\, X), I)$ for every complex $I$. We use this in the next proposition.

**Definition 2.3.4 (The twisted product).** Let $V$ be a vector bundle of rank $N$ on a space $E$. Let $\mathrm{Fib}_N$ be the space of the groupoid of unimodular vectors $v \in A^N$, with a morphism $v \to w$ for each unit $u$ with $v = u w$, and let $L_{\mathrm{Fib}}$ be its line bundle $u \mapsto u$. The *twisted product* $X(E, V)$ is the bisimplicial space with $p$-th column $E_p \times \mathrm{Fib}_N$, that is, $(E_p \times \mathrm{Fib}_N)_k(T) = E_p(T) \times (\mathrm{Fib}_N)_k(T)$. A simplicial map $\theta : [p'] \to [p]$ acts on the first factor through $E$ and on the second factor through the matrix that $V$ assigns to the edge of $\theta$.

There is an isomorphism of spaces $\mathrm{diag}\, X(E, V) \cong \mathbb{P}(V)$ under which the line bundle that comes from $L_{\mathrm{Fib}}$ on the diagonal becomes $L_V$. For each $p$, the column $E_p \times \mathrm{Fib}_N$ is isomorphic to the projective bundle of a vector bundle $V_p$ on the constant space $\mathrm{disc}(E_p)$, compatibly with the line bundles.

**Proposition 2.3.5 (Reduction to a cocycle model).** Let $V$ be a vector bundle of rank $N$ on a space $E$ on which $q$ is invertible. Let $B$ be a space, let $\lambda : X(E, V) \to B$ be a map to the constant bisimplicial space on $B$, and for $j < N$ let $z_j$ be a cocycle of degree $2j$ on $B$ with values in $\mathbb{Z}/q(j)$. Assume:

1. the pullback of $[z_j]$ along $\mathrm{diag}(\lambda)$ is the class $c_1(L_V)^j$ on $\mathbb{P}(V) \cong \mathrm{diag}\, X(E, V)$;
2. for each $p$ the pullback of $[z_j]$ along the $p$-th column of $\lambda$ is $c_1(L_{\mathrm{Fib}})^j$ on $E_p \times \mathrm{Fib}_N$;
3. the projective bundle formula in rank $N$ holds for every vector bundle on every constant space on which $q$ is invertible.

Then the projective bundle formula holds for $V$.

Lean: `GlobalTheory.PBFc.pbf_of_model`.

*Proof.* Fix $n$ and $i$. Pull back along the isomorphism $\mathrm{diag}\, X(E,V) \cong \mathbb{P}(V)$ and then along $\mathrm{AW}$; both maps are bijective on cohomology, the second by the Eilenberg-Zilber theorem. So it is enough to show that the composite map
$$
\varphi : \bigoplus_{j<N} H^{n-2j}(E, \mathbb{Z}/q(i-j)) \to H^n(\mathrm{Tot}(X(E,V)), \mathbb{Z}/q(i))
$$
is bijective. On cocycles, $\varphi$ is given by an explicit formula: pull $a_j$ back to each column, multiply by the pullback of $z_j$ along $\lambda$, and assemble with the Alexander-Whitney map. Hypothesis 1 shows that this formula computes $\varphi$ on classes. The formula commutes with the differentials and respects the filtration of both sides by the simplicial degree $p$ in the first direction. On the graded piece of degree $p$, it becomes the formula map for the bundle $V_p$ on $\mathrm{disc}(E_p)$, by hypothesis 2, and this map is bijective by hypothesis 3, since $q$ is invertible on $\mathrm{disc}(E_p)$. A lemma on column filtrations, the cochain form of the comparison of spectral sequences, which we take as given, then gives that $\varphi$ is bijective. The bisimplicial chains are zero in positive degrees in both directions, so the filtration is bounded on each side and the lemma applies. $\square$

To apply the proposition we need a space $B$ with cocycles that restrict to the right classes on the diagonal and on all columns at once. A universal line bundle gives one.

**Theorem 2.3.6 (From constant spaces to all spaces).** Let $q \geq 1$ and $N \geq 0$. Assume that the projective bundle formula in rank $N$ holds for every vector bundle on every constant space on which $q$ is invertible. Then it holds for every vector bundle of rank $N$ on every space on which $q$ is invertible.

Lean: `GlobalTheory.T.projectiveBundleFormula_of_discrete_spaces` (also `GlobalTheory.PBFg.pbf_of_disc`).

*Proof.* Let $B = \mathrm{Inv}_q \times B\mathrm{GL}_1$, the product of the constant space on the presheaf $\mathrm{Inv}_q$ of the previous section with the classifying space of line bundles. Let $\mathrm{pr}_2 : B \to B\mathrm{GL}_1$ be the second projection, a line bundle on $B$. Then $q$ is invertible on $B$. Choose cocycles $z_j$ that represent $c_1(\mathrm{pr}_2)^j$. Define $\lambda : X(E, V) \to B$ as follows: a simplex of $E_p \times \mathrm{Fib}_N$ over $T$ goes to the point of $\mathrm{Inv}_q(T)$, which exists because $q$ is invertible on $E$, and to the image of its $\mathrm{Fib}_N$ part under $L_{\mathrm{Fib}}$. By construction $\mathrm{pr}_2 \circ \lambda$ is $L_{\mathrm{Fib}}$ on each column and $L_V$ on the diagonal. Since cup powers and $c_1$ commute with pullback on spaces on which $q$ is invertible, the classes of the $z_j$ pull back to $c_1(L_{\mathrm{Fib}})^j$ and to $c_1(L_V)^j$. These are hypotheses 1 and 2 of the proposition, and hypothesis 3 is the assumption. $\square$

**Theorem 2.3.7 (Projective bundle formula).** Let $q \geq 1$, let $E$ be a space on which $q$ is invertible, and let $V$ be a vector bundle of rank $N$ on $E$. Then for all $n, i \in \mathbb{Z}$ the map
$$
\begin{aligned}
\bigoplus_{j=0}^{N-1} H^{n-2j}(E, \mathbb{Z}/q(i-j)) &\to H^n(\mathbb{P}(V), \mathbb{Z}/q(i)), \\
(a_j)_j &\mapsto \sum_{j=0}^{N-1} \pi^* a_j \cup c_1(L_V)^j
\end{aligned}
$$
is bijective.

Lean: `GlobalTheory.EtC.projectiveBundleFormula_vectorBundle_any_space`.

*Proof.* This is the theorem from constant spaces to all spaces, applied with [the theorem on constant spaces](/entry/projective-bundle-formula-discrete-space/) as its hypothesis. $\square$

For a scheme this is the classical formula (SGA 5, Exposé VII; Milne, *Étale Cohomology*, Chapter VI, §10). The Galois row uses it in the form for all spaces, below [the theorem on the local steps for the cohomology of a tower](/entry/steps-holds/).

**Remark 2.3.8.** The theorem quantifies over all vector bundles. By the lemma of the first section on bundles over constant spaces, every bundle on a constant space is trivial, so the generality is needed only for spaces that are not constant.

**Remark 2.3.9 (Formalization).** The projective bundle formula on every space is the condition $D_1$, the fifth of five results of étale cohomology collected into one package in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L119). The reduction to a cocycle model is in [ChainsIsStrictlyLE.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChainsIsStrictlyLE.lean#L62), a module whose name does not describe its main theorem. The Eilenberg-Zilber theorem holds in [PullAwChainsBijective.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PullAwChainsBijective.lean#L16) for any preadditive category with finite coproducts. We did not open the definition of its forward map; its name and the lemmas around it say that it is the Alexander-Whitney map. We opened the statements of the four inputs of the Eilenberg-Zilber theorem and of the column filtration lemma, but not their proofs. The cup product and $c_1$ are chosen classes; see the remark at the end of the first section.
