---
title: The weight case condition
decls:
  - GlobalTheory.ScalConj.twisted_scalar_conjugation
  - GlobalTheory.T.twisted_scalar_conjugation_invariance
  - GlobalTheory.PrimIn.stage4_alt
  - GlobalTheory.T.real_data_weight_vector_family_alt
  - GlobalTheory.PrimIn.primRows3_typesSep3_alt
  - GlobalTheory.T.real_data_weight_vector_family_core_alt
  - GlobalTheory.PrimIn.holds_of_ties_alt
  - GlobalTheory.T.rational_data_sized_family_alt
  - GlobalTheory.Mem.R3.Rw.AtDatumEvaluation.atDat_holds_alt
  - GlobalTheory.Mem.R3.Rw.AtDatumEvaluation.w_of_multEq_and_test_at_weights
  - GlobalTheory.T.w_of_weight_residue_char
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The weight case condition

This section proves the weight case condition from the theorems on theta conditions, the continuation of partial Hecke $L$-functions and the multiplicity statement at the weights. The weight case condition says that at each datum of the weight case, the real datum and the face satisfy four conditions together: primitive rows, the unused choice statements, the third level bound at $s = 1$, and separated types. Step 1 of [the Theorem on the origin extension](/entry/exists-base-lattice-of-prime-alt/) of Section 1 uses it, and so does the second nonvanishing statement of Section 13 and the saturated states of Section 16. The deep step is a conjugation invariance of twisted scalars. It rests on the Howe correspondence at unramified places, the inner product formula for theta lifts, matrix coefficients in the Fock model and the doubling method.

We take as given the following fourteen statements, the *theta condition theorems*. They are fields of $\mathcal{H}_M$ in Section 1.

