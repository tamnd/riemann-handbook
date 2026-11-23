---
title: An ordinary Eisenstein measure
decls:
  - GlobalTheory.EisM.chapterM_of_level
  - GlobalTheory.EisM.chapterM_holds
  - GlobalTheory.T.ordinaryEisensteinEigenfunctional_exists
status: drafted
drafted_by: writer@claude-opus-5-5
---
## An ordinary Eisenstein measure

This section turns the nonvanishing eigenfunctional of [the last section](/entry/eig-f-value-ne-zero/) into the input of the Euler system argument. For a newform $g$ of odd weight $2e + 1$ that is ordinary at an odd prime $l$, it gives a level $N$, an ordinary Hecke eigenfunctional $\lambda$ that sees only forms of the character of $g$, and an $l$-adic measure built from $\lambda$ and products of two Eisenstein series, with a nonzero value $v$ at the character $\psi$. It also gives two auxiliary integers $c_1$, $d_1$ that are used to smooth Siegel units. The result is used in [the unit law of smoothed classes](/entry/kato-global-unit-law-of-smoothed-classes/) of the Kato chapter. The construction is close in spirit to the ordinary projection of [Hida theory](/learn/galois-cohomology/#hida-theory), applied to the Rankin products of Section 9.

We keep the notation of Section 9: coefficient sequences, the spaces $M_k(L, \varepsilon)$, the operators $U_l$, $T_q$, depleted eigenforms, Hecke eigenfunctionals $\lambda(a) = \sum_{n < B} c_n a_n$, the values $\lambda_{\alpha, r}(a) = \alpha^{-r}\lambda(U_l^r a)$, and the Gauss sum transform $\hat\theta$. Fix a prime $l$ and a field isomorphism $\iota : \overline{\mathbb{Q}}_l \to \mathbb{C}$. For $z \in \mathbb{C}$ write $|z|_\iota = |\iota^{-1}(z)|_l$.

**Definition 6.10.1 (Eigenfunctional for all characters).** Let $\chi$ be a character modulo $N$ with $l \nmid N$, $k \geq 1$, $t$ a sequence and $\alpha \in \mathbb{C}$. A Hecke eigenfunctional $\lambda$ of weight $k$, level $Nl$, character $\chi$, eigenvalues $t$ and $U_l$-eigenvalue $\alpha$ *kills the other characters* if $\lambda(a) = 0$ for every character $\varepsilon \neq \chi$ modulo $N$ and every $a \in M_k(Nl, \varepsilon)$.

The space of all modular forms of level $Nl$ for $\Gamma_1(N) \cap \Gamma_0(l)$ is the direct sum of the spaces $M_k(Nl, \varepsilon)$. So a functional that kills the other characters is determined by its values on $M_k(Nl, \chi)$.

**Definition 6.10.2 (Mixed depleted Eisenstein product).** For $k \geq 2$, $u, w : \mathbb{Z} \to \mathbb{C}$ and $F : \mathbb{N}^2 \to \mathbb{C}$, let
$$
Z'_k(u, w, F)_n = \sum_{\substack{n_1 + n_2 = n \\ l \nmid n_1,\ l \nmid n_2}} \ \sum_{x_1 x_2 = n_1} \ \sum_{y_1 y_2 = n_2} x_1^{k-2}\, u(x_1)\, w(y_1)\, F(x_1, y_2).
$$
It differs from the product $Z_k$ of Section 9 in the arguments of $u$ and $F$.

**Definition 6.10.3 (Eisenstein measure).** Let $k = 2e + 1$, $u, w : \mathbb{Z} \to \mathbb{C}$, $\alpha \in \mathbb{C}$ and $\lambda = (B, c)$. For $m \geq 0$ and $f : \mathbb{Z}/l^m \to \mathbb{C}$ put
$$
\mu_m(f) = \lambda_{\alpha, m}\Bigl(Z'_k\bigl(u, w, (A, d) \mapsto f(A d^{-1} \bmod l^m)\bigr)\Bigr).
$$
Let $s \in \mathbb{C}$, $\psi$ a character modulo $l$ and $v_0 \in \mathbb{C}$. We say that $\mu$ is an *Eisenstein measure with sign $s$, character $\psi$ and value $v_0$* if:

1. (Distribution) for $m \geq 1$, $f$ on $\mathbb{Z}/l^m$ with $f(-y) = s f(y)$, and $f'$ on $\mathbb{Z}/l^{m+1}$ with $f'(y) = f(y \bmod l^m)$, we have $\mu_{m+1}(f') = \mu_m(f)$;
2. (Bound) there is $C$ with $|\mu_m(f)|_\iota \leq C\delta$ whenever $|f(y)|_\iota \leq \delta$ for all $y$;
3. (Field) there is a finite extension $E$ of $\mathbb{Q}_l$ in $\overline{\mathbb{Q}}_l$ such that, for every field $E' \supseteq E$ and every $f$ with $\iota^{-1}$ of all values in $E'$, $\iota^{-1}(\mu_m(f)) \in E'$;
4. (Interpolation) there is $C$ such that, for $m \geq 1$, $\delta \geq 0$ and $f$ with $f(-y) = s f(y)$ and
$$
\Bigl|f(a d^{-1}) - \psi(a)\psi^{-1}(d)\Bigl(\frac{d}{a}\Bigr)^{e}\Bigr|_\iota \leq \delta \quad \text{for all } a, d \in \mathbb{N},\ l \nmid a,\ l \nmid d,
$$
we have $|\mu_m(f) - v_0|_\iota \leq C\delta$.

The distribution property and the bound say that $\mu$ is a bounded measure on $\mathbb{Z}_l$, restricted to functions of a given parity. The interpolation property says that $v_0$ is the integral of the locally analytic function $x \mapsto \psi(x) x^{-e}$ on $\mathbb{Z}_l^\times$, in the sense of a limit. The bound is where the ordinary condition $|\alpha|_\iota = 1$ is used: the factor $\alpha^{-m}$ in $\lambda_{\alpha, m}$ does not grow.

For $N \geq 1$ and $s \in \mathbb{C}$ let $w_{N,s}(B) = [B \equiv 1 \bmod N] - s[B \equiv -1 \bmod N]$.

**Theorem 6.10.4 (Ordinary Eisenstein measure at a given level).** Let $l$ be a prime, $\iota$ as above, $e \geq 1$, and $g$ a newform of weight $2e+1$ with coefficients $a_n$ and $|a_l|_\iota = 1$. Let $\psi$ be a character modulo $l$. Let $N \geq 1$ with $l \nmid N$, let $r \geq 7$ be a prime with $r \mid N$, and let $g'$ be a depleted eigenform of weight $2e+1$, level $N$ and character $\chi$ with $g'_n = a_n$ for all $n$ prime to $N$. Put $s = (-1)^e\psi(-1)$. Then there are a character $\theta$ modulo $N$, $\alpha, v \in \mathbb{C}$, a functional $\lambda$ and integers $c_1, d_1$ such that:

1. $N \geq 5$, $|\alpha|_\iota = 1$ and $\alpha^2 - a_l\alpha + \chi(l)\, l^{2e} = 0$;
2. $\lambda$ is a Hecke eigenfunctional of weight $2e+1$, level $Nl$, character $\chi$, eigenvalues $a_q$ and $U_l$-eigenvalue $\alpha$ that kills the other characters;
3. $\chi(-1) = -1$ and $\theta(-1) = s$;
4. the measure $\mu$ built from $\lambda$, $\alpha$, $u = \hat\theta$ and $w = w_{N,s}$ is an Eisenstein measure with sign $s$, character $\psi$ and value $v$, and $v \neq 0$;
5. $c_1, d_1 > 1$ are prime to $6Nl$, $c_1^e \neq z$ for all $z$ with $|z| = 1$, and for $n_1 = \pm 1$ and all $n_2 \in \mathbb{Z}$,
$$
d_1^2 \neq d_1^{e+1}\,(\theta\chi)(d_1)^{n_1}\psi(d_1)^{n_2}, \qquad d_1^2 \neq d_1^{e+1}\,(\theta\chi^{-1})(d_1)^{n_1}\psi(d_1)^{n_2}.
$$

Lean: `GlobalTheory.EisM.chapterM_of_level`.

*Proof.* *Parity.* Since $g'$ is a depleted eigenform of odd weight, $\chi(-1) = -1$. Also $\psi(-1)^2 = 1$, so $s = \pm 1$.

*The character $\theta$.* Since $r \geq 7$ is a prime dividing $N$, the group of characters modulo $N$ is large enough to give $\theta$ with $\theta(-1) = s$, $\theta\chi \neq 1$ and $\theta\chi^{-1} \neq 1$.

*The unit root.* The values of characters at units are roots of unity, so $|\chi(l)|_\iota = 1$, and $|l|_\iota < 1$. The polynomial $X^2 - \chi^{-1}(l)a_l X + \chi^{-1}(l)l^{2e}$ has a unit coefficient $\chi^{-1}(l)a_l$ and a constant term of absolute value less than $1$. So it splits as $(X - \alpha_0)(X - \beta)$ with $|\alpha_0|_\iota = 1$.

*The eigenfunctional.* The nonvanishing theorem of Section 9, applied to $g'$, $\theta$, $\psi$, $\alpha_0$, $\beta$, gives a Hecke eigenfunctional $\lambda_0$ of character $\chi^{-1}$ and eigenvalues $\chi^{-1}(q)a_q$ with a nonzero value on the depleted product $Z_{2e+1}(\theta, \widehat{\theta\chi}, F)$.

*Atkin and Lehner.* Choose $a_0, b_0$ with $N a_0 - l b_0 = 1$. The Atkin and Lehner matrix $\begin{pmatrix} N a_0 & b_0 \\ N l & N \end{pmatrix}$ maps $M_k(Nl, \chi)$ to $M_k(Nl, \chi^{-1})$. Composing $\lambda_0$ with it gives a functional $\lambda$ of character $\chi$, eigenvalues $a_q$ and $U_l$-eigenvalue $\alpha = \chi(l)\alpha_0$ that kills the other characters. It satisfies $\alpha^2 - a_l\alpha + \chi(l)l^{2e} = 0$ and $|\alpha|_\iota = 1$.

*Nonvanishing.* A lemma transfers the nonvanishing through the Atkin and Lehner matrix: the value $v_1 = \lambda_{\alpha, 1}(Z'_{2e+1}(\hat\theta, \theta\chi, F))$ is nonzero.

*The measure.* A second lemma shows that, for a functional that kills the other characters and has a unit $U_l$-eigenvalue, $\mu$ is an Eisenstein measure with value $v = \frac{2}{\varphi(N)} v_1$. As $v_1 \neq 0$, $v \neq 0$.

*The integers.* As $\theta\chi \neq 1$ and $\theta\chi^{-1} \neq 1$, a lemma on smoothing integers gives $c_1$ and $d_1$. $\square$

**Theorem 6.10.5 (Ordinary Eisenstein measures exist).** Let $l \neq 2$ be a prime, $\iota$ as above, $e \geq 1$, and $g$ a newform of weight $2e+1$, level $M$, character $\chi_g$ and coefficients $a_n$, with $l \nmid M$ and $|a_l|_\iota = 1$. Let $\psi$ be a character modulo $l$ and $N_0 \geq 1$ with $l \nmid N_0$. Then there are $N$, characters $\chi$, $\theta$ modulo $N$, and $\alpha$, $v$, $\lambda$, $c_1$, $d_1$ such that $M \mid N$, $N_0 \mid N$, $l \nmid N$, $\chi(d) = \chi_g(d)$ for $d$ prime to $N$, and conditions 1 to 5 of the last theorem hold.

Lean: `GlobalTheory.EisM.chapterM_holds` (also `GlobalTheory.T.ordinaryEisensteinEigenfunctional_exists`, a second name).

*Proof.* Choose a prime $r \geq l + 7$. Then $r \geq 7$ and $r \neq l$. Put $N = M (M N_0 r)^2$. Then $M \mid N$, $N_0 \mid N$, $r \mid N$, and $l \nmid N$, since $l$ divides none of $M$, $N_0$ and $r$. Remove from $g$ the terms $q^n$ with $n$ not prime to $M N_0 r$. The result $g'$ is a depleted eigenform of weight $2e+1$, level $N$ and a character $\chi$ with $\chi(d) = \chi_g(d)$ for $d$ prime to $N$, and $g'_n = a_n$ for $n$ prime to $N$. The square in the level makes room for the depletion at the primes of $M$. Apply the last theorem. $\square$

The hypothesis $l \neq 2$ is not used in the proof. The theorem at a given level holds for $l = 2$ as well.

**Remark 6.10.6 (Formalization).** The claim that this theorem proves is named `CuspidalUnitaryTwistsClaim` ([CuspidalUnitaryTwistsClaim.lean](lean:Development/AbelianVarietyTheory/Statements/CuspidalUnitaryTwists/CuspidalUnitaryTwistsClaim.lean#L13)). A near copy, `ChapterMu` ([ChapterMu.lean](lean:Development/AbelianVarietyTheory/Statements/CuspidalUnitaryTwists/ChapterMu.lean#L43)), uses $u = \theta$ in place of $\hat\theta$ and states only the $\theta\chi^{-1}$ condition on $d_1$; it is imported but not used. In `chapterM_holds` the hypothesis $l \neq 2$ is introduced and never used ([OrdinaryEisensteinEigenfunctionalExists.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/OrdinaryEisensteinEigenfunctionalExists.lean#L109)). The condition on $c_1$ holds for any $c_1 > 1$, since $|c_1^e| > 1$. The conditions on $d_1$ compare $d_1^2$ with a number of absolute value $d_1^{e+1}$, so they hold for any $d_1 > 1$ prime to $Nl$ once $e \geq 2$. In the measure the distribution and interpolation properties ask for $f$ of parity $s$, while the bound and field properties ask for all $f$ and all $m \geq 0$. The second name is a wrapper under `maxHeartbeats 1000000`. The choice of $\theta$, the splitting at the unit root, the Atkin and Lehner transfer, the measure lemma and the smoothing integers were read as statements.
