---
title: Cusp geometry and regularization of cochains
decls:
  - UpperTheory.V.Lit.Geo.stepEx
  - UpperTheory.V.Lit.Geo.g2
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cusp geometry and regularization of cochains

This section proves two results on the locally symmetric spaces of $\mathrm{GL}_a$ over a totally complex field. The first builds a function that measures the distance to the cusp and moves by a fixed amount along a vector field. The second uses that function to show that a closed relative Lie algebra cochain of rapid decay is, up to a relatively exact cochain, equal to one of compact support. This is a regularization theorem in the sense of Borel's paper on regularization in Lie algebra cohomology. It feeds the comparison of cuspidal and compactly supported classes in [the onto theorem for relations](/entry/rel-onto/), and the step function is one input of [the published hypotheses obtained from patching](/entry/published-hypotheses-from-patching-alt/). The background is in [adelic points and compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups), [quotients of finite volume](/learn/groups/#quotients-of-finite-volume) and [Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms).

### Setting

Let $E$ be a totally complex number field and $a \ge 1$. Write $E_\infty = E \otimes_{\mathbb{Q}} \mathbb{R}$, a product of copies of $\mathbb{C}$, and $\mathbb{A}_{E,f}$ for the finite adeles. Put $G = \mathrm{GL}_a(\mathbb{A}_E) = \mathrm{GL}_a(E_\infty) \times \mathrm{GL}_a(\mathbb{A}_{E,f})$, with $\mathrm{GL}_a(E)$ embedded diagonally. Let $K_\infty$ be the unitary group of $E_\infty^a$, and let $\mathfrak{p}$ be the real vector space of Hermitian matrices in $M_a(E_\infty)$. Let $U \subset \mathrm{GL}_a(\mathbb{A}_{E,f})$ be a compact subgroup.

Each $g \in G$ is the product of a central element of $\mathrm{GL}_a(E_\infty)$, coming from the split centre, and an element $\mathrm{rt}(g)$ of the subgroup of adelic norm $1$. Write $\lambda(g)$ for the logarithm of the central factor. It is a homomorphism to $\mathbb{R}$. The *quasi-height* of $g$ is
$$\mathrm{qht}(g) = \inf_{\gamma \in \mathrm{GL}_a(E)} \mathrm{ht}(\gamma\, \mathrm{rt}(g)),$$
where $\mathrm{ht}$ is the height of the [previous sections](/entry/s-pu/). It satisfies $\mathrm{qht} \ge 1$, it is left invariant under $\mathrm{GL}_a(E)$, and it is large exactly near the cusp.

Let $\Xi$ be an irreducible algebraic representation of $\mathrm{GL}_a(E_\infty)$ on $\mathbb{C}^d$. Let $\mathrm{Sm}$ be the smooth functions on $G$, with $\mathfrak{gl}_a(E_\infty)$ acting by right derivatives. A *cochain of degree $q$* is an alternating $\mathbb{R}$-multilinear map
$$\omega \colon \mathfrak{p}^q \to \mathrm{Sm} \otimes_{\mathbb{C}} \mathbb{C}^d.$$
The differential $d$ is the Chevalley-Eilenberg differential for the action of $\mathfrak{gl}_a(E_\infty)$ on $\mathrm{Sm} \otimes \mathbb{C}^d$ through right derivatives on the first factor and $d\Xi$ on the second.

**Definition 7.6.1 (Level, decay and support).** Let $\omega$ be a cochain of degree $q$.

1. $\omega$ has *level $U$* if it is equivariant under the elements of $K_\infty$ of determinant $1$, vanishes as soon as one argument is the identity matrix, and takes values in the span of $\phi \otimes v$ where each $\phi$ is left $\mathrm{GL}_a(E)$-invariant, right $U$-invariant, and has the central character forced by $\Xi$.
2. $\omega$ is *rapidly decreasing* if for all $X \in \mathfrak{p}^q$ and $N \ge 0$ the function $\|\omega(X)(g)\|\, \mathrm{qht}(g)^N$ is bounded on the elements of norm $1$. It is *rapidly decreasing with derivatives* if every iterated Lie derivative of $\omega$ is rapidly decreasing.
3. $\omega$ has *compact support* if there is $R$ with $\omega(X)(g) = 0$ whenever $\mathrm{qht}(g) > R$.
4. $\omega$ is *relatively exact* if $\omega = 0$ when $q = 0$, and $\omega = d\eta$ for a cochain $\eta$ of level $U$ when $q \ge 1$.

