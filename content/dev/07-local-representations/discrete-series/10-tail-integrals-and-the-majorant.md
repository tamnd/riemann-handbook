---
title: Tail integrals and the majorant for coefficients
decls:
  - ReciprocityTheory.ChartRestriction.DS.Xi.aStepBase_of
  - ReciprocityTheory.ChartRestriction.DS.Xi.StepA.inner_eq
  - ReciprocityTheory.ChartRestriction.DS.Xi.StepA.inner_c_le
  - ReciprocityTheory.ChartRestriction.DS.Xi.StepA.aStep_fin
  - ReciprocityTheory.ChartRestriction.DS.Xi.aStepSucc_of
  - ReciprocityTheory.ChartRestriction.DS.Xi.BL.inner_bound
  - ReciprocityTheory.ChartRestriction.DS.Xi.bStepSucc_of
  - ReciprocityTheory.ChartRestriction.DS.Xi.xiExists_of_in
  - ReciprocityTheory.ChartRestriction.DS.Xi.xiExists
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Tail integrals and the majorant for coefficients

This section constructs a function $\Xi$ on a unitary group $U(r+k, r+1)$ that dominates the convolution of two fast decaying functions and that is integrable along a unipotent subgroup against a character weight. The proof is an induction on $r$ through Heisenberg parabolic subgroups. The result is used in the step [the nonempty hypotheses](/step/nonempty-hyps/).

