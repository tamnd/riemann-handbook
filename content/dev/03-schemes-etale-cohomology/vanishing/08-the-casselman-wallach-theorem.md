---
title: The Casselman-Wallach theorem
decls:
  - PositivityTheory.CW.cw_of
  - PositivityTheory.CWB.casselmanWallach
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Casselman-Wallach theorem

This section proves the Casselman-Wallach theorem for the unitary groups $U(p, q)$ ([Theorem 9.8.3](/entry/casselman-wallach/)). Let $\sigma$ be an irreducible unitary representation of $G$ and $\pi$ a smooth representation of moderate growth. Then each map of $(\mathfrak{g}, K)$-modules from the $K$-finite vectors of $\sigma$ to $\pi$ extends to a $G$-map on the smooth vectors of $\sigma$. The extension is unique, and it is a topological isomorphism onto a closed subspace. The key input is the maximum principle of Section 7 ([Theorem 9.7.4](/entry/max-pr/)). It gives the a priori bound for the extension and, a second time, the lower bound. The statement is used through [Theorem 1.1.4 of Volume 15](/entry/casselman-wallach-of-literature/), which returns it in the literature chapter. For the background see [representations of real groups](/learn/representations/#representations-of-real-groups) and [Harish-Chandra modules](/learn/real-groups/#admissible-representations-and-mathfrakg-k-modules) ([[Harish-Chandra module|2MKHH636C3]]).

We keep the notation of Section 7: $G \subseteq M_n(\mathbb{C})$ is the group of $J$, $K = G \cap U(n)$, $\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$, and $\|g\|^2 = \sum_{a,b}|g_{ab}|^2$. Let $\sigma$ be a [unitary representation](/learn/analysis/#lie-groups-and-lie-algebras) ([[unitary representation|74BPYJNZTM]]) of $G$ on a Hilbert space $H$. For $X \in \mathfrak{g}$ and $w \in H$, the vector $d\sigma(X)w$ is the limit of $t^{-1}(\sigma(\exp tX)w - w)$ as $t \to 0$, if it exists. A vector $w$ is *smooth* if all the iterated derivatives $d\sigma(X_1) \cdots d\sigma(X_k)w$ exist for $X_1, \dots, X_k \in \mathfrak{g}$. We write $H^\infty$ for the space of smooth vectors. A vector is *$K$-finite* if it lies in a finite-dimensional subspace that is stable under $\sigma(K)$.

**Definition 9.8.1 (Sobolev norms).** A *word* is a finite list $l = (X_1, \dots, X_k)$ of elements of $\mathfrak{g}$, with $d\sigma(l) = d\sigma(X_1) \cdots d\sigma(X_k)$. For a finite list $S$ of words and $w \in H^\infty$ put
$$\|w\|_S = \sum_{l \in S} \|d\sigma(l)w\|.$$

The empty word gives $\|w\|$. The [Sobolev norms](/learn/analysis/#sobolev-norms) $\|\cdot\|_S$ define the usual Fréchet topology on $H^\infty$.

**Definition 9.8.2 (Smooth representation of moderate growth).** Let $E$ be a complete Hausdorff topological vector space over $\mathbb{C}$ whose topology is given by seminorms $(p_i)_{i \in \mathbb{N}}$. Let $\pi$ and $d\pi$ map matrices to continuous linear operators on $E$. Then $(\pi, d\pi)$ is a *smooth representation of moderate growth* if:

1. $\pi(1) = 1$ and $\pi(ab) = \pi(a)\pi(b)$ for $a, b \in G$;
2. $g \mapsto \pi(g)x$ is continuous on $G$ for each $x \in E$;
3. for each $X \in \mathfrak{g}$ and $x \in E$, $d\pi(X)x$ is the derivative of $t \mapsto \pi(\exp tX)x$ at $t = 0$;
4. for each $i$ there are a continuous seminorm $q$ and $N \geq 0$ with $p_i(\pi(g)x) \leq (1 + \|g\|^2)^N q(x)$ for all $g \in G$ and $x \in E$.

Condition 3 asks that each vector of $E$ is differentiable. So $E$ plays the role of the space of smooth vectors of a representation of moderate growth. A linear map $T_0 : H \to E$ is a *$(\mathfrak{g}, K)$-map* if $T_0(\sigma(k)v) = \pi(k)T_0v$ and $T_0(d\sigma(X)v) = d\pi(X)T_0v$ for all $K$-finite $v$, $k \in K$ and $X \in \mathfrak{g}$.

**Theorem 9.8.3 (Casselman-Wallach theorem for $U(p, q)$).** Let $\sigma$ be an irreducible unitary representation of $G$ on $H$, let $(\pi, d\pi)$ be a smooth representation of moderate growth on $E$, and let $T_0 : H \to E$ be a $(\mathfrak{g}, K)$-map. Then there is a linear map $T : H \to E$ such that:

1. $Tv = T_0v$ for all $K$-finite $v$;
2. $T(\sigma(g)w) = \pi(g)Tw$ for all $g \in G$ and $w \in H^\infty$, and for each $i$ there are $S$ and $C$ with $p_i(Tw) \leq C\|w\|_S$ for all $w \in H^\infty$;
3. each $T'$ with properties 1 and 2 is equal to $T$ on $H^\infty$;
4. $T(H^\infty)$ is closed in $E$;
5. if $T_0v \neq 0$ for some $K$-finite $v$, then for each $S$ there is a continuous seminorm $q$ on $E$ with $\|w\|_S \leq q(Tw)$ for all $w \in H^\infty$.

Lean: `PositivityTheory.CWB.casselmanWallach`.

This is the theorem of Casselman (W. Casselman, *Canonical extensions of Harish-Chandra modules to representations of G*, Canad. J. Math. 41 (1989)) and Wallach (N. Wallach, *Real Reductive Groups II*, Chapter 11) for $U(p, q)$ and an irreducible unitary $\sigma$. Bernstein and Krötz give another proof (Israel J. Math. 199 (2014)). By parts 2 and 5, $T$ is a topological isomorphism from $H^\infty$ onto $T(H^\infty)$ when $T_0 \neq 0$. So the Harish-Chandra module of $\sigma$ has one smooth globalization of moderate growth.

**Theorem 9.8.4 (Reduction to the maximum principle).** If the conclusion of [Theorem 9.7.4](/entry/max-pr/) holds for each admissible unitary module and each $N$, then the conclusion of the last theorem holds.

Lean: `PositivityTheory.CW.cw_of`.

*Proof.* Fix $\sigma$, $\pi$ and $T_0$. We use four facts about $\sigma$, which are standard results of Harish-Chandra's theory.

- (a) $K$-finite vectors are smooth, $d\sigma(X)$ maps them to $K$-finite vectors, and for each $S$ they are dense in $H^\infty$ for $\|\cdot\|_S$.
- (b) The operators $d\sigma(X)$ on the $K$-finite vectors give an admissible unitary module $V$ in the sense of Section 7, with $E_{ab}$ the complex linear extension of $d\sigma$.
- (c) For each $m$ there are $S$ and $C$ with $\|(1 + \Omega_K)^m v\| \leq C\|v\|_S$ for $v \in V$. This holds since $\Omega_K$ is a polynomial in the $d\sigma(X)$.
- (d) For each word $l$, $w \in H^\infty$ and $X \in \mathfrak{g}$, the derivative of $t \mapsto d\sigma(l)\sigma(\exp tX)w$ at $0$ is $d\sigma(l)d\sigma(X)w$.

Step 1 (the a priori bound). Fix $i$, and take $q$ and $N$ from condition 4 for $p_i$. Take $m$, $K_0$ and $I_0$ from [Theorem 9.7.4](/entry/max-pr/) for $V$ and $N$, and $S$, $C$ from (c) for $m$. Let $\lambda$ be a linear form on $E$ with $|\lambda| \leq p_i$, and put $F(v)(g) = \lambda(\pi(g)T_0v)$. Then $F(v)$ is continuous, and $F(v)$ has the derivative $F(d\sigma(X)v)$ along $X$, since $T_0$ is a $(\mathfrak{g}, K)$-map. Also $|F(v)(g)| \leq (1 + \|g\|^2)^N q(T_0v)$. With $B = \max_{e \in I_0} q(T_0e)$, the maximum principle gives $|\lambda(T_0v)| \leq K_0B\|(1 + \Omega_K)^m v\| \leq K_0BC\|v\|_S$. By the Hahn-Banach theorem, $p_i(T_0v)$ is the supremum of such $|\lambda(T_0v)|$. So $p_i(T_0v) \leq K_0BC\|v\|_S$ for all $K$-finite $v$.

Step 2 (extension). By Step 1 and the density in (a), $T_0$ extends from the $K$-finite vectors to $H^\infty$. A sequence of $K$-finite vectors that converges in each Sobolev norm is a Cauchy sequence in $E$, and $E$ is complete. Extend the result linearly to $H$. This gives $T$ with property 1 and the Sobolev bounds of property 2.

Step 3 ($K$ and $\mathfrak{g}$ on smooth vectors). For $w \in H^\infty$, approximate $w$ by $K$-finite vectors. Both sides of $T(\sigma(k)w) = \pi(k)Tw$ and $T(d\sigma(X)w) = d\pi(X)Tw$ are continuous in $w$ for the Sobolev norms, and they are equal on $K$-finite vectors. So they are equal on $H^\infty$.

Step 4 ($G$ on smooth vectors). Let $X \in \mathfrak{g}$ and $w \in H^\infty$. By (d) and Step 3, the curves $t \mapsto T(\sigma(\exp tX)w)$ and $t \mapsto \pi(\exp tX)Tw$ satisfy the same linear differential equation, $u' = d\pi(X)u$, with the same value at $t = 0$. The Sobolev bounds of Step 2 control the first curve, and the growth condition controls the second. So $T(\sigma(\exp X)w) = \pi(\exp X)Tw$. Each $g \in G$ is $k\exp X$ with $k \in K$ and $X \in \mathfrak{g}$, by the Cartan decomposition. With Step 3 for $k$, this gives $T(\sigma(g)w) = \pi(g)Tw$, and property 2 holds.

Step 5 (uniqueness). If $T'$ has properties 1 and 2, then $T' - T$ has Sobolev bounds and is zero on the $K$-finite vectors. By the density in (a) it is zero on $H^\infty$. This is property 3.

Step 6 (the lower bound). Assume $T_0v_0 \neq 0$ for a $K$-finite $v_0$. Then $Tv_0 \neq 0$, and since the seminorms separate points, $p_i(Tv_0) \neq 0$ for some $i$.

1. Condition 4 gives a continuous seminorm $Q$ on $E$ and $N$ with $p_i(\pi(g)x) \leq (1 + \|g\|^2)^N Q(x)$, $Q(\pi(g)x) \leq (1 + \|g\|^2)^N Q(x)$ and $Q(\pi(k)x) = Q(x)$ for $k \in K$. To get $Q$, take the seminorm $q$ of condition 4 and average it over the translates by $K$.
2. For each nonzero $u \in H^\infty$ there is $g \in G$ with $p_i(\pi(g)Tu) \neq 0$. This uses the irreducibility of $\sigma$. So $Q(Tu) \neq 0$, and $Q'(v) = Q(Tv)$ is a $K$-invariant norm on $V$.
3. For each nonzero $v_0' \in V$ there is a $K$-invariant sesquilinear form $\beta$ on $V$ with $|\beta(v, y)| \leq Q'(v)Q'(y)$ and $\beta(v_0', v_0') \neq 0$, and $\Omega_K$ is symmetric for each such $\beta$.
4. With these forms, for each $\eta \in V$ there is $C$ with $|\langle \eta, y\rangle| \leq C\,Q(Ty)$ for $y \in V$. By density and the Sobolev bounds of $T$, the same holds for $y \in H^\infty$.
5. The maximum principle, together with item 4, gives a continuous seminorm $q$ on $E$ with $\|v\| \leq q(Tv)$ for $K$-finite $v$. Here two more facts enter. First, $(1 + \Omega_K)^m$ is surjective on $V$ and symmetric for the inner product. Second, $T(1 + \Omega_K)^m v = D_m(Tv)$ for a continuous operator $D_m$ on $E$, a polynomial in the $d\pi(X)$.
6. For a word $l$ and $K$-finite $v$, $\|d\sigma(l)v\| \leq q(T\,d\sigma(l)v) = q(d\pi(l)Tv)$. The seminorm $q_S = \sum_{l \in S} q \circ d\pi(l)$ is continuous on $E$, and $\|v\|_S \leq q_S(Tv)$. By density, this holds on $H^\infty$. This is property 5.

Step 7 (closed image). If $T_0v_0 \neq 0$ for some $K$-finite $v_0$, then by Step 6 and property 2, $T$ is a homeomorphism from $H^\infty$ onto $T(H^\infty)$. Since $H^\infty$ is complete for the Sobolev norms, $T(H^\infty)$ is complete, so it is closed in the Hausdorff space $E$. If $T_0 = 0$ on the $K$-finite vectors, then $T = 0$ on $H^\infty$ by the argument of Step 5. In that case $T(H^\infty) = \{0\}$, which is closed. This is property 4. $\square$

*Proof of the Casselman-Wallach theorem.* [Theorem 9.7.4](/entry/max-pr/) proves the maximum principle. The last theorem then gives the conclusion. $\square$

**Remark 9.8.5 (Formalization).** The main theorem is `cw_of maxPr` in [FinalB.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/FinalB.lean#L8). The statement `CasselmanWallach` is in [HasDRepIffHasDerivAt.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/HasDRepIffHasDerivAt.lean#L98). There $T_0$ and $T$ are linear maps on all of $H$, and parts 2 to 5 constrain $T$ only on $H^\infty$. In [CwOf.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/CwOf.lean#L36), `cw_of` builds the model of (b) by `model_of` at L37, and then calls `lift_of hM`, which builds the same model again at L33. Properties 1 to 3 are `lift_of_steps` and properties 4 and 5 are `cw_of_steps`, in [CasselmanWallachAdmissible.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/CasselmanWallachAdmissible.lean#L38). Both take the facts (a) to (d) and the lemmas of each step as hypotheses `c1` to `e3d`, which we know only by their statements. Many of these lemmas are in files whose names do not match their content: `d3` (Step 3) in `ZetaClassicalZeroFreeRegion.lean` L61, `d2` (Step 2) in `PageTheorem.lean` L142, `d4b` (Step 4) in `TendstoPiZero.lean` L165, `c5` (fact (a)) in `Imports.lean` L11, `d1b` (Step 1) in `SlopeLimitConstant.lean` L65, `c2a` in `CasimirNonnegative.lean` L34, `c2b` in `MatrixActionAdditive.lean` L25, `e1b` in `ExponentialKSet.lean` L38, `e3a` in `MatrixActionLinear.lean` L43, `e3b` in `HilbertSchmidtSqEq.lean` L40 and `e3c` (item 5 of Step 6) in `EigenspacesOrthogonal.lean` L23. Some statements also have the wrong names. In [SmoothSeminormAndSobolevBounds.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/SmoothSeminormAndSobolevBounds.lean#L130), `faceMap_comp_succAbove_castSucc` (L130) is item 2 of Step 6, and `faceMap_castSucc_comp_eq_succ` (L154) is the operator $D_m$ of item 5; both names are simplicial identities. `CardSubmodulesOfIndexLePow` (L79) says that each vector lies in a finite-dimensional $K$-stable subspace, and `CardSubmodulesAndLinearEquivBounds` (L81) says that the eigenvectors of $\Omega_K$ span. The decomposition `D5` asks only $X \in \mathfrak{g}$, not $X \in \mathfrak{p}$, and this is all Step 4 needs. The closed image is `isClosed_image_of_sobolev_lower` in [IsClosedImageOfSobolevLower.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/IsClosedImageOfSobolevLower.lean#L26). The file of `cw_of_steps` also has `casselman_wallach_admissible` (L110), which this proof does not use. In the Lean code $\|\cdot\|_S$ is `sobNorm`, the growth weight is `hs g` $= \|g\|^2$, and the classical reasons in Steps 2 to 7 are ours.
