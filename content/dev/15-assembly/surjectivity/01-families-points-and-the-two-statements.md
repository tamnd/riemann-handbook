---
title: Families, points and the two statements
decls:
  - GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Families, points and the two statements

This section defines the objects of the chapter and states its main theorem. A family attaches to each large real number $x$ a finite set of data, and each datum has points. At a point there are two indefinite data, an untwisted one and a twisted one. The surjectivity statement says that the untwisted datum satisfies a local index bound, the onto condition, at almost all points. The lower bound for $\lambda$ says that the twisted datum has large scaling factors at almost all points. Both statements hold in a closed way: they hold for all families that are large enough for a threshold. The main theorem proves both from the hypotheses of [the unitary hypotheses chapter](/proof/unitary-hypotheses/). The step [the hypotheses are not empty](/step/nonempty-hyps/) uses the second statement.

**Definition 5.1.1 (Family, points).** A *family* $\mathcal{F}$ with parameter $\varepsilon > 0$ has a number $x_1$ and, for each real $x > x_1$, a finite index set $I(x)$. To each $x > x_1$ and $i \in I(x)$ it attaches a datum $D_{x,i}$ with sizes $L_{x,i}$, and a set of *points* $p$ at $(x, i)$. A point is *regular* if it satisfies the point conditions of the family. It is *rich* if it satisfies three more conditions: the places of single index are twisted, the core ties hold, and the record ties hold.

Lean: `Formalism.MainNotions.FamP`.

**Definition 5.1.2 (Eventually at points).** Let $Q$ be a property of points of $\mathcal{F}$. Then $Q$ holds *eventually at the points* of $\mathcal{F}$ if there is $x_0$ such that $Q(p)$ holds for each $x > x_1$ with $x \ge x_0$, each $i \in I(x)$ and each regular point $p$ at $(x, i)$.

Lean: `GlobalTheory.BigTop.EventuallyAtPoints` (also `GlobalTheory.BigOn.AtPtsAlt`).

**Definition 5.1.3 (Closed property).** Let $\mathcal{C}$ be a class of families and let $P(\mathcal{F}, C_H)$ be a property of a family and a real number. Then $P$ is *closed* for $\mathcal{C}$ if there is $\varepsilon_1 > 0$ with this property: for each $\varepsilon \in (0, \varepsilon_1]$ there is a threshold record $K$ such that $P(\mathcal{F}, C_H)$ holds for each family $\mathcal{F}$ in $\mathcal{C}$ with parameter $\varepsilon$ and each $C_H$ for which $\mathcal{F}$ is large for $K$ and $C_H$.

Lean: `Formalism.MainNotions.Closed`.

A closed property is the form in which the proof uses an estimate along a family: one may shrink $\varepsilon$ and enlarge the threshold. Two closed properties give a closed conjunction: take the smaller $\varepsilon_1$, and join the thresholds. All statements of this chapter are closed for the class $\mathcal{C}_{\mathrm{fam}}$ of the family hypotheses of [the step on closed properties](/step/closed-def/). In most of them the property is "eventually at the points, if $p$ is rich, then $Q(p)$".

Next we define the onto condition. Let $K$ be a number field. For a finite place $w$ of $K$ write $p_w$ for the characteristic of its residue field, $e_w$ for its ramification index over $p_w$, $\bar w$ for the conjugate place, and

$$\lambda_w = \frac{\log N(w)}{[K : \mathbb{Q}]}.$$

**Definition 5.1.4 (Local index).** Let $V$ be a vector space over $K$ and let $A, B$ be two $\mathcal{O}_K$-lattices in $V$. The *local index* of $A$ and $B$ at $w$ is

$$\mathrm{idx}_w(A, B) = \ell_w\big(A / (A \cap B)\big) - \ell_w\big(B / (A \cap B)\big),$$

