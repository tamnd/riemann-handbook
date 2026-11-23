---
title: Hecke closure and word conditions
decls:
  - GlobalTheory.Hk3.HeckeClose.heckeClose
  - GlobalTheory.HTW.RecS.fam_jointBCD
  - GlobalTheory.HTW.RecS.fam_joints
  - GlobalTheory.T.wordConditions_common_natural_representation
  - GlobalTheory.HTW.Rec.recS_wordBase_natural
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke closure and word conditions

This section proves two groups of results that the assembly of Volume 15 takes from this chapter. The first is the Hecke closure of a family of [[theta|6WB6TKE70H]] lifts of level 3: its Hecke operators are rational and have adjoints, they intertwine the rows with the lifts, and the inert eigenvalues separate the types. It is used in [the large unramified exponents of member bundles](/entry/member-bundles-large-unramified-exponents-alt/). The second gives words with prescribed local properties at the inert places of the members of a family, at large scale. It is used in [the closed form of the joint hub conditions](/entry/fam-joint-bcd-closed-alt/).

### Three standard inputs

The Hecke closure takes three known theorems as hypotheses. We state them in their usual form.

**Theorem 5.20.1 (Howe, unramified lemma).** Let $F$ be a nonarchimedean local field of characteristic zero, and let $(G, G')$ be an unramified dual pair of unitary groups over $F$, with hyperspecial subgroups $K$ and $K'$. Let $\omega$ be the Weil representation of $G \times G'$ in a model where the standard vector $\varphi_0$ is fixed by $K \times K'$. Then every vector fixed by $K$ lies in the span of $\omega(G')\varphi_0$, and every vector fixed by $K'$ lies in the span of $\omega(G)\varphi_0$.

Lean: `GlobalTheory.Hk3.HoweUnram`

This is a lemma of the unramified theta correspondence, not full Howe duality; see Howe (1979) and Rallis (1982). In the Lean form, $F$ is a complete field of characteristic zero with a discrete valuation, the dual pair and the Weil module are a local pair datum, and $\varphi_0$ is a nonzero vector $s$ with a vacuum condition whose translates span the module.

**Theorem 5.20.2 (Harish-Chandra finiteness).** Let $G$ be a reductive group over a number field, $U$ an open compact subgroup of $G(\mathbb{A}_f)$, $\rho$ a finite-dimensional representation of a maximal compact subgroup $K_\infty$ of $G(\mathbb{R})$, and $J$ an ideal of finite codimension in the center of the enveloping algebra. Then the automorphic forms that are fixed by $U$, of $K_\infty$-type $\rho$ and killed by $J$ form a finite-dimensional space.

Lean: `GlobalTheory.Published.HarishChandraFinite`

In the Lean form, $G$ is the unitary group of a Hermitian space $V$ over the host, $\rho$ is a family of continuous finite-dimensional representations, one for each embedding $\tau$, and the condition on $J$ is a list of eigenvalues $c$. The space of such forms is not unfolded here.

**Theorem 5.20.3 (Rapid decay of cusp forms).** Let $\varphi$ be a smooth cusp form on $G(\mathbb{Q}) \backslash G(\mathbb{A})$ of uniform moderate growth. Then for every $N$ there is $C$ with $|\varphi(g)|\, \lVert g \rVert^N \le C$ for all $g$, where $\lVert g \rVert$ is the height on the quotient.

Lean: `GlobalTheory.Published.CuspRapidDecay`

### Hecke closure of a family of level 3

Let $D$ be a datum with field of periods $\mathrm{LL}$, $G$ a finite group, and $A_3$ a family of level 3 over $\mathrm{LL}$ with group $G$. It has rows indexed by $t$ and lifts indexed by $(j, t)$, each with a space of forms, a pairing and Hecke operators $T_k$. Let $R$ be real data over a number field $K_s$ and $F$ a face of $A_3$.

**Definition 5.20.4 (Hecke closed).** A row or a lift is *Hecke closed* if each matrix of an operator $T_k$ in the standard basis has entries in the subfield of elements $a$ with $\sigma(a^*) = \overline{\sigma(a)}$ for every complex embedding $\sigma$, and for each $k$ there is $k'$ with $\langle T_k f, g \rangle = \langle f, T_{k'} g \rangle$ for all forms $f$ and $g$. A row or a lift is *inert closed* if the same holds for its inert operators.

A *passage* $\mathrm{tr}$ sends each lift index $j$ and each system of eigenvalues $p$ at the rows to a system of eigenvalues at the lifts. It is *faithful* if, whenever a good form at the lift $j$ is an eigenform with eigenvalues $s$ and its theta image is a nonzero vector in the class $c$ carried by $p$, then $s$ agrees with $\mathrm{tr}(j, p)$ at the inert indices. It *separates* if any two indices $p \ne p'$ of the finite set at $\mu_0$ that differ at an inert index have images $\mathrm{tr}(j, p)$ and $\mathrm{tr}(j, p')$ that differ at an inert index, for every $j$. The *types are separated* if any two distinct indices of this set give different types at every lift $j$.

