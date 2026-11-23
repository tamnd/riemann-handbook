---
title: Completions of cores and prime data
decls:
  - GlobalTheory.Member.exists_completion_of_core_satisfying_laws
  - GlobalTheory.T.exists_realisationPrimeData_curve_lifting
  - GlobalTheory.PrimeData.exists_real_primeData
  - GlobalTheory.RunJoin.archAt_of_run
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Completions of cores and prime data

This section proves three existence results. The first completes a core that satisfies the core laws to a top datum that satisfies all the laws; it is used in [the top datum of a core](/entry/exists-top-of-core/). The second gives local point data at every finite place for a global family of cusp forms; it is used in [the prime data for the heights](/entry/exists-prime-data-heights/). The third gives archimedean data for a global family; it is used in [the surjectivity from the hypotheses](/entry/onto-x-of-hypotheses-alt-alt/). All three entries are in Volume 15.

### Completing a core

Let $D$ be a datum with a CM host $E$ and with $m$ levels, and say that $j$ is *in range* if $1 \le j \le m$. A *core* $T$ over $D$ has parameters: moduli spaces $X_j$ with signatures $(p_j, q_j)$, a field of coefficients, uniformizations $U_j$, Hermitian spaces and level subgroups. The *core laws* are conditions on $T$ about cusp forms, lattices and exponents. These are not unfolded here.

**Definition 5.22.1 (Top datum and laws).** A *top datum* over a core $T$ adds three data: local data $G$ at concrete points, a connection $\nabla_j$ on each $X_j$, and delta data $\delta_j$. The top datum satisfies the *laws* if it satisfies the core laws and, at every $j$ in range:
1. the test condition and the regularity of $U_j$;
2. six conditions on $G$: datum, tower, data, points, lattices and base change;
3. if $1 \le j < m$, the period form does not depend on the model;
4. $\nabla_j$ is the canonical connection for some star ring structure on $\mathcal{O}_E$, and the canonical connection is unique;
5. the theta values of $\nabla_j$ are total and lie in the cusp forms of $T$ at $j$, and they are not zero if $1 \le j < m$;
6. the condition $K_\Psi$ at $j$.

**Theorem 5.22.2 (Completion of a core).** Assume chart independence. Let $T$ be a core over $D$ that satisfies the core laws. Assume:
1. $1 \le p_j + q_j$ for every $j$;
2. the condition $K_\Psi$ at every $j$ in range;
3. for every $j$ in range, every star ring structure on $\mathcal{O}_E$ and every canonical connection $\nabla$ at $j$, the theta values of $\nabla$ lie in the cusp forms of $T$ at $j$, and they are not zero if $j < m$.

Then there is a top datum $T'$ over $T$ that satisfies the laws.

Lean: `GlobalTheory.Member.exists_completion_of_core_satisfying_laws`

*Proof.* **Local data.** A theorem on local data at concrete points, applied to the pins of the core laws and to hypothesis 1, gives $G$ with the six conditions of law 2. **Connections.** For every $j$ there are a star ring structure $s_j$ and a canonical connection $\nabla_j$ for it, with no further hypothesis. **Regularity.** A lemma on levels shows from two pins that the level of $T$ is good. A theorem on charts at good levels, with the compactified moduli spaces and the moduli schemes, then gives the regularity of $U_j$. Put $T' = (T, G, \nabla, \delta)$ with trivial delta data. **Laws.** The test condition comes from the base change of sections. Law 3 comes from a theorem on lattice period forms. Chart independence gives the uniqueness of the canonical connection and the totality of theta values. Hypothesis 3 at $(s_j, \nabla_j)$ gives the rest of law 5, and hypothesis 2 is law 6. $\square$

So two of the laws, the place of the theta values and $K_\Psi$, enter as hypotheses.

### Prime data with curve lifting

Let $T$ be a top datum that satisfies the laws, and let $j$ be in range with the generic frame condition and the generic test condition. Let $G$ be a global family of cusp forms at $j$ with weights $\kappa$, $w_L$ and $w_F$; it has forms $w_1, \dots, w_N$ of weight $w_L$ and an eta form $\eta$. Let $K$ be the field of coefficients. At a finite place $\lambda$ of $K$ the family gives a curve $X_\lambda$ with ring of functions $\mathcal{O}_\lambda$. Each point $\zeta$ of $X_\lambda$ has a ramification index $e(\zeta)$ and an order function $\mathrm{ord}_\zeta$. These objects are not unfolded here.

