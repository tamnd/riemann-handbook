---
title: The archimedean bound and good functionals
decls:
  - GlobalTheory.ArchCM.norm_cfOf_le
  - GlobalTheory.T.norm_cmArcCoefficientFunctional_le
  - GlobalTheory.ArcCM.RunNum.arch_good
  - GlobalTheory.ArcCM.RunNum.arch_all
  - GlobalTheory.ArcCM.numGood_of_famQ
  - GlobalTheory.T.cmArcDatumFamily_functional_bounded_linear_on_cuspForms
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The archimedean bound and good functionals

This section bounds the values of the functional $\mathrm{cf}_d$ at the infinite places and then puts the finite and the infinite bounds together. At a complex embedding $\varepsilon$ of $K_1$, the value $\varepsilon(\mathrm{cf}_d(F))$ is a coefficient of a polynomial in the letters, and the polynomial is a Fourier-Jacobi coefficient of $F$ at each point of a polydisc. The Cauchy inequalities on this polydisc give the bound (Theorem (Cauchy bound)). The radii of the polydisc are the metrics of the lines $\ell(\tau,k)$ of the CM input, so the bound has the form $|\varepsilon(\mathrm{cf}_d(F))|\, n_{V,\varepsilon} \leq \|F\|\, e^{C}$ for the value line $V$ of Section 4. With Theorem (Finite integrality of the coefficient functional), each member of the CM family then gives a *numerically good* functional (Theorem (The CM functionals are numerically good)). This is the form in which [Theorem 4.6.3](/entry/qat-of-kill-detect/) uses the family.

**Definition 4.5.1 (Numerically good functional).** Let $V$ be a $K$-vector space, $M \subset V$ a subset, $S(\sigma, F) \in \mathbb{R}$ a function of the embeddings $\sigma : K \to \mathbb{C}$ and of $F \in V$, $\beta$ a real function on the primes of $K$, and $C_{\mathrm{arch}}, B_{\deg} \in \mathbb{R}$. Let $K_1$ be a number field that contains $K$, and let $\varphi : V \to K_1$ be $K$-linear. Then $\varphi$ is *numerically good* for $(M, S, \beta, C_{\mathrm{arch}}, B_{\deg})$ if there is a good metrized line $N$ over $K_1$ with:

1. $\widehat{\deg}\, N \leq B_{\deg}$;
2. $n_{N, \bar{\sigma}} = n_{N,\sigma}$ for every embedding $\sigma : K_1 \to \mathbb{C}$, where $\bar{\sigma}$ is the complex conjugate of $\sigma$;
3. for every prime $\lambda$ of $K$, every prime $w$ of $K_1$ over $\lambda$ and every $F \in M$ with $\varphi(F) \neq 0$:
$$-e(w|\lambda)\, \beta(\lambda) \leq \mathrm{ord}_w\, \varphi(F) - v_w(I_N);$$
4. for every embedding $\sigma : K_1 \to \mathbb{C}$ and every $F \in M$ with $\varphi(F) \neq 0$:
$$\log |\sigma(\varphi(F))| + \log n_{N,\sigma} \leq \log S(\sigma|_K, F) + C_{\mathrm{arch}}.$$

