---
title: Rankin values and a nonvanishing eigenfunctional
decls:
  - GlobalTheory.EisM.rankin_values_at_zero
  - GlobalTheory.T.pet_eis_lat_eq_and_vo_eq_mul
  - GlobalTheory.EisM.eigF_value_ne_zero
  - GlobalTheory.T.exists_heckeEigenfunctional_depletedEisenstein_ne_zero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rankin values and a nonvanishing eigenfunctional

The Euler system argument needs a linear functional on modular forms that picks out the $g$-eigencomponent of a newform $g$ of odd weight, at the ordinary root $\alpha$ of its Hecke polynomial at $l$, and that does not vanish on a certain product of two Eisenstein series. This section builds such a functional from Petersson products against $g$ and proves the nonvanishing by the Rankin method: the Petersson product of $g$ with a product of Eisenstein series unfolds to a Dirichlet series, whose value at the edge of absolute convergence is nonzero. The result is used in [the ordinary eigenfunctional theorem](/entry/chapter-m-of-level/) of the next section.

Throughout, forms are given by their coefficient sequences. For $a : \mathbb{N} \to \mathbb{C}$ let $a(\tau) = \sum_{n \geq 0} a_n e^{2\pi i n \tau}$ on $\mathcal{H}$. For a Dirichlet character $\chi$ we extend $\chi$ to $\mathbb{Z}$ by $\chi(d) = 0$ when $d$ is not prime to the modulus.

**Definition 6.9.1 (Coefficient sequences of modular forms).** Let $k, L \geq 1$ and let $\chi : \mathbb{Z} \to \mathbb{C}$. A sequence $a$ is a *modular form of weight $k$, level $L$ and character $\chi$* if $|a_n| \leq C (n + 1)^A$ for some $C, A$, and
$$
a(\gamma\tau) = \chi(d)(c\tau + d)^k a(\tau) \qquad \text{for } \gamma = \begin{pmatrix} * & * \\ c & d \end{pmatrix} \in \mathrm{SL}_2(\mathbb{Z}),\ L \mid c.
$$
It is a *cusp form* if also $|a(\tau)|^2 (\mathrm{Im}\,\tau)^k$ is bounded. Write $M_k(L, \chi)$ for these sequences.

**Definition 6.9.2 (Operators).** For a prime $q$ and a sequence $a$, put $(U_q a)_n = a_{qn}$, $(V_q a)_n = a_{n/q}$ if $q \mid n$ and $0$ otherwise, and
$$
(T_q a)_n = a_{qn} + \chi(q) q^{k-1} (V_q a)_n.
$$

**Definition 6.9.3 (Depleted eigenform).** A *depleted eigenform of weight $k$, level $N$ and character $\chi$* (a Dirichlet character modulo $N$) is a cusp form $g$ of weight $k$, level $N$ and character $\chi$ with $g_1 = 1$, $g_n = 0$ for $n$ not prime to $N$, and $T_q g = g_q\, g$ for primes $q \nmid N$.

If $h$ is a newform of level dividing $N$, removing from $h$ the terms $q^n$ with $\gcd(n, N) > 1$ gives a depleted eigenform at level a suitable multiple of $N$. This is how the newform enters in the next section.

