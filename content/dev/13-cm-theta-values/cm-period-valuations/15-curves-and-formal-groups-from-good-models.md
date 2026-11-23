---
title: Curves and formal groups from good models
decls:
  - GlobalTheory.TwV.Lt.exists_genusOne_formal_iso_of_unramified_good_reduction
  - GlobalTheory.CurveThetaInert.torsionTaylorAlgebraic_latticeExists_of_cm
  - GlobalTheory.CurveDictionary.curveDict_of_cm
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Curves and formal groups from good models

The service row of Section 6 needs six hypotheses. Hypothesis 5 came from the CM good model condition in Section 13. This section derives hypotheses 1, 2, 3 and 6 from the same condition: algebraic torsion, genus one models over lattices, the curve dictionary, and curve existence. The good model condition gives a Weierstrass equation with unramified integral coefficients and a unit discriminant. Two further statements on such a model are needed: at an inert prime its formal group is isomorphic to a formal group of height $2$ with an explicit logarithm (the Honda condition), and its torsion points of order prime to $l$ have unramified integral coordinates (the torsion condition). Both are theorems of other chapters. Together with the good model condition of [the previous section](/entry/good-model/), the results here complete the inputs of [the service row from Artin reciprocity](/entry/serv-h-row-of-artin/).

### Two conditions on good models

We keep the notation of Section 13: a squarefree $d \equiv 3 \pmod 4$, a lattice $L$ with complex multiplication by $d$, a prime $l \ge 5$ with $l \nmid d$, a ring isomorphism $\iota : \mathbb{C} \to \mathbb{C}_l$, and $\widehat{\mathbb{Q}}_l^{\mathrm{ur}} \subset \mathbb{C}_l$, the completion of the maximal unramified extension of $\mathbb{Q}_l$. Write $\wp$ and $\wp'$ for the Weierstrass function of $L$ and its derivative.

For $g_2, g_3$ in a field $k$ of characteristic $0$, let $c_2 = g_2/20$, $c_3 = g_3/28$, and for $k \ge 4$

$$
c_k = \frac{3}{(2k+1)(k-3)} \sum_{m=2}^{k-2} c_m c_{k-m}.
$$

These are the coefficients of the Laurent series $\wp(z) = z^{-2} + \sum_{k \ge 2} c_k z^{2k-2}$ of the Weierstrass function with invariants $g_2, g_3$. Put

$$
u_{g_2, g_3}(z) = z \cdot \frac{1 + \sum_{k \ge 2} c_k z^{2k}}{1 - \sum_{k \ge 2} (k-1) c_k z^{2k}} \in k[[z]].
$$

The numerator is $z^2 \wp(z)$ and the denominator is $-z^3 \wp'(z)/2$, so $u_{g_2,g_3} = -2\wp/\wp'$: it expresses the parameter $-2x/y$ of the curve $y^2 = 4x^3 - g_2 x - g_3$ as a series in the elliptic logarithm $z$. Let

$$
\ell(X) = \sum_{j \ge 0} \frac{X^{l^{2j}}}{l^j} \in \mathbb{Q}_l[[X]].
$$

