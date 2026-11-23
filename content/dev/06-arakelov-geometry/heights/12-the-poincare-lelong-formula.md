---
title: The Poincaré-Lelong formula on arithmetic varieties
decls:
  - PositivityTheory.Tls2.Pl.poincareLelong_of_leaves
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Poincaré-Lelong formula on arithmetic varieties

This section proves the Poincaré-Lelong formula for the complex points of a multiprojective arithmetic variety. For a section $s$ of a hermitian line bundle $\bar A$, the formula computes the integral of $\log\|s\|$ against $dd^c f$ times a product of Chern forms. The answer is the integral of $f$ over the horizontal part of the divisor of $s$, minus the integral of $f$ against the first Chern form of $\bar A$. The proof regularizes $\log\|s\|$, applies Stokes' theorem, and takes the limit with the Lelong number computation in affine charts. The theorem takes seven analytic inputs as hypotheses. It is used in [the step on the published results](/step/every-character-of-literature/), where it gives the recursion of arithmetic intersection numbers in the next sections.

### Arithmetic varieties and hermitian line bundles

Let $K$ be a finite set and, for each $k \in K$, let $\iota_k$ be a finite set of variables. Let $\mathbb{Z}[x]$ be the polynomial ring in the variables $x_{k,i}$, multigraded by $K$. A point of the multiprojective space $\prod_k \mathbb{P}^{\iota_k}$ is a vector $z$ with $z_k \ne 0$ for each block $k$.

**Definition 4.12.1 (Arithmetic variety).** A prime ideal $P \subseteq \mathbb{Z}[x]$ is an arithmetic variety of dimension $d$ if $K$ is nonempty, $P$ is multihomogeneous and relevant (for each $k$ some $x_{k,i}$ is not in $P$), $P \cap \mathbb{Z} = 0$, and $\dim \mathbb{Z}[x]/P = d + |K|$. Its complex points $P(\mathbb{C})$ are the points $z$ of the multiprojective space where all elements of $P$ vanish.

So $P$ is an integral closed subscheme, flat over $\mathbb{Z}$, of absolute dimension $d$, and $P(\mathbb{C})$ has complex dimension $d - 1$.

**Definition 4.12.2 (Hermitian line bundle).** A hermitian line bundle $\bar A$ is a multidegree $a \in \mathbb{Z}^K$ and a positive function $h_A$ on the points with $z_k \ne 0$ for all $k$, such that $h_A(c \cdot z) = \prod_k |c_k|^{a_k} h_A(z)$ for all $c \in (\mathbb{C}^\times)^K$. It is smooth if $h_A$ is smooth. A section of $\bar A$ on $P$ is a multihomogeneous $s \in \mathbb{Z}[x]$ of multidegree $a$ with $s \notin P$, and its norm is $\|s\|(z) = |s(z)|/h_A(z)$.

The function $\|s\|$ is invariant under scaling, so it is a function on $P(\mathbb{C})$. The potential of $\bar L$ is $\log h_L$, and its first Chern form is $c_1(\bar L) = dd^c \log h_L$. A line bundle of degree $0$ is a smooth positive function on the multiprojective space.

**Definition 4.12.3 (Integral over the complex points).** Let $P$ be an arithmetic variety with $P(\mathbb{C})$ of dimension $e$, let $\varphi_1, \dots, \varphi_e$ be potentials and $g$ a function. Choose a linear map $\Psi$ from the Segre space to $\mathbb{C}^{e+1}$ that does not vanish on the Segre image of $P(\mathbb{C})$. Over $y \in \mathbb{C}^e$, the points of $P(\mathbb{C})$ with $\Psi = (1, y)$ form a finite fibre, and near a general fibre point $P(\mathbb{C})$ is a holomorphic sheet $\gamma$ over $\mathbb{C}^e$. Put
$$\int_{P(\mathbb{C})} g\, dd^c\varphi_1 \cdots dd^c\varphi_e = \int_{\mathbb{C}^e} \sum_{w} g(\gamma_w(y))\, \det{}_{\mathrm{MA}}(\varphi \circ \gamma_w)(y)\, dy,$$
where the sum runs over the fibre points $w$ and $\det_{\mathrm{MA}}$ is the mixed Monge-Ampère density.

The divisor of $s$ on $P$ is the set of minimal primes $W$ of $P + (s)$ that are relevant, with multiplicity $m_W$ the length of $\mathbb{Z}[x]/(P + (s))$ at $W$. A component $W$ is horizontal if $W \cap \mathbb{Z} = 0$, and vertical otherwise. Vertical components lie in one fibre over a prime $p$ and have no complex points.

