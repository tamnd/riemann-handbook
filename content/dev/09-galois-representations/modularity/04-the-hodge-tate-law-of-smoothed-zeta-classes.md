---
title: The Hodge-Tate law of smoothed zeta classes
decls:
  - UpperTheory.V.Z.Kato.K5.hco
  - UpperTheory.V.Z.Kato.K5.top
  - UpperTheory.V.Z.Kato.K5.smoothedZetaClass_hodgeTateLaw
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hodge-Tate law of smoothed zeta classes

This section proves the Hodge-Tate law of smoothed zeta classes, which Section 3 uses to show that the Euler system class of the unramified zeta theorem is not ordinary at $l$. The law says that a smoothed sum of zeta classes, restricted to inertia at $l$, is a multiple of the cyclotomic logarithm up to a coboundary, and it gives the multiple as a twisted value of a Hecke functional on Eisenstein series. The proof has two steps. The first step is a coefficient law for each zeta system: on inertia, the first coordinate of the system is the cyclotomic logarithm times an average over the units modulo $N$ of Eisenstein values. The second step is the general [Hodge-Tate law from its inputs](/entry/law-of-inputs/), which turns the coefficient law and the existence of presentations into the law for the smoothed system.

### Setting

We keep the notation of Sections 2 and 3. Let $l$ be an odd prime, $\Omega$ an algebraic closure of $\mathbb{Q}$, $\varepsilon \colon \Omega \to \mathbb{C}$ an embedding and $\iota \colon \overline{\mathbb{Q}}_l \to \mathbb{C}$ an isomorphism. Let $X$ be a tower of modular functions over $\Omega$ for $\varepsilon$, as in [towers of modular functions](/entry/tower-exists/), and assume that its $j$-function is a holomorphic function on the upper half plane. Let $j \colon \Omega \to \overline{\mathbb{Q}}_l$ be a ring map and $A = \{z \in \Omega : |j(z)| \leq 1\}$, a valuation ring of $\Omega$ over $l$, with decomposition group $D_A$ and inertia group $I_A$.

For $m \geq 1$ let $\varepsilon_m$ be the [[cyclotomic character|XSGB5K2KEG]] modulo $l^m$ and $H_m = I_A \cap \ker \varepsilon_m$. A *system* is a family of maps $Z_r \colon G_{\mathbb{Q}} \times (\mathbb{Z}/l^r)^\times \to \overline{\mathbb{Q}}_l$. We use the notions of the chapter on Hecke algebras (Section 17 there): a coefficient datum with ring $\mathcal{O}$, the *Hodge-Tate law on inertia* at $(m, c_0, y)$ with a value $h$, the *presentations* of a system, and the *Hodge-Tate law of a system* with a right side $R(m, \psi, z)$. We write $a \equiv_n b$ when $|a - b| \leq |l^n|$.

Fix $e \geq 1$, a level $N$ with $l \nmid N$, integers $c, d$, matrices $g_m(r_0) \in \mathrm{SL}_2(\mathbb{Z})$ for $r_0 \in (\mathbb{Z}/l)^\times$, a projection $\mathrm{pr}$ from the Kummer module of $X$ to $\overline{\mathbb{Q}}_l^2$, a newform $g$ of weight $2e + 1$, a representation $W$ and a character $\psi_0$ of $(\mathbb{Z}/l)^\times$. Let $\rho$ be the twist of $W$ by $\psi_0$ and the power $\varepsilon^{-e}$ that is used for zeta classes. The data are *admissible at $x \in \mathbb{Z}/N$* if $c, d > 1$ are prime to $6lN$, $\mathrm{pr}$ is $\mathbb{Z}_l$-linear and Galois equivariant for $\rho$ on the basis of weight $2e - 1$, with values in $\mathcal{O}$, the Hecke operators $T_q$ for $q \nmid lN$ act through the eigenvalues of $g$ and the diamond operators through scalars, the second rows of the matrices $g_m(r_0)$ are congruent to unit multiples of $(r_0, -1)$ modulo $l$ and their lower left entries are divisible by $N$, and the lower right entry of $W$ on $I_A$ is given by a character that kills $\mu_l$ and lifts $\psi_0$. The data $(e, X, \mathrm{pr}, N, g_m, \alpha)$ are *admissible for zeta classes of weight $2e + 1$* as in the chapter on Euler systems (Section 3 there). Zeta systems for $x$ with an exponent $c_0$ are as in the chapter on Euler systems (Section 4 there).

