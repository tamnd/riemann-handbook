---
title: Chern densities and the compact dual
decls:
  - GlobalTheory.GrassTop.grass_top
  - GlobalTheory.T.compactDual_linearForm_flagDegree_pointClass
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Chern densities and the compact dual

This section sets up the algebra of the chapter. We define the top Chern density of a Hermitian metric at one point, the flag degree of a weight and the point polynomial. Then we prove an algebraic fact: a linear form on polynomials in Chern classes that satisfies the relations of the cohomology of a product of Grassmannians is fixed by its value on the point polynomial. The constant is the flag degree. In the section on [the pointwise Chern densities of the Hodge metric](/entry/pointwise-hodge/) this fact is applied to the linear form "top Chern density at a point", and it turns the proportionality theorem into a statement about one polynomial.

**Definition 7.1.1 (Top Chern density).** Let $n \geq 0$, let $I$ be a finite set and let $(m_\tau)_{\tau \in I}$ be ranks. Let $G = (G_\tau)_{\tau \in I}$ be a family of smooth maps $G_\tau \colon \mathbb{C}^n \to M_{m_\tau}(\mathbb{C})$, read as Gram matrices of Hermitian metrics on trivial bundles, and let $v \in \mathbb{C}^n$. Let $\Theta_{\tau,ab}(v)$ be the curvature matrix of the Chern connection of $G_\tau$ at $v$ in the coordinate directions $a$ and $b$. In the polynomial ring $\mathbb{C}[x_{a,b} : 1 \leq a, b \leq n]$ put
$$\Theta_\tau(v) = \sum_{a,b} \Theta_{\tau,ab}(v)\, x_{a,b}, \qquad \det\bigl(1 + t\,\Theta_\tau(v)\bigr) = \sum_{k \geq 0} c_k(G_\tau)(v)\, t^k.$$
For $P \in \mathbb{C}[x_{a,b}]$ let $\operatorname{top}(P) = \sum_{w \in S_n} \operatorname{sgn}(w)\, [\prod_a x_{a,w(a)}]\,P$, where $[\,\cdot\,]P$ is a coefficient. For a real polynomial $R$ in variables $c_{\tau,k}$ ($\tau \in I$, $k \in \mathbb{N}$) the *top Chern density* of $R$ is
$$\rho_R(G)(v) = \pi^{-n}\, \operatorname{Re} \operatorname{top}\bigl(R(c_k(G_\tau)(v))\bigr).$$

