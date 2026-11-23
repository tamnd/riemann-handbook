---
title: Rallis inner products and multiplicity one
decls:
  - GlobalTheory.RawLift.Assembled.rallisConv_of_siegelWeil
  - GlobalTheory.T.algebraic_modular_forms_strong_multiplicity_one
  - GlobalTheory.GlobDet.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rallis inner products and multiplicity one

This section proves two global facts about automorphic forms on unitary groups. The first is the inner product formula of Rallis for theta lifts from a group $U(W)$ to a definite group $U(V)$ in the stable range, with convergence of every integral in it. It follows from the Siegel-Weil formula and the rapid decay of cusp forms. It is used in [the local splitting of real lifts](/entry/at-real-lift-splits-locally/). The second says that an irreducible space of algebraic modular forms on a unitary group is determined, up to isomorphism, by its local components at the split places and its Satake parameters at the other places. It is used in [the representation of local data](/entry/rep-of-local-h-alt/). Both entries are in Volume 15.

### The inner product formula

Let $E$ be the host, a CM field with totally real subfield $F$, and let $V$ and $W$ be Hermitian spaces over $E$. Fix an additive character $\psi$ of $\mathbb{A}_F / F$, characters $\chi_V$ and $\chi_W$, and a Weil datum $\omega$ for $(\psi, V, W, \chi_V, \chi_W)$: an action of $U(V)(\mathbb{A}) \times U(W)(\mathbb{A})$ on functions on $V \otimes W(\mathbb{A})$. For a theta function $f$, let $\theta(h, g; f)$ be its theta kernel. For a cusp form $\varphi$ on $U(W)$ let
$$
\theta(f, \varphi)(h) = \int_{\mathcal{G}} \overline{\theta(h, g; f)}\, \varphi(g)\, dg,
$$
where $\mathcal{G}$ is a fundamental domain for $U(W)(F)$ in $U(W)(\mathbb{A})$ for a Haar measure $\nu_W$. Let $\mathcal{H}$ be a fundamental domain for $U(V)$ with a Haar measure $\nu_V$, and $\mathcal{F}$ a fundamental domain of covolume $1$ for the rational lattice of $V \otimes W$. Write $\langle f, f' \rangle = \int_{\mathcal{F}} \overline{f}\, f'$.

**Theorem 5.21.1 (Siegel-Weil formula).** Let $A$ and $B$ be Hermitian spaces with $1 \le \dim A$, such that $B$ is anisotropic or $\dim A + r_B < \dim B$, where $r_B$ is the Witt index of $B$. Then the theta integral over $U(B)$ converges absolutely. If also $2 \dim A < \dim B$, then the Siegel Eisenstein series on $U(A \oplus A^-)$ of the Siegel-Weil section of $f$ converges, and it equals the mean value of the theta integral of $f$ over $U(B)(F) \backslash U(B)(\mathbb{A})$.

Lean: `GlobalTheory.Published.WeilSiegelFormulaUnitary`

This is the formula of Weil in his range of absolute convergence; see Weil (1965). The Lean form also asks that the absolute theta integrals are bounded by a continuous seminorm on Schwartz functions.

**Theorem 5.21.2 (Rallis inner product formula).** Assume the Siegel-Weil formula and the rapid decay of cusp forms. Let $V$ be positive definite with $2 \dim W < \dim V$. Let $f_1$ and $f_2$ be theta functions and $\varphi_1$ and $\varphi_2$ smooth cusp forms on $U(W)$. Then the integrals that define $\theta(f_1, \varphi_1)$ converge at every $h$, the function $\overline{\theta(f_1, \varphi_1)}\, \theta(f_2, \varphi_2)$ is integrable on $\mathcal{H}$, the integrand on the right below is integrable, and
$$
\begin{aligned}
\int_{\mathcal{H}} \overline{\theta(f_1, \varphi_1)(h)}\, \theta(f_2, \varphi_2)(h)\, dh
&= \nu_V(\mathcal{H}) \int_{U(W)(\mathbb{A})} \bigl\langle \omega(1, g) f_2, f_1 \bigr\rangle \\
&\qquad \times \int_{\mathcal{G}} \overline{\varphi_1(x)}\, \varphi_2(x g)\, dx\, dg.
\end{aligned}
$$

