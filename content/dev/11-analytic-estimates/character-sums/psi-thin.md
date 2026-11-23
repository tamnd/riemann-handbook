---
id: psi-thin
title: The prime number theorem for one primitive character, uniform in the conductor
kind: theorem
decl: QH.psi_thin
module: Development.AutomorphicArithmetic.MeanSquareBounds.PsiThin
covers: 343
status: drafted
drafted_by: writer@claude
---
This theorem is the prime number theorem for a primitive [[Dirichlet character|JR4QSEFXWF]] $\chi$, with an error that is explicit in a bound $\lambda$ for $\log N$. It assumes that a real $\chi$ has no zero of $L(s,\chi)$ close to 1. Its only user is [`thin`](/entry/thin/), which integrates the bound. The proof is the classical one from the explicit formula and the zero-free region (Davenport, *Multiplicative Number Theory*, Chapters 14, 19 and 20). Below it are 343 declarations.

## Statement

Let $\psi(\chi, u) = \sum_{n \le u} \Lambda(n)\chi(n)$, with $\Lambda$ the [[von Mangoldt function|087EMZTHWN]]. Put $\psi_0(\chi,u) = \psi(\chi,u) - u$ if $\chi = 1$ and $\psi_0(\chi,u) = \psi(\chi,u)$ otherwise. `NoExc` is as in [`thin`](/entry/thin/).

**Theorem.** For each $c_0 > 0$ there are $C, c > 0$ with this property. Let $\chi$ be a primitive character of modulus $N$, and let $\lambda \ge 1$ with $\log N \le \lambda$. If $\chi$ is real and $\chi \ne 1$, suppose that $L(\beta, \chi) \ne 0$ for real $\beta \in (1 - c_0, 1)$. Then for all $u \ge e$,

$$|\psi_0(\chi, u)| \le C\,u\,(\log u + \lambda)^2 \exp\Bigl(-\frac{c \log u}{\lambda + \sqrt{\log u}}\Bigr).$$

## Proof

1. **Zero-free region** (`pt_zero_free`). The zero-free region `zFRDirichlet` allows at most one zero near 1, and only for a real character. `NoExc` removes it. So each zero $\rho = \beta + i\gamma$ of $L(s,\chi)$ with $0 < \beta < 1$ has $\beta \le 1 - c_1/(\lambda + \log(|\gamma| + 3))$.
2. **Zeros near 0** (`pt_zero_symm`). The functional equation of the completed $L$-function sends a zero $\rho$ of $L(s,\chi)$ to the zero $1 - \rho$ of $L(s,\bar\chi)$. The region of step 1 for $\bar\chi$ gives $\beta \ge (c_1/3)/\lambda$ for $|\gamma| \le 2$.
3. **The sum over zeros** (`pt_zero_sum`). The count of zeros in unit windows, `zerosWindow_closed`, and step 2 give $\sum_{|\gamma| < T} 1/|\rho| \le C_2 (\lambda + \log T)^2$, with multiplicity.
4. **Assembly** (`pt_core`). The truncated explicit formula `explicitFormula_closed` bounds $\psi_0(\chi,u) + \sum_{|\gamma|<T} u^\rho/\rho$. Take $T = \exp(\sqrt{\log u})$. Each term $u^\rho$ has size at most $u \exp(-c_1 \log u/(\lambda + \log(T+3)))$, by step 1. Step 3 bounds the sum.

The final constants are $C = C_7(5 + C_2) + C_2$, with $C_7$ the constant of the explicit formula, and $c = \min(c_1/3, 1)$. The rest is bookkeeping.

## In the Lean code

The theorem is in [PsiThin.lean](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PsiThin.lean#L385). The private lemmas `pt_zero_symm`, `pt_core`, `pt_zero_sum` and `pt_zero_free` are in the same file, at lines [27](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PsiThin.lean#L27), [60](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PsiThin.lean#L60), [184](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PsiThin.lean#L184) and [353](lean:Development/AutomorphicArithmetic/MeanSquareBounds/PsiThin.lean#L353). It also calls:

- `Formalism.ZeroFreeDirichlet.zFRDirichlet`, the zero-free region with at most one exceptional zero;
- `explicitFormula_closed` and `zerosWindow_closed`, the proved forms of `ExplicitFormulaWith` and `ZerosWindowWith` in [ExplicitFormula.lean](lean:Formalism/PeriodIntegrals/ExplicitFormula.lean#L16) and [ZerosWindow.lean](lean:Formalism/PeriodIntegrals/ZerosWindow.lean#L10).

We have not opened the proofs of the explicit formula and of the zero count. The explicit formula in Lean has an extra error term $\sum_{|\gamma|<1} 1/|\rho|$, and step 2 is there to bound it. For a primitive $\chi$, the case $\chi = 1$ means $N = 1$.
