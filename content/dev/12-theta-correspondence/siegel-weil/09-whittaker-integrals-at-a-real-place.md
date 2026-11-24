---
title: Whittaker integrals at a real place
decls:
  - PositivityTheory.Rg.Sw.WR.K.GB.clsGainB
  - PositivityTheory.Rg.Sw.WR.D.densOf3
  - PositivityTheory.Rg.Sw.WR.wr
  - PositivityTheory.Rg.Sw.SP.sPrime_of_minor
  - PositivityTheory.Rg.Sw.SP.wrOrd_of_minor
  - PositivityTheory.Rg.Sw.SP.wrOrd
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Whittaker integrals at a real place

This section studies the archimedean Whittaker integral of a polynomial-Gaussian section at a nondegenerate Hermitian matrix $\beta$. It proves two results. The first says that the integral continues to an entire function of the parameter $z$, and that its value at $z = 0$ is a multiple of the density of the Gram map at $\beta$. The second says that, when the Schwartz function lives on $m < n$ vectors, the integral vanishes to order $n - m$ at $z = 0$. The first result is the real place input of [the nondegenerate comparison](/entry/whit-gen-eq/) and of the comparison for $M < n$; the second is the real place input of [the low rank comparison](/entry/whit-gen-low/). See [Fourier coefficients and Whittaker functions](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions).

We use the notation of [the section on Gaussian moments](/entry/cyc-of/): $\mathcal{P}_{m,n}$, the signs $\varepsilon$, $c > 0$, and $p$ and $q$ for the numbers of signs $+$ and $-$.

**Definition 4.9.1 (Coordinates on Hermitian matrices).** Let $E_n$ be the space of real $n \times n$ matrices. For $y \in E_n$ put
$$h(y) = \tfrac{1}{2}(y + y^{t}) + \tfrac{i}{2}(y - y^{t}).$$
The map $h$ is a real linear bijection from $E_n$ onto the Hermitian $n \times n$ matrices. Put $d(y) = \operatorname{Re} \det(1 + h(y)^2)$, and for $t \in \mathbb{R}$ and $\beta \in E_n$ put $\chi_{t,\beta}(y) = \exp(-i t \sum_{a,b} \beta_{ab} y_{ab})$.

**Definition 4.9.2 (Cayley functions).** For $s = \pm 1$ put $u_s(y) = (1 - i s \, h(y))^{-1}$ and $v_s(y) = (1 + i s \, h(y))^{-1}$. Let $R$ be a polynomial in variables $r^{+}_{kl}$ and $r^{-}_{kl}$, and let $R(y)$ be its value at $r^{+} = v_s(y)$ and $r^{-} = u_s(y)$. For $z \in \mathbb{C}$ and $p, q \ge 0$ the Cayley function is
$$C_{s,z,p,q,R}(y) = d(y)^{-z} \det u_s(y)^{p} \det v_s(y)^{q} R(y).$$

**Definition 4.9.3 (Determinant operator).** For $k, l \le n$ let $D_{kl}$ be the derivative in the direction of the matrix with entry $(1+i)/2$ at $(k, l)$ plus the matrix with entry $(1-i)/2$ at $(l, k)$. Put
$$\Delta = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \, D_{1 \sigma(1)} \cdots D_{n \sigma(n)}.$$