The level condition makes $\omega$ a relative $(\mathfrak{g}, K)$ cochain with values in the automorphic functions of level $U$. So the cohomology of these cochains computes the cohomology of the locally symmetric space of level $U$ with coefficients in the local system of $\Xi$.

### Step functions

**Definition 7.6.2 (Step function).** Let $U$ be compact. A *step function* for $U$ consists of a function $f \colon G \to \mathbb{R}$, a function $Y$ from $G$ to $\mathfrak{p}$, and constants $C$, $c$, $f_0$ with the following properties.

1. $c > 0$.
2. $f$ is smooth and all its Lie derivatives of order at least $1$ are bounded. The same holds for each entry of $Y$.
3. $f$ and $Y$ are left invariant under $\mathrm{GL}_a(E)$ and the split centre, and right invariant under $U$. The function $f$ is right invariant under $K_\infty$, and $Y(gk) = k^{-1} Y(g) k$ for $k \in K_\infty$.
4. $0 \le f(g) \le C (1 + \log \mathrm{qht}(g))$ and $\log \mathrm{qht}(g) \le C(1 + f(g))$.
5. (Roots) For $|t| \le 1$ there is $h \in \mathrm{GL}_a(E_\infty)$ with $h h^* = 1 + tY(g)$, $\|h\| \le C$ and $\|h^{-1}\| \le C$.
6. (Up) If $f(g) \ge f_0$ and $h h^* = 1 + Y(g)$, then $f(gh) \ge f(g) + c$.
7. (Down) If $f(g) \ge f_0$ and $h h^* = 1 - Y(g)$, then $f(gh) \le f(g) - c$.
8. (Near) If $|t| \le 1$ and $h h^* = 1 + tY(g)$, then $|f(gh) - f(g)| \le C$.

By (4), $f$ is comparable to $\log \mathrm{qht}$, so $f \ge f_0$ is a neighbourhood of the cusp. By (6) and (7), moving along $Y$ raises $f$ by at least $c$ there, and moving against it lowers $f$ by at least $c$.

**Theorem 7.6.3 (Existence of step functions).** Let $E$ be totally complex, $a \ge 1$, and $U \subset \mathrm{GL}_a(\mathbb{A}_{E,f})$ compact. Then a step function for $U$ exists.

Lean: `UpperTheory.V.Lit.Geo.stepEx`.

*Proof.* Choose an open compact subgroup $L \subset \mathbb{A}_{E,f}^a$ that is stable under right multiplication by $U$. One exists because $U$ is compact. For $g \in G$, let $\Lambda_g$ be the set of $v \in E^a$ with $v g_f \in L$, and map it to $E_\infty^a$ by $v \mapsto v\, \mathrm{rt}(g)_\infty$. Put
$$\Theta(g) = \sum_{v \in \Lambda_g} \exp\bigl(-\pi\, Q(v\, \mathrm{rt}(g)_\infty)\bigr), \qquad f = \log \Theta,$$
where $Q$ is the sum over the archimedean places of the squared Hermitian norm. Since the term $v = 0$ is $1$, $\Theta \ge 1$ and $f \ge 0$. The sum depends on $g$ only through the coset $\mathrm{GL}_a(E) g U K_\infty$ and not on the centre, which gives the invariances in (3). Counting lattice points in balls gives smoothness and bounded derivatives, and gives the two inequalities of (4) between $f$ and $\log \mathrm{qht}$.

Let $\mathrm{mom}(g)$ be the Hermitian matrix of second moments of the vectors $v\, \mathrm{rt}(g)_\infty$ under the weights $\exp(-\pi Q)/\Theta$. Let $\mathrm{dev}(g) = \mathrm{mom}(g) - \ell(\mathrm{mom}(g)) \cdot 1$ be its trace-free part, where $\ell$ is the normalized trace. Write $\langle X, Y \rangle$ for the real trace form. Then $\langle \mathrm{mom}, \mathrm{dev} \rangle = \langle \mathrm{dev}, \mathrm{dev} \rangle$, $\ell(\mathrm{dev}) = 0$, and there is a constant $B$ with $\|\mathrm{mom}\| \le B$, $\|\mathrm{dev}\| \le B$ and $\langle \mathrm{dev}, \mathrm{dev} \rangle \le B$. Two estimates on Gaussian sums do the work.

