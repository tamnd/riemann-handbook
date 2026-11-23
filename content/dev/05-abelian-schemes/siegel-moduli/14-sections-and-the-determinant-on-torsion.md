---
title: Sections and the determinant on torsion
decls:
  - GlobalTheory.SectionCount.sq_vol_eq_det
  - GlobalTheory.T.sections_count_sq_eq_det_form_on_torsion
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Sections and the determinant on torsion

Let $A$ be a principally polarized abelian variety over an algebraically closed field and $M$ a symmetric ample line bundle on $A$. This section proves that the number of sections of $M$ is a natural number $\delta$ with $h^0(M^e) = \delta e^g$ for all $e \ge 1$, and that $\delta^2$ is the determinant of the endomorphism of $A$ that $M$ defines, read on the $l^j$ torsion points. It is the Riemann-Roch theorem for abelian varieties in the form $\chi(M)^2 = \deg \varphi_M$, with the degree computed on the Tate module. The result is used later to compute the Hilbert functions of graphs of endomorphisms and of sums with a principal polarization, where sections are counted through torsion. The background is [abelian varieties over a field](/learn/abelian-varieties/#abelian-varieties-over-a-field) and [the theorem of the cube](/learn/abelian-varieties/#the-theorem-of-the-cube).

We recall the classical statement.

**Theorem 5.14.1 (Riemann-Roch for abelian varieties).** Let $X$ be an abelian variety of dimension $g$ over an algebraically closed field and $L$ a line bundle on $X$. Then $\chi(L) = (L^g)/g!$, $\chi(L)^2 = \deg \varphi_L$, where $\varphi_L : X \to \hat X$ is the map $x \mapsto t_x^* L \otimes L^{-1}$, and if $L$ is ample then $H^i(X, L) = 0$ for $i > 0$, so $h^0(L) = \chi(L)$ (D. Mumford, *Abelian Varieties*, §16).

For an endomorphism $f$ of $X$ and a prime $l$ different from the characteristic, $\deg f = \det(T_l f)$ (D. Mumford, *Abelian Varieties*, §19). The theorem below combines these two facts for the bundle $M$, with the principal polarization used to turn $\varphi_M$ into an endomorphism of $A$.

Fix an algebraically closed field $K$ and a principally polarized abelian variety $P$ over $K$ with abelian variety $A$ of dimension $g$ and principal polarization bundle $L$. For a line bundle $N$ on $A$ and points $x_1, \dots, x_n$ of $A$, write $\Lambda(x_1, \dots, x_n; N)$ for the bundle $\bigotimes_{I} (\sum_{i \in I} x_i)^* N^{(-1)^{n - |I|}}$, where $I$ runs over the subsets of $\{1, \dots, n\}$. So $\Lambda(x, y; N) = (x+y)^* N \otimes x^* N^{-1} \otimes y^* N^{-1} \otimes 0^* N$, and $\Lambda(N) = \Lambda(\mathrm{pr}_1, \mathrm{pr}_2; N)$ is the Mumford bundle on $A \times A$.

**Definition 5.14.2 (Sections, volume, torsion bases).** Let $N$ be a line bundle on $A$.

1. $N$ *has $r$ sections* if there are sections $s_1, \dots, s_r$ of $N$ such that every section is $\sum_i a_i s_i$ for exactly one $(a_1, \dots, a_r) \in K^r$.
2. $N$ *has volume* $\delta \in \mathbb{R}$ if there is $h : \mathbb{N} \to \mathbb{N}$ such that $N^e$ has $h(e)$ sections for every $e$, and $h(e)/e^g \to \delta$.
3. Points $x_1, \dots, x_m$ of $A$ form a *torsion basis* for $k$ if $k > 0$, $k x_i = 0$ for all $i$, and every point $y$ with $k y = 0$ is $\sum_i c_i x_i$ for exactly one $c \in (\mathbb{Z}/k)^m$.
4. An endomorphism $s$ *acts by* a matrix $\mathrm{Mat} \in M_m(\mathbb{Z}/k)$ on $x_1, \dots, x_m$ if $k > 0$ and $s(x_i) = \sum_{i'} \mathrm{Mat}_{i' i} \, x_{i'}$ for all $i$.
5. $s$ is the *form* of $M$ if $s$ is a homomorphism and $\Lambda(M) \cong (1 \times s)^* \Lambda(L)$ on $A \times A$, that is, $\Lambda(M) \cong \Lambda(\mathrm{pr}_1, s \circ \mathrm{pr}_2; L)$.
6. $M$ is *symmetric* if $M \cong (-1)^* M$.

Lean: `SectionsHaveFiniteDimension`, `Vol`, `TorsBasis`, `ActsBy`, `FormIs`, `SymB`.

The form condition says $\varphi_M = \varphi_L \circ s$. Since $\varphi_L$ is an isomorphism, $s = \varphi_L^{-1} \circ \varphi_M$, so $\deg s = \deg \varphi_M$.

**Theorem 5.14.3 (Square of the number of sections).** Assume the laws and the second laws of abelian schemes. Let $K$ be an algebraically closed field, $P$ a principally polarized abelian variety over $K$ of dimension $g$, $M$ a line bundle on $A$, $s$ an endomorphism of $A$ and $l$ a prime with $l \ne 0$ in $K$. Assume that $M$ is relatively ample and symmetric and that $s$ is the form of $M$. Then there is $\delta \in \mathbb{N}$ such that:

1. $M$ has volume $\delta$;
2. $M^e$ has $\delta e^g$ sections for every $e \ge 1$;
3. for every $j$, every torsion basis $x_1, \dots, x_{2g}$ for $l^j$ and every matrix $\mathrm{Mat} \in M_{2g}(\mathbb{Z}/l^j)$ by which $s$ acts on it, $\delta^2 = \det \mathrm{Mat}$ in $\mathbb{Z}/l^j$.

Lean: `GlobalTheory.SectionCount.sq_vol_eq_det` (also `GlobalTheory.T.sections_count_sq_eq_det_form_on_torsion`, a second name).

*Proof.* *The number of sections.* A lemma on symmetric ample bundles gives $\delta \in \mathbb{N}$ with $\delta \ge 1$, such that $M$ has volume $\delta$ and $M^e$ has $\delta e^g$ sections for all $e \ge 1$. This gives parts 1 and 2. It remains to prove part 3.

*Polynomials in $s$.* For a [[polynomial|0SDC934R52]] $F \in \mathbb{Z}[X]$ write $F(s)$ for the endomorphism of $A$ obtained by substituting $s$, so that $1(s) = 1$, $(F + G)(s) = F(s) + G(s)$ and $(XF)(s) = F(s) \circ s$. Put $N_F = \Lambda(1, F(s); L)$, a line bundle on $A$. A lemma on the form gives isomorphisms
$$\begin{aligned} N_1 &\cong L^2, \\ N_X &\cong M^2, \\ N_{G^2 F} &\cong G(s)^* N_F \end{aligned}$$
for all $F$ and $G$. The second one uses that $M$ is symmetric.

*The volume polynomial.* A lemma on volumes gives a function $D : \mathbb{Z}[X] \to \mathbb{Q}$ with three properties. First, in the coefficients of $F$ it is a homogeneous polynomial of degree $g$ with rational coefficients. Second, if $N_F$ is ample, then $N_F$ has volume $D(F)$. Third, for every $F$ and every large integer $t$, the bundle $N_{F + t}$ is ample and $(F + t)(s)$ is [[finite|N9C4X7XKE4]].

*The matrix on the Tate module.* A lemma on Tate modules gives a matrix $U \in M_{2g}(\mathbb{Z}_l)$, the matrix of $s$ on $T_l A$. If the kernel of $F(s)$ is finite, then $|\det F(U)|_l$ is the $l$-adic absolute value of the number of points in that kernel. If $F(U) = 0$, then $F(s) = 0$. And for every torsion basis for $l^j$ on which $s$ acts by $\mathrm{Mat}$, the reduction of $\det U$ modulo $l^j$ is $\det \mathrm{Mat}$.

*Two values of $D$.* A lemma on principal polarizations gives that $L$ has volume $1$, so $L^2$ has volume $2^g$. Since $N_1 \cong L^2$, we get $D(1) = 2^g$. In the same way $N_X \cong M^2$ has volume $2^g \delta$, so $D(X) = 2^g \delta$.

*Pullback by finite maps.* Let $G(s)$ be finite of degree $d$ and $N_F$ ample. Then $N_{G^2 F} \cong G(s)^* N_F$ is ample, and a lemma on pullbacks gives that its volume is $d$ times the volume of $N_F$. So $D(G^2 F) = d \, D(F)$. A lemma on degrees gives $d = p^a \cdot \# \ker G(s)$, where $p$ is the characteristic exponent of $K$. Since $l \ne p$, $|p^a|_l = 1$.

*A norm.* Put $\mathcal{N}(G) = D(G^2)/2^g$. Then $\mathcal{N}(1) = 1$, and $\mathcal{N}$ is a homogeneous polynomial of degree $2g$ in the coefficients. If $F(s)$ and $G(s)$ are finite, the previous step applied three times gives
$$\begin{aligned} D\big((FG)^2\big) = \deg F(s) \cdot \deg G(s) \cdot D(1), \end{aligned}$$
so $\mathcal{N}(FG) = \mathcal{N}(F) \mathcal{N}(G)$, and $|\mathcal{N}(F)|_l = |\# \ker F(s)|_l = |\det F(U)|_l$. Also $(F + t)(s)$ is finite for large $t$. A lemma on polynomial norms states: a homogeneous polynomial function of degree $2g$ with value $1$ at $1$, multiplicative on a set of polynomials that contains $F + t$ for large $t$, whose $l$-adic absolute value agrees there with that of $\det F(U)$, is equal to $\det F(U)$ in $\mathbb{Q}_l$. So $\mathcal{N}(G) = \det G(U)$ for every $G$.

*The square root.* If $H(U) = 0$, then $H(s) = 0$, so $N_{F + H} = N_F$ and $D(F + H) = D(F)$. A lemma on square roots of norms now applies to $D/2^g$: a homogeneous polynomial function of degree $g$ whose values at squares are $\det G(U)$, and which only depends on $F$ through $F(U)$, satisfies $(D(F)/2^g)^2 = \det F(U)$ for every $F$. With $F = X$ we get $\delta^2 = \det U$ in $\mathbb{Z}_l$.

*Reduction.* Let $x_1, \dots, x_{2g}$ be a torsion basis for $l^j$ on which $s$ acts by $\mathrm{Mat}$. The reduction of $\det U$ modulo $l^j$ is $\det \mathrm{Mat}$, so $\delta^2 = \det \mathrm{Mat}$ in $\mathbb{Z}/l^j$. $\square$

**Remark 5.14.4.** For $j = 0$ the ring $\mathbb{Z}/l^0$ is the zero ring and part 3 says nothing. For $j \ge 1$ part 3 determines $\delta^2$ modulo every power of $l$, so it determines the integer $\delta^2$ and with it the natural number $\delta$. The proof does not use $\chi(L) = (L^g)/g!$ or the vanishing theorem directly. It replaces them by the growth of sections, the volume function $D$ and the comparison of degrees with $l$-adic determinants.

**Remark 5.14.5 (Formalization).** The lemma on symmetric ample bundles, `GlobalTheory.sectionsDim_symmetricAmple_pow_eq_mul_pow`, also gives $1 \le \delta$, but this part is discarded with `-` ([SectionsCountSqEqDetFormOnTorsion.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/SectionsCountSqEqDetFormOnTorsion.lean#L210)), so the theorem does not state $\delta \ge 1$. The other lemmas are `GlobalTheory.T.polarisationForm_intPolynomial_bundles`, `GlobalTheory.VolPoly.exists_vol_poly`, the local `exists_matrix` at line 161, `GlobalTheory.T.principalPolarisation_volume_form_symmetric_ample`, `GlobalTheory.T.sectionsPowerGrowthVolume_pull_finite_endomorphism`, `GlobalTheory.T.mapDegree_eq_expChar_pow_mul_card_kernel`, `GlobalTheory.PolyNorm.eq_det` and `GlobalTheory.sq_eq_det_aeval_of_sq`. In the code the group law on endomorphisms is written multiplicatively, so $F(s) + G(s)$ is `ev F * ev G` and $F(s) = 0$ is `ev F = 1`. The degree of a finite map is `MapDeg`, the rank of the pushforward over every nonempty affine open. The second name is a wrapper proved by `first | exact @...` under `maxHeartbeats 1000000`.