1. The Howe correspondence at unramified places ([the local theta correspondence](/learn/theta/#the-local-theta-correspondence)).
2. Rapid decay of cusp forms.
3. Harish-Chandra's finiteness theorem for automorphic forms.
4. Harish-Chandra's theory of $(\mathfrak{g}, K)$-modules.
5. Harish-Chandra's classification of the discrete series (the discrete series cover).
6. The Casselman-Wallach theorem.
7. The Siegel-Weil formula for unitary groups ([the Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula)).
8. Convergence in the Siegel-Weil formula for unitary groups.
9. The local zeta integrals of the [doubling method](/learn/theta/#the-doubling-method).
10. The unramified computation of the doubling integrals for $\mathrm{GL}_n$.
11. The finiteness theorem of Bernstein and Zelevinsky: a representation of a $p$-adic reductive group parabolically induced from an irreducible representation has finite length.
12. Green's classification of the cuspidal characters of $\mathrm{GL}_d(\mathbb{F}_q)$.
13. The [Weil representation](/learn/theta/#the-weil-representation) of a unitary dual pair.
14. Schur orthogonality for square integrable representations: the matrix coefficients of a discrete series are square integrable, with inner products given by the formal degree.

We also assume the continuation of partial Hecke $L$-functions: the partial $L$-function of a Hecke eigenform, with the factors at a finite set of places removed, has a meromorphic continuation ([Hecke $L$-functions](/learn/class-field-theory/#tates-thesis-and-hecke-l-functions)). By statement 9, the Siegel Eisenstein series of the doubling method has a meromorphic continuation.

**Definition 6.15.1 (Data of the weight case).** Let $K$ be a context and $w$ a column datum over a base $B$ with twist datum $T$. A *datum* $z$ of $w$ at a stage $Z$ with weight set $W_t$ consists of a real datum $R$, a face $F$, a core, a geometric datum and a level. The datum is in the *weight case* if the group of $Z$ is true, the group condition holds at the stage, the constant $\kappa$ is defined, the real datum has the extension property, the geometric datum lies in the geometry, the core is principal, the group of $Z$ is of the second kind, $W_t$ is the weight set of $z$ at the scale of $K$, and the residue characteristic of each place of $W_t$ lies in the places of $T$.

**Definition 6.15.2 (The four conditions).** Let $R$ be a real datum and $F$ a face. We say that $(R, F)$ *holds* if four conditions hold: the rows of $(R, F)$ at level three are primitive; the unused choice statements hold; the third level bound holds at $s = 1$; and the types of $(R, F)$ at level three are separated. The *multiplicity equation* for $R$ is an equation between the multiplicities of the isotypic parts of $R$, and the *row test* for $(R, F)$ is the rationality test of the rows of the complex datum of $(R, F)$. The *weight case condition* says that along $\mathrm{Step}_w$ from the start condition, every datum $z$ in the weight case holds.

**Definition 6.15.3 (Size data and ties).** For $\varepsilon > 0$, a *size datum* $L$ at $\varepsilon$ has a scale $x$, a choice of parameters and size bounds. The *base ties* of $(R, F)$ and the *global ties* of a core with $(R, F)$, $\kappa$, $v_0$ and $O$ are the agreements between the real datum and the rational data of the family. The *integral level condition* says that the levels of the lifts are integral. The *Galois descent condition* says that the conjugation $c$ of the face acts on the twisted scalars without change, and the *positivity condition* says that the lifted scalars are positive at all places.

**Theorem 6.15.4 (Conjugation invariance of twisted scalars).** Assume the continuation of the Siegel Eisenstein series, statements 1, 2, 4, 7, 9, 10, 11, 13 and 14. Let $D$ be a datum with a real datum $R$, a face $F$ and $s \in \mathbb{N}$. Assume the third level bound at $s$, separated types, the weak characterization, the extension property and a choice of parameters. Assume that the phases are $1$, that $\psi$ is standard at $-1$, that the framed point has a bar tie, the extension of the orthonormal frames, the pins and the one form map row, and the phase tie. Assume the Hecke and adjoint conditions for rows and lifts, the Hecke, unit and equivalence conditions on the principal level, the block condition, the row test, the lift tests and the surjectivity on $\mathbb{C}$, $\kappa > 0$ and $\lambda_3 > 0$, uniform levels, the principal level weights, the first theorem on parts and the weights of the parts. Then the Galois descent condition holds for the conjugation of $F$.

Lean: `GlobalTheory.ScalConj.twisted_scalar_conjugation` (also `GlobalTheory.T.twisted_scalar_conjugation_invariance`, a second name).

*Proof.* At an unramified place, the Howe correspondence (statement 1) shows that the base level of a theta lift is conjugate to the base level of the lift of the conjugate. So it suffices to give four inputs. The first is the law of the level character at a finite datum: the local integral of a single block in the place models. The second is the inner product formula for the twisted theta lift ([the Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula)). The third is the formula for a matrix coefficient of a Fock vector, which comes from the harmonic module of the Fock model, the decay of harmonics and an integral of powers of $\cosh$. The fourth is the identity between the finite zeta integral of a theta lift and the value of the partial $L$-function, which uses statements 10 and 11. Together they show that the twisted scalar of the conjugate is the conjugate of the twisted scalar, which is the Galois descent condition. $\square$

**Theorem 6.15.5 (Descent and positivity).** Assume the theta condition theorems and the continuation of partial Hecke $L$-functions. Let $D$ be a datum with a finite group $G$, a family, a core, a real datum $R$, a face $F$, data $\kappa$, $v_0$, $O$, and a size datum. Assume the base ties and the global ties, the multiplicity equation for $R$ and the row test. Assume that the levels of the lifts are positive, that $\kappa > 0$ and that $\lambda_3 > 0$ at each index. Then the Galois descent condition holds for the conjugation of $F$, and the positivity condition holds for $R$.

Lean: `GlobalTheory.PrimIn.stage4_alt` (also `GlobalTheory.T.real_data_weight_vector_family_alt`, a second name).

*Proof.* Statement 9 gives the continuation of the Siegel Eisenstein series. The multiplicity equation makes the principal level a unit and an equivalence; with the lift tests it gives the principal level weights, and the partial $L$-function at $s = 1$ gives the parts. The theorem on conjugation invariance gives the Galois descent condition. With the descent condition, the conjugate identity shows that the lifted scalars are positive at all places. $\square$

**Theorem 6.15.6 (Primitive rows and separated types).** Assume the theta condition theorems and the continuation of partial Hecke $L$-functions. For each $\varepsilon > 0$ there is $x_0$ such that the following holds. Let $D$, $G$, a family, a core, $R$, $F$, $\kappa$, $v_0$, $O$ and a size datum $L$ at $\varepsilon$ with scale at least $x_0$ be given, with the size bounds and a choice of parameters. Assume the base ties, the global ties, the multiplicity equation and the row test. Then the rows of $(R, F)$ are primitive, the types are separated, and there is a trace with the semisimple and the separation properties.

Lean: `GlobalTheory.PrimIn.primRows3_typesSep3_alt` (also `GlobalTheory.T.real_data_weight_vector_family_core_alt`, a second name).

*Proof.* The multiplicity equation makes the principal level bijective for large scales, which gives $x_0$. It lifts the data and gives the unit and equivalence conditions. The compatibility of the core gives the lift tests on the modular lattice, and the positive lift tests give the principal level weights and the separated trace. The theorem on descent and positivity gives the Galois descent and positivity conditions. The junk at inert places vanishes. The continuation of partial $L$-functions, with statements 1, 2, 4, 5, 7, 9, 10 and 11, gives the parts. The primitive rows follow from the parts. $\square$

**Theorem 6.15.7 (Sized families hold).** Assume the theta condition theorems and the continuation of partial Hecke $L$-functions. For each $\varepsilon > 0$ there is $x_0$ such that for every stage, every datum $z$ with a size datum $L$ at $\varepsilon$ with scale at least $x_0$, the size bounds and a choice of parameters, the base ties, the global ties, the multiplicity equation, the row test and the integral level condition imply that $z$ holds.

Lean: `GlobalTheory.PrimIn.holds_of_ties_alt` (also `GlobalTheory.T.rational_data_sized_family_alt`, a second name).

*Proof.* Take $x_0$ from the theorem on primitive rows. That theorem gives primitive rows, separated types and the trace. The core comes from its weak form. Rapid decay of cusp forms (statement 2) gives Schur orthogonality for all the rows. The algebraic form has the same norm at conjugate embeddings, and the weights of the levels are irreducible. The four conditions follow: the rows are primitive, the unused choice statements hold with the extension, the conjugation, the levels and the integral level condition, the third level bound holds, and the types are separated. $\square$

**Theorem 6.15.8 (Evaluation at data).** Assume the theta condition theorems and the continuation of partial Hecke $L$-functions. Then along $\mathrm{Step}_w$ from the pinned condition, every datum $z$ whose group is true, with the group condition, the extension property and the geometric condition, satisfies: if the multiplicity equation and the row test hold for $z$, then $z$ holds.

Lean: `GlobalTheory.Mem.R3.Rw.AtDatumEvaluation.atDat_holds_alt`.

*Proof.* Eventually the size data exist at the scale of the theorem on sized families, and the hosts have their frames. By statement 12 there is a bare stage $Z'$. The ledger gives size data $L$ at the stage. The datum $z$ has a copy $y$ at the stage, and it is enough to prove that $y$ holds. The types of the copy are true. The weak characterization of orthonormal frames gives the extension of frames, and the characterization at level three gives the one form map row. The values lie in the coefficient field, the Weber level and the uniform level hold, and the integral level condition holds by statements 1 to 3. The theorem on sized families then gives that $y$ holds, so $z$ holds. $\square$

**Theorem 6.15.9 (Weight case condition).** Assume the theta condition theorems and the continuation of partial Hecke $L$-functions. Assume that along $\mathrm{Step}_w$ from the start condition, every datum in the weight case satisfies the multiplicity equation and the row test. Then the weight case condition holds.

Lean: `GlobalTheory.Mem.R3.Rw.AtDatumEvaluation.w_of_multEq_and_test_at_weights` (also `GlobalTheory.T.w_of_weight_residue_char`, a second name).

*Proof.* The start condition implies the pinned condition, so the theorem on evaluation at data holds along $\mathrm{Step}_w$ from the start condition. A datum in the weight case satisfies the hypotheses of that theorem, and by assumption it satisfies the multiplicity equation and the row test. So it holds. $\square$

**Remark 6.15.10 (Formalization).** The theorems are at [TwistedScalarConjugationInvariance.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedScalarConjugationInvariance.lean#L9) (second name at line 23), [RealDataWeightVectorFamily.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/RealDataWeightVectorFamily.lean#L17) (line 40), [RealDataWeightVectorFamilyCore.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/RealDataWeightVectorFamilyCore.lean#L18) (line 45), [RationalDataSizedFamily.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/RationalDataSizedFamily.lean#L12) (line 33) and [WeightSetResidueCharacteristic.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/WeightSetResidueCharacteristic.lean#L18) (lines 52 and 68). The weight case condition is `WeightCaseCondition` ([NonzeroPlacesOverPrimesLifts.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NonzeroPlacesOverPrimesLifts.lean#L102)), and "holds" is the record `Holds` with the fields `prim`, `aux`, `ok` and `sep`. In the conjugation invariance theorem the intro `pI hH pD _ pBZ _ _ pU pW _` drops four of its ten published hypotheses: the Weil representation of a unitary pair, the doubling zeta integrals, Schur orthogonality and the Harish-Chandra modules. The hypothesis of rapid decay of cusp forms is passed where the inner product formula and the zeta integral identity take their first argument. In the main theorem the multiplicity equation and the row test at the weights are a hypothesis; in Section 1 they come from the multiplicity statement of $\mathcal{H}_M$, so the condition is reduced to an assumption of the same kind. Five of the nine weight case conditions (that $\kappa$ is defined, that the core is principal, the second kind and the two conditions on $W_t$) reach only the hypothesis, not the evaluation theorem. The names "weight residue char", "real data weight vector family", "rational data sized family" and "stage4" do not describe the statements. We did not unfold `MultEq`, `RowTest`, `TiesB`, `TiesG`, `LIntegral`, `GalD`, `PPos`, `PrimRows3`, `TypesSep3`, `Ok3` or the fourteen published statements, so the definitions above give their roles.
