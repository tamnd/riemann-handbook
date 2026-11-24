---
title: Results from the literature
decls:
  - UpperTheory.Lit.Bur.BurPos.burGapPos_of_bmu
  - UpperTheory.Lit.burGapPos
  - UpperTheory.Lit.realInputE_holds
  - UpperTheory.Lit.Sw47.weilUnitary
  - UpperTheory.Lit.prismaticDieudonneHodge
  - UpperTheory.Lit.blochKatoLocal
  - UpperTheory.Lit.HoweDuality.lift_of_irr
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Results from the literature

This section proves six results that the proof uses in the form in which they appear in the literature: uniqueness of real Bessel forms for discrete series with a large gap, an archimedean input on discrete series used to separate functionals, convergence of unitary theta integrals with the Siegel-Weil formula, prismatic Dieudonné modules with their Hodge filtration, the local Bloch-Kato dualities, and the identification of theta lifts for $(GL_r, GL_{r+t})$ over a $p$-adic field. They are passed on by the [literature step](/step/every-character-of-literature/), the [row step](/step/every-character-of-row/), the [Bessel seesaw chapter](/proof/bessel-seesaw/) and the [theta lift for $GL$](/entry/theta-lift-gl-of-zelevinsky-classification/); each theorem below names its user. Each proof here assembles results proved elsewhere in the development.

### Real Bessel forms

Let $J$ be an $n \times n$ Hermitian matrix and $J_0$ an $m \times m$ one, with $1 \leq m$, and let $(F, e, z)$ be a *Bessel frame*: $F$ embeds $\mathbb{C}^m$ isometrically, $e$ spans an isotropic subspace of rank $r$, and $z$ is a vector orthogonal to both, with $n = 2r + m + 1$. Let $\chi$ be a generic character of the unipotent part attached to $(e, z)$. For a [[unitary representation|74BPYJNZTM]] $\sigma$ of $U(J)$ on a Hilbert space $H$ and a finite-dimensional representation $\pi_0$ of $U(J_0)$ on $W$, a *Bessel form* is a bilinear form on the smooth vectors of $H$ and on $W^{*}$ that transforms under the Bessel subgroup by $\chi \otimes \pi_0$; see [Bessel periods](/learn/periods/#bessel-and-fourier-jacobi-periods). We say $\sigma$ is a *[[discrete series|9AB7HYGPEK]] with gap $h$* if, after a change of frame to a diagonal sign matrix, it is the discrete series with Harish-Chandra parameter $\lambda$ whose entries of opposite signs differ by at least $h$.

**Theorem 2.8.1 (Real Bessel forms from Bessel maps).** Assume that Bessel maps into Harish-Chandra type models of discrete series with gap at least $120 n^3$ are unique up to scalars. Let $\langle z, z \rangle < 0$ and let $J_0$ be positive definite. Let $\sigma$ be an irreducible unitary representation of $U(J)$ that is a discrete series with gap $h \geq 120 n^3$, and let $\pi_0$ be a continuous irreducible representation of $U(J_0)$. Then the space of Bessel forms has dimension at most $1$.

Lean: `UpperTheory.Lit.Bur.BurPos.burGapPos_of_bmu`

*Proof.* If $W = 0$ every form is zero. Otherwise normalize the frame: there are matrices $Q$ and $A$ that carry $(J, J_0, F, e, z)$ to the standard frame with $z$ a positive multiple of the last basis vector of the anisotropic part. Conjugating $\sigma$ by $Q$ gives a discrete series in the standard frame with the same gap, and the smooth vectors correspond. The contragredient of $\pi_0$, transported by $A$, is an irreducible representation of the compact group $U(m)$, hence unitarizable and isomorphic to a model of its Harish-Chandra type. Composing a Bessel form with this isomorphism gives a Bessel map in the sense of the hypothesis. By uniqueness any two such maps are dependent, and so are any two Bessel forms. $\square$

**Theorem 2.8.2 (Uniqueness of real Bessel forms with a large gap).** The conclusion of the previous theorem holds without its hypothesis.

Lean: `UpperTheory.Lit.burGapPos`

*Proof.* The [uniqueness of Bessel maps with a gap](/entry/bessel-map-uniq-gap/) is a theorem. Apply the previous theorem. $\square$

This is the archimedean multiplicity one for Bessel models of unitary groups, of the kind proved by Jiang, Sun and Zhu, here only for discrete series with a large gap. Its user is the [separation of Bessel functionals](/entry/bessel-separate-of-step-gap/).

### An archimedean input on discrete series

Let $n \geq 3$, let $\varepsilon$ be signs on $n + 1$ coordinates and $\varepsilon'$ signs on $n$ coordinates, and embed $U(J_{\varepsilon'})$ in $U(J_\varepsilon)$ fixing a unit vector $e_0$. Put $\beta(C, n, B) = \exp\bigl(C (n+1)^4 \log(8 (n+1) B)\bigr)$.

