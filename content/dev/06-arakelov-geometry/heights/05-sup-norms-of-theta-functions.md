---
title: Mean and sup norms of theta functions
decls:
  - GroundTheory.Heights₂.Heights.ThetaBound.full
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Mean and sup norms of theta functions

This section bounds a theta function with half-integral characteristics in two ways. The first bound is an exact formula for the mean of the square of its normalized absolute value over a fundamental domain. The second bound is a pointwise bound for the same function. It has a factor that is small when the first coordinate of the point is far from the integers. The pointwise bound is uniform in the genus $g$ up to a term $Cg\log(2g)$, provided the imaginary part of the period matrix is reduced in the sense of the previous section. The two bounds are used in [the normalized form](/entry/nform/) of the chapter on sup norms of theta sections, where they compare the sup norm of a theta section with its $L^2$ norm.

### Theta functions with characteristics

Let $g \ge 1$. Let $X$ and $Y$ be real $g \times g$ matrices with $Y$ positive definite, and put $\Omega = X + iY$. For $a, b \in \mathbb{R}^g$ and $z \in \mathbb{C}^g$, the theta function with characteristics $a, b$ is
$$\theta[a,b](\Omega, z) = \sum_{k \in \mathbb{Z}^g} \exp\bigl(\pi i\, (k+a)^{\mathsf T} \Omega\, (k+a) + 2\pi i\, (k+a)^{\mathsf T}(z + b)\bigr).$$
The series converges absolutely, because the absolute value of the term is $\exp(-\pi q_Y(k+a) - 2\pi (k+a)^{\mathsf T} \operatorname{Im} z)$, where $q_Y(v) = v^{\mathsf T} Y v$.

**Definition 4.5.1 (Normalized theta function).** For $u_1, u_2 \in \mathbb{R}^g$ put
$$\|\theta\|(u_1, u_2) = \bigl|\theta[a,b](\Omega, \Omega u_1 + u_2)\bigr| \cdot \exp\bigl(-\pi\, q_Y(u_1)\bigr).$$

Every point $z \in \mathbb{C}^g$ is $\Omega u_1 + u_2$ for unique real $u_1, u_2$, since $Y$ is invertible. The factor $\exp(-\pi q_Y(u_1))$ compensates the growth of $\theta$ in the direction of $\Omega\mathbb{R}^g$. When $X$ is symmetric, it makes $\|\theta\|$ periodic in $u_1$ and $u_2$ with respect to $\mathbb{Z}^g$, so that $\|\theta\|$ is the pointwise norm of a section of a line bundle on the complex torus $\mathbb{C}^g/(\mathbb{Z}^g + \Omega\mathbb{Z}^g)$. We do not use this periodicity below; the integrals are over the cube $[0,1]^g \times [0,1]^g$.

**Definition 4.5.2 (Reduced imaginary part).** Let $Y$ be a real positive definite $g \times g$ matrix and $\rho \in \mathbb{R}$. We say that $Y$ is reduced with first minimum $\rho$ if

1. $\rho > 0$ and $\rho^2 \le 2g$;
2. $(Y^{-1})_{11} = \rho^2$;
3. $q_{Y^{-1}}(l) \ge \rho^2$ for every $l \in \mathbb{Z}^g \setminus \{0\}$;
4. $\det Y^{-1} \le \rho^2 (2g)^{g-1}$.

By the last remark of the previous section, every period matrix can be moved by $\mathrm{Sp}_g(\mathbb{Z})$ into this form; we do not use this here.

### Three lemmas

**Lemma 4.5.3 (Absolute value of a term).** Let $Y$ be symmetric. For $k \in \mathbb{Z}^g$, the term of index $k$ of $\theta[a,b](\Omega, \Omega u_1 + u_2)$ has absolute value $\exp(-\pi q_Y(k+a+u_1) + \pi q_Y(u_1))$. Hence
$$\|\theta\|(u_1,u_2) \le \sum_{k \in \mathbb{Z}^g} \exp\bigl(-\pi\, q_Y(k + a + u_1)\bigr).$$

*Proof.* Put $v = k + a$. The real part of the exponent is $-\pi q_Y(v) - 2\pi v^{\mathsf T} Y u_1$: the terms with $X$, $u_2$ and $b$ are purely imaginary. Completing the square with $Y$ symmetric gives $-\pi q_Y(v + u_1) + \pi q_Y(u_1)$. The inequality is the triangle inequality. $\square$

