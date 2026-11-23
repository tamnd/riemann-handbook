---
title: The Hilbert scheme of a finite flat morphism
decls:
  - GlobalTheory.T.hilbertScheme_finite_locallyFree_representable_proper
  - GlobalTheory.HilbertSch.main
  - GlobalTheory.T.exists_local_spec_finite_free_of_finite_flat
  - GlobalTheory.T.isHilbertSchemeRepresentable_of_iso
  - GlobalTheory.HilbGlue.isSheaf_hilbFunctor
  - GlobalTheory.T.isHilbertSchemeRepresentable_of_open_cover
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hilbert scheme of a finite flat morphism

This section proves that every finite, flat morphism $z : Z \to S$ of finite presentation has a Hilbert scheme of every rank $r$, in the sense of the Definition of section 14. Locally on $S$ the morphism is $\operatorname{Spec} B \to \operatorname{Spec} A$ with $B$ free of finite rank over $A$, and there [the affine theorem](/entry/hilbert-scheme-finite-free-algebra-affine-exists/) of section 15 applies. The Hilbert functor of $z$ is a Zariski sheaf, so the local Hilbert schemes glue. The result is the input of [Theorem 6.1.7](/entry/exists-clop-rep-of-rank-of-locally-noetherian/), which classifies the clopen subschemes of rank $r$ of a finite étale cover and leads to [the finite étale scheme of clopen subschemes](/entry/exists-finite-etale-representing-clopen-subschemes/).

We keep the notation of section 14. For a morphism $g : T \to S$ we write $Z_T = Z \times_S T$, and for an open $W \subseteq S$ we write $z|_W : z^{-1}(W) \to W$ for the restriction.

**Definition 2.16.1 (Hilbert functor of a morphism).** Let $z : Z \to S$ be a morphism and $r \geq 0$. For a scheme $T$ let $\operatorname{Hilb}^r_z(T)$ be the set of pairs $(g, V)$ of a morphism $g : T \to S$ and a closed subscheme $V \subseteq Z_T$ that is finite, flat and of rank $r$ over $T$. Pullback along $a : T' \to T$ is $(g, V) \mapsto (g \circ a, (1 \times a)^{-1}(V))$.

Lean: `GlobalTheory.HilbGlue.hilbFunctor`.

For $z = (\operatorname{Spec} B \to \operatorname{Spec} A)$ this is the functor $\operatorname{Hilb}^r$ of section 14. A Hilbert scheme $(H, h, u)$ of rank $r$ for $z$ represents $\operatorname{Hilb}^r_z$, with universal element $(h, U)$, and $h$ is proper.

**Lemma 2.16.2 (Local structure of finite flat morphisms).** Let $z : Z \to S$ be finite, flat and locally of finite presentation, and let $s \in S$. There are an open $W \ni s$, a ring $A$, an $A$-algebra $B$ that is free of finite rank as an $A$-module, and isomorphisms $W \cong \operatorname{Spec} A$ and $z^{-1}(W) \cong \operatorname{Spec} B$ under which $z|_W$ becomes $\operatorname{Spec} B \to \operatorname{Spec} A$.

Lean: `GlobalTheory.T.exists_local_spec_finite_free_of_finite_flat` (also `GlobalTheory.FiniteFlatLocal.exists_finFree_local`).

*Proof.* Choose an affine open $\operatorname{Spec} R \ni s$ with prime $\mathfrak{p}$. Since $z$ is finite, $z^{-1}(\operatorname{Spec} R) = \operatorname{Spec} M$ with $M$ a finite $R$-algebra, and $M$ is flat and of finite presentation over $R$. The module $M_{\mathfrak{p}}$ is free (Matsumura, Theorem 7.10). A basis of $M_{\mathfrak{p}}$ comes from finitely many elements of $M$, and since $M$ is finite and of finite presentation, the map from the free module on these elements to $M$ becomes bijective after we invert some $f \notin \mathfrak{p}$. Take $W = D(f)$, $A = R_f$ and $B = M_f$. $\square$

**Lemma 2.16.3 (Transport along isomorphisms).** Let $z : Z \to S$ and $z' : Z' \to S'$ be morphisms, and let $S' \cong S$ and $Z' \cong Z$ be isomorphisms that are compatible with $z$ and $z'$. If $z'$ has a Hilbert scheme of rank $r$, then so does $z$.

Lean: `GlobalTheory.T.isHilbertSchemeRepresentable_of_iso` (also `GlobalTheory.HilbertSch.isHilbRep_transfer`).

*Proof.* Let $(H, h', u')$ be a Hilbert scheme for $z'$. Compose $h'$ with $S' \cong S$, and identify $Z' \times_{S'} H$ with $Z \times_S H$ by the isomorphism $Z' \cong Z$. A closed subscheme of $Z \times_S T$ is the same as a closed subscheme of $Z' \times_{S'} T$ under these identifications, so the universal property carries over. $\square$

