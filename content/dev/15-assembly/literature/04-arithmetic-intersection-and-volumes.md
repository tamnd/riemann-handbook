---
title: Arithmetic intersection and volumes
decls:
  - UpperTheory.LiteratureTheorems.arith_hilbert_samuel_of_literature
  - UpperTheory.LiteratureTheorems.vol_ge_of_literature
  - UpperTheory.LiteratureTheorems.ar_degree_of_literature
  - UpperTheory.LiteratureTheorems.zarhin_statement
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Arithmetic intersection and volumes

This section states four results of Arakelov geometry: the arithmetic Hilbert-Samuel theorem, the lower bound of the arithmetic volume by the self-intersection, the birational invariance of arithmetic self-intersection together with the Chern-Weil formula for the degree, and Zarhin's trick for abelian schemes over a valuation ring. The first three feed the bound on the volume of the Hodge bundle in the step [EveryCharacter from the literature](/step/every-character-of-literature/), directly and through the bundle of [published Hodge bundle theorems](/step/published-results-arithmetic/). Zarhin's trick reduces statements on abelian schemes to the principally polarised case in the same step. Background is in [Hermitian line bundles](/learn/arakelov/#hermitian-line-bundles), [arithmetic varieties and intersection numbers](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers), [arithmetic volume and bigness](/learn/arakelov/#arithmetic-volume-and-bigness) and [the Hodge bundle and Zarhin's trick](/learn/arakelov/#the-hodge-bundle-and-zarhins-trick).

Throughout, $X$ is an arithmetic variety: an integral scheme, projective and flat over the ring of integers of a number field, whose generic fibre has dimension $D$. So $X$ has dimension $D + 1$. A Hermitian line bundle $\overline{L} = (L, \|\cdot\|)$ on $X$ is a line bundle with a smooth metric on $L(\mathbb{C})$ that is invariant under complex conjugation. Its self-intersection $\widehat{\deg}(\widehat{c}_1(\overline{L})^{D+1}) \in \mathbb{R}$ is defined by Gillet and Soulé. A global section $s$ of $L$ is *small* if $\|s\|_{\sup} \leq 1$. The set of small sections of $L$ is finite, since it is the intersection of a lattice with a compact set.

**Definition 1.4.1 (Arithmetic volume).** The arithmetic volume of $\overline{L}$ is

$$\widehat{\mathrm{vol}}(\overline{L}) = \limsup_{m \to \infty} \frac{\log \# \{\text{small sections of } L^{\otimes m}\}}{m^{D+1} / (D+1)!}.$$

### The arithmetic Hilbert-Samuel theorem

**Theorem 1.4.2 (Arithmetic Hilbert-Samuel).** Let $X$ be an arithmetic variety of relative dimension $D$. Let $\overline{L}$ and $\overline{N}$ be Hermitian line bundles on $X$, and let $\overline{L}$ be nef with self-intersection $a$. Then for all large $m$ the set of small sections of $\overline{L}^{\otimes m} \otimes \overline{N}$ is finite, and

$$\log \# \{\text{small sections of } \overline{L}^{\otimes m} \otimes \overline{N}\} = \frac{a}{(D+1)!} \, m^{D+1} + o(m^{D+1}).$$

Lean: `UpperTheory.LiteratureTheorems.arith_hilbert_samuel_of_literature`.

For $\overline{L}$ ample with positive curvature and $\overline{N}$ trivial this is Gillet and Soulé (Invent. Math. 110, 1992), with the analytic input of Bismut and Vasserot. Abbes and Bouche gave a proof with the Bergman kernel (Ann. Inst. Fourier 45, 1995). The nef case follows by continuity of the arithmetic volume (Moriwaki, *Arakelov Geometry*, AMS, 2014).

*Proof.* In the development it is derived from resolution of singularities in the form of principalisation; see [Theorem 6.7.5 of Volume 6](/entry/arith-hilbert-samuel-of-principalisation/). $\square$

**Theorem 1.4.3 (Volume and self-intersection).** Let $X$ be an arithmetic variety of relative dimension $D$, and let $\overline{L}$ be a Hermitian line bundle on $X$ whose restriction to each fibre is nef and whose metric is semipositive. Let $a$ be the self-intersection of $\overline{L}$. Then

$$a \leq \widehat{\mathrm{vol}}(\overline{L}).$$

Lean: `UpperTheory.LiteratureTheorems.vol_ge_of_literature`.

For nef $\overline{L}$ the two sides are equal, by the Hilbert-Samuel theorem. For relatively nef $\overline{L}$ the inequality is a consequence of Yuan's arithmetic Siu inequality (Invent. Math. 173, 2008).

*Proof.* We derive it from the arithmetic Hilbert-Samuel theorem, together with the calculus of arithmetic intersection numbers and the numerical properties of nef line bundles, which are further inputs from the literature. See [Theorem 6.8.6 of Volume 6](/entry/vol-ge-of-hilbert-samuel/). $\square$

### Birational invariance and the Chern-Weil degree

**Theorem 1.4.4 (Arithmetic degree).** The following two statements hold.

1. (Birational invariance.) Let $X, X'$ be arithmetic varieties of relative dimension $D$ over the same base, both generically smooth. Let $\pi : X' \to X$ be a morphism over the base that is an isomorphism over a nonempty open subset of $X$. If a Hermitian line bundle $\overline{L}$ on $X$ has self-intersection $a$, then $\pi^* \overline{L}$ has self-intersection $a$.
2. (Chern-Weil degree.) Let $Y$ be a projective variety of dimension $d$ over a field $F$, with an embedding $F \to \mathbb{C}$. Let $L$ be the line bundle of a Cartier divisor $\Delta$ on $Y$, and let $\phi$ be a smooth metric on $L(\mathbb{C})$. Then the Chern form $c_1(L, \phi)^d$ is integrable on $Y(\mathbb{C})$, and

$$\int_{Y(\mathbb{C})} c_1(L, \phi)^d = \deg(\Delta^d).$$

Lean: `UpperTheory.LiteratureTheorems.ar_degree_of_literature`.

Part 1 is the projection formula of arithmetic intersection theory (Gillet and Soulé, Publ. Math. IHÉS 72, 1990), applied to a birational $\pi$ of degree one. Part 2 is the Chern-Weil description of the degree (Griffiths and Harris, *Principles of Algebraic Geometry*, Chapter 1). See [Chern-Weil forms](/learn/positivity-resolution/#chern-weil-forms).

*Proof.* Part 1 follows from the existence of arithmetic heights of cycles, built from the Poincaré-Lelong formula and resolution of singularities. Part 2 is [Theorem 4.10.4 of Volume 6](/entry/chern2-chern-degree-complex/). $\square$

### Zarhin's trick

**Theorem 1.4.5 (Zarhin's trick).** Let $C$ be an algebraically closed field with a rank one valuation, and let $R$ be its valuation ring. Let $A$ be an abelian scheme over $R$ with a relatively ample line bundle. Then there are a principally polarised abelian scheme $P$ over $R$ and homomorphisms $i : A \to P$ and $r : P \to A$ with $r \circ i = \mathrm{id}_A$.

Lean: `UpperTheory.LiteratureTheorems.zarhin_statement`.

In the standard form, Zarhin's trick says that $P = (A \times A^\vee)^4$ carries a principal polarisation for every abelian scheme $A$ with a polarisation. Then $A$ is a direct factor of $P$. The trick is due to Zarhin (Invent. Math. 79, 1985). Over a general base see Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque 129 (1985). See [polarizations and Zarhin's trick](/learn/abelian-varieties/#polarizations-and-zarhins-trick).

*Proof.* The construction needs the dual abelian scheme $A^\vee$, which we take from the literature. Then it is [Theorem](/entry/zarhin/), applied to [Theorem 1.6.4 of Volume 5](/entry/dual-abelian-scheme/). $\square$

**Remark 1.4.6 (Formalization).** The four theorems take the record of open statements as an argument and do not use it. Their proofs are single terms ([EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L251), lines 251, 255, 531 and 547). The Hilbert-Samuel theorem is `GlobalTheory.arithHilbertSamuel_of_principalisation` applied to `PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisation_closed`. The volume bound is `GlobalTheory.VolBr.volGe_of_hilbertSamuel` applied to the Hilbert-Samuel theorem and to the inputs `ArCalc` and `NefNumerics`; these are conjunctions of seven and three named statements, which we did not unfold. The degree statement is `PositivityTheory.Prw.arDegree_of`, applied to a height projection of `cycleHeights_direct poincareLelong resK` and to `chernDegreeComplex`. Zarhin's trick is `PositivityTheory.HtPt.Narrow.zarhin` applied to `GlobalTheory.dualAbelianScheme`. The statements are at [SmallSecTensTriv.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/SmallSecTensTriv.lean#L14), [VolGe.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/VolGe.lean#L12), [ArBirational.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ArBirational.lean#L25) and [ZarhinStatement.lean](lean:Development/AutomorphicSpectrum/PublishedTheorems/Algebra₂/ZarhinStatement.lean#L21). We did not unfold `IsArithVar`, `HermLB`, `IsNef`, `NefFib`, `SemiPos`, `IsSelfInter`, `arVol`, `GenSmooth`, `Weight` or `PolAV`. Our reading of $D$ as the relative dimension comes from the exponent $D + 1$ in the Hilbert-Samuel statement. Self-intersection is a relation between $\overline{L}$ and a real number, not a function. In part 1 of the degree statement, $\pi$ is not asked to be proper or surjective; the base ring is any commutative ring with the arithmetic variety hypotheses. The Hilbert-Samuel statement has the extra twist $\overline{N}$, which the standard form does not have.
