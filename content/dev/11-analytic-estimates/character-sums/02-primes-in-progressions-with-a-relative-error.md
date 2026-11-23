---
title: Primes in progressions with a relative error
decls:
  - Formalism.HermitianLattices.Ext.PrimesInProgressions.pnt_progressions_relative_weak_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Primes in progressions with a relative error

This section counts the primes $p \leq X$ with $p \equiv b \pmod M$, for moduli $M$ divisible by $8$. The error is small relative to the main term, and the main term contains the contribution of a possible exceptional zero. The range of $X$ is $\log X \geq C_0\log M\log(\log M + 2)$, which is a little more than a power of $M$. The result is used to count the primes in the sets of primes of the mean square bound of Section 5 ([Theorem 6.5.9](/entry/stage/)). It is a theorem of the type of Linnik's theorem; the Background section on [primes in progressions](/learn/analytic-number-theory/#primes-in-progressions-and-in-short-intervals) gives the setting.

For $X \geq 2$ let $\mathrm{li}\,X = \int_2^X dt/\log t$. For integers $M \geq 1$ and $b$ let $\pi(X; M, b)$ be the number of primes $p \leq X$ with $p \equiv b \pmod M$.

**Definition 6.2.1 (Exceptional pair).** Let $M \geq 2$. An *exceptional pair* modulo $M$ is a pair $(\chi_1, \beta_1)$ of a [[Dirichlet character|JR4QSEFXWF]] $\chi_1 \neq \chi_0$ modulo $M$ with $\chi_1^2 = \chi_0$ and a real number $\beta_1$ with
$$L(\beta_1, \chi_1) = 0, \qquad 1 - \frac{1}{8\log M} < \beta_1 < 1.$$

The theorem below chooses one exceptional pair when there is one. It does not claim that the pair is unique.

**Definition 6.2.2 (Main term).** Let $M \geq 2$, and let $e$ be either an exceptional pair $(\chi_1, \beta_1)$ modulo $M$ or the symbol $\varnothing$. For $b$ an integer and $X \geq 2$ put
$$\mathrm{main}_e(b, X) = \frac{\mathrm{li}\,X}{\varphi(M)} \quad (e = \varnothing), \qquad \mathrm{main}_e(b, X) = \frac{\mathrm{li}\,X - \chi_1(b)\,\mathrm{li}(X^{\beta_1})}{\varphi(M)} \quad (e = (\chi_1, \beta_1)).$$

The second term is the contribution of the zero $\beta_1$ to the explicit formula. If $\chi_1(b) = 1$ the progression has fewer primes than expected, and if $\chi_1(b) = -1$ it has more.

**Theorem 6.2.3 (Primes in progressions with a relative error).** There are constants $c_3 > 0$, $A_0$ and $C_0$ with the following property. For each $M$ with $8 \mid M$ there is $e$, an exceptional pair modulo $M$ or $\varnothing$, such that $e = \varnothing$ only if there is no exceptional pair modulo $M$, and such that for every real $X \geq 2$ with
$$C_0\log M\log(\log M + 2) \leq \log X$$
and every integer $b \geq 0$ prime to $M$,
$$\bigl|\pi(X; M, b) - \mathrm{main}_e(b, X)\bigr| \leq A_0\Bigl(e^{-c_3\log X/\log M} + e^{-\sqrt{c_3\log X}}\Bigr)\,\mathrm{main}_e(b, X).$$

Lean: `Formalism.HermitianLattices.Ext.PrimesInProgressions.pnt_progressions_relative_weak_holds`.

The classical form is the prime number theorem for progressions with the exceptional term, in a range $X \geq M^{c}$ that is polynomial in $M$ (Gallagher, Invent. Math. 11 (1970); Iwaniec and Kowalski, Chapter 18). The theorem here has a wider lower bound on $X$, by the factor $\log(\log M + 2)$, because its zero estimates of [the previous section](/entry/log-density-bound/) lose powers of $\log(MT)$.

