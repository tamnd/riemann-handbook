---
title: The Siegel-Weil formula for a definite space
decls:
  - PositivityTheory.SiegelWeilFormula.KWhit.genDictX_of_k
  - PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_k
  - PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_mid_k
  - PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_pre_k
  - PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_ct_k
  - PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_k
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Siegel-Weil formula for a definite space

The Rallis inner product formula of this chapter computes the inner product of two theta lifts as a value of a Siegel [[Eisenstein series|3NZBZXYWAJ]] on the doubled group. The bridge between the two sides is the [Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula): the Eisenstein series of a section that comes from the Weil representation is, at one point $s_0$, a theta integral. This section proves it for a definite space $A$ over the good base data of [the Weil representation of a good unitary pair](/entry/exists-is-weil-k/). The proof is by induction on the rank of $Y$, with the [constant term split](/entry/ct-split-of-k/) as the induction step and the [Fock space](/entry/k-fin-poly-of-k/) as the space of test vectors. The same proof for all base data is in the chapter [the Siegel-Weil formula](/entry/siegel-weil-std/).

Let $(B, m, n, A, Y)$ be as follows. $B$ is a good base datum for the CM extension $E/F$, $A$ is a space of dimension $m \ge 1$ with signature $(r, s)$ at each real place, $Y$ is a space of dimension $n \ge 1$ with signature $(r', s')$, and either $A$ is hermitian and $Y$ is skew-hermitian or $A$ is skew-hermitian and $Y$ is hermitian. Let $\chi$ be a Hecke character of $\mathbb{A}_E^\times$ whose restriction to $\mathbb{A}_F^\times$ is $\eta^m$, with $\eta$ the quadratic character of $E/F$ (see [Hecke characters](/learn/class-field-theory/#hecke-characters)). A *doubled Weil datum* is a Darboux basis $\kappa$ of the symplectic space $\operatorname{Res}(A \otimes (Y \oplus -Y))$, a representation $\omega$ of the doubled group $G = U(Y \oplus -Y)$ and a representation $S$ of $U(A)$ on the [[Schwartz space|GE020MY43M]] of $\kappa$-coordinates, and a functional $l$, such that $\omega$ and $S$ are the [Weil representation](/learn/theta/#the-weil-representation) of the pair $(U(A), G)$ for the splitting characters given by $\chi$, and $\Phi \mapsto l(\omega(x)\Phi)$ maps the Schwartz space into the sections of the degenerate principal series of $G(\mathbb{A})$ from the Siegel parabolic $P$ (the doubling functional of [the doubling method](/learn/theta/#the-doubling-method)). Let $b$ be a frame of $Y \oplus -Y$ in which $P$ is block upper triangular, $K$ the standard maximal compact subgroup of $G(\mathbb{A})$ for this frame, and $a$ a height on $G(\mathbb{A})$ with $a(pk) = \lvert \det t \rvert$ for $p \in P(\mathbb{A})$ of Levi part $t$ and $k \in K$.

For a function $\varphi$ on $G(\mathbb{A})$ with $\varphi(px) = \chi(\det t)\lvert \det t\rvert^{s_0 + n/2}\varphi(x)$, the *flat section* through $\varphi$ is $\varphi_s(x) = a(x)^{s - s_0}\varphi(x)$. Its Eisenstein series is
$$E(x, s; \varphi) = \sum_{\gamma \in P(F) \backslash G(F)} \varphi_s(\gamma x).$$
We say that $E(x, s; \varphi)$ *has the value $v(x)$ at $s_0$* if for each $x$ there is a meromorphic function $e$ on $\mathbb{C}$ such that the series converges to $e(s)$ for $\operatorname{Re} s$ large, $e$ is holomorphic at $s_0$, and $e(s_0) = v(x)$.

**Theorem 6.4.1 (Siegel-Weil formula for a definite space).** Let $(B, m, n, A, Y)$ be as above with $B$ good and $\min(r, s) = 0$, let $\chi$ be a Hecke character with $\chi|_{\mathbb{A}_F^\times} = \eta^m$, and take a doubled Weil datum $(\kappa, \omega, S, l)$, a frame $b$, the standard maximal compact subgroup $K$ and a height $a$. Let $\mu$ be a Haar measure on $U(A)(\mathbb{A})$ and $D$ a fundamental domain for $U(A)(F)$. Let $\Phi$ be a $K$-finite Schwartz function and $s_0 = (m - n)/2$. Then the Eisenstein series of the flat section through $x \mapsto l(\omega(x)\Phi)$ has at $s_0$ the value
$$E(x, s_0; \Phi) = c\, \frac{1}{\mu(D)} \int_D \theta\bigl(\omega(x) S(g) \Phi\bigr)\, d\mu(g), \qquad c = \begin{cases} 1 & n < m, \\ 2 & m \le n, \end{cases}$$
where $\theta(\Phi') = \sum_{X} \Phi'(X)$ is the sum over the rational $m \times n$ matrices.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_k`.

Since $A$ is definite, $U(A)$ is anisotropic and $U(A)(F) \backslash U(A)(\mathbb{A})$ is compact, so the theta integral converges. In this case the formula with $c = 1$ for $n < m$ is due to Weil (Acta Math. 113, 1965) in the range of absolute convergence; outside that range, and for the constant $2$, it is the regularized Siegel-Weil formula of Kudla and Rallis (Ann. of Math. 140, 1994), whose unitary form is due to Ichino (Math. Z. 247, 2004). The theorem above proves it in the stated form for the $K$-finite vectors.

The proof runs through four reductions. Each one supplies some of the inputs of the next.

**Theorem 6.4.2 (Siegel-Weil formula from the constant term split).** Assume the conclusion of the [constant term split](/entry/ct-split-of-k/) for all Siegel-Weil data over good base data. Then the conclusion of the Siegel-Weil formula for a definite space holds.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_ct_k`.

*Proof.* This is the next theorem applied to the constant term split and to Poisson summation in the form
$$\sum_{X} \int_M \psi\bigl(\varepsilon \operatorname{tr}\, {}^tX J_A \bar Z\bigr)\, f(Z)\, d\nu(Z) = \sum_X f(X)$$
for each Schwartz function $f$ on $M = M_{m \times n}(\mathbb{A}_E)$, each sign $\varepsilon$ and each self-dual Haar measure $\nu$, which is [Poisson summation](/learn/complex-analysis/#poisson-summation-theta-and-mellin) on the adelic vector space $M$. $\square$

**Theorem 6.4.3 (Siegel-Weil formula before the main step).** Assume Poisson summation in the form above and the constant term split. Then the Siegel-Weil formula for a definite space holds.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_pre_k`.

*Proof.* The Weyl element $w$ of $G$ acts in the matrix model by the Fourier transform
$$T(\omega(w)\Phi)(X) = \int_M \psi\bigl(\varepsilon \operatorname{tr}\, {}^tX J_A \bar Z\bigr)\, T\Phi(Z)\, d\nu(Z).$$
The proof of this law has two parts. First, $\omega(w)$ is determined up to a constant $C$ by its commutation with the Siegel parabolic, so the law holds with a factor $C$. Second, the theta sum is invariant under $\omega(w)$ and is not zero for some $\Phi$; with Poisson summation this gives $C = 1$. The Weyl law and the parabolic laws make up the transform laws of [the section on the Fock space](/entry/k-fin-poly-of-k/), together with the bijectivity of $T$, the theta sum and the automorphy of the theta integral (which uses a Siegel set of $U(A)$). From the transform laws the theorem on [K-finite vectors](/entry/k-fin-poly-of-k/) gives that $T\Phi$ is in the Fock space for each $K$-finite $\Phi$. The transform laws also give lower rank data: for each Siegel-Weil datum of rank $n \ge 2$ there is a lower rank datum. The next theorem then gives the formula. $\square$

**Theorem 6.4.4 (Siegel-Weil formula, middle step).** Assume the Weyl law, that $K$-finite vectors have matrix models in the Fock space, that lower rank data exist, and the constant term split. Then the Siegel-Weil formula for a definite space holds.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_mid_k`.

*Proof.* The Weyl law gives all the transform laws, as in the last proof. From them we get: the local instances of the operators at the real places; the dilation law, which says that $t \mapsto \theta$-integral of $\Phi$ at $g\, \iota_w(y\, a(t))$ is holomorphic near the real line for a one-parameter group $a(t)$ of dilations and that its derivatives at $0$ are the theta integrals of the dilated vectors; and the converse of the theorem on K-finite vectors, that a vector with matrix model in the Fock space is $K$-finite. We also use the holomorphy of the leading term of the Eisenstein series at $s_0$, which is the same input as for all base data. The next theorem then gives the formula. $\square$

To state the main step we need the Fourier coefficients of the theta integral.

**Lemma 6.4.5 (Fourier coefficients as local integrals).** Assume the transform laws and the datum properties. Let $d$ be a Siegel-Weil datum, $R$ a real datum, $\Phi$ a $K$-finite vector whose matrix model is a pure product $P \otimes g_f$ in the Fock space, $x$ an element of the Levi subgroup of $P(\mathbb{A})$, and $T$ a nondegenerate rational hermitian matrix. Take coefficient data and a Weyl element $w$. Then there are an anisotropic hermitian matrix $J$ of size $m$ over $E$ (that is, $y^* J y = 0$ only for $y = 0$), a matrix $T'$ of size $n$, local data (an additive character $\psi$, real places, frames, signs that are constant along each real place, local measures and lattices at the finite places, and local Schwartz functions $\Phi_g$, $\Phi_f$, $\Phi_v$), constants $c \in \mathbb{C}$ and $C > 0$, and a bound $t$, such that for $\operatorname{Re} z > t$
$$\int \varphi_z\bigl(w\, n(\beta)\, x\bigr)\, \psi\bigl(-\operatorname{tr}(T\beta)\bigr)\, d\lambda(\beta) = c\, C^{z - s_0} \int W_z(b)\, d\nu(b),$$
where $\varphi_z$ is the flat section through $l(\omega(\cdot)\Phi)$, $W_z$ is the product of the local Whittaker integrals of $\Phi_g$ at $T'$, and the left side is integrable whenever the right side is. Also there are a Haar measure $\mu_H$ on $U(J)(\mathbb{A})$ and a fundamental domain $\mathcal{F}$ for $U(J)(F)$ with
$$\begin{aligned} &\frac{1}{\mu(D)} \int_D \sum_{X \,:\, {}^tX J_A \bar X = -2T} T\bigl(\omega(x)\Phi\bigr)(g^{-1} X)\, d\mu(g) \\ &\qquad = \frac{c}{\mu_H(\mathcal{F})} \int_{\mathcal{F}} \theta_{T'}(h; \Phi_g)\, d\mu_H(h), \end{aligned}$$
where $\theta_{T'}(h; \Phi_g)$ is the theta series of $\Phi_g$ over the rational $X$ with $X^* J X = T'$.

Lean: `PositivityTheory.SiegelWeilFormula.KWhit.genDictX_of_k`.

*Proof.* The lemma assembles five dictionaries: a formula for each cell of the Bruhat decomposition, the relation between the global datum and the local data, a dictionary for the heights, one for the measures, and one for the theta sums. Each translates one object of the datum $d$ into the local language in which the Whittaker integrals are computed. $\square$

The left side of the first identity is the $T$-th Fourier coefficient of the big cell of $E(x, z; \Phi)$, and the right side of the second is the $T$-th Fourier coefficient of the theta integral, written as the mean of a theta series of the definite space $J$. In this form both sides are the same local integrals, and the Siegel-Weil formula of [the doubling method](/learn/theta/#the-doubling-method) for a single nondegenerate coefficient becomes a computation at each place.

**Theorem 6.4.6 (Siegel-Weil formula, main step).** Assume the transform laws, the local instances, the dilation law, the two directions between $K$-finite vectors and the Fock space, the existence of lower rank data, the constant term split, and the holomorphy of the leading term. Then the Siegel-Weil formula for a definite space holds.

Lean: `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of_k`.

*Proof.* We first collect the inputs.

1. The datum properties, the Fock membership, the local operators, and the splitting $g = x\, \iota_w(y)$ of each $g$ in which the height and the section are local functions of $y$.
2. The vacuum space is stable under $K$ and lies in the Fock space.
3. The nondegenerate Fourier coefficients. With the lemma on Fourier coefficients as local integrals, the $T$-th coefficient of $E(x, s_0; \Phi)$ is $c_T$ times the $T$-th coefficient of the theta integral, with $c_T = 1$ for $n < m$ and $c_T = 2$ for $n = m$, and it is $0$ for $m < n$; for $m < n$ no rational $X$ has ${}^tX J_A \bar X = T$ nondegenerate, so the theta side is $0$ as well.
4. The induction step: for $m < n$ the formula with $c = 2$ in rank $n - 1$ gives it in rank $n$. Its inputs include the constant term split, the result of 3 for $m < n$, the holomorphy of the leading term, the vacuum space of 2, and the existence of coefficient data.

With these, the proof has three parts. First, the formula for $n < m$ with $c = 1$, from the coefficients of 3 and the fact that the vacuum vectors generate the polynomial vectors under the local operators. Second, the formula for $n = m$ with $c = 2$, in the same way. Third, the formula for $m < n$ with $c = 2$, by the induction step of 4, started at $n = m$ and run down through the lower rank data. The meromorphic continuation of the Eisenstein series of a $K$-finite section, and the fact that $l(\omega(\cdot)\Phi)$ is a section at $s_0$, join the ranges into the statement. $\square$

**Remark 6.4.7 (Formalization).** The name of the input that proves the datum properties, `auxiliaryExistence_holds`, does not say what it proves. The main step uses the datum properties and the three generic Whittaker results of the copy for all base data, not copies for the good base data ([SiegelWeilFinCore.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinCore.lean#L52), and [SiegelWeilKwhitCutX.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilKwhitCutX.lean#L40)). The step before the main step builds the Weyl law twice from Poisson summation, once for the transform laws and once to pass to the middle step, which builds the transform laws again ([SiegelWeilFinPre.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinPre.lean#L30)); the middle step builds the local instances twice ([SiegelWeilFinMid.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinMid.lean#L23)). The top theorem passes two inputs to the constant term split that it does not use ([SiegelWeilFinFinal.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/SiegelWeilFinFinal.lean#L15)). We have not opened the proofs of the induction step, of the three Whittaker results, of the five dictionaries or of the final assembly, so the proof of the main step above lists its inputs and its three cases and does not reproduce their arguments.
