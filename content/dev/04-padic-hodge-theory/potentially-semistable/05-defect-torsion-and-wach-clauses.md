---
title: The defect of a short exact sequence and the clauses on Wach lattices
decls:
  - GlobalTheory.T.defect_torsion_second_cohomology_kernel
  - GlobalTheory.NL.DefectTorsion.defect_torsion
  - GlobalTheory.T.wachLattice_laterClauses_hold
  - GlobalTheory.NL.wach_used_clauses
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The defect of a short exact sequence and the clauses on Wach lattices

Let $0 \to T_0 \to T_1 \to T_2 \to 0$ be a short exact sequence of crystalline lattices. A bounded Herr cocycle of $T_2$ lifts to a bounded pair over $T_1$, but the lift need not be a cocycle. This section proves that the defect of the lift is a bounded element of $D(T_0)$, and that a power of $p$ times the defect is the differential of a bounded pair over $T_0$. The proof uses [Theorem 6.4.3](/entry/h1f-class-wach-pair-filtration-jumps/) of the previous section. The section then collects the seventeen clauses on Wach lattices that the later sections use. One clause is the defect theorem, and one is [Theorem 6.3.7](/entry/wach-module-descent-to-tame-subextension/). The Wach modules are those of [the Background](/learn/padic-hodge/#lattices-wach-breuil-kisin-and-prismatic-f-crystals).

Fix a good triple $(K, s, L)$ with a Wach datum, as in the previous sections, and write $N(T)$ for the Wach module of a lattice $T$, $N_i(T)$ for its part at the letter $i$, and $X_s = \varphi^{s-1}(\pi)$. Then $\varphi(X_s) = X_s Q$, and $X_s$ is a unit of $\mathcal{E}$. A map of lattices $f : T \to T'$ gives a map $f : D(T) \to D(T')$ that commutes with $\varphi$ and $\Gamma$.

**Definition 6.5.1 (Bounded elements).** Let $T$ be a lattice and $a \in A$. Put
$$N(T)[a^{-1}] = \{ y \in D(T) : a y \in N(T) \}, \qquad a N(T) = \{ a x : x \in N(T) \}.$$
For $M \in \mathbb{N}$, a pair $(y, z) \in D(T)^2$ is *$M$-bounded* if $y \in N(T)[Q^{-M}]$ and $z \in X_s N(T)$.

Lean: `Formalism.MainNotions.DeltaInvariantLattices.invN` (also `Formalism.MainNotions.DeltaInvariantLattices.aN`, the module $a N(T)$).

The differential of the Herr complex sends a pair $(y, z)$ to $d(y, z) = (\gamma - 1) y - (\varphi - 1) z$, so that $(y, z)$ is a Herr cocycle exactly when $d(y, z) = 0$.

**Lemma 6.5.2 (Bound on the differential).** Let $T$ be a lattice and $M \in \mathbb{N}$. Assume that $N(T)$ is stable under $\Gamma$, that $(\gamma_g - 1) N(T) \subseteq \pi N(T)$ for $g \in \Gamma$, that $(\gamma - 1) N(T) \subseteq X_s N(T)$, that $Q^M \varphi(N(T)) \subseteq N(T)$, and that $\gamma(Q) = w Q$ for some $w \in A$ with $w - 1 \in X_s A$. Then for every $M$-bounded pair $(y, z)$,
$$Q^M d(y, z) \in X_s N(T).$$

Lean: `GlobalTheory.NL.DefectTorsion.differential_one_mem_scaled_lattice`.

*Proof.* Since $w - 1$ is a multiple of $X_s$, the element $w$ is a unit $u$ of $A$, and $u^{-M} - 1 = X_s c$ for some $c \in A$. From $\gamma(Q^M y) = u^M Q^M \gamma(y)$ we get
$$Q^M (\gamma - 1) y = u^{-M} (\gamma - 1)(Q^M y) + X_s c \, Q^M y.$$
Both terms lie in $X_s N(T)$, because $Q^M y \in N(T)$. Write $z = X_s m$ with $m \in N(T)$. Then $Q^M \varphi(z) = X_s Q \cdot Q^M \varphi(m)$ and $Q^M z = X_s Q^M m$, and both lie in $X_s N(T)$. $\square$