**Theorem 2.8.3 (Real input for separation).** There is $C > 0$ with the following property. Let $\lambda$ and $\mu$ be interlacing Harish-Chandra parameters for $\varepsilon$ and $\varepsilon'$, with gaps at least $2$, gaps at least $1000 (n+1)^3$ between entries of opposite signs, and entries of size at most $B$, and let $\pi$ and $\sigma$ be the discrete series of $U(J_\varepsilon)$ and $U(J_{\varepsilon'})$ with these parameters. Then there are a unit vector $v_0$ in the lowest $K$-type of $\pi$, $g_0 \in U(J_\varepsilon)$, a smooth unit vector $w'$ of $\sigma$ and $c > 0$ such that, for $v = \pi(g_0) v_0$ and integrals over $h \in U(J_{\varepsilon'})$:

1. for every $b$,
$$\int \overline{\langle v, \pi(h) v \rangle}\, \langle b, \sigma(h) w' \rangle\, dh = c \langle b, w' \rangle;$$
2. for every $g$,
$$\int |\langle v, \pi(g h) v \rangle|\, dh \leq c\, \beta(C, n, B)\, |g e_0|^{-(2n+7)};$$
3. the same integral with $d\pi(X) v$ in one slot is at most $c\, \beta(C, n, B)$ for $X$ in the Lie algebra of $U(J_{\varepsilon'})$ of Hilbert-Schmidt norm at most $1$;
4. $|\langle v, \pi(g) v \rangle| \leq A \|g\|^{-20 (n+1)^2}$ for some $A$.

Lean: `UpperTheory.Lit.realInputE_holds`

*Proof.* Two facts are fed into one general lemma. First, a seed vector in the lowest $K$-type and a moment estimate give $g_0$ with $\|g_0\|$ bounded and $\|P \pi(g_0) v_0\| \geq \beta^{-1}$, where $P$ is the projection onto a copy of $\sigma$ in the restriction of $\pi$. Second, an eigenvalue computation turns a vector with a large projection into a $w'$ satisfying item 1. The lemma adds the bounds 2 to 4 from general estimates for matrix coefficients of discrete series and normalizes $w'$. $\square$

Its user is the [separation of functionals](/entry/functionals-separate-of-howe-unram-of-siegel-weil/), where it gives a nonzero bottom period.

### Theta integrals and the Siegel-Weil formula

**Theorem 2.8.4 (Siegel-Weil for unitary pairs).** Let $A$ and $B$ be Hermitian spaces of ranks $n \geq 1$ and $m$ over the CM field of a datum, let $r$ be the Witt index of $B$, and suppose $r = 0$ or $n + r < m$. Then:

1. there is a continuous seminorm $\nu$ on the adelic Schwartz space with
$$\int_{[U(B)]} \sum_{\xi} |\varphi(h^{-1} \xi)|\, dh \leq \nu(\varphi),$$
the sum over $\xi \in M_{m \times n}(E)$;
2. for a Weil representation $\omega$ of $U(A \oplus A^-) \times U(B)$ and a theta function $f$, the theta kernel $h \mapsto \theta(g, h; f)$ is integrable on $[U(B)]$ for each $g$;
3. if $2n < m$, the section $\Phi_f$ obtained by integrating $\omega(g, 1) f$ over the diagonal is invariant under the rational Siegel parabolic $P$, the [[Eisenstein series|3NZBZXYWAJ]] $\sum_{P(F) \backslash G(F)} \Phi_f(\gamma g)$ converges, and it equals the average of $\theta(g, \cdot\,; f)$ over $[U(B)]$.

Lean: `UpperTheory.Lit.Sw47.weilUnitary`

*Proof.* Absolute convergence of theta integrals under the rank condition follows from reduction theory: Siegel sets for $U(B)$ and the decay of Schwartz functions. A bound of the theta integral by a continuous seminorm gives part 1, and integrability of the kernel on the range of the Weil representation gives part 2. Part 3 is the [Weil-Siegel formula](/entry/weil-siegel-formula/) in the Schwartz model, transported to theta functions. $\square$

This is Weil's form of the [Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula) for $(U(n, n), U(B))$ in the convergent range. Its users are the bundles [of eigen results](/step/published-results-eigen/) and [of first results](/step/published-results-first/) of the literature step.

### Prismatic Dieudonné theory

Let $C$ be an algebraically closed field of characteristic $0$ with a valuation, whose [[valuation ring|QSX12D8RQM]] $\mathcal{O}$ is $p$-adically complete with $p$ not a unit. Let $A_{\inf} = W(\mathcal{O}^\flat)$ be the ring of [[Witt vectors|6N3X2QX4W9]] with Frobenius $\varphi$ and Fontaine's map $\theta \colon A_{\inf} \to \mathcal{O}$ (see [[Fontaine's period rings|K6HW8YWCQJ]]), and let $\xi$ be the generator of $\ker \theta$ attached to a compatible system $\varepsilon$ of $p$-power roots of unity.

