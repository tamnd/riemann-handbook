---
title: The Siegel-Weil formula at the point s0
decls:
  - PositivityTheory.SiegelWeilCoefficients.field
  - PositivityTheory.SiegelWeilCoefficients.lit
  - PositivityTheory.SiegelWeilCoefficients.coefND
  - PositivityTheory.Rg.Sw.Glob.genA_hf
  - PositivityTheory.Rg.Sw.Glob.top7
  - PositivityTheory.Rg.Sw.Glob.top6
  - PositivityTheory.Rg.Sw.Glob.top5
  - PositivityTheory.Rg.Sw.Glob.top3
  - PositivityTheory.Rg.Sw.Glob.top2
  - PositivityTheory.Rg.Sw.Glob.top
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Siegel-Weil formula at the point s0

This section states the Siegel-Weil formula for the pair $(U(n,n), U_V)$ in the range $n < m \le 2n$, where the Eisenstein series does not converge at the point of interest. The formula says that the Eisenstein series continues to $s_0 = \tfrac{m - n}{2}$, is holomorphic there, and has the theta integral as its value. The proof reduces the formula to a list of local and global properties: generation of the group, a dilation property at an archimedean place, the nondegenerate Fourier coefficients, and the absolute convergence theorem of [the section on Gaussian moments](/entry/abs-thm-of/). The formula is cited in [EveryCharacter from the literature](/step/every-character-of-literature/), as part of [the hypotheses at the third place](/step/unitary-group-third-place-hypotheses-def/).

We keep the notation of [the convergent range](/entry/siegel-deg/). Let $V$ be a Hermitian space over $E$ of rank $m$ and Witt index $r_V$. Let $G = U(n, n)$ with Siegel parabolic $P = MN$, and let $K$ be its standard maximal compact subgroup of $G(\mathbb{A})$. For an adelic Hermitian $n \times n$ matrix $b$ let $n(b) = \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}$.

**Definition 4.5.1 (Range).** The pair $(V, n)$ is in the range if $n < m$, $m \le 2n$ and $n + r_V < m$.