**Theorem 6.5.3 (Defect torsion).** Assume a comparison datum is given. Let $(K, s, L)$ be good with its Wach datum, and let $\iota : T_0 \to T_1$ and $\pi : T_1 \to T_2$ form a short exact sequence of crystalline lattices. Let $M, h : \mathbb{Z}/n \to \mathbb{N}$ with $T_1$ having jumps in $[-M, h]$, and put $\bar M = \max_i M_i$. Let $(y_2, z_2)$ be an $\bar M$-bounded Herr cocycle of $T_2$, and let $(y_1, z_1)$ be any $\bar M$-bounded pair of $T_1$ with $\pi(y_1) = y_2$ and $\pi(z_1) = z_2$. Then there is $w \in D(T_0)$ such that:

1. $\iota(w) = d(y_1, z_1)$;
2. $w \in X_s \, N(T_0)[Q^{-\bar M}]$;
3. there are $k \in \mathbb{N}$ and an $\bar M$-bounded pair $(y_0, z_0)$ of $T_0$ with $p^k w = d(y_0, z_0)$.

Lean: `GlobalTheory.NL.DefectTorsion.defect_torsion` (also `GlobalTheory.T.defect_torsion_second_cohomology_kernel`, a second name).

In words, $w$ is the defect of the lift, and its class in the cokernel of $d$ on bounded pairs of $T_0$ is killed by $p^k$.

*Proof.* We use the following facts, which are proved elsewhere in this development.

- (a) The sequence $0 \to D(T_0) \to D(T_1) \to D(T_2) \to 0$ is exact at $D(T_0)$ and $D(T_1)$.
- (b) If $x \in D(T_0)$ and $\iota(x) \in N(T_1)$, then $x \in N(T_0)$.
- (c) $N(T_1)$ is stable under $\Gamma$ and $(\gamma - 1) N(T_1) \subseteq X_s N(T_1)$.
- (d) $Q^{M_i} \varphi(N_{i-1}(T_1)) \subseteq N(T_1)$ for each letter $i$. Since $N(T_1)$ is the sum of the $N_i(T_1)$ and $M_i \leq \bar M$, this gives $Q^{\bar M} \varphi(N(T_1)) \subseteq N(T_1)$.
- (e) For $T = T_1$ and $T = T_2$: $\gamma(Q) = w Q$ with $w - 1 \in X_s A$; the class of every $\bar M$-bounded Herr cocycle lies in $H^1_f(G_{K_s}, T)$; and an $\bar M$-bounded Herr cocycle with class $0$ equals $(\varphi m - m, \gamma m - m)$ for some $m \in N(T)$. For $T_2$ this uses that $T_2$ has jumps in $[-M, h]$, which holds because the jumps of $T_1$ are those of $T_0$ together with those of $T_2$.
- (f) There is $c'' \in \mathbb{N}$ with $p^{c''} N(T_2) \subseteq \pi(N(T_1))$.
- (g) For each $\kappa_2 \in H^1_f(G_{K_s}, T_2)$ there are $c$ and $\kappa_1 \in H^1_f(G_{K_s}, T_1)$ with $\pi_* \kappa_1 = p^c \kappa_2$.
- (h) [Theorem 6.4.3](/entry/h1f-class-wach-pair-filtration-jumps/) for $T_1$.
- (i) The class map is natural: $\mathrm{cl}(\pi y, \pi z) = \pi_* \mathrm{cl}(y, z)$.