**Theorem 2.8.5 (Prismatic Dieudonné modules with Hodge filtration).** There are contravariant functors $M$ to $A_{\inf}$-modules and $D$ to $\mathcal{O}$-modules on $p$-divisible groups $G$ over $\mathcal{O}$, with a $\varphi$-semilinear $\varphi_G$ on $M(G)$, a $\theta$-semilinear $r_G \colon M(G) \to D(G)$ and maps $\omega_G \to D(G) \to \operatorname{Lie}(G^\vee)$, such that:

1. $M$ is additive and $M(G)$ is free of rank the height of $G$;
2. $\varphi(\xi) M(G) \subseteq \varphi_G(M(G))$;
3. $r_G$ is onto with kernel $\xi M(G)$;
4. $0 \to \omega_G \to D(G) \to \operatorname{Lie}(G^\vee) \to 0$ is exact;
5. $M(\mathbb{Q}_p/\mathbb{Z}_p) \cong A_{\inf}$ with $\varphi_G = \varphi$, and $M(\mu_{p^\infty}) \cong A_{\inf}$ with $\varphi_G = \varphi(\xi) \varphi$;
6. every Frobenius-compatible $A_{\inf}$-linear map $M(\mu_{p^\infty}) \to M(\mathbb{Q}_p/\mathbb{Z}_p)$ is $M(f)$ for exactly one $f \colon \mathbb{Q}_p/\mathbb{Z}_p \to \mu_{p^\infty}$.

Lean: `UpperTheory.Lit.prismaticDieudonneHodge`

