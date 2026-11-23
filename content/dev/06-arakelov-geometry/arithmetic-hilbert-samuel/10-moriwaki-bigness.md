---
title: Moriwaki bigness
decls:
  - GroundTheory.Heights₂.Heights.HilbertSamuel.SectionNormSqExtension.proof
  - PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsChain
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Moriwaki bigness

A hermitian line bundle $\bar A$ is big if its arithmetic volume is positive. By results of Yuan and Moriwaki, the volume of a bundle that is semipositive and nef on the fibres is at least its self intersection, so such a bundle with $\bar A^{D+1} > 0$ is big. This section proves this inequality in the coordinates of [the previous section](/entry/theorem-hsmblock/). With it come four more bounds on counts of small sections: the case of curves, the arithmetic Kleiman inequality, and two upper bounds of Hilbert-Samuel type. These five bounds give the statements on bigness and on Hilbert-Samuel bounds that the step [every character from the literature](/step/every-character-of-literature/) uses.

### The setting

We use block data as in the previous section. Let $K$ be a finite set of blocks, and let $y = (y_{k,i})$ be a point with coordinates in a field $\Omega$. Its ideal $P$ in the multigraded ring $\mathbb{Z}[x_{k,i}]$ is the kernel of evaluation at $y$, and we assume that $X = V(P)$ is an [[arithmetic variety|YXWGV80Z2V]] of dimension $D + 1$ and that $\Omega$ is its function field: every element of $\Omega$ is a quotient of two forms of the same multidegree evaluated at $y$.

**Definition 6.10.1 (Hermitian line and small sections).** A hermitian line $\bar A$ is a multidegree $a \in \mathbb{Z}^K$ and a smooth function $h$ on the complex cone with $h(c \cdot z) = \prod_k |c_k|^{a_k} h(z)$. A section of $\bar A^n$ is an element $s \in \Omega$ that is a value of a form of multidegree $na$ on each chart. It is small if $|s(z)| \le h(z)^n$ at every complex point $z$ of $X$. Write $\hat h^0(n)$ for the logarithm of the number of small sections of $\bar A^n$, and
$$\widehat{\operatorname{vol}}(\bar A) = \limsup_{n \to \infty} \frac{\hat h^0(n)}{n^{D+1}/(D+1)!}.$$

The metric is [[plurisubharmonic|FF2P7ER3QT]] in the sense of the development if $\log h$ has a semipositive Levi form on the complex points, relative to an ideal $P_0 \subseteq P$; we then call $\bar A$ semipositive. The bundle is nef on the fibres if its degree on every vertical curve is at least $0$. The self intersection $\bar A^{D+1}$ is the value of an intersection system $I$: a function on families of hermitian lines that is symmetric, additive, and satisfies the inductive formula of Bost, Gillet and Soulé. This is the [[arithmetic intersection number|4HV4WTAX9P]] of the [arithmetic varieties and intersection numbers](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers) of Volume 1.

### Norms of sections on a graph

For the upper bounds we must compare $\bar A^m$ with the bundle $\mathcal{O}(1)$ of a projective embedding given by sections of $\bar A^m$. Let $v_1, \dots, v_N$ be sections of $\bar A^m$ that generate $A^m$. The graph of $v$ is the point $(y, v_1, \dots, v_N)$, with a new block for the $v_j$. Write $\|v_j\|(z) = |v_j(z)| / h(z)^m$.