1. (Taylor) There are $C_2$ and $\varepsilon_2 > 0$ such that, for trace-free Hermitian $X$ with $\|X\| \le \varepsilon_2$ and $hh^* = 1 + X$, $|f(gh) - f(g) + \pi \langle \mathrm{mom}(g), X \rangle| \le C_2 \|X\|^2$. Indeed $Q(vgh) = Q(vg) + (vg) X (vg)^*$, and the first-order term of $\log \Theta$ is the weighted mean of $-\pi (vg)X(vg)^*$.
2. (Gradient) There are $c_0 > 0$ and $f_0$ such that $f(g) \ge f_0$ implies $\langle \mathrm{dev}(g), \mathrm{dev}(g) \rangle \ge c_0$. Near the cusp the lattice $\Lambda_g$ has short vectors in some directions only, so the moment matrix is far from scalar.

Let $\varepsilon_1$, $C_1$ be such that each Hermitian $X$ with $\|X\| \le \varepsilon_1$ is $hh^*-1$ with $\|h\|, \|h^{-1}\| \le C_1$. Choose $\delta > 0$ with $\delta B \le \varepsilon_1$, $\delta B \le \varepsilon_2$ and $C_2 (\delta B)^2 \le \delta c_0$. Put $Y = -\delta\, \mathrm{dev}$ and $c = \delta c_0$. For $|t| \le 1$ and $hh^* = 1 + tY(g)$, the Taylor estimate with $X = tY(g)$ gives
$$\bigl| f(gh) - f(g) - \pi t \delta \langle \mathrm{dev}(g), \mathrm{dev}(g) \rangle \bigr| \le \delta c_0.$$
For $t = 1$ and $f(g) \ge f_0$ this gives $f(gh) \ge f(g) + (\pi - 1)\delta c_0 \ge f(g) + c$, since $\pi - 2 \ge 0$. The case $t = -1$ is the same with the signs reversed. For general $t$ it gives $|f(gh) - f(g)| \le \pi \delta B + \delta c_0$. The choice of $\varepsilon_1$ gives (5). Take $C$ to be the largest of $C_1$, $\pi\delta B + \delta c_0$ and the constants of (4). $\square$

### Regularization

**Theorem 7.6.4 (Regularization).** Let $E$ be totally complex, $a \ge 1$, and $U$ open and compact. Let $\Xi$ be an irreducible algebraic representation, $q \ge 0$, and $\omega$ a cochain of degree $q$ and level $U$ with $d\omega = 0$ that is rapidly decreasing with derivatives. Then there is a cochain $\alpha$ of degree $q$ and level $U$ with $d\alpha = 0$, compact support, and $\omega - \alpha$ relatively exact.

Lean: `UpperTheory.V.Lit.Geo.g2` (also `UpperTheory.V.Lit.Geo.Cs.galois_twist_preserves_siegel_bound`).

*Proof.* Let $P$ be the open cone of positive definite Hermitian matrices in $M_a(E_\infty)$, and $S = \mathrm{GL}_a(\mathbb{A}_{E,f})/U$. The group $\mathrm{GL}_a(E)$ acts on $S \times P$, by $h \cdot p = h p h^*$ on $P$. Level $U$ cochains correspond to $\mathrm{GL}_a(E)$-invariant families $w$ of $\mathbb{C}^d$-valued differential forms on $P$ indexed by $S$, and the correspondence is compatible with $d$. Let $w$ correspond to $\omega$, so $dw = 0$. Let $(f, Y, C, c, f_0)$ be a step function and let $\Phi$ on $S \times P$ be $f$ viewed through the correspondence: $\Phi(xU, g g^*) = f(g x)$. The field $Y$ gives an invariant vector field $W$ on $S \times P$, and $\varphi$ denotes its time-one flow.

Put $u_0 = w$ and $u_{j+1} = \varphi^* u_j$. Cartan's formula gives a homotopy $H$ with $\varphi^* v - v = dHv + H dv$. Since $d$ commutes with $\varphi^*$, each $u_j$ is closed, and so $u_{j+1} - u_j = d(H u_j)$.