**Lemma 2.16.4 (Sheaf property).** For every morphism $z$ and every $r$, the functor $\operatorname{Hilb}^r_z$ is a sheaf for the Zariski topology.

Lean: `GlobalTheory.HilbGlue.isSheaf_hilbFunctor`.

*Proof.* Let $(T_i)$ be an open cover of $T$ and let $(g_i, V_i)$ be pairs over $T_i$ that agree on the overlaps. The maps $g_i$ glue to $g : T \to S$. The closed subschemes $V_i \subseteq Z_{T_i}$ agree on overlaps, so they glue to a closed subscheme $V \subseteq Z_T$, and $V$ is finite, flat and of rank $r$ over $T$ since these conditions are local on $T$. Two pairs that agree on every $T_i$ are equal, since morphisms and closed subschemes are determined locally. $\square$

**Lemma 2.16.5 (Gluing).** Let $z : Z \to S$ be finite, flat and locally of finite presentation, and let $r \geq 0$. Suppose that every $s \in S$ has an open neighbourhood $W$ such that $z|_W$ has a Hilbert scheme of rank $r$. Then $z$ has a Hilbert scheme of rank $r$.

Lean: `GlobalTheory.T.isHilbertSchemeRepresentable_of_open_cover` (also `GlobalTheory.HilbGlue.isHilbRep_of_cover`).

*Proof.* Let $(H_W, h_W, u_W)$ be a Hilbert scheme for $z|_W$. A pair $(g, V) \in \operatorname{Hilb}^r_z(T)$ with $g(T) \subseteq W$ is the same as a pair for $z|_W$, since $Z \times_S T = z^{-1}(W) \times_W T$. So $H_W$, with the composite $H_W \to W \subseteq S$, represents the subfunctor of $\operatorname{Hilb}^r_z$ of pairs whose map to $S$ lands in $W$. This subfunctor is the inverse image of the open $W$ under the map $\operatorname{Hilb}^r_z \to S$, $(g, V) \mapsto g$. The functor $\operatorname{Hilb}^r_z$ is a Zariski sheaf, by the last Lemma, and the opens $W$ cover $S$. So the schemes $H_W$ glue to a scheme $H$ that represents $\operatorname{Hilb}^r_z$, and the inverse image of $W$ in $H$ is $H_W$. Let $(h, U)$ be the universal element. The morphism $h : H \to S$ is proper over each $W$ of the cover, since $h^{-1}(W) \cong H_W$ and $h_W$ is proper. Properness is local on the target, so $h$ is proper. Finally, for $f : T \to H$ with $h \circ f = g$, the pullback of $(h, U)$ along $f$ equals $(g, V)$ if and only if $(1 \times f)^{-1}(U) = V$, and this holds if and only if there is $w : V \to U$ that makes the square of the Definition of a Hilbert scheme cartesian. So $(H, h, U)$ is a Hilbert scheme of rank $r$ for $z$. $\square$

**Theorem 2.16.6 (Hilbert scheme of points).** Let $z : Z \to S$ be finite, flat and locally of finite presentation, and let $r \geq 0$. Then $z$ has a Hilbert scheme of rank $r$. So there are a proper morphism $h : H \to S$ and a closed subscheme $U \subseteq Z \times_S H$, finite and flat of rank $r$ over $H$, such that for every scheme $T$, every $g : T \to S$ and every closed subscheme $V \subseteq Z \times_S T$ that is finite and flat of rank $r$ over $T$, there is exactly one $f : T \to H$ with $h \circ f = g$ and $(1 \times f)^{-1}(U) = V$.

Lean: `GlobalTheory.T.hilbertScheme_finite_locallyFree_representable_proper` (also `GlobalTheory.HilbertSch.main`).

*Proof.* We apply the Lemma on gluing. Let $s \in S$. The Lemma on local structure gives an open $W \ni s$ and isomorphisms that identify $z|_W$ with $\operatorname{Spec} B \to \operatorname{Spec} A$, where $B$ is free of finite rank over $A$. By [the affine theorem](/entry/hilbert-scheme-exists/), $\operatorname{Spec} B \to \operatorname{Spec} A$ has a Hilbert scheme of rank $r$. By the Lemma on transport, so does $z|_W$. $\square$

**Remark 2.16.7.** A finite flat morphism of finite presentation is the same as a finite locally free morphism. Grothendieck constructs Hilbert schemes for projective morphisms over a noetherian base (Séminaire Bourbaki, Exposé 221), and over a noetherian $S$ the theorem is a special case. For a finite locally free morphism one can also represent the functor by a closed subscheme of the Grassmannian of locally free quotients of rank $r$ of $z_*\mathcal{O}_Z$, which makes $H$ projective over $S$. The statement here gives properness only, which is what [Theorem 6.1.7](/entry/exists-clop-rep-of-rank-of-locally-noetherian/) uses, and it puts no noetherian hypothesis on $S$.

