---
title: Free Hodge modules at stalks
decls:
  - PositivityTheory.Xgn.HodgeFreeStalk.at_point
  - PositivityTheory.Xgn.hodge_free_every_stalk
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Free Hodge modules at stalks

The rest of the chapter collects results on the integral structure of the objects that enter proportionality. This section proves a freeness statement. Let $t$ be a semi-abelian scheme with $\mathcal{O}_E$-action. A formal germ of $t$ at a point carries a module of rank $2d$ over the local ring, with an action of $\mathcal{O}_E$. We show that this module is free over $\mathcal{O}_E \otimes R$ when the characteristic polynomials of the action are the right ones. Over a field of characteristic $0$ this is linear algebra. In positive residue characteristic it needs a geometric input on the fibre. The results are used in [freeness at component stalks](/entry/hfree-at-component-stalks/).

Throughout, $E$ is a CM field with host datum $H$, and the star map of $\mathcal{O}_E$ is the complex conjugation $a \mapsto \bar a$ of $H$. Let $X$ be a scheme and $t$ a semi-abelian scheme over $X$ with $\mathcal{O}_E$-action. For $a \in \mathcal{O}_E$ let $P_a \in \mathbb{Z}[T]$ be the characteristic polynomial of multiplication by $a$ on $\mathcal{O}_E$, and fix a $\mathbb{Z}$-basis $(b_j)$ of $\mathcal{O}_E$.