**Definition 5.22.3 (Local point data).** *Local point data* $Q$ at $\lambda$ choose, at every point $\zeta$, a point $y(\zeta)$ of the family at $\lambda$, and they fix a cusp form $g_0$ of weight $w_F$ and integers $c(\zeta)$. They satisfy:
1. the *curve condition* if $\mathcal{O}_\lambda$ is finite dimensional over the local field and reduced, and $a \mapsto a e$ is a bijection from $\mathcal{O}_\lambda$ onto the section module, where $e$ is the restriction of $g_0$;
2. the *tie condition* for scalar data $S$ if, at every $\zeta$: the depth of $y(\zeta)$ is finite; the valuation of $\eta$ at $y(\zeta)$ is finite if $j < m$; $e(\zeta)$ times the depth is an integer; $c(\zeta) = e(\zeta)\, v_{y(\zeta)}(g_0)$; and for each $k$ and each form $g$ of weight $w_0 + k w_L$ or $w_F + k w_L$, the order at $\zeta$ of the restriction of $g$ is $e(\zeta)$ times $v_{y(\zeta)}(g)$ minus $k$ times the depth;
3. the *lift condition* for $(S, G_c, P_{rw}, T_n)$ if, when $G$ is tied for $(S, G_c, P_{rw})$ and conditions 1 and 2 hold, every element of the ball $A_0$ of $Q$ lifts to an element whose jet of order $a_0(T_n)$ lies in the lift module of order $T_n$.

The family $G$ is *tied* for $(S, G_c, P_{rw})$ if the $w_k$ span the lattice of $S$ and lie in the integral lattice, $\log N \le P_{rw}(|w_L| - 1)$, and there are bounds $m_\sigma$ for the logarithms of the sup norms of the $w_k$ at each embedding $\sigma$ whose mean is at most $G_c |w_L|$.

A *section point* at $(\zeta, y)$ is a complete discrete valuation ring $V$ with an evaluation at which $s_1, \dots, s_r$ vanish, $s_0$ is a unit, and the valuations at $y$ are those of the values. It *comes from $W$* if a compatible local map from the local ring at $\zeta$ to $V$ sends some prime element to a prime element. A family $y$ of section points gives local point data $Q(y)$, with $c(\zeta)$ the valuation of the value of $g_0$.

**Theorem 5.22.4 (Prime data with curve lifting).** Let $T$, $j$ and $G$ be as above, let $S$ be scalar data and $g_0$ a cusp form of weight $w_F$. Assume:
1. the curve hypothesis for $(G, S, g_0)$: the $w_k$ span for $S$, $G$ is big, the theta condition holds for $g_0$, and $g_0$ is not zero on any component;
2. generic values are injective and components split;
3. the condition BIR holds at $G$, and at every global family that is big;
4. $n(w_L) > 0$;
5. if $j < m$, then $\eta$ is not zero on any component.

Then for all real $G_c$ and $P_{rw}$ and every $T_n$ there are, at every finite place $\lambda$ and every point $\zeta$ of $X_\lambda$, a point $y_\lambda(\zeta)$ and a section point from $W$ at $(\zeta, y_\lambda(\zeta))$, such that at every $\lambda$ the data $Q(y_\lambda)$ satisfy the curve condition, the tie condition for $S$ and the lift condition for $(S, G_c, P_{rw}, T_n)$.

Lean: `GlobalTheory.PrimeData.exists_real_primeData` (also `GlobalTheory.T.exists_realisationPrimeData_curve_lifting`, a second name)

*Proof.* Fix $\lambda$. **Curve model.** Hypotheses 1 to 3 give a curve model $C$ of $G$ at $\lambda$ for $g_0$. From $C$, the ring $\mathcal{O}_\lambda$ is finite dimensional and reduced. So the uniformizer of the base is a uniformizer of $\mathcal{O}_\lambda$. **Points.** A lemma on real points gives, at every $\zeta$, a point $y$ and a section point from $W$ at $(\zeta, y)$. By generic value injectivity and hypotheses 1 and 5, the values of $g_0$ and, if $j < m$, of $\eta$ at this point are not zero. **Data.** A lemma on section data then gives the three conditions for $Q(y)$. The tie condition uses a depth formula, from the span of the $w_k$ and the integrality of section ratios; the lift condition uses a lift model built from the local rings. Choose these data at every $\lambda$. $\square$

### Archimedean data

