---
title: Valuation multiplicity and birationality
decls:
  - GlobalTheory.HSApp.exists_subspace_vanishing_order_le_phi_alt
  - GlobalTheory.T.exists_section_order_bound_hilbertSamuel_alt
  - GlobalTheory.ValMultRun.valuation_multiplicity_of_consecutive_run_alt
  - GlobalTheory.T.valuation_multiplicity_run_estimate_alt
  - GlobalTheory.DegVal.birOn_of_weight_gaps_large
  - GlobalTheory.T.birOn_wtOf_of_consecutive_gap_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Valuation multiplicity and birationality

The height lower bound of [the height section](/entry/height-lower-bound-general-alt/) compares two weights: the quotient weight $u_1$ of the level and the weight $u_1' = u_1 - 3(p + q)\lambda_H$. It needs a section $\theta$ that carries cusp forms of weight $u_1'$ to cusp forms of weight $u_1$ without losing too much at any valuation, and it needs the cusp forms of a weight to generate the function field of each component. This section proves both facts. The first is a *valuation multiplicity* statement, proved from two bounds on orders of vanishing at the boundary. The second is *birationality*, proved for every weight whose consecutive gaps are large.

Throughout, $Y$ is a good cover at a level, $Z$ a component, and $Y_0 \supset U_0$ the toroidal flag space with its interior ([toroidal compactifications](/learn/geometry/#shimura-varieties-and-toroidal-compactifications)). For a weight $G$ let $S_G(Z)$ be the cusp forms of weight $G$ on $Z$ in the space of the cover. Choosing a trivialization at the generic point of $Z$, each cusp form $f$ has a *generic value* $f(\eta)$ in the function field $\Omega_Z$ of $Z$, and this gives an $F$-linear map $S_G(Z) \to \Omega_Z$.

**Definition 2.13.1 (Birational weight).** A weight $G$ is *birational on* $Z$ if the generic value map $S_G(Z) \to \Omega_Z$ is not zero and the quotients $f(\eta)/g(\eta)$ of generic values, with $g(\eta) \neq 0$, generate $\Omega_Z$ as a field over $F$.

So $G$ is birational on $Z$ when the cusp forms of weight $G$ define a rational map from $Z$ that is birational onto its image ([point separation](/learn/geometry/#point-separation)).

**Definition 2.13.2 (Valuation multiplicity).** Let $G$ and $G'$ be weights. We say that *valuation multiplicity holds from* $G'$ *to* $G$ on $Z$ if there are an integer $a \ge 1$ and a rule $\theta$ with $\theta(\eta) \ne 0$ such that for every $k \ge 1$ and every $f \in S_{a k G'}(Z)$:

1. $\theta^k f \in S_{a k G}(Z)$;
2. for every real valuation $\nu$ of $\Omega_Z$ that is trivial on $F^\times$ there is $v \in S_G(Z)$ with $\nu\bigl((\theta^k f)(\eta)\bigr) \le \nu\bigl(v(\eta)\bigr)^{a k}$.

Condition 2 says that the multiplied form $\theta^k f$ is not more singular, at any valuation of the function field, than an $a k$-th power of a cusp form of weight $G$. Such a bound turns the volume of small sections of weight $G'$ into a bound by the volume of weight $G$, as in [the height lower bound](/entry/height-of-mean-all-bound/).

The local data at a boundary point are valuations of the stalk. Let $y \in Y_0$. A valuation $\nu$ of the stalk $\mathcal{O}_{Y_0, y}$ with values in $\{0\} \cup \exp(\mathbb{Z})$ is *centred at* $y$ if $\nu \le 1$ on the stalk, $\nu < 1$ on the maximal ideal, and $\nu(a) = 0$ only for $a = 0$. We write $\operatorname{ord}_\nu(a) = m$ when $\nu(a) = e^{-m}$. A real number $\varphi$ is a *slope value at* $(y, \nu)$ if there are a complete discrete valuation ring $T$ with fraction field over $F$, an integral point $y'$ of the moduli space over $T$ that specializes to $y$ through a local homomorphism $g \colon \mathcal{O}_{Y_0, y} \to T$, and a real $\rho > 0$, such that $y'$ has the value $\varphi_T$ of its slope invariant, which we do not unfold, $\varphi = \rho \varphi_T$, and $\operatorname{ord}_\nu(a) = \rho \, v_T(g(a))$ for all $a$ with $\nu(a) \ne 0$. In particular $\varphi \ge 0$.

**Theorem 2.13.3 (Sections of small order at the boundary).** Assume the published Hodge bundle theorems, deep goodness, the size condition and the flat degree condition. Then the following holds as a cover statement. Let $u_1$ be the quotient weight of the standard path and $u_b$ its reduced weight, obtained from $u_1$ by rounding its gaps to multiples of $\dim Y_0 + 3$. For every component $Z$, every toroidal flag model, every $\lambda \in \{u_1, u_b\}$, every $y \notin U_0$, every valuation $\nu$ centred at $y$ and every slope value $\varphi$ at $(y, \nu)$, there is a section $w$ of weight $\lambda$ in the space of the cover with $\nu(w_y) \ne 0$ and
$$\operatorname{ord}_\nu(w_y) \le \frac{\varphi}{2500}$$
in every chart of $L_0(\lambda)$ at $y$.

Lean: `GlobalTheory.HSApp.exists_subspace_vanishing_order_le_phi_alt` (also `GlobalTheory.T.exists_section_order_bound_hilbertSamuel_alt`, a second name).

*Proof.* Two cover statements are combined, with the larger of their thresholds. The first is a bound for cusp values at integral points: at an integral point $y'$ over a complete discrete valuation ring $T$, with slope invariant $\varphi_T$, there is $w$ of weight $\lambda$ whose value at $y'$ has $T$-adic order at most $\varphi_T / 2500$. The second says that the specialization $g$ in the definition of a slope value is a local homomorphism, because $\nu$ is centred, and that germs factor through it. Then $\operatorname{ord}_\nu(w_y) = \rho \, v_T(g(w_y)) \le \rho \varphi_T / 2500 = \varphi / 2500$. $\square$

**Theorem 2.13.4 (Valuation multiplicity for the quotient weight).** Assume the published Hodge bundle theorems, Grothendieck's deformation theory, the quoted results, the toroidal compactification of the Siegel space over the integers, the toroidal compactifications for fans with the log Kodaira-Spencer isomorphism, the seminegativity of the Lie algebra, deep goodness, the size condition and the flat degree condition. Then, as a cover statement, valuation multiplicity holds from $u_1'$ to $u_1$ on every component $Z$, where $u_1' = u_1 - 3(p + q)\lambda_H$.

Lean: `GlobalTheory.ValMultRun.valuation_multiplicity_of_consecutive_run_alt` (also `GlobalTheory.T.valuation_multiplicity_run_estimate_alt`, a second name).

*Proof.* Fix a good cover, a component $Z$ and a toroidal flag model. We use a general criterion: let $Y_0$ be a variety, let cusp forms of every weight extend to $Y_0$ with the cusp forms on $Y_0$ inside the space of the cover, let the bundle of weight $u$ be generated by global sections on the interior, and let $s \ne 0$ be a section of weight $a$ with $3a + 8u' = 8u$. If at each $y \notin U_0$ and each valuation $\nu$ centred at $y$ there is a section $w$ of weight $u$ with
$$\nu(s_y)^3 \le \nu(w_y)^8,$$
then valuation multiplicity holds from $u'$ to $u$, with the rule $\theta = s^3$ and $a = 8$.

We check the hypotheses for $u = u_1$. The extension of cusp forms to the compactified flag space holds because $[E : \mathbb{Q}]/2 > 2$, which follows from $[E : \mathbb{Q}] = 4 r$ and $r \ge 4$. The bundle of weight $u_1$ is generated on the interior by the base point freeness of the Hodge bundle, which uses the published list, the quoted results and the gap condition of the standard path. A further cover statement gives a section $s \ne 0$ of weight $8(p + q)\lambda_H$ with
$$\operatorname{ord}_\nu(s_y) \ge \frac{8 \varphi}{625}$$
at each boundary point, centred valuation and slope value. Then
$$3 \cdot 8 (p + q) \lambda_H + 8 u_1' = 8 u_1,$$
so the weights match. At $y \notin U_0$ and $\nu$ centred at $y$, a slope value $\varphi \ge 0$ exists by a further cover statement, and the previous theorem gives $w$ of weight $u_1$ with $\operatorname{ord}_\nu(w_y) \le \varphi / 2500$. If $\nu(s_y) = 0$ the inequality is clear. Otherwise
$$3 \operatorname{ord}_\nu(s_y) \ge \frac{24 \varphi}{625} \ge \frac{8 \varphi}{2500} \ge 8 \operatorname{ord}_\nu(w_y),$$
which is the inequality $\nu(s_y)^3 \le \nu(w_y)^8$. $\square$

Birationality is the second fact. It holds as soon as the gaps of the weight are large compared with the dimension.

**Theorem 2.13.5 (Birationality for large gaps).** Assume the hypotheses on the family, the hypotheses of the second kind, Grothendieck's deformation theory, the quoted results, the toroidal compactification of the Siegel space over the integers, Nadel vanishing with the non-klt divisor and principalisation. Let $Y$ be a deep good cover at level $j$ with $p, q \ge 1$, and let $n$ be the dimension of the flag space. Let $u$ be a weight with
$$u_{\tau, a} - u_{\tau, a + 1} \ge (n + 3)^2 + 2(p + q)$$
for every $\tau$ and every $a$ with $a + 1 < p + q$. Then $u$ is birational on every component $Z$.

Lean: `GlobalTheory.DegVal.birOn_of_weight_gaps_large` (also `GlobalTheory.T.birOn_wtOf_of_consecutive_gap_bound`, a second name).

*Proof.* Two results on cusp forms of weight $u$ are used. Both are proved from the same hypotheses and the gap condition, with Nadel vanishing and principalisation; through [the log canonical criterion](/entry/log-canonical-pair-iff/) cusp forms are sections of adjoint bundles on a resolution, to which these tools apply ([vanishing theorems and resolution](/learn/geometry/#vanishing-theorems-and-resolution)). First, there is a cusp form $f_0$ of weight $u$ with $f_0(\eta) \ne 0$, so the generic value map is not zero. Second, the cusp values separate generic points: there are an embedding $\sigma$ of $F$ and finitely generated $F$-subalgebras $B \subset A$ of $\Omega_Z$ such that $A$ generates $\Omega_Z$ as a field, every element of $B$ is a quotient of generic values, and for each nonzero $b \in B$ there is a complex point $x$ over $\sigma$ with $b(x) \ne 0$ that is the unique point agreeing with $x$ on $B$.

Now an algebraic lemma: under this uniqueness, every $a \in A$ satisfies $a q = p$ for some $p, q \in B$ with $q \ne 0$. Indeed, the map defined by $B$ is injective on complex points over a dense open set, so it is birational onto its image, and $A$ lies in the fraction field of $B$. Hence every $a \in A$ is a quotient $p/q$ of two elements of $B$, so a quotient of quotients of generic values. Since $A$ generates $\Omega_Z$, the quotients of generic values generate $\Omega_Z$. $\square$

**Remark 2.13.6 (Formalization).** In the multiplicity theorem the multiplication property of the section $s$ (that it maps the space of weight $\lambda - 8(p+q)\lambda_H$ into the space of weight $\lambda$) is discarded with `-` ([ValuationMultiplicityOfConsecutiveRun.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ValuationMultiplicityOfConsecutiveRun.lean#L58)); the criterion `valMult_of_section` (ValuationMultiplicityWeight.lean, line 315) needs only the order bounds. The key inequality is proved by `linarith` at line 91. The algebraic lemma is `exists_mul_eq_of_generic_unique_complexPoint` (ExistsMulEqOfGenericUniqueComplexPoint.lean, line 12); the reason given for it above is the standard one, and we did not read its proof. We have not unfolded `HasPhi`, so the slope invariant of an integral point is by name. The reduced weight $u_b$ is `ub` of the weight path, defined with `floorGaps`; it plays no role in the multiplicity theorem.
