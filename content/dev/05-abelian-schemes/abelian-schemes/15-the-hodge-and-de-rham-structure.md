---
title: The Hodge and de Rham structure
decls:
  - GlobalTheory.AbCoh.abelianHodgeDeRham
  - MainStatements.Hodge.Free.abelianHodgeDeRham
  - MainStatements.Hodge.Free.abelianHodgeDeRham'
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hodge and de Rham structure

The section on square zero lifts took the Hodge and de Rham structure as an input. This section proves it (Theorem (Hodge and de Rham structure)). For an [[abelian scheme|JDDXZ89N33]] $A$ over any ring $R$, [[smooth|EXKGG9X6J0]] of relative dimension $g$, the first de Rham cohomology is finite projective of rank $2g$, the Hodge to de Rham sequence in degree 1 is exact with projective terms of rank $g$, all of it commutes with base change, and $H^2_{\mathrm{dR}}$ is the second exterior power of $H^1_{\mathrm{dR}}$. Over a field of characteristic 0 these facts follow from Hodge theory. Over a general base they are a theorem of the type proved in Berthelot, Breen and Messing (see the Notes and references). The theorem is used in [Lifting along nilpotent divided powers](/entry/abelian-scheme-hom-lifting-nilpotent-divided-powers/) and in the de Rham structure of the next section, on the way to [EveryCharacter](/step/every-character/).

As in the earlier sections, the cohomology of a scheme $X$ over $R$ is computed on the category of affine opens of $X$. The structure cohomology $H^i(X, \mathcal{O})$ is that of the functor $U \mapsto \mathcal{O}(U)$. The *de Rham cohomology* $H^i_{\mathrm{dR}}(X)$, for $i = 1, 2$, is the hypercohomology of the de Rham complex $\mathcal{O} \to \Omega^1 \to \Omega^2$ of this functor, computed from the Čech double complex. A class in $H^1_{\mathrm{dR}}(X)$ is given by a pair $(c, \omega)$: functions $c_{UV}$ on pairs $V \subset U$ with the Čech cocycle rule, and 1-forms $\omega_U$ with $d\omega_U = 0$ and $\omega_V - \omega_U|_V = d c_{UV}$. There are a cup product $H^1_{\mathrm{dR}} \times H^1_{\mathrm{dR}} \to H^2_{\mathrm{dR}}$, a map $\mathrm{cl}$ from closed global 1-forms to $H^1_{\mathrm{dR}}(X)$, $\omega \mapsto (0, \omega)$, and a map $H^1_{\mathrm{dR}}(X) \to H^1(X, \mathcal{O})$, $(c, \omega) \mapsto c$. We write $\Omega(X)$ for the $R$-module of global 1-forms.

We use the definition of the *Hodge and de Rham structure* in the section on square zero lifts. We restate it in the form that we prove. For a cartesian square with $X' = A \times_R R'$, pullback gives maps on $H^1_{\mathrm{dR}}$, on $\Omega$ and on $H^1(\mathcal{O})$, and *commutes with base change* means that the induced map $R' \otimes_R M(A) \to M(X')$ is an isomorphism, as in the section on the cohomology of the structure sheaf.

**Theorem 1.15.1 (Hodge and de Rham structure).** Let $R$ be a ring and $A$ an abelian scheme over $R$, smooth of relative dimension $g$. Then:

1. $H^1_{\mathrm{dR}}(A)$ is a finite projective $R$-module of rank $2g$ at each prime, and there is an isomorphism $e : \bigwedge^2_R H^1_{\mathrm{dR}}(A) \to H^2_{\mathrm{dR}}(A)$ with $e(a \wedge b) = a \cup b$;
2. $\Omega(A)$ and $H^1(A, \mathcal{O})$ are finite projective of rank $g$;
3. every global 1-form is closed, the map $\mathrm{cl} : \Omega(A) \to H^1_{\mathrm{dR}}(A)$ is injective, and $H^1_{\mathrm{dR}}(A) \to H^1(A, \mathcal{O})$ is surjective;
4. for every $R$-algebra $R'$ and every cartesian square with $X' = A \times_R R'$, the modules $H^1_{\mathrm{dR}}$, $\Omega$ and $H^1(\mathcal{O})$ commute with base change.

Lean: `GlobalTheory.AbCoh.abelianHodgeDeRham`, `MainStatements.Hodge.Free.abelianHodgeDeRham` (a second proof, see the Remark below).

The rank conditions say that the sequence
$$0 \to \Omega(A) \xrightarrow{\ \mathrm{cl}\ } H^1_{\mathrm{dR}}(A) \to H^1(A, \mathcal{O}) \to 0$$
consists of finite projective modules of ranks $g$, $2g$ and $g$, with the first map injective and the last surjective. The theorem does not assert exactness in the middle.

We use the following facts. In each, $A$ is an abelian scheme over a ring $R$, smooth of relative dimension $g$.

