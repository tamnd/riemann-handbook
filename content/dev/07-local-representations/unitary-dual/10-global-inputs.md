---
title: Global inputs
decls:
  - PositivityTheory.Rg.Cz.clozelCohomological
  - PositivityTheory.Rg.Cz.clozelCohomological_of_three
  - PositivityTheory.Rg.Cz.kType_holds
  - PositivityTheory.RgJS.cauchyAll
  - PositivityTheory.RgJS.cauchy_local_inequality
  - PositivityTheory.Rg.Tf.Loc.bcflUnit
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Global inputs

The last section proves three facts that connect the local theory with automorphic forms. The first is Clozel's theorem: a cuspidal representation of $\mathrm{GL}_a$ over a totally complex number field with regular algebraic infinitesimal character is cohomological. The second is the Cauchy identity for the unramified Euler product of a Rankin and Selberg $L$-function, with absolute convergence and an explicit bound. The third is Kottwitz's base change fundamental lemma for the unit element of the Hecke algebra, for an unramified extension of local fields. Clozel's theorem feeds the step [EveryCharacter from Row0b](/step/every-character-of-row/), the Cauchy identity feeds [Theorem 9.14.5 of Volume 3](/entry/rs-pole/), and the fundamental lemma feeds the step [EveryCharacter](/step/every-character/).

