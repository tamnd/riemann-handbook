---
title: Volumes of unitary groups
decls:
  - ReciprocityTheory.ChartRestriction.DS.qr_lintegral
  - ReciprocityTheory.ChartRestriction.DS.volU_density
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Volumes of unitary groups

The formal degree of a discrete series is a number only after a Haar measure is fixed. The chapter fixes Haar measures on $U(p,q)$ by their density at the identity in exponential coordinates. The first input is the same question for the compact group $U(N)$: the Haar probability measure of $U(N)$, read in exponential coordinates near $1$, has density $1/v(N)$ with respect to Lebesgue measure, where $v(N)$ is the classical volume of $U(N)$. This section proves that statement. It is used in the next section to compute the density of the polar Haar measure of $U(p,q)$ near the identity, and through that in the step [EveryCharacter from the literature](/step/every-character-of-literature/).

Background: [Haar measure](/learn/analysis/#haar-measure), [measures and integrals](/learn/analysis/#measures-and-integrals), [unitary groups](/learn/groups/#unitary-groups), [[Haar measure|VY0HXD3GC4]].

### Coordinates

Let $N \geq 0$. We identify $M_N(\mathbb{C})$ with $\mathbb{C}^{N^2} = \mathbb{R}^{2N^2}$ and give it Lebesgue measure $dZ$. Let $U(N)$ be the group of unitary $N \times N$ matrices.

**Definition 3.1.1 (Triangular coordinates).** Let $T_N = \mathbb{R}^N \times \mathbb{C}^{\{(a,b) : a < b\}}$. For $t = (d, u) \in T_N$ let $R(t)$ be the upper triangular matrix with diagonal $d_1, \dots, d_N$ and entry $u_{ab}$ at $(a,b)$ for $a < b$. Let $T_N^+ \subseteq T_N$ be the set where every $d_j > 0$. The *QR map* is $q(k, t) = k\,R(t)$, from $U(N) \times T_N$ to $M_N(\mathbb{C})$. The *QR weight* is
$$w(t) = \prod_{j=0}^{N-1} d_j^{\,2(N-j)-1},$$
with the diagonal entries indexed from $0$.

Every invertible matrix $Z$ is $k R(t)$ for exactly one pair $(k,t) \in U(N) \times T_N^+$. This is the Gram-Schmidt process applied to the columns of $Z$. The weight $w$ is the Jacobian of $q$ in these coordinates: the $j$-th diagonal entry $d_j$ is the length of a vector in a complex space of dimension $N - j$, and a sphere of radius $d$ in $\mathbb{R}^{2(N-j)}$ has area proportional to $d^{2(N-j)-1}$.

**Definition 3.1.2 (Exponential coordinates on $U(N)$).** Let $E_N = \mathbb{R}^N \times \mathbb{C}^{\{(a,b) : b < a\}}$. For $x = (s, w) \in E_N$ let $S(x)$ be the skew-Hermitian matrix with diagonal $i s_1, \dots, i s_N$, entry $w_{ab}$ at $(a,b)$ for $b < a$, and entry $-\overline{w_{ab}}$ at $(b,a)$. The map $S$ is a real linear isomorphism from $E_N$ onto the Lie algebra $\mathfrak{u}(N)$, and $x \mapsto \exp(S(x))$ is a chart of $U(N)$ near $1$. We give $E_N$ its Lebesgue measure.

**Definition 3.1.3 (Volume of $U(N)$).** Put
$$v(N) = \prod_{i=0}^{N-1} \frac{2\pi^{i+1}}{i!}.$$

For example, $v(1) = 2\pi$, which is the length of the circle $U(1)$ in the coordinate $s \mapsto e^{is}$. The number $v(N)$ is the volume of $U(N)$ for the Riemannian metric that makes $S$ an isometry at $1$. It is the product of the volumes $2\pi^{i+1}/i!$ of the unit spheres $S^{2i+1} \subseteq \mathbb{C}^{i+1}$, by the fibrations $U(i) \to U(i+1) \to S^{2i+1}$.

### The QR integration formula

**Theorem 3.1.4 (Integration in QR coordinates).** Let $\mu$ be a Haar measure on $U(N)$ with $\mu(U(N)) = 1$. There is a constant $C > 0$ such that for every measurable function $f : M_N(\mathbb{C}) \to [0, \infty]$,
$$\int_{M_N(\mathbb{C})} f(Z)\,dZ = C \int_{U(N)} \int_{T_N^+} f\bigl(k R(t)\bigr)\, w(t)\, dt\, d\mu(k).$$

Lean: `ReciprocityTheory.ChartRestriction.DS.qr_lintegral`.

*Proof.* First, $U(N)$ is compact. If it were not, the left invariant measure $\mu$ would give infinite mass to the whole group, which contradicts $\mu(U(N)) = 1$. The set of singular matrices is a proper algebraic subset of $M_N(\mathbb{C})$, so it has Lebesgue measure zero, and we may integrate over $GL_N(\mathbb{C})$ only. On $GL_N(\mathbb{C})$ the measure $|\det Z|^{-2N}\,dZ$ is a Haar measure, both left and right invariant. The QR map identifies $GL_N(\mathbb{C})$ with $U(N) \times B^+$, where $B^+$ is the group of upper triangular matrices with positive diagonal. On $B^+$ the measure $\prod_j d_j^{-2j+1}\,dt$ (indices from $0$) is a Haar measure. The image of $\mu \times (\text{Haar on } B^+)$ under $q$ is invariant under $GL_N(\mathbb{C})$, so it is a multiple of $|\det Z|^{-2N}\,dZ$ by uniqueness of Haar measure. Multiply both sides by $|\det Z|^{2N} = \prod_j d_j^{2N}$. The weight becomes $\prod_j d_j^{2N - 2j - 1} = w(t)$, and we get the formula with some constant $C > 0$. $\square$

The constant can be computed with a Gaussian. Put $f(Z) = e^{-\|Z\|^2}$, where $\|Z\|^2 = \sum_{a,b} |Z_{ab}|^2$. The left side is $\pi^{N^2}$. Since $\|kR(t)\|^2 = \|R(t)\|^2$ for unitary $k$, the inner integral does not depend on $k$. It is a product: each of the $N(N-1)/2$ entries above the diagonal gives a factor $\pi$, and the diagonal entry $d_j$ gives
$$\int_0^\infty e^{-d^2} d^{\,2(N-j)-1}\, dd = \frac{(N-j-1)!}{2}.$$
So the inner integral is $\pi^{N(N-1)/2} \prod_{i<N} i! / 2^N$, and
$$C = \frac{2^N \pi^{N^2 - N(N-1)/2}}{\prod_{i<N} i!} = \prod_{i=0}^{N-1} \frac{2\pi^{i+1}}{i!} = v(N).$$

### Density at the identity

**Theorem 3.1.5 (Density of the Haar probability measure of $U(N)$).** Let $\mu$ be a Haar measure on $U(N)$ with $\mu(U(N)) = 1$, and let $\eta > 0$. There is $\delta > 0$ with the following property. For every measurable set $B \subseteq E_N$ with $\|x\| < \delta$ for all $x \in B$, the set $\exp(S(B)) = \{ k \in U(N) : k = \exp(S(x)) \text{ for some } x \in B \}$ satisfies
$$\frac{1 - \eta}{v(N)} \operatorname{vol}(B) \leq \mu\bigl(\exp(S(B))\bigr) \leq \frac{1 + \eta}{v(N)} \operatorname{vol}(B).$$

Lean: `ReciprocityTheory.ChartRestriction.DS.volU_density`.

*Proof.* By [Theorem 3.1.4](/entry/qr-lintegral/), the QR formula holds with a constant $C$, and the Gaussian computation above gives $C = v(N)$. Consider the chart
$$\Psi(x, t) = \exp(S(x))\,\bigl(1 + R(t)\bigr), \qquad (x, t) \in E_N \times T_N,$$
near $(0, 0)$. Its differential at $(0,0)$ is $(x, t) \mapsto S(x) + R(t)$. This map is a real linear isomorphism from $E_N \times T_N$ onto $M_N(\mathbb{C})$ that preserves Lebesgue measure: the diagonal of $S(x) + R(t)$ is $d + is$, the part below the diagonal is $w$, and the part above is $u - \overline{w}^{\mathsf T}$, a shear. So for small $\delta$ and sets $B$, $E$ of points of norm less than $\delta$, the Lebesgue measure of $\Psi(B \times E)$ lies between $(1 \pm \varepsilon)\operatorname{vol}(B)\operatorname{vol}(E)$. Take for $E$ a small ball around $0$, so that $1 + R(t)$ ranges over a ball around $1$ in $T_N^+$, where $w$ is close to $w(1) = 1$. Apply the QR formula to the indicator function of $\Psi(B \times E)$. By uniqueness of the QR decomposition, this indicator at $kR(t')$ is the product of the indicators of $k \in \exp(S(B))$ and of $t' \in 1 + E$. The formula gives
$$\operatorname{vol}\bigl(\Psi(B \times E)\bigr) = v(N)\,\mu\bigl(\exp(S(B))\bigr) \int_{1 + E} w(t')\,dt',$$
and the last integral lies between $(1 \pm \varepsilon)\operatorname{vol}(E)$. Divide by $v(N)\operatorname{vol}(E)$. The chart $x \mapsto \exp(S(x))$ is injective on a small ball, so $\exp(S(B))$ is measurable. Choose $\varepsilon$ with $(1 + \varepsilon)/(1 - \varepsilon) \leq 1 + \eta$ and $(1 - \varepsilon)/(1 + \varepsilon) \geq 1 - \eta$. $\square$

**Remark 3.1.6 (Formalization).** The QR theorem does not assume that $U(N)$ is compact; it derives compactness from the existence of a Haar probability measure, by contradiction ([QRHaar.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/FormalDegree/HaarVolumes/QRHaar.lean#L20)). The group $U(N)$ is not defined separately: it is the group $U(p,q)$ of the next section for the sign vector with all signs $+$. The value $C = v(N)$ is a separate lemma, proved by the Gaussian computation above ([LintegralGaussTri.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/FormalDegree/HaarVolumes/LintegralGaussTri.lean#L81)). The number $v(N)$ also has two other definitions with the same name in other parts of the development; we have not compared them.
