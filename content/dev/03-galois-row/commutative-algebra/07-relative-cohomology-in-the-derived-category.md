---
title: Relative cohomology in the derived category
decls:
  - UpperTheory.leafLocalization_of_injective_slice_of_restriction_injective
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Relative cohomology in the derived category

Let $B$ be a scheme, $W \subseteq B$ a closed subscheme and $p : Y \to B$ a map. For each étale $U \to B$ we have the scheme $Y_U = Y \times_B U$ and its part $Y_U \times_B W$ over $W$. This section constructs one object $K$ of the derived category of étale sheaves on $B$ that computes the relative cohomology of all the pairs $(Y_U, Y_U \times_B W)$ at once, naturally in $U$. It does the same for a chain $Y_2 \to Y_1 \to Y_0$ over $B$ and for the pair $(U, U \times_B W)$, and it gives the maps between these objects. The finiteness theorem for étale cohomology, [Theorem](/entry/etale-topology-top/), uses the result to move from the cohomology of single schemes to complexes of sheaves on $B$. The proof is a construction with injective sheaves. Its only inputs are two facts on restrictions of injective sheaves.

### Relative cohomology and representing objects

We keep the notation of the earlier sections: a scheme is a space, $R[E]$ is the complex of free sheaves on a space $E$, and $I$ is the chosen injective resolution of $\mathbb{Z}/q(i)$ on the big étale site. It vanishes in negative degrees.

**Definition (Relative cohomology).** Let $f : A \to X$ be a map of spaces, and let $C(f)$ be the mapping cone of $R[f] : R[A] \to R[X]$. The *relative cohomology* $H^n(X, A; \mathbb{Z}/q(i))$ is the degree $n$ cohomology of the complex $\operatorname{Hom}^\bullet(C(f), I)$.

The cone sequence $R[A] \to R[X] \to C(f)$ gives the familiar long exact sequence
$$\cdots \to H^{n-1}(A) \to H^n(X, A) \to H^n(X) \to H^n(A) \to \cdots.$$
A commutative square of spaces from $f' : A' \to X'$ to $f : A \to X$ gives a map of cones $C(f') \to C(f)$, and so a pullback $H^n(X, A) \to H^n(X', A')$.

Let $B_{\mathrm{et}}$ be the small étale site of $B$, and let $D(B)$ be the derived category of sheaves of $\mathbb{Z}/q$-modules on $B_{\mathrm{et}}$. For an étale $U \to B$, let $\mathcal{O}_U \in D(B)$ be the sheafification of the free presheaf $\mathbb{Z}/q[\operatorname{Hom}_B(-, U)]$, placed in degree $0$. For a sheaf $\mathcal{F}$, maps $\mathcal{O}_U \to \mathcal{F}$ are the sections $\mathcal{F}(U)$. So for $K \in D(B)$, the group $\operatorname{Hom}_{D(B)}(\mathcal{O}_U, K[n])$ is the $n$-th hypercohomology of $K$ on $U$.

**Definition (Representing object).** Let $p : Y \to B$ and $\iota : W \to B$ be maps. An object $K \in D(B)$ *represents the relative cohomology of $(p, \iota)$* if there are bijections
$$e_{U,n} : H^n\bigl(Y_U, \, Y_U \times_B W; \, \mathbb{Z}/q(i)\bigr) \xrightarrow{\ \sim\ } \operatorname{Hom}_{D(B)}(\mathcal{O}_U, K[n])$$
for all étale $U \to B$ and all $n$, natural in $U$: for a map $a : U' \to U$ over $B$, the bijection $e_{U',n}$ sends the pullback of $y$ along $a$ to $e_{U,n}(y) \circ \mathcal{O}_a$. For the pair $(B, \iota)$ the same definition with $U$ and $U \times_B W$ in place of $Y_U$ and $Y_U \times_B W$ gives an object that *represents the relative cohomology of $\iota$*.

Let $g : Y' \to Y$ be a map, so $p g : Y' \to B$. Let $K$ and $K'$ represent the relative cohomology of $(p, \iota)$ and $(p g, \iota)$ with bijections $e$ and $e'$. A map $f : K \to K'$ is *compatible with $g$* if $e'_{U,n}(g^* y) = f[n] \circ e_{U,n}(y)$ for all $U$, $n$ and $y$. In the same way, a map $\ell : L \to K$ from an object $L$ that represents the relative cohomology of $\iota$ is *compatible with $p$* if it matches the pullback along $Y_U \to U$.

