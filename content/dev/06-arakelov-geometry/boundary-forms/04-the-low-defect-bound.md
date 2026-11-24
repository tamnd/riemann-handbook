---
title: The low defect bound
decls:
  - GlobalTheory.CovTop.DefCore.defect_bound_of_connected_alt
  - GlobalTheory.CovTop.DefCore.lifts_two_mul_defBound_sub_unitE_le_muCore
  - GlobalTheory.T.two_mul_defBound_sub_le_muCore_of_gramAt
  - GlobalTheory.CovTop.DefLow.covering_low_defect_alt
  - GlobalTheory.T.lowDef_of_gram_of_anchor
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The low defect bound

This section proves the low defect bound: at the last level of every point of a family, the slope of the core lattice is at least $-T_i - C E$, with a constant $C$ that does not depend on the point. The proof has three steps. First, a defect bound $\mathrm{def}$ is attached to the weight of the level, and the slope of the core lattice is at least $2 \, \mathrm{def}$. Second, this holds as a level statement. Third, the anchor condition compares $2 \, \mathrm{def}$ with the main term $T_i$. The low defect bound is one of the inputs of the covolume bound in the last section of this part, where it gives the lower bound for the lift of the core lattice.

We keep the notation of [the previous section](/entry/deg-lie-core-alt/): a point $p$, a level $i$ with $i + 1 = m$, the datum of signature $(p_i, q_i)$ at level $i + 1$, the CM type $\Psi$ with $f = |\Psi|$ elements, the root discriminant $\mathrm{rd}(E)$, the logarithmic period $\log \Omega$ and the flat degree value $\phi$. Let $a$ be the weight of level $i$ and $n$ its number of columns. For $\tau \in \Psi$ let $\lambda_\tau$ be the partition of $a$ at $\tau$, with size $|\lambda_\tau|$, and let $\dim \lambda_\tau \ge 1$ be the dimension attached to it. Let $\mu$ be the slope of the core lattice at level $i$ ([hermitian lattices and slopes](/learn/arakelov/#hermitian-lattices-and-slopes)).

**Definition 2.4.1 (Defect bound).** For $c_1 \in \mathbb{R}$ put
$$\begin{aligned} \mathrm{def}(c_1) = {} & \sum_{\tau \in \Psi} \Bigl[ \Bigl( \frac{|\lambda_\tau|}{p_i} + \frac{n}{2} \Bigr) c_1 - \frac{1}{2} \log \dim \lambda_\tau \Bigr] \\ & + n f p_i \Bigl( \frac{\log 2\pi}{4} - \frac{\log \mathrm{rd}(E)}{2} \Bigr). \end{aligned}$$

We use it with $c_1 = -\phi$. The first sum is linear in $c_1$, with the size of the weight as coefficient, and the last term does not depend on the weight.

**Theorem 2.4.2 (Defect bound at a point).** Assume the published Hodge bundle theorems. There are $M \in \mathbb{R}$ and $C_0 \ge 0$ with the following property. Let $p$ be a point of a family with the row condition, let $i + 1 = m$, and assume the Gram condition, the weight numerics with parameter $P$, the host numerics with parameters $P$, $A$ and $M$, and that the coefficient field is algebraically closed in the function field of each component at level $i + 1$. Then
$$2 \, \mathrm{def}(-\phi) - C_0 E \le \mu.$$

Lean: `GlobalTheory.CovTop.DefCore.defect_bound_of_connected_alt`.

*Proof.* We take $M = 0$ and $C_0 = 0$, so we prove $2 \, \mathrm{def}(-\phi) \le \mu$. At the last level the moduli space has finitely many components, at least one, and the datum is in the definite case, as in [Theorem 2.3.4](/entry/deg-lie-core-alt/). There is a finite group $G$ that acts by level maps on the lattice of the datum, freely on the points of the moduli space, with a character $\chi \colon G \to F^\times$, such that the $\chi$-eigenlattice of the modular forms of the weight of the level has slope at most $\mu$. By [Theorem 2.3.5](/entry/flat-exists-at-core-alt/), each component carries flat sections at each $\tau$, and each of them has degree $\phi$. A lower bound for the slope of eigenlattices in the definite case now applies: for a free action with such a character, and flat sections of degree $\phi$, the $\chi$-eigenlattice has slope at least $2 \, \mathrm{def}(-\phi)$. So $2 \, \mathrm{def}(-\phi) \le \mu$. $\square$

**Theorem 2.4.3 (Defect bound as a level statement).** Assume the published Hodge bundle theorems. Then the following level statement holds: for the levels $i$ with $i + 1 = m$ at which the Gram condition holds,
$$2 \, \mathrm{def}(-\phi) - C E \le \mu.$$

Lean: `GlobalTheory.CovTop.DefCore.lifts_two_mul_defBound_sub_unitE_le_muCore` (also `GlobalTheory.T.two_mul_defBound_sub_le_muCore_of_gramAt`, a second name).

*Proof.* The weight numerics hold as a level statement, and the host numerics hold as a level statement for each value of $M$. Take the constants $M_1, C_1$ of the previous theorem, and the constants $M_2, C_2$ of the companion result for the case where the coefficient field is not algebraically closed in the function field. Put $C = \max(C_1, C_2)$ and take $x$ larger than the thresholds of the three level statements. At a point and a level with $i + 1 = m$ and the Gram condition, the unit $E$ is nonnegative. If the coefficient field is algebraically closed in the function field, the previous theorem gives $2 \, \mathrm{def}(-\phi) - C_1 E \le \mu$; otherwise the companion result gives the same with $C_2$. As $E \ge 0$, both give the bound with $C$. $\square$

The companion result is vacuous: under the row condition, the coefficient field is always algebraically closed in the function field at level $i + 1$, so its hypothesis cannot hold. The case split is therefore only formal.

Now we use the anchor. The *anchor weights* $a_\tau \in \mathbb{Z}$, for $\tau \in \Psi$, are attached to the weight $a$, and $a_{\tau, k}$ are its entries. The anchor condition at level $i$ says, in its first part,
$$\Bigl| T_i - \sum_{\tau \in \Psi} (p_i - q_i)\, a_\tau \log \Omega \Bigr| \le C_A E.$$

We need an elementary estimate of the defect bound by the anchor weights. Let the datum have $q = 0$ and $p \ge 1$, let $n$ be even, and let $\ell \in \mathbb{R}$. Then
$$\begin{aligned} 2 \, \mathrm{def}\bigl(-\phi(\ell)\bigr) \ge {} & -\sum_{\tau} p\, a_\tau \ell - |\ell| \sum_{\tau, k} |a_{\tau, k} - a_\tau| \\ & - \sum_\tau \log \dim \lambda_\tau - n f p \, |\log \mathrm{rd}(E)|, \end{aligned}$$
where $\phi(\ell) = \frac{p}{2} \ell$ is the flat degree value with $\log \Omega$ replaced by $\ell$.

This estimate is proved from the definition of $\mathrm{def}$ together with the definition of the anchor weights, which we do not unfold, so we use it as stated.

**Theorem 2.4.4 (Low defect bound).** Assume the published Hodge bundle theorems, the Gram condition and the anchor condition. Then the low defect condition holds: there is a level statement with constant $C$ such that at each level $i$ with $i + 1 = m$,
$$-T_i - C E \le \mu.$$

Lean: `GlobalTheory.CovTop.DefLow.covering_low_defect_alt` (also `GlobalTheory.T.lowDef_of_gram_of_anchor`, a second name).

*Proof.* Take the constant $C_A$ of the anchor condition, the constant $C_0$ of [Theorem 2.4.3](/entry/lifts-two-mul-def-bound-sub-unit-e-le-mu-core/), and the constant $C_3$ of the following bound on the errors at the last level, which holds as a level statement:
$$\begin{aligned} & |\log \Omega| \sum_{\tau, k} |a_{\tau, k} - a_\tau| + \sum_\tau \log \dim \lambda_\tau \\ & \quad + n f p_i \, |\log \mathrm{rd}(E)| \le C_3 E. \end{aligned}$$
Put $C = C_A + C_3 + C_0$ and take $x$ larger than all the thresholds. Fix a point and the last level. By the weight numerics the signature is the one of the family, so $q_i = 0$ and $p_i \ge 1$ at the last level, and the number $n$ of columns is even. The estimate with $\ell = \log \Omega$ and the error bound give
$$2 \, \mathrm{def}(-\phi) \ge -\sum_\tau p_i a_\tau \log \Omega - C_3 E.$$
The anchor condition with $q_i = 0$ gives $-\sum_\tau p_i a_\tau \log \Omega \ge -T_i - C_A E$. The defect bound gives $\mu \ge 2 \, \mathrm{def}(-\phi) - C_0 E$. Adding the three inequalities gives $\mu \ge -T_i - (C_A + C_3 + C_0) E$. $\square$

**Remark 2.4.5 (Formalization).** The first theorem takes the published list as an argument `_hP` and does not use it, and its witnesses are $M = 0$ and $C_0 = 0$ ([DefectBoundOfConnected.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DefectBoundOfConnected.lean#L21)). In the second theorem (line 32) the branch where the function field condition fails uses `GlobalTheory.T.two_defBound_sub_unitError_le_muCore_alt`, which is proved by contradiction from `fnAlgClosed_core_alt`: the row condition already gives the function field condition ([IsDefinedOfNotFunctionFieldAlgClosed.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/IsDefinedOfNotFunctionFieldAlgClosed.lean#L14)). So the case split is vacuous, and the hypothesis on the function field in the results of the previous section is implied by the row condition. The low defect bound ([CoveringLowDefectBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoveringLowDefectBound.lean#L17)) uses only the first part of the anchor condition; its second name is at line 53. We have not unfolded the partitions $\lambda_\tau$, the dimension $\dim \lambda_\tau$, the anchor weights, the core lattice, or the eigenlattice slope bound and the group action used in the first proof. The estimate by the anchor weights is `GlobalTheory.T.two_definiteBound_ge_anchoredMainTerm_sub_crude_errors`, and the error bound is `GlobalTheory.T.weight_dimension_log_bound'`.