where $\ell_w$ is the [length](/learn/algebra/#rings-ideals-and-modules) of the localization at $w$.

The local index is additive: $\mathrm{idx}_w(A, C) = \mathrm{idx}_w(A, B) + \mathrm{idx}_w(B, C)$. If $B \subseteq A$ it is $\ell_w(A_w / B_w)$.

**Definition 5.1.5 (Indefinite datum, scale).** An *indefinite datum* $S$ over $K$ for index sets $J$ (levels) and $T$ (types, with a base type $\mu_0$) consists of: a map $\mu$ from the finite places of $K$ to $T$; a finite set $T_w$ of *twisted places*; a dimension $D$; for each level $j$ a lattice $M_j$ in $K^{d_W(j)}$ and matrices $\theta_{j,t}$; positive scalars $\lambda(j, t, \mathfrak{p}, v)$ indexed by a level, a type, a part and an infinite place; and error terms $\epsilon(w, j)$. Write $I_w(j) = \mathrm{idx}_w(M_j, \theta_{j, \mu(w)} T_{j, \mu(w)})$, where $T_{j,t}$ is the lattice of the definite side. A *scale* $N$ consists of real functions $F_0(w, j)$, $J_0(t, w, j)$, $E_1(j)$, $\ell_6(j)$ and some further numbers. A family of scales $N(C, C_H)$, $C \in \mathbb{R}$, has the form

$$\begin{aligned} E_1(j) &= C \, E_{1u}, \\ \ell_6(j) &= \ell_{6m}(j) - C \, \ell_{6u}, \end{aligned}$$

with $F_0$ and $J_0$ independent of $C$.

**Definition 5.1.6 (Onto condition).** The datum $S$ is *onto* the scale $N$ if three conditions hold. First, for each $w \in T_w$,

$$\begin{aligned} \sum_j \big(I_w(j) + I_{\bar w}(j)\big) \le \Big( &\sum_j \big(2 e_w F_0(w, j) + e_w \epsilon(w, j)\big) \\ &+ \frac{2 e_w}{p_w^2} \Big) D. \end{aligned}$$

Second, $\epsilon(w, j) \ge 0$ for each $w \in T_w$ and each $j$. Third, for each $j$,

$$\sum_{w \in T_w} \lambda_w \, e_w \big(\epsilon(w, j) + J_0(\mu(w), w, j)\big) \le E_1(j).$$

Lean: `Formalism.L2.Indef.IndefData.ON` (also `Formalism.L2.Indef.Tree.ONwith`, the same three conditions with a given error).

The first condition bounds the distance of the lattices $M_j$ from the images of the definite lattices at each twisted place. The third bounds the total error, weighted by $\lambda_w$, by $C E_{1u}$. So the onto condition becomes easier as $C$ grows.

**Definition 5.1.7 (Lower bound for $\lambda$).** The datum $S$ has the *lower bound for $\lambda$* at $N$ if $\ell_6(j) \le \log \lambda(j, \mu_0, \mathfrak{p}, v)$ for each level $j$, each part $\mathfrak{p}$ and each infinite place $v$.

Lean: `Formalism.L2.Indef.IndefData.L6`.

At each point $p$ there are two indefinite data, $S_p^{-}$ (untwisted) and $S_p^{+}$ (twisted), and a family of scales $N_p(C, C_H)$.

**Definition 5.1.8 (The two statements).** The *surjectivity statement* says that the following property of $(\mathcal{F}, C_H)$ is closed for $\mathcal{C}_{\mathrm{fam}}$: if $\mathcal{F}$ satisfies the divisor bound in $N$, then there is $C_0 \ge 0$ such that, eventually at the points of $\mathcal{F}$, each rich point $p$ has $S_p^{-}$ onto $N_p(C, C_H)$ for all $C \ge C_0$. The *lower bound statement for $\lambda$* says that the following property is closed for $\mathcal{C}_{\mathrm{fam}}$: eventually at the points of $\mathcal{F}$, $S_p^{+}$ has the lower bound for $\lambda$ at $N_p(C, C_H)$ for all $C$.

Lean: `GlobalTheory.BigOn.SurjectiveOntoX` (also `GlobalTheory.BigTop.LambdaLowerBound₂`).

The divisor bound in $N$ says: there are $C$ and $x_0$ such that for $x \ge x_0$, each $i$ and each lift $j$, the sum of the $\eta$-terms of $L_{x,i}$ at $j$ is at most $D_0 \, C x^{\varepsilon} (B_0 + N_c)$. The second statement asks for no richness and holds for all $C$, not only large $C$.

**Theorem 5.1.9 (Surjectivity and the lower bound for $\lambda$).** Assume the [unitary group hypotheses at the third place](/step/unitary-group-third-place-hypotheses-def/). Then the surjectivity statement and the lower bound statement for $\lambda$ hold.

Lean: `GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'`.

*Proof.* The surjectivity statement is [the theorem of Section 10](/entry/onto-x-of-hypotheses-alt-alt/). It uses twelve of the hypotheses: the classification of cuspidal characters of finite general linear groups, the cohomological property of regular algebraic cusp forms, the two statements on $\ell$-adic characters of Hecke characters, the Chebotarev density theorem in degree one, the Galois representations of polarized cusp forms, base change for definite unitary groups, the crystalline lattices of Bhatt and Scholze, the rapid decay of cusp forms, the local Langlands correspondence, the cover by discrete series, and the Casselman-Wallach theorem. The local Langlands correspondence is built from the local hypotheses as in [the step on it](/step/rect-exists-def/). The lower bound statement for $\lambda$ is [the theorem of Section 11](/entry/lam-low-of-hypotheses-alt-alt/). It uses seven hypotheses: the rapid decay of cusp forms, the Weil-Siegel formula, the convergence of the Siegel-Weil integral, the local zeta integrals of the doubling method, the unramified doubling integrals for $\mathrm{GL}$, the finiteness theorem of Bernstein and Zelevinsky, and the formal degree of the compact dual. $\square$

**Remark 5.1.10 (Formalization).** The theorem is at [SurjectiveAndLowWeightOfUnramifiedExponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SurjectiveAndLowWeightOfUnramifiedExponents.lean#L16). The step that uses it keeps only the second part, so the surjectivity statement, with 19,069 declarations below it, does not reach the end of the proof through this theorem. We have not unfolded the point conditions, the three richness conditions, the family hypotheses, or the condition "large for $K$ and $C_H$". The names `p.S false` and `p.S true` are the data that we write $S_p^{-}$ and $S_p^{+}$; the words "untwisted" and "twisted" are our reading of the boolean. The words "unramified exponents" in the file name say nothing about the statement.
