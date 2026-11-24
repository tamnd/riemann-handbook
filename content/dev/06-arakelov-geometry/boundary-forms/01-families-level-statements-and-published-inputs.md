---
title: Families, level statements and the published inputs
decls:
  - GlobalTheory.CovTop.PublishedHodgeBundleTheorems.toClassicalTheorems
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Families, level statements and the published inputs

The estimates of this chapter are uniform: they hold for every family of unitary Shimura data that satisfies the family conditions, for all large values of the parameter $x$, at every point of the family and at every level of the tower of that point. This section fixes the language for such statements. It defines closed statements, statements at all points, level statements and cover statements, and it names the conditions that later sections prove. It ends with the first result of the chapter: the published results on the Hodge bundle give the list of classical inputs, with Mumford proportionality in place of the good Chern-Weil theorem. The covolume bound of the last section of this part is a closed statement in this sense. It is the statement of [the covolume bound step](/step/covolume-bound-of-x-def/).

We do not repeat the construction of a family. A family $\mathcal{F}$ has a threshold $x_1$, a number $m \ge 1$ of levels, a rank $k$, and, for each $x > x_1$ and each index $\iota$, a set of points $p$. A point $p$ carries a tower of uniformizations $U_0, U_1, \dots, U_m$ over a CM field $E$ with a unitary datum of signature $(p, q)$ (we use the letter $p$ for both when no confusion is possible). At each level $i$ there are covers $Y$ of the tower, with the components $Z$ of their moduli spaces. For each $x$ and $\iota$ the family gives a parameter $P = P(x, \iota) \ge 0$, the size parameter. A point satisfies a row condition, which we write $\mathrm{Rows}(p)$; a cover satisfies a goodness condition. We do not unfold these conditions. The family conditions $\mathrm{Fam}$, a long conjunction of conditions on $\mathcal{F}$, are also not unfolded.

**Definition 2.1.1 (Closed statement).** Let $\mathcal{C}$ be a condition on families and let $\Phi(\mathcal{F}, \chi)$ be a statement about a family $\mathcal{F}$ and a choice $\chi$ of auxiliary data. We say that $\Phi$ is *closed under* $\mathcal{C}$ if there is $\varepsilon_1 > 0$ such that for every $\varepsilon \in (0, \varepsilon_1]$ there is a transported constant $K$ with the following property: for all $\mathcal{F}$ and $\chi$ such that $\mathcal{C}(\mathcal{F})$ holds and $\mathcal{F}$ is large with respect to $K$ and $\chi$, the statement $\Phi(\mathcal{F}, \chi)$ holds.

So a closed statement is a statement about all families that are large enough, where "large enough" is measured by a constant that may depend on a small number $\varepsilon$. In this chapter $\mathcal{C}$ is always the family condition $\mathrm{Fam}$.

**Definition 2.1.2 (At all points, eventually).** Let $Q$ be a statement about points of $\mathcal{F}$. We say that $Q$ holds *eventually at all points* of $\mathcal{F}$ if there is $x_0$ such that for every $x > x_1$ with $x \ge x_0$, every index $\iota$ and every point $p$ of $\mathcal{F}$ at $(x, \iota)$ with $\mathrm{Rows}(p)$, the statement $Q(p)$ holds.

Most results of this chapter have the following two forms. Let $Q(p, i, P, C)$ be a statement about a point $p$, a level $i$, the size parameter $P$ and a constant $C$.

**Definition 2.1.3 (Level statement and cover statement).** The *level statement* of $Q$ is the closed statement under $\mathrm{Fam}$ of
$$\exists\, C \ge 0 :\ \text{eventually at all points } p,\ \forall i,\ Q(p, i, P(x, \iota), C).$$
Let $R(p, i, Y, P, C)$ be a statement about a point, a level $i$, a cover $Y$ of level $i$, the parameter $P$ and a constant $C$. The *cover statement* of $R$ is the closed statement under $\mathrm{Fam}$ of
$$\exists\, C \ge 0 :\ \text{eventually at all points } p,\ \forall i \text{ with } i + 1 < m,\ \forall Y \text{ good},\ R(p, i, Y, P, C).$$

