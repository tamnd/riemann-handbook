---
title: The mass of a genus of local data
decls:
  - GlobalTheory.Unfold.SumK.weights_add_up_to_mass_of
  - GlobalTheory.Unfold.SumK.weights_add_up_to_mass
  - GlobalTheory.T.unfolding_genus_weights_sum_to_mass
  - GlobalTheory.Unfold.GenusRows.rows_mass_genus
  - GlobalTheory.T.rowWeights_localOrbits_sum_eq_genusMass
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The mass of a genus of local data

This section proves the mass identity: the sum of the squared weights of the terms whose local data lie in one genus is the mass of the genus. The mass is a sum over rational classes of families of local data, each counted with the inverse order of its stabilizer. This is the analogue, for the terms of the double coset sum, of the Siegel mass formula, which writes the mass of a genus of lattices as a sum of inverse orders of automorphism groups. We first prove the identity for the set of keys of the terms, and then in the form used by the families of classes and double cosets of [Section 2.12.4](/entry/family-group-sum-factors-row-weight-amplitude/). The second form is used in the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/).

We keep the [standing assumptions](/entry/gdat-eq-iff/), the [rational classes](/entry/rat-cls-agree/) $\approx$ of families of local data, and the [terms over a lattice](/entry/orbit-count/) with their keys and weights.

**Definition 2.15.1 (Genus of local data).** Two local data $d_p$ and $y_p$ at $p$ are *locally related* if an element of the local unitary group of the reduced space moves $d_p$ to $y_p$. A family $y$ lies in the *genus* of a family $d$ if $y_p$ is locally related to $d_p$ at every $p$, and $y_p = d_p$ for all but finitely many $p$.