**Proposition 6.10.2 (Norms of sections on the graph).** Let $\bar A$ be smooth and invariant under complex conjugation, let $m \ge 0$, and let $v_1, \dots, v_N$ be sections of $\bar A^m$ that generate $A^m$. Then there is a function $S$ on the set of points with a nonzero coordinate in every block, with these properties.
1. $S$ is smooth and positive.
2. $S$ is invariant under scalars in each block and under complex conjugation.
3. $S(z) = \sum_j \|v_j\|(z)^2$ at every complex point $z$ of $X$.
4. At every complex point $(z, u)$ of the graph and every tangent vector $(w, w')$ there,
$$\operatorname{Levi}\Big(\tfrac12 \log \textstyle\sum_j |u_j|^2 - \tfrac12 \log S(z)\Big) = m \operatorname{Levi}(\log h)(z; w).$$

Lean: `GroundTheory.Heights₂.Heights.HilbertSamuel.SectionNormSqExtension.proof`.

*Proof.* On a chart of $X$ the sections $v_j$ are values of forms $G_j$ of multidegree $ma$. The development builds $S$ explicitly from such chart data and from a finite set of generators of the coordinate ring: it is a weighted sum over the charts of terms $|G_j|^2/h^{2m}$, with correction terms that vanish on $X$, so that $S$ is defined and smooth off $X$ as well. On $X$ the value is $\sum_j \|v_j\|^2$, which gives 3. Positivity uses the hypothesis that the $v_j$ generate. The invariances in 2 follow from the homogeneity of the $G_j$ and of $h$, and from the conjugation invariance of $h$. We take these verifications from the development.

For 4 we use four facts about the Levi form, the hermitian form $\partial \bar\partial$, which the development proves separately.
1. If $u$ vanishes to second order at $z$ in the direction $w$, then $\log(P + u)$ and $\log P$ have the same Levi form there.
2. If $\varphi$ is holomorphic with $\varphi(z) = 0$ and $d\varphi(z) w = 0$, then $\xi (|a + \varphi|^2 - |a|^2)$ vanishes to second order at $z$ in the direction $w$.
3. The Levi form of $\varphi \circ g$, for holomorphic $g$, is the pull back of the Levi form of $\varphi$ by $dg$.
4. The Levi form of $\tfrac12 \log \sum_j |u_j|^2$ at $c\,a$ in the direction $c\,b + \mu a$ equals the one at $a$ in the direction $b$.

On the graph $u_j = v_j(z)$, so $\sum_j |u_j|^2 = h^{2m} S$. In outline: by 1 and 2 the correction terms of $S$ do not change the Levi form at points of the graph. By 3 and 4 the Levi form of $\tfrac12 \log \sum_j |u_j|^2$ along the graph is that of $\tfrac12 \log \sum_j |G_j|^2$. Subtracting $\tfrac12 \log S$ leaves $\tfrac12 \log h^{2m} = m \log h$. $\square$

The proposition says that the Fubini-Study metric of the embedding by $v$, divided by $S$, is the $m$-th power of the metric of $\bar A$ on the graph, in the sense of Levi forms. So it transports semipositivity and the $L^2$ formula from $\bar A^m$ to the embedding.

### The bounds

**Theorem 6.10.3 (Moriwaki bigness and Hilbert-Samuel bounds).** Assume that intersection systems exist, that complex points of arithmetic varieties have resolutions, and that points of bounded height are dense in the sense of the development. Let $I$ be an intersection system and $\bar A$ a hermitian line invariant under complex conjugation on an arithmetic variety $X$ of dimension $D + 1$ as above. Then the following hold.
1. Bigness: if $D \ge 1$ and $\bar A$ is semipositive and nef on the fibres, then $\bar A^{D+1} \le \widehat{\operatorname{vol}}(\bar A)$.
2. Curves: if $D = 0$ and $\bar A$ is semipositive, nef on the fibres and nef on the generic fibre, then $\bar A^{1} \le \widehat{\operatorname{vol}}(\bar A)$.
3. Kleiman: if $\bar A$ is semipositive, nef on the fibres, and $\bar A|_C^{1} \ge 0$ for every horizontal curve $C \subseteq X$, then $\bar A^{D+1} \ge 0$.
4. Upper bound for generated bundles: if $D \ge 1$ and $\bar A$ is generated by small sections in the sense of the development, then $\widehat{\operatorname{vol}}(\bar A) \le \bar A^{D+1}$.
5. Upper bound for bounded monomials: if $D \ge 1$, $\bar A$ is semipositive of multidegree $a \ge 0$, and every monomial of multidegree $a$ in the coordinates has norm at most $1$, then $\limsup_n \hat h^0(n) (D+1)!/n^{D+1} \le \bar A^{D+1}$, with the sections counted in the lattice of the coordinate ring.

Lean: `PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsChain`.

*Proof.* The development proves the theorem in 180 steps. We give their outline; each step is a result of the development that we cite.

Bigness. The [block Hilbert-Samuel formula](/entry/theorem-hsmblock/) gives the $L^2$ covolume of the lattice of sections of $\bar A^n$ for ample $\bar A$. By Minkowski's theorem on lattice points, a lattice of rank $r_n$ and covolume $e^{-\chi(n)}$ has at least about $e^{\chi(n)}$ points in the $L^2$ unit ball, up to a factor $c^{r_n}$, and $r_n = O(n^D)$. The comparison of sup and $L^2$ norms by $C n^{D/2}$ costs $O(n^D \log n)$. So the count of small sections along multiples of an ample bundle is $\bar A^{D+1} n^{D+1}/(D+1)! + o(n^{D+1})$. For $\bar A$ only nef on the fibres, tensor with a small multiple $\varepsilon \bar B$ of an ample bundle and shift the metric. The development shows that a shifted bundle stays big, that small sections separate points after the shift, and that the shift and $\varepsilon$ change the self intersection and the degree by polynomials in the shift and $\varepsilon$. This is where density of points of bounded height is used. Letting $\varepsilon$ and the shift go to $0$ gives 1.

Curves. For $D = 0$ the variety is the spectrum of an order in a number field, and the sections of $\bar A^n$ form a lattice of fixed rank. Count lattice points in a box with the geometry of numbers in the number field. Nefness on the generic fibre gives the degree bound that the count needs. This gives 2.

Kleiman. The development proves a mixed form of the inequality: all mixed intersection numbers of nef hermitian lines are at least $0$. It uses the positivity of the top intersection of scaled Fubini-Study lines and the algebra of mixed tops. Item 3 is the case of equal lines.

Upper bound for generated bundles. Choose small sections $v_1, \dots, v_N$ of $\bar A^m$ that generate, and pass to the graph by [the proposition](/entry/section-norm-sq-extension-proof/). The graph is a power block datum, and the block Hilbert-Samuel formula applies to it. So the $L^2$ degree of the tensor powers is $\bar A^{D+1}$ in the limit. Small sections are then counted in Euclidean balls: by the successive minima of the lattice, which are spanned by small vectors, the number of lattice points in the unit ball is at most $e^{\chi(n) + o(n^{D+1})}$. This gives 4.

Upper bound for bounded monomials. Shift and perturb the monomials so that the bundle becomes generated by small sections, and normalise so that 4 applies. The bound of the monomials controls the change. This gives 5. $\square$

The corollaries of the development combine 1 and 2 into Moriwaki's statement on bigness, and 3, 4 and 5 into the Hilbert-Samuel bounds that the [step](/step/every-character-of-literature/) uses.

**Remark 6.10.4 (Formalization).** The count of small sections is the logarithm of a cardinality that is $0$ for an infinite set, and the volume is an upper limit in the real numbers, which has a conventional value for an unbounded sequence ([PenVol.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/PenVol.lean#L32)). Only the lower bound of Moriwaki's theorem is proved here; the upper bounds 4 and 5 need hypotheses of generation or of bounded monomials. Item 5 has no nef hypothesis, although its name in the development refers to nef bundles. The density of points of bounded height is used once, in the separation of sections after a shift ([HSChain.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/HSChain.lean#L265)). The block Hilbert-Samuel formula is called twice, for the ample count and for the tensor powers on the graph. The four facts on Levi forms are separate statements of the development, proved and fed into the proposition. The steps of the theorem are cited results whose proofs we did not open.

## Notes and references

This chapter proves two results that the main proof uses as published inputs. The arithmetic Hilbert-Samuel formula for nef bundles is proved from principalisation of ideals and feeds [the Hilbert-Samuel formula from the literature](/entry/arith-hilbert-samuel-of-literature/); the volume bound of the eighth section feeds [the volume bound from the literature](/entry/vol-ge-of-literature/). Both are used in the step [published results in arithmetic geometry](/step/published-results-arithmetic/). The bigness and the Hilbert-Samuel bounds of the last section are used in the step [every character from the literature](/step/every-character-of-literature/).

The arithmetic intersection theory and the arithmetic Riemann-Roch theorem are due to Gillet and Soulé. The arithmetic Hilbert-Samuel formula for ample bundles was proved by Gillet and Soulé as a consequence of the arithmetic Riemann-Roch theorem, and by Abbes and Bouche by a direct analytic method. Zhang extended it to nef bundles and introduced the notion of nef hermitian line bundle used here. The inductive definition of heights of cycles is due to Bost, Gillet and Soulé. The lower bound for the volume of a bundle nef on the fibres is due to Yuan and to Moriwaki. The principalisation of ideals goes back to Hironaka; a modern account is in the book of Kollár. The Poincaré-Lelong formula is in Griffiths and Harris.

- H. Gillet and C. Soulé, "Arithmetic intersection theory", Publ. Math. IHÉS 72 (1990), 93 to 174.
- H. Gillet and C. Soulé, "An arithmetic Riemann-Roch theorem", Invent. Math. 110 (1992), 473 to 543.
- A. Abbes and T. Bouche, "Théorème de Hilbert-Samuel « arithmétique »", Ann. Inst. Fourier 45 (1995), 375 to 401.
- S. Zhang, "Positive line bundles on arithmetic varieties", J. Amer. Math. Soc. 8 (1995), 187 to 221.
- J.-B. Bost, H. Gillet and C. Soulé, "Heights of projective varieties and positive Green forms", J. Amer. Math. Soc. 7 (1994), 903 to 1027.
- X. Yuan, "Big line bundles over arithmetic varieties", Invent. Math. 173 (2008), 603 to 649.
- A. Moriwaki, "Continuity of volumes on arithmetic varieties", J. Algebraic Geom. 18 (2009), 407 to 457.
- H. Hironaka, "Resolution of singularities of an algebraic variety over a field of characteristic zero: I", Ann. of Math. 79 (1964), 109 to 203.
- J. Kollár, *Lectures on Resolution of Singularities*, Annals of Mathematics Studies 166, Princeton University Press, 2007, Chapter 3.
- P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978, Chapter 3, Section 2.
- C. Soulé, D. Abramovich, J.-F. Burnol and J. Kramer, *Lectures on Arakelov Geometry*, Cambridge Studies in Advanced Mathematics 33, Cambridge University Press, 1992, Chapters II to IV.