*Proof.* The hypothesis on $\varepsilon$ makes each untilted root a primitive $p^n$-th root of unity, and this gives a frame over $\mathcal{O}$. For $G$ connected with connected dual, the [window matrices](/entry/window-matrices/) give matrices for $T_p G$, $\omega_G$ and $\operatorname{Lie}(G^\vee)$ satisfying Frobenius relations; these lift to $A_{\inf}$ and give a datum for $G$. The datum extends from such $G$ to all $p$-divisible groups, and the functors and maps are built from the data. $\square$

This is the prismatic Dieudonné theory of Anschütz and Le Bras over $\mathcal{O}_C$, in the case of $A_{\inf}$. Its user is the volume branch of the literature step.

### Local Bloch-Kato

**Theorem 2.8.6 (Local Bloch-Kato).** Let $l$ be a prime with its local data and $K$ a finite extension of $\mathbb{Q}_l$. For continuous de Rham representations $V$ of $G_K$:

1. $H^1_f(K, V)$ is finite-dimensional, with
$$\dim H^1_f = \dim H^0 + \dim D_{\mathrm{dR}}(V) - \dim \operatorname{Fil}^0 D_{\mathrm{dR}}(V);$$
2. for $V'$ dual to $V$ with values in $\mathbb{Q}_l(1)$, a cocycle lies in $H^1_f(V)$ exactly when its cup product with every class of $H^1_f(V')$ is a coboundary, and symmetrically;
3. the analogous statement holds for lattices $L \subset V$ and $L' \subset V'$, with divisible classes on one side and integral coboundaries.

Lean: `UpperTheory.Lit.blochKatoLocal`

*Proof.* Local Tate duality and the local Euler characteristic formula give the pairing forms and a bound on $\dim H^1_f$, and the comparison with $D_{\mathrm{dR}}$ gives the exact dimension. The rational and integral dualities follow from their versions for all coefficient rings. The dimension formula is the de Rham computation of $H^1_f$. $\square$

These are Bloch and Kato's local results on $H^1_f$, built on [[Galois cohomology|9MPCZ3EAJM]]. Its user is the row step.

### Theta lifts for general linear groups

**Theorem 2.8.7 (Theta lift for $GL$ from irreducibility).** Let $k$ be a non-archimedean local field, $r < t$, $\mu$ a smooth unitary character of $k^\times$, $\sigma$ a unitarizable representation of $GL_r(k)$ and $\pi$ a smooth irreducible representation of $GL_{r+t}(k)$. Suppose the parabolically induced representation $\sigma \times (\mu \circ \det_t)$ is irreducible and that there is a nonzero bilinear map $B$ from Schwartz functions on $M_{(r+t) \times r}(k)$ and $\pi$ to $\sigma$, equivariant for the twisted Weil representation $\omega_\mu$. Then $\pi \cong \sigma \times (\mu \circ \det_t)$.

Lean: `UpperTheory.Lit.HoweDuality.lift_of_irr`

*Proof.* Call $B$ *$j$-small* if it kills every Schwartz function that vanishes on the matrices of rank less than $j$; being $0$-small means $B = 0$. A step lemma on the orbits of $GL_r(k) \times GL_{r+t}(k)$ shows that for $j < r$, a $(j + 1)$-small $B$ is $j$-small, so by descending induction an $r$-small $B$ is zero. The germs of $B$ on the open set of matrices of full rank are unique and give an evaluation functional $e$; if $e = 0$ then $B$ is $r$-small, hence zero, which is excluded. So $e \neq 0$, and Frobenius reciprocity turns it into a nonzero intertwining map from $\pi$ to $\sigma \times (\mu \circ \det_t)$. Both are irreducible, so the map is an isomorphism. $\square$

This is the explicit Howe correspondence for type II pairs of Mínguez. Its user is the [theta lift for $GL$](/entry/theta-lift-gl-of-zelevinsky-classification/).

