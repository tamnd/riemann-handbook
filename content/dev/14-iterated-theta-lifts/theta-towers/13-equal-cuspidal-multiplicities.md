---
title: Equal cuspidal multiplicities
decls:
  - GlobalTheory.T.twisted_multiplicity_one
  - GlobalTheory.MultEqFinal.twisted_multiplicity_eq
  - UpperTheory.Lit.I5.unitary_theory_of_harishChandra_langlands_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Equal cuspidal multiplicities

One item of the step [the hypotheses are not empty](/step/nonempty-hyps/) asks that the real data of the families have equal multiplicities: a cuspidal representation of a unitary group with fixed discrete series at the real places occurs as often in the cuspidal spectrum as its transfer to an inner form with the same local data. This section proves it from ten published results on representations of real, $p$-adic and finite groups. The work is in Volume 8, in [the equality of cuspidal multiplicities](/entry/mult-eq-of-sides/); here we state the ten inputs, check which of them enter, and turn the conditions on a real datum into the record that the theorem of Volume 8 needs.

The notion of equal multiplicities for a real datum $R$ is the one of Volume 8: for each Hermitian space $W_i$ of $R$, each discrete series model $M_0$ on the space $Y$ of $R$, each isomorphism $\Phi$ of the finite adelic groups that comes from a local isometry with the frame conditions, and each good irreducible admissible $\sigma$,

$$m(\sigma, M_0) = m(\sigma \circ \Phi^{-1}, M_W(i)),$$

where $m$ is the multiplicity in the space of cusp forms with the given discrete series at the real places.

We state the ten inputs in rough form, as the Lean statements give them. We have not compared each Lean form with its source in detail.

**Theorem 3.13.1 (Analyticity of matrix coefficients).** Let $G$ be a real reductive group with a maximal compact subgroup $K$, and $\pi$ an admissible representation. Then the $K$-finite matrix coefficients of $\pi$ are real analytic. The Levi submodules of the induced representations are dense.

This is the analyticity theorem of Harish-Chandra, *Representations of a semisimple Lie group on a Banach space I*, Trans. Amer. Math. Soc. 75 (1953).

**Theorem 3.13.2 (Classification of discrete series).** Let $\mathrm{U}(p, q)$ be a unitary group of rank $n = p + q$, with signature $\varepsilon$. For each strictly decreasing $\lambda \in \mathbb R^n$ with $\lambda_a - (n-1)/2 \in \mathbb Z$ there is an irreducible unitary square integrable representation $\pi_\lambda$ with infinitesimal character $\lambda$, a unique lowest $K$-type $\lambda + \rho_n - \rho_c$, and all other $K$-types of the form $\lambda + \rho_n - \rho_c$ plus a sum of positive roots. Every irreducible unitary square integrable representation is equivalent to one $\pi_\lambda$, after a permutation of the coordinates.

This is the classification of Harish-Chandra, *Discrete series for semisimple Lie groups II*, Acta Math. 116 (1966), with the lowest $K$-type of W. Schmid, *Some properties of square-integrable representations of semisimple Lie groups*, Ann. of Math. 102 (1975).

**Theorem 3.13.3 (Rapid decay of cusp forms).** A cuspidal function of uniform moderate growth on an adelic quotient decays rapidly: for every $N$ its absolute value is bounded by a constant times the $N$-th negative power of the height.

**Theorem 3.13.4 (Finiteness of Harish-Chandra).** For a fixed $K$-type at the real places, a fixed infinitesimal character and a fixed level, the space of automorphic forms is finite dimensional.

These two results are in Harish-Chandra, *Automorphic forms on semisimple Lie groups*, Lecture Notes in Math. 62, Springer (1968).

**Theorem 3.13.5 (Trace class).** For a smooth compactly supported test function $f$, the operator $R_{\mathrm{cusp}}(f)$ on the cuspidal spectrum is of trace class.

This is in I. M. Gelfand, M. I. Graev and I. I. Piatetski-Shapiro, *Representation theory and automorphic functions*, Saunders (1969).

**Theorem 3.13.6 (Factorisation of Dixmier and Malliavin).** Every smooth compactly supported function $f$ on a Lie group is a finite sum $f = \sum_i g_i * h_i$ of convolutions of smooth compactly supported functions.

This is J. Dixmier and P. Malliavin, *Factorisations de fonctions et de vecteurs indéfiniment différentiables*, Bull. Sci. Math. 102 (1978).

**Theorem 3.13.7 (Factorisation of Flath).** An irreducible admissible representation of an adelic reductive group is a restricted tensor product of irreducible admissible local representations, spherical at almost all places.

This is D. Flath, *Decomposition of representations into tensor products*, Proc. Sympos. Pure Math. 33, Part 1 (1979).

**Theorem 3.13.8 (Geometric lemma).** The composition of a parabolic restriction with a parabolic induction of a $p$-adic general linear group has a filtration whose subquotients are inductions of restrictions, indexed by double cosets of Weyl groups.