### The theorem

**Theorem 4.12.4 (Poincaré-Lelong formula).** Assume the seven analytic inputs listed below. Let $P$ be an arithmetic variety of dimension $n + 2$. Let $\bar L_1, \dots, \bar L_n$, $\bar A$ and $\bar B$ be smooth hermitian line bundles with $\bar B$ of degree $0$, and let $s$ be a section of $\bar A$ on $P$. Put $f = \log h_B$ and $\omega = c_1(\bar L_1) \cdots c_1(\bar L_n)$. Then
$$\begin{aligned}
\int_{P(\mathbb{C})} \log\|s\|\; dd^c f\; \omega
&= \sum_{W \text{ horizontal}} m_W \int_{W(\mathbb{C})} f\, \omega \\
&\quad - \int_{P(\mathbb{C})} f\, c_1(\bar A)\, \omega.
\end{aligned}$$

Lean: `PositivityTheory.Tls2.Pl.poincareLelong_of_leaves`

The seven inputs are the following. In the affine ones, $J$ is a prime ideal of $\mathbb{C}[x_1, \dots, x_N]$ with $\dim \mathbb{C}[x]/J = d + 1$, and $\ell_u = \sum_j u_j x_j$ is a linear form not in $J$.

1. Integrability: the function $|\log\|s\||$ times the density of $\omega$ in the definition above is integrable over $\mathbb{C}^e$.
2. Segre charts: on the chart of the Segre space where one coordinate is $1$, the integral over $P(\mathbb{C})$ of a function that is supported in that chart is the sum of the affine integrals over the components of the chart.
3. Chart divisors: the components of the divisor of $s$ in a Segre chart, with their local multiplicities, match the horizontal components $W$ with the multiplicities $m_W$.
4. Branches: off a closed subset $Z(I)$ of dimension less than $d$, each zero $q$ of $\ell_u$ on $Z(J)$ lies on exactly one component $W$ of $J + (\ell_u)$, and near $q$ the variety $Z(J)$ is a finite union of holomorphic branches $\gamma_b$ on which $\ell_u$ vanishes to order $\operatorname{ord}_b$ along $W$.
5. Lelong limit at branches: near such a point $q$, for every smooth function $f$ with compact support, the integral of $f$ against $dd^c \frac{1}{2}\log(|\ell_u|^2 + \varepsilon)$ times smooth forms on $Z(J)$ tends to $\sum_b \operatorname{ord}_b$ times the integral of $f$ over $Z(W)$, as $\varepsilon \to 0$.
6. Local order: the local multiplicity of $J + (\ell_u)$ at $W$ is $\sum_b \operatorname{ord}_b$ ([entry](/entry/local-order/)).
7. Mass near small sets: for every $\delta > 0$, the regularized integrals over a small neighbourhood of $Z(I)$ are at most $\delta$ in absolute value, uniformly in $\varepsilon \in (0, 1]$ ([entry](/entry/reg-mass-near-small/)).

*Proof.* Regularization. For $\varepsilon > 0$ put $\rho_\varepsilon = \frac{1}{2}\log(\|s\|^2 + \varepsilon)$. This is a smooth function, invariant under scaling, so it is the potential of a smooth hermitian line bundle of degree $0$. Stokes' theorem on the variety $P(\mathbb{C})$, for the two degree $0$ potentials $\rho_\varepsilon$ and $f$, gives
$$\int_{P(\mathbb{C})} f\, dd^c\rho_\varepsilon\, \omega = \int_{P(\mathbb{C})} \rho_\varepsilon\, dd^c f\, \omega. \tag{1}$$
The integrability of input 1 and of the Monge-Ampère densities enters here and in the next step.

The right side. As $\varepsilon \to 0$, $\rho_\varepsilon$ decreases to $\log\|s\|$, and $|\rho_\varepsilon| \le |\log\|s\|| + C$ for $\varepsilon \le 1$. By input 1 and dominated convergence, the right side of (1) tends to the left side of the theorem.

