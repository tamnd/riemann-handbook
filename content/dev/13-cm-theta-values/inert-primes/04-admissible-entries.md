---
title: Admissible entries from the kernel law
decls:
  - Formalism.L2.KerInert.AdmLoc2.admissible_general_of_kernel_law
  - Formalism.L2.KerInert.AdmLoc2.admissible_place_of_kernel_law
  - Formalism.L2.KerInert.AdmLoc2.admissible_entries_of_kernel_law
  - Formalism.L2.KerInert.AdmLoc2.admissible_entries_small_chain
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Admissible entries from the kernel law

A pending tuple of a formal group system is *admitted* when it satisfies thirteen conditions. This section shows that the pending tuple built from the kernel family of Section 3 is admitted. First we prove this for a general system, given the theorem of Section 3 and a few hypotheses on the data. Then we specialize to the systems attached to a place of the global datum, where two of the hypotheses follow from ties between levels. The last result of the section is the statement that [the inert theta admissibility theorem](/entry/inert-theta-admissibility-of-complex-multiplication/) needs: under the theorem on good models, every entry at an inert place is admitted.

### The thirteen conditions

Let $X$ be a formal group system at $p$ and $Y$ a pending tuple, as in Section 3. The pending tuple is *admitted* if all of the following hold.
1. Dwork's lemma holds at every prime: for $p \ne 2$ and a series $P$ with no constant term, $\exp(P)$ is integral if and only if $P^\sigma(X^p) - pP = pQ$ with $Q$ integral over $W$.
2. (2), (2b), (3) as in Section 3: the local extension condition at each place, the extension generator condition for all lattice tuples and frames, and valuation at least $0$ after the differential operators.
3. (2c): the pairing series of $Y$ has the pairing property.
4. (3b): for $j < m$, the map $K_j$ of the system sends the space $F_Q(j)$ into $F_Q(j + 1)$.
5. The *expansion condition*: for $j + 1 < m$, $K_j F$ is a sum over the representatives of the kernels of $F$, weighted by the inverse sizes of the stabilizers times a unit; for $j + 1 = m$, a weighted decomposition of the same kind holds, with weights whose $p$-adic valuation is bounded.
6. (5): at each place $v$ and level $j < m$, the series $\Theta_F$ of a pair of lattice tuples equals $u^{\ell}u'^{\ell'}p^{-(n'_v/2)\,\mathrm{vol}}$ times a value of $\Xi$, for units $u, u'$.
7. *Invariance of kernels*: for $\gamma$ in the group of a level, $\ker_j(\gamma L, L_a')(\chi(\gamma)\,\gamma G) = \ker_j(L, L_a')(G)$.
8. (6): the up and down operators along edges are adjoint for the weights $1/|\mathrm{Stab}|$.
9. (7): frames carry series with coefficients of valuation at least $g$ into the lattice of level $j + 1$, up to an explicit power of $p$.
10. (8): a selection condition on the group datum.
11. (11): the condition on the lowest term at each place, as in Section 3.

Items 2 and 3 contain four conditions, so the list has thirteen in all. The pending tuple $Y$ depends on the kernel family $F$ of Section 3 and on all its data. We write $\mathcal{Y}$ for the pending tuple built from the kernel family.

**Definition 6.4.1 (Stabilizer law).** The kernel family satisfies the *stabilizer law* if for every $j < m$, every representative $(c, L_0)$ at level $j$, every lattice tuple $L_a'$ at level $j + 1$, and every $\varepsilon$ in the group of the level that fixes $L_0$,
$$\kappa(\varepsilon)^{-1}\cdot \gamma(\varepsilon)^*\Theta_R(j, (c, L_0), L_a') = \Theta_R(j, (c, L_0), L_a'),$$
where $\Theta_R$ is the series read from the family, $\gamma(\varepsilon)^*$ is the action of $\varepsilon$ on series, and $\kappa$ is the character of the level.

**Lemma 6.4.2 (Invariance from the stabilizer law).** If the kernel family satisfies the stabilizer law, then $\mathcal{Y}$ satisfies the invariance of kernels.

*Proof.* Extend $\Theta_R$ by $0$ outside the levels $j < m$ and the lattice tuples. The extended family satisfies the law of the character $\kappa$ for every element of every stabilizer. A general law for pending tuples says that a family with the law of the character on every stabilizer gives kernels with the invariance of the condition. On the levels $j < m$ and the lattice tuples, the kernels of the extended family and of $\Theta_R$ are equal. $\square$

### The general theorem

We call the following set of assumptions the *inert curve hypotheses*: $p \ge 5$; the data $(\mathfrak{c}, \delta, g)$ are at $(K, p)$; $p$ is inert; the curve is over $W$; $\mathfrak{c}$ is a curve ideal and $\delta$ a twelfth root for it; $\chi$ is as in Section 2; $\lambda$ is the ring map of $g$; and the lattice of $g$ is the lattice of the theta data. The *data hypotheses below the top level* are (A), (C), (X'), (S) and the existence of maps $\rho_v$ with (P), (M) and (F), as in Section 3. The *invariance of $\Xi$* says that for each place $v$ and $j < m$, the series $\Theta_F$ of $\mathcal{Y}$ at $v$ and $j$ have the invariance under additive maps of the system.

**Theorem 6.4.3 (Admissibility from the kernel law).** Assume that the theorem of Section 3 on translates of the inert kernel holds. Let the data of a kernel family be given, and assume the inert curve hypotheses, the data hypotheses below the top level, the invariance of $\Xi$, the stabilizer law, condition (3b) and the expansion condition. Then $\mathcal{Y}$ is admitted.

Lean: `Formalism.L2.KerInert.AdmLoc2.admissible_general_of_kernel_law`

*Proof.* We check the thirteen conditions one by one. Dwork's lemma is a theorem (see Koblitz, *p-adic Numbers, p-adic Analysis, and Zeta-Functions*, Chapter IV, §2). Conditions (2), (2b) and (3) are [the theorem on translates of the inert kernel](/entry/first-kernel-law-global-small/), applied with the inert curve hypotheses and the data hypotheses. Condition (2c) holds at an inert prime by the four facts of Section 1, as in [the laws of the pairing series](/entry/be-winert-of-a/). Condition (3b) and the expansion condition are assumed. Condition (5) is equivalent to the existence of additive maps for $\Xi$, which is the invariance of $\Xi$. The invariance of kernels is the lemma above. Condition (6) holds for every pending tuple. Condition (7) holds for every pending tuple by [the admissibility of pending tuples](/entry/pending-tuple-admissible/). Condition (8) holds for every system. Condition (11) holds at an inert prime for data over $W$. $\square$

### Systems at a place

The global datum gives, for each word $u$, each tuple $\mu$ and each place $w$ with residue characteristic a prime, a formal group system $X_w$ at that prime, with frame data built from level-zero data, an element $a$ and a finite set of bad places. For this system the top level equals the number $m$ of the global datum. A *tie at level $j$* is a compatibility between the pending tuple at the levels $j$ and $j + 1$ and the classes and components of the datum, given by maps $\iota$, $R_d$ and $S_r$. At the top level there are two further conditions on a section $l_p$: a *coupled tie* and a *Hecke condition*.

**Theorem 6.4.4 (Admissibility at a place).** Assume the theorem of Section 3. Let $w$ be a place and $X_w$ its system, with the data of a kernel family, and assume the inert curve hypotheses, the data hypotheses below the top level, the invariance of $\Xi$ and the stabilizer law. Assume that there are $\iota$, $R_d$ and $S_r$ with a tie at every level $j$ with $j + 1 < m$, and, if $m > 0$, a section $l_p$ with the coupled tie and the Hecke condition at level $m - 1$. Then $\mathcal{Y}$ is admitted.

Lean: `Formalism.L2.KerInert.AdmLoc2.admissible_place_of_kernel_law`

*Proof.* For the system at a place, condition (3b) follows from the components of the kernel datum: they are integral and rational, and they are compatible with the maps $K_j$. If $m > 0$, the ties below the top level, the coupled tie and the Hecke condition give the expansion condition: the expansion equality below the top and the decomposition at the top. If $m = 0$, both parts of the expansion condition are empty. Now apply [the general theorem](/entry/admissible-general-of-kernel-law/). $\square$

**Theorem 6.4.5 (Admissible entries).** Assume the theorem of Section 3. Let $w$, $X_w$ and the data be as in the last theorem, with the same hypotheses, except that we now assume only a tie at every level $j < m$, with no assumption at the top level. Then $\mathcal{Y}$ is admitted.

Lean: `Formalism.L2.KerInert.AdmLoc2.admissible_entries_of_kernel_law`

*Proof.* We must produce, when $m > 0$, the section $l_p$ and the two conditions at level $m - 1$. The stabilizer law gives the invariance of kernels by the lemma above. If $m > 0$, a coupled section $l_p$ exists. The tie at level $m - 1$ and the section give the coupled tie. The invariance of kernels, the section and the tie at $m - 1$ give the Hecke condition. Now apply [the theorem at a place](/entry/admissible-place-of-kernel-law/). $\square$

**Corollary 6.4.6 (Admissible entries at inert places).** Assume the theorem on good models of Section 2. Then the conclusion of the theorem on admissible entries holds with no assumption on the translates of the inert kernel.

Lean: `Formalism.L2.KerInert.AdmLoc2.admissible_entries_small_chain`

*Proof.* This is [the theorem on admissible entries](/entry/admissible-entries-of-kernel-law/) applied to [the theorem on translates of the inert kernel](/entry/first-kernel-law-global-small/), which holds under the theorem on good models. $\square$

**Remark 6.4.7 (Formalization).** The corollary sits under `variable [Fact CM2] in` ([AdmissibleEntriesOfKernelLaw.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/AdmissibleEntriesOfKernelLaw.lean#L105)); the parent theorem turns the instance into a hypothesis. The general theorem assumes (3b) and the expansion condition rather than proving them; at a place they come from the ties. The expansion condition is called `ArchimedeanSignatureMatching`, and it has no archimedean content. The invariance of kernels is called `MinkowskiCounting`, and it is not a count. Dwork's lemma is proved as `Pf.positivity_condition_holds`. The word "small chain" in the name of the corollary does not match the statement. The lemma `admissible_stabilizer_of_law` is computed twice, once in the general theorem and once in the theorem on entries (lines 72 and 95). The ties, the coupled tie and the Hecke condition are not unfolded here. The statement of the theorem on entries is defined twice, also in [ThetaSeriesDataHypothesesBelowMaximalLevel.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ThetaSeriesDataHypothesesBelowMaximalLevel.lean#L106).
