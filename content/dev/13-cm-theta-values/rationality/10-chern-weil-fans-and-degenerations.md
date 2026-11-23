---
title: Chern-Weil numbers, fans and degenerations
decls:
  - GlobalTheory.GoodMetric.goodChernWeil_of_goodTopChernForm
  - GlobalTheory.T.topDegreeFormCoeff_chernPoly_eq_sum_representations
  - GlobalTheory.GoodMetric.ChernSpan.topCoeff_chern_eq_sum_rep
  - GlobalTheory.T.aeval_weightedHomogeneous_chern_mem_chernCoefficientSpan
  - GlobalTheory.GoodMetric.ChernSpan.aeval_chern_mem_reach
  - GlobalTheory.SqUnifCoord.main
  - GlobalTheory.PolFan.exists_fine_invariant_fan
  - GlobalTheory.T.exists_invariant_smoothProjective_refinement_polyFan
  - GlobalTheory.PolFan.exists_smooth_refinement
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Chern-Weil numbers, fans and degenerations

The last section collects three results on the compactifications of the Shimura varieties of the theta series. First, Chern-Weil numbers of metrics with logarithmic growth, in the sense of Mumford, reduce to the case of the top Chern form of one bundle. Second, the squares of the coordinates of a degeneration are determined, up to units, by the square of the polarization. Third, there are fans of polarization functions that are fine, invariant and smooth. See [Chern-Weil forms](/learn/positivity-resolution/#chern-weil-forms), [metrics and curvature](/learn/positivity-resolution/#metrics-curvature-and-positivity), [Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction), [toroidal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications) and [Mumford's proportionality theorem](/learn/abelian-varieties/#mumfords-proportionality-theorem).

### Chern polynomials and representations

Let $m = (m_\tau)_{\tau \in \iota}$ be a finite family of ranks and $\mathrm{Mat}_m(S) = \prod_\tau M_{m_\tau}(S)$ for a commutative $\mathbb{R}$-algebra $S$. A *polynomial representation* $\rho$ of $\prod_\tau \mathrm{GL}_{m_\tau}$ is a square matrix of integer polynomials in the entries, multiplicative, with $\rho(1) = 1$ and $\rho(A^{t}) = \rho(A)^{t}$. Its differential at $1$ is a linear map $d\rho$ on $\mathrm{Mat}_m(S)$. For $A \in \mathrm{Mat}_m(S)$, let $c_k(A_\tau)$ be the coefficient of $t^k$ in $\det(1 + t A_\tau)$. A polynomial $R$ in the variables $c_{\tau, k}$ is *of weight $n$* if each monomial has total degree $n$ when $c_{\tau,k}$ has degree $k$.

**Lemma 3.10.1 (Chern span).** Let $R$ be a real polynomial of weight $n$. Then the function $A \mapsto R(c(A))$ on $\mathrm{Mat}_m(S)$ is a real linear combination of functions $A \mapsto c_n(d\rho(A))$ for polynomial representations $\rho$.

Lean: `GlobalTheory.GoodMetric.ChernSpan.aeval_chern_mem_reach` (also `GlobalTheory.T.aeval_weightedHomogeneous_chern_mem_chernCoefficientSpan`, a second name).

*Proof.* Let $T_w$ be the real span of the products $\prod_j \operatorname{tr}(A_{\tau_j}^{k_j})$ with all $k_j \ge 1$ and $\sum_j k_j = w$. By Newton's identities, $c_k(A_\tau)$ lies in $T_k$. The spaces $T_w$ are closed under products, with $T_w T_{w'} \subset T_{w + w'}$, and $1 \in T_0$. So a monomial $\prod c_{\tau,k}^{d_{\tau,k}}$ of weight $n$ lies in $T_n$, and so does $R(c(A))$. The development proves that each product of traces of weight $n$ is a real combination of the functions $c_n(d\rho(A))$. $\square$

For a polynomial $P$ in variables $x_{ab}$, $1 \le a, b \le n$, let $\mathrm{top}(P) = \sum_{w \in S_n} \operatorname{sgn}(w)\,[x_{1 w(1)} \cdots x_{n w(n)}]\,P$. If $x_{ab}$ stands for $dz_a \wedge d\bar z_b$, then $\mathrm{top}(P)$ is the coefficient of the top degree form.

**Theorem 3.10.2 (Top coefficients).** Let $n \ge 0$ and let $R$ be a real polynomial in the $c_{\tau,k}$. Then there are finitely many polynomial representations $\rho_j$ and real numbers $a_j$ such that, for every $A \in \mathrm{Mat}_m(\mathbb{C}[x_{ab}])$ with entries homogeneous of degree $1$,
$$\mathrm{top}\bigl(R(c(A))\bigr) = \sum_j a_j\, \mathrm{top}\bigl(c_n(d\rho_j(A))\bigr).$$

Lean: `GlobalTheory.GoodMetric.ChernSpan.topCoeff_chern_eq_sum_rep` (also `GlobalTheory.T.topDegreeFormCoeff_chernPoly_eq_sum_representations`, a second name).

*Proof.* Let $R_n$ be the component of $R$ of weight $n$. [The lemma](/entry/aeval-chern-mem-reach/) writes $R_n(c(A))$ as $\sum_j a_j c_n(d\rho_j(A))$, and $\mathrm{top}$ is linear. If $A$ has entries of degree $1$, then $c_k(A_\tau)$ is homogeneous of degree $k$, so a monomial of weight $w$ in the $c_{\tau,k}$ is homogeneous of degree $w$. The coefficient $\mathrm{top}$ only sees degree $n$, so the monomials of weight $w \ne n$ contribute $0$. $\square$

### Good metrics

Let $X$ be a smooth projective variety of dimension $n$ over a field $F \subset \mathbb{C}$, let $E$ be a family of vector bundles of ranks $m$ with frames, and let $U \subset X$ be open with complement a divisor with normal crossings. A Hermitian metric $H$ on $E|_U$ is *good* in the sense of Mumford if near each point $y$ there are a chart with coordinates $z_1, \dots, z_n$, in which the boundary is $\prod_{a \in S} z_a = 0$, and a frame $A$, with constants $c$ and $N$, such that the entries of $H$, $H^{-1}$ and of the connection and curvature forms are bounded by $c\,(\sum_{a \in S} |\log |z_a||)^N$ in the Poincaré metric. Let $Y$ be the flag variety of $E$ with the graded refinement of $E$, and for a Chern polynomial $R$ let $\int_Y R$ be the intersection number on $Y$ of the root polynomial of $R$ times the class of a point of the fibre.

The development states three published inputs as hypotheses:

- *Good top Chern forms*: for one bundle, the top Chern form of a good metric on $U$ is integrable, with the integral of the top Chern form of a smooth metric on $X$.
- *Chern-Weil numbers*: for a smooth metric on $X$, $\int_X R(c(H)) = \int_Y R$.
- *Flag push-forward*: if $Q$ is a root polynomial whose antisymmetrization is the root polynomial of $R$ times the discriminant, then the intersection number of $Q$ on $Y$ is $\int_Y R$.

*Good Chern-Weil* is the statement that $\int_U R(c(H)) = \int_Y R$ for every good metric $H$ on $U$, together with the flag push-forward.

**Theorem 3.10.3 (Good Chern-Weil).** Good top Chern forms, Chern-Weil numbers and the flag push-forward imply good Chern-Weil.

Lean: `GlobalTheory.GoodMetric.goodChernWeil_of_goodTopChernForm`

*Proof.* The flag push-forward is a hypothesis. Fix $X$, $E$, $U$, a good metric $H$ on $U$ and $R$. [The top coefficient theorem](/entry/top-coeff-chern-eq-sum-rep/) at $n = \dim X$ gives $\rho_j$ and $a_j$. Choose a smooth metric $H_0$ on $E$ over $X$, which exists since $X$ is projective. For each $j$, the bundle $E_j = \rho_j(E)$ gets the induced metrics $H'_j = \rho_j(H)$ on $U$ and $H'_{0,j} = \rho_j(H_0)$ on $X$.

The metric $H'_j$ is good. Near a point $y$, take the chart, the frame $\rho_j(A)$, and the constants that the development gives for polynomial representations. Then the growth bound needs $\sum_{a \in S} |\log |z_a|| \ge 1$. This holds near $y$: some $z_{a_0}$ vanishes at $y$, so $|z_{a_0}| < e^{-1}$ near $y$.

By Chern-Weil numbers, the top Chern form of $H'_{0,j}$ is integrable with integral $t_j$. By good top Chern forms, the top Chern form of $H'_j$ on $U$ is integrable with the same integral $t_j$. In a chart, the curvature of $\rho_j(H)$ is $d\rho_j$ of the curvature of $H$, and its entries are linear in the $dz_a \wedge d\bar z_b$. So the top coefficient theorem gives, at each point,
$$R(c(H)) = \sum_j a_j\, c_n(H'_j), \qquad R(c(H_0)) = \sum_j a_j\, c_n(H'_{0,j})$$
as densities. By linearity, $\int_U R(c(H)) = \sum_j a_j t_j = \int_X R(c(H_0))$, and by Chern-Weil numbers this is $\int_Y R$. $\square$

### Squares of degeneration coordinates

Let $R$ be a complete Noetherian normal local domain of characteristic $0$, and let $G$ be a semi-abelian scheme over $R$. A *degeneration datum* $D$ gives a character group $X_D$ and, through Mumford's construction, a coordinate $\psi_D(y) \in R$, up to units, for each $y \in X_D$. A *uniformization* $U$ of $G$ by $D$ and a polarized abelian variety $A$ over the fraction field gives a line bundle $L_U$ on $G$.

**Theorem 3.10.4 (Squares of coordinates).** Let $U$ and $U'$ be uniformizations of $G$ by $(D, A)$ and $(D', A')$, and assume $L_{U'}^{2} \cong L_U^{2}$. Then there is an isomorphism $\varepsilon : X_{D'} \to X_D$ such that, for all $y \in X_{D'}$, if $r$ is a coordinate of $\varepsilon(y)$ for $D$ and $r'$ a coordinate of $y$ for $D'$, then $r^2$ and $r'^2$ are associated.

