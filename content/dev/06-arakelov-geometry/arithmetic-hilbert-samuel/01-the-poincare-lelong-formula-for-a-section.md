---
title: The Poincaré-Lelong formula for a section
decls:
  - GlobalTheory.poincareLelong_sec
  - GlobalTheory.T.poincareLelong_formula_section_projective
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Poincaré-Lelong formula for a section

This section proves the [[Poincaré-Lelong formula|B2YBWQQMHA]] for a global section of a line bundle on a projective variety over a field of characteristic zero, in the integrated form that the rest of the chapter uses. The variety may be singular. We reduce to a smooth variety on which the zero locus of the section is a divisor with simple normal crossings, by Hironaka's principalisation of ideals. The formula is the analytic input of the reciprocity law of [the next section](/entry/side-eq-of-generated/). It is a second form of the formula of [the chapter on heights](/entry/poincare-lelong-of-leaves/).

### Mixed integrals

Let $F$ be a field, let $\sigma : F \to \mathbb{C}$ be an embedding and let $X$ be an integral, locally noetherian scheme, projective over $F$, of dimension $e + 1$. We write $X_\sigma(\mathbb{C})$ for the set of complex points of $X$ over $\sigma$. It is covered by algebraic charts, which identify open sets of $X_\sigma(\mathbb{C})$ with open sets of $\mathbb{C}^{e+1}$.

**Definition 6.1.1 (Line bundle with a smooth weight).** A line bundle with a smooth weight at $\sigma$ is a line bundle $M$ on $X$, given by an open cover $(U_i)$ and a cocycle, together with smooth real functions $\varphi_i$ on $U_{i,\sigma}(\mathbb{C})$ that change by $\log |g_{ij}|^2$ under the transition functions $g_{ij}$. The pointwise norm of a section $s$, written $s_i$ on $U_i$, is
$$\|s\|^2 = |s_i|^2 e^{-\varphi_i}.$$
For a smooth real function $u$ on $X_\sigma(\mathbb{C})$ we write $\mathcal{O}(u)$ for the trivial bundle with the weight $u$, and $M(u)$ for $M$ with the weight $\varphi + u$.

