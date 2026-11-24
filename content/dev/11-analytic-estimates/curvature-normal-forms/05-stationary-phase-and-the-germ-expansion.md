---
title: Stationary phase and the germ expansion
decls:
  - Formalism.FourierDecayAlt.P.StationaryPhaseModel.F_zero_small
  - Formalism.FourierDecayAlt.P.StationaryPhaseModel.F_zero
  - Formalism.FourierDecayAlt.P.stationary_phase_holomorphic
  - Formalism.FourierDecayAlt.P.stationary_estimate
  - Formalism.FourierDecayAlt.P.nonstationary_estimate
  - Formalism.FourierDecayAlt.P.germ_rate
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Stationary phase and the germ expansion

This section proves the germ expansion with a rate. An orbital integral at a point near a block matrix is compared with a finite sum of orbital integrals at long Weyl points, with an error of size $O(|t|)$. The theorem has no hypothesis. The proof is a stationary phase argument for a holomorphic phase in several complex variables: a change of variables turns the block integral into an oscillatory integral, the critical points are the roots of one equation, nonstationary phase bounds the part far from the roots, and stationary phase at each root gives the main terms. The theorem, and the weaker germ expansion that follows from it, are inputs of the definite side in the step [nonempty hypotheses](/step/nonempty-hyps/).

### Characters, measures and orbital integrals

