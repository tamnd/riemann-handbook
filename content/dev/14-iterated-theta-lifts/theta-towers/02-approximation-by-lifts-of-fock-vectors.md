---
title: Approximation by lifts of Fock vectors
decls:
  - GlobalTheory.CuspPureApprox.exists_sum_approx_pure_cusp_form
  - GlobalTheory.T.pure_cusp_form_approx_of_twist
  - GlobalTheory.CuspApproxX.cusp_form_approx_by_lift_of_type
  - GlobalTheory.T.cusp_forms_approximated_by_theta_lifts
  - GlobalTheory.CuspTypeApproxX.cuspType_lift_approx_fockSpace
  - GlobalTheory.T.cusp_type_approximation_by_fock_lift
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Approximation by lifts of Fock vectors

This section proves that the theta lift of a cusp form, with any theta function, is close on compact sets to a finite sum of theta lifts with Fock vectors. A property that holds for lifts with Fock vectors and that is stable under such limits then holds for all lifts. The next section uses this to pass cuspidality and the archimedean type from Fock vectors to all theta functions, in [Theorem 3.3.4](/entry/cuspidal-lift-smooth-at-of-cuspidal-lift/). The proof has three steps: weighted approximation of a cusp form by finite sums, a bound for the theta kernel, and the density of lifts with Fock vectors.

We keep the notation of [the previous section](/entry/k-finite-cusp-form-eq-sum-values/): $R$ is a real datum that meets the base conditions of the rows, $G$ is a grid for $R$ whose arrows meet the grid conditions, and $M_{ij}$ is the discrete series model at the node $(i, j)$. We fix the local inputs of [ThetaLocalInputs](/step/theta-local-inputs-def/).

**Definition 3.2.1 (Height function).** For a Hermitian space $V$ of the grid, the height function $\mathrm{ht}_V$ is a positive function on $G_V(\mathbb A)$ attached to the quotient by $G_V(F)$. We say that a function $\varphi$ on $G_V(\mathbb A)$ is rapidly decreasing if $\varphi \cdot \mathrm{ht}_V^a$ is bounded for every $a \ge 0$.

We have not unfolded the height function. It plays the role of a norm on a Siegel domain, and the cusp forms are rapidly decreasing for it by the input on [cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms) of rapid decay.

**Theorem 3.2.2 (Weighted approximation of a cusp form).** Let $0 \le i, j \le m$, and let $\varphi$ be a cusp form of the type of the node $(i, j)$. Let $a \ge 0$ be an integer and $\delta > 0$. Then there are $n \ge 0$, admissible maps $T_1, \ldots, T_n$ on $\mathrm{Vec}(M_{ij})$ and vectors $v_1, \ldots, v_n$ with

$$\Bigl| \varphi(g) - \sum_{l = 1}^n T_l(v_l)(g) \Bigr| \cdot \mathrm{ht}_{V_{ij}}(g)^a \le \delta \qquad \text{for all } g \in G_{V_{ij}}(\mathbb A).$$

Lean: `GlobalTheory.CuspPureApprox.exists_sum_approx_pure_cusp_form` (also `GlobalTheory.T.pure_cusp_form_approx_of_twist`, a second name).

*Proof.* The $K$-finite cusp forms of the type of the node are dense for the weighted norm $\sup_g |f(g)|\, \mathrm{ht}(g)^a$: there is a $K$-finite cusp form $\psi$ of the same type with $|\varphi(g) - \psi(g)|\, \mathrm{ht}(g)^a \le \delta$ for all $g$. This density comes from the local inputs; we have not opened its proof. By [Theorem 3.1.6](/entry/k-finite-cusp-form-eq-sum-values/), $\psi = \sum_l T_l(v_l)$ with admissible maps $T_l$. $\square$