**Remark 2.16.8 (Formalization).** The theorem states the universal property in full, although [HilbertSchemeFiniteLocallyFreeRepresentablePrope.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HilbertSchemeFiniteLocallyFreeRepresentablePrope.lean#L17) imports the definition `IsHilbRep` and the lemmas that it applies return `IsHilbRep`. The module name is cut off after "Prope". In [IsHilbertSchemeRepresentableOfOpenCover.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsHilbertSchemeRepresentableOfOpenCover.lean#L27) the hypotheses that $z$ is finite, flat and of finite presentation are introduced without names. We did not check whether instance search uses them. The gluing step uses a representability lemma for sheaves covered by local representing objects, `GlobalTheory.GenTorsor.isRepresentable_of_cover`, from a module named `JetHarmonics.IsRepresentableOfCover`. The Lemma on local structure rests on `GlobalTheory.FiniteAmpleFP.exists_finFree_app_fp` in a module named `RelAmpleDiagonalDescendedBundleGaloisCover`. Neither name describes the statement. The statement files of this section import Mathlib twice and try the target in three ways (`first | exact @X | exact X | ...`).

## Notes and references

The chapter feeds three parts of the proof. The projective bundle formula of sections 1 to 3, the vanishing of $H^1$ of sections 4 and 5, and the results on the cohomology of curves, fields, the punctured line, coefficients and polynomial rings of sections 9 to 13 are inputs of [the theorem on the local steps](/entry/steps-holds/) of [the Galois row](/proof/galois-row/). Sections 6 to 8 prove [the theorem on étale enlargement](/entry/etale-enlarge-by-uniformiser-roots/), the last step of the enlargement to a good model. Sections 14 to 16 give the Hilbert scheme of points that [Theorem 6.1.7](/entry/exists-clop-rep-of-rank-of-locally-noetherian/) uses to classify clopen subschemes of a finite étale cover.

The projective bundle formula for schemes is in SGA 5 and in Milne's book. Here it is proved for vector bundles on simplicial presheaves, by reduction to constant spaces and the Eilenberg-Zilber theorem. The vanishing of $H^1$ on the generic fibre of a strict henselisation is the degree one case of the local acyclicity of smooth morphisms in SGA 4, Exposé XV, proved here directly from torsors and the Picard group. Abhyankar's lemma and the purity of the branch locus are in SGA 1. The proof of purity here is the induction on dimension with depth and a discriminant. The vanishing of $H^2$ of affine curves and the cohomology of the punctured line follow in general from Artin's theorem on the cohomological dimension of affine schemes; here they are proved by elementary means. The Hilbert scheme is Grothendieck's. Here it is constructed only for finite flat morphisms, by charts and the valuative criterion, and not through the Grassmannian.

- A. Grothendieck, *Revêtements étales et groupe fondamental* (SGA 1), Exposé X, Théorème 3.1 (purity of the branch locus), and Exposé XIII, Lemme 5.2 (Abhyankar's lemma).
- M. Artin, A. Grothendieck and J.-L. Verdier, *Théorie des topos et cohomologie étale des schémas* (SGA 4), Exposé VII, §5 (filtered colimits), Exposé VIII, §2 (sheaves on the spectrum of a field), Exposé XIV, §3 (cohomological dimension of affine schemes), and Exposé XV, §2 (local acyclicity and homotopy invariance).
- A. Grothendieck et al., *Cohomologie $\ell$-adique et fonctions L* (SGA 5), Exposé VII (the projective bundle formula and Chern classes).
- A. Grothendieck and J. Dieudonné, *Éléments de géométrie algébrique* IV, Quatrième partie, §18.8 (strict henselisation).
- A. Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: Les schémas de Hilbert*, Séminaire Bourbaki, Exposé 221, 1960/61.
- N. Nitsure, *Construction of Hilbert and Quot schemes*, in B. Fantechi et al., *Fundamental Algebraic Geometry: Grothendieck's FGA Explained*, Mathematical Surveys and Monographs 123, AMS, 2005, Chapter 5.
- J. S. Milne, *Étale Cohomology*, Chapter II, §2 (the Kummer sequence), Chapter III, §4 and Proposition 4.9 (torsors and the Picard group), and Chapter VI, §10 (the projective bundle formula).
- J.-P. Serre, *Galois Cohomology*, Chapter I, §2 to §4 (cohomology of profinite groups and cohomological dimension), and Chapter II, §2 and §3 (cohomological dimension of fields, and Tsen's theorem in §3.3).
- S. Eilenberg and J. A. Zilber, "On products of complexes", *Amer. J. Math.* 75 (1953).
- P. G. Goerss and J. F. Jardine, *Simplicial Homotopy Theory*, Chapter IV, §2.
- H. Matsumura, *Commutative Ring Theory*, Theorem 7.10 (finite flat modules over local rings are free), Theorem 19.1 (Auslander-Buchsbaum formula) and Theorem 23.8 (Serre's criterion of normality).
- R. Hartshorne, *Algebraic Geometry*, Theorem II.4.7 (valuative criterion of properness).
- The Stacks Project, chapter *Morphisms of Schemes*, section *Valuative criteria*.