Fix $\beta \in \mathbb{C}$, $\beta \ne 0$. Put $\psi(w) = \exp(i\, \mathrm{Re}(\beta w))$, a unitary character of $\mathbb{C}$, and let $\mu$ be $|\beta| / 2\pi$ times Lebesgue measure on $\mathbb{C}$. On $\mathbb{C}^d$, or on the space of strictly upper triangular matrices, we use the product of copies of $\mu$; see [the Fourier transform](/learn/analysis/#the-fourier-transform) for this self-dual normalization. All functions take values in a complex Banach space $V$.

Let $m \in \mathbb{N}$ and $n = m + 2$. Let $w_n$ be the antidiagonal permutation matrix of size $n$ and $U_n$ the upper unipotent group. For $\Phi$ on $n \times n$ complex matrices and $z \in \mathbb{C}$, the *long orbital integral* is

$$\Omega(z) = \int_{U_n} \psi\Bigl(\sum_i u_{i, i+1}\Bigr)\, \Phi(z\, w_n u)\, du .$$

For $t, c \in \mathbb{C}$ the *block orbital integral* $\Omega_B(t, c)$ is the integral of $\Phi(\ell\, \mathrm{diag}(t w_{n-1}, c)\, u')$ against $\psi$ of the subdiagonal sum of $\ell$ and of the superdiagonal sum of $u'$. Here $\ell$ is lower unipotent with free entries only in the last row, and $u'$ is upper unipotent of size $n$.

**Definition 1.5.1 (Derivative bound).** Let $k \in \mathbb{N}$, $A, K \ge 0$ and let $K_c \subset \mathbb{C}$. A function $\Phi$ satisfies the *derivative bound* $(k, A, K)$ over $K_c$ if, at every $Z$ with $\det Z \in \det(w_{n-1}) K_c$, $\Phi$ is $C^k$ and $\|D^j \Phi(Z)\| \le K \min(1, \|Z\|^{-A})$ for $j \le k$.

**Definition 1.5.2 (Remainder).** The *remainder* is

$$\begin{aligned} R(t, c) = {} & |t|^{(m+1)^2}\, \Omega_B(t, c) \\ & - \frac{1}{m+2} \sum_{z} |z|^{(m+1)^2}\, \psi\Bigl(\frac{(m+2) z}{t}\Bigr)\, \Omega(z), \end{aligned}$$

where $z$ runs over the roots of $z^{m+2} = (-1)^{m+3} c\, t^{m+1}$.

### Stationary phase for a holomorphic phase

The model result is a stationary phase bound for $\int \psi(g/t)\, a$ with $g$ holomorphic. The constant does not depend on $g$ or on the critical point, which matters later, when the bound is integrated over a parameter.

**Lemma 1.5.3 (Stationary phase at the origin, small parameter).** Let $d \ge 1$ and $r, \Lambda > 0$. There is $C \ge 0$ with this property. Let $g$ be holomorphic on the ball $B(0, 2r) \subset \mathbb{C}^d$ with $|g| \le \Lambda$ there, with $\partial g(0) = 0$, complex Hessian $H$ at $0$, and $\|x\| \le \Lambda \|\partial g(x)\|$ for $\|x\| \le r$. Let $a$ be of class $C^{2d+2}$ with support in the closed ball of radius $r$ and $\|D^j a\| \le S$ for $j \le 2d + 2$. Then for $0 < |t| \le 1$,

$$\Bigl\| \int \psi\bigl(g/t\bigr)\, a\, d\mu - \psi\bigl(g(0)/t\bigr) \frac{|t|^d}{|\det H|}\, a(0) \Bigr\| \le C S |t|^{d+1}.$$

Lean: `Formalism.FourierDecayAlt.P.StationaryPhaseModel.F_zero_small`

*Proof.* Put $c = \beta |t| / t$, so $|c| = |\beta|$ and $\mathrm{Re}(\beta g / t) = \mathrm{Re}(c g) / |t|$. Thus $\psi(g/t) = e^{i \varphi / |t|}$ with the real phase $\varphi = \chi \cdot \mathrm{Re}(c g)$, where $\chi$ is a bump equal to $1$ on the ball of radius $5r/4$ and supported in $B(0, 2r)$. On the support of $a$ the bump is $1$.

Cauchy estimates on balls of radius $\delta = r / (d + 7)$ bound the derivatives of $\varphi$ of order up to $d + 6$ by $|\beta| \Lambda \max(1, \delta^{-1})^{d+6}$. The hypothesis $\|x\| \le \Lambda \|\partial g(x)\|$ gives, for each $x$ in the ball of radius $r$, a real direction in which the derivative of $\varphi$ is at least a fixed multiple of $\|x\|$. So $0$ is the only critical point of $\varphi$ on the support of $a$, and it is nondegenerate. The same hypothesis bounds $|\det H|$ from below, and Cauchy estimates bound the entries of $H$ by $\Lambda (r/2)^{-2}$.

A real stationary phase reduction then compares the integral with the integral of $a(0)$ times a cutoff against $e^{i q / |t|}$, where $q$ is the quadratic part of $\varphi$ at $0$; the error is $C S |t|^{d+1}$. Last, a Gaussian model computes the quadratic integral. The real Hessian of $\mathrm{Re}(c g)$ at $0$ has signature zero and determinant of absolute value $|\beta|^{2d} |\det H|^2$, so the classical factor is $(2\pi |t|)^d / (|\beta|^d |\det H|)$, and the factor $(|\beta| / 2\pi)^d$ of the measure turns it into $|t|^d / |\det H|$, again with error $O(S |t|^{d+1})$. $\square$

**Lemma 1.5.4 (Stationary phase at the origin).** The bound of the previous lemma holds, with a new constant, for all $t \ne 0$.

Lean: `Formalism.FourierDecayAlt.P.StationaryPhaseModel.F_zero`

*Proof.* For $|t| \le 1$ this is the previous lemma. Let $|t| \ge 1$ and let $M$ be the $\mu$-measure of the closed ball of radius $r$. The integral has norm at most $S M$. To bound the main term, apply the previous lemma at $t = 1$ with the amplitude $a = \chi_r$, a fixed bump with $\chi_r(0) = 1$ and derivative bound $S_\chi$. The integral then has norm at most $S_\chi M$, so $1 / |\det H| \le S_\chi M + C_0 S_\chi = D_1$. Hence the main term has norm at most $|t|^d D_1 S$, and the difference is at most $(M + D_1) S |t|^{d+1}$, since $1 \le |t|^d \le |t|^{d+1}$. $\square$

**Theorem 1.5.5 (Stationary phase for a holomorphic phase).** Let $d \in \mathbb{N}$ and $r, \Lambda > 0$. There is $C$ such that for every $x_0 \in \mathbb{C}^d$, every $g$ holomorphic on $B(x_0, 2r)$ with $|g| \le \Lambda$, $\partial g(x_0) = 0$, complex Hessian $H$ at $x_0$ and $\|x - x_0\| \le \Lambda \|\partial g(x)\|$ for $\|x - x_0\| \le r$, every $a$ as above with support in the closed ball of radius $r$ about $x_0$, and every $t \ne 0$,

$$\Bigl\| \int \psi\bigl(g/t\bigr)\, a\, d\mu - \psi\bigl(g(x_0)/t\bigr) \frac{|t|^d}{|\det H|}\, a(x_0) \Bigr\| \le C S |t|^{d+1}.$$

Lean: `Formalism.FourierDecayAlt.P.stationary_phase_holomorphic`

*Proof.* If $d = 0$, the measure is the point mass, the empty determinant is $1$, and the difference is $0$. If $d \ge 1$, apply the previous lemma to $x \mapsto g(x_0 + x)$ and $x \mapsto a(x_0 + x)$; the measure is invariant under translation. $\square$

### The phase function and the two estimates

Put $D' = (-1)^{m+3} c\, t^{m+1}$. A change of variables, with coordinates $x \in \mathbb{C}^{m+1}$ and $y$ in the strictly upper triangular matrices of size $m + 2$, gives

$$|t|^{(m+1)(m+2)}\, \Omega_B(t, c) = \int \psi\bigl(g_0(x)/t\bigr)\, a(x, y)\, d\mu(x)\, d\mu(y),$$

with the phase $g_0(x) = \sum_k x_k + D' / \prod_k x_k$ and an amplitude $a$ built from $\Phi$. Let $a_\varepsilon$ be the amplitude built from $\Phi$ times the cutoff $\chi(\|Z\| / |t|^{-\varepsilon})$. The critical points of $g_0$ on $(\mathbb{C}^\times)^{m+1}$ are the diagonal points $x = (z, \dots, z)$ with $z^{m+2} = D'$. There $g_0 = (m+2) z$, the complex Hessian is $z^{-1}(1 + J)$ with $J$ the all ones matrix, and its determinant is $(m+2) z^{-(m+1)}$. So the factor $|t|^d / |\det H|$ with $d = m + 1$ is $|t|^{m+1} |z|^{m+1} / (m+2)$.

Fix a compact $K_c \subset \mathbb{C} \setminus \{0\}$. A number $\delta > 0$ is *small* if $100(m+2)\delta \le |z|$ for every root $z$ of $z^{m+2} = D'$ with $D' \in K_c$. For a root $z$, let $\chi_{\delta, z}(x)$ be a cutoff equal to $1$ for $\|x - (z, \dots, z)\| \le \delta$ and $0$ for distance at least $2\delta$. For $\delta$ small, the cutoffs at different roots have disjoint supports. Put $\chi_{\mathrm{far}} = 1 - \sum_z \chi_{\delta, z}$.

**Theorem 1.5.6 (Stationary estimate).** There is $E \in \mathbb{N}$ with this property. Let $\beta \ne 0$, let $K_c$ be compact in $\mathbb{C} \setminus \{0\}$, let $\delta$ be small and $0 < \varepsilon \le 1 / (2(m+2))$. There are $C$ and $t_0 > 0$ such that for every $\Phi$ with a derivative bound $(k, A, K)$ over $K_c$, where $A \ge E (m+2)^2$ and $k \ge 2m + 4$, every $t$ with $0 < |t| \le t_0$ and $c\, t^{m+1} \in K_c$, and every root $z$,

$$\begin{aligned} \Bigl\| & \int \chi_{\delta, z}(x)\, \psi\bigl(g_0(x)/t\bigr)\, a_\varepsilon(x, y)\, d\mu\, d\mu \\ & - \psi\Bigl(\frac{(m+2) z}{t}\Bigr) \frac{|t|^{m+1} |z|^{m+1}}{m+2} \int a_\varepsilon(z, y)\, d\mu(y) \Bigr\| \le C K |t|^{m+2}. \end{aligned}$$

Lean: `Formalism.FourierDecayAlt.P.stationary_estimate`

*Proof.* Fix $y$ and apply the stationary phase theorem in $x$ with $x_0 = (z, \dots, z)$, radius $2\delta$, and amplitude $\chi_{\delta, z} \cdot a_\varepsilon(\cdot, y)$. Near the critical point, $g_0$ is holomorphic, the $x_k$ do not vanish, $|g_0| \le \Lambda$, and $\|x - x_0\| \le \Lambda \|\partial g_0(x)\|$, with $\Lambda$ uniform in $z$ for $z$ in a bounded set. The amplitude is $C^{2m+4}$ with derivatives bounded by $C K (1 + \|y\|)^{E(m+2)^2} \max(1, \|y\|)^{-A}$. The pointwise error is that majorant times $|t|^{m+2}$. The majorant is integrable in $y$ when $A$ is large, so integration in $y$, justified by Fubini and the continuity of the amplitude in $y$, gives the bound. $\square$

**Theorem 1.5.7 (Nonstationary estimate).** There are $C_0 > 0$ and $C_2$ in $\mathbb{N}$ with this property. Let $\beta \ne 0$, $K_c$ compact in $\mathbb{C} \setminus \{0\}$, $\delta$ small and $0 < \varepsilon \le 1 / (C_0 (m+2))$. There are $C$ and $t_0 > 0$ such that for every $\Phi$ with a derivative bound $(k, A, K)$ over $K_c$, where $A \ge (m+1)(m+4) + 1$ and $k \ge C_2 (m+2)^2$, and every $t$ with $0 < |t| \le t_0$ and $c\, t^{m+1} \in K_c$,

$$\Bigl\| \int \chi_{\mathrm{far}}(x)\, \psi\bigl(g_0(x)/t\bigr)\, a_\varepsilon(x, y)\, d\mu\, d\mu \Bigr\| \le C K |t|^{m+2}.$$

Lean: `Formalism.FourierDecayAlt.P.nonstationary_estimate`

*Proof.* The tool is repeated integration by parts with the Wirtinger derivatives. If $\|\partial g\| \ge \eta$ on an open set that holds the support of $a$, $\|\partial^{j+1} g\| \le \|\partial g\|\, L^j$ for $1 \le j \le q$, and $\|D^j a\| \le S L^j$ for $j \le q$, then

$$\Bigl\| \int \psi\bigl(g/t\bigr)\, a\, d\mu \Bigr\| \le C S \Bigl(\frac{|t|\, L}{\eta}\Bigr)^{q} \mu(\mathrm{supp}\, a).$$

On the support of $\chi_{\mathrm{far}}\, a_\varepsilon$ we have $\|x\|, \|y\| \le 2|t|^{-\varepsilon}$, $|x_k| \ge c_0 |t|^{(m+2)\varepsilon}$, and $x$ has distance at least $\delta$ from every critical point. Away from the critical points, $\|\partial g_0\|$ is bounded below by some $c_\delta > 0$. The higher derivatives of $g_0$ satisfy the relative bound with $L$ of size $|t|^{-(m+2)\varepsilon}$, and the amplitude has derivative bounds $C K |t|^{-\varepsilon C_9 (m+2)(j+1)}$. Each integration by parts gains a factor $|t|^{1 - O((m+2)\varepsilon)}$, and the support has measure polynomial in $|t|^{-\varepsilon}$. For $\varepsilon \le 1 / (C_0 (m+2))$ and $q$ of size $C_2 (m+2)^2$ the product is at most $C K |t|^{m+2}$. $\square$

### The germ expansion

**Theorem 1.5.8 (Germ expansion with a rate).** There are $C_1, C_2 \in \mathbb{N}$ with this property. For every $m$, every $\beta \ne 0$ and every compact $K_c \subset \mathbb{C} \setminus \{0\}$ there is $C$ such that for every complete $V$, every $\Phi$ with a derivative bound $(k, A, K)$ over $K_c$ with $A \ge C_1 (m+2)^2$ and $k \ge C_2 (m+2)^2$, and all $t \ne 0$ and $c$ with $c\, t^{m+1} \in K_c$,

$$\| R(t, c) \| \le C K |t| .$$

Lean: `Formalism.FourierDecayAlt.P.germ_rate`

*Proof.* Take $C_0$, $C_2$ from the nonstationary estimate, $E_1$ from the stationary estimate and $E_2$ from the amplitude limit below. Put $\varepsilon = 1/((C_0 + 2)(m+2))$, $C_1 = E_1 + E_2 + 3(C_0 + 2) + 3$, and use $C_2 + 2$ for the order. Choose a small $\delta$.

1. *Large $t$.* For $|t| \ge t_0$ both terms of $R$ are bounded by $C K$, so $\|R\| \le C K |t|$.
2. *Tail.* Write $\Phi = \chi \Phi + (1 - \chi) \Phi$ with the cutoff at radius $|t|^{-\varepsilon}$. The tail bound gives $|t|^{(m+1)^2} \|\Omega_B((1-\chi)\Phi)\| \le C K |t|$ when $A \ge (m+1)(m+4) + (3m+4)/\varepsilon$.
3. *Split.* Change variables in $\Omega_B(\chi \Phi)$ and write $1 = \chi_{\mathrm{far}} + \sum_z \chi_{\delta, z}$. The polynomial $z^{m+2} - D'$ has $m + 2$ distinct roots since $D' \ne 0$.
4. *Far part.* The nonstationary estimate bounds it by $C K |t|^{m+2}$.
5. *Near parts.* The stationary estimate replaces the part at $z$ by the main term, with error $C K |t|^{m+2}$.
6. *Amplitude limit.* As $t \to 0$, $\int a_\varepsilon(z, y)\, d\mu(y)$ differs from $|z|^{-2(m+1)} \int \psi(\sum_i y_{i,i+1} / z)\, \Phi(w_n (z + y))\, d\mu(y)$ by at most $C K |t|$, and the substitution $y = z u$ shows that the last integral is $|z|^{(m+2)(m+1)}\, \Omega(z)$.

Multiply by $|t|^{(m+1)^2 - (m+1)(m+2)} = |t|^{-(m+1)}$. The errors of steps 4 to 6 become $C K |t|$, and the main terms become

$$\frac{|t|^{m+1} |z|^{m+1}}{(m+2)\, |t|^{m+1}}\, |z|^{-2(m+1)} |z|^{(m+2)(m+1)} = \frac{|z|^{(m+1)^2}}{m+2},$$

which are the coefficients in $R$. $\square$

**Remark 1.5.9 (Formalization).** The theorem is assembled at `HermitianCurvatureProofs/ChangeOfVariablesXy.lean:34` from thirteen proved steps. The assembly at `HermitianCurvatureProofs/StationaryPhaseEstimates.lean:688` takes the cutoff specification and the identity of exponents in the last display as inputs and uses neither; the cutoff specification still enters through the two estimates at lines 25 and 29, and the identity of exponents is redone inside the proof. The phase in the sum is the constant $1$; the weaker germ expansion of `HermitianCurvature/StatementG.lean:92` allows an unknown phase of modulus one and asks only that the error tends to $0$. The stationary phase theorem takes the derivative and the Hessian of $g$ as data with derivative conditions, though $g$ is holomorphic and they could be computed. It is declared at `HermitianCurvatureProofs/StationaryPhaseModel.lean:3260` with a full name, after the namespace of the file is closed. The case $|t| \ge 1$ of the stationary phase lemma gets its lower bound for $|\det H|$ from the case $t = 1$ with a bump amplitude (line 3171).
