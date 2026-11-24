---
title: The closing bound for a family
decls:
  - GlobalTheory.T.conclF_of_family_facts_and_bound_at_two_three
  - GlobalTheory.NLinkClose.main_alt_alt
  - GlobalTheory.T.star_ad_and_bb_le_of_joint_cond
  - GlobalTheory.NLink.rowsAD_in_setting_alt
  - GlobalTheory.T.adm_at_inert_of_range
  - GlobalTheory.NLink.InertStep.main_alt_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The closing bound for a family

This section proves the closing conclusion for a family. Step 4 of [the link inequality for one family](/entry/link-n-of-tw-good-galois-preconditions/) of Section 6 uses it for the cut family. The closing conclusion says that at each large member of the family there is hub data with fifteen local bounds and one constant. The bounds split by the range of the prime $\ell_i$ of a local index: the small primes and $3$, the ramified primes, the middle range and the large primes. We prove the bound for the middle range here, and we reduce it at the inert primes to twenty local conditions. The other ranges come from lemmas outside this chapter, and the congruence bound and the joint hub conditions come from Section 9.

Fix a datum $D$ with size data $L$, a parameter choice $P$ and a norm choice $n$. *Hub data* $X$ give, at each local index $i$, two homomorphisms $r_i$ and $\rho_i$ from a Galois group $G_E$ to matrix groups, of ranks $n_V$ and $r$, a length table, an error bound $e_X(i, \pi)$ at each point $\pi$ of $i$, and a finite excluded set of primes. Let $\ell_i$ be the prime of $i$ and $Z^{\mathrm{good}}_i$ the good points at $i$.

**Definition 8.8.1 (The local bound).** For a local index $i$, a point $\pi$ and a real number $b$, the *local bound* $\mathrm{Bd}(i, \pi, b)$ is

$$v(i, \pi) \le s(i, \rho_i, \pi) + b + V(\ell_i) + v_{\ell_i}(h_E) + \epsilon(\ell_i).$$

Here $v(i, \pi)$ is the congruence valuation at $\pi$, $s$ is the Selmer length of $\rho_i$ at $\pi$, $V(\ell_i)$ is a sum of lengths of [[Selmer group|36YNSTESMQ]]s, $h_E$ is the class number of $E$ and $\epsilon(\ell_i)$ is a small error.

A prime $\ell_i$ is *in the middle range* if it is not small, not $3$, not one of the two ramified primes $q$ and $d$, and it is not both above the cutoff $\ell^*$ and outside the excluded set. Hub data are *in setup* with a constant $C_2$ if the norm choice facts hold, $X$ has a canonical form for the row of $C_2$, the parameter bounds hold, a size number of $L$ is at least $8$, a split bound of $D$ is at least $60$, $\rho$ kills the right modules, and the Tate-Shafarevich group is finite of odd order. The *local lifting corollary* at $C_2$ is a consequence of [local lifting theorem B](/entry/local-lifting-theorem-b-of-bloch-kato-tate-duality-euler-char/). The *joint hub conditions* for a row $(C_2, 320, 25, 23, 32, 32)$ say: at each twisted inert index and each good point, a local bound or a local congruence condition holds, by the row of $\ell_i$.

**Definition 8.8.2 (Admitted).** Let $i$ be a local index and $\pi$ a point at $i$. The triple $(r_i, \rho_i, \pi)$ is *admitted* with the data of $X$ at $i$ if twenty local conditions hold. Among them are these. The characteristic polynomials of $r_x(g)$ have coefficients in the Hecke algebra $T_i$. Each $r_x$ is absolutely irreducible, and its residual characteristic polynomial is that of $\bar\rho$ times $\prod_{c=1}^{t} (X - \chi^c)$. The family $r$ is unramified outside $\ell$, $S_i$ and $Q_i$. There is an isomorphism $r(\pi) \cong \rho(\pi) \oplus \bigoplus_c \chi^{c+1}$. A tame bound holds at the places above $\ell$, a length bound holds at the row places and a lift exponent condition holds at the column places. The unramified Hom group is bounded by $v_\ell(h_E)$.

**Theorem 8.8.3 (The inert step).** Assume the published local inputs of Section 6. Let $X$ be hub data in setup with $C_2 \ge 1$, assume the local lifting corollary at $C_2$ and the joint hub conditions for the row $(C_2, 320, 25, 23, 32, 32)$. Let $i$ be a twisted local index with $\ell_i \notin \{g_0, g_1\}$, with $\ell_i$ in the middle range and with $\ell_i$ inert. Then for each $\pi \in Z^{\mathrm{good}}_i$, the triple $(r_i, \rho_i, \pi)$ is admitted.

