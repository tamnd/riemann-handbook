---
title: The mean of theta null norms
decls:
  - GlobalTheory.Theta0MeanCore.core
  - GlobalTheory.Theta0MeanCore.theta0Mean
  - GlobalTheory.T.thetaZero_mean_log_norm_conjugates_of_weber
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The mean of theta null norms

This section bounds the mean, over the Galois conjugates of a CM lattice, of the logarithm of the norm of a normalised theta function. The norm is an $L^2$ norm on the torus, and it is the inverse of a [theta constant with characteristics](/learn/theta-functions-cm/#theta-functions-with-characteristics). The mean of the logarithms of the areas of the conjugate lattices is a class mean, of the kind of [the Chowla-Selberg formula](/learn/elliptic-curves/#the-chowla-selberg-formula). The quotients of the theta constants by $\eta$, raised to the power $12$, are the conjugates of one nonzero algebraic integer, so the sum of their logarithms is not negative. Together these give an upper bound by a Kronecker constant. The bounds are used in [the mean bound for the theta norms](/entry/theta0-mean-le-c/) of the rows chapter.

**Setting.** Let $D$ be a row datum whose host has an imaginary quadratic field $K$ with a prime number $d \geq 4$, and let $\chi$ be the quadratic character modulo $d$. Put
$$\beta(D) = \tfrac12 \Big( \log \sqrt{d} - \gamma + \frac{L'(1, \chi)}{L(1, \chi)} \Big),$$
where $\gamma$ is the Euler constant. The host also has two size numbers $r_E$ and $v$. For a lattice $\Lambda \subset \mathbb{C}$, let $H_\Lambda(z, w) = z \bar w / \mathrm{area}(\Lambda)$, where the area is the least positive value of $|\mathrm{Im}(\bar w_1 w_2)|$ for $w_1, w_2 \in \Lambda$. For $t_0 \in \mathbb{C}$, the *normalised theta function* $\vartheta_{\Lambda, t_0}$ is the translate by $t_0$, in the sense of $H_\Lambda$, of the odd theta function of $\Lambda$, divided by its value at $0$. Its *norm* is the mean over a fundamental domain $F$ of $\Lambda$:
$$N(\Lambda, t_0) = \frac{1}{\mathrm{vol}(F)} \int_F |\vartheta_{\Lambda, t_0}(z)|^2\, e^{-\pi H_\Lambda(z, z)}\, dz.$$

A *Hida setting* $(c, \delta, M, t)$ for $D$ is a curve ideal $c$ of $K$, a twelfth root $\delta$ of the discriminant of the ideal lattice, a number field $M \subset \mathbb{C}$ of degree $n$ that contains the data of the torsion datum of $(c, \delta)$, and for each embedding $\rho$ of $M$ a point $t(\rho)$. Let $\Lambda$ be the lattice of $(c, \delta)$ and $\Lambda^\rho$ its conjugate by $\rho$. We require $2 t(\rho) \in \Lambda^\rho$ and $\tfrac12(1 \pm i \sqrt{d})\, t(\rho) \notin \Lambda^\rho$. Write $N_\rho = N(\Lambda^\rho, t(\rho))$, and put
$$m = \frac1n \sum_\rho \log N_\rho, \qquad m^+ = \frac1n \sum_\rho \max(0, \log N_\rho).$$

We assume two groups of classical identities. The *lattice identities* say that for $\omega \neq 0$ and $\mathrm{Im}\, \tau > 0$, the lattice $\Lambda = \mathbb{Z}\omega + \mathbb{Z}\omega\tau$ has $\Delta(\Lambda) = (2\pi/\omega)^{12} \eta(\tau)^{24}$ and $\mathrm{area}(\Lambda) = |\omega|^2\, \mathrm{Im}\, \tau$. They also give the period in terms of $\eta$, the scaling of $\Delta$, and the agreement of the two definitions of $g_2$, $g_3$ and the Eisenstein series. The *Weber identities* say, for all $\tau$ in the upper half plane, that the differences of $\wp$ at the half periods are $\pi^2$ times the fourth powers of the theta constants, that $\theta_{00} \theta_{01} \theta_{10} = 2 \eta^3$, that $\theta_{00} = \eta\, \mathfrak{f}^2$, $\theta_{01} = \eta\, \mathfrak{f}_1^2$ and $\theta_{10} = \eta\, \mathfrak{f}_2^2$, and that $\mathfrak{f}^{24}$, $-\mathfrak{f}_1^{24}$ and $-\mathfrak{f}_2^{24}$ are the roots of $(X - 16)^3 - j X$.

**Theorem 2.27.1 (Core bound).** Assume the lattice identities and the Weber identities. Let $C_0 > 0$ with $|\theta_{ab}(0, \tau)| \leq C_0$ for all $a, b$ and all $\tau$ with $\mathrm{Im}\, \tau \geq \tfrac12$. Assume that $1728\, g_2^3$ of the lattice of $(c, \delta)$ is an algebraic integer for every curve ideal $c$ and every twelfth root $\delta$ of the discriminant. Then for every Hida setting of $D$:
$$m \leq \beta(D), \qquad m^+ \leq m + \tfrac14 \log d + \max(0, 2 \log C_0).$$

Lean: `GlobalTheory.Theta0MeanCore.core`.

*Proof.* We compute $\log N_\rho$ and $\log \mathrm{area}(\Lambda^\rho)$ in terms of a period basis.

1. *Class mean.* By the theorem on the mean covolume of conjugate lattices,
$$\frac1n \sum_\rho \log \mathrm{area}(\Lambda^\rho) = \log \pi + \gamma + \log \frac{2\pi}{\sqrt d} - \frac{L'(1, \chi)}{L(1, \chi)}.$$
2. *An integer.* By the theorem on twelfth powers, there is a nonzero algebraic integer $X \in M$ such that $|\rho X| = (|\theta_{ab}(0, \tau)| / |\eta(\tau)|)^{12}$ for every $\rho$, every period basis $(\omega, \omega\tau)$ of $\Lambda^\rho$, and every even characteristic $(a, b)$ with $\theta_{ab}(t(\rho)/\omega, \tau) = 0$. The norm of $X$ to $\mathbb{Q}$ is a nonzero integer, so $\sum_\rho \log |\rho X| \geq 0$.
3. *Period bases.* By the theorem on conjugate ideal lattices, each $\Lambda^\rho$ has discriminant $1$ and is $x \Lambda(c')$ for a nonzero ideal $c'$ and $x \neq 0$. So $\Lambda^\rho$ is stable under $\tfrac12(1 + i\sqrt d)$, and it has a basis $(\omega_\rho, \omega_\rho \tau_\rho)$ with $\tfrac12 \leq \mathrm{Im}\, \tau_\rho$ and $2\, \mathrm{Im}\, \tau_\rho \leq \sqrt d$. By the stability, $t(\rho) \notin \Lambda^\rho$.
4. *The norm.* By the theorem on the norms of theta nulls at $2$-torsion points, exactly one even characteristic $(a_\rho, b_\rho)$ has $\theta_{a_\rho b_\rho}(t(\rho)/\omega_\rho, \tau_\rho) = 0$, $N_\rho > 0$, and $N_\rho^{-1} = \sqrt{2\, \mathrm{Im}\, \tau_\rho}\ |\theta_\rho|^2$ with $\theta_\rho = \theta_{a_\rho b_\rho}(0, \tau_\rho)$. So
$$\log N_\rho = -\tfrac12 \log 2 - \tfrac12 \log \mathrm{Im}\, \tau_\rho - 2 \log |\theta_\rho|.$$
5. *The area.* Since $\Delta(\Lambda^\rho) = 1$, the lattice identities give
$$\log \mathrm{area}(\Lambda^\rho) = \log 4 + 2 \log \pi + \log \mathrm{Im}\, \tau_\rho + 4 \log |\eta(\tau_\rho)|.$$
6. *The integer again.* Step 2 gives $\log |\rho X| = 12 (\log |\theta_\rho| - \log |\eta(\tau_\rho)|)$, so $S_\theta \geq S_\eta$, where $S_\theta$ and $S_\eta$ are the sums over $\rho$ of $\log |\theta_\rho|$ and $\log |\eta(\tau_\rho)|$.
7. *The mean.* Let $S_y$ be the sum of $\log \mathrm{Im}\, \tau_\rho$. Steps 1 and 5 give $S_y + 4 S_\eta$. Insert it into the sum of step 4 and use step 6:
$$\begin{aligned} \sum_\rho \log N_\rho &= \tfrac{n}{2} \Big( \log \sqrt d - \gamma + \frac{L'(1, \chi)}{L(1, \chi)} \Big) + 2 (S_\eta - S_\theta) \\ &\leq n\, \beta(D). \end{aligned}$$
8. *Positive parts.* By step 4, $-\log N_\rho \leq \tfrac12 \log (2\, \mathrm{Im}\, \tau_\rho) + 2 \log C_0$, since $\mathrm{Im}\, \tau_\rho \geq \tfrac12$. With $2\, \mathrm{Im}\, \tau_\rho \leq \sqrt d$, this is at most $\tfrac14 \log d + \max(0, 2 \log C_0)$. Since $d \geq 1$, this number is not negative. So $\max(0, \log N_\rho) \leq \log N_\rho + \tfrac14 \log d + \max(0, 2 \log C_0)$. Sum over $\rho$ and divide by $n$. $\square$

**Theorem 2.27.2 (Theta null means).** Assume the lattice identities and the Weber identities. Then for every row datum $D$ and every Hida setting of $D$:

1. $m \leq \beta(D)$;
2. $m \leq L$ for every $L$ with $\log r_E + |L'(1, \chi)/L(1, \chi)| \leq 2L$;
3. $m \leq \tfrac12 L$ for every $L$ with $\log v + |L'(1, \chi)/L(1, \chi)| \leq L$;
4. $m^+ \leq \beta(D) + \tfrac14 \log d + C$, with $C = \max(0, 2 \log C_0) \geq 0$;
5. $m^+ \leq (1 + 2C)\, L$ for every $L$ as in item 3.

Here $C_0$ is a fixed bound for the even theta constants on $\mathrm{Im}\, \tau \geq \tfrac12$, and the constants do not depend on $D$.

Lean: `GlobalTheory.Theta0MeanCore.theta0Mean` (also `GlobalTheory.T.thetaZero_mean_log_norm_conjugates_of_weber`, a second name).

*Proof.* By the theorem on integral $j$ invariants, $1728\, g_2^3$ is integral for every row datum. The theta constants $\theta_{ab}(0, \tau)$ are bounded on $\mathrm{Im}\, \tau \geq \tfrac12$, which gives $C_0$. Then the core bound applies to every Hida setting.

1. This is the first core bound.
2. A comparison that uses $2 \sqrt d \leq r_E$ gives $\beta(D) \leq L$ under the condition of item 2.
3. We have $\sqrt d \leq v$ and $\gamma > \tfrac12$, so $\beta(D) \leq \tfrac12 L$ under the condition of item 3.
4. Add the two core bounds.
5. Under the condition of item 3, $\beta(D) \leq \tfrac12 L$ and $\tfrac14 \log d \leq \tfrac12 L$. Also $\log v \geq \tfrac12$, so $L \geq \tfrac12$ and $C \leq 2CL$. So $m^+ \leq L + 2CL$. $\square$

**Remark 2.27.3 (Formalization).** The two theorems are at [ThetaZeroMeanLogNormConjugatesOfWeber.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaZeroMeanLogNormConjugatesOfWeber.lean#L26), at lines 26 and 132. The second name is in [ThetaZeroMeanLogNormConjugatesOfWeberStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaZeroMeanLogNormConjugatesOfWeberStatement.lean#L13), by a `first | exact` block under one million heartbeats. The means, the Hida setting and $\beta(D)$ are in [SignedLogMeans.lean](lean:Development/AbelianVarietyTheory/BlockTheory/GlobalSignature/SignedLogMeans.lean#L23), and the five bounds are the conjunction at line 61. The two groups of identities are hypotheses, not theorems: they are the propositions at [PeriodPairAgreement.lean](lean:Development/AbelianVarietyTheory/BlockTheory/GlobalSignature/PeriodPairAgreement.lean#L36) and [ThetaConstantWeber.lean](lean:Development/AbelianVarietyTheory/BlockTheory/GlobalSignature/ThetaConstantWeber.lean#L95). The norm of theta nulls of step 4 is proved, and is stated at [JacobiThetaHalfCharacteristic.lean](lean:Development/AbelianVarietyTheory/BlockTheory/GlobalSignature/JacobiThetaHalfCharacteristic.lean#L20). The lemmas of steps 3 to 6 and of the second proof are in [IsPeriodLatticeIff.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/IsPeriodLatticeIff.lean#L27). The norm is in [LatticeIntegralCoordinates.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/LatticeIntegralCoordinates.lean#L280); it picks its fundamental domain by `Classical.epsilon`. The integrand is periodic, so the choice does not change the mean. The character $\chi$ is the Legendre symbol modulo the prime $d$ ([Numbers.lean](lean:Formalism/LocalToGlobal/Divisibility/Numbers.lean#L64)). The proof of the core bound uses the uniqueness of the even characteristic only as existence. Item 3 has the fixed constant $\tfrac12$, so its existential constant is trivial. We have read the statements, not the proofs, of the theorems on the class mean, twelfth powers, conjugate ideal lattices and integral $j$ invariants.