Background: [representations of real groups](/learn/representations/#representations-of-real-groups), [highest weights and branching](/learn/representations/#highest-weights-and-branching), [generic representations](/learn/representations/#generic-representations-and-local-factors), [smooth representations of $p$-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups).

### Cohomological representations

Let $E$ be a totally complex number field and $a \ge 1$. Let $\pi$ be a cuspidal automorphic subrepresentation of $\mathrm{GL}_a(\mathbb{A}_E)$. For each complex embedding $\tau$ of $E$, the Lie algebra $\mathfrak{gl}_a(\mathbb{C})$ acts on the smooth vectors of $\pi$ through the archimedean place of $\tau$, and its center acts by an infinitesimal character, a multiset of $a$ complex numbers. The representation $\pi$ is *regular algebraic* if, for every $\tau$, these $a$ numbers are distinct and each lies in $\mathbb{Z} + \frac{a-1}{2}$. It is *cohomological* if there is an irreducible algebraic representation $\Xi$ of $\mathrm{GL}_a(E \otimes \mathbb{R})$ such that the relative Lie algebra cohomology $H^*(\mathfrak{g}, K; \pi_\infty \otimes \Xi)$ is nonzero, with $K$ the product of the unitary groups $\mathrm{U}(a)$ over the complex places.

**Theorem 7.10.1 (Clozel).** Every regular algebraic cuspidal representation $\pi$ of $\mathrm{GL}_a(\mathbb{A}_E)$ is cohomological.

Lean: `PositivityTheory.Rg.Cz.clozelCohomological` (also `PositivityTheory.Rg.Cz.clozelCohomological_of_three`).

The main local step is a statement on $K$-types of generic modules. Let $V = \mathbb{C}^n$ be the standard representation. For a Young tableau with $N$ boxes, each box labelled by an embedding $\tau$, the tableau fixes a subspace of $M \otimes V^{\otimes N}$ of tensors that are antisymmetric along the columns.

**Theorem 7.10.2 (K-type).** Let $n \ge 1$, and let $M$ be a $(\mathfrak{g}, K)$-module for a product of copies of $\mathfrak{gl}_n(\mathbb{C})$ indexed by the embeddings $\tau$. Assume that, for every $\tau$, the infinitesimal character is given by an injective map $l_\tau : \{1, \dots, n\} \to \mathbb{Z}$, and that $M$ has a nonzero Whittaker functional for each factor. Then there are an integer $s$ and a labelled Young tableau with the following properties. For each $\tau$, the row lengths of the boxes with label $\tau$, after a permutation $w$, satisfy $s - l_\tau(w(i)) = (\text{row length } i) + i$. And there is a $K$-invariant tensor in $M \otimes V^{\otimes N}$, antisymmetric along the columns of the tableau, whose alternation over the pairs of conjugate labels is nonzero.

Lean: `PositivityTheory.Rg.Cz.kType_holds`.

*Proof.* Let $E_{ij}$ be the action of the matrix units on $M$, and extend it to $M \otimes V^{\otimes m}$. On this tensor product, the Jucys and Murphy elements $x_j$ commute with each other and satisfy $x_{j+1} s_j = s_j x_j + 1$ with the simple transpositions $s_j$. The product $\prod_j (u - x_j)$, on the antisymmetric part, equals the quantum determinant $\mathrm{qdet}(E)(u)$, a central polynomial in $u$ of degree $n$. A step formula relates the quantum determinant on $M \otimes V^{\otimes m}$ with that on $M$. Since the infinitesimal character is integral and regular, the joint spectrum of the $x_j$ is a set of integers with a fixed pattern, and the tensors of a fixed content form a chain that is antisymmetric along columns. On the Whittaker side, the functional $\varphi$ satisfies $\varphi \circ \mathrm{qdet}(E_\tau)(u) = (u + s)^n \varphi$. A contraction lowers the degree of a semi-invariant vector of $\varphi$ until it reaches a $K$-fixed vector $\xi$ with $\varphi(w\xi) \ne 0$ for some $w$ in the enveloping algebra. Transferring $\xi$ through the chain gives the tensor of the theorem, and the shape of the tableau follows from the content. $\square$

*Proof of the theorem.* There are five steps.

1. *Whittaker functional.* The Fourier expansion of cusp forms along the unipotent radical of the Borel subgroup gives a nonzero functional $\ell$ on the smooth vectors of $\pi$ that is a Whittaker functional for each $\tau$.
2. *Integral character.* Since $\pi$ is regular algebraic, the infinitesimal character at $\tau$ is given by an injective map $l_\tau$ to $\mathbb{Z}$, up to the shift by $\frac{a-1}{2}$.
3. *K-type.* The theorem on $K$-types gives $s$ and a $K$-invariant tensor of the required shape.
4. *Coefficient.* From the tensor one builds an irreducible algebraic representation $\Xi$ and a nonzero $K$-invariant cochain $\omega \in \mathrm{Hom}(\wedge^q \mathfrak{p}, \pi \otimes \Xi)$. The representation $\Xi$ is *small* for $\pi$: the Casimir operator of $\pi$ acts by a scalar $c$, the trace of $\Xi$ is opposite to that of $\pi$, and the Casimir operator of $\Xi$ is at most $c$ on every vector.
5. *Kuga's lemma.* The representation $\pi$ has a positive definite Hermitian form, invariant up to a twist by a power of $|\det|$. On the complex $\mathrm{Hom}_K(\wedge^\bullet \mathfrak{p}, \pi \otimes \Xi)$, with the form from $\pi$ and an admissible inner product on $\Xi$, Kuga's formula expresses the Laplacian as the difference of the Casimir operators of $\pi$ and of $\Xi$. The Laplacian is nonnegative, and by smallness this difference is nonpositive. So the Laplacian is zero, the cochain $\omega$ is harmonic, and it gives a nonzero cohomology class.

$\square$

### The Cauchy identity

For a partition $\lambda$ with at most $k$ parts, let $s_\lambda$ be the Schur polynomial, and pad $\lambda$ with zeros when it is evaluated at more variables.

**Theorem 7.10.3 (Local Cauchy identity).** Let $k \le m$, $q \ge 2$, $\alpha \in (\mathbb{C}^\times)^m$ and $\beta \in (\mathbb{C}^\times)^k$ with $|\alpha_a| \le \sqrt{q}$ and $|\beta_b| \le \sqrt{q}$. Let $\mathrm{Re}(s) > 1$. Then
$$\sum_{\lambda} s_\lambda(\alpha)\, \overline{s_\lambda(\beta)}\, q^{-s|\lambda|} = \prod_{a=1}^{m} \prod_{b=1}^{k} \bigl(1 - \alpha_a \overline{\beta_b} q^{-s}\bigr)^{-1},$$
the sum over partitions with at most $k$ parts. The sum converges absolutely, and
$$\sum_\lambda \bigl| s_\lambda(\alpha)\, \overline{s_\lambda(\beta)}\, q^{-s|\lambda|} \bigr| \le \bigl(1 - q^{1 - \mathrm{Re}(s)}\bigr)^{-m^2}.$$

Lean: `PositivityTheory.RgJS.cauchy_local_inequality`.

*Proof.* First the identity for $|X| A B < 1$, with $|\alpha_i| \le A$ and $|\beta_j| \le B$: $\sum_\lambda s_\lambda(\alpha) s_\lambda(\beta) X^{|\lambda|} = \prod_{i,j} (1 - \alpha_i \beta_j X)^{-1}$. The generating function of the complete homogeneous polynomials $h_r(\alpha)$ is $\prod_i (1 - \alpha_i t)^{-1}$, and it gives the bound $|h_r(\alpha)| \le \binom{r + m - 1}{m - 1} A^r$. The relation between the elementary and the complete homogeneous polynomials gives the Jacobi and Trudi formula $s_\lambda = \det(h_{\lambda_i - i + j})$ from the alternant formula. Expanding $\prod_j \prod_i (1 - \alpha_i \beta_j X)^{-1} = \prod_j \sum_r h_r(\alpha) (\beta_j X)^r$ and antisymmetrizing in $\beta$ gives the identity when the $\beta_j$ are distinct; both sides are continuous in $\beta$, so it holds for all $\beta$. Padding with zero variables does not change $s_\lambda$, which gives the case $k < m$.

Apply this with $\overline{\beta}$ in place of $\beta$, $X = q^{-s}$ and $A = B = \sqrt{q}$; then $|X| A B = q^{1 - \mathrm{Re}(s)} < 1$. Since $\overline{s_\lambda(\beta)} = s_\lambda(\overline{\beta})$, this is the identity. For the bound, the coefficients of $s_\lambda$ are nonnegative, so $|s_\lambda(\alpha)| \le s_\lambda(A, \dots, A)$ and the same for $\beta$. The sum of absolute values is at most the identity at $\alpha = (A, \dots, A)$, $\beta = (B, \dots, B)$ and $X = |q^{-s}|$, which is $(1 - q^{1 - \mathrm{Re}(s)})^{-mk} \le (1 - q^{1 - \mathrm{Re}(s)})^{-m^2}$. $\square$

**Theorem 7.10.4 (Global Cauchy identity).** Let $E$ be a number field and $S$ a finite set of finite places. For each finite place $w \notin S$ with residue field of size $q_w$, let $\alpha_w \in (\mathbb{C}^\times)^m$ and $\beta_w \in (\mathbb{C}^\times)^k$ with $k \le m$ and all entries of absolute value at most $\sqrt{q_w}$. Let $\mathrm{Re}(s) > 2$. Then the sum over the finitely supported families $(\lambda_w)_{w \notin S}$ of partitions of
$$\prod_{w} s_{\lambda_w}(\alpha_w)\, \overline{s_{\lambda_w}(\beta_w)}\, q_w^{-s|\lambda_w|}$$
converges absolutely, and its value is the partial Euler product $L^S(s) = \prod_{w \notin S} \prod_{a, b} (1 - \alpha_{w,a} \overline{\beta_{w,b}} q_w^{-s})^{-1}$.

Lean: `PositivityTheory.RgJS.cauchyAll`.

*Proof.* Put $\sigma = \mathrm{Re}(s)$. The norms $q_w$ satisfy $q_w \ge 2$, and $\sum_w q_w^{-\sigma'}$ converges for every $\sigma' > 1$. So $\sum_w q_w^{1-\sigma}$ converges, and $q_w^{1-\sigma} \le \frac12$. By the local theorem, the local series at $w$ has constant term $1$ and the sum of the absolute values of its other terms is at most $(1 - q_w^{1-\sigma})^{-m^2} - 1 \le C q_w^{1-\sigma}$ with $C$ depending only on $m$. The product of the local sums of absolute values converges, so the sum over finitely supported families converges absolutely, and its value is the product of the local values. $\square$

### Base change for the unit element

Let $k$ be a nonarchimedean local field of characteristic zero, and let $E/k$ be a finite unramified Galois extension of degree $\ell$, so that a uniformizer of $k$ is a uniformizer of $E$. Let $\sigma$ generate $\mathrm{Gal}(E/k)$, and let $\sigma$ act on $\mathrm{GL}_n(E)$ entrywise. The norm of $\delta \in \mathrm{GL}_n(E)$ is $N\delta = \delta\, \sigma(\delta) \cdots \sigma^{\ell-1}(\delta)$. Its conjugacy class meets $\mathrm{GL}_n(k)$, and $\delta$ is *$\sigma$-regular semisimple* if the characteristic polynomial of $N\delta$ is separable. Let $K_E = \mathrm{GL}_n(\mathcal{O}_E)$ and $K_k = \mathrm{GL}_n(\mathcal{O}_k)$, with the [[Haar measure|VY0HXD3GC4]] of volume $1$ on each. For $\gamma \in \mathrm{GL}_n(k)$ and $\delta \in \mathrm{GL}_n(E)$, let $O_\gamma$ and $TO_\delta$ be the orbital integral and the $\sigma$-twisted orbital integral, over the quotients by the centralizer $G_\gamma$ and the twisted centralizer $G_{\delta\sigma}$.

**Theorem 7.10.5 (Base change fundamental lemma for the unit).** Let $\delta$ be $\sigma$-regular semisimple and $N\delta = h \gamma h^{-1}$ with $\gamma \in \mathrm{GL}_n(k)$, and give $G_{\delta\sigma}$ and $G_\gamma$ the Haar measures that match under conjugation by $h$. Then $TO_\delta(1_{K_E}) = O_\gamma(1_{K_k})$. If $\gamma$ is regular semisimple and is not a norm, then $O_\gamma(1_{K_k}) = 0$.

Lean: `PositivityTheory.Rg.Tf.Loc.bcflUnit`.

*Proof.* Call $\gamma$ *integral* if its characteristic polynomial has coefficients in $\mathcal{O}_k$ and a unit constant term. The proof uses four facts.

1. If $\gamma$ is conjugate into $K_k$, then $\gamma$ is integral. If $g^{-1} \delta \sigma(g) \in K_E$, then $g^{-1} (N\delta) g \in K_E$.
2. If $\gamma$ is integral, there is a unit $c$ of the algebra $\mathcal{O}_E[\gamma]$ with $Nc = \gamma$. This uses that the norm is onto on units in an unramified extension.
3. If $\gamma$ is regular semisimple and $c$ is as in (2), then $g^{-1} c\, \sigma(g) \in K_E$ if and only if $g^{-1} \sigma(g) \in K_E$ and $g^{-1} \gamma g \in K_E$. And the twisted centralizer of $c$ equals the centralizer of $\gamma$. The second claim uses that a matrix commuting with a regular semisimple matrix is a polynomial in it.
4. If $g^{-1}\sigma(g) \in K_E$, then $g \in \mathrm{GL}_n(k) K_E$. Indeed $u = g^{-1}\sigma(g)$ is a cocycle of $\mathrm{Gal}(E/k)$ in $K_E$. This cohomology set is trivial by Lang's theorem over the residue field and successive approximation, so $u = v^{-1}\sigma(v)$ with $v \in K_E$, and $g v^{-1}$ is fixed by $\sigma$.

A regular semisimple $\gamma$ is integral if and only if it is conjugate into $K_k$: if it is integral, it stabilizes the lattice $\mathcal{O}_k[\gamma] v$ for a cyclic vector $v$. If $\gamma$ is not integral, then both integrals vanish by (1). If $\gamma$ is integral, it is a norm by (2). This gives the second claim. Let $c$ be as in (2). Twisted orbital integrals depend only on the $\sigma$-conjugacy class, and $\delta$ is $\sigma$-conjugate to $c$ because their norms are conjugate and $\delta$ is $\sigma$-regular. By (3) and (4), the set of $g$ with $g^{-1} c\, \sigma(g) \in K_E$ is $\{ y u : y \in \mathrm{GL}_n(k),\ u \in K_E,\ y^{-1} \gamma y \in K_k \}$. Its image in $G_\gamma \backslash \mathrm{GL}_n(E)$ has the same measure as the image of $\{y : y^{-1} \gamma y \in K_k\}$ in $G_\gamma \backslash \mathrm{GL}_n(k)$, since $K_E \cap \mathrm{GL}_n(k) = K_k$ and both have volume $1$. $\square$

**Remark 7.10.6 (Formalization).** Clozel's theorem is in [ClozelCohomological.lean](lean:Development/WeilBound/RepresentationTheoryGL/CasimirAlgebra/KugaCoordinates/ClozelCohomological.lean#L8), with its published form in [ClozelCohomologicalModel.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisGeometry₂/ClozelCohomologicalModel.lean#L10). The assembly from three hypotheses is in [ClozelCohomologicalOfThree.lean](lean:Development/WeilBound/RepresentationTheoryGL/CasimirAlgebra/KugaCoordinates/ClozelCohomologicalOfThree.lean#L10), and the five steps are in [ClozelCohomologicalOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/CasimirAlgebra/TensorRelationsGL/ClozelCohomologicalOf.lean#L55). The theorem on $K$-types is in [KTypeHolds.lean](lean:Development/WeilBound/RepresentationTheoryGL/CasimirAlgebra/TensorRelationsGL/KTypeHolds.lean#L27), with its statement in [StepFormula.lean](lean:Development/WeilBound/RepresentationTheoryGL/CasimirAlgebra/TensorRelationsGL/StepFormula.lean#L81). The local Cauchy identity is in [CauchyVariationInequality.lean](lean:Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/CauchyIdentity/CauchyVariationInequality.lean#L20); the identity of line 13 carries the name `cauchy_variation_inequality`, although it contains no inequality. The statements are in [CauchyLoc.lean](lean:Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/AbsoluteRigidity/CauchyLoc.lean#L31). The global identity is in [CauchyAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/AbsoluteRigidity/CauchyAll.lean#L7), and its proof from the local one is in [PolyMulGaussianLeConst.lean](lean:Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/AbsoluteRigidity/CauchyLocalisation/PolyMulGaussianLeConst.lean#L172), a file named for another lemma. The fundamental lemma is in [BcflUnit.lean](lean:Development/WeilBound/RepresentationTheoryGL/TwistedFactors/IntegralUnitBaseChange/BcflUnit.lean#L30), with its statement in [InvTransposeGLInvTransposeGL.lean](lean:Development/WeilBound/RepresentationTheoryGL/TwistedFactors/IntegralUnitBaseChange/InvTransposeGLInvTransposeGL.lean#L263), the four facts as hypotheses in [Development.lean](lean:Development/WeilBound/RepresentationTheoryGL/TwistedFactors/IntegralUnitBaseChange/Development.lean#L145), and the assembly from twenty leaves in [QuotientIntegralOfCompactOpen.lean](lean:Development/WeilBound/RepresentationTheoryGL/TwistedFactors/IntegralUnitBaseChange/QuotientIntegralOfCompactOpen.lean#L18).

## Notes and references

This chapter supplies the local and semi-local representation theory of the step [EveryCharacter](/step/every-character/). Bernstein's irreducibility theorem, the exponent bound and the classification of generic representations fix the form of the unitary generic local components. The branching theorem for $\mathrm{U}(p, q)$ is [the real input E](/entry/real-input-e-holds/), and the formal degree formula is [the formal degree statement of the literature](/entry/formal-degree-compact-dual-of-literature/). Clozel's theorem enters the step [EveryCharacter from Row0b](/step/every-character-of-row/), and the Cauchy identity enters [Theorem 9.14.5 of Volume 3](/entry/rs-pole/).

- I. N. Bernstein, *P-invariant distributions on GL(N) and the classification of unitary representations of GL(N) (non-archimedean case)*, Lie Group Representations II, Lecture Notes in Math. 1041 (1984), 50 to 102.
- I. N. Bernstein and A. V. Zelevinsky, *Representations of the group GL(n, F) where F is a non-archimedean local field*, Russian Math. Surveys 31:3 (1976), 1 to 68.
- I. N. Bernstein and A. V. Zelevinsky, *Induced representations of reductive p-adic groups I*, Ann. Sci. ÉNS 10 (1977), 441 to 472.
- A. V. Zelevinsky, *Induced representations of reductive p-adic groups II*, Ann. Sci. ÉNS 13 (1980), 165 to 210.
- M. Tadić, *Classification of unitary representations in irreducible representations of general linear group (non-archimedean case)*, Ann. Sci. ÉNS 19 (1986), 335 to 382.
- Harish-Chandra, *Discrete series for semisimple Lie groups II*, Acta Math. 116 (1966), 1 to 111.
- H. He, *On the Gan-Gross-Prasad conjecture for U(p,q)*, Invent. Math. 209 (2017), 837 to 884.
- L. Clozel, *Motifs et formes automorphes: applications du principe de fonctorialité*, Automorphic Forms, Shimura Varieties, and L-functions I, Perspect. Math. 10 (1990), 77 to 159.
- H. Jacquet and J. A. Shalika, *On Euler products and the classification of automorphic representations I*, Amer. J. Math. 103 (1981), 499 to 558.
- I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford (1995), Chapter I.
- R. E. Kottwitz, *Base change for unit elements of Hecke algebras*, Compositio Math. 60 (1986), 237 to 250.
