---
title: The record from all rows
decls:
  - GlobalTheory.Fc.nonempty_hyps_of_allRows_alt
  - GlobalTheory.T.hTu_cTmin_of_genusMass
  - GlobalTheory.Fc.row_hTu_cTmin_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The record from all rows

This section proves step 7 of [the theorem that the record of hypotheses is nonempty](/entry/hypotheses-nonempty-of-unramified-exponents-alt/) of Section 1. Step 6 of that proof gives [the record of all rows](/entry/all-rows-of-open0-alt/) of Section 2. Here we read the fields of the record of hypotheses off these rows. The work is to choose one family class $\mathcal{A}$ and one selection $\sigma$ for all rows at the same time. One new row is needed, a size bound for the members of a family, and we prove it first from the genus mass in rank $2$.

We keep the notation of Section 1: slots $Q$, $Q'$, a linkage $\Lambda$, a property $K$ of bases, the linked statement $\mathrm{Lg}(K, Q, Q', r)$, the true slot $\top$, rows $\mathrm{Row}(Q, \Lambda, H)$ and their three facts, the class $\mathcal{D}_3(\mathcal{A})$ and [the closed bound](/step/closed-def/) $\mathrm{Closed}(\mathcal{C}, P)$ of a property $P$ along a class $\mathcal{C}$.

**Definition 8.11.1 (The size condition for members).** Let $F$ be a family. At $x$ and an index $i$ the family has a datum $D_{x,i}$ of rank $m$, size data $L_{x,i}$ with a base $b$ and a size $L$, and members $u$, each with a positive integer $T(u)$. The family carries two constants $C_{\mathrm{Tu}}(F)$ and $C_{\mathrm{YL}}(F)$. The *size condition* $\mathrm{TuSize}(F)$ says: there is $x_0$ such that for all $x \ge x_0$, all $i$ and all members $u$,

$$b^{m/2} \le T(u) \quad\text{and}\quad \log T(u) \le C_{\mathrm{Tu}}(F)\, m\, L.$$

Let $c_{\min}(y) = \max\bigl(11,\ 16 + 3\max(5, y + 1)\bigr)$. For a family class $\mathcal{A}$ let $\mathcal{A}^{\circ}$ be the subclass of families of $\mathcal{A}$ that carry a chosen datum, are smooth and have good twists. The *size statement* is

$$H_{\mathrm{Tu}}(\mathcal{A}) = \mathrm{Closed}\bigl(\mathcal{A}^{\circ},\ F \mapsto (c_{\min}(C_{\mathrm{YL}}(F)) \le C_{\mathrm{Tu}}(F) \Rightarrow \mathrm{TuSize}(F))\bigr).$$

So the lower bound for $T(u)$ is exponential in the rank, and the upper bound is linear in the rank in the logarithm, once the constant $C_{\mathrm{Tu}}$ is large compared to $C_{\mathrm{YL}}$.

**Definition 8.11.2 (Genus mass in rank $n$).** Let $D$ be a datum with CM field $E$ and let $n \ge 1$. The *genus mass in rank $n$* at $D$ says: every [[Hermitian form|8NJ7XY6F1S]] space $W$ over $E$ of rank $n$ with admissible signatures and signature $(n, 0)$ at every real place has the mass $\mathrm{mass}(W) = \mathrm{mass}_I(D, n)$. Here $\mathrm{mass}(W)$ is the mass of the base lattice of $W$ and $\mathrm{mass}_I(D, n)$ is a fixed value of the datum.

So the mass of a positive definite space depends only on the rank. This is the shape of the Siegel mass formula for the genus of a definite hermitian lattice. The *mass ratio under volume* at $D$ says: if the volume tie holds at $D$, then the volume ratio in rank at least $3$ holds at $D$. Both are statements on the volumes of the hermitian spaces of $D$ in all signatures. They come from the Siegel-Weil formula, as in Section 3.

**Proposition 8.11.3 (The size row).** Assume the mass ratio under volume at every datum and the genus mass in rank $2$ at every datum. Then for each slot $Q$ and each linkage $\Lambda$, the row $\mathrm{Row}(Q, \Lambda, (\mathcal{A}, \sigma) \mapsto H_{\mathrm{Tu}}(\mathcal{A}))$ holds.

Lean: `GlobalTheory.Fc.row_hTu_cTmin_alt` (also `GlobalTheory.T.hTu_cTmin_of_genusMass`, a second name).

*Proof.* By the first fact on rows it suffices to prove $H_{\mathrm{Tu}}(\mathcal{A})$ for every class $\mathcal{A}$ and every selection $\sigma$. Fix them. Let $F$ be in $\mathcal{A}^{\circ}$ with $c_{\min}(C_{\mathrm{YL}}(F)) \le C_{\mathrm{Tu}}(F)$. There are three steps.

1. **Volume ties.** The selection gives, at each $x$ above the threshold and each $i$, a built bundle at $D_{x,i}$. A built bundle carries a real tie, and a real tie gives the volume tie at $D_{x,i}$. So the volume tie holds along $F$.
2. **Base volume.** Let $D = D_{x,i}$. The mass ratio under volume and the volume tie give the volume ratio at $D$, and the unfolding of the volume ratio gives the volume of the base in rank $2$ by the measures of $D$. The genus mass in rank $2$ and the volume tie give the volume of a definite space of rank $2$ as its mass. Together, the volume of the base equals $\mathrm{mass}_I(D, r)$, where $r$ is the rank of $D$.
3. **The size condition.** A two sided bound for the degree of $\sigma$ in terms of the gap holds for every family, with no hypothesis. With the base volume of step 2 along $F$, the explicit constants of the family give $\mathrm{TuSize}(F)$ when $c_{\min}(C_{\mathrm{YL}}(F)) \le C_{\mathrm{Tu}}(F)$.

