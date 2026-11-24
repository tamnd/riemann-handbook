---
title: Chern forms of line bundles
decls:
  - GlobalTheory.chernInt_eq_topSelf_of_generated
  - GlobalTheory.T.chernMass_eq_selfIntersection_of_generated
  - GlobalTheory.MassDegree.chernInt_eq_topSelf
  - GlobalTheory.T.chernMass_eq_selfIntersection_lineBundle
  - GlobalTheory.ChernDegree.chernDegreeComplex
  - GlobalTheory.T.degree_eq_integral_topChernForm_complex
  - GlobalTheory.ChernLine.integral_evalF_c1W_eq_interPoly
  - GlobalTheory.T.integral_chernFormPoly_eq_intersectionNumber
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Chern forms of line bundles

This section proves the Chern-Weil theorem for line bundles on a smooth projective variety. The integral of the top power of the first Chern form of a smooth weight is the self intersection number of the bundle. We first prove this for a globally generated bundle, where the bundle is the pull back of $\mathcal{O}(1)$ under a map to a projective space. A twist by a high power of $\mathcal{O}(1)$ and a comparison of two polynomials then give the general case. From the result for one bundle we get the same equality for every polynomial in the first Chern forms of several bundles. This is the input of [the splitting principle](/entry/fibre-integral/) in the next section. For the classical statements see the [Chern-Weil forms](/learn/positivity-resolution/#chern-weil-forms) of Volume 1.

### Varieties and intersection numbers

**Definition 5.1.1 (Projective variety).** Let $F$ be a field. A projective variety over $F$ is a closed subscheme $Y$ of a projective space $\mathbb{P}^N_F$ that is smooth over $F$ of relative dimension $\dim Y$ and geometrically integral. We write $K(Y)$ for its function field and $\operatorname{Div}(Y)$ for its Weil divisors.

Lean: `GlobalTheory.ProjVar.Var`.

**Definition 5.1.2 (Intersection number).** Let $X$ be a scheme over a field $k$, let $\mathcal{F}$ be a coherent sheaf on $X$ and let $L_1, \dots, L_n$ be line bundles on $X$. The intersection number of the $L_i$ on $\mathcal{F}$ is
$$(L_1 \cdots L_n \cdot \mathcal{F}) = \sum_{S \subseteq \{1, \dots, n\}} (-1)^{|S|} \, \chi\Big(\mathcal{F} \otimes \bigotimes_{i \in S} L_i^{-1}\Big).$$
The self intersection of degree $d$ of a line bundle $M$ is $(M^d) = (M \cdots M \cdot \mathcal{O}_X)$ with $d$ factors. For a projective variety $Y$ and divisors $\Delta_1, \dots, \Delta_{\dim Y}$, we write $(\Delta_1 \cdots \Delta_{\dim Y})$ for the intersection number of the line bundles $\mathcal{O}(\Delta_i)$ on $\mathcal{O}_Y$.

Lean: `GlobalTheory.interNum`, `GlobalTheory.topSelfIntersection` and `GlobalTheory.ProjVar.Var.inter`.

This is the definition of Snapper and Kleiman. If $X$ is projective and $n = \dim X$, it is the usual intersection number of [line bundles and divisors](/learn/geometry/#line-bundles-and-divisors), and it is multilinear and symmetric in the $L_i$. We do not unfold here the line bundle $\mathcal{O}(\Delta)$ of a divisor.

**Definition 5.1.3 (Intersection form on polynomials).** Let $Y$ be a projective variety, let $\kappa$ be a set and let $\Delta : \kappa \to \operatorname{Div}(Y)$. The intersection form of $\Delta$ is the $\mathbb{R}$-linear map $\mathbb{R}[x_a : a \in \kappa] \to \mathbb{R}$ that sends a monomial $x_{s(1)} \cdots x_{s(\dim Y)}$ of degree $\dim Y$ to $(\Delta_{s(1)} \cdots \Delta_{s(\dim Y)})$, and every other monomial to $0$. We write it $P \mapsto \langle P \rangle_\Delta$.

Lean: `GlobalTheory.ProjVar.Var.interPoly`.

The value on a monomial does not depend on the order of its factors, since the intersection number is symmetric.

### Weights and Chern integrals

Fix an embedding $\sigma : F \to \mathbb{C}$. We write $Y_\sigma(\mathbb{C})$ for the complex points of $Y$ over $\sigma$. Algebraic charts identify open sets of $Y_\sigma(\mathbb{C})$ with open sets of $\mathbb{C}^{\dim Y}$.

**Definition 5.1.4 (Weight).** Let $B$ be a line bundle on $Y$, given by an open cover $(U_i)$ and a cocycle $(g_{ij})$. A weight on $B$ at $\sigma$ is a family of real functions $\varphi_i$ on $U_{i,\sigma}(\mathbb{C})$ with
$$\varphi_j = \varphi_i - \log |g_{ij}|^2.$$
The norm of a section $s$, written $s_i$ on $U_i$, is $\|s\|^2 = |s_i|^2 e^{-\varphi_i}$. The weight is smooth if each $\varphi_i$ is smooth on $U_{i,\sigma}(\mathbb{C})$.

Lean: `GlobalTheory.Weight` (also `GlobalTheory.Weight.IsCInf`, the smoothness condition).

A weight is a [[Hermitian metric|Q6X6W2N29G]] on $B$ at the place $\sigma$, as in the [hermitian line bundles](/learn/arakelov/#hermitian-line-bundles) of Volume 1. The function $\varphi_i$ is a local potential of the first [[Chern class|PAD37GKDPD]].

**Definition 5.1.5 (Chern integral).** Let $\varphi$ be a smooth weight on $B$ and let $D = \dim Y$. In an algebraic chart with coordinates $z_1, \dots, z_D$ that lies in $U_i$, the Chern density is
$$\rho_\varphi = \frac{D!}{\pi^D} \operatorname{Re} \det \Big( \frac{\partial^2 \varphi_i}{\partial z_j \partial \bar z_l} \Big)_{j,l}.$$
The positive parts and the negative parts of these densities glue to two measures $\mu^+_\varphi$ and $\mu^-_\varphi$ on $Y_\sigma(\mathbb{C})$. A function $f$ on a set $S$ is Chern integrable if it is integrable on $S$ for both measures. The Chern integral is
$$\int_S f \, c_1(B, \varphi)^D = \int_S f \, d\mu^+_\varphi - \int_S f \, d\mu^-_\varphi.$$

Lean: `GlobalTheory.Weight.chernInt` (also `GlobalTheory.Weight.ChernIntegrableOn`, the integrability condition, and `GlobalTheory.AlgChart.chernDens`, the density).

The density is the density of $(dd^c \varphi)^D$ with respect to the Lebesgue measure of the chart. A change of chart multiplies the determinant by the square of the absolute value of a holomorphic Jacobian, so the two measures are well defined.

**Definition 5.1.6 (Presentation of a divisor).** Let $\Delta$ be a divisor on $Y$ and let $L$ be a line bundle with cover $(U_i)$ and cocycle $(g_{ij})$. A family $r_i \in K(Y)^\times$ presents $\Delta$ by $L$ if $r_i = g_{ij} r_j$ for all $i, j$, and if $r_i$ is a local equation of $\Delta$ on $U_i$ for each $i$.

Lean: `GlobalTheory.Cartier.Presents`.

So $r$ is a rational section of $L$ with divisor $\Delta$, and $L$ is isomorphic to $\mathcal{O}(\Delta)$.

### The self intersection of a line bundle

**Lemma 5.1.7 (Generated bundles).** Let $Y$ be a projective variety over $\mathbb{C}$, let $L$ be a line bundle on $Y$ with a smooth weight $\varphi$, and let $u_1, \dots, u_n$ be global sections of $L$ whose non-vanishing loci cover $Y$. Then
$$\int_{Y(\mathbb{C})} c_1(L, \varphi)^{\dim Y} = (L^{\dim Y}).$$

Lean: `GlobalTheory.chernInt_eq_topSelf_of_generated` (also `GlobalTheory.T.chernMass_eq_selfIntersection_of_generated`, a second name).

*Proof.* Put $D = \dim Y$. The field $\mathbb{C}$ is infinite and $Y$ has dimension $D$, so general linear combinations $s_0, \dots, s_D$ of the $u_i$ still generate $L$. These sections define a morphism $g : Y \to \mathbb{P}^D$, and $L$ is isomorphic to $g^* \mathcal{O}(1)$. The Chern integral of a smooth weight does not change under an isomorphism of line bundles that carries one weight to the other, and it does not depend on the choice of the smooth weight. So the left side equals the Chern integral of the pull back of the Fubini-Study weight on $\mathcal{O}(1)$. For this weight the integral is $(g^*\mathcal{O}(1)^D)$. The self intersection depends only on the isomorphism class of the bundle, so it equals $(L^D)$. $\square$

**Theorem 5.1.8 (Chern integral of a line bundle).** Let $Y$ be a projective variety over $\mathbb{C}$ and let $L$ be a line bundle on $Y$ with a smooth weight $\varphi$. Then
$$\int_{Y(\mathbb{C})} c_1(L, \varphi)^{\dim Y} = (L^{\dim Y}).$$

Lean: `GlobalTheory.MassDegree.chernInt_eq_topSelf` (also `GlobalTheory.T.chernMass_eq_selfIntersection_lineBundle`, a second name).

*Proof.* Put $D = \dim Y$. Let $\psi$ be the pull back to $Y$ of the Fubini-Study weight on $\mathcal{O}(1)$ of the ambient projective space $\mathbb{P}^N$. It is smooth. For $m \geq 0$ the bundle $L(m) = L \otimes \mathcal{O}(1)^{\otimes m}$ carries the smooth weight $\varphi + m\psi$.

The Chern density of $\varphi + m\psi$ is the determinant of the sum of two Hessians, one of them multiplied by $m$. So there is a real polynomial $P$ with $P(0) = \int c_1(L, \varphi)^D$ and
$$P(m) = \int_{Y(\mathbb{C})} c_1(L(m), \varphi + m\psi)^D \quad (m \geq 0).$$
The intersection number is a polynomial function of $m$ by the theorem of Snapper. So there is a polynomial $Q$ with $Q(0) = (L^D)$ and $Q(m) = (L(m)^D)$ for $m \geq 0$.

The bundle $\mathcal{O}(1)$ is ample on $Y$. By Serre's theorem there is $m_0$ such that $L(m)$ is generated by global sections for all $m \geq m_0$. For these $m$ the lemma on generated bundles gives $P(m) = Q(m)$. Two polynomials that agree at infinitely many points are equal. So $P = Q$, and the value at $0$ gives the claim. $\square$

The theorem holds for every smooth weight, positive or not. The negative part of the density is the reason for the two measures in the definition of the Chern integral.

**Theorem 5.1.9 (Chern integral of a divisor).** Let $Y$ be a projective variety over $\mathbb{C}$, let $\Delta$ be a divisor on $Y$, let $L$ be a line bundle with a family $r$ that presents $\Delta$, and let $\varphi$ be a smooth weight on $L$. Then the constant function $1$ is Chern integrable on $Y(\mathbb{C})$, and
$$\int_{Y(\mathbb{C})} c_1(L, \varphi)^{\dim Y} = (\Delta \cdots \Delta),$$
with $\dim Y$ factors $\Delta$ on the right.

Lean: `GlobalTheory.ChernDegree.chernDegreeComplex` (also `GlobalTheory.T.degree_eq_integral_topChernForm_complex`, a second name).

*Proof.* The two measures $\mu^\pm_\varphi$ are finite, since the Chern integral of $1$ is the Monge-Ampère integral of a smooth weight on a compact space. So $1$ is Chern integrable. By the theorem above the integral is $(L^{\dim Y})$. Since $r$ presents $\Delta$, the bundle $L$ is isomorphic to $\mathcal{O}(\Delta)$, and $(L^{\dim Y}) = (\Delta \cdots \Delta)$. $\square$

The statement of this theorem is the hypothesis `ChernDegreeComplex` of the development. The same statement over a field $F$ with an embedding $\sigma : F \to \mathbb{C}$ is the hypothesis `ChernDegree`. The development deduces it from the complex case by a separate lemma, which we do not open here. `ChernDegree` is one half of the input `ArDegree` of the step [every character from the literature](/step/every-character-of-literature/).

### Polynomials in first Chern forms

Let $X$ be a projective variety over $F$ and $\sigma : F \to \mathbb{C}$. A smooth weight $\psi$ on a line bundle defines the first Chern form $c_1(\psi) = dd^c \psi$, an even form on $X_\sigma(\mathbb{C})$. For a real polynomial $P$ in variables $x_a$ and forms $\omega_a$, we write $P(\omega)$ for the form obtained by substitution in the algebra of even forms. The integral $\int_X$ of an even form is the integral of its part of top degree, taken as the difference of the integrals of the positive and the negative parts of its density.

**Theorem 5.1.10 (Polynomials in first Chern forms).** Assume `ChernDegree`. Let $X$ be a projective variety over $F$, let $\sigma : F \to \mathbb{C}$, and let $\kappa$ be a finite set. For each $a \in \kappa$ let $\Delta_a$ be a divisor, $L_a$ a line bundle with a family $r_a$ that presents $\Delta_a$, and $\psi_a$ a smooth weight on $L_a$. Then for every $P \in \mathbb{R}[x_a : a \in \kappa]$,
$$\int_{X_\sigma(\mathbb{C})} P\big(c_1(\psi)\big) = \langle P \rangle_\Delta.$$

Lean: `GlobalTheory.ChernLine.integral_evalF_c1W_eq_interPoly` (also `GlobalTheory.T.integral_chernFormPoly_eq_intersectionNumber`, a second name).

*Proof.* Put $D = \dim X$ and let $P_D$ be the homogeneous component of degree $D$ of $P$. The intersection form vanishes on every monomial of degree other than $D$, so $\langle P \rangle_\Delta = \langle P_D \rangle_\Delta$. A product of first Chern forms of degree other than $D$ is a form of degree other than $(D, D)$, and its top density vanishes. So the left side for $P$ equals the left side for $P_D$. For homogeneous polynomials of degree $D$ the equality is a theorem of the development that derives it from `ChernDegree`. We use it here and do not open its proof. $\square$

For $\kappa$ with one element and $P = x^D$ the theorem is the statement `ChernDegree` itself.

**Remark 5.1.11 (Formalization).** The theorems on the self intersection of a line bundle give only the value of the Chern integral, which is a difference of two real integrals. Integrability is a separate claim, and only the theorem on divisors states it; its proof takes it from a comparison with the Monge-Ampère integral. The intersection number is defined by the alternating sum of Euler characteristics, not by a cycle class, and the polynomial in the twist $m$ comes from this sum. The integral of an even form on the atlas of complex points is a definition of the development that we do not unfold beyond its positive and negative parts. The case of a homogeneous polynomial is a separate theorem that the proof cites.
