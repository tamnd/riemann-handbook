---
title: The Gauss integral of a Hermitian form
decls:
  - GlobalTheory.KSp.GaussMain.hasGauss_herm
  - GlobalTheory.T.hasGaussIntegral_hermitian_quadratic_character
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Gauss integral of a Hermitian form

This section computes the Gauss integral of the quadratic character $x \mapsto \psi(\tfrac12 \langle x, xb \rangle)$ on the space of $m \times n$ matrices over a $p$-adic quadratic extension, for each invertible Hermitian $b$. The answer is one constant $\gamma_0$, which does not depend on $b$, times the inverse of the scalar $s(\det b)$ by which the Siegel Levi element $m(a)$ acts in the Schrödinger model. These integrals are the ones that A. Weil used to define his index of a character of second degree (A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964), Chapter I). The result is the analytic input of [the big cell relation](/entry/weyl-cell-relation/) of the next section: it gives the Fourier transform of a Gaussian, and so the constant $\kappa$ by which the Weyl element acts.

### The setting

Let $F$ be a non-archimedean local field of characteristic $0$, and let $E/F$ be a quadratic extension with a quadratic datum $(c, \delta)$ as in [the previous section](/entry/mul-mem-range-norm/). Write $\bar z = c(z)$, extend it to matrices entrywise, and let $\eta$ be the norm residue sign of $E/F$. For a matrix $g$ put $g^* = {}^t\bar g$. Fix:

- an invertible Hermitian matrix $Q \in \mathrm{GL}_m(E)$, that is, $\bar Q_{ji} = Q_{ij}$ for all $i, j$;
- an [[additive character|2WMYTJD33F]] $\psi \colon F \to \mathbb{C}$, continuous, with $|\psi| = 1$ and $\psi \neq 1$;
- a continuous character $\chi \colon E^\times \to \mathbb{C}^\times$ with $|\chi| = 1$ and $\chi(t) = \eta(t)^m$ for $t \in F^\times$;
- an additive [[Haar measure|CE0V9686M8]] $\mu$ on $X = M_{m \times n}(E)$.

**Definition 1.2.1 (The pairing).** For $x, y \in X$ put
$$\langle x, y \rangle = \tfrac12 \operatorname{Tr}_{E/F} \sum_{i,k} Q_{ik}\, (x\, y^*)_{ik}.$$

This is an $F$-bilinear form on $X$ with values in $F$. It is symmetric, since conjugation permutes the terms of the sum and $\operatorname{Tr}_{E/F}$ is invariant under $c$, and it is nondegenerate, since $Q$ is invertible. It is the symplectic pairing of the Lagrangians $X \oplus 0$ and $0 \oplus X$ of $X \oplus X$, and it is the pairing of the Fourier transform of the Schrödinger model.

**Definition 1.2.2 (Scalar of the Levi).** For $z \in E$ put $s(z) = \chi(z)\, |N_{E/F}(z)|_F^{m/2}$ if $z \neq 0$, and $s(0) = 0$.

The map $s$ is multiplicative on $E^\times$. For $t \in F^\times$ one has $s(t) = \eta(t)^m |t|_F^m$.

**Definition 1.2.3 (Gauss value).** Let $f \colon X \to \mathbb{C}$ be locally integrable and $\gamma \in \mathbb{C}$. Say that $f$ has *Gauss value* $\gamma$ if each compact subset of $X$ lies in some compact open subgroup $L \subset X$ with $\int_L f\, d\mu = \gamma$.

For a character of second degree $f$ the integrals $\int_L f\, d\mu$ are constant once $L$ is large, so the Gauss value is the usual regularized integral of $f$ over $X$.

### The theorem

**Theorem 1.2.4 (Gauss integral).** In this setting there is $\gamma_0 \in \mathbb{C}$ such that for each Hermitian $b \in M_n(E)$ with $\det b \neq 0$, the function
$$x \mapsto \psi\bigl(\tfrac12 \langle x, xb \rangle\bigr)$$
on $X$ has Gauss value $\gamma_0\, s(\det b)^{-1}$.

Lean: `GlobalTheory.KSp.GaussMain.hasGauss_herm` (also `GlobalTheory.T.hasGaussIntegral_hermitian_quadratic_character`, a second name).

The determinant of a Hermitian matrix lies in $F$, so $s(\det b)^{-1} = \eta(\det b)^m |\det b|_F^{-m}$.

**Example 1.2.5.** Let $m = n = 1$ and $Q = 1$. A Hermitian $1 \times 1$ matrix is an element $b \in F^\times$, and $\tfrac12\langle x, xb \rangle = \tfrac12 b\, N_{E/F}(x)$. The theorem says that the regularized integral of $\psi(\tfrac12 b N(x))$ over $E$ is $\gamma_0\, \eta(b)\, |b|_F^{-1}$. The factor $|b|_F^{-1}$ comes from the substitution in the norm form, and the sign $\eta(b)$ records whether $b N(\cdot)$ is equivalent to $N(\cdot)$.

