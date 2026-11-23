---
title: Lemma E for energy systems
decls:
  - Formalism.FourierDecayAlt.P.LEx2.lemmaE_closed
  - Formalism.FourierDecayAlt.P.le_E_proof
  - Formalism.FourierDecayAlt.P.LEx2.lemmaE
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lemma E for energy systems

Lemma E computes the limit of an energy as a cutoff is removed. The energy of a word $w = (Y_1, \dots, Y_n)$ of real numbers is built by $n$ applications of an operator, one for each letter, and the lemma says that it tends to $\prod_i |P(Y_i)|$ times the energy of the empty word, where $P$ is a fixed polynomial. This section sets up the abstract frame, an *energy system*, and proves the lemma from a one-step identity. The one-step identity is where the analysis lies: a Cauchy estimate for a smooth cutoff and a Markov inequality for polynomials with values in a normed space. Lemma E is applied to the model setting in [the next section](/entry/lemma-model/).

**Definition 3.5.1 (Weighted base).** A *base* is a measure space $(\Omega, \mu)$ with a measurable function $G : \Omega \to (0, \infty)$. For a finite set $A$, a *field* is a function $u : \Omega \times A \to \mathbb{C}$. For $\varphi : \mathbb{R} \to \mathbb{R}$ let $\varphi u$ denote $(\omega, a) \mapsto \varphi(G(\omega))\, u(\omega, a)$. For weights $\mathrm{wt} \geq 0$ put $|u|^2_{\mathrm{wt}}(\omega) = \sum_a \mathrm{wt}(\omega, a) |u(\omega, a)|^2$. For an operator $T$ on fields and $s \in \mathbb{R}$, the *conjugate* is $T_s u = G^{-s}\, T(G^s u)$, and $\partial^p T u$ is the $p$-th derivative of $s \mapsto T_s u$ at $s = 0$.

The function $G$ plays the role of a radial coordinate, and $T_s$ measures how $T$ fails to commute with powers of $G$. In the application $G$ is a norm on a cone of matrices, and the cutoff removes a neighborhood of its boundary.

**Definition 3.5.2 (Cutoff and regularizer).** A *cutoff* is a smooth $\chi : \mathbb{R} \to [0, 1]$ with $\chi(x) = 0$ for $x \leq 1/2$ and $\chi(x) = 1$ for $x \geq 1$. Put $\chi_\varepsilon(x) = \chi(x/\varepsilon)$. For $\varepsilon > 0$ and $\sigma \in \mathbb{R}$ the *regularizer* is $\theta_{\varepsilon, \sigma}(x) = (x / (x + \varepsilon))^\sigma$. For $\varphi$ with $u \mapsto \varphi(e^u)$ smooth, let $\varphi^{[p]}(x)$ be the $p$-th derivative of $u \mapsto \varphi(e^u)$ at $u = \log x$.

**Definition 3.5.3 (Step).** A *step* over a base consists of a finite set $\iota$, a field $X$ on $\iota$, weights $d_0 > 0$ on $\iota$, and for each $Y \in \mathbb{R}$: an operator $g(Y)$ from fields on $\iota$ to fields on $\{0, 1\} \times \iota$, an operator $g^*(Y)$ back, weights $d(Y)$ on $\{0, 1\} \times \iota$, and matrices $e(Y)(\omega) \in M_\iota(\mathbb{C})$. It also has an integer $r$, a function $P$ and an interval $J = [a, a + L]$. Write $g_s(Y) = g(Y)_s X$. For a cutoff $\chi$ and constants $\sigma, C_R, C_d, C_P$, the step is *admissible* if:

1. all data are measurable, the weights are positive, and $P$ is continuous and nonzero on $J$;
2. (*norm identity*) $g^*(Y)(d(Y)\, g(Y) X) = |P(Y)|\, d_0 X$ for $Y \in J$;
3. (*adjoint*) $g^*(Y)$ is the adjoint of $g(Y)$ for the weight $d(Y)$, tested against $\chi_{\varepsilon'} \theta_{\varepsilon, \sigma} X$;
4. (*locality*) there are $m$ and fields $c_q$ with $g(Y)(\varphi X) = \sum_{q \leq m} \varphi^{[q]}(G)\, c_q$ for all $\varphi$ as above;
5. (*polynomiality*) $g_s(Y)$ is a polynomial in $s$ of degree at most $r + 1$, and $\theta\, |g_s(Y)|^2_{d(Y)}$ is integrable, with an integral continuous in $Y$;
6. (*shift*) for $Y, Y + s \in J$, the $0$-part of $g_s(Y)$ is that of $g(Y + s) X$, and the $1$-part is that of $g(Y + s) X$ plus $(e(Y) - e(Y + s))$ applied to the $0$-part;
7. (*bounds*) $\sum_i d(Y)_{1,i} |((e(Y) - e(Y + s)) v)_i|^2 \leq C_R^2 \sum_i d(Y)_{0,i} |v_i|^2$, $d(Y) \leq C_d\, d(Y + s)$ and $|P(Y + s)| \leq C_P |P(Y)|$, for $Y, Y + s \in J$.

The norm identity says that, formally, $\|g(Y) X\|^2 = |P(Y)| \|X\|^2$. The difficulty is that this computation integrates by parts across the boundary of the cone, and the cutoff makes this rigorous.

**Lemma 3.5.4 (Cauchy estimate).** For $\sigma \geq 4$, $\varepsilon > 0$, $p \in \mathbb{N}$ and $u \in \mathbb{R}$, the function $f(v) = (1 + \varepsilon e^{-v})^{-\sigma}$ satisfies $|f^{(p)}(u)| \leq e\; p!\; (4\sigma)^p f(u)$.

*Proof.* The function $f$ extends holomorphically to the disc $|z - u| \leq \rho$ with $\rho = 1/(4\sigma) \leq 1/16$. Put $x = \varepsilon e^{-u} > 0$. Then $f(z)/f(u) = (1 + \delta)^{-\sigma}$ with $\delta = x(e^{-(z - u)} - 1)/(1 + x)$, and $|\delta| \leq e^\rho - 1 \leq 1.1 \rho$. So $|(1 + \delta)^{-\sigma}| \leq (1 - |\delta|)^{-\sigma} \leq e^{1.2 \sigma \rho} < e$. The Cauchy estimate for the $p$-th derivative on this disc gives $|f^{(p)}(u)| \leq p!\, \rho^{-p}\, e\, f(u)$. $\square$

Since $\theta_{\varepsilon, \sigma}(e^v) = (1 + \varepsilon e^{-v})^{-\sigma}$, the lemma bounds $\theta^{[p]}_{\varepsilon, \sigma}$ by $e\, p!\, (4\sigma)^p\, \theta_{\varepsilon, \sigma}$, uniformly in $\varepsilon$.

**Lemma 3.5.5 (Markov inequality).** Let $H$ be a real normed space, let $a_0, \dots, a_d \in H$, and let $q(t) = \sum_k t^k a_k$. If $\|q(t)\| \leq M$ for $t \in [t_0, t_0 + L]$ with $L > 0$, then $\|q^{(j)}(t)\| \leq (2d^2/L)^j M$ on the same interval, for each $j \geq 0$.

*Proof.* For a real polynomial $p$ of degree at most $d$ with $|p| \leq M$ on $[-1, 1]$, Markov's inequality gives $|p'| \leq d^2 M$ there (P. Borwein and T. Erdélyi, *Polynomials and Polynomial Inequalities*, Section 5.1). An affine change of variable carries $[t_0, t_0 + L]$ to $[-1, 1]$ and multiplies the bound by $2/L$. For $H$, apply this to $\lambda \circ q$ for each functional $\lambda$ of norm at most $1$, and use the Hahn-Banach theorem. Since $q'$ again has degree at most $d$, induction on $j$ gives the claim. $\square$

**Theorem 3.5.6 (One step).** Let $\sigma \geq 4$, $C_R, C_d, C_P \geq 0$, put $C_7 = C_d C_P (1 + C_R)^2$, and let a step be admissible for these constants, with $L > 0$ and
$$16 \sigma (r + 1)^2 (1 + 2e \sqrt{C_7}) \leq L.$$
If $|X|^2_{d_0}$ is integrable, then for each $Y \in J$ the function $|g(Y) X|^2_{d(Y)}$ is integrable and
$$\int_\Omega |g(Y) X|^2_{d(Y)}\, d\mu = |P(Y)| \int_\Omega |X|^2_{d_0}\, d\mu.$$

*Proof (outline).* Insert the regularizer $\theta = \theta_{\varepsilon, \sigma}(G)$ and the cutoff. By locality and polynomiality, the Leibniz rule writes $g(Y)(\theta X)$ as $\sum_{p \leq r + 1} \theta^{[p]}\, \partial^p g(Y) X / p!$. With the adjoint property and the norm identity, $|P(Y)| \int \theta |X|^2_{d_0}$ becomes the regularized energy $E_\varepsilon(Y) = \int \theta |g(Y) X|^2_{d(Y)}$ plus error terms with $p \geq 1$. The Cauchy estimate bounds $\theta^{[p]}$ by $e\, p!\, (4\sigma)^p \theta$. The derivatives $\partial^p g(Y) X$ are derivatives of a polynomial of degree $r + 1$ in $s$, so the Markov inequality on $[0, L]$ bounds them by $(2(r + 1)^2/L)^p$ times the size of $g_s(Y)$ for $s \in [0, L]$. The shift formula and the bounds of condition 7 compare $g_s(Y)$ with $g(Y + s) X$, so the error is at most a geometric series in $8\sigma (r + 1)^2 \sqrt{C_7} / L$ times the supremum of $E_\varepsilon / |P|$ over $J$. The condition on $L$ makes the ratio at most $1/2$, so the error is absorbed, and the energies are bounded uniformly in $\varepsilon$. Fatou's lemma and dominated convergence as $\varepsilon \to 0$ give integrability and the identity. $\square$

**Definition 3.5.7 (Energy system).** An *energy system* consists of a base, a cutoff $\chi$, integers $k, r$, reals $\lambda_1, \dots, \lambda_{k + 2r + 1}$, reals $\alpha < \beta$, an integer $N$, a length $L$, an energy $\mathcal{E}_\varepsilon(w) \in \mathbb{R}$ for $\varepsilon > 0$ and each finite word $w$ of pairs $(b, Y) \in \{0, 1\} \times \mathbb{R}$, a step for each finite list of reals, and a family for each $n$ (described below). For each list $w$, the step of $w$ has $P(Y) = \prod_s (Y + \lambda_s)$, $J = [a_w, a_w + L]$ with $a_w = \alpha + (\beta - \alpha)/3 + 2|w| L$, and the same $r$; and the density of the step of $Y :: w$ is $|g(Y) X|^2_{d(Y)}$ for the step of $w$. Let $\rho(w) = |X|^2_{d_0}$ be the density of the step of $w$, and $j = \int \rho(())\, d\mu$.

So the density of $(Y_1, \dots, Y_n)$ is obtained from the base density by $n$ steps, and the one-step theorem multiplies its integral by $|P(Y_1)|$ at each step.

**Definition 3.5.8 (Families).** A *family* of length $n$ consists of finite sets $R$ and $\iota$, a field $u$ on $R$, operators $g_Y$ from fields on $R$ to fields on $\iota$ for $Y \in \mathbb{R}^n$, a weight $W > 0$, coefficients $c_Y > 0$, fields $m_y$ on $\iota$ and matrices $B_Y(\omega)$, and intervals $J_a$. Its density at $Y$ is $|g_Y u|^2_{W^n c_Y}$. The family is *admissible* if all data are measurable and positive; if it factors, $(g_Y)_s u = B_Y\, m_{Y + s}$ for $Y \in \prod J_a$; if $B_Y$ and its inverse are bounded and measurable; if $y \mapsto m_y$ is a polynomial of degree at most $r + 1$ in each variable; and if each $g_Y$ is local in the sense of condition 4.

**Definition 3.5.9 (Admitted words, size).** A word $w = ((b_1, Y_1), \dots, (b_n, Y_n))$ is *admitted* if each $Y_i \in [\alpha, \beta]$ and $|Y_i - Y_j| > 2$ for $i \neq j$. Its *size* is $\mathrm{size}(w) = \prod_i |P(Y_i)|$. The *boxes* are $I_a = [a', a' + L]$ with $a' = \alpha + (\beta - \alpha)/3 + 2aL$, and a list $(Y_1, \dots, Y_n)$ *lies on the boxes* if $Y_i \in I_{n - i}$. The word $w^+$ of a list is the word with all $b_i = 1$.

**Theorem 3.5.10 (Lemma E).** Let $C_R, C_d, C_P \geq 0$, $C_2 \geq 64(1 + 2e\sqrt{C_7})$ and $C_6 \geq 6 C_2$. Let an energy system satisfy $r + 1 \leq N$, $L = C_2 N (r + 1)^2$, and
$$C_6 \big(k N (r + 1)^2 + N^2 (r + 1)^2\big) \leq \beta - \alpha.$$
Assume the following.

1. No $-\lambda_s$ lies in $[\alpha, \beta]$.
2. For $\varepsilon > 0$ and $n \leq N$ there is a real polynomial $Q$ in $n$ variables, of degree at most $k + 2r + 1$ in each, with $\mathcal{E}_\varepsilon(w) = Q(Y_1, \dots, Y_n)$ for each admitted word $w$ with these $Y_i$, whatever its entries $b_i$.
3. The base density $\rho(())$ is integrable.
4. (*Theorem P*) For each list $Y$ of length $n \leq N$ on the boxes and $\varepsilon > 0$, $\mathcal{E}_\varepsilon(Y^+)$ is the integral of the density of the family of length $n$ at $Y$, with $u$ replaced by $\chi_\varepsilon(G) u$.
5. Each step of a list on the boxes of length less than $N$ is admissible with $\sigma = 4N$ and the constants $C_R, C_d, C_P$, and each family of length at most $N$ is admissible.

Then for each admitted word $w$ of length at most $N$, $\mathcal{E}_\varepsilon(w) \to \mathrm{size}(w)\, j$ as $\varepsilon \to 0^+$.

Lean: `Formalism.FourierDecayAlt.P.LEx2.lemmaE_closed` (also `Formalism.FourierDecayAlt.P.le_E_proof`, a second name, and `Formalism.FourierDecayAlt.P.LEx2.lemmaE`, the same statement with the Cauchy estimate and the Markov inequality as hypotheses).

*Proof.* With $\sigma = 4N$, the condition of the one-step theorem reads $64 N (r + 1)^2 (1 + 2e\sqrt{C_7}) \leq L$, which holds since $L = C_2 N (r + 1)^2$. The bound on $\beta - \alpha$ and $C_6 \geq 6 C_2$ give $kL \leq \beta - \alpha$, $(k + 2r + 1) L \leq \beta - \alpha$ and $6 N L \leq \beta - \alpha$. So the boxes $I_0, \dots, I_{N-1}$ lie in the middle third of $[\alpha, \beta]$, a box of higher index lies at distance at least $L > 2$ to the right, and each list on the boxes gives an admitted word. *Claim.* For each list $w$ on the boxes of length at most $N$, $\rho(w)$ is integrable and $\int \rho(w) = \mathrm{size}(w^+)\, j$. This follows by induction on the length: the one-step theorem, applied to the step of $w$ at $Y \in J$, gives $\int \rho(Y :: w) = |P(Y)| \int \rho(w)$. *Limit on boxes.* By Theorem P, $\mathcal{E}_\varepsilon(w^+)$ is the integral of the family density with $u$ replaced by $\chi_\varepsilon u$. By the factorization and the polynomial form of $m$, this density is a finite sum of products of bounded coefficients with fields $\varphi^{[p]}(G)$ times square integrable fields. As $\varepsilon \to 0$, $\chi_\varepsilon(G) \to 1$, the derivatives tend to zero in $L^2$, and $\mathcal{E}_\varepsilon(w^+) \to \int \rho(w) = \mathrm{size}(w^+)\, j$. *All admitted words.* Since no $-\lambda_s$ lies in $[\alpha, \beta]$, $P$ has constant sign there, so $\mathrm{size}(w) = \pm \prod_i P(Y_i)$ is a polynomial of degree $k + 2r + 1$ in each variable. By assumption 2, $\mathcal{E}_\varepsilon$ is a polynomial of the same degree in each variable. Choose $k + 2r + 2$ distinct points in each box; a list whose $i$-th entry is one of the points of $I_{n - i}$ lies on the boxes. A polynomial of degree at most $D$ in each variable is determined by its values on a product of $D + 1$ points per coordinate, by Lagrange interpolation, and its coefficients are linear in these values. So the coefficients of $\mathcal{E}_\varepsilon$ converge to those of $j\, \mathrm{size}$, and $\mathcal{E}_\varepsilon(w) \to \mathrm{size}(w)\, j$ for each admitted $w$. $\square$

**Remark 3.5.11 (Formalization).** The statement is `LE.LemmaE` ([StatementLE.lean](lean:Formalism/HermitianCurvature/StatementLE.lean#L577)), and the conditions are the definitions of that file: `Step.Imports` (line 208), `Fam.Imports` (line 382), `Sys` (line 450) and its predicates. `lemmaE` ([DerivedCoefficientIntegrable.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/DerivedCoefficientIntegrable.lean#L425)) feeds seventeen steps to `le_eFromConstituents_proof`, among them `stepClaim hC hMV` for the one-step theorem; `lemmaE_closed` (line 430) supplies `cauchy_theta_identity` (Cauchy.lean, line 94) and `markov_inequality_vector` (Markov.lean, line 429, derived from the scalar `markov_inequality` at line 288). The second name `le_E_proof` is declared at line 540, after the namespace is closed, with its full name. We opened the statements of the steps (`StepClaimFromSteps`, `ClaimInduction`, `ReduceToBoxes`, `BoxLimitFromClaim` and the others) but not their proofs, so the proofs above are ours, in outline where marked; the proof of the Cauchy estimate is our own argument along the lines of Cauchy.lean. The energy of the system is a field named `principalHermitianLattice`, a name with no relation to its role. Assumption 2 asks for one polynomial for all choices of the entries $b_i$, so the limit does not see them.
