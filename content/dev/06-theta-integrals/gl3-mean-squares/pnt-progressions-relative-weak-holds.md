---
id: pnt-progressions-relative-weak-holds
title: Primes in progressions with a relative error and the exceptional zero
kind: theorem
decl: Formalism.HermitianLattices.Ext.PrimesInProgressions.pnt_progressions_relative_weak_holds
module: Formalism.GL3MeanSquares.GenusMeanAsymptotics.JacobiCharacterSums.PNTFinal
covers: 485
status: drafted
drafted_by: writer@claude
---
This theorem counts the primes in a progression modulo $M$, with $8 \mid M$, with an error that is small relative to the main term. The main term contains the possible exceptional zero. The theorem goes into [`stage`](/entry/stage/), where `count_a` uses it to count primes in the prime sets of the mean square bound. Below it are 485 declarations.

## Statement

Let $\operatorname{li} X = \int_2^X dt/\log t$ and let $\pi(X; M, b)$ count the primes $p \le X$ with $p \equiv b \pmod M$. An *exceptional pair* for $M$ is a real [[Dirichlet character|JR4QSEFXWF]] $\chi_1 \ne 1$ modulo $M$ and a real $\beta_1$ with $L(\beta_1, \chi_1) = 0$ and $1 - 1/(8\log M) < \beta_1 < 1$.

**Theorem.** There are $c_3 > 0$, $A_0$ and $C_0$ with this property. For each $M$ with $8 \mid M$ choose $e$ as follows: an exceptional pair $(\chi_1, \beta_1)$ if one exists, and nothing otherwise. Put $\mathrm{main}(b, X) = \operatorname{li} X/\varphi(M)$ if there is no pair, and

$$\mathrm{main}(b, X) = \frac{\operatorname{li} X - \operatorname{Re}\chi_1(b)\,\operatorname{li}(X^{\beta_1})}{\varphi(M)}$$

otherwise. Then for $X \ge 2$ with $\log X \ge C_0 \log M \log(\log M + 2)$ and $b$ prime to $M$,

$$\bigl|\pi(X; M, b) - \mathrm{main}(b, X)\bigr| \le A_0\Bigl(e^{-c_3 \log X/\log M} + e^{-\sqrt{c_3 \log X}}\Bigr)\,\mathrm{main}(b, X).$$

## Proof

The proof works with $\psi(y, \chi)$ for all $\chi$ modulo $M$, and then passes to primes. Let $\eta = 1$ if there is no pair and $\eta = \min(1, (1 - \beta_1)\log M)$ otherwise. `PsiRel` bounds $\sum_\chi |\psi(y,\chi) - \delta_\chi y + [\chi = \chi_1]\, y^{\beta_1}/\beta_1|$ by $A y \eta (e^{-c\log y/\log M} + e^{-c\sqrt{\log y}})$.

1. **Small modulus** (`psi_relative_near_range`). For $\log M \le c_A \sqrt{\log y}$ the zero-free region gives the bound with $e^{-c\sqrt{\log y}}$.
2. **Large modulus** (`psi_relative_far_range`). For $\log M > c_A\sqrt{\log y}$ it uses a smoothed explicit formula (`smoothed_explicit_formula`), a differencing at $y$ and $(1+\delta)y$ that returns to $\psi$ (`differenced_explicit_formula`), and a bound for $\sum_\chi \sum_\rho y^{\beta - 1}$ over the zeros other than $\beta_1$ (`zero_sum_bound_lossy`). That bound comes from a zero density estimate $N(\sigma, T) \le C (MT)^{A(1-\sigma)}\log^B(MT)$ over all $\chi$ (`log_density_bound`) and a Deuring-Heilbronn repulsion with a loss of $\log^B$ (`deuring_heilbronn_lossy`, proved by a Turán power sum argument).
3. `glue_ranges` joins the two ranges, and `prime_count_of_psi` passes from $\psi$ to $\pi(X; M, b)$, with a lower bound for $\eta$.

These are the tools of the proof of Linnik's theorem (Iwaniec and Kowalski, *Analytic Number Theory*, Chapter 18), here in forms that lose powers of $\log$. The factor $\log(\log M + 2)$ in the range of $X$ leaves room for that loss.

## In the Lean code

The theorem is in [PNTFinal.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/PNTFinal.lean#L22). Its proof is one term that applies the lemmas above. The statement `PNTAPRelW` is in [MeanSquareHypWIff.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/MeanSquareHypWIff.lean#L38). The intermediate statements are in [DeuringHeilbronnM.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/DeuringHeilbronnM.lean#L35) and [PNTDHBSt.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/PNTDHBSt.lean#L11). We have not opened the proofs of the lemmas.

- The three theorems `explicitS_proof'`, `logDensityM_proof'` and `deuringHeilbronnMB_proof'` in the same file only rename `smoothed_explicit_formula`, `Dens.log_density_bound` and `deuring_heilbronn_lossy`.
- The file defines the standard repulsion `DeuringHeilbronnM`, but the proof uses the weaker `DeuringHeilbronnMB`.
- A second, identical definition of `PNTAPRelW` is in [PrimePairOfPrimeNumberTheoremInProgressions.lean](lean:Formalism/GL3MeanSquares/PrimePairOfPrimeNumberTheoremInProgressions.lean#L26), and [PNTBridge.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/JacobiCharacterSums/PNTBridge.lean#L9) transfers the theorem to it.
