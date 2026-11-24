---
title: Cuts and the Galois preconditions
decls:
  - GlobalTheory.ClosingSixth.conclusionG6_of_adm_alt
  - GlobalTheory.T.prvG6_of_admissible'
  - UpperTheory.GalS.prvG5_of_admissible_cutRec
  - UpperTheory.GalC.facts_of_galois_preconditions_of_cutRec
  - UpperTheory.GalC.exists_good_cut_facts_tie4
  - UpperTheory.GalS.galois_preconditions_at_mem
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cuts and the Galois preconditions

This section proves the two facts that [the closed link bound](/entry/final-alt-alt/) of Section 6 takes. The first is [the good cut facts](/entry/exists-good-cut-facts-tie4/): a datum with the Galois preconditions and $\mathrm{Tie}_4$ has a good cut, and the cut datum has the norm choice facts. The second is [the Galois preconditions at layer points](/entry/galois-preconditions-at-mem/). The norm choice facts differ from the Galois preconditions in four conditions, and two of them are the fifth and sixth Galois conclusions. We prove these two first. They are statements on the local Galois representations at the places over the type primes, and they need [local Galois cohomology](/learn/galois-cohomology/#local-fields).

We keep the notation of Sections 6 and 10. A datum $D$ has local indices $i$, each with a prime $\ell_i$, a ring $O_i$, points $\Pi$ and good families $r_x : G_E \to \mathrm{GL}_{n_V}(O_i)$. A character $\chi_1$ of $G_E$ and an element $\gamma_0$ of the inertia group at a place over $g_k$ are fixed. The index $i$ is *of type HG* if the condition HG of the datum holds at $i$; at such an index a residual representation $\bar\rho$ of rank $r$ may exist. We write $\mathrm{RbEx}(D)$ for the statement that at each index of type HG there is a residual representation.

**Definition 8.13.1 (The fifth and sixth Galois conclusions).** Let $D$ be a datum. The *fifth Galois conclusion* says: at each index $i$ and each place $w$ in $S_i \cup Q_i$ not over $\ell_i$,

1. at the places of $Q_i$ and the places over the primes $p_{de}$, each inertia element $\sigma$ satisfies $(r_x(\sigma) - 1)(r_x(\sigma) - \chi_1(\sigma)) = 0$ and acts as $\mathrm{diag}(1^{(r)}, \chi_1(\sigma)^{(t)})$;
2. at the places over the type primes, a polynomial whose value at $\chi_1(\gamma_0)$ is a unit kills $r_x(\gamma_0)$ on the residual part;
3. a class $\varphi$ vanishes on a fixed element $y_g$, and the starred cohomology group vanishes.

The *sixth Galois conclusion* says: if HG holds at $i$ and $r_x$ has an eigenvector with eigencharacter $\chi_1$ over $K$, then $x$ is in the set $Z_N$ and each parameter of $x$ is cuspidal.

**Definition 8.13.2 (The cut record).** The *cut record* $\mathrm{CutRec}(D)$ says: for each index $i$, each point $\Pi$ at $i$ with a value, and each place $w$ over $g_0$ or $g_1$, the local parameter $\mathrm{loc}_i(\Pi, w)$ is tame, of monodromy zero and squarefree.

**Proposition 8.13.3 (The sixth Galois conclusion).** Let $D$ be a datum with the admissible datum condition, and assume $\mathrm{RbEx}(D)$. Then the sixth Galois conclusion holds at $D$.

Lean: `GlobalTheory.ClosingSixth.conclusionG6_of_adm_alt` (also `GlobalTheory.T.prvG6_of_admissible'`, a second name).

*Proof.* Let $i$ be of type HG and let $r_x$ have an eigenvector with eigencharacter $\chi_1$. The representation decomposes into centred strings, and the weights of a string are pure. The admissible datum makes the summand with eigencharacter $\chi_1$ the $\ell$-adic realization of a Hecke character, by the comparison of a Hecke character with its $\ell$-adic realization. The residual representation of $\mathrm{RbEx}(D)$ fixes the ranks of the absolutely irreducible constituents: over the valuation ring, the irreducible constituents of a product of characteristic polynomials and their ranks are unique. So the string through the eigenvector has length one and rank one. This puts $x$ in $Z_N$ and makes each parameter cuspidal. $\square$

**Theorem 8.13.4 (The fifth Galois conclusion).** Assume local finiteness, local Tate duality and the local Euler characteristic formula of [local Galois cohomology](/learn/galois-cohomology/#local-fields). Let $D$ be a datum with the admissible datum condition, $\mathrm{RbEx}(D)$ and $\mathrm{CutRec}(D)$. Then the fifth Galois conclusion holds at $D$.

Lean: `UpperTheory.GalS.prvG5_of_admissible_cutRec`.

*Proof.* There are three steps.

1. **Local-global compatibility.** The cut record and the admissible datum give the compatibility of $r_x$ at the places of $S_i \cup Q_i$ with the local parameters: the inertia acts through the tame quotient with the eigenvalues of the parameter. This gives parts 1 and 2, and the eigenvalue condition at the places over the type primes.
2. **Cohomology.** Let $\bar\rho(\chi_1^{-1})$ be the residual twist at a place $w$. If $\chi_1(\gamma_0)$ is not a root of the characteristic polynomial of $\bar\rho(\gamma_0)$, then $H^0$ of the twist and of its dual vanish. Local Tate duality gives $H^2 = 0$ from $H^0$ of the dual, and the local Euler characteristic formula with finiteness gives $H^1 = 0$ when $w$ is not over $\ell_i$, since the Euler characteristic is $0$ there.
3. **The class.** With $H^1 = H^2 = 0$, the class $\varphi$ vanishes on $y_g$ and the starred group vanishes. This is a sufficient condition for the Galois clause. $\square$

**Theorem 8.13.5 (Norm choice facts from the Galois preconditions).** Assume the Chebotarev input of the third layer, local finiteness, local Tate duality and the local Euler characteristic. Let $D$ be a datum and $n$ a norm choice that satisfy the Galois preconditions, and assume $\mathrm{CutRec}(D)$. Then $D$ and $n$ satisfy the norm choice facts.

Lean: `UpperTheory.GalC.facts_of_galois_preconditions_of_cutRec`.

*Proof.* The norm choice facts have twenty one fields. Seventeen of them are among the eighteen Galois preconditions. The remaining four are proved as follows.

1. **The residual rank part.** The joint condition in the point conditions gives $\mathrm{RbEx}(D)$.
2. **The second conclusion.** It is the Theorem (The fifth Galois conclusion), the Proposition (The sixth Galois conclusion) and the multiplicity statement of the preconditions.
3. **The weight jumps and admissible jumps.** The tie at $0$ and the first admissibility condition, which are parts of the admissible datum, the second and fifth admissibility conditions of the point conditions and the cut record give the de Rham weights and their jumps at the points. With the weight and block conditions they give the admissibility of the jumps for each size datum.
4. **The duties.** The Chebotarev input, the large coefficient condition, the forty first provision of the first conclusion, the jumps of step 3 and the residual representation give the duties. $\square$

**Theorem 8.13.6 (The good cut facts).** Assume the Chebotarev input, local finiteness, local Tate duality and the local Euler characteristic. Let $D$ be a datum and $n$ a norm choice that satisfy the Galois preconditions and $\mathrm{Tie}_4(D)$. Then $D$ has a good cut $c$ such that the cut datum $D_c$ and the cut norm choice satisfy the norm choice facts and $\mathrm{Tie}_4(D_c)$.

Lean: `UpperTheory.GalC.exists_good_cut_facts_tie4`.

*Proof.* There are three steps.

1. **The cut.** The central elements built from the coefficients of a central idempotent, the Galois preconditions and $\mathrm{Tie}_4(D)$ give a good cut $c$ of $D$: it keeps the indices with good points and acts by an integer on the good eigensystems.
2. **The facts.** Each of the eighteen Galois preconditions moves to the cut. The point conditions move by the forty first provision, the admissible datum moves to the cut, the first conclusion is proved again on the cut from the moved conditions, and the other conditions restrict to the kept points. A good cut satisfies the cut record. The Theorem (Norm choice facts from the Galois preconditions) gives the norm choice facts on the cut.
3. **The ties.** The four ties restrict to the eigenvectors of the cut. $\square$

This is the cut hypothesis of Section 6. Now the Galois preconditions at layer points.

**Theorem 8.13.7 (The Galois preconditions at layer points).** Assume the published inputs of the third layer, the geometric compatibility of the [[Galois representation|JQEYEQJY2G]]s, the local Selmer input, depth zero support, local finiteness, local Tate duality and the local Euler characteristic. Let $h_L$ witness [the local Langlands recursion](/step/rect-exists-def/). Then at every layer point for $h_L$, the datum and its norm choice satisfy the Galois preconditions.

Lean: `UpperTheory.GalS.galois_preconditions_at_mem`.

*Proof.* Properties at every layer point join. Three facts hold at every layer point: the inputs of the point with a pin and the count of jumps, the condition on the finite triples, which uses the local Selmer input, and the good condition on all finite triples. At each point the eighteen conditions are built as follows.

1. **The first twelve.** The local theta inputs, the finiteness of Harish-Chandra, the rapid decay of cusp forms, depth zero support and the count of jumps give twelve conditions: the point conditions of [the theta conditions](/entry/theta-conditions-of-inputs-of-jumps-card/) of Section 15; the admissible datum, from residual irreducibility of [Theorem 3'](/entry/residual-irreducible-of-theorem-three-prime-alt/) of Section 16 with the label tie, the tame eigenvalue condition, the fifth admissibility condition, a Brauer-Nesbitt input and the depth zero condition; the first conclusion; the multiplicity statement, from the reduced multiplicity; the residual representation; the tame eigenvalue condition; the weight condition, from the character choice; the block condition; the unramified $\mu$ tie; the depth condition on the Galois side, from depth zero support; base change; and the lambda condition.
2. **The other six.** The localization uniqueness comes from the coincidence of local data, the large coefficient condition and the norm choice tie from the point inputs, the good triples from the finite triples, the same twist from the twist at the point, and the good condition from the third fact. $\square$

**Remark 8.13.8 (Formalization).** The results are at [PrvG6OfAdm.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PrvG6OfAdm.lean#L16), [AdmissibleJOfRestricted.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AdmissibleJOfRestricted.lean#L28), [CFacts.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFacts.lean#L45) (lines 45 and 58) and [PreAtMem.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PreAtMem.lean#L86). The second name of the sixth conclusion is at PrvG6OfAdmStatement.lean, line 11. The conclusions are `ConclusionG5` and `ConclusionG6` of SumRepresentations.lean (lines 243 and 268), the cut record is `CutRec` of RhoBar.lean (line 12) with `Nc`, and the move of the preconditions to the cut is `pre_cut_alt` (CFacts.lean, line 23). The sixth conclusion uses only lemmas with no hypothesis beyond the admissible datum and $\mathrm{RbEx}$. In the fifth conclusion, step 2 is `hOneTwo_of_localFiniteness_tateDuality_eulerChar`; we did not unfold the three local inputs, nor `HStarZero`. In the norm choice facts, the admissible jumps `admJ` compute the jumps of step 3 a second time. The first twelve conditions are `core0_of_local_duality_inputs` (PreAtMem.lean, line 54), which takes local finiteness, local Tate duality and the local Euler characteristic and does not use them; these three enter the chain only through the fifth conclusion.