Background: [Haar measure](/learn/analysis/#haar-measure), [[Haar measure|VY0HXD3GC4]], [unitary groups](/learn/groups/#unitary-groups), [real reductive groups](/learn/real-groups/#real-reductive-groups).

### The setting

Fix integers $k \geq 1$ and $r \geq 0$, and put $n = 2r + k + 1$. Index the standard basis of $\mathbb{C}^n$ by $0, \dots, n-1$, write $e^*_a = e_{n-1-a}$ for $a < r$ and $w_j = e_{r+j}$ for $j \leq k$. Let $H = H_{k,r}$ be the Hermitian matrix with $H_{a, n-1-a} = H_{n-1-a, a} = 1$ for $a < r$, $H_{w_j w_j} = 1$ for $j < k$, $H_{w_k w_k} = -1$, and zeros elsewhere. Put $\langle v, w\rangle = w^* H v$ and $G = G_{k,r} = \{g : g^* H g = H\}$. Let $K = \{g \in G : g^*g = 1\}$, and let $N = N_{k,r}$ be the unipotent subgroup of the standard flag of isotropic vectors $e_0, \dots, e_{r-1}$. Let $\|g\|$ be the Frobenius norm. A *Haar measure on* a closed subgroup $S$ is a measure on matrices that is carried by $S$, is invariant under left and right translation by $S$, is finite on compact sets and is not zero.

Let $\varphi_a = e^*_a$ for $a < r$, $\varphi_r = (w_0 + w_k)/\sqrt{2}$, and $\varphi'_a = H\varphi_a$. For vectors $Y_0, \dots, Y_r$ let $\Gamma_l(Y)$ be the Gram determinant of $Y_0, \dots, Y_l$ for the standard inner product. For $s \in \mathbb{R}^{r+1}$ put
$$\Delta_l(x) = \Gamma_l(x\varphi)^{1/2}, \qquad \Xi_s(x) = \prod_{l=0}^{r} \Delta_l(x)^{-s_l},$$
$$D_l(g) = \det\bigl(\langle g\varphi'_b, \varphi'_a\rangle\bigr)_{a,b \leq l}, \qquad F_s(g) = \prod_{l=0}^{r} |D_l(g)|^{-s_l}.$$
Let $s^0_l = 2$ for $l < r$ and $s^0_r = k$. We say $s$ is *admissible* if $0 < s^0_l - s_l \leq 1/10$ for all $l$. Put $A_B = 2(k+r)(r+1) + 1$ and, for a Haar measure $\mu$ on $G$,
$$J(\mu, A, s) = \int_G \|g\|^{-A} F_s(g)\, d\mu(g).$$
For $z$ in the span of $w_0, \dots, w_k$ with $T(z) = -\langle z, z\rangle > 0$, let $\lambda_z$ be the real linear form on $N$ that defines the generic character of $N$ attached to $z$, and for a Haar measure $\mu_N$ on $N$ put
$$I(\mu_N, z, s, \delta) = \int_N \Xi_s(m)\,(1 + |\lambda_z(m)|)^{-\delta}\, d\mu_N(m).$$

**Definition 3.10.1 (Statements $\mathrm{A}$ and $\mathrm{B}$).** $\mathrm{A}(k, r)$ says: for every admissible $s$, every Haar measure $\mu$ on $G_{k,r}$ and every $A \geq A_B$, $J(\mu, A, s) < \infty$. $\mathrm{B}(k, r, \delta)$ says: there is $e > 0$ such that for every $s$ with $0 < s^0_l - s_l \leq e$ for all $l$, every $z$ as above and every Haar measure $\mu_N$ on $N_{k,r}$, $I(\mu_N, z, s, \delta) < \infty$.

The *Heisenberg inputs* are a list of 27 statements. They include existence and uniqueness of Haar measures on $G$, $N$, the stabilizers $W_z$ of $z$ and the Levi factor; closedness of these groups; compactness of $W_z$; the Heisenberg group law and its conjugation by the Levi factor; a recursion for Haar measure on $N$; an integration formula along the decomposition below; and the bound $\int_G \|g\|^{-A}\,d\mu < \infty$ for $A \geq A_B$.

### The base case

**Proposition 3.10.2 (Base case of A).** Assume the Heisenberg inputs and the two-sided transformation rule: for every measurable $\Phi \geq 0$ that is invariant under left and right translation by $K$, and all $x, y \in G$, $\int \Phi(g) F_s(x^{-1}gy)\,d\mu = f_s(x)f_s(y)\int \Phi F_s\, d\mu$, where $f_s(x) = \prod_l \Gamma_l(x\varphi')^{-s_l/2}$. Then $\mathrm{A}(k, 0)$ holds for every $k \geq 1$.

Lean: `ReciprocityTheory.ChartRestriction.DS.Xi.aStepBase_of`

*Proof.* Here $G = G_{k,0} \cong U(k, 1)$ and $F_s(g) = |\langle g\varphi'_0, \varphi'_0\rangle|^{-s_0}$ with $0 \leq s_0 < k$. Let $U_0$ be the stabilizer of $w_k$ in $G$. It is compact, so it has a finite Haar measure $\nu$ with $\nu(U_0) > 0$. For $h, h' \in U_0$, $f_s(h) = f_s(h') = 1$, so the rule applied to $\Phi(g) = \|g\|^{-A}$ (which is $K$-invariant on both sides) gives $\int \Phi(g) F_s(h^{-1}gh')\,d\mu = J$. Integrate over $h, h' \in U_0$ and change the order of integration:
$$J \cdot \nu(U_0)^2 = \int_G \|g\|^{-A} \int_{U_0}\int_{U_0} F_s(h^{-1}gh')\,d\nu(h)\,d\nu(h')\,d\mu(g).$$
The inner average has an explicit form in the $w_0$ and $w_k$ entries. Since $|g_{w_k w_k}| \geq 1$ on $G$, two applications of a bound for $\int_{U_0} |\lambda (h^*v)_{w_0} + b|^{-s}\,d\nu(h)$ show that the inner average is at most the constant $(C_0 + \nu(U_0))^2\, 8^{s_0}$, where $C_0 = \int_{U_0} |1 - h_{w_0w_0}|^{-s_0}\,d\nu$ is finite because $s_0 < k$. The bound on $\int \|g\|^{-A}$ then makes the right side finite. If $J$ were infinite, the left side would be infinite, which is a contradiction. $\square$

### The induction step for A

Write $r = 1 + r'$. For $x = (v, t) \in \mathbb{C}^{2r'+k+1} \times \mathbb{R}$ let $h(x) \in N_{k, r}$ be the Heisenberg element with parameter $x$, let $\iota : G_{k,r'} \to G_{k,r}$ be the Levi embedding, and for $c \neq 0$ let $w(c)$ be the matrix with $(0, n-1)$ entry $\bar{c}^{-1}$, $(n-1, 0)$ entry $c$, ones on the other diagonal places and zeros elsewhere. Put
$$\operatorname{os}(x, c, g, x') = h(x)^{-1}\,w(c)\,\iota(g)\,h(x').$$
Let $Y_a(x) = h(x)^{-1}\iota(H_{k,r'})\varphi_a$, $D(x) = \Gamma_0(Y(x))^{1/2}$ and $\Psi_s(x) = \prod_{l=0}^{r'} \bigl(\Gamma_{l+1}(Y(x))/\Gamma_0(Y(x))\bigr)^{-s_{l+1}/2}$. Let $\hat{s}_l = s_{l+1}$. Put
$$E(A, c, g) = \int \|w(c)\,\iota(g)\,h(x)\|^{-A}\,dx, \qquad Q(A, \hat{s}, \mu_1, c) = \int_{G_{k,r'}} E(A, c, g)\,F_{\hat{s}}(g)\,d\mu_1(g).$$
The *Iwasawa form* statement says that every totally isotropic linearly independent family $Y_0, \dots, Y_r$ is $Y_a = \sum_b \tau_{ba}\,\kappa\varphi'_b$ with $\kappa \in K$, $\tau$ upper triangular and $\prod_{j \leq l}|\tau_{jj}|^2 = \Gamma_l(Y)$. The *left rule* is the one-sided form of the transformation rule above.

**Lemma 3.10.3 (Inner integral).** Assume the Heisenberg inputs, the Iwasawa form and the left rule, and let $k \geq 1$, $\mu_1$ a Haar measure on $G_{k,r'}$, $x$ a Heisenberg parameter and $c \neq 0$. Then
$$\int_{G_{k,r'}} \Bigl(\int \|\operatorname{os}(x, c, g, x')\|^{-A}\,dx'\Bigr) F_{\hat{s}}(g)\,d\mu_1(g) = \Psi_s(x)\, Q\bigl(A, \hat{s}, \mu_1, c\,D(x)\bigr).$$

Lean: `ReciprocityTheory.ChartRestriction.DS.Xi.StepA.inner_eq`

*Proof.* A rank one decomposition gives $\kappa \in K$, $m \in G_{k,r'}$ and a parameter $z$ with $h(x)^{-1}w(c) = \kappa\,w(cD(x))\,\iota(m)\,h(z)$ and $\Gamma_l(m\varphi')\,\Gamma_0(Y(x)) = \Gamma_{l+1}(Y(x))$ for all $l$. Move $h(z)$ past $\iota(g)$ with the Levi conjugation rule, drop $\kappa$ since $\|\kappa y\| = \|y\|$, and use invariance of the Heisenberg measure. The inner integral becomes $E(A, cD(x), mg)$. Substitute $g \mapsto m^{-1}g$, which keeps $\mu_1$, and apply the left rule to $\Phi = E(A, cD(x), \cdot)$, which is left $K$-invariant. The factor is $f_{\hat{s}}(m) = \Psi_s(x)$ by the Gram relation. $\square$

**Lemma 3.10.4 (Bound in the variable $c$).** Assume the hypotheses of the previous lemma, and let $C_0$ be such that $E(A, c, g) \leq C_0\, \omega(c)\,\|g\|^{d - A}$ for all $c \neq 0$ and $g \in G_{k,r'}$, where $d = 4r' + 2k + 3$ and $\omega(c) = \min(|c|^{-d}, |c|^{-1})$. Then, for $c \neq 0$,
$$|c|^{2(2r'+k+1)} \int \|\operatorname{os}\|^{-A} F_s(\operatorname{os})\,dx\,dx'\,d\mu_1 \leq |c|^{2(2r'+k+1) - \sum_l s_l} \int \Psi_s(x)\,|C_0|\,\omega(cD(x))\,J(\mu_1, A - d, \hat{s})\,dx,$$
with $\operatorname{os} = \operatorname{os}(x, c, g, x')$.

Lean: `ReciprocityTheory.ChartRestriction.DS.Xi.StepA.inner_c_le`

*Proof.* On these elements $F_s(\operatorname{os}) = \bigl(\prod_l |c|^{-s_l}\bigr) F_{\hat{s}}(g)$. Pull this factor out, apply Tonelli, and use the previous lemma for each $x$. Then bound $Q$ by $|C_0|\,\omega(cD(x))\,J(\mu_1, A - d, \hat{s})$ with the hypothesis on $E$. $\square$

**Theorem 3.10.5 (Induction step for A).** Assume the Heisenberg inputs, the Iwasawa form, the left rule, the Heisenberg coordinate formula, and the finiteness of the model integrals $\int \prod_l \delta_l(x)^{-(s^0_l + \nu_l)}\,dx$ under the cone condition on $\nu$. If $k \geq 1$ and $\mathrm{A}(k, r')$ holds, then $\mathrm{A}(k, 1 + r')$ holds.

Lean: `ReciprocityTheory.ChartRestriction.DS.Xi.StepA.aStep_fin`

*Proof.* Let $s$ be admissible for $(k, 1 + r')$. Then $\hat{s}$ is admissible for $(k, r')$ and $A - d \geq A_B(k, r')$, so $J(\mu_1, A - d, \hat{s}) < \infty$. The integration formula along the decomposition writes $J(\mu, A, s)$ as a positive constant times $\int_{\mathbb{C}} |c|^{2(2r'+k+1)}\int \|\operatorname{os}\|^{-A}F_s(\operatorname{os})$. A bound on $E$ gives $C_0$. By the previous lemma and the scaling $c \mapsto c/D(x)$ in the $c$ integral, $J$ is at most a constant times
$$\int_{\mathbb{C}} |c|^{a}\,\omega(c)\,dc \cdot \int \Psi_s(x)\,D(x)^{-(a+2)}\,dx,$$
with $a = 2(2r'+k+1) - \sum_l s_l$. The first factor is finite because $1 < \sum_l s_l < 2(2r'+k+1) + 1$. The second is a model integral in Heisenberg coordinates whose exponents satisfy the cone condition, since $0 < s^0_l - s_l \leq 1/10$. $\square$

**Corollary 3.10.6 (Step for A).** Under the same hypotheses, $\mathrm{A}(k, r')$ implies $\mathrm{A}(k, r)$ whenever $r = 1 + r'$ and $k \geq 1$.

Lean: `ReciprocityTheory.ChartRestriction.DS.Xi.aStepSucc_of`

*Proof.* Substitute $r = 1 + r'$ and apply [Theorem 3.10.5](/entry/a-step-fin/). $\square$

### The induction step for B

Let $f_0 = e_0$ if $r' > 0$ and $f_0 = z_1$ if $r' = 0$. For $\hat{s}$ as above and $\gamma \in \mathbb{R}$ let $s^\gamma \in \mathbb{R}^{r'+1}$ be $s^\gamma_a = s_{a+1}$ for $a > 0$ and $s^\gamma_0 = s_1 - \gamma$. Let $\iota(z_1)$ be the image of a vector of $\mathbb{C}^{2r'+k+1}$ in $\mathbb{C}^{2r+k+1}$, and let $G_I$ be the model integrand in Heisenberg coordinates, a product of powers of the functions $\delta_l$ times $(1 + |2\operatorname{Im}L(x) + c_0|)^{-\delta}$ for a linear form $L$ with coefficients $\eta, \eta', \zeta$.

**Lemma 3.10.7 (Heisenberg integral at a Levi point).** Assume the Iwasawa form, the coordinate formula, the Levi conjugation rule and the Heisenberg action formula, and let $k \geq 1$. Suppose that for all $\eta, \eta', \zeta, c_0$ with $\eta'_0 \neq 0$, $\int G_I \leq C\,|\eta'_0|^{-\gamma}(1 + |c_0|)^{-\delta/4}$. Let $\langle \varphi_0, f_0\rangle \neq 0$ and $m \in G_{k,r'}$. Then
$$\int \Xi_s(h(X)\iota(m))\,\bigl(1 + |\lambda_{\iota(z_1)}(h(X)\iota(m))|\bigr)^{-\delta}\,dX \leq C\,|\langle \varphi_0, f_0\rangle|^{-\gamma}\,\Xi_{s^\gamma}(m)\,(1 + |\lambda_{z_1}(m)|)^{-\delta/4}.$$

Lean: `ReciprocityTheory.ChartRestriction.DS.Xi.BL.inner_bound`

*Proof.* The Iwasawa form gives $\kappa \in G_{k,r'} \cap K$ and $t$ with $m\varphi_0 = t\,\kappa\varphi_0$, $|t| = \Delta_0(m)$, and $\Delta_{l+1}(h(X)\iota(m)) = \Delta_l(m)\,\Delta_{l+1}(h(\kappa^*X))$. So the integrand is $\prod_a \Delta_a(m)^{-s_{a+1}}$ times $G_I$ at the coordinates of $\kappa^*X$, and $\lambda_{\iota(z_1)}(h(X)\iota(m)) = 2\operatorname{Im}L + \lambda_{z_1}(m)$ with $\eta'_0\,t = \langle \varphi_0, f_0\rangle$. The map $X \mapsto \kappa^*X$ and the coordinate map keep the measure. Apply the hypothesis, and write $|\eta'_0|^{-\gamma} = |\langle\varphi_0, f_0\rangle|^{-\gamma}\Delta_0(m)^{\gamma}$. $\square$

**Theorem 3.10.8 (Induction step for B).** Assume the Heisenberg inputs, the Iwasawa form, the coordinate formula and the oscillatory bound for $\int G_I$. If $r = 1 + r'$, $k \geq 1$, $0 < \delta \leq 1/2$ and $\mathrm{B}(k, r', \delta/4)$ holds, then $\mathrm{B}(k, r, \delta)$ holds.

Lean: `ReciprocityTheory.ChartRestriction.DS.Xi.bStepSucc_of`

*Proof.* Let $e'$ come from $\mathrm{B}(k, r', \delta/4)$, put $\gamma = \min(\delta/8, e'/2)$ and $e = \min(e'/2, \gamma/(4r + 4))$. For $s$ with $0 < s^0_l - s_l \leq e$, the gaps $e_l = s^0_l - s_l$ satisfy $e_0 + 2\sum_{l \geq 1} e_l < \gamma/2$, so the oscillatory bound gives $C$ for the lemma. Write $z = \iota(z_1)$ with $T(z_1) > 0$, so $\langle\varphi_0, f_0\rangle \neq 0$, and $s^\gamma$ has gaps in $(0, e']$. A Haar measure on $N_{k,r}$ is a constant times the image of the Heisenberg measure times a Haar measure $\mu'$ on $N_{k,r'}$. By Tonelli and the lemma, $I(\mu_N, z, s, \delta)$ is at most a constant times $I(\mu', z_1, s^\gamma, \delta/4)$, which is finite. $\square$

### The majorant

**Definition 3.10.9 (Majorant).** For a real place datum $D$ with group $G_{k,r}$, Haar measure $\mu_G$, vectors $z, z'$ and the measures on $W_z \times N$ and $W_{z'} \times N$, a function $\Xi : G \to [0, \infty)$ is a *majorant of order $A$* if there is $C$ such that for all measurable $F, F'$ with $\|g\|^A\|F(g)\| \leq c$ and $\|g\|^A\|F'(g)\| \leq c'$ on $G$, and all $x, y \in G$,
$$\int_G \|F(x^{-1}gy)\|\,\|F'(g)\|\,d\mu_G(g) \leq C c c'\,\Xi(x)\,\Xi(y).$$
It is *integrable with exponent* $\delta$ if it is measurable and $\int_{W_z}\int_N \Xi(mh)(1 + |\lambda_z(m)|)^{-\delta}\,dm\,dh < \infty$, and the same for $z'$.

**Theorem 3.10.10 (Existence of the majorant, from the inputs).** Assume the Heisenberg inputs. Then for every real place datum $D$ and every $A \geq A_B(k, r)$ there is a majorant of order $A$ that is integrable with exponent $2$.

Lean: `ReciprocityTheory.ChartRestriction.DS.Xi.xiExists_of_in`

*Proof.* By induction, the base case and [Corollary 3.10.6](/entry/a-step-succ-of/) give $\mathrm{A}(k, r)$ for all $r$. The base case $\mathrm{B}(k, 0, \delta)$ holds because $N_{k,0}$ is trivial, and [Theorem 3.10.8](/entry/b-step-succ-of/) gives $\mathrm{B}(k, r, 1/2)$ for all $r$. Take $e$ from $\mathrm{B}(k, r, 1/2)$ and $s_l = s^0_l - \min(e, 1/10)$. Then $s$ is admissible and $\Xi = \Xi_s$. A coefficient step turns $J < \infty$ into the majorant property, and an integrability step turns the finiteness of $I$ for $z$ and $z'$ with $\delta = 1/2$ into integrability with exponent $2$. The Iwasawa form, the two transformation rules, the coordinate formula, the model integral bound and the oscillatory bound are separate theorems. $\square$

**Theorem 3.10.11 (Existence of the majorant).** For every real place datum and every $A \geq 2(k + r)(r + 1) + 1$ there is a majorant of order $A$ that is integrable with exponent $2$.

Lean: `ReciprocityTheory.ChartRestriction.DS.Xi.xiExists`

*Proof.* The 27 Heisenberg inputs are separate theorems. Apply [Theorem 3.10.10](/entry/xi-exists-of-in/). $\square$

**Remark 3.10.12 (Formalization).** The hypothesis of the theorem from the inputs is a conjunction of 27 statements, and the final theorem discharges all of them ([XiExistsOfIn.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/XiExistsOfIn.lean#L21)). The base case uses three of them and ends with a proof by contradiction ([MeasurableHaarKernelTriple.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/MeasurableHaarKernelTriple.lean#L204)). The corollary for $\mathrm{A}$ only substitutes $r = 1 + r'$ ([AStepSuccOf.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/AStepSuccOf.lean#L5)). The index shift $l \mapsto l + 1$ has two names with the same definition ([GoodRowsProjectorApplyEqSum.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/GoodRowsProjectorApplyEqSum.lean#L242), [LevelDeterminantOfTriangularChange.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TailIntegrals/LevelDeterminantOfTriangularChange.lean#L19)). We did not open the proofs of the rank one decomposition, the bound on $E$, the model integral bound, the oscillatory bound, the coefficient step or the integrability step.