**Theorem 5.20.5 (Hecke closure).** Assume the unramified lemma of Howe, Harish-Chandra finiteness and the rapid decay of cusp forms. Let $s$ be such that $A_3$ is in order at $s$. Assume:
1. the weak characterisation of $R$ at $F$, the existence condition of $R$ and the inert junk condition of $A_3$;
2. for each $k \in \{0, 1\}$, the series idempotents of type $k$ of $D$ are those of a label map at the type prime $g_k$;
3. if some passage is faithful and separates, then the passage of $A_3$ is faithful and the family separates;
4. the uniformity, unitarity, equivalence and level conditions of $R$ at $F$, and its two theorem conditions;
5. the constant $\kappa$ of $R$ and all the constants $\lambda_3$ are positive;
6. the parts condition of $R$ at $F$ with value false.

Then every row and every lift is Hecke closed and inert closed, the Hecke operators intertwine the rows with the lifts, the types are separated, and there is a passage that is faithful and separates.

Lean: `GlobalTheory.Hk3.HeckeClose.heckeClose`

The conditions in 1 to 6 are not unfolded here.

*Proof.* **Integrals.** Rapid decay gives that the integrals that define the lifts converge, and that the Schur constants of $R$ exist. The characters of $A_3$ are absolutely irreducible, since $A_3$ is in order at $s$.

**The passage.** A lemma on inert eigenvalues uses the lemma of Howe, the convergence, the Schur constants, the irreducible characters, hypothesis 1, the second theorem condition and the positivity. It gives a passage $\mathrm{tr}$ that is faithful and separates.

**Types.** A lemma on finite sets of types uses rapid decay, the lemma of Howe, the convergence, the order at $s$, hypotheses 1 and 3, the positivity and the second theorem condition. It gives that the types are separated.

**Intertwining.** The series idempotents of hypothesis 2 show that the generic character of $A_3$ is good at the level of the face. A lemma on Hecke operators on the rows uses the three standard inputs and gives the intertwining on the definite side. A lemma on Hecke theta lifts of level 3 uses the same inputs, the good generic character, hypotheses 4 to 6, the separated types and hypothesis 3, and it gives the intertwining on the lifts.

**Closure.** A lemma on the weak characterisation with the inert junk condition gives that every row and every lift is Hecke closed and inert closed. $\square$

### Words at inert places

Let $D$ be a datum of type 7, $L$ size data for $D$ and $\mathrm{HW}$ a choice of Wach data for the local data of $D$. Fix a place index $i$ with prime $l_i$, families $r$ and $\rho$ of representations of the Galois group with values in $\mathrm{GL}$ over the local integers, and a point $\pi$. Let $w$ be a place of the host over $l_i$ with local field $K_w$, let $C_x$ be a coefficient extension with field $\mathrm{LL}$, and assume that $(K_w, \mathrm{LL})$ is good. Let $n$ be the degree over $\mathbb{Q}_{l_i}$ of the maximal unramified subfield of $K_w$. A *word* $W$ of length $n$ has a window $W_{\mathrm{win}}(a)$ for each letter $a$ and integers $b$, $w'$, $S$, $\eta$ and $m$; its other data are not unfolded here.

**Definition 5.20.6 (Point inputs).** The point inputs hold for $(r, \rho, \pi)$ if $r$ is good and continuous as a family, $\pi$ lies in the set $Z_i$, the decomposition of $(r, \rho)$ at $\pi$ is semisimple, $\rho$ is continuous at $\pi$, and every twist of $r$ is crystalline at every coefficient extension of every place over $l_i$.