This is a [[Hermitian metric|Q6X6W2N29G]] on $M$ at the single place $\sigma$; see the [hermitian line bundles](/learn/arakelov/#hermitian-line-bundles) of Volume 1. The function $\varphi$ is a local potential of the first [[Chern class|PAD37GKDPD]].

**Definition 6.1.2 (Mixed integral).** Let $\bar L_1, \dots, \bar L_{d}$ be line bundles with smooth weights on a variety of dimension $d$, with weights $\varphi^{(1)}, \dots, \varphi^{(d)}$ in a chart with coordinates $z_1, \dots, z_d$. The mixed density in the chart is
$$\rho = \pi^{-d} \sum_{\tau \in S_d} \operatorname{Re} \det \left( \frac{\partial^2 \varphi^{(\tau(l))}}{\partial z_j \partial \bar z_l} \right)_{j, l}.$$
The positive and the negative parts of $\rho$ glue to two measures $\mu^+$ and $\mu^-$ on the complex points. For a function $f$ that is integrable for both, we put
$$\int f \, c_1(\bar L_1) \cdots c_1(\bar L_d) = \int f \, d\mu^+ - \int f \, d\mu^-.$$

So the mixed integral is the integral against the mixed Monge-Ampère measure of the weights. If all the bundles are equal and the weight is semipositive, the negative part vanishes. For $\mathcal{O}(u)$ the form $c_1$ is $dd^c u$ in the same normalisation.

For a point $z$ of $X$ with closure $Z$, and functions $g$ on $X_\sigma(\mathbb{C})$, we write
$$\int_Z g \, c_1(\bar L_1) \cdots c_1(\bar L_e)$$
for the mixed integral on the reduced closed subscheme $Z$ of the restrictions of $g$ and of the bundles. Let $s$ be a global section of $M$ that does not vanish at the generic point. Then $s$ has a Cartier divisor $\operatorname{div}(s)$, with a multiplicity $\operatorname{mult}_z \operatorname{div}(s) \in \mathbb{Z}$ at each point $z$ of codimension one.

### The formula

We use resolution of singularities in the following form.

**Theorem 6.1.3 (Principalisation of ideals).** Let $k$ be a field of characteristic zero, let $Y$ be an integral scheme, smooth of relative dimension $d$ and projective over $k$, and let $I \ne 0$ be an ideal sheaf on $Y$. Then there is a morphism $s : Y' \to Y$ with these properties: $Y'$ is integral, smooth of relative dimension $d$ and projective over $k$; $s$ is a composite of blow ups along smooth centres over the support of $I$; $s$ is an isomorphism outside the support of $I$; the pull back $s^{-1} I$ is an effective Cartier divisor; and the reduced support of $s^{-1}I$ has simple normal crossings.

Lean: `GlobalTheory.Published.Principalisation`.

This is Hironaka's theorem (Hironaka 1964; Kollár, *Lectures on Resolution of Singularities*, Chapter 3). We take it as given. From it one obtains a log resolution of a pair: for $X$ as above and a section $s$, there is a smooth projective $Y$ with a morphism $\pi : Y \to X$ that maps the generic point to the generic point with residue degree $1$, such that the zero locus of $\pi^* s$ has simple normal crossings. This is the form in which we use [[resolution of singularities|MB52NDA6WN]].

**Theorem 6.1.4 (Poincaré-Lelong formula for a section).** Assume principalisation of ideals. Let $F$, $\sigma$ and $X$ be as above, with $X$ of dimension $e + 1$. Let $\bar L_1, \dots, \bar L_e$ and $\bar M$ be line bundles with smooth weights at $\sigma$. Let $s$ be a global section of $M$ that does not vanish at the generic point of $X$, and let $u$ be a smooth real function on $X_\sigma(\mathbb{C})$. Then
$$\begin{aligned} 2 \int \log \|s\| \, dd^c u \, c_1(\bar L_1) \cdots c_1(\bar L_e) &= \sum_{z} \operatorname{mult}_z \operatorname{div}(s) \int_{\overline{\{z\}}} u \, c_1(\bar L_1) \cdots c_1(\bar L_e) \\ &\quad - \int u \, c_1(\bar M) \, c_1(\bar L_1) \cdots c_1(\bar L_e). \end{aligned}$$

Lean: `GlobalTheory.poincareLelong_sec` (also `GlobalTheory.T.poincareLelong_formula_section_projective`, a second name).

The classical form is the identity of currents $dd^c \log \|s\|^2 = \delta_{\operatorname{div}(s)} - c_1(\bar M)$ on a complex manifold (Griffiths and Harris, *Principles of Algebraic Geometry*, Chapter 3, Section 2). Integrate it against the closed form $u \, c_1(\bar L_1) \cdots c_1(\bar L_e)$ and move $dd^c$ from $u$ to $\log\|s\|^2$. Since $\log \|s\|^2 = 2 \log\|s\|$, this gives the factor $2$ on the left.

*Proof.* Let $\pi : Y \to X$ be the log resolution of the pair $(X, s)$ given by principalisation. So $Y$ is smooth and projective over $F$ of dimension $e + 1$, $\pi$ maps the generic point to the generic point with residue degree $1$, and the zero locus of $s' = \pi^* s$ is a divisor with simple normal crossings. The pull back $\pi^* \bar M$ carries the pulled back weight, so $\|s'\| = \|s\| \circ \pi$ on complex points.

On $Y$ the formula holds for $s'$, the bundles $\pi^* \bar L_i$, $\pi^*\bar M$ and the function $u \circ \pi$. This is the Poincaré-Lelong formula on a smooth projective variety for a section whose divisor has simple normal crossings, which we take as given from the analytic part of the development; near a crossing point it reduces to the one variable formula $dd^c \log |z|^2 = \delta_0$ in each local coordinate.

We transfer the three terms to $X$. A morphism of integral varieties of the same dimension that maps the generic point to the generic point with residue degree $\delta \ne 0$ multiplies mixed integrals by $\delta$. Here $\delta = 1$. Mixed integrals also depend only on the isometry classes of the bundles, and $\pi^* \mathcal{O}(u)$ is isometric to $\mathcal{O}(u \circ \pi)$. So the left side and the last term on $Y$ equal those on $X$.

For the divisor term, fix a point $z$ of codimension one in $X$ and a local equation $f$ of $\operatorname{div}(s)$ near $z$. Near $z$ the map $\pi$ is finite. For the points $w$ of codimension one in $Y$ over $z$ we have
$$\sum_{\pi(w) = z} \operatorname{ord}_w(\pi^* f) \, [\kappa(w) : \kappa(z)] = \operatorname{ord}_z(f) = \operatorname{mult}_z \operatorname{div}(s).$$
Integrals over the closures of the points $w$ push forward to $[\kappa(w) : \kappa(z)]$ times the integral over the closure of $z$. The other points $w$, which map to points of codimension at least two, give no contribution. So the divisor term on $Y$ equals the divisor term on $X$. $\square$

**Remark 6.1.5 (Formalization).** The formula is stated for one embedding $\sigma$ of a field $F$. The integrals are differences of integrals against the positive and the negative parts of a glued density; their existence is part of the inputs used in the proof. The Poincaré-Lelong formula for normal crossings, the pull back of mixed integrals and the push forward of divisor integrals are separate results of the development that the proof cites.
