---
title: Smooth polarized fans
decls:
  - GlobalTheory.CompanionTheory.Ar.Fan.SmoothRefinement.exists_smooth_refinement
  - GlobalTheory.T.exists_smooth_polyhedral_fan_refinement
  - GlobalTheory.CompanionTheory.Ar.Fan.exists_smooth_fan_int
  - GlobalTheory.PolDeg.exists_inv_smooth_fan_noSelfInt
  - GlobalTheory.T.exists_invariant_smoothProjFan_noSelfIntersections
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Smooth polarized fans

This section proves that polarized fans exist. The theorems of Section 1 take a polarized fan with no self-intersections as input. Here we construct such a fan on $\mathbb{Z}$ in each rank. We first refine a polyhedral fan to a smooth one, and then apply this to an explicit function on positive semidefinite integral forms. The main theorem of the chapter uses the fan on $\mathbb{Z}$ in rank $\max(1, [E : \mathbb{Q}] \min(p, q))$ and passes from it to a fan on $\mathcal{O}_E$. The result is part of [the step on the statements from the literature](/step/every-character-of-literature/).

The definitions of Section 1 use only the ring $\mathcal{O}_E$ and its conjugation. So they make sense for a ring $O$ with a map $a \mapsto \bar a$. Invariant functions on $O$, balanced forms on finitely generated projective $O$-modules, cones, polarized fans and fans with no self-intersections are then defined as in Section 1, with $O$ in place of $\mathcal{O}_E$. For $O = \mathbb{Z}$ we take $\bar a = a$. Then a balanced form is a symmetric bilinear form on a lattice. We need some more notions.

**Definition 7.26.1 (CM order).** A ring $O$ with a map $a \mapsto \bar a$ is a *CM order* if $O$ is a Dedekind domain that is finite over $\mathbb{Z}$, there is an injective ring map $O \to \mathbb{C}$, and $\sigma(\bar a) = \overline{\sigma(a)}$ for each ring map $\sigma : O \to \mathbb{C}$ and each $a \in O$.

The ring of integers of a CM field with its conjugation is a CM order, and so is $\mathbb{Z}$ with the identity.

**Definition 7.26.2 (Polyhedral fan).** Let $O$ be a ring with a map $a \mapsto \bar a$ and $\varphi$ an invariant function on $O$. A family $\gamma_1, \dots, \gamma_m$ of forms on $X$ is a *cell* of $\varphi$ if each $\gamma_i$ is balanced and positive semidefinite, $\varphi$ is linear on the cone they span, and the strictness condition of Section 1 holds. So a cone is a cell whose forms are part of a basis of the balanced forms. The function $\varphi$ is a *polyhedral fan* on $X$ if it satisfies the first two conditions of a polarized fan and the following condition. There is a finite set $S$ of forms such that each positive semidefinite balanced real form is, after an automorphism of $X$, a nonnegative real combination of a cell of $\varphi$ with all forms in $S$. It is a polyhedral fan *in rank at most $q$* if it is a polyhedral fan on each $X$ of rank at most $q$.

So a polyhedral fan has cells that need not be simplicial or smooth. A polarized fan is a polyhedral fan whose cones are smooth and closed under taking subfamilies.

**Definition 7.26.3 (Twist invariance, domination).** Let $w_0 \in O$. An invariant function $\varphi$ on $O$ is *invariant under twists fixing $w_0$* if $\varphi(B \circ (\sigma \times \sigma)) = \varphi(B)$ for each ring automorphism $\sigma$ of $O$ with $\sigma(w_0) = w_0$, where $\sigma$ acts on $O^n$ coordinatewise. A module $X$ has *domination* if for all additive maps $\ell, \mu$ from the forms on $X$ to $\mathbb{Z}$, such that $\ell(\beta) > 0$ for each nonzero positive semidefinite balanced $\beta$, there is $C \in \mathbb{N}$ with $\mu(\beta) \le C\, \ell(\beta)$ for all positive semidefinite balanced $\beta$.

**Theorem 7.26.4 (Smooth refinement of a polyhedral fan).** Let $O$ be a CM order of characteristic $0$, $w_0 \in O$ and $q \in \mathbb{N}$. Suppose that each finitely generated projective $O$-module has domination. Let $\psi$ be an invariant function on $O$ that is a polyhedral fan in rank at most $q$ and is invariant under twists fixing $w_0$. Then there is an invariant function $\varphi'$ on $O$ with the following properties:

1. $\varphi'$ is a polarized fan with no self-intersections in rank at most $q$;
2. $\varphi'$ is invariant under twists fixing $w_0$;
3. for each $X$ of rank at most $q$ and each cone $\gamma$ of $\varphi'$ on $X$, $\psi$ is linear on the cone spanned by $\gamma$.

Lean: `GlobalTheory.CompanionTheory.Ar.Fan.SmoothRefinement.exists_smooth_refinement` (also `GlobalTheory.T.exists_smooth_polyhedral_fan_refinement`, a second name).

