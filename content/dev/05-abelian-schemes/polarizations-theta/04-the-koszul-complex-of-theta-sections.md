---
title: The Koszul complex of theta sections
decls:
  - GlobalTheory.koszul_sections_exact_field
  - GlobalTheory.T.koszul_sections_exact_algClosed_polarisedAV
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Koszul complex of theta sections

The rest of the chapter builds an invariant of a principally polarized abelian scheme with a theta section and a basis of tangent vectors: the *key invariant*. It is a unit $\kappa$ made from the torsion of a Koszul complex of sections of powers of the theta bundle, normalized by theta functions. This section sets up the objects and proves the exactness theorem that makes the Koszul complex acyclic: if $g$ sections of $L^n$ on an abelian variety of dimension $g$ over an algebraically closed field have finitely many common zeros, then the Koszul complex of global sections of $L^{l - jn}$ is exact for $l > gn$. The theorem is used in [the key invariant theorem](/entry/ka-st/) to show that the torsion is defined. The background is [coherent cohomology](/learn/commutative-algebra/#coherent-cohomology) and [polarizations and Zarhin's trick](/learn/abelian-varieties/#polarizations-and-zarhins-trick).

**Definition 2.4.1 (The laws of abelian schemes).** All theorems from here to the end of the chapter assume a fixed list of twenty-four facts about abelian schemes and their line bundles. Among them are the rank of the space of global sections over an algebraically closed field, base change for sections, the theorem of the cube, the theorem of the square, rigidity, the Weil pairing and its nondegeneracy, Serre vanishing, and the existence of extensions and quotients. We call them *the laws* and state each theorem with the laws as an assumption.

Lean: `ReciprocityTheory.ChartRestriction.G.Out.Laws`.

**Definition 2.4.2 (Key input).** Let $R$ be a commutative ring. A *key input* $x$ over $R$ consists of the following data.

1. A principally polarized abelian scheme $(A, L)$ over $\operatorname{Spec} R$ of relative dimension $g \geq 1$, as defined in the section on Zarhin's trick: $L$ is rigidified, symmetric, relatively ample and $K(L)$ is trivial.
2. A generator $r$ of $e^{*}L$, where $e$ is the zero section.
3. A section $\theta \in \Gamma(A, L)$ that does not vanish identically on any fibre.
4. Tangent vectors $v_1, \dots, v_g$ at the origin, that is, morphisms $\operatorname{Spec} R[\varepsilon] \to A$ that reduce to $e$ modulo $\varepsilon$, which form a basis of the Lie algebra: every tangent vector is $\sum_k c_k v_k$ for a unique $c \in R^g$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.KeyIn`.

The data $(A, L, \theta)$ is a theta characteristic in algebraic form: over $\mathbb{C}$, $\theta$ is a theta function with characteristics, and the $v_k$ fix the coordinates of the universal cover. A ring map $f : R \to R'$ moves key inputs.

**Definition 2.4.3 (Pullback of key inputs).** Let $f : R \to R'$ be a ring map, $x$ a key input over $R$ and $x'$ one over $R'$. A *pullback* of $x$ to $x'$ along $f$ is a morphism $\varphi : A' \to A$ over $\operatorname{Spec} f$ that identifies $A'$ with the base change of $A$ as a group, with an isomorphism $w : L' \cong \varphi^{*}L$, such that the dimensions agree, $w$ carries $r$ to $r'$ and $\theta$ to $\theta'$, and $\varphi \circ v'_k = v_k \circ \operatorname{Spec}(F)$ for the ring map $F : R[\varepsilon] \to R'[\varepsilon]$ that extends $f$ with $F(\varepsilon) = \varepsilon$. A section $s' \in \Gamma(A', L'^{\,l})$ is the *pullback* of $s \in \Gamma(A, L^l)$ if $\varphi^{*}s = w^{l}(s')$.

Lean: `GlobalTheory.KeyKa.KeyVia`, `GlobalTheory.KeyKa.SecVia`.

Fix a key input $x$ over $R$. For $l \geq 0$ write $\Gamma_l = \Gamma(A, L^l)$. A family $b_1, \dots, b_N$ in $\Gamma_l$ is a *basis* if every section is $\sum_k c_k b_k$ for a unique $c \in R^N$. Over a field, $\Gamma_l$ has dimension $l^g$, since $L$ is principal. Let $n \geq 1$ and let $s_1, \dots, s_g \in \Gamma_n$. We say that $s$ has *finite zeros* if the set of points of $A$ where all $s_i$ vanish is finite.

**Definition 2.4.4 (Koszul matrix).** Let $l > gn$ and, for $0 \leq j \leq g$, let $b_j$ be a basis of $\Gamma_{l - jn}$, with $(l - jn)^g$ elements. Let $m_i(j, j + 1)$ be the matrix of multiplication by $s_i$ from $\Gamma_{l - (j+1)n}$ to $\Gamma_{l - jn}$ in these bases. Let $z_1, \dots, z_d$ be points of $A$ with values in $R$, each with a chart on which $L$ is trivial. The *Koszul matrix* $D$ acts on the free module
$$C = \bigoplus_{I \subseteq \{1, \dots, g\}} R^{(l - |I| n)^g} \;\oplus\; R^d,$$
graded by $|I| + 1$ on the summand of $I$ and by $0$ on $R^d$. Its block from the summand of $I \cup \{i\}$ (with $i \notin I$) to the summand of $I$ is $(-1)^{\#\{j \in I : j < i\}}\, m_i(|I|, |I| + 1)$. Its block from the summand of $\emptyset$ to $R^d$ is the evaluation matrix $(b_{0,k}(z_a))_{a, k}$ in the charts. All other blocks are $0$.

Lean: `GlobalTheory.KeyKa.kosD`, `GlobalTheory.KeyKa.IsMul`, `GlobalTheory.KeyKa.IsBasis`, `GlobalTheory.KeyKa.FinZ`.

So $D$ is the Koszul complex of $s_1, \dots, s_g$ on the twisted section spaces, augmented by evaluation at the points $z_a$:
$$0 \to \bigoplus_{|I| = g} \Gamma_{l - gn} \to \cdots \to \bigoplus_{|I| = 1} \Gamma_{l - n} \to \Gamma_l \to R^d \to 0.$$
The signs are the usual Koszul signs, so $D^2 = 0$. With $d = 0$ it is the plain Koszul complex of global sections.

**Theorem 2.4.5 (Koszul exactness).** Assume the laws. Let $K$ be an algebraically closed field and $x$ a key input over $K$ of dimension $g$. Let $n \geq 1$ and $l > gn$. Let $s_1, \dots, s_g \in \Gamma_n$ have finite zeros. Let $b_j$ be a basis of $\Gamma_{l - jn}$ for $j \leq g$, and let $m$ be the matrices of multiplication by the $s_i$ in these bases. For each point $y$ of $A$ fix a chart containing $y$ on which $L$ is trivial, and identify sections near $y$ with elements of the local ring $\mathcal{O}_{A, y}$. Then:

1. The plain Koszul complex is exact at every term with $I \neq \emptyset$: if $D v = 0$, then there is $w$ with $v_I = (D w)_I$ for every $I \neq \emptyset$.
2. For every family $(a_y)$ of elements $a_y \in \mathcal{O}_{A, y}$, there is $\sigma \in \Gamma_l$ such that $\sigma - a_y$ lies in the ideal $(s_1, \dots, s_g)$ of $\mathcal{O}_{A, y}$ at every common zero $y$ of the $s_i$.
3. If $\sigma \in \Gamma_l$ lies in the ideal $(s_1, \dots, s_g)$ of $\mathcal{O}_{A, y}$ at every common zero $y$, then $\sigma = \sum_i s_i t_i$ with $t_i \in \Gamma_{l - n}$.

Lean: `GlobalTheory.koszul_sections_exact_field` (also `GlobalTheory.T.koszul_sections_exact_algClosed_polarisedAV`, a second name).

*Proof.* Let $Z \subset A$ be the closed subscheme defined by $s_1, \dots, s_g$. It is finite. The local rings of $A$ are regular of dimension $g$, hence Cohen-Macaulay, and at a point of $Z$ the $g$ elements $s_i$ generate an ideal of height $g$. So they form a regular sequence in each local ring of a point of $Z$, and they generate the unit ideal at the other points (H. Matsumura, *Commutative Ring Theory*, Theorem 17.4). Hence the sheaf Koszul complex
$$0 \to \bigoplus_{|I| = g} L^{l - gn} \to \cdots \to \bigoplus_{|I| = 1} L^{l - n} \to L^{l} \to L^{l}|_Z \to 0$$
is exact. Every term other than the last is a sum of copies of $L^{k}$ with $k = l - jn \geq l - gn > 0$, and $H^{q}(A, L^{k}) = 0$ for $q > 0$ and $k > 0$, since $L^k$ is ample (D. Mumford, *Abelian Varieties*, §16). Cut the complex into short exact sequences. The long exact sequences of cohomology, together with the vanishing, show by descending induction on $j$ that the kernels have no higher cohomology and that the complex of global sections is exact at each $j \geq 1$. This is part 1, once the terms are written in the bases $b_j$. In degree $0$ the same argument shows that $\Gamma(A, L^l) \to \Gamma(Z, L^l|_Z)$ is surjective, with kernel the image of $\bigoplus_i \Gamma_{l - n}$. Since $Z$ is finite, $\Gamma(Z, L^l|_Z)$ is the product over $y \in Z$ of $\mathcal{O}_{A, y}/(s_1, \dots, s_g)$ in the fixed charts. Surjectivity is part 2, and the description of the kernel is part 3. $\square$

The theorem has no assumption on the characteristic of $K$. Part 2 with $d$ points gives exactness of the augmented complex at $\Gamma_l$ whenever evaluation at the $z_a$ is the map to $\Gamma(Z, L^l|_Z)$, that is, when $Z$ is reduced and consists of the $z_a$. Then the whole augmented complex is acyclic.

**Definition 2.4.6 (Torsion of a based complex).** Let $C$ be a finite free $R$-module with a basis indexed by a set graded by degree, and $D$ a matrix of degree $-1$ with $D^2 = 0$. A *contraction* is a matrix $h$ of degree $+1$ with $Dh + hD = 1$. If $h$ exists, the restriction of $D + h$ from the even part to the odd part is an isomorphism, and for a bijection $e$ between the basis vectors of even and odd degree we let $t = \det\bigl((D + h)_{\text{even}, e(\text{even})}\bigr)^2$. We say that $t$ is the *square torsion* of $(C, D)$.

Lean: `GlobalTheory.KeyKa.TorsSq`, `GlobalTheory.KeyKa.IsCx`.

The square removes the sign that depends on $e$. The square torsion also does not depend on $h$, so it is an invariant of the based acyclic complex; this uniqueness is used in the later sections. It is the square of the torsion of Milnor and of the determinant of Knudsen and Mumford, computed in the given bases.

**Definition 2.4.7 (Transversal zeros and the Jacobian).** For $s_1, \dots, s_g \in \Gamma_n$, a point $z$ of $A$ with values in $R$ and a chart, the *Jacobian* $\operatorname{jac}(s, z)$ is $\det\bigl(\partial_{v_k} s_i(z)\bigr)_{i, k}$, where $\partial_{v_k} s_i(z)$ is the $\varepsilon$-coefficient of $s_i$ at the point $z + \varepsilon v_k$ in the chart. Points $z_1, \dots, z_d$ are *transversal zeros* of $s$ if each $z_a$ lies in its chart, all $s_i(z_a) = 0$, each $\operatorname{jac}(s, z_a)$ is a unit, the $z_a$ are pairwise distinct on every fibre, and every common zero of the $s_i$ lies on some $z_a$.

Lean: `GlobalTheory.KeyKa.EtZ`, `GlobalTheory.KeyKa.jac`.

**Definition 2.4.8 (Theta comparison).** Let $m \geq 1$ and let $\alpha$ be a $4 \times 4$ integer matrix with $\alpha^{T}\alpha = m$. Let $b$ be a basis of $\Gamma_m$, indexed by a set of size $m^g$. A *theta comparison* of $b$ with constant $\lambda \in R^{\times}$ consists of: points $\xi_{I, r}$ ($r = 1, \dots, 4$) for each index $I$ in the fourth power of the index set, distinct for distinct $I$ on every fibre and with $\sum_r \alpha_{rc}\xi_{I,r} = 0$ for each $c$; a generator $\mu$ of $[m]^{*}L \otimes L^{-m^2}$; for each $I$ a generator $w_I$ of $\bigotimes_r \alpha_r^{*}L \otimes \bigotimes_c \operatorname{pr}_c^{*} L^{-m}$ on $A^4$, where $\alpha_r(y) = \sum_c \alpha_{rc} y_c + \xi_{I, r}$; a matrix $Q$ and units $\rho_I$; such that $\mu$ and $w_I$ are normalized against $r$ with the constants $\rho_I$ along the zero section, and
$$\prod_{r} \theta\bigl(\alpha_r(y)\bigr) = w_I(y) \sum_{I'} Q_{I I'} \prod_{c} b_{I'_c}(y_c).$$
Then $\lambda = \det(Q)^{2m^2} \prod_I \rho_I^{2}$.

Lean: `GlobalTheory.KeyKa.IsSquareDeterminantComparison`.

This is the algebraic form of the addition formula of theta functions: the isogeny $\alpha$ of $A^4$ pulls $L^{\boxtimes 4}$ back to $(L^m)^{\boxtimes 4}$, so the translated products of $\theta$ expand in the product basis, and $\lambda$ measures $b$ against $\theta$.

**Definition 2.4.9 (Admissible data and the key value).** Data $(n, l, l', \alpha)$ is *admissible* for $g$ if $n \geq 4$, $gn < l < l'$ and $\alpha(m)^{T}\alpha(m) = m$ for every $m$. Put $P = \prod_{j = 0}^{g} (l - jn)(l' - jn)$ and
$$t_{\mathrm{c}}(l, t, \lambda) = t^{4P^{3g+2}} \prod_{j = 0}^{g} \lambda_j^{(-1)^j \binom{g}{j} (P/(l - jn))^{3g+2}}.$$
A unit $\kappa$ is a *key value* of $s_1, \dots, s_g \in \Gamma_n$ if there are $d = g!\, n^g$ transversal zeros $z_a$ with charts, bases $b_j$ of $\Gamma_{l - jn}$ and $b'_j$ of $\Gamma_{l' - jn}$ with theta comparisons of constants $\lambda_j$ and $\lambda'_j$ (for $\alpha(l - jn)$ and $\alpha(l' - jn)$), such that $t$ and $t'$ are the square torsions of the augmented Koszul complexes at levels $l$ and $l'$, $J = \prod_a \operatorname{jac}(s, z_a)$, and
$$\kappa = t_{\mathrm{c}}(l, t, \lambda)^{gn - 2l'}\; t_{\mathrm{c}}(l', t', \lambda')^{2l - gn}\; J^{8P^{3g+2}(l' - l)}.$$

Lean: `GlobalTheory.KeyKa.admitted`, `GlobalTheory.KeyKa.KaVal`, `GlobalTheory.KeyKa.kaForm`, `GlobalTheory.KeyKa.degProd`.

The number $g!\, n^g$ is the self-intersection $(nL)^g$, the expected number of common zeros. The exponents are chosen so that changes of the bases and of $\theta$ cancel; that the result does not depend on the sections either is the theorem of [the section on independence](/entry/key-invariant-independent-of-sections/).

**Remark 2.4.10 (Formalization).** The second name of the theorem is proved by a `first | exact … | …` tactic block whose later alternatives are never reached ([KoszulSectionsExactAlgClosedPolarisedAVStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/KoszulSectionsExactAlgClosedPolarisedAVStatement.lean#L20)). The laws are a structure of twenty-four unproved statements ([GlobalSectionsRankAlgClosed.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/GlobalSectionsRankAlgClosed.lean#L187)). The Lean proof cuts the complex with a regularity lemma on affine charts and a Čech exactness lemma for $L^l$ ([KoszulSectionsExactAlgClosedPolarisedAV.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/KoszulSectionsExactAlgClosedPolarisedAV.lean#L403)); the proof above gives the same argument in sheaf language. In the theta comparison, the normalization against $r$ uses values of generators on trivializing charts (`Good`, `val`), which we did not unfold. Part 1 is stated for all cycles of the total complex and concludes only on the components with $I \neq \emptyset$.
