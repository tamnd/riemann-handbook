---
title: Matching of principal congruence functions
decls:
  - GlobalTheory.CongMatch.match_principal_congruence_inert
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Matching of principal congruence functions

This section proves that, at an inert place of a CM field, the indicator of a principal congruence subgroup of the unitary group has an explicit transfer to $\mathrm{GL}_a \times \mathrm{GL}_b$. The transfer is a constant times the indicator of the pairs whose norms lie in principal congruence subgroups of the same level. The proof writes both sides as lattice counts by [the previous section](/entry/kap-orb-congruence-eq-kap-sum/) and compares them with the unit identity of [the unit lemma](/entry/unit-lemma-lie-and-group/). So the matching at every level comes from the matching of unit functions, which is [the Jacquet-Rallis fundamental lemma](/entry/unit-match-all/). The result gives matching test functions at the inert places for the comparison of the twisted trace formula with the trace formula of a unitary group, on the way to the step [every character](/step/every-character/). For the background, see [the relative trace formula and the Jacquet-Rallis fundamental lemma](/learn/trace-formula/#the-relative-trace-formula-and-the-jacquet-rallis-fundamental-lemma) and [the twisted trace formula and base change](/learn/trace-formula/#the-twisted-trace-formula-and-base-change).

We keep the notation of [the previous section](/entry/kap-orb-congruence-eq-kap-sum/): $E$ is a CM field in which every finite place is unramified over $E^+$, $w$ is a finite place of $E$ not split over $E^+$, $c$ is the conjugation of $E_w$, $\theta$ and $\mathcal{N}$ are the twist and the norm on $\mathrm{GL}_m(E_w)$, $\mathrm{U}(n)$ is the unitary group, $K_m(k)$ is the principal congruence subgroup of level $k$, and $O^\kappa_{Q_1, Q_2}$ is the $\kappa$-orbital integral.

**Definition 2.7.1 (Matching at an inert place).** Let $n = a + b$.

1. For a function $\varphi$ on $\mathrm{GL}_a(E_w) \times \mathrm{GL}_b(E_w)$ and monic $Q_1$, $Q_2$ of degrees $a$, $b$, let $SO^\theta_{Q_1, Q_2}(\varphi)$ be the sum of the twisted orbital integrals $TO_{(y_1, y_2)}(\varphi)$ over the twisted conjugacy classes of pairs with $\det(X - \mathcal{N}(y_i)) = Q_i$ for $i = 1, 2$. The twist, the norm and the maximal compact subgroup are taken componentwise.
2. The *transfer factor* is $\Delta(Q_1, Q_2) = (-1)^{\mathrm{ord}_w(R)}\, |R|_w^{1/2}$, where $R = \mathrm{Res}(Q_1, Q_2)$ and $|R|_w = q_w^{-\mathrm{ord}_w(R)}$.
3. A function $f$ on $\mathrm{U}(n)$ and a function $\varphi$ on $\mathrm{GL}_a(E_w) \times \mathrm{GL}_b(E_w)$ *match* if
$$SO^\theta_{Q_1, Q_2}(\varphi) = \Delta(Q_1, Q_2)\, O^\kappa_{Q_1, Q_2}(f)$$
for all monic $Q_1$, $Q_2$ of degrees $a$, $b$ that are conjugate self-reciprocal and have separable product $Q_1 Q_2$.

The sign $(-1)^{\mathrm{ord}_w(R)}$ is the value at $R$ of the quadratic character of $E_w^c$ that belongs to the unramified extension $E_w / E_w^c$. At split places the matching uses a different factor, with a character $\mu$ of $E_w^\times$; see [the split places](/entry/match-ct-mu-of-is-split-at/).

**Theorem 2.7.2 (Matching of principal congruence functions).** Let $E$ be a CM field in which every finite place is unramified over $E^+$, and $w$ a finite place of $E$ that is not split over $E^+$. Let $n = a + b$ and $k \ge 1$. Put
$$f = \mathbf{1}_{\mathrm{U}(n) \cap K_n(k)}, \qquad \varphi(y_1, y_2) = \big(-\sqrt{q_w}\big)^{-kab} \prod_{i = 1}^{2} \mathbf{1}\big[\,y_i \in \mathrm{GL}(\mathcal{O}_w) \text{ and } \mathcal{N}(y_i) \in K(k)\,\big],$$
where in the product $\mathrm{GL}$ and $K(k)$ are of size $a$ for $i = 1$ and of size $b$ for $i = 2$. Then $f$ and $\varphi$ match.

Lean: `GlobalTheory.CongMatch.match_principal_congruence_inert`

The proof needs one more input, which is the form of the unit lemma for elements near $1$.

**Fact (Unit identity near the identity).** Let $K$ be an unramified quadratic datum and $t$ a small element. Let $B_1$, $B_2$ be algebras with involution with $u_i \sigma(u_i) = 1$ for $u_i = 1 + t g_i$, and with $P_1 P_2$ separable. Then
$$(-q)^{-\mathrm{val}(\mathrm{Res}(P_1, P_2))}\, \kappa(B_1, B_2) = S(B_1)\, S(B_2).$$

This is the unit identity of [the unit lemma](/entry/unit-lemma-lie-and-group/) for the pair $(B_1, B_2)$. It follows from the unit lemma for the Lie algebra, which follows in turn from [the fundamental lemma in all ranks](/entry/unit-match-all/). The elements $g_i$ are in the Lie algebra up to the shift: $u_i\sigma(u_i) = 1$ gives $g_i + \sigma(g_i) + t\, g_i \sigma(g_i) = 0$.

*Proof of the Theorem.* Fix $Q_1$, $Q_2$ as in the definition of matching, and let $R = \mathrm{Res}(Q_1, Q_2)$ and $v = \mathrm{ord}_w(R)$.

*Step 1: a model and a small element.* Since $w$ is inert and unramified, there is a [model](/entry/kap-orb-congruence-eq-kap-sum/) $(K, e)$ of $E_w$. Its residue field has $q$ elements with $q^2 = q_w$, so $\sqrt{q_w} = q$. Since $k \ge 1$, there is a small $t \in \mathcal{O}$ with $c_K(t) = t$ and $\mathrm{val}(t) = k$: take a power of a uniformizer of the fixed field.

*Step 2: algebras with involution.* For $i = 1, 2$, let $B_i = E_K[X]/(Q_i^e)$ and $u_i$ the class of $X$. As $Q_i$ is conjugate self-reciprocal, there is a semilinear involution $\sigma$ of $B_i$ with $\sigma(u_i) = u_i^{-1}$. Put $g_i = (u_i - 1)/t$. Then $u_i = 1 + t g_i$ generates $B_i$, $Q_i^e(u_i) = 0$, $\dim B_i = \deg Q_i$, and $u_i \sigma(u_i) = 1$.

*Step 3: the resultant.* Let $\alpha_1, \dots, \alpha_a$ and $\beta_1, \dots, \beta_b$ be the roots of $Q_1^e$ and $Q_2^e$ in an algebraic closure. The roots of $P_i$, the characteristic polynomial of $g_i$, are the $(\alpha_j - 1)/t$ and the $(\beta_l - 1)/t$. So
$$\mathrm{Res}(P_1, P_2) = \prod_{j, l} \frac{\alpha_j - \beta_l}{t} = t^{-ab}\, \mathrm{Res}(Q_1^e, Q_2^e).$$
So $P_1 P_2$ is separable and $\mathrm{val}(\mathrm{Res}(P_1, P_2)) = v - kab$.

*Step 4: the twisted side.* The function $\varphi$ is a constant times a product of functions of $y_1$ and $y_2$, and the twisted classes of pairs are pairs of twisted classes. So
$$SO^\theta_{Q_1, Q_2}(\varphi) = (-q)^{-kab}\, SO^\theta_{Q_1}(\varphi_k)\, SO^\theta_{Q_2}(\varphi_k),$$
where $\varphi_k$ is the level function of [the previous section](/entry/kap-orb-congruence-eq-kap-sum/). By the Theorem on level functions there, $SO^\theta_{Q_i}(\varphi_k) = S(B_i)$.

*Step 5: the unitary side.* By the Corollary on congruence indicators of the previous section, $O^\kappa_{Q_1, Q_2}(f) = \kappa(B_1, B_2)$. Also $\Delta(Q_1, Q_2) = (-1)^v q_w^{-v/2} = (-1)^v q^{-v} = (-q)^{-v}$.

*Step 6: comparison.* By the Fact and Step 3,
$$\begin{aligned}
SO^\theta_{Q_1, Q_2}(\varphi) &= (-q)^{-kab}\, S(B_1)\, S(B_2) \\
&= (-q)^{-kab}\, (-q)^{-(v - kab)}\, \kappa(B_1, B_2) \\
&= (-q)^{-v}\, \kappa(B_1, B_2) = \Delta(Q_1, Q_2)\, O^\kappa_{Q_1, Q_2}(f).
\end{aligned}$$
$\square$

The constant $(-\sqrt{q_w})^{-kab}$ in $\varphi$ is what makes the powers of $-q$ agree. It does not depend on $Q_1$, $Q_2$: the shift by $t$ changes the valuation of every resultant by the same amount $kab$. For $k = 0$ there is no small element of valuation $0$, and the Theorem is stated only for $k \ge 1$.

**Remark 2.7.3 (Formalization).** Matching is a predicate with a character $\mu$ of $E_w^\times$, and the inert case uses $\mu = 1$; the factor $\Delta$ ignores $\mu$ at inert places ([SimpleTwistedTraceFormulaStable.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SimpleTwistedTraceFormulaStable.lean#L264)). The power check of Step 6 is a separate lemma, whose name, `unit_product_rescale_disjoint_finsets`, says nothing about its content: it is an identity of complex numbers in $q$, $v$ and $kab$ ([CongruenceSubgroupIndicatorWeight.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CongruenceSubgroupIndicatorWeight.lean#L19)). The main proof is a chain of rewrites by the named results of Steps 1 to 5 ([CongruenceSubgroupIndicatorWeight.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CongruenceSubgroupIndicatorWeight.lean#L41)). The Fact is used in the form of a theorem that takes the unit lemma for the Lie algebra as a hypothesis; that statement is supplied from the statement of the fundamental lemma in all ranks. We did not unfold these three statements, the construction of Step 2, or the product formula of Step 4. The same theorem has a second name, `GlobalTheory.T.congruence_subgroup_indicator_weight`, stated by `first | exact …` ([CongruenceSubgroupIndicatorWeightStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CongruenceSubgroupIndicatorWeightStatement.lean#L8)).
