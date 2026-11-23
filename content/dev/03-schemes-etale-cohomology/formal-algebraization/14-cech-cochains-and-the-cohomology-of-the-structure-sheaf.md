---
title: Nerve cochains and the cohomology of the structure sheaf
decls:
  - GlobalTheory.CompanionTheory.Hodge.Nerve.cmpSt_of_cxSt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Nerve cochains and the cohomology of the structure sheaf

Sections 12 and 13 work with the cochains of a functor on a finite meet semilattice. This section connects them with the cohomology of the structure sheaf. For a finite affine cover of a scheme that is closed under intersection, the cochain complex of the functor of sections of $\mathcal{O}_X$ computes $H^n(X, \mathcal{O}_X)$ ([coherent cohomology](/learn/commutative-algebra/#coherent-cohomology)). So the bound and the isomorphism of Sections 12 and 13 are statements on $H^1(X, \mathcal{O}_X)$ and $H^2(X, \mathcal{O}_X)$. The result is an input of the [row step](/step/every-character-of-row/).

Let $R$ be a commutative ring and $X$ a scheme over $\operatorname{Spec} R$. Then the modules $H^n(X, \mathcal{O}_X)$ are $R$-modules.

**Definition 7.14.1 (Affine system).** Let $P$ be a meet semilattice. An *affine system* on $X$ indexed by $P$ is a map $u$ from $P$ to the affine open subsets of $X$ such that $u(a \wedge b) = u(a) \cap u(b)$ for all $a, b \in P$, and the sets $u(a)$ cover $X$. Its *functor of sections* is the functor $F_u$ from $P^{\mathrm{op}}$ to commutative $R$-algebras with $F_u(a) = \Gamma(u(a), \mathcal{O}_X)$ and the restriction maps.

The map $u$ is monotone: if $a \leq b$, then $u(a) = u(a \wedge b) = u(a) \cap u(b) \subseteq u(b)$. So $F_u$ is a functor. Each finite intersection of sets of the system is again a set of the system, hence affine.

**Theorem 7.14.2 (Nerve cochains compute the cohomology of the structure sheaf).** Assume that $d \circ d = 0$ on the cochains of every functor, and that pullbacks by coefficient maps commute with $d$. Let $R$ be a commutative ring, $X$ a separated scheme over $\operatorname{Spec} R$, $P$ a finite meet semilattice and $u$ an affine system on $X$ indexed by $P$. Then there are $R$-linear isomorphisms
$$H^0(F_u) \cong H^0(X, \mathcal{O}_X), \qquad H^{n+1}(F_u) \cong H^{n+1}(X, \mathcal{O}_X) \quad (n \geq 0),$$
where $H^n(F_u)$ is the cohomology of the cochain complex of Section 12.

Lean: `GlobalTheory.CompanionTheory.Hodge.Nerve.cmpSt_of_cxSt`.

The proof does not use the hypothesis on $d$ or the separatedness of $X$. The intersections in the cover are affine by the definition of an affine system, and this is what the comparison with sheaf cohomology needs.

*Proof.* Choose a bijection $e : \{1, \dots, m\} \to P$. The opens $U_i = u(e(i))$ cover $X$. For a nonempty set $t \subseteq \{1, \dots, m\}$, induction on $t$ with the rule $u(a \wedge b) = u(a) \cap u(b)$ gives
$$\bigcap_{i \in t} U_i = u\Big(\bigwedge_{i \in t} e(i)\Big),$$
so each finite intersection of the $U_i$ is affine.

For a functor $M$ from $P^{\mathrm{op}}$ to $R$-modules there are two complexes. The *nerve complex* has in degree $n$ the product of $M(c(n))$ over the $n$-chains $c$ of $P^{\mathrm{op}}$, as in Section 12. The *Čech complex* along $e$ has in degree $n$ the product of $M(e(i_0) \wedge \cdots \wedge e(i_n))$ over the strictly increasing sequences $i_0 < \cdots < i_n$, with the alternating sum of the restriction maps as differential.

*Step 1. The two complexes have the same homology.* For each $n$ and each $M$, the homology of the nerve complex of $M$ in degree $n$ is isomorphic to that of the Čech complex along $e$. In degree $0$ both are the limit of $M$ over $P^{\mathrm{op}}$, and the isomorphism is natural in $M$. Each $M$ embeds into a coinduced functor $M \to \prod_b M(b)$, with an exact sequence $0 \to M \to \prod_b M(b) \to Q \to 0$ that is exact at each object of $P^{\mathrm{op}}$. Both constructions take such sequences to short exact sequences of complexes, because they are products of evaluations. We take as given that both complexes of a coinduced functor are acyclic in positive degrees, and a statement on natural maps of such families: a natural isomorphism in degree $0$ between two families of homology modules with long exact sequences, both of which vanish on coinduced objects in positive degrees, extends to isomorphisms in all degrees. Together these give Step 1.

*Step 2. The Čech complex is the Čech complex of the cover.* We take as given that the Čech complex of the functor $F_u$, viewed as $R$-modules, along $e$ has the same homology as the Čech complex of $\mathcal{O}_X$ for the cover $(U_i)$.

*Step 3. Čech cohomology is sheaf cohomology.* We take as given that for a quasi-coherent sheaf and a finite cover by affine opens with affine finite intersections, Čech cohomology and sheaf cohomology agree in each degree. The structure sheaf is quasi-coherent, and the cover $(U_i)$ has the required property by the first paragraph.

*Step 4. The cohomology of Section 12 is the nerve homology.* We take as given that $H^0(F_u) = \ker(d : C^0 \to C^1)$ is isomorphic to the homology of the nerve complex of $F_u$ in degree $0$, and $H^{n+1}(F_u)$ to its homology in degree $n+1$. The two complexes are the same up to the indexing of the differential.

The composition of the isomorphisms of Steps 4, 1, 2 and 3 gives the theorem in each degree. $\square$

Steps 1 to 3 hold for each finite meet semilattice and each functor of sections of a quasi-coherent sheaf. Step 1 replaces the ordered Čech complex, which depends on the choice of $e$, by the nerve complex, which depends only on $P$. This is why Sections 12 and 13 can use chains in $P^{\mathrm{op}}$ and the product category $P^{\mathrm{op}} \times P^{\mathrm{op}}$, with no ordering of the cover.

**Remark 7.14.3 (Formalization).** The theorem is in [ExistsToCoindShortExact.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ExistsToCoindShortExact.lean#L87), and Step 1 is the lemma `nonempty_iso` in the same file. The statement `CmpSt` and the affine system `Sys` are in [H1CommutesBaseChange.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/HodgeWedgeFields/H1CommutesBaseChange.lean#L265). The theorem is stated as `CxSt → CmpSt`. Its proof starts with `intro _ R _ X s _ P _ _ S`, so it uses neither `CxSt` nor the hypothesis `IsSeparated s`. The isomorphisms are given as `Nonempty` of linear equivalences, with no compatibility with cup products or pullbacks. The inputs are `T.nerve_cech_degree_zero_compatible`, `T.natural_degree_zero_homology_iso`, `T.coinduced_nerve_acyclic`, `T.coinduced_cech_acyclic`, `T.cech_structure_sheaf_comparison`, `T.cochain_cohomology_nerve_homology_equiv` and `GlobalTheory.cechHEquivCoh`. In `CmpSt`, $H^0(F_u)$ is the kernel of `dn 0` and $H^{n+1}(F_u)$ is `Hs n`.

## Notes and references

The chapter feeds four parts of the proof. Sections 1 to 6 prove the existence theorem for closed subschemes and the algebraization of formal schemes with an ample line bundle, which give the [theorem on formal thickenings](/entry/formal-thickening-formal-algebraisation/). Sections 7, 8, 9 and 11 give the local facts on branches, multiplicities and masses that the Poincaré and Lelong formula needs; they are inputs of the [literature step](/step/every-character-of-literature/), through [Theorem 7.7.3](/entry/branch-proper-at-point/), [Theorem 7.9.4](/entry/local-order/) and [Theorem 7.11.4](/entry/reg-mass-near-small/). Section 10 proves that the integral of the top Chern form of a Fubini and Study metric is the self-intersection number, the input of the [Chern degree over the complex numbers](/entry/chern2-chern-degree-complex/). Sections 12 and 14 give the Hopf bound on the first cohomology and the comparison with the cohomology of the structure sheaf, inputs of the [row step](/step/every-character-of-row/). Section 13 gives the exterior square of the first cohomology, an input of the [list of chapters of the Hodge and de Rham proof](/entry/abelian-hodge-de-rham-prime/).

- A. Grothendieck, *Éléments de géométrie algébrique III: Étude cohomologique des faisceaux cohérents*, Première partie, Publ. Math. IHÉS 11 (1961), §5.1 and Théorème 5.1.4, for the existence theorem of Sections 1 to 4, and §5.4, for the algebraization of formal schemes of Sections 5 and 6.
- A. Grothendieck, *Éléments de géométrie algébrique II: Étude globale élémentaire de quelques classes de morphismes*, Publ. Math. IHÉS 8 (1961), Théorème 5.6.1, for Chow's lemma, used in the reduction to the projective case of Sections 2 and 3.
- L. Illusie, *Grothendieck's existence theorem in formal geometry*, Chapter 8 of B. Fantechi, L. Göttsche, L. Illusie, S. Kleiman, N. Nitsure and A. Vistoli, *Fundamental Algebraic Geometry: Grothendieck's FGA Explained*, Math. Surveys Monogr. 123, AMS, 2005, for a modern account of Sections 1 to 6.
- R. Hartshorne, *Algebraic Geometry*, Grad. Texts in Math. 52, Springer, 1977, Chapter III, §4, for the comparison of Čech cohomology and sheaf cohomology used in Section 14, and Chapter III, §11, for the theorem on formal functions behind the existence theorem.