Lean: `GlobalTheory.RawLift.Assembled.rallisConv_of_siegelWeil`

*Proof.* The proof joins six facts about the data $(\psi, V, W, \omega)$ with a frame of Lagrangians of $W \oplus W^-$:
1. the pair sum: the inner product of two theta kernels over $\mathcal{H}$ is a sum over the Lagrangians $Y$ of $W \oplus W^-$ of $\nu_V(\mathcal{H})$ times a term at $Y$; this comes from the Siegel-Weil formula;
2. the absolute convergence of the double integral over $\mathcal{G} \times \mathcal{G}$ of the sum of these terms against $|\varphi_1|$ and $|\varphi_2|$; this comes from rapid decay;
3. the absolute convergence of the kernel integrals that define the lifts, with a bound that does not depend on $h$, and $\nu_V(\mathcal{H}) < \infty$; this also comes from rapid decay;
4. the terms at two Lagrangian frames of the same Lagrangian agree, they move under $U(W)(F)$ as the Weil datum moves, and the term at a graph is a value of $\langle \omega(1, \gamma^{-1}) f_2, f_1 \rangle$;
5. the term at $Y$ is invariant under the unipotent radical of the isotropic frame of $Y$;
6. the integral of a cusp form against a continuous function that is invariant under such a unipotent radical is $0$.

With these facts, a kernel identity writes the left side as a double integral of the sum of terms, and the convergence allows the exchange of sum and integrals. The Lagrangians that meet the first factor of $W \oplus W^-$ in $0$ are the graphs, and their sum is the matrix coefficient integral on the right. For each other Lagrangian, facts 5 and 6 show that its contribution is $0$, since the forms $\varphi_i$ are cuspidal. $\square$

This is the inner product formula of Rallis (1984) in the case of a definite target group, where the Siegel-Weil formula is in its convergent range and no regularisation is needed.

### Multiplicity one for algebraic modular forms

Let $L$ be a CM field with maximal totally real subfield $L^+$, and $n \ge 1$. Let $G$ be the unitary group in $n$ variables over $L^+$ attached to $L$, with rational points $G(\mathbb{Q})$ and finite adelic points $G(\mathbb{A}_f)$. An *algebraic weight* is an irreducible finite-dimensional representation $\rho$ of $G(\mathbb{Q})$ on $W$ whose matrix coefficients are polynomials in the images of the matrix entries under the complex embeddings of $L$. An *algebraic modular form* of weight $\rho$ is a function $f : G(\mathbb{A}_f) \to W$ with $f(\gamma g) = \rho(\gamma) f(g)$ for $\gamma \in G(\mathbb{Q})$ that is fixed under right translation by a principal congruence subgroup of some level $N > 0$. An *irreducible space* is a nonzero subspace $S$ of such forms that is stable under right translation and has no proper nonzero stable subspace.

A *split place* is a place $v$ of $L^+$ with an embedding of $L$ into $L^+_v$; it gives a place $w$ of $L$, and $G(L^+_v) \cong \mathrm{GL}_n(L_w)$. An irreducible smooth representation $\sigma$ of $\mathrm{GL}_n(L_w)$ is a *local component* of $S$ if there is an injective map $T : \sigma \to S$ that intertwines $\sigma$ with right translation by the elements of $G(\mathbb{A}_f)$ that are trivial outside $v$. At a place $v$ that is not split, an *inert datum* at a place $w$ over $v$ gives an unramified Hermitian model of $G$ at $v$. The space $S$ has *Satake parameter* $\alpha \in \mathbb{C}^{\lfloor n/2 \rfloor}$ at $v$ if it contains a nonzero vector, fixed by a subgroup $U$ whose elements that are trivial outside $v$ are those of the maximal compact subgroup at $v$, on which every element of the spherical Hecke algebra at $v$ acts by its Satake transform at $\alpha$.

**Theorem 5.21.3 (Multiplicity one from all places).** Let $S_1$ and $S_2$ be irreducible spaces of algebraic modular forms of the same algebraic weight. Assume:
1. at every split place, $S_1$ and $S_2$ have equivalent local components;
2. at every place $v$ of $L^+$ that is not split, there are a place $w$ of $L$ over $v$, an inert datum and a parameter $\alpha$ such that $S_1$ and $S_2$ both have Satake parameter $\alpha$ at $v$.