Now fix a right arrow $(i, j) \to (i + 1, j)$ of the grid, with $i < m$. The arrow carries a Weil representation $\omega$ of $G_{V_{ij}}(\mathbb A) \times G_{V_{i+1,j}}(\mathbb A)$, as in [the Weil representation](/learn/theta/#the-weil-representation). For each index $t$ there is a Haar measure $\nu_t$ on $G_{V_{ij}}(\mathbb A)$ and a fundamental domain $\mathcal F_t$ for $G_{V_{ij}}(F)$. For a theta function $\Phi$ of the arrow, let $\theta_\Phi(h, g)$ be the [theta kernel](/learn/theta/#theta-kernels) at $h \in G_{V_{i+1,j}}(\mathbb A)$ and $g \in G_{V_{ij}}(\mathbb A)$. For a function $\varphi$ on $G_{V_{ij}}(\mathbb A)$ put

$$\Theta_\Phi(\varphi)(h) = \int_{\mathcal F_t} \theta_\Phi(h, g)\, \varphi(g)\, d\nu_t(g),$$

the [global theta lift](/learn/theta/#the-global-theta-lift), when the integrand is integrable.

Let $\mathrm{Vec}^{\mathrm{sm}}(M_{ij})$ be the space of smooth global vectors of the model, the tensor product of the local spaces. Let $\mathcal C_{ij}$ be the span of the linear maps $F$ from $\mathrm{Vec}^{\mathrm{sm}}(M_{ij})$ to functions on $G_{V_{ij}}(\mathbb A)$ that are the linear extension of an admissible multilinear map. We call $\mathcal C_{ij}$ the space of cusp families of the node.

**Theorem 3.2.3 (Approximation of a lift).** Assume that theta lifts with Fock vectors keep cusp forms (the condition of [the next section](/entry/cuspidal-lift-smooth-at-of-cuspidal-lift/)), and that the datum meets the size conditions. Let $i < m$ and $j \le m$, let $t$ be an index, $\Phi$ a theta function of the arrow $(i, j) \to (i + 1, j)$, and $\varphi$ a cusp form of the type of the node $(i, j)$ such that $g \mapsto \theta_\Phi(h, g)\varphi(g)$ is integrable on $\mathcal F_t$ for every $h$. Let $C \subseteq G_{V_{i+1,j}}(\mathbb A)$ be compact and $\varepsilon > 0$. Then there are $n \ge 0$, cusp families $F_1, \ldots, F_n \in \mathcal C_{ij}$ and smooth vectors $v_1, \ldots, v_n$ such that each $g \mapsto \theta_\Phi(h, g) F_l(v_l)(g)$ is integrable on $\mathcal F_t$ for every $h$, and

$$\Bigl| \Theta_\Phi(\varphi)(h) - \sum_{l = 1}^n \Theta_\Phi\bigl(F_l(v_l)\bigr)(h) \Bigr| < \varepsilon \qquad \text{for all } h \in C.$$

Lean: `GlobalTheory.CuspApproxX.cusp_form_approx_by_lift_of_type` (also `GlobalTheory.T.cusp_forms_approximated_by_theta_lifts`, a second name).

*Proof.* The theta kernel has polynomial growth: there are $K \in \mathbb R$ and an integer $a \ge 0$ such that

$$|\theta_\Phi(h, g)| \le |K|\, \mathrm{ht}_{V_{ij}}(g)^a \qquad \text{for } h \in C,\ g \in G_{V_{ij}}(\mathbb A).$$

The fundamental domain has finite volume $\mathrm{vol} = \nu_t(\mathcal F_t)$. Put $\delta = \varepsilon / \bigl(2 (|K| + 1)(\mathrm{vol} + 1)\bigr)$. [Theorem 3.2.2](/entry/exists-sum-approx-pure-cusp-form/) with this $a$ and $\delta$ gives admissible maps $T_l$ and vectors $v_l$. Let $F_l$ be the linear extension of $T_l$ and take the pure tensor of $v_l$ as the smooth vector, so that $F_l(v_l) = T_l(v_l)$. Each $T_l(v_l)$ is a cusp form, so it is rapidly decreasing, and the growth bound makes its integrand integrable. For $h \in C$ and $g \in \mathcal F_t$ we get

$$\Bigl| \theta_\Phi(h, g) \Bigl( \varphi(g) - \sum_l T_l(v_l)(g) \Bigr) \Bigr| \le |K|\, \delta.$$

Integrate over $\mathcal F_t$. The difference of the lifts is at most $|K|\, \delta\, \mathrm{vol} \le \varepsilon / 2 < \varepsilon$. $\square$

The last step replaces the theta function $\Phi$ by Fock vectors. A Fock vector of the arrow is a vector $f$ in the finite part of the Fock model of $\omega$, as in [the Fock model](/learn/theta/#the-fock-model). For a Fock vector $f$ and a polynomial $p$ on the arrow, $\mathrm{fock}(f, p)$ is the theta function built from $f$ and $p$. We have not unfolded this construction.

**Theorem 3.2.4 (Approximation by lifts of Fock vectors).** Assume the hypotheses of [Theorem 3.2.3](/entry/cusp-form-approx-by-lift-of-type/), with $\delta > 0$ in place of $\varepsilon$. Then there are $n \ge 0$, Fock vectors $f_1, \ldots, f_n$, polynomials $p_1, \ldots, p_n$, cusp families $F_1, \ldots, F_n \in \mathcal C_{ij}$ and smooth vectors $v_1, \ldots, v_n$ with

$$\Bigl| \Theta_\Phi(\varphi)(h) - \sum_{l = 1}^n \Theta_{\mathrm{fock}(f_l, p_l)}\bigl(F_l(v_l)\bigr)(h) \Bigr| < \delta \qquad \text{for all } h \in C.$$

Lean: `GlobalTheory.CuspTypeApproxX.cuspType_lift_approx_fockSpace` (also `GlobalTheory.T.cusp_type_approximation_by_fock_lift`, a second name).

*Proof.* Apply [Theorem 3.2.3](/entry/cusp-form-approx-by-lift-of-type/) with $\delta / 2$. It gives $m'$ terms $F_k(v_k)$ with an error less than $\delta / 2$ on $C$. Next use the density of lifts with Fock vectors: for each $k$ there are Fock vectors $f_{k,q}$ and polynomials $p_{k,q}$, $1 \le q \le n_k$, with

$$\Bigl| \Theta_\Phi\bigl(F_k(v_k)\bigr)(h) - \sum_{q = 1}^{n_k} \Theta_{\mathrm{fock}(f_{k,q}, p_{k,q})}\bigl(F_k(v_k)\bigr)(h) \Bigr| < \frac{\delta}{2(m' + 1)}$$

for $h \in C$. This density comes from the local inputs; we have not opened its proof. Index the pairs $(k, q)$ by one index $l$, with $n = \sum_k n_k$, and repeat $F_k$ and $v_k$ for each $q$. The triangle inequality gives an error less than $\delta/2 + m' \delta / (2(m' + 1)) < \delta$. $\square$

**Remark 3.2.5 (Formalization).** The second theorem is a general lemma applied to the first theorem as its approximation input. That lemma takes the condition that lifts with Fock vectors keep cusp forms and the size conditions on the datum, and uses neither ([CuspFormsApproximatedByThetaLifts.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/CuspFormsApproximatedByThetaLifts.lean#L18), the arguments `_hL` and `_hS`). In the third theorem these two conditions go only to the density of lifts with Fock vectors. The height function, the cusp families and the Fock vectors are not unfolded here.