So $\varphi(F)$, read as a section of $N$, is integral up to $\beta$ at the finite places and bounded by $S \cdot e^{C_{\mathrm{arch}}}$ at the infinite places. These are the two halves of a [height](/learn/arakelov/#heights) bound for $\varphi(F)$.

**The Cauchy bound.** Let $\varepsilon : K_1 \to \mathbb{C}$ be an embedding. Its restriction to $K$ is *good* if it maps the fixed root of the base field to the fixed complex root. A unitary chart $U$ at $\varepsilon|_K$ of rank $r$ gives, for each component $k$, a Hermitian datum $X_k$ with a fixed element $\xi_{0,k} \in E$, a weight $\lambda_k$ computed from $(a', n)$, and the restriction $F_k$ of a section $F$; the *pointwise norm* $|F_k(y)|_{\lambda_k}$ of $F_k$ of weight $\lambda_k$ is defined at each point $y$ of the domain of $X_k$. For the weight $a'$ we write $\mathrm{abs}(a') = \sum_\tau \sum_i a'(\tau, i)$ as in Section 3, and we put

$$a_P(E, r, \Lambda_0, c_1) = \tfrac{1}{2} \log \max(1, c_1) + \log \Lambda_0 + \log \mathrm{rd}_E + \log r.$$

**Theorem 4.5.2 (Cauchy bound).** Assume $\mathcal{K}$. Let $d$ be a standard arc datum over $K_1$ with monomial $X^\mu$, and let $s$ be a CM input for $d$ with parameters $(n', \Lambda_0, c_1)$, where $\Lambda_0 \geq 1$. Let $\varepsilon : K_1 \to \mathbb{C}$ be an embedding whose restriction to $K$ is good, let $U$ be a unitary chart at $\varepsilon|_K$ of rank $r$ that is a uniformization, and let $x_0 \in \mathbb{R}$ with $|\tau(\xi_{0,k})| = x_0$ for all components $k$ and all $\tau$. Let $(a', n)$ be a weight with $a'$ decreasing in its second argument and $n$ even. Assume that on each component $k$, every transvection along an isotropic vector that is congruent to $1$ modulo $M$ on $\Lambda$ lies in $\Gamma$ and has $\chi_{\lambda_k} = 1$. Let $F$ be a section of weight $(a', n)$ and $S \geq 0$ with

$$(2\pi x_0)^{-\mathrm{abs}(a')/2}\, |F_k(y)|_{\lambda_k} \leq S$$

for every component $k$ and every point $y$ of the domain of $X_k$. Then

$$|\varepsilon(\mathrm{cf}_d(F))| \cdot n_{V_s(\mu, n), \varepsilon} \leq S \cdot \exp\Big(4\pi + a_P(E, r, \Lambda_0, c_1) \big(\mathrm{abs}(a') + f n\big)\Big).$$

Lean: `GlobalTheory.ArchCM.norm_cfOf_le` (also `GlobalTheory.T.norm_cmArcCoefficientFunctional_le`, a second name).

*Proof.* Step 1: Cauchy inequalities. For $x \in \mathbb{C}^{\{\text{letters}\}}$ let $G(x)$ be the value at $x$ of the polynomial whose coefficients are the images under $\varepsilon$ of the coefficients of $t^{j_d}$ in $N_F$. Then $G$ is a polynomial, and its coefficient of $X^\mu$ is $\varepsilon(\mathrm{cf}_d(F))$. Put $\rho_{\tau,i,l} = n_{\ell(\tau,l),\varepsilon}^{-1} > 0$. By the [Cauchy inequalities](/learn/complex-analysis/#holomorphic-functions) on the polydisc with these radii,

$$|\varepsilon(\mathrm{cf}_d(F))| \prod_{(\tau,i,l)} \rho_{\tau,i,l}^{\mu(\tau,i,l)} \leq \sup \{\, |G(x)| : |x_{\tau,i,l}| \leq \rho_{\tau,i,l} \,\}.$$

The product on the left is $n_{V_s(\mu,n),\varepsilon} \cdot n_{T,\varepsilon}^{\,n}$. Since $G$ is continuous, it suffices to bound $|G(x)|$ at the points $x$ of the polydisc whose letter matrices are invertible.

Step 2: base change to $\mathbb{C}$. The laws in $\mathcal{K}$ give the base change of the arc of $d$ along $\varepsilon$, with its tangent vectors and theta section. The toroidal archimedean condition of $\mathcal{K}$, at the good embedding $\varepsilon|_K$, gives a toroidal datum for the complex arc, and the uniformization $U$ gives a witness.

Step 3: the Fourier-Jacobi coefficient. The module of the point has rank one and $\xi \neq 0$. From these facts and the condition that ties $\nu_0$, $\xi$ and $j_d$ together, a theorem proved outside this chapter identifies $G(x)$, at each $x$ of Step 1, with a Fourier-Jacobi coefficient of $F_k$ at a frame of a component $k$, along the isotropic vector of $\xi$ and at the frequency of $\nu_0$.

Step 4: the bound. The pointwise bound for $F$ gives a bound for this coefficient through the coefficient bounds of the flow on the domain, a theorem proved outside this chapter. In this bound there are three factors. The first is the height matrix $H$ of the frame. The squared length of each letter is at most the flow height, and a bound for Hermitian sums gives $\pi H_{ii} \leq (r \Lambda_0 \sqrt{\max(1, c_1)})^2$. With $\sqrt{|d_E|} = \mathrm{rd}_E^{\,f}$ and $\mathrm{rd}_E \geq 1$, these factors are at most $n_{T,\varepsilon}^{\,n} \exp(a_P (\mathrm{abs}(a') + f n))$. The second is $\exp\big(4\pi \sum_\tau \mathrm{Re}\, \tau(\nu_0)\, (\max(1,c_1)^{-1} - t_\tau)\big)$, where $t_\tau$ are the times of the frame and the sum is over the CM type. The part with $t_\tau$ is the absolute value of the factor of $t^{j_d}$ and cancels. The sum of $\mathrm{Re}\, \tau(\nu_0)$ over the CM type is $\mathrm{Tr}_{E/\mathbb{Q}}(\nu_0)/2 \leq c_1$, so $\max(1,c_1)^{-1} \sum_\tau \mathrm{Re}\, \tau(\nu_0) \leq 1$, and the rest is at most $e^{4\pi}$. The third is $S$. With Step 1 this gives the claim, since the factors $n_{T,\varepsilon}^{\,n}$ cancel. $\square$

**Lemma 4.5.3 (The bound at a good embedding).** Assume $\mathcal{K}$ and the laws of the core, and assume that the chart at each good embedding and each admissible step has principal level $M$. Let $j$ be in the admissible range, $\kappa$ a weight with exponents $(a'_\kappa, n)$, and $C_R, T, c \in \mathbb{R}$. Let $K_1 \supset K$ be a number field, $d$ a standard arc datum over $K_1$ with monomial $X^\mu$, and $s$ a CM input for $d$ with parameters $(n_{\mathrm{At}}, \Lambda_{\mathrm{At}}, c_1)$. Let $\varepsilon : K_1 \to \mathbb{C}$ be an embedding whose restriction to $K$ is good, and let $F \in S$. Then

$$|\varepsilon(\mathrm{cf}_d(F))| \cdot n_{V_s(\mu, n), \varepsilon} \leq \|F\|_{\varepsilon|_K} \cdot e^{C_{\mathrm{At}}}, \qquad C_{\mathrm{At}} = 4\pi + a_P(E, r, \Lambda_{\mathrm{At}}, c_1)\, \mathrm{size}(\kappa).$$

Lean: `GlobalTheory.ArcCM.RunNum.arch_good`.

*Proof.* We apply Theorem (Cauchy bound) with the chart $U$ of the core at $\varepsilon|_K$, the element $x_0$ of the core and $S = \|F\|_{\varepsilon|_K}$. The laws of the core give that $U$ is a uniformization, that $|\tau(\xi_{0,k})| = x_0$, and that $\chi_{\lambda_k} = 1$ on $\Gamma$; with the principal level this gives the condition on transvections. The weight $a'_\kappa$ is decreasing and $n$ is even. We have $\Lambda_{\mathrm{At}} \geq 1$, since $\Lambda_Q$ is a maximum with $1$. The form $F$ is a cusp form, so it is a section of weight $(a'_\kappa, n)$. At a good embedding the sup norm is $(2\pi x_0)^{-\mathrm{abs}(a'_\kappa)/2}$ times the supremum of the pointwise norms, so the pointwise hypothesis holds with $S = \|F\|_{\varepsilon|_K} \geq 0$.

It remains to compare the exponents. The numerics of the pins give $[E : \mathbb{Q}] = 2f$ and $r \geq 1$. So $\mathrm{abs}(a'_\kappa) + f n \leq \mathrm{abs}(a'_\kappa) + f r n \leq \mathrm{size}(\kappa)$, where the last step is a direct count from the formula for the size. Also $a_P \geq 0$, since $\max(1, c_1) \geq 1$, $\Lambda_{\mathrm{At}} \geq 1$, $\mathrm{rd}_E \geq 1$ and $r \geq 1$. So the exponent of Theorem (Cauchy bound) is at most $C_{\mathrm{At}}$. $\square$

**Lemma 4.5.4 (The bound at all embeddings).** In the setting of Lemma (The bound at a good embedding), the same bound holds for every embedding $\varepsilon : K_1 \to \mathbb{C}$.

Lean: `GlobalTheory.ArcCM.RunNum.arch_all`.

*Proof.* If $\varepsilon|_K$ is good, this is Lemma (The bound at a good embedding). If not, then $\bar{\varepsilon}|_K$ is good, since for each embedding of $K$ either it or its complex conjugate is good. We apply the lemma to $\bar{\varepsilon}$. We have $|\bar{\varepsilon}(x)| = |\varepsilon(x)|$, the metrics of the value line satisfy $n_{V,\bar{\varepsilon}} = n_{V,\varepsilon}$ by a lemma on CM lines, and the sup norms satisfy $\|F\|_{\bar{\sigma}} = \|F\|_\sigma$ by a lemma on the recursive construction. So the bound for $\bar{\varepsilon}$ is the bound for $\varepsilon$. $\square$

**Good functionals.** In the setting of Section 1, the elements of the lattice $M \subset S$ are the forms that are $\lambda$-integral for every prime $\lambda$ of $K$. The size data of the core give a real number $\omega$ such that each CM line of a good CM object has normalized degree $\omega/2$. We put $p(\omega) = (1 + |\omega|)/2$ and

$$B_{\mathrm{At}} = \Big( p(\omega) + \tfrac{1}{2} \log \Lambda_{\mathrm{At}} \Big)\, \mathrm{size}(\kappa).$$

**Theorem 4.5.5 (The CM functionals are numerically good).** Assume $\mathcal{K}$ and the laws of the core, and assume that the chart at each good embedding and each admissible step has principal level $M$. Let $j < m$ be in the admissible range, $\kappa$ a weight and $C_R, T, c \in \mathbb{R}$. Let $K_1 \supset K$ be a number field and $d \in \mathrm{Fam}_Q$ an arc datum over $K_1$. Then there is a $K$-linear map $\varphi : S \to K_1$ with $\varphi(F) = \mathrm{cf}_d(F)$ for all $F \in S$, and $\varphi$ is numerically good for

$$\big(M,\ (\sigma, F) \mapsto \|F\|_\sigma,\ \beta_{E, n_{\mathrm{At}}, \mathrm{abs}(a'_\kappa)},\ C_{\mathrm{At}},\ B_{\mathrm{At}}\big).$$

Lean: `GlobalTheory.ArcCM.numGood_of_famQ` (also `GlobalTheory.T.cmArcDatumFamily_functional_bounded_linear_on_cuspForms`, a second name).

*Proof.* Since $d \in \mathrm{Fam}_Q$, it is standard and has a CM input $s$ with parameters $(n_{\mathrm{At}}, \Lambda_{\mathrm{At}}, c_1)$. A lemma on arc data gives two facts: $\mathrm{cf}_d$ is $K$-linear on the sections of weight $(a'_\kappa, n)$, and if $\mathrm{cf}_d(F) \neq 0$ for such a section, then the degree $|\mu|$ of the monomial $X^\mu$ of $d$ is $\mathrm{abs}(a'_\kappa)$. The space $S$ consists of such sections, so $\mathrm{cf}_d$ restricts to a $K$-linear map $\varphi$ on $S$. We have $p(\omega) + \frac{1}{2}\log \Lambda_{\mathrm{At}} \geq 0$, since $\Lambda_{\mathrm{At}} \geq 1$.

Case $|\mu| = \mathrm{abs}(a'_\kappa)$. We take $N = V_s(\mu, n)$. A lemma on value lines, with $\Lambda_{\mathrm{At}} \geq 1$ and the degree statement for $\omega$, gives that $N$ is good and that

$$\widehat{\deg}\, N \leq \Big( p(\omega) + \tfrac{1}{2} \log \Lambda_{\mathrm{At}} \Big) \big( |\mu| + f r n \big).$$

Here $|\mu| + f r n = \mathrm{abs}(a'_\kappa) + f r n \leq \mathrm{size}(\kappa)$, so condition 1 holds. Condition 2 is the lemma on CM lines from the proof of Lemma (The bound at all embeddings). For condition 3, the numerics of the pins give a good level, so the moduli space has models at all primes. Each $F \in M$ is $\lambda$-integral, so Theorem (Finite integrality of the coefficient functional) gives condition 3 with $n' = n_{\mathrm{At}}$ and $A = \mathrm{abs}(a'_\kappa)$. For condition 4, let $F \in M$ with $\varphi(F) \neq 0$. Then $F \neq 0$, so $\|F\|_\sigma > 0$. Lemma (The bound at all embeddings) gives $|\sigma(\varphi(F))|\, n_{N,\sigma} \leq \|F\|_{\sigma|_K} e^{C_{\mathrm{At}}}$, and both sides are positive. We take logarithms.

Case $|\mu| \neq \mathrm{abs}(a'_\kappa)$. Then $\varphi = 0$ on $S$. We take $N = \mathbf{1}$, which is good. Its normalized degree is $0 \leq B_{\mathrm{At}}$, since $\mathrm{size}(\kappa) \geq 1$. Its metrics are $1$, so condition 2 holds, and conditions 3 and 4 are empty. $\square$

**Remark 4.5.6 (Formalization).** The last theorem has the hypothesis $j < m$, but the proof does not use it ([CmArcDatumFamilyFunctionalBoundedLinearOnCuspFor.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/CmArcDatumFamilyFunctionalBoundedLinearOnCuspFor.lean#L153)). The family $\mathrm{Fam}_Q$ puts no condition on the monomial $\mu$ or on $j_d$ ([CarchAt.lean](lean:Development/AbelianVarietyTheory/Definitions/ArchimedeanThetaValues/CarchAt.lean#L25)), so the second case of the proof is a real case: the functional is then $0$ and gives no information. Numerically good is `NumGood` of [ModelsAt.lean](lean:Development/AbelianVarietyTheory/Definitions/ArchimedeanThetaValues/ModelsAt.lean#L181), and $C_{\mathrm{At}}$ and $B_{\mathrm{At}}$ are `CarchAt` and `BdegAt`. The second names are wrappers. We have not unfolded the toroidal datum, the flow on the domain, the height matrix, the degree statement for $\omega$, or the sup norm of the recursive construction.