The operator $\Delta$ is a determinant of first derivatives in the Hermitian coordinates. Its symbol is $\det h(\beta)$ up to powers of $-it$, so that one integration by parts against $\chi_{t,\beta}$ gives
$$\int f \chi_{t,\beta} = \frac{(-1)^n}{(-it)^n \det h(\beta)} \int \Delta f \cdot \chi_{t,\beta}$$
for smooth $f$ whose derivatives are dominated by integrable functions. Let $\sigma_P(b)$ be the function of [the section on Gaussian moments](/entry/cyc-of/) for $P \in \mathcal{P}_{m,n}$; the Fourier transform of a Gaussian shows that $\sigma_P(h(y)) = C_{t/c, 0, p, q, R}(y)$ for some $R$ when $t = \pm c$. See [the Fourier transform](/learn/analysis/#the-fourier-transform).

**Theorem 4.9.4 (Gain of decay).** Let $s = \pm 1$, $p, q, N \ge 0$ and $R$ be given. There are $J \ge 0$, polynomials $a_1, \dots, a_J$ in $z$, continuous functions $G_1, \dots, G_J$ on $E_n$ and a constant $C$ with $|G_j(y)| \le C d(y)^{-(p+q+N)/2}$, such that for all $z$ and $y$
$$\Delta^N C_{s,z,p,q,R}(y) = d(y)^{-z} \sum_{j} a_j(z) G_j(y).$$

Lean: `PositivityTheory.Rg.Sw.WR.K.GB.clsGainB`.

*Proof.* Each $D_{kl}$ applied to a Cayley function gives a sum of Cayley functions: the derivative of $d(y)^{-z}$ brings down a factor $z$ and a matrix entry of $u_s$ or $v_s$, and the derivatives of $u_s$ and $v_s$ are products of their entries. So $\Delta^N C_{s,z,p,q,R}$ is $d^{-z}$ times a sum of terms, each a polynomial in $z$ times a polynomial in the entries of $u_s$ and $v_s$ and their determinants. The operator $\Delta$ is a determinant in the derivatives, and the antisymmetry makes the leading terms combine into one more power of $\det u_s$ or $\det v_s$ for each application, which is a gain of $d^{-1/2}$. The proof writes the derivative through a Cauchy formula, uses the invariance of $\Delta$ under conjugation by unitary matrices to reduce to diagonal $h(y)$, and bounds the remaining terms by an explicit estimate on the diagonal. $\square$

**Theorem 4.9.5 (Density of the Gram map).** Let $c > 0$, $t = \pm c$, $P \in \mathcal{P}_{m,n}$ and $N$ with $n^2 < m + N$. There is a function $g$ on $E_n$, continuous on the set where $\det h(y) \ne 0$, with these two properties. For every compact $S$ in that set,
$$\int_{Q(x) \in h(S)} P(x) \, e^{-c \sum |x_{ai}|^2} \, dx = \int_S g(y) \, dy,$$
where $Q(x)$ is the Gram matrix of $x$ for the signature $\varepsilon$. For every $\beta$ with $\det h(\beta) \ne 0$,
$$\begin{aligned} \Bigl( \frac{2\pi}{|t|} \Bigr)^{n^2} g(\beta) = {} & \frac{1}{\det h(\beta)^N} \Bigl( \frac{(-1)^n}{(-it)^n} \Bigr)^N \\ & \cdot \int \Delta^N \bigl( \sigma_P \circ h \bigr)(y) \, \chi_{t,\beta}(y) \, dy. \end{aligned}$$

Lean: `PositivityTheory.Rg.Sw.WR.D.densOf3`.

*Proof.* By the Gaussian Fourier transform, $\sigma_P \circ h$ is a Cayley function with $z = 0$, and by [the gain of decay](/entry/cls-gain-b/) its $N$-th power of $\Delta$ is bounded by a multiple of $d^{-(p+q+N)/2}$. Since $d(y) \ge c'(1 + |y|^2)$ and $d^{-\sigma}$ is integrable for $\sigma > n^2/2$, the condition $n^2 < m + N$ makes $\Delta^N(\sigma_P \circ h)$ integrable, so the right side defines a continuous function of $\beta$ off the singular set. A mollifier argument shows that this function is the density of the image measure of $P e^{-c|x|^2} dx$ under the Gram map: one tests against smooth functions of compact support, applies Fourier inversion, and integrates by parts $N$ times. $\square$

**Theorem 4.9.6 (Whittaker integral at a real place).** Let $c > 0$, $t = \pm c$ and $P \in \mathcal{P}_{m,n}$. There is a function $g$ on $E_n$, continuous where $\det h \ne 0$ and with the density property of the previous theorem, such that for every $\beta$ with $\det h(\beta) \ne 0$ there are an entire function $W$ and a real $\sigma_0$ with:

1. for $\operatorname{Re} z > \sigma_0$ the function $d(y)^{-z} \sigma_P(h(y)) \chi_{t,\beta}(y)$ is integrable, and
$$W(z) = \int_{E_n} d(y)^{-z} \sigma_P(h(y)) \chi_{t,\beta}(y) \, dy;$$
2. $W(0) = (2\pi/|t|)^{n^2} g(\beta)$.

Lean: `PositivityTheory.Rg.Sw.WR.wr`.

*Proof.* Take $g$ from [the density theorem](/entry/dens-of3/) with $N = n^2 + 1$. Write $\sigma_P \circ h = C_{s,0,p,q,R}$ with $s = t/c$, so the integrand is $C_{s,z,p,q,R} \chi_{t,\beta}$. Every derivative of a Cayley function is bounded by a multiple of $d^{-(\operatorname{Re} z + (p+q)/2)}$, so the integral converges for $\operatorname{Re} z > n^2/2$, and integration by parts $N$ times gives
$$\int C_{s,z,p,q,R} \chi_{t,\beta} = K^N \sum_j a_j(z) \int d^{-z} G_j \chi_{t,\beta},$$
with $K = (-1)^n ((-it)^n \det h(\beta))^{-1}$. The right side, call it $W_N(z)$, is holomorphic on the half plane $\operatorname{Re} z > (n^2 - p - q - N)/2$. The functions $W_N$ agree with the integral for $\operatorname{Re} z > n^2/2$, so they agree with each other on their common domains, and together they define an entire $W$. At $z = 0$ the value is $W_{N}(0)$ for $N = n^2 + 1$, and the density formula identifies it with $(2\pi/|t|)^{n^2} g(\beta)$. $\square$

For the low rank case we need the Cayley operator on polynomials. Let $\mathcal{F}_n$ be the polynomials in variables $Y^{\pm}_{kl}$ with coefficients in $\mathbb{C}[X]$. For $s = \pm 1$, $m \ge 0$, a sign $b$ and $k, l \le n$ there is an operator $H^{b}_{kl}$ on $\mathcal{F}_n$; it is multiplication by $-\gamma_b \alpha_b Y^{b}_{lk}$ plus a derivative term, where $\gamma_{+} = is$, $\gamma_{-} = -is$, $\alpha_{+} = X$ and $\alpha_{-} = m + X$. For index embeddings $I, J$ of $\{1, \dots, \rho\}$ into $\{1, \dots, n\}$, the minor operator is $M^{b}_{I,J} = \sum_{\sigma} \operatorname{sgn}(\sigma) \prod_k H^{b}_{I(k) J(\sigma(k))}$. The Cayley operator $\mathcal{C}$ is the determinant of the operators that represent $\Delta$ on $\mathcal{F}_n$.

**Definition 4.9.7 (Minor formula).** The minor formula is the statement that for all $s = \pm 1$, $m$, $b$, $\rho$, $N$ and $I, J$,
$$\begin{aligned} (M^{b}_{I,J})^N 1 = {} & (\gamma_b^{\rho})^N \prod_{l < N} \prod_{i < \rho} \bigl( -\alpha_b - (l - i) \bigr) \\ & \cdot \det \bigl( Y^{b}_{J(p) I(q)} \bigr)_{p,q}^N. \end{aligned}$$

**Theorem 4.9.8 (Vanishing at zero).** Assume the minor formula. Let $s = \pm 1$, $m < n$, $t \ne 0$ and $\beta \in E_n$ with $\det h(\beta) \ne 0$. There are an entire function $W$ and a real $\sigma_0$ such that for $\operatorname{Re} z > \sigma_0$ the function $C_{s,z,m,0,1} \chi_{t,\beta}$ is integrable with
$$W(z) = \int_{E_n} C_{s,z,m,0,1}(y) \, \chi_{t,\beta}(y) \, dy,$$
and $W^{(j)}(0) = 0$ for all $j < n - m$.

Lean: `PositivityTheory.Rg.Sw.SP.sPrime_of_minor`.

*Proof.* The operator $\mathcal{C}$ applied $N$ times to $C_{s,z,m,0,1}$ gives $C_{s,z,m,0,1}$ times the value at $(u_s, v_s)$ of $\mathcal{C}^N 1$, with $X$ evaluated at $z$. The operators $H^{b}_{kl}$ commute. The minor formula shows that each minor operator applied to 1 produces a factor of a product of $X - j$ type terms. A power of $\det(Y^{-} + Y^{+})$ lies in the ideal generated by products $\mu^{-}_{I,J} \mu^{+}_{I',J'}$ of powers of minors of sizes $m + i$ and $j$ with $i + j = n - m$. Together these show that $X^{n-m}$ divides every coefficient of $\mathcal{C}^N 1$ for $N$ large. Integration by parts $N$ times, as in the proof of [the Whittaker integral theorem](/entry/wr/), then writes $W$ as $z^{n-m}$ times an entire function, so the derivatives of order less than $n - m$ vanish at 0. $\square$

The minor formula is proved in the development, and we now state the consequence for sections.

**Theorem 4.9.9 (Low rank Whittaker integral).** Assume the minor formula. Let $m < n$, a sign $b$, $c > 0$ with $t = c$ or $t = -c$, and $\beta \in E_n$ with $\det h(\beta) \ne 0$. Let $\varepsilon$ be the constant sign $b$ on $m$ rows. There are an entire function $W$ and a real $\sigma_0$ such that for $\operatorname{Re} z > \sigma_0$ the integrand below is integrable and
$$z^{n-m} W(z) = \int_{E_n} d(y)^{-z} \sigma_1(h(y)) \chi_{t,\beta}(y) \, dy,$$
where $\sigma_1$ is the function $\sigma_P$ of the polynomial $P = 1$ for $\varepsilon$, $c$ and $t$.

Lean: `PositivityTheory.Rg.Sw.SP.wrOrd_of_minor` (also `PositivityTheory.Rg.Sw.SP.wrOrd`, the same statement with the minor formula supplied).

*Proof.* Put $s = t/c$ if $b = +$ and $s = -t/c$ if $b = -$, so $s = \pm 1$. The Gaussian integral gives $d^{-z} \sigma_1 \circ h = (\pi/c)^{nm} C_{s,z,m,0,1}$. By [vanishing at zero](/entry/s-prime-of-minor/) the Cayley integral is an entire function $W_0$ whose derivatives of order less than $n - m$ vanish at 0. So $W_0(z) = z^{n-m} g(z)$ with $g$ entire, and $W = (\pi/c)^{nm} g$ satisfies the identity. The second name applies this to the proved minor formula. $\square$

**Remark 4.9.10 (Formalization).** The theorem on the gain of decay is stated in [GBClose.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/MollifiedIntegrability/GBClose.lean#L11), but the result it applies is in [ContDiffHerm.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/MollifiedIntegrability/ContDiffHerm.lean#L22); in the same way the density theorem applies a result from [CardAddB.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/MollifiedIntegrability/CardAddB.lean#L25), and the Whittaker integral theorem one from [ClsShift.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/MollifiedIntegrability/ClsShift.lean#L17). The file names do not match their contents. The Whittaker integral theorem uses the density theorem only with $N = n^2 + 1$. The statement of vanishing at zero is in [CayDivOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/MinorFormulas/CayDivOf.lean#L14), and the low rank theorem is proved in [SecOneConst.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/MinorFormulas/SecOneConst.lean#L73). The derivative term of $H^{b}_{kl}$ is not written out here.
