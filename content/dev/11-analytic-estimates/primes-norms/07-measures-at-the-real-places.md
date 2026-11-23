---
title: Measures at the real places
decls:
  - GlobalTheory.RealPlaceMeasuresProof.realPlaceMeasures
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Measures at the real places

The second half of the chapter computes the ratio of the volumes of two hermitian spaces, one of rank $M$ and one of rank $M - 1$. This section supplies the archimedean part of that computation. It proves three facts about the space $\mathbb{C}^{P+Q}$ with a hermitian form of signature $(P, Q)$. First, the measure $dx = 2^{P+Q}\,dx_{\mathrm{Leb}}$ is the only self-dual [[Haar measure|CE0V9686M8]] for the character $e^{2\pi i\,\mathrm{Tr}\,h(x, y)}$. Second, the sphere $\{q = 1\}$ in $\mathbb{C}^M$ has mass $(2\pi)^M/(M-1)!$ for the measure $dx/dq$. Third, the Haar measure of $U(P, Q)$, with the normalization of the compact dual, is the product of $dx/dq$ on an orbit $\{q = \pm 1\}$ and the Haar measure of the stabilizer, up to the factor $(2\pi)^{-(P+Q)}(P+Q-1)!$. The three facts are used in Section 9, in [the theorem on the volume ratio](/entry/volume-ratio/). For background see [Haar measure](/learn/analysis/#haar-measure) and [the Fourier transform](/learn/analysis/#the-fourier-transform).

### Notation

Let $P, Q \geq 0$ and $V_{P,Q} = \mathbb{C}^{P+Q}$, with coordinates indexed by $P$ indices of sign $\varepsilon_j = 1$ and $Q$ indices of sign $\varepsilon_j = -1$. Put
$$h(x, y) = \sum_j \varepsilon_j x_j\overline{y_j}, \qquad q(x) = h(x, x) \in \mathbb{R}, \qquad b(x, y) = \mathrm{Tr}_{\mathbb{C}/\mathbb{R}}\, h(x, y) = 2\,\mathrm{Re}\, h(x, y).$$
Then $b$ is a nondegenerate symmetric real bilinear form on $V_{P,Q}$. The [[unitary group|0R9R0Y1HDK]] $U(P, Q)$ is the group of complex matrices $g$ with $h(gx, gy) = h(x, y)$. It acts on $V_{P,Q}$ by $g \cdot x = gx$.

**Definition 2.7.1 (Self-dual measure).** Let $V$ be a finite-dimensional real vector space, $\beta$ a real bilinear form on $V$, $e$ a real number and $\mu$ a measure on $V$. For a Schwartz function $\Phi$ put
$$\widehat{\Phi}(y) = \int_V \Phi(x)\, e^{2\pi i e\beta(x, y)}\, d\mu(x).$$
The measure $\mu$ is *self-dual for $e\beta$* if for every Schwartz function $\Phi$ the functions $\Phi$ and $\widehat{\Phi}$ are $\mu$-integrable and $\widehat{\widehat{\Phi}}(x) = \Phi(-x)$ for all $x$.

Let $dx_{\mathrm{Leb}}$ be the Lebesgue measure on $V_{P,Q} = \mathbb{R}^{2(P+Q)}$, and put
$$dx = 2^{P+Q}\, dx_{\mathrm{Leb}}, \qquad c(M) = \frac{(2\pi)^M}{(M-1)!}.$$

**Definition 2.7.2 (Fibre measures of $dx/dq$).** Let $t_0$ be real. A family $(\nu_t)_{t \in \mathbb{R}}$ of measures on $V_{P,Q}$ is a *family of fibre measures of $dx/dq$ near $t_0$* if there are a set $U \supseteq V_{P,Q} \setminus \{0\}$ and an open set $B \ni t_0$ such that:

1. $\nu_t$ is carried by $\{q = t\} \cap U$, for every $t$;
2. $\int_U \varphi\, dx = \int_{\mathbb{R}} \int \varphi\, d\nu_t\, dt$ for every measurable $\varphi \geq 0$;
3. for every continuous $\varphi$ with compact support in $U$, the function $t \mapsto \int\varphi\, d\nu_t$ is defined and continuous on $B$.

Property 2 says that $\nu_t$ is a disintegration of $dx$ along $q$. Property 3 fixes $\nu_t$ for $t \in B$, so for $t_0 \neq 0$ the measure $\nu_{t_0}$ does not depend on the choice of the family.

**Definition 2.7.3 (Compact dual normalization).** A *compact dual normalization* is a choice of a Haar measure $\mu_{P,Q}$ on $U(P, Q)$ for all $P, Q$, such that $\mu_{N,0}$ is a probability measure on the compact group $U(N)$, and $\mu_{P,Q}$ and $\mu_{P+Q,0}$ have the same density at the identity, relative to one Lebesgue measure on the common complexified Lie algebra.

The measure of $U(P, Q)$ is transported from its compact dual $U(P+Q)$ through the Lie algebra $\mathfrak{u}(P, Q) \otimes \mathbb{C} = \mathfrak{gl}_{P+Q}(\mathbb{C}) = \mathfrak{u}(P+Q) \otimes \mathbb{C}$.

**Definition 2.7.4 (Perpendicular frame).** Let $x_0 \in V_{P,Q}$. A *perpendicular frame* of $x_0$ of signature $(P', Q')$ is a pair of a $\mathbb{C}$-linear map $j : V_{P',Q'} \to V_{P,Q}$ and a map $\iota : U(P', Q') \to U(P, Q)$ such that $h(jv, jw) = h(v, w)$, the image of $j$ is $\{y : h(y, x_0) = 0\}$, and $\iota(g')x_0 = x_0$ and $\iota(g')(jv) = j(g'v)$ for all $g'$ and $v$.

### The theorem

**Theorem 2.7.5 (Measures at the real places).** The following three statements hold.

1. *(Self-dual measures.)* Let $e = \pm 1$. A Haar measure $\mu$ on $V_{P,Q}$ is self-dual for $e\,b$ if and only if $\mu = dx$. A Haar measure $\nu$ on $\mathbb{R}$ is self-dual for $e\,ts$ if and only if $\nu$ is the Lebesgue measure.
2. *(Mass of the sphere.)* Let $M \geq 1$, and let $(\nu_t)$ be a family of fibre measures of $dx/dq$ near $1$ on $V_{M,0}$. Then $\nu_1(\{q = 1\}) = c(M)$.
3. *(Quotient measure.)* Let $\beta = \pm 1$ and $x_0 \in V_{P,Q}$ with $q(x_0) = \beta$. Then every $y$ with $q(y) = \beta$ is $g^{-1}x_0$ for some $g \in U(P, Q)$. There is a perpendicular frame of $x_0$, of signature $(P-1, Q)$ if $\beta = 1$ and of signature $(P, Q-1)$ if $\beta = -1$. For every perpendicular frame $(j, \iota)$ of $x_0$ of signature $(P', Q')$, the image of $\iota$ is the stabilizer of $x_0$, and the formula $(\ast)$ below holds for every compact dual normalization $\mu$, every family $(\nu_t)$ of fibre measures of $dx/dq$ near $\beta$, every map $s$ with $s(y)^{-1}x_0 = y$ whenever $q(y) = \beta$, and every measurable $f \geq 0$ on $U(P, Q)$.

$$\int_{U(P,Q)} f\, d\mu_{P,Q} = c(P+Q)^{-1}\int_{\{q = \beta\}} \int_{U(P',Q')} f\bigl(\iota(g')s(y)\bigr)\, d\mu_{P',Q'}(g')\, d\nu_\beta(y). \qquad (\ast)$$

Lean: `GlobalTheory.RealPlaceMeasuresProof.realPlaceMeasures`.

*Proof.* Part 1. Let $T : V_{P,Q} \to \mathbb{R}^{2(P+Q)}$ be the identification of $\mathbb{C}$ with $\mathbb{R}^2$ in each coordinate, and let $S$ be the isometry that multiplies the coordinate $j$ by $e\varepsilon_j$. Put $R = 2S \circ T$. Then
$$e\,b(x, y) = 2e\,\mathrm{Re}\sum_j \varepsilon_j x_j\overline{y_j} = \langle Tx, Ry\rangle.$$
The image of $dx$ under $T$ is $2^{P+Q}$ times Lebesgue measure. The image of $dx$ under $R$ is $2^{P+Q} \cdot 2^{-2(P+Q)} = 2^{-(P+Q)}$ times Lebesgue measure, since $R$ multiplies the volume in real dimension $2(P+Q)$ by $2^{2(P+Q)}$. Substitute $T$ in the inner integral and $R$ in the outer integral of $\widehat{\widehat{\Phi}}$. The double transform becomes the composite of the Euclidean Fourier transform and its inverse, multiplied by the product $2^{P+Q} \cdot 2^{-(P+Q)} = 1$ of the two factors. So Fourier inversion on $\mathbb{R}^{2(P+Q)}$ gives $\widehat{\widehat{\Phi}}(x) = \Phi(-x)$, and $dx$ is self-dual. On $\mathbb{R}$, the same argument with $T = \mathrm{id}$ and $R = \pm\mathrm{id}$ shows that the Lebesgue measure is self-dual. Conversely, every Haar measure is $t\mu_0$ for a self-dual $\mu_0$ and some $t > 0$, and for $t\mu_0$ the double transform is $t^2$ times that for $\mu_0$. Take $\Phi$ a Gaussian, with $\Phi(0) \neq 0$. Then $t\mu_0$ is self-dual only if $t^2 = 1$.

Part 2. On $V_{M,0}$ we have $q(x) = \sum_j |x_j|^2$. The set $\{q \leq r\}$ is a ball of radius $\sqrt{r}$ in $\mathbb{R}^{2M}$, so its measure for $dx$ is $2^M \pi^M r^M/M! = (2\pi)^M r^M/M!$. Let $m(t) = \nu_t(\{q = t\})$. By property 2, for $0 \leq a \leq b$,
$$\int_a^b m(t)\, dt = dx(\{a < q \leq b\}) = \frac{(2\pi)^M(b^M - a^M)}{M!}.$$
The shell $\{1/2 \leq q \leq 2\}$ is compact and does not contain $0$. So by property 3, applied to a continuous function with compact support in $U$ that is $1$ on the shell, the function $m$ is continuous near $1$. Then the fundamental theorem of calculus gives $m(1) = M(2\pi)^M/M! = c(M)$.

Part 3. The transitivity is Witt's theorem: $U(P, Q)$ acts transitively on the vectors of a given nonzero norm. For the existence of a frame, the orthogonal complement $x_0^\perp$ has signature $(P - 1, Q)$ or $(P, Q - 1)$, since $V_{P,Q} = \mathbb{C}x_0 \oplus x_0^\perp$ and $q(x_0) = \beta$. Choose an orthonormal basis of $x_0^\perp$ adapted to the signs. It gives $j$, and $\iota(g')$ is $g'$ on $x_0^\perp$ and the identity on $\mathbb{C}x_0$. For the image of $\iota$, an element $g$ that fixes $x_0$ preserves $x_0^\perp$, and $j^{-1}gj$ is an element $g'$ with $\iota(g') = g$. This shows that the image of $\iota$ is the stabilizer $H$ of $x_0$.

The map $g \mapsto g^{-1}x_0$ identifies $H\backslash U(P, Q)$ with the orbit $\{q = \beta\}$, and $g = \iota(g')s(y)$ with $y = g^{-1}x_0$. The groups $U(P, Q)$ and $H \cong U(P', Q')$ are unimodular, and the measure $\nu_\beta$ is invariant under $U(P, Q)$, because $dx$ and $q$ are. By the uniqueness of invariant measures on $H\backslash U(P, Q)$, the formula $(\ast)$ holds with some constant $\kappa_{P,Q}$ in place of $c(P+Q)^{-1}$. The constant depends only on the densities of $\mu_{P,Q}$, $\mu_{P',Q'}$ and $dx/dq$ near the identity and near $x_0$, and these local densities are the same for $U(P, Q)$ and for its compact dual $U(P+Q)$, by the definition of a compact dual normalization. So $\kappa_{P,Q} = \kappa_{P+Q,0}$. For the compact group take $f = 1$. Then the left side is $1$, and the right side is $\kappa_{N,0}\, c(N) \cdot 1$ by Part 2, with $N = P + Q$. So $\kappa_{P,Q} = c(P+Q)^{-1}$. $\square$

### Comments

The factor $2^{P+Q}$ in $dx$ comes from the trace: the character is $e^{2\pi i\, \mathrm{Tr}\, h(x,y)}$ and not $e^{2\pi i\, \mathrm{Re}\, h(x,y)}$. With this measure the sphere mass $c(M) = (2\pi)^M/(M-1)!$ appears directly, and it is the archimedean factor $((2\pi)^M/(M-1)!)^f$ of [the volume ratio](/entry/volume-ratio/), one factor for each real place of the totally real field. The quotient formula is the step that relates the Haar measure of the unitary group of a space of rank $M$ to that of the stabilizer of a vector, which is the unitary group of the orthogonal complement of rank $M - 1$. Compare [Siegel's mass formula and Tamagawa measures](/learn/hermitian-lattices/#siegels-mass-formula-and-tamagawa-measures).

**Remark 2.7.6 (Formalization).** The theorem is obtained from a second formal version of the three statements in [PerpendicularEmbedding.lean](lean:Development/AbelianVarietyTheory/BlockTheory/GlobalSignature/PerpendicularEmbedding.lean#L79), through the equivalence `GlobalTheory.RealPlaceCompare.typings_agree` ([MeasurePreservingGlue.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/MeasurePreservingGlue.lean#L698)). The second version states only that $dx$ and the Lebesgue measure are self-dual, and the equivalence adds the uniqueness. In that version a family of fibre measures is required on all of $\mathbb{R}$, the section $s$ is measurable, and the convention is $s(y)x_0 = y$ with $f(s(y)\,j(g'))$; the target version uses $s(y)^{-1}x_0 = y$ with $f(\iota(g')s(y))$ and does not ask that $s$ be measurable ([ActionCoordinates.lean](lean:Development/AbelianVarietyTheory/BlockTheory/GlobalSignature/ActionCoordinates.lean#L68)). The quotient formula is stated for every compact dual normalization (`Formalism.BasicNotions.CDHaar`). The equality of densities at the identity in that structure is the field `trick` ([DataCD.lean](lean:Formalism/LocalRingCardinality/DataCD.lean#L57)). The three ingredients are `GlobalTheory.RealPlaceMeasuresProof.selfDualReal`, `GlobalTheory.SphereMassProof.sphereMass` and `GlobalTheory.CompactDualQuot.compactDualQuotient`. The name `typings_agree` is also used for a different result in another namespace.
