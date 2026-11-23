---
id: clozel-conj-c
title: Conjugates of regular algebraic cuspidal representations are cuspidal
kind: theorem
decl: UpperTheory.V.Z.Coh.clozelConjC
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ClozelCohomology.ClozelConjC
covers: 761
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{ClozelConjC}$: for a regular algebraic cuspidal representation $\pi$ of $\mathrm{GL}_a$ over a totally complex field, and an automorphism $\sigma$ of $\mathbb{C}$, the $\sigma$-conjugate of a finite constituent of $\pi$ is a finite constituent of a cuspidal representation. [The published hypotheses from patching](/entry/published-hypotheses-from-patching-alt/) put it in the field `conjC` of $\mathrm{HypothesesH'}$. This is the rationality theorem of Clozel (L. Clozel, *Motifs et formes automorphes: applications du principe de fonctorialité*, in *Automorphic forms, Shimura varieties, and L-functions I*, Academic Press, 1990, Section 3).

## Statement

Let $E$ be a totally complex number field and $a \ge 1$. A finite constituent of a cuspidal representation $\pi$ of $\mathrm{GL}_a(\mathbb{A}_E)$ is a smooth irreducible representation $\tau$ of $\mathrm{GL}_a(\mathbb{A}_{E,f})$ with a nonzero map $\tau \to \pi_f$ that commutes with $\mathrm{GL}_a(\mathbb{A}_{E,f})$. For $\sigma \in \mathrm{Aut}(\mathbb{C})$, a representation $\tau'$ is a $\sigma$-conjugate of $\tau$ if there is an additive bijection $T \colon \tau \to \tau'$ with $T(cv) = \sigma(c)T(v)$ that commutes with the group.

**Theorem.** Let $\pi$ be a cuspidal representation of $\mathrm{GL}_a(\mathbb{A}_E)$ that is regular algebraic, and let $\sigma \in \mathrm{Aut}(\mathbb{C})$. Then there are a cuspidal representation $\pi'$ and finite constituents $\tau$ of $\pi$ and $\tau'$ of $\pi'$ such that $\tau'$ is a $\sigma$-conjugate of $\tau$, and for each embedding $\varphi \colon E \to \mathbb{C}$, if $\pi$ has infinitesimal character $m$ at $\varphi$, then $\pi'$ has infinitesimal character $m$ at $\sigma \circ \varphi$.

## Proof

The proof is by strong induction on $a$.

1. `R.exAlgRepCusp` gives an algebraic representation $\Xi$ whose infinitesimal character at each embedding is the negative of that of $\pi$. `R.conjAlgRep` gives its $\sigma$-conjugate $\Xi'$.
2. `clozelCohC` shows that $\pi$ is cohomological for $\Xi$. `finExC` gives a finite constituent $\tau$ of $\pi$, and `conjEx` gives a $\sigma$-conjugate $\tau'$ of $\tau$.
3. `embed_of` proves the statement `Embed`: there is a nonzero map $j$ from $\tau'$ into automorphic forms that commutes with $\mathrm{GL}_a(\mathbb{A}_{E,f})$, where $m$ is the infinitesimal character read off from $\Xi'$. The image has the property `HasCap` for $m$, which we have not unfolded. Its inputs are statements on harmonic forms and cohomology (`partH`, `relFacts`, `harmSub`, `harmNe`, `harmInj` and others) and three results of Borel type (`Lit.Bor.frameEx`, `Lit.Bor.oneReal`, `Lit.Geo.cuspRapid`).
4. `S.cuspSupport` splits into two cases. Either $\tau'$ is a finite constituent of a cuspidal $\pi'$ with infinitesimal character $m$, and we are done. Or, at almost all places, the Satake parameters of $\tau'$ are the union of those of at least two pieces $P_i$ on $\mathrm{GL}_{n_i}$ with $n_i < a$ and $\sum n_i = a$, whose infinitesimal characters add up to $m$.
5. `noEis` excludes the second case. It uses the Jacquet-Shalika rigidity theorem `jacquetShalikaRigidity` and the induction hypothesis for the smaller ranks.

## In the Lean code

The theorem is in [ClozelConjC.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClozelCohomology/ClozelConjC.lean#L26). Its proof is one application of `clozelConjC_of_steps`, in [ClozelConjCOfSteps.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ConjugateRepresentations/CobordismLinearRelations/ClozelConjCOfSteps.lean#L231), which does the induction. $\mathrm{ClozelConjC}$ is in [GelfandKazhdanReal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PublishedTheorems/GelfandKazhdanReal.lean#L26). The other inputs:

- `Embed` (line 155) and `embed_of` (line 162), in the same file as `clozelConjC_of_steps`.
- `CuspSupport` in [HasCapOneFn.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ConjugateRepresentations/CuspidalSupport/HasCapOneFn.lean#L24).
- `noEis` in [AlgSatSum.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ConjugateRepresentations/CobordismLinearRelations/AlgSatSum.lean#L14).
- `FinExC` in [ClozelConjCOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/ClozelConjCOf.lean#L23).

We have not unfolded the proofs of `embed_of`'s inputs or of `noEis`. The Lean statement asks only for some constituent $\tau$ of $\pi$, not for each one. It speaks of a constituent of $\pi_f$, not of $\pi_f$ itself. The same file also proves `borelInjC`, which is only `Lit.Geo.borelInjC` under a second name.