**Definition 7.8.1 (Hodge operators of a formal germ).** Let $R$ be a ring and $g$ a formal germ of $t$ of dimension $d$ over $R$: a formal group of dimension $d$ over $R$ ([formal group laws](/learn/formal-groups/#formal-group-laws)) with the action of $\mathcal{O}_E$ and its pairing data. For $a \in \mathcal{O}_E$ let $\rho(a) \in M_d(R)$ be the action of $a$ on the tangent space. The *Hodge operator* of $a$ is the endomorphism $\rho_H(a)$ of $R^d \times R^d$ with block matrix
$$h(a) = \begin{pmatrix} \rho(a) & 0 \\ -\beta(a)^{\mathsf{T}} & \rho(\bar a)^{\mathsf{T}} \end{pmatrix},$$
where $\beta(a)$ is the bilinear term of the pairing at $a$. The germ satisfies:

1. the *characteristic condition* of rank $r$ if $\det(T - \rho_H(a)) = P_a(T)^r$ in $R[T]$ for all $a \in \mathcal{O}_E$;
2. the *freeness condition* of rank $r$ if there are $x_1, \dots, x_r \in R^{2d}$ such that the vectors $\rho_H(b_j)\, x_i$ form an $R$-basis of $R^{2d}$.

The freeness condition says that $R^{2d}$ is a free $\mathcal{O}_E \otimes R$-module of rank $r$ with basis $x_1, \dots, x_r$. It implies the characteristic condition. The converse fails in general: over a field of characteristic $p$ that ramifies in $E$, the algebra $\mathcal{O}_E \otimes \mathbb{F}_p$ is not reduced, and the characteristic polynomials do not determine the module.

**Lemma 7.8.2 (Characteristic condition and base change).** Let $f \colon R \to R'$ be a ring map and $g'$ the base change of $g$.

1. If $g$ satisfies the characteristic condition, so does $g'$.
2. If $f$ is injective and $g'$ satisfies the characteristic condition, so does $g$.
3. If $g'$ is isomorphic to a germ $g_0$ over $R'$ and $g_0$ satisfies the characteristic condition, so does $g'$.

*Proof.* The matrix $h(a)$ of $g'$ is the image of the matrix $h(a)$ of $g$, and characteristic polynomials commute with base change. This gives 1, and 2 follows since $R[T] \to R'[T]$ is injective. An isomorphism of germs gives an invertible linear map of $R'^{2d}$ that conjugates the two Hodge operators, and conjugate matrices have the same characteristic polynomial. $\square$

**Theorem 7.8.3 (Freeness at a stalk).** Let $z \in X$, let $R = \mathcal{O}_{X,z}$ with residue field $\kappa(z)$, and let $g$ be a formal germ of $t$ of dimension $d$ over $R$ that satisfies the characteristic condition of rank $r$. Suppose that $t$ satisfies the condition `PowFns`. If $\kappa(z)$ has characteristic $p > 0$, suppose that there is a point $x \colon \operatorname{Spec} k \to X$ with $k$ algebraically closed and image $z$ at which the geometric fibre condition `GeomPF` holds. Then $g$ satisfies the freeness condition of rank $r$.

Lean: `PositivityTheory.Xgn.HodgeFreeStalk.at_point`.

*Proof.* The map $a \mapsto h(a)$ is a ring map $\mathcal{O}_E \to M_{2d}(R)$, by the compatibility of the action and the pairing. Comparing degrees in the characteristic condition gives $2d = r\,[E : \mathbb{Q}]$.

We first show: *if $R \to K$ is a local map to a field and the freeness condition holds after base change to $K$, it holds over $R$.* Choose $x_i \in R^{2d}$ that lift a free basis over $K$. The $r\,[E:\mathbb{Q}] = 2d$ vectors $\rho_H(b_j)\, x_i$ span $R^{2d}$ modulo the maximal ideal, so they span $R^{2d}$ by Nakayama's lemma ([local rings](/learn/commutative-algebra/#local-rings-and-dimension)). A surjective endomorphism of $R^{2d}$ is bijective, so they form a basis.

*Case $\operatorname{char} \kappa(z) = 0$.* By the lemma, the characteristic condition holds over $K = \kappa(z)$. The algebra $E \otimes K$ is a product of fields $K_1 \times \dots \times K_s$, since $E/\mathbb{Q}$ is separable. So $M = K^{2d}$ is $\bigoplus_l M_l$ with $M_l$ a $K_l$-vector space. Take $a$ with $E = \mathbb{Q}(a)$. Then $P_a = \prod_l P_{a,l}$ with $P_{a,l}$ the distinct minimal polynomials of the images of $a$ over $K$, and the characteristic polynomial of $a$ on $M$ is $\prod_l P_{a,l}^{\dim_{K_l} M_l}$. So the characteristic condition gives $\dim_{K_l} M_l = r$ for all $l$, and $M$ is free of rank $r$ over $E \otimes K$. Then lift to $R$.

*Case $\operatorname{char} \kappa(z) = p > 0$.* Take $x$ and $k$ from the hypothesis, and let $f \colon \mathcal{O}_{X,z} \to k$ be the local map at the closed point. Then $p = 0$ in $k$, since $p$ is not a unit in $R$. Base change gives a germ $g_2$ over $k$, which satisfies the characteristic condition by the lemma. The theorem on [freeness in the geometric case](/entry/height-char-free-geometric/) uses `GeomPF` and `PowFns` to give the freeness condition for $g_2$. Lift it to $R$. $\square$

**Definition 7.8.4 (Germ system).** Let $\Omega$ be a field of characteristic $0$, $\xi \colon \operatorname{Spec} \Omega \to X$ a point with image $\eta$, and let $\operatorname{Cpt}(\xi)$ be the set of $x \in X$ with $\eta \rightsquigarrow x$. A *germ system* for $t$ at $\xi$ consists of a formal germ $g_0$ of $t$ at $\xi$, adapted to a Lie model $M$ of dimension $d$, and for each $x \in \operatorname{Cpt}(\xi)$ a formal germ $g_x$ over $\mathcal{O}_{X,x}$ and an isomorphism from $g_0$ to the base change of $g_x$ to $\Omega$. These data are compatible under specialization, and the lattices they define are locally constant. The point $\xi$ is a *generic component point* if $\mathcal{O}_{X,\eta} \to \Omega$ is bijective and $\mathcal{O}_{X,x} \to \Omega$ is injective for each $x \in \operatorname{Cpt}(\xi)$.

**Theorem 7.8.5 (Freeness at every specialization).** Let $\xi$ be a generic component point and $S$ a germ system for $t$ at $\xi$. Suppose that $t$ satisfies `PowFns`, that $g_0$ satisfies the characteristic condition of rank $r$, and that the geometric fibre condition holds at each $x \in \operatorname{Cpt}(\xi)$ of positive residue characteristic, as in the last theorem. Then $g_x$ satisfies the freeness condition of rank $r$ for every $x \in \operatorname{Cpt}(\xi)$.

Lean: `PositivityTheory.Xgn.hodge_free_every_stalk`.

*Proof.* Fix $x \in \operatorname{Cpt}(\xi)$. By part 3 of the lemma, the isomorphism of $S$ moves the characteristic condition from $g_0$ to the base change of $g_x$ to $\Omega$. By part 2, with the injective map $\mathcal{O}_{X,x} \to \Omega$, it holds for $g_x$. Freeness at a stalk gives the freeness condition. $\square$

The characteristic condition is a condition on polynomials, and it is checked once, at the generic point. The theorem turns it into freeness at all points of the closure of $\eta$, including the points of positive characteristic. There the work is done by the geometric case, which rests on [freeness for the geometric fibre](/entry/hfree-geom/).

**Remark 7.8.6 (Formalization).** Both theorems are in [HodgeFreeEveryStalk.lean](lean:Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/HodgeFreeEveryStalk.lean#L148), lines 148 and 178. The block matrix $h(a)$ is `hm` (line 21), and $\beta(a)$ is `bil (B.ad a) 1 1`, which we did not unfold. The conditions `HFree` and `HChar` and the structure `GermSys` are in [GermSys.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/GermSys.lean#L47). We did not unfold `PowFns`, `GeomPF` or `LieModel`. The lifting step and the case of characteristic $0$ are the lemmas `representation_basis_linear_independent` and `characteristic_polynomial_free_generators`, whose proofs we did not open; the proofs above are ours. The hypothesis on the residue characteristic is stated for every prime $p$ with $p = 0$ in $\kappa(z)$, and at most one prime has this property (line 151). Only the injectivity part of the generic component condition is used. The namespace `PositivityTheory` and the folder `WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies` do not describe the content.