Lean: `GlobalTheory.NLink.InertStep.main_alt_alt` (also `GlobalTheory.T.adm_at_inert_of_range`, a second name).

*Proof.* There are five steps.

1. **Seventeen conditions.** Seventeen of the twenty conditions hold at each good point of an index whose prime is not $g_0$ or $g_1$, by the setup.
2. **The tame condition.** The closing of the family gives a Wach module $M_0$ and a tame bound. With [local Bloch-Kato theory](/learn/padic-hodge/#local-bloch-kato-theory), local Tate duality and the local Euler characteristic, Wach modules turn them into the tame condition at $c_B$.
3. **A lower bound.** $\ell_i \ge 11$, since $\ell_i$ is inert and the split bound is at least $10$.
4. **The row length bound.** There are two cases. If $\ell_i$ is a prime of the second row, the long orbits of the inert localisation give the bound, with the lifting corollary. If not, the local bounds of the third and fourth rows give it, with local lifting theorem B at $320$ and [the bound with $25$](/entry/prv-twenty-five-of-bloch-kato-tate-duality-euler-char/). In both cases the input is the joint hub condition.
5. **The lift exponent condition.** At an inert prime the set of column places is empty, so the condition holds. $\square$

Now the middle range. Let $M$ be the set of twisted indices $i$ with $\ell_i \notin \{g_0, g_1\}$ and $\ell_i$ in the middle range.

**Theorem 8.8.4 (The middle range).** Assume the published local inputs. Let $X$ be hub data in setup with $C_2 \ge 1$, and assume the local lifting corollary at $C_2$ and the joint hub conditions. Then for each $i \in M$ and each $\pi \in Z^{\mathrm{good}}_i$:

$$\begin{aligned} v(i, \pi) &\le s(i, \rho_i, \pi) + \Sigma(i, \pi) + V(\ell_i) + v_{\ell_i}(h_E) + e_X(i, \pi) + \epsilon(\ell_i), \\ e_X(i, \pi) &\le 7200\, f\, n\, t^2\, n_V\, \lambda^2. \end{aligned}$$

Here $\Sigma(i, \pi)$ is a sum over the length table, $f$, $n$, $t$ and $n_V$ are numbers of $D$, and $\lambda$ is a size of $L$.

Lean: `GlobalTheory.NLink.rowsAD_in_setting_alt` (also `GlobalTheory.T.star_ad_and_bb_le_of_joint_cond`, a second name).

*Proof.* There are three steps.

1. **Step data.** At an inert prime of $M$, the Theorem (The inert step) gives the twenty conditions. At a split prime, the places over $\ell_i$ are declared, each with ramification index $1$. The good points come from the canonical form of $X$.
2. **The first inequality.** The star inequality for the middle range follows from the row data of $X$, the step data, the integrality from the metric of $D$, a bound in the split case at admitted points, the second admissibility condition at good points of the setup, the killing condition and the finiteness of the Tate-Shafarevich group.
3. **The second inequality.** The invariants of $X$ outside the split case are bounded with $c = 120$. The part of the local bound away from the places is then at most $60c$ times the size term, and $60 \cdot 120 = 7200$. $\square$

The parameter choice, the norm choice and two local data pass to the lemmas without use. The lifting corollary and the joint hub conditions enter only at the inert primes.

Now the family. A family $F$ has a threshold $x_1$, and at $x > x_1$ and $i \in I_x$ a datum $D$, size data $L$ and a parameter choice $P$. Let $\mathrm{mid}(C) = C f m b \log x + C x^C \lambda^2$ with numbers $f$, $m$, $b$ and $\lambda$ of the member.

**Definition 8.8.5 (Family facts and the bound at two and three).** Let $C \ge 0$ and $C_T \in \mathbb{N}$. The *family facts* at $C$ and $C_T$ say: for $x > x_1$, at each member, the norm choice facts hold, a commuting endomorphism condition holds and a paired character condition holds with the constants $C$ and $C_T$. The *bound at two and three* for $F$ says: there are $C_a$ and $x_a$ such that for $x \ge x_a$ and all hub data in setup, $\mathrm{Bd}(i, \pi, \mathrm{mid}(C_a))$ holds at each twisted index with $\ell_i = 2$, or with $\ell_i = 3$ not small, and at each good point $\pi$.

**Definition 8.8.6 (The closing conclusion).** The *closing conclusion* for $F$ says: there are $C_s \ge 0$ and $x_0$ such that for $x \ge x_0$ with $x > x_1$ and for each $i$ at which the Tate-Shafarevich group is finite of odd order, there is hub data $X$ with these fields.

1. Local bounds $\mathrm{Bd}$ at twisted indices and good points, by the range of $\ell_i$: at the small primes and $3$, at the ramified primes $q$ and $d$, in the middle range (the first inequality of the Theorem (The middle range)), and above the cutoff outside the excluded set with $b = 0$.
2. The error bound $e_X \le C_s f n t^2 n_V \lambda^2$, a bound at the primes $g_0$ and $g_1$, the bound of the multiplicity by the rank, few excluded primes each at most $3b$, a small bound, five bounds on the tables and a parity bound.
3. Side facts: passing, rank and killing.

**Theorem 8.8.7 (The closing conclusion).** Assume the published local inputs. Let $F$ be a family with good twists eventually, let $C \ge 0$ and $C_T \in \mathbb{N}$. Assume the family facts at $C$ and $C_T$ and the bound at two and three for $F$. Then the closing conclusion holds for $F$.

Lean: `GlobalTheory.NLinkClose.main_alt_alt` (also `GlobalTheory.T.conclF_of_family_facts_and_bound_at_two_three`, a second name).

*Proof.* There are three steps.

1. **Constants.** The closing of all data gives $C_0$ such that the second conclusion holds at $D$ for each $C_2 \ge C_0$. Put $C_2 = \max(C_0, 1)$. [The polynomial bound](/entry/embedding-jumps-aux2-of-setup/) of Section 9 gives a constant and a polynomial. The admissible parameters of a family give $C_1$. The bound at two and three gives $C_a$, and the star bound at the other small primes gives $C_b$. Put

$$C_s = \max\bigl(\dots, 3C_2 + 1, 2000(C + 1) + 5C_1, C_T, 22365\bigr).$$

2. **Thresholds.** Hub data in setup exist past a threshold. Past further thresholds, the excluded primes are few and small, the special primes are small, [the congruence bound](/entry/eventually-cong-bound-of-facts/) of Section 9 holds, and the [joint hub conditions](/entry/fam-joint-bcd-closed-alt/) of Section 9 hold.
3. **Fields.** The middle range and the error bound with $7200$ are the Theorem (The middle range). The bound at small primes comes from the bound at two and three and $C_b$. The bound at $g_0$ and $g_1$ comes from the paired character condition. The bound above the cutoff comes from the congruence bound. The bound at the ramified primes comes from the second theorem of local lifting. The multiplicity bound is the bound of a good point by the rank. The five table bounds come from the first row and three lemmas on tables. Then all constants increase to $C_s$, since the size conditions are monotone. $\square$

The constant $22365 = 3 \cdot 23 \cdot 320 + 12 \cdot 23 + 9$ is the third constant of the row of $C_2$, and the bound on the rows needs it.

**Remark 8.8.8 (Formalization).** The closing conclusion is `ConclF` with fields `two`, `ram`, `mid`, `large`, `bb`, `typ`, `mult`, `exc`, `small`, `num` and `par`, in [BoundAtTwoThreeFamily.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/BoundAtTwoThreeFamily.lean#L120); the theorem is at [ImportsFurtherTail.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherTail.lean#L22). There the local name `ComplexParameterFamilyContinuity` at [line 30](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherTail.lean#L30) is only the real number $\max(0, C_a, C_b)$. The middle range is at [RowsADInSetting.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowsADInSetting.lean#L15), with the inequalities `StarAD` and `BBLe`, and the inert step at [ImportsFurtherBis.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherBis.lean#L15); "admitted" is `TruncatedSeriesCountingIdentities.admitted`. All three second names are `first | exact … | …` tactics in files named `…Statement.lean`. In the inert step, the seventeen conditions come from `set_pt_of_setup_not_twisted`, whose name says "not twisted" although it is applied at a twisted index; $\ell_i \ge 11$ is `eleven_le` in [InertPlacesGoodSet.lean](lean:Development/AbelianVarietyTheory/Counterexamples/HeckeCharacterExamples/InertPlacesGoodSet.lean#L22), in a folder named `Counterexamples` although it is not a counterexample; and `LiftExponentAtPlaces` is vacuous at [line 46](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherBis.lean#L46). The only caller of the closing conclusion proves the bound at two and three with `at23_family_alt`, so that hypothesis is never an input from outside.