*Proof.* We work with $\psi(y, \chi) = \sum_{n \leq y}\Lambda(n)\chi(n)$ for all characters modulo $M$ at once, and pass to primes at the end. Let $\delta_\chi = 1$ if $\chi = \chi_0$ and $0$ otherwise. The key estimate is a bound for
$$\sum_{\chi \bmod M}\Bigl|\psi(y, \chi) - \delta_\chi y + [\chi = \chi_1]\frac{y^{\beta_1}}{\beta_1}\Bigr|$$
by a constant times $y\,\eta\,(e^{-c\log y/\log M} + e^{-c\sqrt{\log y}})$, where $\eta = 1$ if $e = \varnothing$ and $\eta = \min(1, (1 - \beta_1)\log M)$ otherwise. It is proved in two ranges.

1. *Small modulus*, $\log M \leq c_A\sqrt{\log y}$. Here the classical zero-free region and the truncated explicit formula give the bound with $e^{-c\sqrt{\log y}}$, as in the Background proposition on [the prime number theorem for a character](/learn/analytic-number-theory/#the-explicit-formula).
2. *Large modulus*, $\log M > c_A\sqrt{\log y}$. A smoothed explicit formula expresses $y^{-1}\sum_{n \leq y}\Lambda(n)\chi(n)(y/n - 1)$ as a constant minus $\sum_\rho y^{\rho - 1}/(\rho(\rho - 1))$ over the zeros with $\mathrm{Re}\,\rho > 1 - \kappa$ and $|\mathrm{Im}\,\rho| \leq T + 1$, with an error $C((MT)^Cy^{-\kappa/2} + \log y\log^2(MT)/T)$. Differencing at $y$ and $(1 + \delta)y$ returns to $\psi$ itself. The sum over zeros other than $\beta_1$ is then bounded by $\sum_\chi\sum_\rho y^{\mathrm{Re}\,\rho - 1}$. Split the zeros by real part. The [log zero density bound](/entry/log-density-bound/) counts the zeros with $\mathrm{Re}\,\rho \geq \sigma$, and the [Deuring-Heilbronn theorem](/entry/deuring-heilbronn-lossy/) shows that none of them is closer to $1$ than $\log(c/((1 - \beta_1)\log^3(MT)))/\log(MT)$, up to a constant. With $T$ a power of $M$, the sum is $\ll \eta\,e^{-c\log y/\log M}$ times a power of $\log M$. The condition $\log y \geq C_0\log M\log(\log M + 2)$ makes $e^{-c\log y/\log M}$ smaller than any fixed power of $\log M$, so this power is absorbed.

The two ranges are joined into one bound with the sum $e^{-c_3\log X/\log M} + e^{-\sqrt{c_3\log X}}$. Orthogonality gives
$$\psi(y; M, b) = \frac{1}{\varphi(M)}\sum_\chi\bar\chi(b)\psi(y, \chi),$$
and partial summation passes from $\psi(y; M, b)$ to $\pi(X; M, b)$; the main term $y - \chi_1(b)y^{\beta_1}/\beta_1$ becomes $\mathrm{li}\,X - \chi_1(b)\,\mathrm{li}(X^{\beta_1})$. A lower bound $\mathrm{main}_e(b, X) \gg \eta\,X/(\varphi(M)\log X)$ turns the absolute error into a relative one. $\square$

**Remark 6.2.4 (Formalization).** The theorem is in [PNTFinal.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/PNTFinal.lean#L22), and its proof is one term: `prime_count_of_psi` applied to `glue_ranges`, `psi_relative_near_range` and `psi_relative_far_range`, the last with `explicitS_proof'`, `differenced_explicit_formula` and `zero_sum_bound_lossy`. We have opened the statements of these lemmas, and the proof above follows them; their own proofs are below this chapter. The main term is written with $\mathrm{Re}\,\chi_1(b)$, which equals $\chi_1(b)$ since $\chi_1$ is real. The prime count is the number of primes $p \leq \lfloor X\rfloor$ with $p \bmod M = b \bmod M$. The statement `PNTAPRelW` is defined twice, in [MeanSquareHypWIff.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/MeanSquareHypWIff.lean#L38) and in [PrimePairOfPrimeNumberTheoremInProgressions.lean](lean:Formalism/GL3MeanSquares/PrimePairOfPrimeNumberTheoremInProgressions.lean#L26), with the same text.