So the constant $C$ is uniform in the point, the level and the cover. The level statements concern all levels, and the cover statements concern the levels below the last one. At the last level $i = m - 1$ there are no covers, and we work with the core lattice of the tower instead.

Each point and level come with a few numbers. The *unit of error* $E = E(p) \ge 0$ is a real number attached to $p$. Under the weight numerics of a later section it is $E = f\,m\,b\,L \log\log x$, where $f$, $b$ and $L$ are numbers of the datum. The *main term* $T_i = T_i(p)$ is a real number attached to the level $i$. The *length* is
$$T = \Bigl\lceil \frac{P^2\, d^2\, k}{m} \Bigr\rceil,$$
where $d$ is the dimension of the flag space of the datum at level $i + 1$. The quantities
$$\zeta = 7\Bigl(\frac{d^2}{T} + d\,\rho_B\Bigr), \qquad b_T = \binom{T - 1}{d}$$
occur in many of the bounds, where $\rho_B \in [0, 1)$ is a ratio of weights that we define where it is used.

The estimates of the chapter are named as follows. Each is a level statement or a cover statement of a pointwise condition, and each pointwise condition is stated in the section that proves or uses it.

- *Gram*: a level statement that the lattices of the level have a Gram matrix, are finitely generated, and that the weight lattice at level $i + 1$ is good.
- *Anchor*: a level statement that $T_i$ is within $C E$ of an anchored sum $\sum_\tau (p - q)\, a_\tau \log \Omega$, where the $a_\tau$ are anchor weights and $\log \Omega$ is a logarithmic period, together with two bounds of the same kind.
- *Size*: a level statement with $1 \le b \le E \le x^A b$, $|T_i| \le x^A b$, $|T_i| \le P \kappa$ and $b \le P \kappa$, where $\kappa$ is a size of the weights; below the last level it also says that quotient weights $u_1$ exist and that each of them has $3d + 5 \le T$, $0 \le \rho_B(u_1) < 1$ and $\zeta < 1$.
- *Deep goodness*: a cover statement that the cover is good for the four weights that we use, that the relevant rank is positive, and that the moduli space has finitely many components and at least one.
- *Flat degree*: a cover statement about the degree of flat sections on the components.
- *Cover degree* and *share*: cover statements about the degrees and the ranks of the twisted bundles, for each quotient weight $u_1$.
- *Height* and *cover height sum*: cover statements that bound heights of cusp form lattices from below, for each quotient weight $u_1$.
- *Low defect*: at the last level $i + 1 = m$, $-T_i - C E \le \mu$, where $\mu$ is the slope of the core lattice.

The final statement of this part is the following.

**Definition 2.1.4 (Covolume bound of $X$).** The *covolume bound of $X$* is the closed statement under $\mathrm{Fam}$ of: there is $C_0 \ge 0$ such that eventually at all points $p$, for every $C \ge C_0$, the inequality $L_3$ holds for the lattice system $S(p)$ of $p$ (taken with the boolean flag false) at the stage $N(C, \chi)$.

We do not unfold the inequality $L_3$ or the stages $N(C, \chi)$. The covolume bound is the target of [the covolume bound step](/step/covolume-bound-of-x-def/).

The arithmetic geometry of the chapter rests on published results. Many of them are collected in one list, the published Hodge bundle theorems, which is the input of [the published results step](/step/published-results-arithmetic/). The list has 28 statements: results on toroidal compactifications, arithmetic volumes and intersection theory, de Rham cohomology of abelian schemes, class field theory, semistable reduction, strong approximation for $\mathrm{SU}$, hermitian forms over number fields, Hodge bundles, the good Chern-Weil theorem, and a second group of results in deformation theory, vanishing, positivity and arithmetic Hilbert-Samuel theory. The classical list has 17 statements. It has Mumford proportionality in place of the good Chern-Weil theorem, and it has the finiteness of classes of hermitian lattices.

