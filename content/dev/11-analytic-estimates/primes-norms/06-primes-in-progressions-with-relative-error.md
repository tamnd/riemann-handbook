---
title: Primes in progressions with a relative error
decls:
  - GlobalTheory.Lin.PsiRel.psiAP_relative
  - GlobalTheory.T.chebyshevPsiProgression_relative_error
  - GlobalTheory.Lin.primesRel_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Primes in progressions with a relative error

This section proves the prime number theorem in arithmetic progressions in the form that Linnik's method gives. Let $M \geq 3$ and $(b, M) = 1$. Then $\varphi(M)\psi(u; M, b)$ is equal to $u - \theta u^\beta/\beta$ up to a relative error $C(e^{-c_3\log u/\log M} + e^{-\sqrt{c_3\log u}})$, as soon as $u \geq M^{c_2}$. Here $\beta$ is a possible exceptional zero and $\theta = \chi_1(b)$ is the value of its character at $b$. The range $u \geq M^{c_2}$ is polynomial in $M$, and the error is relative to the main term. The same statement for the number of primes is the result that [the step on the characters of the literature](/step/every-character-of-literature/) uses; in Volume 7 it gives [the theorem on the recursive selection](/entry/rec-s/). The inputs are [the sums over zeros](/entry/sum-rpow-zeros-le/) of Section 5, the explicit formula, the zero-free region and the Deuring-Heilbronn phenomenon. For the classical theory see [primes in progressions](/learn/analytic-number-theory/#primes-in-progressions-and-in-short-intervals).

We keep the notation $Z(\chi; \sigma, T)$ and $\mathrm{ord}_\rho$ of Sections 4 and 5. For $M \geq 1$, an integer $b$ and real $u$, put
$$\psi(u; M, b) = \sum_{\substack{1 \leq n \leq u \\ n \equiv b \bmod M}} \Lambda(n).$$

**Definition 2.6.1 (Exceptional pair).** Let $c_1 > 0$ and $M \geq 3$. A pair $(\chi, \beta)$ of a [[Dirichlet character|JR4QSEFXWF]] $\chi$ modulo $M$ and a real number $\beta$ is *exceptional of level $c_1$* if $\chi^2 = 1$, $1 - c_1/\log M < \beta < 1$, and $L(\beta, \chi^*) = 0$, where $\chi^*$ is the primitive character that induces $\chi$.

**Definition 2.6.2 (Exceptional data).** Let $c_1 > 0$, $M \geq 3$, $b$ an integer, $\theta$ an integer and $\beta$ real. The tuple $(\theta, \beta)$ is *exceptional data of level $c_1$ for $(M, b)$* if one of the following holds:

1. $\theta = 0$, and there is no exceptional pair of level $c_1$ modulo $M$;
2. there is a character $\chi$ modulo $M$ such that $(\chi, \beta)$ is exceptional of level $c_1$ and $\chi(b) = \theta$.

Put $\mathrm{Li}(X) = \int_2^X dt/\log t$ and $E(\theta, \beta; X) = \mathrm{Li}(X) - \theta\,\mathrm{Li}(X^\beta)$.

### The inputs

**Theorem 2.6.3 (Zero-free region with one exceptional zero).** There is $c_0 > 0$ such that for every $c_1 \in (0, c_0]$ there is $c > 0$ with the following properties, for every $M \geq 3$.

1. There is at most one exceptional pair of level $c_1$ modulo $M$.
2. If $(\chi, \beta)$ is exceptional of level $c_1$, then $\chi \neq 1$, $\beta \geq 7/8$, $L(\beta, \chi) = 0$, the zero is simple, and $1 - \beta \geq c/(M^2\log M)$.
3. Let $\chi$ be a character modulo $M$ and $\rho$ a zero of $L(s, \chi)$ with $\mathrm{Re}\,\rho < 1$. Then either $\rho$ is real and $(\chi, \rho)$ is exceptional of level $c_1$, or
$$\mathrm{Re}\,\rho \leq 1 - \frac{c}{\log(M(|\mathrm{Im}\,\rho| + 2))}.$$

Lean: `GlobalTheory.T.exceptionalDirichletZero_unique_zeroFreeRegion`.

This is the classical zero-free region (Davenport, Chapters 13 and 14), with a weak lower bound for $1 - \beta$.

