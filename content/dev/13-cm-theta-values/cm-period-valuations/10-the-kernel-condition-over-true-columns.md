---
title: The kernel condition over true columns
decls:
  - GlobalTheory.ThLoc.locJets_all
  - GlobalTheory.ThLoc.inputs_of_algT
  - GlobalTheory.T.normalisedThetaCMCurveTheorems_of_algebraicTranslates
  - GlobalTheory.PdvClose.at_of_true_columns
  - GlobalTheory.PdvTie.at_of_stdTie
  - GlobalTheory.T.kernelDatumConditions_at_standardKernelComparison
  - GlobalTheory.Pdv.rowAt_of_stdTie
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The kernel condition over true columns

This section proves the second half of the service row of Section 6: the *kernel row of a standard tie*. It says that if the kernel entries of the selected bundles are standard ties in a row, then the kernel condition holds for every selected bundle in a row. The kernel condition has ten parts. Section 8 gave the filtration, and Section 9 gave the orbit bound and the even conditions. Here we collect the other parts and the local facts about CM curves that they need. The result is used in [the service row](/entry/serv-h-row/).

Throughout the section we assume four of the six hypotheses of Section 6: algebraic torsion, genus one models, the curve dictionary and inert integrality.

### The kernel condition

Let $\mathrm{ex}$ be extra data over $D$ with twist $\tau$, and let $E$ be a kernel entry for $\mathrm{ex}$. For numbers $\varepsilon$, series $\beta$ and signs $s_g$ at the places, $E$ gives an entry of orbit data $E(\varepsilon, \beta, s_g)$, with the rows of diagrams of $D$ (Section 9).

**Definition 5.10.1 (Kernel condition).** The pair $(\mathrm{ex}, E)$ satisfies the *kernel condition* if:
1. the pair scalars of $E$ are units;
2. the kernel map of $E$ is rational;
3. $(D, \tau)$ satisfies the filtration condition of Section 8;
4. $D$ has trivial stabilizers at step $0$: every class at step $0$ of the member chain, and of the twisted chain of every used tuple, has a stabilizer with one element;
5. there are $\varepsilon$, $\beta$ and $s_g$ such that $E(\varepsilon, \beta, s_g)$ satisfies the even conditions at inert primes, the even conditions of Section 9, the orbit bound of Section 9, jet integrality, the theta kernel shape at the discriminant, and the shape condition.

### Inputs from CM curves

A lattice $L \subset \mathbb{C}$ *has CM by* $d$ if $\omega_d L \subseteq L$, where $\omega_d = (1 + i\sqrt{d})/2$. For a lattice $L$ we write $j(L) = 1728\, g_2^3 / (g_2^3 - 27 g_3^2)$. The following theorem is classical.

**Theorem 5.10.2 (Integrality of singular moduli).** Let $E$ be an elliptic curve over $\mathbb{C}$ with complex multiplication. Then $j(E)$ is an algebraic integer. (J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Chapter II, Theorem 6.1.)

**Theorem 5.10.3 (Local jets).** The following hold.
1. For an odd prime $p$ prime to $d$, the jets of the linear theta series of a CM lattice are integral at $p$, under good reduction and the normalization of the fourth power of $\theta$.
2. The same holds at $p = 2$, for a Weierstrass model that uniformizes the lattice.
3. If embeddings of $E$ into $\mathbb{C}_p$ that agree modulo the maximal ideal are separated, then at a prime $p$ dividing the discriminant the theta series has the eigenframe shape: it is $\exp(-c\beta)\, s$ with $s$ of integral jets, $|c| \le |d|^{-1/2}$ and $\beta$ a quadratic series.

Lean: `GlobalTheory.ThLoc.locJets_all`

*Proof.* The three parts are three theorems on CM theta series: the odd case, [the case $p = 2$](/entry/jets-two/), and the eigenframe shape. $\square$

**Theorem 5.10.4 (CM curve inputs).** Assume algebraic torsion. Then the following eight statements hold.
1. If $d$ is squarefree, $d \equiv 3 \pmod 4$ and $L$ has CM by $d$, then $j(L)$ is integral over $\mathbb{Z}$.
2. If $d$ is squarefree, $d \equiv 7 \pmod 8$, $L$ has CM by $d$ and $\iota \colon \mathbb{C} \to \mathbb{C}_2$ is a field isomorphism, then there are $c \ne 0$ and a Weierstrass curve $W$ over $\mathbb{C}_2$ that uniformizes $cL$ through $\iota$, has integral coefficients and unit discriminant, and has $|a_1(W)| = 1$.
3. to 5. The three parts of the theorem on local jets.
6. If $d \equiv 7 \pmod 8$, $d \equiv 2 \pmod 3$ and $L$ has CM by $d$, then for every isomorphism $\iota \colon \mathbb{C} \to \mathbb{C}_3$ and every integral Weierstrass curve $W$ that uniformizes $L$, the theta series of $L$ at $3$ has integral jets.
7. Algebraic torsion.
8. Every embedding $\lambda \colon \overline{\mathbb{Q}} \to \mathbb{C}_p$ extends to a field isomorphism $\mathbb{C} \to \mathbb{C}_p$.