**Lemma 4.5.4 (Gaussian lattice sums).** There is $C_3 > 0$ with the following property. Let $Y$ be a real positive definite $g \times g$ matrix and $\rho > 0$ with $q_{Y^{-1}}(l) \ge \rho^2$ for all $l \in \mathbb{Z}^g \setminus \{0\}$. Then for every $u \in \mathbb{R}^g$ the family $\exp(-\frac{\pi}{2} q_Y(k+u))$, $k \in \mathbb{Z}^g$, is summable and
$$\sum_{k \in \mathbb{Z}^g} e^{-\frac{\pi}{2} q_Y(k+u)} \le (C_3 g)^{g/2} (\det Y)^{-1/2} \Bigl(1 + \frac1\rho\Bigr)^g.$$

*Proof.* Write $\frac12 Y = B^{\mathsf T} B$ and let $\Lambda = B\mathbb{Z}^g$. Then $\frac{\pi}{2} q_Y(k+u) = \pi |B(k+u)|^2$. The Poisson summation formula for the Gaussian $e^{-\pi|x|^2}$, which is its own Fourier transform, gives
$$\sum_{k} e^{-\pi |B(k+u)|^2} \le \frac{1}{|\det B|} \sum_{\mu \in \Lambda^\vee} e^{-\pi |\mu|^2}, \qquad \frac{1}{|\det B|} = 2^{g/2} (\det Y)^{-1/2}.$$
A nonzero $\mu \in \Lambda^\vee$ is $B^{-\mathsf T} l$ with $l \in \mathbb{Z}^g \setminus \{0\}$, so $|\mu|^2 = l^{\mathsf T}(B^{\mathsf T}B)^{-1} l = 2 q_{Y^{-1}}(l) \ge \rho^2$. So the nonzero vectors of $\Lambda^\vee$ have length at least $\rho$. Split $\Lambda^\vee$ into shells $m \le |\mu| < m + 1$. Balls of radius $\rho/2$ around the points of a shell are disjoint, so a packing count bounds the number of points by $(1 + 2(m+1)/\rho)^g \le 3^g (m+1)^g (1 + 1/\rho)^g$. The bound $(m+1)^g e^{-\pi m^2} \le g^{g/2} e^{\sqrt g} e^{g/(2\pi)} e^{-m}$ and the sum over $m$ give
$$\sum_{\mu \in \Lambda^\vee} e^{-\pi|\mu|^2} \le 2 \cdot 3^g g^{g/2} e^{\sqrt g + g/(2\pi)} \Bigl(1 + \frac1\rho\Bigr)^g.$$
Finally $2^{g/2} \cdot 2 \cdot 3^g g^{g/2} e^{\sqrt g + g/(2\pi)} \le (72 e^4 g)^{g/2}$, so $C_3 = 72e^4$ works. $\square$

**Lemma 4.5.5 (The first coordinate).** Let $Y$ be positive definite with $(Y^{-1})_{11} = \rho^2 > 0$. For every $v \in \mathbb{R}^g$, $q_Y(v) \ge v_1^2/\rho^2$. Hence, for $a, u_1 \in \mathbb{R}^g$ and $\delta = \operatorname{dist}(u_{1,1} + a_1, \mathbb{Z})$,
$$\sum_{k} e^{-\pi q_Y(k+a+u_1)} \le e^{-\frac{\pi}{2\rho^2}\delta^2} \sum_k e^{-\frac{\pi}{2} q_Y(k + a + u_1)}.$$

*Proof.* By the Cauchy-Schwarz inequality for the inner product given by $Y$, $v_1^2 = (e_1^{\mathsf T} Y^{-1} \cdot Y v)^2 \le q_{Y^{-1}}(e_1)\, q_Y(v) = \rho^2 q_Y(v)$. Write $e^{-\pi q} = e^{-\frac\pi2 q} e^{-\frac\pi2 q}$ and bound the first factor with $q_Y(k+a+u_1) \ge (k_1 + a_1 + u_{1,1})^2/\rho^2 \ge \delta^2/\rho^2$. $\square$

### The bounds