**Definition 6.9.4 (Eisenstein sequences).** For $j \geq 1$, $c \in \mathbb{C}$ and $a, b : \mathbb{Z} \to \mathbb{C}$ let
$$
E_j(c; a, b)_0 = c, \qquad E_j(c; a, b)_n = \sum_{d d' = n} a(d)\, d^{j-1}\, b(d') \quad (n \geq 1).
$$
For characters these are the coefficients of the [Eisenstein series](/learn/automorphic-forms/#eisenstein-series) of weight $j$ with characters $a$, $b$.

**Definition 6.9.5 (Petersson pairing with a weight function).** A *weight function for $\Gamma_0(L)$* is a measurable $\rho : \mathcal{H} \to [0, \infty)$ with $\sum_{\gamma \in \Gamma_0(L)} \rho(\gamma\tau) = 1$ for every $\tau$, whose support lies in finitely many $\mathrm{SL}_2(\mathbb{Z})$-translates of the standard fundamental domain. For $h, f : \mathcal{H} \to \mathbb{C}$ put
$$
\langle h, f \rangle_{k, \rho} = \int_{\mathcal{H}} \rho(\tau)\, \overline{h(\tau)}\, f(\tau)\, (\mathrm{Im}\,\tau)^k \, d\mu(\tau),
$$
for a fixed measure $\mu$ on $\mathcal{H}$.

For a $\Gamma_0(L)$-invariant integrand, $\rho$ cuts the integral down to a fundamental domain, so $\langle h, f \rangle_{k, \rho}$ is a Petersson product written as an integral over all of $\mathcal{H}$.

**Definition 6.9.6 (Eisenstein lattice sum at $s = 0$).** Let $L \geq 1$, $j \geq 1$, and let $\varphi$ be a Dirichlet character modulo $L$. For $F : \mathbb{Z}^2 \to \mathbb{C}$ put $(D F)(x) = F(x) - \frac{1}{L}\sum_{r=0}^{L-1} F(x_1, x_2 + r)$. Define
$$
G_{j, \varphi}(\tau) = \sum_{x \in \mathbb{Z}^2,\ L \mid x_1} \varphi(x_2)\, (D^2 F_\tau)(x), \qquad F_\tau(y) = (y_1 \tau + y_2)^{-j},
$$
with $F_\tau(0) = 0$, as the sum of the family when it is summable, and $0$ otherwise.

The operator $D$ subtracts the average over a period of the second coordinate. When $\varphi \neq 1$ the average of $\varphi$ is $0$, so formally $D$ does not change the sum, but $D^2 F_\tau$ decays fast enough for the sum to converge.

**Theorem 6.9.7 (Rankin values at $s = 0$).** Let $e \geq 1$, $N \geq 1$, and let $l$ be a prime with $l \nmid N$. Let $\chi, \theta$ be characters modulo $N$, $\psi$ a character modulo $l$, and $\varphi$ a character modulo $Nl$ with $\varphi(d) = \theta\chi(d)\, \psi(d)$ for all $d \in \mathbb{Z}$ and $\varphi \neq 1$. Let $g$ be a depleted eigenform of weight $2e + 1$, level $N$ and character $\chi$, let $\rho$ be a weight function for $\Gamma_0(Nl)$, and let $c_0 \in \mathbb{C}$ be such that $E = E_e(c_0; \psi, \theta)$ is a modular form of weight $e$, level $Nl$ and character $\psi\theta$. Let $g^*$ be the sequence $n \mapsto \overline{g_n}$, and put $F = E \cdot G_{e+1, \varphi}$. Then there is $P \neq 0$ with
$$
\langle g^*, F \rangle_{2e+1, \rho} = P, \qquad \langle V_l g^*, F \rangle_{2e+1, \rho} = \frac{\theta(l)}{l^{2e}} P.
$$

Lean: `GlobalTheory.EisM.rankin_values_at_zero` (also `GlobalTheory.T.pet_eis_lat_eq_and_vo_eq_mul`, a second name).

*Proof.* The proof follows the Rankin and Selberg method, with the lattice sum at $s > 0$ as an intermediate step.

*Unfolding.* For $s > 0$, replace $F_\tau(y)$ by $(y_1\tau + y_2)^{-j}|y_1\tau + y_2|^{-2s}$. The lattice sum is then an average over $\Gamma_\infty \backslash \Gamma_0(Nl)$, and the Petersson pairing unfolds to an integral over a strip. This gives a Dirichlet series $\sum_n \overline{h_n}\, b_n\, n^{-w}$ in the coefficients $h$ of $g^*$ or $V_l g^*$ and the coefficients $b$ of $E$, times explicit nonzero factors.

*The Dirichlet series.* The function $g^*$ is a cusp form of character $\chi^{-1}$. By the Hecke relations of $g$, the series $\sum_n g_n b_n n^{-w}$ factors through twisted $L$-series of $g$. The mean square bound for the coefficients of a cusp form gives absolute convergence to the right of the edge.

*Limit $s \to 0$.* The integrals tend to their values at $s = 0$, and the Dirichlet series tends to a value at the edge of absolute convergence. There the twisted $L$-value of $g$ is nonzero, as $\varphi \neq 1$. This gives $P \neq 0$.

*The operator $V_l$.* Since $\psi(d) = 0$ for $l \mid d$, the Eisenstein coefficients satisfy $b_{ln} = \theta(l)\, b_n$ for $n \geq 1$. Then $\sum_n \overline{(V_l h)_n}\, b_n n^{-w} = \theta(l)\, l^{-w} \sum_n \overline{h_n}\, b_n n^{-w}$, by the change of variable $n \mapsto ln$. At the relevant point $w = 2e$ this gives the factor $\theta(l)/l^{2e}$. $\square$

**Definition 6.9.8 (Hecke eigenfunctional).** Let $k \geq 1$, let $\varepsilon$ be a character modulo $N$, $t$ a sequence, and $\alpha \in \mathbb{C}$. A *Hecke eigenfunctional* of weight $k$, level $Nl$, character $\varepsilon$, eigenvalues $t$ and $U_l$-eigenvalue $\alpha$ is a functional $\lambda(a) = \sum_{n < B} c_n a_n$, given by $B \geq 0$ and $c : \mathbb{N} \to \mathbb{C}$, such that for every $a \in M_k(Nl, \varepsilon)$:
$$
\lambda(T_q a) = t_q\, \lambda(a) \quad \text{for primes } q \nmid Nl, \qquad \lambda(U_l a) = \alpha\, \lambda(a).
$$
For $r \geq 0$ put $\lambda_{\alpha, r}(a) = \alpha^{-r} \lambda(U_l^r a)$.

**Definition 6.9.9 (Depleted Eisenstein product).** For $k \geq 2$, $u, v : \mathbb{Z} \to \mathbb{C}$ and $F : \mathbb{N}^2 \to \mathbb{C}$, let $Z_k(u, v, F)$ be the sequence
$$
Z_k(u, v, F)_n = \sum_{\substack{n_1 + n_2 = n \\ l \nmid n_1,\ l \nmid n_2}} \ \sum_{x_1 x_2 = n_1} \ \sum_{y_1 y_2 = n_2} x_1^{k-2}\, u(x_2)\, v(y_1)\, F(x_1, y_1).
$$
It is the coefficient sequence of a product of two Eisenstein series, with the terms $q^{n_1}$ and $q^{n_2}$ for $l \mid n_1$ or $l \mid n_2$ removed. The Gauss sum transform of a character $\varphi$ modulo $L$ is $\hat\varphi(d) = \sum_{y=0}^{L-1}\varphi(y) e^{2\pi i y d / L}$.

**Theorem 6.9.10 (A nonvanishing ordinary eigenfunctional).** Let $l$ be a prime, $\iota : \overline{\mathbb{Q}}_l \to \mathbb{C}$ a field isomorphism, $e \geq 1$, $N \geq 1$ with $l \nmid N$, $\chi, \theta$ characters modulo $N$, $\psi$ a character modulo $l$, and $g$ a depleted eigenform of weight $2e+1$, level $N$ and character $\chi$. Let $\alpha, \beta \in \mathbb{C}$ with
$$
\alpha + \beta = \chi^{-1}(l)\, g_l, \qquad \alpha\beta = \chi^{-1}(l)\, l^{2e}, \qquad |\iota^{-1}(\alpha)|_l = 1.
$$
Assume $\theta(-1) = (-1)^e \psi(-1)$ and $\theta\chi \neq 1$. Then there is a Hecke eigenfunctional $\lambda$ of weight $2e+1$, level $Nl$, character $\chi^{-1}$, eigenvalues $t_q = \chi^{-1}(q) g_q$ and $U_l$-eigenvalue $\alpha$ with
$$
\lambda_{\alpha, 1}\bigl(Z_{2e+1}(\theta, \widehat{\theta\chi}, F)\bigr) \neq 0, \qquad F(x, y) = \psi(x)\psi^{-1}(y)\left(\frac{y}{x}\right)^{e}.
$$

Lean: `GlobalTheory.EisM.eigF_value_ne_zero` (also `GlobalTheory.T.exists_heckeEigenfunctional_depletedEisenstein_ne_zero`, a second name).

*Proof.* *The functional.* Choose a weight function $\rho$ for $\Gamma_0(Nl)$. The form $g^*$ is an eigenform of character $\chi^{-1}$, and $\alpha$, $\beta$ are the roots of its Hecke polynomial at $l$. So a suitable combination of $g^*$ and $V_l g^*$ is a $U_l$-eigenform. A lemma of the development gives a Hecke eigenfunctional $\lambda$ with the stated eigenvalues and
$$
\lambda(a) = \langle V_l g^*, a \rangle_{k, \rho} - \frac{\beta}{l^k}\langle g^*, a\rangle_{k, \rho}, \qquad k = 2e + 1,
$$
for all $a \in M_k(Nl, \chi^{-1})$. A functional of this kind is a finite sum $\sum_{n < B} c_n a_n$ since $M_k(Nl, \chi^{-1})$ is finite dimensional.

*An Eisenstein product.* Let $\varphi$ be the character modulo $Nl$ with $\varphi = \theta\chi \cdot \psi$. It is nontrivial, as $\theta\chi \neq 1$. The parity condition $\theta(-1) = (-1)^e\psi(-1)$ and $\chi(-1) = -1$, which holds for odd weight, make $E = E_e(c_0; \psi, \theta)$ a modular form of weight $e$ for some $c_0$, and make $E' = E_{e+1}(c_1; \hat\varphi, 1)$ a modular form of weight $e + 1$ and character $\varphi^{-1}$. The product $E E'$ lies in $M_k(Nl, \chi^{-1})$. The lattice sum satisfies $G_{e+1, \varphi} = \kappa E'$ for an explicit $\kappa \neq 0$.

*Nonvanishing on the product.* By the Rankin theorem,
$$
\lambda(E E') = \kappa^{-1}\Bigl(\frac{\theta(l)}{l^{2e}} P - \frac{\beta}{l^{2e+1}} P\Bigr) = \frac{P}{\kappa\, l^{2e+1}}\bigl(l\,\theta(l) - \beta\bigr).
$$
Since $\alpha$ is an $l$-adic unit, $|\iota^{-1}(\beta)|_l = |l|^{2e}$, while $|\iota^{-1}(l\theta(l))|_l = |l|$, as $\theta(l)$ is a root of unity. As $2e \neq 1$, $\beta \neq l\theta(l)$, and $\lambda(E E') \neq 0$.

*Depletion.* A last lemma passes from $E E'$ to the depleted product. It uses $\lambda(U_l a) = \alpha\lambda(a)$ and the conditions $\alpha \neq \theta(l)$ and $\alpha \neq l^e \chi^{-1}(l)$, which hold by the same comparison of $l$-adic absolute values. $\square$

The functional has the $U_l$-eigenvalue $\alpha$ of the unit root. Such a functional is *ordinary*. This is what makes the measure of the next section bounded.

**Remark 6.9.11 (Formalization).** The name of the hypothesis "depleted eigenform" in the development is `Prim` ([PetIPSmulRight.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/PetIPSmulRight.lean#L84)); it asks $g_n = 0$ for $n$ not prime to $N$, so it is not the primitive newform. The lattice sum is a `tsum`, which is $0$ for a family that is not summable, and the term at $y = 0$ is $(0^j)^{-1} = 0$ ([PetIPSmulRight.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/PetIPSmulRight.lean#L104)). The pairing integrates against the default measure on $\mathcal{H}$ of the library with the factor $(\mathrm{Im}\,\tau)^k$ as written; I did not check that this measure is the invariant one. The field $\overline{\mathbb{Q}}_l$ is the algebraic closure of $\mathbb{Q}_l$ with its absolute value. Both second names are wrappers under `maxHeartbeats 1000000`. The unfolding, the Dirichlet series identity, the limit at $s = 0$, the existence of the eigenfunctional, the modularity of the Eisenstein sequences and the depletion lemma were read as statements; the proofs given above follow their order in the development.