The left side. Write
$$\rho_\varepsilon = \tfrac{1}{2}\log\bigl(|s|^2 + \varepsilon h_A^2\bigr) - \log h_A.$$
The second term contributes $-\int f\, c_1(\bar A)\, \omega$ for every $\varepsilon$. It remains to show that
$$\int_{P(\mathbb{C})} f\, dd^c\, \tfrac{1}{2}\log\bigl(|s|^2 + \varepsilon h_A^2\bigr)\, \omega \longrightarrow \sum_{W \text{ horizontal}} m_W \int_{W(\mathbb{C})} f\, \omega.$$
Cover the Segre space by the charts where one coordinate is $1$, and split $f$ by a partition of unity subordinate to them. By input 2, each piece becomes an affine integral over the chart components of $P(\mathbb{C})$, and in the chart the function $|s|^2 + \varepsilon h_A^2$ becomes a polynomial section plus a smooth positive term. The limit in the chart is the affine Lelong limit for a polynomial $p$ with a smooth positive weight $k$, for the functions $\frac{1}{2}\log(|p|^2 + \varepsilon k^2)$. Passing to the graph of $p$ makes $p$ a coordinate, so a linear form, and local multiplicities do not change under this surjective change of rings. Stokes' theorem removes the weight $k$, so the case of a linear form $\ell_u$ without weight remains. By input 3 the components and multiplicities of the chart divisors are the $W$ and the $m_W$, so the sum of the chart limits is the right side.

The affine Lelong limit. Let $J$ and $\ell_u$ be as in the inputs, $f$ smooth with compact support, and $\varphi$ smooth potentials near $Z(J)$. We show that
$$\int_{Z(J)} f\, dd^c\, \tfrac{1}{2}\log(|\ell_u|^2 + \varepsilon)\, dd^c\varphi \longrightarrow \sum_W m_W(J + (\ell_u)) \int_{Z(W)} f\, dd^c\varphi.$$
Away from the zeros of $\ell_u$, the regularized form tends to $0$ locally uniformly with all derivatives, because $\log|\ell_u|$ is pluriharmonic there. At a zero $q$ outside the small set $Z(I)$ of input 4, the branches give the local limit $\sum_b \operatorname{ord}_b \int_{Z(W)} f\, dd^c\varphi$ by input 5, and this is $m_W \int_{Z(W)} f\, dd^c\varphi$ by input 6. Near $Z(I)$, input 7 makes the contribution of a cut-off neighbourhood smaller than any $\delta$, uniformly in $\varepsilon$, and the same holds for the limit side, because $Z(I) \cap Z(W)$ has measure zero for the forms on $Z(W)$. A partition of unity joins these three cases.

Conclusion. The two sides of (1) converge to the two sides of the theorem, and limits are unique. $\square$

**Example 4.12.5.** Take $\bar B$ constant, so $f$ is a constant $c$. The left side of the theorem is $0$, and the formula becomes
$$\int_{P(\mathbb{C})} c_1(\bar A)\, \omega = \sum_{W \text{ horizontal}} m_W \int_{W(\mathbb{C})} \omega.$$
For $P = 0$ in $\mathbb{Z}[x_0, x_1]$, so $P(\mathbb{C}) = \mathbb{P}^1$ and $n = 0$, and $s = x_0$ of degree $1$, the divisor is the one point $[0 : 1]$ with multiplicity $1$. The formula says that $\int_{\mathbb{P}^1} c_1(\bar A) = 1$ for every smooth metric of degree $1$. For a general $f$, it says
$$\int_{\mathbb{P}^1} \log\frac{|x_0|}{h_A}\; dd^c f = f([0:1]) - \int_{\mathbb{P}^1} f\, c_1(\bar A).$$

**Remark 4.12.6.** Only horizontal components appear, because the vertical components have no complex points. In the arithmetic intersection theory of the next sections the vertical components come back, with the weight $\log p$. The hypothesis that $\bar B$ has degree $0$ makes $f$ a global function, so that $dd^c f$ is exact and Stokes' theorem applies without boundary terms.

**Remark 4.12.7 (Formalization).** The theorem is assembled in [Development.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/Development.lean#L86). The statement is `ArithmeticPoincareLelongFormula` ([InterSt.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/InterSt.lean#L76)), published under the name `PoincareLelong`. The seven inputs are the hypotheses `PtsAbsIntegrable`, `SegreChartIntegral`, `ChartDivisorCompare`, `DivisorGeneralPointBranches`, `LelongLimitAtBranches`, `LocalOrder` and `RegMassNearSmall`; the theorem does not prove them. Stokes' theorem on the variety is proved in the same file from closed lemmas. The integral over the complex points uses a projection chosen by `Classical.choose`, and it is $0$ when no good projection exists ([IsIntersectionFamily.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/IsIntersectionFamily.lean#L140)); independence of the choice is a separate statement that this proof does not use. The measurability of the integrand is derived from input 1. The same seven inputs also give a second published form of the formula, `poincareLelongInv_of_leaves`, which has extra hypotheses of invariance under complex conjugation that its proof does not use.