**Theorem 4.5.6 (Theta bound).** There is $C > 0$ with the following property. Let $g \ge 1$, let $X$ be a real symmetric $g \times g$ matrix, let $Y$ be a real positive definite $g \times g$ matrix that is reduced with first minimum $\rho$, and let $a, b \in (\frac12\mathbb{Z})^g$. Then
$$\int_{[0,1]^g} \int_{[0,1]^g} \|\theta\|(u_1,u_2)^2 \, du_2\, du_1 = (2^g \det Y)^{-1/2},$$
and for all $u_1, u_2 \in \mathbb{R}^g$, with $\delta = \operatorname{dist}(u_{1,1} + a_1, \mathbb{Z})$,
$$\|\theta\|(u_1,u_2) \le (2^g \det Y)^{-1/4} \exp\Bigl(-\frac{\pi}{2\rho^2}\delta^2 + g\log\Bigl(1 + \frac1\rho\Bigr) + C g \log(2g)\Bigr).$$

Lean: `GroundTheory.Heights₂.Heights.ThetaBound.full`

*Proof.* The mean. Fix $u_1$. As a function of $u_2$, $\theta[a,b](\Omega, \Omega u_1 + u_2)$ is $e^{2\pi i a^{\mathsf T}u_2}$ times an absolutely convergent Fourier series $\sum_k c_k e^{2\pi i k^{\mathsf T} u_2}$, and by the first lemma $|c_k|^2 e^{-2\pi q_Y(u_1)} = e^{-2\pi q_Y(k+a+u_1)}$. By Parseval's formula on the cube (the characters $e^{2\pi i m^{\mathsf T} u}$ have integral $1$ for $m = 0$ and $0$ otherwise),
$$\int_{[0,1]^g} \|\theta\|(u_1,u_2)^2\, du_2 = \sum_{k} e^{-2\pi q_Y(k+a+u_1)}.$$
Integrate over $u_1 \in [0,1]^g$. The translates $k + a + [0,1]^g$ tile $\mathbb{R}^g$, so the result is $\int_{\mathbb{R}^g} e^{-2\pi q_Y(x)}\,dx = \det(2Y)^{-1/2} = (2^g\det Y)^{-1/2}$.

The pointwise bound. Let $C_3$ be the constant of the Gaussian lemma. By the first and third lemmas and then the Gaussian lemma with $u = a + u_1$, which applies by condition 3 of a reduced $Y$,
$$\|\theta\|(u_1,u_2) \le e^{-\frac{\pi}{2\rho^2}\delta^2} (C_3 g)^{g/2} (\det Y)^{-1/2} \Bigl(1 + \frac1\rho\Bigr)^g.$$
It remains to show, with $d = \det Y$, that $(C_3 g)^{g/2} d^{-1/2} \le (2^g d)^{-1/4} (2g)^{Cg}$ for a constant $C$, and to write $(1 + 1/\rho)^g = \exp(g\log(1+1/\rho))$. The inequality is $(C_3 g)^{g/2} 2^{g/4} d^{-1/4} \le (2g)^{Cg}$. By conditions 1 and 4, $d^{-1} \le \rho^2(2g)^{g-1} \le (2g)^g$, so the left side is at most $C_3^{g/2} (2g)^{g/2} (2g)^{g/4} \le C_3^{g/2} (2g)^g$. Take $C = 1 + \log\max(C_3,1)/(2\log 2)$. Since $2g \ge 2$, we have $(2g)^{Cg} \ge (2g)^g \cdot 2^{g\log\max(C_3,1)/(2\log 2)} \ge (2g)^g C_3^{g/2}$. $\square$

**Remark 4.5.7.** The mean is the square of the $L^2$ norm of the theta section for the measure of total mass $1$ on the torus. In the pointwise bound, only the term $Cg\log(2g)$ is independent of $\rho$ and $\delta$. The term $g\log(1+1/\rho)$ is large only when the first minimum is small, and the factor in $\delta$ is small only when $\rho$ is small. These two effects are compared in the chapter on sup norms of theta sections.

**Remark 4.5.8 (Formalization).** The proof of the theorem does not use that $X$ is symmetric or that $a$ and $b$ are half-integral ([PThetaTop.lean](lean:GroundTheory/HeightsAndTheta/Heights/HeightKernels/PThetaTop.lean#L16)): the mean formula and the three lemmas hold for every real $X$ and all real $a, b$. So the theorem holds without these hypotheses. The Poisson step is stated as an inequality, not as the equality of the Poisson formula. The constant of the Gaussian lemma is $72e^4$, and the constant of the theorem is $C = 1 + \log\max(72e^4, 1)/(2\log 2)$.