Fix $T$ and $j$ in range with $j < m$, size data $L_2$, kernel hypotheses $H$, constants $C_2$, $A_2$ and $C_T$, weights $\kappa$, $w_L$ and $w_F$, and integers $T_n$, $n_P$ and $n_W$. The conditions on parameters, on pages, on the hypotheses with constants $(7, 0)$, the generic condition on $G$ and the eta condition are not unfolded here. *Archimedean data* for $(G, w_F, T_n, c_1)$ give, at each component $k$ of the uniformization at the base embedding $\sigma_0$, an archimedean input on the domain of $k$. Its forms are the restrictions of the $w_i$ to $k$, with the weights of $w_L$ and $w_F$, order $T_n$ and constant $c_1$; its other conditions are not unfolded here.

**Lemma 5.22.5 (Squares under an exponential bound).** Let $a > 0$, $b \ge 0$ and $i, p, q$ be real with $ab \le e^{-i(p - q)}$. Then $b^2 \le e^{2iq}\, a^{-2}\, e^{-2ip}$.

*Proof.* Both sides of $ab \le e^{-i(p-q)}$ are at least $0$, so $a^2 b^2 \le e^{-2i(p-q)} = e^{2iq} e^{-2ip}$. Divide by $a^2 > 0$. $\square$

**Theorem 5.22.6 (Archimedean data).** Assume the conditions on parameters, pages and hypotheses, $j < m$, and the generic condition and the eta condition for $G$. Then archimedean data exist for $(G, w_F, T_n, c_1)$, where $c_1$ is fixed by $T_n$ and the constant of the generic condition.

Lean: `GlobalTheory.RunJoin.archAt_of_run`

*Proof.* **Tie.** The page condition gives a tie with the tuple $(1, 2, 1, 2, 1, 2, 1, 4, 7)$ and the constants $(1, 4, 0, 11)$. **Forms.** The hypotheses give weights $w_1$ and $w_2$ with forms $\theta_1$ and $\theta_2$. A theorem gives a cusp form that is not zero on any component, and shows that a form that is not zero on a component is not zero at $\sigma_0$ there. **Rate.** The rate $\theta(w_L)$ is built from the degree of the host, the rank $r$ and the type primes, all positive, so $\theta(w_L) > 0$ because $r \ge 8$. **Main step.** A theorem on archimedean inputs gives the data from these facts and two bounds at every point $x$ of every domain. The first is a lower bound of exponential form, with rate $\theta(w_L)$, for the sum of the squares of the forms of $G$ at $x$, from the generic condition. The second bounds the square of the eta term; it follows from the archimedean bound of the eta condition and the lemma above. $\square$

**Remark 5.22.7 (Formalization).** Several facts about the Lean code:
1. `exists_completion_of_core_satisfying_laws` (UnitaryExistence/ExistsCompletionOfCoreSatisfyingLaws.lean:29) is one term that fills the structure `LawsP` (Formalism/LocalToGlobal/ProjectiveLattices/HasDataCondition.lean:32) over `Top` (line 20). The fields `kPsi`, `thCusp` and `thNe` copy hypotheses. The theta hypothesis is stated for every `StarRing` structure on $\mathcal{O}_E$, though the proof uses it only at the structure from `exists_isNab_uncond` (FormalGroupCharts/ExistsIsNabUncond.lean:19).
2. `GlobalTheory.T.exists_realisationPrimeData_curve_lifting` is a second name, proved by `first | exact @… | …` under `maxHeartbeats 1000000` (GenericRegularity/ExistsRealisationPrimeDataCurveLiftingStatement.lean:10). The file of `exists_real_primeData` (line 52) sets `maxHeartbeats 4000000` for the whole file (ExistsRealisationPrimeDataCurveLifting.lean:19).
3. A near copy, `GlobalTheory.PrimeData.exists_primeData` (GenericRegularity/FiniteDimensionalOfModel.lean:119), has the same hypotheses and the same steps, but gives local point data with no explicit points. Both proofs compute that every local ring is a discrete valuation ring and do not use it (ExistsRealisationPrimeDataCurveLifting.lean:66, FiniteDimensionalOfModel.lean:128).
4. The lift condition `LocalPointData.InLiftC` is an implication (Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/WeightedPrimeSumBound.lean:101): `TiedW`, then `InCurve`, then `InTie`, give `InLift`. So $G_c$ and $P_{rw}$ enter only through the premise `TiedW` (line 57). `InCurve` and `InTie` are at PublishedIntClosHolds.lean:347 and :350; `SecPt`, `FromW` and `secQ` are at Formalism/LocalToGlobal/ProjectiveLattices/NormalizedValuationMul.lean:13, :33 and :48.
5. In `archAt_of_run` the condition on parameters `ParOK` is introduced as `_` and not used (TorusHaarMeasure/ThetaArchimedeanDataIndefiniteModels.lean:58), so the extra data and the prime $p$ do not enter. The tie tuple is fixed at line 60, and the theorem runs under `maxHeartbeats 4000000` (line 54). Its second name `GlobalTheory.T.thetaArchimedeanData_indefiniteModels` (ThetaArchimedeanDataIndefiniteModelsStatement.lean:22) is not in the outline. The data are `GlobalTheory.Shares.ArchAt` (Definitions/ThetaValues/Generic.lean:132); the main step `GlobalTheory.ArchInputs.archAt_nonempty` (CuspFormEvaluations/ValAtAlgebraMap.lean:278) is not unfolded here.