Lean: `GlobalTheory.ThLoc.inputs_of_algT` (also `GlobalTheory.T.normalisedThetaCMCurveTheorems_of_algebraicTranslates`, a second name)

*Proof.* Statement 1 is the integrality of singular moduli: one writes $L = a(\mathbb{Z} + \mathbb{Z}\tau)$ and applies the integrality of the modular invariant $j(\tau)$ at a CM point. Statement 2 is a theorem on good models at $2$. The conditions $|a_1| = 1$ and $|\Delta| = 1$ say that $W$ has good ordinary reduction. Statements 3 to 5 are the theorem on local jets. Statement 6 is a theorem on theta jets at $3$. Statement 7 is the hypothesis. Statement 8 is a lemma on field isomorphisms $\mathbb{C} \to \mathbb{C}_p$ that extend a given embedding of $\overline{\mathbb{Q}}$. $\square$

### Entries over true columns

Let $I$ be a true-column datum (Section 1). The datum is *column normal* if its column data are normalized; this holds when $I$ is a twisted datum. A tied kernel entry $t$ is a *$C$-entry* if its entry is the entry built from place data $P$, a place matrix family $B$ and a hypothesis on them. It has *adapted bases* if at every admissible place there are bases with the conjugation property in which the series of $t$ are the standard series. It is *top pinned* if its top reads are pinned.

**Theorem 5.10.5 (Kernel condition over true columns).** Let $I$ be a true-column datum over a base $B$ that is in order and has pins. Fix laws $l$, a later stage $Z$, a law $l_0$ at step $0$, extra data $\mathrm{ex}$ over $D = D(l, Z)$ with constants $\delta_1, \delta_2$ and size data with scale $a$, and a tied kernel entry $t$ for $\mathrm{ex}$. Assume:
1. $I$ is column normal and its jets are in place;
2. the twist of $\mathrm{ex}$ is $\tau_I(l, l_0, Z)$;
3. $t$ is the standard kernel at $(l, Z)$, a $C$-entry, has adapted bases and is top pinned;
4. the split bound of $B$ is at least $3$, $\delta_1 \ge 5$ and $\delta_2 \ge 4$;
5. every entry of orbit data for $D$ has the shape, and its row differences satisfy $\nu(0) - \nu(1) \le 2a$ at every word, every $j < m$ and every $s \in T$.

Then $(\mathrm{ex}, t)$ satisfies the kernel condition.

Lean: `GlobalTheory.PdvClose.at_of_true_columns`

*Proof.* First we collect the facts about $t$. A lemma on the standard kernel over true columns gives the *duties* of $t$: the column side conditions of Section 8, the $C$-entry property, a rank fact, and a second entry $t'$ with the column side conditions and pinned forms. The column side conditions and the top pin give the kernel hypotheses of $t$. The CM curve inputs hold by the previous theorem. Genus one models, the curve dictionary and inert integrality give the host hypothesis of Section 9. A lemma on admissible kernel series at inert primes, where the Frobenius is not conjugate, gives $\varepsilon$ and $\beta$ that form a standard family and satisfy the even conditions at inert primes with all signs $s_g = -1$.

Now we check the parts of the kernel condition. The pair scalars are units by a lemma on true columns, from the standard kernel. The kernel map is rational, from the $C$-entry and the rank fact. The filtration condition is [the theorem on filtration from pinned forms](/entry/k-fi-of-tie/), applied to $t'$; this is enough, since the filtration condition depends only on $(D, \tau)$. The stabilizers at step $0$ are trivial by a lemma on the level data of $I$. For part 5 we take $\varepsilon$, $\beta$ and $s_g = -1$. The even conditions at inert primes come from the choice of $\varepsilon$ and $\beta$. The even conditions are [the theorem on adapted entries](/entry/frobenius-conjugation-conditions-adapted-kernel-datum-alt/). The orbit bound is [the orbit bound for standard series](/entry/orbit-bound-rec/), with hypothesis 5 and the bounds on $\delta_1$ and $\delta_2$. Jet integrality and the theta kernel shape at the discriminant follow from the CM curve inputs and the kernel hypotheses, with the split bound and the adapted bases. The shape is hypothesis 5. $\square$