*Step 1: a lift of a multiple.* We show that there are $k$ and an $\bar M$-bounded Herr cocycle $(y, z)$ of $T_1$ with $\pi(y) = p^k y_2$ and $\pi(z) = p^k z_2$. By (e), $\kappa_2 = \mathrm{cl}(y_2, z_2) \in H^1_f(G_{K_s}, T_2)$. By (g) there is $\kappa_1$ with $\pi_* \kappa_1 = p^c \kappa_2$, and by (h) there is an $\bar M$-bounded Herr cocycle $(y', z')$ of $T_1$ with $\mathrm{cl}(y', z') = p^{c'} \kappa_1$. The pair $(\pi y' - p^{c'+c} y_2, \pi z' - p^{c'+c} z_2)$ is an $\bar M$-bounded Herr cocycle of $T_2$, and by (i) its class is $p^{c'} \pi_* \kappa_1 - p^{c'+c} \kappa_2 = 0$. By (e) it equals $(\varphi m - m, \gamma m - m)$ with $m \in N(T_2)$. By (f) there is $m_1 \in N(T_1)$ with $\pi(m_1) = p^{c''} m$. Put
$$y = p^{c''} y' - (\varphi m_1 - m_1), \qquad z = p^{c''} z' - (\gamma m_1 - m_1).$$
Since $\varphi$ and $\gamma$ commute, $(\varphi m_1 - m_1, \gamma m_1 - m_1)$ is a Herr cocycle, so $(y, z)$ is one. By (d), $Q^{\bar M}(\varphi m_1 - m_1) \in N(T_1)$, and by (c), $\gamma m_1 - m_1 \in X_s N(T_1)$, so $(y, z)$ is $\bar M$-bounded. Finally $\pi(y) = p^{c''}(\pi y' - \varphi m + m) = p^{c'' + c' + c} y_2$, and in the same way for $z$. Take $k = c'' + c' + c$.

*Step 2: the bound on the defect.* Since $(y_2, z_2)$ is a Herr cocycle, $\pi(d(y_1, z_1)) = d(y_2, z_2) = 0$. By (a) there is $w \in D(T_0)$ with $\iota(w) = d(y_1, z_1)$. This is 1. By (c), (d), (e) and the Lemma, $\iota(Q^{\bar M} w) = Q^{\bar M} d(y_1, z_1) \in X_s N(T_1)$. Write $Q^{\bar M} w = X_s x$ with $x \in D(T_0)$. Then $\iota(x) \in N(T_1)$, so $x \in N(T_0)$ by (b). Hence $Q^{\bar M} w \in X_s N(T_0)$, and since $X_s$ is a unit of $\mathcal{E}$, $w = X_s w'$ with $Q^{\bar M} w' \in N(T_0)$. This is 2.

*Step 3: the torsion.* Take $k$ and $(y, z)$ from Step 1. Then $\pi(p^k y_1 - y) = 0$ and $\pi(p^k z_1 - z) = 0$, so by (a) there are $y_0, z_0 \in D(T_0)$ with $\iota(y_0) = p^k y_1 - y$ and $\iota(z_0) = p^k z_1 - z$. Since $Q^{\bar M} \iota(y_0) \in N(T_1)$, (b) gives $y_0 \in N(T_0)[Q^{-\bar M}]$. In the same way $\iota(z_0) \in X_s N(T_1)$, and the argument of Step 2 gives $z_0 \in X_s N(T_0)$. Since $d(y, z) = 0$,
$$\iota(p^k w) = p^k d(y_1, z_1) = d(p^k y_1 - y, p^k z_1 - z) = \iota(d(y_0, z_0)).$$
Since $\iota$ is injective on $D(T_0)$, $p^k w = d(y_0, z_0)$. This is 3. $\square$

We now state the clauses on Wach lattices. They concern every good triple $(K, s, L)$ with its Wach datum and every crystalline lattice $T$; the clauses on maps concern maps between crystalline lattices.

**Theorem 6.5.4 (Clauses on Wach lattices).** Assume a comparison datum is given. Then the following seventeen clauses hold.

1. $N(T)$ is the sum of the $N_i(T)$, and each $N_i(T)$ is free over the letter $i$ of $A$.
2. $N(T)$ is stable under $\Gamma$, $(\gamma_g - 1) N(T) \subseteq \pi N(T)$ for all $g \in \Gamma$, and $(\gamma - 1) N(T) \subseteq X_s N(T)$.
3. The comparison map $N(T) \to D_{\mathrm{cris}}(T)$ has kernel in $\pi N(T)$ and image spanning $D_{\mathrm{cris}}(T)$ over $L$. It sends $Q^k \varphi(x)$ to $p^k \varphi(\text{image of } x)$ whenever $Q^k \varphi(x) \in N(T)$.
4. The expansions of $N(T)$ at points where $X$ is $\zeta - 1$ for a $p$-power root of unity $\zeta$ have coefficients in $D_{\mathrm{cris}}(T)$, and they give the Hodge filtration at each embedding.
5. If $T$ has jumps in $[-M, h]$, then $Q^{M_i} \varphi(N_{i-1}(T)) \subseteq N(T)$ and $Q^{h_i} N_i(T)$ lies in the span of $\varphi(N_{i-1}(T))$. An element $x$ with $Q^k x \in N(T)$ for some $k$ lies in $N(T)$ exactly when, for each letter $i$, each root of $Q$ at the letter $i$ and each $k$ with $Q^k x \in N(T)$, the element $Q^k x$ lies in $I_k N(T)$, where $I_k$ is the ideal of elements of $A$ whose expansion at that root is divisible by $X^k$.
6. $N(T)$ is saturated: if $p^k x \in N(T)$, then $x \in N(T)$. A map of lattices that is bijective after inverting $p$ is injective on Wach modules and onto up to a power of $p$. For a short exact sequence, the sequence of Wach modules is exact up to powers of $p$, saturated at $T_0$, and has a cokernel of finite length.
7. If $y$ times a finite product of elements $\varphi^j(Q)$ lies in $N(T)$, $z \in \pi N(T)$ and $(y, z)$ is a Herr cocycle, then $\mathrm{cl}(y, z) \in H^1_f(G_{K_s}, T)$.
8. Let $0 \to T \to T' \to \mathbf{1} \to 0$ be exact with $T'$ crystalline, and let $e \in N(\mathbf{1})$ be fixed by $\varphi$ and $\Gamma$. If $x \in N(T')$ maps to a multiple of $e$, then $\varphi x - x$ and $\gamma x - x$ are the images of elements $y \in N(T)[Q^{-\bar M}]$ and $z \in X_s N(T)$, where $T$ has jumps in $[-M, h]$.
9. [Theorem 6.3.7](/entry/wach-module-descent-to-tame-subextension/).
10. A free $A$-submodule of $D(T)$ that spans $D(T)$ over $\mathcal{E}$, is stable under $\gamma$, has $(\gamma - 1)$ with image in $\pi$ times it, and has the two conditions of clause 5 up to some power of $Q$, equals $N(T)$.
11. For $y \geq 1$, the quotient $N(T)[Q^{-y}]/N(T)$ is free of finite rank over $\mathcal{O}$, and $\gamma$ acts on it semisimply with eigenvalues $\chi(\gamma)^{-(a+j)}$, for $a$ a jump of $T$ and $1 \leq j \leq y$.
12. The class map on Herr cocycles is onto $H^1(G_{K_s}, T)$, and its kernel is the set of pairs $(\varphi m - m, \gamma m - m)$ with $m \in D(T)$. If $s = 1$ and $p \neq 2$, a second class map on $\Delta$-invariant Herr cocycles has the same two properties, with $\Delta$-invariant elements $m$.
13. A class $\kappa \in H^1(G_K, T)$ lies in $H^1_f(G_K, T)$ exactly when its restriction to $G_{K_s}$ lies in $H^1_f(G_{K_s}, T)$.
14. Fact (e) of the proof above, for $T$ with jumps in $[-M, h]$.
15. [Theorem 6.5.3](/entry/defect-torsion/).
16. If $\pi : T_1 \to T_2$ is onto and $T_1$ has jumps in $[-M, h]$, then $X_s^{m} N_i(T_2) \subseteq \pi(N_i(T_1))$ for $m = \max_j (M_j + h_j)$. If $s = 1$, a $\Delta$-invariant variable $\pi'$ that is a unit multiple of $\pi^{(p-1)/e}$ gives the same with the exponent $\lceil e m/(p - 1) \rceil$ on $\pi'$, for elements whose $\Delta$-defects lie in $\pi(N_i(T_1))$. Here $e = [K : K_0]$.
17. A comparison of the Wach module with the étale module $D(T)$ through the comparison datum, and a bound at infinite level.

Lean: `GlobalTheory.NL.wach_used_clauses` (also `GlobalTheory.T.wachLattice_laterClauses_hold`, a second name).

*Proof.* Each clause is a theorem of this development, and the proof collects them. Clause 9 is [Theorem 6.3.7](/entry/wach-module-descent-to-tame-subextension/), clause 14 contains the input (e) used above, and clause 15 is [Theorem 6.5.3](/entry/defect-torsion/). $\square$

**Remark 6.5.5 (Formalization).** The seventeen clauses are the conjunction `DeltaInvariantNormBound` in [UsedLocalConclusion.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/UsedLocalConclusion.lean#L9): `WachLatticeFreeGlobal`, `P2` to `P9`, `WachCharacterisation`, `gammaSemisimpleQuotientGlobal`, `Pr2a` to `Pr2d`, `lem3` and `ConclusionE`. The name speaks of a norm bound, but the clauses are structural facts. Clause 1 keeps only the freeness part of `P1`; the parts on duals and tensor products are not included. Clause 10 keeps only the first half of `WachTwistCharacterisation`. In [WachLatticeLaterClausesHold.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WachLatticeLaterClausesHold.lean#L28) the clauses come from `letters_free`, `wachLattice_galois_trivial_mod_uniformizer`, `wachLattice_comparison_dcris`, `wach_lattice_expansion_at_low_level_points`, `wachLattice_heights_from_hodgeJumps`, `wachModule_saturated_exactness_crystalline`, `herrCocycle_poles_frobeniusQ_crystalline`, `p8_of_cmpOf`, `wachModule_descent_to_tame_subextension`, `wachModule_uniqueness_characterisation`, `gammaSemisimpleQuotientD_statement`, `herr_H1_description`, `mem_H1f_iff_res_mem`, `wachIntegralComplex_cocycle_class_finite`, `defect_torsion_second_cohomology_kernel`, `cokernel_crystalline_surjection_killed_by_X_pow`, `NygaardExtension.main` and `local_comparison_of_cmpOf`. We opened only the two proofs of this section. We did not unfold `levN`, `ptK`, `FildR`, `SSEig`, `WachEtaleComparison` or `WachInfiniteLevelBound`, so clauses 4, 11 and 17 are given by their role. The facts (a) to (i) in the proof of the Theorem are `DD_exact` with `fontaine_decompletion`, `mem_wachN_of_map_mem_saturated`, `wachLattice_galois_trivial_mod_uniformizer`, `wachLattice_heights_from_hodgeJumps`, `wachIntegralComplex_cocycle_class_finite` with `jumps_ses_and_one`, `wachN_cokernel_killed_by_power`, `h1fKs_onto_up_to_pow`, `H1f_class_wach_pair_filtration_jumps` and `herr_a_and_natural`. The definition `p2d` at [DeltaInvariantLattices.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DeltaInvariantLattices.lean#L323) does not ask that $(y_1, z_1)$ be a cocycle, and the short exact sequence hypothesis inside it is not used by `defect_of_lift`, which takes exactness from (a). The defect theorem runs under `maxHeartbeats 1600000` and `synthInstance.maxHeartbeats 400000` ([DefectTorsionSecondCohomologyKernel.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DefectTorsionSecondCohomologyKernel.lean#L343)), and Step 1 is the private `lift_multiple_lemma` (line 201). Both second names are proved by `first | exact ...` under `maxHeartbeats 1000000`.