1. (Frame.) The differentials of $A$ have a frame of global 1-forms, and global functions are constant: $R \to H^0(A, \mathcal{O})$ is bijective. This is fact 8 of the section on the cohomology of the structure sheaf, apart from primitivity.
2. (Structure cohomology.) $A$ has the structure cohomology of dimension $g$. This is fact 7 of that section.
3. (Closed forms.) Every global 1-form on $A$ is closed.
4. (Surjectivity.) The map $H^1_{\mathrm{dR}}(A) \to H^1(A, \mathcal{O})$ is surjective.
5. (Rank.) $H^1_{\mathrm{dR}}(A)$ is finite projective of rank $2g$, and each class $x$ in it is primitive: $m^* x = p_1^* x + p_2^* x$.
6. (Cup squares.) $a \cup a = 0$ for each $a \in H^1_{\mathrm{dR}}(A)$.
7. (Forms.) $\Omega(A)$ is finite projective of rank $g$.
8. (Base change of de Rham cohomology and forms.) $H^1_{\mathrm{dR}}$ and $\Omega$ commute with base change for $A$.
9. (Exterior square.) Let $F$ be a functor from a category to $R$-algebras, such that the differentials of $F$ have a frame of global 1-forms, the global functions of $F$ are the constants, every global 1-form of $F$ is closed, $H^1_{\mathrm{dR}}(F) \to H^1(F)$ is surjective, $H^2(F) \cong \bigwedge^2 H^1(F)$ by cup product, and $a \cup a = 0$ for each $a \in H^1_{\mathrm{dR}}(F)$. Then cup product gives an isomorphism $\bigwedge^2 H^1_{\mathrm{dR}}(F) \cong H^2_{\mathrm{dR}}(F)$.

Fact 9 is a statement in homological algebra on the Čech double complex. The idea is that with a frame of closed forms and constant global functions, the Hodge to de Rham spectral sequence degenerates in low degrees, and $H^2_{\mathrm{dR}}$ is then assembled from $\bigwedge^2 \Omega$, $\Omega \otimes H^1(\mathcal{O})$ and $\bigwedge^2 H^1(\mathcal{O}) \cong H^2(\mathcal{O})$, as is $\bigwedge^2 H^1_{\mathrm{dR}}$.

*Proof.* Part 1. By fact 5, $H^1_{\mathrm{dR}}(A)$ is finite projective of rank $2g$. For the exterior square, apply fact 9 to the functor $U \mapsto \mathcal{O}(U)$ on affine opens of $A$. Its hypotheses are: the frame and the constant functions (fact 1), closed forms (fact 3), surjectivity (fact 4), $H^2(A, \mathcal{O}) \cong \bigwedge^2 H^1(A, \mathcal{O})$ (condition 2 of the structure cohomology, by fact 2) and cup squares (fact 6). So $e$ exists.

Part 2. $\Omega(A)$ is finite projective of rank $g$ by fact 7, and $H^1(A, \mathcal{O})$ is by condition 1 of the structure cohomology (fact 2).

Part 3. Closedness is fact 3 and surjectivity is fact 4. For injectivity, let $\omega$ be a global 1-form with $\mathrm{cl}(\omega) = 0$. Then $(0, \omega)$ is the coboundary of a 0-cochain $(f_U)$: $f_V - f_U|_V = 0$ for $V \subset U$ and $df_U = \omega|_U$. The first condition says that the $f_U$ glue to a global function $f$. By fact 1, $f$ is a constant $r \in R$, so $\omega = df = 0$.

Part 4. $H^1_{\mathrm{dR}}$ and $\Omega$ commute with base change by fact 8, and $H^1(\mathcal{O})$ does by condition 3 of the structure cohomology (fact 2). In each case the isomorphism sends $1 \otimes c$ to the pullback of $c$. $\square$

The second statement of fact 5, that all classes in $H^1_{\mathrm{dR}}(A)$ are primitive, is not part of the theorem. It is part (a) of the de Rham structure of the next section.

**Remark 1.15.2 (Formalization).** The theorem is `GlobalTheory.Published.AbelianHodgeDeRham` ([AbelianHodgeDeRham.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/AbelianHodgeDeRham.lean#L15)). Facts 1 to 9 are `GlobalTheory.T.abelianScheme_oneFormFrame_and_square` (which also says that $A \times A$ is abelian of relative dimension $g + g$), `GlobalTheory.T.abelian_structure_cohomology_statement`, `GlobalTheory.T.abelianScheme_globalOneForms_closed`, `GlobalTheory.T.de_rham_to_structure_h1_surjective`, `GlobalTheory.T.de_rham_h1_rank_primitive`, `GlobalTheory.T.cup_self_zero_de_rham_abelian`, `GlobalTheory.T.abelianScheme_global_oneForms_projective_rank`, `GlobalTheory.T.de_rham_global_forms_base_change` and `GlobalTheory.T.hyper_h2_exterior_square_iso`. They are cited by their statements; the sentence on why fact 9 holds is not read from its proof. Injectivity of $\mathrm{cl}$ is `GlobalTheory.ofForm_injective_of_H0Const`. The statement is proved twice. The second proof, `MainStatements.Hodge.Free.abelianHodgeDeRham` ([AbelianHodgeDeRham.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/AbelianDeRham/AbelianHodgeDeRham/AbelianHodgeDeRham.lean#L107)), applies `Chapters.print` to `MainStatements.Hodge.Free.abelianHodgeDeRham'`, a proof of the structure `Chapters` ([Development.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/AbelianDeRham/AbelianHodgeDeRham/Development.lean#L13)). This structure has 47 fields, each an implication between intermediate statements: Čech complexes and homotopies, descent and base change for systems of affine opens, perfectness of the Čech complex, the rank of $H^1(\mathcal{O})$ over a field (at most $g$ and at least $g$), base change and the wedge isomorphism, 1-forms, and a final field that gives the theorem. `Chapters.print` also takes five more inputs: the spreading out of schemes and of smooth and of proper morphisms, and the statements `TrivLocus` and `KFinite` on the trivial locus of a line bundle; these were not unfolded. The two proofs are independent; the proof of the next section uses the second, and [Lifting along nilpotent divided powers](/entry/abelian-scheme-hom-lifting-nilpotent-divided-powers/) uses the first through its second name `GlobalTheory.T.abelianScheme_deRham_locallyFree_hodgeDegenerates`.