**Theorem 2.6.4 (Repulsion).** There is $c > 0$ with the following property. Let $q \geq 1$, let $\chi_1 \neq 1$ be a real character modulo $q$, and let $1/2 \leq \beta < 1$ with $L(\beta, \chi_1) = 0$. Let $\chi$ be a character modulo $q$ and $\rho$ a zero of $L(s, \chi)$ with $1/2 \leq \mathrm{Re}\,\rho < 1$, such that $(\chi, \rho) \neq (\chi_1, \beta)$ or $\beta$ is a multiple zero. If $\log(q(|\mathrm{Im}\,\rho| + 2)) \leq L$, then
$$1 - \mathrm{Re}\,\rho \geq \frac{c}{L}\log\frac{c}{(1 - \beta)L}.$$

Lean: `GlobalTheory.T.one_sub_re_ge_of_exceptional_zero_repulsion`.

This is the Deuring-Heilbronn phenomenon: an exceptional zero very close to $1$ pushes all other zeros away from the line $\mathrm{Re}\, s = 1$ (Iwaniec and Kowalski, Chapter 18).

**Theorem 2.6.5 (Explicit formula).** There is $C > 0$ such that for every $q \geq 1$, every character $\chi$ modulo $q$ and all $2 \leq T \leq u$, the set $Z(\chi; 1/2, T)$ is finite and
$$\Bigl| \sum_{n \leq u} \Lambda(n)\chi(n) - \delta_\chi u + \sum_{\rho \in Z(\chi; 1/2, T)} \mathrm{ord}_\rho\frac{u^\rho}{\rho} \Bigr| \leq C\Bigl(\frac{u}{T} + \sqrt{u}\, q^3\Bigr)\log^2(quT).$$

Lean: `GlobalTheory.T.explicit_formula_dirichlet_zeros_right_half`.