**Remark 2.8.8 (Formalization).** The Bessel theorems are in [RankLeOneOfDep.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/BesselModels/RankLeOneOfDep.lean#L177) and [Separate.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/BesselModels/Separate.lean#L32); the real input is in [RealBranch.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/FockModels/RealBranch.lean#L231); Siegel-Weil is in [FockAnisoFree.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/FockModels/FockAnisoFree.lean#L12), where `fockAniso_free` at L17 takes a hypothesis it does not use; the prismatic theorem is in [PrismaticDieudonneHodge.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/PrismaticDieudonne/PrismaticDieudonneHodge.lean#L19); Bloch-Kato is a second name for the proof in [BlochKatoLocal.lean](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/BlochKatoLocal.lean#L287); the $GL$ theorem is in [MingZel.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/FockModels/MingZel.lean#L17). In the prismatic theorem, clause 6 is full faithfulness for one pair of objects only. The Siegel-Weil theorem is stated for the CM field of a fixed datum, not for an arbitrary CM extension.

## Notes and references

This chapter feeds the [theta matching chapter](/proof/theta-matching/) through the theta integrals and local matching of the sixth section, the [Bessel seesaw chapter](/proof/bessel-seesaw/) through unramified Howe duality and the real inputs, the [unitary hypotheses chapter](/proof/unitary-hypotheses/) through the lifts of the seventh section, and the [literature steps](/proof/literature/) through the remaining results.

The lattice model and the unramified correspondence go back to R. Howe, *θ-series and invariant theory*, Proc. Sympos. Pure Math. 33, Part 1 (1979), 275 to 285, and *Transcending classical invariant theory*, J. Amer. Math. Soc. 2 (1989), 535 to 552; and to S. Rallis, *Langlands' functoriality and the Weil representation*, Amer. J. Math. 104 (1982), 469 to 515. For integral Hermitian lattices see O. T. O'Meara, *Introduction to Quadratic Forms*, Chapter IV, §42. The Weil representation and the Siegel-Weil formula are from A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964), 143 to 211, and *Sur la formule de Siegel dans la théorie des groupes classiques*, Acta Math. 113 (1965), 1 to 87. Splittings over unitary groups are in S. Kudla, *Splitting metaplectic covers of dual reductive pairs*, Israel J. Math. 87 (1994), 361 to 401, and M. Harris, S. Kudla and W. J. Sweet, *Theta dichotomy for unitary groups*, J. Amer. Math. Soc. 9 (1996), 941 to 1004. The Fock model and its $K$-types are in M. Kashiwara and M. Vergne, *On the Segal-Shale-Weil representations and harmonic polynomials*, Invent. Math. 44 (1978), 1 to 47. The doubling integrals are in S. Gelbart, I. Piatetski-Shapiro and S. Rallis, *Explicit Constructions of Automorphic L-Functions*, Lecture Notes in Math. 1254 (1987), Part A. The inner product formula is from S. Rallis, *Injectivity properties of liftings associated to Weil representations*, Compositio Math. 52 (1984), 139 to 169. Multiplicity one for Bessel models is in A. Aizenbud, D. Gourevitch, S. Rallis and G. Schiffmann, *Multiplicity one theorems*, Ann. of Math. 172 (2010), 1407 to 1434, and B. Sun and C.-B. Zhu, *Multiplicity one theorems: the Archimedean case*, Ann. of Math. 175 (2012), 23 to 44. The type II correspondence is A. Mínguez, *Correspondance de Howe explicite: paires duales de type II*, Ann. Sci. Éc. Norm. Supér. 41 (2008), 717 to 741. Prismatic Dieudonné theory is J. Anschütz and A.-C. Le Bras, *Prismatic Dieudonné theory*, Forum Math. Pi 11 (2023), e2. The local Bloch-Kato results are in S. Bloch and K. Kato, *L-functions and Tamagawa numbers of motives*, in *The Grothendieck Festschrift*, Vol. I, Progr. Math. 86 (1990), 333 to 400, Section 3.