In the classical theory, $K$ is the derived direct image on $B_{\mathrm{et}}$ of the relative cohomology complex of the pair, and the bijections are the Leray identifications. The construction below does not use direct image functors. It builds $K$ by hand from $I$.

### Two facts on injective sheaves

The theorem takes two statements as hypotheses. Both are proved elsewhere in the Lean code.

1. *(Injective on the slice.)* Let $J$ be an injective sheaf on the big étale site and let $X \to S$ be a map of schemes. Then the presheaves $V \mapsto J(X \times_S V)$ and $V \mapsto J(V)$ on the category of schemes over $S$ are sheaves for the étale topology and are injective.
2. *(Restriction to the small site.)* The restriction of an injective sheaf on the big étale site over $S$ to the small étale site of $S$ is a sheaf and is injective.

For a functor $G : B_{\mathrm{et}} \to \mathrm{Sch}$, we say that $G$ is *good* if for each injective sheaf $J$ on the big étale site the presheaf $U \mapsto \operatorname{Hom}(R[G(U)], J)$ on $B_{\mathrm{et}}$ is a sheaf and is injective. Four functors occur:
$$\begin{aligned} G_Y(U) &= Y_U, & G_{YW}(U) &= Y_U \times_B W, \\ G_B(U) &= U, & G_{BW}(U) &= U \times_B W, \end{aligned}$$
with the projections $F_Y : G_{YW} \to G_Y$ and $F_B : G_{BW} \to G_B$.

### The theorem

**Theorem (Leaf localization).** Assume statements 1 and 2. Let $q \ge 1$ and $i \in \mathbb{Z}$. Let $\iota : W \to B$ be a closed immersion and let $Y_2 \xrightarrow{g_2} Y_1 \xrightarrow{g_1} Y_0 \xrightarrow{p} B$ be maps of schemes. Then there are objects $K_0, K_1, K_2, L \in D(B)$ and maps
$$K_0 \xrightarrow{f} K_1 \xrightarrow{g} K_2 \xleftarrow{\ \ell\ } L$$
such that:

1. $K_0$, $K_1$ and $K_2$ represent the relative cohomology of $(p, \iota)$, $(p g_1, \iota)$ and $(p g_1 g_2, \iota)$;
2. $L$ represents the relative cohomology of $\iota$;
3. $f$ is compatible with $g_1$, $g$ is compatible with $g_2$, and $\ell$ is compatible with $p g_1 g_2$.

Lean: `UpperTheory.leafLocalization_of_injective_slice_of_restriction_injective`.

*Proof.* The proof has five steps.

1. *The families are good.* Fix $Y \to B$ and an injective sheaf $J$. By the Yoneda lemma, the group of maps from the free sheaf on $Y_U$ to $J$ is $J(Y \times_B U)$. By statement 1 the presheaf $V \mapsto J(Y \times_B V)$ on the big site over $B$ is an injective sheaf, and by statement 2 its restriction to $B_{\mathrm{et}}$ is an injective sheaf. So $G_Y$ is good. A lemma proved elsewhere in the Lean code makes this argument precise.
2. *Transfer along isomorphisms.* Goodness is invariant under an isomorphism of functors. The other families are of the form $G_Y$ up to isomorphism: $G_{YW}$ is $G_{Y \times_B W}$ for the map $Y \times_B W \to B$, $G_B$ is $G_Y$ for $Y = B$ and the identity map, and $G_{BW}$ is $G_W$ for $\iota$. So all four families are good.
3. *A K-injective complex.* Let $F : G_1 \to G_2$ be a map of good functors, and let $C_F(U)$ be the cone of $R[G_1(U)] \to R[G_2(U)]$. Put
$$T_F(U) = \operatorname{Hom}^\bullet(C_F(U), I).$$
The cone vanishes in positive degrees and $I$ vanishes in negative degrees, so each term of $T_F(U)$ is a finite product of groups $\operatorname{Hom}(R[G_j(U)]^{-s}, I^m)$ with $s \ge 0$, and $T_F$ vanishes in negative degrees. Each $I^m$ is injective, so goodness makes each term of $T_F$ an injective sheaf on $B_{\mathrm{et}}$. A bounded below complex of injective sheaves is K-injective.
4. *Identification of the morphisms.* Let $T$ be a K-injective complex. Then $\operatorname{Hom}_{D(B)}(\mathcal{O}_U, T[n])$ is the $n$-th cohomology of the complex of maps $\mathcal{O}_U \to T$, which is $T(U)$. For $T = T_F$ this is the cohomology of $\operatorname{Hom}^\bullet(C_F(U), I)$, which is the relative cohomology of $G_1(U) \to G_2(U)$. A result of the Lean code gives these bijections, their naturality in $U$, and their compatibility with maps of cones.
5. *Assembly.* Put $K_j = T_{F_j}$ for the projection $F_j$ of the pair over $Y_j$, and $L = T_{F_B}$. The map $g_1$ gives a commuting square from $F_1$ to $F_0$, and so a map of cones $C_{F_1} \to C_{F_0}$. Applying $\operatorname{Hom}^\bullet(-, I)$ reverses it and gives $f : K_0 \to K_1$. In the same way $g_2$ gives $g$, and the projections $Y_{2,U} \to U$ give a map of cones $C_{F_2} \to C_{F_B}$ and so $\ell : L \to K_2$. Step 4 gives the bijections and the compatibilities. $\square$

