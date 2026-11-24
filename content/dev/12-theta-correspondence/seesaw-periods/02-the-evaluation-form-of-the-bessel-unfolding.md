---
title: The evaluation form of the Bessel unfolding
decls:
  - GlobalTheory.Unf.evalBF_of_descent
  - GlobalTheory.T.bessel_period_evaluation_unfolding_of_witt_descent
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The evaluation form of the Bessel unfolding

The Bessel period of a theta lift unfolds to an integral of Fourier-Jacobi periods. In the first form of this identity, the theta function enters through a flat map: an integral of the mixed model over a unipotent group $U_X$. This section proves a second form, in which the theta function enters only through its value at one point of the mixed model, and the unipotent integral moves into the group of the outer integral. We assume that Weil data descend along Witt decompositions. The identity is one of the unfolding laws of the next section, and it feeds the chain of seesaw identities of the step [the nonempty hypotheses](/step/nonempty-hyps/). See [Bessel and Fourier-Jacobi periods](/learn/periods/#bessel-and-fourier-jacobi-periods) for the classical periods.

**Definition 7.2.1 (Descent of Weil data).** We say that Weil data descend if the following holds. Let $\omega$ be a Weil datum on $(S, T)$ with characters $\chi_S, \chi_T$. For every Witt decomposition $S = X \oplus S_0 \oplus Y$ there is a Weil datum on $(S_0, T)$ with the same characters, and for every Witt decomposition $T = X' \oplus T_0 \oplus Y'$ there is a Weil datum on $(S, T_0)$ with the same characters.

Let $S$ be a Hermitian space with a Witt decomposition of depth $\rho$, with basis $x_1, \dots, x_\rho$ of $X$. Let $N_S$ be the unipotent radical of the parabolic subgroup of $U(S)$ that fixes the flag $\langle x_1 \rangle \subset \langle x_1, x_2 \rangle \subset \dots \subset X$. For $n \in N_S(\mathbb{A})$ let $n_X \in M_\rho(\mathbb{A}_E)$ be its block on $X$; it is upper unitriangular. Put $\psi_E = \psi \circ \mathrm{Tr}_{\mathbb{A}_E/\mathbb{A}}$ and

$$\begin{aligned} \psi_N(n) &= \psi_E\Bigl(\sum_{i=1}^{\rho - 1} (n_X)_{i, i+1}\Bigr). \end{aligned}$$

Let $R_X \subset N_S$ be the subgroup of elements that fix $X$ pointwise.

**Definition 7.2.2 (Bessel level).** A Bessel level of depth $\rho$ is a Hermitian space $V$ with a Witt decomposition $V = X \oplus V_0 \oplus Y$ of depth $\rho$, an orthogonal decomposition $V_0 = A \oplus L$ with $L$ a line spanned by a rational vector $\zeta$ with $\langle \zeta, \zeta \rangle \neq 0$, such that $[U(A)]$ is compact, together with Haar measures and fundamental domains of volume one for $U(A)$ and $N_V$. The Bessel character of $n \in N_V(\mathbb{A})$ is

$$\begin{aligned} \psi_B(n) &= \psi_E\Bigl(\sum_{i=1}^{\rho - 1} (n_X)_{i, i+1} + c_\rho(n \zeta)\Bigr), \end{aligned}$$

where $c_\rho(n\zeta)$ is the coefficient of $x_\rho$ in $n \zeta$. The Bessel period of a function $f$ on $U(V)(\mathbb{A})$ against a function $\varphi$ on $U(A)(\mathbb{A})$ is

$$\begin{aligned} \mathcal{B}(\varphi, f) &= \int_{\mathcal{F}_A} \int_{\mathcal{N}_V} \varphi(h)\, f(n h)\, \overline{\psi_B(n)} \, dn \, dh, \end{aligned}$$

with $U(A)$ embedded in $U(V)$ through $A \subset V_0$. This is the period of [Gan, Gross and Prasad](/learn/periods/#bessel-and-fourier-jacobi-periods) over the Bessel subgroup $N_V \rtimes U(A)$.

**Definition 7.2.3 (Jacobi level and step).** A Jacobi level of depth $\rho$ is a Hermitian space $W$ with a Witt decomposition $W = X_W \oplus W_0 \oplus Y_W$ of depth $\rho$ such that $[U(W_0)]$ is compact, with Haar measures and fundamental domains of volume one for $U(W_0)$ and $N_W$. A step from a Bessel level $V$ to a Jacobi level $W$ of the same depth is a pair of Weil data $\omega$ on $(V, W)$ and $\omega_0$ on $(V_0, W_0)$, with Haar measures and fundamental domains of volume one for $U(W)$ and the unipotent groups that enter. The theta lift of a function $G$ on $U(W)(\mathbb{A})$ against a theta function $\Phi$ on $W(V, W)$ is

$$\begin{aligned} \theta(G, \Phi)(g) &= \int_{[U(W)]} \omega(g, h) \Phi(0)\, G(h) \, dh. \end{aligned}$$

The Fourier-Jacobi period $\mathcal{J}(\varphi, G', \Xi)$ of a function $G'$ on $U(W)(\mathbb{A})$, against $\varphi$ and a theta function $\Xi$ on $W(V_0, W_0)$, is the integral over $\mathcal{F}_{W_0} \times \mathcal{N}_W$ of $G'(n h)\, \overline{\psi_N(n)}$ times the theta kernel $\int_{\mathcal{F}_A} \varphi(h_0)\, K_\Xi(h_0, n, h)\, dh_0$ built from $\omega_0$ and $\Xi$.

**Definition 7.2.4 (Evaluation and flat maps).** For a theta function $\Psi$ on $W(V, W)$, let $\mathcal{M}_V$ be the mixed coordinate of the last section for the Witt decomposition of $V$, and $\mathcal{M}_W$ the analogous mixed coordinate for the Witt decomposition of $W$. Let $x_0$ be the matrix of the inclusion of $X_W$ in $W$, let $\ell$ be the last basis vector of $E^\rho$, and put $y_0 = -\zeta \ell^{t}$. The evaluation map is

$$\begin{aligned} \mathrm{ev}(\Psi) &= \mathcal{M}_W\bigl(\mathcal{M}_V \Psi(x_0)\bigr)(y_0), \end{aligned}$$

a function on $W(V_0, W_0)$. Let $U_X \subset \mathrm{GL}_\rho(\mathbb{A}_E)$ be the upper unitriangular group, with Haar measure of covolume one, and $\psi_U(u) = \psi_E(\sum_i u_{i, i+1})$. The flat map is

$$\begin{aligned} \flat(\Psi) &= \int_{U_X} \overline{\psi_U(u)}\; \mathcal{M}_W\bigl(\mathcal{M}_V \Psi(x_0 u)\bigr)(y_0) \, du. \end{aligned}$$

The flat map is the evaluation map averaged along the orbit of $x_0$ under $U_X$ against the generic character. It is the form in which the theta function appears when one unfolds the full group $N_W \rtimes U(W_0)$; the evaluation map appears when one unfolds only $R_X \rtimes U(W_0)$.

**Definition 7.2.5 (Quotient integral).** Let $G$ be a group with a measure $\mu_G$ and $R \subset G$ a subgroup with a measure $\mu_R$. A function $f$ on $G$ has quotient integral $z$ if there is an integrable function $F$ on $G$ such that $r \mapsto F(r h)$ is $\mu_R$-integrable for every $h$, $f(h) = \int_R F(r h)\, d\mu_R(r)$ for every $h$, and $z = \int_G F \, d\mu_G$.

This is the precise form of the statement $z = \int_{R \backslash G} f$, where the integrability is part of the claim.

**Theorem 7.2.6 (Evaluation form of the Bessel unfolding).** Assume that Weil data descend. Let a step from a Bessel level $V$ of depth $\rho$ to a Jacobi level $W$ of depth $\rho$ be given. Let $\varphi$ be a continuous automorphic function on $U(A)(\mathbb{A})$, $G$ a rapidly decreasing function on $U(W)(\mathbb{A})$, and $\Phi$ a theta function on $W(V, W)$. Let $\nu_0$ be a Haar measure on $R_X(\mathbb{A})$ and $\mathcal{N}_0$ a fundamental domain for $R_X(F)$ with $\nu_0(\mathcal{N}_0) = 1$. Let $\mu_R$ be the image of $\mu_{W_0} \times \nu_0$ under $(h, n) \mapsto n\, \iota_0(h)$. Then the function

$$\begin{aligned} h &\longmapsto \mathcal{J}\bigl(\varphi, G(\,\cdot\, h), \mathrm{ev}(\omega(1, h) \Phi)\bigr) \end{aligned}$$

on $U(W)(\mathbb{A})$ has quotient integral $\mathcal{B}(\varphi, \theta(G, \Phi))$ with respect to $\mu_R$ and the Haar measure of $U(W)$.

Lean: `GlobalTheory.Unf.evalBF_of_descent` (also `GlobalTheory.T.bessel_period_evaluation_unfolding_of_witt_descent`, a second name).

*Proof.* By descent there is a Weil datum on $(V_0, W)$ with the characters of the step. We use it to define the evaluation periods: the mixed coordinate of $V$ takes values in theta functions on $W(V_0, W)$, and these are the functions to which the second mixed coordinate applies. We start from the flat unfolding, which also follows from descent: the function $h \mapsto \mathcal{J}(\varphi, G(\,\cdot\, h), \flat(\omega(1, h)\Phi))$ has quotient integral $\mathcal{B}(\varphi, \theta(G, \Phi))$ with respect to the measure on the full group $N_W \rtimes U(W_0)$.

Next we compare the two kernels. The group $N_W$ is the product of $R_X$ and a copy of $U_X$, and the Haar measure on $N_W$ is the image of the product measure in unitriangular coordinates. The closed subgroups $N_W \rtimes U(W_0)$ and $N_V \rtimes U(A)$ carry the product of their Haar measures. The integrand of the evaluation period is continuous, and it is invariant under the rational points of $R_X \rtimes U(W_0)$. The flat period is the integral over $U_X$ of evaluation periods:

$$\begin{aligned} \mathcal{J}\bigl(\varphi, G', \flat(\Psi)\bigr) &= \int_{U_X} \mathcal{J}_{u}\bigl(\varphi, G', \mathrm{ev}(\Psi)\bigr)\, du, \end{aligned}$$

where $\mathcal{J}_u$ is the evaluation period with $x_0$ moved to $x_0 u$. The evaluation form is absolutely convergent, so Fubini applies. Finally, integration in stages along $N_W \rtimes U(W_0) = U_X \cdot (R_X \rtimes U(W_0))$ turns the integral over $U_X$ and the quotient by $N_W \rtimes U(W_0)$ into the quotient by $R_X \rtimes U(W_0)$ with the measure $\mu_R$. This gives the claimed quotient integral. $\square$

**Remark 7.2.7 (Formalization).** The Fourier-Jacobi kernel $K_\Xi$ is defined through an operator `opA` that this section does not unfold. The proof constructs an orthogonal decomposition with a zero line from the trivial lemma `nonempty_orthDec_zero` ([BesselPeriodEvaluationUnfoldingOfWittDescent.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/BesselPeriodEvaluationUnfoldingOfWittDescent.lean#L25)), and it proves s-finiteness of a $\sigma$-finite measure with a private lemma at line 33 that only restates an instance of Mathlib. The flat unfolding, the comparison of flat and evaluation periods and the integration in stages are the lemmas `besselPeriod_thetaLift_unfolding`, `flatPeriod_eq_integral_evaluationPeriods` and `invariant_integral_in_stages_alt`, which are not unfolded here.