## Notes and references

This chapter proves [the service row from Artin reciprocity](/entry/serv-h-row-of-artin/), which gives [the service row of the unitary hypotheses](/entry/serv-h-row-link-r-alt/) in Volume 15 and, through it, the step [the unitary hypotheses](/step/hyps-alt-def/) of [the written proof](/proof/unitary-hypotheses/). In Volume 15 it also supplies [the bundles with large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/), [the closed joint conditions](/entry/fam-joint-bcd-closed-alt/), [the arithmetic row at built points](/entry/row-a-at-g-at-built-alt/), [the local splitting of real lifts](/entry/at-real-lift-splits-locally/), [the representation of local data](/entry/rep-of-local-h-alt/), [the prime data for the heights](/entry/exists-prime-data-heights/), [the top datum of a core](/entry/exists-top-of-core/) and [the surjectivity from the hypotheses](/entry/onto-x-of-hypotheses-alt-alt/). In Volume 14 it supplies [the CM good model from global Artin reciprocity](/entry/cm-good-model-of-global-artin-reciprocity/) and [the layer theorem on $C$-entries](/entry/gy-lay-ker-t-ent-c/), and in Volume 8 [the Hecke sums](/entry/exists-sum/). Inside the chapter, [inert theta admissibility](/entry/inert-theta-admissibility-of-complex-multiplication/) of Section 13 and the good models of Section 14 feed the service row of Section 6.

Sources for the classical inputs:

- J. H. Silverman, *The Arithmetic of Elliptic Curves*, Chapter IV, and Chapter VII, §3 and §7. Formal groups and good reduction (Sections 14 and 15).
- J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Chapter II, §4, §6 and §8. Complex multiplication and the integrality of $j$ (Sections 10, 14 and 15).
- J. Neukirch, *Algebraic Number Theory*, Chapter VI, and Chapter VII, §13. Class field theory and the Chebotarev density theorem (Section 14).
- J. Lubin and J. Tate, "Formal complex multiplication in local fields", Ann. of Math. 81 (1965), 380 to 387 (Section 15).
- T. Honda, "On the theory of commutative formal groups", J. Math. Soc. Japan 22 (1970), 213 to 246 (Section 15).
- D. Mumford, *Abelian Varieties*, Chapter III, §12. Quotients by finite group schemes (Section 19).
- A. Weil, "Sur certains groupes d'opérateurs unitaires", Acta Math. 111 (1964), 143 to 211 (Section 21).
- A. Weil, "Sur la formule de Siegel dans la théorie des groupes classiques", Acta Math. 113 (1965), 1 to 87 (Section 21).
- R. Howe, "θ-series and invariant theory", Proc. Sympos. Pure Math. 33, Part 1 (1979), 275 to 285 (Section 20).
- D. Flath, "Decomposition of representations into tensor products", Proc. Sympos. Pure Math. 33, Part 1 (1979), 179 to 183 (Section 21).
- S. Rallis, "Langlands' functoriality and the Weil representation", Amer. J. Math. 104 (1982), 469 to 515 (Section 21).
- S. Rallis, "On the Howe duality conjecture", Compositio Math. 51 (1984), 333 to 399 (Section 21).
- S. Kudla and S. Rallis, "A regularized Siegel-Weil formula: the first term identity", Ann. of Math. 140 (1994), 1 to 80 (Section 21).
- A. Ichino, "A regularized Siegel-Weil formula for unitary groups", Math. Z. 247 (2004), 241 to 277 (Section 21).
- B. H. Gross, "Algebraic modular forms", Israel J. Math. 113 (1999), 61 to 93 (Section 21).
- Harish-Chandra, *Automorphic Forms on Semisimple Lie Groups*, Lecture Notes in Math. 62, Chapter I, Theorem 1. Finiteness of automorphic forms (Section 20).
- C. Moeglin and J.-L. Waldspurger, *Spectral Decomposition and Eisenstein Series*, Chapter I. Rapid decay of cusp forms (Section 20).