**Definition 4.5.2 (Standard data).** Standard data for $(V, n)$ consist of: a standard character $\psi$; a Hecke character $\chi$ of $\mathbb{A}_E^\times$ with restriction $\eta^m$ to $\mathbb{A}^\times$; fixed archimedean data $\theta$; a Haar measure $\mu$ on $\mathrm{Mat}_{m \times n}(\mathbb{A}_E)$ of covolume 1; a representation $\omega$ of $G(\mathbb{A})$ on the Schwartz space that satisfies the formulas of the [Schrödinger model](/learn/theta/#the-schrdinger-model) for $\psi$, $\chi$ and $V$; a height $H$ on $G(\mathbb{A})$ with $H(pk) = |\det a|$ when $p \in P(\mathbb{A})$ has Levi block $a$ and $k \in K$; a real parameter $l$ adapted to $\psi$; a Cartan involution $s_\tau$ for the Gram matrix of $V$ at each archimedean place $\tau$; a Haar measure $\nu$ on $U_V(\mathbb{A})$; and a function $\Phi$ in the Fock space, the span of the functions $p(x, \bar x) \cdot (\text{Gaussian for } s) \cdot \varphi_f(x_f)$ with $p$ a polynomial and $\varphi_f$ Schwartz-Bruhat.

**Definition 4.5.3 (Eisenstein series and theta integral).** Put $s_0 = \tfrac{m}{2} - \tfrac{n}{2}$ and $\Phi_z(g) = H(g)^{z - s_0} (\omega(g)\Phi)(0)$. The [[Eisenstein series|3NZBZXYWAJ]] is
$$E(g, z) = \sum_{\gamma \in P(F) \backslash G(F)} \Phi_z(\gamma g).$$
The theta integral $I(g)$ is the average over $[U_V]$ of $\theta(g, h) = \sum_{\xi} (\omega(g)\Phi)(h^{-1}\xi)$, with $\xi$ over all $m \times n$ matrices over $E$.

**Definition 4.5.4 (Holomorphic value).** A set $U \subseteq \mathbb{C}$ is a right domain if it contains a right half-plane and $U + t \subseteq U$ for $t \ge 0$. A function $h$ on a right half-plane has holomorphic value $c$ at $s_0$ if there are a right domain $U \ni s_0$ and a function $\tilde h$ meromorphic on $U$, equal to $h$ on a right half-plane, analytic at $s_0$, with $\tilde h(s_0) = c$.

**Theorem 4.5.5 (Siegel-Weil formula at $s_0$).** Let $(V, n)$ be in the range and let standard data be given. Then the following hold.

1. For each $g$, the function $h \mapsto \theta(g, h)$ is integrable on $[U_V]$.
2. For $\operatorname{Re} z > \tfrac n2$ the section $\Phi_z$ is left invariant under $P(F)$ and the series $E(g, z)$ converges absolutely.
3. For each $g$, the function $z \mapsto E(g, z)$ has holomorphic value $I(g)$ at $s_0$.

Lean: `PositivityTheory.SiegelWeilCoefficients.field`.

*Proof.* Part 1 follows from the convergence theorem of Weil for the theta integral, since $n + r_V < m$. Part 2 follows from the Iwasawa decomposition $G(\mathbb{A}) = P(\mathbb{A}) K$, which makes $\Phi_z$ left invariant under $P(F)$, and from the convergence of Siegel Eisenstein series of degenerate sections for $\operatorname{Re} z > \tfrac n2$. Part 3 is [the theorem on the value at $s_0$](/entry/lit/). $\square$

**Theorem 4.5.6 (Value at $s_0$).** Let $(V, n)$ be in the range with $n \ge 1$ and let standard data be given. Then for each $g \in G(\mathbb{A})$, the function $z \mapsto E(g, z)$ has holomorphic value $I(g)$ at $s_0$.

Lean: `PositivityTheory.SiegelWeilCoefficients.lit`.

*Proof.* Apply [the reduction theorem](/entry/top7/) with three inputs: [generation of the group](/entry/gen-a-hf/), [the dilation property](/entry/g-idil-gen/), and [the nondegenerate coefficients](/entry/coef-nd/). Note that $n \ge 1$ follows from $n < m \le 2n$. $\square$

We now state the inputs. The first is a fact about generators.

**Proposition 4.5.7 (Generation).** The group $G(\mathbb{A})$ is generated by the elements $n(b)$, the block diagonal elements $\operatorname{diag}(a, d)$ and the lower unipotent elements $\begin{pmatrix} 1 & 0 \\ c & 1 \end{pmatrix}$.

Lean: `PositivityTheory.Rg.Sw.Glob.genA_hf`.

*Proof.* At each place, the local group is generated by these elements and the local maximal compact subgroup, by the Bruhat decomposition, and the compact subgroup is in turn generated by them at the archimedean and finite places. The local statements are glued along the restricted product, using that almost all components lie in the compact subgroup. $\square$

**Definition 4.5.8 (Fourier coefficient).** Let $\lambda$ be a Haar measure on the adelic Hermitian matrices with a fundamental domain $\mathcal{G}$ for the rational ones of measure 1. For a function $f$ on $G(\mathbb{A})$, a rational Hermitian $\beta$ and $g \in G(\mathbb{A})$, the $\beta$-th coefficient is
$$f_\beta(g) = \int_{\mathcal{G}} f(n(b) g) \, \psi\bigl(-\tfrac12 \operatorname{Tr}_{E/F}\operatorname{tr}(\beta b)\bigr) \, d\lambda(b).$$
See [Fourier coefficients](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions).

**Theorem 4.5.9 (Nondegenerate coefficients).** Let $(V, n)$ be in the range, let standard data be given, and let $\lambda$ and $\mathcal{G}$ be as above. For each rational Hermitian $\beta$ with $\det \beta \ne 0$ and each $g$, the function $z \mapsto E_\beta(g, z)$ has holomorphic value $I_\beta(g)$ at $s_0$.

Lean: `PositivityTheory.SiegelWeilCoefficients.coefND`.

*Proof.* For $\operatorname{Re} z > \tfrac n2$ the coefficient unfolds to the big cell: with $w = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$,
$$E_\beta(g, z) = \int \Phi_z(w \, n(b) \, g) \, \psi\bigl(-\tfrac12 \operatorname{Tr}_{E/F}\operatorname{tr}(\beta b)\bigr) \, d\lambda(b).$$
The coefficient $I_\beta(g)$ of the theta integral is the frame integral of $\omega(g)\Phi$ at $\beta$, by the convergence of the theta integral. The right side above is a product of local Whittaker integrals. At the archimedean places it is computed through the Iwasawa decomposition and its restriction to the maximal compact subgroup, which uses the splitting of the Fock space and the additivity of the frame integral in $\beta$. The condition $n + r_V < m$ gives the anisotropy needed at the places where $V$ is small. The product continues holomorphically to $s_0$, and its value there is the frame integral, by the nondegenerate Siegel-Weil comparison. $\square$

The proof of the value at $s_0$ uses the following properties. We list them as named assumptions, since each reduction below removes some of them.

1. Fourier action: the Weyl element acts on pure tensors $f \otimes \Psi$, with $f$ at a real place $\tau$, by $\kappa$ times a partial Fourier transform at $\tau$, with $\kappa \ne 0$.
2. Action away from $\tau$: an element trivial at $\tau$ acts only on the factor $\Psi$.
3. Decomposition: each $g$ is $x \iota(y)$ with $x$ trivial at $\tau$, commuting with $\iota(U(n,n)(\mathbb{R}))$, where $\iota$ embeds the group at $\tau$.
4. Local factorisation: there is a local operator $L$ with $\omega(\iota y)(f \otimes \Psi) = L(y) f \otimes \Psi$.
5. Local instances: each such $L$ comes with a signature $(p, q)$, local data and a $K$-equivariance through a representation $\rho$ of the compact group, with $L(y)$ applied to polynomial-Gaussian functions given by sections in $y$.
6. Lie action: $\omega$ applied to a function with polynomial part $X \cdot P$ is the derivative along $\exp(tX)$.
7. Derivative vanishing: the theta integral of such a derivative is 0.
8. Dilation: for each $g$, $X$ and dilation family $a(t)$, the function $t \mapsto I(g \iota(y a(t)))$ extends holomorphically to an open set containing $\mathbb{R}$, jointly continuous in $y$, and its derivatives at 0 are theta integrals of the dilated functions.
9. Schwartz derivative: for $c > 0$ and a polynomial $P$, the functions $x \mapsto P(e^{tX} x) e^{-c|e^{tX}x|^2}$ are differentiable in $t$ in the Schwartz topology.
10. Theta automorphy: $I$ is continuous and left invariant under $G(F)$.
11. Strong continuation: the Eisenstein series continues meromorphically, with a polynomial $d$ and a right domain.
12. The absolute convergence theorem of [the section on Gaussian moments](/entry/abs-thm-of/), and Weil's convergence theorem for theta integrals.

**Theorem 4.5.10 (Main reduction).** Assume the absolute convergence theorem, local factorisation, action away from $\tau$, local instances, theta automorphy, Lie action, derivative vanishing, dilation, strong continuation, the nondegenerate coefficients, and Weil's convergence theorem. Then for $(V, n)$ in the range with $n \ge 1$ and standard data, $z \mapsto E(g, z)$ has holomorphic value $I(g)$ at $s_0$ for each $g$.

Lean: `PositivityTheory.Rg.Sw.Glob.top`.

*Proof.* Fix $g$. Split the frames of the theta series at the real place $\tau$ and the Fock space as a tensor product of a part at $\tau$ and a part away from $\tau$. Local factorisation gives local operators, and local instances give for each polynomial $P$ a section in the variable at $\tau$ with a signature $(p, q)$. The absolute convergence theorem gives, for these sections, the holomorphic value at $s_0$ of the Eisenstein series of $H^{z - s_0} \cdot \sec(P)$, with value the theta integral of $P$. The decomposition $g = x \iota(y)$ and the action away from $\tau$ move $g$ to the group at $\tau$. Lie action and derivative vanishing show that the derivatives of the remaining part integrate to 0. The dilation property and strong continuation give the joint holomorphy in $z$ and the dilation variable. The nondegenerate coefficients and theta automorphy identify the limit with $I(g)$. $\square$

**Proposition 4.5.11 (First reduction).** The conclusion of the main reduction holds under local factorisation, action away from $\tau$, local instances, theta automorphy, Lie action, derivative vanishing, dilation and the nondegenerate coefficients.

Lean: `PositivityTheory.Rg.Sw.Glob.top2`.

*Proof.* The absolute convergence theorem holds by [its proof in the section on Gaussian moments](/entry/abs-thm-of/). Strong continuation and Weil's convergence theorem are proved results. Apply [the main reduction](/entry/glob-top/). $\square$

**Proposition 4.5.12 (Second reduction).** The conclusion holds under local factorisation, action away from $\tau$, local instances, Lie action, derivative vanishing, dilation and the nondegenerate coefficients.

Lean: `PositivityTheory.Rg.Sw.Glob.top3`.

*Proof.* Theta automorphy follows from Weil's convergence theorem: an absolutely convergent theta integral is continuous and left $G(F)$-invariant. Apply [the first reduction](/entry/top2/). $\square$

**Proposition 4.5.13 (Third reduction).** The conclusion holds under local factorisation, action away from $\tau$, Lie action, derivative vanishing, dilation and the nondegenerate coefficients.

Lean: `PositivityTheory.Rg.Sw.Glob.top5`.

*Proof.* Local instances follow from the action away from $\tau$ and the fact that pure tensors lie in both the Schwartz space and the Fock space, by [the theorem on local instances](/entry/loc-inst-of-away/). Apply [the second reduction](/entry/top3/). $\square$

**Proposition 4.5.14 (Fourth reduction).** The conclusion holds under the Fourier action, generation, the Schwartz derivative property, derivative vanishing, dilation and the nondegenerate coefficients.

Lean: `PositivityTheory.Rg.Sw.Glob.top6`.

*Proof.* Generation, the Fourier action and the decomposition (a proved fact) give the action away from $\tau$: generators trivial at $\tau$ commute with the operators at $\tau$. Local factorisation follows from the decomposition and the local operators. Lie action follows from the Schwartz derivative property, the operator form of the Fourier action, and the factorisation away from $\tau$. Apply [the third reduction](/entry/top5/). $\square$

**Theorem 4.5.15 (Reduction to three inputs).** Assume generation, the dilation property and the nondegenerate coefficients. Then for $(V, n)$ in the range with $n \ge 1$ and standard data, $z \mapsto E(g, z)$ has holomorphic value $I(g)$ at $s_0$ for each $g$.

Lean: `PositivityTheory.Rg.Sw.Glob.top7`.

*Proof.* The Fourier action and the Schwartz derivative property are proved results, and derivative vanishing follows from Weil's convergence theorem. Apply [the fourth reduction](/entry/top6/). $\square$

**Remark 4.5.16 (Formalization).** The names of the two main theorems, "field" and "lit", carry no content ([CoefND.lean](lean:Development/WeilBound/RepresentationTheoryGL/EisensteinSeries/SiegelEisensteinHalfPlane/IntegralUnitCoefficients/CoefND.lean#L19)). The third reduction sits in a file named for a fourth, and there is no fourth reduction with that number ([Top4.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/Top4.lean#L6)). The file of the first and second reductions has a name about vanishing but no vanishing statement ([VanishTop2.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/GlobalGaussLaws/VanishTop2.lean#L13)). The real parameter $l$ and the archimedean data $\theta$ are not unfolded here. The proofs in this section only pass hypotheses between the reductions; the sketches of the main reduction and of the nondegenerate coefficients follow the names of the cited results, which we have not all unfolded.
