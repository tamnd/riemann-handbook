---
id: mahler-section
title: The Mahler measure of a Chow form cut by one linear form
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Short.mahlerSection
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.MahlerSectionStatementHolds
covers: 317
status: drafted
drafted_by: writer@claude
---
This theorem proves `MahlerSection.Statement`: a formula for the Mahler measure of a Chow form after one group of its variables is replaced by a fixed linear form. It is an archimedean input to the heights of cycles in the volume branch, below [the covolume bound](/proof/literature/). Its statement form is `mahler_section_statement_holds`, and the Fubini-Study Chow height formula `Fs.stMain` uses that form.

## Statement

Fix an invertible complex $n \times n$ matrix $h$. It gives a norm $\|u\|_h = |h u|$ on $\mathbb{C}^n$ and a dual norm $\|y\|_h^* = |(h^{T})^{-1} y|$. For a polynomial $f$ in $k$ groups of $n$ variables, let $m_k(f)$ be the mean of $\log |f|$ over the product of $k$ unit spheres of $\|\cdot\|_h$ (`mahler`).

Let $Z = \sum_W Z_W\, W$ be a cycle of homogeneous relevant primes $W$ in $\mathbb{C}[y_1, \dots, y_n]$. Let $f$ be a Chow form of $Z$ in $e + 1$ groups: $f = c \prod_W g_W^{Z_W}$ with $c \neq 0$, where $g_W$ divides exactly the polynomials that vanish on the set of $(e+1)$-tuples of linear forms with a common nonzero zero on $W$. Let $f$ be homogeneous of degree $\delta$ in each group. Let $u \in \mathbb{C}^n$, with the linear form $\ell_u = \sum_j u_j y_j$ in no $W$.

**Theorem.** With $f_u$ the polynomial in $e$ groups got by putting $u$ in the first group,

$$m_e(f_u) = m_{e+1}(f) + \frac{\delta H_{n-1}}{2} + \sum_W Z_W \int_{C_W} \log \frac{|\ell_u(y)|}{\|y\|_h^*}\, d\mu_W(y).$$

Here $H_{n-1} = 1 + \tfrac12 + \dots + \tfrac1{n-1}$, $C_W$ is the cone of $W$ in the unit ball, and $\mu_W$ is the Hausdorff measure of real dimension $2(e+1)$ divided by the volume of the unit ball of $\mathbb{C}^{e+1}$ (`coneIntegral`).

We do not name a source for this formula.

## Proof

Call the *defect* at $u$ the difference $m_e(f_u) - \sum_W Z_W \int_{C_W} \log(|\ell_u|/\|\cdot\|_h^*)\, d\mu_W$.

1. **The defect splits.** `mahlerDefect_eq_sum`: $f_u = c \prod_W (g_W)_u^{Z_W}$, each $(g_W)_u$ is nonzero (`SpecFirstNe`) and multihomogeneous. The Mahler measure of a product, `mahler_measure_of_product`, gives that the defect is $\log|c| + \sum_W Z_W \bigl(m_e((g_W)_u) - \int_{C_W} \log(|\ell_u|/\|\cdot\|_h^*)\, d\mu_W\bigr)$.
2. **The defect is constant.** `defectConstDim`: by `mahler_minus_cone_integral_indep`, each bracket in step 1 is the same for all admissible $u$. So the defect does not depend on $u$.
3. **Average.** `MahlerSectionOfConst`: a constant defect equals its average over the unit ball. The average is $m_{e+1}(f) + \delta H_{n-1}/2$ by `DefectAverage`. The admissible points have full measure in the ball (`AdmissibleAENrm`), and the ball has finite positive volume (`BallVolume`).

## In the Lean code

The theorem is in [MahlerSectionStatementHolds.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/MahlerSectionStatementHolds.lean#L53), and the definitions are in [Statements.lean](lean:GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/Statements.lean#L226) and [StatementsMahler.lean](lean:GroundTheory/HeightsAndTheta/Heights/ArithmeticBezout/StatementsMahler.lean#L42). `mahler_minus_cone_integral_indep` calls `Crofton.defect_eq_of_linForm_notMem`, and `mahler_measure_of_product` calls `Crofton.mahler_C_mul_prod_pow`. We have not opened their proofs or the proof of `DefectAverage`. The library has a second proof, `MahlerSection.proof`, by induction on $e$ through `DefectConstZero` and `DefectConstStep`. This theorem does not use it: it proves the constancy for every $e$ at once. The matrix $h$ is only asked to be invertible, so the "Hermitian norm" is the pullback of the standard one.