Let $\chi \colon \mathbb{N} \to \mathbb{Z}_l$ be multiplicative and $N$-periodic, with $\chi(\delta)$ a unit for $\delta$ prime to $N$. Let $\lambda$ be a linear form on sequences in $\overline{\mathbb{Q}}_l$ with the finiteness and congruence condition of the chapter on Hecke algebras for level $N$, weight $2e - 1$ and the character $\chi$. This condition gives a finite set $S$ that supports $\lambda$, the fact that each value $\lambda(e_i)$ on a unit vector is unramified over $\mathcal{O}$, an integer $c_L$ and units $p(n)$ with $|p(n)| = 1$ and $p(n + 1) \equiv_n p(n)$.

For $m \geq 1$, $\beta \in \mathbb{Z}$, $t \in \mathbb{Z}$ and $\delta \in (\mathbb{Z}/N)^\times$, let $\bar\delta$ be the least residue of $\delta^{-1}$ and let $Q_{\delta}(i)$ be the $i$-th coefficient of the Eisenstein-type series of weight $2e + 1$
$$
P^{(2e+1)}_{m}\bigl(x t \bar\delta,\, t\bar\delta;\, \zeta_{Nl^m}^{\beta}\bigr)
$$
of the [coefficient law on inertia](/entry/thdiam/), formed with $c$, $d$ and the matrices of determinant $1$ in the unit set modulo $l^m$. Here $\zeta_{Nl^m} \in \Omega$ is the root of unity with $\varepsilon(\zeta_{Nl^m}) = e^{2\pi i/(Nl^m)}$.

### The coefficient law

**Theorem 8.4.1 (Coefficient law for zeta systems).** Assume the data above, with $(e, X, \mathrm{pr}, N, g_m, \alpha)$ admissible for zeta classes of weight $2e + 1$, and assume that each $s \in I_A$ with $\varepsilon_1(s) = 1$ satisfies $\rho(s)_{21} = 0$ and $\rho(s)_{22} = 1$. Then for each $c_0$ there are $c' \in \mathbb{N}$ and $\kappa_0 \neq 0$ with the following property. Let $x \in \mathbb{Z}/N$ be such that the data are admissible at $x$, and let $Y$ be a zeta system for $x$ with exponent $c_0$. Let $m \geq 1$, $y \in (\mathbb{Z}/l^m)^\times$, and let $\beta, t$ be integers with $\beta \equiv y \bmod l^m$, $\beta \equiv 1 \bmod N$ and $l^m t \equiv 1 \bmod N$. Then the system $Y(\cdot)_1$ satisfies the Hodge-Tate law on inertia at $(m, c', y)$ with value
$$
\begin{aligned}
h = {}& p(m)^{-1}\, l^{c_0}\, \kappa_0 \sum_{\delta \in (\mathbb{Z}/N)^\times} \chi(\delta)^{-1} \\
&\cdot \lambda\bigl(i \mapsto l^m\, j(Q_\delta(i))\bigr).
\end{aligned}
$$

Lean: `UpperTheory.V.Z.Kato.K5.hco`.

The constants $c'$ and $\kappa_0$ do not depend on $x$, $m$, $y$ or $Y$. The units $p(m)$ are those of the condition on $\lambda$.

*Proof.* The linear form $\lambda$ is supported on the finite set $S$. Choose $k$ with $\sum_{i \in S} |\lambda(e_i)| \leq l^k$, so $|l^k \lambda(e_i)| \leq 1$ for each $i \in S$. Let $M$ be the number of units modulo $N$. Then $M \neq 0$ in $\overline{\mathbb{Q}}_l$, and since $|l| < 1$ there is $v$ with $|l^v| \leq |M|$. So $|l^v/M| \leq 1$.

If there is no $x$ at which the data are admissible, the statement holds with $c' = 0$ and $\kappa_0 = 1$, because there is nothing to prove. Otherwise fix $x_0$ at which the data are admissible. The admissibility at $x_0$ and the admissibility for zeta classes are the hypotheses of the [coefficient law on inertia](/entry/thdiam/) with the unit index. This gives $c_1$ and $\kappa' \neq 0$, which depend only on $l$, $N$ and $e$. Put
$$
c' = c_1 + k + v, \qquad \kappa_0 = \kappa'/M.
$$

