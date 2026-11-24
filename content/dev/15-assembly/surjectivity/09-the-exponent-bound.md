---
title: The exponent bound
decls:
  - GlobalTheory.ExpTie.Asm.expSt_of_alt
  - GlobalTheory.T.expSt_of_num_sumExp_model
  - GlobalTheory.BigOn.exponent_bound_of_unitaryThetaStandardTheorems_alt
  - GlobalTheory.T.expSt_of_base_change_and_crystalline_lattices
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The exponent bound

This section proves the exponent statement: at the recorded objects of the rich points of a family, the exponents $J_0$ at the twisted places are bounded, place by place, by weights $J_p(j, \ell)$ whose sums against $\log \ell$ are at most an explicit constant. The proof has a combinatorial part, a bound for the exponent of a block in terms of the exponents of its two halves, and an arithmetic part, the model statement of Section 8. All the published inputs of Sections 7 and 8 enter here, and only through the model statement. The surjectivity statement of [Section 5.10.7](/entry/onto-x-of-hypotheses-alt-alt/) uses the result. The background is in [the Galois representation of an automorphic representation](/learn/galois-representations/#the-galois-representation-of-an-automorphic-representation).

We start with the combinatorial part. For $N \in \mathbb{N}$, a sequence $\lambda \colon \mathbb{N} \to \mathbb{N}$ and a prime $\ell$ there is an exponent $e_\ell(N, \lambda) \in \mathbb{N}$, the exponent of $\ell$ in the Weyl lattice of rank $N$ with the residues of $\lambda$. Write $\mathrm{UN}(N, \lambda, a)$ for the shifted values of $\lambda$ that enter the Hodge-Tate jumps of Section 7.

**Lemma 5.9.1 (Cutting a block).** Let $N \in \mathbb{N}$ and $\lambda \colon \mathbb{N} \to \mathbb{N}$ with antitone residues, let $\ell$ be a prime, and let $\mathrm{lo} \in \mathbb{Z}$ and $h \in \mathbb{N}$ with $\mathrm{lo} \le \mathrm{UN}(N, \lambda, a) \le \mathrm{lo} + h$ for each $a < N$. Then for each $a \le N$

$$\begin{aligned} e_\ell(N, \lambda) &\le e_\ell(a, \lambda) + e_\ell\big(N - a, \lambda(a + \cdot)\big) \\ &\quad + a (N - a) \lfloor \log_\ell h \rfloor. \end{aligned}$$

Lean: `GlobalTheory.T.weylLattice_exact_exponent_block_cut` (also `GlobalTheory.LeviCut.exCut`, a second name).

The lemma is proved in [its own entry](/entry/ex-cut/); it is a statement on the Weyl modules of $\mathrm{GL}_N$ in characteristic $\ell$ of the kind treated by Jantzen (*Representations of Algebraic Groups*, Part II, Chapter 2), and it holds with no hypothesis.

**Definition 5.9.2 (Numerical statement).** The *numerical statement* is the closed property: eventually at the points of $\mathcal{F}$, for each rich point $p$ and each level $j$, there are parameters $P$ and weights $W$ that match the size data at $j$ and pass the numerical checks.

Lean: `GlobalTheory.ExpTie.NumStAlt`.

**Definition 5.9.3 (Sum statement).** The *sum statement* is the closed property: eventually at the points of $\mathcal{F}$, for each rich point $p$, each level $j$, each $(P, W)$ that matches and passes the checks, each type $t$ and each place $w$, the inclusion of Section 8 holds at $w$ at the level $J_A(P, \ell)$ of the weights, where $\ell$ is the residue characteristic of $w$.

Lean: `GlobalTheory.ExpTie.ExponentSumStatement`.

Both statements hold with no input. For the numerical statement the parameters are those of the size data, and the weights come from the forced weights of the point. The sum statement is a statement on the lattices of a block at the level of the weights, and it is proved in the development.

**Theorem 5.9.4 (Smallness).** The smallness condition holds.

Lean: `GlobalTheory.T.small_estimate` (also `GlobalTheory.ExpTie.smallSt_alt`).

*Proof.* The condition holds at every point, so the closed property holds with any thresholds. Let $p$ be a regular rich point, $(P, W)$ a pair that matches and passes the checks, and $w$ a twisted place with $W$ in range at $\ell$. The residue characteristic $\ell$ of $w$ is prime. The range condition at $\ell$ gives $N_r + 1 < \ell$ by the bound on the parameters, and it gives $\ell \nmid \operatorname{disc} E$ by the special condition of the dictionary. The primitive links of $p$ give the complex data conditions at the base level; these make the block subspace stable under the block operators and put it in their space, at each level. $\square$

So, by Section 5, the frame statement holds too, with no input.

Next the target. Let $p$ be a point with the records of Section 2, and let $O$ be a recorded object at $p$. The number record of $p$ at the constants $C$ and $C_H$ gives exponents $J_0(t, w, j)$ for a type $t$, a twisted place $w$ and a level $j$. Write $\mu(w)$ for the type of $w$ and $\ell_w$ for its residue characteristic. Let $T_2$, $m$, $b$ and $x_e$ be the parameters of the point, and put

$$E_J = 30\, T_2\, m\, b\, x_e^2 + 2 m b.$$

**Definition 5.9.5 (Exponent bound).** The number record $N$ of $p$ and the object $O$ have the *exponent bound* if:

1. $J_0(\mu(w), w, j) \ge 0$ for each twisted place $w$ and each level $j$;
2. there are weights $J_p(j, \ell) \ge 0$, for each level $j$ and each $\ell \in \mathbb{N}$, with $J_0(\mu(w), w, j) \le J_p(j, \ell_w)$ for each twisted place $w$ and each level $j$;
3. for each $j$ and each finite set $Q$ of primes,

$$\sum_{\ell \in Q} J_p(j, \ell) \log \ell \le E_J.$$

Lean: `GlobalTheory.BigOn.HasExpBound`.

Conditions 2 and 3 are the two leaf conditions on $J_p$ in the record object. See also [the exponent bound at an object](/entry/has-exp-bound-at/).

**Definition 5.9.6 (Exponent statement).** The *exponent statement* is the statement for all record objects of Section 2 with the property: for all reals $C$ and $C_H$, the number record of $p$ at $(C, C_H)$ and $O$ have the exponent bound.

Lean: `GlobalTheory.BigOn.ExponentStatement`.

**Theorem 5.9.7 (Exponent bound from the model statement).** The lemma on cutting a block, the numerical statement, the sum statement and the model statement imply the exponent statement.

Lean: `GlobalTheory.ExpTie.Asm.expSt_of_alt` (also `GlobalTheory.T.expSt_of_num_sumExp_model`, a second name).

*Proof.* Join the three closed statements, and take the largest of their three height thresholds. For the bad constant records take the threshold $c_0 = 0$. Let $p$ be a rich point beyond the thresholds, $r$ a pair of runs and $O$ a recorded object at $p$. For each level $j$ the numerical statement gives a pair $(P_j, W_j)$. The record of $O$ gives four equalities: the size $m$, the height $x$ and the parameter $\varepsilon$ of the object are those of the point, and the realized chain has the torus of the point. Now the exponent bound at an object gives the exponent bound for each $C$ and $C_H$ from the lemma on cutting a block, the inclusion of the sum statement at each $(j, t, w)$, and the model condition at each twisted place $w$ in range. $\square$

The exponent bound at an object does the local work. At a twisted place $w$ in range, the model condition gives Hida settings that cover the block. Each setting gives an inclusion at some level $J$, and the cover gives the inclusion of the block at that level, which bounds $J_0$ at $w$. The weights $J_p(j, \ell)$ are the largest such levels at $\ell$, and they vanish at the primes not in range. The lemma on cutting a block, with the sum statement, bounds them by the exponent of the Weyl lattice of the weights at $\ell$, and these exponents have a sum against $\log \ell$ of at most $E_J$.

**Theorem 5.9.8 (The exponent statement).** Assume that regular algebraic cusp forms are cohomological, the two theorems on $\ell$-adic characters of Hecke characters, Chebotarev in degree one, the theorem on Galois representations of polarized cusp forms, base change for definite unitary groups, the theorem on crystalline lattices and the local Langlands correspondence. Then the exponent statement holds.

Lean: `GlobalTheory.BigOn.exponent_bound_of_unitaryThetaStandardTheorems_alt` (also `GlobalTheory.T.expSt_of_base_change_and_crystalline_lattices`, a second name).

*Proof.* Apply the theorem above. The lemma on cutting a block, the numerical statement and the sum statement hold with no input. For the model statement apply the theorem of Section 8 with Chebotarev in degree one, the theorem on crystalline lattices, the smallness condition above, the frame statement of Section 5 and the Galois statement of Section 7; the last uses all eight inputs and the smallness condition. $\square$

**Remark 5.9.9 (Formalization).** The theorem from the model statement is in [ExpStOf.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExpStOf.lean#L20). It takes the threshold $c_0 = 0$ and does not use the conditions on the bad constant records (line 27): the bound holds for each constant record. The file has an empty section `Point` that only declares variables. The proof is the same, line for line, as a theorem in [ExpansionOfNumericsModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExpansionOfNumericsModel.lean#L80), which uses the older wrapper for statements at points. The main theorem and its second name are in [ExponentBoundOfUnitaryThetaStandardTheorems.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExponentBoundOfUnitaryThetaStandardTheorems.lean#L20), at lines 20 and 38; the second is a one-line call with `maxHeartbeats` set to 1000000. Its proof is one term (lines 31 to 33), and in it only the model statement depends on the eight hypotheses. The name "unitary theta standard theorems" does not describe the statement: no input and no part of the conclusion is about a theta correspondence. The smallness theorem is in [SmallStAltAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SmallStAltAlt.lean#L12), and its second name `small_estimate` does not estimate anything. The cut lemma is stated in [StatementE.lean](lean:Formalism/PieriBlockIdeals/StatementE.lean#L25). The exponent bound is in [RealisedChainTorusEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RealisedChainTorusEq.lean#L82), and the statement in [ExportSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportSt.lean#L43). We have not unfolded the exponent $e_\ell$, the values $\mathrm{UN}$, the inclusion of the sum statement or the leaf conditions on $J_p$; the paragraph on the local work is our reading of the names in the exponent bound at an object, and the value of $E_J$ is taken from its entry.
