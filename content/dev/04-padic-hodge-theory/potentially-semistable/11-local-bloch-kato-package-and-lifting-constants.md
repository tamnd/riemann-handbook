---
title: The local Bloch-Kato package and the local lifting constants
decls:
  - GlobalTheory.BlochKatoLocalOfHyp.bkAll_of_blochKatoLocal
  - GlobalTheory.BlochKatoLocalOfHyp.blochKatoLocal_allPrimes_of_blochKato
  - GlobalTheory.T.localConstants_from_admitted_local_Galois_statements
  - GlobalTheory.localConstants_from_admitted_local_Galois_statements_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local Bloch-Kato package and the local lifting constants

This section proves two local inputs of the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). The first is the local Bloch-Kato package of the previous section, for every prime and every finite extension of $\mathbb{Q}_\ell$. We derive it from the local results of Bloch and Kato, local Tate duality and the local Euler characteristic formula. The published results are stated over $\mathbb{Q}_\ell$; the package is over any finite extension $L$ of $\mathbb{Q}_\ell$ and also contains a right exactness statement and a statement with finite coefficients. The second input is a family of local statements on Wach modules and on lifts of Bloch-Kato classes, with the explicit constants $10$, $23$, $32$ and $32$. We use the [Bloch-Kato groups](/learn/padic-hodge/#local-bloch-kato-theory) and the [[Galois cohomology|9MPCZ3EAJM]] of [local fields](/learn/galois-cohomology/#local-fields).

We keep the notation of the previous sections. For a representation $V$ of $G_K$, a *Bloch-Kato cocycle* is a continuous cocycle $c : G_K \to V$ such that $c(g) \otimes 1 = g x - x$ for some $x \in V \otimes B$, and $H^1_f(K, V)$ is the space of their classes. Local period data at $\ell$ that is tied to its $A_{\inf}$ data gives, for each finite extension $K$ of $\mathbb{Q}_\ell$, the period data of $K$; all statements below are about these period data.

**Theorem 6.11.1 (The local Bloch-Kato package at one field).** Assume the local results of Bloch and Kato, local Tate duality and the local Euler characteristic formula. Let $\ell$ be a prime, fix local period data at $\ell$ that is tied to its $A_{\inf}$ data, and let $K$ be a finite extension of $\mathbb{Q}_\ell$. Then the five statements of the local Bloch-Kato package hold for the period data of $K$.

Lean: `GlobalTheory.BlochKatoLocalOfHyp.bkAll_of_blochKatoLocal`.

*Proof.* The local results of Bloch and Kato, applied to the tied period data and to $K$, give three statements over $\mathbb{Q}_\ell$: the dimension formula, the rational duality and the integral duality. We get the five statements of the package from these in the following order.

Statement 1, the rational duality over $L$, follows from the rational duality over $\mathbb{Q}_\ell$ by a result proved elsewhere in this development. The classical reason is this: a representation over $L$ is a representation over $\mathbb{Q}_\ell$ by restriction of scalars, and an $L$-bilinear pairing into $L(1)$ followed by the trace $L \to \mathbb{Q}_\ell$ is a $\mathbb{Q}_\ell$-bilinear pairing into $\mathbb{Q}_\ell(1)$; Bloch-Kato cocycles do not depend on the field of coefficients.

Statement 2, the dimension formula over $L$, follows in the same way from the dimension formula over $\mathbb{Q}_\ell$, by a result proved elsewhere in this development.

Statement 3, right exactness on $H^1_f$, uses only the tie between the period data and the $A_{\inf}$ data. Let $f : V \to V'$ be a surjective $G_K$-map with $V$ crystalline, and let $c'$ be a Bloch-Kato cocycle of $V'$ with $c'(g) \otimes 1 = g x' - x'$. Since $V$ is crystalline, $V'$ is de Rham and the maps $D_{\mathrm{cris}}(V) \to D_{\mathrm{cris}}(V')$ and $D_{\mathrm{dR}}(V) \to D_{\mathrm{dR}}(V')$ are onto, with the filtration. The element $x'$ gives an element $d_1$ of $D_{\mathrm{cris}}(V')$ and an element $d_2$ of $D_{\mathrm{dR}}(V')$; we lift them to $D_{\mathrm{cris}}(V)$ and $D_{\mathrm{dR}}(V)$, and from the lifts we build a Bloch-Kato cocycle $c$ of $V$ with an element $x \in V \otimes B$. Then $f(x) - x'$ is fixed by $\varphi$ and lies in $\mathrm{Fil}^0$ after the map to $B_{\mathrm{dR}}$. By the fundamental exact sequence for crystalline representations, $f(x) - x' = v \otimes 1$ with $v \in V'$. Hence $f \circ c - c'$ is the coboundary of $v$.

Statement 4, the integral duality over $\mathcal{O}$, follows from the integral duality over $\mathbb{Z}_\ell$ by a result proved elsewhere in this development.

Statement 5, the integral duality with coefficients $T/\varpi^r T$, follows from statements 1 and 4 by a result proved elsewhere in this development, which uses local Tate duality, the local Euler characteristic formula and the tie. $\square$

**Theorem 6.11.2 (The local Bloch-Kato package at all primes).** Assume the local results of Bloch and Kato, local Tate duality and the local Euler characteristic formula. Then for every datum, every prime $\ell$ and every finite extension $K$ of $\mathbb{Q}_\ell$, the local Bloch-Kato package holds for the period data of $K$ in the local data of the datum at $\ell$.

Lean: `GlobalTheory.BlochKatoLocalOfHyp.blochKatoLocal_allPrimes_of_blochKato`.

*Proof.* A datum gives, at each prime $\ell$, local period data, $A_{\inf}$ data and a tie between them. Apply the previous Theorem to them. $\square$

This is the input "local Bloch-Kato package" of the twisted torsion statements in the previous section.

We now state the lifting statements. Fix a datum, Wach data, Fontaine data and a comparison datum over it, and a good triple $(K, s, L)$ with its Wach datum. Let $F : T_1 \to T_2$ be a map of lattices that is onto, with $T_1$ and $T_2$ crystalline. Assume that at each letter $i$ the jumps of $T_1$ over the embeddings above $i$ lie in $[-M_i, h_i]$, and put $M = \max_i M_i$ and $H = \max_i (M_i + h_i)$. We say that we are in *case A* if $K = K_0$, $s = 1$ and $\ell \neq 2$, and in *case B* if $G_{K_s}$ is the whole group and $[K : K_0] = (\ell - 1)\ell^{s-1}$. Put
$$c_H = \Big\lceil 1 + \log_\ell (H + 1) \Big\rceil, \qquad e_A = \Big\lfloor \frac{H \ell}{(\ell - 1)^2} + 3 + \log_\ell (H + 1) \Big\rfloor, \qquad e_B = 2 H s + v_\ell((2H)!).$$
We say that $F$ *lifts with exponent $e$* if for every Bloch-Kato cocycle $c$ of $T_2$ the cocycle $\ell^e c$ is $F \circ c_1$ plus a coboundary, for a Bloch-Kato cocycle $c_1$ of $T_1$.

**Definition 6.11.3 (Local lifting statements).** Let $C, C_A, C_B, C_K \in \mathbb{R}$. The *local lifting statements with constants $C, C_A, C_B, C_K$* say that, for every prime $\ell$ and every good triple $(K, s, L)$ with its Wach datum, the following eight statements hold.

1. A resultant bound: let $S_1, S_2 \subseteq \mathbb{Z}$ be finite and disjoint, $s_0 \in \mathbb{N}$, and $c : \mathbb{Z} \to \mathcal{O}$ with $v(c_a - c_b) = s_0 + v_\ell(a - b)$ for distinct $a, b \in S_1 \cup S_2$. Put $P_j = \prod_{b \in S_j} (X - c_b)$. If $v(P_2(c_a)) + v(P_1'(c_a)) \leq E$ for all $a \in S_1$, then $\ell^E$ lies in the ideal of $\mathcal{O}[X]$ generated by $P_1$ and $P_2$.
2. Bounds on the cokernel of $N_i(T_1) \to N_i(T_2)$: it is killed by $X^H$, by $\ell^{e_B}$ in case B, by $\ell^{e_A}$ in case A, and by explicit elements in the case $s = 1$, $\ell \neq 2$ with $[K : K_0] = e$.
3. In case A, with $s_i$ the least $k$ such that $\pi^k$ kills that cokernel, $\ell^a \pi^j$ kills it whenever $(s_i - j)\ell/(\ell - 1)^2 + c_H \leq a$.
4. In case A, $s_{i-1} \leq M_i + h_i + c_H + 3 + s_i/(\ell - 1)$.
5. In case A, a list of bounds on $s_i$ and on two related exponents, the last of them with the constant $C$.
6. In case A, formulas for $\gamma - 1$ on $\pi_0^r N^\Delta_i(T)$ and bounds on the solutions of a recursion in $N^\Delta_i(T)$.
7. In case A, decompositions of $\varphi^k(\pi_0 + \ell)$ and of $(\varphi^j \pi_0)^r$ in the ring of the Wach datum.
8. The lifting theorem: in case A, $F$ lifts with an exponent $e_{PA}$, and in case B with an exponent $e_{PB}$, both explicit in $\ell$, $s$, $M$, $H$ and the jumps of $T_1$; a product of the numbers $1 - \chi(\gamma)^{-j}$, over a finite set of integers $j$ built from the jumps of $T_1$ and from $M$, is a unit times a power of $\ell$; $e_{PA} \leq C_A (2 + H/\ell + \log_\ell(H + 1))$ in case A, $e_{PB} \leq C_B (H s + 1)$ in case B, and $e_{PB} \leq C_K H$ in case B with $s = 1$; and the lifting descends to subfields $K' \subseteq K$ with $K/K'$ Galois, with the exponent increased by $v_\ell [K : K']$.

Lean: `Formalism.MainNotions.LiftingTheory.aux₃`.

**Theorem 6.11.4 (The local lifting statements with fixed constants).** Assume the local results of Bloch and Kato, local Tate duality and the local Euler characteristic formula. Then for every datum and all Wach, Fontaine and comparison data over it, the local lifting statements hold with the constants $C = 10$, $C_A = 23$, $C_B = 32$ and $C_K = 32$.

Lean: `GlobalTheory.localConstants_from_admitted_local_Galois_statements_alt` (also `GlobalTheory.T.localConstants_from_admitted_local_Galois_statements`, a second name).

*Proof.* The proof does not use the three assumptions. The lifting theory has twenty-three conditions on the local data, which are its admitted inputs. They include the clauses on Wach lattices of the Theorem in the section on Wach clauses, the existence of Herr classes for extensions up to a unit, a semisimplicity statement for $\gamma$, restriction and corestriction on $H^1_f$, the naturality of the class maps, Fontaine's bounds and a statement on jumps. This development proves all twenty-three from the given data. By [Theorem 8.20.2](/entry/frobenius-lifting/), the twenty-three conditions imply the local lifting statements with the constants $10$, $23$, $32$ and $32$. $\square$

**Remark 6.11.5 (Formalization).** The Theorem at one field uses `GlobalTheory.T.blochKatoAnnihilator_of_rationalLocalDuality`, `GlobalTheory.T.blochKatoDim_of_Ql_dimensionFormula`, `GlobalTheory.BKRightExact.bkARightExact_of_tied`, `GlobalTheory.T.blochKato_annihilator_of_integralLocalDuality` and `GlobalTheory.T.breuilKisin_partC_of_partA_partB_finite_level`; the first four statements of the package are `bkACore`, `bkADim`, `bkARightExact` and `bkBCore`, and the fifth is `bkC`. Local Tate duality and the Euler characteristic formula enter only in the last of these, at [BlochKatoLocalAllPrimesOfBlochKato.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BlochKatoLocalAllPrimesOfBlochKato.lean#L22), whose name refers to Breuil-Kisin modules although it proves statement 5. We opened the proof of right exactness: its intro drops the crystallinity of $V'$, which is not needed since `lift_periods` shows that $V'$ is de Rham; the lifts come from `GlobalTheory.T.crystalline_coboundary_lift` and `GlobalTheory.T.exists_blochKato_cocycle_of_crys_deRham_pair`, whose proofs we did not open. We did not open the proofs of the other four steps, so the reasons given for statements 1, 2, 4 and 5 are the classical ones. The local lifting statements are `aux₃` in [LiftingTheory.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LiftingTheory.lean#L589), the conjunction of `ConclusionL`, `ConclusionW`, `WachAnnihilatorAll`, `WachExponentRecursionAll`, `WachResultConstant`, `ConclusionH`, `ExistsUnitClasses` and `LiftTheoremAllCases`. We unfolded `coreL`, `coreWX`, `coreWA`, `coreWB`, `WachQuotientAnnihilator`, `WachExponentRecursion`, `coreLiftA`, `coreLiftB`, `coreLiftR` and `coreLiftO`; the statements 5, 6 and 7 and the descent in 8 are given by their role. The proof is `fun _ _ _ D HW F Cm => ...` at [LocalConstantsFromAdmittedLocalGaloisStatements.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalConstantsFromAdmittedLocalGaloisStatements.lean#L14): the three hypotheses are discarded, so the name of the theorem is misleading. The twenty-three conditions are `LiftingTheory.admitted`, proved by `GlobalTheory.LiftAdmitted.all_admitted` through its second name `GlobalTheory.T.liftingTheorem_wachModuleLemma_hypotheses_admitted`; of its two conjuncts only the first is used. That proof drops clause 17 of the Wach clauses and calls `GlobalTheory.T.wachLattice_laterClauses_hold` a second time for one condition. The second name is proved by `first | exact ...` under `maxHeartbeats 1000000`.