Lean: `GlobalTheory.SqUnifCoord.main`

*Proof.* The uniformizations give an isomorphism $\varepsilon$ of the character groups, and the isomorphism of the squares gives an isomorphism of the polarized abelian parts. The two degeneration maps agree on the even characters. Let $s$ and $s'$ be coordinates of $2\varepsilon(y)$ and $2y$. Then $s \sim r^4$ and $s' \sim r'^4$, by the quadratic law of the coordinates. The agreement on even characters gives $s^4 \sim s'^4$. So $(r^2)^8 \sim (r'^2)^8$.

It remains to show that $a^k \sim b^k$ with $k \ge 1$ implies $a \sim b$ in an integrally closed domain. If $a = 0$, then $b = 0$. Otherwise write $b^k = u a^k$ with a unit $u$. Then $(b/a)^k = u$ and $(a/b)^k = u^{-1}$ are integral over $R$, so $b/a$ and $a/b$ lie in $R$, and $b/a$ is a unit. $\square$

### Fine invariant fans

Let $E$ be a CM field with a host datum, with complex conjugation $\bar{\ }$ and a root of unity $w_0$. An *invariant function* $\varphi$ assigns a real number to each form $B$ on $O_E^n$, with $\varphi(B \circ r) = \varphi(B)$ for every surjection $r$. For a projective $O_E$-module $X$ of rank at most $q$, $\varphi$ is a *polyhedral fan* on $X$ if it is homogeneous and superadditive on the positive semi-definite Hermitian forms, integral and positive on the balanced forms, and the semi-definite cone is covered, up to automorphisms, by finitely many cones on which $\varphi$ is linear. It is a *polarization fan* if, in addition, faces of cones are cones and every form is a nonnegative combination of the generators of one cone. A *smooth* fan has no self-intersection: no automorphism of $X$ moves one ray of a cone to another ray of the same cone. The function is *twist invariant* if it is invariant under the automorphisms of $O_E$ that fix $w_0$. A cone is *fine at $N$* if, for every $y$, the forms of the cone have a common minimum on $y + N X$.

**Theorem 3.10.5 (Smooth refinement).** Let $\psi$ be a twist invariant polyhedral fan up to rank $q$, and assume that the linear forms on balanced forms dominate. Then there is a smooth twist invariant polarization fan $\varphi'$ up to rank $q$ such that $\psi$ is linear on every cone of $\varphi'$.

Lean: `GlobalTheory.PolFan.exists_smooth_refinement` (also `GlobalTheory.T.exists_invariant_smoothProjective_refinement_polyFan`, a second name).

*Proof.* The development first refines $\psi$ to a twist invariant simplicial fan $\varphi$ with labels, and then refines $\varphi$ to a smooth one $\varphi'$. Each cone of $\varphi'$ lies in a cone of $\varphi$, which lies in a cone of $\psi$, and $\psi$ is linear there. $\square$

**Theorem 3.10.6 (Fine invariant fan).** Let $\varphi_s$ be a polarization fan over $\mathbb{Z}$ up to rank $g$, let $[E : \mathbb{Q}]\,q \le g$, and let $\mathcal{N}$ be a finite set of levels $N \ge 1$. Then there is a smooth, twist invariant and positive polarization fan $\varphi'$ over $O_E$ up to rank $q$, homogeneous under integer scaling, such that on every cone of $\varphi'$ the restriction of $\varphi_s$ is linear and the cone is fine at every $N \in \mathcal{N}$.

Lean: `GlobalTheory.PolFan.exists_fine_invariant_fan`

*Proof.* Build from $\varphi_s$ the base function at the levels $N - 1$, $N \in \mathcal{N}$, with a common denominator. The development proves that it is a twist invariant polyhedral fan up to rank $q$, with a finite polyhedral cover of the balanced forms, and that linear forms dominate. [The smooth refinement](/entry/pol-fan-exists-smooth-refinement/) gives a smooth $\varphi'$, which is then extended to a homogeneous positive polarization fan $\varphi''$ with the same cones. On a cone of $\varphi''$, the base function is linear, so the restriction of $\varphi_s$ is linear and the cone is fine at each level $(N - 1) + 1 = N$. $\square$

**Remark 3.10.7 (Formalization).** The Chern-Weil theorem is [GoodChernWeilOfGoodTopChernForm.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/GoodChernWeilOfGoodTopChernForm.lean#L149), with `isGood_polyRep` at line 108 and `curvPoly_polyRep` at line 78. Its proof passes the hypothesis `FlagPushForward` through as the second half of the conclusion (`refine ⟨?_, hP⟩`, line 152), since `GoodChernWeil` is defined as `GoodChernNumbers ∧ FlagPushForward` in [MumfordProportionality.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/MumfordProportionality.lean#L30). The top coefficient theorem is [TopDegreeFormCoeffChernPolyEqSumRepresentations.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TopDegreeFormCoeffChernPolyEqSumRepresentations.lean#L30), and the lemma is [AevalWeightedHomogeneousChernMemChernCoefficient.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/AevalWeightedHomogeneousChernMemChernCoefficient.lean#L47). The span `Reach` and `TrSpan` are defined in a file named `SumSumEqSumPair.lean` (line 233). The step from products of traces to `Reach` is the unopened `T.tracePowerListProduct_mem_chernCoefficientRealSpan`. The degeneration theorem is [UnifPolarizationSquareIso.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/UnifPolarizationSquareIso.lean#L50), with `associated_of_pow` at line 20. The proof gets $(r^2)^8 \sim (r'^2)^8$, which is $r^{16} \sim r'^{16}$, so the same lemma with $k = 16$ gives $r \sim r'$; the statement with squares is weaker than what the proof shows. Its Statement file uses the name `T.unif_polarization_square_iso`, which is not in the outline, and `IsCN` is in `HomExtNormalSt.lean` (line 140). The fans are [ExistsFineInvariantFan.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsFineInvariantFan.lean#L17) and [ExistsInvariantSmoothProjectiveRefinementPolyFan.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsInvariantSmoothProjectiveRefinementPolyFan.lean#L8), with `IsPolFan`, `NoSelfInt` and `IsCone` in `SumMulEqZeroOfSumToReal.lean`, `IsPolyFan` and `Dominates` in `ExistsEqAddOfRedVEq.lean`, and `IsTwInv` and `IsPosFn` in `SysExOfPol.lean`. The file names of these definitions do not describe their content.

## Notes and references

The results of this chapter feed [the nonempty hypotheses](/step/nonempty-hyps/) through the theta series of Sections 1 and 4, the Wach lattices of Section 6, the column data of Sections 7 and 9, and the Fock data, harmonic records and theta vectors of Section 8. The full rank theorem of Section 5 feeds [the export at a bundle](/entry/export-at-of-bundles-alt/) of Volume 7, and the inert Satake parameters feed [the agreement of Satake parameters](/entry/sat-agree/) of Volume 15. The fans of Section 10 feed [the key rules for every character](/step/every-character-of-literature/). The Chern-Weil theorem feeds [good Chern-Weil](/entry/good-chern-weil/) of Volume 6, and the theorem on squares of coordinates feeds [the uniqueness on a trait](/entry/trait-uniq/) of Volume 5.

- J. Neukirch, *Algebraic Number Theory*, Grundlehren 322, Springer, 1999, Chapter VI, Sections 4 to 6 (the Artin reciprocity law and ray class fields).
- S. Kudla, *Splitting metaplectic covers of dual reductive pairs*, Israel J. Math. 87 (1994), 361 to 401.
- R. Howe, *Transcending classical invariant theory*, J. Amer. Math. Soc. 2 (1989), 535 to 552.
- R. Howe, *Remarks on classical invariant theory*, Trans. Amer. Math. Soc. 313 (1989), 539 to 570.
- G. B. Folland, *Harmonic Analysis in Phase Space*, Annals of Mathematics Studies 122, Princeton, 1989, Chapters 1 and 4 (the Fock model and the oscillator representation).
- M. Kashiwara and M. Vergne, *On the Segal-Shale-Weil representations and harmonic polynomials*, Invent. Math. 44 (1978), 1 to 47.
- S. Rallis, *On the Howe duality conjecture*, Compositio Math. 51 (1984), 333 to 399.
- L. Berger, *Limites de représentations cristallines*, Compositio Math. 140 (2004), 1473 to 1498.
- B. Bhatt and P. Scholze, *Prismatic F-crystals and crystalline Galois representations*, Camb. J. Math. 11 (2023), 507 to 562.
- O. T. O'Meara, *Introduction to Quadratic Forms*, Grundlehren 117, Springer, 1963, Chapter IX (lattices over local fields).
- R. Jacobowitz, *Hermitian forms over local fields*, Amer. J. Math. 84 (1962), 441 to 465.
- D. Mumford, *Hirzebruch's proportionality theorem in the non-compact case*, Invent. Math. 42 (1977), 239 to 272.
- D. Mumford, *An analytic construction of degenerating abelian varieties over complete rings*, Compositio Math. 24 (1972), 239 to 288.
- A. Ash, D. Mumford, M. Rapoport and Y.-S. Tai, *Smooth Compactifications of Locally Symmetric Varieties*, second edition, Cambridge, 2010, Chapters I and II (torus embeddings, polyhedral cone decompositions and smooth refinements).
- G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Ergebnisse 22, Springer, 1990, Chapters II and III (degeneration data and Mumford's construction) and Chapter IV (toroidal compactifications).
- P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978, Chapter 3, Section 3 (Chern classes and Chern-Weil forms).