*Proof.* We refine $\psi$ in two steps.

1. A lemma on simplicial refinements uses all the hypotheses. It gives an invariant function $\varphi$ with a labelling of its cells, such that the cells of $\varphi$ are simplicial and labelled, $\varphi$ is invariant under twists fixing $w_0$, and $\varphi$ is subordinate to $\psi$. Here subordinate means that, in rank at most $q$, $\psi$ is linear on each cell of $\varphi$.
2. A lemma on smooth subordinate fans uses the CM order, domination and the output of step 1. It gives an invariant function $\varphi'$ with properties 1 and 2 that is subordinate to $\varphi$.
3. Subordination is transitive, so $\varphi'$ is subordinate to $\psi$. Each cone of $\varphi'$ is a cell of $\varphi'$. So $\psi$ is linear on each cone of $\varphi'$ in rank at most $q$. This is property 3. $\square$

This is the classical route to smooth cone decompositions: first a simplicial subdivision, then a subdivision of each simplicial cone into cones spanned by part of a basis of the lattice. Twist invariance and the action of the automorphisms of $X$ must be kept along the way.

We apply the theorem to one function on $\mathbb{Z}$. For $g \in \mathbb{N}$ let $\nu_g$ be the invariant function on $\mathbb{Z}$ that, for a symmetric bilinear form $B$ on $\mathbb{Z}^n$, is
$$\nu_g(B) = 2^g \Bigl( 2^{-n} \sum_{y \in (\mathbb{Z}/2)^n} \inf \{ B(a, a) : a \in \mathbb{Z}^n,\ a \equiv y \bmod 2 \} - B(0, 0) \Bigr).$$
So $\nu_g$ is $2^g$ times the mean, over the classes of $\mathbb{Z}^n / 2\mathbb{Z}^n$, of the infimum of $B(a, a)$ on the class, minus $2^g B(0, 0)$. For $n = 1$ and $B(a, b) = ab$ we get $\nu_g(B) = 2^{g-1}$.

**Theorem 7.26.5 (Smooth polarized fans on the integers).** For each $g \in \mathbb{N}$ there is an invariant function $\varphi$ on $\mathbb{Z}$ that is a polarized fan with no self-intersections in rank at most $g$.

Lean: `GlobalTheory.CompanionTheory.Ar.Fan.exists_smooth_fan_int` (also `GlobalTheory.PolDeg.exists_inv_smooth_fan_noSelfInt`, a second name; `GlobalTheory.T.exists_invariant_smoothProjFan_noSelfIntersections`, a third name).

*Proof.* We apply the previous theorem with $O = \mathbb{Z}$, $\bar a = a$, $w_0 = 0$, $q = g$ and $\psi = \nu_g$.

1. The ring $\mathbb{Z}$ with the identity is a CM order of characteristic $0$.
2. A finitely generated projective $\mathbb{Z}$-module $Y$ is free. By reduction theory it has a *reduction cover*: finitely many families of positive semidefinite symmetric forms such that each positive semidefinite real form is, after an automorphism of $Y$, a nonnegative combination of the forms of one family. A lemma on integer lattices gives that $Y$ has domination.
3. A lemma on the function $\nu_g$ uses the reduction covers of step 2. It gives that $\nu_g$ is a polyhedral fan in rank at most $g$.
4. The function $\nu_g$ is invariant under twists fixing $0$. The only ring automorphism of $\mathbb{Z}$ is the identity, so this holds for any invariant function.
5. The previous theorem gives $\varphi'$ with properties 1 to 3. Property 1 is the claim. $\square$

Properties 2 and 3 are not used. The statement does not keep property 3, although the proof gives a fan on whose cones $\nu_g$ is linear.