**Definition 5.20.7 (Word base).** A word $W$ is a *word base* for $(r, \rho, \pi, w, C_x)$ if:
1. $K_w$ lies in the maximal unramified extension of $\mathbb{Q}_{l_i}$, and the degree condition holds;
2. $\mathrm{LL}$ splits $K_w$;
3. every lattice $T_1$ in a sum of twisted duals of $r$ is crystalline, has its Hodge-Tate jumps at each letter $a$ in the window $W_{\mathrm{win}}(a)$, and has the lifting jumps of $W$;
4. every lattice $T_2$ of the twisted dual of $\rho$ at $\pi$ is crystalline, has at most $m$ small jumps at $\eta$ for each letter, and has its jumps as in 3;
5. $W$ satisfies the number condition of $L$, it is small, and $1 \le S$ and $1 \le \eta$.

**Definition 5.20.8 (Joint conditions).** Let $C_2$ be a real number. The *joint condition B* with constant $C_2$ holds for $(L, \mathrm{HW})$ if at every $i$ such that $l_i$ is inert and unramified and lies in the row range of $L$, at every $(r, \rho, \pi)$ with point inputs and every $w$ over $l_i$: $K_w$ is unramified, and for every $C_x$ there is a word base $W$ that satisfies the thick letter surjection hypotheses, with $11 \le l_i$, $j_A + 1 \le n$,
$$
C_2\, (j_A + 1)\, (w' + S + \eta + 1) \le b,
$$
and with clusters of thick letters, where $j_A$ is an integer of $L$ at $l_i$. The *joint condition CD* asks the same at every inert unramified $l_i$, without the row range, with a word base $W$ that satisfies the thick letter surjection hypotheses, $11 \le l_i$ and a box condition, and that is either of type NT or alternating with its alternating hypotheses.

**Theorem 5.20.9 (Word base at a natural point).** Let $L$ be roomy for a constant $C_0$. Assume the admissibility of type 7 of $D$, the Fontaine condition at all places over each $l_i$, the conclusion J of $D$ and the point inputs for $(r, \rho, \pi)$. Let $l_i$ not be a small prime of the host and be different from the primes $q$ and $d$ of the host. Then there are a sign $\varepsilon = \pm 1$ and a map $g$ from $\mathbb{Z}/n$ to the group of $D$ that is an orbit of the inverse Frobenius at $l_i$, such that the recurrence word of $(L, \varepsilon, g)$ is a word base.

Lean: `GlobalTheory.HTW.Rec.recS_wordBase_natural` (also `GlobalTheory.T.wordConditions_common_natural_representation`, a second name)

*Proof.* A lemma on Hodge-Tate jumps over coefficient extensions gives $\varepsilon$, a second integer datum $\kappa$ and the position of the jumps. A lemma on word conditions at a place, applied to the Frobenius orbit, gives $g$ with the orbit property, the degree condition, the local conditions and the number condition. A lemma on recurrence words gives that the word is small, with $1 \le S$ and $1 \le \eta$. The local conditions give conditions 1 to 4; for condition 4 the two counts of small jumps are equal by definition. $\square$

A *family* $F_m$ with parameter $\varepsilon_F$ gives, for each $x > x_1$, a nonempty index set $I_x$, and for $j \in I_x$ a datum $D(x, j)$, size data $L(x, j)$ at scale $x$ with fixed constants $\varepsilon_F$ and $e_z$, and a choice of parameters whose list of constants does not depend on $(x, j)$. Its other data are not unfolded here.

**Theorem 5.20.10 (Joint conditions along a family).** Let $F_m$ be a family and $C_2$ a real number. Assume the admissibility of type 7 and the Fontaine condition for all data. Then there is $x_0$ such that for all $x \ge x_0$ with $x > x_1$, all $j \in I_x$ and all $\mathrm{HW}$: if the conclusion J holds for $D(x, j)$, then the joint condition B with constant $C_2$ and the joint condition CD hold for $L(x, j)$.

Lean: `GlobalTheory.HTW.RecS.fam_joints`

*Proof.* The constants $\varepsilon_F$ and $e_z$ are positive, since they are the constants of a member at an index of $I_0$. Let $A$ be the eighth constant of the list of parameters, so that the constant $C_{Lw}$ of every member is at most $A$. A lemma on long orbits at large scale gives $x_B$ such that the joint condition B with constant $C_2$ holds for all size data at scale at least $x_B$ with these constants. A lemma on inert primes at large scale gives $x_C$ for the joint condition CD in the same way. Take $x_0 = \max(x_B, x_C)$. The scale of $L(x, j)$ is $x$, so both lemmas apply. $\square$

**Corollary 5.20.11 (Hub conditions along a family).** Let $F_m$ be a family and $R$ row constants with first constant $C_2$. Assume the admissibility of type 7 and the Fontaine condition for all data. Then there is $x_0$ with this property. Let $x \ge x_0$ with $x > x_1$, let $j \in I_x$, and let $X$ be hub data for $D(x, j)$. Assume the conclusion J for $D(x, j)$, and the point inputs for $(X_r, X_\rho, \pi)$ at every twisted place $i$ with $l_i$ inert and every good $\pi$. Then at every such $i$ and $\pi$, the local bound condition with constant $C_2$ holds if $l_i$ is in the row range of $L(x, j)$, and the local congruence condition holds if not.

Lean: `GlobalTheory.HTW.RecS.fam_jointBCD`

*Proof.* Take $x_0$ from the previous theorem with the constant $C_2$. An inert prime at a twisted place is inert and unramified. The bound condition takes from the joint condition B the word, its word base and the three numerical facts, after a lemma that identifies two orders of $l_i$. The congruence condition takes from the joint condition CD the word, its word base, the box condition and the alternative. $\square$

**Remark 5.20.12 (Formalization).** Several facts about the Lean code:
1. `GlobalTheory.T.wordConditions_common_natural_representation` is a second name, proved by `first | exact @… | …` under `maxHeartbeats 1000000` (WordConditionsCommonNaturalRepresentationStatement.lean:14). The three standard inputs are definitions of propositions (PublishedTheorems/GaloisGeometry₂/HoweUnram.lean:8, PublishedTheorems/AutomorphicForms₂/HarishChandraFinite.lean:50, PublishedTheorems/AutomorphicForms₂/ExistsNormLeHeightPow.lean:28). The project proves them as `GlobalTheory.Hk3.howeUnram_holds` (Proofs/SatakeParameters/RhoMemOfMkEq.lean:250), `PositivityTheory.RgHf.harishChandraFinite` (FiniteOfCuspOfConstTerm.lean:129) and `GlobalTheory.RapidDecay.cuspRapidDecay` (CuspFormsRapidDecay.lean:10), but `heckeClose` keeps them as hypotheses.
2. Hecke closed is `OkH` (Formalism/LocalToGlobal/Divisibility/LiftLat.lean:132) and inert closed is `InertRationalAdjoint` (InertRationalAdjoint.lean:63); the two structures have the same two fields `rat` and `adj`. Faithful is `TrISem` (ZeroPartEigenvalueConvention.lean:236) and separated types is `TypesSep3` (InertRationalAdjoint.lean:154). The definition `TrISepWith` occurs twice with the same text, in `GlobalTheory.Hk3` (Definitions/GaloisGeometry/GoodGeneric.lean:27) and in `Formalism.IndefR` (Formalism/LocalToGlobal/IndefiniteReal/TrISepWith.lean:33).
3. In `fam_jointBCD` the row constants $R$ enter only through `R.C₂` (FamJointBCD.lean:20). The step from the joint conditions to the hub conditions is `frozenBCD_of`, a lemma in the folder Counterexamples/HeckeCharacterExamples (ClusteredLetterwiseBoxes.lean:205), with `frozenB_of` and `frozenCD_of` at lines 116 and 123.
4. In `fam_joints` the eighth constant is `Fm.PK.getD 7 0`, and the equality of `CLw` with it is `famJ_CLw_eq` (FamJEpsPos.lean:15). The positivity of $\varepsilon_F$ and $e_z$ uses the index set at $x = 0$ (lines 20 and 25). The two lemmas at large scale are `GlobalTheory.T.inertLongOrbitWordConditions_of_large_scale` and `GlobalTheory.T.inertPrimeWordConditions_of_large_scale`.
5. Word base, the point inputs and the joint conditions are `WordBase`, `PtIn`, `JointB` and `JointCD` (Definitions/GaloisGeometry/ThickLetterWordLatticeSurjectionHypotheses.lean:30, 56, 65 and 74). The two counts of small jumps are `lowCount` in two namespaces, and `lowCount_eq_smallHodgeTateJumpCountOverLetter` shows that they agree by unfolding (WordConditionsCommonNaturalRepresentation.lean:18).
