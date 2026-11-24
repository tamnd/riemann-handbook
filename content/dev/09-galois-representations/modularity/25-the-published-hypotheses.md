---
title: The published hypotheses
decls:
  - UpperTheory.V.Z.Coh.clozelConjC
  - UpperTheory.V.Z.Bc.cycC_of_fin_js
  - UpperTheory.V.Z.Bc.cycC_holds
  - UpperTheory.One.Join.cm_abelian_inputs_from_literature
  - UpperTheory.V.HV.DescentVanishingReductions.published_hypotheses_from_patching_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The published hypotheses

Most theorems of this chapter assume the extended hypotheses: a list of results of the literature on automorphic representations and their Galois representations. This section shows that the list follows from two inputs, the literature hypotheses in rank $n$ and a weak form of descent for unitary groups. The other items are proved here or in earlier sections: Clozel's theorem on the conjugates of cohomological representations, cyclic base change of prime degree over a totally imaginary field, quadratic base change for $\mathrm{GL}_2$ (section 23) and the rank two descent of section 24. We also show that the CM inputs of the literature follow from the open image condition. The result feeds [the published inputs](/proof/literature/) of the proof.

For a number field $F$ and $n \ge 1$, a cuspidal system of rank $n$ over $F$ is a cuspidal representation of $\mathrm{GL}_n(\mathbb{A}_F)$, given through its Satake parameters $\mathrm{sat}(v)$ at the finite places and its infinitesimal characters at the archimedean places. We use the notions of [base change](/learn/automorphic-forms/#base-change) and of regular algebraic representations from the Background.

**Theorem 8.25.1 (Clozel's conjugation theorem).** Let $E$ be a totally imaginary number field, $n \ge 1$, $\pi$ a regular algebraic cuspidal representation of $\mathrm{GL}_n(\mathbb{A}_E)$ and $\sigma \in \mathrm{Aut}(\mathbb{C})$. Then there are a cuspidal $\pi'$ of $\mathrm{GL}_n(\mathbb{A}_E)$, an irreducible constituent $\tau$ of the finite part of $\pi$ and an irreducible constituent $\tau'$ of the finite part of $\pi'$ with $\tau' \cong {}^{\sigma} \tau$, such that for each embedding $\varphi \colon E \to \mathbb{C}$, if $\pi$ has infinitesimal character $m$ at $\varphi$, then $\pi'$ has infinitesimal character $m$ at $\sigma \circ \varphi$.

Lean: `UpperTheory.V.Z.Coh.clozelConjC`.

*Proof.* This is Clozel's theorem [Clozel, *Motifs et formes automorphes*, Theorem 3.13], and the proof follows his. Since $\pi$ is regular algebraic, it is cohomological: there is an algebraic representation $\Xi$ of $\mathrm{GL}_n$ such that $\pi_f$ contributes to the cohomology of the locally symmetric spaces with coefficients in $\Xi$. The cuspidal cohomology injects into the full cohomology (Borel), through harmonic forms and the rapid decay of cusp forms. The cohomology has a rational structure, and $\sigma$ maps the cohomology with coefficients $\Xi$ to the cohomology with coefficients ${}^{\sigma}\Xi$, and the $\pi_f$-part to a ${}^{\sigma}\pi_f$-part. There is no Eisenstein class with the Hecke eigenvalues of ${}^{\sigma}\tau$, so this part is cuspidal and comes from a cuspidal $\pi'$, whose infinitesimal character is given by ${}^{\sigma}\Xi$. $\square$

Now let $K$ be a totally imaginary field and $M/K$ a Galois extension of prime degree $p$. A Hecke character $\eta \ne 1$ of $K$ is a character of $M/K$ if $\eta^{p} = 1$ and $\eta(v)^{f} = 1$ at almost all $v$ where a place of $M$ above $v$ has norm $(N v)^{f}$. A system $\mathrm{sat}$ over $K$ is self-twisted by $\eta$ if at almost all $v$ the multiset $\mathrm{sat}(v)$ is invariant under multiplication by $\eta(v)$. A system $\mathrm{sat}'$ over $M$ is a weak base change of $\mathrm{sat}$ if at almost all places $w$ of $M$ with $N w = (N v)^{f}$,

$$\mathrm{sat}'(w) = \{ \alpha^{f} : \alpha \in \mathrm{sat}(v) \}.$$

**Definition 8.25.2 (Cyclic base change).** Cyclic base change holds if, for all $K$, $M$ and $n$ as above, three things hold.

1. (Lift.) Each regular algebraic cuspidal system $\mathrm{sat}$ over $K$ is self-twisted by a character of $M/K$, or has a cuspidal weak base change $\mathrm{sat}'$ over $M$ whose infinitesimal character at each $\tau$ is that of $\mathrm{sat}$ at the place below.
2. (Descent.) Each regular algebraic cuspidal system $\mathrm{sat}'$ over $M$ whose Satake parameters agree at the places above the same place of $K$, at almost all places, is a weak base change of a cuspidal system over $K$ with the same infinitesimal characters.
3. (Fibres.) If two cuspidal systems $\mathrm{sat}$ and $\mathrm{sat}_1$ over $K$ have the same cuspidal weak base change, then at almost all $v$, $\mathrm{sat}_1(v) = \eta(v)\, \mathrm{sat}(v)$ for some $\eta$ that is $1$ or a character of $M/K$.

These are the three statements of Arthur and Clozel for the base change of $\mathrm{GL}_n$ along a cyclic extension of prime degree, written with Satake parameters only.

**Theorem 8.25.3 (Cyclic base change from the literature).** Assume the finiteness of automorphic forms on $\mathrm{GL}_n$ and the rigidity theorem of Jacquet and Shalika. Assume the base change of Arthur and Clozel in the following form: for $K$, $M$, $n$ as above, each regular algebraic cuspidal $\pi$ over $K$ satisfies $\pi \otimes \eta \cong \pi$ for a character $\eta$ of $M/K$, or has a cuspidal weak base change with the same infinitesimal characters; each regular algebraic cuspidal $P$ over $M$ with $P^{\sigma} \cong P$ for each $\sigma \in \mathrm{Gal}(M/K)$ is a weak base change of a cuspidal $\pi$ with the same infinitesimal characters; and two cuspidal $\pi$, $\pi_1$ with the same weak base change $P$, with $P$ Galois invariant, satisfy $\pi_1 \cong \pi \otimes \eta$ with $\eta = 1$ or a character of $M/K$. Then cyclic base change holds.

Lean: `UpperTheory.V.Z.Bc.cycC_of_fin_js`.

*Proof.* Each cuspidal system comes from a cuspidal representation. The lift statement follows from the first assumption: if $\pi \otimes \eta \cong \pi$, then the Satake parameters at almost all $v$ satisfy $\mathrm{sat}(v) = \eta(v)\, \mathrm{sat}(v)$, since $\pi$ has Satake parameters at almost all places (the finiteness of automorphic forms) and they are unique. For the descent and the fibres we must show that a cuspidal $P$ over $M$ whose Satake parameters agree at conjugate places is isomorphic to each conjugate $P^{\sigma}$. The conjugate $P^{\sigma}$ is a cuspidal representation, and its Satake parameter at $w$ is that of $P$ at $\sigma^{-1} w$, a place above the same place of $K$ with the same norm. So $P$ and $P^{\sigma}$ have the same Satake parameters at almost all places, and $P^{\sigma} \cong P$ by strong multiplicity one, which is the rigidity theorem of Jacquet and Shalika over a totally imaginary field and the strong multiplicity one theorem over a totally real field. For the fibres, a weak base change has Satake parameters at the places above $v$ determined by $\mathrm{sat}(v)$, so it is conjugation invariant. Then the second and third assumptions give the descent and the fibres, and the isomorphism $\pi_1 \cong \pi \otimes \eta$ gives $\mathrm{sat}_1(v) = \eta(v)\, \mathrm{sat}(v)$ at almost all $v$. $\square$

**Theorem 8.25.4 (Cyclic base change).** Cyclic base change holds.

Lean: `UpperTheory.V.Z.Bc.cycC_holds`.

*Proof.* The finiteness of automorphic forms on $\mathrm{GL}_n$ and the rigidity of Jacquet and Shalika are proved in the development. The base change of Arthur and Clozel is proved in the development in a stronger form, which also gives the local lifts at split places and the absence of self-twists in the descent; forgetting these parts gives the form above. So the [Theorem 8.25.3](/entry/cyc-c-of-fin-js/) applies. $\square$

**Theorem 8.25.5 (Extended hypotheses from the literature).** Assume the literature hypotheses in rank $n$ and the weak descent for unitary groups. Then the extended hypotheses hold.

Lean: `UpperTheory.V.HV.DescentVanishingReductions.published_hypotheses_from_patching_alt`.

*Proof.* We list the items and their sources.

1. The literature hypotheses in rank $n$ are the first item.
2. The cohomology of cuspidal representations over CM fields (Clozel) follows from the literature hypotheses.
3. The conjugation of cohomological representations is the [Theorem 8.25.1](/entry/clozel-conj-c/) of Clozel above.
4. The injectivity of cuspidal cohomology into the full cohomology (Borel) is proved in the development.
5. The Galois representations of regular algebraic cuspidal representations of $\mathrm{GL}_2$ over a totally real field follow from the literature hypotheses, the [Theorem 8.23.11](/entry/quad-bc2/) on quadratic base change of section 23 and admissibility over totally real fields.
6. Strong multiplicity one, the theorem of Gelfand and Kazhdan and admissibility over totally real fields are proved in the development.
7. Quadratic base change in the form of the literature follows from the theorem of section 23.
8. The newform theory follows from the semisimplicity of the cuspidal spectrum and admissibility.
9. The weak descent for unitary groups is the second assumption.
10. Cyclic base change is the [Theorem 8.25.4](/entry/cyc-c-holds/) above.
11. The descent in rank two is the [Theorem 8.24.7](/entry/desc-s/) of section 24.
12. The existence of definite quaternion algebras and the semisimplicity of the cuspidal spectrum over totally real fields are proved in the development. $\square$

The CM inputs are the results on abelian varieties with complex multiplication and on Hecke characters that the proof uses through [the CM inputs](/step/cm-abelian-inputs-from-literature/).

**Theorem 8.25.6 (CM inputs from the literature).** Assume the open image condition. Then the following hold: the deformation theory of Grothendieck for abelian schemes, the de Rham cohomology of abelian schemes, the dual crystal of an abelian scheme, the comparison of periods, the periods of the Gauss-Manin connection, the theorem of Serre and Tate on good reduction, the main theorem of complex multiplication for elliptic curves, the generation of the Hilbert class field by $j$, the theorem of Siegel and Klingen with that of Deligne and Ribet, the functional equation of partial zeta functions, and the functional equation of Hecke and Tate.

Lean: `UpperTheory.One.Join.cm_abelian_inputs_from_literature`.

*Proof.* Each item is a theorem of the literature that is proved in the development. The theorem of Deligne and Ribet, with the theorem of Siegel and Klingen, gives the combined statement. The dual crystal comes from the dual abelian scheme and the crystalline lifts. $\square$

**Remark 8.25.7 (Formalization).** The conjugation theorem gives only some irreducible constituent $\tau$ of the finite part of $\pi$, not the finite part itself ([GelfandKazhdanReal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PublishedTheorems/GelfandKazhdanReal.lean#L26)). Its proof combines named steps (Jacquet-Shalika rigidity, cohomology, harmonic forms, rapid decay, the absence of Eisenstein classes) through `clozelConjC_of_steps`, which we have not unfolded; our sketch reads the names. A cuspidal system is a sum of a totally imaginary and a totally real case, and the private lemma `smo0` ([CycFree.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/BaseChangeUnits/CycFree.lean#L13)) closes the two mixed cases by the contradiction that a field is both totally real and totally complex. The hypothesis of the CM theorem is not used: each lemma `*_of_open` that it calls ignores the open image condition and returns a theorem proved without it ([TemperedProductOfSquareIntegrable.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean#L209)). The descent in rank two enters as the first alternative of a disjunction (`Desc2`).