**Remark 7.26.6 (Formalization).** The proofs are in [ExistsSmoothPolyhedralFanRefinement.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/ConvexCones/ExistsSmoothPolyhedralFanRefinement.lean#L12) and [ExistsSmoothFanInt.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/ConvexCones/ExistsSmoothFanInt.lean#L29). The `T.*` names are wrappers, at line 7 and line 12 of the matching `Statement` files, that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. The name `GlobalTheory.PolDeg.exists_inv_smooth_fan_noSelfInt` is a term alias of `exists_smooth_fan_int`, with no tactic, in [ExistsInvariantSmoothProjFanNoSelfIntersections.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsInvariantSmoothProjFanNoSelfIntersections.lean#L12), lines 12 to 13. The words "Proj" in the third name and "smooth projective" in its file name do not match the statement, which asks only for a polarized fan with no self-intersections. The CM order is `CMOrd` and twist invariance is `IsTwG`, at lines 14 and 160 of [VorFunEvalEqFineMean.lean](lean:CompanionTheory/SpectralGeometry/CountingDefinitions/VoronoiMeans/VorFunEvalEqFineMean.lean#L14). Cells, polyhedral fans, reduction covers and domination are `IsCell`, `IsPolyFanOn` and `IsPolyFan`, `HasRedCover` and `Dominates`, at lines 226, 236, 250, 284 and 290 of [ExistsEqAddOfRedVEq.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsEqAddOfRedVEq.lean#L236). The function $\nu_g$ is `vorFun ℤ g` (line 169 of the first of these files), and its formula is the lemma `vorFun_eval_eq_fineMean` (line 192) with `fineMean 1` (line 133 of the second). We do not identify the cells of $\nu_g$ with a decomposition from the literature. The first theorem has both instance arguments `[IsDedekindDomain O]` and `[Module.Finite ℤ O]` and the hypothesis `CMOrd O bar`, whose fields `ded` and `fin` say the same; the instances are redundant. Its steps are `T.exists_simplicial_labelled_refinement` (line 14) and `T.exists_smooth_subordinate_fan` (line 15). In the second proof, step 2 is `hasRedCover_int_proj` (line 17) and `dominates_int_proj` (line 23), which calls `T.integer_lattice_dominates`; step 3 is `T.voronoi_fan_is_polyhedral` (line 31); step 4 is `baseFun_twist` (line 33); and line 34 drops properties 2 and 3 with `⟨φ, h₁, h₂, -, -⟩`. These lemmas have no entries in this chapter, and we use only their statements. The theorem is used in `ToroidalCompactificationHolds.lean` at line 12, in rank $\max(1, [E : \mathbb{Q}] \min(p, q))$. That proof drops the absence of self-intersections (`⟨φs, hs, -⟩`) and passes to a fan on $\mathcal{O}_E$ with `PolFan.exists_fine_invariant_fan` (line 13), which gives a fan with no self-intersections on its own. It is also used in `SiegelIntegralToroidalOfPolarisedChartsForFan.lean` at line 14.

## Notes and references

The chapter follows the algebraic theory of toroidal and minimal compactifications of Faltings and Chai, *Degeneration of Abelian Varieties*, Ergebnisse der Mathematik und ihrer Grenzgebiete (3) 22, Springer, 1990, and its extension to PEL type by Lan, *Arithmetic Compactifications of PEL-Type Shimura Varieties*, London Mathematical Society Monographs 36, Princeton University Press, 2013. Our setting is a unitary moduli scheme with a host and a level as in Section 1, and the formal statements differ in many details from these books.

Sections 1 and 14 to 16 state and prove the toroidal compactification for a polarized fan, with fan charts, rigid charts and the logarithmic Kodaira-Spencer isomorphism. The general construction is in Chapter IV of Faltings and Chai and in Chapter 6 of Lan. The cone decompositions come from Ash, Mumford, Rapoport and Tai, *Smooth Compactification of Locally Symmetric Varieties*, Math Sci Press, 1975, Chapter II. The local structure along the boundary is that of toroidal embeddings in Kempf, Knudsen, Mumford and Saint-Donat, *Toroidal Embeddings I*, Lecture Notes in Mathematics 339, Springer, 1973, Chapter I.

Sections 2 to 9 treat Fourier expansions, the boundary ideal, normalized blowups and the minimal compactification through theta functions and the Hodge bundle. The minimal compactification by modular forms is in Chapter V of Faltings and Chai and in Chapter 7 of Lan. The algebraic theory of theta functions is in Mumford, "On the equations defining abelian varieties I", Inventiones Mathematicae 1 (1966), 287 to 354. Blowups and normalization are as in Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics 52, Springer, 1977, Chapter II.

Sections 10 to 13 build canonical families and tautological charts from degeneration data. Degeneration data, Raynaud extensions and the converse construction are in Chapters II and III of Faltings and Chai and in Chapters 4 and 5 of Lan. The construction of a degenerating family from its periods is Mumford, "An analytic construction of degenerating abelian varieties over complete rings", Compositio Mathematica 24 (1972), 239 to 288.

Sections 17 to 24 use heat operators to compare the Kodaira-Spencer map with the derivatives of the periods. The heat equations for theta functions on a polarized abelian scheme are in Welters, "Polarized abelian varieties and the heat equations", Compositio Mathematica 49 (1983), 173 to 194. The use of the Kodaira-Spencer map along the boundary follows Chapters III and IV of Faltings and Chai and Chapter 6 of Lan.

Section 25 is Čech cohomology. The Čech description of the cohomology of the structure sheaf and the base change for proper morphisms are in Hartshorne, Chapter III. The polarization map and the dual abelian variety are in Mumford, *Abelian Varieties*, Tata Institute of Fundamental Research Studies in Mathematics 5, Oxford University Press, 1970, Chapters II and III.

Section 26 constructs smooth polarized fans by subdivision. The existence of smooth subdivisions is in Kempf, Knudsen, Mumford and Saint-Donat, Chapter I, and cone decompositions of the cone of positive definite forms that are invariant under the arithmetic group are in Ash, Mumford, Rapoport and Tai, Chapter II.