Decay. For an order $k$ and constants $A, B, M \ge 0$, say that a form satisfies the decay bound $(k, A, B, M)$ if, where $f \ge f_0$, its derivatives up to order $k$ are at most $M \exp(B|\lambda| - A f)$. Rapid decrease of $\omega$, with $f \le C(1 + \log \mathrm{qht})$, gives $B \ge 0$ such that $w$ satisfies the bound $(k, A, B, M)$ for every $A \ge 0$ and some $M$. One step of the flow moves the point up by $c$ in $f$. So there is $D \ge 0$ such that, if $v$ satisfies $(k, A, B, M)$, then $\varphi^* v$ satisfies $(k, A, B, D e^{-Ac} M)$. Take $A = 2D/c$. Then $D e^{-Ac} = D e^{-2D} \le 1/2$, and by induction $u_j$ satisfies $(k, A, B, 2^{-j} M)$. A local estimate turns these bounds into pointwise bounds of order $2^{-j}$ at every point where $\Phi > f_0 + C$. Hence $u_j \to 0$ there.

Case $q = 0$. Then $Hv = 0$ for a function $v$, and $dw = 0$, so $\varphi^* w = w$ and $u_j = w$ for all $j$. So $w = 0$ wherever $\Phi > f_0 + C$. A form that vanishes where $\Phi$ is large corresponds to a cochain of compact support, so $\omega$ has compact support. Take $\alpha = \omega$. Then $\omega - \alpha = 0$ is relatively exact.

Case $q \ge 1$. The forms $y_j = H u_j$ are invariant and satisfy $dy_j = u_{j+1} - u_j$. The homotopy keeps the decay bound up to a constant $D'$, on the region $f \ge f_0 + C$, so the bounds on $y_j$ and their derivatives are summable in $j$ near each point where $\Phi > f_0 + C$. Since $u_j \to 0$ there, the telescoping series gives an invariant $z$ with $dz = w$ where $\Phi > f_0 + C + 1$. A cut-off and retraction argument on the cone $P$, which uses its convexity and an invariant gauge, replaces $z$ by an invariant form $z'$ that corresponds to a cochain and still satisfies $dz' = w$ where $\Phi > f_0 + C + 1$. Let $\eta$ be the cochain of level $U$ that corresponds to $z'$, and put $\alpha = \omega - d\eta$. Then $\alpha$ has level $U$ and $d\alpha = d\omega = 0$. It corresponds to $w - dz'$, which vanishes where $\Phi > f_0 + C + 1$, so $\alpha$ has compact support. Finally $\omega - \alpha = d\eta$ is relatively exact. $\square$

**Remark 7.6.5.** The theorem says that the inclusion of compactly supported cochains into rapidly decreasing ones induces a surjection on the classes considered here. Borel proved results of this kind for general reductive groups with a different method. The proof above uses only the function $f$ and the flow of $Y$, so it needs no reduction theory beyond the estimates on $\Theta$.

**Remark 7.6.6 (Formalization).** The theorem `UpperTheory.V.Lit.Geo.g2` in [ImportsVariant.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/LieGeometryGrowth/ImportsVariant.lean#L17) applies `Cs.galois_twist_preserves_siegel_bound` ([G2Assumption.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/LieGeometryGrowth/G2Assumption.lean#L71)) to eleven lemmas `Cs.lamEx`, …, `Cs.supp`. That name has nothing to do with Galois twists; the lemma is the proof above, and the eleven inputs (decay under pullback, decay of the homotopy, local bounds, summation, retraction, support) are proved in the same folder and not unfolded here. Both `G2` and `StepEx` live in the namespace `Lit`, used elsewhere for published inputs, but here they are proved. In the proof of `stepEx` ([StepEx.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/LieGeometryGrowth/StepEx.lean#L22)), the lattice $L$ comes from `UpperTheory.unitaryGroup_lieAlgebra_eq_skewHermitian` and the gradient bound from `UpperTheory.traceForm_posDef_of_totallyReal`. Both names are misleading: the first proves the existence of a $U$-stable lattice, the second proves the gradient estimate for $E$ totally complex. The other inputs from the folder GeometricSideEstimates have the same problem: `UpperTheory.unitarySimilitudeGroup_isSmooth_cmDatum` proves the existence of the square roots $h$ in (5), and `UpperTheory.hermitian_trace_form_estimate` proves the bounds on $\mathrm{mom}$ and $\mathrm{dev}$. The level condition asks for equivariance only under elements of $K_\infty$ of determinant $1$.