Now let $x$, $Y$, $m$, $y$, $\beta$ and $t$ be as in the statement. Let $E$ be the value $l^{c_0}\kappa'\sum_\delta \chi(\delta)^{-1}\lambda(i \mapsto l^m j(Q_\delta(i)))$ and choose $k_E$ with $|E| \leq l^{k_E}$. Put $n = m + k_E + c_L$. The zeta system condition at level $m$ and precision $n$ gives a class $b$ in the Kummer module of weight $2e - 1$ that represents $Y_m$ to precision $n$. For each $\delta$, the coefficient law on inertia gives a modular form $g_\delta$ with coefficients in $A$ such that, for $s \in H_m$,
$$
l^{c_1} j(\varphi_i) \equiv_n l^{c_1}\bigl(l^{c_0 + m}\kappa' j(Q_\delta(i)) + j(s(g_{\delta, i})) - j(g_{\delta, i})\bigr),
$$
where $\varphi$ is the class attached to $b$ and to the twist by $\delta$.

Apply $\lambda$ to these congruences, multiply by $\chi(\delta)^{-1}$ and sum over $\delta$. Since $\chi(\delta)$ is a unit of $\mathbb{Z}_l$, the factor $\chi(\delta)^{-1}$ has absolute value $1$. Since $\lambda$ is supported on $S$, the coboundary part is a finite sum over the index set $S \times (\mathbb{Z}/N)^\times$, with points the coefficients $g_{\delta, i}$ and weights
$$
o_{i, \delta} = \frac{l^v}{M}\, p(n)^{-1}\, l^k\lambda(e_i)\, \chi(\delta)^{-1}.
$$
Each weight has absolute value at most $1$, by the choice of $k$ and $v$ and because $|p(n)| = 1$. Each weight is unramified over $\mathcal{O}$: the elements unramified over $\mathcal{O}$ form a field, and $l$, $M$, $\chi(\delta)$ and $\lambda(e_i)$ are unramified. The condition on $\lambda$ relates the sum of the values of the classes $\varphi$ to $p(n)$ times $Y_m(s, y)_1$. The division by $M$ costs at most $v$ powers of $l$, and the bound on the weights costs at most $k$ powers. Finally $p(n) \equiv_m p(m)$, since $n \geq m$ and $p(r + 1) \equiv_r p(r)$ for each $r$. So
$$
l^{c'} Y_m(s, y)_1 \equiv_m l^{c'} h\, \lambda_m(s) + \sum_{i, \delta} o_{i, \delta}\bigl(j(s g_{\delta, i}) - j(g_{\delta, i})\bigr)
$$
for $s \in H_m$, where $\lambda_m$ is the cyclotomic logarithm at level $m$. The inertia hypothesis on $\rho$ is used here: it makes the second coordinate of the Galois action trivial on $H_m$, so the first coordinate of the cocycle is a function on $H_m$ to which the law applies. This is the Hodge-Tate law on inertia at $(m, c', y)$ with value $h$. $\square$

### The law for the smoothed system

Let $c_w \colon \mathbb{Z}/N \to \mathcal{O}$ be weights. The data are *admissible with weights $c_w$* if they are admissible at each $x$ with $c_w(x) \neq 0$. For an integer $d_0 \geq 2$ prime to $l$, the *smoothed system* of a system $Y$ is
$$
Z_r(s, y) = Y_r(s, y)_1 - d_0\, Y_r(s, y d_0)_1.
$$
For $m \geq 1$, a [[Dirichlet character|JR4QSEFXWF]] $\psi$ modulo $l^m$ and $x \in \mathbb{Z}/N$, let $E_{m, \psi, x}$ be the $\chi$-average of the twisted Eisenstein coefficients of weight $2e + 1$, as in the [Hodge-Tate law from its inputs](/entry/law-of-inputs/).

**Theorem 8.4.2 (Hodge-Tate law of smoothed zeta classes).** Let $W$ be in normal form for $(e, S, A)$, with a source $g$ of weight $2e + 1$ that is unramified at $l$. Assume that the data are admissible with weights $c_w$ and admissible for zeta classes of weight $2e + 1$. Let $Y$ be a weighted zeta system with exponent $c_0$ that is a cocycle for $\rho$ and $\varepsilon_r^{-1}$, locally constant, with first coordinate in $\mathcal{O}$. Let $\chi$ and $\lambda$ be as above, and let $d_0 \geq 2$ be prime to $l$. Then there are $m_0, c_1 \in \mathbb{N}$, $\kappa \neq 0$ and $v_m \in \overline{\mathbb{Q}}_l$ with $|v_m| = 1$ and $v_{m+1} \equiv_m v_m$, such that the smoothed system satisfies the Hodge-Tate law with $(m_0, c_1)$ and right side
$$
\begin{aligned}
R(m, \psi, z) = {}& \bigl(1 - d_0\psi^{-1}(d_0)\bigr)\, v_m\, \kappa\, \psi^{-1}(N) \sum_{a \in \mathbb{Z}/l^m} \psi(a) z^a \\
&\cdot \lambda\Bigl(i \mapsto \sum_{x \in \mathbb{Z}/N} c_w(x)\, E_{m, \psi, x}(l^m i)\Bigr).
\end{aligned}
$$

Lean: `UpperTheory.V.Z.Kato.K5.top` (also `UpperTheory.V.Z.Kato.K5.smoothedZetaClass_hodgeTateLaw`, a second name).

At $z = j(\zeta_m)$, for a primitive root of unity $\zeta_m$ of order $l^m$, the sum over $a$ is a Gauss sum of $\psi$. The Gauss sum of a primitive character is not zero, and the factor $1 - d_0\psi^{-1}(d_0)$ is not zero when $\psi(d_0) \neq d_0$. So the right side is not zero when the value of $\lambda$ is not zero. This is the form in which Section 3 uses the law.

*Proof.* The [Hodge-Tate law from its inputs](/entry/law-of-inputs/) has exactly this conclusion for the data of the theorem, and it has two inputs. The first input is the conclusion of the coefficient law for each index with admissible data and each zeta system with exponent $c_0$, under the hypothesis that each $s \in I_A$ with $\varepsilon_1(s) = 1$ has second row $(0, 1)$ under $\rho$. This is the previous theorem. The second input is that there are $m_0$ and $c'_0$ such that for each $m \geq m_0$ and each primitive root of unity $\zeta$ of order $l^m$ the smoothed system has a presentation at $(m, c'_0, \zeta)$. This is the existence of presentations for smoothed cocycles, which uses only that $Y$ is a locally constant cocycle with integral first coordinate. Apply that theorem to these two inputs. $\square$

The proof of the law from its inputs smooths the coefficient laws at $y$ and at $y d_0$, sums against $\psi$ and replaces the value $h$ by the Hodge-Tate value of a presentation. The factor $1 - d_0 \psi^{-1}(d_0)$ comes from the substitution $b \mapsto b d_0^{-1}$ in this sum, and the Gauss sum comes from the sum over $b$ of $\psi(b)$ times the Eisenstein values.

**Remark 8.4.3 (Formalization).** In the coefficient law the predicate of admissible data at $x$ takes the index $x$ as an argument but does not use it in its body ([AdmissibleNewformZetaData.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/AdmissibleNewformZetaData.lean#L15)). So admissibility at one index is admissibility at all indices, and the proof can take the constants of the coefficient law on inertia at one index $x_0$ and use them for every $x$ ([Hco.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SmoothedZetaClasses/Hco.lean#L79)). The case with no admissible index is handled by a separate branch with $c' = 0$ and $\kappa_0 = 1$ ([Hco.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SmoothedZetaClasses/Hco.lean#L74)). The theorem is stated with the full data of the Eisenstein pieces, and the long predicates for $\lambda$ and for zeta systems are summarized in words here and are not unfolded. The Hodge-Tate law of smoothed zeta classes is proved in a file named `Imports.lean`, by one application of `GlobalTheory.HTLawZeta.law_of_inputs` to the coefficient law and `GlobalTheory.LambdaValuationPowers.Smooth.exists_pres_smoothed` ([Imports.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SmoothedZetaClasses/Imports.lean#L31)). The second name restates the same theorem through the named statement `UpperTheory.V.Z.Kato.Joint.SmoothedZetaClassHodgeTateLawStatement` and is proved by the first name ([SmoothedZetaClassHodgeTateLaw.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SmoothedZetaClasses/SmoothedZetaClassHodgeTateLaw.lean#L4)).