**Definition 2.15.2 (Mass of a genus).** For each rational class $o$ of families of local data fix a representative $y_o$. The *mass* of the genus of $d$ is
$$m(d) = \sum_{o} \frac{\mathbf{1}[y_o \text{ lies in the genus of } d]}{\#\operatorname{Stab}(y_o)} \in [0, \infty],$$
where the sum runs over all rational classes and $1/\infty = 0$.

The mass counts each rational class in the genus once, with the inverse order of its stabilizer. This is the usual weighting of a mass formula: a class with more symmetries counts less.

**Definition 2.15.3 (Closed under local moves).** A set $T_S$ of terms is *closed under local moves* if the following holds. Let $t$ lie over $\Lambda$ and $t'$ lie over $\Lambda'$. If at every $p$ some element of the local unitary group of the reduced space moves $\Lambda_p$ to $\Lambda'_p$, and $t \in T_S$, then $t' \in T_S$.

**Theorem 2.15.4 (Weights add up to the mass).** Assume:

1. at every place, local relation of data is an equivalence relation;
2. under the standing assumptions, the genus is stable under rational relation: if $\Lambda$ lies over $y$, $y$ lies in the genus of $d$, and $y \approx y'$, then $y'$ lies in the genus of $d$.

Then the following holds under the standing assumptions. Let $T_S$ be closed under local moves. Let $t_0 \in T_S$ lie over $\Lambda_0$, let $\Lambda_0$ lie over $y_0$, and let $y_0$ lie in the genus of $d$. Let $K$ be the set of keys of the terms $t \in T_S$ that lie over some lattice $\Lambda$ that lies over some family $y$ in the genus of $d$. Let $\omega \colon K \to \mathbb{R}$ satisfy $\omega(\kappa) = \mathrm{wt}(t)^2$ for every term $t$ with key $\kappa$. Then
$$\sum_{\kappa \in K} \omega(\kappa) = m(d)$$
in $[0, \infty]$.

Lean: `GlobalTheory.Unfold.SumK.weights_add_up_to_mass_of`.

*Proof.* Map each key $\kappa \in K$ to a rational class: choose a term $t$ with key $\kappa$, a lattice $\Lambda$ under it and a family $y$ under $\Lambda$, and take the class of $y$. By the [Theorem on rational classes](/entry/rat-cls-agree/), this class does not depend on the choices: two lattices under terms with one key are rationally related, and rational relation of lattices is rational relation of the families over them. Sum over the fibres of this map. It remains to show that the fibre over a class $o$ has sum $\mathbf{1}[y_o \in \text{genus}]/\#\operatorname{Stab}(y_o)$.

If the fibre is not empty, $y_o$ is rationally related to a family in the genus, so by assumption (2) it lies in the genus. So a class outside the genus has an empty fibre and contributes $0$ on both sides. Now let $y_o$ lie in the genus of $d$. By assumption (1), lying in the genus of $d$ is symmetric and transitive, so $y_o$ lies in the genus of $y_0$. Then $y_o$ and $y_0$ differ only at finitely many places, and at those places by local unitary moves. Glue: the lattice $\Lambda_0$ changed at these places by the local moves is a lattice $\Lambda_1$ over $y_o$. By the [Theorem on glued lattices](/entry/exists-term-of-loc-over/), some term $t_1$ lies over $\Lambda_1$. It lies in $T_S$, because $T_S$ is closed under local moves and $t_0 \in T_S$. Now apply the [orbit count](/entry/orbit-count/) to $t_1$ and $\Lambda_1$. The fibre over $o$ is the key set of the rational class of $\Lambda_1$, every key has weight $\mathrm{wt}(t_1)$, and
$$\sum_{\kappa \in \text{fibre}} \omega(\kappa) = \#K_o\, \mathrm{wt}(t_1)^2 = \frac{1}{\#\operatorname{Stab}(\Lambda_1)} = \frac{1}{\#\operatorname{Stab}(y_o)}.$$
The last equality is the equality of stabilizers in the [Theorem on rational classes](/entry/rat-cls-agree/), together with the invariance of the stabilizer order on a class. $\square$

**Corollary 2.15.5 (Weights add up to the mass, unconditional form).** Under the standing assumptions, the conclusion of the Theorem holds with no further assumption.

Lean: `GlobalTheory.Unfold.SumK.weights_add_up_to_mass` (also `GlobalTheory.T.unfolding_genus_weights_sum_to_mass`, a second name).

*Proof.* Both assumptions of the Theorem hold. Local relation is an equivalence relation, because it is given by an action of the local unitary group of the reduced space on local data. The genus is stable under rational relation. Let $\eta \in H_0(F, F')$ move $y$ to $y'$. At each place the extension of $\eta$ lies in the local unitary group, so $y'_p$ is locally related to $y_p$, hence to $d_p$. The lattice $\eta\Lambda$ lies over $y'$, and by the local-global principle for Hermitian lattices, $\eta\Lambda$ and $\Lambda$ agree at all but finitely many places. Over equal local lattices the local data are equal, so $y'_p = y_p = d_p$ at all but finitely many places. $\square$

### Families of classes and double cosets

The double coset sum is organized by classes $c$ of terms and rational double cosets $\nu$. A *local family* consists of a finite set $P$ of places, at each place $p$ a local frame pair, a set of representatives of the local data, a base datum $d_{0,p}$, a finite set $D_p$ of data, a weight $\mathrm{rw}(c) \in \mathbb{R}$ for each class, and a partial map
$$\mathrm{dat}(c, \nu) \in \textstyle\prod_{p \in P} D_p \cup \{\text{none}\}.$$
A term $t$ lies *over the orbit* of a datum $d$ at $p$ if a local unitary map $g$ moves the local term of $t$ at $p$ to a term over a datum locally related to $d$. A class map $\mathrm{cls}$ on a set $T_S$ of terms *separates rows* if, for $t, t' \in T_S$ in the same double coset, $\mathrm{cls}(t) = \mathrm{cls}(t')$ holds if and only if $t$ and $t'$ have the same row.

**Theorem 2.15.6 (Row weights and the mass of the genus).** Under the standing assumptions, let $T_S$ be a set of terms, $\mathrm{cls}$ a class map and a local family as above whose frame pairs are based on $(F, F')$. Assume:

1. $\mathrm{cls}$ separates rows on $T_S$, and $T_S$ is closed under local moves;
2. for $p \in P$, every datum in $D_p$ is one of the representatives;
3. for $p \notin P$, every $t \in T_S$ with point $w$ lies over the orbit of $d_{0,p}$ at $p$;
4. some lattice $\Lambda_0$ has, at every $p \notin P$, a local term over $d_{0,p}$ with lattice $\Lambda_{0,p}$;
5. for every $(c, \nu)$: if $\mathrm{dat}(c, \nu)$ is none, no $t \in T_S$ with point $w$ has class $c$ and double coset $\nu$; if $\mathrm{dat}(c, \nu) = \delta$, some $t \in T_S$ with point $w$ has class $c$ and double coset $\nu$, and every such $t$ lies over the orbit of $\delta_p$ at each $p \in P$ and has $\mathrm{rw}(c) = \mathrm{wt}(t)^2$.

Let $\delta \in \prod_{p \in P} D_p$ be a value of $\mathrm{dat}$, and let $y$ be the family with $y_p = \delta_p$ for $p \in P$ and $y_p = d_{0,p}$ for $p \notin P$. Then every $y_p$ has a local term over it, and
$$\sum_{(c, \nu) :\, \mathrm{dat}(c, \nu) = \delta} \mathrm{rw}(c) = m(y).$$

Lean: `GlobalTheory.Unfold.GenusRows.rows_mass_genus` (also `GlobalTheory.T.rowWeights_localOrbits_sum_eq_genusMass`, a second name).

*Proof.* Local relation is symmetric and transitive, and two representatives that are locally related are equal; all three facts come from the action of the local unitary group on local inner data. Pick $(c, \nu)$ with $\mathrm{dat}(c, \nu) = \delta$ and a term $t_0 \in T_S$ of class $c$ and double coset $\nu$. Move $t_0$ to the base frames: there is a lattice $\Lambda$ under $t_0$, and its local data at each place are determined by the lattice and the orbits. At $p \in P$ the local datum is locally related to $\delta_p$, by (5). At $p \notin P$ it is locally related to $d_{0,p}$, by (3). By the local-global principle for Hermitian lattices, the lattice $\Lambda$ and $\Lambda_0$ of (4) agree at all but finitely many places, and at such places equal lattices have equal data. So the family $y_0$ of local data of $\Lambda$ lies in the genus of $y$. This also shows that each $y_p$ has a local term over it.

Now compare the index sets. Send a pair $(c, \nu)$ with $\mathrm{dat}(c, \nu) = \delta$ to the key $(\operatorname{row}(t), \nu)$ of any term $t$ of class $c$ and double coset $\nu$. Since $\mathrm{cls}$ separates rows, this does not depend on $t$, and the map is injective. Its image is the key set $K$ of the [Corollary 2.15.5](/entry/weights-add-up-to-mass/) for the genus of $y$: a term over a lattice over a family in the genus has local data in the orbits of $\delta_p$ and $d_{0,p}$, so its pair $(\mathrm{cls}(t), \nu(t))$ has $\mathrm{dat} = \delta$. Under this bijection $\mathrm{rw}(c) = \mathrm{wt}(t)^2$. The sum is therefore $\sum_{\kappa \in K} \mathrm{wt}^2$, which is $m(y)$ by the Corollary. $\square$

**Remark 2.15.7 (Formalization).** The mass is `massA`, a `tsum` over `Quot GRel` with the representative `o.out` ([LocClosed.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/LocClosed.lean#L79)). The genus test is applied to `o.out`, so it depends on the choice of representative unless the genus is stable under rational relation; this is why the Theorem has assumption (2). The conditional form takes its two assumptions as hypotheses `hRelEqv` and `hInv`, and the unconditional form discharges them ([UnfoldingGenusWeightsSumToMass.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/UnfoldingGenusWeightsSumToMass.lean#L28)). In both forms the point $w$ and the hypotheses on the Gram matrix are only passed on. The file of the last theorem proves symmetry and transitivity of local relation again (`rel_symm`, `rel_trans`), although the equivalence is available as a lemma.