The bound is closed along $\mathcal{A}^{\circ}$, since it holds at every family of the class. $\square$

Now the main result. We use the inputs that step 7 of Section 1 lists. The *Siegel mass ratio for CM data* is a consequence of the Siegel-Weil formula. Four statements have no hypothesis: thin scales, the decay of a gap, finite dimensional rows and positivity at the type primes. Two more are a row bound and a main equality, both consequences of the Siegel-Weil formula. Four group conditions on $K$, $Q$ and $Q'$ (a base condition, a first and a second retwisting condition and an export condition) are assumed under the Minkowski divisor condition, and $\mathrm{ExBL}(K, Q, Q', \Lambda)$ is the existence of bundles with a large base condition.

**Theorem 8.11.4 (The record from all rows).** Assume the Siegel mass ratio for CM data, thin scales, the decay of a gap, finite dimensional rows, positivity at the type primes, the row bound, the main equality, the mass ratio under volume at every datum and the genus mass in rank $2$ at every datum. Let $K$ be a property of bases, $Q$ and $Q'$ slots, $\Lambda$ a linkage, $N$ a predicate on family classes and $\mathrm{DR}$ a definite side type. Assume:

1. the Minkowski divisor condition implies the four group conditions for $K$, $Q$ and $Q'$;
2. $\mathrm{ExBL}(K, Q, Q', \Lambda)$ holds;
3. the record of all rows holds for $K$, $Q$, $Q'$, $\Lambda$, $N$ and $\mathrm{DR}$.

Then the [record of hypotheses](/step/hyps-alt-def/) for $N$ and $\mathrm{DR}$ has an element.

Lean: `GlobalTheory.Fc.nonempty_hyps_of_allRows_alt`.

*Proof.* There are five steps.

1. **The extra rows.** The counting field of the record of all rows gives a list of counting constants $c_{30}$, a constant $c_I > 0$, a bound for $c_{30}$ and a linked row for the irreducibility count. The Proposition (The size row) gives the size row at $Q'$ and $\Lambda$. By the Remark (The true slot) of Section 1 it becomes a linked row $\mathrm{Lg}(K, Q, Q', \cdot)$, since $\mathrm{LB}(K, Q, \top)$ always holds.
2. **One row.** By the second fact on rows, linked rows at the same $K$, $Q$, $Q'$ and $\Lambda$ join by conjunction. We join $27$ rows: $25$ fields of the record of all rows, the counting row of step 1 and the size row. The joined statement is the conjunction of all the statements $H(\mathcal{A}, \sigma)$.
3. **A class and a selection.** The linked row gives a slot $R$ with $\mathrm{LB}(K, Q, R)$ and a row at $Q' \wedge R$, and the row gives a property $E$ of bundles. Let $\mathcal{A}$ be the class of the families whose bundles at points of $Q' \wedge R$ that $\Lambda$ links have $E$, and let $\sigma$ pick such a bundle. Then $H(\mathcal{A}, \sigma)$ holds for the joined statement. Each family of $\mathcal{A}$ has the seven duties and stable members. Under the Minkowski divisor condition, hypothesis 1, hypothesis 2 and the Siegel mass ratio give the existence statement for $\mathcal{A}$ with the cutoff $c_{\min}$.
4. **Working classes.** The record of hypotheses states its closed bounds on two working classes $W_1(\mathcal{A})$ and $W_3(\mathcal{A})$. A family is in $W_3(\mathcal{A})$ exactly when it is in $\mathcal{D}_3(\mathcal{A})$, and it is in $W_1(\mathcal{A})$ exactly when it is in $\mathcal{A}^{\circ}$. A closed bound along a class holds along each subclass. So the ten closed bounds of step 3 (the class count, the operator on the Hecke module, four period entry rows, the column valuations, admissibility at generator places, the second complement and the tie row) move to the classes that the record uses. The seven duties give the duty of each family.
5. **The fields.** The cutoff is $c_{\min}$. The six statements with no hypothesis or from the Siegel-Weil formula, the two mass inputs, the counting constants and the bound of step 1 enter the record as they are. The bundle conditions (the real bound, the twist, primitivity, the lambda prime, the divisor, the decomposition point and the instance row) hold at each selected bundle. For the selection jump, the row gives that a jump exists at each selected bundle, and the record takes one. The other rows enter as statements on $\mathcal{A}$ and $\sigma$. $\square$

**Remark 8.11.5 (Formalization).** The theorem is at [NonemptyHypsOfAllRows.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NonemptyHypsOfAllRows.lean#L19) and the record is `HypsAlt` in [Hyps.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Hyps.lean#L22). Step 3 is `UpperTheory.Top.classSel` ([ClassSel.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/ClassSel.lean#L14)); its fact `IsSel`, that $\sigma$ is a selection, is dropped. The selection jump is taken with `Classical.choice` from a `Nonempty` statement. Step 4 is `Closed.sub` with the equivalences of `GlobalTheory.T.workingFamClass_copies_eq_frozen`. The proposition is at [RowHTuCTmin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowHTuCTmin.lean#L11), and its second name at [RowHTuCTminStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowHTuCTminStatement.lean#L11) is a `first | exact …` wrapper. The size statement is `R1.H_hTu` at the cutoff `cTmin`, the mass ratio under volume is `MassRatioUnderVolume`, and the genus mass is `GenusMassAt D 2`. Step 2 of the proposition is `volume_eq_mass_rank_two` with `volumeMass_of_unfolding` and `volume_mass_of_genus_rank`, and step 3 is `tuSize_min` with `explicit_bound_family`. We did not unfold `VolTie`, `VolumeRatio₂` or the explicit constants. The record of all rows has the type `Lg1` in each field, and the proof reads the fields as rows by type ascription.