**Definition 5.10.6 (Standard tie).** Let $O$ be an object over $D$ and $t$ a tied kernel entry for $\mathrm{ex}(O)$. The triple $(D, O, t)$ is a *standard tie* if there are a base $B$, a true-column datum $I$ over $B$, laws $l$, $l_0$ and a later stage $Z$ such that $(D, O, t) = (D(l, Z), O', t')$ for an object $O'$ and an entry $t'$ with the following: $I$ is in order, has pins, is twisted and has its jets; the twist of $\mathrm{ex}(O')$ is $\tau_I(l, l_0, Z)$; and $t'$ is the standard kernel, a $C$-entry, has adapted bases and is top pinned.

**Theorem 5.10.7 (Kernel condition for a standard tie).** Let $(D, O, t)$ be a standard tie. Assume that the split bound of $D$ is at least $3$, that $\delta_1 \ge 5$ and $\delta_2 \ge 4$ for the constants of $O$, and that hypothesis 5 of the previous theorem holds for the size data of $O$. Then $(\mathrm{ex}(O), t)$ satisfies the kernel condition.

Lean: `GlobalTheory.PdvTie.at_of_stdTie` (also `GlobalTheory.T.kernelDatumConditions_at_standardKernelComparison`, a second name)

*Proof.* By the equality in the definition we may assume $D = D(l, Z)$, $O = O'$ and $t = t'$. A twisted true-column datum is column normal. Then this is the previous theorem applied to $I$, $l$, $Z$, $l_0$, $\mathrm{ex}(O)$ and $t$. $\square$

### The kernel row

**Theorem 5.10.8 (Kernel row of a standard tie).** Let $Q$ be a slot, $\mathrm{Lk}$ a linkage and $\mathrm{ker}$ a kernel assignment. Assume that the property "$(D, O, \mathrm{ker}(b))$ is a standard tie" satisfies the row condition. Then the property "every selected bundle $b \in \mathrm{Bd}(D, O, c)$ satisfies the kernel condition for $(\mathrm{ex}(O), \mathrm{ker}(b))$" holds in a row for $(Q, \mathrm{Lk})$.

Lean: `GlobalTheory.Pdv.rowAt_of_stdTie`

*Proof.* A uniformity lemma on shapes says: for every $\varepsilon$ there is $x_0(\varepsilon)$ such that for every family at scale $\varepsilon$, every $x \ge x_0(\varepsilon)$ beyond the start of the family and every index $i$, every entry of orbit data for the datum at $(x, i)$ has the shape and the row differences at most $2a$, and the split bound of the datum is at least $3$.

Let $E(\kappa, D, O, c, b)$ say that $x_0(\varepsilon_\kappa)$ is at most the scale of $O$ and that $(D, O, \mathrm{ker}(b))$ is a standard tie. The first part satisfies the row condition for every parameter: the scale of the object of a constructed point is the scale of its context, and we take the threshold $x_0(\varepsilon_\kappa)$. The second part satisfies the row condition by hypothesis, and two row conditions combine.

Let $\sigma$ be a selection along $E$. Take a family at scale $\varepsilon$, a scale $x$ beyond its start and an index $i$. The parameter $\kappa$ of the family has $\varepsilon_\kappa = \varepsilon$, and the object of the family at $(x, i)$ has scale $x$. So $x_0(\varepsilon) \le x$, and the uniformity lemma applies. It gives hypothesis 5 and the split bound. The constants of the family are fixed with $\delta_1 = 5$ and $\delta_2 = 4$. The selected entry is a standard tie. The previous theorem gives the kernel condition. $\square$

**Remark 5.10.9 (Formalization).** Several facts about the Lean code:
1. `GlobalTheory.T.normalisedThetaCMCurveTheorems_of_algebraicTranslates` and `GlobalTheory.T.kernelDatumConditions_at_standardKernelComparison` are second names, proved by `first | exact @… | …` under `maxHeartbeats 1000000`. The file name NormalisedThetaCMCurveTheoremsOfAlgebraicTransla.lean is cut short.
2. In `GlobalTheory.ThLoc.inputs_of_algT` the hypothesis is only copied into the field `algT` (NormalisedThetaCMCurveTheoremsOfAlgebraicTransla.lean:18). So the inputs are equivalent to algebraic torsion. Statement 1 is `cm1`, which does not use that $d$ is squarefree (JInvNormLeOne.lean:11). Statement 5 is an implication from `EmbSep`, which is not proved here. The theta series `thetaLin` and `thetaZ`, and the predicates `Unif`, `EmbSep`, `IntOpLoc`, `IntOpTwoLoc` and `ShapeEigenLoc`, are not unfolded here.
3. In the kernel condition `GlobalTheory.Pdv.At` (IsEntC.lean:19) the parts `UnUnit`, `KmapRat`, `EvenConditionsInert`, `JetIntegralityBis`, `ThetaKernelShapeAtD` and `Shape` are not unfolded here. The properties `Adapted` and `TopPinned` of a tied entry are not unfolded either.
4. Hypothesis 5 quantifies over every entry `Ee` of orbit data, so it is a condition on the datum and the size data, not on the entry of $t$. In `GlobalTheory.Pdv.rowAt_of_stdTie` the split bound is read off for one entry with zero data, `OrbitPlaces.ofKer … (fun _ => 0) (fun _ _ => 0) (fun _ _ => 0)` (RowAtOfStdTie.lean:34), and $\delta_1, \delta_2$ come from `Fm.fixed`.
5. In `GlobalTheory.PdvClose.at_of_true_columns` the split bound is asked for the host of the base $B$, while the kernel condition is about $D(l, Z)$. The filtration part is proved for the second entry $t'$ of the duties, not for $t$.