Mumford proportionality is the following statement. Let $E$ be a CM field with a unitary datum of signature $(p, q)$, a level, an integral model with a toroidal model, a complex embedding and a good uniformization $U$. Then for each flag component $Y_k$ and each weight $\lambda$,
$$\bigl(L_\lambda^{\dim Y_k}\bigr) = \operatorname{covol}(U_k) \cdot \deg_{\mathrm{flag}}(\lambda),$$
where $L_\lambda$ is the automorphic line bundle of weight $\lambda$ and $\deg_{\mathrm{flag}}(\lambda)$ is the degree of $\lambda$ on the compact dual flag variety. This is the form of Hirzebruch proportionality proved by D. Mumford, "Hirzebruch's proportionality theorem in the non-compact case", Invent. Math. 42 (1977), 239 to 272. The good Chern-Weil theorem is Mumford's statement that Chern forms of good metrics compute Chern numbers, together with the push-forward formula for full flag bundles.

**Theorem 2.1.5 (Classical inputs from the published bundle).** Assume the published Hodge bundle theorems. Then the classical list holds.

Lean: `GlobalTheory.CovTop.PublishedHodgeBundleTheorems.toClassicalTheorems`.

*Proof.* Fifteen statements of the classical list are statements of the published list, so they hold by assumption. The finiteness of classes of hermitian lattices is proved without any assumption: for a CM field $E$ and a nondegenerate hermitian matrix over $E$, the lattices whose dual is a fixed fractional ideal times the lattice, with marked vectors, fall into finitely many classes under the unitary group. Mumford proportionality follows from the good Chern-Weil theorem by [Theorem 7.7.9](/entry/toroidal-flag-proportionality-of-good-chern-weil/) of the chapter on Hodge metrics. That theorem constructs a good metric on the Hodge bundle whose Chern integral is $\operatorname{covol}(U_k) \cdot \deg_{\mathrm{flag}}(\lambda)$, writes $(L_\lambda^{\dim Y_k})$ as an intersection number of a polynomial in the Chern roots on the flag bundle, and applies the good Chern-Weil theorem to identify the two numbers. $\square$

The covolume bound uses the published list in two ways. It uses the classical list for the analytic and the lattice theoretic steps. It uses the second group of the published list directly: the Kawamata-Viehweg vanishing theorem, nefness, the Nadel vanishing theorem and principalization enter the Hilbert-Samuel estimates and the orbit separation of later sections.

**Remark 2.1.6 (Formalization).** The published list is a structure with the fields `p1`, `p2`, `p3`, `p4`, `p5`, `p8`, `p12`, `p13`, `p14`, `p16`, `p19`, `p20`, `p22`, `p23`, `p25`, `p26` and `q1`, `q4`, `q6`, `q7`, `q8`, `q9`, `q10`, `q11`, `q13`, `q15`, `q16`, `q18` ([ToKnownTheoremsOf.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ToKnownTheoremsOf.lean#L7)). Three more projections, `p18`, `q2` and `q12`, are theorems that take the list as an argument `_h` and do not use it: they are proved outright (lines 36 to 38). The classical list `Hypotheses''` is built in `toClassicalTheoremsOf` (line 39), which tries `exact h.p16` before it uses the proportionality hypothesis, by a `first` tactic. The theorem is a one-line term at [CoveringTopologyRefinement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/CoveringTopologyRefinement.lean#L10); `GlobalTheory.T.covering_topology_refinement` (line 17) is a second name, proved by a `first` tactic with three alternatives. We have not unfolded `Closed`, `FamHyp`, `RowsTAlt`, the largeness condition `Large`, the inequality `L3` or the Hodge bundle statements of the list, so the descriptions above of the list are by the names of its fields.