This is J. Bernstein and A. Zelevinsky, *Induced representations of reductive p-adic groups I*, Ann. Sci. École Norm. Sup. 10 (1977).

**Theorem 3.13.9 (Polynomial ring of Zelevinsky).** The Grothendieck ring of the smooth representations of finite length of all $p$-adic general linear groups, with the product given by parabolic induction, is a polynomial ring in the classes of the segments.

This is A. Zelevinsky, *Induced representations of reductive p-adic groups II*, Ann. Sci. École Norm. Sup. 13 (1980).

**Theorem 3.13.10 (Cuspidal characters of Green).** The cuspidal irreducible characters of $\mathrm{GL}_d(\mathbb F_g)$ are parametrized by the primitive characters of $\mathbb F_{g^d}^\times$ up to Frobenius, and each has degree

$$\prod_{i=1}^{d-1} (g^i - 1).$$

This is J. A. Green, *The characters of the finite general linear groups*, Trans. Amer. Math. Soc. 80 (1955).

**Theorem 3.13.11 (Equal multiplicities from the inputs).** Assume the ten inputs above. Let $R$ be a real datum with a face $F$, and assume that the conditions of the datum hold at $F$. Then $R$ has equal multiplicities.

Lean: `UpperTheory.Lit.I5.unitary_theory_of_harishChandra_langlands_alt`.

*Proof.* We check the assumptions of [Theorem 2.5.4 of Volume 8](/entry/mult-eq-of-sides/). Assumption 1 is the [existence of pseudo-coefficients](/entry/local-pseudo-coefficient-existence-unitary-group/) for the discrete series of $\mathrm{U}(p, q)$ with large gaps. Assumption 2 consists of rapid decay, the finiteness of Harish-Chandra, the factorisation of Dixmier and Malliavin, and the statement of Green. Assumption 3, the spectral side, follows from the classification of discrete series and the trace class property. For assumption 4, [trace separation](/entry/trace-separation-of-iwahori-trace/) has two inputs: the trace on Iwahori double cosets, which is proved, and the separation of exponents, which follows from the geometric lemma and the polynomial ring of Zelevinsky. Assumption 5 is the [direct elliptic side](/entry/elliptic-side-direct/), from the trace class property, and the elliptic expansion. $\square$

**Theorem 3.13.12 (Equal multiplicities for the real data of the chapter).** Assume the ten inputs above. Let $D$ be a datum and $R$ a real datum of $D$ with a face $F$, of the kind used for the families of this chapter. Assume:

1. the family of $R$ is good at some level $s$;
2. $R$ satisfies the weak characterisation at $F$, and the condition of existence at the points holds;
3. the host hypothesis of $D$ holds;
4. there are size data for $D$ with a parameter choice;
5. the class field of $D$ is the whole field;
6. the guard on $Q$ and the condition on good types hold for the underlying real datum.

Then the underlying real datum of $R$ has equal multiplicities.

Lean: `GlobalTheory.MultEqFinal.twisted_multiplicity_eq` (also `GlobalTheory.T.twisted_multiplicity_one`, a second name).

*Proof.* The conditions of the datum at $F$ are a record of six fields, and we build it from the hypotheses. The core field comes from the weak characterisation. The parameter choice is hypothesis 4. The absolute irreducibility of the characters is a field of the goodness of the family. The good types and the guard are hypothesis 6. The gap condition

$$100\, r^4 \le \lambda_{n}(\tau) - \lambda_{n+1}(\tau)$$

on the parameters at the real places is a field of the host hypothesis. Then [Theorem 3.13.11](/entry/unitary-theory-of-harish-chandra-langlands-alt/) applies. $\square$

**Remark 3.13.13 (Formalization).** The theorem from the inputs ([UnitaryThetaCorrespondenceOfHyp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/UnitaryThetaCorrespondenceOfHyp.lean#L15)) takes the analyticity of matrix coefficients and the factorisation of Flath and uses neither. Its name speaks of a theta correspondence and of Langlands, but neither appears in the statement or the proof; it is a wrapper of [Theorem 2.5.4 of Volume 8](/entry/mult-eq-of-sides/), whose proof is in [TraceEqXOfGeomExpansionX.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TraceEqXOfGeomExpansionX.lean#L555). In the theorem for the real data ([TwistedMultiplicityOne.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedMultiplicityOne.lean#L15)) hypothesis 5 is not used, the level $s$ is free and only the irreducibility field of hypothesis 1 is used, and no twist appears although the name speaks of one. The record of conditions is built in [ScalarHypothesesOfTopRows.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ScalarHypothesesOfTopRows.lean#L18). The ten inputs are statements in the published theorems of the formalization, for example [AdmissibleCoefficientsAnalytic.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/AdmissibleCoefficientsAnalytic.lean#L26) and [GreenCuspidalIff.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/GreenCuspidalIff.lean#L8).