For $B$ the spectrum of a separably closed field, $D(B)$ is the derived category of $\mathbb{Z}/q$-modules, $\mathcal{O}_B$ is $\mathbb{Z}/q$, and the theorem only says that $K_0$ is a complex whose cohomology groups are $H^n(Y_0, Y_0 \times_B W)$. The content lies in the naturality in $U$: the objects $K_j$ glue the relative cohomology of all étale neighbourhoods of points of $B$.

**Remark.** The Lean statement asks that $\iota$ is a closed immersion, through an instance argument of the proposition `LateralTheory.E.LeafConsPf.LeafLoc`, but the proof at [LeafLocalizationOfInjectiveSliceOfRestrictionInj.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/LeafLocalizationOfInjectiveSliceOfRestrictionInj.lean#L96) never uses it: the construction works for any map $\iota$. The theorem is an implication. Statement 1 is supplied in [EtaleTopology.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleTopology.lean#L220) under the name `LateralTheory.Fin.InjSlice.intersectionNumber_baseChange`, an alias at FinInjSlice.lean line 9 that has nothing to do with intersection numbers. The conclusion feeds the statement `LateralTheory.E.EtaleTopologySheaves.LeafCons` at line 223 of the same file. The proof file has thirteen private helpers, among them the map of cones `coneM` and the natural maps `mYn`, `bY`, `mWn` and `bW`.

## Notes and references

The chapter supplies inputs to two results of Volume 3. The projective bundle formula in all ranks, [Theorem](/entry/pbf-all/), uses the rank two case and the induction step, and through them the Künneth formula for $\mathbb{G}_m$. The finiteness theorem for étale cohomology, [Theorem](/entry/etale-topology-top/), uses the finiteness of Picard torsion, which rests on the section on Kummer classes, and the relative cohomology objects of the last section. The representation of clopen subschemes of fixed rank feeds [Theorem](/entry/exists-finite-etale-representing-clopen-subschemes/).

- J. S. Milne, *Étale Cohomology*, Princeton University Press, 1980. Chapter I, §4 (étale morphisms); Chapter III, §1 (cohomology on the étale site) and Proposition 4.9 (Hilbert's Theorem 90); Chapter VI, §2 and §4 (proper and smooth base change), §10 (the projective bundle formula).
- A. Grothendieck et al., *SGA 4*, Exposé XIV (finiteness theorems), and *SGA 5*, Exposé VII (the projective bundle formula and Chern classes in étale cohomology).
- A. Grothendieck, *EGA IV*, 17.9.1 (étale morphisms and open immersions); and "Techniques de construction et théorèmes d'existence en géométrie algébrique IV: les schémas de Hilbert", Séminaire Bourbaki 221.
- R. Hartshorne, *Algebraic Geometry*, Springer, 1977. Chapter I, §6 (nonsingular curves and function fields).
- D. Mumford, *Abelian Varieties*, Oxford University Press, 1970. §4 (the $n$-torsion points of an abelian variety).
- N. Spaltenstein, "Resolutions of unbounded complexes", *Compositio Math.* 65 (1988). K-injective complexes.
