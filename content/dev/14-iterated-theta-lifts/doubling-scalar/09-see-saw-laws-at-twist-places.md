---
title: See-saw laws at twist places
decls:
  - GlobalTheory.T.seeSawTwistPlaceLaws_of_rootOfUnityRescaling
  - GlobalTheory.QTw.laws_of_pin_resc
  - GlobalTheory.T.seeSawIteratedIntegralLaw_at_twist_of_factorisation
  - GlobalTheory.QLawPf.qLaw_of_pin
  - GlobalTheory.QLawPf.oneChart
status: drafted
drafted_by: writer@claude-opus-5-5
---
## See-saw laws at twist places

A [see-saw](/learn/theta/#seesaw-pairs) chain of theta lifts carries, at its twist places, a decoration: coefficients, weights, combinations of group elements and a constant at each index of the chain. Three laws link the decoration to the chain: an iterated integral law at each inner index, an integral law at the last steps, and a law of finite cells. This section proves the first law when the decoration is *pinned*, that is, when it is the product over the twist places of local data. It then proves all three laws for a decoration that is a pinned one rescaled by roots of unity. The input is [the double step at finitely many split places](/entry/val-q/). The result is used in [the rescaled laws](/entry/laws-resc-alt/) of the chapter on the open orbit, for the multiplicity condition in branch 3 of the [unitary hypotheses](/proof/unitary-hypotheses/).

**Setting.** Fix common see-saw data $c$ for a datum $D$ with chain length $m$: hermitian spaces $V_j$ and $X_j$, Weil representations, Jacobi and Bessel subgroups at each inner position, period maps $\mathrm{per}$, and a top group with a fundamental domain. Fix data $v$ at the twist places, with lattices $N_j$, and a tuple $t$ with character index sets $\mathrm{Ch}_j$ and the see-saw lifts. A *decoration* $w$ of $t$ consists of a finite set $Q$ of twist places and, for each index $j$:

- combinations $e_Q(j)$ of operators on theta functions, and $e_{Q,T}(j)$ at the top;
- coefficients $d_Q(j, \alpha, \gamma)$ for $\alpha \in \mathrm{Ch}_j$ and $\gamma \in \mathrm{Ch}_{j+1}$;
- combinations $\varepsilon(j, \alpha)$ of group elements, and $\varepsilon_T(j, \beta)$ at the top;
- a constant $c_Q(j)$;
- sets $F_X(j, \alpha)$ and $F_Y(j)$ of admissible functions.

Below, $j$ and $\sigma$ satisfy $j + 2(\sigma+1) + 2 = m$, so that the indices $j$, $j+1$, $j+2$ form an inner see-saw position. For theta functions $\Psi_1, \Psi_2$, a function $\varphi$ on the group of $X_j$, an element $g$, and points $q_1, q_2$ of the groups of $V_{j+1}$ and $V_{j+2}$ at the places of $Q$, let $\mathrm{hand}(\Psi_1, \Psi_2, \varphi; g, q_1, q_2)$ be the see-saw lift of $\varphi$ by the two Weil representations, and let $\mathrm{ctr}(\Psi_1, \Psi_2)$ be the contracted theta function of the position. Write $\mathrm{bl}(\varphi, d, d', \Theta)$ for the lift of $\varphi$ by the bi-combination of $\Theta$ with the coefficients $d, d'$.

**Definition 2.9.1 (Iterated integral law).** The decoration $w$ satisfies the *iterated integral law* if, for every inner position $(j, \sigma)$, all Haar measures $\mu_1, \rho_1$ on the group of $V_{j+1}$ at $Q$ and its Jacobi subgroup, and $\mu_2, \rho_2$ on the group of $V_{j+2}$ at $Q$ and its Bessel subgroup, which give volume one to the elements stabilising the lattices, all theta functions $\Psi_1, \Psi_2$ that are vacuum at $Q$, all continuous automorphic $\varphi_\alpha \in F_X(j, \alpha)$, and every automorphic $f \in F_Y(j+2)$, the function
$$(q_1, q_2) \mapsto \sum_{\alpha} \sum_{g} \varepsilon(j, \alpha)(g)\, \mathrm{per}\big(\mathrm{hand}(e_Q(j)\Psi_1, e_Q(j+1)\Psi_2, \varphi_\alpha; g, q_1, q_2),\ R(q_2) f\big)$$
has the iterated quotient integral, in the sense of [the last section](/entry/val-q/),
$$c_Q(j) \sum_{\beta} \mathrm{per}\Big(\sum_{\alpha, \gamma} \mathrm{bl}\big(\varphi_\alpha, d_Q(j, \alpha, \gamma), d_Q(j+1, \gamma, \beta), \mathrm{ctr}(\Psi_1, \Psi_2)\big),\ \varepsilon(j+2, \beta) \cdot f\Big).$$

The *last step law* is the analogous identity at the last position $j + 2 = m$, with the integral over the fundamental domain of the top group in place of the iterated integral, and $e_{Q,T}$, $\varepsilon_T$ in place of $e_Q$, $\varepsilon$. The *finite cell law* says that at each inner position there are a compact open subgroup $K_1$ of the group of $V_{j+1}$ at $Q$ and a finite set $T_1$ such that each $k \in K_1$ acts on $e_Q(j)\Psi_1$ by a nonzero scalar $a^{-1}$ and on $e_Q(j+1)\Psi_2$ by $a$, and such that the support of the flattened theta function at $(g, x)$, for $g$ in the support of $\varepsilon(j, \alpha)$, is covered by finitely many cells $r\, q\, K_1$ with $r$ in the Jacobi subgroup and $q \in T_1$.

**Definition 2.9.2 (Pinned and rescaled decorations).** The decoration $w$ is *pinned* if there are split place data $Q_1, \dots, Q_r$ of the see-saw, at distinct places, with $Q = \{q_1, \dots, q_r\}$, characters $\chi_j$ of the ideles that match the splitting characters of the lifts, and bijections $\mathrm{Ch}_j \cong \prod_i \mathrm{Ch}_j(Q_i)$, such that
$$\begin{aligned} e_Q(j) &= e^{(1)}(j) * \dots * e^{(r)}(j), \qquad d_Q(j, \alpha, \gamma) = \prod_i \mathrm{wt}_i(\alpha_i) \cdot \big(d^{(1)}(\alpha_1, \gamma_1) * \dots * d^{(r)}(\alpha_r, \gamma_r)\big), \\ \varepsilon(j, \alpha) &= \prod_i \mathrm{wt}_i(\alpha_i) \cdot \big(\varepsilon^{(1)}(\alpha_1) * \dots * \varepsilon^{(r)}(\alpha_r)\big), \qquad c_Q(j) = \prod_i \big(n_i(j+1)\, n_i(j+2)\big)^{-1}, \end{aligned}$$
with similar formulas at the top, and every $f \in F_Y(j)$ is of the right type at each $q_i$. Here $\mathrm{wt}_i$ are the weights and $n_i$ the indices of the local data. For numbers $s(j, \alpha) \in \mathbb{C}$ the *rescaled* decoration $w^s$ has
$$d_Q^s(j, \alpha, \gamma) = \frac{s(j, \alpha)}{s(j+1, \gamma)}\, d_Q(j, \alpha, \gamma), \qquad \varepsilon^s(j, \alpha) = s(j, \alpha)\, \varepsilon(j, \alpha), \qquad \varepsilon_T^s(j, \beta) = s(j, \beta)\, \varepsilon_T(j, \beta),$$
and agrees with $w$ otherwise. The decoration $w$ is *pinned up to roots of unity* if $w = w_0^s$ with $w_0$ pinned and every $s(j, \alpha)$ a root of unity.

The validity conditions on $c$, $t$, $v$ and the condition that the Weil representations of $v$ are compatible are assumed throughout and called the *standing conditions*.

**Theorem 2.9.3 (One chart).** Assume the standing conditions, and let $w$ be pinned by $Q_1, \dots, Q_r$. Fix an inner position $(j, \sigma)$, normalised measures, vacuum theta functions $\Psi_1, \Psi_2$ as in the iterated integral law, one index $\alpha \in \mathrm{Ch}_j$, a continuous automorphic $\varphi$, and a continuous automorphic $f \in F_Y(j+2)$. Then the function
$$(q_1, q_2) \mapsto \sum_{g} \varepsilon(j, \alpha)(g)\, \mathrm{per}\big(\mathrm{hand}(e_Q(j)\Psi_1, e_Q(j+1)\Psi_2, \varphi; g, q_1, q_2),\ R(q_2) f\big)$$
has the iterated quotient integral
$$c_Q(j) \sum_{\gamma} \sum_{\beta} \mathrm{per}\Big(\mathrm{bl}\big(\varphi, d_Q(j, \alpha, \gamma), d_Q(j+1, \gamma, \beta), \mathrm{ctr}(\Psi_1, \Psi_2)\big),\ \varepsilon(j+2, \beta) \cdot f\Big).$$

Lean: `GlobalTheory.QLawPf.oneChart`.

*Proof.* The matching characters of the pin give a double step $S$ for the position, and each local datum $Q_i$ with the index $\alpha_i$ gives a split place datum of $S$ in the sense of [the last section](/entry/val-q/).

1. *Normalisations.* At each $q_i$, an element stabilises the lattice $N_{j+1}$ (or $N_{j+2}$) if and only if it is integral for the local datum. So the measures are normalised as in the theorem on finitely many places.
2. *The double step.* Apply [the theorem on finitely many split places](/entry/val-q/) with the coefficients $c_1 = c_2 = \delta_0$, which are away from every place, the theta functions $\Psi_1, \Psi_2$, which are vacuum for each local datum, $\varphi$ and $f$, which is typed at each $q_i$ by the pin, and $g = h_1 = h_2 = 1$.
3. *The weight.* Multiply the iterated integral by the constant $\prod_i \mathrm{wt}_i(\alpha_i)$.
4. *The integrand.* By the pin, $\varepsilon(j, \alpha)$ is this weight times the convolution of the local one chart elements, and $e_Q(j)$, $e_Q(j+1)$ are the convolutions of the local operators. By the compatibility of the Weil representations, the see-saw lift is the value of the double step. So the integrand of step 3 is the function of the theorem.
5. *The value.* The product of the local volumes is $c_Q(j)$, by the pin and the values of the local indices. The sums over the products of the local index sets are the sums over $\gamma \in \mathrm{Ch}_{j+1}$ and $\beta \in \mathrm{Ch}_{j+2}$, through the bijections of the pin. The local weights of $\gamma$ and $\beta$ combine with the convolutions of the local coefficients to give $d_Q(j, \alpha, \gamma)$, $d_Q(j+1, \gamma, \beta)$ and $\varepsilon(j+2, \beta)$. The scalars pass through the bi-combination, the translation, the lift and the period, which are linear. So the value of step 3 is the value of the theorem. $\square$

**Theorem 2.9.4 (Iterated integral law for pinned decorations).** Assume the standing conditions. If $w$ is pinned, then $w$ satisfies the iterated integral law.

Lean: `GlobalTheory.QLawPf.qLaw_of_pin` (also `GlobalTheory.T.seeSawIteratedIntegralLaw_at_twist_of_factorisation`, a second name).

*Proof.* Fix the data of the law. The pin gives characters for the position, and the theorem on one chart applies to each $\alpha \in \mathrm{Ch}_j$. A finite sum of functions with iterated quotient integrals has the sum of the values as its iterated quotient integral, so the function of the law has the iterated integral
$$c_Q(j) \sum_{\alpha} \sum_{\gamma} \sum_{\beta} \mathrm{per}\big(\mathrm{bl}(\varphi_\alpha, d_Q(j, \alpha, \gamma), d_Q(j+1, \gamma, \beta), \mathrm{ctr}(\Psi_1, \Psi_2)),\ \varepsilon(j+2, \beta) \cdot f\big).$$
Move the sum over $\beta$ outside. Each lift $\mathrm{bl}(\cdots)$ is a continuous automorphic function, since the coefficients of a pinned decoration are finite combinations. The period is additive in its first argument on continuous automorphic functions, so the inner double sum moves inside the period. This is the value of the law. $\square$

The admissible sets $F_X(j, \alpha)$ play no role in this proof: only the continuity of the $\varphi_\alpha$ is used.

**Theorem 2.9.5 (Laws for decorations pinned up to roots of unity).** Assume the standing conditions. If $w$ is pinned up to roots of unity, then $w$ satisfies the iterated integral law, the last step law and the finite cell law.

Lean: `GlobalTheory.QTw.laws_of_pin_resc` (also `GlobalTheory.T.seeSawTwistPlaceLaws_of_rootOfUnityRescaling`, a second name).

*Proof.* Write $w = w_0^s$ with $w_0$ pinned and each $s(j, \alpha)$ a root of unity; in particular $s(j, \alpha) \neq 0$. Let $w_0'$ be $w_0$ with every set $F_X(j, \alpha)$ replaced by the set of all functions. The pin does not involve these sets, so $w_0'$ is also pinned. For pinned decorations we have three laws: the iterated integral law by the last theorem, [the last step law](/entry/see-saw-iterated-integral-law-last-steps-of-local-factorisation/) and the finite cell law, both proved later in this chapter. Apply them to $w_0'$ and to $w_0$.

1. *The iterated integral law for $w$.* Given $\varphi_\alpha$, apply the law for $w_0'$ to the functions $s(j, \alpha)\varphi_\alpha$; this is allowed since $F_X$ of $w_0'$ contains every function, and $s(j, \alpha) \varphi_\alpha$ is still continuous automorphic. On the left, $s(j, \alpha)$ moves from $\varphi_\alpha$ to $\varepsilon(j, \alpha)$, which gives $\varepsilon^s(j, \alpha)$. On the right, for each $\beta$,
$$\begin{aligned} &\sum_{\alpha, \gamma} \mathrm{bl}(\varphi_\alpha, d_Q^s(j, \alpha, \gamma), d_Q^s(j+1, \gamma, \beta), \Theta) \\ &\quad = s(j+2, \beta)^{-1} \sum_{\alpha, \gamma} \mathrm{bl}(s(j, \alpha)\varphi_\alpha, d_Q(j, \alpha, \gamma), d_Q(j+1, \gamma, \beta), \Theta),\end{aligned}$$
since the factors $s(j+1, \gamma)$ cancel; this uses $s(j+1, \gamma) \neq 0$. The factor $s(j+2, \beta)^{-1}$ cancels against $\varepsilon^s(j+2, \beta) = s(j+2, \beta)\, \varepsilon(j+2, \beta)$.
2. *The last step law for $w$.* The same computation, with $\varepsilon_T$ in place of $\varepsilon$ at the top.
3. *The finite cell law for $w$.* The law for $w_0$ gives $K_1$ and $T_1$. The operators $e_Q$ are not rescaled, and the support of $\varepsilon^s(j, \alpha)$ is contained in the support of $\varepsilon(j, \alpha)$. So the same $K_1$ and $T_1$ work. $\square$

The proof uses only that the numbers $s(j, \alpha)$ are not zero. The condition that they are roots of unity gives in addition that the rescaled coefficients have the same absolute values as the pinned ones.

**Remark 2.9.6 (Formalization).** The theorem on one chart and the iterated integral law are at [SeeSawIteratedIntegralLawAtTwistOfFactorisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawIteratedIntegralLawAtTwistOfFactorisation.lean#L229) (lines 229 and 310), and the rescaled laws at [SeeSawTwistPlaceLawsOfRootOfUnityRescaling.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawTwistPlaceLawsOfRootOfUnityRescaling.lean#L15). The three laws are defined in [PlaceLaws.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PlaceLaws.lean#L228), the pin in [CosInj.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/CosInj.lean#L152), the rescaling and the pin up to roots of unity in [RescOne.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/RescOne.lean#L9), and the rescaling lemmas of steps 1 to 3 in [CombSmulLeft.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/CombSmulLeft.lean#L165). The lemma that the rescaled coefficients keep their absolute values is at line 181 of that file; the proof does not call it, so the root of unity condition is stronger than what the proof needs. The iterated integral law for pinned decorations does not use the validity of the tuple $t$. The theorem on one chart uses the theorem on finitely many places only at $g = h_1 = h_2 = 1$ and $c_1 = c_2 = \delta_0$. We have read the statements, not the proofs, of the lemmas on the normalisation of the measures, the vacuum of the local data, the see-saw lift as a double step value, the continuity of the lifts, the additivity of the period, the finite sums of iterated integrals, and the last step and finite cell laws for pinned decorations. We have not unfolded the see-saw data $c$, $v$, $t$ and their validity conditions, the compatibility of the Weil representations, the see-saw lift, the contracted theta function, the period, the vacuum condition and the local one chart elements; their descriptions above follow their names and the statements that use them.
