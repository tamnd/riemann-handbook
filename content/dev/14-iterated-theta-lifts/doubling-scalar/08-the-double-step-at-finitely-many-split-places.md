---
title: The double step at finitely many split places
decls:
  - GlobalTheory.T.doubleStep_adelicIntegral_finiteTwistPlaces
  - GlobalTheory.QVal.valQ
  - GlobalTheory.QVal.valQr_succ
  - GlobalTheory.T.iteratedInnerIntegral_at_first_of_splitPlaces
  - GlobalTheory.QValInner.innerVal_iter2
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The double step at finitely many split places

A [see-saw](/learn/theta/#seesaw-pairs) argument for two consecutive steps of a theta chain leads to an iterated integral over two quotient groups at a finite set of split places. At one split place this integral is computed by a local law, proved in a later part of this chapter. This section passes from one place to finitely many: the iterated integral at $r$ split places is the product of the $r$ local laws, in the sense that the coefficients, weights and volumes of the places multiply. The proof is an induction on $r$ that peels off one place at a time with Fubini's theorem for quotient integrals. The result is used in [the section on see-saw laws](/entry/one-chart/), where it is applied to one chart at the twist places.

**Setting.** Fix an additive character $\psi$ of the adeles of the standard kind and an integer $\sigma \geq 0$. A *double step* $S$ consists of hermitian spaces $B$, $J$, $B'$ and smaller spaces $B_A$, $J_0$, $B'_A$, the Weil representations of the two dual pairs $(U(B), U(J))$ and $(U(J), U(B'))$, a Jacobi subgroup $R_1$ of $U(J)$ and a Bessel subgroup $R_2$ of $U(B')$. For coefficients $c_1, c_2$ (finite combinations of points of the small spaces), theta functions $f_1, f_2$, an automorphic function $\varphi$ on $U(B_A)$, an automorphic function $f$ on $U(B')$, and points $g, h_1, h_2$ of the three adelic groups, the double step has a *value* $\mathrm{val}(c_1, c_2, f_1, f_2, \varphi, f; g, h_1, h_2) \in \mathbb{C}$. It is a period over $U(B')$ of a lift of $\varphi$ by the two Weil representations, paired with the right translate of $f$ by $h_2$.

**Definition 2.8.1 (Split place data).** A *split place datum* $Q$ of $S$ consists of:

- a finite place $q$ of $E$ over a split place $v$ of $F$, with local field $k = F_v$, the Haar measure of $k$ with $\mathcal{O}$ of volume one, and a local character of conductor one;
- integers $n_0, n_1, n_2, c$ and homomorphisms $\mathrm{gl}_0, \mathrm{gl}_1, \mathrm{gl}_2$ from $\mathrm{GL}_{n_0+c+3}(k)$, $\mathrm{GL}_{n_1+c+2}(k)$ and $\mathrm{GL}_{n_2+c+1}(k)$ to the three adelic groups, which are local at $q$;
- local data: a finite combination $e_0$ of elements of $\mathrm{GL}_{n_0+c+3}(k)$, operators $D_1, D_2$ on theta functions, finite index sets $A_1, A_2$ with weights $w_1, w_2$, coefficients $d_1(\gamma)$ and $d_2(\gamma, \beta)$, finite combinations $e_2(\beta)$ of elements of $\mathrm{GL}_{n_2+c+1}(k)$, and a volume $\mathrm{vol}_J$.

A family $Q_1, \dots, Q_r$ of split place data has *distinct places* if the places $v_i$ are distinct. Its *integrand* is the function of $x \in U(J)(\mathbb{A})$ and $y \in U(B')(\mathbb{A})$
$$I(x, y) = \sum_{a} E(a)\, \mathrm{val}\big(c_1, c_2, D_1 f_1, D_2 f_2, \varphi, f;\ g a,\ h_1 x,\ h_2 y\big),$$
where $E = e_0^{(1)} * \dots * e_0^{(r)}$ is the convolution of the images of the $e_0$ under $\mathrm{gl}_0$, and $D_1$, $D_2$ stand for the composites of the operators of the places. Its *value* is
$$\begin{aligned} V = \prod_{i=1}^r \mathrm{vol}_{J,i} \sum_{\gamma, \beta} \prod_{i=1}^r w_1(\gamma_i)\, w_2(\beta_i) \cdot \mathrm{val}\big(&c_1 * d_1(\gamma_1) * \dots * d_1(\gamma_r),\ c_2 * d_2(\gamma_1, \beta_1) * \dots, \\ &f_1, f_2, \varphi,\ e_2(\beta) \cdot f;\ g, h_1, h_2\big), \end{aligned}$$
where $\gamma = (\gamma_i)$ and $\beta = (\beta_i)$ run over the products of the index sets, and $e_2(\beta) \cdot f$ is the translate of $f$ by the convolution of the $e_2(\beta_i)$.

For a closed subgroup $R$ of a group $G$ with Haar measures $\rho$ and $\mu$, write $\int_{R \backslash G} u = z$ if $u$ has the quotient integral $z$ in the $L^1$ sense. A function $I(x, y)$ has the *iterated quotient integral* $z$ if there is $u_1$ with $\int_{R_1 \backslash G_1} u_1 = z$ and $\int_{R_2 \backslash G_2} I(x, \cdot) = u_1(x)$ for every $x$.

**Theorem 2.8.2 (Double step at finitely many split places).** Let $Q_1, \dots, Q_r$ be split place data of $S$ with distinct places, and let $G_1$, $G_2$ be the subgroups of $U(J)(\mathbb{A})$ and $U(B')(\mathbb{A})$ supported at these places. Let $\mu_1, \mu_2$ be Haar measures on $G_1, G_2$ and $\rho_1, \rho_2$ Haar measures on $R_1 \cap G_1$, $R_2 \cap G_2$, all giving volume one to the elements that are integral at every place $q_i$. Assume that $c_1, c_2$ are away from every $q_i$; that $f_1, f_2$ are theta functions which are vacuum vectors at every $q_i$; that $\varphi$ and $f$ are continuous automorphic functions, with $f$ of the right type at every $q_i$; and that $g, h_1, h_2$ are integral at every $q_i$. Then $I$ has the iterated quotient integral $V$ over $R_1 \cap G_1 \backslash G_1$ and $R_2 \cap G_2 \backslash G_2$.

Lean: `GlobalTheory.QVal.valQ` (also `GlobalTheory.T.doubleStep_adelicIntegral_finiteTwistPlaces`, a second name).

*Proof.* We prove the statement for a fixed number $r$ of places by induction on $r$. For $r = 0$ it is a lemma on the empty family, where the groups are trivial and the products and convolutions are empty. The step from $r$ to $r+1$ is the next theorem. $\square$

**Theorem 2.8.3 (Adding one split place).** If the last theorem holds for every family of $r$ split place data, then it holds for every family of $r + 1$ split place data.

Lean: `GlobalTheory.QVal.valQr_succ`.

*Proof.* Let $Q_0, \dots, Q_r$ have distinct places. Write $G_1 = G_1' \times G_{1,0}$ and $G_2 = G_2' \times G_{2,0}$, where $G_{i,0}$ is the local group at $q_0$ and $G_i'$ is the group at the other $r$ places.

1. *Reduction of the period groups.* A lemma on the family of split places reduces the iterated integral over $G_1, G_2$ to an iterated integral over the products: it gives Haar measures $m_1, m_2$ on the local groups at $q_0$, and $s_1, s_2$ on the local Jacobi and Bessel subgroups, each with the integral elements of volume one; Haar measures with the same normalisation at the other $r$ places; and it shows that the iterated quotient integral over $G_1, G_2$ follows from the iterated quotient integral over the products.
2. *Compact open levels.* The integral elements at the $r$ places form compact open subgroups of $G_1'$ and $G_2'$, and the same holds at $q_0$.
3. *Invariance.* The integrand is invariant under these compact open subgroups at the $r$ places.
4. *Finiteness.* For each $x$, the integrand is supported on finitely many double cosets.
5. *The inner integral.* For fixed points $x', y'$ at the $r$ places, the integral over the local groups at $q_0$ is the inner value of $x', y'$, by the next theorem.
6. *The outer integral.* The inner value is the integrand of the $r$ places $Q_1, \dots, Q_r$, with the coefficients $c_1 * d_1(\gamma_0)$, $c_2 * d_2(\gamma_0, \beta_0)$ and the translate $e_2(\beta_0) \cdot f$, summed against the weights of $Q_0$. By the induction hypothesis its iterated integral over $G_1', G_2'$ is $V$.
7. *Assembly.* Fubini's theorem for quotient integrals on a product of groups, with the facts of steps 2 to 4, combines steps 5 and 6 into the iterated integral over the products, with the value $V$. By step 1 this proves the claim. $\square$

For the inner integral, let $Q_0, \dots, Q_r$ have distinct places, let $I$ be the integrand of the whole family and let $I'$ be the integrand of $Q_1, \dots, Q_r$. The *inner value* at points $x, y$ supported at $q_1, \dots, q_r$ is
$$\mathrm{in}(x, y) = \mathrm{vol}_{J,0} \sum_{\gamma \in A_1} \sum_{\beta \in A_2} w_1(\gamma)\, w_2(\beta)\, I'_{\gamma, \beta}(x, y),$$
where $I'_{\gamma, \beta}$ is formed with the coefficients $c_1 * d_1(\gamma)$, $c_2 * d_2(\gamma, \beta)$ and the translate $e_2(\beta) \cdot f$, all from $Q_0$.

**Theorem 2.8.4 (Inner integral at the first place).** Let $Q_0, \dots, Q_r$ be split place data with distinct places, and assume the hypotheses of the theorem on finitely many places. Let $m_1, m_2$ be Haar measures on the local groups at $q_0$, and $s_1, s_2$ Haar measures on the local Jacobi and Bessel subgroups, all giving volume one to the integral elements. Let $x$ and $y$ be supported at $q_1, \dots, q_r$. Then the function $(x_0, y_0) \mapsto I(x\, \mathrm{gl}_1(x_0),\ y\, \mathrm{gl}_2(y_0))$ has the iterated quotient integral $\mathrm{in}(x, y)$ over the local groups at $q_0$.

Lean: `GlobalTheory.QValInner.innerVal_iter2` (also `GlobalTheory.T.iteratedInnerIntegral_at_first_of_splitPlaces`, a second name).

*Proof.* Let $E'$ be the convolution of the $e_0$ of $Q_1, \dots, Q_r$, and let $f_1', f_2'$ be the theta functions $f_1, f_2$ after the operators of $Q_1, \dots, Q_r$.

1. *Separation of the places.* The places $q_1, \dots, q_r$ are not $q_0$. So every element in the support of $E'$ is integral at $q_0$, and it commutes with the image of $\mathrm{gl}_0$. Also $x$, $y$ are integral at $q_0$. The points $g, h_1, h_2$ are integral at $q_0$, since they are integral at all the places.
2. *The vacuum at $q_0$.* The operators of the other places are finite, they are away from $q_0$, and they satisfy an orthogonality condition. A lemma shows that such operators keep the vacuum at $q_0$, so $f_1', f_2'$ are vacuum vectors at $q_0$.
3. *Expansion of the integrand.* Since the convolution and the operators of $Q_0$ commute with those of the other places,
$$I(x\, \mathrm{gl}_1(x_0),\ y\, \mathrm{gl}_2(y_0)) = \sum_{a'} E'(a')\, G_{a'}(x_0, y_0),$$
where $G_{a'}$ is the integrand of the single place $Q_0$, formed with $f_1', f_2'$ at the points $g a'$, $h_1 x$, $h_2 y$.
4. *The local law.* For each $a'$ in the support of $E'$, the points $g a'$, $h_1 x$, $h_2 y$ are integral at $q_0$, by step 1. So [the local law at one split place](/entry/split-place-double-step-local-iterated-integral-proof/) gives a function $u_{a'}$ with $\int G_{a'}(x_0, \cdot) = u_{a'}(x_0)$ and $\int u_{a'} = Z(a')$, where $Z(a')$ is the value of the single place $Q_0$ at the same points. That law uses the Haar measures of the datum $Q_0$; a lemma on invariant integrals over symmetric Haar subgroups shows that the same quotient integrals hold for $m_1, s_1$ and $m_2, s_2$.
5. *Summation.* By the definitions, $\mathrm{in}(x, y) = \sum_{a'} E'(a')\, Z(a')$. A finite sum of functions with quotient integrals has the sum of the integrals as its quotient integral; this is an induction on the finite set. Put $u = \sum_{a'} E'(a')\, u_{a'}$. Then $\int u = \mathrm{in}(x, y)$, and by step 3, $\int I(x\, \mathrm{gl}_1(x_0), y\, \mathrm{gl}_2(\cdot)) = u(x_0)$. $\square$

The induction removes the first place, and the inner theorem computes the removed place with the remaining places fixed. The order matters only for the bookkeeping of the coefficients: the coefficients of $Q_0$ are added first, then those of $Q_1, \dots, Q_r$.

**Remark 2.8.5 (Formalization).** The three theorems are at [DoubleStepAdelicIntegralFiniteTwistPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DoubleStepAdelicIntegralFiniteTwistPlaces.lean#L25) (lines 47 and 25) and [IteratedInnerIntegralAtFirstOfSplitPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/IteratedInnerIntegralAtFirstOfSplitPlaces.lean#L163). The split place datum is defined in [IsOneComb.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsOneComb.lean#L71), the statement for finitely many places at line 183 of the same file, the version with a fixed number $r$ of places, the integrand, the value and the inner value in [ValQOfValQr.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ValQOfValQr.lean#L73), and the iterated quotient integral in [ValLastX.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ValLastX.lean#L21). The statement for finitely many places names the set of places by a predicate that must equal the set of the $q_i$; the passage to the version with $r$ places substitutes it away, so the predicate carries no information. The finite sum lemma of step 5 is proved in the same file (line 123), and so is the support statement of step 1 (line 144). We have read only the statements of the lemmas behind the base case, steps 1 to 7 of the induction step, and steps 2 and 4 of the inner theorem. We have not unfolded the value of the double step, the Jacobi and Bessel subgroups, the conditions of being away, vacuum and typed, the operators $D_1, D_2$ and the quotient integral; the descriptions above follow their names and the statements that use them.