*Proof.* The proof reduces the integral to products of one-variable integrals of norm forms.

First, $Q$ and $b$ are diagonalized by congruence: there are $u \in \mathrm{GL}_m(E)$, $a \in \mathrm{GL}_n(E)$ and $D'_1, \dots, D'_m$, $D_1, \dots, D_n$ in $F^\times$ with $Q = u\, \mathrm{diag}(D'_i)\, u^*$ and $b = a\, \mathrm{diag}(D_j)\, a^*$. This is the Gram-Schmidt process for a nondegenerate [[Hermitian form|8NJ7XY6F1S]], which works since the characteristic is not $2$.

Second, in the new coordinates the form is a sum of norms. With $x' = {}^t u\, x\, a$ and $t_{ij} = \tfrac12 D'_i D_j$,
$$\tfrac12\langle x, xb \rangle = \sum_{i,j} t_{ij}\, N_{E/F}(x'_{ij}).$$

Third, the diagonal case is a product of integrals over $E$: there is one constant $g$ such that for all $t \in (F^\times)^{m \times n}$ the function $x' \mapsto \psi(\sum t_{ij} N(x'_{ij}))$ has Gauss value $g \prod_{i,j} \eta(t_{ij})\, |t_{ij}|_F^{-1}$. For one variable this is the statement of the example: substituting $x \mapsto \lambda x$ in the norm form multiplies $t$ by $N(\lambda)$, which changes the integral by $|N(\lambda)|_F^{-1}$; and the two classes of $t$ modulo norms differ by a sign, by the local theory of Weil indices.

Fourth, the linear map $x \mapsto {}^t u\, x\, a$ multiplies the Haar measure by the constant $|N \det u|_F^{-n} |N \det a|_F^{-m}$, and a compact open subgroup goes to a compact open subgroup. So the Gauss value of the original function is this constant times the Gauss value in the diagonal case.

Fifth, the product over $t_{ij} = s_i D_j$, with $s_i = \tfrac12 D'_i$, splits into a part that depends only on $Q$ and a part that depends only on $b$. Here one needs that $\eta$ is a character of $F^\times$, which is [the theorem on non-norms](/entry/mul-mem-range-norm/), and that $|\cdot|_F$ is multiplicative. Put
$$\gamma_0 = g\, |N \det u|_F^{-n} \Bigl(\prod_i \eta(s_i)\, |s_i|_F^{-1}\Bigr)^n,$$
which does not depend on $b$. The rest is
$$|N\det a|_F^{-m} \Bigl(\prod_j \eta(D_j)\, |D_j|_F^{-1}\Bigr)^m .$$
Since $\det b = N(\det a) \prod_j D_j$, since $\eta$ is trivial on norms, and since $\chi = \eta^m$ on $F^\times$, this is $s(\det b)^{-1}$. $\square$

**Remark 1.2.6.** The theorem does not compute $\gamma_0$. [The next section](/entry/weyl-cell-relation/) shows that $\gamma_0 \neq 0$, which is all that is needed there. The classical value is a product of Weil indices, an eighth root of unity times a power of $|2|_F$ and of the volume of $\mu$.

**Remark 1.2.7 (Formalization).** The definition of the Gauss value, `HasGauss` (Definitions/Divisors/UnipVal.lean, line 39), asks that every compact set lie in some compact open subgroup with the right integral. It does not ask this for every large subgroup, so it is weaker than the usual stabilization; it is enough for the use in the next section. The four steps of the proof are wrappers in `GlobalTheory.T` (`exists_GL_diagonal_congruent_hermitian`, `hermitianMatrixColumnPairing_diagonal_norm`, `gaussIntegral_diagonal_hermitianForm_matrices`, and a change of variables for Haar measure), and we have not opened their proofs; most of the declarations below the theorem lie under them. The helpers `sgnHom`, `sgn_inv`, `det_herm`, `sc_det_inv`, `glT` and `sandwich` are in HasGaussIntegralHermitianQuadraticCharacter.lean (lines 27 to 84). The theorem itself is at line 99. Several hypotheses of the statement, such as the Hermitian condition on $Q$ and the restriction condition on $\chi$, are bound as `_` in the type and recovered by `intro`. The absolute value $|\cdot|_F$ appears as `distribHaarChar F` in the change of variables and as `nabs F` in the final step. The second name is a `first | exact ...` wrapper (HasGaussIntegralHermitianQuadraticCharacterStatement.lean, line 9).
