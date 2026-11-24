---
title: The unfolding laws of a chain
decls:
  - GlobalTheory.Unf.unfoldings_of_chain
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The unfolding laws of a chain

A chain of theta lifts climbs a tower of Hermitian spaces and alternates two kinds of periods: Bessel periods on the odd rungs and Fourier-Jacobi periods on the even rungs. Each rung is an unfolding identity, and the chain closes with a seesaw identity at the bottom. This section collects the eight laws that the chain uses and proves that they hold for every global datum. The result is the input of [the row chain unfolding](/entry/iter-chain/), which is used in the step [the nonempty hypotheses](/step/nonempty-hyps/). For the general method see [the global theta lift](/learn/theta/#the-global-theta-lift) and [theta towers](/learn/theta/#theta-towers).

We use the Bessel and Jacobi levels, the steps, the periods $\mathcal{B}$ and $\mathcal{J}$, and the flat and evaluation maps of the last section. A step in the other direction, from a Jacobi level of depth $\sigma + 1$ to a Bessel level of depth $\sigma$, has the same kind of data, with a flat map $\flat'$ taken at the last row of the mixed model instead of the point $(x_0, y_0)$.

**Definition 7.3.1 (The eight laws).** Fix a global datum. We consider the following statements, each for all levels, steps, automorphic functions and theta functions of the given kind.

1. Flat Bessel unfolding. For a step from a Bessel level to a Jacobi level, a continuous automorphic $\varphi$, a rapidly decreasing $G$ and a theta function $\Phi$, the function $h \mapsto \mathcal{J}(\varphi, G(\,\cdot\, h), \flat(\omega(1, h)\Phi))$ has quotient integral $\mathcal{B}(\varphi, \theta(G, \Phi))$ over the Fourier-Jacobi group $N_W \rtimes U(W_0)$.
2. Evaluation Bessel unfolding. The same with $\mathrm{ev}$ in place of $\flat$ and the group $R_X \rtimes U(W_0)$, as in the [Theorem 7.2.6](/entry/eval-bf-of-descent/).
3. Fourier-Jacobi unfolding. For a step from a Jacobi level $W$ of depth $\sigma + 1$ to a Bessel level $V$ of depth $\sigma$, a quasi-automorphic family $Y$ of theta functions on $W(W_0, L)$, a rapidly decreasing $G$ on $U(V)(\mathbb{A})$ and a theta function $\Phi$, the function $h \mapsto \mathcal{B}(\Theta_Y(\flat'(\omega(1, h)\Phi)), G(\,\cdot\, h))$ has quotient integral equal to the Fourier-Jacobi period of $\theta(G, \Phi)$ against $Y$. Here $\Theta_Y$ is the theta lift of the restricted theta function against $Y$.
4. Double step. For a step from a Bessel level of depth $\sigma + 1$ to a Jacobi level, followed by a step to a Bessel level of depth $\sigma$, the two unfoldings compose: the inner functions are automorphic, and the Bessel period of the double lift is a quotient integral of quotient integrals of the Bessel period at the lower level.
5. Last law. At depth $0$, the Bessel period of a double lift $\theta(\theta(F, \Phi_2), \Phi_1)$ equals an explicit integral $Q(\varphi, \Phi_1, \Phi_2, F)$ over the compact quotients.
6. Iterated unfolding. For a chain of steps with theta data, the iterated integral $Q$ of the chain computes the Bessel period of the top lift, whenever the chain is rapid.
7. Contraction law. For a double step, the contraction of the two theta functions over the line $L$ gives theta functions in each variable, and the composed theta lifts equal a double integral of two theta kernels against $\varphi$.
8. Last seesaw. The seesaw identity below holds.

**Definition 7.3.2 (Last seesaw identity).** Let $V_0 = A \oplus L$ and $X = T \oplus L''$ be orthogonal decompositions with $L$ and $L''$ lines, and let $\tau \colon L'' \to L$ be a linear map with $\tau^{*} J_L \tau = -\xi_0 \bar\xi_0\, J_{L''}$. Let $S$ be a Hermitian space. Let Weil data be given on $(V_0, S)$, $(A, S)$, $(L, S)$, $(S, X)$, $(S, T)$, $(S, L'')$, with characters $\chi_A \chi_z, \chi_A, \chi_z$ for the first factors on the left and $\chi_T \chi_z^{-1}, \chi_T, \chi_z^{-1}$ for the second factors on the right, and common characters $\chi_S$, $\chi_S'$ for $S$. For theta functions $\Xi$ on $W(V_0, S)$ and $\Phi_2$ on $W(S, T)$, and $u \in W(A, S)$, put $\Xi_u^{\tau}(w) = \Xi(u, \tau w)$ on $W(S, L'')$, through $W(V_0, S) = W(A, S) \oplus W(L, S)$. The last seesaw identity says: each $\Xi_u^{\tau}$ is a theta function, and for all $h_0 \in U(A)(\mathbb{A})$, $h \in U(S)(\mathbb{A})$ and $h' \in U(T)(\mathbb{A})$

$$\begin{aligned} \omega_T(h, h')\Phi_2(0)\cdot \omega_1(h_0, h)\,\Xi(0) &= \omega_A(h_0, h)\Bigl[u \mapsto \omega_X(h, h')\bigl(\Phi_2 \boxtimes \Xi_u^{\tau}\bigr)(0)\Bigr](0). \end{aligned}$$

Here $h_0$ acts through $U(A) \subset U(V_0)$, $h'$ acts through $U(T) \subset U(X)$, and $\Phi_2 \boxtimes \Xi_u^{\tau}$ is the function on $W(S, X) = W(S, T) \oplus W(S, L'')$. The two sides are the two ways to compute a theta kernel of the seesaw pair formed by $U(V_0) \supset U(A) \times U(L)$ and $U(S) \times U(S)$ with $U(X) \supset U(T) \times U(L'')$. This is the identity of [Kudla's seesaw](/learn/theta/#reductive-dual-pairs), written for theta kernels.

**Theorem 7.3.3 (The unfolding laws of a chain).** For every global datum the eight laws hold.

Lean: `GlobalTheory.Unf.unfoldings_of_chain`.

*Proof.* First, Weil data descend along Witt decompositions; this is proved for every datum earlier in the development. With descent, the flat Bessel unfolding, the Fourier-Jacobi unfolding, the double step and the iterated unfolding are separate theorems, each proved from descent. The evaluation Bessel unfolding is the [Theorem 7.2.6](/entry/eval-bf-of-descent/) applied to descent. The last law is Fubini's theorem for the double lift at depth $0$, where all quotients are compact. The contraction law is the computation of the composed lifts in the double step through two theta column lifts. The last seesaw identity is proved directly from the Weil data. $\square$

**Remark 7.3.4 (Formalization).** The law called `ContrLaw` is supplied by the lemma `doubleStep_eq_two_thetaColumnLifts`, and the law called `DoubleStep` by `besselPeriod_double_step_unfolding_of_descent`; the names cross ([UnfoldingsOfChain.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UnfoldingsOfChain.lean#L23)). The last law and the seesaw identity are proved without descent, by `doubleLiftPeriod_rankZero_fubini_compactQuotient` and `lastSeeSaw_thetaIdentity`. The descent itself is `weilDatum_descends_to_wittCore`. None of these lemmas is unfolded here, so the descriptions of the laws 3 to 7 stay at the level of their statements.