This is the logarithm of a formal group of height $2$ of the kind studied by Honda ([formal group laws](/learn/formal-groups/#formal-group-laws)).

**Definition 5.15.1 (Honda condition).** The *Honda condition* says: for all $d$, $L$, $l$ as above such that $l$ is inert in $\mathbb{Q}(\sqrt{-d})$, that is, $-d$ is not a square modulo $l$, for every $\iota$ and every good model $(g_2, g_3)$ of $L$ at $(l, \iota)$, there is $\varepsilon \in \widehat{\mathbb{Q}}_l^{\mathrm{ur}}$ with $|\varepsilon| = 1$ such that every coefficient of the series $u_{g_2, g_3}(\varepsilon\, \ell(X))$ lies in $\widehat{\mathbb{Q}}_l^{\mathrm{ur}}$ and has absolute value at most $1$.

The composite of the logarithm $\varepsilon\,\ell$ with the exponential $u_{g_2,g_3}$ of the curve is a homomorphism between the two formal groups. The condition says that it is integral, so that the formal group of the good model is isomorphic over the unramified integers to the group with logarithm $\varepsilon\,\ell$. The Honda condition is a theorem: [the Honda condition for CM curves](/entry/honda-cm3-cm3/), with a second proof in [the third integrality statement](/entry/cm-integrality-three/).

**Definition 5.15.2 (Torsion condition).** The *torsion condition* says: for all $d$, $L$, $l$ as above, every $\iota$ and every $\lambda \in \mathbb{C}_l^\times$ such that $(\lambda^4 \iota(g_2(L)), \lambda^6 \iota(g_3(L)))$ is a good model, and for every $z \in \mathbb{C}$ with $Nz \in L$ and $z \notin L$ for some $N \ge 1$ with $l \nmid N$, the numbers $\lambda^2 \iota(\wp(z))$ and $\lambda^3 \iota(\wp'(z))$ lie in $\widehat{\mathbb{Q}}_l^{\mathrm{ur}}$ and have absolute value at most $1$.

So the torsion points of order prime to $l$ of the good model have unramified integral coordinates. This is the classical behaviour of torsion on a curve with good reduction ([reduction and minimal models](/learn/elliptic-curves/#reduction-and-minimal-models)). The torsion condition is a theorem: [the torsion condition for CM curves](/entry/cm4/).

### Curve existence

Recall the curve existence hypothesis and the curve condition from Section 2.

**Theorem 5.15.3 (Curve existence from good models).** Assume the CM good model condition. Then the curve existence hypothesis holds.

Lean: `GlobalTheory.TwV.Lt.exists_genusOne_formal_iso_of_unramified_good_reduction`

*Proof.* The Honda condition holds by [the Honda condition for CM curves](/entry/honda-cm3-cm3/). Let $D$, $\mathfrak{c}$, $\delta$, $B$, $\chi$ and $p$ be as in the hypothesis, so that $p \ge 5$ is inert in $K$ and prime to the norm of $\mathfrak{c}$, and let $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$ be a ring map. The good model condition and the Honda condition give a genus one model at $p$: a formal group $g$ at $p$ whose map is $\lambda$, with a Lubin-Tate isomorphism, a model over the Witt vectors, and the theta condition at $(\mathfrak{c}, \delta)$. The part of the curve condition on the $2$-torsion of $g$ and $B$ is one of the parts of the theta condition. The other parts of the curve condition ($p \ge 5$, $p$ inert, the conditions on $\mathfrak{c}$, $\delta$ and $\chi$) are hypotheses. So $g$ satisfies the curve condition. $\square$

### Lattice models and the curve dictionary

The next result gives hypotheses 1, 2 and 3 of Section 6. We describe them as in that section.
1. *Algebraic torsion.* For every datum $D$, curve ideal $\mathfrak{c}$, twelfth root $\delta$ of the discriminant of its lattice, base $B$ and character $\chi$ of the right type, the Taylor coefficients of $B$ at the torsion points twisted by $\chi$ are algebraic.
2. *Genus one models over lattices.* For every $D$, $\mathfrak{c}$, $\delta$ as in 1, every prime $p \ge 5$ inert in $K$ and every $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$, there are another curve ideal $\mathfrak{c}'$ with a twelfth root $\delta'$ that has the same value at $\lambda$ as $(\mathfrak{c}, \delta)$, and a formal group $g$ at $p$ with map $\lambda$, a Lubin-Tate isomorphism, a model over the Witt vectors, and the theta condition at $(\mathfrak{c}', \delta')$.
3. *Curve dictionary.* For every $D$, $\mathfrak{c}$, $\delta$, every prime $l \ge 5$ inert in $K$, and every formal group $g$ at $l$ with a Lubin-Tate isomorphism, the theta condition at $(\mathfrak{c}, \delta)$ and a model $W$ over the Witt vectors, there are $g_2, g_3, \varepsilon, s_2 \in \widehat{\mathbb{Q}}_l^{\mathrm{ur}}$ such that $g_2, g_3$ are the invariants of $W$, $\varepsilon$ is the inverse of the unit of the Lubin-Tate isomorphism, the sigma series of the lattice, rescaled by the inverse $u^{-1}$ of the scale unit of the model, is $u^{-1}$ times the sigma series of $W$ with parameter $s_2$, the product $u^{-1}\varepsilon$ has absolute value $1$, the curve relations hold for $(g_2, g_3, \varepsilon, s_2)$, and the dictionary integrality holds for every datum $D'$.

Statement 2 differs from the genus one model of the previous proof: it drops the condition that $p$ is prime to the norm of $\mathfrak{c}$, and in exchange it may replace $(\mathfrak{c}, \delta)$ by a pair with the same value.

**Theorem 5.15.4 (Curve dictionary from good models).** Assume the CM good model condition, the Honda condition and the torsion condition. Then the curve dictionary 3 holds.

Lean: `GlobalTheory.CurveDictionary.curveDict_of_cm`

*Proof.* The dictionary follows from the good model condition and the torsion condition, together with eight results of other chapters on lattices, Weierstrass models and formal groups. Among them are the algebraicity of the sigma series of a lattice with algebraic invariants, the integrality of the theta unit function of a short Weierstrass model, and the integrality of the inverse series of an integral formal group isomorphism. These results are not unfolded here. The Honda condition is not used. $\square$

**Theorem 5.15.5 (Torsion algebraicity, lattice models and the curve dictionary).** Assume the CM good model condition. Then algebraic torsion 1, genus one models over lattices 2 and the curve dictionary 3 hold.

Lean: `GlobalTheory.CurveThetaInert.torsionTaylorAlgebraic_latticeExists_of_cm`

*Proof.* Algebraic torsion holds with no hypothesis. The Honda condition holds by [the third integrality statement](/entry/cm-integrality-three/), and the torsion condition holds by [the torsion condition for CM curves](/entry/cm4/). Statement 2 follows from the good model condition and the Honda condition by the construction of genus one models. Statement 3 is the previous theorem. $\square$

**Remark 5.15.6 (Formalization).** Several facts about the Lean code:
1. The Honda condition is `Formalism.L2.Th1.CM.CM3` and the torsion condition is `Formalism.L2.Th1.CM.CM4` (Formalism/LocalToGlobal/TorsionIntegrality/CMGoodModels/Statement.lean:49 and CM4.lean:5). The series $u_{g_2,g_3}$ is `uSer` (Statement.lean:32), built from `wpNum`, `wpDen` and the coefficients `cW`, and $\ell$ is `ltLog` (line 35).
2. `curveDict_of_cm` takes the Honda condition as an argument but does not use it: the argument is written `_` (CurveDictOfCm.lean:18). The eight results are passed to `curveDict_of_inputs` (SatakeParameters/PadicNormTwoHundredSixteenEqOneOfFiveLe.lean:666); none of them is in the chapter outline, so they have no entry links. The three named in the proof are `curveLattice_sigmaTwo_algebraic_of_invariants_algebraic`, `thetaUnitFunction_shortModel_integral` and `inverse_series_formalGroup_iso_integral`; the proof describes them by their names only.
3. In the same way `datum_exists_lattice` takes the torsion condition and does not use it (SatakeParameters/ExistsRingEquivTranscendental.lean:348). So in `torsionTaylorAlgebraic_latticeExists_of_cm` the torsion condition reaches only the curve dictionary.
4. The first part of `torsionTaylorAlgebraic_latticeExists_of_cm`, `AlgTAll`, is the theorem `GlobalTheory.ThLoc.algTAll` and does not use the good model condition (TorsionTaylorAlgebraicLatticeExistsOfCm.lean:17).
5. Two different proofs of the Honda condition are used: `GlobalTheory.HondaCM3.cm3` in the curve existence theorem (ExistsGenusOneFormalIsoOfUnramifiedGoodReduction.lean:24) and `ReciprocityTheory.ChartRestriction.L1.cmIntegralityThree` in the lattice models (TorsionTaylorAlgebraicLatticeExistsOfCm.lean:18).
6. The curve existence theorem is a wrapper of `curveEx_of_cm` (same file, line 17), which uses `datum_exists_coprime` (ExistsRingEquivTranscendental.lean:277). The definitions `AlgTAll`, `GenusOneModelExistsLattice` and `CurveDict` (Formalism/LocalToGlobal/InertKernelTheory/StatementAlgT.lean:9, GenusOneModelExistsLattice.lean:17, DefsRepDict.lean:10) are described above from their statements. The predicates `At`, `ModelOverW`, `LTIso`, `B.AlgT`, `CurveAt` and `DictInt` are not unfolded here.