The variable $x_{a,b}$ plays the part of the 2-form $dz_a \wedge d\bar z_b$. These 2-forms commute, and $\prod_a dz_a \wedge d\bar z_{w(a)} = \operatorname{sgn}(w) \prod_a dz_a \wedge d\bar z_a$. So $\operatorname{top}(P)$ is the coefficient of the top form in the form $P$, and $\rho_R(G)$ is the density of the [Chern-Weil form](/learn/positivity-resolution/#chern-weil-forms) $R(c(G))$ with respect to Lebesgue measure, with the normalization fixed by the factor $\pi^{-n}$. We give the variable $c_{\tau,k}$ the *weight* $k$. A polynomial is *weighted homogeneous* of degree $d$ if each of its monomials has weight $d$.

From now on we fix the following data. Let $E$ be a CM field, with complex conjugation $\tau \mapsto \bar\tau$ on the set $I = \operatorname{Hom}(E, \mathbb{C})$. Let $p, q \geq 0$, $N = p + q$, and let $\Psi \subseteq I$ be the set of embeddings that send a fixed element $r \in E$ to a fixed complex number $r_0$. For $\tau \in I$ let $m_\tau = p$ if $\tau \in \Psi$ and $m_\tau = q$ otherwise.

**Definition 7.1.2 (Roots and antisymmetrization).** The *roots* are variables $x_{\tau,i}$ for $\tau \in I$ and $0 \leq i < m_\tau$. The ring map $\chi$ from $\mathbb{R}[c_{\tau,k}]$ to $\mathbb{R}[x_{\tau,i}]$ sends $c_{\tau,k}$ to the elementary [symmetric polynomial](/learn/combinatorics/#symmetric-polynomials) $e_k(x_{\tau,0}, \dots, x_{\tau,m_\tau-1})$. The discriminant is $\Delta = \prod_\tau \prod_{i<j} (x_{\tau,j} - x_{\tau,i})$. For $Q \in \mathbb{R}[x_{\tau,i}]$,
$$\operatorname{antisym}(Q) = \sum_{w \in \prod_\tau S_{m_\tau}} \Bigl(\prod_\tau \operatorname{sgn}(w_\tau)\Bigr)\, w \cdot Q,$$
where $w$ acts by $x_{\tau,i} \mapsto x_{\tau,w_\tau(i)}$.

An antisymmetric polynomial is divisible by $\Delta$, with a symmetric quotient in each block of roots. So for each $Q$ there is $R$ with $\operatorname{antisym}(Q) = \chi(R)\,\Delta$.

**Definition 7.1.3 (Weights, flag degree and point polynomial).** A *weight* is a map $\lambda \colon \Psi \times \{0, \dots, N-1\} \to \mathbb{Z}$. Its *exponents* are the integers $e_\lambda(\tau, i)$ on the roots given by $e_\lambda(\tau,i) = \lambda_\tau(i)$ for $\tau \in \Psi$ and $i < p$, and $e_\lambda(\bar\tau, i) = -\lambda_\tau(N-1-i)$ for $\tau \in \Psi$ and $i < q$. For $D \geq 0$ put
$$Q_{\lambda,D} = \Bigl(-\sum_{(\tau,i)} e_\lambda(\tau,i)\, x_{\tau,i}\Bigr)^D.$$
Let $D_0 = |\Psi|\,N(N-1)/2$. For a polynomial $P$ in variables $y_{\tau,i}$ ($\tau \in \Psi$, $i < N$) put
$$\deg_{\mathrm{Fl}}(P) = (-1)^{D_0} \sum_{w \in S_N^{\Psi}} \Bigl(\prod_\tau \operatorname{sgn}(w_\tau)\Bigr) \Bigl[\prod_{\tau,i} y_{\tau,i}^{N-1-w_\tau(i)}\Bigr] P.$$
The *flag degree* of $\lambda$ is $\deg_{\mathrm{Fl}}(\lambda) = \deg_{\mathrm{Fl}}(\ell_\lambda^{D_0})$, with $\ell_\lambda = -\sum_{\tau,i} \lambda_\tau(i)\, y_{\tau,i}$. The *point polynomial* is
$$P_0 = \prod_{\tau \in \Psi} \bigl((-1)^p c_{\tau,p}\bigr)^q.$$

Here $D_0$ is the dimension of the product of full flag varieties $\mathrm{Fl}(N)^\Psi$, and $\deg_{\mathrm{Fl}}$ is the integral over this product, written in Chern roots $y_{\tau,i}$ of the tautological line bundles: the antisymmetrization against the staircase monomial is the classical formula for the integral over a flag variety. So $\deg_{\mathrm{Fl}}(\lambda)$ has the form of the top self-intersection of the line bundle of weight $\lambda$. On each Grassmannian $\operatorname{Gr}(p, N)$, with tautological bundle $S$ of rank $p$, the polynomial $P_0$ gives the class $c_p(S^\vee)^q$. This is the Schubert class of $(1^p)$ to the power $q$, which is the class of a point by the Pieri rule.

**Theorem 7.1.4 (Linear forms on the compact dual).** Let $\lambda$ be a weight, let $n \geq 0$ and $D = |\Psi|\,N(N-1)/2$, and let $R \in \mathbb{R}[c_{\tau,k}]$ with $\operatorname{antisym}(Q_{\lambda,D}) = \chi(R)\,\Delta$. Let $L \colon \mathbb{R}[c_{\tau,k}] \to \mathbb{R}$ be a linear form such that for all $Q$:

1. $L(Q) = 0$ if $Q$ is weighted homogeneous of a degree $d \neq n$;
2. $L\bigl((c_{\tau,0} - 1)\,Q\bigr) = 0$ for all $\tau \in I$;
3. $L(c_{\tau,k}\,Q) = 0$ for all $\tau \in I$ and $k > m_\tau$;
4. for $\tau \in \Psi$ and $k \geq 1$,
$$L\Bigl(\sum_{a=0}^{k} (-1)^{k-a}\, c_{\tau,a}\, c_{\bar\tau,k-a}\, Q\Bigr) = 0.$$

Then $L(R) = \deg_{\mathrm{Fl}}(\lambda)\, L(P_0)$.

Lean: `GlobalTheory.GrassTop.grass_top` (also `GlobalTheory.T.compactDual_linearForm_flagDegree_pointClass`, a second name).

Relation 4 says that $c(\mathcal{E}_\tau)\,c(\mathcal{E}_{\bar\tau}^\vee) = 1$ in positive degree, since $c_j(\mathcal{E}^\vee) = (-1)^j c_j(\mathcal{E})$. On $\operatorname{Gr}(p, N)$ the tautological bundle $S$ and the quotient $\mathbb{C}^N/S$ satisfy $c(S)\,c(\mathbb{C}^N/S) = 1$ by the Whitney sum formula (Milnor and Stasheff, *Characteristic Classes*, §14). Relations 2 to 4 are the relations of the cohomology ring of $\prod_{\tau \in \Psi} \operatorname{Gr}(p, N)$, with $\mathcal{E}_\tau = S$ and $\mathcal{E}_{\bar\tau} = (\mathbb{C}^N/S)^\vee$. This product is the compact dual of the symmetric domain of the next sections.

*Proof.* Let $J$ be the ideal generated by the polynomials $c_{\tau,0} - 1$, the $c_{\tau,k}$ with $k > m_\tau$, and the sums of relation 4. Since conditions 2 to 4 hold for every multiplier $Q$, the form $L$ vanishes on $J$. If $\chi(Q) = 0$, then $Q$ lies in the ideal generated by the first two kinds of generators, by the fundamental theorem on symmetric polynomials, so $L(Q) = 0$.

The polynomial $Q_{\lambda,D}$ is homogeneous of degree $D$ in the roots, so $\chi(R)\,\Delta$ is homogeneous of degree $D$. The discriminant $\Delta$ is nonzero and homogeneous of degree $\delta = |\Psi|\bigl(p(p-1)/2 + q(q-1)/2\bigr)$. So $\chi(R)$ is homogeneous of degree $e = D - \delta = |\Psi|\,pq$. Let $R_e$ be the weighted homogeneous part of $R$ of degree $e$. Then $\chi(R - R_e) = 0$, because $\chi$ sends weight to degree. So $L(R) = L(R_e)$.

Let $\int_{\mathrm{Gr}}$ be the linear form $Q \mapsto \deg_{\mathrm{Fl}}\bigl(\rho(\chi(Q)\,\Delta)\bigr)/(p!\,q!)^{|\Psi|}$, where $\rho$ is a ring map that sends the roots of $\tau$ and of $\bar\tau$, for $\tau \in \Psi$, to the flag variables $y_{\tau,i}$. This is the integral over $\prod_\Psi \operatorname{Gr}(p,N)$, computed on the flag variety: a fibre of $\mathrm{Fl}(N) \to \operatorname{Gr}(p, N)$ is $\mathrm{Fl}(p) \times \mathrm{Fl}(q)$, and the factor $(p!\,q!)^{|\Psi|}$ accounts for it. It satisfies $\int_{\mathrm{Gr}} R = \deg_{\mathrm{Fl}}(\lambda)$ by the hypothesis on $R$, $\int_{\mathrm{Gr}}$ vanishes on $J$, and $\int_{\mathrm{Gr}} P_0 = 1$. Also $\int_{\mathrm{Gr}} R = \int_{\mathrm{Gr}} R_e$, since $\chi(R - R_e) = 0$.

Now there are two cases. If $n = e$: the part of degree $e = \dim \prod_\Psi \operatorname{Gr}(p, N)$ of the quotient by $J$ is spanned by $P_0$, so $R_e - c\,P_0 \in J$ for some $c \in \mathbb{R}$. Apply $\int_{\mathrm{Gr}}$: $c = \int_{\mathrm{Gr}} R_e = \deg_{\mathrm{Fl}}(\lambda)$. Apply $L$: $L(R) = L(R_e) = c\,L(P_0)$. If $n \neq e$: $R_e$ and $P_0$ are weighted homogeneous of degree $e$, so $L(R_e) = L(P_0) = 0$ by condition 1, and both sides are $0$. $\square$

**Remark 7.1.5.** The flag degree has a closed form. With $D_0 = |\Psi|\,N(N-1)/2$, one expects
$$\deg_{\mathrm{Fl}}(\lambda) = D_0! \prod_{\tau \in \Psi} \prod_{i<k} \frac{\lambda_\tau(i) - \lambda_\tau(k)}{k - i},$$
that is, $D_0!$ times the value of the Weyl dimension polynomial at $\lambda$. This section does not use or prove the formula.

**Remark 7.1.6 (Formalization).** The theorem is in [CompactDualLinearFormFlagDegreePointClass.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/CompactDualLinearFormFlagDegreePointClass.lean#L80); the second name only restates it. The Chern connection and its curvature, `conn` and `curv`, were not unfolded here; we read them by their names. The exponents $e_\lambda$ are given by `wtOf` and then by a reindexing `exZ` that we did not unfold. The degree $n$ of condition 1 is free: when $n \neq |\Psi|\,pq$ the conclusion is $0 = 0$ (lines 144 to 146). The closed form of the Remark is the proposition `FlagDegFormula` in [FlagDegFormula.lean](lean:Formalism/DegreeFormula/FlagDegFormula.lean#L27), which is stated and not proved there. The steps "the top part is spanned by $P_0$" and "$\int_{\mathrm{Gr}}$ of $R$ is the flag degree" are the lemmas `grassmannProduct_topDegree_eq_smul_pointClass` and `grassmannProductIntegral_eq_flagDegree_weight`, which we did not open.
