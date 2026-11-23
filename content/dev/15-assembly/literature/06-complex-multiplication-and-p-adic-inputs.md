---
title: Complex multiplication and p-adic inputs
decls:
  - UpperTheory.LiteratureTheorems.join_out_of_literature
  - UpperTheory.LiteratureTheorems.cm_curve_good_outside_prime_st_of_literature
  - UpperTheory.LiteratureTheorems.bhatt_scholze_integral_of_literature
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Complex multiplication and p-adic inputs

This section states the arithmetic inputs of the chapter: the statements on periods and zeta denominators that follow from the theory of [[complex multiplication|D3HEJTVY7G]] and from the rationality of zeta values, the existence of Gross's elliptic curves with complex multiplication by $\mathbb{Q}(\sqrt{-p})$, and the theorem of Bhatt and Scholze that crystalline lattices are realised by prismatic F-crystals. The first is a field of the [non-endoscopic bundle](/entry/literature-nonexistence/). The second and third are fields of the bundle of [unitary group hypotheses](/step/published-results-eigen/), the third through its local part. Background is in [complex multiplication](/learn/elliptic-curves/#complex-multiplication), [Gross's curves](/learn/elliptic-curves/#grosss-curves) and [prismatic Dieudonné theory](/learn/formal-groups/#prismatic-dieudonn-theory).

### Periods and zeta denominators

Let $K$ be an imaginary quadratic field. The proof uses five classical results.

1. (Main theorem of complex multiplication.) For $\sigma \in \mathrm{Aut}(\mathbb{C} / K)$ and a lattice $\Lambda$ with $\mathrm{End}(\Lambda) = \mathcal{O}_K$, the image $\sigma(j(\Lambda))$ is $j$ of the lattice $s^{-1} \Lambda$, where $s$ is an idele attached to $\sigma$ by class field theory (Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Theorem 5.4).
2. (Hilbert class field.) $K(j(\mathcal{O}_K))$ is the [[Hilbert class field|WWCJ7CR2R3]] of $K$ (Cox, *Primes of the Form $x^2 + ny^2$*, Theorem 11.1).
3. (Siegel-Klingen and Deligne-Ribet.) The partial zeta values of a totally real field at negative odd integers are rational, with the denominators and congruences of Deligne and Ribet (Invent. Math. 59, 1980).
4. The functional equation of the partial zeta functions of a totally real field.
5. The functional equation of Hecke L-functions in Tate's form.

From these the proof derives five statements, which we do not unfold: lower bounds for the $\ell$-adic valuations of toric sums attached to Hecke characters of a CM field; the transport of these sums under $\mathrm{Aut}(\mathbb{C} / K)$; the algebraicity of twisted toric sums divided by a power of one period; bounded denominators of the partial zeta values of the maximal real subfield; and a reflection identity between two completed Hecke L-functions at integers.

**Proposition 1.6.1 (Periods and zeta denominators).** The five statements above hold.

Lean: `UpperTheory.LiteratureTheorems.join_out_of_literature`.

*Proof.* This is [Theorem 1.1 of Volume 13](/entry/join-out-of-five/) applied to the five classical results. That theorem first proves that the divided-power jets of CM lattice functions are integral, that their values are algebraic, and how $\mathrm{Aut}(\mathbb{C} / K)$ acts on these values. Then it reads off the five statements. $\square$

### Gross's curves

**Theorem 1.6.2 (Gross).** Let $p > 3$ be a prime with $p \equiv 3 \pmod 4$. Let $\Lambda = \mathcal{O}_{\mathbb{Q}(\sqrt{-p})} \subset \mathbb{C}$ and $F = \mathbb{Q}(j(\Lambda)) \subset \mathbb{C}$. There is an elliptic curve $A$ over $F$, given by a Weierstrass equation, with these properties.

1. $j(A) = j(\Lambda)$, so $A$ has complex multiplication by $\mathcal{O}_{\mathbb{Q}(\sqrt{-p})}$.
2. $A$ has good reduction at every finite place of $F$ that does not divide $p$.
3. At every finite place $v$ of $F$, the minimal discriminant of $A$ is $-p^3$ up to a unit at $v$.

Lean: `UpperTheory.LiteratureTheorems.cm_curve_good_outside_prime_st_of_literature`.

This is the curve $A(p)$ of Gross, *Arithmetic on Elliptic Curves with Complex Multiplication* (LNM 776, 1980).

*Proof.* We take the result from Gross. In the development it is [Theorem](/entry/cm-curve-good-outside-prime/). $\square$

### Prismatic F-crystals

Let $\ell$ be a prime and $K$ a finite extension of $\mathbb{Q}_\ell$ with algebraic closure $\overline{K}$, completion $C$ and Galois group $G_K$. Let $A_{\mathrm{inf}} = W(\mathcal{O}_{C^\flat})$. A prismatic F-crystal $E$ over $\mathcal{O}_K$ has a value $E(P)$ at each prism $P$. Fix a prism $P_0$ over $\mathcal{O}_K$ with an isomorphism of its ring with $A_{\mathrm{inf}}$. For a $G_K$-stable $\mathbb{Z}_\ell$-lattice $T$, the crystal $E$ *realises* $T$ through a map $j : E(P_0) \to W(C^\flat) \otimes_{\mathbb{Z}_\ell} T$ if $j$ is compatible with Frobenius and with $G_K$.

**Theorem 1.6.3 (Bhatt-Scholze).** The following two statements hold.

1. Let $V$ be a crystalline representation of $G_K$ on a finite-dimensional $\mathbb{Q}_\ell$-space, and let $T \subset V$ be a $G_K$-stable lattice. Then there is a prismatic F-crystal $E$ over $\mathcal{O}_K$ that realises $T$.
2. Let $E$ and $E'$ realise lattices $T$ and $T'$. Then every $G_K$-equivariant map $f : T \to T'$ comes from a unique map $u : E \to E'$ of F-crystals.

Lean: `UpperTheory.LiteratureTheorems.bhatt_scholze_integral_of_literature`.

Part 1 is essential surjectivity and part 2 is full faithfulness of the étale realisation from prismatic F-crystals to lattices in crystalline representations. This is Bhatt and Scholze, *Prismatic F-crystals and crystalline Galois representations* (Camb. J. Math. 11, 2023). It gives the integral [[Galois representation|QW17YJ6ZCT]] theory that the proof uses at the places above $\ell$.

*Proof.* We take the result from Bhatt and Scholze. In the development it is [Theorem 6.13.4 of Volume 4](/entry/bhatt-scholze-integral/). $\square$

**Remark 1.6.4 (Formalization).** The three theorems take the record of open statements as an argument and do not use it. The first is `GlobalTheory.JoinFun.joinOut_of_five` applied to the five classical results, each a one-line theorem of the same file ([EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L233), lines 221 to 233). The other two are the terms `GlobalTheory.Published.cmCurveGoodOutsidePrime` and `GlobalTheory.BSP.bhattScholzeIntegral` (lines 267 and 277). The proposition is the conjunction `JoinOut` of five statements, `ToricDenominator`, `Transport`, `TwistedTransport`, `ZetaDenominators` and `Refl` ([HypothesisBundleConversions.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HypothesisBundleConversions.lean#L7)). Our description of them follows their definitions, which we did not unfold to the end. The name of the conjunction says nothing about its content. The derivation is at [JoinOutOfFive.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/JoinOutOfFive.lean#L15). Gross's theorem is stated at [CmCurveGoodOutsidePrimePremises.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/CmCurveGoodOutsidePrimePremises.lean#L35); there $F$ is a subfield of $\mathbb{C}$, the lattice $\Lambda$ is the set of algebraic integers of $\mathbb{Q}(\sqrt{-p})$, and the minimal discriminant is asked at every finite place, including those above $p$. The Bhatt-Scholze statement is at [BhattScholzeIntegral.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/BhattScholzeIntegral.lean#L12). In part 1 the crystalline condition refers to a standard local prime $P$ that does not occur in the conclusion. We did not unfold the prisms, the F-crystals `FCrys`, the predicate `Realises` or the ring `WCb`.