Compare [the explicit formula](/learn/analytic-number-theory/#the-explicit-formula) and Davenport, Chapter 19.

**Theorem 2.6.6 (From $\psi$ to $\pi$).** Let $c_2, c_3, C, c_S > 0$. There are $c_2', c_3', C' > 0$ with the following property. Let $B \geq 3$, $1 \leq \varphi \leq B$, let $P$ be a set of positive integers, and let $\theta$ be an integer and $\beta$ real such that $\theta = 0$, or $\theta = \pm 1$, $\beta \geq 7/8$ and $1 - \beta \geq c_S/B^3$. Suppose that for all $u \geq B^{c_2}$,
$$\Bigl| \varphi\sum_{\substack{n \leq u \\ n \in P}} \Lambda(n) - \Bigl(u - \frac{\theta u^\beta}{\beta}\Bigr) \Bigr| \leq C\bigl(e^{-c_3\log u/\log B} + e^{-\sqrt{c_3\log u}}\bigr)\Bigl(u - \frac{\theta u^\beta}{\beta}\Bigr).$$
Then for all $X \geq B^{c_2'}$, the number $\pi_P(X)$ of primes $p \leq X$ in $P$ satisfies
$$\bigl| \varphi\,\pi_P(X) - E(\theta, \beta; X) \bigr| \leq C'\bigl(e^{-c_3'\log X/\log B} + e^{-\sqrt{c_3'\log X}}\bigr) E(\theta, \beta; X).$$

Lean: `GlobalTheory.T.primeCount_relative_error_of_psi_relative_error`.

The proof is partial summation against $1/\log t$, after removal of the prime powers. The derivative of $u - \theta u^\beta/\beta$ is $1 - \theta u^{\beta - 1}$, and the integral of its quotient by $\log t$ is $E(\theta, \beta; X)$ up to a bounded term.

### Two elementary lemmas

**Lemma 2.6.7 (Size of the main term).** Let $\theta \leq 1$, $7/8 \leq \beta < 1$ and $V \geq 8$. Then
$$\frac{e^V \min(1, (1 - \beta)V)}{4} \leq e^V - \frac{\theta e^{\beta V}}{\beta}.$$

*Proof.* Put $x = (1 - \beta)V > 0$. Since $\theta \leq 1$, the right side is at least $e^V(1 - e^{-x}/\beta)$. Since $\beta \geq 7/8$ and $V \geq 8$, we have $1/\beta = 1 + (1 - \beta)/\beta \leq 1 + 8x/(7V) \leq 1 + x/7$. So it is sufficient to show $1 - e^{-x}(1 + x/7) \geq \min(1, x)/4$. If $x \leq 1$, then $e^{-x} \leq 1 - x + x^2/2 \leq 1 - x/2$, so the left side is at least $x/2 - x/7 \geq x/4$. If $x \geq 1$, the function $e^{-x}(1 + x/7)$ is decreasing, so it is at most $8/(7e) < 3/4$. $\square$

**Lemma 2.6.8 (Choice of the width).** Let $c, d > 0$. There are $c' \in (0, c/2]$, $K \geq 1$ and $R_1$ such that for every $\delta > 0$ and every $R \geq \max(R_1, 0)$ there is $a \geq 0$ with $a = c$ or $a = d\log(d/\delta)$, and
$$e^{-aR/2} \leq K\min(1, \delta)\, e^{-c'R}.$$

*Proof.* Put $d_0 = \min(1, d/e)$, $c' = \min(c/2, d/4)$, $K = 1/d_0$ and $R_1 = 4/d$. If $\delta \geq d_0$, take $a = c$. Then $K\min(1, \delta) \geq 1$ and $e^{-cR/2} \leq e^{-c'R}$. If $\delta < d_0$, take $a = d\ell$ with $\ell = \log(d/\delta)$. Then $\ell \geq 1$, since $d/\delta > d/d_0 \geq e$. Since $dR \geq 4$, we have $dR\ell/2 \geq \ell + dR/4$. So $e^{-aR/2} \leq e^{-\ell}e^{-dR/4} = (\delta/d)e^{-dR/4} \leq K\delta\, e^{-c'R}$, because $d_0 \leq d$. $\square$

The lemma expresses the following alternative. If $1 - \beta$ is not too small, the zero-free region gives a width $c/L$ for all zeros. If $1 - \beta$ is very small, the main term loses a factor $(1 - \beta)L$, but repulsion gives a larger width $d\log(d/((1 - \beta)L))/L$, and the gain $e^{-aR/2}$ compensates the loss.

### The theorem for $\psi$

**Theorem 2.6.9 (Relative error for $\psi$ in progressions).** There is $c_0 > 0$ such that for every $c_1 \in (0, c_0]$ there are $c_2, c_3, C > 0$ with the following property. Let $M \geq 3$, $(b, M) = 1$, let $(\theta, \beta)$ be exceptional data of level $c_1$ for $(M, b)$, and let $u \geq M^{c_2}$. Then
$$\Bigl| \varphi(M)\psi(u; M, b) - \Bigl(u - \frac{\theta u^\beta}{\beta}\Bigr) \Bigr| \leq C\bigl(e^{-c_3\log u/\log M} + e^{-\sqrt{c_3\log u}}\bigr)\Bigl(u - \frac{\theta u^\beta}{\beta}\Bigr).$$

Lean: `GlobalTheory.Lin.PsiRel.psiAP_relative` (also `GlobalTheory.T.chebyshevPsiProgression_relative_error`, a second name).

*Proof.* Let $c_0$ be the constant of the zero-free region, fix $c_1 \in (0, c_0]$, and let $c$ be the corresponding constant. Let $d$ be the constant of repulsion, $C_e$ that of the explicit formula, $A, C_a, \eta_0$ those of [the sums over zeros](/entry/sum-rpow-zeros-le/), and $c', K, R_1$ those of the lemma on the width, for $c$ and $d$.

Step 1 (scales). Write $u = e^V$ and $m = \log M \geq 1$. Put
$$L = 10m + \sqrt{V}, \qquad T = e^{8m + \sqrt{V}}.$$
We choose $c_2$ so large that $V \geq c_2 m$ implies $V \geq R_0 L$ with $R_0 = \max(R_1, A, 8)$; see Step 5. Then $2 \leq T \leq u$, $(MT)^A \leq e^{AL} \leq u$, and $V/L \geq R_1$. Since $M \geq 3$ and $T \geq 2$, every $\rho$ with $|\mathrm{Im}\,\rho| \leq T$ satisfies $\log(M(|\mathrm{Im}\,\rho| + 2)) \leq \log(M^2T) = L$. So, by the zero-free region, every zero $\rho \in Z(\chi; 1/2, T)$ is either real with $(\chi, \rho)$ exceptional, or satisfies $\mathrm{Re}\,\rho \leq 1 - c/L$.

Step 2 (orthogonality). By orthogonality of characters,
$$\varphi(M)\psi(u; M, b) = \sum_{\chi \bmod M} \overline{\chi}(b) \sum_{n \leq u} \Lambda(n)\chi(n).$$
Insert the explicit formula for each $\chi$. The term $\delta_\chi u$ gives $u$. If there is an exceptional pair $(\chi_1, \beta)$ with $\chi_1(b) = \theta$, then $\overline{\chi_1}(b) = \theta$, and the simple zero $\beta$ gives $\theta u^\beta/\beta$. Each other zero has $|\rho| \geq 1/2$, so $|u^\rho/\rho| \leq 2u \cdot u^{\mathrm{Re}\,\rho - 1}$. There are at most $M$ characters. So, if all zeros other than $\beta$ satisfy $\mathrm{Re}\,\rho \leq 1 - \eta$, then
$$\Bigl| \varphi(M)\psi(u; M, b) - \Bigl(u - \frac{\theta u^\beta}{\beta}\Bigr) \Bigr| \leq M C_e\Bigl(\frac{u}{T} + \sqrt{u}M^3\Bigr)\log^2(MuT) + 2u\sum_\chi \sum_{\substack{\rho \in Z(\chi; 1/2, T) \\ \mathrm{Re}\,\rho \leq 1 - \eta}} \mathrm{ord}_\rho\, u^{\mathrm{Re}\,\rho - 1}.$$
The same holds with $\theta = 0$ if there is no exceptional pair.

Step 3 (the general bound). Let $a \geq 0$ and $w > 0$ satisfy

1. $w \geq \min(1, c)e^{-3m}$;
2. $e^{-aV/(2L)} \leq Kw\, e^{-c'V/L}$;
3. $uw/4 \leq u - \theta u^\beta/\beta$;
4. all zeros in the boxes, other than the exceptional zero $\beta$ of $\chi_1$ if there is one, satisfy $\mathrm{Re}\,\rho \leq 1 - a/L$.

By Step 2 with $\eta = a/L$ and by the sums over zeros, the error is at most
$$u\Bigl[ C_e e^m\bigl(e^{-8m - \sqrt{V}} + e^{-V/2}e^{3m}\bigr)(9m + V + \sqrt{V})^2 + 2C_a\bigl(Kw\,e^{-c'V/L} + e^{-\eta_0 V}\bigr) \Bigr].$$
By Step 5 and condition 1, the bracket is at most $C(e^{-c_3V/m} + e^{-\sqrt{c_3V}})w/4$. By condition 3, this gives the theorem.

Step 4 (the two cases). If there is no exceptional pair, then $\theta = 0$. Take $a = c$ and $w = 1$. Condition 2 holds since $c' \leq c/2$ and $K \geq 1$, and condition 4 is Step 1. Otherwise $(\theta, \beta)$ comes from an exceptional pair $(\chi_1, \beta)$ with $\chi_1(b) = \theta$. By the zero-free region, $\chi_1 \neq 1$, $\beta \geq 7/8$, $\beta$ is a simple zero of $L(s, \chi_1)$, and $1 - \beta \geq c/(M^2\log M) \geq c e^{-3m}$, since $\log M \leq M$. Also $\theta \leq |\chi_1(b)| \leq 1$. Apply the lemma on the width with $\delta = (1 - \beta)L$ and $R = V/L$. It gives $a$, and we take $w = \min(1, (1 - \beta)L)$. Condition 1 holds since $L \geq 1$. Condition 2 is the lemma. Condition 3 follows from the lemma on the main term, since $L \leq V$. For condition 4, let $\rho \neq \beta$ or $\chi \neq \chi_1$. If $a = c$, use Step 1 and the uniqueness of the exceptional pair. If $a = d\log(d/((1 - \beta)L))$, use repulsion with this $L$.

Step 5 (the final inequality). Choose $R \geq \max(R_0, 2, 1/\eta_0)$, and put
$$c_3 = \min\Bigl(\frac{1}{4}, \frac{c'}{20}, \frac{c'^2}{4}\Bigr), \qquad c_2 = 20R + 4R^2.$$
If $V \geq c_2 m$, then $V \geq 20Rm$ and $\sqrt{V} \geq 2R$. So $R \cdot 10m \leq V/2$ and $R\sqrt{V} \leq V/2$, which gives $RL \leq V$. Let $P = e^{-c_3V/m} + e^{-\sqrt{c_3V}}$. Since $V/L \geq \min(V/(20m), \sqrt{V}/2)$, we get $e^{-c'V/L} \leq P$. Since $\eta_0 V \geq L \geq 3m + \sqrt{V}$, we get $e^{-\eta_0V} \leq e^{-3m}P$. In the first term, $e^m e^{-8m - \sqrt{V}} = e^{-3m}e^{-4m - \sqrt{V}}$ and $e^m e^{-V/2}e^{3m} \leq e^{-3m}e^{-V/4}$, and the factors $e^{-4m - \sqrt{V}/2}(9m + V + \sqrt{V})^2$ are bounded. So the bracket is at most a constant times $e^{-3m}P + wP$, and by condition 1 at most a constant times $wP$. $\square$

### The theorem for primes

**Theorem 2.6.10 (Primes in progressions with a relative error).** There are $c_1 \in (0, 1/8]$ and $c_2, c_3, C_A, c_S > 0$ with the following properties, for every $M \geq 3$.

1. There is at most one exceptional pair of level $c_1$ modulo $M$.
2. If $(\chi, \beta)$ is exceptional of level $c_1$, then $1 - \beta \geq c_S/(M^2\log M)$.
3. Let $(b, M) = 1$, let $(\theta, \beta)$ be exceptional data of level $c_1$ for $(M, b)$, and let $X \geq M^{c_2}$. Then
$$\bigl| \varphi(M)\,\pi(X; M, b) - E(\theta, \beta; X) \bigr| \leq C_A\bigl(e^{-c_3\log X/\log M} + e^{-\sqrt{c_3\log X}}\bigr)E(\theta, \beta; X).$$

Lean: `GlobalTheory.Lin.primesRel_holds`.

*Proof.* Let $a$ be the constant $c_0$ of the zero-free region, and $a'$ the constant $c_0$ of the theorem for $\psi$. Put $c_1 = \min(1/8, a, a')$. Let $c$ be the constant of the zero-free region for this $c_1$, and $c_2, c_3, C$ those of the theorem for $\psi$. Apply the theorem from $\psi$ to $\pi$ with $c_2, c_3, C$ and $c_S = c$. It gives $c_2', c_3', C'$, and these are the constants of the claim, with $C_A = C'$.

Properties 1 and 2 are parts 1 and 2 of the zero-free region. For property 3, take $B = M$, $\varphi = \varphi(M)$ and $P$ the set of $n \equiv b \pmod M$. Then $1 \leq \varphi(M) \leq M$. If $\theta \neq 0$, then $\theta = \chi(b)$ for a character with $\chi^2 = 1$, and $\chi(b)^2 = 1$ gives $\theta = \pm 1$. Also $\beta \geq 7/8$, and $1 - \beta \geq c/(M^2\log M) \geq c/M^3$. The hypothesis on $\psi$ is the theorem for $\psi$. So the theorem from $\psi$ to $\pi$ gives property 3. $\square$

The lower bound in property 2 is far from Siegel's bound $1 - \beta \gg_\varepsilon M^{-\varepsilon}$, but it is effective, and the constants of the theorem are effective.

**Remark 2.6.11 (Formalization).** The four inputs are separate formal results, proved elsewhere in the development; we have not checked their proofs. An exceptional pair asks for a zero of the $L$-function of the primitive character, while the zero-free region concludes that $\beta$ is a zero of $L(s, \chi)$ for the imprimitive character ([ZerosDisc.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ZerosDisc.lean#L26)). The repulsion statement is empty when $(1 - \beta)L \geq c$, since then its right side is not positive ([RepulsionStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/RepulsionStatement.lean#L8)). The function $E(\theta, \beta; X)$ is `Formalism.HermitianLattices.GL2PrimeSums.Emain`, in a file of the folder GL3MeanSquares ([SmoothedRemainderRealIntegralFormula.lean](lean:Formalism/GL3MeanSquares/SmoothedRemainderRealIntegralFormula.lean#L107)). The steps of the proof for $\psi$ are the lemmas `orth`, `zsum`, `combine`, `struct`, `mainLower`, `realEnd` and `etaChoice` in the namespace `GlobalTheory.Lin.PsiRel`. The proof for primes weakens $c/(M^2\log M)$ to $c/M^3$ ([PrimesInProgressionsRelativeError.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/PrimesInProgressionsRelativeError.lean#L36)), and the sign lemma is `GlobalTheory.Lin.sign_of_sq_eq_one`. The wrapper `GlobalTheory.T.chebyshevPsiProgression_relative_error` is stated in a file of its own and proved by citing the theorem.