Then $S_1$ and $S_2$ are isomorphic as representations of $G(\mathbb{A}_f)$.

Lean: `GlobalTheory.GlobDet.main` (also `GlobalTheory.T.algebraic_modular_forms_strong_multiplicity_one`, a second name)

*Proof.* Choose a nonzero $f \in S_1$ and a level $N$ that fixes it. At each place $v$ that is not split, the vectors of hypothesis 2 are fixed by the maximal compact subgroup at $v$. A lemma on Satake parameters shows that every vector of $S_i$ fixed by such a $U$ is an eigenvector of the spherical Hecke algebra at $v$ with the Satake transform at $\alpha$ as eigenvalue. With hypothesis 1, a lemma on Hecke modules at all places gives a linear map $\phi$ that sends the vectors of level $N$ of $S_1$ to vectors of level $N$ of $S_2$, is not zero on them, and commutes with every double coset operator of level $N$. A reconstruction lemma turns $\phi$ into an isomorphism of representations. $\square$

The standard statement is that an irreducible admissible representation of $G(\mathbb{A}_f)$ is the restricted tensor product of its local components (Flath, 1979). So two irreducible constituents that are isomorphic at every place are isomorphic. For algebraic modular forms in the sense of Gross (1999), this is the form used here. Strong multiplicity one asks for agreement at almost all places only; the theorem here does not give that.

**Remark 5.21.4 (Formalization).** Several facts about the Lean code:
1. `GlobalTheory.T.algebraic_modular_forms_strong_multiplicity_one` is a second name, proved by `first | exact @… | …` under `maxHeartbeats 1000000` (AlgebraicModularFormsStrongMultiplicityOneStatement.lean:7). Its name says "strong multiplicity one", but its hypotheses are at all places: equivalent local components at every split place and the same Satake parameters at every other place. Each place that is not split must also carry a spherical vector in both spaces.
2. The definitions are `NG.IsIrrRep` and `NG.IsoRep` (Formalism/LocalToGlobal/GaloisLevelStructure/DefsAut.lean:52 and :55), `NG.SatAt` (DefsAutLoc.lean:14), `NG.AlgWt` (DefsAut.lean:81), local components `IsLocS` (Definitions/AutomorphicMembership/RingSpecNormalisedCharacterEq.lean:49) and inert data `InertDatum` (Formalism/AlgebraicWeights/InertDatumExists.lean:18). The proof uses `GlobalTheory.InertSph.satU_of_fixed` (SatUOfFixed.lean:24), `GlobalTheory.T.algebraicModularForms_heckeModules_iso_all_places` and `GlobalTheory.HeckeRecon.recon` (HeckeDEqSum.lean:109); these are not unfolded here.
3. `rallisConv_of_siegelWeil` is one term (RallisConvOfHypotheses.lean:19) that applies `GlobalTheory.RawLift.rallisConv_of_steps` (Proofs/InertiaEigenvalues/RallisConvOfSteps.lean:23) to the six facts. They are `SWPair`, `EisAbs`, `KerAbs`, `TermMove`, `TermInv` and `CuspKill` (Definitions/NonGaloisDescent/IsWeilDatumOOneOfRankZero.lean:56, 62, 69, 75, 83 and 90). Only the first uses the Siegel-Weil formula (`swPair`, SwSection.lean:91), and only the second and third use rapid decay (`eisAbs`, LintegralNeTopOfBounds.lean:104, and `kerAbs_of_cuspRapidDecay`, KerAbsOfCuspRapidDecay.lean:21). The other three are proved without hypotheses (OmRatInvApply.lean:58, TermInv.lean:19, CuspKillHolds.lean:17).
4. The conclusion is `GlobalTheory.RawLift.RallisConv` (Definitions/NonGaloisDescent/LengthPosOfPosDef.lean:61), with the lift `upLift` at line 57 and the pairing `thetaIP` at line 54. The Siegel-Weil formula is a definition of a proposition (PublishedTheorems/TwistedTraceFormula/WeilSiegelFormulaUnitary.lean:56); the theorem keeps it as a hypothesis.
