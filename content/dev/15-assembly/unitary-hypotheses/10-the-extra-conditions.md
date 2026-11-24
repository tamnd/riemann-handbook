---
title: The extra conditions
decls:
  - GlobalTheory.T.exists_const_tieChi_bound_of_facts
  - GlobalTheory.ExtraFromFacts.main_alt_alt
  - GlobalTheory.T.exists_bound_tieChi_of_prints
  - GlobalTheory.NormFromFacts.main_alt_alt
  - GlobalTheory.T.conclusion41_of_pAdicHodge_alt
  - GlobalTheory.ClosingLocalInputs.main_alt_alt
  - GlobalTheory.T.no_cut_passes_of_artin_reciprocity
  - GlobalTheory.Pass.stepsNoCut_of_artin_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The extra conditions

This section proves the extra conditions at a datum with the norm choice facts and the four tie conditions. Step 1 of [the link inequality for one family](/entry/link-n-of-tw-good-galois-preconditions/) of Section 6 uses them, and they become the family facts of Section 8 for the cut family. There are two conditions. The first is a commuting endomorphism of the Hecke module that separates the good eigensystems from the others. The second is a length bound for a congruence module at the type primes. The first comes from a central element of a group algebra and the series tie. The second has the content. It rests on a crystalline period bound and on Artin reciprocity, and its constant is $C_T = 40$.

We keep the notation of Sections 6 to 8. A datum $D$ has a CM field $E$, two type primes $g_0$ and $g_1$, ranks $r$, $n_V$, $t$ and $f$, and local indices $i$. At $i$ there are a prime $\ell_i$, a ring $O_i$, a finite set $X_i$ of Hecke eigensystems with subsets $Z^{\mathrm{good}}_i \subseteq Z_i$, and a Hecke algebra $T_i$ that acts on a free $O_i$-module $M_i$.

**Definition 8.10.1 (The congruence length).** Let $M^{\mathrm{low}}_i$ be the lattice part of the good eigenspaces in $M_i$, and $M^{\mathrm{up}}_i$ the part of the good eigenspaces in the lattice plus the other eigenspaces. The *congruence length* $\eta_i$ is the $\ell_i$-adic length of $M^{\mathrm{up}}_i / M^{\mathrm{low}}_i$. It measures the congruences between good and other eigensystems. Let $m(\pi)$ be the Hecke multiplicity of $\pi$.

**Definition 8.10.2 (The paired character condition).** Let $C \in \mathbb{R}$ and $C_T \in \mathbb{N}$. The *paired character condition* at $D$, $C$ and $C_T$ says the following. Let $i$ be a local index with $\ell_i = g_k$, and let $k' \neq k$. Let $r_x : G_E \to \mathrm{GL}_{n_V}(O_i)$ and $\rho_x : G_E \to \mathrm{GL}_r(O_i)$, for $x \in X_i$, be good families with a semisimple decomposition at each $\pi \in Z_i$. Let $\eta, s, S \in \mathbb{N}$, let $\mathrm{sg}$ be signs at the places over $\ell_i$, and let $U(w) \subset \mathbb{Z}$ be finite sets with:

1. $\eta + t + 1 < s$, $\log g_{k'} \le 2 \log g_k$, and $C_T\bigl((s + S)(n_V + 1)^2 + (n_V + 1)^3\bigr) < g_k$;
2. the signs are opposite at distinct conjugate places over $\ell_i$;
3. at each place $w$ over $\ell_i$, $|U(w)| \le n_V$, $U(w)$ holds the jumps of the local twist of $r_x$, and each $a \in U(w)$ is in $[0, t)$, near the centre $(t - 1)/2$, or in a window fixed by $\mathrm{sg}(w)$, with $a \neq -1, t$;
4. a finiteness condition at each good $\pi$, and the Tate-Shafarevich groups at $\ell_i$ of the twists $e$ with $0 < e < t$ are finite.

Then

$$\eta_i \le \sum_{\pi \in Z^{\mathrm{good}}_i} m(\pi)\, R(\pi),$$

where $R(\pi)$ is $4 f C n_V^3 (n_V + \eta + t) + 2 f r^2$ plus five local terms.

**Definition 8.10.3 (The extra conditions).** The *commuting endomorphism condition* at $D$ says: at each twisted index $i$ with $\ell_i \notin \{g_0, g_1\}$ there is an endomorphism $\alpha$ of $M_i$ that commutes with $T_i$, acts on each eigenvector of a good eigensystem by a fixed integer $N$, and acts by $0$ on each eigenvector of an eigensystem of $Z_i$ that is not good. The *extra conditions* at $D$, $C$ and $C_T$ are the commuting endomorphism condition and the paired character condition.

**Theorem 8.10.4 (The closing local inputs).** Assume global Artin reciprocity, the integrality input of Bhatt and Scholze, Fontaine's ring $B_{\mathrm{cris}}$, local Bloch-Kato theory, local Tate duality and the local Euler characteristic. Let $D$ be a datum with its local data, and let $C_T \ge 40$ and $8 C_T \le C$. Assume a pending datum of $D$ that is admissible in depth zero with the eigen span property, and twelve named conditions on $D$: the tie at $0$, the first, second and fifth admissibility conditions, the forty first provision, the fifth and sixth Galois conclusions, residual irreducibility of rank $r$, the series tie, a wild idempotent choice at the type primes, the inertia tie and the character tie. Then the paired character condition holds at $D$, $C$ and $C_T$.

Lean: `GlobalTheory.ClosingLocalInputs.main_alt_alt` (also `GlobalTheory.T.conclusion41_of_pAdicHodge_alt`, a second name).

*Proof.* There are four steps.

1. **The crystalline period bound.** The five $p$-adic inputs give a lifting statement at each prime $\ell$, since $C_T \ge 40$. For potentially crystalline lattices and a surjection between them, with jumps in $U \subset [-\eta, H]$ and inertia through a set of size at most $N$, if $C_T(H N^2 + N^3) < \ell$, then a lifting property holds with an explicit bound.
2. **Local statements.** [Local Bloch-Kato theory](/learn/padic-hodge/#local-bloch-kato-theory), local Tate duality and the local Euler characteristic give a local absorption bound for lengths, a local theorem with Bloch-Kato and duality, and the local Bloch-Kato conditions at all places.
3. **Residual facts.** At a good point the residual representation spans the matrix algebra, so it is absolutely irreducible. The congruences at the type primes hold. The Galois family conditions are read off the forty first provision.
4. **Conclusion.** Artin reciprocity and the facts of steps 1 to 3 give the bound. $\square$

The *norm choice facts* at a datum and a norm choice are a record of twenty one named conditions, as in Section 6. They include the admissible datum, the forty first provision, the first and second conclusions and residual irreducibility.

**Theorem 8.10.5 (The paired character condition from the facts).** Assume the published local inputs of Section 6. Then there is $C_T \in \mathbb{N}$ such that for each datum $D$ and norm choice $n$ with the norm choice facts and $\mathrm{Tie}_4(D)$, the paired character condition holds at $D$, $8 C_T$ and $C_T$.

Lean: `GlobalTheory.NormFromFacts.main_alt_alt` (also `GlobalTheory.T.exists_bound_tieChi_of_prints`, a second name).

*Proof.* Take $C_T = 40$ and $C = 8 C_T = 320$. Then $C_T \ge 40$ and $8 C_T \le C$. The integrality input of Bhatt and Scholze gives the local data of $D$: a Wach functor and a comparison. Now apply the Theorem (The closing local inputs). Its twelve conditions come from the hypotheses. The tie at $0$ and the first, second and fifth admissibility conditions come from the admissible datum. The forty first provision comes from the first conclusion, the fifth and sixth Galois conclusions from the second conclusion, residual irreducibility from the residual representation, and the wild idempotent choice from the duties. The pending datum and the other ties are $\mathrm{Tie}_4(D)$. $\square$

With $C_T = 40$ the bound asks $g_k > 40\bigl((s + S)(n_V + 1)^2 + (n_V + 1)^3\bigr)$. Local finiteness is not used.

The commuting endomorphism comes from a list of step statements with no cut.

**Definition 8.10.6 (The steps with no cut).** The *steps with no cut* are sixteen statements about a datum $D$, a local index $i$, a family $r$ and a place $w$ over $\ell_i$. We name those that we use.

1. *Central idempotent coefficients*: for a finite group $\Gamma$, a central idempotent $e$ of $\mathbb{C}[\Gamma]$ and a primitive $|\Gamma|$-th root of unity $\zeta$, each $|\Gamma| \cdot e(h)$ lies in $\mathbb{Z}[\zeta]$.
2. *The central step*: the first statement gives, at each $i$, a central element of a group algebra over $O_i$ whose image is $N$ times a product of the local operators of the series labels over all pairs $(k, v)$.
3. to 15. Statements on the places over a type prime, on the local type, on the potential, jump and lift families of the twists and duals of $r$, on the continuity of the twists, on local bounds, on a character at the type primes, and on the span of the residual representation.
16. *The global statement*: a bound of the congruence valuation of a cut by a sum of local terms.

The first statement is true. A central idempotent of $\mathbb{C}[\Gamma]$ is a sum of the idempotents

$$e_\chi = \frac{\chi(1)}{|\Gamma|} \sum_{g \in \Gamma} \chi(g^{-1})\, g,$$

and the values of the characters lie in $\mathbb{Z}[\zeta]$ (Serre, Linear Representations of Finite Groups, Section 2.6).

**Proposition 8.10.7 (The steps with no cut).** Assume global [[Artin reciprocity|7938EKMMVR]]. Then the sixteen steps with no cut hold.

Lean: `GlobalTheory.Pass.stepsNoCut_of_artin_alt` (also `GlobalTheory.T.no_cut_passes_of_artin_reciprocity`, a second name).

*Proof.* Each of the first fifteen statements is a theorem with no hypothesis. The first is the computation above. The sixteenth is the global pass from Artin reciprocity. $\square$

Only the last step uses Artin reciprocity, through [global class field theory](/learn/class-field-theory/#global-class-field-theory).

**Theorem 8.10.8 (The extra conditions).** Assume the published local inputs. Then there are $C \ge 0$ and $C_T \in \mathbb{N}$ such that for each datum $D$ and norm choice $n$ with the norm choice facts and $\mathrm{Tie}_4(D)$, the extra conditions hold at $D$, $C$ and $C_T$.

Lean: `GlobalTheory.ExtraFromFacts.main_alt_alt` (also `GlobalTheory.T.exists_const_tieChi_bound_of_facts`, a second name).

*Proof.* There are three steps.

1. **The paired character condition.** The Theorem (The paired character condition from the facts) gives $C_T$ with the paired character condition at $8 C_T$ and $C_T$. Put $C = 8 C_T$, so $C \ge 0$.
2. **A central element.** The Proposition (The steps with no cut) gives the central step and the central idempotent coefficients. Together they give, at each $i$, the central element of the group algebra.
3. **The commuting endomorphism.** The eigen span property of the pending datum, the central element, the series tie and five of the norm choice facts give the commuting endomorphism condition. The five facts are the forty first provision, the label tie, the tie at $0$ and the first and fifth admissibility conditions. The central element acts by the scalar $N$ on the types of good eigensystems and by $0$ on the others, and the eigen span property moves this to the eigenvectors. $\square$

The character tie and the inertia tie of $\mathrm{Tie}_4$ are used only in step 1.

**Remark 8.10.9 (Formalization).** The extra conditions are `ExtraAlt`, which is `Extra` of [BoundAtTwoAndThreeForFamily.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/BoundAtTwoAndThreeForFamily.lean#L51) with `aux₃` replaced by `PairedCharacterConditionAlt`, which drops the hypothesis `SetSQ`; the name speaks of characters, but the statement is a length bound. The theorems are at [ImportsExtraAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsExtraAlt.lean#L18), [ImportsFurtherLast.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherLast.lean#L13), [AdmG14OfAux.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AdmG14OfAux.lean#L15) and [StepsNoCutOfArtin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/StepsNoCutOfArtin.lean#L13); the four second names are `first | exact … | …` tactics in files named `…Statement.lean`. Neither the module names nor the second names describe the statements: `exists_const_tieChi_bound_of_facts` and `exists_bound_tieChi_of_prints` take the character tie as a hypothesis, "prints" matches nothing, and `conclusion41_of_pAdicHodge_alt` has 41 only in the hypothesis `provisionFortyOne`. `NormFromFacts.main_alt_alt` states "there is $C_T$" and proves it for $C_T = 40$; the field `LocalFinitenessK` of `Hypotheses₂` is not used. The closing local inputs use `crystallinePeriodBound_all_constant_ge_forty`, which has 3,069 declarations below it, and `admT_of_artin_reciprocity_and_local_conditions`. The steps with no cut are `NoCutStatement`, which differs from `StepsNoCut` in three parts: `adm2_alt` for `adm2`, `GaloisFamilyConditions'` for `GaloisFamilyConditions`, and the global step without `SetSQ`. The central step `StepCentral` takes a pending datum that its conclusion does not name. The name `StepCont` is also used in `GlobalTheory.SWLow`, at [LowRangeOfSteps.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LowRangeOfSteps.lean#L90), for a statement on CM extensions.
